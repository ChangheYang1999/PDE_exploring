"""
ipm2polar.py  --  full-plane polar spectral discretization for IPM Setting II

Problem (PROMPT.md):   (c_l X + U(X) - U(0)) . grad rho = rho,   U = (-psi_y, psi_x),  -Lap psi = d_x rho,
jet  rho = x^2 + O(|X|^3) at the origin, no symmetry imposed anywhere.

Representation.  rho(r,theta) = sum_{m=-M}^{M} rho_m(r) e^{i m theta}, rho_{-m} = conj(rho_m),
rho_m(r) = r^{kappa_m} q_m(xi),  xi = log(1 + r^2/L^2) in [0, xi_max],  xi_max = log(1 + R^2/L^2),
kappa_m = |m| for |m| <= K, otherwise K or K+1 with the parity of m.  q_m is a polynomial of degree N
in xi represented by its values at the Chebyshev-Gauss-Radau nodes (node x=1 <-> xi_max included,
x=-1 <-> r=0 excluded).  A smooth function of xi is an even smooth function of r, so the prefactor
r^{kappa_m} gives every mode the parity in r required for smoothness at the origin.

Velocity law (default: single-subtraction renormalized Biot-Savart, class rho = O(|X|^alpha), alpha<1):
per mode m the radial Poisson ODE  -(psi_m'' + psi_m'/r - m^2 psi_m/r^2) = f_m,  f = d_x rho, with
  m = 0      : regular at 0, psi_0(0) = 0 (irrelevant constant);  no outer condition (local solve)
  |m| = 1    : regular at 0, and no linear term (psi_1 = O(r^3)) : this is the subtraction of U(0)
  |m| >= 2   : regular at 0, Robin condition  psi_m' + (|m|/R) psi_m = R^{|m|-1} I_out,m at r = R,
               I_out,m = int_R^infty s^{1-|m|} f_m(s) ds from a tail model (zero or power law)
Optionally (renorm_modes containing 2) the |m|=2 modes are instead fixed by a gauge value of the r^2
Taylor coefficient (class B), see PROMPT.md section 3.

Products are evaluated pseudo-spectrally in theta on a padded grid (3/2 rule); the radial direction
is collocation (pointwise products).  Everything is float64 / complex128 on the chosen device.
"""
import math
import numpy as np
import torch


# ----------------------------------------------------------------------------------------------
# Lagrange interpolation utilities (barycentric form, arbitrary nodes)
# ----------------------------------------------------------------------------------------------
def bary_weights(x):
    x = np.asarray(x, dtype=np.float64)
    n = len(x)
    logw = np.zeros(n)
    sgn = np.ones(n)
    for j in range(n):
        d = x[j] - np.delete(x, j)
        logw[j] = -np.sum(np.log(np.abs(d)))
        sgn[j] = np.prod(np.sign(d))
    logw -= logw.max()
    return sgn * np.exp(logw)


def diff_matrix(x):
    """Differentiation matrix of the degree-(n-1) interpolant on nodes x."""
    x = np.asarray(x, dtype=np.float64)
    n = len(x)
    w = bary_weights(x)
    D = np.zeros((n, n))
    for j in range(n):
        for k in range(n):
            if j != k:
                D[j, k] = (w[k] / w[j]) / (x[j] - x[k])
        D[j, j] = -np.sum(D[j, :])
    return D


def interp_row(x, x0):
    """Row vector ell with ell @ f = p(x0), p the interpolant of f on nodes x (x0 not a node)."""
    x = np.asarray(x, dtype=np.float64)
    w = bary_weights(x)
    t = w / (x0 - x)
    return t / np.sum(t)


# ----------------------------------------------------------------------------------------------
class Disc:
    def __init__(self, Nr, Ntheta, R, L=1.0, K=2, renorm_modes=(0, 1), tail="zero", tail_alpha=None,
                 gauge2=0.0 + 0.0j, device=None, pad=3, tail_exps=None, smooth=False, prefactor="r"):
        """
        Nr      : number of radial nodes (polynomial degree Nr-1 in xi)
        Ntheta  : number of theta points of the unpadded grid; modes m = 0..M with M = Ntheta//2 - 1
        R       : outer radius of the computational domain
        L       : radial map scale, xi = log(1 + r^2/L^2)
        K       : maximal explicit vanishing order enforced at the origin via the prefactor r^kappa_m
        renorm_modes : set of |m| whose Poisson mode is fixed by a Taylor condition at r=0
                  instead of the outer (decay/Robin) condition.  {0,1} = single subtraction (U(0)).
        tail    : 'zero' (rho = 0 beyond R) or 'power' (rho_m(r) = rho_m(R) (r/R)^tail_alpha beyond R)
        gauge2  : value of the r^2 Taylor coefficient of psi_2 if 2 is in renorm_modes (class B gauge)
        pad     : padding factor for pseudo-spectral products (3 -> Ntheta_pad = 3(M+1))
        """
        self.dev = torch.device(device if device is not None else ("cuda" if torch.cuda.is_available() else "cpu"))
        self.Nr, self.Ntheta, self.R, self.L, self.K = Nr, Ntheta, float(R), float(L), K
        self.M = Ntheta // 2 - 1
        self.renorm_modes = set(renorm_modes)
        self.tail, self.tail_alpha, self.gauge2 = tail, tail_alpha, complex(gauge2)
        self.tail_exps = tail_exps          # explicit (q1, q2) tail exponents; None -> (p, 2p-1), p = tail_alpha or 1/c_l
        self.Np = pad * (self.M + 1)           # padded theta grid size (>= 3M+2 for quadratic products)
        if self.Np % 2:
            self.Np += 1
        # --- radial nodes: Chebyshev-Gauss-Radau on [-1,1] including +1 (xi_max), excluding -1 (r=0)
        N = Nr - 1
        j = np.arange(Nr)
        x = np.cos(2 * np.pi * j / (2 * N + 1))              # x_0 = 1 > x_1 > ... > x_N > -1
        self.x = x
        self.xi_max = math.log(1.0 + self.R ** 2 / self.L ** 2)
        xi = self.xi_max * (1.0 + x) / 2.0
        s = self.L ** 2 * (np.exp(xi) - 1.0)
        r = np.sqrt(s)
        self.xi_np, self.s_np, self.r_np = xi, s, r
        Dx = diff_matrix(x)
        D = Dx * (2.0 / self.xi_max)                         # d/dxi
        self.D_np = D
        ell0 = interp_row(x, -1.0)                           # value at xi = 0 (r=0)
        self.ell0_np = ell0
        self.ell0d_np = ell0 @ D                             # d/dxi at xi = 0
        xi_s = 1.0 / (self.L ** 2 + s)                       # dxi/ds = e^{-xi}/L^2
        self.xi_s_np = xi_s
        # torch copies
        f64 = dict(dtype=torch.float64, device=self.dev)
        self.r = torch.tensor(r, **f64)
        self.s = torch.tensor(s, **f64)
        self.xi = torch.tensor(xi, **f64)
        self.xi_s = torch.tensor(xi_s, **f64)
        self.D = torch.tensor(D, **f64)
        self.ell0 = torch.tensor(ell0, **f64)
        self.ell0d = torch.tensor(self.ell0d_np, **f64)
        self.Dc = self.D.to(torch.complex128)
        self.ell0c = self.ell0.to(torch.complex128)
        self.ell0dc = self.ell0d.to(torch.complex128)
        # theta grids
        self.theta = torch.arange(Ntheta, **f64) * (2 * math.pi / Ntheta)
        self.theta_p = torch.arange(self.Np, **f64) * (2 * math.pi / self.Np)
        self.cos_p, self.sin_p = torch.cos(self.theta_p), torch.sin(self.theta_p)
        # modes
        self.m = torch.arange(self.M + 1, device=self.dev)
        kap = np.array([self._kappa(mm) for mm in range(self.M + 1)])
        self.kappa_np = kap
        self.kappa = torch.tensor(kap, **f64)
        # r^kappa etc. as [M+1, Nr] arrays
        rr = self.r[None, :]
        kk = self.kappa[:, None]
        self.prefactor = prefactor
        self.rk_psi = (rr ** kk).to(torch.complex128)        # r^kappa   (psi side, always)
        self.rkm1_psi = (rr ** (kk - 1)).to(torch.complex128)  # r^(kappa-1)
        if prefactor == "r":
            self.rk = self.rk_psi                            # rho/zeta side prefactor P_m(r) = r^kappa
            self.rkm1 = self.rkm1_psi                        # P_m / r
            self.dpre = (kk * rr ** (kk - 1)).to(torch.complex128)   # dP_m/dr
        elif prefactor == "s":
            ss = rr / torch.sqrt(self.L ** 2 + rr ** 2)      # s = r / sqrt(L^2 + r^2): ~ r/L at 0, -> 1 at infinity
            dss = self.L ** 2 / (self.L ** 2 + rr ** 2) ** 1.5
            self.rk = (ss ** kk).to(torch.complex128)        # P_m = s^kappa (no amplification at large r)
            self.rkm1 = (ss ** kk / rr).to(torch.complex128) # P_m / r
            self.dpre = (kk * ss ** (kk - 1) * dss).to(torch.complex128)   # dP_m/dr
        else:
            raise ValueError(prefactor)
        self.sc = self.s.to(torch.complex128)
        self.xi_sc = self.xi_s.to(torch.complex128)
        self.kappac = self.kappa.to(torch.complex128)
        self.mc = self.m.to(torch.complex128)
        self.k_tail = int(np.argmin(np.abs(r - 0.6 * self.R)))
        # smoothness-constrained representation (see class docstring and the numerical record)
        self.smooth = smooth
        self.J = np.array([(abs(mm) - self._kappa(mm)) // 2 if smooth else 0 for mm in range(self.M + 1)])
        self.nfree = [Nr - int(j) for j in self.J]                 # unknowns per mode
        G = np.ones((self.M + 1, Nr)); Gp = np.zeros((self.M + 1, Nr))
        E = []                                                      # coefficient-to-node matrices [Nr, Nr - J]
        Edxi = []                                                   # coefficient-to-(d/dxi at nodes)
        Epinv = []                                                  # pseudo-inverses of G E (for pack / stable derivative)
        for mm in range(self.M + 1):
            J = int(self.J[mm])
            if J > 0:
                t = xi / self.xi_max
                G[mm] = t ** J
                Gp[mm] = J * t ** (J - 1) / self.xi_max
            # qt_m is a polynomial of degree N - J in x, represented by Chebyshev coefficients (no extrapolation):
            # qt_m(x_j) = sum_k b_k T_k(x_j), k = 0..N-J.  Well conditioned (|T_k| <= 1).
            kk = np.arange(Nr - J)
            thx = np.arccos(np.clip(x, -1.0, 1.0))
            Em = np.cos(np.outer(thx, kk))
            with np.errstate(divide="ignore", invalid="ignore"):
                dEm = np.where(np.sin(thx)[:, None] > 1e-14, kk[None, :] * np.sin(np.outer(thx, kk)) / np.sin(thx)[:, None], kk[None, :] ** 2)
            E.append(Em)
            Edxi.append(dEm * (2.0 / self.xi_max))
            Epinv.append(np.linalg.pinv(G[mm][:, None] * Em))          # fit q = G (E b) directly: b = pinv(G E) q
        self.G = torch.tensor(G, **f64).to(torch.complex128)
        self.Gp = torch.tensor(Gp, **f64).to(torch.complex128)
        self.E = [torch.tensor(Em, **f64).to(torch.complex128) for Em in E]
        self.Edxi = [torch.tensor(Dm, **f64).to(torch.complex128) for Dm in Edxi]
        self.Epinv = [torch.tensor(Pm, **f64).to(torch.complex128) for Pm in Epinv]
        self.offsets = np.concatenate([[0], np.cumsum([self.nfree[0]] + [2 * n for n in self.nfree[1:]])])
        # Poisson inverse per mode (real matrices; applied to complex data)
        self._build_poisson()

    # ------------------------------------------------------------------------------------------
    def _kappa(self, m):
        m = abs(m)
        if m <= self.K:
            return m
        return self.K if (m - self.K) % 2 == 0 else self.K + 1

    def _build_poisson(self):
        """Per mode m: matrix A_m acting on p (psi_m = r^kappa p) with  A_m p = -g_m, g_m = f_m / r^kappa,
        one row replaced by the boundary/renormalization condition.  Also the vector b_m multiplying the
        tail integral I_out (so that rhs = -g_m + b_m * I_out)."""
        Nr, D = self.Nr, self.D_np
        s, xi_s, r = self.s_np, self.xi_s_np, self.r_np
        Ainv = np.zeros((self.M + 1, Nr, Nr))
        bvec = np.zeros((self.M + 1, Nr))
        rowsel = np.zeros(self.M + 1, dtype=int)
        for mm in range(self.M + 1):
            kap = self._kappa(mm)
            # Lap(r^kap p e^{im th}) = r^kap [4 s xi_s^2 (p_xixi - p_xi) + 4(kap+1) xi_s p_xi + (kap^2-m^2) p / s]
            A = (4.0 * (s * xi_s ** 2)[:, None] * (D @ D - D) + 4.0 * (kap + 1) * xi_s[:, None] * D
                 + np.diag((kap ** 2 - mm ** 2) / s))
            b = np.zeros(Nr)
            if mm in self.renorm_modes:
                # Taylor condition at r = 0: p(xi=0) = value; replaces the row of node 0 (xi_max)
                # value: 0 for m=0,1 ; gauge2 handled separately for m=2 (complex) via self.g2rhs
                A[0, :] = self.ell0_np
                rowsel[mm] = 0
            else:
                # Robin at r = R: (kap+|m|) p + 2 S p_xi xi_s(S) = R^{|m|-kap} I_out
                A[0, :] = 2.0 * s[0] * xi_s[0] * D[0, :]
                A[0, 0] += (kap + mm)
                b[0] = r[0] ** (mm - kap)
                rowsel[mm] = 0
            Ainv[mm] = np.linalg.inv(A)
            bvec[mm] = b
        f64 = dict(dtype=torch.float64, device=self.dev)
        self.Ainv = torch.tensor(Ainv, **f64)
        self.Ainvc = self.Ainv.to(torch.complex128)
        self.bvec = torch.tensor(bvec, **f64)
        self.A_cond = np.array([np.linalg.cond(np.linalg.inv(Ainv[mm])) for mm in range(min(self.M + 1, 8))])

    # ------------------------------------------------------------------------------------------
    # modal <-> physical
    # ------------------------------------------------------------------------------------------
    def to_phys(self, cm):
        """cm: complex [M+1, Nr] (mode m>=0 coefficients of a real field, c_{-m} = conj c_m).
        Returns real field on the padded grid [Np, Nr]."""
        Np = self.Np
        full = torch.zeros((Np // 2 + 1, self.Nr), dtype=torch.complex128, device=self.dev)
        full[: self.M + 1] = cm
        # irfft normalization: real f = sum_m c_m e^{im th}; torch.fft.irfft expects half-spectrum of DFT
        return torch.fft.irfft(full, n=Np, dim=0) * Np

    def to_modes(self, f):
        """f: real [Np, Nr] -> complex modes [M+1, Nr] (truncated: dealiasing)."""
        c = torch.fft.rfft(f, dim=0) / self.Np
        return c[: self.M + 1]

    # ------------------------------------------------------------------------------------------
    # fields from q
    # ------------------------------------------------------------------------------------------
    def rho_modes(self, q, constrained=True):
        """q: complex [M+1, Nr] (q_0 must be real).  Returns rho_m, d_r rho_m, (1/r) d_theta rho_m as modes.
        With smooth=True and constrained=True, q holds the full-grid values of G_m * qt_m (as produced by unpack) and
        the derivative uses the product rule with G (exact for the constrained polynomial space).  Derived fields that
        are not in constrained form (e.g. the modes of rho = zeta^2) must be passed with constrained=False."""
        if self.smooth and constrained:
            # division-free: recover the Chebyshev coefficients by the weighted fit b = pinv(G E) q (exact for q in the
            # constrained space, dominated by the outer nodes), then evaluate qt and d qt/dxi from the coefficients
            rows_qt, rows_dqt = [], []
            for mm in range(self.M + 1):
                b = self.Epinv[mm] @ q[mm]
                rows_qt.append(self.E[mm] @ b); rows_dqt.append(self.Edxi[mm] @ b)
            qt = torch.stack(rows_qt, 0); qt_xi = torch.stack(rows_dqt, 0)
            qxi = self.Gp * qt + self.G * qt_xi
        else:
            qxi = q @ self.Dc.T                 # d/dxi
        qs = qxi * self.xi_sc[None, :]          # d/ds   (s = r^2 here)
        rho_m = self.rk * q
        # d/dr (P_m q) = P_m' q + P_m * 2 r q_s ;  with P_m = r^kappa this is r^{kappa-1}(kappa q + 2 r^2 q_s) as before
        drho_m = self.dpre * q + self.rk * (2.0 * torch.sqrt(self.sc)[None, :] * qs)
        tth_m = self.rkm1 * (1j * self.mc[:, None]) * q                                # (1/r) d_theta
        return rho_m, drho_m, tth_m

    def dx_modes(self, drho_m, tth_m):
        """modes of d_x rho = cos th * rho_r - sin th * rho_th / r  (pseudo-spectral, padded)."""
        dr = self.to_phys(drho_m)
        dt = self.to_phys(tth_m)
        f = self.cos_p[:, None] * dr - self.sin_p[:, None] * dt
        return self.to_modes(f)

    def tail_Iout(self, rho_m, cl=None):
        """Tail integrals I_out,m = int_R^inf s^{1-|m|} f_m(s) ds for the Robin conditions of the modes |m| >= 2.
        'zero'  : rho = 0 beyond R.
        'power' : rho_m(r) = rho_m(R) (r/R)^p beyond R, p = tail_alpha or 1/c_l (specification 2, A term only).
        'power2': rho_m(r) = a_m r^p + b_m r^{2p-1} beyond R (specification 2, A and B terms), (a_m, b_m) matched to the
                  computed rho_m at r = R and at the node nearest 0.6 R.
        For rho_{m'}(s) = a s^q:  f_m(s) = (1/2)[(q-m+1) a_{m-1} + (q+m+1) a_{m+1}] s^{q-1}  and
        int_R^inf s^{1-m} s^{q-1} ds = R^{q-m+1} / (m-1-q)   (needs m-1-q > 0)."""
        I = torch.zeros(self.M + 1, dtype=torch.complex128, device=self.dev)
        if self.tail == "zero":
            return I
        if self.tail_exps is not None:
            q1, q2 = float(self.tail_exps[0]), float(self.tail_exps[1])
            p = q1
        else:
            p = float(self.tail_alpha) if self.tail_alpha is not None else 1.0 / cl   # self-consistent exponent
            q1, q2 = p, 2.0 * p - 1.0
        R = self.R
        rhoR = rho_m[:, 0]                                   # node 0 is r = R
        if self.tail == "power":
            terms = [(rhoR / R ** p, p)]
        elif self.tail == "power2A":
            # audited two-term model (specification M14(d)): rho = r^p A + r^{2p-1} B, B = J_p[A]/(c_l - 1),
            # J = (p+1) Psi A' - p Psi' A, Psi'' + (p+1)^2 Psi = (sin th A)' - (p+1) cos th A.  A from rho(R)/R^p after
            # removing the B part once (one fixed-point sweep).  No fitted coefficients.
            cl_ = 1.0 / p
            a = rhoR / R ** p
            for _sweep in range(2):
                b = self._B_from_A(a, p) / (cl_ - 1.0)
                a = (rhoR - b * R ** (2 * p - 1)) / R ** p
            b = self._B_from_A(a, p) / (cl_ - 1.0)
            terms = [(a, p), (b, 2.0 * p - 1.0)]
        elif self.tail == "power2":
            k = self.k_tail
            rk = self.r[k]
            # solve [R^q1 R^q2; rk^q1 rk^q2] (a,b) = (rho(R), rho(rk)) per mode
            det = R ** q1 * rk ** q2 - R ** q2 * rk ** q1
            a = (rhoR * rk ** q2 - rho_m[:, k] * R ** q2) / det
            b = (-rhoR * rk ** q1 + rho_m[:, k] * R ** q1) / det
            terms = [(a, q1), (b, q2)]
        else:
            raise ValueError(self.tail)
        zero = torch.zeros((), dtype=torch.complex128, device=self.dev)
        for coef, q in terms:
            for mm in range(2, self.M + 1):
                lo = coef[mm - 1]
                hi = coef[mm + 1] if mm + 1 <= self.M else zero
                fm = 0.5 * ((q - mm + 1) * lo + (q + mm + 1) * hi)
                den = mm - 1 - q
                if float(den) <= 0:          # outside class S (p >= 1): signal to the solver via NaN
                    return I * float("nan")
                I[mm] = I[mm] + fm * R ** (q - mm + 1) / den
        return I

    def _B_from_A(self, a, p):
        """Modes (m = 0..M) of J_p[A] for A given by its modes a (complex, m >= 0): Psi solves
        Psi'' + (p+1)^2 Psi = (sin th A)' - (p+1) cos th A ; J = (p+1) Psi A' - p Psi' A (products pseudo-spectral)."""
        M = self.M
        # full spectrum m = -M..M
        full = torch.zeros(2 * M + 1, dtype=torch.complex128, device=self.dev)
        full[M:] = a; full[:M] = torch.flip(a[1:], [0]).conj()
        mm = torch.arange(-M, M + 1, device=self.dev).to(torch.float64)
        def shift(v, k):           # modes of e^{i k th} v
            out = torch.zeros_like(v)
            if k > 0: out[k:] = v[:-k]
            elif k < 0: out[:k] = v[-k:]
            else: out = v.clone()
            return out
        sinA = (shift(full, 1) - shift(full, -1)) / (2j)
        cosA = (shift(full, 1) + shift(full, -1)) / 2.0
        rhs = 1j * mm * sinA - (p + 1.0) * cosA
        den = (p + 1.0) ** 2 - mm ** 2
        Psi = rhs / den
        # physical products on the padded grid
        def phys(v):
            c = torch.zeros(self.Np // 2 + 1, dtype=torch.complex128, device=self.dev)
            c[: M + 1] = v[M:]
            return torch.fft.irfft(c, n=self.Np) * self.Np
        A_p = phys(full); Ad_p = phys(1j * mm * full); Psi_p = phys(Psi); Psid_p = phys(1j * mm * Psi)
        J_p = (p + 1.0) * Psi_p * Ad_p - p * Psid_p * A_p
        Jm = torch.fft.rfft(J_p) / self.Np
        return Jm[: M + 1]

    def poisson(self, f_m, rho_m=None, cl=None):
        """Solve the per-mode radial Poisson problems.  f_m: modes of d_x rho [M+1, Nr].
        Returns p_m with psi_m = r^kappa p_m.  Row 0 of each mode system is the condition row:
        Robin modes: rhs = R^{|m|-kappa} I_out,m ; renormalized modes: rhs = prescribed Taylor value."""
        g = f_m / self.rk_psi                                # kappa <= K+1 : safe division (psi side: r^kappa)
        rhs = -g
        bc = torch.zeros(self.M + 1, dtype=torch.complex128, device=self.dev)
        if rho_m is not None and self.tail != "zero":
            bc = bc + self.tail_Iout(rho_m, cl) * self.bvec[:, 0].to(torch.complex128)
        if 2 in self.renorm_modes and self.M >= 2:
            bc = bc.clone()
            bc[2] = self.gauge2
        rhs = torch.cat([bc[:, None], rhs[:, 1:]], dim=1)
        p = torch.einsum("mij,mj->mi", self.Ainvc, rhs)
        return p

    def velocity_modes(self, p):
        """From p (psi_m = r^kappa p_m): modes of U_r = -(1/r) d_theta psi, U_theta = d_r psi,
        and of U_theta / r."""
        pxi = p @ self.Dc.T
        ps = pxi * self.xi_sc[None, :]
        psi_m = self.rk_psi * p
        Ur_m = -(1j * self.mc[:, None]) * self.rkm1_psi * p                             # -(im/r) psi_m
        Ut_m = self.rkm1_psi * (self.kappac[:, None] * p + 2.0 * self.sc[None, :] * ps)  # d_r psi_m
        return psi_m, Ur_m, Ut_m

    # ------------------------------------------------------------------------------------------
    def residual_modes(self, q, cl, return_all=False):
        """Modes of R = (c_l X + V).grad rho - rho  on the collocation grid, V = U - U(0) (the
        renormalized law).  Also returns the elliptic residual check and the Taylor data."""
        rho_m, drho_m, tth_m = self.rho_modes(q)
        f_m = self.dx_modes(drho_m, tth_m)
        p = self.poisson(f_m, rho_m, cl)
        psi_m, Ur_m, Ut_m = self.velocity_modes(p)
        # physical space products (padded grid)
        dr = self.to_phys(drho_m)
        dt = self.to_phys(tth_m)                 # (1/r) d_theta rho
        Ur = self.to_phys(Ur_m)
        Ut = self.to_phys(Ut_m)
        rho = self.to_phys(rho_m)
        adv = Ur * dr + Ut * dt                  # U . grad rho = U_r rho_r + (U_theta / r) rho_theta
        Rphys = cl * self.r[None, :] * dr + adv - rho
        R_m = self.to_modes(Rphys)
        if not return_all:
            return R_m
        return dict(R_m=R_m, Rphys=Rphys, rho=rho, rho_m=rho_m, f_m=f_m, p=p, psi_m=psi_m,
                    Ur=Ur, Ut=Ut, dr=dr, dt=dt)

    def zeta_residual_modes(self, qz, cl, return_all=False):
        """Signed square root formulation (specification 4.5): zeta with rho = zeta^2, residual
        Rz = (c_l X + V[zeta^2]).grad zeta - zeta/2 (modes on the grid)."""
        z_m, dz_m, tz_m = self.rho_modes(qz)             # zeta modes and derivatives (same representation)
        z = self.to_phys(z_m)
        dz = self.to_phys(dz_m)
        tz = self.to_phys(tz_m)
        rho = z * z
        rho_m = self.to_modes(rho)
        q_rho = rho_m / self.rk
        rho_m2, drho_m, tth_m = self.rho_modes(q_rho, constrained=False)    # re-expanded rho (truncated to M modes)
        f_m = self.dx_modes(drho_m, tth_m)
        p = self.poisson(f_m, rho_m2, cl)
        psi_m, Ur_m, Ut_m = self.velocity_modes(p)
        Ur = self.to_phys(Ur_m)
        Ut = self.to_phys(Ut_m)
        Rz = cl * self.r[None, :] * dz + Ur * dz + Ut * tz - 0.5 * z
        Rz_m = self.to_modes(Rz)
        if not return_all:
            return Rz_m
        # also the rho-residual R = V.grad rho - rho = 2 zeta Rz (exact identity) and its modes
        dr = self.to_phys(drho_m)
        dt = self.to_phys(tth_m)
        rho_rep = self.to_phys(rho_m2)
        Rphys = cl * self.r[None, :] * dr + Ur * dr + Ut * dt - rho_rep
        return dict(Rz_m=Rz_m, Rz=Rz, zeta=z, rho=rho_rep, rho_m=rho_m2, q_rho=q_rho, f_m=f_m, p=p,
                    psi_m=psi_m, Ur=Ur, Ut=Ut, Rphys=Rphys, R_m=self.to_modes(Rphys), dr=dr, dt=dt, dz=dz, tz=tz)

    def residual_vec_zeta(self, v, jet_weight=1.0, res_weight=None, jet_mode="fixed", compat_weight=0.0, cl_fixed=None, f0=None):
        """Real residual vector for the zeta formulation: transport modes (weighted) + jet rows
        zeta(0)=0, zeta_x(0)=1 [, zeta_y(0)=0 if jet_mode == 'fixed'] [+ explicit compatibility row
        compat_weight * (c_l - 1/2 - psi_xy(0)) if compat_weight > 0 (referee protocol item 2)]."""
        qz, cl = self.unpack(v)
        lam_h = None
        if cl_fixed is not None:                # continuation in c_l: last slot of v is the forcing amplitude lambda
            lam_h = cl
            cl = torch.as_tensor(cl_fixed, dtype=torch.float64, device=self.dev)
        if compat_weight > 0.0:
            out = self.zeta_residual_modes(qz, cl, return_all=True)
            Rz_m = out["Rz_m"]
            U0, pxx, pxy, pyy = self.taylor_psi(out["p"])
        else:
            Rz_m = self.zeta_residual_modes(qz, cl)
        if lam_h is not None and f0 is not None:
            Rz_m = Rz_m - lam_h * f0            # f0: fixed forcing as (unweighted) residual modes
        if res_weight is not None:
            Rz_m = Rz_m * res_weight[None, :]
        parts = [Rz_m[0].real, Rz_m[1:].real.reshape(-1), Rz_m[1:].imag.reshape(-1)]
        z0, zx, zy, _, _, _ = self.taylor_rho(qz)
        if jet_mode == "fixed":
            jet = torch.stack([z0, zx - 1.0, zy]) * jet_weight
        elif jet_mode == "rotating":
            jet = torch.stack([z0, zx - 1.0]) * jet_weight
        else:
            raise ValueError(jet_mode)
        if compat_weight > 0.0:
            comp = (cl - 0.5 - (pxy if jet_mode == "fixed" else torch.sqrt(pxy ** 2 + pyy ** 2)))[None] * compat_weight
            return torch.cat(parts + [jet, comp])
        return torch.cat(parts + [jet])

    # ------------------------------------------------------------------------------------------
    # Taylor data at the origin
    # ------------------------------------------------------------------------------------------
    def taylor_rho(self, q):
        """Returns rho(0), grad rho(0) = (rho_x, rho_y), Hessian entries (rho_xx, rho_xy, rho_yy)
        from the modal representation (exact for the interpolant)."""
        q0 = (q[0] @ self.ell0c).real          # rho_0(0)
        q0xi = (q[0] @ self.ell0dc).real       # d rho_0 / dxi (0)
        q0s = q0xi / self.L ** 2                                   # d rho_0 / ds (0)  -> rho_0 = q0 + q0s r^2 + ...
        q1 = q[1] @ self.ell0c                 # rho_1 = r q1(0) + ...   (kappa_1 = 1)
        q2 = q[2] @ self.ell0c                 # rho_2 = r^2 q2(0) + ...  (kappa_2 = 2)
        if self.prefactor == "s":              # s^kappa = (r/L)^kappa (1 + O(r^2)): leading coefficients scale by L^-kappa
            q1 = q1 / self.L; q2 = q2 / self.L ** 2
        # rho ~ q0 + 2 Re[q1 (x+iy)] + q0s (x^2+y^2) + 2 Re[q2 (x+iy)^2]
        rho0 = q0
        rx, ry = 2 * q1.real, -2 * q1.imag
        rxx = 2 * q0s + 4 * q2.real
        ryy = 2 * q0s - 4 * q2.real
        rxy = -4 * q2.imag
        return rho0, rx, ry, rxx, rxy, ryy

    def taylor_psi(self, p):
        """psi(0)-independent data: grad psi(0) -> U(0) = (-psi_y, psi_x); Hessian of psi at 0."""
        p0xi = (p[0] @ self.ell0dc).real
        p0s = p0xi / self.L ** 2
        p1 = p[1] @ self.ell0c
        p2 = p[2] @ self.ell0c
        psix, psiy = 2 * p1.real, -2 * p1.imag
        pxx = 2 * p0s + 4 * p2.real
        pyy = 2 * p0s - 4 * p2.real
        pxy = -4 * p2.imag
        U0 = (-psiy, psix)
        return U0, pxx, pxy, pyy

    # ------------------------------------------------------------------------------------------
    # packing of unknowns
    # ------------------------------------------------------------------------------------------
    def pack(self, q, cl):
        """q: full-grid modal values [M+1, Nr].  With smooth=True the free unknowns are qt_m at the outer nodes
        (q_m = G_m * qt_m); the innermost J_m values are slaved."""
        if not self.smooth:
            v = [q[0].real.reshape(-1), q[1:].real.reshape(-1), q[1:].imag.reshape(-1),
                 torch.tensor([cl], dtype=torch.float64, device=self.dev)]
            return torch.cat(v)
        parts = []
        for mm in range(self.M + 1):
            b = self.Epinv[mm] @ q[mm]                               # Chebyshev coefficients of qt (q = G E b)
            if mm == 0:
                parts.append(b.real)
            else:
                parts.append(b.real); parts.append(b.imag)
        parts.append(torch.as_tensor([float(cl)], dtype=torch.float64, device=self.dev))
        return torch.cat(parts)

    def unpack(self, v):
        Nr, M = self.Nr, self.M
        if not self.smooth:
            q0 = v[:Nr]
            re = v[Nr: Nr + M * Nr].reshape(M, Nr)
            im = v[Nr + M * Nr: Nr + 2 * M * Nr].reshape(M, Nr)
            q = torch.cat([q0[None, :].to(torch.complex128), torch.complex(re, im)], dim=0)
            cl = v[-1]
            return q, cl
        rows = []
        for mm in range(self.M + 1):
            n = self.nfree[mm]; o = int(self.offsets[mm])
            if mm == 0:
                qt = v[o: o + n].to(torch.complex128)
            else:
                qt = torch.complex(v[o: o + n], v[o + n: o + 2 * n])
            full = self.E[mm] @ qt                                   # coefficients -> values at all nodes
            rows.append(self.G[mm] * full)
        q = torch.stack(rows, dim=0)
        return q, v[-1]

    def nunk(self):
        if not self.smooth:
            return self.Nr + 2 * self.M * self.Nr + 1
        return int(self.offsets[-1]) + 1

    def residual_vec(self, v, jet_weight=1.0, res_weight=None, jet_mode="fixed"):
        """Full real residual vector: transport residual modes (real/imag) at all nodes + jet conditions.
        jet_mode 'fixed'   : rho(0)=0, grad rho(0)=0, D^2 rho(0) = diag(2,0)            (6 conditions)
        jet_mode 'rotating': rho(0)=0, grad rho(0)=0, D^2 rho(0) rank one with trace 2  (5 conditions:
                             rxx+ryy-2 = 0 and rxx*ryy - rxy^2 = 0); the orientation is free and reported."""
        q, cl = self.unpack(v)
        R_m = self.residual_modes(q, cl)
        if res_weight is not None:
            R_m = R_m * res_weight[None, :]
        parts = [R_m[0].real, R_m[1:].real.reshape(-1), R_m[1:].imag.reshape(-1)]
        rho0, rx, ry, rxx, rxy, ryy = self.taylor_rho(q)
        if jet_mode == "fixed":
            jet = torch.stack([rho0, rx, ry, rxx - 2.0, rxy, ryy]) * jet_weight
        elif jet_mode == "rotating":
            jet = torch.stack([rho0, rx, ry, rxx + ryy - 2.0, rxx * ryy - rxy ** 2]) * jet_weight
        else:
            raise ValueError(jet_mode)
        return torch.cat(parts + [jet])

    # ------------------------------------------------------------------------------------------
    # Cartesian evaluation of the interpolant (for verification / output)
    # ------------------------------------------------------------------------------------------
    def eval_modes_at(self, cm, kappa, r_eval, theta_eval):
        """Evaluate sum_m r^kappa_m q_m(xi(r)) e^{i m theta} at arbitrary points (numpy, slow but exact)."""
        cm = cm.detach().cpu().numpy()
        r_eval = np.asarray(r_eval, dtype=np.float64)
        xi_e = np.log(1.0 + r_eval ** 2 / self.L ** 2)
        x_e = 2.0 * xi_e / self.xi_max - 1.0
        # interpolation matrix from nodes to x_e
        w = bary_weights(self.x)
        Pm = np.zeros((len(x_e), self.Nr))
        for i, xe in enumerate(x_e):
            d = xe - self.x
            if np.any(np.abs(d) < 1e-14):
                Pm[i, np.argmin(np.abs(d))] = 1.0
            else:
                t = w / d
                Pm[i] = t / t.sum()
        out = np.zeros(len(r_eval))
        for mm in range(self.M + 1):
            qm = Pm @ cm[mm]
            val = (r_eval ** kappa[mm]) * qm * np.exp(1j * mm * theta_eval)
            out += val.real if mm == 0 else 2.0 * val.real
        return out

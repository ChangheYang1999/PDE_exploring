#!/usr/bin/env python
"""SPEC v1.19 3.6 (l), test-only double-double tables (numerics, 2026-10-29; v2 09:5xZ after V230: exact binary64 import and split): the parameter-dependent radial basis derivative matrices B[l] and the
twist tables of src/bases/radial.py evaluated in 34-digit mpmath arithmetic on the radial nodes and rounded ONCE to double-double (hi, lo) pairs.
Same formulas as RadialBasis.matrices / twist_tables (jets of order K in rho = r^2): B[l, n, j, k] = d^n/drho^n [ (s/R0)^-(p_l) damp(rho) Phi_k(x) ],
s = sqrt(rho + R0^2), x = 1 - 2 R0/(s + R0), Phi_k = T_k(2x - 1), p_l = alpha + l - shift or power(l); damp = (rho/(rho + R1^2))^core_damp;
C[m, n, j] = d^n/drho^n cos(m beta), S likewise, beta = omega/(2 c_l) log(1 + rho/R0^2). Inputs c_l, omega, R0, R1 and the nodes rho are the
float64 values (exact inputs). Not used by production; gates.py and src/ are untouched."""
import math
import mpmath as mp
import torch

mp.mp.dps = 34
DT = torch.float64


def _mpf(x):
    """Exact import of the binary64 value x (mp.mpf(float) converts the binary value exactly; V230: repr() would import a decimal approximation)."""
    return mp.mpf(float(x))


def jmul(a, b):
    K = len(a) - 1
    return [sum((a[k] * b[n - k] for k in range(n + 1)), mp.mpf(0)) for n in range(K + 1)]


def jrecip(a):
    K = len(a) - 1
    inv0 = 1 / a[0]; out = [inv0]
    for n in range(1, K + 1):
        out.append(-inv0 * sum((a[k] * out[n - k] for k in range(1, n + 1)), mp.mpf(0)))
    return out


def jaffine_pow(u, p, K):
    """Jet of u^p, u affine in rho with slope 1 (u a scalar mpf at the node): coefficients C(p, n) u^(p - n)."""
    out = []; c = mp.mpf(1)
    for n in range(K + 1):
        if n > 0:
            c = c * (p - (n - 1)) / n
        out.append(c * mp.power(u, p - n))
    return out


def jaffine_log(u, K):
    out = [mp.log(u)]
    for n in range(1, K + 1):
        out.append(((-1) ** (n - 1)) / mp.mpf(n) * mp.power(u, -n))
    return out


def jcos_sin(u):
    K = len(u) - 1
    c = [mp.cos(u[0])]; s = [mp.sin(u[0])]
    for n in range(1, K + 1):
        accc = sum((k * u[k] * s[n - k] for k in range(1, n + 1)), mp.mpf(0)); accs = sum((k * u[k] * c[n - k] for k in range(1, n + 1)), mp.mpf(0))
        c.append(-accc / n); s.append(accs / n)
    return c, s


def jconst(c, K):
    return [mp.mpf(c)] + [mp.mpf(0)] * K


def jscale(a, c):
    return [x * c for x in a]


def jadd(a, b):
    return [x + y for x, y in zip(a, b)]


def jchebyshev_shifted(x, Nk):
    K = len(x) - 1
    two_x_m1 = jadd(jscale(x, 2), jconst(-1, K))
    T = [jconst(1, K), two_x_m1]
    for k in range(2, Nk):
        T.append(jadd(jscale(jmul(two_x_m1, T[-1]), 2), jscale(T[-2], -1)))
    return T[:Nk]


def to_dd(x):
    """mpf -> (hi, lo) float64 pair with hi + lo = x to about 1e-32 relative (hi = round(x); lo = round(x - hi) with hi imported exactly; V230)."""
    hi = float(x); lo = float(x - mp.mpf(hi))
    return hi, lo


def matrices_dd(rho, alpha, R0, Lmax, K, shift=0.0, power=None, core_damp=0, R1=None, Nk=16, lmask=None):
    """Double-double B[l, n, j, k] (two float64 tensors hi, lo of shape (Lmax+1, K+1, Nr, Nk)). alpha may be an mpf (double-double value) or float;
    power(l) may return an mpf or float; mirrors RadialBasis.matrices (jets module) with the n! conversion of to_derivs."""
    rho_f = [float(v) for v in torch.as_tensor(rho).reshape(-1).tolist()]
    R0m = _mpf(R0); alpha_m = alpha if isinstance(alpha, mp.mpf) else _mpf(alpha)
    R1m = R0m if R1 is None else _mpf(R1)
    Nr = len(rho_f)
    hi = torch.zeros(Lmax + 1, K + 1, Nr, Nk, dtype=DT); lo = torch.zeros_like(hi)
    fact = [mp.factorial(n) for n in range(K + 1)]
    for j, rj in enumerate(rho_f):
        rho_m = _mpf(rj); u = rho_m + R0m * R0m
        s = jaffine_pow(u, mp.mpf("0.5"), K)
        sp = jadd(s, jconst(R0m, K))
        x = jadd(jconst(1, K), jscale(jrecip(sp), -2 * R0m))
        Phi = jchebyshev_shifted(x, Nk)
        damp = None
        if core_damp and core_damp > 0:
            u1 = rho_m + R1m * R1m
            frac = jadd(jconst(1, K), jscale(jaffine_pow(u1, mp.mpf(-1), K), -(R1m * R1m)))
            damp = frac
            for _ in range(int(core_damp) - 1):
                damp = jmul(damp, frac)
        for l in range(Lmax + 1):
            if power is None:
                p = -(alpha_m + l - _mpf(shift)) / 2
            else:
                pw = power(l); p = -(pw if isinstance(pw, mp.mpf) else _mpf(float(pw))) / 2
            env = jscale(jaffine_pow(u, p, K), mp.power(R0m, -(2 * p)))
            if damp is not None:
                env = jmul(env, damp)
            if lmask is not None and l in lmask:
                continue
            for k in range(Nk):
                prod = jmul(env, Phi[k])
                for n in range(K + 1):
                    h_, l_ = to_dd(prod[n] * fact[n]); hi[l, n, j, k] = h_; lo[l, n, j, k] = l_
    return hi, lo


def twist_tables_dd(rho, omega, c_l, R0, Mmax, K):
    """Double-double C[m, n, j], S[m, n, j] (hi, lo tensors of shape (Mmax+1, K+1, Nr)); omega, c_l float64 exact inputs; the value log(1 + rho/R0^2)
    as in the production code (log1p; identical in exact arithmetic), derivatives from the jet of log(rho + R0^2)."""
    rho_f = [float(v) for v in torch.as_tensor(rho).reshape(-1).tolist()]
    R0m = _mpf(R0); om = _mpf(omega); cl = _mpf(c_l); Nr = len(rho_f)
    Ch = torch.zeros(Mmax + 1, K + 1, Nr, dtype=DT); Cl = torch.zeros_like(Ch); Sh = torch.zeros_like(Ch); Sl = torch.zeros_like(Ch)
    fact = [mp.factorial(n) for n in range(K + 1)]
    for j, rj in enumerate(rho_f):
        rho_m = _mpf(rj); u = rho_m + R0m * R0m
        lg = jaffine_log(u, K); lg[0] = mp.log(1 + rho_m / (R0m * R0m))
        beta = jscale(lg, om / (2 * cl))
        for m in range(Mmax + 1):
            c, s_ = jcos_sin(jscale(beta, m))
            for n in range(K + 1):
                h_, l_ = to_dd(c[n] * fact[n]); Ch[m, n, j] = h_; Cl[m, n, j] = l_
                h_, l_ = to_dd(s_[n] * fact[n]); Sh[m, n, j] = h_; Sl[m, n, j] = l_
    return (Ch, Cl), (Sh, Sl)


def alpha_dd(c_l):
    """alpha = (1 - c_l)/c_l as an mpf from the exact float64 c_l."""
    cl = _mpf(c_l); return (1 - cl) / cl


if __name__ == "__main__":
    # self-test against the float64 production tables on the production node set of a small basis
    import sys, os, time
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from src.bases.radial import RadialBasis
    from src.bases import radial as radmod
    torch.set_default_dtype(DT)
    t0 = time.time()
    rb = RadialBasis(16)
    rho = torch.tensor([1e-6, 0.01, 0.09, 0.5, 2.0, 50.0, 4096.0 ** 2], dtype=DT)
    c_l = 0.42; alpha = (1.0 - c_l) / c_l; R0 = 0.3; K = 4; Lmax = 6
    B = rb.matrices(rho, alpha, R0, Lmax, K, shift=0.0)
    Bh, Bl = matrices_dd(rho, alpha_dd(c_l), R0, Lmax, K, shift=0.0, Nk=16)
    rel = ((B - Bh).abs() / (B.abs() + 1e-300)); scale = B.abs().amax(dim=-1, keepdim=True)
    print("B[l] float64 vs dd(hi): max relative-to-row-scale deviation", float(((B - Bh).abs() / (scale + 1e-300)).max()), "max |lo/hi|", float((Bl.abs() / (Bh.abs() + 1e-300)).max()))
    BB = rb.matrices(rho, alpha, R0, Lmax, K, power=lambda l: 2 * alpha + 1 + l, core_damp=2, R1=0.3, Nk=8)
    BBh, BBl = matrices_dd(rho, alpha_dd(c_l), R0, Lmax, K, power=lambda l: 2 * alpha_dd(c_l) + 1 + l, core_damp=2, R1=0.3, Nk=8)
    sc = BB.abs().amax(dim=-1, keepdim=True); print("B channel (power, core_damp 2): max deviation / row scale", float(((BB - BBh).abs() / (sc + 1e-300)).max()))
    C, S = rb.twist_tables(rho, 0.3, c_l, R0, 6, K)
    (Ch, Cl), (Sh, Sl) = twist_tables_dd(rho, 0.3, c_l, R0, 6, K)
    print("twist C, S float64 vs dd(hi): max abs deviation", float((C - Ch).abs().max()), float((S - Sh).abs().max()), "max |lo|", float(Cl.abs().max()))
    # V230 controls: exact import and split
    for xv in (mp.mpf(1) / 10, mp.mpf(2) / 3, mp.sqrt(mp.mpf(2)), mp.mpf("1e-200") / 3, -mp.pi * 1e10):   # (pairs lose precision only when lo is subnormal, below about 1e-292; the tables stay far above)
        h_, l_ = to_dd(xv); err = abs((mp.mpf(h_) + mp.mpf(l_) - xv) / xv)
        assert err < mp.mpf("1e-31"), (xv, h_, l_, err)
    assert _mpf(0.1) == mp.mpf(0.1) and _mpf(0.1) != mp.mpf("0.1")
    print("V230 controls: to_dd relative error < 1e-31 on five values; _mpf imports the exact binary64 value")
    print(f"self-test done in {time.time() - t0:.1f} s (7 nodes)")


# ---------------------------------------------------------------- tail reduction (TailConstraints.expand) in double-double (screen: tail-reduction solutions -> double-double)
def expand_dd(tc, z_red):
    """Double-double version of TailConstraints.expand for nu = 0: the dependent coefficients (top two of each A/C column from the 4x4 pair and 2x2
    single systems with p = (a_env + l)/2, q = m kappa/2; the top one of each B/D column from the k^2 moment) are solved in 34-digit mpmath from the
    exact binary64 free coefficients and parameters and rounded once to (hi, lo); the free coefficients and the parameters are exact (lo = 0).
    Returns (z_full_hi, z_full_lo) in the layout of model.pack. Mirrors expand step by step (same k2, k4 vectors, same ordering)."""
    import torch
    from src.equations.fields import alpha_of
    model = tc.model; Nq = model.Nq
    assert tc.nu <= 0, "expand_dd mirrors the nu = 0 constraints only"
    dev = z_red.device
    off = 0; red = {}
    for name in ("A", "C", "B", "D", "E"):
        n = tc.red_sizes[name]; nc = tc.ncols[name]
        a = z_red[off: off + n * nc].reshape(n, nc) if n > 0 else torch.zeros(0, nc, dtype=DT, device=dev); off += n * nc
        if nc != Nq:
            a = torch.zeros(n, Nq, dtype=DT, device=dev).index_copy(1, tc.cols[name], a)
        red[name] = a
    c_l = float(z_red[-2]); omega = float(z_red[-1])
    clm = _mpf(c_l); om = _mpf(omega); alpha = (1 - clm) / clm; kappa = om / clm
    Nk = tc.Nk; k2 = [mp.mpf(k) ** 2 for k in range(Nk)]; k4 = [(mp.mpf(8) / 3) * k2[k] * (k2[k] - 1) for k in range(Nk)]   # the production vectors: k2 = k^2, k4 = (8/3) k^2 (k^2 - 1)
    assert torch.allclose(tc.k2.cpu(), torch.tensor([float(v) for v in k2])) and torch.allclose(tc.k4.cpu(), torch.tensor([float(v) for v in k4]))
    def col_mpf(t):
        return [_mpf(v) for v in t.detach().cpu().tolist()]
    def solve_pair(fa, fb, p, q):
        # unknowns (a_{N-2}, a_{N-1}, b_{N-2}, b_{N-1}); rows: k2.a = 0; k2.b = 0; (k4 - p).a + q 1.b = 0; -q 1.a + (k4 - p).b = 0
        ra = [k2, [mp.mpf(0)] * Nk, [k4[k] - p for k in range(Nk)], [-q] * Nk]
        rb = [[mp.mpf(0)] * Nk, k2, [q] * Nk, [k4[k] - p for k in range(Nk)]]
        M = mp.matrix(4, 4); rhs = mp.matrix(4, 1)
        for i in range(4):
            M[i, 0] = ra[i][Nk - 2]; M[i, 1] = ra[i][Nk - 1]; M[i, 2] = rb[i][Nk - 2]; M[i, 3] = rb[i][Nk - 1]
            rhs[i] = -(sum((ra[i][k] * fa[k] for k in range(Nk - 2)), mp.mpf(0)) + sum((rb[i][k] * fb[k] for k in range(Nk - 2)), mp.mpf(0)))
        u = mp.lu_solve(M, rhs)
        return fa + [u[0], u[1]], fb + [u[2], u[3]]
    def solve_single(fa, p):
        ra = [k2, [k4[k] - p for k in range(Nk)]]
        M = mp.matrix(2, 2); rhs = mp.matrix(2, 1)
        for i in range(2):
            M[i, 0] = ra[i][Nk - 2]; M[i, 1] = ra[i][Nk - 1]; rhs[i] = -sum((ra[i][k] * fa[k] for k in range(Nk - 2)), mp.mpf(0))
        u = mp.lu_solve(M, rhs)
        return fa + [u[0], u[1]]
    full_h = {}; full_l = {}
    for name, a_env in (("A", alpha), ("C", alpha - 1)):
        cols = [None] * Nq
        for (qc, qs, m, l) in tc.pairs:
            p = (a_env + l) / 2; q = m * kappa / 2
            a, b = solve_pair(col_mpf(red[name][:, qc]), col_mpf(red[name][:, qs]), p, q)
            cols[qc] = a; cols[qs] = b
        for (q0, l) in tc.singles:
            p = (a_env + l) / 2
            cols[q0] = solve_single(col_mpf(red[name][:, q0]), p)
        H = torch.zeros(Nk, Nq, dtype=DT); L = torch.zeros(Nk, Nq, dtype=DT)
        for qq in range(Nq):
            for k in range(Nk):
                h_, l_ = to_dd(cols[qq][k]); H[k, qq] = h_; L[k, qq] = l_
        full_h[name] = H.to(dev); full_l[name] = L.to(dev)
    extra_h = {}; extra_l = {}
    for name in ("B", "D"):
        n = dict(model.layout)[name]
        if n > 0:
            H = torch.zeros(n, Nq, dtype=DT); L = torch.zeros(n, Nq, dtype=DT)
            for qq in range(Nq):
                free = col_mpf(red[name][:, qq])
                if n == 1:
                    vals = free if len(free) == 1 else [mp.mpf(0)]
                else:
                    k2n = [mp.mpf(k) ** 2 for k in range(n)]
                    top = -sum((k2n[k] * free[k] for k in range(n - 1)), mp.mpf(0)) / k2n[n - 1]
                    vals = free + [top]
                for k in range(n):
                    h_, l_ = to_dd(vals[k]); H[k, qq] = h_; L[k, qq] = l_
            extra_h[name] = H.to(dev); extra_l[name] = L.to(dev)
    if tc.red_sizes["E"] > 0:
        extra_h["E"] = red["E"]; extra_l["E"] = torch.zeros_like(red["E"])
    zh = model.pack(full_h["A"], full_h["C"], torch.tensor(c_l, dtype=DT, device=dev), torch.tensor(omega, dtype=DT, device=dev), extra=extra_h)
    zl = model.pack(full_l["A"], full_l["C"], torch.tensor(0.0, dtype=DT, device=dev), torch.tensor(0.0, dtype=DT, device=dev), extra=extra_l)
    return zh, zl


# ---------------------------------------------------------------- stable linear operator (src/equations/linear_stable.linear_velocity): radial arrays in double-double
def linear_radial_dd(model, dh, dl, c_l, omega, K=2):
    """The radial derivative arrays allT, allS (K+1, Nr, Nq) of linear_velocity BEFORE the twist, in 34-digit mpmath from the exact binary64 nodes,
    parameters and the (hi, lo) coefficients dh, dl (dicts as model.unpack_all), rounded once to (hi, lo); returns dict with per-channel
    'transformed' arrays {name: (hi, lo)} and the channel kinds, so that the caller applies the production twist (in double-double) and sums.
    Mirrors linear_velocity step by step: ss = u^(1/2) (order K+1), xx = 1 - 2 R0/(ss + R0), rr = (rho, 1, 0), invu = u^-1; Phi Chebyshev jets of xx;
    poly = sum_k Phi_k coeff_k; core damping for B, D, E; env = u^(-nu/2) R0^nu; P = poly[:K+1], P' = (n+1) poly[n+1];
    radial = delta P + c nu R0^2 invu P + 2 c rr P'; rot = -w R0^2 invu dphi (E: -w dphi) with dphi = tw_sign m P[partner]; transformed = n! env (radial + rot)."""
    import torch
    rho_f = [float(v) for v in model.rho.detach().cpu().tolist()]; Nr = len(rho_f); Nq = model.Nq
    ell = [int(v) for v in model.l_arr.detach().cpu().tolist()]
    R0m = _mpf(float(model.R0)); clm = _mpf(c_l); om = _mpf(omega); alpha = (1 - clm) / clm
    partner = [int(v) for v in model.partner.detach().cpu().tolist()]; tw_sign = [_mpf(v) for v in model.tw_sign.detach().cpu().tolist()]; m_arr = [_mpf(v) for v in model.m_arr.detach().cpu().tolist()]
    fact = [mp.factorial(n) for n in range(K + 1)]
    out = {}
    for name, kind in (("A", "T"), ("C", "S"), ("B", "T"), ("D", "S"), ("E", "S")):
        if name not in dh or dh[name].numel() == 0:
            continue
        ch_h = dh[name].detach().cpu(); ch_l = (dl[name].detach().cpu() if (dl is not None and name in dl and dl[name].numel() > 0) else torch.zeros_like(ch_h))
        nk = ch_h.shape[0]
        coeff = [[_mpf(ch_h[k, q]) + _mpf(ch_l[k, q]) for q in range(Nq)] for k in range(nk)]
        if name == "E":
            coeff = [[(coeff[k][q] if ell[q] >= 2 else mp.mpf(0)) for q in range(Nq)] for k in range(nk)]
        Th = torch.zeros(K + 1, Nr, Nq, dtype=DT); Tl = torch.zeros_like(Th)
        damp_on = name in ("B", "D", "E") and model.channels["core_damp"]
        R1m = _mpf(model.channels.get("R1") if model.channels.get("R1") is not None else float(model.R0))
        for j, rj in enumerate(rho_f):
            rho_m = _mpf(rj); u = rho_m + R0m * R0m
            ss = jaffine_pow(u, mp.mpf("0.5"), K + 1)
            xx = jadd(jconst(1, K + 1), jscale(jrecip(jadd(ss, jconst(R0m, K + 1))), -2 * R0m))
            rr = [rho_m, mp.mpf(1)] + [mp.mpf(0)] * (K - 1)
            invu = jaffine_pow(u, mp.mpf(-1), K)
            Phi = jchebyshev_shifted(xx, nk)                                   # jets of order K+1
            damp = None
            if damp_on:
                frac = jadd(jconst(1, K + 1), jscale(jaffine_pow(rho_m + R1m * R1m, mp.mpf(-1), K + 1), -(R1m * R1m)))
                damp = jconst(1, K + 1)
                for _ in range(int(model.channels["core_damp"])):
                    damp = jmul(damp, frac)
            for q in range(Nq):
                poly = [sum((Phi[k][n] * coeff[k][q] for k in range(nk)), mp.mpf(0)) for n in range(K + 2)]
                if damp is not None:
                    poly = jmul(poly, damp)
                l_ = ell[q]
                if name == "A":
                    nu = alpha + l_; delta = mp.mpf(0)
                elif name == "C":
                    nu = alpha + l_ - 1; delta = mp.mpf(0)
                elif name == "B":
                    nu = 2 * alpha + 1 + l_; delta = mp.mpf(-1)
                elif name == "D":
                    nu = 2 * alpha + l_; delta = mp.mpf(-1)
                else:
                    nu = mp.mpf(2 * l_ + 1); delta = 1 - clm * (l_ + 3)
                env = jscale(jaffine_pow(u, -nu / 2, K), mp.power(R0m, nu))
                P = poly[: K + 1]; Pp = [(n + 1) * poly[n + 1] for n in range(K + 1)]
                radial = jscale(P, delta)
                radial = jadd(radial, jscale(jmul(invu, P), clm * nu * R0m * R0m))
                radial = jadd(radial, jscale(jmul(rr, Pp), 2 * clm))
                qp = partner[q]
                polyp = [sum((Phi[k][n] * coeff[k][qp] for k in range(nk)), mp.mpf(0)) for n in range(K + 2)]
                if damp is not None:
                    polyp = jmul(polyp, damp)
                dphi = jscale(polyp[: K + 1], tw_sign[q] * m_arr[q])
                rot = jscale(dphi, -om) if name == "E" else jscale(jmul(invu, dphi), -om * R0m * R0m)
                tr = jmul(env, jadd(radial, rot))
                for n in range(K + 1):
                    h_, l2 = to_dd(tr[n] * fact[n]); Th[n, j, q] = h_; Tl[n, j, q] = l2
        out[name] = dict(kind=kind, hi=Th.to(model.rho.device), lo=Tl.to(model.rho.device), twist=(name != "E"))
    return out

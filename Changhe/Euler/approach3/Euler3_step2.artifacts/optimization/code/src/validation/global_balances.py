"""Global balances of an exact profile (lead d64, FINAL_REPORT 2b item 6; Stage II S9): total helicity H_tot = int U.Omega (exterior term
H_F R^(2 - 2 alpha)/(2 alpha - 2), H_F = lim r^(2 alpha + 1) int_S2 h dS) and the renormalized energy E_ren = lim (int_B_R |U|^2 - (R^p/p) E_F(R)),
p = 3 - 2 alpha, E_F(R) = R^(2 alpha) int_S2 |U|^2 dS (campaign convention, no 1/2; -> int |F|^2 = 1 in the gauge). Exact profiles of the tail
class have H_tot = 0 and E_ren = 0; every state has int Omega.R_u = (1 - 2 c_l) H_tot and int U.R_u = beta_0 E_ren. Also reported: H_tot / int |h|
and the core alignment int h / int |U||Omega| on r < r_core. Quadrature: dense geometric radial grid (n_per_octave radii per octave from
R0 2^-k_in to R0 2^k_out) with the holdout angular Gauss grid; cumulative Simpson-like O(h^4) rule in log r (integral of the cubic through
four neighbours per interval); the ball below the first radius uses the first-radius density (O(rho_min^3)). Differentiable in z (for the S9 rows)."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import Model, alpha_of

DT = torch.float64


def _cum_weights(lr):
    """Lower-triangular matrix W (n, n): (W g)_j = int_(lr_0)^(lr_j) g dlog r, cubic-interpolant rule (O(h^4)) on the uniform grid lr."""
    n = len(lr); W = np.zeros((n, n)); row = np.zeros(n)
    xg, wg = np.polynomial.legendre.leggauss(4)
    for j in range(1, n):
        j0 = int(np.clip(j - 2, 0, n - 4)); idx = [j0, j0 + 1, j0 + 2, j0 + 3]
        xs = 0.5 * (lr[j] - lr[j - 1]) * xg + 0.5 * (lr[j] + lr[j - 1])
        for a_ in idx:
            val = np.ones_like(xs)
            for b_ in idx:
                if b_ != a_:
                    val *= (xs - lr[b_]) / (lr[a_] - lr[b_])
            row[a_] += 0.5 * (lr[j] - lr[j - 1]) * (wg * val).sum()
        W[j] = row
    return W


class GlobalBalances:
    def __init__(self, model, n_per_octave=8, k_in=10, k_out=20, device=None):
        device = device or model.r.device
        self.model = model; R0 = model.R0
        radii = R0 * 2.0 ** np.linspace(-k_in, k_out, n_per_octave * (k_in + k_out) + 1)
        Lx = getattr(model, "L_ext", model.L)
        self.em = Model(L=model.L, Nk=model.Nk, m_parity=model.m_parity, R0=R0, r_nodes=radii, ntheta=2 * Lx + 12, nphi=4 * Lx + 18, c_l=model.c_l0, omega=model.omega0,
                        free_params=model.free_params, channels=model.channels, device=device, phi0=math.pi / (2 * (4 * Lx + 18)))
        self.r = self.em.r; self.lr = torch.log(self.r)
        self.W = torch.tensor(_cum_weights(np.log(radii)), dtype=DT, device=device)
        self.w_ang = self.em.grid.w                                   # sum 4 pi

    def pressure(self, prob, z, c_l, omega):
        """Full-space pressure P (Nr, Na) on the dense grid from the training-grid source (for the head flux Phi(s))."""
        from ..pressure.poisson_sh import PressureSolver
        from ..equations import residuals as res
        ps = getattr(self, "_ps", None)
        if ps is None or abs(ps.c_l - float(c_l)) > 1e-12 or abs(ps.omega - float(omega)) > 1e-12:
            ps = PressureSolver(self.model, p0=2 * alpha_of(float(c_l)) + 2, omega=float(omega), c_l=float(c_l), eval_model=self.em); self._ps = ps
        f = res.pressure_source(self.model.fields_grid(z, need_vort=False)['GU'])
        P, gradP, _, _ = ps.solve(f)
        return P

    def far_energy_rate(self, prob, z, c_l=None, omega=None, k_report=(12, 14, 16)):
        """Lead d67 (2026-10-25T06:28Z item 2): Phi(s) = s^2 int_S2 (|U|^2/2 + P) U_r dOmega (head flux), Phi_F(s) = s^(3 alpha - 2) Phi(s) (-> the tail
        constant), K_1 = 2 (2 - 3 alpha) Phi_F, kappa(s) = s^(alpha + 1) (E_F(s) - 1) / K_1(s) (exact profile: kappa -> 1, no s^-2 term in E_F); reported at
        s = R0 2^k, k in k_report (where E_F - 1 is 1e-4 to 1e-6, well above roundoff; at 2^20 R0 the difference E_F - 1 is roundoff-limited)."""
        model = self.model
        aT, aS, cl_, om_ = model.unpack(z)
        c_lf = float(cl_) if c_l is None else float(c_l); omf = float(om_) if omega is None else float(omega); alpha = alpha_of(c_lf)
        with torch.no_grad():
            F = self.em.fields_grid(z, need_vort=False); U = F['U']
            P = self.pressure(prob, z, c_lf, omf)
            n = self.em.grid.n.T                                         # (3, Na)
            Ur = (U * n[:, None, :]).sum(0)
            head = ((0.5 * (U ** 2).sum(0) + P) * Ur * self.w_ang[None, :]).sum(1) * self.r ** 2        # Phi(s)
            EF = self.r ** (2 * alpha) * ((U ** 2).sum(0) * self.w_ang[None, :]).sum(1)
            PhiF = self.r ** (3 * alpha - 2) * head; K1 = 2 * (2 - 3 * alpha) * PhiF
            out = {}
            for k in k_report:
                j = int(torch.argmin((self.r - model.R0 * 2.0 ** k).abs()).item())
                kap = float(self.r[j] ** (alpha + 1) * (EF[j] - 1.0) / K1[j]) if abs(float(K1[j])) > 1e-300 else None
                out[f"2^{k}"] = dict(r=float(self.r[j]), E_F_minus_1=float(EF[j] - 1.0), Phi_F=float(PhiF[j]), K_1=float(K1[j]), kappa=kap)
        return out


    def integrals(self, z, c_l=None, omega=None, r_core=None, K_H=None):
        """Returns dict with E_ren, H_tot (exterior term included), H_abs = int |h|, H_tot_over_abs, core_alignment, and the convergence of E_ren / H_tot
        over the last two octaves (all torch scalars, differentiable in z). K_H: the state's carried first far-helicity coefficient (SPEC v1.24 7.8,
        far_field.correction.far_helicity_coefficients); when given, the exterior helicity estimate carries its second term
        K_H R^(1 - 3 alpha)/(3 alpha - 1) (FINAL_REPORT section 2 item 34 (c)); H_tot_one_term keeps the first-term value for comparison."""
        model = self.model
        aT, aS, cl_, om_ = model.unpack(z)
        c_lf = float(cl_) if c_l is None else float(c_l); alpha = alpha_of(c_lf); p = 3 - 2 * alpha
        F = self.em.fields_grid(z, need_vort=True)
        U, Om = F['U'], F['Om']
        h = (U * Om).sum(0); e2 = (U ** 2).sum(0)
        Ah = (h * self.w_ang[None, :]).sum(1); Aabs = (h.abs() * self.w_ang[None, :]).sum(1); Ae = (e2 * self.w_ang[None, :]).sum(1)     # (Nr,) sphere integrals
        r3 = self.r ** 3
        def cum(A):                                                    # int_0^r A s^2 ds = int A e^(3t) dt + ball below r_0
            return self.W @ (A * r3) + A[0] * r3[0] / 3.0
        Hc = cum(Ah); Habs = cum(Aabs); Ec = cum(Ae)
        HF = self.r ** (2 * alpha + 1) * Ah; EF = self.r ** (2 * alpha) * Ae
        AF = self.r ** (2 * alpha + 1) * Aabs                            # absolute-helicity tail coefficient (verifier 2026-10-25T05:54Z: the denominator needs its exterior term too)
        Htot_one = Hc + HF * self.r ** (2 - 2 * alpha) / (2 * alpha - 2)
        ext2 = (float(K_H) * self.r ** (1 - 3 * alpha) / (3 * alpha - 1)) if K_H is not None else torch.zeros_like(self.r)
        Htot_r = Htot_one + ext2
        Habs_r = Habs + AF * self.r ** (2 - 2 * alpha) / (2 * alpha - 2)
        Eren_r = Ec - self.r ** p / p * EF
        j = len(self.r) - 1; j2 = j - 2 * int(round((len(self.r) - 1) / (math.log2(float(self.r[-1] / self.r[0])))))   # two octaves in
        out = dict(E_ren=Eren_r[j], H_tot=Htot_r[j], H_tot_one_term=Htot_one[j], H_tot_exterior_second_term=ext2[j], K_H_used=(float(K_H) if K_H is not None else None),
                   H_abs=Habs_r[j], H_abs_finite_ball=Habs[j], H_tot_over_abs=Htot_r[j] / Habs_r[j].clamp_min(1e-300),
                   H_tot_over_abs_finite_denominator=Htot_r[j] / Habs[j].clamp_min(1e-300), E_F_end=EF[j], H_F_end=HF[j], A_F_end=AF[j],
                   E_ren_change_2oct=(Eren_r[j] - Eren_r[j2]).abs(), H_tot_change_2oct=(Htot_r[j] - Htot_r[j2]).abs(), alpha=alpha, p=p, R_end=self.r[j])
        # S9 J4 (lead 2026-10-25T05:42Z, d64 A2): E_ren = int_0^inf s^(p-1) (E_F(s) - 1) ds (E_F(0) = 0, E_F(inf) = 1), so an exact profile needs radii with
        # E_F > 1; weighted excess = int s^(p-1) (E_F - 1)_+ ds, deficit = int s^(p-1) (1 - E_F)_+ ds; H_tot = int s^(1 - 2 alpha) H_F(s) ds needs H_F to change sign.
        # The ball below rho_min contributes -rho_min^p / p to the radial form (E_F = 0 there). The term (E_F(R) - 1) R^p/p below is the
        # finite-radius conversion between the two forms, NOT an exterior correction (verifier 2026-10-25T06:14Z); the infinite exterior
        # part would be (E_F(R) - 1) R^p/(q - p) for a tail rate q and is not computed here.
        with torch.no_grad():
            g = self.r ** (p - 1) * (EF - 1.0)
            excess = (self.W[j] * (self.r * torch.clamp(g, min=0.0))).sum()                      # dr = r dlog r
            deficit = (self.W[j] * (self.r * torch.clamp(-g, min=0.0))).sum() + self.r[0] ** p / p
            # finite-radius conversion (verifier 05:54Z correction of the sign): int_0^R s^(p-1)(E_F - 1) ds = Ec - R^p/p, and the finite-radius row is
            # E_ren(R) = Ec - E_F(R) R^p/p = [radial integral] - (E_F(R) - 1) R^p/p; the infinite exterior correction is a different quantity (reported
            # separately as (E_F(R) - 1) R^p/(q - p) only when a tail rate q is fitted; not done here)
            E_ren_radial = -deficit + excess - (EF[j] - 1.0) * self.r[j] ** p / p
            kmax = int(torch.argmax(EF).item())
            sgn = torch.sign(HF); flips = [float(self.r[k]) for k in range(1, len(self.r)) if sgn[k] * sgn[k - 1] < 0]
            out.update(E_F_max=EF[kmax], r_at_E_F_max=self.r[kmax], E_F_weighted_excess=excess, E_F_weighted_deficit=deficit, E_ren_radial_form=E_ren_radial,
                       E_ren_two_forms_rel_diff=(E_ren_radial - Eren_r[j]).abs() / Eren_r[j].abs().clamp_min(1e-300), E_ren_two_forms_abs_diff=(E_ren_radial - Eren_r[j]).abs(),
                       H_F_sign_change_radii=flips[:8], H_F_n_sign_changes=len(flips))
        if r_core is not None:
            msk = (self.r < float(r_core))
            if msk.sum() >= 2:
                Wc = self.W[:, msk]
                hn = (h * self.w_ang[None, :]).sum(1); an = ((U.norm(dim=0) * Om.norm(dim=0)) * self.w_ang[None, :]).sum(1)
                jc = int(msk.sum().item()) - 1
                Hcore = (self.W[jc] * (hn * r3)).sum() + hn[0] * r3[0] / 3.0; Acore = (self.W[jc] * (an * r3)).sum() + an[0] * r3[0] / 3.0
                out.update(core_alignment=Hcore / Acore.clamp_min(1e-300), core_radius_used=float(self.r[jc]))
        return out


def far_rate_text(fr):
    return "kappa finite-radius quotient (d67; exact profile -> 1; the limiting coefficient ratio is the direct K_carried/K_required) " + ", ".join(f"{k}: {v['kappa']:.3g} (E_F-1 {v['E_F_minus_1']:.2e}, Phi_F {v['Phi_F']:.3e})" if v['kappa'] is not None else f"{k}: n/a" for k, v in fr.items())


def balances_text(b):
    f = lambda v: float(v) if torch.is_tensor(v) else v
    s = (f"E_ren={f(b['E_ren']):.4f} (change over the last two octaves {f(b['E_ren_change_2oct']):.1e}, E_F(R_end)={f(b['E_F_end']):.4f}) | H_tot={f(b['H_tot']):.4f} incl. exterior term"
         + (f" (both terms, v1.24; second term {f(b['H_tot_exterior_second_term']):.1e} at R_end)" if b.get('K_H_used') is not None else "") + " "
         f"(change {f(b['H_tot_change_2oct']):.1e}) | int|h|={f(b['H_abs']):.4f} incl. its exterior term (finite ball {f(b['H_abs_finite_ball']):.4f}) | H_tot/int|h|={f(b['H_tot_over_abs']):.4f} (finite-ball denominator {f(b['H_tot_over_abs_finite_denominator']):.4f})")
    if "core_alignment" in b:
        s += f" | core alignment int h / int |U||Omega| (r < {b['core_radius_used']:.3g})={f(b['core_alignment']):.3f}"
    if "E_F_max" in b:
        s += (f" | J4: max E_F={f(b['E_F_max']):.5f} at r={f(b['r_at_E_F_max']):.3g}, weighted excess {f(b['E_F_weighted_excess']):.2e} deficit {f(b['E_F_weighted_deficit']):.3f}, "
              f"E_ren radial form {f(b['E_ren_radial_form']):.4f} (two forms differ {f(b['E_ren_two_forms_rel_diff']):.1e} relative, {f(b.get('E_ren_two_forms_abs_diff', float('nan'))):.1e} absolute), H_F sign changes {b['H_F_n_sign_changes']} at r={[round(v, 3) for v in b['H_F_sign_change_radii']]}")
    return s + " (exact profile: E_ren = 0, H_tot = 0; d64 formulas, primary fields)"

"""Is the change between two successive fitted states (coarse A -> fine B, same branch) a weakly constrained direction of the fine
problem? The coarse state is transferred to the fine basis by lm_solve.refit (its fields are evaluated on the fine grid and fitted in
the fine basis; the transfer error is measured), d = z_B - z_A' is the coefficient difference, J = Jacobian of the fine problem at z_B
(fixed beta; rows = weighted desingularized residuals, origin rows and, if the state has them, the first-tail rows). Reported:
  sigma_eff = |J d| / |d| against the singular value spectrum of J (fraction of singular values below sigma_eff),
  the energy of d in the smallest 1, 5, 20 percent of the right singular directions,
  the misfits |F(z_A')|, |F(z_B)| in the fine problem, the linear prediction |F(z_B) - J d| of |F(z_A')|,
  and the relative sup changes of a, G, W1, W2 on the fine collocation grid (B against A'), with the transfer error (A' against A).
Sampled, fitted-state data; a direction with a small sigma_eff is a direction the objective constrains weakly at z_B, no more."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import LMProblem, load_state, refit, make_model, rad_of_r, dev, DT

def build(d):
    tail = float(d['tail']) if ('tail' in d and float(d['tail']) > 0) else None
    p = LMProblem(int(d['N']), int(d['M']), float(d['L']), float(d['beta_map']), float(d['sigma_a']), float(d['sigma_G']),
                  float(d['a0_target']), float(d['w_origin']), float(d['beta']), ov=float(d['Ne']) / int(d['N']),
                  mapname=str(d['mapname']), Rw=float(d['Rw']), tail=tail, t1=(float(d['t1']) if tail else 1e-5))
    z = p.pack(torch.tensor(d['ca'], dtype=DT, device=dev), torch.tensor(d['cG'], dtype=DT, device=dev), float(d['beta']))
    return p, z

def main(pa, pb):
    dA, dB = load_state(pa), load_state(pb); pA, zA = build(dA); pB, zB = build(dB)
    print(f"A = {pa} (N={pA.N}, M={pA.M}, tail={pA.tail}), B = {pb} (N={pB.N}, M={pB.M}, tail={pB.tail}), beta = {float(dB['beta'])}")
    with torch.no_grad():
        zAp = refit(pA, zA, pB)
        FA, FB = pB.F(zAp), pB.F(zB); d = zB - zAp
        # fields on the fine collocation grid: A (original basis), A' (transferred), B
        mo = pA.model; rad_old = rad_of_r(mo, pA.mapname, pB.model.r)
        tmp = make_model(pA.mapname, pA.N, pA.M, pA.L, pA.beta_map, pA.sigma_a, pA.sigma_G, rad_old, pB.model.th)
        caA, cGA, bA = pA.unpack(zA); fA = tmp.fields(caA, cGA, bA)
        caAp, cGAp, bAp = pB.unpack(zAp); fAp = pB.model.fields(caAp, cGAp, bAp)
        caB, cGB, bB = pB.unpack(zB); fB = pB.model.fields(caB, cGB, bB)
        def rel(f1, f2, k): return float((f2[k] - f1[k]).abs().max() / f2[k].abs().max())
        print("  transfer error A' vs A on the fine grid (rel. sup): " + ", ".join(f"{k} {rel(fA, fAp, k):.2e}" for k in ('a', 'G', 'W1', 'W2')))
        print("  change B vs A' on the fine grid (rel. sup):        " + ", ".join(f"{k} {rel(fAp, fB, k):.2e}" for k in ('a', 'G', 'W1', 'W2')))
        print(f"  misfits in the fine problem: |F(A')| = {float(FA.norm()):.4e}, |F(B)| = {float(FB.norm()):.4e} (B's logged RMS is |F|/sqrt(rows) convention of lm_solve: rows = {FB.numel()})")
        J = pB.jac(zB); Jd = J @ d
        print(f"  |d| = {float(d.norm()):.4e}, |J d| = {float(Jd.norm()):.4e}, sigma_eff = |J d|/|d| = {float(Jd.norm()/d.norm()):.4e}; linear prediction |F(B) - J d| = {float((FB - Jd).norm()):.4e} against |F(A')| = {float(FA.norm()):.4e}")
        rem = FA - (FB - Jd)   # F(zB - d) - [F(zB) - J d]: nonlinear remainder of the step
        print(f"  nonlinear remainder |F(zA') - F(zB) + J d| = {float(rem.norm()):.4e} (against |J d| = {float(Jd.norm()):.4e}, |F(A')| = {float(FA.norm()):.4e})")
        for t in (0.0, 0.25, 0.5, 0.75, 1.0):
            print(f"    |F(zA' + t d)| at t = {t:.2f}: {float(pB.F(zAp + t * d).norm()):.4e}", flush=True)
        try:
            U, S, Vh = torch.linalg.svd(J, full_matrices=False); S = S.cpu().numpy()
            sig = float(Jd.norm() / d.norm()); frac = float((S < sig).mean())
            print(f"  singular values of J: max {S[0]:.3e}, median {np.median(S):.3e}, min {S[-1]:.3e}; fraction below sigma_eff: {frac:.3f} (sigma_eff/max = {sig/S[0]:.2e})")
            c = (Vh @ d).cpu().numpy(); e = c**2 / np.sum(c**2); n = len(c)
            for pct in (1, 5, 20, 50):
                k = max(1, int(round(pct / 100 * n))); print(f"  energy of d in the smallest {pct:2d} percent of singular directions ({k} of {n}): {e[-k:].sum():.3f}  (singular values there <= {S[-k]:.3e})")
        except torch.OutOfMemoryError:
            del J; torch.cuda.empty_cache()
            print("  SVD skipped: CUDA out of memory (GPU shared); sigma_eff and the remainder above stand on their own")

if __name__ == '__main__': main(sys.argv[1], sys.argv[2])

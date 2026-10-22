"""jac_augmented.py -- continuation (augmented) Jacobians from a saved inner Jacobian (runs/jac_<tag>.npz of jacobian_fp.py), CPU only (shift 6;
astra shift6b: the weak exponent direction near a turning point lives in the AUGMENTED system, not in the inner map).
Unknowns x (active coefficients) with the inner fixed-point equation F(x; lambda, beta) = T(x) - x = 0 and the scalar strain equation
m(x; lambda, beta) = c_op(beta).x + lambda c_f - 1 - beta/2 = 0:
  B_beta   = [[I - J_T, -T_beta], [c^T, c_beta.x* - 1/2]]      (lambda fixed, unknowns (x, beta); singular at a turning point of beta(lambda), i.e. where m_beta = 0)
  B_lambda = [[I - J_T, -T_lambda], [c^T, c_f]]                (beta fixed, unknowns (x, lambda); regular iff m_lambda != 0)
  C        = [[I - J_T, -T_lambda, -T_beta], [c^T, c_f, c_beta.x* - 1/2]]   (1333 x 1334; its kernel is the tangent of the solution curve)
Reported: singular values (smallest few) of B_beta, B_lambda, C in the raw coefficient-plus-parameter Euclidean norm and with the parameter
columns scaled to the median column norm of I - J_T (parameter-scaling dependence); the kernel vector of C (tangent) and its (dlambda, dbeta)
components; the Schur-complement check m_lambda = c_f + c^T (I - J_T)^-1 T_lambda, m_beta likewise.
Usage: python3 code/jac_augmented.py runs/jac_L2v.npz --c_f 1.922901 [--out runs/jacaug_L2v.json]"""
import sys, json, argparse, numpy as np
ap = argparse.ArgumentParser(); ap.add_argument('jac'); ap.add_argument('--c_f', type=float, required=True); ap.add_argument('--out', default='')
a = ap.parse_args(); J = np.load(a.jac)
JT = J['JT']; n = JT.shape[0]; I = np.eye(n); A = I - JT
Tl = J['dT_dlam']; Tb = J['dT_dbeta']; c = J['c_act']; cb = J['dc_dbeta']; xs = J['x_star']
mb_expl = float(cb @ xs - 0.5)
def aug(cols, last):
    top = np.hstack([A, -np.stack(cols, 1)]); bot = np.concatenate([c, last])[None, :]
    return np.vstack([top, bot])
out = {}
sA = np.linalg.svd(A, compute_uv=False); out['inner'] = dict(sigma_min=float(sA[-1]), sigma_max=float(sA[0]), median_col_norm=float(np.median(np.linalg.norm(A, axis=0))))
scale = out['inner']['median_col_norm']
for name, cols, last in [('B_beta', [Tb], [mb_expl]), ('B_lambda', [Tl], [a.c_f]), ('C_full', [Tl, Tb], [a.c_f, mb_expl])]:
    M = aug(cols, last); s = np.linalg.svd(M, compute_uv=False)
    # parameter columns scaled to the median coefficient column norm
    cols_s = [col * scale / np.linalg.norm(np.concatenate([col, [l]])) for col, l in zip(cols, last)]; last_s = [l * scale / np.linalg.norm(np.concatenate([col, [l]])) for col, l in zip(cols, last)]
    Ms = aug(cols_s, last_s); ss = np.linalg.svd(Ms, compute_uv=False)
    out[name] = dict(shape=list(M.shape), sv_smallest_raw=s[-4:][::-1].tolist(), sv_largest_raw=float(s[0]), sv_smallest_scaled=ss[-4:][::-1].tolist(), sv_largest_scaled=float(ss[0]), param_col_norms=[float(np.linalg.norm(np.concatenate([col, [l]]))) for col, l in zip(cols, last)])
    print(f"{name} {M.shape}: raw singular values smallest {s[-4:][::-1]} largest {s[0]:.3f}; parameter columns scaled to {scale:.3f}: smallest {ss[-4:][::-1]} largest {ss[0]:.3f}")
# tangent of the curve: kernel of C (raw)
C = aug([Tl, Tb], [a.c_f, mb_expl]); U, S, Vh = np.linalg.svd(C); t = Vh[-1]
dl, db = t[-2], t[-1]; out['tangent'] = dict(dlambda=float(dl), dbeta=float(db), dlambda_over_dbeta=float(dl / db) if abs(db) > 1e-300 else None, coeff_part_norm=float(np.linalg.norm(t[:-2])), residual=float(np.linalg.norm(C @ t)))
print(f"tangent of the solution curve (kernel of C): dlambda/dbeta = {dl / db:+.5e} (Jacobian-based -m_beta/m_lambda = {-(mb_expl + c @ np.linalg.solve(A, Tb)) / (a.c_f + c @ np.linalg.solve(A, Tl)):+.5e}); |C t| = {np.linalg.norm(C @ t):.2e}")
ml = a.c_f + c @ np.linalg.solve(A, Tl); mbt = mb_expl + c @ np.linalg.solve(A, Tb)
out['schur'] = dict(m_lambda=float(ml), m_beta=float(mbt), bound_sigma_min_B_beta=float(abs(mbt) / np.sqrt(1 + np.linalg.norm(np.linalg.solve(A, Tb)) ** 2)), bound_sigma_min_B_lambda=float(abs(ml) / np.sqrt(1 + np.linalg.norm(np.linalg.solve(A, Tl)) ** 2)))
print('Schur complements:', out['schur'])
if a.out: json.dump(out, open(a.out, 'w'), indent=1)

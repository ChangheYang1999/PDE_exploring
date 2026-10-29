"""Lead cross-review of the verifier's topic68 (variable-projection derivatives): numerical checks of
(1) the full-rank derivative z' = B^+(b' - B'z) - (B^T B)^-1 B'^T r on the (s, t) example and on random matrices,
(2) the Daleckii-Krein truncated-SVD derivative (4)-(5) on random matrices with a fixed retained set,
(3) the two zero-residual counterexamples (rotating subspace; max-column-scaled), where the frozen-subspace derivative is 0."""
import json, numpy as np
rng = np.random.default_rng(7)
out = {}
def fd(fun, h=1e-6):
    return (fun(h) - fun(-h)) / (2 * h)
# (1) example
s, dlt = 0.3, 0.2
zfun = lambda t: np.linalg.lstsq(np.array([[s], [t]]), np.array([1.0, dlt]), rcond=None)[0][0]
out['ex1_fd'] = fd(zfun); out['ex1_formula'] = dlt / s**2; out['ex1_frozen'] = 0.0
# (1) random full rank
m, n = 9, 4
B0, B1, b0, b1 = rng.normal(size=(m, n)), rng.normal(size=(m, n)), rng.normal(size=m), rng.normal(size=m)
Bt = lambda t: B0 + t * B1; bt = lambda t: b0 + t * b1
z0 = np.linalg.lstsq(B0, b0, rcond=None)[0]; r0 = B0 @ z0 - b0
zp = np.linalg.pinv(B0) @ (b1 - B1 @ z0) - np.linalg.solve(B0.T @ B0, B1.T @ r0)
zfd = (np.linalg.lstsq(Bt(1e-6), bt(1e-6), rcond=None)[0] - np.linalg.lstsq(Bt(-1e-6), bt(-1e-6), rcond=None)[0]) / 2e-6
out['rand_fullrank_err'] = float(np.abs(zp - zfd).max())
out['rand_fullrank_omitted_norm'] = float(np.linalg.norm(np.linalg.solve(B0.T @ B0, B1.T @ r0)))
# (2) truncated SVD with fixed retained set
def trunc(M, b, k):
    U, S, Vt = np.linalg.svd(M, full_matrices=False)
    return Vt[:k].T @ ((U[:, :k].T @ b) / S[:k])
M0 = rng.normal(size=(m, n)) @ np.diag([3, 1.5, 1e-2, 5e-3]); M1 = rng.normal(size=(m, n)); k = 2
H = M0.T @ M0; Hp = M1.T @ M0 + M0.T @ M1; g = M0.T @ b0; gp = M1.T @ b0 + M0.T @ b1
lam, V = np.linalg.eigh(H); idx = np.argsort(lam)[::-1]; lam, V = lam[idx], V[:, idx]
f = np.array([1 / l if i < k else 0.0 for i, l in enumerate(lam)])
L = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        L[i, j] = (-1 / lam[i]**2 if i < k else 0.0) if i == j else (f[i] - f[j]) / (lam[i] - lam[j])
yp = V @ (L * (V.T @ Hp @ V)) @ V.T @ g + V @ np.diag(f) @ V.T @ gp
yfd = (trunc(M0 + 1e-6 * M1, b0 + 1e-6 * b1, k) - trunc(M0 - 1e-6 * M1, b0 - 1e-6 * b1, k)) / 2e-6
y0 = trunc(M0, b0, k)
U, S, Vt = np.linalg.svd(M0, full_matrices=False)
frozen = Vt[:k].T @ ((U[:, :k].T @ (b1 - M1 @ y0)) / S[:k])
out['trunc_DK_err'] = float(np.abs(yp - yfd).max())
out['trunc_frozen_err'] = float(np.abs(frozen - yfd).max()); out['trunc_true_norm'] = float(np.linalg.norm(yfd))
# (3a) rotating subspace counterexample
eps = 0.01
Rt = lambda t: np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
Mt = lambda t: np.diag([1, eps]) @ Rt(t).T
bb = np.array([1.0, 0.0])
yf = lambda t: trunc(Mt(t), bb, 1)
out['cx1_true'] = fd(yf).tolist(); out['cx1_residual'] = float(np.abs(Mt(0.1) @ yf(0.1) - bb).max())
Mp = (Mt(1e-6) - Mt(-1e-6)) / 2e-6
U, S, Vt = np.linalg.svd(Mt(0), full_matrices=False)
out['cx1_frozen'] = (Vt[:1].T @ ((U[:, :1].T @ (-Mp @ yf(0))) / S[:1])).tolist()
# (3b) max-column-scaled counterexample
kap = 2 * (1 - eps**2) / eps**2
Mt2 = lambda t: np.array([[1, 1], [eps * (1 + kap * t), -eps]])
def vplus(t):
    w, Vv = np.linalg.eigh(Mt2(t).T @ Mt2(t)); v = Vv[:, np.argmax(w)]; return v * np.sign(v.sum())
y2 = lambda t: trunc(Mt2(t), Mt2(t) @ vplus(t), 1)
h = 1e-8
out['cx2_true_norm'] = float(np.linalg.norm((y2(h) - y2(-h)) / (2 * h)))
out['cx2_colmax'] = [float(np.abs(Mt2(h)).max(axis=0).max()), float(np.abs(Mt2(h)).max(axis=0).min())]
Mp2 = (Mt2(h) - Mt2(-h)) / (2 * h); bp2 = (Mt2(h) @ vplus(h) - Mt2(-h) @ vplus(-h)) / (2 * h)
U, S, Vt = np.linalg.svd(Mt2(0), full_matrices=False)
out['cx2_frozen_norm'] = float(np.linalg.norm(Vt[:1].T @ ((U[:, :1].T @ (bp2 - Mp2 @ y2(0))) / S[:1])))
print(json.dumps(out, indent=1))
json.dump(out, open('checks/topic68_check_output.json', 'w'), indent=1)

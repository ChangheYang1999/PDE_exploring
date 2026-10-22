"""Stationarity diagnostics of saved least-squares states (coverage-table cell 'numerical gradients and stationarity tolerances'): rebuild
the state's fixed-beta objective from the checked top-level saved settings (beta, Rw, w_origin, tail rows and t1, patch rows and patch_n
when present; ypen/pres rows are not reconstructed, so states fitted with them are not handled), evaluate F(z), the gradient g = J^T F of
phi = (1/2)|F|^2 by reverse-mode AD, Jg by one jvp, and an estimate s_hat of sigma_max(J) by power iteration on J^T J (jvp/vjp pairs, no
Jacobian formed; the relative change of the estimate over the last 5 iterations is printed as a convergence indicator, no error bound).
Reports: |F| rebuilt and stored (a consistency check at the stored point; equality of one norm does not identify the residual map),
|g|, s_hat, the normalized gradient estimate eta_hat = |g| / (s_hat |F|) (for the exact sigma_max the operator-norm inequality puts it in
[0, 1]), the Gauss-Newton model's optimal decrease along -g, Delta* = |g|^4 / (2 |Jg|^2), relative to phi (this is the model decrease,
not a decrease of the nonlinear objective), and the lower bound eta_hat^2 of Delta*/phi that holds with the exact sigma_max. Sampled
values of fitted states; nothing about profiles. Usage: python3 -u code/stationarity.py state1.npz [state2.npz ...]"""
import sys, json, ast, numpy as np, torch
sys.path.insert(0, 'code')
import lm_solve as L

def build(d):
    extra = d['extra'].item() if 'extra' in d else {}
    if isinstance(extra, bytes): extra = extra.decode()
    if isinstance(extra, str):
        try: extra = json.loads(extra)
        except Exception:
            try: extra = ast.literal_eval(extra)
            except Exception: extra = {}
    if not isinstance(extra, dict): extra = {}
    if extra.get('ypen') or extra.get('pres'): raise SystemExit('state fitted with ypen/pres rows: objective not reconstructed by this script')
    mapname = str(d['mapname']) if 'mapname' in d else 'xi'
    N, M, Ld = int(d['N']), int(d['M']), float(d['L']); ov = float(d['Ne']) / N
    beta = float(d['beta']); beta_map = float(d['beta_map']) if 'beta_map' in d else beta
    tail = float(d['tail']) if 'tail' in d else float(extra.get('tail') or 0.0); tail = tail if tail > 0 else None
    t1 = float(d['t1']) if 't1' in d else float(extra.get('t1', 1e-5))
    patch = np.array(d['patch']).tolist() if 'patch' in d else extra.get('patch')
    patch = tuple(patch) if (patch is not None and len(patch) == 4 and any(float(v) != 0.0 for v in patch)) else None   # [0,0,0,0] = saved sentinel for 'no patch'
    patch_n = extra.get('patch_n')
    wmax = float(d['wmax']) if ('wmax' in d and float(d['wmax']) > 0) else None
    prob = L.LMProblem(N, M, Ld, beta_map, float(d['sigma_a']), float(d['sigma_G']), float(d['a0_target']),
                       float(d['w_origin']) if 'w_origin' in d else 3.0, beta, ov=ov, mapname=mapname,
                       Rw=float(d['Rw']) if 'Rw' in d else 30.0, wmax=wmax, tail=tail, t1=t1, patch=patch, patch_n=patch_n)
    z = prob.pack(torch.tensor(d['ca'], dtype=L.DT, device=L.dev), torch.tensor(d['cG'], dtype=L.DT, device=L.dev), beta)
    return prob, z, dict(tail=tail, t1=t1, patch=patch, extra=extra)

def patch_n_of(extra): return extra.get('patch_n') if isinstance(extra, dict) else None

def main(paths, iters=30):
    print("state                        N   M   n_unk   m_rows   |F| rebuilt   |F| stored    |J^T F|     s_hat(sigma_max est) conv5   eta_hat=|g|/(s_hat|F|)   Delta*/phi=|g|^4/(2|Jg|^2 phi)   eta_hat^2   settings")
    for p in paths:
        d = L.load_state(p); name = p.split('/')[-1].replace('.npz', '')
        prob, z, st = build(d); extra = st.get('extra', {})
        hist = json.loads(str(d['hist'])) if 'hist' in d else []
        Fst = hist[-1]['Fnorm'] if hist else float('nan')
        z = z.detach().clone().requires_grad_(True)
        Fz = prob.F(z); Fn = float(Fz.norm())
        g = torch.autograd.grad(0.5 * (Fz ** 2).sum(), z)[0].detach(); gn = float(g.norm())
        # power iteration for sigma_max(J)
        torch.manual_seed(0); v = torch.randn(z.numel(), dtype=L.DT, device=L.dev); v /= v.norm(); hist_s = []
        zc = z.detach()
        for k in range(iters):
            u = torch.func.jvp(prob.F, (zc,), (v,))[1]                     # J v
            w = torch.func.vjp(prob.F, zc)[1](u)[0]                         # J^T (J v)
            hist_s.append(float(w.norm()) ** 0.5); v = w / w.norm()
        smax = hist_s[-1]; conv = abs(hist_s[-1] - hist_s[-6]) / hist_s[-1]
        Jg = torch.func.jvp(prob.F, (zc,), (g,))[1]; Jgn = float(Jg.norm())
        phi = 0.5 * Fn ** 2; eta = gn / (smax * Fn); dstar = (gn ** 4 / (2 * Jgn ** 2)) / phi
        print(f"{name:28s} {int(d['N']):3d} {int(d['M']):3d} {z.numel():7d} {Fz.numel():8d}   {Fn:.6e}  {Fst:.6e}  {gn:.3e}  {smax:.4e}  {conv:.1e}   {eta:.3e}              {dstar:.3e}                     {eta**2:.3e}   tail={st['tail']} t1={st['t1']:.0e} patch={st['patch']} patch_n={patch_n_of(extra)}")

if __name__ == '__main__':
    main(sys.argv[1:])

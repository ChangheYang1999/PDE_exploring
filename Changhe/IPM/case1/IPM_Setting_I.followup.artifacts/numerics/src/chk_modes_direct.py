import sys, os, json
sys.path.insert(0, './src')
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt
jpath, rpath = sys.argv[1], sys.argv[2]
J, z, model, ch, D0 = jt.load_J(jpath, 480); del J; torch.cuda.empty_cache(); n = z.shape[0]; N, M = model.N, model.M
b, cl, C = ch.unpack(z); cl = float(cl)
s4 = f'./runs/s4e_{os.path.basename(D0["state"]).replace(".npz","")}.json'
xstar = float(json.load(open(s4))['xstar'])
r, w, v = model.radii(cl); th = model.ang.theta_np
rr = np.repeat(r[1:], M); tt = np.tile(th, N); X = rr*np.cos(tt); Y = rr*np.sin(tt); dP = np.hypot(X-xstar, Y)
near5 = np.concatenate([dP < 5, [True, False]]); near2 = np.concatenate([dP < 2, [True, False]])
R = torch.load(rpath); Wv = R['Wv'].cuda().double(); D = R['D'].double().cpu().numpy(); Q = R['Q'].double().cpu().numpy()
U, sv, Wt = np.linalg.svd(D, full_matrices=False); kk = Wv.shape[1]
Fz = lambda zz: ch.F(zz, **jt.RES_KW)
print(f'state {D0["state"]}, stored Ritz values: ' + ' '.join(f'{x:.2e}' for x in sv[::-1][:8]))
for i in range(6):
    vv = Wv[:, kk-1-i]; vv = vv / vv.norm()
    stored = sv[kk-1-i] * U[:, kk-1-i]
    fs2 = (stored[near2]**2).sum()/(stored**2).sum(); fs5 = (stored[near5]**2).sum()/(stored**2).sum()
    for s in (1e-4, 1e-3):
        d = ((Fz(z + s*vv) - Fz(z - s*vv))/(2*s)).cpu().numpy()
        f2 = (d[near2]**2).sum()/(d**2).sum(); f5 = (d[near5]**2).sum()/(d**2).sum()
        rn = np.sqrt((d[near5]**2).mean()); rf = np.sqrt((d[~near5]**2).mean())
        print(f'mode {i}: stored |Dw| {sv[kk-1-i]:.3e} nearP frac 2/5 {fs2:.3f}/{fs5:.3f} | direct s={s:g}: |d| {np.linalg.norm(d):.3e} nearP frac 2/5 {f2:.3f}/{f5:.3f} rms near5 {rn:.2e} elsewhere {rf:.2e}', flush=True)
# noise floor: two evaluations of F at z
F1 = Fz(z).cpu().numpy(); F2 = Fz(z).cpu().numpy(); dn = F1 - F2
print(f'F repeatability: |F1 - F2| {np.linalg.norm(dn):.2e}, near5 fraction {(dn[near5]**2).sum()/((dn**2).sum()+1e-300):.3f}; |F| {np.linalg.norm(F1):.4e} near5 fraction {(F1[near5]**2).sum()/(F1**2).sum():.3f}')

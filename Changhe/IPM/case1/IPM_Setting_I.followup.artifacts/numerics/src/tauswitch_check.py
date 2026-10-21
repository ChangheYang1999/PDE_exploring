"""Validate the smooth orbit-step schedule (charmap.TAU_SWITCH): F_S (schedule) against F_A (position switch) and F_C (dt everywhere)
at a state; smoothness of F_S along a soft direction; cost. Usage: python3 src/tauswitch_check.py runs/state.npz runs/softvecs.pt tag"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt
spath, vfile, tag = sys.argv[1], sys.argv[2], sys.argv[3]
m0, x0, d0 = ipn.load_state(spath); b0, cl = m0.unpack(x0); cl = float(cl); C = float(d0['C'])
model = ipn.Model(m0.N, m0.M, m0.L, device='cuda', beta=m0.beta, nmodes=m0.nmodes, Mq=m0.Mq, Npsi=480); ch = cm.Charac(model)
z = ch.pack(b0, cl, C); n = z.shape[0]
def FS(zz): cm.TAU_SWITCH = 7.5; return ch.F(zz, **jt.RES_KW)
def FSf(zz): cm.TAU_SWITCH = 7.5; return ch.F_fixed(zz, dt=jt.RES_KW['dt'], dt_near=jt.RES_KW['dt_near'], nsteps=922)
def FA(zz): cm.TAU_SWITCH = None; r = ch.F(zz, **jt.RES_KW); cm.TAU_SWITCH = 7.5; return r
def FC(zz): cm.TAU_SWITCH = None; r = ch.F_fixed(zz, dt=jt.RES_KW['dt'], dt_near=jt.RES_KW['dt']); cm.TAU_SWITCH = 7.5; return r
def FS5(zz): cm.TAU_SWITCH = 7.5; r = ch.F(zz, dt=0.005, dt_near=0.02, far_psi=True, r_far=1e10, n_coll=3, coll_scale=0.02); return r
out = dict(tag=tag, state=spath)
t0 = time.time(); S0 = FS(z); tS = time.time() - t0
t0 = time.time(); Sf0 = FSf(z); tSf = time.time() - t0
t0 = time.time(); A0 = FA(z); tA = time.time() - t0
t0 = time.time(); C0 = FC(z); tC = time.time() - t0
t0 = time.time(); S5 = FS5(z); tS5 = time.time() - t0
out.update(FS=float(S0.norm()), FSf=float(Sf0.norm()), FA=float(A0.norm()), FC=float(C0.norm()), FS5=float(S5.norm()), S_Sf=float((S0 - Sf0).norm()), S_A=float((S0 - A0).norm()), S_C=float((S0 - C0).norm()), S_C_inf=float((S0 - C0).abs().max()), S_S5=float((S0 - S5).norm()), S_S5_inf=float((S0 - S5).abs().max()), t=dict(S=tS, Sf=tSf, A=tA, C=tC, S5=tS5))
print(f'{tag}: |F_S| {out["FS"]:.4e} (F_fixed version {out["FSf"]:.4e}, |S - Sf| {out["S_Sf"]:.1e}) |F_A| {out["FA"]:.4e} |F_C| {out["FC"]:.4e} |F_S(dt/2)| {out["FS5"]:.4e}', flush=True)
print(f'  |S - A| {out["S_A"]:.2e}  |S - C| {out["S_C"]:.2e} (max {out["S_C_inf"]:.1e})  |S - S(dt/2)| {out["S_S5"]:.2e} (max {out["S_S5_inf"]:.1e}); times S {tS:.1f}s Sf {tSf:.1f}s A {tA:.1f}s C {tC:.1f}s S5 {tS5:.1f}s', flush=True)
# rows where S - A is largest
r, _, _ = model.radii(cl); N, M = model.N, model.M
d = (S0 - A0)[:N * M].abs().cpu().numpy()   # rows 0..n_coll*M-1 are collocation rows (first 3 radial nodes), then Psi rows at nodes i = 4..N
idx = np.argsort(-d)[:5]
print('  largest |S - A| rows (flat index, value):', [(int(i), float(d[i])) for i in idx], ' hP row', float((S0 - A0)[-2]), ' ident row', float((S0 - A0)[-1]), flush=True)
S = torch.load(vfile); V = S['Vsoft_unscaled'].cuda().double(); v = V[:, 0] / V[:, 0].norm()
prev = None; rows = []
for s in (1e-4, 1e-3, 1e-2):
    dd = (FS(z + s * v) - FS(z - s * v)) / (2 * s)
    e = dict(s=s, d=float(dd.norm()), diff_prev=(float((dd - prev).norm()) if prev is not None else None), maxrow=(float((dd - prev).abs().max()) if prev is not None else None)); rows.append(e); prev = dd
    print(f'  F_S soft0 s {s:g}: |d| {e["d"]:.4e}' + (f' |d - d_prev| {e["diff_prev"]:.2e} (max row {e["maxrow"]:.1e})' if e['diff_prev'] is not None else ''), flush=True)
out['soft0_FS'] = rows
json.dump(out, open(f'{jt.LANE}/runs/tauswitch_{tag}.json', 'w'), indent=1); print('saved', flush=True)

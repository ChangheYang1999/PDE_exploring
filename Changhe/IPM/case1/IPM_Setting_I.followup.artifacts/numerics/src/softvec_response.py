"""Accurate-residual response along stored soft right singular vectors (dense_newton output runs/<tag>_softvecs.pt, scaled
coordinates with the c_l entry per 1/400): |dF/ds| (central, s = 0.05 and 0.2), d h(P)/ds, d(identity)/ds, dc_l/ds, and the
c_l and far-field energy fractions of each vector.  This is the lead's 06:09Z posting item after the accurate Jacobian.
Usage: python3 src/softvec_response.py runs/dn2_n120m48_softvecs.pt runs/dn2_n120m48.npz [Npsi=480]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm

LANE = '.'
vpath, spath = sys.argv[1], sys.argv[2]; Npsi = int(sys.argv[3]) if len(sys.argv) > 3 else 480
S = torch.load(vpath); V = S['Vsoft'].cuda(); ss = S['ssoft']
m0, x, d = ipn.load_state(spath); b, cl = m0.unpack(x); C = float(d['C'])
model = ipn.Model(m0.N, m0.M, m0.L, device='cuda', beta=m0.beta, nmodes=m0.nmodes, Mq=m0.Mq, Npsi=Npsi); ch = cm.Charac(model)
z = ch.pack(b, cl, C); n = z.numel(); N, M = model.N, model.M
scale = torch.ones(n, device='cuda'); scale[-2] = 1.0 / 400.0
Fz = lambda zz: ch.F(zz, dt=0.01, dt_near=0.04, far_psi=True, r_far=1e10, n_coll=3, coll_scale=0.02)
F0 = Fz(z); r, w_, v_ = model.radii(float(cl)); thd = model.ang.theta_np * 180 / np.pi
print(f'state {spath}: |F|_2 {F0.norm().item():.4e}, h(P)-1 {F0[-2].item():+.3e}, ident {F0[-1].item():+.3e}, c_l {z[-2].item():.9f}')
rows = []
for i in range(V.shape[1]):
    v = scale * V[:, i]; v = v / v.norm()
    vb = v[:N * M].reshape(N, M).cpu().numpy(); en = vb ** 2; tot = float((v ** 2).sum())
    far = float(en[r[1:] >= 100].sum() / tot); yax = float(en[:, thd >= 80].sum() / tot)
    out = dict(i=i, sigma=float(ss[i]), dcl=float(v[-2]), dC=float(v[-1]), far_fraction=far, yaxis_fraction=yax)
    for s_ in (0.05, 0.2):
        dF = (Fz(z + s_ * v) - Fz(z - s_ * v)) / (2 * s_)
        out[f'dF_ds_{s_}'] = float(dF.norm()); out[f'dhP_ds_{s_}'] = float(dF[-2]); out[f'dident_ds_{s_}'] = float(dF[-1])
    rows.append(out)
    print(f'  v{i}: sigma {out["sigma"]:.3e} dc_l {out["dcl"]:+.3e} dC {out["dC"]:+.3e} far {far:.2f} y-axis {yax:.2f} | |dF/ds| {out["dF_ds_0.05"]:.3e} / {out["dF_ds_0.2"]:.3e}  dh(P)/ds {out["dhP_ds_0.05"]:+.2e}  dident/ds {out["dident_ds_0.05"]:+.2e}')
json.dump(rows, open(f'{LANE}/runs/softresp_{os.path.basename(spath).replace(".npz", "")}.json', 'w'), indent=1)

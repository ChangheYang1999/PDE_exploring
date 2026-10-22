"""Lead 22:25Z (a): evaluate a saved lambda-stage state at other lambda values (predictor residual), with the fixed seed
representation (no re-projection): fit objective, max weighted mismatches, coefficient fixed-point defect, strain mismatch.
Usage: python3 code/predictor_check.py runs/blam1_lambda0.97.npz 0.97 0.96 0.94"""
import sys, os, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, DT
from charnewton import CharResidual
torch.set_default_dtype(DT)
f = sys.argv[1]; lams = [float(v) for v in sys.argv[2:]]; dev = 'cuda'
d = np.load(f)
Nt, K, Nphi, grade, L = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L'])
bb = float(d['beta_seed']) if 'beta_seed' in d.files and float(d['beta_seed']) > 0 else float(d['beta_basis'])
beta = float(d['beta']); a0 = float(d['a0'])
b = Basis(Nt, int(d['deg']), K, Nphi, ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=grade)
res = CharResidual(b, L, bb, Nphi_res=24, r_in=float(d['r_in']), dt=float(d['dt']), device=dev, max_steps=20000, rmap=str(d['rmap']), beta_fixed=beta, wc=0.0, include_RF=True)
res.use_graph = True; res.free_a0 = False; res.eps = 1.0
cGf = torch.tensor(d['cG_f'], dtype=DT, device=dev); cG = torch.tensor(d['cG'], dtype=DT, device=dev); act = res.active
print(f"state {f}: beta={beta:.6f} a0={a0:.6f} basis beta_b={bb} stored lambda={float(d['lam']) if 'lam' in d.files else float('nan')}")
for lam in lams:
    res.cG_f = lam * cGf
    R, info = res.run(cG[None], return_all=True)
    Gc = info['G_char'][0]; xfit = res.PG @ (res.wG * a0 * Gc); ell = (xfit @ res.c_op_act).item()
    RG = res.wG * (a0 * Gc - info['G_rep'][0]); RF = a0 * info['RF'][0]
    obj = (RG ** 2).sum().item() + (RF ** 2).sum().item(); fdef = (xfit - cG[act]).norm().item()
    print(f"  lambda={lam:.3f}: obj={obj:.4e} max|wRG|={RG.abs().max().item():.3e} max|wRF|={RF.abs().max().item():.3e} coeff defect |f|={fdef:.3e} ell={ell:.6f} m={ell - 1 - beta / 2:+.5f} unfinished={res.n_unfinished}")

"""Shift 8: sensitivity of the SOLVER'S RUNTIME velocity (CharResidual.prepare + velocity: nodal S_k = Psi_k / r^pk from the modal Green
inverse at the collocation radii, piecewise interpolation in t and differentiation of the interpolant, plus the fixed source block) to the
Gaussian quadrature order of the Green formula (ng_quad 12 = all production runs, vs NG). Frozen archived coefficients; same state, same
beta_basis, same source. Reports, on half circles of radius r (x > 0), max |U_48 - U_12| relative to max |U_48| and to beta r.
Usage: python3 code/runtime_vel_quad.py runs/<state>.npz [--ng 48] [--radii 1e2,...,1e9] [--nphi 181] [--out runs/x.json]"""
import sys, os, json, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT
from charnewton import CharResidual
from fixedsrc import make_source_block
ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--ng', type=int, default=48); ap.add_argument('--ng_ref', type=int, default=12, help='reference quadrature order (12 = production)')
ap.add_argument('--radii', type=str, default='1e2,1e3,1e4,1e5,1e6,1e7,1e8,1e9'); ap.add_argument('--nphi', type=int, default=181); ap.add_argument('--out', type=str, default='')
args = ap.parse_args(); dev = 'cuda'
d = np.load(args.state)
Nt, K, Nphi, grade, L = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L'])
rmap = str(d['rmap']); r_in = float(d['r_in']); dt = float(d['dt']); ngc = int(d['ngc']); deg = int(d['deg']); mreg = int(d['mreg'])
beta = float(d['beta']); bb = float(d['beta_basis']); lam = float(d['lam']); Nphi_res = int(d['Nphi_res']) if 'Nphi_res' in d.files else Nphi
cG = torch.tensor(d['cG'], dtype=DT, device=dev)
cG_f = torch.tensor(d['cG_f'], dtype=DT, device=dev); bb_seed = float(d['beta_seed'])
sm = dict(K=int(d['seed_K']), Nt=int(d['seed_Nt']), deg=int(d['seed_deg']), Nphi=int(d['seed_Nphi']), ngc=int(d['seed_ngc']), mreg=int(d['seed_mreg']), grade=float(d['seed_grade']), L=float(d['seed_L']), rmap=str(d['seed_rmap']))
def build(ng):
    b = Basis(Nt, deg, K, Nphi, ng_coll=ngc, ng_quad=ng, m_reg=mreg, device=dev, grade=grade)
    res = CharResidual(b, L, bb, Nphi_res=Nphi_res, r_in=r_in, dt=dt, device=dev, max_steps=20000, rmap=rmap, beta_fixed=beta, wc=0.0, include_RF=True)
    bs = Basis(sm['Nt'], sm['deg'], sm['K'], sm['Nphi'], ng_coll=sm['ngc'], ng_quad=ng, m_reg=sm['mreg'], device=dev, grade=sm['grade'])
    gs = Geometry(bs, bb_seed, sm['L'], rmap=sm['rmap'])
    make_source_block(gs, cG_f, res, lam)
    return res
out = dict(state=args.state, beta=beta, lam=lam, K=K, Nt=Nt, ng_ref=args.ng_ref, ng=args.ng, rows=[])
phi = torch.linspace(0, np.pi, args.nphi + 2, dtype=DT, device=dev)[1:-1]
W = {}
for ng in (args.ng_ref, args.ng):
    res = build(ng)
    with torch.no_grad():
        bt, nodal, jet = res.prepare(cG[None])
        rows = []
        for rs in args.radii.split(','):
            r = float(rs); X = torch.stack([r * torch.sin(phi), -r * torch.cos(phi)], -1)[None]
            Wv, _ = res.velocity(X, bt, nodal)
            rows.append((r, (Wv[0] - bt[0] * X[0]).cpu().numpy()))
        W[ng] = rows
    print(f'# ng {ng}: beta {bt.item():.6f} c {res.c_last.item() if hasattr(res,"c_last") else float("nan"):.9f}')
    del res; torch.cuda.empty_cache()
for (r, U12), (_, U48) in zip(W[args.ng_ref], W[args.ng]):
    dU = np.abs(U48 - U12).max(); mU = np.abs(U48).max()
    row = dict(r=r, max_dU=float(dU), max_U48=float(mU), rel_to_maxU=float(dU / mU), rel_to_beta_r=float(dU / (beta * r)))
    out['rows'].append(row); print(f"r={r:9.3g} max|dU|={dU:.3e} max|U48|={mU:.4g} rel={dU / mU:.3e} over_beta_r={dU / (beta * r):.3e}")
if args.out: json.dump(out, open(args.out, 'w'), indent=1); print('saved', args.out)

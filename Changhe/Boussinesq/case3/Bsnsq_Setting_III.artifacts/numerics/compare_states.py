"""Compare two states on the same basis: G and F fields at the collocation nodes by radial band, mode amplitudes,
strain, sign structure. Usage: python3 code/compare_states.py A.npz B.npz"""
import sys, os, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT
torch.set_default_dtype(DT)
dev = 'cuda'
A = np.load(sys.argv[1]); B = np.load(sys.argv[2])
Nt, K, Nphi, grade, L, bb = int(A['Nt']), int(A['K']), int(A['Nphi']), float(A['grade']), float(A['L']), float(A['beta_basis'])
b = Basis(Nt, int(A['deg']), K, Nphi, ng_coll=int(A['ngc']), m_reg=int(A['mreg']), device=dev, grade=grade)
g = Geometry(b, bb, L, rmap=str(A['rmap']))
def fields(d):
    cG = torch.tensor(d['cG'], dtype=DT, device=dev); cF = torch.tensor(d['cF'], dtype=DT, device=dev)
    return (g.Phi0G @ cG).cpu().numpy(), (g.Phi0F @ cF).cpu().numpy(), (g.c_op @ cG).item(), cG.cpu().numpy(), cF.cpu().numpy()
GA, FA, cA, cGA, cFA = fields(A); GB, FB, cB, cGB, cFB = fields(B)
rr = g.rr.cpu().numpy(); x = g.x.cpu().numpy(); y = g.y.cpu().numpy()
print(f"A: {sys.argv[1]} a0={float(A['a0']) if 'a0' in A.files else float('nan'):.5f} strain={cA:.6f} |cG|max={np.abs(cGA).max():.3f}")
print(f"B: {sys.argv[2]} a0={float(B['a0']) if 'a0' in B.files else float('nan'):.5f} strain={cB:.6f} |cG|max={np.abs(cGB).max():.3f}")
print(f"{'band':>14} {'max|GA|':>9} {'max|GB|':>9} {'max|GA-GB|':>11} {'minGA':>8} {'minGB':>8} | {'max|FA|':>9} {'max|FB|':>9} {'max|FA-FB|':>11} {'minFA':>8} {'minFB':>8}")
for lo, hi in [(0, 0.1), (0.1, 0.3), (0.3, 1), (1, 3), (3, 10), (10, 30), (30, 100), (100, 1e3), (1e3, 1e5), (1e5, 1e99)]:
    m = (rr >= lo) & (rr < hi)
    if not m.any(): continue
    print(f"{lo:7.1e}-{hi:6.0e} {np.abs(GA[m]).max():9.3e} {np.abs(GB[m]).max():9.3e} {np.abs(GA[m]-GB[m]).max():11.3e} {GA[m].min():8.3f} {GB[m].min():8.3f} | "
          f"{np.abs(FA[m]).max():9.3e} {np.abs(FB[m]).max():9.3e} {np.abs(FA[m]-FB[m]).max():11.3e} {FA[m].min():8.3f} {FB[m].min():8.3f}")
# angular mode amplitudes of G at a few radii (nodes at that radius)
Nc = b.Nc
GA2 = GA.reshape(Nc, Nphi); GB2 = GB.reshape(Nc, Nphi); rc = rr.reshape(Nc, Nphi)[:, 0]
print("G along the vertical axis directions (phi = 0 is y < 0 (below), phi = pi is above) at selected radii: GA(below) GA(above) | GB(below) GB(above)")
for r_t in [0.05, 0.3, 1, 2, 3, 5, 10, 30, 100]:
    i = int(np.argmin(np.abs(rc - r_t)))
    print(f"  r={rc[i]:8.3f}: {GA2[i,0]:9.4f} {GA2[i,-1]:9.4f} | {GB2[i,0]:9.4f} {GB2[i,-1]:9.4f}   (max over angle {np.abs(GA2[i]).max():.4f} / {np.abs(GB2[i]).max():.4f})")

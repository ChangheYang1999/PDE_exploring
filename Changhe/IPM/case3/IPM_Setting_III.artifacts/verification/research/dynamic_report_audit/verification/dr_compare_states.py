"""dr_compare_states.py -- where do two DR states (different resolutions, same tau) differ?  Evaluates rho of both on a common polar grid and prints
max|rho_A - rho_B| by radial shell together with max|rho|, and the angular spectrum of the difference in the core.  usage: A.pt NA MA B.pt NB MB C"""
import sys, numpy as np, torch
sys.path.insert(0, 'numerics/src'); import dr
torch.set_default_dtype(torch.float64)
A, NA, MA, B, NB, MB, C = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), int(sys.argv[6]), float(sys.argv[7])
mA = dr.DR(NA, MA, C, device='cuda'); mB = dr.DR(NB, MB, C, device='cuda')
sA = torch.load(A, weights_only=False); sB = torch.load(B, weights_only=False); print('tau', sA['tau'], sB['tau'])
rr = np.concatenate([np.geomspace(1e-3, 1e3, 121)]); th = np.linspace(0.02, np.pi/2 - 0.02, 64); RR, TT = np.meshgrid(rr, th, indexing='ij')
def ev(m, s):
    u = s['u'].to('cuda'); du, info = m.rhs(u, want=True); e = m.evaluate(info['beta'], info['cx'].item(), info['flds'], RR, TT); return e, info
eA, iA = ev(mA, sA); eB, iB = ev(mB, sB)
print(f"c: {iA['c'].item():.8f} {iB['c'].item():.8f}")
for lo, hi in [(1e-3, 1e-2), (1e-2, 1e-1), (0.1, 1), (1, 10), (10, 100), (100, 1e3)]:
    msk = (RR >= lo) & (RR < hi)
    d = np.abs(eA['rho'] - eB['rho'])[msk]; dU = np.abs(eA['U2'] - eB['U2'])[msk]
    print(f"r in [{lo:.0e},{hi:.0e}): max|drho| {d.max():.2e} (max|rho| {np.abs(eA['rho'][msk]).max():.2e}, rel {d.max()/np.abs(eA['rho'][msk]).max():.1e}); max|dU2| {dU.max():.2e} (max|U2| {np.abs(eA['U2'][msk]).max():.2e})")
# angular structure of the difference at r = 0.3 and r = 3
for r0 in [0.03, 0.3, 3.0]:
    i = np.argmin(np.abs(rr - r0)); d = (eA['rho'] - eB['rho'])[i]
    # fit cos(2k th) content of d/sin(th)
    f = d / np.sin(TT[i]); K = np.arange(0, 24); Cm = np.cos(np.outer(TT[i], 2 * K)); coef = np.linalg.lstsq(Cm, f, rcond=None)[0]
    print(f"r = {rr[i]:.3f}: difference angular coefficients |c_k| (k = 0..11): " + ' '.join(f'{abs(c):.1e}' for c in coef[:12]) + f" ; max|rho| {np.abs(eA['rho'][i]).max():.2e}")

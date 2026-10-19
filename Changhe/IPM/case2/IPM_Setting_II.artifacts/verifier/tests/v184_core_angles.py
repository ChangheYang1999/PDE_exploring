"""V184 (diagnostic for V181): at the DR512 base, the angular distance between the exit angle TH of each grid orbit and
the nearer Gamma exit angle (th1 or th2), per band of log r, and the size of A(TH) and of T there. Numerics classes imported
read only (no bytecode)."""
import sys, time, math
sys.dont_write_bytecode = True
import numpy as np, torch
sys.path.insert(0, 'code')
torch.set_default_dtype(torch.float64)
from pfwd_parity import ParityMap, load_base
t0 = time.time()
fn = 'runs/pfwd/bn/DR512_a2-1.000_it0.npz'
g0, coef, F_odd0, p, lo, hi = load_base(fn, 512)
K = Ko = 16; F_even = np.zeros(K); F_even[:min(K, len(coef))] = coef[:K]; F_odd = np.zeros(Ko)
PM = ParityMap(g0.shape[0], 512, lo, hi, p, F_even, F_odd, xeven=False)
S = PM.S; lr = S.lr.cpu().numpy()
Tg0, info0, TH = PM.T_exit(g0)
th1 = math.radians(info0['th1_deg']); th2 = math.radians(info0['th2_deg'])
TH = TH.cpu().numpy(); Tg = Tg0.cpu().numpy(); g = g0.cpu().numpy(); sc = PM.scale.cpu().numpy() if torch.is_tensor(PM.scale) else np.asarray(PM.scale)
w = lambda a: np.abs((a + np.pi) % (2 * np.pi) - np.pi)
dist = np.minimum(w(TH - th1), w(TH - th2))
A = PM.Afun(torch.tensor(TH), (th1, th2)).cpu().numpy() if hasattr(PM, 'Afun') else None
print('p %.6f lo %.2f hi %.2f; th1 %.12f th2 %.12f (rad); setup %.1f s' % (p, lo, hi, th1, th2, time.time() - t0))
bands = [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 10.01)]
print('band: dist to Gamma exit angle (rad) min / median / max over the band; median A(TH); median |T|; median |u| = |g/scale|')
for a, b in bands:
    m = (lr >= a) & (lr < b)
    d = dist[m].ravel(); Am = A[m].ravel() if A is not None else np.zeros(1)
    print('[%5.1f,%5.1f): %.2e / %.2e / %.2e ; A %.2e ; T %.2e ; u %.2e' % (a, b, d.min(), np.median(d), d.max(), np.median(Am), np.median(np.abs(Tg[m])), np.median(np.abs((g / sc)[m]))))
print('fraction of all orbits with dist < 1e-8: %.3f, < 1e-12: %.3f' % ((dist < 1e-8).mean(), (dist < 1e-12).mean()))

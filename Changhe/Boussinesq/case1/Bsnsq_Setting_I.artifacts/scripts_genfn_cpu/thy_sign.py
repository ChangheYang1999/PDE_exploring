"""Sign of Theta_y over the plane for a stored LM state (is the mixed chart (x, eta = Theta/a0) global?)."""
import sys, math, numpy as np, torch
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'scripts_polar_char'))
torch.set_num_threads(1)
from evalfields import *
f = sys.argv[1]
P, cT, cO, NT, NO, K = load_coefs(f)
r = torch.logspace(-2, 8, 401, dtype=DT)
th = torch.linspace(0, math.pi / 2, 181, dtype=DT)
prof = radial_profiles(P, cT, cO, r, NT, NO, K)
o = fields_at(prof, r, th, P.beta, NT, NO)
Thy = o['Thy'].numpy(); Th = o['Th'].numpy(); Thx = o['Thx'].numpy()
a0 = Thy[0, 0]
print('a0 approx', a0, 'c', prof['c'])
print('min Theta_y/a0', Thy.min() / a0, 'at r', float(r[np.unravel_index(Thy.argmin(), Thy.shape)[0]]), 'th deg', float(th[np.unravel_index(Thy.argmin(), Thy.shape)[1]]) * 180 / math.pi)
for lo, hi in [(0, 1), (1, 10), (10, 1e2), (1e2, 1e4), (1e4, 1e6), (1e6, 1e9)]:
    m = (r.numpy() >= lo) & (r.numpy() < hi)
    print('r in [%g,%g): min Theta_y/a0 %.4e, min Theta_x %.3e max Theta_x %.3e' % (lo, hi, Thy[m].min() / a0, Thx[m][:, 1:].min(), Thx[m][:, 1:].max()))
# far field scaled: r^(2 delta) Theta_y
d = 1 / P.beta
for i in [200, 300, 400]:
    print('r=%.3g  min_phi r^(2d) Theta_y = %.4e   phi_min deg %.1f' % (float(r[i]), (Thy[i] * float(r[i]) ** (2 * d)).min(), float(th[Thy[i].argmin()]) * 180 / math.pi))

"""Project a stored LM state onto the generating-function basis: fit G_x(x, eta) = y at sample points, eta = Theta/a0,
after the spatial scaling X -> l X (Theta -> l Theta). Usage: python3 proj.py state.npz l J Kw out.npz"""
import sys, math, numpy as np, torch
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'scripts_polar_char'))
torch.set_num_threads(1)
from evalfields import load_coefs, radial_profiles, fields_at
from jets import monos, DT
from model import Model
f, l, J, Kw, out = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
alpha = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0
P, cT, cO, NT, NO, K = load_coefs(f)
r = torch.logspace(-2, 8, 241, dtype=DT)
th = (torch.arange(48, dtype=DT) + 0.5) * math.pi / 96
prof = radial_profiles(P, cT, cO, r, NT, NO, K)
o = fields_at(prof, r, th, P.beta, NT, NO)
c_lm = prof['c']
# normalize the LM state to c = -2 exactly (Theta, Omega scale with k = -2/c, which we ignore at 1e-8)
Th = o['Th'].numpy(); X = o['X'].numpy(); Y = o['Y'].numpy()
r0 = torch.tensor([1e-6], dtype=DT); prof0 = radial_profiles(P, cT, cO, r0, NT, NO, K)
o0 = fields_at(prof0, r0, torch.tensor([math.pi / 2], dtype=DT), P.beta, NT, NO)
a0 = float(o0['Th'][0, 0]) / 1e-6
print('LM a0 %.6f c %.9f' % (a0, c_lm))
x = (l * X).ravel(); y = (l * Y).ravel(); eta = (l * Th / a0).ravel()
mod = Model(J, Kw, alpha=alpha)
Bm = mod.basis_matrix(torch.tensor(x), torch.tensor(eta), p=1)
L, ix = monos(1)
B10 = Bm[ix[(1, 0)]].numpy()
w = 1.0 / (np.abs(y) + 0.1 * np.abs(x) + 1e-3)
Aw = B10 * w[:, None]; bw = y * w
c0 = mod.h00_row()
# constraint H(0,0) = 1 with a heavy row
Aw = np.vstack([Aw, 1e6 * c0]); bw = np.concatenate([bw, [1e6]])
sc = np.linalg.norm(Aw, axis=0); sc[sc == 0] = 1
sol, *_ = np.linalg.lstsq(Aw / sc, bw, rcond=1e-14)
c = sol / sc
fit = B10 @ c
rel = np.abs(fit - y) / (np.abs(y) + 1e-12)
rr = np.sqrt(x**2 + y**2)
for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 1e3), (1e3, 1e6), (1e6, 1e9)]:
    m = (rr >= lo) & (rr < hi)
    if m.any(): print('r in [%g,%g): max rel err of G_x = y: %.3e  (%d pts)' % (lo, hi, rel[m].max(), m.sum()))
print('H00', c0 @ c)
np.savez(out, c=c, a0=a0, J=J, Kw=Kw, m=3, beta=3.0, l=l, src=f, alpha=alpha)

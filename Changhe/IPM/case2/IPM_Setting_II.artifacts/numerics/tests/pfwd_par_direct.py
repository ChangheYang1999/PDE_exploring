"""Direct (explicit-datum) parts of the x-odd rows of the parity-free Jacobian at an x-even base (referee audit, item 3), to split each linear-response column
into direct + indirect (state-response) parts.  Rows: odd LSQ coefficients (direct = identity), 5 M_up, 5 M_dn (band offsets 0.75, 1.25, 1.75, 2.25 deg at the zeros
90 / 270 deg), 50 psi_yy(0) (direct = outer-tail term -(1/pi) int A chi_j cos 3th dth r_max^(p-1)/(1-p) with A the base datum on the grid).
Usage: python3 tests/pfwd_par_direct.py base.npz [Nth=512]"""
import sys, json, math, numpy as np
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True); a = json.loads(str(d['args'])); p = float(a['p']); coef = np.array(a['par'], float)[:int(a.get('K', 16))]
K = 16; offs = np.radians([0.75, 1.25, 1.75, 2.25]); th1, th2 = math.pi / 2, 3 * math.pi / 2
chi = lambda j, t: (np.cos((j + 1) * t) if (j + 1) % 2 == 1 else np.sin((j + 1) * t))
th = np.linspace(0, 2 * math.pi, 4096, endpoint=False)
F = sum(coef[j] * (np.sin((j + 1) * th) if (j + 1) % 2 == 1 else np.cos((j + 1) * th)) for j in range(len(coef)))
A = np.cos(th) ** 2 * np.exp(F); rmax = math.exp(10.0); tail = rmax ** (p - 1) / (1 - p)
print('base', fn, 'p', p, 'direct parts of the x-odd rows per unit b_j (weights 5, 5, 50):')
print('  j   5 dM_up/db_j   5 dM_dn/db_j   50 dpsi_yy0/db_j (tail only)')
out = {}
for j in range(K):
    Mup = 5 * (np.mean(chi(j, th1 + offs)) - np.mean(chi(j, th1 - offs))); Mdn = 5 * (np.mean(chi(j, th2 + offs)) - np.mean(chi(j, th2 - offs)))
    a3c = np.mean(A * chi(j, th) * np.cos(3 * th)) * 2  # (1/pi) int A chi cos3th dth = 2 mean over the circle
    psi = 50 * (-(a3c * tail))
    out['b%d' % (j + 1)] = dict(M_up=Mup, M_dn=Mdn, psi_yy0=psi)
    print('  b%-3d %12.5f %12.5f %12.6f' % (j + 1, Mup, Mdn, psi))
json.dump(out, open('runs/pfwd/par/direct_parts_%s.json' % fn.split('/')[-1].replace('.npz', ''), 'w'), indent=1)

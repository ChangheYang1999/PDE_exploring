"""Lead 16:12Z item 3: r^{1/beta} Omega(r, phi) at r = 100, 300, 1000, 3000 and 8 angles (natural tail -> nonzero G(phi))."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state
for path in sys.argv[1:]:
    d = load_state(path); beta = float(d['beta'])
    rs = np.array([30., 100., 300., 1000., 3000., 10000.]); th = np.linspace(0.1, np.pi / 2 - 0.1, 8)
    m, f = eval_state(d, rs, th)
    Om = (f['x'] * f['y'] * f['G']).cpu().numpy()
    print(f"=== {path}: beta={beta}; r^(1/beta) Omega(r,phi); columns phi = " + ", ".join(f"{t:.2f}" for t in th))
    for i, r in enumerate(rs):
        print(f"  r={r:7.0f}: " + " ".join(f"{v:+.3e}" for v in (r ** (1 / beta)) * Om[i]))

"""Lead 16:26Z item 2: s(y) = Omega_x(0,y)/Theta_xx(0,y) = G(0,y)/(2 a(0,y)) on the y-axis (exact: 1/(2beta+1) at 0,
positive, ~ C y^{1/beta} for an exact profile with W2(0,y) > 0)."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state
for path in sys.argv[1:]:
    d = load_state(path); beta = float(d['beta'])
    ys = np.array([1e-3, 1, 3, 10, 30, 100, 300, 1000, 3000.])
    m, f = eval_state(d, ys, np.array([np.pi / 2 - 1e-9]))
    a = f['a'][:, 0].cpu().numpy(); G = f['G'][:, 0].cpu().numpy(); w2 = f['w2'][:, 0].cpu().numpy()
    s = G / (2 * a)
    print(f"=== {path}: beta={beta}, 1/(2beta+1) = {1/(2*beta+1):.5f}")
    print("    y        a(0,y)       G(0,y)       s=Omega_x/Theta_xx   W2/y")
    for y, av, gv, sv, wv in zip(ys, a, G, s, w2):
        print(f"  {y:8.3f}  {av:+.4e}  {gv:+.4e}  {sv:+.5f}          {wv:+.4f}")
    pos = (ys >= 1) & (a > 0) & (G > 0)
    if pos.sum() > 2:
        sl = np.polyfit(np.log(ys[pos]), np.log(s[pos]), 1)[0]; print(f"  log-log slope of s over the positive range: {sl:+.3f} (natural tail 1/beta = {1/beta:.3f})")

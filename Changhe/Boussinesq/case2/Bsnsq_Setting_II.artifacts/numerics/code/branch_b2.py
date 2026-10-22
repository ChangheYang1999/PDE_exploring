"""Lead 17:08Z (beta = 2): which tail branch is a state closest to? Natural: r^{1/2} Omega -> G(phi), U ~ r^{1/2};
bounded-velocity: r Omega -> sin(phi) H'(phi) with H = lim Theta. Report r^{1/2} Omega at r = 5, 20, 80 (8 angles),
r Omega vs sin(phi) H'(phi) at r = 80, 300 (H from Theta at r = 3000), and sup|U| growth."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state
for path in sys.argv[1:]:
    d = load_state(path); beta = float(d['beta'])
    th = np.linspace(0.1, np.pi / 2 - 0.1, 8); thf = np.linspace(0.01, np.pi / 2 - 0.01, 181)
    rs = np.array([5., 20., 80., 300., 3000.])
    m, f = eval_state(d, rs, th); Om = (f['x'] * f['y'] * f['G']).cpu().numpy(); Th = (f['x']**2 * f['y'] * f['a']).cpu().numpy()
    print(f"=== {path}: beta={beta}; angles phi = " + ", ".join(f"{t:.2f}" for t in th))
    print("  natural-branch test  r^{1/2} Omega(r, phi):")
    for i, r in enumerate(rs[:4]): print(f"    r={r:5.0f}: " + " ".join(f"{v:+.3e}" for v in np.sqrt(r) * Om[i]))
    print("  bounded-branch test  r Omega(r, phi)  vs  sin(phi) H'(phi), H(phi) = Theta(3000, phi):")
    mf, ff = eval_state(d, np.array([3000.0]), thf); H = (ff['x']**2 * ff['y'] * ff['a']).cpu().numpy()[0]
    Hp = np.gradient(H, thf); target = np.sin(th) * np.interp(th, thf, Hp)
    print(f"    sin(phi) H'(phi):   " + " ".join(f"{v:+.3e}" for v in target))
    for i, r in enumerate(rs[2:4]): print(f"    r Omega, r={r:5.0f}: " + " ".join(f"{v:+.3e}" for v in rs[2 + i] * Om[2 + i]))
    print("  Theta(r, phi) at r = 80, 300, 3000 (bounded H?):")
    for i in [2, 3, 4]: print(f"    r={rs[i]:5.0f}: " + " ".join(f"{v:+.3e}" for v in Th[i]))
    rr = np.geomspace(5, 3000, 12); mu, fu = eval_state(d, rr, thf); U = np.hypot(fu['U1'].cpu().numpy(), fu['U2'].cpu().numpy()).max(1)
    print("  sup_phi |U| at r = " + ", ".join(f"{r:.0f}:{u:.2e}" for r, u in zip(rr, U)) + f"; slope on [80,3000]: {np.polyfit(np.log(rr[rr>=80]), np.log(U[rr>=80]), 1)[0]:+.3f} (natural 1/2, bounded 0)")

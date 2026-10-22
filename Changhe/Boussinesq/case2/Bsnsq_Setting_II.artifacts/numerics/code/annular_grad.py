"""Lead 17:56Z: for beta > 2 states, annular ratios on A_R = {R < |X| < 2R}:
  R^{-(2-4/beta)} int_{A_R} |grad Theta|^2 ,  E(R) R^{-(4-2/beta)},  E(R) R^{-(4-4/beta)}  (E = annular kinetic energy)."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state
for path in sys.argv[1:]:
    d = load_state(path); beta = float(d['beta'])
    th = np.linspace(1e-4, np.pi / 2 - 1e-4, 200)
    print(f"=== {path}: beta={beta}")
    print("    R      gradTheta ratio   E R^-(4-2/beta)   E R^-(4-4/beta)")
    for R0 in [25., 50., 100., 200., 400., 800.]:
        rg = np.linspace(R0, 2 * R0, 121)
        m, f = eval_state(d, rg, th)
        x = f['x'].cpu().numpy(); y = f['y'].cpu().numpy(); a = f['a'].cpu().numpy(); ax = f['a_x'].cpu().numpy(); ay = f['a_y'].cpu().numpy()
        Tx = x * y * (2 * a + x * ax); Ty = x ** 2 * (a + y * ay)
        U2 = f['U1'].cpu().numpy() ** 2 + f['U2'].cpu().numpy() ** 2
        R, TH = np.meshgrid(rg, th, indexing='ij')
        G2 = 4 * np.trapz(np.trapz((Tx ** 2 + Ty ** 2) * R, th, axis=1), rg)
        E = 4 * np.trapz(np.trapz(U2 * R, th, axis=1), rg)
        print(f"  {R0:6.0f}   {G2 * R0 ** (-(2 - 4 / beta)):.4e}        {E * R0 ** (-(4 - 2 / beta)):.4e}        {E * R0 ** (-(4 - 4 / beta)):.4e}")

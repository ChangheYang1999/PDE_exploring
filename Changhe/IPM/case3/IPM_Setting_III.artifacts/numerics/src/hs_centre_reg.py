"""
hs_centre_reg.py -- centre regularity of saved hydrostatic trial states: on the y-axis G(y) = g(0, y) = y (1 + E y^2 + ...) and on the x-axis
k(xi) = g_y(xi, 0) = 1 + B xi^2 + ...  For each state print (G/y - 1)/y^2 and (k - 1)/xi^2 at y, xi = 1e-4 .. 1 (a clean cubic jet gives a plateau
equal to E, B; a drift like y^(d-3) means the discrete function is not C^3-like at the centre on that scale) and the local log-log slope of |G/y - 1|.
Also the first-quadrant check g(xi, y)/y - 1 along the diagonal.  Diagnostic of trial states only.
usage: python3 src/hs_centre_reg.py runs/a.pt ...
"""
import sys, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import hs, hs_solve
torch.set_default_dtype(torch.float64)
ys = np.array([1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1.0]); zs = np.zeros_like(ys)
print("y or xi:      " + " ".join(f"{v:10.0e}" for v in ys))
for f in sys.argv[1:]:
    st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev); ge = hs.GEval(m, m.beta_full(u))
    G = ge(zs, ys)[0]; k = ge(ys, zs)[2]; gd = ge(ys / np.sqrt(2), ys / np.sqrt(2))[0]
    e_loc = (G / ys - 1) / ys ** 2; b_loc = (k - 1) / ys ** 2
    lg = np.log(np.abs(G / ys - 1)); slope = np.gradient(lg, np.log(ys))
    print(f"{f.split('/')[-1][:-3]} {N}x{M} c={c}  E_state={st.get('E', float('nan')):+.4f} B_state={st.get('B', float('nan')):+.4f}  (first Radau node r = {float(m.rad.rR[1]):.3e})")
    print("  (G/y-1)/y^2: " + " ".join(f"{v:+10.4f}" for v in e_loc))
    print("  slope|G/y-1|:" + " ".join(f"{v:+10.4f}" for v in slope))
    print("  (k-1)/xi^2:  " + " ".join(f"{v:+10.4f}" for v in b_loc))
    print("  diag (g/y-1)/r^2: " + " ".join(f"{v:+10.4f}" for v in (gd / (ys / np.sqrt(2)) - 1) / ys ** 2))

# ---- additions after external referee cauchy1 (shift 6): pointwise logarithmic slope from the first derivative, angular jet fit, B = 6E compatibility ----
def referee_tests(files):
    """s(y) = (y G' - G)/(G - y) (pointwise log slope of G - y, exact first derivative), angular fit of (grad g - (0,1))/r^2 to (2B cos sin, B cos^2 + 3E sin^2)
    at fixed radii (fit residual = how well ONE pair (B, E) describes the jet at that radius), and B - 6E (a C^3 solution of the axis equation needs B = 6E)."""
    print("\n--- referee tests: pointwise slope s(y) = (y G'(y) - G)/(G - y); angular LSQ fit (B_r, E_r) at radius r with relative fit residual; B - 6E ---")
    ysl = np.array([1e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1]); zs = np.zeros_like(ysl)
    rr = np.array([3e-3, 1e-2, 3e-2, 1e-1]); th = np.linspace(0.02, np.pi / 2 - 0.02, 24)
    print("y:            " + " ".join(f"{v:9.0e}" for v in ysl))
    for f in files:
        st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
        hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev); ge = hs.GEval(m, m.beta_full(u))
        G, _, Gy = ge(zs, ysl); s = (ysl * Gy - G) / (G - ysl)
        E, B = st.get('E', float('nan')), st.get('B', float('nan'))
        if E != E: E = float(((G / ysl - 1) / ysl ** 2)[0]); B = float(((ge(ysl, zs)[2] - 1) / ysl ** 2)[0])
        print(f"{f.split('/')[-1][:-3]} {N}x{M}: s(y) = " + " ".join(f"{v:9.4f}" for v in s) + f"   | exact E {E:+.4f} B {B:+.4f}  B - 6E = {B - 6 * E:+.3f}")
        for r in rr:
            X = r * np.cos(th); Y = r * np.sin(th); _, gx, gy = ge(X, Y)
            lhs = np.concatenate([gx / r ** 2, (gy - 1) / r ** 2]); A = np.stack([np.concatenate([2 * np.cos(th) * np.sin(th), np.cos(th) ** 2]), np.concatenate([np.zeros_like(th), 3 * np.sin(th) ** 2])], 1)
            coef, *_ = np.linalg.lstsq(A, lhs, rcond=None); res = np.abs(A @ coef - lhs).max() / np.abs(lhs).max()
            print(f"      r = {r:7.0e}: angular fit B_r = {coef[0]:+.4f}  E_r = {coef[1]:+.4f}  B_r - 6 E_r = {coef[0] - 6 * coef[1]:+.4f}  rel fit residual {res:.1e}")

if __name__ == '__main__' and len(sys.argv) > 1:
    referee_tests(sys.argv[1:])

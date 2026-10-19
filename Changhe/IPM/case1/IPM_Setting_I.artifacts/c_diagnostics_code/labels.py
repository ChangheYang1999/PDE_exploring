"""Where the backward characteristics from r = 20 cross y = 2, 1, 0.5 near P (construct1 final)."""
import sys, numpy as np
sys.argv = ['x', 'final_candidate.npz', '20', '1']
exec(open('char_defect.py').read().split("print(f'{f}: x*")[0])
for t0 in np.linspace(0.02, np.pi / 2 - 0.02, 15):
    X0 = [20 * np.cos(t0), 20 * np.sin(t0), 0.0]
    sol = solve_ivp(rhs, (0, 200), X0, rtol=1e-10, atol=1e-12, max_step=0.02, dense_output=True,
                    events=lambda tau, Z: np.hypot(Z[0] - xs, Z[1]) - 0.03)
    T = np.linspace(0, sol.t[-1], 20000); Z = sol.sol(T)
    s = f'theta0 {t0:.3f}:'
    for yy in (4, 2, 1, 0.5):
        i = np.where((Z[1] < yy) & (np.abs(Z[0] - xs) < 5))[0]
        s += f'  y={yy}: xi {Z[0, i[0]] - xs: .3e}' if len(i) else f'  y={yy}: --'
    print(s)

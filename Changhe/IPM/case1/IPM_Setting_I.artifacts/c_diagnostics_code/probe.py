import sys, numpy as np
sys.argv = ['x', 'final_candidate.npz', '20', '1']
exec(open('char_defect.py').read().split("print(f'{f}: x*")[0])
print('x*', xs)
for y in (0.03, 0.1, 0.3, 1.0, 2.0, 4.0):
    for dx in (-0.2, 0.0, 0.2):
        l, t = polar((xs + dx, y)); print(f'  q at (x*{dx:+.1f}, {y}): {float(sq.ev(l, t)): .3e}', end='')
    print()
for t0 in (0.2387, 0.6761, 1.1134):
    X0 = [20 * np.cos(t0), 20 * np.sin(t0), 0.0]
    sol = solve_ivp(rhs, (0, 200), X0, rtol=1e-10, atol=1e-12, max_step=0.05, dense_output=True,
                    events=lambda tau, Z: np.hypot(Z[0] - xs, Z[1]) - 0.01)
    T = np.linspace(0, sol.t[-1], 4000); Z = sol.sol(T); dP = np.hypot(Z[0] - xs, Z[1])
    s = f' theta0 {t0}: '
    for e in (10, 4, 2, 1, 0.5, 0.3, 0.1, 0.03, 0.01):
        i = np.argmax(dP < e); s += f' |X-P|<{e}: tau {T[i]:.2f} J {Z[2, i]: .2e};'
    print(s)

"""Check of analysis.md 9.4: int_0^{x*} (1/g - 1/(g0 x^2)) dx = 1/(g0 x*), g = rho_y(x,0), on exported axis data."""
import sys, numpy as np
from scipy.interpolate import CubicSpline
d = np.load(sys.argv[1])
x, g, w = d['axis_x'], d['axis_G1'], d['axis_w']
s = np.where((w[:-1] < 0) & (w[1:] >= 0))[0][0]
xs = float(CubicSpline(x[s - 3:s + 4], w[s - 3:s + 4]).roots(extrapolate=False)[0])
g0 = float(np.polyfit(x[:40] ** 2, g[:40] / x[:40] ** 2, 2)[-1])
u = np.log(x)
f = (1 / g - 1 / (g0 * x ** 2)) * x          # integrand in u
cs = CubicSpline(u, f)
i0 = 0
# 1/g - 1/(g0 x^2) -> const at 0, so the piece on [0, x0] is about const * x0
lead = (1 / g[0] - 1 / (g0 * x[0] ** 2)) * x[0]
I = float(cs.integrate(u[i0], np.log(xs))) + lead
print(dict(x_star=xs, g0=g0, integral=I, target=1 / (g0 * xs), rel=(I - 1 / (g0 * xs)) * g0 * xs))

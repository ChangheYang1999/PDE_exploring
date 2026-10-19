import numpy as np
from scipy.interpolate import CubicSpline
a = np.load('../runs/b3w/R1e7_N3520_axis.npz'); b = np.load('../runs/b3w/R1e5_N2160_axis.npz')
e = np.load('final_diagnostic_fields.npz')
print('c_l', float(a['c_l']), float(b['c_l']), float(e['c_l']), 'x*', float(a['x_star']), float(b['x_star']))
sa = CubicSpline(np.log(a['x']), a['w']); sb = CubicSpline(np.log(b['x']), b['w'])
ex, ew = e['axis_x'], e['axis_w']
se = CubicSpline(np.log(ex[ex > 0]), ew[ex > 0])
A = 2 * float(a['c_l']) - 1
print('x       w(R1e7N3520)        rel(R1e5N2160 - R1e7)   rel(export - R1e7)')
for t in (0.003, 0.01, 0.05, 0.15, 0.3, 0.5, 1.0, 1.5, 2.5, 4.0, 6.0, 8.0, 8.5, 10.0):
    wa = sa(np.log(t))
    print('%-7g %.14f  %10.3e  %10.3e' % (t, wa, sb(np.log(t)) / wa - 1, se(np.log(t)) / wa - 1))

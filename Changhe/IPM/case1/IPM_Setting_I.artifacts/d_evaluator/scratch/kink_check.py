"""G47: one-sided radial log-derivatives of the transplanted c_l direction at the numerics R (closure junction)."""
import sys
import numpy as np
sys.path.insert(0, 'scratch')
from dir_on_shape import direction_on
dz = np.load(sys.argv[1], allow_pickle=True); sz = np.load(sys.argv[2], allow_pickle=True)
R = float(sz['R'])
th = np.array([0.1, 0.4, 0.8, 1.2, 1.5])
for h in [1e-3, 1e-4]:
    r = R * np.array([1 - 2 * h, 1 - h, 1.0, 1 + h, 1 + 2 * h])
    d, _ = direction_on(r, th, dz, sz)
    left = (3 * d[2] - 4 * d[1] + d[0]) / (2 * h * R)
    right = (-3 * d[2] + 4 * d[3] - d[4]) / (2 * h * R)
    print('h', h, 'r*d_r drho / drho  left', np.round(R * left / d[2], 4), 'right', np.round(R * right / d[2], 4))

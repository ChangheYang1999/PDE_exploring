"""Fit objective |raw_fun| of shapes on a given grid (lead, 2026-10-18). Usage: python3 objnorm.py NR NT SHAPE.npz ..."""
import sys
import json
import numpy as np
from centre_fit import load_shape
nr, nt = int(sys.argv[1]), int(sys.argv[2])
for f in sys.argv[3:]:
    s, z = load_shape(f, nr, nt)
    res, cen, source = s.raw_fun(z)
    print(json.dumps(dict(shape=f, nr=nr, nt=nt, norm=float(np.linalg.norm(res)), hP1=float(source[1] - 1), cl=float(1 / z[0]))))

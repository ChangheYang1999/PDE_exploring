import numpy as np
from indicial_rec import coeffs
for A, a in [(2.0, 3.0), (1.7, 0.9), (3.0, 10.0)]:
    d = 3 + 1e-9
    D, Ms, Mp = coeffs(d, A, a, 2)
    M = np.array([[D[0], Mp[1]], [Ms[0], D[1]]])
    # normalize to the same scaling as referee: det of (T+aN) restricted to (sin, sin3); compare ratio
    pred = 4*A - (A+11)*a/8 + a**2/16
    print(A, a, "det =", np.linalg.det(M), " referee pred =", pred, " ratio =", np.linalg.det(M)/pred)

# Test: the backward-recurrence "root" coincides with the endpoint-exponent crossing kappa = p_y, d* = (2+a0)/(A+1)
import numpy as np
from indicial_rec2 import G
from indicial_root import root
for (A, a0) in [(2.0, 4.0), (2.0, 5.0), (3.0, 2.5), (1.5, 1.0)]:
    ds = (2+a0)/(A+1)
    rs = []
    for n in [2000, 20000, 200000]:
        r = root(A, a0, ds-0.3, ds+0.3, n); rs.append(r)
    print(f"A={A} a0={a0}: d* = {ds:.6f}; Miller sign-change at n=2e3,2e4,2e5:", [None if r is None else round(r,6) for r in rs], flush=True)
# exact smooth mode y r^{A-1}: d=A, a0=(A-1)(A+3): residual of the single-mode vector
from indicial_rec import coeffs
for A in [1.3, 2.0, 2.7]:
    a0 = (A-1)*(A+3); D, Ms, Mp = coeffs(A, A, a0, 5)
    print(f"exact mode check A={A}: row1 {D[0]:.2e}, row3 {Ms[0]:.2e}")

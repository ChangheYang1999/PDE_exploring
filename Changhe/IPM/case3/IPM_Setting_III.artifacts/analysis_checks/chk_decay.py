import numpy as np
from indicial_rec2 import G
eps=0.2; A=1+2*eps; a0=4*eps; d=1+0.8484*eps
for n in [2000, 20000, 200000]:
    g,c = G(d,A,a0,n)
    idx=[0,1,2,5,10,30,100,300,1000,3000,10000,30000]
    print(n, f"G={g:.3e}", " ".join(f"{i}:{c[i]:+.3e}" for i in idx if i<n))
kap=(A*d-1)/(A-1); print("kappa",kap, "pi/2 exponent", -(d-1)/(A-1))

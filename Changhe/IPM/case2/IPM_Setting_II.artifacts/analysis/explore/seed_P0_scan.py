import numpy as np, sys
sys.path.insert(0, 'explore')
from seed_P0_c import strain, make_f
p = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
for FE in [1.0, 2.0, 4.0]:
    for alpha in [0.0, 0.2, 0.5]:
        for beta in [1.0, 2.0, 4.0, 8.0]:
            f0 = make_f(alpha, beta, FE)
            f = (lambda f0: (lambda x, y: f0(x, y)*(1 + x*x + y*y)**(p/2)))(f0)
            print(FE, alpha, beta, 'c =', round(strain(f, nr=1200, nt=768, p=p), 4), flush=True)

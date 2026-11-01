import sys, math, numpy as np
sys.path.insert(0, '.')
from ffcore import *
R = RingF()
rng = np.random.default_rng(1)
ff = FarField(R, 1.8, [1.0])
for trial in range(5):
    J = rng.integers(1, 9); K = rng.integers(0, 9)
    b = [0.0] + list(rng.standard_normal(J)); a = list(rng.standard_normal(K + 1))
    P1, P2 = ff.products(b, a)
    th = np.linspace(0.1, 2 * math.pi, 777)
    g = eval_even_sine(b, th); f = eval_odd_sine(a, th)
    gp = (np.cos(np.outer(th, 2 * np.arange(len(b)))) * (2 * np.arange(len(b)))) @ np.asarray(b)
    fp = (np.cos(np.outer(th, 2 * np.arange(len(a)) + 1)) * (2 * np.arange(len(a)) + 1)) @ np.asarray(a)
    e1 = np.max(np.abs(eval_odd_sine(P1, th) - g * fp)); e2 = np.max(np.abs(eval_odd_sine(P2, th) - gp * f))
    print(f'trial {trial}: J={J} K={K} err(g f\')={e1:.2e} err(g\' f)={e2:.2e}')
# Poisson inverse check on grid: -(g'' + (p+1)^2 g) = p cos f - sin f'
for trial in range(3):
    K = rng.integers(0, 7); a = list(rng.standard_normal(K + 1)); p = rng.uniform(-3, 1)
    ff.delta = 1 - 1 / 1.8
    class T: pass
    n = 1; ffp = FarField(R, 1.8, a); 
    # emulate p via delta: p = 1 - n*delta -> pick delta = 1 - p (n=1)
    ffp.delta = 1 - p
    b, st = ffp.poisson(a, 1)
    th = np.linspace(0.1, 2 * math.pi, 555)
    g = eval_even_sine(b, th); js = 2 * np.arange(len(b))
    gpp = -(np.sin(np.outer(th, js)) * js ** 2) @ np.asarray(b)
    f = eval_odd_sine(a, th); ks = 2 * np.arange(len(a)) + 1
    fp = (np.cos(np.outer(th, ks)) * ks) @ np.asarray(a)
    lhs = -(gpp + (p + 1) ** 2 * g); rhs = p * np.cos(th) * f - np.sin(th) * fp
    print(f'poisson trial {trial}: K={K} p={p:.3f} err={np.max(np.abs(lhs-rhs)):.2e} min_active_den={st}')

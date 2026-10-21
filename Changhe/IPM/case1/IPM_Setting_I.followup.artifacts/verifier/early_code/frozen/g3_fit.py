# Next-order test of the axis expansion G3(s) = c1 s + K s^p* + c3 s^3 + K1 s^p1* + ... (s > 0),
# c3 = Taylor coefficient of s^3 y^3 by the analytically continued Beta integral, K1 from the second term of the
# high-frequency symbol expansion (1+X)^-b = X^-b (1 - b/X + ...), X = t^2 eta^(2A-2).
import json, numpy as np, mpmath as mp
R = json.load(open('runs/frozen_g3.json'))
x, w = np.polynomial.legendre.leggauss(200); t = 0.5*x+1.5; w = 0.5*w
phi = np.exp(-1/((t-1)*(2-t)))
def mom(k): return float(np.sum(w*phi*t**k))
out = []
for r in R:
    A, g, b = r['A'], r['g'], r['b']
    if abs(g-(A+2)) < 1e-12: continue
    ps = (g-2)/A
    m3 = 3*A+1; q3 = (m3+1)/(2*A-2)          # eta^(3A+3-2) = eta^(3A+1)
    B3 = float(mp.gamma(q3)*mp.gamma(b-q3)/mp.gamma(b))
    c3 = -(1/(36*np.pi**2))*mom(3-(3*A+2)/(A-1))*(1/(2*A-2))*B3
    p1s = (g+2*A-4)/A; p1 = -p1s+2/A          # int eta^(3-g-2A) sin(c eta^A) = (1/A) c^p1s Gamma(p1) sin(pi p1/2)
    p1 = (4-2*A-g)/A
    K1 = -b*(1/(6*np.pi**2*A))*float(mp.gamma(p1)*mp.sin(mp.pi*p1/2))*mom(-2*b-2+p1s)
    print('A=%g g=%g  c1=%.10e K=%.10e c3=%.10e K1=%.10e p*=%.4f p1*=%.4f' % (A, g, r['c1_pred'], r['K_pred'], c3, K1, ps, p1s))
    rows = []
    for row in r['rows']:
        s = row['s']
        Gm = row['G3_minus_c1s'] if 'G3_minus_c1s' in row else row['G3'] - r['c1_pred']*s   # avoid re-adding c1 s
        r1 = Gm/s**ps
        r2 = (Gm - c3*s**3)/s**ps
        r3 = (Gm - c3*s**3 - r['K_pred']*s**ps - K1*s**p1s)
        print('  s=%.0e  (G3-c1 s)/s^p* = %.10e  (G3-c1 s-c3 s^3)/s^p* = %.10e  rel.dev %.2e   remainder after 4 terms %.3e (= %.2e s^p*)'
              % (s, r1, r2, r2/r['K_pred']-1, r3, r3/s**ps))
        rows.append(dict(s=s, r1=r1, r2=r2, rem=r3))
    out.append(dict(A=A, g=g, c1=r['c1_pred'], K=r['K_pred'], c3=c3, K1=K1, rows=rows))
json.dump(out, open('runs/frozen_g3_fit.json', 'w'), indent=1)

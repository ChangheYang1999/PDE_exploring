# numerical sanity check of the axis expansions (2) and (3) of 3.77 draft v1
from mpmath import mp, mpf, quad, exp, log, sqrt, inf
mp.dps=30
def Gfrom(v,p,K,y):
    # G(y) = K y^p exp(-int_y^inf (1/v - p/t) dt)
    return K*y**p*exp(-quad(lambda t: 1/v(t)-p/t,[y,10*y,100*y,inf]))
# (2): c=3, p=1/3, v = c y + aQ y^p + E(y), E = y^{-eps}
c=mpf(3); p=1/c; D=c-1; K=mpf('1.3'); Q=mpf('0.7'); eps=mpf('0.4'); aQ=Q/(p*(1-p))
v=lambda t: c*t+aQ*t**p+t**(-eps)
A2=K*Q/((1-p)*D)
for y in [mpf(10)**3,mpf(10)**5,mpf(10)**7]:
    G=Gfrom(v,p,K,y); print('c=3', y, (G-K*y**p-A2*y**(2*p-1))/y**(p-1))
# (3): c=2, v = 2y + 4Q sqrt y + C0 + y^{e}, e=-0.3
c=mpf(2); p=mpf(1)/2; C0=mpf('0.9'); e=mpf('-0.3')
v=lambda t: 2*t+4*Q*sqrt(t)+C0+t**e
for y in [mpf(10)**3,mpf(10)**5,mpf(10)**7]:
    G=Gfrom(v,p,K,y); print('c=2', y, (G-K*sqrt(y)-2*K*Q)/y**(-p), 'target', K*C0/4)

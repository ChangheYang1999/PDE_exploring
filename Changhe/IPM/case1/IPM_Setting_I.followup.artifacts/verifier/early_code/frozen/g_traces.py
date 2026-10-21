# Request (o3) item 2: odd-j axis traces G_j(s) = coefficient of y^j in v(s, .) for the even imaginary packet
# Phi = i(beta1 - beta2) (as in g3_even.py), in cases where g* < j - 1 so G_j is unbounded:
#   G_j(s) = c_j int phi(t) int_0^inf eta^(j-2) (1+t^2 eta^q)^-b cos(s t eta^A) d eta dt,  c_j = -(1/pi^2)(-1)^((j-1)/2)/j!
# Prediction (leading, mu_j = (1+g-j)/A in (-1,0)):  G_j(s) ~ Kj |s|^mu_j,
#   Kj = c_j (1/A) Gamma(a) cos(pi a/2) int phi t^(-2b+mu_j) dt,  a = -mu_j.
# Check |s|^((j-1)/A) G_j(s) -> 0 (fred17 02_axis (20)) and the leading coefficient.
import sys, json, numpy as np, mpmath as mp
from scipy import integrate
sys.path.insert(0, 'code/frozen')
from g3_axis import _panels, _GX, _GW
from g3_even import alt_tail_cos, tn, tw, ph

def Jj(c, t, A, g, j):
    b = g/(2*(A-1)); e = (2*A-2)/A; lc = np.log(c); al = (j-1)/A
    def h(u):
        u = np.atleast_1d(np.asarray(u, float))
        return (1/A)*c**(-al)*u**(al-1)*np.exp(-b*np.log1p(np.exp(2*np.log(t)+e*(np.log(u)-lc))))
    lo = 1e-12*min(c, 1.0)
    head = (1/A)*c**(-al)*lo**al/al          # int_0^lo h(u) cos u du, h = leading power there (u/c <= 1e-12)
    e1 = list(np.geomspace(lo, 1.0, int(8*np.log10(1/lo))+2))
    U1 = 40.5*np.pi
    e2 = list(np.arange(1, 81)*(np.pi/2)) + [U1]
    edges = sorted(set(e1 + [c*f for f in (0.3, 1, 3) if lo < c*f < 1] + [z for z in e2 if 1.0 < z <= U1]))
    xx, ww = _panels(edges)
    return head + np.sum(ww*h(xx)*np.cos(xx)) + alt_tail_cos(h, U1)

if __name__ == '__main__':
    out = []
    for (A, g, j) in [(3.0, 3.5, 5), (3.0, 3.5, 7), (2.0, 1.0, 3), (3.0, 3.5, 3)]:
        b = g/(2*(A-1)); mu = (1+g-j)/A; a = -mu
        cj = -(1/np.pi**2)*(-1)**((j-1)//2)/float(mp.factorial(j))
        Kj = cj*(1/A)*float(mp.gamma(a)*mp.cos(mp.pi*a/2))*np.sum(tw*ph*tn**(-2*b+mu))
        print('A=%g g=%g j=%d  mu_j=%.6f  Kj pred %.10e' % (A, g, j, mu, Kj), flush=True)
        rows = []
        for s in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-8]:
            G = cj*np.sum(tw*ph*np.array([Jj(s*tt, tt, A, g, j) for tt in tn]))
            rows.append(dict(s=s, G=G, ratio=G/s**mu, normalized=s**((j-1)/A)*G))
            print('   s=%.0e  G_j=%.10e  G_j/s^mu = %.10e  |s|^((j-1)/A) G_j = %.3e' % (s, G, G/s**mu, s**((j-1)/A)*G), flush=True)
        out.append(dict(A=A, g=g, j=j, mu=mu, Kj=Kj, rows=rows))
    json.dump(out, open('runs/frozen_g_traces.json', 'w'), indent=1)

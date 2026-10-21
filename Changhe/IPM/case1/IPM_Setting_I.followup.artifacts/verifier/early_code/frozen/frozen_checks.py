# Request (o2), part 2: L_g v = 0 at points (finite differences for D, Fourier quadrature for U2), smoothness on
# circles (spectrum of v(r cos th, r sin th)), and quasi-homogeneity at A = 3 (direct subtraction of the Taylor terms
# of quasi-degree < 1+g, coefficients by Beta integrals) against u_0 from the finite-part leading-symbol integral.
import sys, json, time, numpy as np, mpmath as mp
sys.path.insert(0, 'code/frozen')
import vpacket as V
from math import factorial

def taylor_coef(A, g, j, k):
    b = g/(2*(A-1)); m = A*j+k-2; q = (m+1)/(2*A-2)
    x, w = np.polynomial.legendre.leggauss(200); t = 0.5*x+1.5; w = 0.5*w
    ph = np.exp(-1/((t-1)*(2-t)))
    M = np.sum(w*ph*t**j*t**(-(m+1)/(A-1)))/(2*A-2)
    B = float(mp.gamma(q)*mp.gamma(b-q)/mp.gamma(b))
    return -(1/np.pi**2)*(-1)**((j+k)//2-1)/(factorial(j)*factorial(k))*M*B

def Lg(P, gL, s, y, h):
    A = P.A
    vs = []
    for k in (-2, -1, 1, 2):
        vk, _, _ = P.eval(s+k*h, [y]); vs.append(vk[0])
    v5, U5, _ = P.eval(s, [y-2*h, y-h, y, y+h, y+2*h])
    v0, U0 = v5[2], U5[2]
    ds = (vs[0] - 8*vs[1] + 8*vs[2] - vs[3])/(12*h)
    dy = (v5[0] - 8*v5[1] + 8*v5[3] - v5[4])/(12*h)
    terms = np.array([A*s*ds, y*dy, -v0, gL*U0])
    return terms.sum(), np.abs(terms).sum(), v0, U0

out = {}
t0 = time.time()
# 1. L_g at points
pts = [(0.5, 0.3), (-0.7, 0.8), (0.05, 1.0), (1.2, 0.1), (0.3, 2.0), (-0.02, 0.4)]
out['Lg'] = []
for (A, g) in [(3.0, 5.5), (3.0, 5.0), (3.0, 3.5), (10.15, 29.75)]:
    P = V.Packet(A, g)
    Pc = V.Packet(A, g*1.01)        # control: symbol exponent b of g*1.01, equation with g
    for (s, y) in pts:
        rows = {}
        for h in (2e-3, 1e-3):
            r, sc, v0, U0 = Lg(P, g, s, y, h)
            rows['h%.0e' % h] = dict(Lg=r, scale=sc, rel=r/sc)
        rc, scc, _, _ = Lg(Pc, g, s, y, 1e-3)
        rows['control_b(1.01g)'] = dict(Lg=rc, scale=scc, rel=rc/scc)
        rows.update(A=A, g=g, s=s, y=y, v=v0, U2=U0)
        out['Lg'].append(rows)
        print('Lg A=%g g=%g (s,y)=(%g,%g) v=%.6e  rel(h=2e-3)=%.2e rel(h=1e-3)=%.2e  control rel=%.2e' %
              (A, g, s, y, v0, rows['h2e-03']['rel'], rows['h1e-03']['rel'], rows['control_b(1.01g)']['rel']), flush=True)
print('time', time.time()-t0, flush=True)

# 2. circles
out['circle'] = []
N = 128
for (A, g) in [(3.0, 5.5), (10.15, 29.75), (3.0, 3.5)]:
    P = V.Packet(A, g)
    for r in (1.0, 0.3):
        th = (np.arange(N)+0.5)*np.pi/(2*N)
        f = np.array([P.eval(r*np.cos(a), [r*np.sin(a)])[0][0] for a in th])
        # extend: f(pi - th) = -f(th), f(-th) = -f(th); full grid th_j = (j+1/2) pi/(2N), j = 0..4N-1
        q1 = f; q2 = -f[::-1]; q3 = f; q4 = -f[::-1]
        full = np.concatenate([q1, q2, q3, q4])
        c = np.abs(np.fft.rfft(full))/len(full)
        mx = c.max()
        dec = [float(c[k]/mx) for k in (2, 6, 10, 20, 30, 40, 60, 80, 100, 140, 200, 255)]
        out['circle'].append(dict(A=A, g=g, r=r, max_abs_v=float(np.abs(f).max()), spec_k=[2, 6, 10, 20, 30, 40, 60, 80, 100, 140, 200, 255], spec_rel=dec))
        print('circle A=%g g=%g r=%g max|v|=%.3e  |c_k|/max at k=2,6,10,20,30,40,60,80,100,140,200,255:' % (A, g, r, np.abs(f).max()),
              ' '.join('%.1e' % d for d in dec), flush=True)
print('time', time.time()-t0, flush=True)

# 3. quasi-homogeneity at A = 3, g = 5.5 (and the resonant g = 5)
def u0(A, g, s, y, Tterms):
    # -(1/pi^2) int phi t^-2b int_0^inf eta^(-2-g) [sin(s t eta^A) sin(y eta) - T] d eta dt  (finite part)
    b = g/(2*(A-1))
    x, w = np.polynomial.legendre.leggauss(16)
    tt, tw = V.comp_gl(np.linspace(1, 2, 401)); ph = np.exp(-1/((tt-1)*(2-tt)))*tt**(-2*b)*tw
    # eta in (0,1]: geometric panels, series-safe f - T
    e1 = np.concatenate([[0.0], np.geomspace(1e-6, 1, 120)])
    ex, ew = V.comp_gl(e1)
    St = s*tt[None, :]*ex[:, None]**A; Y = y*ex[:, None]
    def sinm(x, n):   # sin x minus its Taylor polynomial through degree n-2 (n odd = first kept degree), by series
        out = np.zeros_like(x); term = None
        for kk in range(n, n+60, 2):
            out = out + (-1)**((kk-1)//2)*x**kk/factorial(kk)
        return out
    if Tterms == 'g55':     # T = (st eta^A)(y eta - (y eta)^3/6)
        fT = sinm(St, 3)*np.sin(Y) + St*sinm(Y, 5)
    else:                   # resonant g = 5: only T = (st eta^A)(y eta); the s y^3 term is kept (log divergence cut at 1e-6)
        fT = sinm(St, 3)*np.sin(Y) + St*sinm(Y, 3)
    inner = np.sum((ew*ex**(-2-g))[:, None]*fT, axis=0)
    # eta > 1: plain f, cut where s eta^A > OMC
    ee = (V.OMC/abs(s))**(1/A)
    e2 = np.arange(1.0, ee+1e-12, 0.01); e2[-1] = ee
    ex2, ew2 = V.comp_gl(e2)
    f2 = np.sin(s*tt[None, :]*ex2[:, None]**A)*np.sin(y*ex2)[:, None]
    outer = np.sum((ew2*ex2**(-2-g))[:, None]*f2, axis=0)
    # minus int_1^inf eta^(-2-g) T
    if Tterms == 'g55':
        Tint = s*tt*(y/(g+1-(A+1)) - y**3/6/(g+1-(A+3)))
    else:
        Tint = s*tt*(y/(g+1-(A+1)))
    return float(-(1/np.pi**2)*np.sum(ph*(inner+outer-Tint)))

out['scaling'] = []
for (A, g, tag) in [(3.0, 5.5, 'g55')]:
    P = V.Packet(A, g)
    a11 = taylor_coef(A, g, 1, 1); a13 = taylor_coef(A, g, 1, 3)
    for (s, y) in [(0.5, 0.5), (-0.3, 1.0), (1.0, 0.2)]:
        U0v = u0(A, g, s, y, tag)
        rows = []
        for k in range(0, 9):
            mu = 2.0**(-k)
            vv = P.eval(mu**A*s, [mu*y])[0][0]
            Vm = (vv - a11*mu**(A+1)*s*y - a13*mu**(A+3)*s*y**3)/mu**(1+g)
            rows.append(dict(mu=mu, V=Vm, dev=Vm-U0v))
        out['scaling'].append(dict(A=A, g=g, s=s, y=y, a11=a11, a13=a13, u0=U0v, rows=rows))
        print('scaling A=%g g=%g (s,y)=(%g,%g) a11=%.8e a13=%.8e u0=%.10e' % (A, g, s, y, a11, a13, U0v))
        for rr in rows:
            print('   mu=%.5f  V=%.10e  V-u0=%.3e' % (rr['mu'], rr['V'], rr['dev']), flush=True)
json.dump(out, open('runs/frozen_checks.json', 'w'), indent=1)
print('time', time.time()-t0)

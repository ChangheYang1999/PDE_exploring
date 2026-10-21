"""Interval Taylor certificate. All mathematical inputs are exact decimal strings.

Run from fred23 with timeout 540, PYTHONDONTWRITEBYTECODE=1, and BLAS/OMP threads=1.
The only transcendental arithmetic is mpmath.iv at 40 decimal places.
Every integrated Taylor remainder is enclosed on its entire real interval.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import resource
resource.setrlimit(resource.RLIMIT_AS, (1_900_000_000, 1_900_000_000))
import json
import sys
import time
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
from mpmath import iv

iv.dps = 40
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/"data/fitted_reference.json"
DATA = json.loads(SOURCE.read_text())
A0 = F(DATA["A0_exact"])
L0 = F(DATA["L0_exact"])
e0 = 1/L0**2
qrat = list(map(F, DATA["q_power_coefficients_exact_decimal"]))


def I(x=0):
    if isinstance(x, F):
        return iv.mpf(x.numerator)/x.denominator
    return iv.mpf(x)


def endpoint(x):
    sign, man, exp, bc = x
    assert bc >= 0, "nonfinite interval endpoint"
    return (-1 if sign else 1)*F(man)*(F(2)**exp)


def bounds(x):
    return tuple(endpoint(t) for t in x._mpi_)


def hull(a, b):
    aa, bb = bounds(a), bounds(b)
    return iv.mpf([I(min(aa[0], bb[0])).a, I(max(aa[1], bb[1])).b])


def box(a, b):
    return hull(I(a), I(b))


def absmax(x):
    return max(map(abs, bounds(x)))


def record(x):
    lo, hi = bounds(x)
    return {"lower": str(lo), "upper": str(hi),
            "display": [float(lo), float(hi)]}


class J:
    """Taylor jet; coefficients are intervals, coefficient k = derivative/k!."""
    def __init__(self, v, n=None):
        if isinstance(v, J):
            self.c = v.c[:]
        elif isinstance(v, (list, tuple)):
            self.c = [I(x) for x in v]
        else:
            self.c = [I(v)] + [I(0)]*n
        self.n = len(self.c)-1

    @classmethod
    def var(cls, v, n):
        a = cls(v, n)
        a.c[1] = I(1)
        return a

    def coerce(self, x):
        return x if isinstance(x, J) else J(x, self.n)

    def __add__(self, x):
        x = self.coerce(x)
        return J([a+b for a, b in zip(self.c, x.c)])

    __radd__ = __add__

    def __neg__(self):
        return J([-a for a in self.c])

    def __sub__(self, x):
        return self + (-self.coerce(x))

    def __rsub__(self, x):
        return self.coerce(x) + (-self)

    def __mul__(self, x):
        x = self.coerce(x)
        return J([sum((self.c[k]*x.c[m-k] for k in range(m+1)), I(0))
                  for m in range(self.n+1)])

    __rmul__ = __mul__

    def inv(self):
        lo, hi = bounds(self.c[0])
        assert lo > 0 or hi < 0, f"division through zero: {self.c[0]}"
        a = [1/self.c[0]]
        for m in range(1, self.n+1):
            a.append(-sum((self.c[k]*a[m-k] for k in range(1, m+1)), I(0))/self.c[0])
        return J(a)

    def __truediv__(self, x):
        return self*self.coerce(x).inv()

    def __rtruediv__(self, x):
        return self.coerce(x)*self.inv()

    def __pow__(self, n):
        if isinstance(n, int):
            if n < 0:
                return self.inv()**(-n)
            out, base = J(1, self.n), self
            while n:
                if n % 2:
                    out = out*base
                base = base*base
                n //= 2
            return out
        return (self.log()*n).exp()

    def diff(self):
        return J([(k+1)*self.c[k+1] for k in range(self.n)]+[I(0)])

    def integ(self, c=0):
        return J([I(c)]+[self.c[k-1]/k for k in range(1, self.n+1)])

    def exp(self):
        a = [iv.exp(self.c[0])]
        for m in range(1, self.n+1):
            a.append(sum((k*self.c[k]*a[m-k] for k in range(1, m+1)), I(0))/m)
        return J(a)

    def log(self):
        assert bounds(self.c[0])[0] > 0
        return (self.diff()/self).integ(iv.log(self.c[0]))


SHIFT_CACHE = {}


def poly(p, x):
    # Exact translation prevents dependency inflation from large alternating
    # monomial coefficients near t=1. It does not approximate the polynomial.
    lo, hi = bounds(x.c[0])
    c = F(round(64*(lo+hi)),128)
    key = tuple(p), c
    if key not in SHIFT_CACHE:
        SHIFT_CACHE[key] = [
            sum(p[m]*comb(m,k)*c**(m-k) for m in range(k,len(p)))
            for k in range(len(p))]
    coeff = SHIFT_CACHE[key]
    xx = x-c
    out = J(0, x.n)
    for cc in coeff[::-1]:
        out = out*xx + cc
    return out


q = list(qrat)
qp = [k*q[k] for k in range(1, len(q))]
H = [A0]+[F(0)]*(len(q)+2)
for k, c in enumerate(q):
    H[k+1] -= c
    H[k+3] += c
Hp = [k*H[k] for k in range(1, len(H))]
# w/u=-A(1-t)/(1+t) + t(1-t)^2 q(t).
# Polynomial piece p(u)=u^3(1-u^2)^2q(u^2).
p = [F(0)]*(2*len(q)+6)
for k, c in enumerate(q):
    for off, mult in ((3, 1), (5, -2), (7, 1)):
        p[2*k+off] += mult*c
pp = [k*(k-1)*p[k] for k in range(2, len(p))]
ppp = [k*(k-1)*(k-2)*p[k] for k in range(3, len(p))]
# pp/u as a polynomial in t.
Jpoly = [F(0)]*((len(pp)+1)//2)
for k, c in enumerate(pp):
    if k % 2:
        Jpoly[(k-1)//2] = -c/A0
    else:
        assert c == 0


def bernstein(p, a, b):
    n = len(p)-1
    c = [sum(p[m]*comb(m,k)*a**(m-k)*(b-a)**k for m in range(k,n+1))
         for k in range(n+1)]
    z = [sum(c[k]*F(comb(j,k),comb(n,k)) for k in range(j+1)) for j in range(n+1)]
    return min(z), max(z)


def poly_bounds(p, a=F(0), b=F(1), panels=128):
    vals = [bernstein(p, a+(b-a)*F(i,panels), a+(b-a)*F(i+1,panels))
            for i in range(panels)]
    return min(v[0] for v in vals), max(v[1] for v in vals)


def Fprime(x):
    return (1+x)**2*poly(q,x)/(2*poly(H,x))


def tint(p, rad):
    return sum((p.c[k]*I(2*rad**(k+1)/F(k+1))
                for k in range(0, p.n, 2)), I(0))


class Reconstruction:
    def __init__(self, panels=64, order=10):
        self.panels, self.order = panels, order
        self.pref = [I(0)]
        self.cache = {F(0): I(0)}
        for i in range(panels):
            a, b = F(i,panels), F(i+1,panels)
            self.pref.append(self.pref[-1]+self.integrate(a,b))
            self.cache[b] = self.pref[-1]
        self.T1 = self.pref[-1]

    def integrate(self, a, b):
        if a == b:
            return I(0)
        c, d = (a+b)/2, (b-a)/2
        pt = Fprime(J.var(c,self.order))
        ran = Fprime(J.var(box(a,b),self.order))
        return tint(pt,d)+ran.c[self.order]*I(2*d**(self.order+1)/F(self.order+1))

    def point(self, t):
        t = F(t)
        if t not in self.cache:
            k = min(int(t*self.panels), self.panels-1)
            self.cache[t] = self.pref[k]+self.integrate(F(k,self.panels),t)
        return self.cache[t]

    def enclosure(self, a, b):
        # q<0 and H>0 were certified by exact Bernstein arithmetic.
        return hull(self.point(a),self.point(b))

    def tjet(self, x, at):
        return Fprime(x).integ(at)

    def ujet(self, u, at):
        return (2*u*Fprime(u*u)).integ(at)


def origin(x, beta, tj):
    z = (1-x)*poly(H,x)/(A0*(1+x))
    # D=2t dz/dt and J0=-w''/(A0*u), evaluated without differentiation loss.
    Dz = 2*x*((-2*poly(H,x)/(1+x)**2)+(1-x)*poly(Hp,x)/(1+x))/A0
    Jz = -4*(3-x)/(1+x)**3+poly(Jpoly,x)
    E = -(1-x).log()+tj
    Fg = z**(-4)*(E*(-(beta+1))).exp()*(1+z+Dz)/2
    Fw = z**(-4)*(E*(-(beta+2))).exp()*Jz/2
    V = z.inv()*(E*(1-beta)).exp()
    return [[f, -E*f, E*E*f] for f in (Fg,Fw)], [V,E*V,E*E*V]


def ufunctions(u, tj):
    t = u*u
    h = poly(H,t)
    g = t*h/(A0*(1+t))*tj.exp()
    k = 2/u+2*u*(poly(Hp,t)/h-1/(1+t)+Fprime(t))
    w2 = 4*A0*u*(3-t)/(1+t)**3+poly(pp,u)
    a = u*(1+u)*h/(1+t)
    Qg = k/(2*g*g)
    Qw = -w2/(2*A0*g**3)
    return g, a, Qg, Qw


def moments(rad, den, sign):
    """Integral r^den/den and its first two beta derivatives; den'=sign."""
    rr = I(rad)
    ll = iv.log(rr)
    value = iv.exp(den*ll)/den
    a = sign*(ll-1/den)
    return [value, value*a, value*(a*a+1/(den*den))]


def origin_integrals(rec, beta, Q1, order=12, uc=F(1,4)):
    R = uc*uc
    xp = J.var(0,order)
    xr = J.var(box(0,R),order)
    fp, vp = origin(xp,beta,rec.tjet(xp,I(0)))
    fr, vr = origin(xr,beta,rec.tjet(xr,rec.enclosure(0,R)))
    result = [[I(0)]*3 for _ in range(2)]
    for i in range(2):
        for j in range(3):
            val = I(0)
            for kk in range(order+1):
                ff = fp[i] if kk < order else fr[i]
                vv = vp if kk < order else vr
                m1 = moments(uc,I(2*kk-4)-beta,-1)
                m2 = moments(uc,I(2*kk+1)-beta,-1)
                for l in range(j+1):
                    val += comb(j,l)*(ff[l].c[kk]*m1[j-l]-Q1[i]*vv[l].c[kk]*m2[j-l])
            result[i][j] = val
    return result


def source_smooth(rec, beta, a, b, order, point=False):
    """Jets in s=1-u, including divided difference and its derivative bounds."""
    u = J.var(I(a) if point else box(a,b),order+1)
    ta = rec.point(a*a) if point else rec.enclosure(a*a,b*b)
    g, aa, qg, qw = ufunctions(u,rec.ujet(u,ta))
    # Replace u derivatives by s derivatives.
    def reflect(v):
        return J([(-1)**k*v.c[k] for k in range(order+1)])
    g, aa = reflect(g), reflect(aa)
    weight = ((aa/A0).log()*(beta-2)+g.log()*(1-beta)).exp()
    logn = (aa/(A0*g)).log()
    ans = []
    for qq in (qg,qw):
        quotient = J([(-1)**(k+1)*qq.c[k+1] for k in range(order+1)])
        ff = quotient*weight
        ans.append([ff,ff*logn,ff*logn*logn])
    return ans


def source_integrals(rec,beta,order=10,de=F(1,16)):
    pt = source_smooth(rec,beta,F(1),F(1),order,True)
    ran = source_smooth(rec,beta,1-de,F(1),order,False)
    result = [[I(0)]*3 for _ in range(2)]
    for i in range(2):
        for j in range(3):
            for k in range(order+1):
                ff = pt[i] if k < order else ran[i]
                mm = moments(de,I(k)+beta,1)
                for l in range(j+1):
                    result[i][j] += comb(j,l)*ff[l].c[k]*mm[j-l]
    return result


def middle_functions(rec,beta,Q1,a,b,order,point=False):
    u = J.var(I(a) if point else box(a,b),order)
    tt = rec.point(a*a) if point else rec.enclosure(a*a,b*b)
    g, aa, qg, qw = ufunctions(u,rec.ujet(u,tt))
    n = (1-u)*aa/(A0*g)
    logn = n.log()
    weight = (logn*(beta-2)).exp()/g
    ans = []
    for i,qq in enumerate((qg,qw)):
        ff = (qq-Q1[i])*weight
        ans.append([ff,ff*logn,ff*logn*logn])
    return ans


def middle_integrals(rec,beta,Q1,panels=88,order=8,uc=F(1,4),de=F(1,16)):
    result = [[I(0)]*3 for _ in range(2)]
    for p in range(panels):
        a = uc+(1-de-uc)*F(p,panels)
        b = uc+(1-de-uc)*F(p+1,panels)
        c,d = (a+b)/2,(b-a)/2
        pt = middle_functions(rec,beta,Q1,c,c,order,True)
        ran = middle_functions(rec,beta,Q1,a,b,order,False)
        for i in range(2):
            for j in range(3):
                result[i][j] += tint(pt[i][j],d)+ran[i][j].c[order]*I(2*d**(order+1)/F(order+1))
    return result


def integral_certificate(rec,beta):
    at1 = J.var(1,1)
    g,a,qg,qw = ufunctions(at1,rec.ujet(at1,rec.T1))
    Q1 = [qg.c[0],qw.c[0]]
    parts = [origin_integrals(rec,beta,Q1),
             middle_integrals(rec,beta,Q1),
             source_integrals(rec,beta)]
    total = [[sum((p[i][j] for p in parts),I(0)) for j in range(3)] for i in range(2)]
    print("integrals",[[record(x)["display"] for x in v] for v in total],flush=True)
    return total, {"parts":[[[record(x) for x in v] for v in p] for p in parts],
                   "total":[[record(x) for x in v] for v in total],
                   "Q1_components":[record(x) for x in Q1]}


def parameters(jj,aa,ee):
    beta = 2/aa
    c = (beta-1)/(3*aa)
    cp = (aa-4)/(3*aa**3)
    cpp = (12-2*aa)/(3*aa**4)
    bp,bpp = -2/aa**2,4/aa**3
    j = [jj[0][k]+ee*aa*jj[1][k] for k in range(3)]
    jw = jj[1]
    return dict(B=c*j[0],
                BA=cp*j[0]+c*(ee*jw[0]+bp*j[1]),
                Be=c*aa*jw[0],
                BAA=cpp*j[0]+2*cp*(ee*jw[0]+bp*j[1])
                    +c*(2*ee*bp*jw[1]+bpp*j[1]+bp*bp*j[2]),
                BAe=cp*aa*jw[0]+c*(jw[0]+aa*bp*jw[1]))


def main():
    start=time.time()
    hmin,hmax = poly_bounds(H)
    qmin,qmax = poly_bounds(q)
    assert hmin >= A0 and qmax < 0
    rec = Reconstruction()
    print("geometry",float(hmin),float(hmax),"T1",rec.T1,flush=True)
    jj0, cert0 = integral_certificate(rec,I(2/A0))
    p0 = parameters(jj0,I(A0),I(e0))
    hh,hp = F("0.06"),F("0.0003")
    jjr,certr = integral_certificate(rec,box(2/(A0+hh),2/(A0-hh)))
    pr = parameters(jjr,box(A0-hh,A0+hh),box(e0-hp,e0+hp))
    out = {"arithmetic":"mpmath.iv, 40 decimal places; rigorous Taylor integral remainders",
           "reference":DATA,
           "geometry":{"H_lower":str(hmin),"H_upper":str(hmax),"q_lower":str(qmin),"q_upper":str(qmax)},
           "T1":record(rec.T1),"gstar":record(iv.exp(rec.T1)/2),
           "base":cert0,"parameter_box":certr,
           "values_base":{k:record(v) for k,v in p0.items()},
           "values_box":{k:record(v) for k,v in pr.items()},
           "elapsed_seconds":time.time()-start}
    assert bounds(p0["B"])[0] > F("0.28")
    assert absmax(p0["BA"]) < F("0.1")
    assert absmax(p0["Be"]) < F(30)
    assert absmax(pr["BAA"]) < F(1)
    assert absmax(pr["BAe"]) < F(10)
    (ROOT/"data/obstruction_certificate.json").write_text(json.dumps(out,indent=2)+"\n")
    for tag,pv in (("base",p0),("box",pr)):
        print(tag,{k:record(v)["display"] for k,v in pv.items()},flush=True)
    print("seconds",time.time()-start)


if __name__ == "__main__":
    main()

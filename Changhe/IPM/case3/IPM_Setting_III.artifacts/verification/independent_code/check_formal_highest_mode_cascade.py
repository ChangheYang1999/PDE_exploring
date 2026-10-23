#!/usr/bin/env python3
"""Independent rational Laurent-polynomial checks of the formal top cascade.

No producer or lead code is imported. This is supporting algebra, not an
all-order asymptotic theorem or an IPM existence certificate.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time

started = time.monotonic()
checks = 0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def addz(a, b):
    return (a[0]+b[0], a[1]+b[1])


def mulz(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def clean(a):
    return {k: z for k, z in a.items() if z != (0, 0)}


def add(a, b):
    c = dict(a)
    for k, z in b.items():
        c[k] = addz(c.get(k, (F(0), F(0))), z)
    return clean(c)


def scale(a, s):
    return clean({k: (s*z[0], s*z[1]) for k, z in a.items()})


def mul(a, b):
    c = {}
    for k, z in a.items():
        for l, w in b.items():
            c[k+l] = addz(c.get(k+l, (F(0), F(0))), mulz(z, w))
    return clean(c)


def derivative(a):
    return clean({k: mulz((F(0), F(k)), z) for k, z in a.items()})


def sine(k, c=F(1)):
    return {k: (F(0), -c/2), -k: (F(0), c/2)} if k else {}


def cosine(k):
    return {k: (F(1, 2), F(0)), -k: (F(1, 2), F(0))}


def sine_coefficient(a, k):
    z = a.get(k, (F(0), F(0)))
    check(z[0] == 0, 'coefficient is sine only')
    check(a.get(-k, (F(0), F(0))) == (0, -z[1]), 'real sine parity')
    return -2*z[1]


def degree(k, p):
    return (k+1)*p-k


def frequency(k, n):
    return (k+1)*(n+1)-1


def source(theta, s):
    # Direct Cartesian derivative in polar variables, in Laurent arithmetic.
    return add(scale(mul(cosine(1), theta), s),
               scale(mul(sine(1), derivative(theta)), F(-1)))


def inverse(theta, s):
    f = source(theta, s)
    phi = {}
    for k, z in f.items():
        d = k*k-(s+1)**2
        check(d != 0, 'test mode is nonresonant')
        phi[k] = (z[0]/d, z[1]/d)
    check(add(scale(phi, (s+1)**2), derivative(derivative(phi)))
          == scale(f, F(-1)), 'Poisson angular equation')
    return phi


def transport(phi, si, theta, sj):
    ur = scale(derivative(phi), F(-1))
    ut = scale(phi, si+1)
    return add(scale(mul(ur, theta), sj), mul(ut, derivative(theta)))


def c_formula(i, j, n, p):
    return (1 - F(2)*(j+1)*(n+1)/((i+1)*(n+p)+2))/4


ps = [F(1, 9), F(1, 3), F(2, 5), F(1, 2), F(7, 8), F(999, 1000)]
ns = [1, 3, 5, 9]
sign_rows = []
for p in ps:
    D = 1/p-1
    for n in ns:
        # Full Fourier multiplication, retaining the lower stream harmonic.
        for i in range(8):
            si = degree(i, p)
            ni = frequency(i, n)
            theta_i = sine(ni, F(2*i+3, i+2))
            phi = inverse(theta_i, si)
            top = sine_coefficient(phi, ni+1)
            check(top == -F(2*i+3, i+2)/(2*(ni+si+2)), 'top stream')
            check(ni+1 > abs(si+1), 'top nonresonance')
            for j in range(8):
                sj = degree(j, p)
                nj = frequency(j, n)
                aj = F(3*j-5, j+3)
                out = transport(phi, si, sine(nj, aj), sj)
                actual = sine_coefficient(out, ni+1+nj)
                want = F(2*i+3, i+2)*aj*c_formula(i,j,n,p)
                check(actual == want, 'independent top transport')
                check(max(map(abs, out), default=0) <= ni+1+nj, 'angular bound')
                check(si+sj-1 == degree(i+j+1,p), 'radial matching')
                check(degree(i+j+1,p)/p-1 == -(i+j+1)*D, 'Euler factor')
                u,v=F(i+1),F(j+1)
                S=u+v; B=n+p; A=n+1; t=u*v
                f=v/(u*B+2)+u/(v*B+2)
                rational=(B*(S*S-2*t)+2*S)/(B*B*t+2*B*S+4)
                check(f == rational, 'paired rational expression')
                check(f >= 2*S/(B*S+4), 'balanced pair minimizes')
                check(S*(n+2-p)>4, 'strict sign condition')
                check(c_formula(i,j,n,p)+c_formula(j,i,n,p)<0, 'paired strict sign')
                if i==j:
                    check(c_formula(i,j,n,p)<0, 'diagonal strict sign')
        # Arbitrary lower density modes cannot alter the top interaction.
        for i in range(4):
            ni=frequency(i,n); si=degree(i,p)
            theta={}
            for m in range(1,ni+1,2):
                theta=add(theta,sine(m,F(m+2, m+3)))
            phi=inverse(theta,si)
            for j in range(4):
                nj=frequency(j,n); sj=degree(j,p)
                other={}
                for m in range(1,nj+1,2):
                    other=add(other,sine(m,F(2*m-3,m+2)))
                out=transport(phi,si,other,sj)
                want=F(ni+2,ni+3)*F(2*nj-3,nj+2)*c_formula(i,j,n,p)
                check(sine_coefficient(out,frequency(i+j+1,n))==want,
                      'lower modes do not change top coefficient')
        # Recurrences obtained solely from Laurent transport, two amplitude signs.
        for a in [F(2,3),F(-3,2)]:
            vals=[a]
            for k in range(1,9):
                rhs=F(0)
                for i in range(k):
                    j=k-1-i
                    ni=frequency(i,n); nj=frequency(j,n)
                    si=degree(i,p); sj=degree(j,p)
                    phi=inverse(sine(ni,vals[i]),si)
                    out=transport(phi,si,sine(nj,vals[j]),sj)
                    rhs += sine_coefficient(out,frequency(k,n))
                vals.append(rhs/(k*D))
                b=vals[k]/((-1)**k*a**(k+1))
                check(b>0, 'independently generated coefficient sign')
            check(vals[1]==a*a*(p-n)/(4*D*(n+p+2)), 'first correction')
            sign_rows.append({'p':str(p),'n':n,'a':str(a),'orders':8,
                              'A1':str(vals[1]),'A2':str(vals[2]),
                              'all_normalized_signs_positive':True})

out={'utc':datetime.now(timezone.utc).isoformat(), 'verdict':'PASS',
     'exact_checks':checks,'elapsed_seconds':time.monotonic()-started,
     'method':'Independent exact rational Laurent Fourier differentiation, Poisson inversion and transport products',
     'hierarchies':sign_rows,
     'scope':'Supporting finite algebra checks; all-order formal sign theorem is in PROOF.md. No actual-profile expansion certified.',
     'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
p=Path('research/formal_highest_mode_cascade/verification/CHECK.json')
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='hierarchies'},indent=2))

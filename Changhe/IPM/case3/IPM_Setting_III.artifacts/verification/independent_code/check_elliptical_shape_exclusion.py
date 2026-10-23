"""Exact supporting checks for the separately written elliptical proof.
No solver, network, server, numerical inverse, or producer code is imported.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib


def clean(p):
    return {ij: Q(v) for ij, v in p.items() if v}


def add(*pp):
    p = {}
    for q in pp:
        for ij, v in q.items():
            p[ij] = p.get(ij, Q(0)) + v
    return clean(p)


def scale(p, c):
    return clean({ij: c*v for ij, v in p.items()})


def mul(p, q):
    out = {}
    for (i, j), v in p.items():
        for (k, l), w in q.items():
            ij = (i+k, j+l)
            out[ij] = out.get(ij, Q(0)) + v*w
    return clean(out)


def power(p, n):
    out = {(0, 0): Q(1)}
    for _ in range(n):
        out = mul(out, p)
    return out


def diff(p, axis):
    out = {}
    for ij, v in p.items():
        if ij[axis]:
            jk = list(ij)
            jk[axis] -= 1
            out[tuple(jk)] = ij[axis]*v
    return clean(out)


def lap(p):
    return add(diff(diff(p, 0), 0), diff(diff(p, 1), 1))


def axis(p):
    return clean({ij: v for ij, v in p.items() if ij[1] == 0})


checks = []

def equal(name, left, right, **meta):
    assert left == right, (name, meta, left, right)
    checks.append(dict(name=name, **meta))


x = {(1, 0): Q(1)}
y = {(0, 1): Q(1)}
xy = mul(x, y)
params = [(Q(1), Q(1)), (Q(4), Q(1)), (Q(1), Q(9)),
          (Q(2, 3), Q(7, 4)), (Q(1, 100), Q(100))]
for al, be in params:
    for t in [Q(0), Q(1, 7), Q(2), Q(11)]:
        at, bt = al/(1+al*t), be/(1+be*t)
        s = add(scale(power(x, 2), at), scale(power(y, 2), bt))
        sd = add(scale(power(x, 2), -at*at), scale(power(y, 2), -bt*bt))
        for degree in range(0, 11):
            ff = power(s, degree)
            fp = scale(power(s, degree-1), degree) if degree else {}
            fpp = scale(power(s, degree-2), degree*(degree-1)) if degree>=2 else {}
            rhs = scale(mul(xy, add(mul(fpp, sd), scale(fp, -Q(3, 2)*(at+bt)))), -4)
            equal('Cartesian Laplacian versus t derivative', lap(mul(xy, ff)), rhs,
                  alpha=str(al), beta=str(be), t=str(t), degree=degree)
    for u in [Q(0), Q(1, 100), Q(1, 4), Q(1, 2), Q(1)]:
        hh = be+(al-be)*u
        # Multiply mu-2(u mu)' by h^(5/2)/sqrt(alpha).
        lhs = -3*u*hh+3*(al-be)*u*u
        equal('Volterra weight derivative with radicals cancelled', lhs, -3*be*u,
              alpha=str(al), beta=str(be), u=str(u))

for al, be in params:
    for degree in range(1, 9):
        ell = Q(degree+3, degree+1)
        aa = Q(7+degree, 3)
        kk, dd = aa*al/2, ell-1
        z = scale(power(x, 2), al)
        s = add(z, scale(power(y, 2), be))
        fc = [Q(1)] + [Q((-1)**j*(j+1), j+3) for j in range(1, degree+1)]
        jc = [dd/kk] + [Q(j+2, 2*j+5) for j in range(1, degree+1)]
        fxy = add(*(scale(power(s, j), c) for j,c in enumerate(fc)))
        fz = add(*(scale(power(z, j), c) for j,c in enumerate(fc)))
        fzp = add(*(scale(power(z, j-1), j*c) for j,c in enumerate(fc) if j))
        jj = add(*(scale(power(z, j), c) for j,c in enumerate(jc)))
        jp = add(*(scale(power(z, j-1), j*c) for j,c in enumerate(jc) if j))
        rho = scale(mul(y, fxy), aa)
        psi = add(scale(mul(xy, jj), -kk), scale(mul(power(x, 3), power(y, 3)), Q(3, 7)))
        u1, u2 = scale(diff(psi, 1), -1), diff(psi, 0)
        w1, w2 = add(scale(x, ell), u1), add(scale(y, ell), u2)
        rr = add(mul(w1, diff(rho, 0)), mul(w2, diff(rho, 1)), scale(rho, -1))
        direct = scale(axis(diff(rr, 1)), 1/aa)
        expected = add(scale(mul(mul(z, add({(0,0):ell}, scale(jj, kk))), fzp), 2),
                       mul(add({(0,0):dd}, scale(jj,-kk), scale(mul(z,jp),-2*kk)), fz))
        equal('full Cartesian transport derivative versus axis equation', direct, expected,
              alpha=str(al), beta=str(be), degree=degree)

for degree in range(1, 101):
    for dd in [Q(1, 100), Q(1, 3), Q(1), Q(10), Q(1000)]:
        aa = 2*dd+1
        gap = 2*degree*aa-dd*(2*degree+1)
        equal('strict jet gap', gap, (2*degree-1)*dd+2*degree,
              degree=degree, D=str(dd))
        assert gap > 0
    # Isotropic moment integral directly integrates u^(degree+1).
    for al in [Q(1, 10), Q(1), Q(7)]:
        moment = 1/(al*(degree+2))
        total = 1/(2*al)
        assert 0 < moment < total
        equal('isotropic moment ratio', moment/total, Q(2, degree+2),
              alpha=str(al), degree=degree)

for p,q in [(Q(1),Q(2)),(Q(2),Q(3)),(Q(1,10),Q(5)),(Q(7),Q(1))]:
    al,be = p*p,q*q
    direct = 2*p/((al-be)**2)*((p+be/p)-2*q)
    equal('elliptical center moment elementary antiderivative', direct, 2/(p+q)**2,
          sqrt_alpha=str(p), sqrt_beta=str(q))

root = Path(__file__).resolve().parent.parent
sources = [root/'research/elliptical_shape_exclusion/PROOF.md', Path(__file__).resolve()]
record = dict(utc=datetime.now(timezone.utc).isoformat(), verdict='PASS', count=len(checks),
              checks=checks, hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
              scope='Exact supporting algebra. Flat uniqueness is proved analytically, not established by sampling.')
out = root/'research/elliptical_shape_exclusion/verification/checks.json'
out.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({k:record[k] for k in ['utc','verdict','count']}))

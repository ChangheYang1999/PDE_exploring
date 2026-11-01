"""Exact low-order Cartesian comparison for the new product decomposition."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import factorial
import json, time, sys
sys.dont_write_bytecode = True
from flint import arb, arb_poly, ctx
from laurent_log_audit import L, Q, Poly, parse
from maximal_log_cartesian_check import poisson
from factorial_product_audit import angular, exact_contains

ROOT = Path('research/78_factorial_product_losses')
ctx.prec = 640
start = time.monotonic()
F, G, checks = {}, {}, []
N = 30


def positive(A):
    return L(A.q, A.M, [Poly([])]+A.a[1:]) if A.a else A


def cols(A, even):
    return [[2*row[A.M+m] for m in range(0 if even else 1, A.M+1, 2)] for row in A.a]


def exact_norm(A):
    return sum((Q(factorial(q))*sum((2*abs(row[A.M+m]) for m in range(1, A.M+1)), Q(0))
                for q, row in enumerate(A.a)), Q(0))


for n in range(1, N+1):
    p = Q(1)-Q(2*n, 3)
    if n == 1:
        F[n] = parse(p, {1:[Q(1)]})
        G[n] = poisson(F[n])
        continue
    S, PP = L(p, 0, []), L(p, 0, [])
    out, pp = [arb_poly([]) for _ in range(n//3+2)], [arb_poly([]) for _ in range(n//3+2)]
    den, pden = Q(0), Q(0)
    for i in range(1, n):
        j = n-i
        Gi, Fj = G[i], F[j]
        S += Gi.X()*Fj.Y()-Gi.Y()*Fj.X()
        gp, fp = positive(Gi), positive(Fj)
        PP += gp.X()*fp.Y()-gp.Y()*fp.X()
        w = 2*j*(abs(Gi.q)+1)+2*i*(abs(Fj.q)+1)
        den += w*exact_norm(Gi)*exact_norm(Fj)
        pden += w*exact_norm(gp)*exact_norm(fp)
        for u, gc in enumerate(cols(Gi, True)):
            Ag, Cg = angular([arb(z) for z in gc], 2*i, True)
            for v, fc in enumerate(cols(Fj, False)):
                Af, Cf = angular([arb(z) for z in fc], 2*j-1, False)
                X, Y = Ag*Cf, Cg*Af
                top, low = arb(Gi.q)*X-arb(Fj.q)*Y, u*X-v*Y
                out[u+v] += top
                if u+v:
                    out[u+v-1] += low
                if u and v:
                    pp[u+v] += top
                    pp[u+v-1] += low
    count = 0
    for actual, expected in [(out,S), (pp,PP)]:
        for q, row in enumerate(actual):
            for m in range(1, 2*n, 2):
                z = 2*expected.a[q][expected.M+m] if q < len(expected.a) and m <= expected.M else Q(0)
                assert exact_contains(2*row[2*n-1+m], z), (n,q,m)
                count += 1
    assert not PP.a or not PP.a[0]
    term = S.scale(Q(1,2*(n-1)))
    F[n] = term
    while term.a:
        term = term.dt().scale(Q(3,2*(n-1)))
        F[n] += term
    assert (F[n].scale(2*(n-1))-F[n].dt().scale(3)-S).zero()
    G[n] = poisson(F[n])
    row = dict(n=n, exact_cartesian_checks=count, full_norm=str(exact_norm(S)), denominator=str(den),
        rho=arb(exact_norm(S)/den).str(30, radius=True),
        positive_rho=arb(exact_norm(PP)/pden).str(30, radius=True) if pden else None)
    checks.append(row)
    if n % 10 == 0:
        print(json.dumps(dict(n=n, checks=count, rho=row['rho'], positive_rho=row['positive_rho'],
                             elapsed_s=time.monotonic()-start)), flush=True)
result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),
    N=N, delta='2/3', input='sin(theta)', source_sha256={}, checks=checks,
    coefficient_checks=sum(r['exact_cartesian_checks'] for r in checks),
    actual_elapsed_s=time.monotonic()-start)
for name in ['factorial_product_exact_check.py', 'maximal_log_cartesian_check.py']:
    raw = Path('code', name).read_bytes()
    (ROOT/'sources'/(name+'.txt')).write_bytes(raw)
    result['source_sha256'][name] = sha256(raw).hexdigest()
(ROOT/'verification/exact_prefix.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(dict(all_pass=True, coefficient_checks=result['coefficient_checks'],
                      actual_elapsed_s=result['actual_elapsed_s'])), flush=True)

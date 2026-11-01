"""Finite tests for the fixed-edge top constant, including the central-pair correction."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, time, sys
sys.dont_write_bytecode = True
from gmpy2 import mpq as Q
from flint import arb, fmpq, ctx
ctx.prec = 512
start = time.monotonic()
N = 2048
source = sorted(Path('research/113_edge_top_radii/verification').glob('*/checks.json'))[-1]
raw = source.read_bytes()
data = json.loads(raw)
assert data['all_checks_pass']
reference = Path('research/102_edge_recurrence_reference/verification/exact_reference.json')
ref = json.loads(reference.read_text())['variants']
ball = lambda x: arb(fmpq(str(x)))
text = lambda x: x.str(36, radius=True)
counts = dict(positive_tail_coefficients=0, positive_generated_coefficients=0,
              exact_gamma_product_checks=0, cartesian_inclusions=0,
              gamma_formula_intersections=0, first_order_cancellations=0)
cache = {}
rows = []
for row in data['rows']:
    delta = Q(row['delta']); B = row['B']; K = row['K']
    eta = B-delta; d = delta/(1-delta)
    key = (str(delta), B)
    if key not in cache:
        h = [Q(0), Q(1)]
        for n in range(2, 62):
            h.append(sum((Q(2*B*(n-i))/(eta*i+2)-1)*h[i]*h[n-i]
                         for i in range(1, n))/(4*d*(n-1)))
        cache[key] = h
    h = cache[key]
    R = ball(Q(row['R_lower'])).union(ball(Q(row['R_upper'])))
    cc = [Q(B)*h[i]/(2*d*(eta*i+2)) for i in range(1, K+1)]
    pp = [ball(ci)*R**i for i, ci in enumerate(cc, 1)]
    mu = sum((i*p for i, p in enumerate(pp, 1)), arb(0))
    s = 2-ball(delta)/B-arb(B-2)/(B*mu)
    correction = sum((p*(s*i-ball(i-1+(eta*i+2)/B))
                      for i, p in enumerate(pp, 1)), arb(0))
    assert correction.contains(0)
    counts['first_order_cancellations'] += 1
    g = [arb(0)] + [ball(h[n])*R**n for n in range(1, 2*K+1)]
    exact = [Q(0)] + h[1:2*K+1]
    gamma_product = Q(1)
    if K == 1 and B == 2:
        a = 2/eta; ss = 2-delta/2; RR = d*(4-delta)
        kappa = ball(RR/2)*ball(1+a).gamma()/ball(1+a-ss).gamma()
    selected = []
    for n in range(2, N+1):
        if n > 2*K:
            value = arb(0); ev = Q(0)
            for i in range(1, K+1):
                j = n-i
                q = h[i]*(B*(Q(j)/(eta*i+2)+Q(i)/(eta*j+2))-1)/(2*d*(n-1))
                assert q > 0
                counts['positive_tail_coefficients'] += 1
                value += ball(q)*R**i*g[j]
                if n <= 64: ev += q*exact[j]
            g.append(value)
            if n <= 64: exact.append(ev)
        assert g[n] > 0
        counts['positive_generated_coefficients'] += 1
        if K == 1 and B == 2:
            if n == 2:
                gamma_product = (1+a-ss)/(2*RR*(1+a))
            elif n <= 64:
                gamma_product *= (n-1+a-ss)/(RR*(n-1+a))
            if n <= 64:
                assert gamma_product == exact[n]
                counts['exact_gamma_product_checks'] += 1
        if delta == Q(2,3) and B == 2 and K in [1,3] and n <= 18:
            physical = Q(ref[str(K)]['rows'][n-1]['density']['0'][str(2*n-1)])
            assert (g[n]/R**n).contains(fmpq(str((-1)**(n-1)*physical)))
            counts['cartesian_inclusions'] += 1
        if n in [64,128,256,512,1024,2048]:
            w = g[n]*arb(n)**s
            result = dict(n=n,normalized_coefficient=text(w),
                          consecutive_ratio_times_R=text(g[n]/g[n-1]))
            if K == 1 and B == 2:
                explicit = kappa*ball(n+a-ss).gamma()/ball(n+a).gamma()*arb(n)**ball(ss)
                assert (w-explicit).contains(0)
                counts['gamma_formula_intersections'] += 1
                result.update(exact_limit=text(kappa), ratio_to_limit=text(w/kappa),
                              n_times_relative_error=text(n*(w/kappa-1)))
            selected.append(result)
    rows.append(dict(delta=str(delta),B=B,K=K,maximum_order=N,radius=text(R),
                     exponent=text(s),selected=selected))
    print(json.dumps(dict(delta=str(delta),B=B,K=K,last=selected[-1],
                          actual_elapsed_s=time.monotonic()-start)),flush=True)
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
root = Path('research/117_edge_top_constant/verification')/stamp
(root/'sources').mkdir(parents=True)
result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
              precision_bits=512,maximum_order=N,all_finite_checks_pass=True,
              counts=counts,rows=rows,input_path=str(source),input_sha256=sha256(raw).hexdigest(),
              reference_path=str(reference),reference_sha256=sha256(reference.read_bytes()).hexdigest(),
              actual_elapsed_s=time.monotonic()-start,
              scope='Finite exact and ball comparisons, including the factor1/2 for the first central pair. Infinite asymptotics require independent proof review.')
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
for p in [Path(__file__),Path('research/117_edge_top_constant/PROOF.md')]:
    (root/'sources'/(p.name+'.txt')).write_bytes(p.read_bytes())
manifest = {str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest())
            for p in root.rglob('*') if p.is_file()}
(root/'MANIFEST.json').write_text(json.dumps(dict(files=manifest),indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),counts=counts,
                      actual_elapsed_s=result['actual_elapsed_s'])),flush=True)

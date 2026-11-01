"""Exact global minima from finite gaps and a coefficient-positive rational tail."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from math import comb
import json, sys, time
sys.dont_write_bytecode = True
import sympy as sp
root = Path('research/139_period_five_response_minima')
src = Path('research/130_period_five_tuning/verification')
start = time.monotonic()
b, k = sp.symbols('b k')

def coeff(e):
    p = sp.Poly(e, b, domain=sp.QQ)
    return [F(str(p.nth(j))) for j in range(p.degree()+1)]

def ivmul(a, z):
    values = [x*y for x in a for y in z]
    return min(values), max(values)

def evaluate(a, interval):
    out = (F(0), F(0))
    for c in reversed(a):
        lo, hi = ivmul(out, interval)
        out = lo+c, hi+c
    return out

def absolute(a):
    lo, hi = a
    assert lo > 0 or hi < 0, ('unresolved sign', str(a))
    return (lo, hi) if lo > 0 else (-hi, -lo)

def signed(a, sign):
    return a if sign == 1 else (-a[1], -a[0])

def save(name, data):
    (root/'verification'/name).write_text(json.dumps(data, indent=2)+'\n')

try:
    data = json.loads((src/'symbolic_responses.json').read_text())
    N = sp.Poly(sp.sympify(data['numerator']), k, b, domain=sp.QQ)
    D = sp.Poly(sp.sympify(data['denominator']), k, domain=sp.QQ)
    nd, bd = N.degree(k), N.degree(b)
    mat = [[F(0)]*(bd+1) for _ in range(nd+1)]
    for (j, m), v in N.terms():
        mat[j][m] = F(str(v))
    dc = [F(str(D.nth(j))) for j in range(D.degree()+1)]
    small = {r['k']:coeff(sp.sympify(r['sigma'])) for r in json.loads((src/'small_responses.json').read_text())['rows']}
    limit = coeff(sp.sympify(data['sigma_infinity']))
    rootrows = json.loads((src/'irreducibility_sturm_checks.json').read_text())['real_roots']
    shifts = {}
    def shift(K):
        if K not in shifts:
            nm = [[sum(mat[j][m]*comb(j,t)*K**(j-t) for j in range(t,nd+1)) for m in range(bd+1)] for t in range(nd+1)]
            dd = [sum(dc[j]*comb(j,t)*K**(j-t) for j in range(t,len(dc))) for t in range(len(dc))]
            assert all(c > 0 for c in dd)
            shifts[K] = nm, dd
        return shifts[K]
    def fixed(j):
        if j in small:
            return small[j]
        den = sum(c*j**m for m,c in enumerate(dc))
        assert den > 0
        return [sum(mat[t][m]*j**t for t in range(nd+1))/den for m in range(bd+1)]
    rows = []
    for index, (rr, target_k) in enumerate(zip(rootrows,[5,8,5,6,5,5]),1):
        interval = tuple(map(F, rr['interval']))
        raw_target = evaluate(small[target_k], interval)
        target_sign = 1 if raw_target[0]>0 else -1
        target_poly = [target_sign*c for c in small[target_k]]
        target_iv = evaluate(target_poly, interval)
        assert target_iv[0]>0
        limit_iv = evaluate(limit, interval)
        tail_sign = 1 if limit_iv[0]>0 else -1
        assert absolute(limit_iv)[0] > target_iv[1]
        trials = []
        for K in [11,16,24,32,48,64,96,128,256,512,1024]:
            nm, dd = shift(K)
            bounds = []
            for t, co in enumerate(nm):
                den = dd[t] if t<len(dd) else F(0)
                target_co = [(target_poly[m] if m<len(target_poly) else F(0)) for m in range(bd+1)]
                expression = [tail_sign*co[m]-den*target_co[m] for m in range(bd+1)]
                bounds.append(evaluate(expression, interval))
            trials.append(dict(K=K, negative_or_zero_lower_bounds=sum(lo<=0 for lo,hi in bounds)))
            if all(lo>0 for lo,hi in bounds):
                break
        else:
            raise AssertionError(('no tail certificate', index, trials))
        finite = []
        for j in range(2,K):
            iv = evaluate(fixed(j), interval)
            av = absolute(iv)
            if j != target_k:
                gap = av[0]-target_iv[1]
                assert gap>0, ('nonpositive finite gap', index,j,str(gap))
            else:
                gap = F(0)
            finite.append(dict(k=j,signed_interval=list(map(str,iv)),absolute_interval=list(map(str,av)),gap_lower=str(gap)))
        # Decimal rational at three significant figures, rounded strictly downward.
        power = 0
        while target_iv[0]*10**power < 100:
            power += 1
        scale = 10**power
        simple_lower = F((target_iv[0]*scale).numerator//(target_iv[0]*scale).denominator,scale)
        assert 0 < simple_lower < target_iv[0]
        row = dict(root_index=index,root_interval=rr['interval'],unique_minimizer=target_k,
                   minimum_sign=target_sign,minimum_polynomial_coefficients=list(map(str,target_poly)),
                   minimum_interval=list(map(str,target_iv)),minimum_approx=float(sum(target_iv)/2),
                   simple_uniform_lower_bound=str(simple_lower),tail_from_k=K,tail_sign=tail_sign,
                   finite_checks=finite,tail_trials=trials,
                   tail_polynomial_coefficient_bounds=[list(map(str,x)) for x in bounds],
                   shifted_denominator_coefficients=list(map(str,dd)))
        rows.append(row)
        save('checks.partial.json',dict(rows=rows))
        print(json.dumps(dict(root=index,k=target_k,minimum=row['minimum_approx'],s=str(simple_lower),K=K,elapsed_s=time.monotonic()-start)),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
    save('checks.json',result)
    (root/'sources/period_five_response_minima.py').write_bytes(Path('code/period_five_response_minima.py').read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    save('MANIFEST.json',dict(files=files))
    print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as exc:
    import traceback
    failure=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(frame.filename).name,line=frame.lineno) for frame in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start)
    save('FAILURE.json',failure)
    print(json.dumps(failure),flush=True)
    raise SystemExit(1)

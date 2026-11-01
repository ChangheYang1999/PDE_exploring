"""Rebuild and independently certify the all-index two-coefficient criterion."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
import sympy as sp
root=Path('research/146_four_ninths_profiles');out=root/'verification';start=time.monotonic()
k,b=sp.symbols('k b')
def coeffs(poly,var):
    p=sp.Poly(poly,var,domain=sp.QQ)
    return [F(str(p.nth(j))) for j in range(p.degree()+1)]
def evaluate(a,x):
    y=F(0)
    for v in reversed(a):y=y*x+v
    return y
def shift(a,K):
    return [sum((a[i]*comb(i,j)*K**(i-j) for i in range(j,len(a))),F(0)) for j in range(len(a))]
def rational_parts(expr):
    n,d=sp.fraction(sp.cancel(expr));return coeffs(n,k),coeffs(d,k)
def stringify(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,list):return [stringify(y) for y in x]
    if isinstance(x,dict):return {key:stringify(value) for key,value in x.items()}
    return x
try:
    obstruction_path=Path('research/144_general_rational_response_limit/verification/h2_Q9.json')
    src=json.loads(obstruction_path.read_text());O=coeffs(sp.sympify(src['first_obstruction']),b)
    generic={m:sp.sympify(json.loads((out/('mode'+str(m)+'_generic.json')).read_text())['sigma']) for m in [1,3]}
    small={m:{row['k']:F(row['sigma']) for row in json.loads((out/('mode'+str(m)+'_small.json')).read_text())['rows']} for m in [1,3]}
    comparisons=[]
    for m in [1,3]:
        n,d=rational_parts(generic[m])
        for t in [10,11]:
            assert evaluate(n,t)/evaluate(d,t)==small[m][t]
            comparisons.append(dict(mode=m,k=t,exactly_equal=True))
    expr=sp.cancel(sp.Rational(O[-1].numerator,O[-1].denominator)*generic[1]-sp.Rational(O[0].numerator,O[0].denominator)*generic[3])
    N,D=rational_parts(expr)
    if D[-1]<0:N=[-x for x in N];D=[-x for x in D]
    finite=[]
    for t in range(1,10):
        value=O[-1]*small[1][t]-O[0]*small[3][t]
        assert value
        finite.append(dict(k=t,value=value,sign=1 if value>0 else -1,method='direct folded-carrier Cartesian responses'))
    tail=None;trials=[]
    for K in [10,16,24,32,48,64,96,128,256,512,1024,2048,4096]:
        n,d=shift(N,K),shift(D,K);sn=1 if n[-1]>0 else -1;sd=1 if d[-1]>0 else -1
        ok=all(sn*x>=0 for x in n) and sn*n[0]>0 and all(sd*x>=0 for x in d) and sd*d[0]>0
        trials.append(dict(K=K,passes=bool(ok)))
        if ok:
            tail=dict(K=K,numerator_sign=sn,denominator_sign=sd,
                      numerator_shifted_coefficients_ascending=n,denominator_shifted_coefficients_ascending=d)
            break
    assert tail is not None,'No positive tail certificate found'
    for t in range(10,tail['K']):
        nv,dv=evaluate(N,t),evaluate(D,t);assert nv and dv
        finite.append(dict(k=t,value=nv/dv,sign=1 if nv*dv>0 else -1,method='exact rational Horner evaluation of generic criterion'))
    inputs={str(p):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest())
            for p in [obstruction_path]+[out/('mode'+str(m)+suffix+'.json') for m in [1,3] for suffix in ['_small','_generic']]}
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
                numerator_coefficients_ascending=N,denominator_coefficients_ascending=D,numerator_degree=len(N)-1,denominator_degree=len(D)-1,
                direct_generic_comparisons=comparisons,finite_checks=finite,tail_positive_certificate=tail,tail_trials=trials,
                all_positive_integer_indices_covered=True,inputs=inputs,actual_elapsed_s=time.monotonic()-start,
                scope='Exact nonvanishing of D_k for every integer k>=1. Together with irreducibility and limiting coprimality, every real obstruction root has positive response infimum.')
    (out/'criterion_checks.json').write_text(json.dumps(stringify(result),indent=2)+'\n')
    for name in ['four_ninths_criterion.py','four_ninths_responses.py','tuned_cartesian_exact.py','exact_polynomial_certificates.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    (out/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
    print(json.dumps(dict(all_checks_pass=True,numerator_degree=len(N)-1,denominator_degree=len(D)-1,tail_K=tail['K'],finite_checks=len(finite),actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as exc:
    import traceback
    failure=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start)
    (out/'CRITERION_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)

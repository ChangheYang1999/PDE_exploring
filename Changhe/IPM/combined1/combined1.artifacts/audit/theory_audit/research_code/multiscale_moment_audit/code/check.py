from pathlib import Path
from datetime import datetime, timezone
import sys, json, hashlib, time
import sympy as sp
from flint import arb, ctx, fmpq as Q
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'source/code'))
from moments import integral, ar
ctx.prec=2048
start=time.monotonic()
x=sp.Symbol('x')
def rational(v):
    return ar(Q(str(v)))
def reference(P,factors):
    expression=sum(sp.Rational(p)*x**k for k,p in enumerate(P))
    for a,m in factors:expression/=(1+sp.Rational(a)*x)**m
    partial=sp.apart(expression,x)
    assert sp.cancel(partial-expression)==0
    answer=arb(0)
    for term in sp.Add.make_args(partial):
        num,den=sp.fraction(term)
        if not den.has(x):
            poly=sp.Poly(term,x)
            answer+=sum((rational(c)/int(k[0]+1) for k,c in poly.terms()),arb(0))
            continue
        coeff, facs=sp.factor_list(den,x)
        assert len(facs)==1
        factor,power=facs[0]
        pol=sp.Poly(factor,x)
        assert pol.degree()==1 and not num.has(x)
        slope,constant=pol.all_coeffs()
        assert slope>0 and constant>0
        a=sp.Rational(slope/constant)
        C=sp.Rational(num/(coeff*constant**power))
        if power==1:answer+=rational(C/a)*(1+rational(a)).log()
        else:answer+=rational(C*(1-(1+a)**(1-power))/(a*(power-1)))
    return answer,str(partial)
cases=[
    ('signed_repeated',['1','-3','2'],[['2',2],['11',1]]),
    ('improper_three_scale',['-2','5','0','-7','1','9'],[['1/3',1],['7',1],['100',1]]),
    ('zero_scale_signed',['-1','3','-4'],[['0',8],['31',3]]),
    ('repeated_large',['1','-2','1'],[['999',5],['3/7',2]]),
]
rows=[]
for name,P,factors in cases:
    got=integral('0',P,factors,Q(1,2**120))
    ref,partial=reference(P,factors)
    assert got['lower']<=ref.upper() and got['upper']>=ref.lower(),name
    rows.append({'case':name,'P':P,'factors':factors,'partial_fractions':partial,'reference':ref.str(100),'lower':got['lower'].str(100),'upper':got['upper'].str(100),'panel_count':len(got['panels']),'overlap':True})
    print(name,'PASS',len(got['panels']),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'rows':rows,'elapsed_seconds':time.monotonic()-start,'inputs':{str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [BASE/'PROOF.md',Path(__file__),BASE/'source/PROOF.md',BASE/'source/code/moments.py']}}
target=BASE/'verification/independent_partial_fractions.json'
assert not target.exists()
target.write_text(json.dumps(out,indent=2)+'\n')
print('DONE',out['elapsed_seconds'],flush=True)

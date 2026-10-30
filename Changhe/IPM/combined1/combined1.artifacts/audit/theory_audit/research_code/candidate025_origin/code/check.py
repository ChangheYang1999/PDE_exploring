"""Exact local power series; no imported candidate field implementation."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from math import comb
import hashlib,json,sys,time
from flint import arb,ctx
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def binom(a,n):
    z=Q(1)
    for i in range(n):z*=Q(a-i,i+1)
    return z
start=time.monotonic();ctx.prec=512
raw=B/'data/candidate025.json';peerfile=B/'source/N4_direct.json'
data=json.loads(raw.read_text());peer=json.loads(peerfile.read_text())
assert sha(raw)==peer['generator_sha256']=='3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17'
c=Q(data['cl_exact']);gamma=1/c;delta=1-gamma
coef=[Q(0),Q(0),Q(0)];touched=0;summands=0
for g in data['generators']:
    m=int(g['m']);w=int(g['spec'][1]);kind=g['spec'][0]
    assert m>=0 and w>=0 and kind in ['mono','leg','legq','legqs']
    if m+w>2:continue
    N=0 if kind=='mono' else int(g['spec'][2])
    q=int(g['spec'][3]) if kind in ['legq','legqs'] else 0
    R=Q(g['spec'][4]) if kind=='legqs' else Q(1)
    assert R>0
    p=(3+gamma-int(g['j'])*delta)/2
    touched+=1
    for k in range(min(N,2-m-w)+1):
        n=2-m-w-k;d=w+q+k
        series=sum((binom(p-m,i)*binom(-d,n-i)/R**(2*(n-i)) for i in range(n+1)),Q(0))
        coeff=Q(g['coef'])*(-1)**(N+k)*comb(N,k)*comb(N+k,k)/R**(2*(w+k))
        coef[m]+=coeff*series;summands+=1
b0,b1,b2=coef;a40=b0+b1+b2;a22=2*b0-6*b2;a04=b0-b1+b2
strain=4*a22;a0=-4*a22-24*a04
assert c+strain==1 and a0>0
fields={'strain':strain,'a0':a0,'x2y2_coefficient':a22,'y4_coefficient':a04}
checks={k:v==Q(peer['origin'][k]) for k,v in fields.items()};assert all(checks.values()),checks
ball=arb(a0.numerator)/arb(a0.denominator)
assert ball.overlaps(arb(peer['a0_arb']))
result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':peer['candidate'],
'inputs':{str(p):sha(p) for p in [raw,peerfile,B/'PROOF.md',Path(__file__)]},
'raw_count':len(data['generators']),'contributing_generators':touched,'contributing_summands':summands,
'quartic_coefficients':{'x4':str(a40),'x2y2':str(a22),'y4':str(a04)},
'origin':{k:str(v) for k,v in fields.items()},'c_plus_strain':str(c+strain),'a0_positive':True,
'a0_arb':ball.str(80),'N4_exact_comparisons':checks,'elapsed_seconds':time.monotonic()-start,
'verdict':'CONFIRMED exact independent local origin jet'}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(result['utc'],result['contributing_generators'],result['contributing_summands'],result['a0_arb'],result['elapsed_seconds'])

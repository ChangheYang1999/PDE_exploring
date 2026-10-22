from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import isqrt
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_repair_transfer';scale=10**35
rows=[]
for M,N,d in [(16,1440,F(8447,10**18)),(24,4488,F(6419,250000000000000000))]:
 q=N*d*d;whole=q.numerator*scale**2//q.denominator;r=isqrt(whole);lo,hi=F(r,scale),F(r+1,scale);assert lo*lo<=q<hi*hi
 gram=sum([2*d+d*d for j in range(N)],F(0));assert gram==N*(2*d+d*d)
 rows.append({'M':M,'N':N,'delta_exact':str(d),'eta_squared_exact':str(q),'eta_rational_root_interval':list(map(str,[lo,hi])),'gram_perturbation_exact_upper':str(gram)})
a=json.loads((D/'evidence/compute.json').read_text());tests=0
for p,q in zip(rows,a['records'],strict=True):
 for key in ['M','N','delta_exact','eta_squared_exact','gram_perturbation_exact_upper']:assert p[key]==q[key]
 l,h=map(F,p['eta_rational_root_interval']);al,ah=map(F,q['eta_arb512']);pub=F(q['eta_strict_public_upper']);g=F(p['gram_perturbation_exact_upper']);gp=F(q['gram_strict_public_upper']);exact=F(p['eta_squared_exact'])
 assert 0<al<=ah and al*al<=exact<=ah*ah
 assert 0<l<=h<pub and 0<al<=ah<pub and pub*pub>exact and gp>g;tests+=10
 p['eta_strict_public_upper']=q['eta_strict_public_upper'];p['gram_strict_public_upper']=q['gram_strict_public_upper']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files={str(p.relative_to(B)):sha(p) for p in [D/'PROOF.md',D/'evidence/proof_first.json',D/'evidence/compute.json',Path(__file__)]}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INTEGER_ROOT_AND_EXACT_SUM_INDEPENDENT_GRAM_CONSTANTS','strict_and_enclosure_comparisons':tests,'records':rows,'files':files,'scope':'Independent scalar calculations; no actual Gram entries, eigenvalues, whitening or operator claim.'}
p=D/'evidence/independent.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'records':rows}))

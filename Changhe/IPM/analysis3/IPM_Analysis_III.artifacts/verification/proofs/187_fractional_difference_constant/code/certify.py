import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1];ctx.threads=1
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def rec(x):return {'ball':x.str(80),'lower_exact':str(x.lower().fmpq()),'upper_exact':str(x.upper().fmpq())}
p0=LANE/'proofs/179_high_residual_lower/evidence/independent_1024.json'
p1=LANE/'proofs/182_high_residual_difference_lower/evidence/independent_8008_1024.json'
prev=LANE/'proofs/182_high_residual_difference_lower/evidence/final_certificate.json'
old=json.loads(prev.read_text());assert old['verdict']=='CONFIRMED'
for p in (p0,p1):assert old['artifacts'][str(p.relative_to(LANE))]==sha(p)
x=json.loads(p0.read_text());y=json.loads(p1.read_text())
assert x['verdict']==y['verdict']=='PASS'
for k in ('input_sha256','scalar_sha256','cache_sha256'):assert x[k]==y[k]==old[k]
original=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
assert sha(original)==x['input_sha256']
xl=F(x['weighted_derivatives'][5]['lower_exact']);xu=F(x['weighted_derivatives'][5]['upper_exact'])
yl=F(y['weighted_derivatives'][5]['lower_exact']);yu=F(y['weighted_derivatives'][5]['upper_exact'])
dlo=xl-yu;dhi=xu-yl;assert dlo>0
dt=abs(F(x['t'])-F(y['t']));assert dt==F(1,125)
ctx.prec=1024
csq=8/(3*(2*arb.pi()).sqrt());factor=csq.sqrt()*(aa(dt).log()*aa(F(3,4))).exp()
b=aa(dlo)/factor
primary={'bits':ctx.prec,'constant_squared':rec(csq),'evaluation_factor':rec(factor),'lower_expression':rec(b)}
integer=int(b.lower().floor().fmpq());assert b>integer
ctx.prec=768
I=aa(F(3,4)).gamma()*aa(F(1,4)).gamma()/(2*aa(F(5,2)).gamma())
csq2=2*I/arb.pi();factor2=(csq2*(aa(dt)**aa(F(3,2)))).sqrt();b2=aa(dlo)/factor2
assert csq2.overlaps(arb(primary['constant_squared']['ball']))
assert factor2.overlaps(arb(primary['evaluation_factor']['ball']))
assert b2.overlaps(arb(primary['lower_expression']['ball'])) and b2>integer
secondary={'bits':ctx.prec,'integral_I':rec(I),'constant_squared':rec(csq2),'evaluation_factor':rec(factor2),'lower_expression':rec(b2)}
obj={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','reported_lower_bound':str(integer),'points':[x['t'],y['t']],'separation':str(dt),'difference_exact_lower':str(dlo),'difference_exact_upper':str(dhi),'primary':primary,'independent_beta_gamma':secondary,'input_sha256':x['input_sha256'],'cache_sha256':x['cache_sha256'],'scalar_sha256':x['scalar_sha256'],'scope':'fixed high norm of topic177, scalar summand only; no inverse or closure inference','hashes':{str(p.relative_to(LANE)):sha(p) for p in (p0,p1,prev,ROOT/'PROOF.md',Path(__file__))}}
(ROOT/'evidence/calculation.json').write_text(json.dumps(obj,indent=2)+'\n')
print(integer);print(primary['lower_expression']['ball']);print(obj['date'])

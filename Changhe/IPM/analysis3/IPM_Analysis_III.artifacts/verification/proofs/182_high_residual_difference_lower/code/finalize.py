import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1];ctx.prec=1024;ctx.threads=1
p0=LANE/'proofs/179_high_residual_lower/evidence/independent_1024.json';p1=ROOT/'evidence/independent_8008_1024.json';pilot=ROOT/'evidence/pilot_pairs.json'
def a(q):q=F(q);return arb(q.numerator)/q.denominator
def rec(x):return {'ball':x.str(90),'lower':str(x.lower().fmpq()),'upper':str(x.upper().fmpq())}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
x=json.loads(p0.read_text());y=json.loads(p1.read_text());assert x['verdict']==y['verdict']=='PASS';assert x['input_sha256']==y['input_sha256'];assert x['scalar_sha256']==y['scalar_sha256'];assert x['cache_sha256']==y['cache_sha256']
diff=abs(arb(x['weighted_derivatives'][5]['ball'])-arb(y['weighted_derivatives'][5]['ball']));dt=abs(F(x['t'])-F(y['t']));constant=(8*arb(2).sqrt()/(3*arb.pi())).sqrt();bound=diff/(constant*(a(dt).log()*a(F(3,4))).exp())
row=next(r for r in json.loads(pilot.read_text())['rows'] if r['t']=='8' and r['u']=='1001/125');assert bound.overlaps(arb(row['bound']['ball']));assert bound>36400585492
obj={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','precision':1024,'reported_lower_bound':'36400585492','points':[x['t'],y['t']],'separation':str(dt),'difference':rec(diff),'constant':rec(constant),'norm_lower_expression':rec(bound),'input_sha256':x['input_sha256'],'scalar_sha256':x['scalar_sha256'],'cache_sha256':x['cache_sha256'],'scope':'exact normalized modal residual in the fixed equivalent high norm of topic177; no inverse or nonlinear smallness assertion','artifacts':{str(p.relative_to(LANE)):sha(p) for p in [p0,p1,pilot,ROOT/'PROOF.md',ROOT/'code/combine.py',ROOT/'code/independent_point.py',Path(__file__)]}}
(ROOT/'evidence/final_certificate.json').write_text(json.dumps(obj,indent=2)+'\n');print(bound.str(35));print(obj['date'])

import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from itertools import combinations
import json,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1];ctx.prec=1024;ctx.threads=1
source=LANE/'proofs/179_high_residual_lower/evidence/nearby_pilot.json'
def a(q):q=F(q);return arb(q.numerator)/q.denominator
def rec(x):return {'ball':x.str(80),'lower':str(x.lower().fmpq()),'upper':str(x.upper().fmpq())}
raw=json.loads(source.read_text());constant=(8*arb(2).sqrt()/(3*arb.pi())).sqrt();rows=[]
for p,q in combinations(raw['rows'],2):
 diff=abs(arb(p['weighted_derivatives'][5]['ball'])-arb(q['weighted_derivatives'][5]['ball']));dt=abs(F(p['t'])-F(q['t']));bound=diff/(constant*(a(dt).log()*a(F(3,4))).exp())
 rows.append({'t':p['t'],'u':q['t'],'derivative_difference':rec(diff),'bound':rec(bound)})
rows.sort(key=lambda r:F(r['bound']['lower']),reverse=True)
obj={'date':datetime.now(timezone.utc).isoformat(),'status':'PENDING_INDEPENDENT_PAIR_RECONSTRUCTION','constant':rec(constant),'rows':rows,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'evidence/pilot_pairs.json').write_text(json.dumps(obj,indent=2)+'\n')
for r in rows[:5]:print(r['t'],r['u'],r['bound']['ball'])

"""Reuse the verified full-angular envelope with the new exact radial weight."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,math
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
RUN=LANE/'proofs/134_residual_green_taylor/evidence/production_28'
CERT=LANE/'proofs/154_residual_final_audit/evidence/final_certificate.json'
ORIGINAL=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(x):
 x=F(x);return arb(x.numerator)/x.denominator
def exact(x):
 m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def rec(x):return {'ball':x.str(60),'lower_exact':str(exact(x.lower())),'upper_exact':str(exact(x.upper()))}
cert=json.loads(CERT.read_text());meta=json.loads((RUN/'metadata.json').read_text())
assert cert['status']=='CONFIRMED'
assert sha(ORIGINAL)==cert['source_sha256']==meta['source_sha256']
assert sha(RUN/'leaves.jsonl')==cert['journal_sha256']
assert sha(RUN/'metadata.json')==cert['metadata_sha256']
rows=[json.loads(line) for line in (RUN/'leaves.jsonl').read_text().splitlines()]
rows.sort(key=lambda row:F(row['left']))
assert len(rows)==1860 and F(rows[0]['left'])==-40 and F(rows[-1]['right'])==20
assert all(F(x['right'])==F(y['left']) for x,y in zip(rows,rows[1:]))
for row in rows:
 assert F(row['left'])<F(row['right'])
 assert F(row['right'])<=0 or F(row['left'])>=0
 assert F(row['center_norm']['lower_exact'])>=0 and F(row['variation_bound']['lower_exact'])>=0

def compute(bits):
 ctx.prec=bits;ctx.threads=1
 total=arb(0);groups={kind:arb(0) for kind in ('inner','spline','outer')}
 for row in rows:
  l=F(row['left']);r=F(row['right']);b=F(-1,2) if r<=0 else F(123,20)
  M=F(row['center_norm']['upper_exact'])+F(row['variation_bound']['upper_exact'])
  weight=aa(b*l).exp()*aa(b*(r-l)).expm1()/aa(b)
  value=aa(M*M)*weight
  groups[row['kind']]+=value;total+=value
 inner=aa(cert['inner_tail_upper_exact'])
 outer=aa(meta['outer_tail']['energy_upper']['upper_exact'])*arb(-12).exp()
 total+=inner+outer
 return {'total_energy':total,'norm_bound':total.sqrt(),'inner_tail':inner,'outer_tail':outer,**{'finite_'+k:v for k,v in groups.items()}}
low=compute(384);high=compute(768)
for key in high:assert high[key].overlaps(low[key])
hi=exact(high['total_energy'].upper())
scaled=hi*1000000
upper=F(math.isqrt(scaled.numerator//scaled.denominator)+1,1000)
assert hi<upper*upper
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','uniform_angular_interval':['18/5','4'],'radial_exponents':['17/2','37/20'],'strict_norm_upper_exact':str(upper),'strict_norm_upper_decimal':f'{upper.numerator/upper.denominator:.3f}','precision_bits':[384,768],'leaf_count':len(rows),'bounds':{k:rec(v) for k,v in high.items()},'source_sha256':sha(ORIGINAL),'parent_certificate_sha256':sha(CERT),'journal_sha256':sha(RUN/'leaves.jsonl'),'metadata_sha256':sha(RUN/'metadata.json'),'proof_sha256':sha(TOP/'PROOF.md'),'script_sha256':sha(Path(__file__))}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'date':out['date'],'status':'PASS','strict_norm_upper':str(upper),'bounds':{k:v.str(20) for k,v in high.items()}},indent=2))

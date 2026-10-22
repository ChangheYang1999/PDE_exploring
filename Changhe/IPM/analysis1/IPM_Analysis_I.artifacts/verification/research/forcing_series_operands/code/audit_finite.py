"""Authenticate ancestors and independently compare all finite operand witnesses."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,sys,time
import numpy as np
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];tic=time.monotonic();ff=lambda x:Q.from_float(float(x))
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for v in iter(lambda:f.read(1048576),b''):h.update(v)
 return h.hexdigest()
prior=read(B/'research/forcing_composed_cutoff/evidence/verdict.json');assert prior['status']=='CONFIRMED_V21_FINITE_COMPONENTS_PHYSICAL_FORCING_OPEN';pins=dict(prior['files']);assert len(pins)==208
for f,h in pins.items():assert sha(B/f)==h,f
expected={'regeneration':'REGENERATED_GEOMETRY_SERIES_OPERANDS_REQUIRING_AUDIT','exact_iv':'PASS_EXACT_SERIES_OPERANDS_AND_IV160','arb':'PASS_ARB512_SERIES_AND_DIRECT_GEOMETRY','geometry_iv':'PASS_IV160_SQUARED_HALFANGLE_GEOMETRY','source_linkage':'PASS_SELECTED_FROZEN_EXPRESSION_LINKAGE'}
e={name:read(D/'evidence'/f'{name}.json') for name in expected}
for name,s in expected.items():assert e[name]['status']==s,name
rows=read(D/'evidence/blocks.json');assert len(rows)==832
with np.load(D/'evidence/operands.npz',allow_pickle=False) as z:d={k:z[k].copy() for k in z.files}
for k,v in d.items():assert np.isfinite(v).all(),k
for k in ['q_rad','q_rem','uq_rad','uq_rem','coef_rad']:assert (d[k]>=0).all(),k
for k in ['exact_iv','arb']:
 assert e[k]['operands_sha256']==sha(D/'evidence/operands.npz');assert e[k]['blocks_sha256']==sha(D/'evidence/blocks.json')
assert e['geometry_iv']['blocks_sha256']==sha(D/'evidence/blocks.json')
exact={r['index']:r for r in e['exact_iv']['records']};arb=e['arb']['records'];iv=e['geometry_iv']['records'];assert len(exact)==789 and len(arb)==len(iv)==832
counts={'exact_B_inside_Arb_Horner':0,'q_ratio_engine_checks':0,'exact_tail_retests':0,'coefficient_square_retests':0};minU=minX=minT=None
import math
for n,r in enumerate(rows):
 H,W,c,U,x=map(ff,[r[k] for k in ['H','W','c0','Umax','xr']]);assert c>0 and x>=0 and U>0
 Bq=sum((abs(ff(d['uq_mid'][n,i,j]))+ff(d['uq_rad'][n,i,j]))*H**i*W**j for i in range(13) for j in range(9))+ff(d['uq_rem'][n]);assert Q(arb[n]['B_interval'][0])<=Bq<=Q(arb[n]['B_interval'][1])<=U;counts['exact_B_inside_Arb_Horner']+=1
 mu=(U-Bq)/Bq;mx=(c*x-U)/U;assert mu>0 and mx>0;minU=mu if minU is None else min(minU,mu);minX=mx if minX is None else min(minX,mx)
 for eng in [arb,iv]:
  v=eng[n];assert v['index']==n;ql,qu=Q(v['q_lower']),Q(v['q_upper']);assert 0<=ql<=qu
  assert Q(v['q_ratio_lower_margin'])==ql-c*(1-x)>0;assert Q(v['q_ratio_upper_margin'])==c*(1+x)-qu>0;counts['q_ratio_engine_checks']+=2
 if r['active']:
  v=exact[n];assert 0<x<Q(3,5);R=ff(r['tail']);assert R>0;rel=(R*R*c*(1-x)**2-x**34)/x**34;assert rel>0
  assert Q(v['Umax_relative_margin'])==mu and Q(v['ratio_relative_margin'])==mx and Q(v['tail_squared_relative_margin'])==rel
  minT=rel if minT is None else min(minT,rel);counts['exact_tail_retests']+=1
  for k in range(17):
   m,rad=ff(d['coef_mid'][n,k]),ff(d['coef_rad'][n,k]);L=(-1)**k*m-rad;V=(-1)**k*m+rad;A=Q(math.comb(2*k,k),4**k)*c**(-k);assert 0<L<=V and L*L*c<=A*A<=V*V*c;counts['coefficient_square_retests']+=1
assert counts=={'exact_B_inside_Arb_Horner':832,'q_ratio_engine_checks':3328,'exact_tail_retests':789,'coefficient_square_retests':13413}
for key,value in [('minimum_relative_Umax_margin',minU),('minimum_relative_ratio_margin',minX),('minimum_relative_squared_tail_margin',minT)]:assert Q(e['exact_iv'][key])==value
assert e['source_linkage']['scalar_counts']=={'c0':832,'uq':832,'Umax':832,'xr':832,'tail':789,'coef':12624,'coef0':789}
assert e['source_linkage']['uq_array_entries_compared']==195520 and e['source_linkage']['canonical_local_knots']==14
assert e['regeneration']['active']==789 and e['regeneration']['fallback']==43
proof=read(D/'evidence/proof_first.json');assert proof['sha256']==sha(D/'PROOF.md')
# Pin the completed finite evidence, excluding this audit's own output.
for p in [B/'research/forcing_composed_cutoff/evidence/verdict.json',D/'PROOF.md',D/'GEOMETRY_ADDENDUM.md',*sorted((D/'code').glob('*.py')),*sorted((D/'evidence').glob('*'))]:
 if p.name in ['finite_audit.json','verdict.json'] or p.is_dir():continue
 pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-tic,'status':'PASS_SERIES_FINITE_AUDIT_MODEL_REVIEW_PENDING','prior_pins':208,'counts':counts,'minimum_relative_margins':{'Umax':str(minU),'ratio':str(minX),'squared_tail':str(minT)},'source_counts':e['source_linkage']['scalar_counts'],'active_blocks':789,'fallback_blocks':43,'pins':dict(sorted(pins.items())),'scope':'Contemporary finite geometric/scalar witness. No old execution, full composed residual or forcing norm accepted.'}
(D/'evidence/finite_audit.json').write_text(json.dumps(out,indent=2)+'\n')
review=dict(out);review.pop('pins');review['evidence_sha256']={k:sha(D/'evidence'/f'{k}.json') for k in expected};review['geometry_minimum_margins']={k:{key:e[k][key] for key in ['minimum_q_ratio_lower_margin','minimum_q_ratio_upper_margin']} for k in ['arb','geometry_iv']};review['finite_audit_sha256']=sha(D/'evidence/finite_audit.json');(D/'evidence/review_summary.json').write_text(json.dumps(review,indent=2)+'\n')
print(out['utc'],out['status'],out['seconds'],len(pins),counts)

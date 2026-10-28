"""Outward aggregation of saved component uppers, no producer code imported."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,math,hashlib
from flint import arb,ctx
ctx.prec=256
BASE=Path(__file__).resolve().parents[1]
num=Path('numerics')
src=num/'data/certSups_131.jsonl';summ=num/'data/certSups_131_summary2.json'
rows=[json.loads(s) for s in src.read_text().splitlines() if s.strip()]
summary=json.loads(summ.read_text())
assert len(rows)==40081 and len({(r['i'],r['k']) for r in rows})==40081
assert all(r['status']=='ok' for r in rows)
def A(x):
 q=Q(x);return arb(q.numerator)/q.denominator
def finite(x):return isinstance(x,(int,float)) and math.isfinite(x)
origin=next(r for r in rows if r['r_lo']==0)
r0=A(origin['r_hi']);ratio=((1+8*r0*r0)/(1+4*r0*r0))**(arb(2)/5)
ratio_saved=A(summary['origin_square_weight_ratio_applied'])
checks={}
for key,entry in summary.items():
 if not isinstance(entry,dict):continue
 good=[r for r in rows if finite(r[key])]
 bad=[r for r in rows if not finite(r[key])]
 assert len(good)==entry['n_certified_cells'] and len(bad)==entry['n_nonfinite_cells']
 vals=[]
 for r in good:
  v=A(r[key])
  if r['r_lo']==0 and key.startswith('wFrob'):v*=ratio
  vals.append((v,r))
 # Ball midpoint only selects the candidate maximum; every inequality is then checked.
 vmax,rmax=max(vals,key=lambda t:float(t[0].mid()))
 bound=A(str(entry['rounded_up_6sig']))
 assert all(v<bound or v==bound for v,r in vals)
 checks[key]={'finite_count':len(good),'missing_count':len(bad),'rounded_upper_valid':True,'rounded_upper_decimal':str(entry['rounded_up_6sig']),'max_cell':[rmax['i'],rmax['k']]}
# Every component is finite, including the cells with nonfinite tensor outputs.
allnorms={}
for name in ['rho','U']:
 for order in [1,2]:
  key=f'Frob_D{order}_{name}'
  types=['rho'] if name=='rho' else ['U1','U2']
  maxun=arb(0);maxw=arb(0);cellun=None;cellw=None;recovered=0;values=[]
  for r in rows:
   ss=Q(0)
   for typ in types:
    for i in range(order+1):
     b=r[f'{typ}_{i}_{order-i}'];assert finite(b) and b>=0
     ss+=math.comb(order,i)*Q(b)**2
   un=A(ss).sqrt();rr=A(r['r_hi'])
   w=(1+(8 if r['r_lo']==0 else 4)*rr*rr)**(arb(2)/5)
   wn=un*w;values.append((un,wn))
   if float(un.mid())>float(maxun.mid()):maxun=un;cellun=[r['i'],r['k']]
   if float(wn.mid())>float(maxw.mid()):maxw=wn;cellw=[r['i'],r['k']]
   if not finite(r[key]):recovered+=1
  # Conservative decimal upper at five digits after the decimal point.
  up=int((maxun.upper()*100000).ceil().unique_fmpz());wp=int((maxw.upper()*100000).ceil().unique_fmpz())
  assert all(v<A(Q(up,100000)) and w<A(Q(wp,100000)) for v,w in values)
  allnorms[key]={'all_cells':len(rows),'recovered_nonfinite_tensor_cells':recovered,'max_of_component_aggregation':maxun.str(60),'weighted_max':maxw.str(60),'unweighted_upper_rational':str(Q(up,100000)),'weighted_upper_rational':str(Q(wp,100000)),'unweighted_upper_decimal':f'{up/100000:.5f}','weighted_upper_decimal':f'{wp/100000:.5f}','max_cell':cellun,'weighted_max_cell':cellw}
  print(key,allnorms[key]['unweighted_upper_decimal'],allnorms[key]['weighted_upper_decimal'],'recovered',recovered,flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED aggregation conditional on saved component upper bounds','precision_bits':ctx.prec,'origin_ratio':ratio.str(65),'saved_ratio_valid_upper':ratio_saved>ratio,'summary_checks':checks,'all_component_aggregation':allnorms,'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'summary_sha256':hashlib.sha256(summ.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((BASE/'numerics_audit/C2_CORRECTION_PROOF.md').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('saved ratio upper',ratio_saved>ratio,ratio.str(40),flush=True)

"""Fresh exact-rational audit of geometry coverage metadata and output inequalities."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n8_geometry';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());g=json.loads((E/'geometry_inputs.json').read_text())
assert c['status']=='PASS_ALL_N8_COORDINATE_GEOMETRY_ONLY'
for p,h in c['files'].items():assert sha(B/p)==h,p
counts=0;unique=0;nodechecks=0;checks=0
for tag,r in g['runs'].items():
 result=c['results'][tag];needed={};nrad=len(r['radial']);nang=r['ntheta'];K=r['K'];cap=F(r['theta_cap_exact'][0]);eps=F(r['epsilon_exact']);pmn=F(r['p_min_exact']);pmx=F(r['p_max_exact']);R=3*F(r['delta_max_exact_decimal'])
 for mask in r['masks']:
  d=F(mask['delta']);assert F(mask['cutoff_float_exact'])>=3*d
  for k,js in enumerate(mask['omitted_per_radial']):
   for j in js:
    key=(mask['ci'],k,j);needed[key]=max(needed.get(key,F()),d);counts+=1
 unique+=len(needed);assert len(needed)==result['unique_omitted_boxes'] and sum(result['clamp_cases'].values())==len(needed)
 for i,box in enumerate(r['angular']):
  assert F(box['lo_exact'])<=cap*i/nang and F(box['hi_exact'])>=cap*(i+1)/nang;nodechecks+=2
 for box in r['radial']:
  a,b,h=map(F,[box['cell_left_exact'],box['cell_right_exact'],box['h_up_exact']]);lo,hi=F(box['t_lo_exact']),F(box['t_hi_exact']);k=box['k']
  assert h>=b-a and lo<=a+k*h/K and hi>=a+(k+1)*h/K;nodechecks+=2
 for cov in result['coverage']:
  assert F(cov['first_radius']['upper_exact'])<pmn-R and F(cov['last_radius']['lower_exact'])>pmx+R
  assert F(cov['cap_sine']['lower_exact'])>R/pmn;checks+=3
 w=result['worst_gap_box'];d=F(w['largest_omitted_delta_exact']);threshold=(3*d+eps)**2
 assert threshold==F(w['threshold_squared_exact'])
 gap=min(F(w['arb_squared_distance']['lower_exact']),F(w['iv_squared_distance']['lower_exact']))-threshold
 assert gap==F(result['minimum_squared_gap_exact'])>F('0.000001' if tag=='full' else '0.0000001');checks+=2
 for row in result['fine_large_disc_counterexamples']:
  witness=pmn+2*F(row['delta_exact']);up=max(F(row['coordinate_radius_arb_upper']['upper_exact']),F(row['coordinate_radius_iv_upper']['upper_exact']))
  assert witness==F(row['witness_radius_lower_exact']) and witness-up==F(row['positive_gap_exact'])>0 and up<F('8.656431');checks+=3
assert counts==584546 and unique==203682 and c['counts']=={'omitted_cell_delta_pairs':counts,'unique_omitted_boxes':unique,'two_engine_distance_pairs':unique,'fine_actual_domain_counterexamples':3}
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_GEOMETRY_OUTPUT_AUDIT','counts':{'omitted_pairs_recounted':counts,'unique_boxes_recounted':unique,'subnode_endpoint_checks':nodechecks,'strict_saved_inequalities':checks},'scope':'Fresh scalar/coverage audit, not historical mask identity. The primary two-engine run proves the actual excluded distances.','files':{str(p.relative_to(B)):sha(p) for p in [D/'PROOF.md',D/'ADDENDUM.md',D/'CLOSURE_SCOPE.md',Path(__file__),E/'checks.json',E/'geometry_inputs.json']}}
(E/'output_audit.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items() if k!='files'}))

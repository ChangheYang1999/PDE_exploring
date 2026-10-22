"""Complete exact range aggregation and independent saved-maximum comparisons."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,time,math
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_bernstein';SOURCE=B/'research/residual_cell_cauchy'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def be(x):
 assert x['schema']=='arb-dyadic-mid-radius-v1';m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);assert r>=0;return m-r,m+r

def ceiling(x):y=x*10**12;return F(y.numerator//y.denominator+1,10**12)
def pin(p):
 n=str(p.relative_to(B));h=sha(p);assert n not in pins or pins[n]==h;pins[n]=h
start=time.monotonic();manifest=json.loads((D/'data_exact/manifest.json').read_text());plan=json.loads((D/'data_exact/arithmetic_plan.json').read_text());pf=json.loads((D/'evidence/proof_first.json').read_text());assert pf['proof_sha256']==sha(D/'PROOF.md');assert manifest['cells']==[4102,4125,4211] and manifest['chunks']==[[a,min(a+64,522)] for a in range(0,522,64)] and manifest['subcells']==plan['subcells']==8 and plan['arb_bits']==512 and manifest['degree']==plan['degree']==64;pins=dict(plan['files'])
for n,hsh in pins.items():assert sha(B/n)==hsh
old=json.loads((SOURCE/'evidence/output_audit.json').read_text());assert old['status']=='PASS_COMPLETE_THREE_CELL_CAUCHY_OUTPUT_AUDIT';caps=json.loads((B/'research/derivative_scalar_aggregation/sources/runs__cert_deriv_middle.json').read_text())['rows'];assert len(caps)==7809 and all(row['ci']==i for i,row in enumerate(caps));records=[];counts={'cells':0,'mode_records':0,'chunks':0,'saved_modal_maximum_enclosure_checks':0,'coefficient_radius_checks':0,'recorded_Bernstein_coefficient_checks':0,'coefficient_stream_matches':0,'cell_derivative_bounds':0};comparisons={};selected_maxima={}
for cell in manifest['cells']:
 original=next(x for x in old['records'] if x['cell']==cell);h=F(original['h_exact']);assert h>0;coeff={kind:json.loads((SOURCE/'evidence'/('%s_%d.json'%(kind,cell))).read_text())['coefficient_boxes'] for kind in ['arb','iv']};sums={(i,j):[F(0)]*8 for i in range(6) for j in range(6-i)};seen=[]
 for chunk,(a,b) in enumerate(manifest['chunks']):
  paths={kind:D/'evidence'/('%s_%d_%d.json'%(kind,cell,chunk)) for kind in ['exact','subdivision']};data={kind:json.loads(p.read_text()) for kind,p in paths.items()};x=data['exact'];y=data['subdivision'];assert x['status']=='COMPUTED_EXACT_LOCAL_BERNSTEIN_MAXIMA_NEEDS_INDEPENDENT_CHECK' and y['status']=='PASS_EXACT_AND_ARB_SUBDIVISION_AND_DIRECT_STREAM_BINDING'
  for kind,obj in data.items():
   assert obj['cell']==cell and obj['chunk']==chunk and obj['mode_range']==[a,b] and obj['subcells']==8 and len(obj['records'])==b-a;assert datetime.fromisoformat(pf['utc'])<datetime.fromisoformat(obj['utc'])
   for n,hsh in obj['files'].items():assert sha(B/n)==hsh and (n not in pins or pins[n]==hsh);pins[n]=hsh
   pin(paths[kind])
  assert x['modal_subcell_maxima']==y['modal_subcell_maximum_checks']==(b-a)*48 and x['modal_derivatives']==y['coefficient_radius_checks']==(b-a)*6 and y['bernstein_coefficient_checks']==(b-a)*8*375 and y['arb_bits']==512
  for rr,ss in zip(x['records'],y['records']):
   N=rr['mode_index'];assert N==ss['mode_index'] and N==len(seen)
   assert a<=N<b and rr['frequency']==ss['frequency']==2*N+1 and len(rr['orders'])==len(ss['orders'])==6;seen.append(N);rads=[]
   for q in range(65):
    l,r=be(coeff['arb'][N][q]);u,v=be(coeff['iv'][N][q]);left,right=max(l,u),min(r,v);assert left<=right;rads.append((right-left)/2)
   for i,(ro,so) in enumerate(zip(rr['orders'],ss['orders'])):
    assert ro['order']==so['order']==i;error=sum((F(math.factorial(q)//math.factorial(q-i))*rads[q] for q in range(i,65)),F(0));assert F(ro['coefficient_radius_exact'])==F(so['coefficient_radius_exact'])==error;counts['coefficient_radius_checks']+=1;assert ro['bernstein_coefficients_sha256']==so['coefficient_stream_sha256'] and len(ro['bernstein_coefficients_sha256'])==64;assert ro['bernstein_coefficient_count']==so['bernstein_coefficient_checks']==8*(65-i);counts['coefficient_stream_matches']+=1;assert len(ro['bernstein_maxima_exact'])==len(so['bernstein_maxima_boxes'])==8
    for sub,(value,box) in enumerate(zip(ro['bernstein_maxima_exact'],so['bernstein_maxima_boxes'])):
     val=F(value);lower,upper=[F(box[k]) for k in ['lower_exact','upper_exact']];assert 0<=lower<=val<=upper;counts['saved_modal_maximum_enclosure_checks']+=1
     for j in range(6-i):sums[i,j][sub]+=(2*N+1)**j*(val+error)
   counts['mode_records']+=1
  counts['recorded_Bernstein_coefficient_checks']+=y['bernstein_coefficient_checks'];counts['chunks']+=1
 assert seen==list(range(522));results={}
 for i in range(6):
  for j in range(6-i):
   key='W_%d_%d'%(i,j);finite=h**(-i)*max(sums[i,j]);previous=original['bounds'][key];tail=F(previous['tail_upper_exact']);assert tail>0;new=finite+tail;oldvalue=F(previous['total_upper_exact']);chosen=min(new,oldvalue);cap=F.from_float(caps[cell][key]);label='VALIDATES_SAVED_CAP_ON_SELECTED_CELL' if chosen<=cap else 'UPPER_TOO_LARGE_TO_VALIDATE_SAVED_CAP';comparisons[label]=comparisons.get(label,0)+1
   results[key]={'bernstein_finite_upper_exact':str(finite),'inherited_tail_upper_exact':str(tail),'bernstein_total_upper_exact':str(new),'bernstein_strict_ceiling_exact':str(ceiling(new)),'old_total_upper_exact':str(oldvalue),'old_strict_ceiling_exact':str(ceiling(oldvalue)),'chosen_upper_exact':str(chosen),'chosen_strict_ceiling_exact':str(ceiling(chosen)),'choice':'BERNSTEIN' if new<=oldvalue else 'PREVIOUS_CAUCHY_FINITE_SUM','saved_cap_exact':str(cap),'saved_comparison':label,'display_only':float(chosen),'subinterval_weighted_finite_sums_exact':[str(v) for v in sums[i,j]],'maximizing_bound_subinterval_indices':[s for s,v in enumerate(sums[i,j]) if v==max(sums[i,j])]};assert chosen<ceiling(chosen);counts['cell_derivative_bounds']+=1
   if key not in selected_maxima or chosen>F(selected_maxima[key]['upper_exact']):selected_maxima[key]={'cell':cell,'upper_exact':str(chosen),'strict_ceiling_exact':str(ceiling(chosen)),'display_only':float(chosen)}
 records.append({'cell':cell,'h_exact':str(h),'left_exact':original['left_exact'],'right_exact':original['right_exact'],'bounds':results});counts['cells']+=1
assert counts=={'cells':3,'mode_records':1566,'chunks':27,'saved_modal_maximum_enclosure_checks':75168,'coefficient_radius_checks':9396,'recorded_Bernstein_coefficient_checks':4698000,'coefficient_stream_matches':9396,'cell_derivative_bounds':63}
for p in [D/'data_exact/manifest.json',D/'data_exact/arithmetic_plan.json',SOURCE/'evidence/output_audit.json',Path(__file__)]:pin(p)
for n,hsh in pins.items():assert sha(B/n)==hsh
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETE_THREE_CELL_BERNSTEIN_RANGE_AUDIT','counts':counts,'comparison_counts':comparisons,'records':records,'selected_cell_majorant_maxima':selected_maxima,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Same3 selected cells only, canonical and analytic tail inputs inherited. Saved maxima and radii reread and checked; all 4698000 coefficient checks are recorded prior computation counts with matched exact-stream digests. No complete cover, global forcing norm, physical maximum location, inverse, nonlinear closure or IPM endpoint.'}
with (D/'evidence/output_audit.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:out[k] for k in ['utc','status','counts','comparison_counts','seconds']}));print(json.dumps({k:{'cell':v['cell'],'display_only':v['display_only']} for k,v in selected_maxima.items()}))

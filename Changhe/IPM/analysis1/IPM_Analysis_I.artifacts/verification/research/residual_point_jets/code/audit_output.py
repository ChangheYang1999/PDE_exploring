"""Exact rational audit of all saved point jets, full coverage and Wiener sums."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,time,sys,platform
from collections import Counter
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_point_jets'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def read(p):return json.loads(p.read_text())
def box(v):
 assert v['schema']=='arb-dyadic-mid-radius-v1'
 m=F(int(v['mid_m']))*F(2)**int(v['mid_e']);r=F(int(v['rad_m']))*F(2)**int(v['rad_e']);assert r>=0
 return m-r,m+r
def interval(v):
 a,b=F(v['lower_exact']),F(v['upper_exact']);assert a<=b;return a,b
def encoded(v):return {'lower_exact':str(v[0]),'upper_exact':str(v[1])}
def overlap(x,y):
 a,b=max(x[0],y[0]),min(x[1],y[1]);assert a<=b;return a,b
def sums(row,j):
 low=F(0);high=F(0)
 for n,(a,b) in enumerate(row):
  low+=(2*n+1)**j*(0 if a<=0<=b else min(abs(a),abs(b)));high+=(2*n+1)**j*max(abs(a),abs(b))
 return low,high
start=time.monotonic();manifest=read(D/'data_exact/manifest.json');prep=read(D/'evidence/preparation.json');pins={};expected=[0,5,100,500,1500,2761,3925,4102,4125,4211,5622,7038,7808];assert manifest['cells']==expected and [p['cell'] for p in prep['points']]==expected
assert prep['exact_density_coefficients']==27248 and prep['free_Leibniz_identities']==12 and prep['exponential_polynomial_basis_checks']==56 and prep['Laurent_unit_test'] is True
old=read(B/'research/residual_samples/evidence/sample_result.json');saved=read(B/'research/derivative_scalar_aggregation/sources/runs__cert_deriv_middle.json')['rows'];prior={p['cell']:p for p in old['samples']};assert sorted(prior)==expected
counts=Counter();rows=[];maxima={};minimum_margin=None
for ci in expected:
 pa=D/'evidence'/('arb_%d.json'%ci);pb=D/'evidence'/('iv_%d.json'%ci);a,b=read(pa),read(pb)
 assert a['status']=='COMPUTED_PHYSICAL_GREEN_POINT_JETS_NEEDS_INDEPENDENT_AUDIT' and b['status']=='PASS_TWO_RECURRENCES_AND_POINT_JET_COEFFICIENTS'
 assert a['cell']==b['cell']==ci and a['t_exact']==b['t_exact']==prior[ci]['t_exact'];assert a['orders']==b['orders']==6 and a['modes']==b['modes']==522
 assert a['pairs']==408726 and b['integer_polynomial_products']==168 and b['coefficient_comparisons']==3132 and a['original_order_zero_overlaps']==b['order_zero_prior_comparisons']==522
 assert a['bits']==448 and b['iv_dps']==180 and b['quantization_bits']==640
 assert len(a['coefficient_boxes'])==len(b['coefficient_boxes'])==6
 for obj in [a,b]:
  for n,h in obj['files'].items():assert n not in pins or pins[n]==h;pins[n]=h
 weight=overlap(interval(a['weight_at_point']),interval(b['weight_at_point']));assert weight[0]>0
 data={};pointcomparisons=Counter()
 for i in range(6):
  assert len(a['coefficient_boxes'][i])==len(b['coefficient_boxes'][i])==522
  first=[box(v) for v in a['coefficient_boxes'][i]];second=[box(v) for v in b['coefficient_boxes'][i]];joint=[]
  for n,(v,w) in enumerate(zip(first,second)):
   joint.append(overlap(v,w));counts['coefficient_comparisons']+=1
   if i==0:overlap(joint[-1],box(prior[ci]['residual_coefficients'][n]));counts['order_zero_prior_comparisons']+=1
  for j in range(6-i):
   key='W_%d_%d'%(i,j);z=sums(joint,j);z2=sums(second,j);z1=sums(first,j)
   assert z==interval(b['wiener_sums'][key]) and z2==interval(b['iv_wiener_sums'][key])
   v=interval(a['wiener_sums'][key]);assert v[0]<=z1[0]<=z1[1]<=v[1];counts['exact_Wiener_checks']+=1
   ratio=(z[0]/weight[1],z[1]/weight[0]);data[key]={'Wiener':encoded(z),'Wiener_over_m':encoded(ratio)}
   if key not in maxima:maxima[key]={'lower':ratio[0],'upper':ratio[1],'lower_cell':ci,'upper_cell':ci}
   else:
    if ratio[0]>maxima[key]['lower']:maxima[key].update(lower=ratio[0],lower_cell=ci)
    if ratio[1]>maxima[key]['upper']:maxima[key].update(upper=ratio[1],upper_cell=ci)
   if key in saved[ci]:
    cap=F.from_float(saved[ci][key]);status='CONSISTENT_AT_SAMPLE' if z[1]<=cap else 'EXCEEDS_SAVED_MAJORANT_AT_SAMPLE' if z[0]>cap else 'OVERLAP_ONLY';assert b['saved_comparisons'][key]['comparison']==status and F(b['saved_comparisons'][key]['saved_majorant_exact'])==cap
    firststatus='CONSISTENT_AT_SAMPLE' if v[1]<=cap else 'EXCEEDS_SAVED_MAJORANT_AT_SAMPLE' if v[0]>cap else 'OVERLAP_ONLY';assert a['saved_comparisons'][key]['comparison']==firststatus
   else:status='NO_SAVED_FIELD';assert a['saved_comparisons'][key]['comparison']==b['saved_comparisons'][key]['comparison']==status
   pointcomparisons[status]+=1
 counts['points']+=1;counts['integer_polynomial_products']+=b['integer_polynomial_products'];counts['Arb_scatter_pairs']+=a['pairs'];counts.update(pointcomparisons)
 rows.append({'cell':ci,'t_exact':a['t_exact'],'r':a['r'],'comparisons':dict(pointcomparisons),'derivative_point_sums':data})
 for p in [pa,pb]:pins[str(p.relative_to(B))]=sha(p)
for n,h in prep['files'].items():assert n not in pins or pins[n]==h;pins[n]=h
for p in [D/'data_exact/manifest.json',D/'evidence/preparation.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():assert sha(B/n)==h,n
assert counts['points']==13 and counts['coefficient_comparisons']==40716 and counts['order_zero_prior_comparisons']==6786 and counts['exact_Wiener_checks']==273 and counts['integer_polynomial_products']==2184 and counts['Arb_scatter_pairs']==5313438
maxout={}
for key,v in maxima.items():
 maxout[key]={'lower_exact':str(v['lower']),'upper_exact':str(v['upper']),'lower_cell':v['lower_cell'],'upper_cell':v['upper_cell'],'display_only':float(v['upper'])}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETE_THIRTEEN_POINT_DERIVATIVE_OUTPUT_AUDIT','counts':dict(counts),'records':rows,'max_over_thirteen_point_Wiener_over_m':maxout,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-start,'runtime':{'python':platform.python_version(),'optimize':sys.flags.optimize},'scope':'Exact saved-output audit for finite point derivative boxes, conditional on inherited canonical inputs. All coefficients were recomputed by two ODE representations and angular methods. Point Wiener values do not bound a whole cell or prove a pointwise angle lower bound. No physical derivative Taylor remainder, Sobolev forcing norm, global inverse or endpoint.'}
with (D/'evidence/output_audit.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','counts','seconds']}));print(json.dumps({k:(v['display_only'],v['upper_cell']) for k,v in maxout.items()}))

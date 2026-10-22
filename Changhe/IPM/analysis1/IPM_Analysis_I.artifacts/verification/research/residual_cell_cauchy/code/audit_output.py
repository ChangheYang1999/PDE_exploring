"""Exact retained-output audit and complete selected-cell Cauchy aggregation."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,time,math
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_cauchy'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def be(x):
 assert x['schema']=='arb-dyadic-mid-radius-v1';m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);assert r>=0;return m-r,m+r

def strictceil(x,d=10**12):return F((x*d).numerator//(x*d).denominator+1,d)
def pin(p):
 n=str(p.relative_to(B));h=sha(p);assert n not in pins or pins[n]==h; pins[n]=h
start=time.monotonic();manifest=json.loads((D/'data_exact/manifest.json').read_text());assert manifest['status']=='PASS_EXACT_THREE_CELL_INPUT_BINDING' and [x['cell'] for x in manifest['cells']]==[4102,4125,4211] and manifest['radial_degree']==64 and manifest['disk_radius_exact']=='4' and manifest['radial_stride']==129;pins=dict(manifest['files'])
for n,hsh in pins.items():assert sha(B/n)==hsh
pf=json.loads((D/'evidence/proof_first.json').read_text());assert pf['proof_sha256']==sha(D/'PROOF.md')
saved=json.loads((B/'research/derivative_scalar_aggregation/sources/runs__cert_deriv_middle.json').read_text())['rows'];records=[];counts={'cells':0,'coefficient_comparisons':0,'point_jet_comparisons':0,'opposite_arithmetic_disk_checks':0,'cell_derivative_bounds':0,'ball_polynomial_products_recorded':0,'integer_polynomial_products_recorded':0};maxima={};comparison_counts={}
for rec in manifest['cells']:
 cell=rec['cell'];h=F(rec['h_exact']);paths={kind:D/'evidence'/('%s_%d.json'%(kind,cell)) for kind in ['arb','iv','arb_preflight','iv_preflight','disk_audit']};data={kind:json.loads(p.read_text()) for kind,p in paths.items()};a=data['arb'];b=data['iv'];da=data['disk_audit'];assert a['status']=='COMPUTED_PHYSICAL_GREEN_CELL_TAYLOR_NEEDS_INDEPENDENT_AUDIT' and b['status']=='PASS_TWO_CELL_TAYLOR_RECURRENCES_AND_POINT_COMPARISONS' and da['status']=='PASS_OPPOSITE_ARITHMETIC_DISK_MAJORANTS';assert a['degree']==b['degree']==64 and a['modes']==b['modes']==522
 for kind,obj in data.items():
  assert obj['cell']==cell
  for n,hsh in obj['files'].items():assert sha(B/n)==hsh and (n not in pins or pins[n]==hsh);pins[n]=hsh
  pin(paths[kind])
 for kind in ['arb','iv']:
  assert datetime.fromisoformat(pf['utc'])<datetime.fromisoformat(data[kind+'_preflight']['utc'])<datetime.fromisoformat(data[kind]['utc']);assert data[kind+'_preflight']['B_j']==data[kind]['B_j'];assert len(data[kind]['coefficient_boxes'])==522 and all(len(x)==65 for x in data[kind]['coefficient_boxes'])
 point={kind:json.loads((B/'research/residual_point_jets/evidence'/('%s_%d.json'%(kind,cell))).read_text()) for kind in ['arb','iv']};joint=[];maxden=1
 for N in range(522):
  row=[]
  for q in range(65):
   alo,ahi=be(a['coefficient_boxes'][N][q]);blo,bhi=be(b['coefficient_boxes'][N][q]);lo,hi=max(alo,blo),min(ahi,bhi);assert lo<=hi,('DISJOINT',cell,N,q);counts['coefficient_comparisons']+=1
   if q<=5:
    factor=F(math.factorial(q))*h**(-q)
    for kind,u,v in [('arb',alo,ahi),('iv',blo,bhi)]:
     p,r=be(point[kind]['coefficient_boxes'][q][N]);assert max(u*factor,p)<=min(v*factor,r);counts['point_jet_comparisons']+=1
   cap=max(abs(lo),abs(hi));assert cap.denominator&(cap.denominator-1)==0;maxden=max(maxden,cap.denominator);row.append(cap)
  joint.append(row)
 # All coefficient endpoints are exact dyadics. A common denominator permits exact integer weighted sums.
 sums=[[0]*65 for _ in range(6)]
 for N,row in enumerate(joint):
  w=2*N+1;wp=[w**j for j in range(6)]
  for q,cap in enumerate(row):
   assert maxden%cap.denominator==0;num=cap.numerator*(maxden//cap.denominator)
   for j in range(6):sums[j][q]+=wp[j]*num
 bounds=[]
 for j in range(6):
  vals=[F(data[kind]['B_j'][j]['upper_exact']) for kind in ['arb','iv']]+[F(da['results'][kind]['B_j'][j]['upper_exact']) for kind in ['arb','iv']];assert all(v>0 for v in vals);bounds.append(min(vals))
 assert da['formula_checks']==12;counts['opposite_arithmetic_disk_checks']+=12
 cellbounds={}
 for i in range(6):
  factor=h**(-i);fall65=math.factorial(65)//math.factorial(65-i);ratio=F(66,4*(66-i));assert ratio<1
  for j in range(6-i):
   key='W_%d_%d'%(i,j);finite=factor*F(sum((math.factorial(q)//math.factorial(q-i))*sums[j][q] for q in range(i,65)),maxden);tail=bounds[j]*factor*F(fall65,4**65)/(1-ratio);total=finite+tail;ceil=strictceil(total);assert finite>=0 and tail>0 and total<ceil;counts['cell_derivative_bounds']+=1
   entry={'finite_upper_exact':str(finite),'tail_upper_exact':str(tail),'total_upper_exact':str(total),'strict_ceiling_exact':str(ceil),'display_only':float(total)}
   if key in saved[cell]:
    cap=F.from_float(saved[cell][key]);entry['saved_cap_exact']=str(cap);entry['saved_comparison']='INDEPENDENT_BOUND_BELOW_SAVED_CAP' if total<=cap else 'INDEPENDENT_UPPER_TOO_LARGE_TO_VALIDATE_SAVED_CAP'
   else:entry['saved_comparison']='NO_SAVED_FIELD'
   comparison_counts[entry['saved_comparison']]=comparison_counts.get(entry['saved_comparison'],0)+1;cellbounds[key]=entry
   if key not in maxima or total>F(maxima[key]['upper_exact']):maxima[key]={'cell':cell,'upper_exact':str(total),'strict_ceiling_exact':str(ceil),'display_only':float(total)}
 assert a['point_jet_comparisons']==b['point_jet_comparisons']==3132 and b['coefficient_comparisons']==33930 and a['ball_polynomial_products']==2 and b['integer_polynomial_products']==8;counts['ball_polynomial_products_recorded']+=2;counts['integer_polynomial_products_recorded']+=8;counts['cells']+=1
 records.append({'cell':cell,'left_exact':rec['left_exact'],'right_exact':rec['right_exact'],'h_exact':str(h),'B_upper_exact':[str(x) for x in bounds],'bounds':cellbounds,'producer_seconds':a['seconds'],'independent_seconds':b['seconds']})
assert counts=={'cells':3,'coefficient_comparisons':101790,'point_jet_comparisons':18792,'opposite_arithmetic_disk_checks':36,'cell_derivative_bounds':63,'ball_polynomial_products_recorded':6,'integer_polynomial_products_recorded':24}
for p in [D/'data_exact/manifest.json',Path(__file__)]:pin(p)
for n,hsh in pins.items():assert sha(B/n)==hsh
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETE_THREE_CELL_CAUCHY_OUTPUT_AUDIT','counts':counts,'comparison_counts':comparison_counts,'records':records,'selected_cell_maxima':maxima,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Three designated closed cells only. Bounds for sum of modal suprema of D_t^i coefficients weighted by angular frequencies, i+j<=5, imply the corresponding cell sup of Fourier-Wiener sums. Canonical moment inputs inherited; no fresh integration, global derivative cover, forcing norm, inverse, nonlinear closure or endpoint. Polynomial product counts are recorded computation counts, not re-executed products.'}
with (D/'evidence/output_audit.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:result[k] for k in ['utc','status','counts','comparison_counts','seconds']}));print(json.dumps({k:{'cell':v['cell'],'display_only':v['display_only']} for k,v in maxima.items()}))

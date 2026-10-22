"""Independent record audit, exact input linkage and symbolic range identities."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime,timezone
import numpy as np
assert not sys.flags.optimize
BASE=Path(__file__).resolve().parents[3];D=BASE/'research/flow_composition';OUT=D/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def parse(p):
 def pairs(a):
  r={}
  for k,v in a:assert k not in r,('duplicate',k);r[k]=v
  return r
 return json.loads(Path(p).read_text(),object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
def exact(x):return F(float(x))
def fbox(m,r):m,r=exact(m),exact(r);assert r>=0;return m-r,m+r
counts={}
def check(condition,label):
 assert bool(condition),label
 counts[label]=counts.get(label,0)+1
# No source/checker imports. Validate the two independent Bernstein maps on a basis.
identities=0
for power in range(13):
 global_b=[F(comb(k,power),comb(12,power))*2**power if k>=power else F(0) for k in range(13)]
 left=[sum((F(comb(k,j),2**k)*global_b[j] for j in range(k+1)),F(0)) for k in range(13)]
 right=[sum((F(comb(12-k,j),2**(12-k))*global_b[k+j] for j in range(13-k)),F(0)) for k in range(13)]
 for alpha,actual in [(F(0),left),(F(1),right)]:
  want=[sum((F(comb(power,j))*alpha**(power-j)*F(comb(k,j),comb(12,j)) for j in range(min(power,k)+1)),F(0)) for k in range(13)]
  check(actual==want,'symbolic_radial_basis');identities+=13
# Angular basis in z: B20=1-2z+z², B21=2z-2z², B22=z².
basis=[(1,-2,1),(0,2,-2),(0,0,1)]
for p,controls,want in [(0,(1,1,1),(1,0,0)),(1,(-1,0,1),(-1,2,0)),(2,(1,-1,1),(1,-4,4))]:
 got=tuple(sum(controls[i]*basis[i][j] for i in range(3)) for j in range(3));check(got==want,'symbolic_angular_basis');identities+=3
prep=parse(OUT/'preparation.json');check(prep['nodes']==[[0,1,7],[12800,12801,7],[25599,25600,7]],'selected_nodes');check(prep['radial_cells']==[0,4102,7808],'selected_radial_cells')
check(prep['proof_sha256']==sha(D/'PROOF.md')==parse(OUT/'proof_first.json')['proof_sha256'],'proof_first_pin')
check(prep['code_sha256']==sha(D/'code/prepare.py'),'producer_pin')
check(prep['angular_current_equals_accepted_73'] is True,'reported_angular_equality')
for p,h in prep['dependency_pins'].items():check(sha(BASE/p)==h,'dependency_hash')
with np.load(BASE/'research/flow_angular/evidence/finite_arrays.npz',allow_pickle=False) as z:angular={key:z[key] for key in ('selected','midpoints','radii','distinct_half_widths','remainder_arrays')}
with np.load(BASE/'research/flow_scalars/evidence/scalar_arrays.npz',allow_pickle=False) as z:scalars=z['middle']
records=[];smallest=None;all_ranges=0
for packet in prep['packets']:
 ci=packet['ci'];path=BASE/packet['file'];check(sha(path)==packet['sha256'],'packet_hash')
 with np.load(path,allow_pickle=False) as z:data={key:z[key] for key in z.files}
 check(set(data)==set(packet['arrays']),'packet_array_names')
 for key,x in data.items():
  spec=packet['arrays'][key];check(np.isfinite(x).all(),'packet_finite');check(x.dtype.str==spec['dtype'] and list(x.shape)==spec['shape'],'packet_dtype_shape');check(hashlib.sha256(np.ascontiguousarray(x).tobytes()).hexdigest()==spec['sha256'],'packet_array_hash')
  if key.endswith(('_rad','_rem')):check((x>=0).all(),'packet_nonnegative')
 check(np.array_equal(data['nodes'],np.array(prep['nodes'])),'packet_nodes')
 check(np.array_equal(data['scalar'],scalars[ci]),'complete_scalar_row_equality')
 rp=BASE/packet['radial_input_file'];check(sha(rp)==packet['radial_input_sha256'],'radial_archive_hash')
 with np.load(rp,allow_pickle=False) as z:
  for key in ('P_mid','P_rad','P_rem','R_mid','R_rad','R_rem','scalar'):check(np.array_equal(data[key],z[key]),'radial_array_equality')
 check(data['P_mid'].shape==data['P_rad'].shape==data['R_mid'].shape==data['R_rad'].shape==(261,13),'radial_dimensions')
 check(data['P_rem'].shape==data['R_rem'].shape==(261,),'radial_remainder_dimensions')
 check(data['angular_mid'].shape==data['angular_rad'].shape==(3,3,3,261),'angular_dimensions');check(data['angular_rem'].shape==(3,3,261),'angular_remainder_dimensions')
 for ai,node in enumerate(prep['nodes']):
  k=angular['selected'].tolist().index(node)
  for key,old in [('angular_mid','midpoints'),('angular_rad','radii')]:check(np.array_equal(data[key][ai],angular[old][k]),'angular_current_byte_equality')
  w=angular['distinct_half_widths'].tolist().index(float(data['d'][ai]));rr=angular['remainder_arrays'][w]
  for fam in range(3):check(np.array_equal(data['angular_rem'][ai,fam],rr[0 if fam==0 else 1]),'angular_remainder_byte_equality')
  d=exact(data['d'][ai]);check(d>0,'positive_angular_width')
  for fam in range(3):
   for n in range(1,262):
    constant=8*n**3 if fam==0 else 4*n**4+8*n**3+6*n*n+2*n
    check(exact(data['angular_rem'][ai,fam,n-1])>=F(constant,6)*d**3,'exact_angular_remainder')
 k=F(1615536043799051,9007199254740992);cl=fbox(*data['cl']);check(cl[0]<=1/k<=cl[1],'exact_cl')
 h=exact(data['scalar'][0]);ell=exact(data['ell'][0]);check(0<h<F(1,522) and 2*ell>=h,'radial_coverage')
 for j in range(27):check(exact(data['scalar'][9+j])>=h**j,'exact_h_powers')
 mu=fbox(*data['scalar'][7:9]);mu_fn=lambda r:F(1129,1000)+(F(952,100)-F(1129,1000))/(1+(r/6)**4)
 rlo,rhi=map(exact,data['scalar'][5:7]);check(0<rlo<=rhi,'positive_radii');check(mu[0]<=mu_fn(rhi)<=mu_fn(rlo)<=mu[1],'exact_mu')
 old={}
 for engine in ('exact','iv'):
  p=OUT/f'{engine}_{ci:04d}.json';rec=parse(p);check(rec['status']=='PASS' and rec['ci']==ci,'completed_method_record');check(rec['code_sha256']==sha(D/f'code/{engine}_check.py'),'method_code_pin');check(rec['packet_sha256']==sha(path),'method_input_pin');check(rec['preparation_sha256']==sha(OUT/'preparation.json'),'method_preparation_pin');check(len(rec['rows'])==3,'method_row_count')
  check(rec['start_utc']>=prep['utc'] and rec['end_utc']>=rec['start_utc'],'recorded_chronology')
  for ai,row in enumerate(rec['rows']):
   check(row['angular_index']==ai and row['node']==prep['nodes'][ai],'method_row_identity');check(row['modal_products']==30537 and row['degree']==12 and row['radial_subintervals']==2,'method_count')
   check(len(row['ranges'])==4 and {x['name'] for x in row['ranges']}=={'s','v1x','v2y','T0'},'range_names')
   for result in row['ranges']:
    name=result['name'];lo,hi=map(F,result['reference']);tl,th=map(F,result['target']);check(tl==exact(data['target_'+name+'_lo'][ai]) and th==exact(data['target_'+name+'_hi'][ai]),'candidate_target_equality');check(tl<=lo<=hi<=th and result['contained'] is True,'independent_exact_containment')
    margins=[lo-tl,th-hi];check(margins==list(map(F,result['margins'])),'saved_margin');smallest=min(margins) if smallest is None else min(smallest,*margins)
    if engine=='exact':
     e=F(result['analytic_error']);check(e>=0,'nonnegative_analytic_error');old[(ai,name)]=(lo,hi,e)
    else:
     a,b,e=old[(ai,name)];check(max(a,lo)<=min(b,hi),'reference_overlap');el,eh=map(F,result['analytic_error_interval']);check(el<=e<=eh,'second_error_contains_exact_error')
    all_ranges+=1
  records.append({'file':str(p.relative_to(BASE)),'sha256':sha(p),'ci':ci,'engine':engine,'ranges':12})
check(all_ranges==72,'total_reference_ranges')
result={'utc':utc(),'status':'PASS_FINITE_COMPOSITION_RECORD_AUDIT','counts':counts,'symbolic_coefficient_positions':identities,'rectangles':9,'source_ranges':36,'reference_range_checks':72,'modal_products_per_engine':274833,'smallest_exact_inclusion_margin':str(smallest),'records':records,'code_sha256':sha(__file__),'scope':'Finite contemporary composition only; physical canonical radial input and complete finite-flow coverage OPEN.'}
path=OUT/'audit_outputs.json';assert not path.exists();path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('utc','status','rectangles','reference_range_checks','modal_products_per_engine')}),flush=True)

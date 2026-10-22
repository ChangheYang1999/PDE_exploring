"""Make explicitly untrusted contemporary flow outputs from frozen small inputs."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,hashlib,json,time,platform
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import numpy as np
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/flow_composition';E=D/'evidence';SRC=B/'research/flow_certificate/evidence/source'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def raw(a):return hashlib.sha256(np.ascontiguousarray(a,dtype='<f8').tobytes()).hexdigest()
pins={}
for topic in ('flow_angular','flow_scalars','radial_tm_instance'):
 p=B/f'research/{topic}/evidence/verdict.json';v=json.loads(p.read_text());assert v['status'].startswith('CONFIRMED'),v['status']
 for rel,want in v['files'].items():
  assert sha(B/rel)==want,rel
  if rel in pins:assert pins[rel]==want
  pins[rel]=want
 pins[str(p.relative_to(B))]=sha(p)
assert pins['research/flow_certificate/evidence/source/cert_flow.py']=='bb47a2d7a46807b02c0e943d7b50d31fb31b6a42c4be55fdbbf1c3a2b90031f6'
sys.path.insert(0,str(SRC));import cert_flow as src
from cert_resid import TMArr,bernstein_matrix
from midrad import MR,U,succ
ctx.prec=128;ctx.threads=1
nodes=[(0,1,7),(12800,12801,7),(25599,25600,7)]
def endpoints(node):
 l,r,depth=node;ctx.prec=128;hp=arb.pi()/2;base=l//128;off=(l-128*base)//(r-l);a=hp*base/200;b=hp*(base+1)/200
 for bit in range(depth-1,-1,-1):
  m=(a+b)/2
  if (off>>bit)&1:a=m
  else:b=m
 return a,b
cells=[endpoints(n) for n in nodes];ang=src.AngCache(np.arange(1,262))
fac=[ang.factors(a,b) for a,b in cells]
am=np.array([[[f[fam][j].m for j in range(3)] for fam in ('cos','C','S')] for f in fac]);ar=np.array([[[f[fam][j].r for j in range(3)] for fam in ('cos','C','S')] for f in fac])
rem=np.array([[f[fam][3] for fam in ('cos','C','S')] for f in fac]);width=np.array([f['d'] for f in fac])
assert am.shape==ar.shape==(3,3,3,261) and rem.shape==(3,3,261)
with np.load(B/'research/flow_angular/evidence/finite_arrays.npz',allow_pickle=False) as z:
 for j,node in enumerate(nodes):
  idx=[tuple(map(int,x)) for x in z['selected']].index(node)
  assert np.array_equal(am[j],z['midpoints'][idx]) and np.array_equal(ar[j],z['radii'][idx])
  widx=list(z['distinct_half_widths']).index(width[j]);rr=z['remainder_arrays'][widx]
  assert np.array_equal(rem[j,0],rr[0]) and np.array_equal(rem[j,1],rr[1]) and np.array_equal(rem[j,2],rr[1])
C=src.FlowCertifier.__new__(src.FlowCertifier);C.Nf=261;C.M=260;C.Q=12;C.n=np.arange(1,262)
k=F(1615536043799051,9007199254740992);assert F(float(k))==k
cl=1.0/float(k);C.c_l=MR(cl,succ(U*abs(cl)));C.Bern=bernstein_matrix(12)
assert F(float(C.c_l.m))-F(float(C.c_l.r))<=1/k<=F(float(C.c_l.m))+F(float(C.c_l.r))
for row in range(13):
 for col in range(13):
  from math import comb
  x=F(comb(row,col),comb(12,col)) if col<=row else F(0)
  assert F(float(C.Bern.m[row,col]))-F(float(C.Bern.r[row,col]))<=x<=F(float(C.Bern.m[row,col]))+F(float(C.Bern.r[row,col]))
packets=[]
for ci in (0,4102,7808):
 p=B/f'research/radial_tm_instance/evidence/selected_v3_cell_{ci:04d}.npz'
 with np.load(p,allow_pickle=False) as z:a={key:z[key].copy() for key in z.files}
 scalar=a['scalar'];h=float(scalar[0]);ell=float(succ(h/2));assert 2*F(ell)>=F(h)>0
 for j in range(27):assert F(float(scalar[9+j]))>=F(h)**j
 P=TMArr(MR(a['P_mid'],a['P_rad']),a['P_rem']);R=TMArr(MR(a['R_mid'],a['R_rad']),a['R_rem']);mu=MR(scalar[7],scalar[8])
 start=utc();targets=C.cell_bounds(P,R,scalar[9:],h,cells,ang,mu,K=2)
 out={key:a[key] for key in ('P_mid','P_rad','P_rem','R_mid','R_rad','R_rem','scalar')}
 out.update(angular_mid=am,angular_rad=ar,angular_rem=rem,d=width,nodes=np.array(nodes,dtype=np.int64),cl=np.array([float(C.c_l.m),float(C.c_l.r)]),ell=np.array([ell]))
 for key,val in targets.items():out['target_'+key]=np.asarray(val,dtype=np.float64)
 for key,val in out.items():
  assert np.isfinite(val).all(),key
  if key.endswith(('_rad','_rem')):assert (val>=0).all(),key
 dest=E/f'packet_{ci:04d}.npz';assert not dest.exists();np.savez_compressed(dest,**out)
 packets.append({'ci':ci,'utc_start':start,'utc_end':utc(),'file':str(dest.relative_to(B)),'sha256':sha(dest),'radial_input_file':str(p.relative_to(B)),'radial_input_sha256':sha(p),'arrays':{key:{'shape':list(val.shape),'dtype':val.dtype.str,'sha256':hashlib.sha256(np.ascontiguousarray(val).tobytes()).hexdigest()} for key,val in out.items()}})
result={'utc':utc(),'status':'UNTRUSTED_CANDIDATE_OUTPUTS_PREPARED','nodes':nodes,'radial_cells':[0,4102,7808],'rectangles':9,'target_ranges':36,'angular_current_equals_accepted_73':True,'canonical_radial_membership':'OPEN; topics98/99','conditional_radial_models':'accepted topic93 exact finite input premise','runtime':{'python':sys.version,'numpy':np.__version__,'platform':platform.platform(),'source_arb_bits':128,'threads':1},'packets':packets,'dependency_pins':pins,'code_sha256':sha(__file__),'proof_sha256':sha(D/'PROOF.md')}
assert result['proof_sha256']==json.loads((E/'proof_first.json').read_text())['proof_sha256']
(E/'preparation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('utc','status','rectangles','target_ranges')}),flush=True)

"""Data, exact dyadic endpoints and provenance; no coefficient engine."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
 os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,math,hashlib,platform
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import numpy as np
import flint,mpmath
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
ctx.threads=1
BASE=Path(__file__).resolve().parents[3]
DIR=BASE/'research/radial_tm_full';OUT=DIR/'evidence'
SOURCE=BASE/'research/flow_certificate/evidence/source'
EXPECTED={
 'green':'c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1',
 'partition':'56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2',
 'cert_flow.py':'bb47a2d7a46807b02c0e943d7b50d31fb31b6a42c4be55fdbbf1c3a2b90031f6',
 'cert_resid.py':'15a7535dbe5d7249ea38e089229591591976eef1151f298c932873f9e9dec828',
 'midrad.py':'5b5feb4ad511e66d57d228a3b754e44cfa2ceb17a33f717dde991c464d5f598e'}
PATHS={'green':BASE.parent/'ipmA-num/data/cert_green.npz',
 'partition':BASE/'research/middle_residual/evidence/partition_exact.json',
 'scalars':BASE/'research/flow_scalars/evidence/scalar_arrays.npz',
 'scalar_checks':BASE/'research/flow_scalars/evidence/checks.json'}
PATHS.update({name:SOURCE/name for name in ('cert_flow.py','cert_resid.py','midrad.py')})
SEED='ipmA-ver/topic101/radial-full/replay/v1'
SCALE=1<<1074

def utc():return datetime.now(timezone.utc).isoformat()
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False)
def pairs_no_duplicates(pairs):
 out={}
 for k,v in pairs:
  assert k not in out,('duplicate JSON key',k)
  out[k]=v
 return out
def parse(text):return json.loads(text,object_pairs_hook=pairs_no_duplicates,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
def load(path):return parse(Path(path).read_text())
def f64_units(x):
 x=float(x);assert math.isfinite(x)
 n,d=x.as_integer_ratio();p=d.bit_length()-1;assert d==1<<p and p<=1074
 return n<<(1074-p)
def units_array(a):return [[f64_units(x) for x in row] for row in a]
def rational_arb(q):
 q=Fraction(q);return arb(fmpq(q.numerator,q.denominator))
def rational_string(q):
 q=Fraction(q);return str(q)
def arb_endpoints(x):
 assert x.is_finite(),'nonfinite Arb'
 return tuple((int(m),int(e)) for m,e in (x.lower().man_exp(),x.upper().man_exp()))
def iv_endpoints(x):
 result=[]
 for sign,m,e,bits in x._mpi_:
  assert bits>=0,'nonfinite iv'
  result.append((-int(m) if sign else int(m),int(e)))
 return tuple(result)
def compare_to_units(d,c):
 m,e=map(int,d);shift=e+1074
 a,b=(m<<shift,int(c)) if shift>=0 else (m,int(c)<<(-shift))
 return (a>b)-(a<b)
def compare_dyadics(a,b):
 ma,ea=map(int,a);mb,eb=map(int,b);e=min(ea,eb)
 aa,bb=ma<<(ea-e),mb<<(eb-e)
 return (aa>bb)-(aa<bb)
def inside(bounds,lo,hi):
 assert lo<=hi and compare_dyadics(bounds[0],bounds[1])<=0
 return compare_to_units(bounds[0],lo)>=0 and compare_to_units(bounds[1],hi)<=0
def positive_upper_within(bounds,budget):
 assert compare_dyadics(bounds[0],(0,0))>=0 and compare_dyadics(bounds[0],bounds[1])<=0
 return compare_to_units(bounds[1],budget)<=0

def replay_base():
 digest=hashlib.sha256(SEED.encode('ascii')).digest();chosen=[]
 for k in range(0,len(digest),4):
  v=int.from_bytes(digest[k:k+4],'big')%7809
  if v not in chosen:chosen.append(v)
  if len(chosen)==2:break
 assert len(chosen)==2
 return sorted({0,7808,*chosen})
def array_manifest(arrays):
 result={}
 for name in sorted(arrays):
  a=np.ascontiguousarray(arrays[name]);assert a.dtype==np.dtype('float64') and np.isfinite(a).all(),name
  if name.endswith(('_rad','_rem')):assert (a>=0).all(),name
  result[name]={'dtype':a.dtype.str,'shape':list(a.shape),'sha256':hashlib.sha256(a.tobytes(order='C')).hexdigest()}
 return result

def current_pins():
 paths=dict(PATHS)
 for p in sorted((DIR/'code').glob('*.py')):paths['code/'+p.name]=p
 for name in ('PROOF.md','ADDENDUM.md','OPTIMIZATION.md'):
  p=DIR/name
  if p.exists():paths[name]=p
 paths['proof_first']=OUT/'proof_first.json'
 hashes={name:{'path':str(p),'sha256':sha(p)} for name,p in paths.items()}
 for name,value in EXPECTED.items():assert hashes[name]['sha256']==value,name
 assert hashes['scalars']['sha256']==load(PATHS['scalar_checks'])['array_sha256']
 assert hashes['PROOF.md']['sha256']==load(OUT/'proof_first.json')['proof_sha256']
 return hashes

def runtime():
 return {'python':sys.version,'numpy':np.__version__,'python_flint':flint.__version__,'mpmath':mpmath.__version__,'platform':platform.platform(),'libc':list(platform.libc_ver())}

class Data:
 def __init__(self):
  part=load(PATHS['partition']);self.points=[];self.parents=[];last=None
  for index,sp in enumerate(part['spans']):
   left,right=Fraction(sp['a_exact']),Fraction(sp['b_exact']);count=sp['count']
   assert isinstance(count,int) and count>0 and left<right and sp['first_cell']==len(self.points)
   if last is not None:assert left==last,'parent gap'
   self.points.extend(left+(right-left)*j/count for j in range(count));self.parents.extend([index]*count);last=right
  self.points.append(last)
  assert len(part['spans'])==1558 and len(self.points)==7810 and len(self.parents)==7809
  assert all(a<b for a,b in zip(self.points,self.points[1:]))
  with np.load(PATHS['green']) as f:
   self.arrays={k:f[k] for k in ('T_mid','T_rad','A_mid','A_rad','B_mid','B_rad','tb','tb_rad')}
  with np.load(PATHS['scalars']) as f:self.scalars=f['middle']
  assert self.scalars.shape==(7809,36)
  for name,a in self.arrays.items():
   shape=(7809,8,260) if name.startswith('T_') else (7810,261) if name.startswith(('A_','B_')) else (7810,)
   assert a.shape==shape and a.dtype==np.float64 and np.isfinite(a).all(),name
   if name.endswith('_rad'):assert (a>=0).all(),name
  assert self.scalars.dtype==np.float64 and np.isfinite(self.scalars).all()
  # This exact check supplies both endpoints of every canonical finite cell.
  for i,p in enumerate(self.points):
   m=Fraction(float(self.arrays['tb'][i]));r=Fraction(float(self.arrays['tb_rad'][i]));assert r>=0 and m-r<=p<=m+r
  sys.path.insert(0,str(SOURCE))
  from cert_flow import FlowCertifier
  from midrad import MR
  self.MR=MR;self.producer=FlowCertifier.__new__(FlowCertifier)
  self.producer.M=260;self.producer.Nf=261;self.producer.Q=12;self.producer.n=np.arange(1,262,dtype=float)
 def cell(self,i):
  assert 0<=i<7809
  v=self.scalars[i];h=Fraction(float(v[0]));elo=Fraction(float(v[1]))-Fraction(float(v[2]));ehi=Fraction(float(v[1]))+Fraction(float(v[2]))
  assert 0<self.points[i+1]-self.points[i]<=h and 522*h<1 and 0<elo<=ehi
  num=(h.numerator*(1<<40)+h.denominator-1)//h.denominator;wide=Fraction(num,1<<40)
  assert h<=wide
  # Producer precision is part of the candidate, unrelated to our interval engines.
  ctx.prec=128;d=self.arrays;MR=self.MR
  T=MR(d['T_mid'][i],d['T_rad'][i]);A=MR(d['A_mid'][i],d['A_rad'][i]);B=MR(d['B_mid'][i],d['B_rad'][i]);E=MR(v[1],v[2])
  P,R,_=self.producer.psi_tms(float(h),E,[(0.0,T)],A,B)
  forcing,_=self.producer.f_terms_from_a([(0.0,T)]);assert len(forcing)==1 and float(forcing[0][0].m)==0 and float(forcing[0][0].r)==0
  F=forcing[0][1]
  arrays={'P_mid':P.c.m,'P_rad':P.c.r,'P_rem':P.r,'R_mid':R.c.m,'R_rad':R.c.r,'R_rem':R.r,
   'F_mid':F.m,'F_rad':F.r,'A_mid':A.m,'A_rad':A.r,'B_mid':B.m,'B_rad':B.r,'T_mid':T.m,'T_rad':T.r,'scalar':v}
  manifest=array_manifest(arrays)
  for name in ('P_mid','P_rad','R_mid','R_rad'):assert arrays[name].shape==(261,13)
  for name in ('F_mid','F_rad'):assert arrays[name].shape==(261,8)
  for name in ('P_rem','R_rem','A_mid','A_rad','B_mid','B_rad'):assert arrays[name].shape==(261,)
  return {'i':i,'a':self.points[i],'b':self.points[i+1],'h':h,'wide':wide,'elo':elo,'ehi':ehi,'arrays':arrays,'array_manifest':manifest}

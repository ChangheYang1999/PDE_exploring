from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import ast,struct,pickle,io,json,hashlib,sys,zipfile,math
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_jump_rank'
def check(v,s):
 if not v:raise ValueError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class DT:
 def __init__(self,code,*args):self.code=code;self.endian='<'
 def __setstate__(self,state):self.endian=state[1]
class AR:
 def __setstate__(self,s):
  ver,shape,dt,order,blob=s;check(ver==1 and isinstance(shape,tuple) and len(shape)==1 and shape[0]<10000 and dt.code=='f8' and dt.endian in ('<','=','>') and len(blob)==8*shape[0],'array state')
  self.values=struct.unpack(dt.endian+'d'*shape[0],blob)
 def __iter__(self):return iter(self.values)
 def __len__(self):return len(self.values)
 def __getitem__(self,i):return self.values[i]
def recon(cls,shape,code):
 check(cls is AR and shape==(0,) and code==b'b','reconstruct signature');return AR()
def scalar(dt,blob):
 check(dt.code=='f8' and dt.endian in ('<','=','>') and len(blob)==8,'scalar');return struct.unpack(dt.endian+'d',blob)[0]
class Reader(pickle.Unpickler):
 globals=[]
 def find_class(self,m,n):
  self.globals.append([m,n]);allowed={('numpy','dtype'):DT,('numpy','ndarray'):AR}
  for mod in ['numpy._core.multiarray','numpy.core.multiarray']:allowed[mod,'_reconstruct']=recon;allowed[mod,'scalar']=scalar
  check((m,n) in allowed,'unapproved global');return allowed[m,n]
def dy(x):
 bits=struct.unpack('>Q',struct.pack('>d',x))[0];sign=-1 if bits>>63 else 1;exp=(bits>>52)&2047;mant=bits&((1<<52)-1);check(exp!=2047,'finite dyadic')
 if exp:mant+=1<<52;power=exp-1075
 else:power=-1074
 return F(sign*mant*(1<<max(power,0)),1<<max(-power,0))
def enc(x):return str(x.numerator)+'/'+str(x.denominator)
def poly(c,x):return sum((dy(z)*x**j for j,z in enumerate(c)),F(0))
a=json.loads((D/'evidence/compute.json').read_text());b=json.loads((D/'evidence/independent.json').read_text());pins={};copies=0
for n,h in b['files'].items():check(sha(B/n)==h,'second pin');pins[n]=h
for rec in b['records']:
 meta=Reader(io.BytesIO((B/rec['source']).read_bytes())).load();cols=meta['cols']
 for row in rec['pivots']:
  ids=row['column_indices'];base=cols[ids[0]][1]
  for mode,idx in enumerate(ids):
   mm,pcs,lab=cols[idx];check(mm==mode and lab==row['label'] and len(pcs)==len(base),'mode, label and exact piece count')
   for pp,qq in zip(pcs,base,strict=True):
    check(len(pp)==len(qq)==4 and len(pp[3])==len(qq[3]),'piece/degree structure')
    for x,y in zip(pp[:3],qq[:3],strict=True):check(struct.pack('>d',x)==struct.pack('>d',y),'endpoint bits')
    for x,y in zip(pp[3],qq[3],strict=True):check(struct.pack('>d',x)==struct.pack('>d',y),'coefficient bits')
   copies+=1
 # Recalculate exact diagonal product modulo the tested prime from primary fractions.
 aa=next(x for x in a['records'] if x['source']==rec['source']);prod=1
 for row in aa['pivots']:
  v=F(row['diagonal_exact']);prod=prod*v.numerator*pow(v.denominator,-1,b['prime'])%b['prime']
 check(prod==rec['diagonal_product_mod_prime']!=0,'all exact diagonals modular product')
for p in [D/'evidence/independent.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
summary={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_STRUCTURED_RADIAL_COPY_AND_DIAGONAL_PRODUCT_AUDIT','copies_checked':copies,'records':[{k:v for k,v in r.items() if k!='pivots'}|{'first_pivot':r['pivots'][0],'last_pivot':r['pivots'][-1]} for r in b['records']],'reported_counts':a['reported_counts'],'files':pins,'scope':'This adds explicit per-piece/degree delimiters to the independent bit-copy check. All original results retained unchanged.'};p=D/'evidence/summary.json';check(not p.exists(),'immutable');p.write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({'utc':summary['utc'],'status':summary['status'],'copies':copies,'pins':len(pins)}))

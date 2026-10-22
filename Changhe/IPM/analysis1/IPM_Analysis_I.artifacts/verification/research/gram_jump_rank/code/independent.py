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
V=B/'research/gram_internal_jumps';prime=1000000007
check(all(prime%d for d in range(2,math.isqrt(prime)+1)),'trial division primality')
def dm(x):
 bits=struct.unpack('>Q',struct.pack('>d',x))[0];s=-1 if bits>>63 else 1;e=(bits>>52)&2047;n=bits&((1<<52)-1);check(e!=2047,'finite')
 if e:n+=1<<52;power=e-1075
 else:power=-1074
 return (s*n*pow(2,power,prime))%prime
records=[]
def signature(pcs):return b''.join(struct.pack('>d',x) for a,b,al,c in pcs for x in [a,b,al,*c])
for stem in ['c2raw_M16_s16_p4_cols','c2raw_M24_s8_p4_cols']:
 p=V/'sources'/(stem+'.pkl');meta=Reader(io.BytesIO(p.read_bytes())).load();cols=meta['cols'];lo,hi=map(dy,[meta['cells'][0],meta['cells'][-1]]);modes=sorted(set(m for m,pc,lab in cols));check(modes==list(range(len(modes))),'modes');M=len(modes);selected=[]
 for idx,(m,pcs,lab) in enumerate(cols):
  if m!=0 or not lab.startswith('sp') or not pcs:continue
  if not all(lo<dy(a)<dy(b)<hi and dy(al)==0 for a,b,al,c in pcs):continue
  check(all(dy(pcs[i][1])<=dy(pcs[i+1][0]) for i in range(len(pcs)-1)),'ordered disjoint');check(dy(pcs[0][3][0])==0,'continuous zero initial support trace');t=pcs[0][1];left=F(0);right=F(0);lm=0;rm=0
  for a,b,al,c in pcs:
   if dy(b)==dy(t):
    left+=poly(c,dy(t)-dy(a));x=(dm(t)-dm(a))%prime;lm=(lm+sum(dm(cc)*pow(x,j,prime) for j,cc in enumerate(c)))%prime
   if dy(a)==dy(t):right+=dy(c[0]);rm=(rm+dm(c[0]))%prime
  diag=right-left;mod=(rm-lm)%prime;check(mod!=0 and diag.numerator*pow(diag.denominator,-1,prime)%prime==mod,'modular pivot agrees exact direct sum')
  copies=[]
  for mode in modes:
   matches=[(j,pc) for j,(m,pc,ll) in enumerate(cols) if m==mode and ll==lab];check(len(matches)==1 and signature(matches[0][1])==signature(pcs),'bit-exact radial copies');copies.append(matches[0][0])
  selected.append((dy(t),{'label':lab,'column_indices':copies,'pivot_hex':t.hex(),'pivot_exact':enc(dy(t)),'diagonal_exact':enc(diag),'diagonal_mod_prime':mod,'support_start_hex':pcs[0][0].hex(),'support_end_hex':pcs[-1][1].hex()},pcs))
 selected.sort(key=lambda z:z[0]);check(len(set(z[0] for z in selected))==len(selected),'distinct first break pivots');N=len(selected);zeros=0;det=1
 for j,(t,rec,pcs) in enumerate(selected):
  det=det*rec['diagonal_mod_prime']%prime
  for s,_,_ in selected[:j]:
   check(s<t,'ordered upper entry');check(all(dy(a)>=t for a,b,al,c in pcs[1:]),'later pieces begin after first break');check(dy(pcs[0][3][0])==0,'initial value zero');zeros+=1
 check(det!=0,'modular triangular determinant')
 rank=M*N;n=len(cols);caps={'Fminus':n+2-rank,'Fminus_noJ':n+1-rank,'free':n+2+M-rank,'free_noJ':n+1+M-rank};records.append({'source':str(p.relative_to(B)),'source_sha256':sha(p),'M':M,'N':N,'selected_coordinate_columns':rank,'n_function_columns':n,'tested_upper_zeros':zeros,'conforming_dimension_upper_bounds':caps,'section_column_counts':{name:cap+rank for name,cap in caps.items()},'diagonal_product_mod_prime':det,'pivots':[z[1] for z in selected]})
# This engine has not read the primary calculation until here.
a=json.loads((D/'evidence/compute.json').read_text());check(a['status']=='PASS_EXACT_TRIANGULAR_JUMP_RANK_AND_REPORTED_COUNT_COMPARISON','primary status')
for x,y in zip(records,a['records'],strict=True):
 for k in ['source','source_sha256','M','N','selected_coordinate_columns','n_function_columns','tested_upper_zeros','conforming_dimension_upper_bounds','section_column_counts']:check(x[k]==y[k],'independent record '+k)
 for xx,yy in zip(x['pivots'],y['pivots'],strict=True):
  for k,v in yy.items():check(xx[k]==v,'independent pivot '+k)
reports=[]
for item in a['reported_counts']:
 p=B/item['file'];check(sha(p)==item['sha256'],'report hash');z=json.loads(p.read_text());check(z['mode']=='H1m' and z['Mh']==16 and z['stride']==16,'H1 report');caps=records[0]['conforming_dimension_upper_bounds']
 for name,sec in z['sections'].items():check(sec['ncol']==records[0]['section_column_counts'][name] and sec['n_kept']==item['retained'][name]>caps[name],'reported count')
 reports.append({'file':item['file'],'status':'COUNT_GREATER_THAN_CONFORMING_DIMENSION_UPPER_BOUND','retained':item['retained']})
pins={}
for n,h in a['files'].items():check(sha(B/n)==h,'input pin');pins[n]=h
for p in [D/'evidence/compute.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_STRUCTURAL_ZEROS_MODULAR_RANK_AND_DIRECT_POWER_SUM','prime':prime,'prime_check':'Exact trial division through floor(sqrt(prime)); no probabilistic test','method':'No NumPy; data-only pickle proxies; direct binary64 power sums and independent modular dyadic evaluation. Upper zeros follow from first-piece continuity before the strictly ordered first break.','records':records,'reported_counts':reports,'files':pins,'scope':'Dimension bound for exact encoded function spans; no actual Q rank or reconstruction error certified.'};p=D/'evidence/independent.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'records':[{k:r[k] for k in ['M','N','diagonal_product_mod_prime','tested_upper_zeros','conforming_dimension_upper_bounds']} for r in records],'pins':len(pins)}))

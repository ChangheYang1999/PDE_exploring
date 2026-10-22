from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import ast,struct,pickle,io,json,hashlib,sys,zipfile,math
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_conforming_repair'
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
from mpmath import iv
iv.dps=120
L=F(8614738245908811,1125899906842624);k=F(1615536043799051,9007199254740992)
def I(x):x=F(x);return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def tupleq(v):s,n,e,bc=v;return F((-1 if s else 1)*n)*F(2)**e
def ibox(v):return [tupleq(x) for x in v._mpi_]
def weight(t):z=iv.exp(I(2*t));return z*iv.exp(I(F(3,2)-k)*iv.log(1+z/I(L*L)))
def p2int(c,w):return sum((dy(ci)*dy(cj)*w**(i+j+1)/F(i+j+1) for i,ci in enumerate(c) for j,cj in enumerate(c)),F(0))
def affsquare(l,r,w):return w*(l*l+l*r+r*r)/3
V=B/'research/gram_internal_jumps';records=[];traces=0
for stem in ['c2raw_M16_s16_p4_cols','c2raw_M24_s8_p4_cols']:
 source=V/'sources'/(stem+'.pkl');meta=Reader(io.BytesIO(source.read_bytes())).load();cols=meta['cols'];lo,hi=dy(meta['cells'][0]),dy(meta['cells'][-1]);M=len(set(m for m,pcs,lab in cols));selected=[];cache={};maxD=F(0);maxE=F(0);maxR=F(0)
 for ci,(m,pcs,lab) in enumerate(cols):
  if m!=0 or not lab.startswith('sp') or not pcs:continue
  if not all(lo<dy(a)<dy(b)<hi and dy(al)==0 for a,b,al,c in pcs):continue
  check(all(dy(pcs[j][1])==dy(pcs[j+1][0]) for j in range(len(pcs)-1)),'consecutive pieces');check(len(pcs[0][3])>=3 and dy(pcs[0][3][-1])!=0,'nonlinear first piece');vals=[F(0)]
  for j in range(1,len(pcs)):vals.append((poly(pcs[j-1][3],dy(pcs[j-1][1])-dy(pcs[j-1][0]))+dy(pcs[j][3][0]))/2)
  vals.append(F(0));U=I(0);VV=I(0);rpcs=[]
  for j,(a,b,al,c) in enumerate(pcs):
   a,b=dy(a),dy(b);w=b-a;left=vals[j]-dy(c[0]);right=vals[j+1]-poly(c,w);slope=(right-left)/w
   check(dy(c[0])+left==vals[j] and poly(c,w)+left+slope*w==vals[j+1],'repaired traces');traces+=2
   ei=affsquare(left,right,w)+affsquare(3*left+slope,3*right+slope,w);vv=p2int(c,w);check(ei>=0 and vv>0,'positive exact integrals')
   for t in [a,b]:
    if t not in cache:cache[t]=weight(t)
   U+=cache[b]*I(ei);VV+=cache[a]*I(vv);maxD=max(maxD,abs(left),abs(right));maxE=max(maxE,abs(slope));rpcs.append({'a_exact':enc(a),'b_exact':enc(b),'beta_left':enc(vals[j]),'beta_right':enc(vals[j+1]),'correction_constant':enc(left),'correction_linear':enc(slope),'exact_error_integral':enc(ei),'exact_original_square_integral':enc(vv)})
  ubox=ibox(U);vbox=ibox(VV);check(0<ubox[0]<=ubox[1] and 0<vbox[0]<=vbox[1],'positive interval denominator');ratio=iv.sqrt(U/VV);rb=ibox(ratio);maxR=max(maxR,rb[1]);selected.append({'column_index':ci,'label':lab,'pieces':rpcs,'U_iv120':list(map(enc,ubox)),'V_iv120':list(map(enc,vbox)),'sqrt_ratio_iv120':list(map(enc,rb))})
 starts=[F(row['pieces'][0]['a_exact']) for row in selected];check(starts==sorted(starts) and len(set(starts))==len(starts),'independent support ordering');records.append({'source':str(source.relative_to(B)),'M':M,'N':len(selected),'independent_repaired_functions':M*len(selected),'columns':selected,'max_coefficient_error_exact':enc(maxD),'max_t_derivative_error_exact':enc(maxE),'endpoint_weight_count':len(cache),'max_ratio_upper':enc(maxR)})
# All repairs, polynomial integrals and interval ratios completed independently above.
a=json.loads((D/'evidence/compute.json').read_text());check(a['status']=='PASS_EXACT_AFFINE_CONTINUOUS_REPAIR_AND_ARB_BROKEN_ENERGY_BOUNDS','first method status');check(traces==a['exact_repaired_trace_checks'],'trace count')
for x,y in zip(records,a['records'],strict=True):
 for key in ['source','M','N','independent_repaired_functions','max_coefficient_error_exact','max_t_derivative_error_exact','endpoint_weight_count']:check(x[key]==y[key],'record agreement '+key)
 for xx,yy in zip(x['columns'],y['columns'],strict=True):
  for key in ['column_index','label','pieces']:check(xx[key]==yy[key],'exact repair agreement '+key)
  check(F(xx['sqrt_ratio_iv120'][1])<F(y['public']['uniform_single_column_relative_broken_energy_upper']),'independent uniform ratio ceiling')
 check(F(x['max_coefficient_error_exact'])<F(y['public']['uniform_coefficient_sup_error_upper']) and F(x['max_t_derivative_error_exact'])<F(y['public']['uniform_t_derivative_sup_error_upper']),'strict derivative/value ceilings');x['public']=y['public']
pins={}
for n,h in a['files'].items():check(sha(B/n)==h,'primary pin');pins[n]=h
for p in [Path(__file__),D/'evidence/compute.json']:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_BIT_DECODE_ENDPOINT_MOMENTS_AND_IV_REPAIR_BOUNDS','k_exact':enc(k),'L_exact':enc(L),'exact_repaired_trace_checks':traces,'records':records,'files':pins,'scope':'Single-column broken-energy comparison only; no weak X distance from raw functions, no arbitrary-combination relative bound, operator or matrix transfer.'};p=D/'evidence/independent.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'traces':traces,'records':[{k:r[k] for k in ['M','N','public']} for r in records]}))

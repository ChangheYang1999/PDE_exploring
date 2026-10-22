from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,io,json,pickle,struct,sys
from mpmath import iv
assert not sys.flags.optimize
iv.dps=120
B=Path(__file__).resolve().parents[3];D=B/'research/gram_c2_repair'
def check(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
class DT:
 def __init__(self,code,*args):self.code=code;self.endian='<'
 def __setstate__(self,s):self.endian=s[1]
class AR:
 def __setstate__(self,s):
  ver,shape,dt,order,blob=s;check(ver==1 and isinstance(shape,tuple) and len(shape)==1 and shape[0]<10000 and dt.code=='f8' and dt.endian in ('<','=','>') and len(blob)==8*shape[0],'array state');self.values=struct.unpack(dt.endian+'d'*shape[0],blob)
 def __iter__(self):return iter(self.values)
 def __len__(self):return len(self.values)
 def __getitem__(self,i):return self.values[i]
def recon(cls,shape,code):check(cls is AR and shape==(0,) and code==b'b','reconstruction');return AR()
def scalar(dt,blob):check(dt.code=='f8' and dt.endian in ('<','=','>') and len(blob)==8,'scalar');return struct.unpack(dt.endian+'d',blob)[0]
class Reader(pickle.Unpickler):
 def find_class(self,m,n):
  allow={('numpy','dtype'):DT,('numpy','ndarray'):AR}
  for module in ('numpy._core.multiarray','numpy.core.multiarray'):allow[module,'_reconstruct']=recon;allow[module,'scalar']=scalar
  check((m,n) in allow,'pickle global');return allow[m,n]
def dy(x):
 bits=struct.unpack('>Q',struct.pack('>d',x))[0];sign=-1 if bits>>63 else 1;ex=(bits>>52)&2047;ma=bits&((1<<52)-1);check(ex!=2047,'finite dyadic')
 if ex:ma+=1<<52;power=ex-1075
 else:power=-1074
 return F(sign*ma*(1<<max(power,0)),1<<max(-power,0))
def enc(q):return str(q.numerator)+'/'+str(q.denominator)
def falling(j,q):
 z=1
 for n in range(q):z*=j-n
 return z
def direct(c,t,q=0):return sum((falling(j,q)*c[j]*t**(j-q) for j in range(q,len(c))),F(0))
def energy_unit(c):return sum((ci*cj/F(i+j+1) for i,ci in enumerate(c) for j,cj in enumerate(c)),F(0))
def I(q):q=F(q);return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def tq(t):s,m,e,bc=t;return F((-1 if s else 1)*m)*F(2)**e
def ibox(v):return [tq(x) for x in v._mpi_]
H=[[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,F(1,2),F(-3,2),F(3,2),F(-1,2)],[0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,F(1,2),-1,F(1,2)]]
H=[list(map(F,row)) for row in H];basischecks=0
for j,h in enumerate(H):
 for side in (0,1):
  for q in range(3):check(direct(h,F(side),q)==F(j==3*side+q),'unit Hermite Kronecker jet');basischecks+=1
# Fixed exact parameters from the already defined background; primary outputs are read only after this engine computes every new repair and bound.
L=F(8614738245908811,1125899906842624);k=F(1615536043799051,9007199254740992)
def weight(t):z=iv.exp(I(2*t));return z*iv.exp(I(F(3,2)-k)*iv.log(1+z/I(L*L)))
records=[];tot={'columns':0,'pieces':0,'endpoint_jet_values':0};pins={}
for stem in ('c2raw_M16_s16_p4_cols','c2raw_M24_s8_p4_cols'):
 path=B/'research/gram_internal_jumps/sources'/(stem+'.pkl');meta=Reader(io.BytesIO(path.read_bytes())).load();lo,hi=dy(meta['cells'][0]),dy(meta['cells'][-1]);cols=meta['cols'];M=len(set(m for m,pcs,lab in cols));outcols=[];cache={};maxratio=F(0);starts=[]
 for ci,(mode,pcs,label) in enumerate(cols):
  if mode!=0 or not label.startswith('sp') or not pcs:continue
  if not all(lo<dy(a)<dy(b)<hi and dy(alpha)==0 for a,b,alpha,c in pcs):continue
  raw=[]
  for a,b,alpha,c in pcs:
   aa,bb=dy(a),dy(b);cc=[dy(q) for q in c];raw.append((aa,bb,cc,[[direct(cc,t,q) for q in range(3)] for t in (F(0),bb-aa)]))
  check(all(raw[j-1][1]==raw[j][0] for j in range(1,len(raw))),'common pieces');check(len(raw[0][2])>=7 and raw[0][2][-1]!=0,'degree above5');starts.append(raw[0][0]);target=[[F(0)]*3]+[[(raw[j-1][3][1][q]+raw[j][3][0][q])/2 for q in range(3)] for j in range(1,len(raw))]+[[F(0)]*3];U=I(0);V=I(0);outpcs=[]
  for j,(aa,bb,cc,jets) in enumerate(raw):
   w=bb-aa;e=[w**q*(target[j+side][q]-jets[side][q]) for side in (0,1) for q in range(3)]
   dunit=[sum((e[n]*H[n][power] for n in range(6)),F(0)) for power in range(6)];d=[z/w**power for power,z in enumerate(dunit)]
   for side,t in enumerate((F(0),w)):
    for q in range(3):check(direct(cc,t,q)+direct(d,t,q)==target[j+side][q],'exact reconstructed repaired jet');tot['endpoint_jet_values']+=1
   combo=[3*dunit[z]+(z+1)*dunit[z+1]/w if z<5 else 3*dunit[z] for z in range(6)];ei=w*(energy_unit(dunit)+energy_unit(combo));vi=w*energy_unit([v*w**power for power,v in enumerate(cc)]);check(ei>=0 and vi>0,'unit interval energy positivity')
   for t in (aa,bb):
    if t not in cache:cache[t]=weight(t)
   U+=cache[bb]*I(ei);V+=cache[aa]*I(vi);outpcs.append({'a_exact':enc(aa),'b_exact':enc(bb),'target_left_jet':list(map(enc,target[j])),'target_right_jet':list(map(enc,target[j+1])),'correction_coefficients':list(map(enc,d)),'exact_error_integral':enc(ei),'exact_original_square_integral':enc(vi)});tot['pieces']+=1
  vb=ibox(V);ub=ibox(U);check(0<vb[0]<=vb[1] and 0<ub[0]<=ub[1],'positive interval ratio');rb=ibox(iv.sqrt(U/V));maxratio=max(maxratio,rb[1]);tot['columns']+=1;outcols.append({'column_index':ci,'label':label,'first_piece_degree':len(raw[0][2])-1,'pieces':outpcs,'U_iv120':list(map(enc,ub)),'V_iv120':list(map(enc,vb)),'sqrt_ratio_iv120':list(map(enc,rb))})
 check(starts==sorted(starts) and len(starts)==len(set(starts)) and all(-5<s<9 for s in starts),'starts');records.append({'source':str(path.relative_to(B)),'M':M,'N':len(outcols),'independent_repaired_functions':M*len(outcols),'columns':outcols,'endpoint_weight_count':len(cache),'max_ratio_upper_exact':enc(maxratio)})
# Primary result is inspected only after all independent computation has completed.
p=D/'evidence/compute.json';a=json.loads(p.read_text());check(a['status']=='PASS_EXACT_C2_HERMITE_LINEAR_SYSTEM_AND_ARB512_BROKEN_NORM_BOUNDS','primary status');check(F(a['L_exact'])==L and F(a['k_exact'])==k,'parameter agreement');old=json.loads((B/'research/gram_conforming_repair/evidence/compute.json').read_text())
for xx,yy,zz in zip(records,a['records'],old['records'],strict=True):
 for key in ('source','M','N','independent_repaired_functions','endpoint_weight_count'):check(xx[key]==yy[key],'record agreement '+key)
 for c,d in zip(xx['columns'],yy['columns'],strict=True):
  for key in ('column_index','label','first_piece_degree','pieces'):check(c[key]==d[key],'all coefficient and integral agreement '+key)
  check(F(c['sqrt_ratio_iv120'][1])<F(yy['public']['single_column_relative_broken_norm_error_upper']),'independent strict ratio ceiling')
 delta0=F(zz['public']['uniform_single_column_relative_broken_energy_upper']);delta2=F(yy['public']['single_column_relative_broken_norm_error_upper']);xd=F(yy['public']['single_column_relative_X_distance_from_C0_upper']);check(0<delta0<1 and (delta0+delta2)/(1-delta0)<xd,'true X-distance ceiling');xx['public']=yy['public']
check(tot=={'columns':277,'pieces':2216,'endpoint_jet_values':13296},'complete scope counts')
for n,h in a['files'].items():check(sha(B/n)==h,'all primary dependencies '+n);pins[n]=h
for p in (p,Path(__file__)):pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_NUMPY_FREE_IEEE_HERMITE_BASIS_HILBERT_MOMENTS_AND_IV120','unit_Hermite_jet_checks':basischecks,'totals':tot,'records':records,'files':dict(sorted(pins.items())),'scope':'All repaired coefficients, endpoint jets and exact moments matched independently. New C2,1 family; no old matrix transfer or IPM endpoint.'};p=D/'evidence/independent.json';check(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'unit_Hermite_jet_checks':basischecks,'totals':tot,'records':[{k:r[k] for k in ('M','N','public')} for r in records]}))

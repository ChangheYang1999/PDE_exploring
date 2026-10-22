"""Two independent exact source-functional calculations for three saved v2 vectors."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from collections import Counter
import ast, hashlib, io, json, math, os, pickle, struct, sys, time, zipfile
import numpy as np
from flint import fmpq as Q, arb, ctx
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=256
iv.dps=100
B=Path(__file__).resolve().parents[3]; D=B/'research/projection_source_constraints'
def need(v,s):
 if not v: raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def load(p):return json.loads(Path(p).read_text())
class Reader(pickle.Unpickler):
 def find_class(self,m,n):
  table={('numpy','ndarray'):np.ndarray,('numpy','dtype'):np.dtype}
  for prefix in ['numpy.core.multiarray','numpy._core.multiarray']:
   table[prefix,'scalar']=np._core.multiarray.scalar;table[prefix,'_reconstruct']=np._core.multiarray._reconstruct
  need((m,n) in table,'unsupported pickle global');return table[m,n]
def ieee(w):
 s=-1 if w>>63 else 1;e=(w>>52)&2047;m=w&((1<<52)-1);need(e!=2047,'nonfinite word')
 return Q(s*(m if e==0 else m+(1<<52)))*Q(2)**(-1074 if e==0 else e-1075)
def qr(v):return ieee(int.from_bytes(struct.pack('>d',float(v)),'big'))
def npy(raw):
 need(raw[:6]==b'\x93NUMPY' and tuple(raw[6:8]) in [(1,0),(2,0),(3,0)],'NPY magic/version')
 off=10 if raw[6]==1 else 12;n=int.from_bytes(raw[8:off],'little');need(off+n<=len(raw),'complete header')
 node=ast.parse(raw[off:off+n].decode('utf8' if raw[6]==3 else 'latin1').strip(),mode='eval').body
 need(isinstance(node,ast.Dict) and len(node.keys)==3,'three distinct header keys')
 keys=[ast.literal_eval(k) for k in node.keys];need(len(set(keys))==3 and set(keys)=={'descr','shape','fortran_order'},'header key set')
 h=ast.literal_eval(node);need(type(h['shape']) is tuple and all(type(x) is int and x>=0 for x in h['shape']) and type(h['fortran_order']) is bool,'shape/order types')
 desc=h['descr'];need(type(desc) is str and len(desc)>=3,'dtype text');p=raw[off+n:];cnt=math.prod(h['shape'])
 if desc=='|b1':
  need(len(p)==cnt and all(x in [0,1] for x in p),'bool payload');v=[bool(x) for x in p]
 else:
  need(desc[0] in '<>' and desc[1] in 'fiU','permitted fixed dtype');endian='little' if desc[0]=='<' else 'big'
  if desc[1] in 'fi':
   need(desc[2:]=='8' and len(p)==cnt*8,'numeric payload')
   words=[int.from_bytes(p[i:i+8],endian,signed=desc[1]=='i') for i in range(0,len(p),8)]
   v=[ieee(w) for w in words] if desc[1]=='f' else words
  else:
   width=int(desc[2:]);need(width>0 and len(p)==4*width*cnt,'unicode payload')
   v=[p[i:i+4*width].decode('utf-32-le' if endian=='little' else 'utf-32-be').rstrip('\0') for i in range(0,len(p),4*width)]
 return h,v

def member(p,name):
 with zipfile.ZipFile(p) as z:
  need(z.namelist().count(name+'.npy')==1,'unique NPZ member');return npy(z.read(name+'.npy'))
def fr(v):
 need(type(v) in [float,np.float64] and math.isfinite(v),'binary64 finite scalar');return F.from_float(float(v))
def ep(v,convert):
 need(type(v) in [float,np.float64] and not math.isnan(v),'endpoint scalar');return float(v) if math.isinf(v) else convert(v)
def horner(c,x):
 p=F(0)
 for v in reversed(c):p=p*x+v
 return p

def arbend(a):
 need(a.rad()==0 and a.is_finite(),'finite exact Arb endpoint');m,e=a.man_exp();return F(int(m))*F(2)**int(e)
def ivends(a):
 out=[]
 for s,m,e,bc in a._mpi_:
  need(bc>=0,'finite iv endpoint');out.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
 return out
start=utc();tick=time.monotonic();binding=load(D/'evidence/source_binding.json');proof=load(D/'evidence/proof_first.json')
need(sha(D/'PROOF.md')==proof['proof_sha256'] and sha(D/'evidence/source_binding.json')==proof['source_binding_sha256'],'proof/source identity')
need(datetime.fromisoformat(proof['utc'])<datetime.fromtimestamp(Path(__file__).stat().st_mtime,timezone.utc)<datetime.fromisoformat(start),'proof before code before run')
pins=dict(binding['files'])
for n,h in pins.items():need(sha(B/n)==h,'prior pin '+n)
cols=Reader(io.BytesIO((B/binding['column_path']).read_bytes())).load()['cols'];need(len(cols)==1953 and sha(B/binding['column_path'])==binding['column_sha256'],'frozen columns')
J=[fr(float.fromhex(x)) for x in binding['joins_hex']];JQ=[]
for name,j in zip(['tmin','t0'],J,strict=True):
 h,v=member(B/binding['source_vector_path'],name);need(h['shape']==() and h['descr'][1:]=='f8' and len(v)==1,'source join metadata')
 need(v[0]==Q(j.numerator,j.denominator),'independent stored join equality');JQ.append(v[0])
counts=Counter();TA=[];TB=[];piecesA=[];piecesB=[];modes=[];labels=[];types=Counter()
for mode,pcs,label in cols:
 need(type(mode) in [int,np.int64] and 0<=int(mode)<16,'angular index');modes.append(int(mode));labels.append(label)
 pa=[];pb=[]
 for a,b,al,c in pcs:
  need(isinstance(c,np.ndarray) and c.dtype==np.dtype('float64') and c.ndim==1 and 1<=len(c)<=8,'coefficient array type')
  for v in [a,b,al,*c]:
   need(type(v) in [float,np.float64],'source scalar type');types[type(v).__module__+'.'+type(v).__name__]+=1
  aa,bb=ep(a,fr),ep(b,fr);aq,bq=ep(a,qr),ep(b,qr)
  need(aa<bb and aa!=math.inf and bb!=-math.inf and not(aa==-math.inf and bb==math.inf),'support')
  pa.append((aa,bb,fr(al),[fr(v) for v in c]));pb.append((aq,bq,qr(al),[qr(v) for v in c]))
  counts['guarded_piece_scalars']+=3+len(c)
 for i,p in enumerate(pa):
  for q in pa[i+1:]:need(p[1]<=q[0] or q[1]<=p[0],'pairwise disjoint supports')
 aout=[];bout=[]
 for j,jq in zip(J,JQ,strict=True):
  need(sum(b==j for a,b,al,c in pa)<=1 and sum(a==j for a,b,al,c in pa)<=1,'unique one-sided endpoint')
  aa=[F(0),F(0)];bb=[Q(0),Q(0)]
  for a,b,al,c in pa:
   if b==j:sgn=1
   elif a==j:sgn=-1
   else:continue
   x=j-(b if a==-math.inf else a);need(al*x==0,'unit endpoint exponential')
   p=horner(c,x);dp=horner([i*c[i] for i in range(1,len(c))],x)
   aa[0]+=sgn*p;aa[1]+=sgn*(al*p+dp);counts['endpoint_contributions']+=1
  for a,b,al,c in reversed(pb):
   if a==jq:sgn=-1
   elif b==jq:sgn=1
   else:continue
   x=jq-b if a==-math.inf else jq-a;need(al*x==0,'alternate unit exponential')
   for i in range(len(c)-1,-1,-1):
    term=c[i]*x**i;bb[0]+=sgn*term;bb[1]+=sgn*al*term
    if i:bb[1]+=sgn*i*c[i]*x**(i-1)
  need(all(Q(v.numerator,v.denominator)==w for v,w in zip(aa,bb,strict=True)),'independent exact trace')
  aout+=aa;bout+=bb;counts['two_method_trace_equalities']+=2
 TA.append(aout);TB.append(bout)
 need(len(aout)==4,'four traces per function column')
counts['columns']=len(cols)
# Static complete source statements. This identifies the recipe, not an execution.
source=B/'research/projection_energy_distance/source/c2_Kproj.py';tree=ast.parse(source.read_text())
main=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='main_A')
ext=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='extended_cols')
imports=[x for x in tree.body if isinstance(x,ast.ImportFrom) and x.module=='c2_gram2'];need(len(imports)==1 and 'piece_jet' in [x.name for x in imports[0].names],'source evaluator import')
loops=[x for x in ast.walk(main) if isinstance(x,ast.For) and isinstance(x.target,ast.Name) and x.target.id=='gi'];need(len(loops)==1,'unique function-column loop')
need(ast.unparse(loops[0].iter)=='range(nfun)','function columns only')
need('row = np.zeros(nF)' in ast.unparse(main) and 'x = Q @ y' in ast.unparse(main),'original coordinate x and zero-filled row')
extract=ast.get_source_segment(source.read_text(),loops[0])+'\n'+ast.get_source_segment(source.read_text(),ext)+'\n'
(D/'sources/constraint_recipe.txt').write_text(extract)
records=[]
for rel,NJ,free,nf in zip(binding['projection_paths'],[0,1,1],[False,False,True],[1955,1955,1971],strict=True):
 p=B/rel
 with np.load(p,allow_pickle=False) as z:
  need(z['x'].dtype==np.dtype('float64') and z['x'].shape==(nf,) and np.isfinite(z['x']).all(),'complete finite vector')
  xa=[fr(x) for x in z['x']]
  expected_modes=modes+[-1,-1]+(list(range(16)) if free else [])
  expected_labels=labels+['KP','TAU']+(['tail%d'%i for i in range(16)] if free else [])
  need(z['col_m'].tolist()==expected_modes and z['col_label'].tolist()==expected_labels,'full original coordinate metadata')
  for name,want in [('Mh',16),('NJ',NJ),('nfun',1953),('nF',nf),('free',free)]:
   need(z[name].shape==() and z[name].item()==want,'numpy scalar metadata')
   hdr,v=member(p,name);need(hdr['shape']==() and v==[want],'independent scalar metadata')
 hdr,xb=member(p,'x');need(hdr['shape']==(nf,) and hdr['descr'][1:]=='f8' and all(Q(a.numerator,a.denominator)==b for a,b in zip(xa,xb,strict=True)),'manual coefficient equality')
 for name,want in [('col_m',expected_modes),('col_label',expected_labels)]:
  hdr,v=member(p,name);need(hdr['shape']==(nf,) and v==want,'manual entire coordinate array')
 counts['manual_vector_entries']+=nf;counts['metadata_array_entries']+=2*nf;counts['metadata_scalars']+=5
 acc=[[[F(0) for nu in range(NJ+1)] for j in range(2)] for m in range(16)]
 for i in range(1953):
  for j in range(2):
   for nu in range(NJ+1):acc[modes[i]][j][nu]+=xa[i]*TA[i][2*j+nu]
 rows=[]
 for m in range(16):
  for j in range(2):
   for nu in range(NJ+1):
    value=acc[m][j][nu];alt=sum((xb[i]*TB[i][2*j+nu] for i in range(1952,-1,-1) if modes[i]==m),Q(0))
    need(alt==Q(value.numerator,value.denominator),'independent row sum');counts['independent_row_equalities']+=1
    a=abs(value);n=a.numerator*10**30//a.denominator;lo,hi=F(n,10**30),F(n+1,10**30)
    need(lo<=a<hi and Q(n,10**30)<=abs(alt)<Q(n+1,10**30),'outward decimal both methods')
    rows.append({'mode':m,'join_index':j,'order':nu,'value_exact':str(value),'abs_decimal_lower':str(lo),'abs_decimal_upper':str(hi)})
 maximum=max(abs(F(r['value_exact'])) for r in rows);where=[{k:r[k] for k in ['mode','join_index','order']} for r in rows if abs(F(r['value_exact']))==maximum]
 ar=arb(maximum.numerator)/maximum.denominator;ae=[arbend(ar.lower()),arbend(ar.upper())]
 ie=ivends(iv.mpf(maximum.numerator)/maximum.denominator)
 need(ae[0]<=maximum<=ae[1] and ie[0]<=maximum<=ie[1],'both independent rational maximum enclosures')
 nz=sum(F(r['value_exact'])!=0 for r in rows);counts['nonzero_rows']+=nz;counts['max_interval_enclosures']+=2
 n=maximum.numerator*10**30//maximum.denominator
 records.append({'file':rel,'NJ':NJ,'free':free,'nF':nf,'rows':rows,'nonzero_rows':nz,'max_abs_exact':str(maximum),'max_abs_decimal_lower':str(F(n,10**30)),'max_abs_decimal_upper':str(F(n+1,10**30)),'maximizers':where,'arb256_max_abs':list(map(str,ae)),'iv100_max_abs':list(map(str,ie)),'later_coordinates_nonzero':sum(x!=0 for x in xa[1953:]),'source_kernel_membership':'REFUTED' if nz else 'CONFIRMED'})
need(counts['two_method_trace_equalities']==7812 and counts['independent_row_equalities']==160 and counts['manual_vector_entries']==5881 and counts['metadata_scalars']==15,'complete fixed coverage')
for p in [D/'PROOF.md',D/'evidence/source_binding.json',D/'evidence/proof_first.json',D/'sources/constraint_recipe.txt',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'end pin '+n)
out={'start_utc':start,'utc':utc(),'status':'PASS_TWO_METHOD_EXACT_SOURCE_CONSTRAINTS_ONLY','counts':dict(counts),'piece_scalar_types':dict(types),'families':records,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Explicit frozen column interpretation of three saved vectors; labels/indexes match completely, but v2 vectors lack join/pickle-hash metadata. No historical execution, physical trace, exact projection, Sobolev norm, global inverse or endpoint assertion.'}
with (D/'evidence/checks.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:out[k] for k in ['utc','status','counts','seconds']}))
print(json.dumps([{'NJ':r['NJ'],'free':r['free'],'rows':len(r['rows']),'nonzero':r['nonzero_rows'],'max':float(F(r['max_abs_exact'])),'where':r['maximizers']} for r in records]))

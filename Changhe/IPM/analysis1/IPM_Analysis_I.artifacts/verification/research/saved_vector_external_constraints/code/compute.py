"""Exact Horner traces and original-coordinate saved-vector constraints; Arb magnitude boxes."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,pickle,io,sys,os,time,math
import numpy as np
from flint import arb,ctx
assert not sys.flags.optimize
ctx.prec=512
B=Path(__file__).resolve().parents[3];D=B/'research/saved_vector_external_constraints'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def need(v,s):
 if not v:raise ValueError(s)
class Reader(pickle.Unpickler):
 def find_class(self,m,n):
  if m in ['numpy.core.multiarray','numpy._core.multiarray'] and n in ['_reconstruct','scalar']:return getattr(np._core.multiarray,n)
  if m=='numpy' and n in ['ndarray','dtype']:return getattr(np,n)
  raise ValueError('unsupported pickle global')
def rat(x):
 x=float(x);need(math.isfinite(x),'finite exact scalar');return F.from_float(x)
def endpoint(x):
 x=float(x);need(not math.isnan(x),'endpoint is not nan');return x if math.isinf(x) else rat(x)
def dy(x):
 need(x.is_finite() and x.rad()==0,'finite exact endpoint');m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def box(q):
 x=arb(q.numerator)/q.denominator;lo,hi=dy(x.lower()),dy(x.upper());need(lo<=q<=hi,'Arb rational containment');return list(map(str,[lo,hi]))
def dec(q):
 n=q.numerator*10**30//q.denominator
 return {'lower_exact':str(F(n,10**30)),'upper_exact':str(F(n+1,10**30))}
def horner(c,x):
 y=F(0)
 for v in reversed(c):y=y*x+v
 return y
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();man=json.loads((D/'data_exact/manifest.json').read_text());bind=json.loads((D/'evidence/source_binding.json').read_text());need(bind['status']=='PASS_STATIC_ORIGINAL_COORDINATE_VECTOR_SOURCE_PATH','prior source binding');pins=dict(bind['files'])
for p in [D/'data_exact/manifest.json',D/'evidence/source_binding.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'prior digest')
need(datetime.fromisoformat(bind['utc'])<datetime.fromisoformat(start),'source binding before trace arithmetic')
records=[];totals={'columns':0,'vector_coefficients':0,'trace_entries':0,'functionals':0,'nonzero_functionals':0,'endpoint_contributions':0}
for row in man['families']:
 M,nf=row['M'],row['nF'];cols=Reader(io.BytesIO((B/row['cols_path']).read_bytes())).load()['cols'];need(len(cols)==nf,'column count');joins=[rat(float.fromhex(x)) for x in row['joins_hex']]
 with np.load(B/row['vector_path'],allow_pickle=False) as z:
  hh=z['Fminus_h'];need(hh.dtype==np.dtype('float64') and hh.shape==(row['n_extended'],5) and np.isfinite(hh).all(),'saved vectors');need(np.count_nonzero(hh[nf+2:])==0,'extra coordinates zero');h=[[rat(v) for v in hh[i,:]] for i in range(nf)]
 sums=[[[F(0) for q in range(4)] for m in range(M)] for v in range(5)];table=[]
 for i,(mode,pcs,label) in enumerate(cols):
  need(int(mode)==mode and 0<=int(mode)<M,'exact angular mode');mode=int(mode);pieces=[]
  for a,b,al,c in pcs:
   a,b=endpoint(a),endpoint(b);need(a<b and a!=math.inf and b!=-math.inf and not(a==-math.inf and b==math.inf),'valid support');need(len(c)>0,'nonempty polynomial');pieces.append((a,b,rat(al),[rat(v) for v in c]))
  pieces.sort(key=lambda p:p[0]);need(all(p[1]<=q[0] for p,q in zip(pieces,pieces[1:])),'disjoint piece interiors');traces=[]
  for j in joins:
   ending=[p for p in pieces if p[1]==j];starting=[p for p in pieces if p[0]==j];need(len(ending)<=1 and len(starting)<=1,'unique one-sided contributions');out=[F(0),F(0)]
   for sign,pp in [(1,ending),(-1,starting)]:
    for a,b,al,c in pp:
     x=j-(b if a==-math.inf else a);need(al*x==0,'exact endpoint exponential');p=horner(c,x);dp=horner([k*c[k] for k in range(1,len(c))],x);out[0]+=sign*p;out[1]+=sign*(al*p+dp);totals['endpoint_contributions']+=1
   traces.extend(out)
  table.append({'column':i,'mode':mode,'label':label,'traces_exact':list(map(str,traces)),'h_exact':list(map(str,h[i]))})
  for v in range(5):
   for q in range(4):sums[v][mode][q]+=h[i][v]*traces[q]
  totals['columns']+=1;totals['vector_coefficients']+=5;totals['trace_entries']+=4
 out=[]
 for v in range(5):
  constraints=[]
  for m in range(M):
   for q in range(4):
    value=sums[v][m][q];constraints.append({'mode':m,'join_index':q//2,'order':q%2,'value_exact':str(value),'abs_arb512_exact':box(abs(value)),'abs_decimal':dec(abs(value))});totals['functionals']+=1;totals['nonzero_functionals']+=value!=0
  mx=max(abs(F(r['value_exact'])) for r in constraints);out.append({'vector':v,'constraints':constraints,'nonzero':sum(F(r['value_exact'])!=0 for r in constraints),'max_abs_exact':str(mx),'max_abs_decimal':dec(mx)})
 records.append({'M':M,'nF':nf,'joins_exact':list(map(str,joins)),'vector_path':row['vector_path'],'cols_path':row['cols_path'],'columns':table,'vectors':out})
for n,h in pins.items():need(sha(B/n)==h,'final digest')
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_EXACT_SAVED_VECTOR_EXTERNAL_CONSTRAINTS_REQUIRES_INDEPENDENT_CHECK','records':records,'counts':totals,'seconds':time.monotonic()-tick,'arb_bits':ctx.prec,'files':dict(sorted(pins.items())),'scope':'Exact source-defined function-column constraints of saved dyadic original-coordinate vectors. KP/TAU/source extra columns zero; no physical full-field cancellation, exact SVD, PDE norm or endpoint assertion.'}
with (D/'data_exact/constraints.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'counts':totals,'seconds':out['seconds'],'summaries':[{'M':r['M'],'vectors':[{k:v[k] for k in ['vector','nonzero','max_abs_decimal']} for v in r['vectors']]} for r in records]}))

"""Exact row cancellation levels and separate pure-source convention diagnostics."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import ast, hashlib, io, json, math, pickle, struct, sys, time, os
import numpy as np
from flint import fmpq as Q
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/projection_source_constraints'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def load(p):return json.loads(Path(p).read_text())
class Reader(pickle.Unpickler):
 def find_class(self,m,n):
  table={('numpy','ndarray'):np.ndarray,('numpy','dtype'):np.dtype}
  for p in ['numpy.core.multiarray','numpy._core.multiarray']:
   table[p,'scalar']=np._core.multiarray.scalar;table[p,'_reconstruct']=np._core.multiarray._reconstruct
  need((m,n) in table,'restricted class');return table[m,n]
def qrat(v):
 w=int.from_bytes(struct.pack('>d',float(v)),'big');sg=-1 if w>>63 else 1;e=(w>>52)&2047;m=w&((1<<52)-1);need(e!=2047,'finite binary64')
 return Q(sg*(m if e==0 else m+(1<<52)))*Q(2)**(-1074 if e==0 else e-1075)
def fr(v):return F.from_float(float(v))
def qr(v):return Q(v.numerator,v.denominator)
def traces(pcs,joins,R):
 out=[]
 for j in joins:
  val=[R(0),R(0)]
  for a,b,al,c in pcs:
   a=-math.inf if a==-math.inf else R(a);b=math.inf if b==math.inf else R(b)
   if b==j:sg=1
   elif a==j:sg=-1
   else:continue
   x=j-(b if a==-math.inf else a);al=R(al);c=[R(v) for v in c];need(al*x==0,'fatal nonunit exponential')
   val[0]+=sg*sum((v*x**i for i,v in enumerate(c)),R(0))
   val[1]+=sg*sum((al*v*x**i for i,v in enumerate(c)),R(0))+sg*sum((i*c[i]*x**(i-1) for i in range(1,len(c))),R(0))
  out+=val
 return out
start=utc();tick=time.monotonic();a=load(D/'evidence/checks.json');s=load(D/'evidence/source_binding.json');pins=dict(a['files']);pins[str((D/'evidence/checks.json').relative_to(B))]=sha(D/'evidence/checks.json')
for n,h in pins.items():need(sha(B/n)==h,'prior pin')
need(datetime.fromtimestamp((D/'REVIEW_RESOLUTION.md').stat().st_mtime,timezone.utc)<datetime.fromtimestamp(Path(__file__).stat().st_mtime,timezone.utc),'supplement proof before code')
cols=Reader(io.BytesIO((B/s['column_path']).read_bytes())).load()['cols'];joins=[fr(float.fromhex(v)) for v in s['joins_hex']]
with np.load(B/s['source_vector_path'],allow_pickle=False) as z:
 need(int(z['Mh'])==16 and all(fr(z[k])==j for k,j in zip(['tmin','t0'],joins,strict=True)),'source vector Mh and both exact joins')
counts={'rows':0,'row_entry_counts':0,'exact_abs_sum_equalities':0,'exact_ratio_checks':0,'source_endpoint_float_diagnostics':0,'manufactured_endpoint_cases':0,'manufactured_interior_cases':0,'fatal_gate_cases':0}
TA=[traces(pcs,joins,fr) for mode,pcs,label in cols];TB=[traces(pcs,[qr(j) for j in joins],qrat) for mode,pcs,label in cols]
# Complete inspected pure source, identity with the pinned full source is inherited
# from topic148. Compile only these AST nodes into an explicit NumPy namespace.
ns={'np':np}
for filename,name,kind in [('snapshot_v3__piece_jet.txt','piece_jet',ast.FunctionDef),('ExpPolyBasis.txt','ExpPolyBasis',ast.ClassDef)]:
 p=B/'research/external_constraint_rank/sources'/filename;tree=ast.parse(p.read_text());need(len(tree.body)==1 and isinstance(tree.body[0],kind) and tree.body[0].name==name,'single allowed pure definition')
 need(not any(isinstance(x,(ast.Import,ast.ImportFrom)) for x in ast.walk(tree)),'no imported modules in excerpt')
 exec(compile(tree,'<frozen pure convention diagnostic>','exec'),ns)
jet=ns['piece_jet'];Exp=ns['ExpPolyBasis'];max_float_error=F(0)
for i,(mode,pcs,label) in enumerate(cols):
 need(all(qr(x)==y for x,y in zip(TA[i],TB[i],strict=True)),'alternate decoded complete traces')
 for j,t in enumerate(joins):
  for nu in [0,1]:
   vf=jet(pcs,float(t),'-',nu)-jet(pcs,float(t),'+',nu);need(math.isfinite(vf),'finite pure source diagnostic')
   max_float_error=max(max_float_error,abs(fr(vf)-TA[i][2*j+nu]));counts['source_endpoint_float_diagnostics']+=1
pcs=[(-np.inf,0.0,3.0,np.array([2.0,5.0])),(0.0,1.0,0.0,np.array([7.0,-2.0]))]
want=[F(-5),F(13),F(5),F(-2)];need(traces(pcs,[F(0),F(1)],fr)==want,'exact manufactured orientation')
for j,t in enumerate([0.,1.]):
 for nu in [0,1]:need(fr(jet(pcs,t,'-',nu)-jet(pcs,t,'+',nu))==want[2*j+nu],'source manufactured endpoint');counts['manufactured_endpoint_cases']+=1
for t in [-0.5,-0.25,0.25,0.75,1.5]:
 for nu in [0,1]:
  expect=(math.exp(3*t)*(2+5*t) if nu==0 else math.exp(3*t)*(11+15*t)) if t<0 else ((7-2*t if nu==0 else -2) if t<1 else 0)
  got=float(Exp(pcs).eval([t],nu)[0]);need(abs(got-expect)<=1e-14*(1+abs(expect)),'manufactured anchor/interior derivative');counts['manufactured_interior_cases']+=1
try:traces([(0.,1.,2.,np.array([1.]))],[F(1)],fr)
except ValueError as e:need(str(e)=='fatal nonunit exponential','specific nonunit rejection');counts['fatal_gate_cases']+=1
else:raise ValueError('nonunit example passed')
t=np.nextafter(1.,2.);shifted=[(0.,t,0.,np.array([1.]))];need(traces(shifted,[F(1)],fr)==[0,0] and jet(shifted,1.,'-',0)==0,'one-ulp endpoint nonincidence');counts['fatal_gate_cases']+=1
records=[]
for fam in a['families']:
 with np.load(B/fam['file'],allow_pickle=False) as z:x=[fr(v) for v in z['x']];xq=[qrat(v) for v in z['x']]
 rows=[]
 for row in fam['rows']:
  m,j,nu=[row[k] for k in ['mode','join_index','order']];p=2*j+nu
  indices=[i for i,(mode,pcs,label) in enumerate(cols) if mode==m];nentry=sum(TA[i][p]!=0 for i in indices)
  sA=sum((abs(x[i]*TA[i][p]) for i in indices),F(0));sB=sum((abs(xq[i]*TB[i][p]) for i in reversed(indices)),Q(0));need(qr(sA)==sB,'independent absolute-product sum')
  value=F(row['value_exact']);need(abs(value)<=sA,'triangle inequality');eta=abs(value)/sA if sA else None
  if eta is None:need(value==0,'zero denominator case')
  else:need(qr(eta)*sB==abs(qr(value)) and 0<=eta<=1,'exact ratio cross multiplication');counts['exact_ratio_checks']+=1
  rows.append({'mode':m,'join_index':j,'order':nu,'nonzero_matrix_entries':nentry,'row_identically_zero':nentry==0,'sum_abs_products_exact':str(sA),'cancellation_ratio_exact':str(eta) if eta is not None else None})
  counts['rows']+=1;counts['row_entry_counts']+=1;counts['exact_abs_sum_equalities']+=1
 positive=[F(r['cancellation_ratio_exact']) for r in rows if r['cancellation_ratio_exact'] is not None];mx=max(positive)
 records.append({'file':fam['file'],'rows':rows,'nonzero_matrix_rows':sum(not r['row_identically_zero'] for r in rows),'zero_denominator_rows':sum(r['cancellation_ratio_exact'] is None for r in rows),'max_cancellation_ratio_exact':str(mx),'maximizers':[{k:r[k] for k in ['mode','join_index','order']} for r in rows if r['cancellation_ratio_exact'] is not None and F(r['cancellation_ratio_exact'])==mx]})
need(counts['rows']==counts['row_entry_counts']==counts['exact_abs_sum_equalities']==160 and counts['source_endpoint_float_diagnostics']==7812,'full fixed coverage')
for p in [D/'REVIEW_RESOLUTION.md',D/'MANUFACTURED_CORRECTION.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'final input identity')
out={'start_utc':start,'utc':utc(),'status':'PASS_EXACT_CANCELLATION_LEVELS_AND_SOURCE_CONVENTION_DIAGNOSTICS','counts':counts,'source_float_minus_exact_trace_max_abs':str(max_float_error),'families':records,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Literal pair only; pure extracted source executes only as a supplemental convention diagnostic. No historical matrix identity, full physical trace, error estimate or inverse.'}
with (D/'evidence/supplement.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:out[k] for k in ['utc','status','counts','seconds']}));print(json.dumps([{'file':r['file'],'nonzero_matrix_rows':r['nonzero_matrix_rows'],'zero_denominators':r['zero_denominator_rows'],'max_cancellation_ratio':float(F(r['max_cancellation_ratio_exact']))} for r in records]))

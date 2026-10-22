"""Frozen angular source, exact tree and streaming evidence primitives.
No JavaScript/TypeScript, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,re,ctypes,importlib
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
import flint,mpmath
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/flow_angular_full';E=D/'evidence';OLD=B/'research/flow_angular';SRC=B/'research/flow_certificate/evidence/source'
sys.path.insert(0,str(SRC));import cert_flow as source
ctx.threads=1
N=261;TOTAL=51000;COEFF=9*N
FIELDS=('cos_a','cos_b','sin_a','sin_b')
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def digest(x):return hashlib.sha256(canon(x).encode()).hexdigest()
def rawhash(x):return hashlib.sha256(np.asarray(x,dtype='<f8',order='C').tobytes(order='C')).hexdigest()
def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def safe_tag(s):assert re.fullmatch('[a-zA-Z0-9_]+',s);return s
def load(p):return json.loads(Path(p).read_text())
def write_json(p,x):
 p=Path(p);t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(x,indent=2)+'\n');t.replace(p)
def log_event(tag,value):
 with (E/(safe_tag(tag)+'_restarts.jsonl')).open('a') as f:f.write(canon({'utc':utc(),**value})+'\n');f.flush();os.fsync(f.fileno())
def ball_record(x):
 assert x.is_finite()
 return [[int(y) for y in x.mid().man_exp()],[int(y) for y in x.rad().man_exp()]]
def ancestry_record(node):
 l,r,d=node;base=l//128;off=(l-128*base)//(r-l)
 return {'base':base,'bits':[(off>>j)&1 for j in range(d-1,-1,-1)]}
def endpoints_record(a,b,node):return {'balls':[ball_record(a),ball_record(b)],'ancestry':ancestry_record(node)}

def integer_nodes():
 stack=[(128*i,128*(i+1),0) for i in range(200)];out=[]
 while stack:
  l,r,d=stack.pop();out.append((l,r,d))
  if d<7:m=(l+r)//2;stack.extend([(l,m,d+1),(m,r,d+1)])
 assert len(out)==TOTAL and len(set(out))==TOTAL
 return out

def actual_nodes():
 ctx.prec=128;hp=arb.pi()/2
 stack=[(hp*i/200,hp*(i+1)/200,128*i,128*(i+1),0) for i in range(200)]
 while stack:
  a,b,l,r,d=stack.pop();ctx.prec=128
  if d<7:m=(a+b)/2;j=(l+r)//2;stack.extend([(a,m,l,j,d+1),(m,b,j,r,d+1)])
  yield a,b,(l,r,d)

def ancestry_node(l,r,depth):
 ctx.prec=128;hp=arb.pi()/2;base=l//128;off=(l-128*base)//(r-l)
 a=hp*base/200;b=hp*(base+1)/200
 for bit in range(depth-1,-1,-1):
  m=(a+b)/2
  if (off>>bit)&1:a=m
  else:b=m
 return a,b

def load_geometry():
 v=load(OLD/'evidence/verdict.json');assert v['status']=='CONFIRMED_FINITE_ANGULAR_RESULT';pins={}
 for f,h in v['files'].items():assert sha(B/f)==h,f;pins[f]=h
 pins[str((OLD/'evidence/verdict.json').relative_to(B))]=sha(OLD/'evidence/verdict.json')
 with np.load(OLD/'evidence/finite_arrays.npz',allow_pickle=False) as z:
  nodes=z['nodes'].copy();keys=z['keys'].copy();widths=z['distinct_half_widths'].copy();rems=z['remainder_arrays'].copy()
  selected={tuple(map(int,node)):(m.copy(),r.copy()) for node,m,r in zip(z['selected'],z['midpoints'],z['radii'],strict=True)}
 assert len(selected)==221
 assert nodes.shape==(TOTAL,3) and keys.shape==(TOTAL,4) and np.all(np.isfinite(keys))
 assert [tuple(map(int,x)) for x in nodes]==integer_nodes() and len(set(map(tuple,keys)))==TOTAL
 assert widths.shape==(8,) and rems.shape==(8,2,N)
 tables={};exact=0
 for d,row in zip(widths,rems,strict=True):
  assert np.isfinite(d) and d>0 and np.all(np.isfinite(row)) and np.all(row>=0)
  for fam in range(2):
   for n,rr in enumerate(row[fam],1):
    pref=8*n**3 if fam==0 else 4*n**4+8*n**3+6*n*n+2*n
    assert F(float(rr))>=F(pref,6)*F(float(d))**3;exact+=1
  tables[float(d).hex()]=row
 assert len(tables)==8 and exact==4176
 return nodes,keys,tables,pins,selected

def new_cache():ctx.prec=128;return source.AngCache(np.arange(1,N+1))

def source_packet(cache,a,b,node,keyrow,tables,selected):
 ctx.prec=128;fac=cache.factors(a,b)
 actualkey=source.AngCache.key(None,a,b);assert actualkey==tuple(map(float,keyrow))
 m=np.asarray([[fac[f][j].m for j in range(3)] for f in ('cos','C','S')],dtype=np.float64)
 r=np.asarray([[fac[f][j].r for j in range(3)] for f in ('cos','C','S')],dtype=np.float64)
 rem=np.asarray([fac[f][3] for f in ('cos','C','S')],dtype=np.float64)
 assert m.shape==r.shape==(3,3,N) and rem.shape==(3,N)
 assert np.all(np.isfinite(m)) and np.all(np.isfinite(r)) and np.all(r>=0) and np.all(np.isfinite(rem)) and np.all(rem>=0)
 d=float(fac['d']);wh=d.hex();assert np.isfinite(d) and d>0 and wh in tables
 assert rawhash(rem[0])==rawhash(tables[wh][0]) and rawhash(rem[1])==rawhash(tables[wh][1])==rawhash(rem[2])
 geo=np.asarray([*fac['cos_a'],*fac['cos_b'],*fac['sin_a'],*fac['sin_b'],fac['a_lo'],fac['b_hi'],d],dtype=np.float64)
 assert geo.shape==(11,) and np.all(np.isfinite(geo)) and all(geo[2*j]<=geo[2*j+1] for j in range(4))
 assert bool(geo[8]<=0)==(node[0]==0)
 old=False
 if tuple(node) in selected:
  om,orr=selected[tuple(node)];assert rawhash(np.stack((m,r)))==rawhash(np.stack((om,orr)));old=True
 cache.cache.clear();ep=endpoints_record(a,b,node)
 record={'source_box_sha256':rawhash(np.stack((m,r))),'geometry_sha256':rawhash(geo),'remainder_sha256':rawhash(rem),'cache_key_hex':[float(x).hex() for x in actualkey],'width_hex':wh,'endpoint_record':ep,'endpoint_record_sha256':digest(ep),'old_selected_agreement':old,'axis_predicate_checked':True}
 return m,r,geo,record

def startup_remainders(nodes,keys,tables,selected):
 cache=new_cache();seen=set();records=[]
 for depth in range(8):
  index=next(i for i,n in enumerate(nodes) if int(n[2])==depth);node=tuple(map(int,nodes[index]));a,b=ancestry_node(*node)
  _,_,_,record=source_packet(cache,a,b,node,keys[index],tables,selected)
  seen.add(record['width_hex']);records.append({'node_index':index,'width_hex':record['width_hex'],'remainder_sha256':record['remainder_sha256']})
 assert seen==set(tables)
 return records

def witnesses(m,r):
 return [{'family':f,'derivative':d,'n':n+1,'mid_hex':float(m[f,d,n]).hex(),'rad_hex':float(r[f,d,n]).hex()} for f,d,n in [(0,0,0),(0,1,130),(0,2,260),(1,0,260),(1,1,0),(1,2,130),(2,0,130),(2,1,260),(2,2,0)]]

def runtime():
 rounding=ctypes.CDLL(None).fegetround();assert rounding==0
 paths=set()
 for name in ('flint.types.arb','flint.types.acb','numpy._core._multiarray_umath','mpmath.libmp.libmpf','mpmath.libmp.libmpi'):
  p=Path(importlib.import_module(name).__file__).resolve();paths.add(p)
 for line in Path('/proc/self/maps').read_text().splitlines():
  p=line.split()[-1]
  if p.startswith('/') and any(s in p.lower() for s in ('flint','libgmp','libmpfr','openblas')) and Path(p).is_file():paths.add(Path(p))
 return {'python':sys.version,'numpy':np.__version__,'flint':flint.__version__,'mpmath':mpmath.__version__,'binary_and_arithmetic_source_sha256':{str(p):sha(p) for p in sorted(paths)},'hardware_rounding_mode':rounding,'threads':1,'source_precision':128,'arb_reference_precision':512,'iv_decimal_precision':180,'fresh_arb_precision':1536}

def current_files(dep):
 files=dict(dep)
 for p in list((D/'code').glob('*.py'))+list((D/'code').glob('*.sh'))+list((D/'source').glob('*.json'))+[D/'PROOF.md',D/'ADDENDUM.md',E/'proof_first.json',E/'addendum_first.json']:
  assert p.is_file(),p;files[str(p.relative_to(B))]=sha(p)
 return dict(sorted(files.items()))

def header(indices,dep,startup):
 full=indices==list(range(TOTAL))
 return {'type':'header','schema':1,'scope':'FULL_FINITE_ANGULAR' if full else 'PARTIAL_DIAGNOSTIC','indices':None if full else indices,'planned_cells':len(indices),'total_finite_cells':TOTAL,'runtime':runtime(),'methods':['Arb512_even_trigonometric_sums','iv180_even_trigonometric_recurrence'],'files':current_files(dep),'coefficients_per_cell':COEFF,'geometry_checks_per_cell':7,'axis_predicate_checks_per_cell':1,'exact_remainder_checks':4176,'startup_actual_remainders':startup}

def row_payload(slot,index,node,packet,m,r):
 return {'type':'row','slot':slot,'node_index':index,'node':list(node),**packet,'coefficient_checks':{'arb512':COEFF,'iv180':COEFF},'geometry_checks':{'arb512':7,'iv180':7},'remainder_table_comparisons':1,'witnesses':witnesses(m,r)}

def append_chain(payload,previous):
 return {**payload,'previous_chain':previous,'chain':hashlib.sha256((previous+'\n'+canon(payload)).encode()).hexdigest()}

def validate_row(row,slot,index,node,previous,keys,tables,selected):
 assert row['type']=='row' and row['slot']==slot and row['node_index']==index and row['node']==list(node)
 assert row['coefficient_checks']=={'arb512':COEFF,'iv180':COEFF} and row['geometry_checks']=={'arb512':7,'iv180':7} and row['remainder_table_comparisons']==1
 for key in ('source_box_sha256','geometry_sha256','remainder_sha256','endpoint_record_sha256'):assert re.fullmatch('[0-9a-f]{64}',row[key])
 assert row['previous_chain']==previous
 payload={k:v for k,v in row.items() if k not in ('previous_chain','chain')};assert append_chain(payload,previous)==row
 assert len(row['witnesses'])==9 and row['cache_key_hex']==[float(x).hex() for x in keys[index]]
 assert row['width_hex'] in tables and row['axis_predicate_checked'] is True and row['old_selected_agreement']==(tuple(node) in selected)
 a,b=ancestry_node(*node);ep=endpoints_record(a,b,node);assert row['endpoint_record']==ep and row['endpoint_record_sha256']==digest(ep)
 return row['chain']

def totals(rows):
 return {'cells':len(rows),'coefficients_per_engine':len(rows)*COEFF,'geometry_per_engine':len(rows)*7,'axis_predicates':len(rows),'remainder_table_comparisons':len(rows),'distinct_widths':sorted({r['width_hex'] for r in rows}),'old_selected_agreements':sum(r['old_selected_agreement'] for r in rows),'exact_remainder_checks':4176}

def footer(rows,previous,head):
 assert len(rows)==head['planned_cells']
 return {'type':'footer','scope':head['scope'],'totals':totals(rows),'final_chain':previous,'header_sha256':digest(head)}

def read_stream(path,head,nodes,keys,tables,selected,repair_tag=None):
 rows=[];end=None;previous=digest(head);removed=None
 with Path(path).open('rb') as f:
  first=f.readline();assert first.endswith(b'\n') and json.loads(first)==head,'header mismatch'
  while True:
   pos=f.tell();line=f.readline()
   if not line:break
   if not line.endswith(b'\n'):
    assert repair_tag is not None and not f.read(1),'uncommitted trailing line'
    removed={'offset':pos,'bytes':len(line),'sha256':hashlib.sha256(line).hexdigest()};break
   item=json.loads(line);assert end is None,'record after footer'
   if item.get('type')=='footer':end=item;assert item==footer(rows,previous,head)
   else:
    slot=len(rows);assert slot<head['planned_cells'];index=slot if head['indices'] is None else head['indices'][slot]
    previous=validate_row(item,slot,index,tuple(map(int,nodes[index])),previous,keys,tables,selected);rows.append(item)
 if removed:
  log_event(repair_tag,{'action':'remove_uncommitted_trailing_line',**removed})
  with Path(path).open('r+b') as f:f.truncate(removed['offset']);f.flush();os.fsync(f.fileno())
 return rows,previous,end

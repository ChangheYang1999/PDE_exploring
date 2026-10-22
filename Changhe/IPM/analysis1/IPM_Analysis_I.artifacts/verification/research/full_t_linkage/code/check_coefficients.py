"""All finite spline T coefficients: Arb angular inverse versus exact interpolation."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone
from time import monotonic
import argparse,bisect,gzip,hashlib,json,math,re,resource,sys
import numpy as np
from flint import arb,ctx,fmpq,fmpq_mat
assert not sys.flags.optimize
ctx.prec=640;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/full_t_linkage';E=D/'evidence'
ARCHIVE_SHA='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
GREEN_SHA='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
TRIAL_SHA='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
PARTITION_SHA='56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2'

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def unique_pairs(pairs):
 out={}
 for k,v in pairs:
  assert k not in out,('duplicate JSON key',k);out[k]=v
 return out
def strict_json(s):return json.loads(s,object_pairs_hook=unique_pairs,parse_constant=lambda x:(_ for _ in ()).throw(ValueError('nonfinite JSON '+x)))
def load(p):return strict_json(Path(p).read_text())
def q(v):
 if isinstance(v,fmpq):return v
 v=F(v);return fmpq(v.numerator,v.denominator)
def a(v):return arb(q(v))
def ratfloat(v):
 v=float(v);assert math.isfinite(v);n,d=v.as_integer_ratio();return fmpq(n,d)
def rathex(s):
 assert isinstance(s,str)
 match=re.fullmatch(r'([+-]?)0x([0-9a-fA-F]+)\.([0-9a-fA-F]*)p([+-]?[0-9]+)',s);assert match,('invalid hex',s)
 sign,integer,fraction,exponent=match.groups();exact=fmpq((-1 if sign=='-' else 1)*int(integer+fraction,16))*fmpq(2)**(int(exponent)-4*len(fraction))
 assert exact==ratfloat(float.fromhex(s)),('hex not exactly binary64',s)
 return exact
def dyadic(m,e):return fmpq(int(m))*fmpq(2)**int(e)
def decode(d):
 assert isinstance(d,dict) and set(d)=={'schema','mid_m','mid_e','rad_m','rad_e'} and d['schema']=='arb-dyadic-mid-radius-v1'
 m,r=dyadic(d['mid_m'],d['mid_e']),dyadic(d['rad_m'],d['rad_e']);assert r>=0
 return m-r,m+r
def ball(d):
 lo,hi=decode(d);return a(lo).union(a(hi))
def endpoints(v):
 assert v.is_finite(),'nonfinite Arb enclosure'
 lo,hi=v.lower(),v.upper();lm,le=lo.man_exp();hm,he=hi.man_exp();lo,hi=dyadic(lm,le),dyadic(hm,he);assert lo<=hi
 return lo,hi

def cox_values(knots,ell,t):
 """Definition evaluated at a strictly interior node, active indices only."""
 assert knots[ell]<t<knots[ell+1]
 previous={ell:fmpq(1)}
 for degree in range(1,8):
  current={}
  for i in range(ell-degree,ell+1):
   left=knots[i+degree]-knots[i];right=knots[i+degree+1]-knots[i+1]
   current[i]=((t-knots[i])*previous.get(i,fmpq(0))/left if left else 0)+((knots[i+degree+1]-t)*previous.get(i+1,fmpq(0))/right if right else 0)
  previous=current
 return [previous[i] for i in range(ell-7,ell+1)]

def deboor_weights(knots,ell,t):
 d=[[fmpq(i==j) for i in range(8)] for j in range(8)]
 for r in range(1,8):
  for j in range(7,r-1,-1):
   denominator=knots[ell+1+j-r]-knots[ell-7+j];assert denominator>0
   alpha=(t-knots[ell-7+j])/denominator
   d[j]=[(1-alpha)*u+alpha*v for u,v in zip(d[j-1],d[j])]
 return d[7]

def multiply_linear(poly,c0,c1):
 result=[fmpq(0)]*(len(poly)+1)
 for j,v in enumerate(poly):result[j]+=c0*v;result[j+1]+=c1*v
 return result

def interpolation_matrix(nodes):
 cols=[]
 for i,zi in enumerate(nodes):
  poly=[fmpq(1)]
  for j,zj in enumerate(nodes):
   if j!=i:poly=multiply_linear(poly,-zj/(zi-zj),1/(zi-zj))
  cols.append(poly)
 return fmpq_mat([[cols[i][power] for i in range(8)] for power in range(8)])
NODES=[fmpq(2*i+1,16) for i in range(8)];LAGRANGE=interpolation_matrix(NODES)

def exact_parent(knots,S,ell,left,right):
 weights=[];component_equalities=0
 for zi in NODES:
  t=left+(right-left)*zi;first=deboor_weights(knots,ell,t);second=cox_values(knots,ell,t)
  assert len(first)==len(second)==8
  for u,v in zip(first,second):assert u==v;component_equalities+=1
  assert sum(first,fmpq(0))==1 and all(x>=0 for x in first)
  weights.append(first)
 local=fmpq_mat([[S[m][i] for m in range(260)] for i in range(ell-7,ell+1)])
 return LAGRANGE*fmpq_mat(weights)*local,component_equalities

def exact_shift(Z,h,offset):
 matrix=fmpq_mat([[fmpq(math.comb(k,l))*offset**(k-l)/h**l if k>=l else fmpq(0) for k in range(8)] for l in range(8)])
 return matrix*Z

def inverse_angular(H):
 assert len(H)==262 and all(len(row)==8 for row in H)
 assert all(endpoints(v)==(0,0) for v in H[261])
 out=[[arb(0) for _ in range(8)] for _ in range(260)]
 sums=[[arb(0) for _ in range(8)] for _ in range(2)];weighted=[[arb(0) for _ in range(8)] for _ in range(2)]
 for m in range(259,0,-1):
  j=m+1;p=j%2
  for k in range(8):sums[p][k]+=H[j][k];weighted[p][k]+=j*H[j][k]
  opposite=1-m%2;same=m%2
  for k in range(8):out[m][k]=4*(weighted[opposite][k]-(m-1)*sums[opposite][k]-weighted[same][k]+m*sums[same][k])
 for k in range(8):out[0][k]=4*H[0][k]+out[2][k]/2
 return out

def arb_shift(parent,x):
 weights=[[a(math.comb(k,l)*x**(k-l)) if k>=l else arb(0) for k in range(8)] for l in range(8)]
 return [[sum((weights[l][k]*parent[m][k] for k in range(l,8)),arb(0)) for m in range(260)] for l in range(8)]

def forward_angular_exact(A):
 """Direct signed frequency collection, not the exceptional row formulas."""
 H=[[fmpq(0) for _ in range(8)] for _ in range(262)]
 for m in range(260):
  for freq in (1+2*m,1-2*m,3+2*m,3-2*m):
   assert freq and abs(freq)%2==1;j=(abs(freq)-1)//2;sign=1 if freq>0 else -1
   for k in range(8):H[j][k]+=sign*A[k,m]/8
 return H

def sample_triples():
 seed=hashlib.sha256((TRIAL_SHA+GREEN_SHA+ARCHIVE_SHA+':T').encode()).hexdigest();selected=set()
 for i in range(192):
  d=hashlib.sha256((seed+':'+str(i)).encode()).digest();selected.add((int.from_bytes(d[:8],'big')%7809,d[8]%8,int.from_bytes(d[9:17],'big')%260))
 assert len(selected)==192
 for cell in (0,4102,7808):
  for power in (0,1,7):
   for mode in (0,1,2,3,128,258,259):selected.add((cell,power,mode))
 return seed,selected

def append(out,record):out.write(json.dumps(record,sort_keys=True,separators=(',',':'))+'\n');out.flush();os.fsync(out.fileno())
def stream_update(hasher,data):hasher.update(json.dumps(data,sort_keys=True,separators=(',',':')).encode()+b'\n')
def classify(lo,hi,tl,th):
 assert lo<=hi and tl<=th
 if tl<=lo<=hi<=th:return 'CONTAINED'
 if hi<tl or th<lo:return 'DISJOINT'
 return 'OVERLAP_ONLY'

def saved_span(row,part):
 assert row['type']=='span' and all(row[k]==v for k,v in part.items())
 assert row['counts']=={'arb_contained':part['count']*2080,'rational_contained':part['count']*2080,'rational_in_arb':part['count']*2080,'archive_H_contained':2096,'deboor_cox_equalities':64}
 assert len(row['stream_sha256'])==64 and len(row['H_stream_sha256'])==64 and not row['failures']
 for item in row['worst_margins'].values():assert q(item['margin_exact'])>=0

def inspect_inputs():
 paths={'trial':B/'data_exact/modal_v2.json','archive':B/'research/middle_residual/evidence/original_knots.jsonl.gz','partition':B/'research/middle_residual/evidence/partition_exact.json','archive_audit':B/'research/middle_residual/evidence/knot_audit.json'}
 expected={'trial':TRIAL_SHA,'archive':ARCHIVE_SHA,'partition':PARTITION_SHA};pins={}
 for key,path in paths.items():
  pins[str(path.relative_to(B))]=sha(path)
  if key in expected:assert pins[str(path.relative_to(B))]==expected[key]
 d=load(paths['trial']);assert d['degree']==7 and d['arrays']['S']['shape']==[260,1565] and d['arrays']['knots']['shape']==[1573]
 vals=d['arrays']['S']['hex'];assert len(vals)==260*1565;S=[[rathex(v) for v in vals[m*1565:(m+1)*1565]] for m in range(260)]
 knots=[rathex(v) for v in d['arrays']['knots']['hex']];assert len(knots)==1573 and all(x<=y for x,y in zip(knots,knots[1:]))
 nonempty=[(i,x,y) for i,(x,y) in enumerate(zip(knots,knots[1:])) if x<y];assert len(nonempty)==1558
 partition=load(paths['partition']);assert partition['input_sha256']==TRIAL_SHA and partition['grid_sha256']==GREEN_SHA and partition['cells']==7809
 parts=partition['spans'];assert len(parts)==1558;first=0
 for i,(part,(ell,x,y)) in enumerate(zip(parts,nonempty)):
  assert part=={'span':i,'first_cell':first,'count':part['count'],'a_exact':str(x),'b_exact':str(y)} and isinstance(part['count'],int) and part['count']>0
  assert 7<=ell and ell<1565;first+=part['count']
 assert first==7809
 audit=load(paths['archive_audit']);assert audit['status']=='PASS' and audit['archive_sha256']==ARCHIVE_SHA and audit['partition_sha256']==PARTITION_SHA and audit['spans']==1558 and audit['cells']==7809 and audit['footer_read']
 for path in (D/'PROOF.md',D/'ADDENDUM.md',D/'evidence/proof_first.json',D/'evidence/addendum_first.json',Path(__file__)):pins[str(path.relative_to(B))]=sha(path)
 return paths,pins,knots,S,nonempty,parts

def calculate_span(rec,part,knots,S,ell,arrays,samples):
 left,right=q(part['a_exact']),q(part['b_exact']);h=right-left
 assert q(rec['polynomial_mid_exact'])==(left+right)/2
 Hraw=rec['density_polynomials'];assert len(Hraw)==262 and all(len(row)==8 for row in Hraw)
 H=[[ball(v) for v in row] for row in Hraw];parent=inverse_angular(H);Z,basis_equalities=exact_parent(knots,S,ell,left,right)
 Htrue=forward_angular_exact(exact_shift(Z,h,fmpq(1,2)));counts=Counter();hs=hashlib.sha256();ts=hashlib.sha256();worst={};captured=[]
 def note_margin(key,margin,entry):
  if key not in worst or margin<q(worst[key]['margin_exact']):worst[key]={'margin_exact':str(margin),'entry':entry}
 for j in range(262):
  for k in range(8):
   lo,hi=decode(Hraw[j][k]);v=Htrue[j][k];data={'j':j,'power':k,'exact':str(v),'target_lo':str(lo),'target_hi':str(hi)}
   if not lo<=v<=hi:raise AssertionError(('H polynomial outside canonical archive',part['span'],data))
   counts['archive_H_contained']+=1;note_margin('archive_H',min(v-lo,hi-v),data);stream_update(hs,data)
 counts['deboor_cox_equalities']=basis_equalities
 for child in range(part['count']):
  cell=part['first_cell']+child;offset=fmpq(child,part['count']);exact=exact_shift(Z,h,offset);directed=arb_shift(parent,h*(offset-fmpq(1,2)))
  for k in range(8):
   for m in range(260):
    v=exact[k,m];lo,hi=endpoints(directed[k][m]);mid=ratfloat(arrays['T_mid'][cell,k,m]);rad=ratfloat(arrays['T_rad'][cell,k,m]);tl,th=mid-rad,mid+rad
    data={'cell':cell,'power':k,'mode':m,'t_exact':str(left+h*offset),'exact':str(v),'arb_lo':str(lo),'arb_hi':str(hi),'target_mid_hex':float(arrays['T_mid'][cell,k,m]).hex(),'target_rad_hex':float(arrays['T_rad'][cell,k,m]).hex()}
    status=classify(lo,hi,tl,th)
    if status!='CONTAINED' or not tl<=v<=th or not lo<=v<=hi:
     failure={'span':part['span'],'arb_classification':status,'rational_target_contains':tl<=v<=th,'rational_arb_contains':lo<=v<=hi,'entry':data};raise ArithmeticError(json.dumps(failure))
    counts['arb_contained']+=1;counts['rational_contained']+=1;counts['rational_in_arb']+=1
    note_margin('arb',min(lo-tl,th-hi),data);note_margin('rational',min(v-tl,th-v),data);note_margin('cross',min(v-lo,hi-v),data)
    if (cell,k,m) in samples:captured.append(data)
    stream_update(ts,data)
 row={'type':'span',**part,'counts':dict(counts),'stream_sha256':ts.hexdigest(),'H_stream_sha256':hs.hexdigest(),'worst_margins':worst,'selected_records':captured,'failures':[],'utc':utc()};saved_span(row,part)
 return row

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='full');ap.add_argument('--spans',default='all');ap.add_argument('--resume',action='store_true');ap.add_argument('--green',type=Path,default=B.parent/'ipmA-num/data/cert_green.npz');args=ap.parse_args();assert args.tag.replace('_','').isalnum()
 resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));started=monotonic();paths,pins,knots,S,nonempty,parts=inspect_inputs();assert sha(args.green)==GREEN_SHA
 selected=list(range(1558)) if args.spans=='all' else sorted(set(map(int,args.spans.split(','))));assert selected and 0<=selected[0]<=selected[-1]<1558
 seed,samples=sample_triples();header={'type':'header','schema':'ipm-full-t-linkage-v1','utc':utc(),'full_run':selected==list(range(1558)),'selected_spans':selected,'expected_cells':sum(parts[i]['count'] for i in selected),'files':pins,'green_sha256':GREEN_SHA,'green_path':str(args.green),'arb_bits':640,'exact_engine':'python-flint fmpq matrices','sample_seed':seed,'sample_triples':sorted(map(list,samples))}
 output=E/(args.tag+'_spans.jsonl');rows=[];had_footer=False
 if output.exists():
  assert args.resume,'Existing output requires --resume'
  with output.open('r+b') as f:
   line=f.readline();assert line.endswith(b'\n');old=strict_json(line);assert {k:v for k,v in old.items() if k!='utc'}=={k:v for k,v in header.items() if k!='utc'};header=old
   while True:
    pos=f.tell();line=f.readline()
    if not line:break
    if not line.endswith(b'\n'):f.seek(pos);f.truncate();break
    row=strict_json(line)
    if row['type']=='complete':assert len(rows)==len(selected) and not f.read();had_footer=True;break
    assert len(rows)<len(selected);saved_span(row,parts[selected[len(rows)]]);rows.append(row)
 else:
  with output.open('w') as f:append(f,header)
 resumed=len(rows)
 resume_path=E/(args.tag+'_resume_events.jsonl')
 if args.resume:
  resume_event={'utc':utc(),'resumed_spans':resumed,'last_saved_span':selected[resumed-1] if resumed else None,'next_span':selected[resumed] if resumed<len(selected) else None,'producer_sha256':sha(Path(__file__)),'header_sha256':hashlib.sha256(json.dumps(header,sort_keys=True,separators=(',',':')).encode()).hexdigest()}
  with resume_path.open('a') as rf:append(rf,resume_event)
 else:assert not resume_path.exists(),'Orphan resume events require inspection'
 resume_events=[]
 if resume_path.exists():
  with resume_path.open() as rf:
   for line in rf:
    assert line.endswith('\n');ev=strict_json(line);assert ev['producer_sha256']==sha(Path(__file__)) and ev['header_sha256']==hashlib.sha256(json.dumps(header,sort_keys=True,separators=(',',':')).encode()).hexdigest();resume_events.append(ev)
 with np.load(args.green,allow_pickle=False) as g:arrays={k:g[k] for k in ('T_mid','T_rad','tb','tb_rad','parent')}
 for k,x in arrays.items():
  assert np.all(np.isfinite(x)),k
  if k!='parent':assert x.dtype==np.dtype('float64'),(k,x.dtype)
 assert arrays['T_mid'].shape==arrays['T_rad'].shape==(7809,8,260) and np.all(arrays['T_rad']>=0)
 assert arrays['tb'].shape==arrays['tb_rad'].shape==(7810,) and np.all(arrays['tb_rad']>=0)
 assert arrays['parent'].shape==(7809,) and np.issubdtype(arrays['parent'].dtype,np.integer)
 assert np.array_equal(arrays['parent'],np.concatenate([np.full(p['count'],p['span'],dtype=arrays['parent'].dtype) for p in parts]))
 for part in parts:
  for child in range(part['count']+(part['span']==1557)):
   cell=part['first_cell']+child;t=q(part['a_exact'])+(q(part['b_exact'])-q(part['a_exact']))*fmpq(child,part['count']);m=ratfloat(arrays['tb'][cell]);r=ratfloat(arrays['tb_rad'][cell]);assert m-r<=t<=m+r
 print(json.dumps({'utc':utc(),'stage':'inputs_ready','resumed_spans':resumed,'selected_spans':len(selected),'seconds':monotonic()-started}),flush=True)
 targets=set(selected[resumed:]);footer=False
 with gzip.open(paths['archive'],'rt') as f,output.open('a') as out:
  ah=strict_json(next(f));assert ah['type']=='header' and ah['degree']==7 and ah['spans']==1558 and ah['cells']==7809 and ah['stream_modes']==261 and ah['comparison_grid_sha256']==GREEN_SHA and ah['hashes']['input']==TRIAL_SHA
  last=-1
  for line in f:
   rec=strict_json(line)
   if rec['type']=='complete':assert last==1557 and rec['spans']==1558 and rec['cells']==7809 and not f.read();footer=True;break
   assert rec['type']=='span' and rec['span']==last+1;last+=1;part=parts[last];assert all(rec[k]==v for k,v in part.items())
   if last not in targets:
    if not header['full_run'] and last>selected[-1]:break
    continue
   try:row=calculate_span(rec,part,knots,S,nonempty[last][0],arrays,samples)
   except BaseException as exc:
    (E/(args.tag+'_failure.json')).write_text(json.dumps({'utc':utc(),'span':last,'exception':type(exc).__name__,'detail':str(exc)},indent=2)+'\n');raise
   append(out,row);rows.append(row)
   if len(rows)%10==0 or len(rows)==len(selected):
    progress={'utc':utc(),'spans_complete':len(rows),'spans_required':len(selected),'cells_complete':sum(r['count'] for r in rows),'seconds_this_process':monotonic()-started};(E/(args.tag+'_progress.json')).write_text(json.dumps(progress,indent=2)+'\n');print(json.dumps(progress),flush=True)
  if header['full_run']:assert footer
  assert len(rows)==len(selected)
  if not had_footer:append(out,{'type':'complete','utc':utc(),'spans':len(rows),'cells':sum(r['count'] for r in rows),'combined_stream_sha256':hashlib.sha256(''.join(r['stream_sha256']+r['H_stream_sha256'] for r in rows).encode()).hexdigest()})
 assert sha(args.green)==GREEN_SHA and sha(paths['archive'])==ARCHIVE_SHA
 captures=[v for r in rows for v in r['selected_records']];keys={(v['cell'],v['power'],v['mode']) for v in captures};assert len(keys)==len(captures)
 if header['full_run']:assert keys==samples
 summary={'utc':utc(),'status':'COMPUTED_FULL_REQUIRES_OUTPUT_AUDIT' if header['full_run'] else 'OPEN_PARTIAL_DIAGNOSTIC','spans':len(rows),'cells':sum(r['count'] for r in rows),'counts':dict(sum((Counter(r['counts']) for r in rows),Counter())),'selected_records':len(captures),'resumed_spans':resumed,'resume_events':resume_events,'resume_events_sha256':sha(resume_path) if resume_path.exists() else None,'archive_footer_read':footer,'files':pins,'source_sha256':sha(Path(__file__)),'output_sha256':sha(output),'seconds_this_process':monotonic()-started,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'All or explicitly partial finite-annulus spline T coefficients and original H polynomials only. No new I/J integration, radial remainder, flow or IPM endpoint.'}
 (E/(args.tag+'_summary.json')).write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:v for k,v in summary.items() if k!='files'},indent=2),flush=True)
if __name__=='__main__':main()

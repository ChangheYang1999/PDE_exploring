"""Every canonical Green A/B boundary: Arb particular polynomials versus iv convolution."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from datetime import datetime,timezone
from time import monotonic
import argparse,gzip,hashlib,json,math,resource,sys
import numpy as np
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/full_green_linkage';E=D/'evidence';N=96
ctx.prec=512;ctx.threads=1;iv.dps=180
ARCHIVE_SHA='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
GREEN_SHA='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
PARTITION_SHA='56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2'
TRIAL_SHA='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def qa(v):v=F(v);return arb(fmpq(v.numerator,v.denominator))
def qi(v):v=F(v);return iv.mpf(v.numerator)/v.denominator
def fa(v):m,e=v.man_exp();return F(int(m))*F(2)**int(e)
def fi(t):
 s,m,e,bc=t;assert bc>=0 and m>=0 and s in (0,1),'nonfinite iv endpoint'
 return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(v):
 if isinstance(v,arb):assert v.is_finite();lo,hi=fa(v.lower()),fa(v.upper())
 else:lo,hi=fi(v._mpi_[0]),fi(v._mpi_[1])
 assert lo<=hi
 return lo,hi

def decode(v):
 assert v['schema']=='arb-dyadic-mid-radius-v1'
 m=F(int(v['mid_m']))*F(2)**int(v['mid_e']);r=F(int(v['rad_m']))*F(2)**int(v['rad_e']);assert r>=0
 return m,r

def dual(v):
 m,r=decode(v)
 return qa(m-r).union(qa(m+r)),qi(m)+iv.mpf([-1,1])*qi(r)

def horner(p,x):
 result=p[-1]*0
 for a in reversed(p):result=result*x+a
 return result

def endpoint_poly(p,shift,reverse=False):
 q=[]
 for j in range(len(p)):
  v=sum((p[k]*qi(math.comb(k,j)*shift**(k-j)) for k in range(j,len(p))),qi(0))
  q.append(-v if reverse and j%2 else v)
 return q

def particular(p,kappa,sign):
 if not kappa:return [arb(0)]+[sign*a/(j+1) for j,a in enumerate(p)]
 q=[arb(0)]*len(p);nxt=arb(0)
 for j in reversed(range(len(p))):q[j]=(sign*p[j]-(j+1)*nxt)/kappa;nxt=q[j]
 return q

@lru_cache(maxsize=32768)
def expa(rate,u):return qa(rate*u).exp()

moment_metrics=Counter();max_phi7_tail=F(0)
@lru_cache(maxsize=32768)
def convolution(rate,u):
 """Return exp(rate*u) and the eight complete convolution moments."""
 global max_phi7_tail
 assert u>=0
 if not u:return qi(1),tuple(qi(0) for _ in range(8))
 zexact=rate*u;assert abs(zexact)<F(263,25)
 z=qi(zexact);expo=iv.exp(z)
 if not rate:
  moment_metrics['zero_rate_exact_moments']+=1
  return expo,tuple(qi(u**(j+1)/F(j+1)) for j in range(8))
 term=qi(F(1,8));total=term
 for l in range(1,N+1):term=term*z/(l+8);total+=term
 ratio=qi(abs(zexact))/(N+10);assert ends(ratio)[1]<1
 tail=abs(term)*qi(abs(zexact))/(N+9)/(1-ratio)
 top=ends(tail)[1];assert top>=0;max_phi7_tail=max(max_phi7_tail,top)
 phi=[None]*8;phi[7]=total+iv.mpf([-1,1])*qi(top)
 for j in range(6,-1,-1):phi[j]=(1+z*phi[j+1])/(j+1)
 moments=tuple(qi(u**(j+1))*phi[j] for j in range(8))
 for x in moments:assert ends(x)[0]>0
 moment_metrics['phi7_series_with_complete_tail']+=1;moment_metrics['descending_phi_identities']+=7
 return expo,moments

def propagated(endpoint,p,rate,u):
 expo,moments=convolution(rate,u)
 return expo*endpoint+sum((x*y for x,y in zip(p,moments)),qi(0))

def evaluate_span(rec,selected_nodes=None):
 """No exported A/B values are arguments to either reconstruction."""
 a,b=F(rec['a_exact']),F(rec['b_exact']);h=b-a;mid=(a+b)/2;assert h>0 and F(rec['polynomial_mid_exact'])==mid
 Hraw=rec['density_polynomials'];assert len(Hraw)==262 and all(len(p)==8 for p in Hraw)
 assert all(decode(v)==(F(0),F(0)) for v in Hraw[261])
 assert len(rec['i_left'])==len(rec['j_right'])==261
 hp=[list(zip(*(dual(v) for v in p))) for p in Hraw]
 Ha=[list(p[0]) for p in hp];Hi=[list(p[1]) for p in hp]
 Ia,Ii=map(list,zip(*(dual(v) for v in rec['i_left'])));Ja,Ji=map(list,zip(*(dual(v) for v in rec['j_right'])))
 left=[endpoint_poly(p,-h/2) for p in Hi];right=[endpoint_poly(p,h/2,True) for p in Hi]
 ip=[particular(Ha[n-1],2*n+4,1) for n in range(1,262)]
 jp=[particular(Ha[n],4-2*n,-1) for n in range(1,262)]
 ir=[Ia[n-1]-horner(ip[n-1],qa(-h/2)) for n in range(1,262)]
 jr=[Ja[n-1]-horner(jp[n-1],qa(h/2)) for n in range(1,262)]
 count=int(rec['count']);first=int(rec['first_cell']);nodes=range(count+(rec['span']==1557))
 for j in nodes:
  index=first+j
  if selected_nodes is not None and index not in selected_nodes:continue
  t=a+h*F(j,count);u=t-a;v=b-t;x=qa(t-mid);exp4a=qa(4*t).exp();exp4i=iv.exp(qi(4*t));ux=qi(u)
  hvA=[horner(p,x) for p in Ha];hvI=[horner(p,ux) for p in left]
  for n in range(1,262):
   im=horner(ip[n-1],x)+expa(-(2*n+4),u)*ir[n-1]
   jm=horner(jp[n-1],x)+expa(4-2*n,v)*jr[n-1]
   ii=propagated(Ii[n-1],left[n-1],-(2*n+4),u)
   ji=propagated(Ji[n-1],right[n],4-2*n,v)
   sa=(hvA[n-1]+hvA[n])/2;si=(hvI[n-1]+hvI[n])/2
   yield index,t,n,{'A':{'arb':exp4a*(sa-2*n*im),'iv':exp4i*(si-2*n*ii)},'B':{'arb':exp4a*(2*n*jm-sa),'iv':exp4i*(2*n*ji-si)}}

def classification(lo,hi,tl,th):
 if tl<=lo<=hi<=th:return 'CONTAINED'
 if max(lo,tl)>min(hi,th):return 'DISJOINT'
 return 'OVERLAP_ONLY'

def sample_pairs():
 seed=hashlib.sha256((ARCHIVE_SHA+GREEN_SHA).encode()).hexdigest();pairs=set()
 for j in range(128):
  h=hashlib.sha256((seed+':'+str(j)).encode()).digest();pairs.add((int.from_bytes(h[:8],'big')%7810,1+int.from_bytes(h[8:16],'big')%261))
 assert len(pairs)==128
 return seed,pairs

def inspect_inputs():
 files={};paths={'archive':B/'research/middle_residual/evidence/original_knots.jsonl.gz','partition':B/'research/middle_residual/evidence/partition_exact.json','trial':B/'data_exact/modal_v2.json','archive_audit':B/'research/middle_residual/evidence/knot_audit.json','old_selected':B/'research/modal_green/evidence/selected_boundaries.json','old_verdict':B/'research/modal_green/evidence/output_audit.json'}
 expected={'archive':ARCHIVE_SHA,'partition':PARTITION_SHA,'trial':TRIAL_SHA}
 for k,p in paths.items():
  digest=sha(p);files[str(p.relative_to(B))]=digest
  if k in expected:assert digest==expected[k],k
 audit=json.loads(paths['archive_audit'].read_text());assert audit['status']=='PASS' and audit['archive_sha256']==ARCHIVE_SHA and audit['partition_sha256']==PARTITION_SHA
 partition=json.loads(paths['partition'].read_text());assert partition['input_sha256']==TRIAL_SHA and partition['grid_sha256']==GREEN_SHA and partition['cells']==7809
 parts=partition['spans'];assert len(parts)==1558
 first=0;previous=None
 for i,p in enumerate(parts):
  a,b=F(p['a_exact']),F(p['b_exact']);assert p['span']==i and p['first_cell']==first and p['count']>0 and a<b
  assert b-a<F(1,50) and 526*(b-a)<F(263,25)
  if previous is not None:assert a==previous
  previous=b;first+=p['count']
 assert first==7809
 old=json.loads(paths['old_selected'].read_text());oa=json.loads(paths['old_verdict'].read_text());assert old['counts']=={'CONTAINED':180,'OVERLAP_ONLY':0,'DISJOINT':0}
 assert oa['status'].startswith('CONFIRMED'),oa['status']
 assert oa['result_sha256']==sha(paths['old_selected']) and oa['compared_artifact_sha256']==GREEN_SHA
 assert audit['spans']==1558 and audit['cells']==7809 and audit['footer_read']
 # Old accepted result has its own pinned exact output and comparison artifact.
 assert old['green_sha256']==GREEN_SHA and old['input_sha256']==TRIAL_SHA
 fixtures={(r['boundary_index'],r['stream_index_n'],r['array']):r for r in old['comparisons']};assert len(fixtures)==180
 for p in (D/'PROOF.md',D/'ADDENDUM.md',D/'evidence/proof_first.json',D/'evidence/addendum_first.json',Path(__file__)):files[str(p.relative_to(B))]=sha(p)
 return paths,parts,fixtures,files

def make_header(args,parts,files,selected,seed,samples):
 return {'type':'header','schema':'ipm-full-green-linkage-v1','utc':utc(),'selected_spans':selected,'full_run':selected==list(range(1558)),'engines':{'arb_bits':512,'iv_decimal_digits':180,'phi7_series_last_index':N},'files':files,'green_path':str(args.green),'green_sha256':GREEN_SHA,'expected_spans':len(selected),'expected_boundaries':sum(parts[i]['count']+(i==1557) for i in selected),'sample_seed':seed,'sample_pairs':sorted([list(x) for x in samples])}

def append_record(f,v):f.write(json.dumps(v,separators=(',',':'),sort_keys=True)+'\n');f.flush();os.fsync(f.fileno())

def audit_saved_span(row,part):
 assert row['type']=='span' and row['span']==part['span']
 for k in ('first_cell','count','a_exact','b_exact'):assert row[k]==part[k]
 nb=part['count']+(part['span']==1557);expected=nb*261
 assert row['boundaries']==nb and len(row['stream_sha256'])==64
 for name in ('A','B'):
  for eng in ('arb','iv'):
   c=row['counts'][name+'/'+eng];assert c=={'CONTAINED':expected},c
 assert row['cross_engine_overlaps']==2*expected and not row['failures']


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='full');ap.add_argument('--spans',default='all');ap.add_argument('--resume',action='store_true');ap.add_argument('--green',type=Path,default=B.parent/'ipmA-num/data/cert_green.npz');args=ap.parse_args();assert args.tag.replace('_','').isalnum()
 resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=monotonic();paths,parts,fixtures,files=inspect_inputs();assert sha(args.green)==GREEN_SHA
 selected=list(range(1558)) if args.spans=='all' else sorted(set(map(int,args.spans.split(','))));assert selected and 0<=selected[0]<=selected[-1]<1558
 seed,samples=sample_pairs();header=make_header(args,parts,files,selected,seed,samples);output=E/(args.tag+'_spans.jsonl');saved=[];had_footer=False
 if output.exists():
  assert args.resume,'Existing output requires explicit --resume'
  with output.open('r+b') as f:
   line=f.readline();assert line.endswith(b'\n');old=json.loads(line)
   assert {k:v for k,v in old.items() if k!='utc'}=={k:v for k,v in header.items() if k!='utc'};header=old
   while True:
    offset=f.tell();line=f.readline()
    if not line:break
    if not line.endswith(b'\n'):f.seek(offset);f.truncate();break
    r=json.loads(line)
    if r['type']=='complete':assert len(saved)==len(selected) and not f.read();had_footer=True;break
    assert len(saved)<len(selected);audit_saved_span(r,parts[selected[len(saved)]]);saved.append(r)
 else:
  with output.open('w') as f:append_record(f,header)
 with np.load(args.green,allow_pickle=False) as g:
  arrays={k:g[k] for k in ('A_mid','A_rad','B_mid','B_rad','tb','tb_rad','parent')}
 for k,x in arrays.items():
  assert np.all(np.isfinite(x)),k
  if k!='parent':assert x.dtype==np.dtype('float64'),(k,x.dtype)
 assert arrays['parent'].shape==(7809,) and np.issubdtype(arrays['parent'].dtype,np.integer)
 assert np.array_equal(arrays['parent'],np.concatenate([np.full(p['count'],p['span'],dtype=arrays['parent'].dtype) for p in parts]))
 for name in ('A','B'):assert arrays[name+'_mid'].shape==arrays[name+'_rad'].shape==(7810,261) and np.all(arrays[name+'_rad']>=0)
 assert arrays['tb'].shape==arrays['tb_rad'].shape==(7810,) and np.all(arrays['tb_rad']>=0)
 for p in parts:
  for j in range(p['count']+(p['span']==1557)):
   i=p['first_cell']+j;t=F(p['a_exact'])+(F(p['b_exact'])-F(p['a_exact']))*F(j,p['count']);m=F.from_float(float(arrays['tb'][i]));r=F.from_float(float(arrays['tb_rad'][i]));assert m-r<=t<=m+r
 print(json.dumps({'utc':utc(),'stage':'inputs_ready','selected_spans':len(selected),'resumed_spans':len(saved),'expected_boundaries':header['expected_boundaries']}),flush=True)
 targets=set(selected[len(saved):]);rows=list(saved)
 with output.open('a') as out,gzip.open(paths['archive'],'rt') as f:
  ah=json.loads(next(f));assert ah['type']=='header' and ah['degree']==7 and ah['stream_modes']==261 and ah['spans']==1558 and ah['cells']==7809 and ah['comparison_grid_sha256']==GREEN_SHA and ah['hashes']['input']==TRIAL_SHA
  last=-1;archive_footer=False
  for line in f:
   rec=json.loads(line)
   if rec['type']=='complete':assert rec['spans']==1558 and rec['cells']==7809 and last==1557 and not f.read();archive_footer=True;break
   assert rec['type']=='span' and rec['span']==last+1;last+=1
   assert all(rec[k]==parts[last][k] for k in parts[last])
   if last not in targets:
    if not header['full_run'] and last>selected[-1]:break
    continue
   counts={name+'/'+eng:Counter() for name in ('A','B') for eng in ('arb','iv')};worst={};cross=0;records=hashlib.sha256();captured=[];failures=[];boundaryset=set()
   for index,t,n,vals in evaluate_span(rec):
    boundaryset.add(index)
    for name,engines in vals.items():
     bounds={eng:ends(x) for eng,x in engines.items()};la,ha=bounds['arb'];li,hi=bounds['iv']
     m=F.from_float(float(arrays[name+'_mid'][index,n-1]));r=F.from_float(float(arrays[name+'_rad'][index,n-1]));tl,th=m-r,m+r
     data={'boundary':index,'n':n,'array':name,'t_exact':str(t),'target_mid_hex':float(arrays[name+'_mid'][index,n-1]).hex(),'target_rad_hex':float(arrays[name+'_rad'][index,n-1]).hex(),'bounds':{eng:list(map(str,q)) for eng,q in bounds.items()}}
     if max(la,li)>min(ha,hi):
      data['error']='DISJOINT_ENGINE_ENCLOSURES';(E/(args.tag+'_failure.json')).write_text(json.dumps(data,indent=2)+'\n');raise AssertionError(data['error'])
     cross+=1
     for eng,(lo,hi) in bounds.items():
      key=name+'/'+eng;status=classification(lo,hi,tl,th);counts[key][status]+=1
      margin=min(lo-tl,th-hi)
      if key not in worst or margin<F(worst[key]['margin_exact']):worst[key]={'margin_exact':str(margin),'entry':data}
      if status!='CONTAINED':failures.append({'engine':eng,'status':status,'entry':data})
     if (index,n,name) in fixtures or (index,n) in samples:
      if (index,n,name) in fixtures:assert fixtures[(index,n,name)]['log_boundary_exact']==str(t)
      captured.append(data)
     records.update(json.dumps(data,separators=(',',':'),sort_keys=True).encode()+b'\n')
   row={'type':'span',**parts[last],'boundaries':len(boundaryset),'counts':{k:dict(v) for k,v in counts.items()},'cross_engine_overlaps':cross,'stream_sha256':records.hexdigest(),'worst_raw_margins':worst,'selected_records':captured,'failures':failures,'utc':utc(),'seconds_this_process':monotonic()-start}
   if failures:
    (E/(args.tag+'_failed_span.json')).write_text(json.dumps(row,indent=2)+'\n');raise AssertionError(('noncontained',last,len(failures)))
   audit_saved_span(row,parts[last]);append_record(out,row);rows.append(row)
   if len(rows)%10==0 or len(rows)==len(selected):print(json.dumps({'utc':utc(),'spans_complete':len(rows),'spans_required':len(selected),'seconds_this_process':monotonic()-start,'cached_convolutions':convolution.cache_info().currsize}),flush=True)
  if header['full_run']:assert archive_footer
  assert len(rows)==len(selected)
  if not had_footer:append_record(out,{'type':'complete','utc':utc(),'spans':len(rows),'boundaries':sum(r['boundaries'] for r in rows),'stream_rows_sha256':hashlib.sha256(''.join(r['stream_sha256'] for r in rows).encode()).hexdigest()})
 assert sha(args.green)==GREEN_SHA and sha(paths['archive'])==ARCHIVE_SHA
 captures=[v for r in rows for v in r['selected_records']];keys={(v['boundary'],v['n'],v['array']) for v in captures};assert len(keys)==len(captures)
 if header['full_run']:assert set(fixtures)<=keys and {(i,n,name) for i,n in samples for name in ('A','B')}<=keys
 summary={'utc':utc(),'status':'COMPUTED_FULL_REQUIRES_OUTPUT_AUDIT' if header['full_run'] else 'OPEN_PARTIAL_DIAGNOSTIC','spans':len(rows),'boundaries':sum(r['boundaries'] for r in rows),'entries_per_engine':sum(r['boundaries'] for r in rows)*261*2,'all_counts':{k:dict(sum((Counter(r['counts'][k]) for r in rows),Counter())) for k in ('A/arb','A/iv','B/arb','B/iv')},'selected_records':len(captures),'series_metrics_this_process':dict(moment_metrics),'max_phi7_tail_this_process_exact':str(max_phi7_tail),'source_sha256':sha(Path(__file__)),'output_sha256':sha(output),'files':files,'seconds_this_process':monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Full or explicitly partial A/B boundary membership using the accepted canonical archive. No second complete canonical integration, no T membership or full-flow claim.'}
 (E/(args.tag+'_summary.json')).write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:v for k,v in summary.items() if k not in ('files','all_counts')},indent=2),flush=True)
if __name__=='__main__':main()

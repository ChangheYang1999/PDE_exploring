"""Exact finite matrix-margin recount of one already admitted balanced root."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
from math import isqrt
import argparse, gzip, json, os, sys, time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--publication',required=True);p.add_argument('--output',required=True);a=p.parse_args()
assert os.sched_getaffinity(0)=={50}and os.getpriority(os.PRIO_PROCESS,0)>=19
assert all(os.environ.get(x)=='1'for x in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'])
start=datetime.now(timezone.utc);tick=time.monotonic();checks=0;files={}
def ck(b):
 global checks
 assert b;checks+=1
def h(path):
 d=sha256()
 with path.open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
def local(n):
 p=Path(n);ck(not p.is_absolute()and '..'not in p.parts and str(p)==n);return R/p
def bind(n,v=None):
 p=local(n);z=h(p);ck(v is None or z==v);ck(n not in files or files[n]==z);files[n]=z;return p
def read(p):return json.loads(p.read_text())
def lower_decimal(q):
 n=(q.numerator*10**12)//q.denominator;v=Q(n,10**12);ck(v<=q<v+Q(1,10**12));return str(v)
pub=read(bind(a.publication));ck(pub['status']=='CONFIRMED_LOCAL_COMPONENTS')
for n,v in pub['files'].items():bind(n,v)
paths=[n for n in pub['files']if n.endswith('/result.json.gz')];ck(len(paths)==1)
with gzip.open(local(paths[0]),'rt')as f:x=json.load(f)
ck(x['status']=='COMPLETED_BALANCED_ROOT_REPLAY');j=x['index'];ck(type(j)is int and 0<=j<127)
checks_paths=[n for n in pub['files']if n.endswith('/check_v01.json')and '/roots/root_'in n];ck(len(checks_paths)==1)
component=read(local(checks_paths[0]));ck(component['status']=='PASS_ADOPTED_BALANCED_COMPONENTS'and component['root']==x['root'])
ck(component['result_sha256']==pub['files'][paths[0]])
for suffix,field in [('/execution.json','receipt_sha256'),('/actual_review_v01.json','actual_review_sha256')]:
 matches=[n for n in pub['files']if n.endswith(suffix)];ck(len(matches)==1 and pub['files'][matches[0]]==component[field])
ck(component['flags']['primary']is True)
ck(x['source']['id']=='C2-N1-013'and x['source']['fixed_c_exact']=='4076476460239181/2251799813685248')
ck(x['source']['raw_sha256']=='a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a')
ck(x['complete_angular_partition']is True and x['root']['index']==j)
ck([Q(x['root'][k])for k in ['left_exact','right_exact']]==[Q(j,128),Q(j+1,128)])
ck(x['aggregates']['primary']['all_leaves_pass']is True)
dlo=(1+3*Q(j,128))/4;dhi=(1+3*Q(j+1,128))/4;rows=[];previous=Q(-1);scale=10**12
ck([r['word']for r in x['leaves']]==x['leaf_words'])
for row in x['leaves']:
 w=row['word'];ck(isinstance(w,str)and set(w)<={'0','1'}and len(w)<=12)
 k=int(w or '0',2);den=2**len(w);lo=Q(2*k,den)-1;hi=Q(2*(k+1),den)-1
 ck([lo,hi]==list(map(Q,row['angular_interval_exact']))and lo==previous);previous=hi
 v={n:list(map(Q,row['bounds'][n]))for n in ['a','b','e']}
 for z in v.values():ck(len(z)==2 and z[0]<=z[1])
 al,bl=v['a'][0],v['b'][0];eu=max(map(abs,v['e']));K=Q(1)if lo<=0<=hi else 1-min(lo*lo,hi*hi)
 discr=((al-bl)/2)**2+K*eu*eu;n=isqrt(discr.numerator*scale*scale//discr.denominator)+1;u=Q(n,scale)
 ck(Q(n-1,scale)**2<=discr<u*u)
 L=(al+bl)/2-u;ell=Q(3,5)+L/(dlo if L<0 else dhi)
 ck(ell<=Q(3,5)+L/dlo and ell<=Q(3,5)+L/dhi)
 rows.append(dict(word=w,angular_interval_exact=[str(lo),str(hi)],K_exact=str(K),strict_sqrt_upper_exact=str(u),scaled_lower_exact=str(L),lambda_min_lower_exact=str(ell),outward_lower_exact=lower_decimal(ell)))
ck(previous==1 and bool(rows));worst=min(rows,key=lambda r:Q(r['lambda_min_lower_exact']));ell=Q(worst['lambda_min_lower_exact']);combined=max(Q(3,5),ell)
for p in [Path(__file__),D/'PROOF_v02.md',D/'formal/README.md']:bind(str(p.relative_to(R)))
for n,v in files.items():ck(h(local(n))==v)
out=local(a.output);ck(out.parent==D/'verification');outward=lower_decimal(ell)
z=dict(status='CONDITIONAL_EXACT_BALANCED_MATRIX_MARGIN',started_utc=start.isoformat(),finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,checks=checks,index=j,source=x['source'],root=x['root'],leaves=rows,minimum_word=worst['word'],lambda_min_lower_exact=str(ell),outward_lower_exact=outward,combined_with_prior_exact=str(combined),targets={n:combined>=Q(n)for n in ['7/10','71/100','3/4']},files=files,scope='Exact arithmetic on imported successfully admitted containing intervals; independent review required for a stronger regional matrix claim. No global bound or closure.')
with out.open('x')as f:json.dump(z,f,indent=2);f.write('\n')
print('MATRIX_MARGIN',j,z['outward_lower_exact'],z['targets'],'checks',z['checks'],'seconds',z['elapsed_seconds'],flush=True)

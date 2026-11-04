"""Exact matrix-margin adapter for a complete ordinary-host local recount."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from math import isqrt
import argparse,gzip,json,os,sys,time
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'scripts'))
from campaign_bindings_v01 import Bindings,digest,named,P
sys.set_int_max_str_digits(0)
p=argparse.ArgumentParser()
for n in ['recount','recount-sha256','output']:p.add_argument('--'+n,required=True)
a=p.parse_args()
assert os.sched_getaffinity(0)=={50} and os.getpriority(os.PRIO_PROCESS,0)>=19
assert all(os.environ.get(k)=='1' for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'])
start=datetime.now(timezone.utc);tick=time.monotonic();b=Bindings();checks=0
J=list(range(97,55,-1));H=P/'numerics_agent_2/source_host_049/ordinary_v01';scale=10**12
out=named(R,a.output);assert out.parent==D/'verification' and not out.exists()
def ck(x):
 global checks
 assert x;checks+=1
def interval(v):
 ck(type(v)is list and len(v)==2);lo,hi=map(Q,v);ck(lo<=hi);return lo,hi
rp=named(R,a.recount);ck(rp.parent==R/'research/ordinary_slabs_host_method/verification');b.add(rp,a.recount_sha256)
c=json.loads(rp.read_text());ck(c['status']=='CONFIRMED_RECOUNT' and c['checks']>0)
ck([x['root_index']for x in c['slabs']]==J);b.mapping(P,c['bindings'])
records=[]
for spec in c['slabs']:
 st=time.monotonic();j=spec['root_index'];cp=H/f'cells_root{j}_v01.json.gz';name=str(cp.relative_to(P))
 ck(name in c['bindings']);b.add(cp,c['bindings'][name])
 with gzip.open(cp,'rt')as f:x=json.load(f)
 ck(x['status']=='COMPUTED' and x['root_index']==j and x['joint_flags']['primary']is True and spec['joint_flags']['primary']is True)
 ck(x['radial_cells']==32 and x['angular_cells']==256 and x['cell_count']==8192 and len(x['cells'])==8192)
 sigma=Q(255-2*j,256);rho=Q(1,255-2*j)
 ck(Q(x['sigma_exact'])==sigma and Q(x['rho_exact'])==rho)
 domain=[str(Q(j,128-j)),str(Q(j+1,127-j))];ck(x['domain_r_squared']==spec['domain_r_squared']==domain)
 seen=set();worst=None
 for v in x['cells']:
  u,k=v['radial_index'],v['angular_index'];ck(type(u)is int and type(k)is int and 0<=u<32 and 0<=k<256 and(u,k)not in seen);seen.add((u,k))
  al,au=interval(v['fields']['a']);bl,bu=interval(v['fields']['b']);el,eu=interval(v['fields']['e']);sl,su=interval(v['sin_squared'])
  K=min(Q(1),su);ck(K>=0 and sl<=1)
  xl=-rho+2*rho*Q(u,32);xh=-rho+2*rho*Q(u+1,32);dl=1-Q(3,4)*sigma*(1+xh);dh=1-Q(3,4)*sigma*(1+xl);ck(0<dl<=dh)
  disc=((al-bl)/2)**2+K*max(abs(el),abs(eu))**2;n=isqrt(disc.numerator*scale*scale//disc.denominator)+1;ck(Q(n-1,scale)**2<=disc<Q(n,scale)**2)
  L=(al+bl)/2-Q(n,scale);ell=Q(3,5)+L/(dl if L<0 else dh)
  if worst is None or ell<worst[0]:worst=(ell,u,k)
 ck(len(seen)==8192);val=Q(worst[0].numerator*scale//worst[0].denominator,scale);ck(val<=worst[0]<val+Q(1,scale))
 b.add(cp,c['bindings'][name]);row=dict(index=j,archive=name,archive_sha256=c['bindings'][name],cell_count=len(seen),domain_r_squared=domain,minimum_cell=list(worst[1:]),minimum_lower_exact=str(worst[0]),outward_lower_exact=str(val),seconds=time.monotonic()-st);records.append(row)
 print('HOST_MATRIX',j,str(val),row['seconds'],flush=True)
for fp in [D/'PROOF.md',D/'formal/README.md',Path(__file__),R/'scripts/campaign_bindings_v01.py']:b.add(fp)
b.recheck();lower=min(Q(x['outward_lower_exact'])for x in records)
z=dict(status='CONDITIONAL_EXACT_HOST_MATRIX_RECOUNT',started_utc=start.isoformat(),finished_utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-tick,arithmetic_checks=checks,binding_checks=b.checks,recount_sha256=a.recount_sha256,regions=records,union_r_squared=['7/9','49/15'],minimum_outward_lower_exact=str(lower),files=b.own(),external_bindings=b.external(),data_symlink_aliases=b.symlinks,scope='Exact arithmetic on the complete locally recounted host intervals. Source containment and stronger matrix claims require distinct independent actual review. No global bound or closure.')
with out.open('x')as f:json.dump(z,f,indent=2);f.write('\n')
print('HOST_MATRIX_DONE',checks,b.checks,str(lower),z['seconds'],flush=True)

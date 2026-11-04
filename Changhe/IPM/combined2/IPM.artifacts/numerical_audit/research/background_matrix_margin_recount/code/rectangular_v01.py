"""Exact eigenvalue recount of frozen, already admitted rectangular field cells."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
from math import isqrt
import gzip,json,time,os,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parents[1]
assert os.sched_getaffinity(0)=={50}and os.getpriority(os.PRIO_PROCESS,0)>=19
assert all(os.environ.get(k)=='1'for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'])
checks=0
def ck(x):
 global checks
 assert x;checks+=1
def h(p):
 z=sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):z.update(b)
 return z.hexdigest()
def path(n):
 q=Path(n);ck(not q.is_absolute()and str(q)==n)
 p=(R/q).resolve();ck(p.is_relative_to(R.parent.resolve())and p.relative_to(R.parent.resolve()).parts[0]in ['numerical_audit','theory_audit']);return p
def interval(x):
 ck(isinstance(x,list)and len(x)==2);a,b=map(Q,x);ck(a<=b);return a,b
mfile=D/'verification/rectangular_manifest_v01.json';m=json.loads(mfile.read_text());start=datetime.now(timezone.utc);tick=time.monotonic()
ck(m['status']=='PREPARED_RECTANGULAR_MATRIX_RECOUNT')
ck(m['fixed_c_exact']=='4076476460239181/2251799813685248'and m['source_archive_sha256']=='2e3c649402c72ad50836f41f35c5657f50232a877557a5641038262355fa689d')
for n,v in m['files'].items():ck(h(path(n))==v)
ck([(r['kind'],r['index'])for r in m['regions']]==[('slab',j)for j in list(range(126,106,-1))+[105,103,101,99]]+[('annulus',k)for k in range(7,21)]+[('terminal',21)])
rows=[];scale=10**12
for spec in m['regions']:
 st=time.monotonic();name=spec['archive'];ck(name in m['files'])
 with gzip.open(path(name),'rt')as f:x=json.load(f)
 kind=spec['kind'];idx=spec['index'];nr=spec['radial_cells'];na=256
 ck(x['cell_count']==nr*na==len(x['cells']))
 if kind=='slab':
  ck(x['status']=='COMPUTED'and x['root_index']==idx and x['joint_flags']['primary']is True)
  sigma=Q(255-2*idx,256);rho=Q(1,255-2*idx);ck(Q(x['sigma_exact'])==sigma and Q(x['rho_exact'])==rho)
  ck(list(map(Q,x['domain_r_squared']))==[Q(idx,128-idx),Q(idx+1,127-idx)])
 elif kind=='annulus':
  ck(x['status']=='CONFIRMED'and x['K']==idx);sigma=Q(3,2**(idx+2));rho=Q(1,3)
 else:ck(kind=='terminal'and x['status']=='CONFIRMED'and x['K']==21 and idx==21)
 if kind!='terminal':ck(x['radial_cells']==nr and x['angular_cells']==na)
 seen=set();worst=None
 for c in x['cells']:
  ui,ai=(c['y_index'],c['phi_index'])if kind=='terminal'else(c['radial_index'],c['angular_index'])
  ck(type(ui)is int and type(ai)is int and 0<=ui<nr and 0<=ai<na and(ui,ai)not in seen);seen.add((ui,ai))
  al,au=interval(c['fields']['a']);bl,bu=interval(c['fields']['b']);el,eu=interval(c['fields']['e']);sl,su=interval(c['sin_squared']);K=min(Q(1),su);ck(K>=0)
  if kind=='terminal':dl=1-Q(3,4*2**21);dh=Q(1)
  else:
   xl=-rho+2*rho*Q(ui,nr);xh=-rho+2*rho*Q(ui+1,nr);dl=1-Q(3,4)*sigma*(1+xh);dh=1-Q(3,4)*sigma*(1+xl)
  ck(0<dl<=dh)
  disc=((al-bl)/2)**2+K*max(abs(el),abs(eu))**2;n=isqrt(disc.numerator*scale*scale//disc.denominator)+1
  ck(Q(n-1,scale)**2<=disc<Q(n,scale)**2)
  L=(al+bl)/2-Q(n,scale);ell=Q(3,5)+L/(dl if L<0 else dh)
  if worst is None or ell<worst[0]:worst=(ell,ui,ai)
 ck(len(seen)==nr*na)
 val=Q((worst[0].numerator*scale)//worst[0].denominator,scale);ck(val<=worst[0]<val+Q(1,scale));ck(h(path(name))==m['files'][name])
 row=dict(kind=kind,index=idx,archive=name,archive_sha256=m['files'][name],cell_count=len(seen),minimum_cell=list(worst[1:]),minimum_lower_exact=str(worst[0]),outward_lower_exact=str(val),combined_lower_exact=str(max(Q(3,5),val)),seconds=time.monotonic()-st)
 rows.append(row);print('REGIONAL_MATRIX',kind,idx,str(val),'seconds',row['seconds'],flush=True)
for n,v in m['files'].items():ck(h(path(n))==v)
z=dict(status='CONDITIONAL_EXACT_RECTANGULAR_MATRIX_RECOUNT',started_utc=start.isoformat(),finished_utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-tick,checks=checks,manifest_sha256=h(mfile),regions=rows,scope='New exact matrix lower bounds from already admitted containing intervals. All new claims require independent review. No inner missing-region or global H4/existence claim.')
with (D/'verification/rectangular_result_v01.json').open('x')as f:json.dump(z,f,indent=2);f.write('\n')
print('RECTANGULAR_DONE',checks,z['seconds'],flush=True)

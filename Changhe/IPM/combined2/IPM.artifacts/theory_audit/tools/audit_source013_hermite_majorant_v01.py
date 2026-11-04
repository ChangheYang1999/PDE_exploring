"""Exact signed cubic Hermite majorant from certified full-plane moments."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime,timezone
from math import isqrt
import os,sys,time,json
sys.set_int_max_str_digits(0)
assert os.sched_getaffinity(0)=={40} and os.getpriority(os.PRIO_PROCESS,0)>=19
B=Path('research/source013_hermite_majorant');V=B/'verification';P=Path('research/source013_moment_refinement');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();n=0;files={}
def ck(x):
 global n
 n+=1;assert x
def h(p):return sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def put(p,d):
 with p.open('x')as f:json.dump(d,f,indent=2);f.write('\n')
for name in ['result_v01.json','certificate_review_v01.json','check_v01.json']:
 src=P/'verification'/name;dst=B/'source'/name
 if not dst.exists():os.link(src,dst)
 ck(h(src)==h(dst));files[str(src)]=h(src);files[str(dst)]=h(dst)
r=read(B/'source/result_v01.json');audit=read(B/'source/check_v01.json');review=read(B/'source/certificate_review_v01.json');ck(audit['status']=='PASS' and audit['output_sha256']==h(B/'source/result_v01.json'));ck(review['status']=='BOUND')
for rel,z in review['bindings'].items():ck(not Path(rel).is_absolute() and h(Path(rel))==z)
ck(r['source']['id']=='C2-N1-013' and r['source']['fixed_c_exact']=='4076476460239181/2251799813685248')
ck([v['order']for v in r['tensor_energies']]==[0,1,2,3]);L=[F(v['lower_exact'])for v in r['tensor_energies']];U=[F(v['upper_exact'])for v in r['tensor_energies']];ck(all(0<=l<=u for l,u in zip(L,U)));q=F(21,10);a=F(1);b=F(13000);t=b-a
# Pairs encode exact coefficients of z_a and z_b.
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def scale(c,x):return (c*x[0],c*x[1])
fa=((1+a)**2,F(0));fb=(F(0),(1+b)**2);ga=(q*(1+a),F(0));gb=(F(0),q*(1+b))
c=scale(1/t**2,add(scale(3,add(fb,scale(-1,fa))),scale(-t,add(gb,scale(2,ga)))))
d=scale(1/t**3,add(scale(t,add(gb,ga)),scale(-2,add(fb,scale(-1,fa)))))
coeff=[add(add(fa,scale(-a,ga)),add(scale(a*a,c),scale(-a**3,d))),add(ga,add(scale(-2*a,c),scale(3*a*a,d))),add(c,scale(-3*a,d)),d]
for x,fv,gv in [(a,fa,ga),(b,fb,gb)]:
 value=(F(0),F(0));deriv=(F(0),F(0))
 for j,p in enumerate(coeff):
  value=add(value,scale(x**j,p))
  if j:deriv=add(deriv,scale(j*x**(j-1),p))
 ck(value==fv and deriv==gv)
def root(v):
 S=10**50;N=v.numerator*S**10//v.denominator;lo=0;hi=1<<((N.bit_length()+9)//10)
 while lo+1<hi:
  m=(lo+hi)//2
  if m**10<=N:lo=m
  else:hi=m
 out=F(lo,S),F(lo+1,S);ck(out[0]**10<=v<=out[1]**10);return out
za=root(1+a);zb=root(1+b)
def enclosure(p):
 terms=[(k*z[0],k*z[1]) for k,z in zip(p,[za,zb])];return sum(min(z)for z in terms),sum(max(z)for z in terms)
ci=[enclosure(p)for p in coeff];parts=[max(pl*l,pl*u,pu*l,pu*u)for (pl,pu),l,u in zip(ci,L,U)];energy=sum(parts);ck(energy>0)
# Sign-specific comparisons catch accidental use of upper moments for negative coefficients.
for (pl,pu),l,u,e in zip(ci,L,U,parts):
 ck(pl<=pu and e==max(pu*l,pu*u))
 if pu<0:ck(e==pu*l)
 if pl>=0:ck(e==pu*u)
K=10**24;k=isqrt(energy.numerator*K*K//energy.denominator);upper=F(k+1,K);ck(upper*upper>=energy);oldlo,oldhi=map(F,r['fractional_norm_interval_exact']);ck(oldlo<=upper<oldhi)
J=10**22;j=-((-upper.numerator*J)//upper.denominator);display=str(j//J)+'.'+str(j%J).zfill(22);ck(F(display)>=upper)
out=dict(source=r['source'],fractional_order_exact=str(q),nodes_exact=[str(a),str(b)],roots_intervals_exact=[[str(v)for v in z]for z in [za,zb]],coefficient_linear_forms=[[str(v)for v in p]for p in coeff],coefficient_intervals_exact=[[str(v)for v in z]for z in ci],moment_choices=['lower'if z[1]<0 else'upper'for z in ci],energy_upper_exact=str(energy),fractional_norm_interval_exact=[str(oldlo),str(upper)],fractional_display=['0.0035510975483434412497',display],old_upper_exact=str(oldhi))
put(V/'result_v01.json',out)
for p in [B/'PROOF.md',Path('tools/audit_source013_hermite_majorant_v01.py')]:files[str(p)]=h(p)
put(V/'check_v01.json',dict(status='PASS',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,checks=n,files=files,output_sha256=h(V/'result_v01.json'),scope='One rigorous signed cubic spectral majorant from accepted full-plane moments; no optimality or closure claim.'))
print('PASS',n,'interval',out['fractional_display'],'coefficient_midpoints',[float((lo+hi)/2)for lo,hi in ci], 'moment_choices',out['moment_choices'])

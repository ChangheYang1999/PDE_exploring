"""Exact middle coverage, directed summaries and independent conditional costs."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[v]='1'
import sys,json,math,time,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_certificate/evidence';ctx.prec=512;ctx.threads=1;iv.dps=180
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def qa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def qi(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def aq(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def iq(x):s,m,e,b=x;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def bounds(x):return tuple(aq(y) for y in [x.lower(),x.upper()]) if isinstance(x,arb) else tuple(iq(y) for y in x._mpi_)
def rec(x):a,b=bounds(x);assert a<=b;return {'lower_exact':str(a),'upper_exact':str(b),'display':[float(a),float(b)]}
def exp_series(x,N=160):
 z=bounds(x)[1];assert 0<=bounds(x)[0]<=z<N+2
 p=iv.mpf(1);s=p
 for j in range(1,N+1):p=p*x/j;s+=p
 tail=qi(z)**(N+1)/math.factorial(N+1)/(1-qi(z)/(N+2))
 return s+iv.mpf([0,tail.b])
def main():
 start=time.monotonic();paths=[E/'flow_middle.json',B/'research/middle_residual/evidence/partition_exact.json',B.parent/'ipmA-num/data/cert_green.npz',Path(__file__),B/'research/flow_certificate/PROOF.md']
 source=json.loads(paths[0].read_text());part=json.loads(paths[1].read_text());d=np.load(paths[2]);tb=d['tb'];tr=d['tb_rad'];pts=[]
 for sp in part['spans']:
  a,b=F(sp['a_exact']),F(sp['b_exact']);n=sp['count'];assert sp['first_cell']==len(pts)
  if pts:assert pts[-1]<a
  pts.extend(a+(b-a)*i/n for i in range(n))
 pts.append(F(part['spans'][-1]['b_exact']));assert len(pts)==7810==len(tb)==len(tr)
 assert part['grid_sha256']==sha(paths[2])=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
 assert source['complete_region'] and source['done'] and source['selection']==[0,None] and source['nc_total']==7809 and len(source['rows'])==7809 and source['ntheta']==200
 geom=0;slack=qa(0);maxh=F(0);checked=[]
 for i,t in enumerate(pts):assert F(float(tb[i]))-F(float(tr[i]))<=t<=F(float(tb[i]))+F(float(tr[i]));geom+=1
 U=2.**-53;beta=np.nextafter(U/(1-U),np.inf);suc=lambda x:np.nextafter(x,np.inf)
 for i,row in enumerate(source['rows']):
  assert row['ci']==i and row['region']=='middle' and F(row['t_a'])==F(float(tb[i]));a,b=pts[i:i+2];assert a<b
  ra,rb=qa(a).exp(),qa(b).exp();assert qa(F(row['r_lo']))<ra and rb<qa(F(row['r_hi']));geom+=2
  m=tb[i+1]-tb[i];rad=suc(suc(suc(tr[i+1]+tr[i])+suc(beta*abs(m))));h=suc(abs(m)+rad);assert F(h)>=b-a and suc(522.*h)<=1.;maxh=max(maxh,F(h));geom+=2
  if i in (0,3803,3963,4102,4134,4667,5396,7808):checked.append({'ci':i,'left_exact':str(a),'right_exact':str(b),'r_left':rec(ra),'r_right':rec(rb),'r_hull_exact':[str(F(row['r_lo'])),str(F(row['r_hi']))],'h_up_exact':str(F(h))})
 rows=source['rows'];glob=source['glob'];ag={}
 for key,kind in [('s_min','min'),('v2y_min','min'),('T0_max_in','max'),('T0_max_out','max'),('V1_max_in','max')]:
  f=min if kind=='min' else max;r=f(rows,key=lambda r:r[key]);assert r[key]==glob[key];ag[key]={'exact':str(F(r[key])),'ci':r['ci']}
 sf=min((r for r in rows if r['r_hi']>=20),key=lambda r:r['s_min']);assert sf['s_min']==glob['s_min_far'];ag['s_min_far']={'exact':str(F(sf['s_min'])),'ci':sf['ci']}
 assert sum(r['n_unresolved'] for r in rows)==glob['n_unresolved']==245 and sum(r['axis_sign_fail'] for r in rows)==glob['axis_sign_fail']==0
 safe=[('T0_max_in','1.278','upper'),('T0_max_out','-0.2399','upper'),('V1_max_in','-12.834','upper'),('v2y_min','0.98845','lower'),('s_min_far','3.4957','lower'),('v1x_axis_above_min','0.0077249','lower')]
 for key,q,kind in safe:assert F(glob[key])<F(q) if kind=='upper' else F(glob[key])>F(q)
 unsafe=[('T0_max_in','1.2779','upper'),('T0_max_out','-0.2400','upper'),('v1x_axis_above_min','0.007725','lower')]
 for key,q,kind in unsafe:assert F(glob[key])>F(q) if kind=='upper' else F(glob[key])<F(q)
 box=[F(float(x)) for x in source['PAR']['box']];assert box[0]<F('4.8') and box[1]>F('6.82') and box[2]>F('2.85');w=box[1]-box[0];assert F('2.02')<w<F('2.020000000000001')
 costs=[]
 for k,limit in [(F(1,5),F('6.31')),(F(11,50),F('5.76'))]:
  z=(F(639,500)+k)*w/F(6417,500);a=qa(z).exp()/qa(k);v=exp_series(qi(z))/qi(k)
  assert bounds(a)[1]<limit and bounds(v)[1]<limit and max(bounds(a)[0],bounds(v)[0])<=min(bounds(a)[1],bounds(v)[1])
  costs.append({'kappa_exact':str(k),'exponent_exact':str(z),'arb':rec(a),'iv_series':rec(v),'strict_upper_exact':str(limit)})
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_GEOMETRY_AND_CONDITIONAL_SCALARS_ONLY','method':'Exact rational partition and directed comparisons; Arb512 exact endpoint exponentials; iv180 positive exponential series for box costs. No flow-field enclosure accepted by this audit alone.','geometry_checks':geom,'cells':7809,'max_h_up_exact':str(maxh),'r20_crossing_cells':[r['ci'] for r in rows if r['r_lo']<20<=r['r_hi']],'geometry_examples':checked,'aggregate':ag,'safe_decimal_comparisons':safe,'unsafe_decimal_comparisons':unsafe,'box_exact':list(map(str,box)),'width_exact':str(w),'costs':costs,'seconds':time.monotonic()-start,'files':{str(p.resolve()):sha(p) for p in paths}}
 (E/'geometry.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['utc','status','geometry_checks','cells','r20_crossing_cells','seconds']}));print([(x['kappa_exact'],x['arb']['display'],x['strict_upper_exact']) for x in costs])
if __name__=='__main__':main()

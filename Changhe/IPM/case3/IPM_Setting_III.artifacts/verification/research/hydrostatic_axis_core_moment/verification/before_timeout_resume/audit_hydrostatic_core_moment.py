"""One-process independent16-state core-moment audit, no producer code."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,time,re
sys.set_int_max_str_digits(0)
import numpy as np
import torch
import mpmath as mp
import gmpy2
from q_local_checkpoint import QLocalCheckpoint
from hydrostatic_axis_primitive import primitive,endpoint,evaluate,mnum
from hydrostatic_core_moment import cheb_to_w,guard,beta_moment,integral_moment,logarithm_coefficient,endpoint_second,exactmp
from independent_hydrostatic import CartesianQJet,VerticalInverse
r=Path('research/hydrostatic_axis_core_moment');dest=r/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
inputs=json.loads((dest/'INPUTS.json').read_text());out={'status':'RUNNING','start_utc':utc(),'pid':os.getpid(),'proof_sha256':sha(r/'PROOF.md'),'driver_sha256':sha(__file__),'library_sha256':sha('independent_code/hydrostatic_core_moment.py'),'checks':[],'states':[]}
def save():(dest/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
def check(name,ok,evidence=None):
 out['checks'].append({'name':name,'passed':bool(ok),'evidence':evidence})
 if not ok:out['status']='FAILED';save();raise AssertionError(name)
# Exact polynomial conversion gate and independent finite integral manufactures.
Q=gmpy2.mpq
for n in [1,2,3,5,9]:
 cc=[Q(j*j-3*j+1,j+1)for j in range(n+1)];pw=cheb_to_w(cc)
 for xx in [Q(0),Q(1,7),Q(1,2),Q(1)]:
  direct=sum((v*xx**j for j,v in enumerate(pw)),Q(0));tt=1-2*xx
  prev=Q(1);cur=tt;expect=cc[0]
  if len(cc)>1:expect+=cc[1]*cur
  for j in range(2,len(cc)):prev,cur=cur,2*tt*cur-prev;expect+=cc[j]*cur
  check(f'exact conversion n{n} x{xx}',direct==expect)
with mp.workdps(85):
 for PP in [Q(5,4),Q(3,2),Q(7,4)]:
  for cc in [[Q(0),Q(1)],[Q(0),Q(0),Q(1)],[Q(0),Q(2),Q(-3),Q(5),Q(1)]]:
   a,_=beta_moment(cc,PP,Q(3));b=integral_moment(cc,PP,Q(3));check(f'finitepart manufacture P{PP} coeff{cc}',abs(a-b)<mp.mpf('1e-70'),mp.nstr(abs(a-b),12))
 a,_=beta_moment([Q(0),Q(1)],Q(3,2),Q(3));check('manufacture k=w negativepi',abs(a+mp.pi*3/2**mp.mpf('1.5'))<mp.mpf('1e-75'))
 a,_=beta_moment([Q(0),Q(0),Q(1)],Q(3,2),Q(3));check('manufacture k=w2 positivepi',abs(a-mp.pi*3/2**mp.mpf('1.5'))<mp.mpf('1e-75'))
for vals in [[Q(0),Q(1),Q(0)],[Q(0),Q(2),Q(1)],[Q(0),Q(-3),Q(5)]]:
 check('exact log coefficient manufacture '+str(vals),logarithm_coefficient(vals,Q(2),Q(4))==vals[2]-vals[1]/4)
save();print(utc(),'manufactures PASS',len(out['checks']),flush=True)
# Freeze parsed producer fits as comparisons, not as input to the independent constants.
producer={};current=None
for line in (dest/'hs_m0.txt').read_text().splitlines():
 mt=re.match(r'=== (\S+) ',line)
 if mt:current=mt.group(1);producer[current]={}
 mt=re.match(r'  m_0 = ([+\-0-9.]+)',line)
 if mt and current:producer[current]['m0_fit']=float(mt.group(1))
 mt=re.search(r'B_log ([+\-0-9.]+)  maxres',line)
 if mt and current:producer[current]['B_log_fit']=float(mt.group(1))
selected_integral={'hsA_c3.0_N48','hsE_c3.0_N96_hr','hsC_c3.0_N128_fine_hr'}
for item in inputs['states']:
 t0=time.monotonic();tag=item['tag'];src=Path(item['frozen']);check('source hash '+tag,sha(src)==item['sha256'])
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(src)
 polys=primitive(q.exact_coefficients(),q.kappa);kw=cheb_to_w(polys['K']);hw=cheb_to_w(polys['H']);PP=Q(q.kappa);LL=Q(q.L)
 check('k endpoint '+tag,kw[0]==0);check('H endpoint '+tag,hw[0]==0)
 kt,ktt=endpoint_second(polys['K']);ht,htt=endpoint_second(polys['H'])
 check('k1 independent endpoint '+tag,kw[1]==-2*kt);check('k2 independent endpoint '+tag,kw[2]==2*ktt)
 check('h1 independent endpoint '+tag,hw[1]==-2*ht);check('h2 independent endpoint '+tag,hw[2]==2*htt)
 cert={key:[[str(t.numerator),str(t.denominator)]for t in val]for key,val in [('k_w',kw),('H_w',hw)]};cert.update(P=[str(PP.numerator),str(PP.denominator)],L=[str(LL.numerator),str(LL.denominator)])
 certfile=dest/(tag+'.polynomials.json');certfile.write_text(json.dumps(cert,indent=2)+'\n')
 row={'tag':tag,'N':q.N,'M':q.M,'source_sha256':item['sha256'],'polynomial_sha256':sha(certfile),'P_exact':str(PP),'L_exact':str(LL),'producer_fits':producer.get(tag,{}),'node_reconstruction':q.node_reconstruction_details(),'values':[]}
 out['states'].append(row);save()
 G=guard(kw+hw);values=[]
 for extra in [65,105]:
  with mp.workdps(G+extra):
   P=exactmp(PP);L=exactmp(LL);p=1-1/P;C=L/2**P;c=mp.mpf(q.cl);KK=exactmp(hw[1])*C**(1/P);QQ=exactmp(kw[1])*C**(1/P)/P;c2=C**(2/P)*(exactmp(hw[2])-exactmp(hw[1])/(2*P));r2=(c*(2*p-1)-1)*c2+KK*QQ/(1-p)
   vals={'precision':mp.mp.dps,'map_p':mp.nstr(p,65),'cp_minus1':mp.nstr(c*p-1,65),'K':mp.nstr(KK,65),'Q':mp.nstr(QQ,65),'c2':mp.nstr(c2,65),'r2':mp.nstr(r2,65),'c2_required_if_cp1':mp.nstr(KK*QQ/((1-p)*(c-1)),65),'centre_defect':mp.nstr(exactmp(polys['cH'])+c-1,65)}
   if PP<2:
    val,mass=beta_moment(kw,PP,LL);vals.update(m0=mp.nstr(val,65),absolute_sum=mp.nstr(mass,12))
   else:
    exactlog=logarithm_coefficient(kw,PP,LL);vals.update(B_log=mp.nstr(exactmp(exactlog),65),B_log_exact=str(exactlog));check('exact log endpoint second method '+tag,exactlog==LL/4*(2*ktt+kt/2))
   values.append(vals)
 row['values']=values
 with mp.workdps(90):
  key='m0'if PP<2 else'B_log';err=abs(mp.mpf(values[0][key])-mp.mpf(values[1][key]));check('precision refinement '+tag,err<mp.mpf('1e-55'),mp.nstr(err,12));row['constant_precision_difference']=mp.nstr(err,12)
 if tag in selected_integral:
  with mp.workdps(G+65):
   integral=integral_moment(kw,PP,LL);closed,_=beta_moment(kw,PP,LL);err=abs(integral-closed);row['finite_integral_check']={'working_digits':mp.mp.dps,'value':mp.nstr(integral,55),'difference':mp.nstr(err,12)};check('convergent integral vs beta '+tag,err<mp.mpf('1e-45'),mp.nstr(err,12))
 row['seconds_exact']=time.monotonic()-t0;save();print(utc(),tag,'exact',key,values[-1][key][:24],'seconds',row['seconds_exact'],flush=True)
 # Cartesian derivatives and independent full vertical quadrature at matching physical points.
 field=CartesianQJet(q);levels=[]
 for order,tail,split in [(24,160,128.),(40,320,512.)]:
  inv=VerticalInverse(field.jet,q.p,order,tail,split,.125);points=[]
  for y in [.1,1.,1e3,1e4,1e8]:
   g,gx,gy,gxx=map(float,field.jet(0.,y));V2=inv.at(0.,y)['V'][1];transport=(q.cl*y+V2)*gy;R=transport-g;Nf=abs(transport)+abs(g);Nv=abs(g)+abs(y*gy)+abs(V2*gy)
   check('physical denominator '+tag+str((order,y)),Nf>0 and Nv>0)
   KK=float(values[-1]['K']);QQ=float(values[-1]['Q']);pm=float(values[-1]['map_p']);F=V2-QQ*y**pm/(pm*(1-pm))
   points.append(dict(y=y,g=g,gy=gy,V2=V2,R=R,Nf=Nf,Nv=Nv,signed_R_Nf=R/Nf,R_Nv=abs(R)/Nv,F=F,y_signed_R_Nf=y*R/Nf))
  levels.append(dict(order=order,tail_order=tail,split=split,points=points));row['physical_levels']=levels;save()
 row['physical_refinement']=[dict(y=a['y'],delta_V2=b['V2']-a['V2'],delta_R_Nf=b['signed_R_Nf']-a['signed_R_Nf'])for a,b in zip(levels[0]['points'],levels[1]['points'])]
 row['seconds_total']=time.monotonic()-t0;save();print(utc(),tag,'DONE seconds',row['seconds_total'],flush=True)
out.update(status='DONE',finished_utc=utc(),count=len(out['checks']));save();print(utc(),'DONE',out['count'],flush=True)

"""Two independent directed calculations of actual finite radial ODE boxes."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,time,hashlib,argparse,math,platform
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import numpy as np
import flint,mpmath
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
BASE=Path(__file__).resolve().parents[3];D=BASE/'research/radial_tm_instance';OUT=D/'evidence'
SRC=BASE/'research/flow_certificate/evidence/source';sys.path.insert(0,str(SRC))
from cert_flow import FlowCertifier
from midrad import MR
ctx.threads=1
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def qa(q):
 q=F(q);return arb(fmpq(q.numerator,q.denominator))
def qi(q):
 q=F(q);return iv.mpf(q.numerator)/q.denominator
def af(x):
 m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def vf(x):
 s,m,e,_=x;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def bounds(x):
 if isinstance(x,arb):
  assert x.is_finite();return af(x.lower()),af(x.upper())
 assert not (mpmath.isnan(x.a) or mpmath.isnan(x.b));return tuple(vf(t) for t in x._mpi_)
def make(m,r,engine):
 m,r=F(float(m)),F(float(r));assert r>=0
 if engine=='arb':return qa(m-r).union(qa(m+r))
 return iv.mpf([qi(m-r).a,qi(m+r).b])
def magq(m,r):return abs(F(float(m)))+F(float(r))
def tw(j,k,lam):
 if j<=k:return F(0)
 ans=sum((F(math.factorial(k+v),math.factorial(v))*lam**(j-k-1-v)*2**v for v in range(j-k)),F())/math.factorial(j)
 if lam==0:assert ans==F(2**(j-k-1),j*math.factorial(j-k-1))
 return ans

def primary(n,h,em,er,am,ar,bm,br,fm,fr,Q):
 E=make(em,er,'arb');Z=E*E;A=make(am,ar,'arb');B=make(bm,br,'arb');FF=[make(m,r,'arb') for m,r in zip(fm,fr)]
 lp,lm=2*n-2,-2*n-2;P=[];R=[]
 for j in range(Q+1):
  cplus=qa(F(lp**j,2*math.factorial(j)));cminus=qa(F(lm**j,2*math.factorial(j)))
  fp=arb(0);rr=arb(0)
  for k,x in enumerate(FF):
   a,b=tw(j,k,lm),tw(j,k,lp);fp+=x*qa((a-b)/2);rr-=x*qa((a+b)/2)
  P.append((B*cplus+A*cminus)/Z+Z*fp)
  R.append((B*cplus-A*cminus)/Z+Z*rr)
 eh=qa(h);e2=(2*eh).exp();elo=F(float(em))-F(float(er));ehi=F(float(em))+F(float(er));assert elo>0
 C=[magq(m,r) for m,r in zip(fm,fr)];G=[]
 for i in range(Q+1):
  exact=sum((ck*math.comb(i,v)*2**(i-v)*F(math.factorial(k),math.factorial(k-v))*h**(k-v) for k,ck in enumerate(C) for v in range(min(i,k)+1)),F())
  G.append(qa(ehi**2*exact)*e2)
 ds=[]
 for lam,mm,rr in [(lp,bm,br),(lm,am,ar)]:
  yy=(qa(max(lam,0))*eh).exp()*(qa(magq(mm,rr)/elo**2)+eh*G[0])
  dd=abs(lam)**(Q+1)*yy+sum((abs(lam)**(Q-i)*G[i] for i in range(Q+1)),arb(0));ds.append(dd)
 H=(ds[0]+ds[1])*qa(h**(Q+1)/F(2*math.factorial(Q+1)))
 return P,R,H

def secondary(n,h,em,er,am,ar,bm,br,fm,fr,Q):
 E=make(em,er,'iv');Z=E**2;A=make(am,ar,'iv');B=make(bm,br,'iv');FF=[make(m,r,'iv') for m,r in zip(fm,fr)]
 lp,lm=2*n-2,-2*n-2;N=len(FF)
 wp=[iv.mpf(0),iv.mpf(1)]+[iv.mpf(0) for k in FF]
 wm=[iv.mpf(1),iv.mpf(0)]+[iv.mpf(0) for k in FF]
 P=[];R=[]
 for j in range(Q+1):
  for sg,out in [(1,P),(-1,R)]:
   weights=[(x+sg*y)/2 for x,y in zip(wp,wm)]
   out.append((A*weights[0]+B*weights[1])/Z+Z*sum((x*w for x,w in zip(FF,weights[2:])),iv.mpf(0)))
  if j<Q:
   npw=[lp*x/(j+1) for x in wp];nmw=[lm*x/(j+1) for x in wm]
   for k in range(min(j,N-1)+1):
    fk=qi(F(2**(j-k),(j+1)*math.factorial(j-k)))
    npw[k+2]-=fk;nmw[k+2]+=fk
   wp,wm=npw,nmw
 hh=qi(h);elo=F(float(em))-F(float(er));ehi=F(float(em))+F(float(er));assert elo>0
 cp=[qi(magq(m,r)) for m,r in zip(fm,fr)];G=[]
 for i in range(Q+1):
  value=iv.mpf(0)
  for c in reversed(cp):value=value*hh+c
  G.append(qi(ehi)**2*iv.exp(2*hh)*value)
  cp=[2*c+(k+1)*cp[k+1] if k+1<len(cp) else 2*c for k,c in enumerate(cp)]
 ds=[]
 for lam,mm,rr in [(lp,bm,br),(lm,am,ar)]:
  yy=iv.exp(max(lam,0)*hh)*(qi(magq(mm,rr))/qi(elo)**2+hh*G[0]);dd=abs(lam)**(Q+1)*yy
  for i in range(Q+1):dd+=abs(lam)**(Q-i)*G[i]
  ds.append(dd)
 H=(ds[0]+ds[1])*hh**(Q+1)/(2*math.factorial(Q+1))
 return P,R,H

def partition_points(part):
 pts=[]
 for sp in part['spans']:
  a,b=F(sp['a_exact']),F(sp['b_exact']);nn=sp['count'];assert sp['first_cell']==len(pts)
  pts.extend(a+(b-a)*j/nn for j in range(nn))
 pts.append(F(part['spans'][-1]['b_exact']));return pts

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cells',default='0');ap.add_argument('--modes',default='1,20,261');ap.add_argument('--tag',default='smoke');ap.add_argument('--arb-bits',type=int,default=512);ap.add_argument('--iv-dps',type=int,default=180);args=ap.parse_args()
 cells=[int(v) for v in args.cells.split(',')];modes=list(range(1,262)) if args.modes=='all' else [int(v) for v in args.modes.split(',')]
 assert len(set(cells))==len(cells) and all(0<=i<7809 for i in cells) and len(set(modes))==len(modes) and all(1<=n<=261 for n in modes)
 start=time.monotonic();counts=Counter();records=[];failures=[];finite=True
 green=BASE.parent/'ipmA-num/data/cert_green.npz';scalar=BASE/'research/flow_scalars/evidence/scalar_arrays.npz';part=BASE/'research/middle_residual/evidence/partition_exact.json'
 paths=[Path(__file__),D/'PROOF.md',D/'ADDENDUM.md',D/'evidence/proof_first.json',green,scalar,part,BASE/'research/flow_scalars/evidence/checks.json',BASE/'research/flow_certificate/evidence/modal_verdict.json',D/'REFINEMENT.md']+[SRC/n for n in ('cert_flow.py','cert_resid.py','midrad.py')]
 pins={str(p):sha(p) for p in paths}
 assert pins[str(green)]=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
 assert pins[str(SRC/'cert_flow.py')]=='bb47a2d7a46807b02c0e943d7b50d31fb31b6a42c4be55fdbbf1c3a2b90031f6'
 assert pins[str(SRC/'cert_resid.py')]=='15a7535dbe5d7249ea38e089229591591976eef1151f298c932873f9e9dec828'
 assert pins[str(SRC/'midrad.py')]=='5b5feb4ad511e66d57d228a3b754e44cfa2ceb17a33f717dde991c464d5f598e'
 scalar_checks=json.loads(paths[7].read_text());assert sha(scalar)==scalar_checks['array_sha256']
 d=np.load(green);sc=np.load(scalar)['middle'];pts=partition_points(json.loads(part.read_text()))
 # Materialize once; do not decompress the full NPZ for each selected cell.
 Tm,Tr,Am,Ar,Bm,Br,tb,tbr=[d[k] for k in ('T_mid','T_rad','A_mid','A_rad','B_mid','B_rad','tb','tb_rad')]
 C=FlowCertifier.__new__(FlowCertifier);C.M=260;C.Nf=261;C.Q=12;C.n=np.arange(1,262,dtype=float)
 iv.dps=args.iv_dps
 for ci in cells:
  v=sc[ci];h=F(float(v[0]));assert 0<pts[ci+1]-pts[ci]<=h and 522*h<1
  for j in (ci,ci+1):assert F(float(tb[j]))-F(float(tbr[j]))<=pts[j]<=F(float(tb[j]))+F(float(tbr[j]))
  for conv,exp in [(qa,lambda x:x.exp()),(qi,iv.exp)]:
   ctx.prec=args.arb_bits;l,u=bounds(exp(conv(pts[ci])));assert F(float(v[1]))-F(float(v[2]))<=l<=u<=F(float(v[1]))+F(float(v[2]));counts['common_E_point']+=1
  ctx.prec=128;tt=MR(Tm[ci],Tr[ci]);aa=MR(Am[ci],Ar[ci]);bb=MR(Bm[ci],Br[ci]);ee=MR(v[1],v[2])
  P,R,hp=C.psi_tms(float(h),ee,[(0.0,tt)],aa,bb);ft,_=C.f_terms_from_a([(0.0,tt)]);assert len(ft)==1;FF=ft[0][1]
  arrays=dict(P_mid=P.c.m,P_rad=P.c.r,P_rem=P.r,R_mid=R.c.m,R_rad=R.c.r,R_rem=R.r,F_mid=FF.m,F_rad=FF.r,A_mid=aa.m,A_rad=aa.r,B_mid=bb.m,B_rad=bb.r,scalar=v,T_mid=tt.m,T_rad=tt.r)
  for k,x in arrays.items():
   assert np.isfinite(x).all(),k
   if k.endswith(('_rad','_rem')):assert (x>=0).all(),k
  cp=OUT/(args.tag+'_cell_%04d.npz'%ci);np.savez_compressed(cp,**arrays);pins[str(cp)]=sha(cp)
  for n in modes:
   ctx.prec=args.arb_bits
   inputs=(n,h,v[1],v[2],aa.m[n-1],aa.r[n-1],bb.m[n-1],bb.r[n-1],FF.m[n-1],FF.r[n-1],12)
   for name,fn in [('arb'+str(args.arb_bits),primary),('iv'+str(args.iv_dps),secondary)]:
    pp,rr,hh=fn(*inputs);lo,hi=bounds(hh);assert 0<=lo<=hi
    rec={'cell':ci,'n':n,'engine':name,'remainder_lower':str(lo),'remainder_upper':str(hi),'coefficient_failures':[],'remainder_pass':{}}
    for label,vals,candidate in [('P',pp,P),('R',rr,R)]:
     for j,x in enumerate(vals):
      a,b=bounds(x);m=F(float(candidate.c.m[n-1,j]));r=F(float(candidate.c.r[n-1,j]));passed=m-r<=a<=b<=m+r;counts[name+'_coefficient_comparisons']+=1;counts[name+'_coefficient_pass']+=int(passed)
      if not passed:
       fail={'cell':ci,'n':n,'engine':name,'kind':'coefficient','family':label,'j':j,'candidate_mid':str(m),'candidate_rad':str(r),'independent_lo':str(a),'independent_hi':str(b)};failures.append(fail);rec['coefficient_failures'].append([label,j])
     budget=F(float(candidate.r[n-1]));passed=hi<=budget;counts[name+'_remainder_comparisons']+=1;counts[name+'_remainder_pass']+=int(passed);rec['remainder_pass'][label]=passed
     if not passed:failures.append({'cell':ci,'n':n,'engine':name,'kind':'remainder','family':label,'candidate_budget':str(budget),'independent_upper':str(hi),'ratio_display':float(hi/budget) if budget else None})
    records.append(rec)
  print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'cell':ci,'modes':len(modes),'counts':dict(counts),'failures':len(failures),'seconds':time.monotonic()-start}),flush=True)
 for p,v in pins.items():assert sha(p)==v,p
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_LOCAL_RADIAL_ODE_BOXES' if not failures else 'OPEN_SUFFICIENT_CONTAINMENT_TEST_FAILED','cells':cells,'modes':modes,'Q':12,'counts':dict(counts),'failures':failures,'records':records,'files':pins,'runtime':{'python':sys.version,'numpy':np.__version__,'flint':flint.__version__,'mpmath':mpmath.__version__,'platform':platform.platform(),'libc':platform.libc_ver()},'seconds':time.monotonic()-start,'scope':'Local ODE propagation for exactly the exported finite boxes; canonical input membership and full field inequalities are separate OPEN obligations.'}
 (OUT/(args.tag+'_checks.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('utc','status','cells','modes','counts','seconds')}),flush=True)
if __name__=='__main__':main()

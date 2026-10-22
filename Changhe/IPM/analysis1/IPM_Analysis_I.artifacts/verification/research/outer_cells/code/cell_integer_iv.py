"""Independent iv Taylor models and exact integer interval convolution."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json,hashlib,math,time,resource,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint,mpmath
from flint import fmpz_poly
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/outer_cells/evidence';OV='7857fb1b2347ec5ec1e1206db7272c5144d903b0209f23e2a5d46cad9664d1ac';Z=(F(0),F(0));iv.dps=160

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def rf(t):
 sign,m,e,bc=t;assert bc>=0;return (-1 if sign else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 assert not iv.isnan(x) and not iv.isinf(x);a,b=map(rf,x._mpi_);assert a<=b;return a,b
def out(x):a,b=ends(x);return {'lower_exact':str(a),'upper_exact':str(b),'display':str(x)}
def hull(lo,hi):assert lo<=hi;return iv.mpf([iq(lo).a,iq(hi).b])
def top(x):return iq(ends(x)[1])
def padd(a,b):return a[0]+b[0],a[1]+b[1]
def pscale(a,q):return a[0]*q,a[1]*q

def setup(Q=16,Pint=512):
 assert 6<=Q<=32 and Pint>=384;assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
 vp=B/'research/outer_majorant/evidence/verdict.json';assert sha(vp)==OV;v=json.loads(vp.read_bytes());assert v['status']=='CONFIRMED'
 op=B/'research/outer_majorant/evidence/outer_result.json';cp=B/'research/outer_majorant/evidence/exact_outer_coefficients.json'
 assert sha(op)==v['files'][str(op.relative_to(B))] and sha(cp)==v['files'][str(cp.relative_to(B))]
 old=json.loads(op.read_bytes());co=json.loads(cp.read_bytes());beta=list(map(F,co['beta_exact']));k=F(old['scalars_exact']['k']);L=F(old['scalars_exact']['L']);tb=F(co['tb_exact']);assert 0<k<F(1,2) and L>0 and len(beta)==11 and beta[0]==k
 zz=list(map(F,co['correction_parameter_exact_interval']));z=hull(*zz)
 def ev(pair):return iq(pair[0])+iq(pair[1])*z
 def evaluate(c):return [ev(v) for v in c]
 cs=[[[tuple(map(F,x)) for x in c] for c in row['basis']] for row in co['rows']];assert len(cs)==262 and all(v==Z for c in cs[-1] for v in c);assert all(len(row)==11 for row in cs)
 assert all(len(c)==(7 if b==10 else 1) for row in cs for b,c in enumerate(row))
 density=[];dts=[];lins=[]
 for row in cs[:261]:
  density.append([evaluate(c) for c in row]);dtrow=[];erow=[]
  for b,c in enumerate(row):
   deriv=[pscale(c[l+1],l+1) if l+1<len(c) else Z for l in range(len(c))]
   d=[padd(pscale(x,beta[b]),y) for x,y in zip(c,deriv)];el=[padd(pscale(x,beta[b]/k-1),pscale(y,1/k)) for x,y in zip(c,deriv)]
   if b==0:assert el==[Z]
   dtrow.append(evaluate(d));erow.append(evaluate(el))
  dts.append(dtrow);lins.append(erow)
 def inverse(c,lam):
  assert lam!=0;q=[Z]*len(c)
  for l in range(len(c)-1,-1,-1):q[l]=pscale(padd(c[l],pscale(q[l+1],-l-1) if l+1<len(c) else Z),1/lam)
  return q
 ps=[];ss=[];hs=[];exactchecks=0;assert len(old['green'])==261
 for n,green in enumerate(old['green'],1):
  assert green['n']==n;pr=[];sr=[];m=2*n
  for b,beta_b in enumerate(beta):
   cm,cp_=cs[n-1][b],cs[n][b];assert len(cm)==len(cp_)
   f=[]
   for l in range(len(cm)):
    deriv=padd(pscale(cm[l+1],l+1),pscale(cp_[l+1],l+1)) if l+1<len(cm) else Z
    f.append(pscale(padd(padd(pscale(cm[l],beta_b+1-m),pscale(cp_[l],beta_b+1+m)),deriv),F(1,2)))
   qp=inverse(f,beta_b+1+m);qm=[pscale(x,-1) for x in inverse(f,beta_b+1-m)]
   for key,q in [('plus_exact',qp),('minus_exact',qm)]:
    assert q==[tuple(map(F,x)) for x in green[key][b]];exactchecks+=2*len(q)
   pr.append(evaluate([pscale(padd(x,y),F(-1,2)) for x,y in zip(qp,qm)]));sr.append(evaluate([pscale(padd(y,pscale(x,-1)),F(1,2)) for x,y in zip(qp,qm)]))
  ps.append(pr);ss.append(sr);hb=green['H_over_R4'];hs.append(-hull(F(hb['lower_exact']),F(hb['upper_exact']))/2)
 assert exactchecks==17748
 factorials=[math.factorial(i) for i in range(Q+1)]
 mat=[[sum(2**i*(-1)**(l-i)*math.comb(l,i)*math.comb(j,i)*factorials[i]*factorials[Q-i] for i in range(min(j,l)+1)) for l in range(Q+1)] for j in range(Q+1)]
 return {'Q':Q,'Pint':Pint,'k':k,'L':L,'tb':tb,'beta':beta,'density':density,'dt':dts,'linear':lins,'pv':ps,'sv':ss,'hs':hs,'r2':iv.exp(iq(2*tb)),'r3':iv.exp(iq(3*tb)),'matrix':mat,'factorialQ':factorials[Q],'exact_Green_scalar_checks':exactchecks,'old_result_sha256':sha(op),'coefficient_sha256':sha(cp)}

def bound_cell(data,left,right,primary=None):
 start=time.monotonic();a,b=F(left),F(right);assert 0<=a<b;tc=(a+b)/2;h=(b-a)/2;Q=data['Q'];Pint=data['Pint'];base=2*Q+1;cache={};tca,ha=iq(tc),iq(h);hp=[ha**i for i in range(7)];tp=[tca**i for i in range(7)]
 def term(c,lam):
  if all(ends(x)==(0,0) for x in c):return [iv.mpf(0)]*(Q+1),iv.mpf(0)
  if lam not in cache:
   ell=iq(lam*h);eabs=abs(ell);fac=iv.exp(iq(lam*tc));coefs=[iv.mpf(1)]
   for q in range(1,Q+1):coefs.append(coefs[-1]*ell/q)
   tails=[fac*iv.exp(eabs)*eabs**(Q-l+1)/math.factorial(Q-l+1) for l in range(7)];cache[lam]=(coefs,fac,tails)
  coeff,fac,tails=cache[lam];d=len(c)-1
  shifted=[sum((math.comb(j,l)*c[j]*tp[j-l]*hp[l] for j in range(l,d+1)),iv.mpf(0)) for l in range(d+1)]
  p=[iv.mpf(0)]*(Q+1)
  for l,cl in enumerate(shifted):
   for q in range(l,Q+1):p[q]+=cl*coeff[q-l]
  return [fac*x for x in p],top(sum((abs(x)*tails[l] for l,x in enumerate(shifted)),iv.mpf(0)))
 def combine(cs,lams,scale):
  p=[iv.mpf(0)]*(Q+1);r=iv.mpf(0)
  for c,lam in zip(cs,lams):
   q,s=term(c,lam);p=[x+y for x,y in zip(p,q)];r+=s
  return [x*scale for x in p],top(r*abs(scale))
 def scaled(tm,c):return [v*c for v in tm[0]],top(tm[1]*abs(c))
 def added(x,y):return [a+b for a,b in zip(x[0],y[0])],top(x[1]+y[1])
 rho=[combine(cs,data['beta'],data['r3']) for cs in data['density']];D=[combine(cs,data['beta'],data['r3']) for cs in data['dt']];H=[scaled(x,iq(2*j+1)) for j,x in enumerate(rho)];Lin=[combine(cs,data['beta'],data['r3']) for cs in data['linear']]
 rates=[x-1 for x in data['beta']];P=[];S=[]
 for n in range(1,262):
  tr=scaled(term([data['hs'][n-1]],F(-2*n-2)),data['r2']);P.append(added(combine(data['pv'][n-1],rates,data['r2']),tr));S.append(added(combine(data['sv'][n-1],rates,data['r2']),tr))
 model_seconds=time.monotonic()-start
 def quant(x,p):
  lo,hi=ends(x);lo*=2**p;hi*=2**p;il=lo.numerator//lo.denominator;ih=-((-hi.numerator)//hi.denominator);mid=(il+ih)//2;rad=max(mid-il,ih-mid);assert rad>=0;return mid,rad
 def angular(models,kind):
  even=kind in ['velocity_cos','velocity_sin'];size=(523 if even else 522)*base;ms=[0]*size;rs=[0]*size
  for j,(p,r) in enumerate(models):
   positive=261+j+1 if even else 261+j;negative=261-j-1 if even else 260-j
   for l,v in enumerate(p):
    if kind in ['velocity_cos','density_cos']:v=v/2
    mi,ri=quant(v,Pint);ms[positive*base+l]=mi;rs[positive*base+l]=ri;ms[negative*base+l]=-mi if kind in ['velocity_sin','density_sin'] else mi;rs[negative*base+l]=ri
  norm=top(sum((abs(x) for p,r in models for x in p),iv.mpf(0)));rem=top(sum((r for p,r in models),iv.mpf(0)))
  return ms,rs,norm,rem
 pe=angular(P,'velocity_cos');se=angular(S,'velocity_sin');de=angular(D,'density_sin');he=angular(H,'density_cos')
 def convolve(x,y):
  mx,rx=fmpz_poly(x[0]),fmpz_poly(x[1]);my,ry=fmpz_poly(y[0]),fmpz_poly(y[1]);mc=mx*my;rc=fmpz_poly([abs(i) for i in x[0]])*ry+rx*fmpz_poly([abs(i) for i in y[0]])+rx*ry;return mc,rc
 mc1,rc1=convolve(pe,de);mc2,rc2=convolve(se,he);mc,rc=mc1+mc2,rc1+rc2;assert mc.degree()<1044*base and rc.degree()<1044*base
 polynomial_seconds=time.monotonic()-start-model_seconds
 linear_rem=top(sum((r for p,r in Lin),iv.mpf(0)))
 def prodtail(x,y):return x[2]*y[3]+y[2]*x[3]+x[3]*y[3]
 nonpoly=top(prodtail(pe,de)+prodtail(se,he)+linear_rem);den=2**(2*Pint);fact=data['factorialQ'];mat=data['matrix'];sum_Bint=0;high_int=0;overlaps=0
 assert primary is None or (primary['left_exact']==str(a) and primary['right_exact']==str(b) and primary['Q']==Q)
 for q in range(522):
  centers=[int(mc[(522+q)*base+l]) for l in range(2*Q+1)];radii=[int(rc[(522+q)*base+l]) for l in range(2*Q+1)]
  if q<261:
   for l,x in enumerate(Lin[q][0]):m,r=quant(x,2*Pint);centers[l]+=m;radii[l]+=r
  assert all(r>=0 for r in radii)
  if primary is not None and 'coefficients' in primary:
   for l,(m,r) in enumerate(zip(centers,radii)):
    old=primary['coefficients'][q][l];lo,hi=F(old['lower_exact']),F(old['upper_exact']);assert lo<=hi and max(lo,F(m-r,den))<=min(hi,F(m+r,den)),('disjoint',q,l);overlaps+=1
  high_int+=sum(abs(centers[l])+radii[l] for l in range(Q+1,2*Q+1))
  maximum=0
  for row in mat:
   center=sum(x*y for x,y in zip(centers,row));radius=sum(x*abs(y) for x,y in zip(radii,row));maximum=max(maximum,abs(center)+radius)
  sum_Bint+=maximum
 polynorm=F(sum_Bint,den*fact);discarded=F(high_int,den);W=top(iq(polynorm+discarded)+nonpoly)
 k,L,tb=data['k'],data['L'],data['tb'];ul=iv.exp(iq(tb+a))/iq(L);ur=iv.exp(iq(tb+b))/iq(L);ml=iv.exp(3*iv.log(ul)+iq((k-3)/2)*iv.log(1+ul*ul));assert ends(ml)[0]>0;Wm=top(W/ml)
 weights={str(delta):out(top(Wm*iv.exp(iq(delta)*iv.log(1+ur)))) for delta in [F(0),F(1,2),F(1,2)-k]}
 l2sq=top(iv.pi*Wm*Wm*iq(L*L/2)*(iv.log(1+ur*ur)-iv.log(1+ul*ul)))
 return {'left_exact':str(a),'right_exact':str(b),'tc_exact':str(tc),'h_exact':str(h),'Q':Q,'Pint':Pint,'max_abs_lambda_h_exact':str(h*max(abs(x) for x in data['beta']+rates+[F(-2*n-2) for n in range(1,262)])),'W':out(W),'W_over_m':out(Wm),'weighted':weights,'L2_squared':out(l2sq),'retained_Bernstein_sum_exact':str(polynorm),'discarded_polynomial_remainder_exact':str(discarded),'retained_Bernstein_sum':out(iq(polynorm)),'discarded_polynomial_remainder':out(iq(discarded)),'nonpolynomial_remainder':out(nonpoly),'coefficient_overlap_checks':overlaps,'exact_integer_convolutions':8,'model_seconds':model_seconds,'convolution_seconds':polynomial_seconds,'seconds':time.monotonic()-start}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);args=ap.parse_args();assert args.tag.replace('_','').isalnum();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));st=time.monotonic();rp=E/(args.tag+'_arb.json');primary=json.loads(rp.read_bytes());assert primary['status']=='COMPUTED_REQUIRES_INDEPENDENT_AUDIT';assert primary['source_sha256']==sha(B/'research/outer_cells/code/cell_arb.py') and primary['proof_sha256']==sha(B/'research/outer_cells/PROOF.md');data=setup(primary['cell']['Q']);assert primary['old_result_sha256']==data['old_result_sha256'] and primary['coefficient_sha256']==data['coefficient_sha256'];row=primary['cell'];r=bound_cell(data,row['left_exact'],row['right_exact'],row)
 d={'utc':utc(),'status':'PASS_SELECTED_CELL' if r['coefficient_overlap_checks']==522*(2*r['Q']+1) else 'COMPUTED_WITHOUT_COEFFICIENT_COMPARISON','source_sha256':sha(__file__),'proof_sha256':primary['proof_sha256'],'primary_source_sha256':primary['source_sha256'],'primary_result_sha256':sha(rp),'outer_verdict_sha256':OV,'old_result_sha256':data['old_result_sha256'],'coefficient_sha256':data['coefficient_sha256'],'exact_Green_scalar_checks':data['exact_Green_scalar_checks'],'iv_dps':iv.dps,'cell':r,'total_seconds':time.monotonic()-st};(E/(args.tag+'_iv.json')).write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(r),flush=True)

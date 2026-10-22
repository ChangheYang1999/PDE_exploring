"""Inner independent density-moment ODEs and integer interval convolution."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,math,time,resource,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import fmpz_poly
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/inner_cells/evidence';iv.dps=160
sys.path.insert(0,str(B/'research/inner_majorant/code'));import audit_inner_iv as integrals
IV='69923605fab0dad07205705e32b52f26770053cf7392cfd919d1fb2ff415a0fc'
assert sys.flags.optimize==0

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def rf(t):s,m,e,bc=t;assert bc>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 assert not iv.isnan(x) and not iv.isinf(x);a,b=map(rf,x._mpi_);assert a<=b;return a,b
def out(x):a,b=ends(x);return {'lower_exact':str(a),'upper_exact':str(b),'display':str(x)}
def hull(a,b):assert a<=b;return iv.mpf([iq(a).a,iq(b).b])
def top(x):return iq(ends(x)[1])
def inverse_explicit(p,lam):
 assert lam>0
 return [sum(((-1)**(j-l)*F(math.factorial(j),math.factorial(l))*p[j]/lam**(j-l+1) for j in range(l,len(p))),F(0)) for l in range(len(p))]

def setup(Q=16,Pint=512):
 assert 7<=Q<=32 and Pint>=384;vp=B/'research/inner_majorant/evidence/verdict.json';assert sha(vp)==IV;v=json.loads(vp.read_text());assert v['status']=='CONFIRMED'
 for p,h in v['files'].items():assert sha(B/p)==h
 co=json.loads((B/'research/inner_majorant/evidence/exact_inner_coefficients.json').read_text());old=json.loads((B/'research/inner_majorant/evidence/inner_result.json').read_text());ta=F(co['ta_exact']);bi=F(co['bi_exact']);k=F(old['k_exact']);L=F(old['L_exact']);assert bi>=49 and k==F(1615536043799051,9007199254740992) and L>0
 alpha=[F(0)]+[F(2*i+2) for i in range(7)]+[bi];cs=[]
 for j,row in enumerate(co['rows']):
  assert row['j']==j and F(row['C'])==(F(1,4) if j<2 else 0);cs.append([[F(row['C'])]]+[[F(c)] for c in row['D']]+[list(map(F,row['Ei']))])
 assert len(cs)==262 and all(x==0 for p in cs[-1] for x in p)
 # Independently formed direct inner Bhat1 primitive, with denominators >=2.
 b1=[]
 for al,cm,cp in zip(alpha,cs[0],cs[1]):
  f=[]
  for l in range(len(cm)):
   deriv=(l+1)*(cm[l+1]+cp[l+1]) if l+1<len(cm) else 0
   f.append(((al+2)*cm[l]+(al+6)*cp[l]+deriv)/2)
  b1.append([-q for q in inverse_explicit(f,al+2)])
 case=next(c for c in old['cases'] if c['T_exact']=='0');J0=[None]
 for n,row in enumerate(case['upper_Green'],2):
  assert row['n']==n;w=row['j_boundary'];J0.append(hull(F(w['lower_exact']),F(w['upper_exact'])))
 assert len(J0)==261
 factorials=[math.factorial(i) for i in range(Q+1)];matrix=[[sum(2**i*(-1)**(l-i)*math.comb(l,i)*math.comb(j,i)*factorials[i]*factorials[Q-i] for i in range(min(j,l)+1)) for l in range(Q+1)] for j in range(Q+1)]
 return {'Q':Q,'Pint':Pint,'k':k,'L':L,'ta':ta,'alpha':alpha,'cs':cs,'b1':b1,'J0':J0,'R2':iv.exp(iq(2*ta)),'R3':iv.exp(iq(3*ta)),'matrix':matrix,'factorialQ':factorials[Q]}

def bound_cell(data,left,right,primary=None):
 start=time.monotonic();a,b=F(left),F(right);assert a<b<=0;tc=(a+b)/2;h=(b-a)/2;Q=data['Q'];Pint=data['Pint'];base=2*Q+1;alpha=data['alpha'];cache={};zero=([iv.mpf(0)]*(Q+1),iv.mpf(0));ha=iq(h)
 def term(p,lam):
  if not any(p):return zero
  if lam not in cache:
   ell=iq(lam*h);fac=iv.exp(iq(lam*tc));power=[iv.mpf(1)]
   for q in range(1,Q+1):power.append(power[-1]*ell/q)
   tails=[fac*iv.exp(abs(ell))*abs(ell)**(Q-l+1)/math.factorial(Q-l+1) for l in range(7)];cache[lam]=(power,fac,tails)
  power,fac,tails=cache[lam];shifted=[iq(h**l*sum((p[j]*math.comb(j,l)*tc**(j-l) for j in range(l,len(p))),F(0))) for l in range(len(p))];poly=[iv.mpf(0)]*(Q+1)
  for l,x in enumerate(shifted):
   for q in range(l,Q+1):poly[q]+=x*power[q-l]
  return [fac*x for x in poly],top(sum((abs(x)*tails[l] for l,x in enumerate(shifted)),iv.mpf(0)))
 def added(x,y):return [a+b for a,b in zip(x[0],y[0])],top(x[1]+y[1])
 def scaled(x,c):return [c*y for y in x[0]],top(abs(c)*x[1])
 def norm(p):return top(sum((abs(x) for x in p),iv.mpf(0)))
 def multiply(x,y):
  p=[iv.mpf(0)]*(2*Q+1)
  for i,xi in enumerate(x[0]):
   for j,yj in enumerate(y[0]):p[i+j]+=xi*yj
  rem=sum((abs(v) for v in p[Q+1:]),iv.mpf(0))+norm(x[0])*y[1]+norm(y[0])*x[1]+x[1]*y[1];return p[:Q+1],top(rem)
 def combine(ps,off,scale):
  r=zero
  for p,al in zip(ps,alpha):r=added(r,term(p,al+off))
  return scaled(r,scale)
 def derivative(ps):return [[(al+3)*p[l]+((l+1)*p[l+1] if l+1<len(p) else 0) for l in range(len(p))] for al,p in zip(alpha,ps)]
 def ode(y0,lam,sig,G):
  ell=iq(lam*h);powers=[iv.mpf(1)]
  for q in range(1,Q+1):powers.append(powers[-1]*ell)
  p=[]
  for q in range(Q+1):
   value=y0*powers[q]/math.factorial(q)
   for l in range(q):value+=sig*ha*G[0][l]*math.factorial(l)*powers[q-1-l]/math.factorial(q)
   p.append(value)
  remainder=iv.exp(abs(ell))*(abs(ell*p[Q]+sig*ha*G[0][Q])/(Q+1)+ha*G[1]);return p,top(remainder)
 Hhat=[combine(ps,0,iv.mpf(1)) for ps in data['cs']];rho=[];D=[];H=[];Eta=[];ED=[]
 for j,ps in enumerate(data['cs'][:261]):
  rho.append(combine(ps,3,data['R3']));D.append(combine(derivative(ps),3,data['R3']));H.append(scaled(rho[-1],iq(2*j+1)));es=[[F(0)]]+ps[1:];Eta.append(combine(es,3,data['R3']));ED.append(combine(derivative(es),3,data['R3']))
 Lin=[zero for _ in range(262)];c=iq(3/data['k']-1)
 def sine_add(nu,model,scalar):
  assert nu!=0;dest=(abs(nu)-1)//2;Lin[dest]=added(Lin[dest],scaled(model,scalar if nu>0 else -scalar))
 for j,(eta,dt) in enumerate(zip(Eta,ED)):
  nu=2*j+1;sine_add(nu,dt,1/iq(data['k']));sine_add(nu,eta,iq(-1))
  for freq in [nu+2,nu-2]:sine_add(freq,dt,-c/2)
  for freq in [nu+2,2-nu]:sine_add(freq,eta,c*nu/2)
 er2=scaled(term([F(1)],F(2)),data['R2']);P=[];S=[]
 for n in range(1,262):
  m=2*n;i0=iv.mpf(0)
  for al,p in zip(alpha,data['cs'][n-1]):
   if any(p):
    q=inverse_explicit(p,m+4+al);val=sum((x*tc**l for l,x in enumerate(q)),F(0));i0+=iv.exp(iq(al*tc))*iq(val)
  it=ode(i0,-m-4,1,Hhat[n-1]);avg=scaled(added(Hhat[n-1],Hhat[n]),iq(F(1,2)));Adiv=multiply(er2,added(avg,scaled(it,iq(-m))))
  if n==1:Bdiv=combine(data['b1'],2,data['R2'])
  else:
   j0=iv.exp(iq((m-4)*tc))*data['J0'][n-1]
   for al,p in zip(alpha,data['cs'][n]):
    if any(p):j0+=iv.exp(iq(al*tc))*integrals.integrate(p,tc,-tc,4-m+al)
   jt=ode(j0,m-4,-1,Hhat[n]);Bdiv=multiply(er2,added(scaled(jt,iq(m)),scaled(avg,iq(-1))))
  P.append(scaled(added(Adiv,Bdiv),iq(F(-1,2))));S.append(scaled(added(Bdiv,scaled(Adiv,iq(-1))),iq(F(1,2))))
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
  if q<262:
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
 k,L,tb=data['k'],data['L'],data['ta'];ul=iv.exp(iq(tb+a))/iq(L);ur=iv.exp(iq(tb+b))/iq(L);ml=iv.exp(3*iv.log(ul)+iq((k-3)/2)*iv.log(1+ul*ul));assert ends(ml)[0]>0;Wm=top(W/ml)
 weights={str(delta):out(top(Wm*iv.exp(iq(delta)*iv.log(1+ur)))) for delta in [F(0),F(1,2),F(1,2)-k]}
 l2sq=top(iv.pi*Wm*Wm*iq(L*L/2)*(iv.log(1+ur*ur)-iv.log(1+ul*ul)))
 return {'left_exact':str(a),'right_exact':str(b),'tc_exact':str(tc),'h_exact':str(h),'Q':Q,'Pint':Pint,'max_abs_ODE_lambda_h_exact':str(526*h),'W':out(W),'W_over_m':out(Wm),'weighted':weights,'L2_squared':out(l2sq),'retained_Bernstein_sum_exact':str(polynorm),'discarded_polynomial_remainder_exact':str(discarded),'retained_Bernstein_sum':out(iq(polynorm)),'discarded_polynomial_remainder':out(iq(discarded)),'nonpolynomial_remainder':out(nonpoly),'coefficient_overlap_checks':overlaps,'exact_integer_convolutions':8,'model_seconds':model_seconds,'convolution_seconds':polynomial_seconds,'seconds':time.monotonic()-start}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);args=ap.parse_args();assert args.tag.replace('_','').isalnum();rp=E/(args.tag+'_arb.json');pr=json.loads(rp.read_text());assert pr['status']=='COMPUTED_REQUIRES_INDEPENDENT_AUDIT' and pr['inner_verdict_sha256']==IV
 assert pr['source_sha256']==sha(B/'research/inner_cells/code/cell_arb.py') and pr['proof_sha256']==sha(B/'research/inner_cells/PROOF.md');data=setup(pr['cell']['Q']);row=pr['cell'];r=bound_cell(data,row['left_exact'],row['right_exact'],row)
 d={'utc':utc(),'status':'PASS_SELECTED_CELL' if r['coefficient_overlap_checks']==522*(2*r['Q']+1) else 'COMPUTED_WITHOUT_COEFFICIENT_COMPARISON','source_sha256':sha(__file__),'proof_sha256':pr['proof_sha256'],'primary_source_sha256':pr['source_sha256'],'primary_result_sha256':sha(rp),'inner_verdict_sha256':IV,'iv_dps':iv.dps,'cell':r};(E/(args.tag+'_iv.json')).write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(r),flush=True)

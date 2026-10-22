"""Independent middle cells: density ODEs, iv antiderivatives, integer convolution.
The shared canonical archive is an explicit audited dependency. No primary
physical Green ODE or primary radial polynomial products are used here.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,math,time,hashlib
from pathlib import Path
from fractions import Fraction as F
import flint, mpmath
from flint import fmpz_poly
from mpmath import iv
BASE=Path(__file__).resolve().parents[3]
iv.dps=160
assert flint.__version__=="0.9.0" and mpmath.__version__=="1.3.0"
if sys.flags.optimize:raise RuntimeError('Assertions must be active')
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def rf(t):
 s,m,e,bc=t;assert bc>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 assert not iv.isnan(x) and not iv.isinf(x)
 a,b=map(rf,x._mpi_);assert a<=b;return a,b
def hull(a,b):assert a<=b;return iv.mpf([iq(a).a,iq(b).b])
def top(x):return iq(ends(x)[1])
def out(x):a,b=ends(x);return {'lower_exact':str(a),'upper_exact':str(b),'display':str(x)}
def ball_ends(v):
 assert set(v)=={'schema','mid_m','mid_e','rad_m','rad_e'} and v['schema']=='arb-dyadic-mid-radius-v1'
 m,e,r,f=[int(v[k]) for k in ('mid_m','mid_e','rad_m','rad_e')];assert r>=0
 mid=F(m)*F(2)**e;rad=F(r)*F(2)**f;return mid-rad,mid+rad

def setup(k,L,Q=16,Pint=512):
 assert Q==16 and Pint>=384 and 0<k<F(1,2) and L>0
 fact=[math.factorial(i) for i in range(Q+1)]
 matrix=[[sum(2**i*(-1)**(l-i)*math.comb(l,i)*math.comb(j,i)*fact[i]*fact[Q-i] for i in range(min(j,l)+1)) for l in range(Q+1)] for j in range(Q+1)]
 return {'k':k,'L':L,'Q':Q,'Pint':Pint,'factorials':fact,'factorialQ':fact[Q],'matrix':matrix}

def decode_span(item):
 assert item['type']=='span'
 a,b=F(item['a_exact']),F(item['b_exact']);center=F(item['polynomial_mid_exact'])
 assert a<b and center==(a+b)/2
 polys=[[hull(*ball_ends(v)) for v in p] for p in item['density_polynomials']]
 I=[hull(*ball_ends(v)) for v in item['i_left']];J=[hull(*ball_ends(v)) for v in item['j_right']]
 assert len(polys)==262 and all(len(p)==8 for p in polys) and all(ends(v)==(0,0) for v in polys[-1]) and len(I)==len(J)==261
 return {'a':a,'b':b,'center':center,'polys':polys,'I':I,'J':J}

def shift(p,delta):
 return [sum((p[j]*iq(math.comb(j,l)*delta**(j-l)) for j in range(l,len(p))),iv.mpf(0)) for l in range(len(p))]

def integrate_exp_poly(p,H,lam):
 """Complete antiderivative with exact rational coefficients, including lam=0."""
 H,lam=F(H),F(lam);assert H>=0
 if not H:return iv.mpf(0)
 if not lam:return sum((v*iq(H**(j+1)/F(j+1)) for j,v in enumerate(p)),iv.mpf(0))
 q=[sum((p[j]*iq((-1)**(j-l)*F(math.factorial(j),math.factorial(l))/lam**(j-l+1)) for j in range(l,len(p))),iv.mpf(0)) for l in range(len(p))]
 qH=sum((v*iq(H**j) for j,v in enumerate(q)),iv.mpf(0))
 return iv.exp(iq(lam*H))*qH-q[0]

def center_values(span,tc):
 assert span['a']<=tc<=span['b']
 jets=[shift(p,tc-span['center']) for p in span['polys']]
 hl,hr=tc-span['a'],span['b']-tc;I=[];J=[]
 for n in range(1,262):
  lam=F(-2*n-4)
  p=[(-1)**j*v for j,v in enumerate(jets[n-1])]
  I.append(iv.exp(iq(lam*hl))*span['I'][n-1]+integrate_exp_poly(p,hl,lam))
  lam=F(4-2*n)
  J.append(iv.exp(iq(lam*hr))*span['J'][n-1]+integrate_exp_poly(jets[n],hr,lam))
 return jets,I,J

def closed_ode(y0,lam,sig,g,h,Q):
 # Complete density-ODE formula; the forcing polynomial has no remainder.
 assert h>0 and Q>=len(g)-1 and abs(sig)<=1
 ha=iq(h);ell=iq(lam*h);fact=[math.factorial(i) for i in range(Q+1)]
 powers=[iv.mpf(1)]
 for j in range(1,Q+1):powers.append(powers[-1]*ell)
 p=[]
 for q in range(Q+1):
  v=y0*powers[q]
  if q:v+=sig*ha*sum((g[j]*fact[j]*powers[q-1-j] for j in range(min(q,len(g)))),iv.mpf(0))
  p.append(v/fact[q])
 gQ=g[Q] if Q<len(g) else iv.mpf(0)
 rem=top(iv.exp(abs(ell))*abs(ell*p[Q]+sig*ha*gQ)/(Q+1))
 return p,rem

def model_ops(tc,h,Q):
 exp_cache={}
 def exp_poly(c,lam):
  # c contains the complete polynomial in v=(t-tc)/h, degree<=7.
  if lam not in exp_cache:
   ell=iq(lam*h);fac=iv.exp(iq(lam*tc));powers=[iv.mpf(1)]
   for q in range(1,Q+1):powers.append(powers[-1]*ell/q)
   tail=[fac*iv.exp(abs(ell))*abs(ell)**(Q-l+1)/math.factorial(Q-l+1) for l in range(8)]
   exp_cache[lam]=fac,powers,tail
  fac,powers,tail=exp_cache[lam];d=len(c)-1;assert d<=7
  p=[fac*sum((c[l]*powers[q-l] for l in range(min(d,q)+1)),iv.mpf(0)) for q in range(Q+1)]
  return p,top(sum((abs(v)*tail[l] for l,v in enumerate(c)),iv.mpf(0)))
 def add(x,y):return [a+b for a,b in zip(x[0],y[0])],top(x[1]+y[1])
 def scale(x,c):return [c*v for v in x[0]],top(abs(c)*x[1])
 def norm(p):return top(sum((abs(v) for v in p),iv.mpf(0)))
 def multiply(x,y):
  p=[iv.mpf(0)]*(2*Q+1)
  for i,xi in enumerate(x[0]):
   for j,yj in enumerate(y[0]):p[i+j]+=xi*yj
  r=sum((abs(v) for v in p[Q+1:]),iv.mpf(0))+norm(x[0])*y[1]+norm(y[0])*x[1]+x[1]*y[1]
  return p[:Q+1],top(r)
 return {"exp_poly":exp_poly,"add":add,"scale":scale,"norm":norm,"multiply":multiply}

def quant(x,p):
 lo,hi=ends(x);lo*=2**p;hi*=2**p;il=lo.numerator//lo.denominator;ih=-((-hi.numerator)//hi.denominator)
 mid=(il+ih)//2;rad=max(mid-il,ih-mid);assert rad>=0;return mid,rad
def angular(models,kind,Q,Pint):
 base=2*Q+1
 even=kind in ('velocity_cos','velocity_sin');size=(523 if even else 522)*base;ms=[0]*size;rs=[0]*size
 for j,(p,r) in enumerate(models):
  positive=262+j if even else 261+j;negative=260-j
  for l,v in enumerate(p):
   if kind in ('velocity_cos','density_cos'):v=v/2
   mi,ri=quant(v,Pint);ms[positive*base+l]=mi;rs[positive*base+l]=ri
   ms[negative*base+l]=-mi if kind in ('velocity_sin','density_sin') else mi;rs[negative*base+l]=ri
 return ms,rs,top(sum((abs(x) for p,r in models for x in p),iv.mpf(0))),top(sum((r for p,r in models),iv.mpf(0)))

def convolve(x,y):
 mx,rx=fmpz_poly(x[0]),fmpz_poly(x[1]);my,ry=fmpz_poly(y[0]),fmpz_poly(y[1])
 return mx*my,fmpz_poly([abs(i) for i in x[0]])*ry+rx*fmpz_poly([abs(i) for i in y[0]])+rx*ry

def bernstein_max(centers,radii,matrix):
 maximum=0
 for row in matrix:
  center=sum(x*y for x,y in zip(centers,row));radius=sum(x*abs(y) for x,y in zip(radii,row))
  maximum=max(maximum,abs(center)+radius)
 return maximum

def bound_cell(data,span,left,right,primary=None,primary_point=None,point_coefficients=None):
 start=time.monotonic();a,b=F(left),F(right);assert span['a']<=a<b<=span['b']
 tc=(a+b)/2;h=(b-a)/2;ha=iq(h);Q=data['Q'];Pint=data['Pint'];base=2*Q+1;fact=data['factorials']
 jets,I,J=center_values(span,tc);center_checks=0;jet_checks=0
 if primary_point is not None:
  assert F(primary_point['t_exact'])==tc and list(map(F,primary_point['cell_endpoints_exact']))==[a,b]
  for values,key in [(I,'i'),(J,'j')]:
   assert len(primary_point[key])==len(values)
   for x,old in zip(values,primary_point[key]):
    lo,hi=ball_ends(old);u,v=ends(x);assert max(lo,u)<=min(hi,v),('moment',key);center_checks+=1
  assert len(primary_point['density_polynomial_at_point'])==262
  for p,q in zip(jets,primary_point['density_polynomial_at_point']):
   assert len(q)==8
   for x,y in zip(p,q):
    lo,hi=ball_ends(y);u,v=ends(x);assert max(lo,u)<=min(hi,v),'density shift';jet_checks+=1
 H=[[v*iq(h**l) for l,v in enumerate(p)] for p in jets]
 Hp=[[(l+1)*p[l+1]*iq(h**l) for l in range(7)]+[iv.mpf(0)] for p in jets]
 zero=([iv.mpf(0)]*(Q+1),iv.mpf(0));exp_cache={}
 ops=model_ops(tc,h,Q)
 exp_poly,add,scale,norm,multiply=[ops[k] for k in ("exp_poly","add","scale","norm","multiply")]
 def ode(y0,lam,sig,g):return closed_ode(y0,lam,sig,g,h,Q)

 ex2=exp_poly([iv.mpf(1)],F(2));P=[];S=[];maxmomentrem=iv.mpf(0)
 for n in range(1,262):
  m=2*n;itm=ode(I[n-1],F(-m-4),1,H[n-1]);jtm=ode(J[n-1],F(m-4),-1,H[n])
  hm=([x+y for x,y in zip(H[n-1],H[n])]+[iv.mpf(0)]*(Q-7),iv.mpf(0))
  P.append(scale(multiply(ex2,add(jtm,scale(itm,iv.mpf(-1)))),iq(F(-m,2))))
  S.append(scale(multiply(ex2,add(scale(add(jtm,itm),iv.mpf(m)),scale(hm,iv.mpf(-1)))),iq(F(1,2))))
  maxmomentrem=iq(max(ends(maxmomentrem)[1],ends(itm[1])[1],ends(jtm[1])[1]))
 rho=[exp_poly(p,F(3)) for p in H[:261]]
 D=[exp_poly([3*x+y for x,y in zip(p,q)],F(3)) for p,q in zip(H[:261],Hp[:261])]
 Theta=[scale(x,iv.mpf(2*j+1)) for j,x in enumerate(rho)]
 k=data['k'];Lin=[exp_poly([x*iq(3/k-1)+y*iq(1/k) for x,y in zip(p,q)],F(3)) for p,q in zip(H[:261],Hp[:261])]
 model_seconds=time.monotonic()-start
 pe=angular(P,'velocity_cos',Q,Pint);se=angular(S,'velocity_sin',Q,Pint);de=angular(D,'density_sin',Q,Pint);he=angular(Theta,'density_cos',Q,Pint)
 mc1,rc1=convolve(pe,de);mc2,rc2=convolve(se,he);mc,rc=mc1+mc2,rc1+rc2
 assert mc.degree()<1044*base and rc.degree()<1044*base
 conv_seconds=time.monotonic()-start-model_seconds
 def prodtail(x,y):return x[2]*y[3]+y[2]*x[3]+x[3]*y[3]
 nonpoly=top(prodtail(pe,de)+prodtail(se,he)+sum((r for p,r in Lin),iv.mpf(0)))
 den=2**(2*Pint);sumB=0;high=0;overlaps=0;point_overlaps=0
 if point_coefficients is not None:assert len(point_coefficients)==522
 if primary is not None:assert F(primary['left_exact'])==a and F(primary['right_exact'])==b and primary['degree']==Q and len(primary['residual_coefficients_z'])==522
 for q in range(522):
  centers=[int(mc[(522+q)*base+l]) for l in range(2*Q+1)]
  radii=[int(rc[(522+q)*base+l]) for l in range(2*Q+1)]
  if q<261:
   for l,x in enumerate(Lin[q][0]):m,r=quant(x,2*Pint);centers[l]+=m;radii[l]+=r
  assert all(r>=0 for r in radii)
  if primary is not None:
   oldrow=primary['residual_coefficients_z'][q];assert len(oldrow)==Q+1
   for l,old in enumerate(oldrow):
    lo,hi=ball_ends(old);mi,ri=centers[l],radii[l]
    assert max(lo,F(mi-ri,den))<=min(hi,F(mi+ri,den)),('coefficient',q,l);overlaps+=1
  if point_coefficients is not None:
   lo,hi=ball_ends(point_coefficients[q]);assert max(lo,F(centers[0]-radii[0],den))<=min(hi,F(centers[0]+radii[0],den)),('independent point',q);point_overlaps+=1
  high+=sum(abs(centers[l])+radii[l] for l in range(Q+1,2*Q+1))
  sumB+=bernstein_max(centers,radii,data['matrix'])

 retained=F(sumB,den*data['factorialQ']);discarded=F(high,den);W=top(iq(retained+discarded)+nonpoly)
 L=data['L'];ul=iv.exp(iq(a))/iq(L);ur=iv.exp(iq(b))/iq(L)
 ml=iv.exp(3*iv.log(ul)+iq((k-3)/2)*iv.log(1+ul*ul));assert ends(ml)[0]>0
 Wm=top(W/ml);weights={str(delta):out(top(Wm*iv.exp(iq(delta)*iv.log(1+ur)))) for delta in [F(0),F(1,2),F(1,2)-k]}
 l2sq=top(iv.pi*Wm*Wm*iq(L*L/2)*(iv.log(1+ur*ur)-iv.log(1+ul*ul)))
 return {'left_exact':str(a),'right_exact':str(b),'tc_exact':str(tc),'h_exact':str(h),'Q':Q,'Pint':Pint,
 'iv_dps':iv.dps,'mpmath_version':mpmath.__version__,'python_flint_version':flint.__version__,'max_center_moment_interval_width_exact':str(max(ends(v)[1]-ends(v)[0] for v in I+J)),'W':out(W),'W_over_m':out(Wm),'weighted':weights,'L2_squared':out(l2sq),'m_left':out(ml),
 'retained_Bernstein_sum_exact':str(retained),'discarded_polynomial_remainder_exact':str(discarded),
 'nonpolynomial_remainder':out(nonpoly),'diagnostic_max_density_moment_remainder':out(maxmomentrem),
 'max_abs_ODE_lambda_h_exact':str(526*h),'coefficient_overlap_checks':overlaps,'center_moment_overlap_checks':center_checks,
 'shifted_density_overlap_checks':jet_checks,'exact_integer_convolutions':8,'independent_point_iv_coefficient_overlaps':point_overlaps,'model_seconds':model_seconds,
 'convolution_seconds':conv_seconds,'seconds':time.monotonic()-start}

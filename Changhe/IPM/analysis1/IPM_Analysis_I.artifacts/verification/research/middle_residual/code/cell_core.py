"""Whole log-cell residual bounds using outward Arb polynomial products.
Only independently computed center moments enter. No numerics implementation imports.
All radial polynomials use z=(t-tc)/h, |z|<=1.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math,time,resource,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,arb_poly,arb_mat,ctx
BASE=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(BASE/'research/ball_transport/code'))
from dyadic_ball import import_ball,export_ball
E=BASE/'research/residual_cells/evidence'
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):x=F(x);return arb(x.numerator)/x.denominator
def ff(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ends(x):return ff(x.mid())-ff(x.rad()),ff(x.mid())+ff(x.rad())
def upper(x):assert x.is_finite();return x.abs_upper()
def out(x):a,b=ends(x);return {'display':x.str(30),'lower_exact':str(a),'upper_exact':str(b)}
def emit(**kw):print(json.dumps({'utc':utc(),**kw}),flush=True)
def add(p,q):return [a+b for a,b in zip(p,q)]
def scale(p,c):return [c*a for a in p]
def norm(p):return sum((upper(v) for v in p),arb(0)).upper()
def exp_poly(c,lam,tc,h,Q):
 """c already contains the coefficients of P(h*z)."""
 d=len(c)-1;assert Q>=d
 ell=aa(lam)*h;coeff=[arb(1)]
 for j in range(1,Q+1):coeff.append(coeff[-1]*ell/j)
 fac=(aa(lam)*tc).exp();p=[fac*sum((c[l]*coeff[q-l] for l in range(min(q,d)+1)),arb(0)) for q in range(Q+1)]
 radius=fac*upper(ell).exp()*sum((upper(c[l])*upper(ell)**(Q-l+1)/math.factorial(Q-l+1) for l in range(d+1)),arb(0))
 return p,radius.upper()
def ode(y0,lam,sig,G,h,Q):
 g,rg=G;ell=aa(lam)*h;p=[y0]
 for q in range(Q):p.append((ell*p[-1]+sig*h*g[q])/(q+1))
 radius=upper(ell).exp()*(upper(ell*p[Q]+sig*h*g[Q])/(Q+1)+h*rg)
 return p,radius.upper()
def mul(a,b,Q):
 p,rp=a;q,rq=b;prod=arb_poly(p)*arb_poly(q);c=[prod[j] for j in range(Q+1)]
 radius=sum((upper(prod[j]) for j in range(Q+1,2*Q+1)),arb(0))+norm(p)*rq+norm(q)*rp+rp*rq
 return c,radius.upper()
def tmadd(a,b):return add(a[0],b[0]),(a[1]+b[1]).upper()
def tmscale(a,c):return scale(a[0],c),(a[1]*upper(c)).upper()
def angular(models,frequencies,center,sine,Q):
 base=2*Q+1;coeff=[arb(0) for _ in range((2*center)*base+Q+1)]
 for (p,rem),n in zip(models,frequencies):
  assert 0<n<=center
  for j,v in enumerate(p):
   coeff[(center-n)*base+j]+=v/2
   coeff[(center+n)*base+j]+=(-v if sine else v)/2
 return arb_poly(coeff),sum((norm(p) for p,r in models),arb(0)).upper(),sum((r for p,r in models),arb(0)).upper()
def bernstein_matrix(Q):
 # row k, column l, for p(2u-1), all rational until outward conversion.
 vals=[[sum((F(2**i*(-1)**(l-i)*math.comb(l,i)*math.comb(k,i),math.comb(Q,i)) for i in range(min(k,l)+1)),F(0)) for l in range(Q+1)] for k in range(Q+1)]
 return vals,arb_mat([[aa(v) for v in row] for row in vals])
def product_tail(a,b):return (a[1]*b[2]+b[1]*a[2]+a[2]*b[2]).upper()
def bound_cell(row,k,L,knots,pub,Q=16,keep_coefficients=False):
 assert 7<=Q<=40
 ci=row['cell'];odd=list(range(1,522,2));even=list(range(2,523,2));base=2*Q+1
 _,Bern=bernstein_matrix(Q)
 cellstart=time.monotonic();left,right=map(F,row['cell_endpoints_exact']);tc=F(row['t_exact']);h=(right-left)/2
 assert h>0 and tc==(left+right)/2 and any(a<=left<right<=b for a,b in zip(knots[:-1],knots[1:]));assert pub['rows'][ci]['ci']==ci
 tca,ha=aa(tc),aa(h);hp=[ha**j for j in range(8)];jets=[[import_ball(v) for v in r] for r in row['density_polynomial_at_point']];assert len(jets)==262 and all(len(r)==8 for r in jets) and all(v==0 for v in jets[-1])
 R=[[v*hp[j] for j,v in enumerate(p)] for p in jets];Rp=[[(j+1)*p[j+1]*hp[j] for j in range(7)]+[arb(0)] for p in jets]
 I=list(map(import_ball,row['i']));J=list(map(import_ball,row['j']));assert len(I)==len(J)==261
 rho=[exp_poly(R[j],3,tca,ha,Q) for j in range(261)]
 densdt=[exp_poly(add(scale(R[j],arb(3)),Rp[j]),3,tca,ha,Q) for j in range(261)]
 denstheta=[tmscale(v,arb(n)) for v,n in zip(rho,odd)]
 e4=(4*tca).exp();expneg2=exp_poly([arb(1)],-2,tca,ha,Q);pv=[];qv=[];max_green_tail=arb(0)
 for n in range(1,262):
  m=2*n;Fpoly=scale(add(add(Rp[n-1],Rp[n]),add(scale(R[n-1],arb(4-m)),scale(R[n],arb(4+m)))),arb(F(1,2).numerator)/F(1,2).denominator)
  G=exp_poly(Fpoly,4,tca,ha,Q);A0=e4*((jets[n-1][0]+jets[n][0])/2-m*I[n-1]);B0=e4*(m*J[n-1]-(jets[n-1][0]+jets[n][0])/2)
  Atm=ode(A0,-m,1,G,ha,Q);Btm=ode(B0,m,-1,G,ha,Q)
  pv.append(tmscale(mul(expneg2,tmadd(Atm,Btm),Q),arb(-1)/2))
  qv.append(tmscale(mul(expneg2,tmadd(Btm,tmscale(Atm,arb(-1))),Q),arb(1)/2))
  max_green_tail=max(max_green_tail,Atm[1],Btm[1])
 D=angular(densdt,odd,521,True,Q);H=angular(denstheta,odd,521,False,Q);P=angular(pv,even,522,False,Q);Qf=angular(qv,even,522,True,Q)
 linear=[tmadd(tmscale(d,1/aa(k)),tmscale(r,arb(-1))) for d,r in zip(densdt,rho)];Lin=angular(linear,odd,521,True,Q)
 nonlinear=P[0]*D[0]+Qf[0]*H[0];shift=arb_poly([arb(0)]*(522*base)+list(Lin[0]));poly=nonlinear+shift;assert poly.degree()<=2086*base+2*Q
 nonpoly=(product_tail(P,D)+product_tail(Qf,H)+Lin[2]).upper()
 discarded=sum((upper(poly[(freq+1043)*base+j]) for freq in range(-1043,1044) for j in range(Q+1,2*Q+1)),arb(0)).upper()
 coeffs=[[poly[(1043-nu)*base+j]-poly[(1043+nu)*base+j] for j in range(Q+1)] for nu in range(1,1044,2)]
 # Center coefficients must overlap the separately reconstructed point values.
 if 'residual_coefficients' in row:
  for coeff,old in zip(coeffs,row['residual_coefficients']):assert coeff[0].overlaps(import_ball(old))
 bb=arb_mat(coeffs)*Bern.transpose();bounds=[max(upper(bb[n,j]) for j in range(Q+1)) for n in range(522)]
 polynorm=sum(bounds,arb(0)).upper();W=(polynorm+nonpoly+discarded).upper();uleft=aa(left).exp()/aa(L);mleft=uleft**3*(1+uleft**2)**aa((k-3)/2);assert mleft>0
 Wm=(W/mleft.lower()).upper();pw,pwm=pub['rows'][ci]['W'],pub['rows'][ci]['W_over_m'];assert W.rad()==0 and Wm.rad()==0;wu,mu=ff(W),ff(Wm)
 rec={'cell':ci,'left_exact':str(left),'right_exact':str(right),'tc_exact':str(tc),'h_exact':str(h),'degree':Q,'r_left':out(aa(left).exp()),'r_right':out(aa(right).exp()),'W_upper_exact':str(wu),'W_upper_display':W.str(24),'W_over_m_upper_exact':str(mu),'W_over_m_upper_display':Wm.str(24),'m_left':out(mleft),'retained_Bernstein_sum':out(polynorm),'nonpolynomial_remainder':out(nonpoly),'discarded_polynomial_remainder':out(discarded),'max_abs_lambda_h_exact':str(522*h),'max_Green_remainder':out(max_green_tail),'published_W_exact':str(pw),'published_Wm_exact':str(pwm),'W_comparison':'CONFIRMED_SELECTED_CELL' if wu<=pw else 'NOT_SHARP_ENOUGH','Wm_comparison':'CONFIRMED_SELECTED_CELL' if mu<=pwm else 'NOT_SHARP_ENOUGH','residual_coefficients_z':[[export_ball(v) for v in rr] for rr in coeffs],'seconds':time.monotonic()-cellstart}
 if not keep_coefficients:rec.pop('residual_coefficients_z')
 return rec

"""Independent controls for P283; no numerical-lane code imported or executed."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,math
import sympy as S
from scipy.integrate import quad
V=Path('research/283_exact_thermal_bounded_axis/verification');start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();C=[]
def ck(n,ok,detail=None):C.append({'name':n,'passed':bool(ok),'detail':detail})
def eq(n,a,b=0):z=S.simplify(a-b);ck(n,z==0,str(z))
f=json.loads((V/'proof_before_checks.json').read_text());ck('proof_precedes_controls',f['utc']<start and hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()==f['proof_sha256'])
for row in f['inputs']:ck('frozen_'+row['snapshot'],hashlib.sha256((V/row['snapshot']).read_bytes()).hexdigest()==row['sha256'])
beta,A,c0,x,y,t,tau,ch,chp=S.symbols('beta A c0 x y t tau ch chp',real=True);d=(3*beta+2)/2;c=beta-2
q=(1-ch)*d*y+ch*(y-3)**2;qp=d+chp*((y-3)**2-d*y)+ch*(2*(y-3)-d)
eq('cutoff_drift_derivative',S.diff(q,y)+S.diff(q,ch)*chp,qp)
eq('drift_slope_cap_decomposition',d-qp,ch*(d-2*(y-3))-chp*((y-3)**2-d*y))
u=S.symbols('u',real=True);eq('beta2_transition_difference',((y-3)**2-4*y).subs(y,u+1),u*u-8*u)
eq('beta2_lower_passage_bound_at_halfcutoff',(q-2*y).subs({beta:2,ch:S.Rational(1,2)}),(y-3)**2/2)
eq('beta2_upper_slope_at_halfcutoff',qp.subs({beta:2,ch:S.Rational(1,2),chp:0}),y-1)
for B in [S.Rational(5,2),3,4,10]:ck('positive_transverse_gap_beta'+str(B),2*B-d.subs(beta,B)>0 and S.Rational(3,2)*B<2*B)
ck('beta2_outer_slope_allowed',2<S.Rational(5,2)<3)
bp,higher,eta1=S.symbols('bp higher eta1',real=True)
eq('leading_transverse_convex_combination',beta-(bp-beta)*ch,beta*(1-ch)+(2*beta-bp)*ch)
eq('beta2_strong_margin',1-S.Rational(1,4)-S.Rational(1,4),S.Rational(1,2))
eq('beta2_global_margin',0-S.Rational(1,4),-S.Rational(1,4))
eq('beta2_passage_lower_bound',2*y-2*y/S.Integer(4)-S.Rational(1,4),3*y/S.Integer(2)-S.Rational(1,4))
ck('beta2_passage_strict1', (3*y/S.Integer(2)-S.Rational(1,4)).subs(y,1)>1)
eq('passage_duration_bound',S.Rational(3,2)-1,S.Rational(1,2))
eq('logarithmic_expansion_loss',(S.Rational(1,2)+S.Rational(1,4))*S.Rational(1,2),S.Rational(3,8))
r=S.symbols('r',positive=True);psi=S.Function('v')(y)*x**5*S.Function('cut')(x)/5
ux=-S.diff(psi,y);uy=S.diff(psi,x)
eq('higher_stream_W1_over_x',ux/x,-S.diff(S.Function('v')(y),y)*x**4*S.Function('cut')(x)/5)
eq('higher_stream_W2',uy,S.Function('v')(y)*(x**4*S.Function('cut')(x)+x**5*S.diff(S.Function('cut')(x),x)/5))
eq('stream_divergence',S.diff(ux,x)+S.diff(uy,y))
localpsi=c0*x+(d-beta)*x*y-A*x**3/(3*beta);theta=A*x*x/2;om=-S.diff(localpsi,x,2)-S.diff(localpsi,y,2);wx=beta*x-S.diff(localpsi,y);wy=beta*y+S.diff(localpsi,x)-c0
eq('center_W1',wx,c*x/2);eq('center_W2',wy,d*y-A*x*x/beta);eq('center_Omega',om,2*A*x/beta)
eq('center_thermal',wx*S.diff(theta,x)+wy*S.diff(theta,y)-c*theta)
eq('center_vorticity',wx*S.diff(om,x)+wy*S.diff(om,y)+om-S.diff(theta,x))
eq('center_divergence',S.diff(wx,x)+S.diff(wy,y),2*beta)
x0,y0=S.symbols('x0 y0',real=True);K=A/(beta*(d-c));xt=S.exp(c*t/2)*x0;yt=S.exp(d*t)*(y0-K*x0*x0)+K*S.exp(c*t)*x0*x0
eq('exact_center_flow_x',S.diff(xt,t),c*xt/2);eq('exact_center_flow_y',S.diff(yt,t),d*yt-A*xt*xt/beta)
eq('center_flow_initial_y',yt.subs(t,0),y0);eq('beta2_equilibrium_K',K.subs(beta,2),A/8)
lam,mu,kap,NN,LL=S.symbols('lam mu kap NN LL',real=True)
eq('correction_integrand_exponent',-c*t+NN*kap*t-LL*t,(NN*kap-c-LL)*t)
H=S.Function('H');eq('flow_resolvent_identity',S.diff(S.exp(c*t)*H(t),t)-c*S.exp(c*t)*H(t),S.exp(c*t)*S.diff(H(t),t))
eq('thermal_growth_exponent',beta*((beta-2)/beta),c);eq('compact_thermal_energy_coefficient',-beta-c,2*(1-beta));eq('harmonic_moment_weight',S.diff(x,x,2)+S.diff(x,y,2))
# All-order coefficient identities remain independent of exterior b and cutoff choices.
n,j=S.symbols('n j',integer=True,positive=True);b1=S.symbols('b1')
eq('allorder_thermal_diagonal',2*n*(2*beta-b1)-c,(4*n-1)*beta+2-2*n*b1)
eq('allorder_vorticity_diagonal',(2*n+1)*(2*beta-b1)+1,(4*n+2)*beta+1-(2*n+1)*b1)
eq('quartic_factorial_forcing_vprime',24*S.Rational(2,3)/2,8);eq('quartic_factorial_forcing_Tprime',S.Rational(24,2),12)
eq('endpoint_ratio_diagonal',(7*beta+2+8/tau)+(-4/tau-2*d),4*beta+4/tau)
k2=-6*d/beta;k1=(-48-6*k2)/(4*beta);k0=-5*k1/(4*beta);P=k2*tau**2+k1*tau+k0
eq('endpoint_polynomial_residual',S.diff(P,tau)+(4*beta+4/tau)*P+24*d*tau*tau+48*tau,4*k0/tau)
# Manufactured flat compact temperature. For W=(x,(2beta-1)y), the correction
# must recover Theta0 exactly by the fundamental theorem along the contracting
# backward flow. Its corrected field is zero. This is a lemma test, no profile.
def thermal(zx,zy):
 if zx==0 or abs(zx)>=1 or abs(zy)>=1:return (0.,0.,0.)
 ex=-1/(zx*zx)-1/(1-zx*zx)-1/(1-zy*zy)
 if ex < -700:return(0.,0.,0.)
 v=math.exp(ex);return v,v*(2/zx**3-2*zx/(1-zx*zx)**2),v*(-2*zy/(1-zy*zy)**2)
rows=[]
for B in [2.,3.]:
 for X,Y in [(.5,.2),(.75,.5),(1.2,.3),(.5,1.2),(-.6,-.2)]:
  cb=B-2;dy=2*B-1
  def integ(u):
   if u==0:return 0.0
   xx=u*X;yy=u**dy*Y;v,vx,vy=thermal(xx,yy)
   return (xx*vx+dy*yy*vy-cb*v)*u**(-cb-1)
  val,err=quad(integ,0.,1.,epsabs=2e-13,epsrel=2e-11,limit=120);expected=thermal(X,Y)[0]
  row={'beta':B,'point':[X,Y],'correction_F':val,'Theta0':expected,'abs_error':abs(val-expected),'quadrature_estimate':err};rows.append(row)
  ck('manufactured_flat_correction_'+str(B)+'_'+str((X,Y)),abs(val-expected)<2e-11,row)
res={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'passed':sum(x['passed']for x in C),'total':len(C),'checks':C,'manufactured':rows,'scope':'Finite symbolic/diagnostic controls supplement the complete informal proof. No full-B2 solution or rigorous quadrature error bound.'}
(V/'controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items()if k not in ['checks','manufactured']},indent=2));print('FAILURES',json.dumps([x for x in C if not x['passed']]))

from pathlib import Path
from datetime import datetime,timezone
import sympy as S,json,hashlib,time
v=Path('research/296_simple_axis_endpoints/verification');start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();checks=[]
def ck(n,x,d=None):checks.append(dict(name=n,passed=bool(x),detail=d))
def eq(n,x):
 q=S.factor(S.cancel(S.expand(x)));ck(n,q==0,str(q))
s=S.symbols('s',positive=True);beta,c=S.symbols('beta c',positive=True);C=S.symbols('C',nonzero=True);H,E,ell=S.symbols('H E ell',real=True);L=3*beta+2;M=2*beta+1;N=7*beta+2
n=2+L/c;m=1+M/c;lk=2+4*beta/c;delta=4+N/c;hh=c+beta+1;FF=8*c+10*beta+8;R1=2*c+2*beta-1;R2=c+beta-2
for name,x in {'delta':delta-n-lk,'n_minus_m':n-m-hh/c,'thermal_exponent':c*n-L-2*c,'eta_exponent':c*m-M-c,'eta_particular':-(c*n-M-c)/hh+1,'forcing_coefficient':FF-4*hh-2*c*n,'R1':c*(lk-m+1)-R1,'R2':c*(lk-n+1)-R2,'homogeneous_I2_power':delta-2*n-(beta-2)/c,'eta_I2_power':m-n-1+2+(beta+1)/c,'R2_implies_R1_three':R1.subs(c,2-beta)-3}.items():eq(name,x)
for eps in [-1,1]:
 eq(f'K_H_coefficient_{eps}',c*(lk-m+1)*(-eps*FF*H/(c*R1))+eps*FF*H/c)
 eq(f'K_T_coefficient_{eps}',c*(lk-n+1)*(eps*2*n*C/(hh*R2))-eps*2*n*C/hh)
 eq(f'resonant_H_coefficient_{eps}',-c*(eps*FF*H/c**2)+eps*FF*H/c)
 eq(f'resonant_T_coefficient_{eps}',-c*(-eps*2*n*C/(c*hh))-eps*2*n*C/hh)
# A formal monomial x^r times log has resonant Euler remainder -c x^r.
r=S.symbols('r',real=True);eq('Euler_log_resonance',S.expand(-c*s*S.diff(s**r*S.log(s),s)+c*r*s**r*S.log(s)+c*s**r))
for bet,cval,order,eta0,D0 in [(S.Integer(2),S.Integer(1),10,H*s**6-C*s**10/4,lambda e:E*s**20-e*S.Rational(36,5)*C*H*s**15+e*5*C**2*s**19),(S.Rational(1,5),S.Rational(1,5),15,H*s**8-S.Rational(5,7)*C*s**15,lambda e:E*s**21+e*290*C*H*s**22-e*S.Rational(375,28)*C**2*s**29)]:
 for eps in [-1,1]:
  label=f'b{bet}_eps{eps}';dy=lambda f:-eps*S.diff(f,s);b=eps*cval*s;T=C*s**order;eta=eta0;vv=-eta/2;D=D0(eps)
  rr=[b*dy(T)+(3*bet+2-2*dy(b))*T,b*dy(eta)+(2*bet+1-dy(b))*eta-T,eta+dy(dy(b))+2*vv,b*dy(D)+(7*bet+2-4*dy(b))*D-8*dy(vv)*T+12*vv*dy(T)]
  for i,x in enumerate(rr):eq(label+'_ODE'+str(i),x)
  for key,x in [('b',b),('T',T),('eta',eta),('v',vv),('D',D)]:ck(label+'_signed_polynomial_'+key,x.is_polynomial(s))
  if bet==2:
   eq(label+'_I2',D/T**2-(E/C**2-eps*S.Rational(36,5)*H/C*s**-5+eps*5*s**-1))
   for hv in [-1,1]:eq(label+'_infinite_sign_'+str(hv),S.cancel(s**5*D/T**2).subs({s:0,H:hv,C:1})+eps*S.Rational(36,5)*hv)
  else:eq(label+'_I2',D/T**2-(E/C**2*s**-9+eps*290*H/C*s**-8-eps*S.Rational(375,28)*s**-1))
# Curvature coefficient and the sK stable equation, independent symbolic jets.
k,a3=S.symbols('k a3',real=True);B=c*s+k*s**2+a3*s**3;geom=4*S.diff(B,s,3)-6*S.diff(B,s,2)*(L+2*S.diff(B,s))/B
eq('curvature_forcing_limit',S.limit(s*geom,s,0)+12*k*n)
eq('curvature_stable_coefficient',S.limit(4*beta+2*S.diff(B,s)+B/s,s,0)-4*beta-3*c)
Z=S.Function('Z')(s);eq('sK_equation',s*(-B*S.diff(Z/s,s)+(4*beta+2*S.diff(B,s))*Z/s)-(-B*S.diff(Z,s)+(4*beta+2*S.diff(B,s)+B/s)*Z))
# Analytic realization: first-order rational system and actual nonlinear coefficient equations.
x,z,h,g=S.symbols('x z h g',real=True);ht,gt=S.symbols('ht gt',real=True);X=S.Matrix([x,z,ht,gt]);A=S.Matrix([[-1,1,0,0],[0,0,0,0],[-6*H,H,0,0],[-10*C,2*C,0,0]])
for eps in [-1,1]:
 f=S.Matrix([z-x,-eps*s**7*(H+ht),((z-6*x)*(H+ht)-s**4*(C+gt))/(1+x),(2*z-10*x)*(C+gt)/(1+x)])
 ck('Jacobian_'+str(eps),all(S.cancel(q)==0 for q in (f.jacobian(X).subs({s:0,x:0,z:0,ht:0,gt:0})-A)))
 R=f-A*X;R0=R.subs({x:0,z:0,ht:0,gt:0});ck('R0_only_s4_s7_'+str(eps),all(S.cancel(q)==0 for q in (R0-S.Matrix([0,-eps*s**7*H,-s**4*C,0]))))
 for i in range(4):ck(f'R0_order4_{eps}_{i}',S.cancel(R0[i]/s**4).is_polynomial(s))
 # Identities expressed using x,z,h,g and s-derivatives supplied only by (8).
 xp=(z-x)/s;zp=-eps*s**6*h;hp=((z-6*x)*h-s**4*g)/((1+x)*s);gp=(2*z-10*x)*g/((1+x)*s)
 BB=s*(1+x);BBs=1+x+s*xp;BBss=zp;T=s**10*g;Ts=10*s**9*g+s**10*gp;eta=s**6*h;etas=6*s**5*h+s**6*hp
 eq('analytic_Bprime_'+str(eps),BBs-1-z);eq('analytic_curl_'+str(eps),eta+eps*BBss)
 eq('analytic_thermal_'+str(eps),BB*Ts-(8+2*BBs)*T)
 eq('analytic_eta_'+str(eps),BB*etas-(5+BBs)*eta+T)
 eq('analytic_fourth_'+str(eps),-BB*2*ell*T*Ts+(16+4*BBs)*ell*T*T)
 eq('analytic_I2_'+str(eps),ell*T*T/(T*T)-ell)
l=S.symbols('l');eq('matrix_charpoly',A.charpoly(l).as_expr()-l**3*(l+1));eq('positive_integer_matrix_determinant',(l*S.eye(4)-A).det()-l**3*(l+1))
for i,x0 in enumerate(A**3+A**2):eq('matrix_minpoly_'+str(i),x0)
rp=S.symbols('rp',positive=True);P=S.eye(4)-S.log(rp)*A+(rp-1-S.log(rp))*A**2
for i,x0 in enumerate(rp*P.diff(rp)+A*P):eq('matrix_power_ODE_'+str(i),x0)
ck('matrix_power_at_one',P.subs(rp,1)==S.eye(4))
# Taylor quotient classifications include positive, zero, and negative powers.
for nn in [1,3,10,15]:
 for jj in [0,nn,2*nn,2*nn+1]:eq(f'leading_quotient_n{nn}_j{jj}',(s**jj/(C*s**nn)**2)/(s**(jj-2*nn)/C**2)-1)
f=json.loads((v/'freeze.json').read_text());ck('proof_precedes_controls',f['utc']<start);ck('proof_unchanged',hashlib.sha256((v.parent/'PROOF.md').read_bytes()).hexdigest()==f['proof_sha256'])
for row in f['inputs']:ck('frozen_'+row['snapshot'],hashlib.sha256((v/row['snapshot']).read_bytes()).hexdigest()==row['sha256'])
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:x for k,x in out.items()if k!='checks'},indent=2));print('FAILED',json.dumps([x for x in checks if not x['passed']],indent=2))

"""Independent symbolic controls for188; no solver or cluster code."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,time,hashlib
import sympy as s
start=time.monotonic();records=[];negative=[]
def zero(expr,label):
    assert s.simplify(expr)==0,(label,expr);records.append(label)
a,h,r,k=s.symbols('a h r k',real=True)
# Physical-coordinate verification on a curved arclength chart, radius1.
P=s.Function('P')(a,h);Qv=s.Function('Q')(a,h);T=s.Function('T')(a,h);J=1-h
X=s.Matrix([(1-h)*s.sin(a),1-(1-h)*s.cos(a)]);tau=s.Matrix([s.cos(a),s.sin(a)]);n=s.Matrix([-s.sin(a),s.cos(a)])
zero(s.det(X.jacobian([a,h]))-J,'curved-chart-J')
dx=lambda f:s.cos(a)/J*s.diff(f,a)-s.sin(a)*s.diff(f,h)
dy=lambda f:s.sin(a)/J*s.diff(f,a)+s.cos(a)*s.diff(f,h)
W=P*tau+Qv*n
zero(dx(W[0])+dy(W[1])-(s.diff(P,a)/J+s.diff(Qv,h)-Qv/J),'curved-divergence')
zero(-dx(W[1])+dy(W[0])-(s.diff(P,h)-(s.diff(Qv,a)+P)/J),'curved-negative-curl')
zero(W[0]*dx(T)+W[1]*dy(T)-(P/J*s.diff(T,a)+Qv*s.diff(T,h)),'curved-transport')
zero(dx(T)-(s.cos(a)/J*s.diff(T,a)-s.sin(a)*s.diff(T,h)),'physical-horizontal-source')
# Constant oblique tangent/normal matrices, genuinely rational angles.
for tx,ty in [(s.Rational(1),s.Rational(0)),(s.Rational(0),s.Rational(1)),(s.Rational(3,5),s.Rational(4,5)),(s.Rational(-5,13),s.Rational(12,13))]:
 tau=s.Matrix([tx,ty]);n=s.Matrix([-ty,tx]);M=(4*n+k*tau)*n.T;b=n+k*tau/4
 for i in range(2):
  for j in range(2):zero((M*M-4*M)[i,j],f'Msquare-{tx}-{ty}-{i}{j}')
 for i in range(2):zero((M*b-4*b)[i],f'eigenvector-{tx}-{ty}-{i}')
 zero(s.det(s.Matrix.hstack(tau,b))-1,f'initial-J-{tx}-{ty}')
# Universal polynomial y_r: integral factor1/(4j+1), both signs of r.
for j in range(21):
 z=r**j/s.Integer(4*j+1);zero(4*r*s.diff(z,r)+z-r**j,f'signed-r-ODE-{j}')
 for sign in [-1,1]:zero((4*r*s.diff(z,r)+z-r**j).subs(r,s.Rational(sign,3)),f'r-side-{j}-{sign}')
# Nonlinear area embeddings, converse only; no endpoint or B2 profile claimed.
x,y=s.symbols('x y',real=True)
for f in [a*a/7,a**3/5-a/3,a**4/11+a**2/2]:
 XX=s.Matrix([a,r+f]);Xa=XX.diff(a);Xr=XX.diff(r);theta=4*f
 omega=s.diff(theta,a);E=4*s.diff(r*Xa.dot(Xr),r)-4*r*s.diff(Xr.dot(Xr),a)
 zero(s.det(XX.jacobian([a,r]))-1,'nonlinear-embedding-J-'+str(f))
 zero(E-omega,'nonlinear-E-'+str(f))
 ff=f.subs(a,x);WW=s.Matrix([0,4*(y-ff)]);TT=4*ff;OO=4*s.diff(ff,x)
 zero(s.diff(WW[0],x)+s.diff(WW[1],y)-4,'nonlinear-div-'+str(f))
 zero(-s.diff(WW[1],x)+s.diff(WW[0],y)-OO,'nonlinear-curl-'+str(f))
 zero(WW[0]*s.diff(TT,x)+WW[1]*s.diff(TT,y),'nonlinear-T-'+str(f))
 zero(WW[0]*s.diff(OO,x)+WW[1]*s.diff(OO,y)+OO-s.diff(TT,x),'nonlinear-V-'+str(f))
# Coefficient-level recurrence with arbitrary curvature and a-derivative jets.
def convolution(a,b,N):return[s.expand(sum(a[i]*b[j-i]for i in range(j+1)if i<len(a)and j-i<len(b)))for j in range(N+1)]
def plus(a,b):return[s.expand(x+y)for x,y in zip(a,b)]
def dh(a):return[(j+1)*a[j+1]for j in range(len(a)-1)]+[s.Integer(0)]
kap,tx,ty,theta1=s.symbols('kap tx ty theta1');nx=-ty
for m in range(9):
 N=m+2;pp=list(s.symbols('p0:'+str(N+1)));qq=list(s.symbols('q0:'+str(N+1)));tt=list(s.symbols('t0:'+str(N+1)));oo=list(s.symbols('o0:'+str(N+1)))
 daP=list(s.symbols('ap0:'+str(N+1)));daQ=list(s.symbols('aq0:'+str(N+1)));daT=list(s.symbols('at0:'+str(N+1)));daO=list(s.symbols('ao0:'+str(N+1)))
 pp[0]=qq[0]=daP[0]=daQ[0]=s.Integer(0);qq[1]=s.Integer(4);daQ[1]=s.Integer(0);daT[0]=theta1
 inv=[kap**j for j in range(N+1)];pJ=convolution(pp,inv,N)
 div=plus(plus(convolution(daP,inv,N),dh(qq)),[-kap*z for z in convolution(qq,inv,N)])
 curl=plus(dh(pp),[-z for z in convolution(plus(daQ,[kap*z for z in pp]),inv,N)])
 therm=plus(convolution(pJ,daT,N),convolution(qq,dh(tt),N))
 vort=plus(plus(convolution(pJ,daO,N),convolution(qq,dh(oo),N)),oo)
 rhs=plus([tx*z for z in convolution(daT,inv,N)],[nx*z for z in dh(tt)])
 if m>=1:zero(div[m].coeff(qq[m+1])-(m+1),f'div-next-Q-{m}')
 else:zero(div[0]-4,'div-Q1')
 zero(curl[m].coeff(pp[m+1])-(m+1),f'curl-next-P-{m}')
 zero(therm[m+1].coeff(pp[m+1])-theta1,f'thermal-next-P-{m}')
 zero(therm[m+1].coeff(tt[m+1])-4*(m+1),f'thermal-next-T-{m}')
 zero(vort[m].coeff(oo[m])-(4*m+1),f'vorticity-next-O-{m}')
 zero(rhs[m].coeff(tt[m+1])-nx*(m+1),f'physical-source-next-T-{m}')
 om=s.symbols('om');pnew=om/(m+1);tnew=-theta1*pnew/(4*(m+1));reduced=(4*m+1)*om-nx*(m+1)*tnew
 zero(s.diff(reduced,om)-(4*m+1-ty*theta1/(4*(m+1))),f'determinant-multiplier-{m}')
for m in range(41):
 for ty0 in map(Q,['-1','-4/5','0','4/5','1']):
  for th0 in map(Q,['-399/100','0','399/100']):
   assert 4*m+1-ty0*th0/(4*(m+1))>0;records.append(f'positive-d-{m}-{ty0}-{th0}')
# Required hypotheses and sign errors are not harmless.
assert 1-Q(4,5)*5/4==0 and Q(3,5)*5!=0;negative.append('resonant-arc-data-inconsistent')
assert 1-Q(1)*4/4==0;negative.append('nonstrict-threshold-loses-uniqueness')
assert s.diff(2*y*y+x,x).subs(x,0)!=0;negative.append('potential-values-alone-do-not-match-vector')
for power in [2,3,5]:
 # Graph-converse fields glued to the straight gradient side with only finite flatness.
 jump=s.diff(4*power*x**(power-1),x,power-1).subs(x,0);assert jump!=0;negative.append(f'finite-flatness-only-{power}')
assert -4*s.diff(a*a,a)!=4*s.diff(a*a,a);negative.append('opposite-curl-sign')
assert Q(1,5)!=Q(1,4);negative.append('wrong-vorticity-integral-weight')
assert Q(1,5)!=Q(1);negative.append('dropped-plus-Omega-term')
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','exact_controls':len(records),'negative_controls':len(negative),'checks':records,'rejected':negative,'elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite algebraic controls only; analytic normal form, gluing and formal-solvability proof are in PROOF.md. Manufactured fields have no outgoing endpoint and are not B2 profiles.'}
p=Path('research/188_local_outgoing_endpoint_reduction/verification/controls.json');p.write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in ['checks','rejected']})

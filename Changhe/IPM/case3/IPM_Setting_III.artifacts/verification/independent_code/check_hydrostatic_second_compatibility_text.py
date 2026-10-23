"""Result205: exact general cusp algebra and frozen-text scope audit."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
import sympy as s
r=Path('research/hydrostatic_second_compatibility_text_audit/verification');checks=[]
def ck(name,ok,detail=None):checks.append(dict(name=name,pass_=bool(ok),detail=detail))
def zero(name,value):
 z=s.simplify(value);ck(name,z==0,str(z))
for row in json.loads((r/'INPUTS.json').read_text())['files']:
 ck('frozen source hash '+row['name'],hashlib.sha256((r/row['name']).read_bytes()).hexdigest()==row['sha256'])
for number,count in ((198,38),(199,94)):
 q=json.loads((r/f'checks{number}.json').read_text());ck(f'prior {number} all {count} independent checks passed',len(q['checks'])==count and all(t['passed']for t in q['checks']))
b=(r/'body.txt').read_text();a=(r/'app.txt').read_text()
for phrase in ['Let 1/2 < p < 1','K = f(0, 1) > 0','V[f], given by (2) of 3.72','smooth on R^2 minus the origin','Define f_{3p-2} by (1)','only if C_d(f_d) = 0','the expansion that leads to (1) formal as in 3.74(d)','no hydrostatic solution is constructed','the conditions at higher degrees are not examined','expansions with angular layers or other matching are not excluded','nothing is claimed for c >= 2']:
 ck('body hypothesis or scope '+phrase,phrase in b)
for phrase in ['uniformly for xi near any point','bounds for all xi-derivatives','smooth and odd in xi','first two terms are smooth and even in xi','the quotient tends to 0, since d < 1','jump contributes -(p + 1)(1 - p)','W_e -> W_* uniformly','W_e\', F_e converge boundedly almost everywhere','K_e = K_* int exp(-2a) eta_e(a) da','W = (W_e + delta W_0)/(K_e + delta)','s O(s^{d - 4}) integrable','a quadratic polynomial','negative at t = 0 by (a) and positive at t = 1']:
 ck('appendix supporting step '+phrase,phrase in a)
p,q,x,y,t,S,K,Q,delta,Ke=s.symbols('p q x y t S K Q delta Ke',positive=True)
B=s.Function('B')(t)
curv=q*(q-1)*B-2*(q-1)*t*s.diff(B,t)+t*t*s.diff(B,t,2)
boundary=t**3*s.diff(B,t)-(2*q+1)*t*t*B
zero('finitepart two-IBP derivative',s.diff(boundary,t)+(q+1)*(q+2)*t*B-t*curv)
zero('axis leading moment terms cancel',(q-(2*q+1))*K+(q+1)*(q+2)*K/(q+2))
# Substitute each exterior monomial directly in the primitive boundary identity.
for deg,coef,target in [(q,K,0),(q-2,Q/2,Q*S**q/q)]:
 f=coef*t**deg;lhs=S**3*s.diff(f,t).subs(t,S)-(2*q+1)*S*S*f.subs(t,S)+(q+1)*(q+2)*coef*S**(deg+2)/(deg+2)
 zero('subtracted exterior monomial '+str(deg),lhs-target)
zero('canonical pure axis power',Q*y**q/q+Q*y*y**(q-1)/(1-q)-Q*y**q/(q*(1-q)))
# Differentiate the exact remainder representation at finite lower endpoint.
e=s.Function('e')(t);A=s.Function('A')(S);Btail=s.Function('Btail')(S)
# A=int_S^inf e, Btail=int_S^inf t e. The derivative of -(Btail-S*A) is A.
rem=-Btail+S*A
zero('tail remainder derivative',s.diff(rem,S).subs({s.diff(A,S):-e.subs(t,S),s.diff(Btail,S):-S*e.subs(t,S)})-A)
zero('tail remainder bound exponent',q+(q-2)*(-1)-2)
D=(1-p)/p;d=2*p-1
zero('degree-d equation',(d/p-1)+D)
zero('degree-third equation',((3*p-2)/p-1)+2*D)
beta=p*(p+2)
zero('explicit coefficient simplification',-p/( (p+2)**2*(1-p))*(beta*(1-d*d)/d+(3-beta)*(d+1)*(d+2)/(3-d))+3*p*p*(4*p*p+5*p-1)/((p+2)**2*(2*p-1)*(2-p)))
zero('explicit beta positive gap',3-beta-(1-p)*(p+3))
# Scaling of the general quotient: h is quadratic in f and the next coefficient cubic.
alpha,Vf,F,H,Vh=s.symbols('alpha Vf F H Vh',real=True)
zero('normalized density has K1',(Ke+delta)/(Ke+delta)-1)
zero('quadratic normalization coefficient',((Vf+delta*Vh)/(Ke+delta))*((F+delta*H)/(Ke+delta))-(Vf*F+delta*(Vf*H+Vh*F)+delta**2*Vh*H)/(Ke+delta)**2)
zero('third coefficient amplitude cubic',(alpha*Vf)*(alpha**2*H)+(alpha**2*Vh)*(alpha*F)-alpha**3*(Vf*H+Vh*F))
# Log smoothing preserves exactly the density transform and its upper coefficients.
aa,ss=s.symbols('aa ss',real=True);kk,bb=s.symbols('kk bb',real=True)
zero('log-smoothed exterior K',s.exp((p-2)*aa)*kk*s.exp(-p*aa)-kk*s.exp(-2*aa))
zero('log-smoothed exterior b',s.exp((p-2)*aa)*bb*s.exp(-(p-2)*aa)-bb)
Kstar=(1-p)*(p+2)/2;bstar=-p*(1-p)/2
zero('jump size',Kstar+bstar-(1-p))
zero('limiting positive moment',-(p+1)*(1-p)+p*Kstar/(2*p+1)-(p+2)*bstar/(2*p-1)-(1-p)**2*(2*p*p+2*p+1)/(4*p*p-1))
for pp in (s.Rational(3,5),s.Rational(2,3),s.Rational(3,4),s.Rational(9,10),s.Rational(99,100)):
 ck('positive Mstar '+str(pp),((1-p)**2*(2*p*p+2*p+1)/(4*p*p-1)).subs(p,pp)>0)
 ck('negative explicit Cd factor '+str(pp),(-3*p*p*(4*p*p+5*p-1)/((p+2)**2*(2*p-1)*(2-p))).subs(p,pp)<0)
# Read every producer check line, including the two exact symbolic zeros.
lines=(r/'lead_check198.txt').read_text().strip().splitlines();ck('lead check has three values and exact degree checks',len(lines)==4 and lines[-1]=='0 0')
for line in lines[:3]:
 w=line.split();pv=float(w[0]);v=float(w[1]);f1=float(w[2]);f2=float(w[3]);rel=float(w[5]);q1=float(w[7]);q2=float(w[8])
 ck('lead cutoff check negative '+str(pv),v<0 and f1<0 and f2<0)
 ck('lead printed agreement '+str(pv),abs(v-f1)/abs(f1)<1e-9 and rel<1e-9,dict(observed=abs(v-f1)/abs(f1),printed=rel))
 ck('lead two coefficients and curvature agree '+str(pv),abs(f1-f2)<1e-12 and abs(q1-q2)<1e-12)
ck('lead finite-cutoff method explicitly inspected','Sc=mp.mpf(10)**8' in (r/'lead_check198.py').read_text() and 'I+=f(Sc)*Sc/(2-d)' in (r/'lead_check198.py').read_text())
result=dict(utc=datetime.now(timezone.utc).isoformat(),checks=checks,pass_count=sum(t['pass_']for t in checks),fail_count=sum(not t['pass_']for t in checks),scope='Exact section3.76v1, trace and formal-hierarchy scopes only; no endpoint')
(r/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(result['utc'],result['pass_count'],'PASS',result['fail_count'],'FAIL')
for row in checks:
 if not row['pass_']:print('FAIL',row)
if result['fail_count']:raise SystemExit(1)

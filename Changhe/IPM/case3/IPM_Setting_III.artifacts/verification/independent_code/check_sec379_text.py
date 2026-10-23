from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,re
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
import sympy as S
import mpmath as mp
from negative_signed_layer import parameters,constants,contour_moments,series_moments,combination_moments
root=Path('research/sec379_text_audit');v=root/'verification/v1';checks=[];rows=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(name,test,evidence=None):checks.append({'name':name,'passed':bool(test),'evidence':evidence})
def flat(t):return ' '.join(t.split())
def num(x):return mp.nstr(x,24)
for d in json.loads((v/'INPUTS.json').read_text()):check('frozen '+d['frozen'],sha(d['frozen'])==d['sha256'])
prior=json.loads(Path('research/negative_signed_inner_layer/verification/CHECKS.json').read_text())
check('224 gate',prior['status']=='PASS'and prior['count']==111)
for key,path in [('proof_sha256','research/negative_signed_inner_layer/PROOF.md'),('module_sha256','independent_code/negative_signed_layer.py'),('driver_sha256','independent_code/check_negative_signed_layer.py')]:check('224 '+key,prior[key]==sha(path))
b=flat((v/'body.txt').read_text());app=flat((v/'app.txt').read_text())
for x in ['0 < p < 1','K = Theta(pi/2) > 0','three bounds of 3.72(d)','v(y) = c y - V_2(0, y)','- p K w = 0','h\'\' + (mu th - n)(mu th - n + 1) w = 0','coefficient of z^p in h at infinity is -p K C_p(Theta)/D','X = +lambda/z^2','leading order only','other layer widths','nonlinear inner balances','matching with the core','not profiles at finite slope']:
 check('body '+x,x in b)
for x in ['v\' = c - int_y^inf g_xixi(0, t) dt','centre condition int_0^inf g_xixi(0, t) dt = c - 1','0 < K < inf','the contour is deformed so that p/2 lies on its left and 0 on its right','3 pi/2','differentiation under the integral','there is no exponential part','Gamma(-1/2) = -2 sqrt(pi)','u_G(0) = Gamma(1 - b_1) Gamma(a_1) Gamma(a_2)/Gamma(b_2) < 0','These checks concern the formal inner problem only']:
 check('appendix '+x,x in app)
p,z,lam,K,j=S.symbols('p z lam K j',positive=True);r=p-2/(p+1);mu=(p+1)/2;A=(1-mu)/p;a=-p/2;b0=(1-p)/2;d=1/(p+1);B=1-d;kap=a+b0-B-2
exprs={'closed odd middle':d+b0-(3-p**2)/(2*(p+1)),'closed odd denominator':2-b0-(3+p)/2,'exponential z power':p-2*kap-(5+2*p+r),'pole separation':d-p/2-(1-p)*(p+2)/(2*(p+1)),'tail convergence':(p-r-2)+2*p/(p+1),'leading equation sign':-2*A*(-p*K/(1/p-1))-p*K,'derivative exponent':(5+2*p+r)-3-(2*p+r+2),'Wronskian exponent':(2*p+r-1)-2*(2*p+r+2)-(-2*p-r-5),'bounded exponent':(2*p+r+2)+(-2*p-r-5)+3,'inverse factor':mu**2*(p-r)**2-1,'axis correction power':(S.Symbol('gamma')-2)+1-(S.Symbol('gamma')-1)}
for name,e in exprs.items():check(name,S.simplify(e)==0,str(S.factor(e)))
h=S.Function('h')(z);theta=lambda f:z*S.diff(f,z)
L=theta(theta(theta(h)))-(2*p+r+2)*theta(theta(h))+(p*r+p*(p+2)+r*(p+2))*theta(h)-p*r*(p+2)*h+2*lam*S.diff(h,z,2)
P=(1-2*p-r)/z+2*lam/z**3;Q=(p**2+2*p*r+r-1)/z**2;R=-p*r*(p+2)/z**3
check('normalized scalar ODE',S.simplify(L/z**3-(S.diff(h,z,3)+P*S.diff(h,z,2)+Q*S.diff(h,z)+R*h))==0)
H=S.Function('H')(z);vv=S.Function('v')(z);hh=H*vv
full=S.diff(hh,z,3)+P*S.diff(hh,z,2)+Q*S.diff(hh,z)+R*hh
reduced=H*S.diff(vv,z,3)+(3*S.diff(H,z)+P*H)*S.diff(vv,z,2)+(3*S.diff(H,z,2)+2*P*S.diff(H,z)+Q*H)*S.diff(vv,z)+vv*(S.diff(H,z,3)+P*S.diff(H,z,2)+Q*S.diff(H,z)+R*H)
check('reduction of order identity',S.simplify(full-reduced)==0)
logW=-3*S.log(H)+(2*p+r-1)*S.log(z)+lam/z**2
check('Wronskian integrating factor',S.simplify(S.diff(logW,z)+3*S.diff(H,z)/H+P)==0)
uE=S.Function('uE')(z);II=S.Function('II')(z);uB=uE*II
check('second order Wronskian',S.simplify(uE*S.diff(uB,z)-S.diff(uE,z)*uB-uE**2*S.diff(II,z))==0)
check('recurrence monomial',S.simplify(L.subs(h,z**j).doit()-((j-p)*(j-r)*(j-p-2)*z**j+2*lam*j*(j-1)*z**(j-2)))==0)
C0,D0=S.symbols('C0 D0',nonzero=True);U0=-2*lam*D0/C0
check('nonzero bounded derivative',S.simplify(C0**(-2)/(2*lam*U0)+1/(4*lam**2*D0*C0))==0)
# Exact residue coefficients, independent of the producer's expansion implementation.
def residue_sum(pv,X,count):
 q=parameters(pv);aa,bb,dd=q['a'],q['b'],q['d'];ans=mp.mpf(0)
 for aa,bb in [(aa,bb),(bb,aa)]:
  for n in range(count):
   ans+=(-1)**n/mp.factorial(n)*mp.gamma(aa+n)*mp.gamma(dd+aa+n)*mp.gamma(bb-aa-n)/mp.gamma(2-aa-n)*X**(-aa-n)
 return ans
mp.mp.dps=60
plist=[mp.mpf(1)/4,mp.mpf(1)/3,mp.sqrt(2)-1,mp.mpf(1)/2,mp.mpf(3)/4]
for pv in plist:
 tag=num(pv);co=constants(pv)
 closed=-2*mp.sqrt(mp.pi)*mp.gamma((1-pv)/2)*mp.gamma((3-pv**2)/(2*(pv+1)))/mp.gamma((3+pv)/2)
 check(tag+' closed odd',abs(closed-co['odd'])<mp.mpf('1e-53'),num(closed))
 for X in [mp.mpf(200),mp.mpf(800)]:
  val=contour_moments(pv,X,48,0)[0];six=residue_sum(pv,X,6);err=abs((six-val)/val);tol=mp.mpf('1.5e-15')if X==200 else mp.mpf('3.4e-19')
  check(tag+' six residues X'+str(X),err<tol,num(err));rows.append({'p':tag,'X':num(X),'G':num(val),'six_residue_relative_error':num(err)})
 for X in [mp.mpf('1e-6'),mp.mpf('1e-9')]:
  g,_=combination_moments(pv,X,0);bound=mp.mpf('4.5e-5')if X==mp.mpf('1e-6')else mp.mpf('4.5e-8')
  check(tag+' smallX bound '+str(X),abs(X*g[0])<bound,num(X*g[0]))
 # Check residue matching derivative independent of quoted six-term expansion.
 check(tag+' nonzero infinity coefficient',co['A1']<0,num(co['A1']))
q=parameters(mp.mpf('.5'));co=constants(mp.mpf('.5'))
for X,quoted in [(100,'-0.155546'),(400,'-0.151909'),(1600,'-0.151032')]:
 val,_=series_moments(mp.mpf('.5'),mp.mpf(X),1,0);rat=val[0]/(mp.exp(X)*mp.mpf(X)**(q['a']+q['b']-q['B']-2));check('printed exponent coefficient '+str(X),abs(rat-mp.mpf(quoted))<=mp.mpf('5e-7'),num(rat))
# The Radau results are producer diagnostics, not certified connection coefficients.
prod=(v/'producer_chk2.txt').read_text()
for claimed in ['0.44389770','0.90480539','0.74336560','1.40698785']:check('Radau record '+claimed,claimed in prod)
for pv,quoted in [(mp.mpf('.25'),'0.443896'),(mp.mpf('.5'),'0.904794'),(mp.sqrt(2)-1,'0.743360'),(mp.mpf('.75'),'1.406913')]:
 co=constants(pv);rat=co['odd']/co['even'];check('connection ratio '+str(pv),abs(rat-mp.mpf(quoted))<mp.mpf('5e-7'),num(rat))
# Signed axis normal form and tail integral manufacture, not a global profile.
for cv in [S.Rational(3,2),S.Integer(2),S.Integer(3)]:
 vel=cv*z-(cv-1)*S.atan(z);curv=S.diff(vel,z,2)
 check('signed axis manufacture c'+str(cv),S.simplify(curv-2*(cv-1)*z/(1+z**2)**2)==0 and S.diff(vel,z).subs(z,0)==1)
 check('signed moment c'+str(cv),S.integrate(curv,(z,0,S.oo))==cv-1)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS'if all(x['passed']for x in checks)else'FAIL','count':len(checks),'checks':checks,'rows':rows,'proof_sha256':sha(root/'PROOF.md'),'driver_sha256':sha(__file__),'body_sha256':sha(v/'body.txt'),'app_sha256':sha(v/'app.txt'),'scope':'Analytic text and independent finite series/contour checks; Radau records inspected, trajectory not independently certified; full endpoint OPEN'}
(v/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print([x for x in checks if not x['passed']])
if out['status']!='PASS':raise SystemExit(1)

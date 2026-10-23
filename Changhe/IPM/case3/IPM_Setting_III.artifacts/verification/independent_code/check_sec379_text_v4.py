"""Result226v4: exact new paragraph, analytic operator and recorded-diagnostic audit."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
import sympy as S
import mpmath as mp
R=Path('research/sec379_text_audit');V=R/'verification/v4';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
flat=lambda t:' '.join(t.split())
def check(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
for row in json.loads((V/'INPUTS.json').read_text())['files']:check('frozen '+Path(row['frozen']).name,sha(row['frozen'])==row['sha256'])
g=json.loads((R/'verification/v3/CHECKS.json').read_text());check('v3 gate59',g['status']=='PASS'and g['count']==59)
for field,name in [('body_sha256','body.txt'),('app_sha256','app.txt')]:check('v3unchanged '+name,g[field]==sha(R/'verification/v3'/name))
zroot=Path('research/negative_signed_laplace_proof');zz=json.loads((zroot/'verification/CHECKS.json').read_text());check('228 gate273',zz['status']=='PASS'and zz['count']==273);check('228proofhash',zz['proof_sha256']==sha(zroot/'PROOF.md'));check('228modulehash',zz['module_sha256']==sha('independent_code/negative_signed_laplace.py'))
b=flat((V/'body.txt').read_text());a=flat((V/'app.txt').read_text());b3=flat((R/'verification/v3/body.txt').read_text());a3=flat((R/'verification/v3/app.txt').read_text())
for old,new in [('except the sign of K and the symmetry in (d), which are proved','except the sign of K, the symmetry in (d) and the statement in (c) on the solutions of (1), which are proved'),('Apart from the symmetry and the sign of K, which are exact, this is formal, and the count','The symmetry, the sign of K and the statement in (c) on the solutions of (1) are exact; the derivation of (1) as the leading inner problem is formal, and the count')]:
 check('bodyreplacement present '+old[:24],b3.count(old)==1 and b.count(new)==1);b3=b3.replace(old,new)
check('allbodychanges accounted',b3==b)
start='That these are all the solutions with C^1 even extension also follows';end='A numerical evaluation of'
extra=a[a.index(start):a.index(end,a.index(start))];check('newAbelparagraphunique',a.count(extra)==1)
rest=a.replace(extra,'');old='and E(z)/(A_E z^{p + 2}) = 1 to 1e-6 at z = 1e4. These checks concern the formal inner problem only.'
new='and E(z)/(A_E z^{p + 2}) = 1 to 1e-6 at z = 1e4; with the derivatives in z computed from the Gauss derivative formula, E and E_1 satisfy the equation with relative residuals below 1e-20 at z = 0.3, 0.7 and 3 (p = 0.25, 0.5 and 0.75). These checks concern the formal inner problem only.'
check('newnumericclause exact',rest.count(new)==1);check('allappendixchanges accounted',rest.replace(new,old)==a3)
for clause in ['E_1(z) = z Gamma((1 - s)/2)^{-1}','tau^{-(1 + s)/2}','E_1 is odd and smooth with E_1\'(0) = 1','W_2 = E E_1\' - E_1 E\' tends to 1','h and h\' are bounded','not integrable at 0','h = h(0+) E + h\'(0+) E_1 on z > 0 by uniqueness']:
 check('Abelclause '+clause,clause in extra)
for clause in ['other layer widths, nonlinear inner balances','the nonlocal outer terms, logarithms and the matching with the core','proves no nonexistence','not profiles at finite slope']:
 check('scope '+clause,clause in b)
p,z,lam=S.symbols('p z lam',positive=True);s=p-2/(1+p);h=S.Function('h')(z);theta=lambda f:S.expand(z*S.diff(f,z))
lhs=theta(theta(theta(h)-p*h)-s*(theta(h)-p*h))-(p+2)*(theta(theta(h)-p*h)-s*(theta(h)-p*h))+2*lam*S.diff(h,z,2)
P=(1-2*p-s)/z+2*lam/z**3;check('h2coefficient',S.simplify(S.expand(lhs).coeff(S.diff(h,z,2))/z**3-P)==0)
W=z**(2*p+s-1)*S.exp(lam/z**2);check('Abelfactor',S.simplify(S.diff(W,z)+P*W)==0)
ae=(1-p)/2;gamma=(1-s)/2;check('oddgamma',S.simplify(gamma-ae-1/(1+p))==0);check('oddweight',S.simplify(gamma-1+(1+s)/2)==0)
u,G=S.symbols('u G',positive=True);k=S.symbols('k',nonnegative=True,integer=True);t=u**(1/G)
check('producerendpointsubstitution',S.simplify(S.exp(-t)*t**(G-1+k)*S.diff(t,u)-S.exp(-u**(1/G))*u**(k/G)/G)==0)
q=S.symbols('q');F=S.Function('F');hz=z*F(z*z/lam)
for j in range(4):
 # Derive epsilon1 chain coefficients as an independent symbolic expression.
 calculated=S.diff(hz,z,j);check('oddchain'+str(j),S.simplify(calculated-(z*S.diff(F(z*z/lam),z,j)+(j*S.diff(F(z*z/lam),z,j-1)if j else 0)))==0)
with mp.workdps(85):
 for pp in [mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75')]:
  d=1/(pp+1);lm=4*pp**2/((1+pp)**2*(1-pp));A=[]
  for eps in [0,1]:
   aa=(eps-pp)/2;cc=mp.mpf(eps)+mp.mpf('.5');A.append(mp.gamma(cc)*mp.gamma(1+d)*lm**(-(pp+2-eps)/2)/(mp.gamma(aa)*mp.gamma(aa+d)*mp.gamma(cc-aa+1)))
  ce=mp.gamma(-pp/2)*mp.gamma(d-pp/2)*mp.gamma(mp.mpf('.5'))/mp.gamma(2+pp/2);co=mp.gamma((1-pp)/2)*mp.gamma(d+(1-pp)/2)*mp.gamma(mp.mpf('-.5'))/mp.gamma((3+pp)/2)
  check('signs p'+str(pp),A[0]<0<A[1]and ce<0 and co<0);check('connection p'+str(pp),abs(-A[0]/A[1]-(co/ce)/mp.sqrt(lm))<mp.mpf('1e-75'))
  line=next(l for l in (V/'producer_transformed_check.log').read_text().splitlines()if l.startswith(str(float(pp))+' '));nums=re.search(r' AE (\S+) AO (\S+)',line)
  check('reportedcoefficients p'+str(pp),max(abs(mp.mpf(v)/ref-1)for v,ref in zip(nums.groups(),A))<mp.mpf('3e-11'))
oldlog=(V/'producer_original_check.log').read_text();newlog=(V/'producer_transformed_check.log').read_text();oldres=list(map(float,re.findall(r'max rel ODE res (\S+)',oldlog)));newres=list(map(float,re.findall(r'max rel ODE res (\S+)',newlog)))
check('original claim not supported',len(oldres)==3 and max(oldres)>1e-6,oldres);check('correctedmeasured residuals',len(newres)==3 and max(newres)<1e-20,newres)
check('reportedparameters',all(newlog.count(str(p)+' AE ')==1 for p in [.25,.5,.75]));check('producer transformed code frozen','t = u^(1/g)'in(V/'producer_chk228.py').read_text())
check('ownindependent numericalcheck scope',max(abs(level['physical_normalized_residual'])for row in zz['rows']for level in row['levels'][-1:])<2e-8)
result=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'REVISION4_PROOF.md'),driver_sha256=sha(__file__),body_sha256=sha(V/'body.txt'),app_sha256=sha(V/'app.txt'),own228_sha256=sha(zroot/'verification/CHECKS.json'),numerical_scope='Producer1e-20 residuals are checked recorded diagnostics, not an own independently certified1e-20 accuracy claim. Own real-integral evaluator has its separately recorded quadrature discrepancies.')
(V/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count']);print([x for x in checks if not x['passed']])
if result['status']!='PASS':raise SystemExit(1)

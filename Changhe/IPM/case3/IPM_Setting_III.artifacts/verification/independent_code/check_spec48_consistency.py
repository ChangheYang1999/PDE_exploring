"""Result 239: exact scaling and scoped consistency audit of frozen SPEC v48."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial
import hashlib,json
import sympy as s
ROOT=Path('research/spec48_consistency_audit');V=ROOT/'verification'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[]
def check(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
manifest=json.loads((V/'INPUTS.json').read_text())
for q in manifest['files']:check('frozen '+q['source'],sha(Path(q['frozen']))==q['sha256'])
spec=(V/'SPEC.md').read_text();report=(V/'FINAL_REPORT.md').read_text()
check('SPEC version48','Version v48, 2026-10-21T14:51Z' in spec)
check('F2 false literal present','with L_can and b L_can^2 invariant' in spec)
check('correct covariance already in54','satisfies L_l = l L' in spec)
check('signed K scope omitted','Global slices: L = 1 (5.4) or K fixed' in spec)
check('final beta sign qualification','for every beta of the sign of N(rho*)' in report)
check('SPEC universal T2 omission','(T2) is NOT enforced by any solver' in spec)
check('report weighted T2 counterexample','Raising the weight of the cubic relations in the fit from 1 to 100' in report and 'T1 = -6.9e-7, T2 = 2.1e-7' in report)
check('SPEC obsolete degree13 claim','(degree <= 13 only; general statement open)' in spec)
check('report all-degree theorem','For every odd n >= 5 every real resonance satisfies a0 > 4A + n - 5' in report)
check('report harmonic qualification','fix at each degree the harmonic datum of the stream function' in report)
g41=spec.split(' (G41) ',1)[1].split(' (G42) ',1)[0]
check('G41 header installed','installed as FINAL_REPORT 3.78' in g41)
check('G41 obsolete tail','Consequence if confirmed' in g41 and 'Not in report.' in g41)
x,y,l=s.symbols('x y l',real=True,positive=True)
fixture=[]
for sign in [-1,1]:
 rho=sign*y*(1+x*x+y*y)**s.Rational(-1,4)
 scaled=l*rho.subs({x:x/l,y:y/l},simultaneous=True)
 a=s.simplify(s.diff(scaled,y).subs({x:0,y:0}))
 b=s.simplify(s.diff(scaled,x,2,y).subs({x:0,y:0})/2)
 K=s.limit(scaled.subs(x,0)/s.sqrt(y),y,s.oo)
 length=s.simplify((K/a)**2)
 check(str(sign)+' invariant slope',a==sign)
 check(str(sign)+' cubic scale',s.simplify(b+sign/(4*l*l))==0)
 check(str(sign)+' far scale',s.simplify(K-sign*s.sqrt(l))==0)
 check(str(sign)+' covariant length',length==l)
 check(str(sign)+' invariant cubic length',s.simplify(b*length**2+sign/4)==0)
 check(str(sign)+' length not invariant',length.subs(l,4)!=1)
 fixture.append(dict(sign=sign,a=str(a),b=str(b),K=str(K),L=str(length),at_lambda4={k:str(v.subs(l,4))for k,v in [('a',a),('b',b),('K',K),('L',length)]}))
# Check general transformation exponents algebraically, without requiring fixture transport.
p=s.symbols('p',real=True)
check('scale exponent cancellation',s.simplify(-2+2*(1-p)/(1-p))==0)
check('length exponent',s.simplify((1-p)/(1-p))==1)
# Exact positivity at all integer k is analytic; these exercise the bracket and boundary algebra.
for k in [2,3,7,12,25]:
 for A in [F(1001,1000),F(3,2),F(3),F(17,3),F(100)]:
  ell=lambda i:2*k+2*i*(A-1)
  bracket=1-ell(2)/ell(1)+F(k*(2*k+1),3)
  check(f'k{k} A{A} positive bracket',bracket>0 and ell(2)/ell(1)<2)
  def poly(aa):
   terms=[]
   for j in range(k+1):
    t=F(factorial(2*k+1),factorial(2*j+1)*factorial(2*k-2*j+1))
    for i in range(j+1,k+1):t*=1-aa/ell(i)
    terms.append(t)
   return sum(terms)
  check(f'k{k} A{A} threshold positivity',poly(ell(2))>0)
  check(f'k{k} A{A} negative slope positivity',poly(F(-7))>0)
  check(f'k{k} A{A} threshold identity',ell(2)==4*A+(2*k+1)-5)
check('parent finite PDE controls',all(z['both_PDEs_exact']for z in json.loads((V/'all_degree_checks.json').read_text())['exact_PDE_examples']))
findings=[dict(item='F2',verdict='REFUTED',repair='L_can scales by lambda; b L_can^2 is invariant.'),dict(item='5.5',verdict='OPEN as globally phrased',repair='K=kappa covers only sign(K)=sign(kappa); L=1 covers both signs. No negative-profile nonexistence was established.'),dict(item='4.3',verdict='REFUTED as universal omission claim',repair='T2 is a penalty in the 4.7(b) fit. Recompute it independently and add a condition not used in that fit. A penalty is not exact enforcement.'),dict(item='F7',verdict='REFUTED current open-status label',repair='State the scoped all-degree fixed-top-harmonic bound, not unrestricted polynomial-pair exclusion.'),dict(item='G41/G42',verdict='REFUTED current installation-status wording',repair='Replace obsolete not-in-report and installation-request labels; preserve formal PDE scope.')]
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,fixture=fixture,findings=findings,proof_sha256=sha(ROOT/'PROOF.md'),code_sha256=sha(Path(__file__)),scope='Exact covariance and frozen-document consistency only; no primary-profile existence or exclusion.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print([c for c in checks if not c['passed']])
if out['status']!='PASS':raise SystemExit(1)

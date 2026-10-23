from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,ast

def main():
 r=Path('research/stationarity_inference_audit');v=r/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();s=json.loads((v/'SOURCES.json').read_text());paths=[Path('independent_code/check_stationarity_acceptance.py'),r/'ACCEPTANCE_RULE_PROOF.md',r/'PROOF.md',v/'CHECKS.json',v/'SOURCES.json']+[Path(z['frozen'])for z in s['entries']];binds={str(p):sha(p)for p in paths};checks=[]
 def ck(n,b,e=None):
  checks.append(dict(name=n,passed=bool(b),evidence=e))
  if not b:raise AssertionError((n,e))
 for z in s['entries']:ck('source '+z['frozen'],sha(z['frozen'])==z['sha256'])
 old=json.loads((v/'CHECKS.json').read_text());ck('counterexample arithmetic',old['status']=='PASS_EXACT_LOGICAL_COUNTEREXAMPLE'and old['count']==34 and all(z['passed']for z in old['checks']))
 for p,h in old['bindings'].items():ck('counterexample dependency '+p,sha(p)==h)
 eps=F(77,10000);M=F(8192);alpha=F(1,10000);rho2=eps*eps/(1+eps*eps)
 ck('manufactured rho squared less than required slope',0<rho2<alpha,dict(rho2=str(rho2),alpha=str(alpha)))
 ck('Cauchy lower-bound polynomial positive coefficients',(alpha-rho2)>0 and M*rho2>0)
 lam=F(1,2**15);u=-eps*lam;norm2=(eps+u)**2+(1+M*u*u)**2;n0=eps*eps+1;threshold=1-alpha*lam
 ck('explicit smaller step strict norm descent',norm2<n0)
 ck('explicit smaller step positive threshold',threshold>0)
 ck('explicit smaller step rejected by actual-form test',norm2>n0*threshold**2)
 dot=eps*(eps+u)+1+M*u*u
 ck('supporting hyperplane exact',dot/n0==1-rho2*lam+M*rho2*lam*lam)
 ck('Cauchy exact squared inequality',dot*dot<=n0*norm2 and dot>0)
 # This interval only encloses the rounding bin of a printed decimal, not numerical error.
 lo=F('0.0077175');hi=F('0.0077185');ck('entire printed-rho rounding bin below alpha',0<lo<hi and hi*hi<alpha,dict(lo=str(lo),hi=str(hi)))
 text=(v/'producer_stationarity_log.txt').read_text();ck('source log observed negative derivative','directional derivative F^T J du = -1.0380e-17'in text)
 ck('source log observed nonzero normalized gradient','3.633e-03  (first-order stationarity, full)'in text)
 ck('source finite-step conclusion observed','no decrease along du: numerical local minimum along the GN direction'in text)
 source=(v/'producer_stationarity_static.py').read_text();tree=ast.parse(source);calls=[z for z in ast.walk(tree)if isinstance(z,ast.Call)and isinstance(z.func,ast.Name)and z.func.id=='range'];ck('source finite trial range',any(ast.dump(z)==ast.dump(ast.parse('range(0, 13)',mode='eval').body)for z in calls))
 ck('source norm threshold form','r < 1 - 1e-4 * lam'in source)
 for p,h in binds.items():ck('unchanged '+p,sha(p)==h)
 out=dict(status='PASS_EXACT_ACCEPTANCE_COUNTEREXAMPLE',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=binds,scope='Exact logical result and frozen source-text audit. Actual Jacobian, gradient and discrete state remain unverified. No primary IPM endpoint.')
 (v/'ACCEPTANCE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks))
if __name__=='__main__':main()

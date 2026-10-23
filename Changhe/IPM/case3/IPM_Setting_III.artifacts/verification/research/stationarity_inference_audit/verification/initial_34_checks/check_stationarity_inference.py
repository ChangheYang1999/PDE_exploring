from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,math

def main():
 r=Path('research/stationarity_inference_audit');v=r/'verification';paths=[Path('independent_code/check_stationarity_inference.py'),r/'PROOF.md',v/'COUNTEREXAMPLE_INPUT.json'];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();binds={str(p):sha(p)for p in paths};data=json.loads((v/'COUNTEREXAMPLE_INPUT.json').read_text());e=F(data['epsilon']);M=F(data['M']);checks=[];rows=[]
 def ck(n,b):
  checks.append(dict(name=n,passed=bool(b)))
  if not b:raise AssertionError(n)
 ck('exact manufactured parameters',e==F(77,10000)and M==8192and data['trial_exponents']==list(range(13)))
 ck('nonstationary gradient',e!=0);ck('strict initial descent derivative',-2*e*e<0)
 def difference(lam):
  u=-e*lam;direct=(e+u)**2+(1+M*u*u)**2-e*e-1;formula=e*e*lam*(-2+(1+2*M)*lam)+M*M*e**4*lam**4
  ck('identity at '+str(lam),direct==formula);return direct
 for k in data['trial_exponents']:
  lam=F(1,2**k);z=difference(lam);ck('rejected tested step '+str(k),z>0);rows.append(dict(k=k,lambda_exact=str(lam,s)if False else str(lam),norm_square_change=str(z)))
 lam=F(1,2**data['smaller_exponent']);z=difference(lam);ck('explicit smaller strict descent',z<0);rows.append(dict(k=data['smaller_exponent'],lambda_exact=str(lam),norm_square_change=str(z)))
 for p,d in binds.items():ck('unchanged '+p,sha(p)==d)
 out=dict(status='PASS_EXACT_LOGICAL_COUNTEREXAMPLE',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=binds,rows=rows,projected_fraction_display=float(e)/math.sqrt(1+float(e)**2),scope='Refutes the inference only. Actual producer Jacobian and solver-state stationarity not recomputed.')
 (v/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['projected_fraction_display'])
if __name__=='__main__':main()

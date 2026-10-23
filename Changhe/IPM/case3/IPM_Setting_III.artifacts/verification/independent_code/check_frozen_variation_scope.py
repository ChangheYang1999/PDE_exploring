from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math,re
import sympy as S
root=Path('research/frozen_variation_scope/verification');checks=[]
def ck(name,x):
 ok=bool(x);checks.append(dict(name=name,passed=ok));assert ok,name
t,e=S.symbols('t e',real=True);B=1/(1-t);q=1/(1-t)**2;z=S.exp(2*t);de=1/((1-t)*(1-t-e*t))
ck('background_ODE',S.simplify(S.diff(B,t)-B**2)==0)
ck('exact_difference_quotient',S.simplify(((1+e)/(1-(1+e)*t)-B)/e-de)==0)
ck('actual_variational_ODE',S.simplify(S.diff(q,t)-2*B*q)==0)
ck('eps_limit_not_frozen',S.simplify(S.limit(de,e,0)-q)==0 and S.simplify(q-z)!=0)
ck('frozen_error_t2',S.limit((q-z)/t**2,t,0)==1)
K=S.symbols('K',real=True);A=S.Matrix([[-1,K],[0,-1]]);v=S.exp(-t)*S.Matrix([K*t,1]);ck('stable_matrix_exact_evolution',S.simplify(S.diff(v,t)-A*v)==S.zeros(2,1));ck('stable_matrix_spectrum',A.eigenvals()=={-1:2})
T=.299;rat=(1-T)**-2/math.exp(2*T)-1
ck('explicit_nonzero_limit_error',rat>.1)
log=(root/'flow_log.txt').read_text();vals=[tuple(map(float,m)) for m in re.findall(r'eps ([0-9e+.-]+).*?all ([0-9e+.-]+) core ([0-9e+.-]+)$',log,re.M)]
ck('eight_flow_comparisons',len(vals)==8)
ck('reported_plateaus',vals[2][1]==vals[3][1] and abs(vals[7][1]-vals[6][1])<2e-5)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=checks,scalar_counterexample_time=T,relative_frozen_error=rat,reported_comparisons=vals,source_sha256={p.name:sha(p)for p in root.iterdir()if p.is_file()},code_sha256=sha(Path(__file__)),proof_sha256=sha(root.parent/'PROOF.md'),endpoint='UNRESOLVED')
(root/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

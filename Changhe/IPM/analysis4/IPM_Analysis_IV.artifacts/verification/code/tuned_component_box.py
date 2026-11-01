"""Exact componentwise supersolutions for the tuned-series majorant system."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
import sympy as sp
R=sp.Rational
z,W,U,V,E=sp.symbols('z W U V E');Y=sp.Matrix([W,U,V,E])
root=Path('research/124_tuned_component_radius');start=time.monotonic()

def check(name,a,kap,s):
 d=R(3,2)*kap*a*a;e=3*kap*a*d;P=a*z+d*z*z+e*z**3
 phi=sp.Matrix([
 R(3,2)*kap*(d*d+2*a*e+2*d*e*z+e*e*z*z)+3*kap*P*W+R(3,2)*kap*z**4*W*W+kap*E*(P+z**4*W),
 R(3,2)*kap*(2*d*e+e*e*z)+3*kap*(a+d*z+e*z*z)*W+R(3,2)*kap*z**3*W*W+kap*z**3*E*W,
 R(3,2)*kap*(e*e+2*(d+e*z)*W+z*z*W*W)+kap*z*z*E*W+3*kap*a*U,
 kap/s*(3*e*W+R(3,2)*z*W*W+z*E*W+3*a*V+3*d*U)])
 c=phi.subs({z:0,W:0,U:0,V:0,E:0});J=phi.jacobian(Y).subs(z,0)
 assert J**4==sp.zeros(4)
 assert all(x>=0 for x in J)
 Q=sp.eye(4)+J+J**2+J**3;assert (sp.eye(4)-J)*Q==sp.eye(4)
 Y0=Q*c;assert all(x>0 for x in Y0)
 remainder=(phi-c-J*Y).applyfunc(sp.expand)
 assert remainder.subs(z,0)==sp.zeros(4,1)
 assert all(v>=0 for p in remainder for v in sp.Poly(p,z,W,U,V,E).coeffs())
 G=(Y0+Q*remainder).applyfunc(sp.expand);box=2*Y0
 in_box=G.subs(dict(zip(Y,box)))
 trials=[];chosen=None
 for power in range(0,202,2):
  z0=R(1,2**power);value=in_box.subs(z,z0);ratios=[sp.cancel(value[i]/box[i]) for i in range(4)]
  passed=all(q<=1 for q in ratios)
  if power>=20 or passed:trials.append(dict(power=power,maximum_box_ratio=str(max(ratios)),passes=passed))
  if passed:chosen=power;break
 assert chosen is not None
 z0=R(1,2**chosen);value=in_box.subs(z,z0)
 return dict(name=name,a=str(a),kappa=str(kap),sigma_lower=str(s),d=str(d),e=str(e),J=[[str(v) for v in J.row(i)] for i in range(4)],Q=[[str(v) for v in Q.row(i)] for i in range(4)],Y0=[str(x) for x in Y0],box=[str(x) for x in box],z0=str(z0),power=chosen,exterior_radius_power=3*chosen//2,transformed_map=[str(p) for p in G],map_on_box=[str(v) for v in value],ratios=[str(sp.cancel(value[i]/box[i])) for i in range(4)],dyadic_trials=trials)

try:
 refined=json.loads(Path('research/123_tuned_response_minimum/verification/checks.json').read_text())['rows']
 for row,a,sigma in zip(refined,[R(1281,1000),R(1647,1000)],[R(38124,10**9),R(15683,10**7)]):
  assert a>=1+R(row['root_interval'][1])
  assert sigma < -R(row['sigma4']['upper'])
 rows=[check('both_roots_common',R(2),R(10),R(1,100000)),check('root1_refined',R(1281,1000),R(28,3),R(38124,10**9)),check('root2_refined',R(1647,1000),R(28,3),R(15683,10**7)),check('compatible_B6_family',R(3),R(14),R(1,200000))]
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,refined_input_inequalities_verified=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
 (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
 (root/'sources/code.py.txt').write_bytes(Path(__file__).read_bytes())
 for path,name in [(Path('research/120_tuned_explicit_radius/verification/response_bound.json'),'common_response_bound.json'),(Path('research/123_tuned_response_minimum/verification/checks.json'),'refined_response_bound.json'),(Path('research/122_tuned_compatible_stability/verification/checks.json'),'family_arithmetic.json')]:
  (root/'sources'/name).write_bytes(path.read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
 (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps(dict(all_checks_pass=True,rows=[dict(name=r['name'],power=r['power'],radius_power=r['exterior_radius_power'],maximum_ratio=float(max(R(q) for q in r['ratios']))) for r in rows],actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as exc:
 import traceback
 print(json.dumps(dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno,code=f.line) for f in traceback.extract_tb(exc.__traceback__)])),flush=True)
 raise SystemExit(1)

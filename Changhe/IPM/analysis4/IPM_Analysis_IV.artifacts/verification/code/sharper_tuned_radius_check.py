"""Independently propose and exactly certify rational positive majorant supersolutions."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
import sympy as sp
import mpmath as mp
R=sp.Rational;mp.mp.dps=65
root=Path('research/126_sharper_tuned_radius');start=time.monotonic()
z,W,U,V,E=sp.symbols('z W U V E');Y=sp.Matrix([W,U,V,E]);rows=[]
source=json.loads(Path('research/123_tuned_response_minimum/verification/checks.json').read_text())['rows']
for index,a,s,z0,displayR in [(1,R(12807,10000),R(38,10**6),R(1138,10**14),26100000000000000),(2,R(16464,10000),R(15,10000),R(1644,10**13),475000000000000)]:
 assert 1+R(source[index-1]['root_interval'][1])<a
 assert s < -R(source[index-1]['sigma4']['upper'])
 kap=R(28,3);d=R(3,2)*kap*a*a;e=3*kap*a*d;P=a*z+d*z*z+e*z**3
 phi=sp.Matrix([R(3,2)*kap*(d*d+2*a*e+2*d*e*z+e*e*z*z)+3*kap*P*W+R(3,2)*kap*z**4*W*W+kap*E*(P+z**4*W),R(3,2)*kap*(2*d*e+e*e*z)+3*kap*(a+d*z+e*z*z)*W+R(3,2)*kap*z**3*W*W+kap*z**3*E*W,R(3,2)*kap*(e*e+2*(d+e*z)*W+z*z*W*W)+kap*z*z*E*W+3*kap*a*U,kap/s*(3*e*W+R(3,2)*z*W*W+z*E*W+3*a*V+3*d*U)])
 c=phi.subs({z:0,W:0,U:0,V:0,E:0});J=phi.jacobian(Y).subs(z,0);assert J**4==sp.zeros(4)
 Q=sp.eye(4)+J+J**2+J**3;rem=(phi-c-J*Y).applyfunc(sp.expand)
 assert rem.subs(z,0)==sp.zeros(4,1)
 assert all(v>=0 for x in rem for v in sp.Poly(x,z,W,U,V,E).coeffs())
 G=(Q*c+Q*rem).applyfunc(sp.expand)
 fn=sp.lambdify((z,W,U,V,E),G,'mpmath')
 zm=mp.mpf(str(sp.N(z0*R(1001,1000),70))); y=mp.matrix([0,0,0,0])
 for it in range(20000):
  nxt=fn(zm,*y)
  assert max(abs(v) for v in nxt)<mp.mpf('1e100')
  err=max(abs(nxt[i]-y[i])/max(1,abs(nxt[i])) for i in range(4));y=nxt
  if err<mp.mpf('1e-55'):break
 else:raise AssertionError('proposal iteration did not settle')
 # Fixed significant-digit rational proposal. Exact verification below is authoritative.
 yh=sp.Matrix([R(mp.nstr(v,45)) for v in y]);sub=dict(zip([z,*Y],[z0,*yh]));vals=phi.subs(sub)
 margins=yh-vals;assert all(v>0 for v in margins)
 radius_test=R(displayR)**2*z0**3;assert radius_test>1
 rows.append(dict(root_index=index,a=str(a),kappa=str(kap),sigma_lower=str(s),z0=str(z0),Yhat=list(map(str,yh)),Phi_at_Yhat=list(map(str,vals)),positive_margins=list(map(str,margins)),relative_margins=[str(sp.cancel(margins[i]/yh[i])) for i in range(4)],display_radius=displayR,radius_test=str(radius_test),certified_radius_approx=str(sp.N(z0**(-R(3,2)),40)),proposal_iterations=it+1))
res=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
(root/'verification/checks.json').write_text(json.dumps(res,indent=2)+'\n');(root/'sources/checker.py.txt').write_bytes(Path(__file__).read_bytes())
for name in ['majorant_opt.py','majorant_opt.out','sigma_bound_check2.py','sigma_bound_check2.out']:
 p=Path('../a4-lead/code/tuned')/name
 if p.exists():(root/'sources'/name).write_bytes(p.read_bytes())
(root/'sources/response_certificate.json').write_bytes(Path('research/123_tuned_response_minimum/verification/checks.json').read_bytes())
files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
(root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
print(json.dumps(dict(all_checks_pass=True,rows=[dict(root_index=r['root_index'],radius=r['certified_radius_approx'],display_radius=r['display_radius'],iterations=r['proposal_iterations']) for r in rows],actual_elapsed_s=res['actual_elapsed_s'])),flush=True)

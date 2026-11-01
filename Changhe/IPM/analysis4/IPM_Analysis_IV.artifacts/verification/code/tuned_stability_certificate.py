"""Exact majorant box and response-bound arithmetic for topic122."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
import sympy as sp
start=time.monotonic();R=sp.Rational
z,W,U,V,E=sp.symbols('z W U V E')
a=3;kap=14;s=R(1,200000);d=R(3,2)*kap*a*a;e=3*kap*a*d
L=R(3,2);Mb=10*kap**3*L**2
assert Mb==61740
radius_profile=R(1,100000)/(128*Mb)
assert radius_profile==R(1,790272000000)
P=a*z+d*z*z+e*z**3
phi=sp.Matrix([
 R(3,2)*kap*(d*d+2*a*e+2*d*e*z+e*e*z*z)+3*kap*P*W+R(3,2)*kap*z**4*W*W+kap*E*(P+z**4*W),
 R(3,2)*kap*(2*d*e+e*e*z)+3*kap*(a+d*z+e*z*z)*W+R(3,2)*kap*z**3*W*W+kap*z**3*E*W,
 R(3,2)*kap*(e*e+2*(d+e*z)*W+z*z*W*W)+kap*z*z*E*W+3*kap*a*U,
 kap/s*(3*e*W+R(3,2)*z*W*W+z*E*W+3*a*V+3*d*U)])
Y=sp.Matrix([W,U,V,E]);J=phi.jacobian(Y).subs(z,0);c=phi.subs({z:0,W:0,U:0,V:0,E:0})
assert J**4==sp.zeros(4)
Q=sp.eye(4)+J+J**2+J**3;Y0=Q*c
psi=(phi-c-J*Y).applyfunc(lambda x:sp.cancel(x/z))
for p in psi:assert all(c>=0 for c in sp.Poly(p,z,W,U,V,E).coeffs())
M=2**70;z0=R(1,2**160)
bound=Q*psi.subs({z:1,W:2*M,U:2*M,V:2*M,E:2*M})
assert max(Y0)<=M and z0*max(bound)<=M
root=Path('research/122_tuned_compatible_stability')
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_exact_checks_pass=True,a=a,kappa=kap,sigma_lower=str(s),d=str(d),e=str(e),uniform_cubic_bound=str(Mb),profile_radius=str(radius_profile),M=str(M),z0=str(z0),J=[[str(v) for v in J.row(i)] for i in range(4)],Y0=[str(v) for v in Y0],Q_Psi_box_bound=[str(v) for v in bound],maximum_bound_times_z0=str(z0*max(bound)),actual_elapsed_s=time.monotonic()-start)
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'sources/tuned_stability_certificate.py.txt').write_bytes(Path(__file__).read_bytes())
files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
(root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)

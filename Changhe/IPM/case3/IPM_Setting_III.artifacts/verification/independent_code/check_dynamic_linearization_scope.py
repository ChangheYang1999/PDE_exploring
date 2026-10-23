import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib
out=Path('research/dynamic_linearization_scope/verification');proof=out.parent/'PROOF.md'
created=datetime.fromtimestamp(proof.stat().st_mtime,timezone.utc).isoformat()
eps,C,c,ch,rho,h,cw,xd_rho,xd_h,u_drho,u_dh,uh_drho,uh_dh=s.symbols('eps C c ch rho h cw xd_rho xd_h u_drho u_dh uh_drho uh_dh')
f=-(c+eps*ch)/(C-1)*(rho+eps*h-C*(xd_rho+eps*xd_h))-(u_drho+eps*(u_dh+uh_drho)+eps**2*uh_dh)
expected=-c/(C-1)*h+C*c/(C-1)*xd_h-u_dh-uh_drho-ch/(C-1)*(rho-C*xd_rho)
assert s.simplify(s.diff(f,eps).subs(eps,0)-expected)==0
kx,ky,a,b1,b2=s.symbols('kx ky a b1 b2',real=True);den=kx**2+ky**2;psi=s.I*kx/den
assert s.simplify(-s.I*ky*psi-kx*ky/den)==0
assert s.simplify(s.I*kx*psi+kx**2/den)==0
assert s.simplify(-b1*(-s.I*ky*psi)-b2*(s.I*kx*psi)-(b2*kx**2-b1*kx*ky)/den)==0
r,d,t=s.symbols('r d t',positive=True);integ=(s.log(1+r*r)-s.log(1+r*r*s.exp(-2*d*t)))/(2*d)
assert s.simplify(s.diff(integ,t)-r*r*s.exp(-2*d*t)/(1+r*r*s.exp(-2*d*t)))==0
assert integ.subs(t,0)==0
J=s.Matrix([[0,1],[1,0]]);V=s.Matrix([1,0]);lam=(V.T*J*V)[0];assert J*V-lam*V==(s.eye(2)-V*V.T)*J*V
assert J*V-lam*V!=s.zeros(2,1)
J2=s.diag(1,-1);trajectory=s.Matrix([0,s.exp(-t)]);assert s.diff(trajectory,t)==J2*trajectory
L,P,z=s.symbols('L P z',positive=True)
r2=L**2*(1+z)/2*(1-z)**(-2*P);Q=(1-z)/2+P*(1+z)
assert s.simplify(s.diff(r2,z)/2-r2*Q/(1-z*z))==0
record=dict(utc=datetime.now(timezone.utc).isoformat(),initial_proof_written_utc='2026-10-21T07:04:15.962671+00:00',latest_proof_written_utc=created,checks=10,status='PASS',proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),producer_source_sha256=hashlib.sha256(Path('../numerics/src/dr.py').read_bytes()).hexdigest())
(out/'MANIFEST.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))

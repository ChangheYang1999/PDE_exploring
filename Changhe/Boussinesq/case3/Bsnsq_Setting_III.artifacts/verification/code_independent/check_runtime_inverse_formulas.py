"""Symbolic audit of the corrected dummy-variable Green formulas, P291."""
from pathlib import Path
from datetime import datetime,timezone
import time,json,hashlib
import sympy as S
R=Path('research/291_runtime_velocity_norms/verification');t0=time.monotonic();started=datetime.now(timezone.utc).isoformat();checks=[]
def check(n,ok,d=None):checks.append({'name':n,'passed':bool(ok),'detail':d})
def zero(n,v):check(n,S.simplify(v)==0,str(S.simplify(v)))
r,rho=S.symbols('r rho',positive=True);n=S.symbols('n',integer=True,positive=True);H=S.Function('H')
A=S.Integral(rho**(n+1)*H(rho),(rho,0,r));B=S.Integral(rho**(1-n)*H(rho),(rho,r,S.oo));p=(r**(-n)*A+r**n*B)/(2*n)
dp=(-r**(-n-1)*A+r**(n-1)*B)/2
zero('general_green_derivative',S.diff(p,r)-dp)
zero('general_green_poisson',S.diff(p,r,2)+S.diff(p,r)/r-n*n*p/r**2+H(r))
A1=S.Integral(rho**2*H(rho),(rho,0,r));C=S.Integral(H(rho),(rho,0,r));p1=(A1/r-r*C)/2;dp1=(-A1/r**2-C)/2
zero('relative_mode1_derivative',S.diff(p1,r)-dp1)
zero('relative_mode1_poisson',S.diff(p1,r,2)+S.diff(p1,r)/r-p1/r**2+H(r))
x,y=S.symbols('x y',real=True);Psi=S.Function('Psi')(x,y)
zero('stream_curl_sign',S.diff(S.diff(Psi,x),x)-S.diff(-S.diff(Psi,y),y)-S.diff(Psi,x,2)-S.diff(Psi,y,2))
phi=S.symbols('phi',real=True)
zero('polar_unit_radial',S.sin(phi)**2+S.cos(phi)**2-1)
zero('polar_orientation',S.sin(phi)*S.sin(phi)+S.cos(phi)*S.cos(phi)-1)
for k in [1,3,5]:zero('angular_product_'+str(k),S.expand_trig(S.sin(phi)*S.cos(k*phi)-(S.sin((k+1)*phi)-S.sin((k-1)*phi))/2))
b,L,z=S.symbols('b L z',positive=True);rad=L*S.sqrt(z**(-2*b)-1);jac=b*L**2*z**(-2*b-1)/rad;D=z**(b+1)*rad/(L*z**(-b));zero('odd_mode_jacobian_identity',D*jac-b*L)
proof=(R.parent/'PROOF.md').read_text();check('correct_variable_ngreen', 'rho^(n+1)H_n(rho)' in proof and 'rho^(1-n)H_n(rho)' in proof)
check('correct_variable_mode1','rho^2 H_1(rho)' in proof and 'integral_0^r H_1(rho)' in proof)
check('explicit_decay_scope','0<s<1' in proof)
check('initial_typo_preserved','rho^(n+1)H_n(r) d rho' in (R/'PROOF_initial.md').read_text())
check('explicit_runtime_condition','conditional on the reported arrays' in proof)
meta=json.loads((R/'manifest.json').read_text());hashf=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();check('corrected_proof_hash',hashf(R.parent/'PROOF.md')==meta['proof_sha256'])
out={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'passed':sum(c['passed']for c in checks),'total':len(checks),'checks':checks,'code_sha256':hashf(__file__),'corrected_proof_sha256':hashf(R.parent/'PROOF.md'),'scope':'Exact symbolic radial ODE and derivative identities, polar and source-moment formulas; no numerical error enclosure.'}
(R/'formula_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print([c for c in checks if not c['passed']])

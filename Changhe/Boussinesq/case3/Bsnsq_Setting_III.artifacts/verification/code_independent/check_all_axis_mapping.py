"""P278 supplement: low-order identification and endpoint polynomial controls."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as S
V=Path('research/278_all_axis_jets_compact_extension/verification');start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();C=[]
def check(n,b,detail=None):C.append(dict(name=n,passed=bool(b),detail=detail))
def zero(n,e):check(n,S.simplify(e)==0,str(S.simplify(e)))
beta,A,tau=S.symbols('beta A tau',positive=True);x,y,c0=S.symbols('x y c0',real=True);d=(3*beta+2)/2
b,a1,a2,v1,q0=[S.Function(n)(y)for n in ['b','a1','a2','v1','q0']]
T=2*a1;D=24*a2
rT2=b*S.diff(a2,y)+(7*beta+2-4*S.diff(b,y))*a2-S.Rational(2,3)*S.diff(v1,y)*a1+v1*S.diff(a1,y)
lowD=b*S.diff(D,y)+(7*beta+2-4*S.diff(b,y))*D-8*S.diff(v1,y)*T+12*v1*S.diff(T,y)
zero('D_equals_24a2_identity',lowD-24*rT2)
zero('thermal_secondjet_equation',(b*S.diff(T,y)+(3*beta+2-2*S.diff(b,y))*T)-2*(b*S.diff(a1,y)+(3*beta+2-2*S.diff(b,y))*a1))
zero('q0_equation_is_eta',b*S.diff(q0,y)+(2*beta+1-S.diff(b,y))*q0-2*a1-(b*S.diff(q0,y)+(2*beta+1-S.diff(b,y))*q0-T))
zero('center_a0_equals_A_half',S.diff(A*x*x/2,x,2)-A)
zero('D_normalization',S.diff(D*x**4/24,x,4)-D)
zero('local_center_thermal',(beta-2)*x/2*S.diff(A*x*x/2,x)-(beta-2)*A*x*x/2)
zero('local_center_vorticity',(beta-2)*x/2*(2*A/beta)+2*A*x/beta-A*x)
for sign in [1,-1]:
 by=sign/tau**2;dy=lambda f:sign*tau**2*S.diff(f,tau);theta=tau**-4*S.exp(-2*d*tau);vv=-sign
 zero('endpoint_transport_'+str(sign),by*sign*tau**2-1)
 zero('endpoint_bprime_'+str(sign),dy(by)+2/tau)
 zero('endpoint_bsecond_'+str(sign),dy(dy(by))-2*sign)
 zero('endpoint_forcing_'+str(sign),(8*dy(vv)*theta-12*vv*dy(theta))/theta+24*d*tau**2+48*tau)
 zero('theta_logderivative_'+str(sign),S.diff(theta,tau)/theta+4/tau+2*d)
zero('K_coefficient_constant',7*beta+2-2*d-4*beta)
k2=-6*d/beta;k1=(-48-6*k2)/(4*beta);k0=-5*k1/(4*beta);poly=k2*tau**2+k1*tau+k0
zero('endpoint_polynomial_residual',S.diff(poly,tau)+(4*beta+4/tau)*poly+24*d*tau**2+48*tau-4*k0/tau)
for bv in [2,S.Rational(31,10),4,20]:check('negative_leading_coefficient_'+str(bv),k2.subs(beta,bv)<0)
zero('beta2_polynomial',poly.subs(beta,2)-(-12*tau**2+3*tau-S.Rational(15,8)))
# The explicit beta2 constant is -15/8, as in the informal derivation.
q=json.loads((V/'mapping_proof_before_checks.json').read_text());check('proof_unchanged',hashlib.sha256((V/'MAPPING_PROOF.md').read_bytes()).hexdigest()==q['sha256'])
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(c['passed']for c in C),total=len(C),checks=C,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=q['sha256'],scope='Finite exact supplement to full informal mapping proof; no new B2 endpoint.')
(V/'mapping_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds']);print([c for c in C if not c['passed']])

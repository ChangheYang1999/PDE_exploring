"""Exact polynomial certificates only; proof is in ../PROOF.md."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time
import sympy as s
start=time.monotonic()
root=Path(__file__).resolve().parents[1]
M,u=s.symbols('M u', real=True)
def q(m): return m**4+10*m**2+5+(2*m**2+6)*u+u**2
certificates={
 'down':s.expand(q(M)-q(M-2)-4*(M-1)*(M**2+(M-2)**2+10+2*u)),
 'one_three':s.expand(11*q(1)-q(3)-64*u-10*u**2),
 'up':s.expand(5*q(M)-q(M+2)-4*(M-3)*(M**3+M**2+7*M+3)-(8*M**2-8*M+16)*u-4*u**2),
}
assert all(x==0 for x in certificates.values())
l,k=s.symbols('lambda kappa',positive=True)
A=12+l+11/k
B=8+l+1/l+k+5/k
old=[x.subs({l:1,k:4}) for x in (A,B)]
new=[x.subs({l:s.Rational(2,3),k:4}) for x in (A,B)]
assert old==[s.Rational(63,4),s.Rational(61,4)]
assert new==[s.Rational(185,12)]*2
C=s.Rational(185,96)
assert 1<s.Rational(5,3)<C<s.Rational(63,32)<2
assert (5*q(1)+q(3)).subs(u,0)/(8*q(1).subs(u,0))==2
assert (q(0)+q(2)).subs(u,0)/(4*q(0).subs(u,0))==s.Rational(33,10)
assert s.Rational(33,10)>(7+2*s.sqrt(6))/4
out={'utc':datetime.now(timezone.utc).isoformat(), 'seconds':time.monotonic()-start,
     'polynomial_identities':{k:str(v) for k,v in certificates.items()},
     'young_old':[str(x) for x in old], 'young_balanced':[str(x) for x in new],
     'squared_constant':str(C),'old_squared_constant':'63/32',
     'parity_counterexamples':{'cosine_limit':'2','radial_limit':'33/10'},
     'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'verification/result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

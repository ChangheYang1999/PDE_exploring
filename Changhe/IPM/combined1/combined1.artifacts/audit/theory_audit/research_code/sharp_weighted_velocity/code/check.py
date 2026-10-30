from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
import sympy as s
start=time.monotonic();base=Path(__file__).resolve().parents[1]
n,a,p,k=s.symbols('n a p k',real=True)
# q stands for Re integral H' conjugate(H), which vanishes.
# The coefficients below multiply integral |H'|^2, Re(H' Hbar), |H|^2 pointwise.
F=s.Matrix([1,-2*(n-p),(n-p)**2]);G=s.Matrix([1,2*(n+p),(n+p)**2])
D=s.Matrix([1,-2*(a-p),(a-p)**2]);Kn=(n+a)/(n-a)
rhs=4*n*a/(n-a)**2*(D+s.Matrix([0,0,(n*n-a*a)*(a-p)/a]))
diff=(Kn**2*F-G-rhs).applyfunc(s.factor)
# An exact derivative cross term is allowed; its constant coefficient integrates to zero.
assert diff[0]==0 and diff[2]==0 and not diff[1].has(p)
Fp=s.Matrix([1,2*(k+p),(k+p)**2]);Gp=s.Matrix([1,-2*(k-p),(k-p)**2])
bdiff=(Fp-Gp-s.Matrix([0,0,4*k*p])).applyfunc(s.factor)
assert bdiff==s.Matrix([0,4*k,0])
record={'utc':datetime.now(timezone.utc).isoformat(),
        'proof_sha256':sha256((base/'PROOF.md').read_bytes()).hexdigest(),
        'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'forward_identity_difference_coefficients':[str(x) for x in diff],
        'backward_identity_difference_coefficients':[str(x) for x in bdiff],
        'all_identity_checks_pass':True,
        'velocity_constants':{'a=6/5':str(2/(2-s.Rational(6,5))),'a=7/5':str(2/(2-s.Rational(7,5)))},
        'elapsed_seconds':time.monotonic()-start}
(base/'verification/identities.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

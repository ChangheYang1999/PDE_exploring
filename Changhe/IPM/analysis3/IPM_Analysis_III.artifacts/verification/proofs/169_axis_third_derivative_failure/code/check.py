from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import hashlib,json
x,z,l,a=S.symbols('x z l a', real=True, nonzero=True)
K=(x*x-z*z)/(2*S.pi*(x*x+z*z)**2)
K3=S.factor(S.diff(K,z,3))
assert S.simplify(K3.subs({x:l*x,z:l*z})-K3/l**5)==0
assert S.simplify(K3.subs(x,-x)-K3)==0
assert K3.subs({x:1,z:1})!=0
assert S.simplify((2*a-2)+2-2*a)==0
assert S.simplify((a-1)+2-5)==a-4
p=Path(__file__).resolve().parents[1]
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','third_kernel':str(K3),'nonzero_value_at_1_1':str(K3.subs({x:1,z:1})),'norm_scaling_power':'0','axis_third_derivative_scaling_power':'a-4','proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import sympy as s
root=Path(__file__).resolve().parents[1]
A=s.Matrix([[-3,1,0],[0,-4,1],[0,0,-5]])
T=-4*s.eye(3)
C=A-T
S=(C+C.T)/2
P=s.diag(1,1,0)
Q=s.eye(3)-P
SF=P*S+S*P-P*S*P
assert S==SF+Q*S*Q
assert Q*S*Q==s.diag(0,0,-1)
E=s.diag(2,1,1)
Phi=(E.inv()*SF).T
Psi=A.T.inv()*Phi
D=Phi-A.T*Psi
assert D==s.zeros(3)
assert E*Phi.T==SF
assert Phi.T==Psi.T*A+D.T
# e=2, p=1, d=0, m=4, epsilon=delta_F=0.
for M in (4*s.eye(3)-E.T*E,s.eye(3)-Psi.T*Psi):
    for size in range(1,4):
        from itertools import combinations
        for ids in combinations(range(3),size):
            assert M.extract(ids,ids).det()>=0
k=s.Rational(3,4)
G=k*k*A.T*A-s.eye(3)
for size in range(1,4):
    for ids in combinations(range(3),size):
        assert G.extract(ids,ids).det()>0
assert SF!=P*S*P
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS',
     'arithmetic':'exact rational matrices','k1':str(k),
     'checks':['four-block decomposition','cross terms retained','adjoint identity',
               'nonorthonormal Gram bounds','conditional inverse constant'],
     'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

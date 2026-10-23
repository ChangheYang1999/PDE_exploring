"""Small exact arithmetic supporting the independent frozen appendix audit."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
checks=[]
def record(label,condition,**evidence):
    assert condition,label
    checks.append(dict(test=label,passed=True,**evidence))
m=F(11,3)
b=[(m*m+4*j*j)/(4*abs(4*j*j-m*m))for j in [1,2,3]]
record('Jacobi row coefficients',b==[F(157,340),F(265,92),F(445,812)],values=list(map(str,b)))
B=F(1,2)+b[1]+max(b[0],b[2]);record('infinite row bound',B==F(18342,4669),value=str(B))
k=B-(m-1);eps=F(1,5)/k
record('explicit near-one endpoint',eps==F(14007,88370)and eps>F(158,1000),value=str(eps))
# Entire polynomial identity, not a finite-N sample.
left=[-37*4-12*5,-12*4,37-12]
right=[-4*52,52-4*25,25]
record('all-N Hessian factorization',left==right,ascending_coefficients=left,factors=['N-4','25N+52'],domain='N>=4')
total=F(5,2)+F(49,8)+F(37,16)
record('all-radius slow constant',total==F(175,16)and total<11,value=str(total))
record('sqrt2 over3 is above47/100',2>9*F(47,100)**2,gap=str(2-9*F(47,100)**2))
record('final strict endpoint comparison',F(47,1100)>F(1,24),gap=str(F(47,1100)-F(1,24)))
# A primitive of sin(theta)sin(3theta) has coefficients of sqrt3 below
# at 0,pi/3,2pi/3,4pi/3,5pi/3,2pi. The sign is constant per interval.
v=[F(0),F(3,16),F(-3,16),F(3,16),F(-3,16),F(0)]
a=sum(abs(x-y)for x,y in zip(v,v[1:]))
record('absolute angular cancellation integral',a==F(3,2),coefficient_of_sqrt3=str(a))
source=Path('evidence/lead_merge_audit/APPENDIX_347_348_20261020T2240Z.md')
r=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',frozen_source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact arithmetic supporting the hand audit; it does not replace the analytic proofs.')
Path('evidence/lead_merge_audit/APPENDIX_347_349_CONSTANTS.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r),flush=True)

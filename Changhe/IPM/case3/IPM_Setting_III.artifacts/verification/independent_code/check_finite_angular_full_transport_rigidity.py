"""Independent exact algebra supporting result93; no producer imports."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, random

rng = random.Random(930021)
checks = []
def eq(label, lhs, rhs):
    assert lhs == rhs, (label, lhs, rhs)
    checks.append(label)
def coeff_sincos(a, b, target):
    out = F(0)
    for k in (a+b, a-b):
        if abs(k) == target:
            out += F(1 if k > 0 else -1, 2)
    return out

for m in (1,3,5,7,9,15,31):
    for trial in range(9):
        r=F(rng.randint(1,11),rng.randint(1,9))
        jets={j:tuple(F(rng.randint(-11,11),rng.randint(1,9)) for _ in range(2)) for j in range(1,m+1,2)}
        streams={k:tuple(F(rng.randint(-11,11),rng.randint(1,9)) for _ in range(2)) for k in range(2,m+2,2)}
        total=F(0)
        for j,(b,bp) in jets.items():
            for k,(p,pp) in streams.items():
                total += -k*p*bp/r*coeff_sincos(j,k,2*m+1)
                total += j*b*pp/r*coeff_sincos(k,j,2*m+1)
        b,bp=jets[m];p,pp=streams[m+1]
        eq(f'top harmonic m={m} trial={trial}',total,(m*b*pp-(m+1)*p*bp)/(2*r))
        J,Jp,Jpp=[F(rng.randint(-11,11),rng.randint(1,9)) for _ in range(3)]
        p=-J/(2*r**(m+1))
        pp=-(Jp-(m+1)*J/r)/(2*r**(m+1))
        b=Jp/r**(m+1)
        bp=(Jpp-(m+1)*Jp/r)/r**(m+1)
        E=(m+1)*J*Jpp-m*Jp**2-(m+1)*J*Jp/r
        eq(f'modal to J ODE m={m} trial={trial}',(m*b*pp-(m+1)*p*bp)/(2*r),E/(4*r**(2*m+3)))
        z=F(rng.randint(1,9),rng.randint(1,7));zp=F(rng.randint(-9,9),7);zpp=F(rng.randint(-9,9),5)
        sign=(-1)**trial
        J=sign*z**(m+1);Jp=sign*(m+1)*z**m*zp
        Jpp=sign*(m+1)*(m*z**(m-1)*zp*zp+z**m*zpp)
        E=(m+1)*J*Jpp-m*Jp**2-(m+1)*J*Jp/r
        eq(f'component substitution m={m} trial={trial}',E,(m+1)**2*z**(2*m+1)*(zpp-zp/r))
        A=F(rng.randint(1,7),5);B=F(rng.randint(1,7),3)
        z=A*r*r+B;zp=2*A*r;zpp=2*A
        J=z**(m+1);Jp=(m+1)*z**m*zp
        Jpp=(m+1)*(m*z**(m-1)*zp*zp+z**m*zpp)
        eq(f'explicit local branch m={m} trial={trial}',(m+1)*J*Jpp-m*Jp**2-(m+1)*J*Jp/r,F(0))
        # Independently differentiate P twice and check its source.
        b=Jp/r**(m+1);bp=(Jpp-(m+1)*Jp/r)/r**(m+1)
        p=-J/(2*r**(m+1))
        pp=-Jp/(2*r**(m+1))+(m+1)*J/(2*r**(m+2))
        ppp=-Jpp/(2*r**(m+1))+(m+1)*Jp/r**(m+2)-(m+1)*(m+2)*J/(2*r**(m+3))
        eq(f'Poisson top mode m={m} trial={trial}',-(ppp+pp/r-(m+1)**2*p/r**2),(bp-m*b/r)/2)

root=Path('research/finite_angular_full_transport_rigidity')
record={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','checks':len(checks),'items':checks,
        'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact rational algebra; component, boundary, canonical uniqueness proof audited in PROOF.md, not a numerical theorem.'}
(root/'verification/exact_checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='items'}))

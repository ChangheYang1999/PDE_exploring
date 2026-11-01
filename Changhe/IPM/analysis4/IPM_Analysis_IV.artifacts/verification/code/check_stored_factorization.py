from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
from math import gcd,isqrt,prod
import json,time
root=Path('research/193_stored_denominator_factorization');start=time.monotonic()
source=Path('../a4-num/notes/cand007_f1.json');data=json.loads(source.read_text())
c=Fraction(data['c_l_exact']);delta=1-1/c;A,D=delta.numerator,delta.denominator
assert (A,D)==(1824676646553933,4076476460239181)
factors=[127,114599,280091797];assert prod(factors)==D
numerator_factors=[3,883,5737,6133,19577];assert prod(numerator_factors)==A
trials=[]
for side,primes in [('denominator',factors),('numerator',numerator_factors)]:
    for p in primes:
        limit=isqrt(p);tested=list(range(2,limit+1));assert all(p%d for d in tested)
        trials.append(dict(side=side,prime=p,square_root_floor=limit,trial_divisors=len(tested)))
assert gcd(A,2*D)==1 and A%2==1 and 2*D==8152952920478362
assert all((D*(2*j+2)-127*A)%127==0 and (D*(2*j-2)+127*A)%127==0 for j in range(20))
assert (D-A)%127 and Fraction(127*A,D-A).numerator%127==0
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,c=str(c),delta=str(delta),factors=factors,numerator_factors=numerator_factors,primality_checks=trials,gcd_A_2D=gcd(A,2*D),first_resonance=2*D,source=dict(path=str(source),sha256=sha256(source.read_bytes()).hexdigest()),scope='Exact factorization and failure of direct TheoremP hypotheses only; stored first compatibility remains OPEN.',actual_elapsed_s=time.monotonic()-start)
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n');(root/'sources/check_stored_factorization.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result))

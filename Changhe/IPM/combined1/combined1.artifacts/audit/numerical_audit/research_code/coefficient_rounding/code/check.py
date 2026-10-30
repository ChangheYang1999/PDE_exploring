from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from hashlib import sha256
from flint import arb,ctx
import json
ctx.prec=2048
root=Path(__file__).resolve().parents[1]
target=Path('RUN_ROOT/numerics_N3/certification/hminus1.py')
x_exact=10**300+10**80;x=arb(x_exact)
assert x.is_exact()
B=400
s=x.mid().str(200,radius=False)
q_decimal=Fraction(round(Fraction(s)*2**B),2**B)
mid=x.mid().fmpq();q_mid=Fraction(int(mid.numerator),int(mid.denominator))
q_exact=Fraction(round(q_mid*2**B),2**B)
assert q_exact==x_exact
err=abs(q_decimal-x_exact)
assert err==10**80
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
     'test_integer':'10^300+10^80','fixed_significant_digits':200,'dyadic_fractional_bits':B,
     'fixed_decimal_absolute_error':str(err),'exact_midpoint_absolute_error':'0',
     'claimed_dyadic_error_limit':str(Fraction(1,2**(B+1))),
     'fixed_decimal_violates_limit':bool(err>Fraction(1,2**(B+1))),
     'target_sha256':sha256(target.read_bytes()).hexdigest(),
     'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Reproduces a coefficient-conversion accuracy defect; causal role in actual d2 solve remains untested.'}
(root/'source/N3_hminus1.py.txt').write_bytes(target.read_bytes())
(root/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

"""Exact monomial witnesses for the deficit-only norm obstruction."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
from math import comb,factorial
import json,time
start=time.monotonic();rows=[]
for m in range(1,101):
 h=m-1
 coefficient=Fraction(1,factorial(h)**2)
 ratio=factorial(2*h)*coefficient
 assert ratio==comb(2*h,h)
 assert ratio>=Fraction(4**h,2*h+1)
 rows.append(dict(m=m,central_binomial=str(ratio),row_sum=str(4**h),lower_bound=str(Fraction(4**h,2*h+1))))
root=Path('research/70_deficit_weight_obstruction')
(root/'verification/checks.json').write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),all_passed=True,witness_count=len(rows),rows=rows,actual_elapsed_s=time.monotonic()-start,code_sha256=sha256(Path(__file__).read_bytes()).hexdigest()),indent=2)+'\n')
(root/'sources/deficit_weight_obstruction.py.txt').write_bytes(Path(__file__).read_bytes())
print('100 exact monomial witnesses and binomial lower bounds passed.')

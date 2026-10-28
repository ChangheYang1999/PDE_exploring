"""Evaluate the proved axis-local saving. No optimization or LP is run."""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from flint import arb, ctx
ctx.prec = 256
root=Path(__file__).resolve().parents[1]
out=root/'08_improved_upper_bounds/local_functional_audit/quantitative_gap/verification/values.json'
def enc(x):
    return {'display':str(x), 'lower':str(x.lower().fmpq()), 'upper':str(x.upper().fmpq())}
c=(arb(10)/9).log()*(arb(1)/10).sin()/arb.pi()
rows=[]
for a in [Fraction(1,100),Fraction(3,10),Fraction(1,2),Fraction(3,4)]:
    aa=arb(a.numerator)/a.denominator
    eta=c*((arb(3)/5)**aa-(arb(11)/20)**aa)
    assert eta>0
    rows.append({'alpha':str(a),'eta':enc(eta)})
proof=root/'08_improved_upper_bounds/local_functional_audit/quantitative_gap/PROOF.md'
assert Fraction(963171,1600000)>Fraction(3,5)
data={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'scope':'Evaluations of an analytically proved saving only. Independent lead cross-read pending.','sha256':{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),proof]}}
out.write_text(json.dumps(data,indent=2)+'\n')
for row in rows: print(row['alpha'],row['eta']['display'])
print(data['timestamp_utc'])

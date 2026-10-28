from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ctx.prec=384
assert Q(6,5)**10<8
assert 5**3<3**5 and 5<2**10
assert 507+40+1==548
assert Q(548*6,3)<2**11
assert (arb(548*6)*(arb(2)/arb.pi()).sqrt())<2**12
assert 507*4+40*2+3==2111
assert 2<Q(5,4)**5
assert Q(3*2111*5,4)<2**13
assert 2*2**11+arb(2).sqrt()<2**14
assert 10<4*arb.pi()
root=Path(__file__).resolve().parents[1]
data={"status":"ARITHMETIC_PASS", "time_utc":datetime.now(timezone.utc).isoformat(),
      "constants":{"gradient":2**11,"gradient_holder":2**12,"growth":2**13,"product":2**14},
      "holder_coefficient_upper":str(arb(548*6)*(arb(2)/arb.pi()).sqrt()),
      "proof_sha256":hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
      "code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      "scope":"Arithmetic verification accompanying the separate analytical proof audit."}
(root/'verification/constants.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))

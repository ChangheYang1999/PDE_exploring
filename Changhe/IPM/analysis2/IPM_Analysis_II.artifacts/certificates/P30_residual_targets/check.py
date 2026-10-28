from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
import json
H=Path(__file__).resolve().parent;B=H.parents[1]
s=Q(3,2**31);eta=Q(1,2**35)
assert 0<s<=Q(1,2**12)
assert 36<128
assert 16*eta==Q(1,2**31)
# Squared comparison, with only positive quantities.
assert Q(36,2**123)<Q(1,2**116)
files=[H.parent/'PROOF.md',B/'18_fractional_constants/PROOF.md',B/'16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md',B/'20_real_velocity/PROOF.md',B/'24_weaker_matrix/PROOF.md']
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED exact residual target corollary','s':str(s),'eta':str(eta),'low_target':'6*2^(-123/2) < 2^(-58)','point_target':'2^(-31)*max(1,r^(1/5))','dependencies':{str(p.relative_to(B)):sha256(p.read_bytes()).hexdigest() for p in files},'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
H.joinpath('check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

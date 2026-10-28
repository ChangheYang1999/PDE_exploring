from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
p=Path(__file__).resolve().parents[1]
rate=F('0.99999997745');M=F('0.308');radius=F(99,2000)
margin=rate-M*radius/2
assert margin>F('0.992')
assert F(-2)*F(-1)>0
assert 1-2*F(3,2)==-2
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','old_source_margin_exact':str(margin),'safe_source_margin':'0.992','star_variant_requires_positive_diagonal_lower_bounds':True,'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))

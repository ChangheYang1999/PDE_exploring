"""Exact counterexamples; no imported production code is executed."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
old=[(F(0),F(1)),(F(1),F(2)),(F(2),F(3))];new=[old[0],old[2]]
lo=min(a for a,b in new);hi=max(b for a,b in new)
replaced=[(a,b) for a,b in old if a>=lo and b<=hi]
assert min(a for a,b in replaced)==lo and max(b for a,b in replaced)==hi
witness=F(3,2);assert not any(a<=witness<=b for a,b in new)
assert min([10,10])>-100
row=[F(10),None];assert any(x is not None for x in row)
assert min(x for x in row if x is not None)>-100
files={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'evidence').glob('*.py')}
out={'date':datetime.now(timezone.utc).isoformat(),'status':'COUNTEREXAMPLES_CONFIRMED','radial_gap_witness':str(witness),'endpoint_assertion':'PASSES_WITH_GAP','angular_selection':'PASSES_WITH_GAP','reported_bound':10,'actual_infimum':-100,'source_sha256':files,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest()}
(ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

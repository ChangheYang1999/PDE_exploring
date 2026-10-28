from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1]
p=R/'08_improved_upper_bounds/local_projection/strict_increment/larger_disks/enlarged_exact_disks'
c=Q(1487,2000);a=1-c;d=Q(3,4)-c
A=Q(1,162)-Q(22,27)*d;B=Q(2,27)+Q(8,3)*d;C=Q(8,3)-Q(17,3)*d
assert C>0 and 4*A*C-B*B>0 and 2*a<c and 2*a*a<c*c
v=p/'verification';v.mkdir(exist_ok=True)
record=dict(time_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED arithmetic only; analytic review pending',c=str(c),a=str(a),d=str(d),A=str(A),B=str(B),C=str(C),discriminant_margin=str(4*A*C-B*B),quadratic_minimum=str(A-B*B/(4*C)),s_max=str(1/(2*a)),sha256={str(x.relative_to(R)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [p/'PROOF.md',Path(__file__)]})
(v/'rational_checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

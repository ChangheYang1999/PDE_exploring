from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json
root=Path('research/192_supremum_proof_qualifications')
theory=Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md')
s=theory.read_text();start=s.index('Since even $\\sum_kx_');end=s.index('In the primary normalization',start)
(root/'sources/lead_v35_excerpt.md').write_text(s[start:end]+'\n')
m,Q,t=F(10),F(5),F(1,2)
ratios=[t*(m+Q*k)/(m+Q*(k+1)) for k in [0,1]]
assert ratios==[F(1,3),F(3,8)] and ratios[0]<ratios[1]<1
own=Path('research/187_sharp_prefix_tail_bounds/PROOF.md');old=own.read_text()
old=old.replace('This uses only rational comparisons and always terminates. The supremum is therefore an attained rational maximum.','This uses comparisons and always terminates. When m, Q and t are rational, all comparisons are exact rational comparisons and the attained maximum is rational; no rationality is asserted for arbitrary real t.')
own.write_text(old)
d=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,source_sha256=sha256(theory.read_bytes()).hexdigest(),d0_ratios=list(map(str,ratios)),d1_ratio='1/2',irrational_example=dict(m=10,Q=5,K=1,d=0,t='sqrt(2)/2',maximum='sqrt(2)/30'),scope='Corrects proof wording only; exact rational examples and tail inequalities are unchanged.')
(root/'verification/checks.json').write_text(json.dumps(d,indent=2)+'\n')
(root/'sources/check_supremum_qualifications.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(d))

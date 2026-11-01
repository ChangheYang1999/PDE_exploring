"""Check the support-rule example without dividing at its first resonance."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
from hashlib import sha256
import json
from rational_scan_audit import compute
result=compute(Fraction(4,9),{11:'1'},9)
assert result['kappa_exact']=='0' and result['forcing_exact']=='0'
assert min(map(int,result['density_at_resonance']))>=3
result.update(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
              code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),leading_density={'11':'1'},
              scope='Compatibility of the first stream resonance only; no all-order continuation claimed.')
Path('research/25_unpopulated_resonance/verification/sin11_delta4_9.json').write_text(json.dumps(result,indent=2)+'\n')
print('First resonance exactly compatible; smallest populated positive density frequency:',min(map(int,result['density_at_resonance'])),flush=True)

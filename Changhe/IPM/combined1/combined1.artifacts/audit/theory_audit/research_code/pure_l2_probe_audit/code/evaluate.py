from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import time
from flint import arb, ctx

base = Path(__file__).resolve().parents[1]
ctx.prec = 512
start = time.monotonic()
src = base / 'source/T4_weak_integrals.json'
rec = json.loads(src.read_text())['probes'][0]
assert rec['p'] == 2
I = abs(arb(rec['pairing']))
A, B, C = (arb(rec[key]) for key in ('A', 'B', 'C'))
r = arb(27) / 10000
rows = []
for coefficient in (5, 3):
    D = A + coefficient * B + C
    root = 2 * I / (D + (D*D + 4*I).sqrt())
    gap = I - D*r - r*r
    assert gap > 0
    rows.append({'B_coefficient': coefficient, 'D': D.str(90),
                 'necessary_L2_radius': root.str(90),
                 'radius_test': '27/10000', 'gap': gap.str(90),
                 'closed_ball_excluded': bool(gap > 0)})
output = {'utc': datetime.now(timezone.utc).isoformat(), 'precision_bits': ctx.prec,
          'source_sha256': sha256(src.read_bytes()).hexdigest(),
          'code_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
          'proof_sha256': sha256((base / 'PROOF.md').read_bytes()).hexdigest(),
          'I': I.str(90), 'rows': rows, 'elapsed_seconds': time.monotonic()-start}
(base / 'verification/d2_512.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))

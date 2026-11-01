"""A three-state interval compatibility check for the current numerics source."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import importlib.util
import json
import sys
sys.dont_write_bytecode = True
from flint import arb, fmpq

src = Path('../a4-num/code/ffcore.py')
blob = src.read_bytes()
digest = sha256(blob).hexdigest()
snapshot = Path('research/19_interval_resonance/sources') / ('ffcore_' + digest + '.py')
snapshot.write_bytes(blob)
spec = importlib.util.spec_from_file_location('audited_ffcore', snapshot)
ff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ff)
R = ff.RingArb(256)
obj = ff.FarField(R, '2', ['1'])
assert obj.delta_exact == fmpq(1, 2)
rows = []
for label, a0 in [('exact_zero', arb(0)), ('ambiguous_zero', arb(0, '1e-30')), ('nonzero', arb(1))]:
    _, stats = obj.poisson([a0], 8)
    record = stats['resonances'][0]
    num = -4 * a0
    correct = 'COMPATIBLE' if num.is_zero() else ('OPEN' if num.contains(0) else 'INCOMPATIBLE')
    source = 'COMPATIBLE' if record['num_zero'] else 'INCOMPATIBLE'
    rows.append(dict(label=label, a0=str(a0), numerator=str(num),
                     source_decision=source, justified_decision=correct,
                     source_record=record, mismatch=(source != correct)))
assert rows[1]['mismatch'] and not rows[0]['mismatch'] and not rows[2]['mismatch']
out = dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
           source=str(src), source_sha256=digest, source_snapshot=str(snapshot),
           precision_bits=256, delta='1/2', n=8, resonant_j=1, tests=rows,
           scope='Unit audit of interval classification, not a claim that an observed nonzero exact compatibility coefficient vanishes.')
Path('research/19_interval_resonance/verification/three_state_check.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'source_sha256': digest, 'checks': len(rows), 'misclassified': [r['label'] for r in rows if r['mismatch']]}))

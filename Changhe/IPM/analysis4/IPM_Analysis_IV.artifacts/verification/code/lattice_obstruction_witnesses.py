"""Replay exact retained witnesses for the generic harmonic-lattice obstruction."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
from datetime import datetime, timezone
import json, time
ROOT=Path('research/203_generic_lattice_obstruction')
start=time.monotonic()
rows=[]
for M in [17,19]:
    path=Path(f'research/36_free_multipole_compatibility/verification/sin{M}.json')
    raw=path.read_bytes()
    d=json.loads(raw)
    (ROOT/'sources'/path.name).write_bytes(raw)
    r=Fraction(d['kappa_at_beta0'])
    s=Fraction(d['slope_exact'])
    assert r and not s
    assert Fraction(d['kappa_at_beta1'])==r
    assert d['obstructed_for_all_beta']
    rows.append(dict(M=M,source=str(path),source_sha256=sha256(raw).hexdigest(),
                     constant_exact=str(r),response_exact=str(s),constant_approx=float(r)))
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
result=dict(checked_at_utc=now,all_checks_pass=True,
            method='Exact rational replay of retained witnesses; no new recurrence claimed.',
            rows=rows,actual_elapsed_s=time.monotonic()-start)
(ROOT/'verification/witness_checks.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'sources/lattice_obstruction_witnesses.py').write_bytes(Path(__file__).read_bytes())
manifest=dict(checked_at_utc=now,files={str(p.relative_to(ROOT)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest())
    for p in ROOT.rglob('*') if p.is_file() and p.name!='MANIFEST.json'})
(ROOT/'verification/MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(checked_at_utc=now,all_checks_pass=True,
    approximate_witnesses=[dict(M=r['M'],value=r['constant_approx']) for r in rows],
    actual_elapsed_s=result['actual_elapsed_s'])))

"""Preserve the only still-growing proof referenced by V635."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
b=Path('research/301_final_claim_audit');a=b/'verification/admission_V635.json';d=json.loads(a.read_text());r=next(x for x in d['checked_proofs'] if x['topic']==303)
p=Path(r['path']);raw=p.read_bytes();assert sha256(raw).hexdigest()==r['sha256']
q=b/'sources/proof303_at_V635.md';assert not q.exists();q.write_bytes(raw)
out=dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),scope='Historical proof bytes preserved without editing the original admission.',bindings=[dict(admission=str(a),original_path=r['path'],sha256=r['sha256'],snapshot=str(q))])
(b/'verification/historical_reading_bindings.json').write_text(json.dumps(out,indent=2)+'\n');print(out['at'],q)

"""Exact raw-nodal to serialized-mean integrity; no certificate mutation."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
import numpy as np
manifest=Path('research/regularity/verification/EARLY_INPUT_MANIFEST.json');d=json.loads(manifest.read_text());rows=[]
for r in d['inputs']:
    p=Path(r['input']);source=Path(r['source'])
    assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
    assert hashlib.sha256(source.read_bytes()).hexdigest()==r['source_sha256']
    inp=json.loads(p.read_text());raw=np.load(source,allow_pickle=False)
    assert int(raw['N'])==inp['N']and int(raw['M'])==inp['M']
    assert float(raw['p']).hex()==inp['map_power_hex']and float(raw['L']).hex()==inp['length_hex']
    for rr,(num,den)in zip(raw['b'],inp['mean_radial_values'],strict=True):
        assert sum((F(float(v))for v in rr),F(0))/inp['M']==F(int(num),int(den))
    rows.append(dict(input=r['input'],radial_means_checked=len(inp['mean_radial_values'])))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',manifest_sha256=hashlib.sha256(manifest.read_bytes()).hexdigest(),rows=rows,scope='Exact source data integrity only; original Arb interval certificate is retained unchanged.')
Path('research/regularity/verification/early_input_integrity.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)

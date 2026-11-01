"""Reproduce the improved Q4 dyadic boxes with the independent majorant."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from hashlib import sha256
import json, time, sys
sys.dont_write_bytecode = True
from general_component_radius import Majorant, stringify
start = time.monotonic()
root = Path('research/143_period_four_response_bounds')
old = json.loads((root/'verification/checks.json').read_text())
rows = []
for row, q in zip(old['rows'], [40,47,49,48,46,46]):
    a, s = F(row['a']), F(row['sharper_lower'])
    assert F(row['infimum_interval'][0]) > s
    m = Majorant(4, a, F(20), s)
    box = [2*v for v in m.Y0]
    z = F(1, 2**q)
    value = m.transformed(z, box)
    margins = [b-v for b,v in zip(box,value)]
    assert all(v > 0 for v in margins)
    earlier = m.transformed(2*z,box)
    assert any(v > b for v,b in zip(earlier,box))
    out = dict(root_index=row['root_index'],a=a,s=s,z0=z,z_power=q,radius_power=2*q,
               constant=m.constant,J=m.J,T=m.T,Y0=m.Y0,box=box,map_on_box=value,
               margins=margins,maximum_ratio=max(v/b for v,b in zip(value,box)),
               previous_dyadic_map=earlier,previous_dyadic_fails=True)
    rows.append(out)
    print(json.dumps(dict(root=row['root_index'],q=q,maximum_ratio=float(out['maximum_ratio']))),flush=True)
m = Majorant(4,F(163,100),F(20),F(43,1000000))
box=[2*v for v in m.Y0];z=F(1,2**52);value=m.transformed(z,box)
assert all(v<b for v,b in zip(value,box))
assert any(v>b for v,b in zip(m.transformed(2*z,box),box))
common=dict(a=m.a,s=m.lower,z0=z,z_power=52,radius_power=104,Y0=m.Y0,box=box,map_on_box=value,
            maximum_ratio=max(v/b for v,b in zip(value,box)))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
            rows=rows,common=common,actual_elapsed_s=time.monotonic()-start)
(root/'verification/sharper_dyadic_radii.json').write_text(json.dumps(stringify(result),indent=2)+'\n')
(root/'sources/period_four_sharper_radii.py').write_bytes(Path(__file__).read_bytes())
files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest())
       for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
(root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)

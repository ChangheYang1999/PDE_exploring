"""Freeze and check all exact radius-table entries against admitted metadata."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
from collections import defaultdict
import json,re,sys,time
sys.dont_write_bytecode=True
from read_evidence_bytes import read_bytes
BASE=Path('research/269_summary_radius_audit')
start=time.monotonic();now=datetime.now(timezone.utc)
outdir=BASE/'verification'/now.strftime('%Y%m%dT%H%M%SZ');outdir.mkdir()
source=Path('../a4-lead/FINAL_SUMMARY.md');text=source.read_text()
(outdir/'lead_summary.md').write_text(text)
aggregate=Path('artifacts/current_certified_radii.json');raw=aggregate.read_bytes();d=json.loads(raw)
(outdir/'aggregate.json').write_bytes(raw)
groups=defaultdict(list);checked=[]
for row in d['rows']:
    delta=F(row['delta']);h,Q=row['h'],row['Q'];q=row['q']
    assert delta==F(2*h,Q)
    assert F(row['radius_exponent'])==F(q,2*h)
    assert F(row['amplitude_exponent'])==1/delta
    value=read_bytes(row['path']);assert sha256(value).hexdigest()==row['sha256'],row['path']
    groups[(row['family'],delta)].append(row)
    checked.append(dict(family=row['family'],delta=str(delta),root_index=row['root_index'],q=q,radius_exponent=row['radius_exponent'],amplitude_exponent=row['amplitude_exponent'],certificate=row['path'],sha256=row['sha256']))
for value in groups.values():value.sort(key=lambda r:r['root_index'])
section=text.split('## Certified radii at rational',1)[1].split('## 1.',1)[0]
seen=set();compared=[]
for line in section.splitlines():
    if not line.startswith('| '):continue
    cells=[v.strip() for v in line.strip().strip('|').split('|')]
    label=cells[0]
    if label in ('two-mode','Candidate-shaped'):family=label
    elif label.startswith('single harmonic '):family='single sin'+re.search(r'\\sin(\d+)',label).group(1)
    else:continue
    delta=F(re.search(r'\$([0-9]+/[0-9]+)\$',cells[1]).group(1))
    c=F(re.search(r'\(\$([0-9/]+)\$\)',cells[1]).group(1));assert c==1/(1-delta)
    key=(family,delta);assert key in groups and key not in seen;seen.add(key)
    exponents=[F(v.strip()) for v in cells[2].replace('$','').replace('\\','').split(',')]
    expected=[F(v['radius_exponent']) for v in groups[key]];assert exponents==expected,(key,exponents,expected)
    restored=[]
    if family=='Candidate-shaped':
        restored=[F(v.strip()) for v in cells[3].replace('$','').replace('\\','').split(',')]
        assert restored==[F(v['restored_original_amplitude_exponent']) for v in groups[key]]
    compared.append(dict(family=family,delta=str(delta),c_l=str(c),exponents=list(map(str,exponents)),restored=list(map(str,restored))))
assert seen==set(groups)
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,profile_count=len(checked),group_count=len(groups),certificate_hashes_checked=len(checked),exact_radius_equalities=len(checked),exact_amplitude_equalities=len(checked),published_groups=compared,rows=checked,source_summary=dict(path=str(outdir/'lead_summary.md'),sha256=sha256(text.encode()).hexdigest()),source_aggregate=dict(path=str(outdir/'aggregate.json'),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-start)
(outdir/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
(BASE/'sources/summary_radius_audit.py').write_bytes(Path('code/summary_radius_audit.py').read_bytes())
print(json.dumps({k:v for k,v in result.items() if k not in ['rows','published_groups']}))

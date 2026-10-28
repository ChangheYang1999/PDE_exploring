"""Same-witness comparison to the numerical lane's ten completed polygon runs."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib
from flint import arb,ctx
ctx.prec=256;ROOT=Path(__file__).resolve().parents[1];NUM=ROOT/'numerics_data'
specs=[('a120_a35.json','num_v2_layercake_a60.json'),('a110_a35.json','num_v2_layercake_a60.json'),('a15_a12.json','structured_full_a_half.json'),('a310_a12.json','structured_full_a_half.json'),('a25_a12.json','structured_full_a_half.json'),('a12_a12.json','structured_full_a_half.json'),('a35_a25.json','num_v2_layercake_a40.json'),('a710_a25.json','num_v2_layercake_a40.json'),('a34_a310.json','num_v2_layercake_a30.json'),('a45_a310.json','num_v2_layercake_a30.json')]
rows=[];hashes={};directory=ROOT/'05_team_audit/numerical_certificate_v2/verification';directory.mkdir(parents=True,exist_ok=True)
for numname,ownname in specs:
    p=NUM/'cert2'/numname;raw=p.read_bytes();(directory/numname).write_bytes(raw)
    nc=json.loads(raw);op=ROOT/'data'/ownname;oc=json.loads(op.read_text());assert Fraction(nc['a'])==Fraction(oc['a'])
    row=next(r for r in oc['rows'] if Fraction(r['alpha'])==Fraction(nc['alpha']))
    lo=arb(row['safe_decimal_lower_10_places']);hi=arb(row['safe_decimal_upper_10_places'])
    nlo=arb(nc['I_lower']);nhi=arb(nc['I_upper']);assert lo>nlo
    assert not (hi<nlo or lo>nhi)
    contained=bool(lo>nlo and hi<nhi)
    rows.append(dict(alpha=nc['alpha'],shape=nc['a'],numerics_file=str(p.relative_to(NUM)),numerics_lower=nc['I_lower'],numerics_upper=nc['I_upper'],independent_file=str(op.relative_to(ROOT)),independent_lower=row['safe_decimal_lower_10_places'],independent_upper=row['safe_decimal_upper_10_places'],independently_proved_lower=True,independent_interval_contained=contained,intervals_overlap=True))
    hashes[str((directory/numname).relative_to(ROOT))]=hashlib.sha256(raw).hexdigest();hashes[str(op.relative_to(ROOT))]=hashlib.sha256(op.read_bytes()).hexdigest()
paths=['05_team_audit/numerical_certificate_v2/PROOF.md','05_team_audit/numerical_certificate_v2/source/certify_lb.py','05_team_audit/numerical_certificate_v2/source/zcurve.py','code/compare_num_v2_polygon.py','code/check_num_kernel_v2.py','data/num_kernel_v2_checks.json']
for p in paths:hashes[p]=hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=rows,source_hashes=hashes,status='All ten reported lower bounds independently proved by the same-witness layer-cake certificate; all interval pairs overlap')
(ROOT/'data/num_v2_polygon_comparison.json').write_text(json.dumps(out,indent=2)+'\n');(directory/'manifest.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows:print(r['alpha'],r['shape'],'lower independently proved, own enclosure contained:',r['independent_interval_contained'])

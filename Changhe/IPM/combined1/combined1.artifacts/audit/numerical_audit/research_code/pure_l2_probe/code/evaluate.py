"""Necessary L2 correction radius from the weak identity in divergence form."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
from flint import arb,ctx
ctx.prec=512;start=time.monotonic()
ROOT=Path(__file__).resolve().parents[3]
source=ROOT/'research/weak_probe/verification/d2_1024.json'
data=json.loads(source.read_text());row=next(r for r in data['probes'] if r['p']==2)
I=abs(arb(row['pairing']));D=arb(row['denominator_without_d'])
assert I>0 and D>0
lower=2*I/(D+(D*D+4*I).sqrt())
r=arb(27)/10000;rhs=D*r+r*r;gap=I-rhs
assert gap>0 and lower>r
boxes=[]
for b in row['boxes']:
 m=arb(b['m']);g=I-D*m-m*m
 assert g>0
 boxes.append({'framework':b['framework'],'L2_cap':m.str(80),'necessary_gap':g.str(80),'excluded':True})
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':'d2','precision_bits':ctx.prec,
 'pairing_absolute':I.str(80),'linear_denominator':D.str(80),'gradient_probe_sup_exact':'1',
 'necessary_L2_radius_lower':lower.str(80),'excluded_closed_L2_radius_exact':'27/10000',
 'rhs_at_rational_radius':rhs.str(80),'strict_gap_at_rational_radius':gap.str(80),'boxes':boxes,
 'source_sha256':sha256(source.read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
 'proof_sha256':sha256((ROOT/'research/pure_l2_probe/PROOF.md').read_bytes()).hexdigest(),
 'elapsed_seconds':time.monotonic()-start,
 'scope':'Any real L2 distributional divergence-form stationary correction at the same c. No gradient cap. N4-ORIGIN pending review.'}
(ROOT/'research/pure_l2_probe/verification/d2_512.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

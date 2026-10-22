"""Retained exact display check and source-level range semantics, no cell replay."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
D=Path(__file__).resolve().parents[1];ROOT=D.parents[1];NUM=ROOT.parent/'ipmA-num'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pins={}
for name in ['variants_summary.py','cert_resid_regions.py']:
 original=NUM/'src'/name;dest=D/'sources'/name;assert not dest.exists();dest.write_bytes(original.read_bytes());pins[str(dest.relative_to(ROOT))]=sha(dest)
v=(D/'sources/variants_summary.py').read_text();r=(D/'sources/cert_resid_regions.py').read_text()
assert 'r_range=[float(ra.min()), float(ra.max())]' in v and 'ra = np.array([r["r_a"] for r in rr])' in v
assert 'e = ta.exp()' in r and 'r_a = float(e.mid())' in r and 'h = tau[ci + 1] - tau[ci]' in r
raw=json.loads((D/'evidence/inputs.json').read_text());report=(D/'sources/NUM_REPORT.md').read_text();assert '4.9727e-9 (middle) + 3.9065e-7 (outer) + 3.4826e-16 (inner) <= 3.9562e-7' in report
inputs={'rounded_middle':'4.9727e-9','rounded_outer':'3.9065e-7','rounded_inner':'3.4826e-16','claimed_sum_ceiling':'3.9562e-7','safe_rounded_sum_ceiling':'3.9563e-7'}
ip=D/'evidence/precision_inputs.json';ip.write_text(json.dumps(inputs,indent=2)+'\n');pins[str(ip.relative_to(ROOT))]=sha(ip)
s=sum((F(inputs[n]) for n in ['rounded_middle','rounded_outer','rounded_inner']),F(0));claim=F(inputs['claimed_sum_ceiling']);actual=F(raw['finite_sum_exact']);assert actual<claim<s<F(inputs['safe_rounded_sum_ceiling'])
z={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_DISPLAY_COUNTEREXAMPLE_AND_SOURCE_RANGE_SEMANTICS','source_sha256':sha(Path(__file__)),'snapshot_files':pins,'range_semantics':'The outer/inner r_range uses min/max of stored approximate left-anchor radii, not the upper right endpoint or a coverage certificate. No physical cell cover is verified here.','rounded_sum_exact':str(s),'claimed_ceiling_exact':str(claim),'excess_exact':str(s-claim),'raw_finite_sum_exact':str(actual),'raw_finite_sum_below_claim':True,'rounded_sum_claim_refuted':True,'whole_norm_hypothesis_still_open':True}
(D/'evidence/precision_checks.json').write_text(json.dumps(z,indent=2)+'\n');print(json.dumps(z,indent=2))

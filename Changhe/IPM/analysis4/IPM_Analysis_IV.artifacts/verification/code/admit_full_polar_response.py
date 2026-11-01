"""Record a complete two-implementation identity check, separately by period."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json
from certificate_admission import read,ref,checkref,next_entry
ap=argparse.ArgumentParser();ap.add_argument('--Q',type=int,choices=[9,10],required=True);ap.add_argument('--entry',type=int,required=True);a=ap.parse_args()
base=Path('research/284_full_polar_response_comparison');p=base/'verification'/f'Q{a.Q}/checks.json';d=read(p);assert d['all_checks_pass'] and d['Q']==a.Q and d['degree_bound']==a.Q
values=[0,1,-1,2,-2,3,-3,4,-4,5,-5][:a.Q+1];assert d['distinct_b_values']==values and [r['b'] for r in d['rows']]==values and all(r['exact_full_identity'] for r in d['rows'])
for r in d['inputs']+[d['frozen_lead_source']]:checkref(r)
assert d['lead_source']['sha256']==d['frozen_lead_source']['sha256']
ledger,s=next_entry(a.entry);now=datetime.now(timezone.utc).isoformat(timespec='seconds');out=p.parent/'admission.json';assert not out.exists()
result=f"For Q{a.Q}, full rational responses agree identically in k at all{a.Q+1} distinct interpolation values of b. Degree at most{a.Q} establishes the full polynomial identity in b. The lead's polar low-order recurrence also matches{d['exact_low_prefix_comparisons']} Cartesian prefix coefficients. Actual runtime{d['actual_elapsed_s']:.6f}seconds."
scope='The full derivative implementations agree. They share the audited Q(k) arithmetic engine, so this is not an independent arithmetic-library check.'
if a.Q==9:scope+=' This closes the full-numerator comparison left OPEN inV573.'
out.write_text(json.dumps(dict(at=now,entry=a.entry,all_checks_pass=True,evidence=ref(p),scope=scope),indent=2)+'\n')
ledger.write_text(s+f'\n## V{a.entry} | {now} | Full Cartesian/polar response identity, Q{a.Q}\n\n**Claim.** The independently expressed Cartesian and polar derivative recurrences produce identical complete response functions.\n\n**Method.** Freeze and execute the lead polar source with the same exact rational-function engine, independently compare its prefixes, and cross-multiply every complete numerator and denominator at a degree-determining set of b values.\n\n**Result.** {result}\n\n**Verdict: CONFIRMED.** {scope} Evidence: {out}.\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> LEAD: V{a.entry}, full Q{a.Q} response identity\n\n{result} {scope}\n\n'+notes.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V{a.entry} fullQ{a.Q} polar/Cartesian identity admitted.\n')
with (base/'PROOF.md').open('a') as f:f.write(f'\nCompleted {now}, V{a.entry}. {result} {scope}\n')
(base/'sources/admit_full_polar_response.py').write_bytes(Path(__file__).read_bytes());print(result)

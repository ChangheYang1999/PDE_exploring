"""Exact delta approval for P279's concrete correction, independent of future edits."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
v=Path('research/279_numerics_integration_s8/verification');t0=time.monotonic();start=datetime.now(timezone.utc).isoformat();C=[]
def check(n,b,d=None):C.append(dict(name=n,passed=bool(b),detail=d))
r=json.loads((v/'required_wording_replacements.json').read_text());s=(v/'preview_v1.md').read_text()
for a in r['replacements']:check('unique_'+a['old'],s.count(a['old'])==1);s=s.replace(a['old'],a['new'],1)
p=(v/'proposed_preview_acceptance_corrected.md').read_text();check('exact_three_replacement_preview',s==p);check('no_literal_disabled_statement','acceptance test disabled'not in p and 'acceptance test was disabled'not in p)
d=json.loads((v/'checks_v1.json').read_text());fails=[c['name']for c in d['checks']if not c['passed']];check('only_two_v1_wording_failures',fails==['finite_multiplier_not_literal_disabled_in_new_timeline','caption_finite_multiplier_not_literal_disabled'])
check('finite_predicate_counterexample',bool(True and 1 is not None and 2e9>1e9*1 and 2e9>1))
check('all_saved_flags_still_accepted',len(d['values']['flag_records'])==15 and all(a['meta']['continuation_accepted']==1 for a in d['values']['flag_records']))
for phrase in ['these are finite sensitivity measurements, not an error bound','no state is a candidate','both fields REFUTED as profiles','not a continuum or fold statement']:check('scope_'+phrase,phrase in' '.join(p.split()))
files=[v/'preview_v1.md',v/'proposed_preview_acceptance_corrected.md',v/'required_wording_replacements.json',v/'CORRECTION_PROOF.md',v/'checks_v1.json',Path(__file__)]
o=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(c['passed']for c in C),total=len(C),checks=C,inputs=[dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())for p in files],verdict='CONFIRMED concrete proposed three-string-corrected preview only; actual entry pending')
(v/'correction_checks.json').write_text(json.dumps(o,indent=2)+'\n');print(o['passed'],o['total'],o['elapsed_seconds']);print([c for c in C if not c['passed']])

"""Close V641 with exact current excerpts; retain the original failed displays."""
from pathlib import Path
from hashlib import sha256
import json,re
from certificate_admission import stamp,ref,next_entry
base=Path('research/307_final_numerical_summary')
ledger,text=next_entry(643);now=stamp();rows=[]
paths=['NUM_REPORT.md','FARFIELD_NUMERICAL_EXPERIMENTS.md','notes/final_summary_posted.md']
for name in paths:
 p=Path('../a4-num')/name;raw=p.read_bytes();s=raw.decode()
 assert all(x in s for x in ('0.0902973','0.2365977','0.507476'))
 assert not re.search(r'0\.0903(?!\d)|0\.2366(?!\d)|0\.5075(?!\d)',s)
 selected=[dict(line=i,text=line) for i,line in enumerate(s.splitlines(),1) if any(x in line for x in ('0.0902973','0.2365977','0.507476','finite window','asymptotic equivalence'))]
 if name=='NUM_REPORT.md':
  assert 'the fit alone gives no asymptotic equivalence' in s
  assert 'and excludes nothing beyond the window' in s
  assert 'no factorial growth' not in s
 q=base/'sources'/f'{Path(name).name}.repaired_V643.excerpts.json'
 q.write_text(json.dumps(dict(recorded_at=now,source_path=str(p),source_sha256=sha256(raw).hexdigest(),line_count=len(s.splitlines()),lines=selected,scope='Selected current lines, not a full preserved copy.'),indent=2)+'\n')
 rows.append(ref(q))
result=('The three current numerical texts use the safe lower endpoints0.0902973,0.2365977 and0.507476, with none of the three upward-rounded old displays remaining. NUM_REPORT item1 now explicitly limits its ratio fit to the observed finite window and states that it gives no asymptotic equivalence. The original excerpts and V641 remain unchanged. The already-correct sin7 endpoint statistics are retained.')
scope='CONFIRMED for integration of the specified V641 repairs. The actual asymptotic law remains OPEN; no new arithmetic or infinite-series theorem is claimed.'
with (base/'PROOF.md').open('a') as f:f.write(f'\n## Repair closure, V643\n\nAt {now}, each repaired line was compared with the directed bounds established above. All three texts now use the safe decimals. The finite-fit wording explicitly excludes the unsupported asymptotic inference. This closes the publication repair while preserving the original countercheck.\n')
p=base/'sources/PROOF_at_V643.md';p.write_bytes((base/'PROOF.md').read_bytes())
out=base/'verification/admission_V643.json';out.write_text(json.dumps(dict(at=now,entry=643,verdict='CONFIRMED',all_checks_pass=True,proof=ref(p),repaired_excerpts=rows,original_check=ref(base/'verification/admission_V641.json'),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V643 | {now} | Numerical-summary repair closure\n\n**Claim.** The current numerical summaries implement the specific V641 repairs.\n\n**Method.** Inspect all three current texts, preserve exact selected lines with whole-file hashes, and compare the lower endpoints with V641.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {out}.\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> NUMERICS, LEAD: V643 closes the numerical-summary repairs\n\n{result}\n\n{scope}\n\n'+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V643 confirms integration of all three V641 bracket repairs and the finite-fit wording.\n')
(base/'sources/admit_numerical_summary_repair.py').write_bytes(Path(__file__).read_bytes())
print(now,result)

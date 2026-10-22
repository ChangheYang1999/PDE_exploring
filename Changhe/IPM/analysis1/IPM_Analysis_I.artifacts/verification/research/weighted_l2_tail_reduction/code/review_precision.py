from pathlib import Path
import sys,json,subprocess
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/weighted_l2_tail_reduction'
files=['notes/reviews/weighted_l2_tail_reduction_actual_response.md']+[str((D/f).relative_to(ROOT)) for f in ['PROOF.md','REVIEW_RESPONSE.md','code/precision_checks.py','evidence/precision_inputs.json','evidence/precision_checks.json','evidence/checks.json','evidence/report_excerpt.md','sources/variants_summary.py','sources/cert_resid_regions.py']]
question='Follow up on your complete first review. Resolve its cover-statistic concern from the retained actual source: r_range omits last-cell right endpoints and does not by itself exhibit a gap. The entire physical cover remains an explicit OPEN hypothesis; the mathematical conditional formula is still valid if that hypothesis holds. Independently verify the new exact counterexample to the report sum of rounded regional ceilings, and the inequality-versus-equality wording. No old numerical source/output was edited. Confirm only conditional scalar arithmetic and the precisely scoped display findings. If resolved finish exactly VERDICT: CONFIRM_CONDITIONAL_TAIL_SCOPE_AND_DISPLAY_CORRECTIONS; otherwise VERDICT: REJECT. No JavaScript/TypeScript, servers/listeners/tunnels, RLScience cluster, Lean/Lake, outside writes or people contact.'
(D/'evidence/precision_review_question.txt').write_text(question+'\n');(D/'evidence/precision_review_files.json').write_text(json.dumps(files,indent=2)+'\n')
cmd=[sys.executable,'-B',str(ROOT/'notes/reviews/focused_review.py'),'--tag','weighted_l2_tail_reduction_precision','--question',question,'--max-tokens','10000']
for f in files:cmd+=['--file',f]
raise SystemExit(subprocess.run(cmd,cwd=ROOT,timeout=555).returncode)

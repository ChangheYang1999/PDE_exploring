"""Reconcile completed C wrapper timings without invoking any policy."""
from collections import defaultdict
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.publish_terminal_validation import timing_accounting
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
A=E/'analysis/decision_timing_accounting'

def main():
    inputs={}
    def read(p):
        inputs[str(p)]=hashlib.sha256(Path(p).read_bytes()).hexdigest()
        return json.loads(Path(p).read_text())
    rows=[];table=[]
    for version,campaign,entryfile,receiptfile in (
        ('best_v9e','reserved-C-best-v9e-001','reserved-C-best-v9e-001-entrypoint-summary.json','final_reserved_validation/verification/best_v9e.json'),
        ('best_v9f','reused-C-best-v9f-001','reused-C-best-v9f-001-archived-entrypoint-summary.json','reused_c_validation/verification/full_games.json')):
        strict=read(R/(campaign+'-strict.json'));entry=read(R/entryfile)
        receipt=read(E/'analysis'/receiptfile)
        assert strict['valid_conditions']==72 and entry['all_passed'] and entry['count']==72
        jobs={j['id']:j for j in read(R/campaign/'jobs.json')}
        entries={c['job']:c for c in entry['cases']}
        assert set(jobs)==set(entries)=={c['job'] for c in strict['cases']}
        groups=defaultdict(list)
        for c in strict['cases']:
            j=jobs[c['job']];checked=entries[c['job']]
            prefix=len(j.get('prefixes',[[],[]])[j['condition']['candidate_side']])
            assert checked['prefix_rounds']==prefix<=c['rounds']
            detail=read(checked['audit_path'])['cases'][0]
            assert len(detail['entrypoint_rounds'])==c['rounds']
            actual=sum(d['policy_invoked'] for d in detail['entrypoint_rounds'])
            assert actual==checked['policy_rounds']==c['rounds']-prefix
            for rnd,d in enumerate(detail['entrypoint_rounds'],1):
                assert d['round']==rnd and d['policy_invoked']==(rnd>prefix)
            groups[c['condition']['scenario']].append(c)
        metrics={}
        for scenario,cc in groups.items():
            result=timing_accounting(cc,entries)
            old=receipt['metrics'][scenario]
            assert result['timed_decision_wrapper_calls']==old['candidate_calls']
            assert result['total_timed_wrapper_seconds']==old['total_candidate_decision_seconds']
            assert result['maximum_timed_wrapper_call_seconds']==old['max_candidate_call_seconds']
            metrics[scenario]=result
            table.append(f'| {version} | {scenario} | {result["timed_decision_wrapper_calls"]} | {result["prescribed_prefix_turns"]} | {result["actual_policy_calls"]} |')
        assert sum(m['actual_policy_calls'] for m in metrics.values())==entry['policy_rounds']
        assert sum(m['prescribed_prefix_turns'] for m in metrics.values())==entry['skipped_prefix_rounds']
        wrong=deepcopy(strict['cases'][0]);wrong['decision_seconds_candidate_first'][0]['calls']+=1
        try:timing_accounting([wrong],entries)
        except AssertionError:pass
        else:raise AssertionError('Wrong wrapper count was accepted.')
        rows.append(dict(version=version,campaign=campaign,metrics=metrics,
            actual_policy_calls=entry['policy_rounds'],prescribed_prefix_turns=entry['skipped_prefix_rounds'],
            wrong_count_rejected=True))
    stamp=datetime.now(timezone.utc).isoformat()
    text='\n'.join(['# Corrected interpretation of pool C timing counts','',f'Checked {stamp}.','',
        'CONFIRMED: the old candidate_calls metric counts calls to the outer timing wrapper. It includes prescribed prefix turns. The fresh-entry policy-call counts were already correct. Every one of the 144 completed game records agrees with its job prefix and per-round fresh-entry audit; a deliberately wrong wrapper count is rejected. No candidate or opponent is executed by this check.','',
        '| Candidate | Start | Wrapper calls | Prefix turns | Actual policy calls |','|---|---|---:|---:|---:|']+table+['',
        'For best_v9e the totals are 1,224 wrapper calls, 120 prefix turns and 1,104 policy calls. For best_v9f they are 1,208, 120 and 1,088. Original total_candidate_decision_seconds and max_candidate_call_seconds retain the timing-wrapper interpretation, including prefix-copy operations. They cannot be relabeled as isolated policy-only timings.','',
        'The original reports and receipts are preserved. The final pool D publisher now has explicit timed_decision_wrapper_calls, actual_policy_calls and prescribed_prefix_turns fields, together with wrapper total and maximum seconds. This check exercises that same accounting function on completed data. The declared D opponents, histories, protocol and start restriction are unchanged.','',
        'Reproduce with python -B -m bot_research.experiments.validation.check_decision_timing_accounting from the project root using the supplied environment, a free assigned low-priority core, disabled bytecode and research-local temporary files. The receipt is verification/accounting.json.',''])
    output=A/'RESULTS.md'
    with output.open('x') as f:f.write(text)
    for p in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd()),E/'publish_terminal_validation.py',E/'evaluate.py',E/'isolated_match.py'):
        inputs[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
    result=dict(time_utc=stamp,all_passed=True,games=144,policy_calls_performed=0,campaigns=rows,input_sha256=inputs)
    atomic_json(A/'verification/accounting.json',result,exclusive=True)
    for area,version in (('final_reserved_validation','best_v9e'),('reused_c_validation','best_v9f')):
        add=E/'analysis'/area/'TIMING_ADDENDUM.md'
        with add.open('x') as f:f.write(f'# Timing accounting addendum\n\nChecked {stamp}.\n\nThe original candidate_calls field counts timing-wrapper calls, including prescribed prefix turns. It is not the actual policy-call count on continuation starts. All original game and fresh-entry results remain valid and unchanged. See ../decision_timing_accounting/RESULTS.md and its pinned accounting receipt for the complete {version} correction. Original aggregate seconds also include prefix-copy overhead.\n')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Timing-wrapper accounting correction\n\nClaim and verdict: CONFIRMED on144completedCconditions. Old candidate_calls fields include prefix turns; fresh-entry counts were correct. best_v9e has1224wrapper/120prefix/1104policycalls, best_v9f1208/120/1088. Original seconds include prefix overhead. Complete data and per-round audit reconciled; wrong-count fixture rejected. Dpublisher corrected before candidate freeze, with no Dexecution. Existing results preserved with timing addenda. See {output}.\n')
    print(json.dumps({k:v for k,v in result.items() if k!='input_sha256'}))

if __name__=='__main__':main()

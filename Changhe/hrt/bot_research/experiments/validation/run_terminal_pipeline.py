"""Run all fixed terminal checks after the declared selection and time gate.

Launch only on an assigned free core. This module does not create processes
with additional parallelism and each blocking child has a bounded timeout.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import time

E=Path('bot_research/experiments/validation')
R=Path('bot_research/runs/validation')
DEADLINE=datetime.fromisoformat('2026-11-01T00:57:42+00:00')


def main():
    declaration=json.loads((E/'terminal-candidate-declaration-001.json').read_text())
    name=declaration['campaign_name'];directory=R/name
    def event(**data):
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),**data)),flush=True)
    def verify():
        for p,h in declaration['source_sha256'].items():
            assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    def run(module,*args):
        if (DEADLINE-datetime.now(timezone.utc)).total_seconds()<590:
            event(stopped_before_child=True,reason='Insufficient time before worker deadline.')
            raise SystemExit(3)
        verify()
        command=['.venv/bin/python','-B','-m','bot_research.experiments.validation.'+module,*map(str,args)]
        event(command=command)
        child=subprocess.run(command,timeout=580)
        event(returncode=child.returncode)
        if child.returncode:raise SystemExit(child.returncode)
    earliest=datetime.fromisoformat(declaration['not_before_utc'])
    event(time_gate_pending=True,not_before_utc=earliest.isoformat())
    while datetime.now(timezone.utc)<earliest:time.sleep(5)
    verify()
    assert datetime.fromisoformat(declaration['selection_time_utc'])<=datetime.fromisoformat(declaration['time_utc'])
    assert declaration['candidate']=='bot_research.bots.best:decide'
    assert declaration['expected_conditions']==96
    sha=declaration['candidate_sha256'];candidate=declaration['candidate']
    event(time_and_selection_gates_passed=True)
    separation_done=False
    for batch in range(80):
        args=['--candidate',candidate,'--candidate-sha256',sha,'--output-dir',directory,'--max-seconds',480,'--match-timeout',300]
        if directory.exists():args+=['--resume']
        run('terminal_validation',*args)
        if not separation_done:
            for label,module in [('parameter','audit_terminal_separation'),('scenario','audit_terminal_scenario_separation')]:
                output=R/(name+'-'+label+'-separation.json')
                if not output.exists():run(module,'--campaign',directory,'--output',output)
            snapshot=R/(name+'-separation-inputs')
            if not (snapshot/'manifest.json').exists():
                run('snapshot_audit_inputs','--audits',
                    R/(name+'-parameter-separation.json'),
                    R/(name+'-scenario-separation.json'),
                    '--output-dir',snapshot)
            separation_done=True
        summary=json.loads((directory/'summary.json').read_text())
        if summary['complete']:break
    else:raise SystemExit('Incomplete terminal campaign after bounded batches.')
    assert summary['all_completed_successfully'],summary
    strict=R/(name+'-strict.json')
    if not strict.exists():run('audit_terminal_campaign','--directory',directory,'--candidate-sha256',sha,'--output',strict)
    assert not json.loads(strict.read_text())['current_source_drift']
    audit=R/(name+'-replays')
    for batch in range(50):
        args=['--campaign',directory,'--output-dir',audit,'--max-seconds',240,'--match-timeout',300]
        if audit.exists():args+=['--resume']
        run('replay_campaign_bounded',*args)
        summary=json.loads((audit/'summary.json').read_text())
        if summary['all_passed']:break
        assert not summary['counts'].get('failed',0),summary
    else:raise SystemExit('Incomplete terminal replay checks.')
    replay=R/(name+'-replay.json')
    if not replay.exists():run('summarize_reserved_replays','--campaign-audit',strict,'--audit-dirs',audit,'--output',replay)
    rendered=R/(name+'-summary.md')
    if not rendered.exists():run('render_terminal_summary','--campaign-audit',strict,'--replay-audit',replay,'--output',rendered)
    losses=R/(name+'-losses.json')
    if not losses.exists():run('diagnose_reserved_losses','--campaign-audit',strict,'--output',losses)
    event(matches_and_replays_complete=True)
    audit=R/(name+'-entrypoints')
    for batch in range(80):
        args=['--campaign',directory,'--candidate-sha256',sha,'--output-dir',audit,'--max-seconds',240,'--match-timeout',300]
        if audit.exists():args+=['--resume']
        run('audit_best_entrypoints_bounded',*args)
        summary=json.loads((audit/'summary.json').read_text())
        if summary['all_passed']:break
        assert not summary['counts'].get('failed',0),summary
    else:raise SystemExit('Incomplete terminal entry-point checks.')
    entry=R/(name+'-entrypoint-summary.json')
    if not entry.exists():run('summarize_entrypoint_audits','--audit-dirs',audit,'--candidate-sha256',sha,'--expected',96,'--output',entry)
    verify()
    run('publish_terminal_evidence')
    event(all_completed=True)


if __name__=='__main__':main()

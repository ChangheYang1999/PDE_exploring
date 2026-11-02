"""Record a final installed candidate and an exact quotation of its selection note.

This declaration performs no candidate or opponent calls. A human-readable
selection record is copied to the worker-owned evidence directory so later
team-note appends cannot alter the evidence used for the declaration.
"""
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure

E=Path('bot_research/experiments/validation')
A=E/'analysis/terminal_reserved_validation'
M=E/'terminal_holdout_manifest.json'


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--candidate-sha256',required=True)
    p.add_argument('--selection-source',required=True)
    p.add_argument('--selection-excerpt',required=True)
    p.add_argument('--selection-time-utc',required=True)
    p.add_argument('--campaign-name',default='reserved-D-final-001')
    args=p.parse_args()
    digest=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
    stamp=datetime.now(timezone.utc)
    selected=datetime.fromisoformat(args.selection_time_utc)
    assert selected.tzinfo is not None and selected<=stamp
    assert args.campaign_name.startswith('reserved-D-') and '/' not in args.campaign_name
    assert not (Path('bot_research/runs/validation')/args.campaign_name).exists()
    candidate=Path('bot_research/bots/best.py')
    assert digest(candidate)==args.candidate_sha256
    text=Path(args.selection_source).read_text()
    assert len(args.selection_excerpt)>=40 and args.selection_excerpt in text
    archived=A/'verification/final_selection_note.md'
    with archived.open('x') as f:f.write(text)
    manifest=json.loads(M.read_text())
    for path,sha in manifest['source_sha256'].items():assert digest(path)==sha,path
    assert digest(manifest['prefix_check'])==manifest['prefix_check_sha256']
    modules=['terminal_validation','audit_terminal_campaign','audit_terminal_separation',
        'audit_terminal_scenario_separation','render_terminal_summary',
        'replay_campaign_bounded','summarize_reserved_replays','diagnose_reserved_losses',
        'audit_best_entrypoints_bounded','summarize_entrypoint_audits','publish_terminal_validation',
        'declare_terminal_candidate','run_terminal_pipeline',
        'snapshot_audit_inputs','publish_terminal_evidence']
    roots={'bot_research.bots.best'}|{'bot_research.experiments.validation.'+m for m in modules}
    paths=set(static_closure(roots))|{Path(s) for s in manifest['source_sha256']}|{
        M,Path(manifest['prefix_check']),A/'PROOF.md',archived,Path('configs/balanced.json'),Path('td_game/balanced.json')}
    hashes={str(f):digest(f) for f in sorted(paths)}
    declaration=dict(time_utc=stamp.isoformat(),selection_time_utc=selected.isoformat(),
        selection_excerpt=args.selection_excerpt,selection_record=str(archived),selection_record_sha256=digest(archived),
        candidate='bot_research.bots.best:decide',candidate_sha256=args.candidate_sha256,
        manifest=str(M),manifest_sha256=digest(M),not_before_utc=manifest['not_before_utc'],
        expected_conditions=96,campaign_name=args.campaign_name,source_sha256=hashes,
        use='Report the final selected policy. Do not select or tune candidates from D outcomes.',
        candidate_and_opponent_calls=0)
    out=E/'terminal-candidate-declaration-001.json'
    atomic_json(out,declaration,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp.isoformat()}: Terminal candidate declared\n\nClaim and verdict: OPEN, final installed SHA {args.candidate_sha256} declared for the unchanged96-condition D reserve. Selection time {selected.isoformat()}; exact selection excerpt and a copy of the note retained. No candidate or opponent calls occur in this declaration. Games may start only after {manifest["not_before_utc"]}; D is report-only, with no D-informed candidate choice. Declaration: {out}.\n')
    print(json.dumps(dict(time_utc=stamp.isoformat(),declaration=str(out),source_files=len(hashes),candidate_calls=0)))


if __name__=='__main__':main()

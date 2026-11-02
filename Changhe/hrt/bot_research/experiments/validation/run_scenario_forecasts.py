"""Explicit paired scenario cases with fresh processes and frozen sources.

Scenario behavior lives in observation-only policy wrappers. Conditions mark
these as known-prefix development, excluded from standard strength totals.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys
import time
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation import archive_sources, digest, execution_context, now
from bot_research.experiments.validation.final_validation_strict import read_result
from bot_research.experiments.validation.run_forecast_full import summarize
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--match-timeout', type=float, default=300)
    parser.add_argument('--max-seconds', type=float, default=480)
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--declare-only', action='store_true')
    args = parser.parse_args()
    if not 0 < args.match_timeout <= args.max_seconds <= 500:
        parser.error('Require 0 < match-timeout <= max-seconds <= 500.')
    directory, declaration = Path(args.output_dir), Path(args.manifest)
    for path in (directory, declaration):
        if path.is_absolute() or '..' in path.parts or path.parts[:1] != ('bot_research',):
            parser.error('Use project-relative research paths.')
    if args.resume:
        metadata = json.loads((directory/'freeze.json').read_text())
        jobs = json.loads((directory/'jobs.json').read_text())
        if digest(declaration) != metadata['manifest_sha256']:
            raise ValueError('Declaration changed after freeze.')
    else:
        manifest = json.loads(declaration.read_text())
        directory.mkdir(parents=True, exist_ok=False)
        for name in ('jobs', 'results', 'replays'):
            (directory/name).mkdir()
        jobs = []
        for case in manifest['cases']:
            for side in (0, 1):
                identifier = f'case{len(jobs):04d}'
                candidate, opponent = case['candidate'], case['opponent']
                bots = [{'spec': candidate['spec']}, {'spec': opponent['spec']}]
                names = [candidate['id'], opponent['id']]
                if side:
                    bots.reverse()
                    names.reverse()
                condition = dict(candidate_side=side, candidate_id=candidate['id'],
                    candidate_spec=candidate['spec'], opponent_id=opponent['id'],
                    opponent_spec=opponent['spec'], initial_state='standard-with-known-call-through-prefix',
                    scenario=case['scenario'], engine_seed=None, purpose=manifest['purpose'],
                    strength_score_eligible=False, pool='development')
                jobs.append(dict(id=identifier, names=names, bots=bots, condition=condition,
                    replay_path=str(directory/'replays'/(identifier+'.jsonl'))))
        identities = {(j['condition']['candidate_id'], j['condition']['opponent_id'], j['condition']['candidate_side']) for j in jobs}
        if len(identities) != len(jobs):
            raise ValueError('Scenario case names must identify every assignment uniquely.')
        roots = {'bot_research.experiments.validation.run_scenario_forecasts',
                 'bot_research.experiments.validation.forecast_match'}
        roots.update(b['spec'].partition(':')[0] for job in jobs for b in job['bots'])
        paths = set(static_closure(roots)) | {declaration, Path('td_game/balanced.json'), Path('configs/balanced.json')}
        frozen = {str(p): digest(p) for p in sorted(paths)}
        metadata = dict(started_utc=now(), manifest_sha256=digest(declaration),
            purpose=manifest['purpose'], source_sha256=frozen, source_roots=sorted(roots),
            runtime=execution_context(), match_timeout=args.match_timeout)
        archive_sources(frozen, directory)
        atomic_json(directory/'freeze.json', metadata, exclusive=True)
        atomic_json(directory/'jobs.json', jobs, exclusive=True)
        for job in jobs:
            atomic_json(directory/'jobs'/(job['id']+'.json'), job, exclusive=True)
    def check_sources():
        changed = [name for name, value in metadata['source_sha256'].items()
                   if not Path(name).is_file() or digest(name) != value]
        if changed:
            raise ValueError('Frozen inputs changed: '+repr(changed))
    check_sources()
    started = time.perf_counter()
    if not args.declare_only:
        for job in jobs:
            output = directory/'results'/(job['id']+'.json')
            failure_path = directory/'results'/(job['id']+'.failure.json')
            if output.exists() or failure_path.exists():
                continue
            if args.max_seconds-(time.perf_counter()-started) < metadata['match_timeout']:
                break
            check_sources()
            failure = None
            command = [sys.executable, '-B', '-m', 'bot_research.experiments.validation.forecast_match',
                       '--job', str(directory/'jobs'/(job['id']+'.json')), '--output', str(output)]
            try:
                process = subprocess.run(command, capture_output=True, text=True,
                                         timeout=metadata['match_timeout'], check=False)
                if process.returncode:
                    failure = dict(job=job['id'], time_utc=now(), returncode=process.returncode,
                                   stderr=public_diagnostic(process.stderr)[-12000:])
                else:
                    read_result(output, job, metadata['source_sha256'])
            except subprocess.TimeoutExpired:
                failure = dict(job=job['id'], time_utc=now(), timeout_seconds=metadata['match_timeout'])
            except (ValueError, KeyError, TypeError, OSError) as error:
                failure = dict(job=job['id'], time_utc=now(), error=public_diagnostic(str(error)))
            if failure:
                atomic_json(failure_path, failure, exclusive=True)
            check_sources()
            result = summarize(directory, jobs, metadata)
            print(json.dumps(dict(finished=job['id'], valid=result['valid_completed'],
                                  failures=len(result['failures']), invalid=result['invalid'])), flush=True)
    print(json.dumps(summarize(directory, jobs, metadata)), flush=True)


if __name__ == '__main__':
    main()

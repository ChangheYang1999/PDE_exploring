"""Exercise fresh-interpreter repeatability and prefix semantics without holdouts."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

_calls = 0


def stateful_probe(observation):
    global _calls
    _calls += 1
    gold = observation['players'][observation['player']]['gold']
    if _calls < 4:
        return [{'op': 'buy_factory'}] * min(20, gold // 20)
    return [{'op': 'buy_minion', 'type': 'tier2'}] * min(80, gold // 40)


def mutating_probe(observation):
    observation['players'][observation['player']]['gold'] = 0
    raise RuntimeError('intentional fixture exception')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    directory = Path(args.output_dir)
    directory.mkdir(exist_ok=False)
    results = []
    for i in range(2):
        job = {'names': ['stateful_probe', 'rush_t1'],
               'bots': [{'spec': 'bot_research.experiments.validation.check_isolation:stateful_probe'},
                        {'profile': {'roster': ['tier1']}}],
               'condition': {'initial_state': 'standard', 'engine_seed': None},
               'replay_path': str(directory / f'repeat{i}.replay.jsonl')}
        job_path = directory / f'repeat{i}.job.json'
        output = directory / f'repeat{i}.result.json'
        job_path.write_text(json.dumps(job, sort_keys=True) + '\n')
        subprocess.run([sys.executable, '-B', '-m', 'bot_research.experiments.validation.isolated_match',
                        '--job', str(job_path), '--output', str(output)], timeout=60, check=True)
        results.append(json.loads(output.read_text()))
    assert results[0]['trajectory_sha256'] == results[1]['trajectory_sha256']
    assert not any(results[0]['bot_errors']) and not any(results[0]['rejected_actions'])
    job = {'names': ['mutating_probe', 'rush_t1'],
           'bots': [{'spec': 'bot_research.experiments.validation.check_isolation:mutating_probe'},
                    {'profile': {'roster': ['tier1']}}],
           'condition': {'initial_state': 'prescribed one-round prefix', 'engine_seed': None},
           'prefixes': [[[{'op': 'buy_factory'}] * 5], [[{'op': 'buy_factory'}] * 5]],
           'replay_path': str(directory / 'prefix.replay.jsonl')}
    path = directory / 'prefix.job.json'
    out = directory / 'prefix.result.json'
    path.write_text(json.dumps(job, sort_keys=True) + '\n')
    subprocess.run([sys.executable, '-B', '-m', 'bot_research.experiments.validation.isolated_match',
                    '--job', str(path), '--output', str(out)], timeout=60, check=True)
    row = json.loads(out.read_text())
    assert all(player['n_factories'] == 5 for player in row['history'][0]['players'])
    assert not any(e['round'] == 1 for e in row['bot_errors'][0])
    assert row['bot_errors'][0][0]['round'] == 2
    summary = {'completed_utc': datetime.now(timezone.utc).isoformat(),
               'repeat_trajectory_sha256': results[0]['trajectory_sha256'],
               'fresh_process_repetition_equal': True, 'prefix_skips_underlying_call': True,
               'fixture_errors_expected_after_prefix': True,
               'source_sha256': {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in (
                   'bot_research/experiments/validation/check_isolation.py',
                   'bot_research/experiments/validation/isolated_match.py')}}
    (directory / 'summary.json').write_text(json.dumps(summary, sort_keys=True, indent=2) + '\n')
    print(json.dumps(summary, sort_keys=True))


if __name__ == '__main__':
    main()

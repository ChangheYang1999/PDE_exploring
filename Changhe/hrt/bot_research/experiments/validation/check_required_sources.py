"""Fault injection for omitted engine and bot source attestations."""
from copy import deepcopy
import argparse
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import read_result, now
from bot_research.experiments.validation.required_sources import CORE_SOURCES


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    root = Path(args.output_dir)
    root.mkdir(exist_ok=False)
    job = {'condition': {'candidate_side': 0}, 'bots': [
        {'spec': 'bot_research.experiments.validation.check_isolation:stateful_probe'},
        {'profile': {'roster': ['tier1']}}]}
    frozen = {name: 'expected' for name in CORE_SOURCES | {
        'bot_research/experiments/validation/check_isolation.py',
        'bot_research/bots/counters/archetypes.py'}}
    base = {'condition': job['condition'], 'candidate_outcome': 'W', 'result': {'winner': 0},
            'bot_errors': [[], []], 'rejected_actions': [{}, {}], 'source_changed_during_match': [],
            'source_sha256': dict(frozen), 'source_sha256_at_end': dict(frozen)}
    variants = {'valid': deepcopy(base)}
    for field in ('source_sha256', 'source_sha256_at_end'):
        for problem in ('missing', 'empty', 'changed', 'unknown', 'omit_engine', 'omit_bot'):
            row = deepcopy(base)
            if problem == 'missing':
                row.pop(field)
            elif problem == 'empty':
                row[field] = {}
            elif problem == 'changed':
                row[field]['td_game/combat.py'] = 'different'
            elif problem == 'unknown':
                row[field]['unexpected.py'] = 'unexpected'
            elif problem == 'omit_engine':
                row[field].pop('td_game/combat.py')
            else:
                row[field].pop('bot_research/bots/counters/archetypes.py')
            variants[field + '_' + problem] = row
    checks = {}
    for label, row in variants.items():
        path = root / (label + '.json')
        atomic_json(path, row, exclusive=True)
        try:
            read_result(path, job, frozen)
        except ValueError:
            accepted = False
        else:
            accepted = True
        checks[label] = accepted == (label == 'valid')
    output = {'time_utc': now(), 'checks': checks, 'all_passed': all(checks.values()),
              'scope': 'Synthetic attestation faults only; no held-out opponents.'}
    atomic_json(root / 'checks.json', output, exclusive=True)
    print(json.dumps(output, sort_keys=True))
    assert output['all_passed']


if __name__ == '__main__':
    main()

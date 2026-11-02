"""Fault-injection checks for complete unchanged-engine replay verification."""
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.replay_audit import audit_record_sequence, audit_row
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fixture', default='bot_research/runs/validation/frozen-strict-check-001/results/fixture-side0.json')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    row = json.loads(Path(args.fixture).read_text())
    records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
    audit_row(row)
    checks = {'original_fixture_passes': True}
    faults = []
    def add(name, mutate):
        r, rs = deepcopy(row), deepcopy(records)
        mutate(r, rs)
        faults.append((name, r, rs))
    add('wrong_hp', lambda r, rs: r['hp'].__setitem__(0, r['hp'][0] + 1))
    add('wrong_result', lambda r, rs: r['result'].__setitem__('winner', 0))
    add('wrong_hp_difference', lambda r, rs: r.__setitem__('hp_difference_p0', 1))
    add('wrong_round_count', lambda r, rs: r.__setitem__('rounds', r['rounds'] - 1))
    add('wrong_digest', lambda r, rs: r.__setitem__('trajectory_sha256', '0' * 64))
    add('wrong_rollup', lambda r, rs: r['history'][0]['players'][0].__setitem__('gold', -1))
    add('missing_terminal_record', lambda r, rs: rs.pop())
    add('extra_records', lambda r, rs: rs.extend(deepcopy(rs[-2:])))
    add('wrong_initial_hp', lambda r, rs: rs[0]['snapshot'].__setitem__('hp', 801))
    add('wrong_action', lambda r, rs: rs[2]['event'][0]['action'].__setitem__('op', 'unknown_action'))
    add('wrong_intermediate_snapshot', lambda r, rs: rs[2]['snapshot'].__setitem__('gold', -1))
    add('swapped_player_records', lambda r, rs: rs.__setitem__(slice(2, 4), rs[2:4][::-1]))
    for name, r, rs in faults:
        try:
            audit_record_sequence(r, rs)
        except (ValueError, KeyError, TypeError):
            checks[name] = True
        else:
            checks[name] = False
    sources = set(static_closure({'bot_research.experiments.validation.check_replay_audit'}))
    sources |= {Path(args.fixture), Path(row['replay_path']), Path('td_game/balanced.json')}
    result = {'time_utc': now(), 'checks': checks, 'all_passed': all(checks.values()),
              'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps(result['checks']))
    assert result['all_passed']


if __name__ == '__main__':
    main()

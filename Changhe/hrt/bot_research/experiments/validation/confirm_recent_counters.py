"""Verify saved development confirmations, including complete replay equality."""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
from datetime import datetime, timezone
from bot_research.experiments.validation.artifact_io import atomic_json


def read_lines(path):
    return [json.loads(line) for line in Path(path).read_text().splitlines()]


def normalized(path):
    rows = read_lines(path)
    for row in rows:
        row.pop('match', None)
        row['snapshot']['name'] = str(row['player'])
    return rows


def clean(row):
    return not (any(row['bot_errors']) or any(row['rejected_actions']) or
                row['source_changed_during_match'] or row['forecast_mismatch_rounds'])


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    args = p.parse_args()
    base = Path('bot_research/runs/validation')
    timing = read_lines(base/'forecast-timing-finalists-001.jsonl')
    finalists = json.loads((base/'forecast-timing-summary-001.json').read_text())['paired_finalists']
    expected = {(f['screen_index'], side) for f in finalists for side in (0,1)}
    actual = {(r['condition']['screen_index'], r['condition']['counter_side']) for r in timing}
    assert len(timing) == len(actual) == len(expected) == 24 and actual == expected
    assert all(clean(r) for r in timing)
    schedules = read_lines(base/'known-planner003-schedule2-001.jsonl')
    equalities = []
    for row in schedules:
        side = row['condition']['counter_side']
        oldpath = base/('scheduled-rollout-001-iteration2.json' if side == 0 else 'scheduled-rollout-001-iteration2-side1.json')
        old = json.loads(oldpath.read_text())
        assert clean(row) and clean(old)
        equal = normalized(row['replay_path']) == normalized(old['replay_path'])
        assert equal and row['history'] == old['history'] and row['accepted_actions'] == old['accepted_actions']
        equalities.append({'side':side,'reference':str(oldpath),'history_equal':True,
                           'accepted_counts_equal':True,'complete_trajectory_equal_up_to_names':equal})
    f = json.loads((base/'scheduled-rollout-003-filtered-unit.json').read_text())
    u = json.loads((base/'scheduled-rollout-002-unfiltered-unit.json').read_text())
    assert clean(f) and clean(u)
    unit_equal = normalized(f['replay_path']) == normalized(u['replay_path'])
    assert unit_equal
    result = {'time_utc':datetime.now(timezone.utc).isoformat(),
              'timing_conditions':len(timing),'timing_outcomes':dict(Counter(r['counter_outcome'] for r in timing)),
              'timing_pair_outcomes':[{'screen_index':i,'sides':[{'side':r['condition']['counter_side'],
                  'hp_counter_first':r['hp'] if r['condition']['counter_side']==0 else list(reversed(r['hp'])),
                  'rounds':r['rounds']} for r in timing if r['condition']['screen_index']==i]}
                  for i in sorted({r['condition']['screen_index'] for r in timing})],
              'schedule_equality':equalities,'unit_filter_complete_trajectory_equal':unit_equal,
              'all_clean':True}
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__':
    main()

"""Publish the completed, fixed-policy budget transfer comparison."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E / 'analysis/budget_handoff_transfer'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    now = datetime.now(timezone.utc).isoformat()
    inputs = []
    rows = []
    calls = filtered = pairs = count = 0
    outcomes = Counter()
    for tag, expected in (('a', 16), ('b', 16), ('c', 8)):
        prefix = R / f'budget-transfer-{tag}001'
        ds = {}
        for kind in ('strict', 'replay', 'summary', 'data', 'histories'):
            path = Path(f'{prefix}-{kind}.json')
            ds[kind] = json.loads(path.read_text())
            inputs.append(path)
        s, h = ds['summary'], ds['histories']
        assert ds['strict']['valid_conditions'] == ds['strict']['expected_conditions'] == expected
        assert s['valid_conditions'] == s['expected_conditions'] == expected
        assert s['unresolved_conditions'] == 0 and not s['repeat_disagreements']
        assert s['identical_assignment_pairs'] == s['complete_assignment_pairs'] == expected // 2
        assert ds['replay']['all_passed'] and ds['replay']['count'] == expected
        assert ds['data']['all_passed']
        assert all(h[k] for k in ('all_fresh_actions_legal', 'all_observations_unchanged',
            'all_replayed', 'exact_counter_policy_reproduction', 'no_post_handoff_minions'))
        for path, sha in h['input_sha256'].items():
            assert digest(path) == sha, path
        for row in s['rows']:
            values = {(x['outcome'], tuple(x['hp']), x['rounds']) for x in row['results']}
            assert len(row['results']) == 2 and len(values) == 1
            outcome, hp, rnd = next(iter(values))
            assert outcome == 'W'
            rows.append(f'| {row["candidate"]} | {row["opponent"]} | {hp[0]}:{hp[1]} | {rnd} |')
        calls += sum(len(c['rounds']) for c in h['cases'])
        filtered += sum(len(c['filtered_proposals']) for c in h['cases'])
        pairs += expected // 2
        count += expected
        outcomes.update(s['outcomes'])
        inputs.append(E / f'budget-transfer-{tag}001.json')
    assert count == 40 and calls == 1584 and filtered == 520 and pairs == 20
    assert outcomes == {'W': 40}
    verdict = ('REFUTED: the four fixed budget-handoff policies transfer their wins against '
        'P5TNUBM to the five declared targets. All 40 transfer games are target wins. '
        'The earlier wins remain valid for P5TNUBM only in their tested conditions.')
    text = f'''# Fixed budget handoffs fail to transfer

Checked {now}.

{verdict}

Every row below represents both physical assignments. HP is target:counter; every target wins. These are standard-start development games with no retuning of the counter between targets.

| Target | Fixed counter | HP in each assignment | Final round |
|---|---|---|---:|
''' + '\n'.join(rows) + '''

The counter buys one tier4 in round 5, then stops buying minions at handoff 6 or 7. Its defensive hypotheses append pure-tier purchases costing at most half or all of the public opponent budget, capped at 120 copies. It uses no opponent policy model. P4TNUB and best_v9e concede no damage; the earlier 755:740 advantage against P5TNUBM never arises. Fortress v36 and v37 both survive undamaged and eventually destroy the counter. The lead8 opponent takes damage but finishes ahead. The budget forecast is a finite heuristic set, not an immunity certificate for every affordable roster.

The 40 declared games all pass strict accounting, complete original-engine replay, source/data archive checks, and fresh reconstruction of the counter from public observations. All 20 assignment pairs have identical normalized histories. The 1,584 fresh counter decisions match exactly, leave observations unchanged, and submit legal action lists. There are no bot errors or rejected submitted actions. A total of 520 parent factory proposals are removed locally after the added strike; they are never submitted. No minions are bought after handoff.

The fortress planners retain their wall-clock stopping conditions, so observed agreement is not a universal determinism claim. Player swaps are controls, not independent random samples. No held-out condition or pool C game is used. This complete-policy comparison does not isolate one defensive purchase or prove that every HP-triggered or model-free counter fails.

To reproduce, use each of the three budget-transfer manifests with `run_data_development`, a fresh output directory, `--max-seconds 500 --match-timeout 300`, and `--resume` if necessary. Then run the strict, original-engine replay, data-closure and `check_budget_handoff_histories` checks. Run from the project root using `.venv/bin/python -B`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH="$PWD"`, `TMPDIR="$PWD/bot_research/tmp"`, one thread, low priority and the assigned CPU affinity.

Audit inputs:

'''
    text += '\n'.join(f'- `{p}`.' for p in inputs) + '\n'
    (A / 'verification').mkdir(parents=True, exist_ok=True)
    result = A / 'RESULTS.md'
    with result.open('x') as stream:
        stream.write(text)
    inputs += [A / 'PROOF.md', result, Path(__file__).relative_to(Path.cwd())]
    atomic_json(A / 'verification/full_games.json', dict(time_utc=now, all_passed=True,
        input_sha256={str(p): digest(p) for p in inputs}, target_outcomes=dict(outcomes),
        games=count, identical_assignment_pairs=pairs, fresh_decisions=calls,
        local_filtered_proposals=filtered, scope=verdict), exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as stream:
        stream.write(f'\n## {now}: Fixed budget counters do not transfer\n\n'
            f'Claim and verdict: {verdict}\n\n'
            'Method and result: 40 predeclared standard games, five targets, four unchanged '
            'counter settings, both assignments. All original-engine replays and source/data '
            'checks pass. All 1,584 fresh counter decisions reproduce and all 20 assignment '
            'pairs match. No submitted invalid actions or bot errors. Full table: '
            'experiments/validation/analysis/budget_handoff_transfer/RESULTS.md; '
            'receipt verification/full_games.json. Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now, published=str(result), games=count, fresh_decisions=calls)))


if __name__ == '__main__':
    main()

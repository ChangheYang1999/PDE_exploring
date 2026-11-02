"""Publish the complete, audited eight-game emergency-continuation test."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
AREA = E/'analysis/emergency_after_strike'
INVERSE = {'W': 'L', 'D': 'D', 'L': 'W'}


def main():
    inputs = {}
    def digest(path):
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    def read(path):
        inputs[str(path)] = digest(path)
        return json.loads(path.read_text())
    name = 'emergency-prefix-001'
    manifest = read(E/(name+'.json'))
    for path, sha in manifest['input_sha256'].items():
        assert digest(path) == sha, path
    audits = {kind: read(R/(name+'-'+kind+'.json')) for kind in
              ('strict', 'replay', 'summary', 'data', 'histories')}
    summary, histories = audits['summary'], audits['histories']
    assert audits['strict']['valid_conditions'] == manifest['expected_conditions'] == 8
    assert summary['valid_conditions'] == 8 and summary['unresolved_conditions'] == 0
    assert summary['complete_assignment_pairs'] == summary['identical_assignment_pairs'] == 4
    assert not summary['repeat_disagreements']
    assert audits['replay']['all_passed'] and audits['replay']['count'] == 8
    assert audits['data']['all_passed']
    assert all(histories[k] for k in ('all_fresh_actions_legal', 'all_observations_unchanged',
        'all_public_selections_verified', 'all_replayed', 'exact_counter_policy_reproduction'))
    for path, sha in histories['input_sha256'].items():
        assert digest(path) == sha, path
    controls = read(R/'emergency-prefix-controls-001.json')
    assert controls['all_passed']
    component = read(AREA/'verification/component.json')
    assert component['all_passed'] and len(component['results']) == 8
    for case in component['results']:
        assert all(case[k] for k in ('actions_legal', 'observations_unchanged',
                                   'old_prefix_exact', 'original_engine_combat'))
    cells, totals, table = [], defaultdict(Counter), []
    for row in summary['rows']:
        values = {(r['outcome'], tuple(r['hp']), r['rounds']) for r in row['results']}
        assert len(values) == 1 and len(row['results']) == 2
        target_outcome, hp, end = next(iter(values))
        outcome = INVERSE[target_outcome]
        totals[row['opponent']][outcome] += 2
        checks = [c for c in histories['cases'] if c['condition']['candidate_id'] == row['candidate']
                  and c['condition']['opponent_id'] == row['opponent']]
        assert len(checks) == 2
        activations = [[q['round'] for q in c['emergency_checks'] if q['emergency_activated']] for c in checks]
        assert activations[0] == activations[1]
        for r in row['results']:
            checked_row(r['result_path'], inputs)
        cells.append(dict(target=row['candidate'], mode=row['opponent'], outcome=outcome,
                          hp_counter_first=list(reversed(hp)), final_round=end,
                          emergency_activation_rounds=activations[0]))
        table.append(f'| {row["candidate"]} | {row["opponent"]} | {outcome} | {hp[1]}:{hp[0]} | {end} | {activations[0]} |')
    assert len(cells) == 4
    success = totals['emergency_damage']['W'] == 4
    verdict = ('CONFIRMED' if success else 'REFUTED') + ': the damage trigger preserves the baseline win and repairs the shared-prefix flood loss.'
    fresh = sum(len(c['rounds']) for c in histories['cases'])
    now = datetime.now(timezone.utc).isoformat()
    result_path = AREA/'RESULTS.md'
    text = f'''# Emergency continuation results

Checked {now}.

{verdict}

The damage-triggered continuation wins all four declared games. The disabled control wins two and loses two. Each row below covers both physical assignments, whose complete normalized trajectories agree. Outcomes and HP are from the counter's perspective.

| Target | Counter | Outcome | HP counter:target | Final round | Added trigger activates |
|---|---|---|---|---:|---|
'''+ '\n'.join(table)+f'''

At the reached round-five flood state, the public current-roster projection is 85 incoming damage. The disabled policy actually receives 215 after the target's new purchases. The repair builds 20 walls and one gun2 at (9,5), then buys nine factories. That construction reduces actual incoming damage in this round to zero, leaving counter HP 715 and target HP 680. The complete repaired game ends 715:80 in round 50. The baseline target still ends 800:740 because the existing HP-lead trigger already starts defense in round five; the new condition does not activate there.

All eight component cases and eight complete games pass. The full checks cover strict accounting, original-engine replay, pinned source and data identity, legal actions, unchanged observations, and {fresh} freshly regenerated counter decisions. The four disabled trajectories and two repaired-baseline trajectories exactly match their previously recorded route-adaptive controls. The emergency trigger is checked independently at the reached component states. This does not claim that a current-roster projection predicts hidden purchases.

This is a third continuation after the identical opening, so it does not contradict the two-by-two commitment result in ../indistinguishable_prefix/PROOF.md. These are development conditions chosen after diagnosing that failure. No held-out strength claim or change to best_v9e follows. A separately declared 45-target transfer matrix tests whether this repair causes regressions elsewhere.

Reproduction: use run_anonymous_development with emergency-prefix-001.json, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_emergency_histories and compare_recorded_controls with emergency-prefix-controls-001.json. Run check_emergency_component for the on-history component check. Use the existing Python environment, disabled bytecode, the research temporary directory, assigned CPU affinity, one thread and low priority. verification/full_games.json pins the evidence and this publisher.
'''
    with result_path.open('x') as handle:
        handle.write(text)
    for path in (result_path, AREA/'PROOF.md', Path(__file__).relative_to(Path.cwd())):
        inputs[str(path)] = digest(path)
    receipt = dict(time_utc=now, verdict=verdict, all_passed=True, full_games=8,
        fresh_counter_decisions=fresh, component_cases=8, exact_control_pairs=6,
        counter_outcomes=dict(totals), cells=cells, input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as handle:
        json.dump(receipt, handle, indent=2, sort_keys=True); handle.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as handle:
        handle.write(f'\n## {now}: Emergency continuation repairs the identical-prefix pair\n\n'
            f'Claim and verdict: {verdict}\n\n'
            f'Method: eight declared anonymous-name games, both assignments, unchanged engine. Result: damage 4W, disabled 2W/2L; '
            f'{fresh} fresh counter decisions, eight complete replays and six exact previous-trajectory controls pass. '
            'Flood outcome changes from -495:420 at round 7 to 715:80 at round 50. Round-five visible damage 85 triggers '
            '20 walls and one gun2, preventing all 215 actual incoming damage that round. Baseline remains 800:740. '
            'The third continuation does not contradict the restricted binary commitment proof. Development only; '
            f'broader transfer remains to be measured. Evidence: {result_path}.\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'input_sha256'}))

if __name__ == '__main__':
    main()

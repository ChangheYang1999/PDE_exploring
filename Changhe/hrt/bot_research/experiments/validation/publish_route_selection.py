"""Publish the route selector's declared development and adversarial matrices."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
INVERSE = {'W': 'L', 'D': 'D', 'L': 'W'}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--experiment', choices=('repair', 'challenge'), required=True)
    args = parser.parse_args()
    repair = args.experiment == 'repair'
    names = ['route-selector-001'] if repair else ['route-challenge-a001', 'route-challenge-b001']
    area = E/'analysis'/('route_gated_selection' if repair else 'route_feature_challenge')
    inputs = {}
    totals = defaultdict(Counter)
    cells, records, table = {}, {}, []
    calls = filtered = games = assignments = 0
    for name in names:
        path = E/(name+'.json'); inputs[str(path)] = digest(path)
        manifest = json.loads(path.read_text())
        assert manifest['expected_conditions'] == 48
        audits = {}
        for kind in ('strict', 'replay', 'summary', 'data', 'histories'):
            path = R/(name+'-'+kind+'.json'); inputs[str(path)] = digest(path)
            audits[kind] = json.loads(path.read_text())
        assert audits['strict']['valid_conditions'] == audits['strict']['expected_conditions'] == 48
        summary, histories = audits['summary'], audits['histories']
        assert summary['valid_conditions'] == summary['expected_conditions'] == 48
        assert summary['unresolved_conditions'] == 0 and not summary['repeat_disagreements']
        assert summary['complete_assignment_pairs'] == summary['identical_assignment_pairs'] == 24
        assert audits['replay']['all_passed'] and audits['replay']['count'] == 48
        assert audits['data']['all_passed']
        assert all(histories[key] for key in ('all_fresh_actions_legal', 'all_observations_unchanged',
            'all_public_selections_verified', 'all_replayed', 'exact_counter_policy_reproduction'))
        assert all(digest(path) == sha for path, sha in histories['input_sha256'].items())
        for case in histories['cases']:
            c = case['condition']
            key = c['candidate_id'], c['opponent_id'], c['candidate_side']
            assert key not in records
            records[key] = checked_row(case['result'], inputs)
        for row in summary['rows']:
            values = {(r['outcome'], tuple(r['hp']), r['rounds']) for r in row['results']}
            assert len(row['results']) == 2 and len(values) == 1
            target_outcome, hp, end = next(iter(values))
            cases = [c for c in histories['cases'] if c['condition']['candidate_id'] == row['candidate']
                     and c['condition']['opponent_id'] == row['opponent']]
            assert len(cases) == 2
            selected = {case['selected'] for case in cases}; assert len(selected) == 1
            selected = next(iter(selected))
            projections = [next(r['projection'] for r in case['rounds'] if r['round'] == 4) for case in cases]
            assert projections[0] == projections[1]
            q = projections[0]
            counter_outcome = INVERSE[target_outcome]
            totals[row['opponent']][counter_outcome] += 2
            key = row['candidate'], row['opponent']; assert key not in cells
            cells[key] = dict(counter_outcome=counter_outcome, hp_counter_first=list(reversed(hp)),
                              rounds=end, selected=selected, projection=q)
            table.append(f'| {row["candidate"]} | {row["opponent"]} | {selected} | {q["enemy_route_length"]} | '
                         f'{q["projected_lead"]} | {counter_outcome} | {hp[1]}:{hp[0]} | {end} |')
        calls += sum(len(c['rounds']) for c in histories['cases'])
        filtered += sum(len(c['early_filtered_proposals']) + len(c['growth_filtered_proposals']) for c in histories['cases'])
        games += 48; assignments += 24
    controls, mistakes = [], []
    if repair:
        path = R/'route-selector-controls-001.json'; inputs[str(path)] = digest(path)
        control = json.loads(path.read_text())
        assert control['all_passed'] and len(control['pairs']) == 48
        assert all(pair['same_complete_trajectory'] for pair in control['pairs'])
        assert all(digest(path) == sha for path, sha in control['input_sha256'].items())
        controls = control['pairs']
        verdict = ('CONFIRMED' if totals['route_adaptive']['L'] == 0 else 'REFUTED') + (
            ': the route gate removes the ten previous adaptive losses on the disclosed24-target development set.'
        )
        # Four distinct opening parameters must all still be beaten.
        preserved = all(cells[t, 'route_adaptive']['counter_outcome'] == 'W'
                        for t in ('P5M_poke0', 'P5M_poke2', 'P5M_poke3', 'P5M_poke4'))
        assert preserved
        explanation = ('The route gate is a repair chosen after the previous outcomes were known. '
            'It keeps the early strike for a positive no-enemy-action projection only when the visible enemy route '
            'is longer than the spawn/base Manhattan distance. Otherwise it chooses growth. The early and growth '
            'branches are unchanged. Forty-eight predeclared comparisons reproduce the corresponding old forced-branch '
            'histories, so the improvement is attributable to selecting between these branches on this fixed set. '
            'The old controls add no independent sample. All four declared nominee opening-count variants remain wins. '
            'An aggressive route-building challenge is reported separately, with no general robustness inference here.')
    else:
        for target in sorted({t for t, mode in cells}):
            adaptive = cells[target, 'route_adaptive']; selected = adaptive['selected']
            other = 'growth' if selected == 'early' else 'early'
            for side in (0, 1):
                a, b = records[target, 'route_adaptive', side], records[target, 'route_'+selected, side]
                same = a['canonical_replay_sha256'] == b['canonical_replay_sha256']
                assert same, (target, side, selected)
                controls.append(dict(target=target, side=side, selected=selected,
                    same_complete_trajectory=True, adaptive=a['result_path'], forced=b['result_path'],
                    canonical_sha256=a['canonical_replay_sha256']))
            alternative = cells[target, 'route_'+other]
            if adaptive['counter_outcome'] == 'L' and alternative['counter_outcome'] in ('W', 'D'):
                mistakes.append(dict(target=target, selected=selected, hp_counter_first=adaptive['hp_counter_first'],
                    alternative=other, alternative_outcome=alternative['counter_outcome'],
                    alternative_hp_counter_first=alternative['hp_counter_first']))
        verdict = ('CONFIRMED' if mistakes else 'OPEN') + (
            ': the declared route-builder matrix contains a selector loss avoided by its alternative fixed branch.'
        )
        explanation = ('The sixteen opponents are existing MazeGrower policies: four exact layouts, growth through '
            'round3 or6, and repeated tier1 or tier5 purchases thereafter. There is no bait. All targets and all three '
            'modes are retained below. The predicate uses public geometry, but geometry does not restrict hidden current '
            'or later purchases. This matrix challenges the selection rule after its repair; it is development evidence, '
            'not a random draw of unseen opponents. Every adaptive history agrees with its selected forced branch. '
            'A different fixed branch can still lose, so none is claimed to dominate the others.')
    scores = '; '.join(f'{mode}: {v["W"]}W/{v["D"]}D/{v["L"]}L' for mode, v in totals.items())
    now = datetime.now(timezone.utc).isoformat()
    text = f'''# Route-gated selection: {args.experiment}

Checked {now}.

{verdict}

Counter outcomes: {scores}.

{explanation}

'''
    if mistakes:
        text += 'Controlled failure witnesses, with HP from the counter perspective:\n\n'
        text += '\n'.join('- `'+m['target']+'`: '+m['selected']+' loses '+str(m['hp_counter_first'])+
            '; '+m['alternative']+' gives '+m['alternative_outcome']+' '+str(m['alternative_hp_counter_first'])+'.'
            for m in mistakes) + '\n\n'
    text += '''Each row represents both physical assignments with identical normalized histories. All outcomes and HP below are from the counter's perspective; the target name identifies the opposing policy.

| Target | Counter mode | Selected branch | Enemy route length at round4 | Projected lead | Counter outcome | HP counter:target | Final round |
|---|---|---|---:|---:|---|---|---:|
'''+ '\n'.join(table)+f'''

All{games} full games pass strict accounting, original-engine replay, source and data pinning, and fresh policy regeneration. All{calls} regenerated decisions reproduce their recorded submissions, leave the input observation unchanged and pass action legality. There are{filtered} locally filtered planner proposals; no submitted action is rejected. All{assignments} assignment pairs and{len(controls)} complete-history controls agree. Assignment swaps and fixed-branch controls are reproducibility evidence, not independent random samples.

The growth delegate retains a three-second planner cutoff. These observations do not establish unconditional reproducibility under arbitrary machine load. Selection reads only public observations and legitimate local state. The installed best_v9e and the pool-C validation are unchanged by this experiment.

The manifests, strict/replay/data/history audits and pipeline logs are listed by digest in verification/full_games.json. Reproduce using run_data_development on the named manifests, audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, and check_route_histories, under the documented project-root Python environment, disabled bytecode, assigned affinity, single thread and low priority. The repair also uses the separately declared compare_recorded_controls input.
'''
    result_path = area/'RESULTS.md'
    with result_path.open('x') as f: f.write(text)
    for path in (result_path, area/'PROOF.md', Path(__file__).relative_to(Path.cwd())):
        inputs[str(path)] = digest(path)
    result = dict(time_utc=now, all_passed=True, games=games, fresh_decisions=calls,
        local_filtered_proposals=filtered, identical_assignment_pairs=assignments,
        exact_control_pairs=len(controls), controls=controls, input_sha256=inputs,
        counter_outcomes_by_mode=dict(totals), failures_avoided_by_alternative=mistakes,
        verdict=verdict, cells=[dict(target=t, mode=m, **c) for (t,m),c in cells.items()])
    with (area/'verification/full_games.json').open('x') as f:
        json.dump(result, f, sort_keys=True, indent=2); f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {now}: Route selection {args.experiment} fully audited\n\nClaim and verdict: {verdict}\n\n'
            f'Method and result:{games} declared games; {scores}. All{calls} fresh decisions, {assignments} assignment '
            f'pairs and{len(controls)} exact history controls pass, with no bot errors or submitted rejections. '
            f'Controlled failures: '+json.dumps(mistakes)+'. Full table: '+str(result_path)+
            '. Development evidence only; installed bot and pool C unchanged.\n')
    print(json.dumps(dict(time_utc=now, games=games, calls=calls, scores=dict(totals),
                         exact_controls=len(controls), verdict=verdict, witnesses=mistakes)))


if __name__ == '__main__':
    main()

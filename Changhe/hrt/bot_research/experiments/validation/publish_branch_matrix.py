"""Publish audited route-branch transfer and anonymous-prefix matrices."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction
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
    parser.add_argument('--experiment', choices=('transfer', 'prefix'), required=True)
    args = parser.parse_args()
    prefix = args.experiment == 'prefix'
    name = 'prefix-fork-001' if prefix else 'route-transfer-001'
    topic = 'indistinguishable_prefix' if prefix else 'route_selector_transfer'
    area = E/'analysis'/topic
    inputs = {}

    def read(path):
        inputs[str(path)] = digest(path)
        return json.loads(path.read_text())

    manifest = read(E/(name+'.json'))
    expected = manifest['expected_conditions']
    audits = {kind: read(R/(name+'-'+kind+'.json'))
              for kind in ('strict', 'replay', 'summary', 'data', 'histories')}
    strict, summary, histories = (audits[k] for k in ('strict', 'summary', 'histories'))
    assert strict['valid_conditions'] == strict['expected_conditions'] == expected
    assert summary['valid_conditions'] == summary['expected_conditions'] == expected
    assert summary['unresolved_conditions'] == 0 and not summary['repeat_disagreements']
    assert summary['complete_assignment_pairs'] == summary['identical_assignment_pairs'] == expected//2
    assert audits['replay']['all_passed'] and audits['replay']['count'] == expected
    assert audits['data']['all_passed']
    assert all(histories[k] for k in ('all_fresh_actions_legal', 'all_observations_unchanged',
        'all_public_selections_verified', 'all_replayed', 'exact_counter_policy_reproduction'))
    assert all(digest(p) == h for p, h in histories['input_sha256'].items())
    records, cells, totals, table = {}, {}, defaultdict(Counter), []
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
        selected = {c['selected'] for c in cases}
        assert len(selected) == 1
        selected = next(iter(selected))
        projections = [next(r['projection'] for r in c['rounds'] if r['round'] == 4) for c in cases]
        assert projections[0] == projections[1]
        q = projections[0]
        outcome = INVERSE[target_outcome]
        totals[row['opponent']][outcome] += 2
        key = row['candidate'], row['opponent']
        assert key not in cells
        cells[key] = dict(counter_outcome=outcome, hp_counter_first=list(reversed(hp)),
                         rounds=end, selected=selected, projection=q)
        table.append(f'| {row["candidate"]} | {row["opponent"]} | {selected} | {q["enemy_route_length"]} | '
                     f'{q["projected_lead"]} | {outcome} | {hp[1]}:{hp[0]} | {end} |')
    controls = []
    for target in sorted({target for target, mode in cells}):
        selected = cells[target, 'route_adaptive']['selected']
        for side in (0, 1):
            a, b = records[target, 'route_adaptive', side], records[target, 'route_'+selected, side]
            assert a['canonical_replay_sha256'] == b['canonical_replay_sha256']
            controls.append(dict(target=target, side=side, selected=selected,
                adaptive=a['result_path'], forced=b['result_path'], canonical_sha256=a['canonical_replay_sha256']))
    calls = sum(len(c['rounds']) for c in histories['cases'])
    extra = {}
    if prefix:
        p = read(R/(name+'-prefixes.json'))
        assert all(p[k] for k in ('all_prefixes_equal', 'all_fresh_decisions_equal',
                                  'all_observations_unchanged', 'all_actions_legal', 'all_replayed'))
        assert len(p['cases']) == expected and len(p['comparisons']) == 10
        assert all(digest(path) == sha for path, sha in p['input_sha256'].items())
        pair = {'baseline': {'route_early': 'W', 'route_growth': 'L'},
                'flood': {'route_early': 'L', 'route_growth': 'W'}}
        opposite = all(cells[target, mode]['counter_outcome'] == value
                       for target, modes in pair.items() for mode, value in modes.items())
        a = E/'run_data_development.py'
        b = E/'run_anonymous_development.py'
        transformed = a.read_text().replace("names=[candidate['id'],opponent['id']]", "names=['anonymous_target','anonymous_selector']")
        transformed = transformed.replace('bot_research.experiments.validation.run_data_development',
                                           'bot_research.experiments.validation.run_anonymous_development')
        transformed = transformed.replace('Fresh-process development matrix with explicit manifests and frozen sources.',
                'Anonymous public names in a fresh-process, explicitly declared development matrix.')
        assert b.read_text() == transformed
        inputs[str(a)] = digest(a); inputs[str(b)] = digest(b)
        extra.update(full_prefix_comparisons=10, both_policy_fresh_decisions=sum(len(c['decisions']) for c in p['cases']),
                     opposite_outcomes=opposite, anonymous_wrapper_exact_transformation=True)
        if opposite:
            payoff = [[1, -1], [-1, 1]]
            half = Fraction(1, 2)
            row_mix = [sum(half*payoff[i][j] for i in (0, 1)) for j in (0, 1)]
            column_mix = [sum(half*payoff[i][j] for j in (0, 1)) for i in (0, 1)]
            assert row_mix == column_mix == [0, 0]
            extra['restricted_game'] = dict(rows=['early', 'growth'], columns=['baseline', 'flood'],
                payoff=payoff, row_mixture=['1/2', '1/2'], column_mixture=['1/2', '1/2'], value='0')
        verdict = ('CONFIRMED' if opposite else 'REFUTED') + ': opposite fixed-branch preferences after identical full public prefixes.'
        explanation = ('The targets share the same P5TNUBM opening with no round-one poke. Baseline continues that policy; '
            'flood buys tier1 entries from round4. Public names are held fixed. All ten full-prefix comparisons agree, '
            'including the entire observations before rounds1,2,3 and4, without masking names or other fields. '
            'Both policies were freshly regenerated on every recorded observation, in addition to the route-selector check. ')
        if opposite:
            explanation += ('Each deterministic selector that commits to E or G from this common history must lose to one '
                'of these two targets. The equal mixture has exact maximin utility0 in this two-by-two W/L game, '
                'with win utility+1 and loss utility-1. A third policy, another opening or later adaptation is outside this '
                'statement. No impossibility for the full game follows.')
    else:
        passed = totals['route_adaptive']['L'] == 0
        verdict = ('CONFIRMED' if passed else 'REFUTED') + ': the unchanged adaptive selector avoids defeat on the five declared transfer targets.'
        explanation = ('These five frozen teammate policies were selected before this30-game transfer matrix. '
            'Every target and all three counter modes are retained. The test extends development coverage, '
            'without creating held-out evidence or altering the installed bot. The separately reported route-builder '
            'challenge exposes losses of this same selector and must be considered alongside this table. '
            'The defense worker retains fortress38 as its recommendation and describes fortress39 as a trade-off.')
    scores = '; '.join(f'{mode}: {v["W"]}W/{v["D"]}D/{v["L"]}L' for mode, v in totals.items())
    now = datetime.now(timezone.utc).isoformat()
    text = f'''# Route-branch {args.experiment} results

Checked {now}.

{verdict}

Counter outcomes: {scores}.

{explanation}

Each row represents both physical assignments, which have identical normalized complete trajectories. Outcomes and HP are from the counter perspective.

| Target | Counter mode | Selected branch | Enemy route length at round4 | Projected lead | Counter outcome | HP counter:target | Final round |
|---|---|---|---:|---:|---|---|---:|
'''+ '\n'.join(table)+f'''

All{expected} games pass strict accounting, original-engine replay, pinned source and data checks, and fresh selector regeneration. All{calls} fresh selector decisions agree and leave observations unchanged; no submitted action is rejected and no bot error occurs. There are{expected//2} identical assignment pairs and{len(controls)} exact adaptive-versus-selected-branch controls. Repeated deterministic trajectories are reproducibility checks, not independent samples. The growth planner retains a three-second cutoff; these observed identities are not an unconditional guarantee under arbitrary load.

The proof gives exact hypotheses and scope. verification/full_games.json pins the manifests, audit receipts, result and replay files, and publisher. Reproduction uses {'run_anonymous_development' if prefix else 'run_data_development'} with {name}.json, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives and check_route_histories{', followed by check_prefix_fork' if prefix else ''}. Use the documented project-root environment, existing Python, disabled bytecode, assigned affinity, one thread and low priority. This development experiment does not change best_v9e or its final pool-C evidence.
'''
    if prefix:
        text += f'\nThe independent both-policy check regenerates{extra["both_policy_fresh_decisions"]} decisions and validates ten complete public-prefix equalities. The anonymous wrapper is verified as an exact transformation of the standard wrapper affecting only display names, its self-source root and its module description.\n'
    result_path = area/'RESULTS.md'
    with result_path.open('x') as f:
        f.write(text)
    for path in (result_path, area/'PROOF.md', Path(__file__).relative_to(Path.cwd())):
        inputs[str(path)] = digest(path)
    result = dict(time_utc=now, all_passed=True, games=expected, fresh_selector_decisions=calls,
        counter_outcomes_by_mode=dict(totals), exact_control_pairs=len(controls), controls=controls,
        verdict=verdict, input_sha256=inputs, cells=[dict(target=t, mode=m, **cell) for (t,m),cell in cells.items()], **extra)
    with (area/'verification/full_games.json').open('x') as f:
        json.dump(result, f, indent=2, sort_keys=True); f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {now}: Route-branch {args.experiment} complete\n\nClaim and verdict: {verdict}\n\n'
                f'Method and result:{expected} declared games; {scores}. All{calls} fresh selector decisions and'
                f'{len(controls)} complete selected-branch controls agree; all engine/source/data audits pass. '
                + explanation + f' Full evidence: {result_path}.\n')
    print(json.dumps(dict(time_utc=now, games=expected, scores=dict(totals), verdict=verdict, **extra)))


if __name__ == '__main__':
    main()

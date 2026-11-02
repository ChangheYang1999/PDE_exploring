"""Publish the complete predeclared early-wall policy comparison."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
AREA = E/'analysis/early_wall_policy'


def main():
    inputs = {}
    def digest(p):
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)] = digest(p)
        return json.loads(Path(p).read_text())
    def verify(mapping):
        for p, h in mapping.items():
            assert digest(p) == h, p
            inputs[p] = h
    declaration = read(E/'early-wall-campaigns-001.json')
    component = read(AREA/'verification/component.json')
    assert component['all_passed']
    assert len(component['cases']) == 16
    verify(component['input_sha256'])
    witnesses = read('bot_research/bots/counters/data/early_wall_guard_001.json')
    assert [w['id'] for w in witnesses['witnesses']] == [f'guard{i:02d}' for i in range(8)]
    rows = []
    pairs = []
    checked_calls = forecast_calls = filtered = 0
    for item in declaration['campaigns']:
        name = item['name']
        expected = item['expected']
        manifest = read(E/(name+'.json'))
        verify(manifest['input_sha256'])
        audit = {k:read(R/(name+'-'+k+'.json')) for k in
                 ('strict', 'replay', 'summary', 'data', 'fresh')}
        assert audit['strict']['valid_conditions'] == expected
        assert audit['strict']['attempt_counts'] == {'valid':expected}
        assert not audit['strict']['unresolved']
        assert not audit['strict']['repeat_disagreements']
        assert audit['replay']['all_passed'] and audit['replay']['count'] == expected
        assert audit['data']['all_passed']
        fresh = audit['fresh']
        assert all(fresh[k] for k in ('all_passed', 'all_replayed',
                   'all_actions_legal', 'all_observations_unchanged'))
        assert fresh['games'] == expected
        verify(fresh['input_sha256'])
        checked_calls += fresh['checked_calls']
        filtered += fresh['filtered_proposals']
        fresh_cases = {c['result']:c for c in fresh['cases']}
        if item['kind'] == 'clone':
            forecast = read(R/(name+'-forecast.json'))
            assert all(forecast[k] for k in ('all_fresh_actions_agree',
                'all_predictions_exact', 'all_observations_unchanged',
                'all_fresh_actions_legal', 'all_original_combat_agrees'))
            verify(forecast['input_sha256'])
            forecast_calls += forecast['checked_calls']
        grouped = defaultdict(list)
        for job in read(R/name/'jobs.json'):
            path = R/name/'results'/(job['id']+'.json')
            row = checked_row(str(path), inputs)
            c = row['condition']
            fc = fresh_cases[str(path)]
            assert fc['witness'] == item['witness']
            reverse = item['kind'] == 'clone'
            side = 1-c['candidate_side'] if reverse else c['candidate_side']
            outcome = {'W':'L','L':'W','D':'D'}[row['outcome']] if reverse else row['outcome']
            hp = row['hp_candidate_first'][::-1] if reverse else row['hp_candidate_first']
            timing = row['decision_seconds_candidate_first'][::-1] if reverse else row['decision_seconds_candidate_first']
            opponent = 'matching_r3_tier2_clone' if reverse else c['opponent_id']
            policy_spec = c['opponent_spec'] if reverse else c['candidate_spec']
            opponent_spec = c['candidate_spec'] if reverse else c['opponent_spec']
            x = dict(witness=item['witness'], kind=item['kind'], policy_spec=policy_spec,
                opponent=opponent, opponent_spec=opponent_spec, side=side,
                outcome=outcome, hp=hp, rounds=row['rounds'],
                decision_seconds_policy_first=timing, result=str(path),
                canonical_replay_sha256_candidate_perspective=row['canonical_replay_sha256'],
                filtered_proposals=fc['filtered_proposals'], guard_trace=fc['guard_trace'])
            rows.append(x)
            grouped[(policy_spec, opponent_spec)].append(x)
        for specs, rr in grouped.items():
            assert len(rr) == 2 and {x['side'] for x in rr} == {0,1}
            rr.sort(key=lambda x:x['side'])
            pairs.append(dict(witness=item['witness'],kind=item['kind'],
                policy_spec=specs[0],opponent_spec=specs[1],opponent=rr[0]['opponent'],
                outcomes=[x['outcome'] for x in rr],
                same_history=rr[0]['canonical_replay_sha256_candidate_perspective'] == rr[1]['canonical_replay_sha256_candidate_perspective']))
    assert len(rows) == 80 and len(pairs) == 40
    assert sum(r['kind'] == 'team' for r in rows) == 64
    assert sum(r['kind'] == 'clone' for r in rows) == 16
    assert checked_calls == sum(2*r['rounds'] for r in rows)
    assert forecast_calls == sum(r['rounds'] for r in rows if r['kind'] == 'clone')
    first_clone = [r for r in rows if r['witness'] == 'guard00' and r['kind'] == 'clone']
    assert len(first_clone) == 2
    h1 = all(r['outcome'] == 'W' for r in first_clone)
    nonlosing = []
    for i in range(8):
        w = f'guard{i:02d}'
        rr = [r for r in rows if r['witness'] == w and r['kind'] == 'team']
        assert len(rr) == 8
        if all(r['outcome'] != 'L' for r in rr):
            nonlosing.append(w)
    h2 = bool(nonlosing)
    stamp = datetime.now(timezone.utc).isoformat()
    targets = ['best_v9e','fortress41','V33C','P5TNUBM','matching_r3_tier2_clone']
    assert {r['opponent'] for r in rows} == set(targets)
    lines = ['# Early walls in complete games', '', f'Checked {stamp}.', '',
        f'The predeclared strict-win claim for guard00 against its updated public-state forecaster is {"CONFIRMED" if h1 else "REFUTED"}. The separate claim that some fixed witness avoids loss on all four teammate opponents is {"CONFIRMED" if h2 else "REFUTED"}. All eighty declared conditions are included.', '',
        'Each policy uses a registered wall layout in round one or two, its selected guard turret in round three, a tier4 purchase in round four when affordable, and the frozen Fortress38 continuation from round five. The earlier component established a feasible cash and defense schedule. This comparison measures the resulting complete games.', '',
        'Cells give policy outcome, policy:opponent HP and ending round. Equal assignments share a cell. The last column uses a separately updated matching model for each row; it is one fixed attack setting, round three and tier2.', '',
        '| Witness | best_v9e | Fortress41 | V33C | P5TNUBM | Matching clone |',
        '|---|---|---|---|---|---|']
    for i in range(8):
        w = f'guard{i:02d}'
        cells = []
        for target in targets:
            rr = sorted((r for r in rows if r['witness'] == w and r['opponent'] == target),key=lambda r:r['side'])
            assert len(rr) == 2
            vv = [f'{r["outcome"]} {r["hp"][0]}:{r["hp"][1]} r{r["rounds"]}' for r in rr]
            cells.append(vv[0] if vv[0] == vv[1] else 'seat0 '+vv[0]+'; seat1 '+vv[1])
        lines.append('| '+w+' | '+' | '.join(cells)+' |')
    lines += ['', 'Witnesses with no teammate loss: '+(', '.join(nonlosing) if nonlosing else 'none')+'. Choosing among these rows after reading the table is development selection, not held-out validation.', '',
        f'All {checked_calls} freshly regenerated decisions across both policies agree with the recorded actions. The clone audit additionally checks {forecast_calls} fresh forecasts against actual target actions and original incoming combat. Original-engine replay, complete registered source and data archives, legal submissions and observation immutability checks pass. The guard filtered {filtered} proposed actions before submission; these are recorded separately from rejected engine actions, of which there were none.', '',
        f'{sum(p["same_history"] for p in pairs)} of forty physical-assignment pairs have identical complete canonical histories. These are deterministic reproducibility checks. The independent conditions vary the witness and opposing policy, not a random seed.', '',
        '| Witness | Calls | Total policy decision seconds | Largest policy decision seconds |',
        '|---|---:|---:|---:|']
    timings = []
    for i in range(8):
        w = f'guard{i:02d}'
        tt = [r['decision_seconds_policy_first'][0] for r in rows if r['witness'] == w]
        t = dict(witness=w,calls=sum(x['calls'] for x in tt),total=sum(x['total'] for x in tt),maximum=max(x['max'] for x in tt))
        timings.append(t)
        lines.append(f'| {w} | {t["calls"]} | {t["total"]:.6f} | {t["maximum"]:.6f} |')
    lines += ['', 'Timing covers actual game decisions, excluding subsequent audit replay. All games used one assigned CPU core at low priority with one numerical thread on the shared machine. These timings are execution measurements, not hardware-independent complexity bounds.', '',
        'The matching forecaster is allowed to decline a purchase that cannot damage its predicted defense. A draw in this column therefore does not mean four tier2 copies were submitted in that game; the direct four-copy defense was checked separately in the earlier-wall component. Other attack rounds, tiers, mixed rosters and adaptive opponents remain outside this matrix.', '',
        'Reproduce the sixteen manifests listed in early-wall-campaigns-001.json with modules bot_research.experiments.validation.run_data_development (teammates) or bot_research.experiments.validation.run_data_forecasts (clones). Run audit_development_strict, replay_audit, audit_data_archives and check_early_wall_histories for each campaign; clone campaigns also require check_timing_forecaster_histories. Exact bounded commands are retained in runs/validation/early-wall-team-001-pipeline.log and early-wall-clone-001-pipeline.log. Use the existing Python with bytecode disabled, research temporary directory, assigned affinity, low priority and one numerical thread.', '']
    out = AREA/'RESULTS.md'
    with out.open('x') as f:
        f.write('\n'.join(lines))
    for p in (out, AREA/'PROOF.md',Path(__file__).relative_to(Path.cwd())):
        inputs[str(p)] = digest(p)
    result = dict(time_utc=stamp,all_audits_passed=True,games=80,fresh_decisions=checked_calls,
        additional_forecast_calls=forecast_calls,filtered_proposals=filtered,
        first_witness_strict_clone_win=h1,some_witness_no_teammate_loss=h2,
        nonlosing_team_witnesses=nonlosing,pairs=pairs,rows=rows,timings=timings,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Early-wall full matrix complete\n\nClaim and verdict: guard00 strict clone win {"CONFIRMED" if h1 else "REFUTED"}; existence of a fixed witness with no teammate loss {"CONFIRMED" if h2 else "REFUTED"}. All80games, {checked_calls} fresh decisions and {forecast_calls} fresh forecasts pass the original-engine, source, legality and observation checks. Nonlosing witnesses: {", ".join(nonlosing) or "none"}. Filtered proposals: {filtered}; engine rejections and bot errors: zero. Full condition table and timing: {out}. These are development results; the clone setting is only round3/tier2.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('pairs','rows','timings','input_sha256')}))


if __name__ == '__main__':
    main()

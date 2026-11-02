"""Publish the declared guard00 timing grid against correctly updated private models."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E/'analysis/early_wall_forecaster'
INVERSE = {'W':'L', 'L':'W', 'D':'D'}
RANK = {'L':0, 'D':1, 'W':2}


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
    def parameters(spec):
        return {k:json.loads(v[0]) for k, v in parse_qs(spec.partition('?')[2]).items()}
    declaration = read(E/'early-wall-forecaster-campaigns-001.json')
    assert declaration['games'] == 40 and len(declaration['controls']) == 40
    component = read(A/'verification/component.json')
    assert component['all_passed'] and component['prefixes'] == 8
    verify(component['input_sha256'])
    old_receipts = [read(E/'analysis'/area/'verification/full_games.json') for area in
                    ('delegated_forecaster', 'forced_early_forecaster')]
    for receipt in old_receipts:
        assert receipt['all_audits_passed']
        verify(receipt['input_sha256'])
    cases = {}
    fresh_calls = forecast_calls = filtered = same_pairs = 0
    for item in declaration['campaigns']:
        name = item['name']
        manifest = read(E/(name+'.json'))
        verify(manifest['input_sha256'])
        audits = {k:read(R/(name+'-'+k+'.json')) for k in
                  ('strict', 'replay', 'summary', 'data', 'fresh', 'forecast')}
        strict, replay, fresh, forecast = (audits[k] for k in ('strict','replay','fresh','forecast'))
        assert strict['valid_conditions'] == 8 and strict['attempt_counts'] == {'valid':8}
        assert not strict['unresolved'] and not strict['repeat_disagreements']
        assert replay['all_passed'] and replay['count'] == 8 and audits['data']['all_passed']
        assert audits['summary']['valid_conditions'] == 8
        assert audits['summary']['complete_assignment_pairs'] == 4
        same_pairs += audits['summary']['identical_assignment_pairs']
        assert fresh['games'] == 8 and all(fresh[k] for k in
            ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'))
        assert all(forecast[k] for k in ('all_fresh_actions_agree','all_predictions_exact',
                   'all_observations_unchanged','all_fresh_actions_legal','all_original_combat_agrees'))
        verify(fresh['input_sha256'])
        verify(forecast['input_sha256'])
        fresh_calls += fresh['checked_calls']
        forecast_calls += forecast['checked_calls']
        filtered += fresh['filtered_proposals']
        for case in fresh['cases']:
            assert case['result'] not in cases and case['witness'] == 'guard00'
            cases[case['result']] = case
    assert len(cases) == 40
    modes = ('adaptive', 'early', 'guard')
    counts = {mode:Counter() for mode in modes}
    timing = {mode:{who:dict(calls=0,total_seconds=0.0,max_seconds=0.0)
                   for who in ('target','attacker')} for mode in modes}
    comparisons = []
    transitions = {mode:Counter() for mode in ('adaptive','early')}
    for pair in declaration['controls']:
        checked = {mode:checked_row(pair[mode],inputs) for mode in modes}
        raw = {mode:read(row['result_path']) for mode, row in checked.items()}
        params = {}
        values = {}
        for mode, row in checked.items():
            c = row['condition']
            assert c['candidate_id'] == pair['setting'] and c['candidate_side'] == pair['forecaster_side']
            p = parameters(c['candidate_spec'])
            model = p.pop('model_spec')
            model_params = p.pop('model_parameters')
            if mode == 'guard':
                assert model == 'bot_research.bots.counters.early_wall_guard:@make'
                assert model_params == {'witness':'guard00'}
            else:
                assert model == 'bot_research.bots.counters.delegated_defense:@make'
                assert model_params == ({'delegate':'fortress38'} if mode == 'adaptive' else
                                        {'delegate':'fortress38','mode':'early'})
            params[mode] = p
            outcome = INVERSE[row['outcome']]
            counts[mode][outcome] += 1
            trace = raw[mode]['forecast_trace']
            assert len(trace) == row['rounds']
            values[mode] = dict(outcome=outcome,hp=row['hp_candidate_first'][::-1],
                rounds=row['rounds'],attack_count=sum(t['attack_count'] for t in trace),
                attack_rounds=[t['round'] for t in trace if t['attack_count']],
                canonical_replay_sha256=row['canonical_replay_sha256'])
            for who, tm in zip(('attacker','target'), row['decision_seconds_candidate_first']):
                dest = timing[mode][who]
                dest['calls'] += tm['calls']
                dest['total_seconds'] += tm['total']
                dest['max_seconds'] = max(dest['max_seconds'],tm['max'])
        assert params['adaptive'] == params['early'] == params['guard']
        for mode in transitions:
            transitions[mode][values[mode]['outcome']+'->'+values['guard']['outcome']] += 1
        comparisons.append(dict(**pair,parameters=params['guard'],target_side=1-pair['forecaster_side'],
            results=values,filtered_proposals=cases[pair['guard']]['filtered_proposals']))
    assert counts['adaptive'] == Counter(W=0,D=2,L=38)
    assert counts['early'] == Counter(W=6,D=10,L=24)
    assert fresh_calls == 2*sum(x['results']['guard']['rounds'] for x in comparisons)
    assert forecast_calls == sum(x['results']['guard']['rounds'] for x in comparisons)
    repeats = []
    for control in declaration['repeat_controls']:
        old, new = (checked_row(control[k],inputs) for k in ('a','b'))
        assert old['canonical_replay_sha256'] == new['canonical_replay_sha256']
        repeats.append(dict(**control,exact=True))
    assert len(repeats) == 2
    improvements = sum(RANK[x['results']['guard']['outcome']] > RANK[x['results']['early']['outcome']] for x in comparisons)
    regressions = sum(RANK[x['results']['guard']['outcome']] < RANK[x['results']['early']['outcome']] for x in comparisons)
    h1 = counts['guard']['L'] == 0
    h2 = regressions == 0 and improvements > 0
    verdict = lambda b:'CONFIRMED' if b else 'REFUTED'
    score = lambda c:f'{c["W"]}W/{c["D"]}D/{c["L"]}L'
    grouped = defaultdict(list)
    for row in comparisons:
        grouped[row['setting']].append(row)
    assert len(grouped) == 20
    table = []
    for setting, rows in sorted(grouped.items()):
        assert {r['target_side'] for r in rows} == {0,1}
        cells = []
        for mode in modes:
            values = []
            for row in sorted(rows,key=lambda x:x['target_side']):
                v = row['results'][mode]
                values.append(f'{v["outcome"]} {v["hp"][0]}:{v["hp"][1]} r{v["rounds"]}; buys {v["attack_count"]}')
            cells.append(values[0] if values[0] == values[1] else 'seat0 '+values[0]+'; seat1 '+values[1])
        table.append('| '+setting+' | '+' | '.join(cells)+' |')
    stamp = datetime.now(timezone.utc).isoformat()
    text = f'''# Early-wall guard against matching timing attackers

Checked {stamp}.

The no-loss claim is {verdict(h1)}. The stricter paired improvement claim over the forced-early target is {verdict(h2)}: {improvements} improved settings and assignments, {regressions} regressions. The fixed guard scores {score(counts['guard'])}; the adaptive delegated target scored {score(counts['adaptive'])}, and its forced-early version {score(counts['early'])}.

This table includes all twenty timing configurations and both assignments. Each attacker predicts the actual target policy through a private public-state model. Replacing the target therefore also replaces the attacker's model. These are comparisons against a matching-model adversary family, not an ablation against one unchanged opposing policy. The earlier round-three/tier2/defense-first=false draw is repeated in two explicitly labeled control games; the other nineteen settings were new for this fixed guard when declared.

Cells give target outcome, target:attacker HP, ending round, and the total number of attacker roster purchases recorded in its trace. An attacker can decline an unprofitable purchase. A draw with zero purchases does not independently demonstrate survival of the nominal attack.

| Configuration | Adaptive delegate | Forced early delegate | Early-wall guard00 |
|---|---|---|---|
'''+ '\n'.join(table)+f'''

All forty new games pass strict accounting, original-engine replay, registered source/data checks, and complete fresh reconstruction of both policies. The new checks reproduce {fresh_calls} policy calls and independently verify {forecast_calls} attacker predictions and incoming combat results. The guard filters {filtered} proposed actions before submission; the engine rejects none, and there are no bot errors. All eight predeclared component prefixes pass. Both earlier draw controls reproduce exactly. {same_pairs} of twenty assignment pairs have identical normalized complete histories.

The controls are eighty previously audited games. They do not add eighty new executions here. This is targeted development evidence selected after earlier counterexamples, not reserved final validation. It establishes only the finite table and its recorded execution behavior. It does not prove global optimality or load-independent behavior for wall-clock-limited planning.

Full per-game source/result references, attack rounds, outcome transitions and measured decision times are in verification/full_games.json. Reproduce the five manifests listed in early-wall-forecaster-campaigns-001.json using run_data_forecasts, audit_development_strict, replay_audit, audit_data_archives, check_early_wall_histories and check_timing_forecaster_histories. The bounded pipeline log records exact commands. Use the original environment from the project root with disabled bytecode, the research temporary directory, one assigned low-priority core and one numerical thread.
'''
    output = A/'RESULTS.md'
    with output.open('x') as f:
        f.write(text)
    for p in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):
        inputs[str(p)] = digest(p)
    receipt = dict(time_utc=stamp,all_audits_passed=True,new_games=40,old_control_games=80,
        no_loss_verdict=verdict(h1),paired_improvement_verdict=verdict(h2),target_outcomes=counts,
        transitions_to_guard=transitions,improvements=improvements,regressions=regressions,
        fresh_calls=fresh_calls,forecast_calls=forecast_calls,filtered_proposals=filtered,
        identical_assignment_pairs=same_pairs,repeats=repeats,timing=timing,
        comparisons=comparisons,input_sha256=inputs)
    with (A/'verification/full_games.json').open('x') as f:
        json.dump(receipt,f,indent=2,sort_keys=True)
        f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Early-wall matching-model grid complete\n\nClaim and verdict: no loss {verdict(h1)}; paired improvement over forced early {verdict(h2)}. Method: forty new games on the fixed twenty-setting timing grid, with correctly updated target models and eighty explicit old controls. Result: guard {score(counts["guard"])}, forced early {score(counts["early"])}, adaptive {score(counts["adaptive"])}; {improvements} improvements and {regressions} regressions from forced early. All {fresh_calls} fresh calls, {forecast_calls} forecast checks, original-engine replays and source/data audits pass; two known draw repeats agree. Development evidence. Full table: {output}.\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('comparisons','input_sha256','timing','repeats')}))


if __name__ == '__main__':
    main()

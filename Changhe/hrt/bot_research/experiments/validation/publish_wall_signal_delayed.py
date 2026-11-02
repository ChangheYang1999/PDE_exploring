"""Publish the full predeclared delayed twenty-wall attack grid."""
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E / 'analysis/wall_signal_delayed'


def main():
    inputs = {}
    digest = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)] = digest(p)
        return json.loads(Path(p).read_text())
    def verify(mapping):
        for p, h in mapping.items():
            assert digest(p) == h, p
            inputs[p] = h
    declaration = read(E / 'wall-signal-delayed-campaigns-001.json')
    verify(declaration['input_sha256'])
    component = read(A / 'verification/components.json')
    assert component['all_passed'] and len(component['cases']) == 24
    verify(component['input_sha256'])
    rows, groups, fresh, extra = [], defaultdict(list), 0, 0
    for campaign in declaration['campaigns']:
        name, label = campaign['name'], campaign['label']
        root = R / name
        audits = {k: read(R / (name + '-' + k + '.json')) for k in ('strict', 'replay', 'data', 'fresh', 'forecasts')}
        strict = audits['strict']
        assert strict['valid_conditions'] == strict['expected_conditions'] == 6
        assert strict['attempt_counts'] == {'valid': 6} and not strict['unresolved'] and not strict['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count'] == 6 and audits['data']['all_passed']
        for key in ('fresh', 'forecasts'):
            audit = audits[key]
            assert all(audit[k] for k in ('all_passed', 'all_replayed', 'all_actions_legal', 'all_observations_unchanged'))
            verify(audit['input_sha256'])
        fresh += audits['fresh']['checked_calls']
        extra += audits['forecasts']['checked_calls']
        traces = {x['result_path']: x for x in audits['forecasts']['cases']}
        freeze = read(root / 'freeze.json')
        verify({str(root / 'sources' / p): h for p, h in freeze['source_sha256'].items()})
        for job in read(root / 'jobs.json'):
            path = str(root / 'results' / (job['id'] + '.json'))
            record = checked_row(path, inputs)
            target = record['condition']['opponent_id']
            trace = traces[path]['rounds']
            attacks = [x for x in trace if x['attack_count']]
            row = dict(setting=label, target=target, record=record,
                       purchases=sum(x['attack_count'] for x in attacks),
                       forecast_mismatch_rounds=[x['round'] for x in trace if not x['model_matches']])
            rows.append(row)
            groups[(label, target)].append(row)
    assert len(rows) == 24 and fresh == 2 * extra
    for pair in groups.values():
        assert len(pair) == 2 and {x['record']['condition']['candidate_side'] for x in pair} == {0, 1}
        for key in ('outcome', 'hp_candidate_first', 'rounds', 'canonical_replay_sha256'):
            assert pair[0]['record'][key] == pair[1]['record'][key]
    one = lambda label, target: groups[(label, target)][0]
    score = {'W': 1, 'D': 0, 'L': -1}
    winners, improvements = [], []
    for campaign in declaration['campaigns']:
        label = campaign['label']
        j, h, i = (one(label, target)['record'] for target in ('J', 'H', 'I'))
        assert j['canonical_replay_sha256'] == h['canonical_replay_sha256']
        if j['outcome'] == 'W':
            winners.append(label)
        if score[j['outcome']] > score[i['outcome']]:
            improvements.append(label)
    h1, h2 = bool(winners), bool(set(winners) & set(improvements))
    stamp = datetime.now(timezone.utc).isoformat()
    lines = ['# Later purchases behind the same public wall signal', '', f'Checked {stamp}.', '',
             'H1, at least one setting beats J on the exact H-response history: ' + ('CONFIRMED' if h1 else 'REFUTED') + '.',
             'H2, at least one such setting has a strictly better outcome against J than against I: ' + ('CONFIRMED' if h2 else 'REFUTED') + '.', '',
             'All four attackers use the same twenty-wall first move and the same private H model. Only the declared purchase round and tier differ. '
             'The settings were selected from earlier successful attacks on wall-free H, after the nineteen-wall tier2 attack had lost its six games. '
             'This is targeted development, with no claim that the grid was sampled at random.', '',
             '| Setting | Opponent | Attacker result | HP attacker:opponent | End round | Units bought | Forecast mismatch count |',
             '|---|---|---|---|---:|---:|---:|']
    for campaign in declaration['campaigns']:
        label = campaign['label']
        for target in ('J', 'H', 'I'):
            row = one(label, target)
            r = row['record']
            lines.append(f'| {label} | {target} | {r["outcome"]} | {r["hp_candidate_first"][0]}:{r["hp_candidate_first"][1]} | {r["rounds"]} | {row["purchases"]} | {len(row["forecast_mismatch_rounds"])} |')
    lines += ['', 'Every displayed row represents both physical assignments, with identical normalized histories. '
              f'All 24 full games pass strict accounting, original-engine replay, archived-source and data checks, {fresh} fresh external decisions and {extra} additional attacker/forecast checks. '
              'The 24 prefix cases passed first. There were no submitted rejections, bot errors, source drift or mutated observations.', '',
              'Every J history exactly matches the corresponding H history. The private H forecasts agree against both targets; mismatches against I are retained. '
              'This confirms the selected response but does not by itself establish an exploit. The same attacker against I is the control for attributing an outcome difference to that response choice.', '',
              'Winning settings against J: ' + (', '.join(winners) if winners else 'none') + '. '
              'Settings whose outcome against J exceeds their outcome against I: ' + (', '.join(improvements) if improvements else 'none') + '.', '',
              'The results cover this declared grid only. A refuted hypothesis leaves other signal designs and purchase schedules open. '
              'The inherited branch proof assumes the observed common first move and correctly advanced private state; wall-clock-dependent choices outside the checked histories are not covered. '
              'Neither these policies nor their outcomes are used in pool D. Full timings, sources and commands are retained in the four manifests, verification/full_games.json and runs/validation/wall-signal-delayed-001-pipeline.log.', '']
    output = A / 'RESULTS.md'
    with output.open('x') as stream:
        stream.write('\n'.join(lines))
    inputs[str(output)] = digest(output)
    result = dict(time_utc=stamp, all_passed=True, new_games=24, h1=h1, h2=h2,
                  winning_settings=winners, better_against_J_than_I=improvements,
                  fresh_calls=fresh, forecast_checks=extra, rows=rows, input_sha256=inputs)
    atomic_json(A / 'verification/full_games.json', result, exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as stream:
        stream.write(f'\n## {stamp}: Delayed wall-signal grid complete\n\nH1 at least one win against J: ' + ('CONFIRMED' if h1 else 'REFUTED')
                     + '; H2 such a win improves on the I control: ' + ('CONFIRMED' if h2 else 'REFUTED')
                     + f'. Winning settings {winners}; outcome improvements over I {improvements}. '
                     + f'All 24 games, twelve assignment pairs, {fresh} fresh external decisions and {extra} forecast checks pass. '
                     + 'Every J history equals its H control. See experiments/validation/analysis/wall_signal_delayed/RESULTS.md. This is selected development evidence.\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('rows', 'input_sha256')}), flush=True)


if __name__ == '__main__':
    main()

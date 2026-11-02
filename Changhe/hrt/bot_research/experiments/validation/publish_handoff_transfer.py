"""Publish already audited finite handoff-transfer tables, without running policies."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json


SETTINGS = {
    'nominee-handoff': ('nominee_handoff', 'Early-defense nominees against disclosed handoff counters',
        'The disclosed counters do not all retain their wins: P5TNUBM wins all ten conditions. '
        'P4TNUB remains vulnerable to the public-HP trigger and both forecast deadlines. '
        'The original forecast model is deliberately unchanged and differs from both targets.'),
    'fortress36-handoff': ('fortress36_handoff', 'Frozen fortress v36 against disclosed handoff counters',
        'The claim that v36 wins all ten conditions is REFUTED: the public-HP trigger wins in both assignments. '
        'The four forecast and visible-roster settings are beaten. These are complete-policy results; '
        'they do not isolate either of v36\'s two added options.'),
    'retargeted-forecast': ('retargeted_forecast', 'Exact P5TNUBM forecasting does not restore the counter win',
        'The counter-repair hypothesis is REFUTED on both declared deadlines and assignments. '
        'The target remains undamaged and wins 800:755. Exact action prediction is confirmed on '
        'these 200 reached calls, but it supplies no winning guarantee.')}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', choices=SETTINGS, required=True)
    a = parser.parse_args()
    n = a.campaign
    topic, title, verdict = SETTINGS[n]
    e = Path('bot_research/experiments/validation')
    r = Path('bot_research/runs/validation')
    d = e / 'analysis' / topic
    paths = {k: r / f'{n}-{k}-001.json' for k in ('strict', 'replay', 'summary', 'data')}
    paths['forecast_histories'] = r / f'{n}-forecast-histories-001.json'
    paths['comparison'] = r / (f'{n}-comparison-001.json' if n == 'retargeted-forecast'
                              else f'{n}-forecast-comparison-001.json')
    if n != 'retargeted-forecast':
        paths['hp_histories'] = r / 'nominee-f36-hp-histories-001.json'
    data = {k: json.loads(p.read_text()) for k, p in paths.items()}
    s, f = data['summary'], data['forecast_histories']
    assert s['valid_conditions'] == s['expected_conditions']
    assert not s['repeat_disagreements']
    assert data['replay']['all_passed'] and data['data']['all_passed']
    assert f['exact_counter_policy_reproduction'] and f['all_replayed']
    assert f['all_observations_unchanged'] and f['all_fresh_actions_legal'] and f['no_internal_rejections']
    if 'hp_histories' in data:
        h = data['hp_histories']
        assert h['exact_policy_reproduction'] and h['no_post_handoff_attacks'] and h['no_internal_rejections']
    candidates = sorted({row['candidate'] for row in s['rows']})
    scores = {c: Counter() for c in candidates}
    rows = []
    for row in s['rows']:
        cases = row['results']
        assert len(cases) == 2 and {x['side'] for x in cases} == {0, 1}
        signatures = {(x['outcome'], tuple(x['hp']), x['rounds']) for x in cases}
        assert len(signatures) == 1
        x = cases[0]
        scores[row['candidate']].update(y['outcome'] for y in cases)
        rows.append(f"| {row['candidate']} | {row['opponent']} | {x['outcome']} | {x['hp'][0]}:{x['hp'][1]} | {x['rounds']} |")
    decisions = sum(len(x['rounds']) for x in f['cases'])
    bad_model = sum(len(x['model_action_differences']) for x in f['cases'])
    now = datetime.now(timezone.utc).isoformat()
    text = f'# {title}\n\nPublished {now}.\n\n{verdict}\n\n'
    text += ('Every row below represents both physical assignments. HP is target:counter, '
             'and W/L is from the target\'s perspective. These are standard-start development '
             'conditions on the unchanged bundled engine. They do not use reserved pool C.\n\n')
    text += '| Target | Counter | Outcome in each seat | HP | Final round |\n|---|---|---|---|---:|\n' + '\n'.join(rows) + '\n\n'
    text += 'Across the declared games: ' + '; '.join(f'{c}: {scores[c]["W"]}W, {scores[c]["D"]}D, {scores[c]["L"]}L' for c in candidates) + '.\n\n'
    text += (f'All {s["valid_conditions"]} games pass strict condition accounting, original-engine '
             f'replay and source/data archive checks. All {s["complete_assignment_pairs"]} assignment '
             'pairs have identical normalized complete histories. These paired executions are '
             'reproducibility checks, not independent random samples. No bot errors or rejected '
             'submitted actions occurred.\n\n')
    text += (f'Fresh counter instances reproduce every forecast-counter action on {decisions} '
             f'recorded public observations, with unchanged inputs and legal outputs. There are '
             f'{bad_model} complete-action prediction disagreements with the target. Such '
             'disagreement is distinct from counter-policy reproduction. ')
    if n == 'retargeted-forecast':
        assert bad_model == 0
        text += ('All model predictions agree here. The old-model comparison changes only the '
                 'model specification and its parameter dictionary.\n\n')
    else:
        relevant = [x for x in data['hp_histories']['cases'] if x['condition']['candidate_id'] in candidates]
        text += (f'The additional {len(relevant)} public-HP histories also reproduce exactly; '
                 'the counter buys no minions after handoff.\n\n')
    comps = data['comparison']['comparisons']
    text += (f'Of {len(comps)} paired full-policy interventions, '
             f'{sum(x["same_complete_trajectory"] for x in comps)} have identical full histories. '
             'This comparison cannot establish a one-round causal effect.\n\n')
    if n == 'retargeted-forecast':
        rounds = [rr for x in f['cases'] for rr in x['rounds'] if rr['switched']]
        text += (f'After handoff, all {len(rounds)} recorded rounds cause zero damage to the counter. '
                 'The earlier 45-point HP deficit remains.\n\n')
        assert all(rr['actual_counter_incoming_damage'] == 0 for rr in rounds)
    text += ('The exact target and opponent specifications, parameters and declared input hashes '
             f'are in [the manifest](../../{n}-001.json). The audit artifacts are:\n\n')
    for key, path in paths.items():
        text += f'- {key}: `{path}`.\n'
    text += ('\nTo reproduce, run from the project root with `PYTHONDONTWRITEBYTECODE=1`, '
             '`PYTHONPATH="$PWD"`, `OMP_NUM_THREADS=1`, and `TMPDIR="$PWD/bot_research/tmp"`. '
             'Choose a new output directory, then repeat with `--resume` until all declared cases finish:\n\n'
             '```sh\n'
             'nice -n 19 taskset -c 28 .venv/bin/python -B -m bot_research.experiments.validation.run_data_development '
             f'--manifest bot_research/experiments/validation/{n}-001.json '
             f'--output-dir bot_research/runs/validation/{n}-reproduction '
             '--max-seconds 500 --match-timeout 300\n```\n\n'
             'The recorded match runtimes and audit runtimes are in their result files. '
             'No repeated deterministic condition is counted as an additional independent sample.\n')
    output = d / 'RESULTS.md'
    if output.exists():
        raise FileExistsError(output)
    output.write_text(text)
    paths.update(manifest=e / f'{n}-001.json', results=output,
                 proof=d / 'PROOF.md', publisher=Path(__file__).relative_to(Path.cwd()))
    hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths.values()}
    (d / 'verification').mkdir(exist_ok=True)
    atomic_json(d / 'verification' / 'full_games.json', dict(time_utc=now,
        input_sha256=hashes, all_passed=True, outcomes={c: dict(v) for c, v in scores.items()},
        scope=verdict), exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as stream:
        stream.write(f'\n## {now}: {title}\n\nClaim and verdict: {verdict}\n\n'
                     f'Method: {s["valid_conditions"]} declared standard-start games, both physical assignments, '
                     'strict accounting, complete original-engine replay, source/data archive verification, '
                     f'and {decisions} fresh public-history forecast-counter calls. Result: '
                     + '; '.join(f'{c} {scores[c]["W"]}W/{scores[c]["D"]}D/{scores[c]["L"]}L' for c in candidates)
                     + f'. All {s["complete_assignment_pairs"]} assignment pairs match completely. '
                     f'Full table, exact conditions and proof scope: experiments/validation/analysis/{topic}/RESULTS.md. '
                     f'Evidence receipt: analysis/{topic}/verification/full_games.json. Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now, campaign=n, published=str(output), outcomes={c: dict(v) for c, v in scores.items()})))


if __name__ == '__main__':
    main()

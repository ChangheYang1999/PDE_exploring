"""Publish audited early-heavy strike and knowledge-intervention campaigns."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import argparse, hashlib, json
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', choices=('early-heavy-handoff','early-heavy-knowledge'), required=True)
    args = parser.parse_args()
    name = args.campaign
    e = Path('bot_research/experiments/validation')
    r = Path('bot_research/runs/validation')
    topic = name.replace('-', '_')
    root = e/'analysis'/topic
    paths = {key:r/f'{name}-{key}-001.json' for key in ('strict','replay','summary','data','comparison')}
    paths['histories'] = r/f'{name}-forecast-histories-001.json'
    data = {key:json.loads(path.read_text()) for key,path in paths.items()}
    summary, histories = data['summary'], data['histories']
    assert summary['valid_conditions'] == summary['expected_conditions']
    assert not summary['repeat_disagreements']
    assert data['replay']['all_passed'] and data['data']['all_passed']
    assert histories['exact_counter_policy_reproduction'] and histories['all_replayed']
    assert histories['all_observations_unchanged'] and histories['all_fresh_actions_legal']
    assert histories['no_internal_rejections']
    rows = []
    scores = Counter()
    for row in summary['rows']:
        results = row['results']
        assert len(results) == 2 and {x['side'] for x in results} == {0,1}
        assert len({(x['outcome'],tuple(x['hp']),x['rounds']) for x in results}) == 1
        x = results[0]
        rows.append(f'| {row["opponent"]} | {x["outcome"]} | {x["hp"][0]}:{x["hp"][1]} | {x["rounds"]} |')
        scores.update(y['outcome'] for y in results)
    cases = histories['cases']
    decisions = sum(len(x['rounds']) for x in cases)
    mismatch = sum(len(x['model_action_differences']) for x in cases)
    filtered = sum(len(x['filtered_parent_proposals']) for x in cases)
    # The similarly named diagnostic field describes TARGET purchases.
    # Inspect the recorded COUNTER actions to check the handoff promise.
    for case in cases:
        row = json.loads(Path(case['result']).read_text())
        records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
        counter_side = 1 - case['condition']['candidate_side']
        for trace in case['rounds']:
            if trace['switched']:
                record = records[2 * trace['round'] + counter_side]
                assert not any(event['kind'] == 'action' and event['action']['op'] == 'buy_minion'
                               for event in record['event'])
    if name == 'early-heavy-handoff':
        title = 'One round-five tier4 wins with an early exact-model handoff'
        verdict = ('CONFIRMED: one tier4 in round five followed by exact-public-model defense from '
                   'round six or seven beats P5TNUBM in both assignments, 755:740. REFUTED: the same '
                   'claim for handoffs eight and nine; both lose. Every no-strike control loses.')
        assert mismatch == 0
        mechanism = ('The checked opening component shows the target buying three splashes in round five, '
            'with total splash exposure190 and no gun. One tier4 survives, dealing60. The counter had '
            'already lost45 to the three opening tier1 copies, so it leads755:740. With handoff six or '
            'seven it takes no later damage. Handoff eight concedes26 later, and handoff nine concedes192. '
            'The intervention changes the counter\'s factory purchases and all later play as well; '
            'it is not an isolated estimate of the value of60 damage.\n\n')
        paths['opening'] = r/'early-heavy-opening-001.json'
    else:
        title = 'The early-heavy counter depends on accurate anticipatory defense'
        verdict = ('REFUTED: either visible-roster defense or the older P5TNUB model preserves the '
                   'early-heavy win against P5TNUBM. All eight interventions lose. This is evidence '
                   'of model dependence in these conditions, not a claim that no other defender could win.')
        mechanism = ('Each intervention retains the round-five tier4 and the handoff deadline. '
            'The visible variant still advances the exact model but does not use predicted purchases '
            'in its defensive threat list. The old-model variant changes only the model specification '
            'and its parameter dictionary. Their exact-model reference games are the handoff-six and '
            'handoff-seven strike games from early-heavy-handoff-001. Those four reference games are '
            'reused comparisons, not new samples.\n\n')
        paths['reference_summary'] = r/'early-heavy-handoff-summary-001.json'
        paths['reference_replay'] = r/'early-heavy-handoff-replay-001.json'
    now = datetime.now(timezone.utc).isoformat()
    text = f'# {title}\n\nChecked {now}.\n\n{verdict}\n\n'
    text += ('Each row represents both physical assignments. Outcome is from the P5TNUBM target\'s '
             'perspective; HP is target:counter. These are standard-start development games on the '
             'unchanged bundled engine. They do not use reserved pool C.\n\n'
             '| Counter setting | Target outcome in each seat | HP | Final round |\n'
             '|---|---|---|---:|\n' + '\n'.join(rows) + '\n\n')
    text += mechanism
    text += (f'All {summary["valid_conditions"]} games pass strict condition accounting, complete '
             'original-engine replay, and source/data archive checks. All '
             f'{summary["complete_assignment_pairs"]} assignment pairs have identical normalized histories. '
             'There are no bot errors or rejected submitted actions. These deterministic paired games '
             'are not independent population samples.\n\n')
    text += (f'Fresh counter instances reproduce all {decisions} recorded decisions from unchanged public '
             f'observations and return legal lists. There are {mismatch} full-action target-model disagreements. '
             f'The outer strike filter omits {filtered} now-unaffordable parent proposals across the games; '
             'these are explicitly recorded local filtering decisions, not submitted invalid actions. '
             'The parent has no internal rejections. No minion is purchased after handoff.\n\n')
    text += (f'All {len(data["comparison"]["comparisons"])} declared matched interventions have changed '
             'complete histories. First differences and round-by-round summaries are in the comparison '
             'artifact. The parameter interventions are full policies.\n\n')
    text += (f'Exact source hashes and specifications are in [the declaration](../../{name}-001.json). '
             'The counter uses a separately initialized public-policy clone; it never reads pending '
             'submissions, engine objects or an opponent instance.\n\nAudit inputs:\n\n')
    for key,path in paths.items():
        text += f'- {key}: `{path}`.\n'
    text += ('\nReproduce from the project root with `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH="$PWD"`, '
             '`OMP_NUM_THREADS=1`, and `TMPDIR="$PWD/bot_research/tmp"`. Use a new output directory and '
             'repeat with `--resume` until all declared cases finish:\n\n```sh\n'
             'nice -n 19 taskset -c 28 .venv/bin/python -B -m bot_research.experiments.validation.run_data_development '
             f'--manifest bot_research/experiments/validation/{name}-001.json '
             f'--output-dir bot_research/runs/validation/{name}-reproduction --max-seconds 500 --match-timeout 300\n```\n')
    target = root/'RESULTS.md'
    with target.open('x') as stream:
        stream.write(text)
    paths.update(proof=root/'PROOF.md', results=target, manifest=e/f'{name}-001.json',
                 publisher=Path(__file__).relative_to(Path.cwd()))
    hashes = {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths.values()}
    atomic_json(root/'verification/full_games.json',dict(time_utc=now,all_passed=True,input_sha256=hashes,
        target_outcomes=dict(scores),decisions=decisions,model_disagreements=mismatch,
        local_filtered_proposals=filtered,scope=verdict),exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as stream:
        stream.write(f'\n## {now}: {title}\n\nClaim and verdict: {verdict}\n\n'
            f'Method: {summary["valid_conditions"]} predeclared standard games with both player assignments, '
            'strict accounting, original-engine replay, source/data checks and '
            f'{decisions} fresh public-history counter decisions. Result from target perspective: '
            f'{scores["W"]}W/{scores["D"]}D/{scores["L"]}L; all assignment pairs match. '
            f'Model disagreements: {mismatch}. Local proposals filtered after the strike: {filtered}; '
            'no rejected submitted actions. Details and exact conditions: '
            f'experiments/validation/analysis/{topic}/RESULTS.md; receipt verification/full_games.json. '
            'Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now,published=str(target),target_outcomes=dict(scores),decisions=decisions)))

if __name__ == '__main__':
    main()

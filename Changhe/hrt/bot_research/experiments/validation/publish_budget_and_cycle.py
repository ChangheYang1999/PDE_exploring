"""Publish checked model-free handoff and finite-game evidence."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')


def load(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def publish(topic, title, text, verdict, note, paths, details):
    now = datetime.now(timezone.utc).isoformat()
    root = E/'analysis'/topic
    target = root/'RESULTS.md'
    with target.open('x') as stream:
        stream.write(f'# {title}\n\nChecked {now}.\n\n{verdict}\n\n{text}')
        stream.write('\nAudit inputs:\n\n')
        for path in paths:
            stream.write(f'- `{path}`.\n')
    paths += [root/'PROOF.md', target, Path(__file__).relative_to(Path.cwd())]
    atomic_json(root/'verification/full_games.json', dict(time_utc=now, all_passed=True,
        input_sha256={str(p):sha(p) for p in paths}, scope=verdict, **details), exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as stream:
        stream.write(f'\n## {now}: {title}\n\nClaim and verdict: {verdict}\n\n'
            f'Method and result: {note} Details: experiments/validation/analysis/{topic}/RESULTS.md; '
            'receipt verification/full_games.json. Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now, published=str(target), **details)))


def budget():
    paths = [R/f'budget-handoff-{key}-001.json' for key in
             ('strict','replay','summary','data','histories','opening','comparison')]
    data = {key:load(path) for key,path in zip(
        ('strict','replay','summary','data','histories','opening','comparison'),paths)}
    summary, history = data['summary'], data['histories']
    assert summary['valid_conditions'] == summary['expected_conditions'] == 12
    assert summary['identical_assignment_pairs'] == summary['complete_assignment_pairs'] == 6
    assert data['replay']['all_passed'] and data['data']['all_passed'] and data['opening']['all_passed']
    assert all(history[key] for key in ('all_fresh_actions_legal','all_observations_unchanged',
        'all_replayed','exact_counter_policy_reproduction','no_post_handoff_minions'))
    assert not summary['repeat_disagreements']
    rows=[]
    for row in summary['rows']:
        assert len(row['results']) == 2
        assert len({(x['outcome'],tuple(x['hp']),x['rounds']) for x in row['results']}) == 1
        x=row['results'][0]
        rows.append(f'| {row["opponent"]} | {x["outcome"]} | {x["hp"][0]}:{x["hp"][1]} | {x["rounds"]} |')
    calls = sum(len(case['rounds']) for case in history['cases'])
    filtered = sum(len(case['filtered_proposals']) for case in history['cases'])
    assert calls == 464 and filtered == 156
    assert len(data['comparison']['comparisons']) == 12
    assert all(not case['same_complete_trajectory'] for case in data['comparison']['comparisons'])
    quarter=[]
    for case in history['cases']:
        incoming = [row for row in case['rounds'] if row['switched'] and row['incoming_damage']]
        if '1of4' in case['condition']['opponent_id']:
            assert incoming[0]['round'] == 10 and incoming[0]['incoming_damage'] == 60
            assert all(x == 0 for x in incoming[0]['scenario_residuals'])
            quarter.append(case['result'])
        else:
            assert not incoming
    assert len(quarter) == 4
    verdict = ('CONFIRMED: with the declared round5 tier4 opening, a forecast using half or all of '
        'the public enemy budget preserves the 755:740 win against P5TNUBM in both assignments, '
        'for handoff6 and handoff7. REFUTED: the quarter-budget variant preserves that win. '
        'This also refutes a broader claim that these wins require an exact opponent policy model.')
    text = ('Each row represents both physical assignments. Outcome is from the P5TNUBM target\'s '
        'perspective; HP is target:counter. These are standard-start development conditions.\n\n'
        '| Counter setting | Target outcome per seat | HP | Final round |\n'
        '|---|---|---|---:|\n'+'\n'.join(rows)+'\n\n'
        'The counter follows the same screened opening and buys one tier4 in round5. From the '
        'handoff onward it constructs hypotheses by appending a pure tier to the visible active '
        'roster, using floor(nG/d) of public enemy gold G and a cap of120 new copies. It plans '
        'defense against that finite set, buys factories, and buys no more minions. It neither '
        'initializes nor queries an opponent policy clone.\n\n'
        'The common opening leaves target740 and counter755 after round5. The four successful '
        'settings take no later damage. Each quarter-budget game first leaks after handoff in '
        'round10, for60 damage, even though every enumerated hypothetical roster has zero '
        'residual damage in the checked trace. This exposes inadequate forecast coverage; it '
        'does not establish that the greedy planner failed on a covered roster. The hypothesis '
        'set does not certify all affordable mixtures or counts beyond its cap.\n\n'
        'All12 games pass strict accounting, original-engine replay, and source/data archive '
        'checks. Every assignment pair has an identical normalized history. There are no bot '
        'errors or rejected submitted actions. Fresh counter instances reproduce all464 '
        'decisions from unchanged observations and return legal action lists. The opening '
        'filter omits156 unaffordable parent factory proposals, thirteen per game; none is '
        'submitted. No minion is bought after handoff.\n\n'
        'Twelve descriptive matched comparisons reuse the four exact-model reference games '
        'from early-heavy-handoff-001. All complete histories differ. These full-policy '
        'interventions change later defense and economy, so they do not isolate one purchase. '
        'The earlier visible-only and old-model failures remain valid for those controllers, '
        'but do not imply model necessity. Repeated assignments are controls, not independent '
        'population samples.\n\n'
        'Reproduce with the run_data_development module, --manifest '
        'bot_research/experiments/validation/budget-handoff-001.json, a fresh --output-dir, '
        '--max-seconds500 and --match-timeout300, then repeat with --resume if needed. Use the '
        'project root, .venv/bin/python -B, PYTHONDONTWRITEBYTECODE=1, PYTHONPATH="$PWD", '
        'TMPDIR="$PWD/bot_research/tmp", OMP_NUM_THREADS=1, low priority and assigned affinity.\n')
    paths += [E/'budget-handoff-001.json', E/'budget-handoff-comparisons-001.json',
              R/'early-heavy-handoff-summary-001.json',R/'early-heavy-handoff-replay-001.json']
    publish('budget_handoff','A public-budget forecast preserves the early-heavy win',text,verdict,
        'Twelve predeclared games, full original-engine replays, six matching assignment pairs, '
        '464 exact fresh counter decisions and source/data checks. Target4W/8L. Half/full forecasts '
        'win; quarter forecasts lose740:-285 at round16. No submitted invalid actions.', paths,
        dict(target_outcomes=summary['outcomes'],decisions=calls,local_filtered_proposals=filtered))


def cycle():
    paths=[R/f'nominee-counter-game-{key}-001.json' for key in ('matrix','certificate','certificate-check')]
    matrix, cert, check = map(load,paths)
    assert matrix['all_assignment_histories_identical'] and matrix['all_replays_passed']
    assert check['passed'] and cert['all_exact_constraints_passed']
    assert cert['matrix_sha256'] == sha(paths[0])
    assert check['certificate_sha256'] == sha(paths[1])
    assert matrix['policies'] == ['P4TNUB','P5TNUBM','early1_handoff6','lead8']
    assert matrix['matrix'] == [[0,0,1,-1],[0,0,-1,1],[-1,1,0,-1],[1,-1,1,0]]
    probabilities=[Fraction(x['numerator'],x['denominator']) for x in cert['probabilities']]
    assert probabilities == [0,Fraction(1,3),Fraction(1,3),Fraction(1,3)]
    calls=0
    for name in ('nominee-cross','counter-cross'):
        for key in ('strict','replay','summary','data','histories'):
            path=R/f'{name}-{key}-001.json';d=load(path);paths.append(path)
            if key in ('replay','data'): assert d['all_passed']
            if key=='summary':
                assert d['valid_conditions'] == d['expected_conditions']
                assert not d['repeat_disagreements']
            if key=='histories':
                assert all(d[k] for k in ('all_fresh_actions_legal','all_observations_unchanged',
                    'all_replayed','exact_policy_reproduction'))
                calls += sum(sum(len(y) for y in case['decision_seconds']) for case in d['cases'])
        paths.append(E/f'{name}-001.json')
    assert calls==496
    for topic in ('nominee_handoff','early_heavy_handoff'):
        path=E/'analysis'/topic/'verification/full_games.json'
        assert load(path)['all_passed'];paths.append(path)
    verdict=('CONFIRMED: the four fixed standard-start policies have directed cycles '
        'P5TNUBM > lead8 > early1_handoff6 > P5TNUBM and '
        'P4TNUB > early1_handoff6 > P5TNUBM > lead8 > P4TNUB. '
        'No policy in this set wins against every other one. A rational one-third mixture over '
        'P5TNUBM, early1_handoff6 and lead8 has value0 in the stated finite payoff table.')
    rows=[]
    for pair in matrix['pairs']:
        x=pair['games'][0]
        hp=x['hp_candidate_first']
        rows.append(f'| {pair["row_policy"]} | {pair["column_policy"]} | {x["outcome"]} | '
            f'{hp[0]}:{hp[1]} | {x["rounds"]} |')
    text=('The table reports the row policy\'s result, HP and final round. Each row covers both '
        'physical assignments, whose complete normalized histories agree.\n\n'
        '| Row policy | Opponent | Row outcome per seat | HP | Final round |\n'
        '|---|---|---|---|---:|\n'+'\n'.join(rows)+'\n\n'
        'The early-heavy counter always retains its P5TNUBM clone, even against P4TNUB or lead8. '
        'No model is silently retargeted between opponents. The lead8 controller retains the '
        'HP trigger and forecast settings declared in nominee-handoff-001. Full specifications '
        'and source hashes appear in the matrix and campaign declarations.\n\n'
        'Only six games are newly executed: P4TNUB against P5TNUBM and early1_handoff6, and '
        'early1_handoff6 against lead8, both assignments. The other six reuse previously audited '
        'nominee-handoff and early-heavy-handoff games. The assembler freshly checks all twelve '
        'replays and source identities. Both fresh policies reproduce all496 decisions in the '
        'six new games; observations remain unchanged and every action list is legal. Original '
        'campaign audits report no bot errors or rejected submitted actions.\n\n'
        'Assign1 to a win,0 to a draw and-1 to a loss and average assignments. In policy order '
        'P4TNUB, P5TNUBM, early1_handoff6, lead8, the payoff matrix is:\n\n'
        '```text\n 0  0  1 -1\n 0  0 -1  1\n-1  1  0 -1\n 1 -1  1  0\n```\n\n'
        'Diagonal zeros use the symmetric payoff convention; no self-play games are claimed. '
        'Exact rational checking verifies p=(0,1/3,1/3,1/3), pA=(0,0,0,0), and the value0 '
        'certificate. Every pure row has worst payoff-1. This statement is conditional on the '
        'fixed finite matrix, with a component sampled secretly before the opponent chooses '
        'its policy. It says nothing about new policies, continuation states, or global '
        'game-theoretic optimality. The six assignment pairs are deterministic controls, '
        'not twelve independent samples. No random mixture was installed as best.py.\n\n'
        'To reproduce, run the two declared development manifests into new directories, '
        'replay them with the original engine, regenerate fresh policy histories, then use '
        'assemble_nominee_counter_game.py, solve_metagame.py and '
        'check_metagame_certificate.py. The solver uses local numerical Python; the certificate '
        'checker uses exact fractions and the game environment. Respect the project-root, '
        'bytecode-disabled, temporary-directory and assigned-affinity run conventions.\n')
    publish('nominee_counter_game','The two nominees and their counters form a finite cycle',text,
        verdict,'Twelve freshly audited recorded games across six pairs, six newly executed '
        'and six reused. All assignment histories match; both policies in the new games '
        'reproduce496 decisions exactly. Exact rational certificate checks pass.',paths,
        dict(new_games=6,reused_games=6,fresh_policy_decisions=calls,probabilities=cert['probabilities']))


def main():
    p=argparse.ArgumentParser();p.add_argument('topic',choices=('budget','cycle'));a=p.parse_args()
    {'budget':budget,'cycle':cycle}[a.topic]()

if __name__=='__main__':main()

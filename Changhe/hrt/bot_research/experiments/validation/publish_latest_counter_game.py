"""Bind the latest three-policy table to complete audited fixed-policy games."""
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from urllib.parse import parse_qs
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
AREA = E/'analysis/latest_counter_game'


def normalized_spec(spec):
    base, _, query = spec.partition('?')
    parameters = {k:json.loads(v[0]) for k,v in parse_qs(query).items()}
    if base == 'bot_research.bots.counters.delegated_defense:@make':
        parameters.setdefault('mode','adaptive')
        parameters.setdefault('delegate','econ20')
    return base,parameters


def main():
    inputs = {}
    def digest(p):
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)] = digest(p)
        return json.loads(Path(p).read_text())
    d = read(E/'latest-counter-game-campaigns-001.json')
    policies = d['policies']
    assert set(policies) == {'B','C','D'}
    cases = []
    fresh_new = 0
    edges = []
    all_items = [dict(x,reused=False) for x in d['campaigns']] + [dict(x,name=x['campaign'],reused=True) for x in d['reused']]
    for item in all_items:
        name,a,b = item['name'],item['a'],item['b']
        m = read(E/(name+'.json'))
        for p, sha in m['input_sha256'].items():
            assert digest(p) == sha,p
            inputs[p] = sha
        strict = read(R/(name+'-strict.json'))
        replay = read(R/(name+'-replay.json'))
        data = read(R/(name+'-data.json'))
        assert not strict['unresolved'] and not strict['repeat_disagreements']
        assert replay['all_passed'] and data['all_passed']
        if item['reused']:
            hist = read(R/(name+'-histories.json'))
            assert hist['exact_counter_policy_reproduction']
            assert all(hist[k] for k in ('all_fresh_actions_legal','all_observations_unchanged','all_public_selections_verified','all_replayed'))
            delegation = read(R/(name+'-delegation.json'))
            assert delegation['all_passed']
            if a == 'C':
                forecast = read(R/(name+'-fresh-forecaster.json'))
                # Inspect the actual stored schema rather than treating its existence as success.
                assert all(forecast[k] for k in ('all_fresh_actions_agree', 'all_fresh_actions_legal',
                    'all_observations_unchanged', 'all_original_combat_agrees', 'all_predictions_exact'))
            ids = item['cases']
        else:
            fresh = read(R/(name+'-fresh.json'))
            assert fresh['all_passed'] and fresh['all_actions_legal'] and fresh['all_observations_unchanged'] and fresh['all_replayed']
            assert fresh['games'] == strict['valid_conditions'] == 2
            fresh_new += fresh['checked_calls']
            ids = ['case0000','case0001']
        pair = []
        for ident in ids:
            path = R/name/'results'/(ident+'.json')
            row = checked_row(str(path),inputs)
            c = row['condition']
            assert normalized_spec(c['candidate_spec']) == normalized_spec(policies[a]['spec'])
            assert normalized_spec(c['opponent_spec']) == normalized_spec(policies[b]['spec'])
            case = dict(a=a,b=b,reused=item['reused'],result=str(path),candidate_side=c['candidate_side'],
                outcome=row['outcome'],hp_a_first=row['hp_candidate_first'],rounds=row['rounds'],
                canonical_replay_sha256=row['canonical_replay_sha256'],
                decision_seconds_a_first=row['decision_seconds_candidate_first'])
            pair.append(case);cases.append(case)
        pair.sort(key=lambda x:x['candidate_side'])
        assert [r['candidate_side'] for r in pair] == [0,1]
        assert pair[0]['outcome'] == pair[1]['outcome']
        assert pair[0]['hp_a_first'] == pair[1]['hp_a_first'] and pair[0]['rounds'] == pair[1]['rounds']
        assert pair[0]['canonical_replay_sha256'] == pair[1]['canonical_replay_sha256']
        value = {'W':1,'D':0,'L':-1}[pair[0]['outcome']]
        edges.append(dict(a=a,b=b,value=value,hp_a_first=pair[0]['hp_a_first'],rounds=pair[0]['rounds'],reused=item['reused']))
    assert len(cases) == 12 and sum(c['reused'] for c in cases) == 4
    order = ['B','C','D']
    A = [[None]*3 for _ in order]
    for e in edges:
        i,j = order.index(e['a']),order.index(e['b'])
        assert A[i][j] is None and (i==j or A[j][i] is None)
        if i == j:assert e['value']==0
        A[i][j] = e['value'];A[j][i] = -e['value']
    assert all(v is not None for row in A for v in row)
    cycle = A[0][1]==A[1][2]==A[2][0]==1
    certificate = None
    if cycle:
        p = [Fraction(1,3)]*3
        rows = [sum(Fraction(A[i][j])*p[j] for j in range(3)) for i in range(3)]
        cols = [sum(p[i]*Fraction(A[i][j]) for i in range(3)) for j in range(3)]
        assert rows == cols == [0,0,0]
        certificate = dict(weights=[str(v) for v in p],row_payoffs=[str(v) for v in rows],
                           column_payoffs=[str(v) for v in cols],value='0')
    stamp = datetime.now(timezone.utc).isoformat()
    verdict = ('CONFIRMED' if cycle else 'REFUTED')+': the specified cycle B>C>D>B holds in the paired recorded game.'
    lines = ['# A fixed game after counter adaptation','',f'Checked {stamp}.','',verdict,'',
        'B is frozen best_v9e. D is the adaptive Fortress38 continuation. C is the round3/tier2 public-clone attacker, with its D model unchanged even against B and itself. All exact specifications are in verification/full_games.json and the declaration.','',
        'Twelve recorded games define three off-diagonal pairings and three measured self-play cases, each in both physical assignments. Eight games are new and four are explicitly reused. Every assignment pair has the same complete normalized history. Reused games and repeated histories add no independent evidence.','',
        '| Row policy | B | C | D |','|---|---:|---:|---:|']
    for name,row in zip(order,A):lines.append('| '+name+' | '+' | '.join(str(v) for v in row)+' |')
    lines += ['','Payoff is +1 for a win, 0 for a draw and -1 for a loss under the engine result. The table is a description of these finite standard-start games.','',
        '| Pair, first policy perspective | Outcome | Final HP | Ending round | Source |',
        '|---|---|---|---:|---|']
    for e in edges:
        lines.append(f'| {e["a"]} vs {e["b"]} | '+{1:'W',0:'D',-1:'L'}[e['value']]+f' | {e["hp_a_first"][0]}:{e["hp_a_first"][1]} | {e["rounds"]} | '+('Reused' if e['reused'] else 'New')+' |')
    if certificate:
        lines += ['','Exact rational arithmetic verifies that the uniform one-third mixture has zero expected payoff against every column, and holds every row to zero. Together these inequalities certify maximin value0 for this recorded three-policy table. They do not certify the mixture against a fourth policy, a different initial state or a different load-dependent execution.']
    else:
        lines += ['','The proposed strict cycle is absent. No uniform-mixture optimality certificate is claimed.']
    lines += ['',f'All eight new games pass strict accounting, original-engine replay, explicit source/data checks and {fresh_new} fresh action-generating decisions across both policies. No rejected action, observation mutation or bot error is recorded. Reused edges retain their original fresh-counter and handoff audits; the C-D edge additionally has exact private-model forecast checks. C is permitted to forecast incorrectly against B or itself: the actual C action generator is what is held fixed and independently regenerated.','',
       'Reproduce the four latest-counter-game manifests using run_data_development, then strict, replay, data and check_fixed_game_histories checks. Reproduce the two named reused campaigns or restore their exact recorded evidence, then run publish_latest_counter_game. The pipeline log keeps complete bounded commands. Use the existing Python, disabled bytecode, the research temporary directory, one numerical thread, assigned affinity and low priority.','']
    out = AREA/'RESULTS.md'
    with out.open('x') as f:f.write('\n'.join(lines))
    for p in (out,AREA/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    receipt = dict(time_utc=stamp,all_passed=True,verdict=verdict,new_games=8,reused_games=4,
        fresh_new_decisions=fresh_new,policies=policies,order=order,payoff=A,certificate=certificate,
        unique_canonical_histories=len({c['canonical_replay_sha256'] for c in cases}),
        cases=cases,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Fixed three-policy game complete\n\nClaim and verdict: {verdict}\n\nMethod: eight new and four reused audited games, both assignments of all edges and measured self-play. Result: payoff rows in B,C,D order are {A}; all {fresh_new} new decisions regenerated. The clone retains its same D model against every policy. '+('Uniform mixture has exact value0 only in this finite table. ' if certificate else 'No cycle-mixture claim. ')+f'Evidence: {out}.\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('policies','cases','input_sha256')}))


if __name__ == '__main__':
    main()

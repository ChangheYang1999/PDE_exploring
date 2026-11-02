"""Declare and independently check the second shared-prefix selector."""
from collections import defaultdict
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json
import time
from bot_research.bots.counters.wall_prefix_selector import WallPrefixSelector
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.finite_table_certificate import verify as verify_certificate
from bot_research.experiments.validation.policy_value_snapshot import freeze_state
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.publish_ten_policy_game_v2 import norm
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E/'analysis/wall_prefix_selector'
D = E/'wall-prefix-selector-001.json'
OLD = E/'analysis/ten_policy_game/verification/full_games.json'
ORDER = ['B','C','D','G','H','I','J','L','M','N','O']
BRANCH = dict(zip(ORDER, ['G','L','L','G','L','L','L','G','G','G','G']))
PREDICTED = [1,0,1,0,1,0,1,1,1,1,0]


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    return json.loads(Path(p).read_text())


def verify():
    d = read(D)
    amendment = read(E/'wall-prefix-selector-checker-amendment-001.json')
    for p, h in amendment['input_sha256'].items():
        assert sha(p) == h, p
    for p, h in d['input_sha256'].items():
        assert sha(p) == h, p
    return d


def declare():
    prior = read(E/'ten-policy-game-declaration-001.json')
    old = read(OLD)
    assert old['all_passed'] and old['order'] == ORDER[:-1]
    assert old['certificate']['weights'] == ['0','0','0','1/3','0','0','1/3','0','0','1/3']
    assert verify_certificate(old['payoff'], old['certificate']['weights'])
    assert not verify_certificate(old['payoff'], ['0']*10)
    assert not verify_certificate(old['payoff'], ['-1','2']+['0']*8)
    policies = dict(prior['policies'])
    policies['O'] = dict(id='O', spec='bot_research.bots.counters.wall_prefix_selector:@make')
    modules = {'bot_research.experiments.validation.'+s for s in (
        'wall_prefix_selector_check','run_data_development','audit_development_strict',
        'replay_audit','audit_data_archives','check_fixed_game_histories')}
    modules |= {p['spec'].partition(':')[0] for p in policies.values()}
    paths = set(static_closure(modules)) | {A/'PROOF.md',A/'PROTOCOL.md',OLD,
        E/'ten-policy-game-declaration-001.json', Path('td_game/balanced.json'),Path('configs/balanced.json')}
    paths.update(Path(p) for p in prior['input_sha256'] if '/data/' in p and p.endswith('.json'))
    baselines = []
    for target in ORDER:
        selected = BRANCH[target]
        old_target = 'G' if target == 'O' else target
        for side in (0,1):
            matches = [c for c in old['cases'] if {c['a'],c['b']} == {selected,old_target} and
                       (c['candidate_side'] if c['a'] == selected else 1-c['candidate_side']) == side]
            assert len(matches) == 1, (target, side)
            case = matches[0]
            filename = case['result']
            raw = read(filename)
            replay = raw['replay_path']
            baselines.append(dict(opponent=target, side=side, selected=selected, result=filename,
                replay=replay, reference_side=side, old_pair=[case['a'],case['b']]))
            paths.update([Path(filename),Path(replay)])
    pins = {str(p):sha(p) for p in sorted(paths)}
    stamp = now()
    campaigns = []
    for index, opponents in enumerate([ORDER[:4],ORDER[4:8],ORDER[8:]]):
        name = f'wall-prefix-selector-{index:02d}-001'
        atomic_json(E/(name+'.json'), dict(declared_utc=stamp,candidates=[policies['O']],
            opponents=[policies[k] for k in opponents],input_sha256=pins,
            purpose='Selected second shared-prefix counter; standard start; no reserved D use.'), exclusive=True)
        campaigns.append(dict(name=name,opponents=opponents,expected=2*len(opponents)))
    atomic_json(D, dict(declared_utc=stamp,policies=policies,order=ORDER,campaigns=campaigns,
        baselines=baselines,new_games=22,policy_calls_before_declaration=0,input_sha256=pins,
        predicted_branches=BRANCH,predicted_payoffs=PREDICTED,
        hypotheses=['H1 nonloss vsG/J/N and positive uniform mean separately in each seat',
                    'H2 nonloss vsalltenoldpolicies in each seat',
                    'H3 complete predicted row and self draws'],
        arithmetic_fixtures_passed=True),exclusive=True)
    print(json.dumps(dict(time_utc=stamp,new_games=22,pins=len(pins),policy_calls_before_declaration=0)),flush=True)


def canonical_records(path, side):
    records = [json.loads(s) for s in Path(path).read_text().splitlines()]
    for row in records:
        row.pop('match',None)
        row['player'] ^= side
        row['snapshot']['name'] = 'counter' if row['player'] == 0 else 'opponent'
        for event in row['event']:
            event.pop('order',None)
        if row.get('result') is not None and row['result']['winner'] is not None:
            row['result']['winner'] ^= side
    records.sort(key=lambda row:(row['round'],row['player']))
    return records


def branches(index):
    begin = time.perf_counter()
    d = verify()
    campaign = d['campaigns'][index]
    root = R/campaign['name']
    inputs = {str(D):sha(D)}
    source = read(root/'freeze.json')['source_sha256']
    for p,h in source.items():
        assert sha(p) == h
        inputs[p] = h
    cases = []
    for job in read(root/'jobs.json'):
        path = root/'results'/(job['id']+'.json')
        checked = checked_row(str(path),inputs)
        row = read(path)
        side = row['condition']['candidate_side']
        target = row['condition']['opponent_id']
        records = [json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
        rounds = row['rounds']
        assert len(records) == 2*(rounds+1) and rounds >= 2
        assert all(rec['round'] == i//2 and rec['player'] == i%2 for i,rec in enumerate(records))
        assert all(rec.get('result') is None for rec in records[:-2])
        assert records[-1]['result'] is not None and records[-1]['result'] == records[-2]['result'] == row['result']
        enemy = records[2+(1-side)]['snapshot']
        selected = 'L' if not enemy['buildings'] and not enemy['roster'] else 'G'
        selector = WallPrefixSelector()
        reference = resolve({'spec':d['policies'][selected]['spec']})
        # Resolve uses a bound decide method for these two object policies.
        reference_object = reference.decide.__self__
        cfg = balanced_config()
        engine = Engine(cfg,tuple(row['bot_specs']))
        assert normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2]
        trace = []
        for rnd in range(1,rounds+1):
            obs = engine.observation(side)
            saved = deepcopy(obs)
            got = selector.decide(obs)
            assert obs == saved
            refarg = deepcopy(saved)
            expected = reference.decide(refarg)
            assert refarg == saved
            pair = records[2*rnd:2*rnd+2]
            actions = [[e['action'] for e in rec['event'] if e['kind']=='action'] for rec in pair]
            assert got == expected == actions[side], (target,side,rnd)
            own = player_from_snapshot(saved['players'][side])
            assert all(apply_action(own,a,rnd,cfg)['accepted'] for a in got)
            chosen = selector.l if selected == 'L' else selector.g
            assert freeze_state(vars(chosen)) == freeze_state(vars(reference_object)), (target,side,rnd,'state')
            assert selector.selected == (None if rnd == 1 else selected)
            assert normalized(engine.play_round(actions)) == pair
            trace.append(dict(**selector.trace[-1],selected_reference_actions_agree=True,
                              selected_reference_state_agrees=True))
        assert engine.result == row['result']
        baseline = next(b for b in d['baselines'] if b['opponent']==target and b['side']==side)
        current = canonical_records(row['replay_path'],side)
        previous = canonical_records(baseline['replay'],baseline['reference_side'])
        same = current == previous
        divergence = None
        if not same:
            offset = next((i for i in range(min(len(current),len(previous))) if current[i]!=previous[i]),
                          min(len(current),len(previous)))
            divergence = dict(record_index=offset,new=current[offset] if offset<len(current) else None,
                              old=previous[offset] if offset<len(previous) else None)
        cases.append(dict(result_path=str(path),opponent=target,side=side,selected=selected,
            predicted_branch_agrees=selected==BRANCH[target],trace=trace,whole_stream_checked=True,
            baseline=baseline,same_selected_old_history=same,first_divergence=divergence,
            rounds=rounds,selector_calls=rounds,reference_calls=rounds))
        print(json.dumps(dict(time_utc=now(),case=job['id'],selected=selected,calls_each=rounds,
                             baseline_history_agrees=same)),flush=True)
    assert len(cases)==campaign['expected']
    verify()
    assert all(sha(p)==h for p,h in inputs.items())
    result = dict(time_utc=now(),all_passed=True,all_replayed=True,all_actions_legal=True,
        all_observations_unchanged=True,all_reference_actions_agree=True,all_reference_states_agree=True,
        selector_calls=sum(c['selector_calls'] for c in cases),reference_calls=sum(c['reference_calls'] for c in cases),
        cases=cases,input_sha256=inputs,elapsed_seconds=time.perf_counter()-begin)
    atomic_json(R/(campaign['name']+'-branches.json'),result,exclusive=True)


def publish():
    d = verify()
    inputs = dict(d['input_sha256'])
    def checked_read(p):
        inputs[str(p)] = sha(p)
        return read(p)
    cases = []
    fresh_calls = selector_calls = reference_calls = 0
    for campaign in d['campaigns']:
        name,size = campaign['name'],campaign['expected']
        root = R/name
        audits = {k:checked_read(R/(name+'-'+k+'.json')) for k in ('strict','replay','data','fresh','branches')}
        strict = audits['strict']
        assert strict['valid_conditions']==strict['expected_conditions']==size
        assert strict['attempt_counts']=={'valid':size} and not strict['unresolved'] and not strict['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count']==size and audits['data']['all_passed']
        for k in ('fresh','branches'):
            audit = audits[k]
            assert all(audit[n] for n in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'))
            for p,h in audit['input_sha256'].items():
                assert sha(p)==h,p
                inputs[p]=h
        assert audits['fresh']['games']==size
        assert audits['branches']['all_reference_actions_agree'] and audits['branches']['all_reference_states_agree']
        fresh_calls += audits['fresh']['checked_calls']
        selector_calls += audits['branches']['selector_calls']
        reference_calls += audits['branches']['reference_calls']
        branchmap = {c['result_path']:c for c in audits['branches']['cases']}
        for job in checked_read(root/'jobs.json'):
            path = root/'results'/(job['id']+'.json')
            row = checked_row(str(path),inputs)
            target = row['condition']['opponent_id']
            assert norm(row['condition']['candidate_spec'])==norm(d['policies']['O']['spec'])
            assert norm(row['condition']['opponent_spec'])==norm(d['policies'][target]['spec'])
            branch = branchmap[str(path)]
            cases.append(dict(opponent=target,side=row['condition']['candidate_side'],outcome=row['outcome'],
                payoff={'W':1,'D':0,'L':-1}[row['outcome']],hp_O_first=row['hp_candidate_first'],
                rounds=row['rounds'],selected=branch['selected'],
                canonical_replay_sha256=row['canonical_replay_sha256'],
                same_selected_old_history=branch['same_selected_old_history'],
                first_divergence=branch['first_divergence'],result=str(path)))
    assert len(cases)==22
    assert fresh_calls==2*sum(c['rounds'] for c in cases)
    assert selector_calls==reference_calls==sum(c['rounds'] for c in cases)
    groups = defaultdict(list)
    for c in cases: groups[c['opponent']].append(c)
    pairs = []
    for target in ORDER:
        group = sorted(groups[target],key=lambda c:c['side'])
        assert len(group)==2 and [c['side'] for c in group]==[0,1]
        pairs.append(dict(opponent=target,same_history=group[0]['canonical_replay_sha256']==group[1]['canonical_replay_sha256'],
            same_outcome=group[0]['outcome']==group[1]['outcome']))
    means = {str(side):str(sum(Fraction(c['payoff'],3) for c in cases if c['side']==side and c['opponent'] in ('G','J','N'))) for side in (0,1)}
    h1 = all(c['payoff']>=0 for c in cases if c['opponent'] in ('G','J','N')) and all(Fraction(v)>0 for v in means.values())
    h2 = all(c['payoff']>=0 for c in cases if c['opponent']!='O')
    h3 = all(c['payoff']==PREDICTED[ORDER.index(c['opponent'])] and c['selected']==BRANCH[c['opponent']] for c in cases)
    old = checked_read(OLD)
    matrix = [list(row)+[None] for row in old['payoff']]+[[None]*11]
    same_outcomes = all(p['same_outcome'] for p in pairs)
    certificate = None
    if same_outcomes:
        for i,target in enumerate(ORDER):
            value = groups[target][0]['payoff']
            if i==10: assert value==0
            matrix[10][i],matrix[i][10]=value,-value
        weights = ['0']*10+['1']
        pure = verify_certificate(matrix,weights)
        if pure: certificate=dict(weights=weights,column_payoffs=matrix[10],exact_value='0')
    else:
        matrix=None
        pure=False
    stamp = now()
    verdict = lambda h:'CONFIRMED' if h else 'REFUTED'
    lines = ['# A second public selector challenges the ten-policy mixture','',f'Completed {stamp}.','',
        f'H1 **{verdict(h1)}**: nonloss against G/J/N and positive uniform-mixture payoff in both assignments. Exact means by physical seat: {means}.',
        f'H2 **{verdict(h2)}**: nonloss against allten old policies in each assignment.',
        f'H3 **{verdict(h3)}**: the whole predicted row, branch choices and self draws.', '',
        'O advances G and L through their identical20-wall/four-factory opening. At round2 it keeps L if the opponent has no building and no roster, otherwise G. It keeps the selected private history and never reselects. Names and pending submissions are not used. This rule was chosen after the earlier ten-policy table; it is selected development evidence.', '',
        '| Opponent | Selected member | Seat0 outcome and HP | Seat1 outcome and HP | Rounds0/1 |',
        '| --- | --- | --- | --- | --- |']
    for target in ORDER:
        x,y=sorted(groups[target],key=lambda c:c['side'])
        lines.append(f'| {target} | {x["selected"]}/{y["selected"]} | {x["outcome"]} {x["hp_O_first"][0]}:{x["hp_O_first"][1]} | {y["outcome"]} {y["hp_O_first"][0]}:{y["hp_O_first"][1]} | {x["rounds"]}/{y["rounds"]} |')
    lines += ['',f'Twenty-two new games pass strict legality/source checks, data archival checks and original-engine replay. All {fresh_calls} fresh external decisions match. A separate audit adds {selector_calls} selector calls and {reference_calls} standalone selected-member calls; every action and every selected persistent state agrees. Every record stream has an explicit terminal boundary.', '',
        f'{sum(p["same_history"] for p in pairs)}/11 assignment pairs have identical normalized full histories. {sum(c["same_selected_old_history"] for c in cases)}/22 histories equal their selected old member\'s retained baseline under the stated label/order normalization. Any first divergence is retained in verification/full_games.json.', '',
        f'The pure-O rational certificate for the expanded measured11-policy table is {"CONFIRMED" if pure else "not established"}. '+('Its column payoffs are '+str(matrix[10])+'. ' if pure else '')+'The old uniform G/J/N certificate retains its original ten-policy scope. A successful new response narrows its applicability; it does not invalidate that old finite arithmetic.', '',
        'This is no claim of unrestricted optimality or dominance against unseen policies or starts. The common-prefix theorem remains conditional on matching decision-relevant environmental branches; these exact reproductions verify the listed executions. There is no final-candidate change and no reservedD use. Definitions, proof and prospective methods are in PROOF.md and PROTOCOL.md.']
    with (A/'RESULTS.md').open('x') as f:f.write('\n'.join(lines)+'\n')
    result=dict(time_utc=stamp,all_passed=True,new_games=22,external_fresh_calls=fresh_calls,
        extra_selector_calls=selector_calls,standalone_reference_calls=reference_calls,
        h1=h1,h2=h2,h3=h3,uniform_GJN_payoff_by_seat=means,order=ORDER,payoff=matrix,
        pure_O_certificate=certificate,cases=cases,pairs=pairs,
        input_sha256={**inputs,str(D):sha(D),str(A/'RESULTS.md'):sha(A/'RESULTS.md')})
    atomic_json(A/'verification/full_games.json',result,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Second shared-prefix selector complete\n\nH1 positive mean/no loss against G/J/N {verdict(h1)}, exact per-seat means{means}; H2 nonloss against allten old policies {verdict(h2)}; H3 predicted whole row {verdict(h3)}.22newgames,{fresh_calls} fresh external decisions,{selector_calls} extra selector and{reference_calls} standalone-response calls. PureO11-policy certificate {"CONFIRMED" if pure else "OPEN"}. Baseline transfer{sum(c["same_selected_old_history"] for c in cases)}/22 and identical assignment histories{sum(p["same_history"] for p in pairs)}/11. Scope is the selected standard finite game. Evidence: experiments/validation/analysis/wall_prefix_selector/RESULTS.md. D andbest.pyunchanged.\n')
    print(json.dumps({k:result[k] for k in ('time_utc','new_games','h1','h2','h3','external_fresh_calls','uniform_GJN_payoff_by_seat')}),flush=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['declare','branches','publish'])
    parser.add_argument('--index',type=int,choices=[0,1,2])
    args=parser.parse_args()
    if args.mode=='branches':
        assert args.index is not None
        branches(args.index)
    else:globals()[args.mode]()


if __name__=='__main__':main()

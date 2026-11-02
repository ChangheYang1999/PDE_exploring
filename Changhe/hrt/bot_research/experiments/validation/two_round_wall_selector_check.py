"""Prospectively declare and independently validate the two-round selector."""
from collections import defaultdict
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse, hashlib, json, time
from bot_research.bots.counters.two_round_wall_selector import TwoRoundWallSelector
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.finite_table_certificate import verify as certificate
from bot_research.experiments.validation.policy_value_snapshot import freeze_state
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.publish_ten_policy_game_v2 import norm
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.wall_prefix_selector_check_v2 import canonical_records
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
E=Path('bot_research/experiments/validation'); R=Path('bot_research/runs/validation')
A=E/'analysis/two_round_wall_selector'; D=E/'two-round-wall-selector-001.json'
ORDER=['B','C','D','G','H','I','J','L','M','N','O','P','Q','R']
BRANCH=dict(zip(ORDER,['G','L','L','G','L','L','L','G','G','G','G','G','G','G']))
TAU={k:(3 if k in ('C','D','H','I','J','P','Q') else 2) for k in ORDER}
PREDICTED=[1,0,1,0,1,0,1,1,1,1,0,1,0,0]
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def verify():
    d=read(D)
    for p,h in d['input_sha256'].items():assert sha(p)==h,p
    return d

def declare():
    prior=read(E/'wall-prefix-selector-001.json')
    policies=dict(prior['policies'])
    policies['P']=read(E/'delayed-wall-counter-001.json')['policies']['P']
    policies['Q']=read(E/'reserved-wall-counter-001.json')['policies']['Q']
    policies['R']=dict(id='R',spec='bot_research.bots.counters.two_round_wall_selector:@make')
    parents={k:read(E/'analysis'/area/'verification/full_games.json') for k,area in
        [('O','wall_prefix_selector'),('P','delayed_wall_counter'),('Q','reserved_wall_counter')]}
    assert all(p['all_passed'] for p in parents.values())
    modules={'bot_research.experiments.validation.'+s for s in ('two_round_wall_selector_check',
        'run_data_development','audit_development_strict','replay_audit','audit_data_archives','check_fixed_game_histories')}
    modules|={p['spec'].partition(':')[0] for p in policies.values()}
    paths=set(static_closure(modules))|{A/'PROOF.md',A/'PROTOCOL.md',
        E/'reviews/two-round-wall-selector-review-001.md',Path('td_game/balanced.json'),Path('configs/balanced.json')}
    for stem,area in [('wall-prefix-selector','wall_prefix_selector'),('delayed-wall-counter','delayed_wall_counter'),('reserved-wall-counter','reserved_wall_counter')]:
        paths|={E/(stem+'-001.json'),E/'analysis'/area/'PROOF.md',E/'analysis'/area/'verification/full_games.json'}
    paths|={Path(p) for p in prior['input_sha256'] if '/data/' in p and p.endswith('.json')}
    baselines=[]
    for target in ORDER:
        for side in (0,1):
            if target in ORDER[:10] or target=='R':
                old_target='O' if target=='R' else target
                b=deepcopy(next(b for b in prior['baselines'] if b['opponent']==old_target and b['side']==side))
                b['opponent']=target
            else:
                matches=[c for c in parents[target]['cases'] if c['opponent']=='G' and 1-c['side']==side]
                assert len(matches)==1,(target,side)
                c=matches[0];raw=read(c['result'])
                b=dict(opponent=target,side=side,selected='G',result=c['result'],replay=raw['replay_path'],
                    reference_side=side,old_pair=[target,'G'])
            paths|={Path(b['result']),Path(b['replay'])};baselines.append(b)
    pins={str(p):sha(p) for p in sorted(paths)};stamp=now();campaigns=[]
    for index,opponents in enumerate([ORDER[:5],ORDER[5:10],ORDER[10:]]):
        name=f'two-round-wall-selector-{index:02d}-001'
        atomic_json(E/(name+'.json'),dict(declared_utc=stamp,candidates=[policies['R']],
            opponents=[policies[k] for k in opponents],input_sha256=pins,
            purpose='Selected two-round public-prefix response; standard starts, no reserved D.'),exclusive=True)
        campaigns.append(dict(name=name,opponents=opponents,expected=2*len(opponents)))
    atomic_json(D,dict(declared_utc=stamp,new_games=28,policy_calls_before_declaration=0,
        policies=policies,order=ORDER,campaigns=campaigns,baselines=baselines,input_sha256=pins,
        predicted_branches=BRANCH,predicted_selection_rounds=TAU,predicted_payoffs=PREDICTED,
        hypotheses=['H1 exact predicted branch and selection round in each game',
        'H2 exact selected old history in every game','H3 exact predicted payoff row in both seats',
        'H4 support-row premises for a pure-R value-zero certificate in every skew completion']),exclusive=True)
    print(json.dumps(dict(time_utc=stamp,new_games=28,pins=len(pins),policy_calls_before_declaration=0)),flush=True)

def branches(index):
    begin=time.perf_counter();d=verify();campaign=d['campaigns'][index];root=R/campaign['name']
    inputs={**d['input_sha256'],str(D):sha(D)}
    def checked_read(p):inputs[str(p)]=sha(p);return read(p)
    source=checked_read(root/'freeze.json')['source_sha256']
    for p,h in source.items():assert sha(p)==h;inputs[p]=h
    cases=[]
    for job in checked_read(root/'jobs.json'):
        path=root/'results'/(job['id']+'.json');checked_row(str(path),inputs);row=checked_read(path)
        side=row['condition']['candidate_side'];target=row['condition']['opponent_id'];rounds=row['rounds']
        inputs[row['replay_path']]=sha(row['replay_path'])
        records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
        assert rounds>=3 and len(records)==2*(rounds+1)
        assert all(rec['round']==i//2 and rec['player']==i%2 for i,rec in enumerate(records))
        assert all(rec.get('result') is None for rec in records[:-2])
        assert records[-1]['result'] is not None and records[-1]['result']==records[-2]['result']==row['result']
        enemy1=records[2+(1-side)]['snapshot'];enemy2=records[4+(1-side)]['snapshot']
        present1=bool(enemy1['buildings'] or enemy1['roster']);present2=bool(enemy2['buildings'] or enemy2['roster'])
        selected='G' if present1 or present2 else 'L';tau=2 if present1 else 3
        selector=TwoRoundWallSelector();reference=resolve({'spec':d['policies'][selected]['spec']})
        reference_object=reference.decide.__self__;cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']))
        assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
        trace=[]
        for rnd in range(1,rounds+1):
            obs=engine.observation(side);saved=deepcopy(obs)
            got=selector.decide(obs);assert obs==saved
            arg=deepcopy(saved);expected=reference.decide(arg);assert arg==saved
            pair=records[2*rnd:2*rnd+2]
            actions=[[e['action'] for e in rec['event'] if e['kind']=='action'] for rec in pair]
            assert got==expected==actions[side],(target,side,rnd,'actions')
            own=player_from_snapshot(saved['players'][side])
            assert all(apply_action(own,a,rnd,cfg)['accepted'] for a in got)
            chosen=selector.g if selected=='G' else selector.l
            assert freeze_state(vars(chosen))==freeze_state(vars(reference_object)),(target,side,rnd,'state')
            assert selector.selected==(None if rnd<tau else selected)
            assert selector.selection_round==(None if rnd<tau else tau)
            assert normalized(engine.play_round(actions))==pair
            trace.append(dict(**selector.trace[-1],selected_reference_actions_agree=True,selected_reference_state_agrees=True))
        assert engine.result==row['result']
        baseline=next(b for b in d['baselines'] if b['opponent']==target and b['side']==side)
        applicable=baseline['selected']==selected
        current=canonical_records(row['replay_path'],side);previous=canonical_records(baseline['replay'],baseline['reference_side'])
        same=applicable and current==previous;divergence=None
        if applicable and not same:
            offset=next((i for i in range(min(len(current),len(previous))) if current[i]!=previous[i]),min(len(current),len(previous)))
            divergence=dict(record_index=offset,new=current[offset] if offset<len(current) else None,old=previous[offset] if offset<len(previous) else None)
        cases.append(dict(result_path=str(path),opponent=target,side=side,selected=selected,selection_round=tau,
            predicted_branch_agrees=selected==BRANCH[target] and tau==TAU[target],trace=trace,whole_stream_checked=True,
            baseline=baseline,baseline_applicable=applicable,same_selected_old_history=same,first_divergence=divergence,
            rounds=rounds,selector_calls=rounds,reference_calls=rounds))
        print(json.dumps(dict(time_utc=now(),case=job['id'],selected=selected,selection_round=tau,calls_each=rounds,baseline_history_agrees=same)),flush=True)
    assert len(cases)==campaign['expected'];verify();assert all(sha(p)==h for p,h in inputs.items())
    atomic_json(R/(campaign['name']+'-branches.json'),dict(time_utc=now(),all_passed=True,all_replayed=True,
        all_actions_legal=True,all_observations_unchanged=True,all_reference_actions_agree=True,all_reference_states_agree=True,
        selector_calls=sum(c['selector_calls'] for c in cases),reference_calls=sum(c['reference_calls'] for c in cases),
        cases=cases,input_sha256=inputs,elapsed_seconds=time.perf_counter()-begin),exclusive=True)

def publish():
    d=verify();inputs={**d['input_sha256'],str(D):sha(D)};cases=[];fresh_calls=selector_calls=reference_calls=0
    def checked_read(p):inputs[str(p)]=sha(p);return read(p)
    for campaign in d['campaigns']:
        name,n=campaign['name'],campaign['expected'];root=R/name
        audits={k:checked_read(R/(name+'-'+k+'.json')) for k in ('strict','replay','data','fresh','branches')}
        strict=audits['strict']
        assert strict['valid_conditions']==strict['expected_conditions']==n
        assert strict['attempt_counts']=={'valid':n} and not strict['unresolved'] and not strict['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count']==n and audits['data']['all_passed']
        for kind,audit in audits.items():
            for p,h in audit.get('input_sha256',audit.get('inputs',{})).items():assert sha(p)==h,p;inputs[p]=h
        for k in ('fresh','branches'):
            assert all(audits[k][n] for n in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'))
        assert audits['fresh']['games']==n
        assert audits['branches']['all_reference_actions_agree'] and audits['branches']['all_reference_states_agree']
        fresh_calls+=audits['fresh']['checked_calls'];selector_calls+=audits['branches']['selector_calls'];reference_calls+=audits['branches']['reference_calls']
        branchmap={c['result_path']:c for c in audits['branches']['cases']}
        for job in checked_read(root/'jobs.json'):
            path=root/'results'/(job['id']+'.json');row=checked_row(str(path),inputs);target=row['condition']['opponent_id']
            assert norm(row['condition']['candidate_spec'])==norm(d['policies']['R']['spec'])
            assert norm(row['condition']['opponent_spec'])==norm(d['policies'][target]['spec'])
            b=branchmap[str(path)]
            cases.append(dict(opponent=target,side=row['condition']['candidate_side'],outcome=row['outcome'],
                payoff={'W':1,'D':0,'L':-1}[row['outcome']],hp_R_first=row['hp_candidate_first'],rounds=row['rounds'],
                selected=b['selected'],selection_round=b['selection_round'],predicted_branch_agrees=b['predicted_branch_agrees'],
                canonical_replay_sha256=row['canonical_replay_sha256'],baseline_applicable=b['baseline_applicable'],
                same_selected_old_history=b['same_selected_old_history'],first_divergence=b['first_divergence'],result=str(path)))
    assert len(cases)==28 and fresh_calls==2*sum(c['rounds'] for c in cases)
    assert selector_calls==reference_calls==sum(c['rounds'] for c in cases)
    groups=defaultdict(list)
    for c in cases:groups[c['opponent']].append(c)
    pairs=[]
    for target in ORDER:
        group=sorted(groups[target],key=lambda c:c['side']);assert len(group)==2 and [c['side'] for c in group]==[0,1]
        pairs.append(dict(opponent=target,same_history=group[0]['canonical_replay_sha256']==group[1]['canonical_replay_sha256'],same_outcome=group[0]['outcome']==group[1]['outcome']))
    h1=all(c['predicted_branch_agrees'] for c in cases);h2=all(c['same_selected_old_history'] for c in cases)
    h3=all(c['payoff']==PREDICTED[ORDER.index(c['opponent'])] for c in cases)
    h4=all(p['same_outcome'] for p in pairs) and all(c['payoff']>=0 for c in cases) and all(c['payoff']==0 for c in groups['R'])
    support_certificate=None
    if h4:
        row=[groups[k][0]['payoff'] for k in ORDER];completion=[[0]*14 for _ in ORDER]
        for i,v in enumerate(row):completion[-1][i]=v;completion[i][-1]=-v
        weights=['0']*13+['1'];assert certificate(completion,weights)
        assert not certificate(completion,['0']*14)
        support_certificate=dict(weights=weights,column_payoffs=row,exact_value='0',
            scope='Every real skew-symmetric completion matching this support row; no complete table asserted.')
    stamp=now();verdict=lambda x:'CONFIRMED' if x else 'REFUTED'
    lines=['# Waiting through two shared decisions','',f'Completed {stamp}.','',
        f'H1 **{verdict(h1)}**: predicted selection member and round in every game.',
        f'H2 **{verdict(h2)}**: every full history equals its selected retained control.',
        f'H3 **{verdict(h3)}**: the predicted payoff row holds in both physical assignments.',
        f'H4 **{verdict(h4)}**: paired outcomes and a nonnegative support row with self draw establish the conditional pure-R certificate.','',
        'R advances both G and L through round one. If the enemy remains publicly empty, it advances both through their shared five-factory round two. It chooses G when buildings or roster become visible, otherwise L in round three. The selected private state is retained. This is selected development evidence after O, P and Q, not held-out evaluation.','',
        '| Opponent | Member and selection round | Seat0 outcome and HP | Seat1 outcome and HP | Rounds0/1 |',
        '| --- | --- | --- | --- | --- |']
    for target in ORDER:
        x,y=sorted(groups[target],key=lambda c:c['side'])
        lines.append(f'| {target} | {x["selected"]}@{x["selection_round"]}/{y["selected"]}@{y["selection_round"]} | {x["outcome"]} {x["hp_R_first"][0]}:{x["hp_R_first"][1]} | {y["outcome"]} {y["hp_R_first"][0]}:{y["hp_R_first"][1]} | {x["rounds"]}/{y["rounds"]} |')
    lines+=['',f'All28 new games pass strict action/source accounting, data archival checks, full original-engine replay and {fresh_calls} fresh external decisions. An additional {selector_calls} R and {reference_calls} standalone member calls agree in actions and selected private values at every round. All terminal boundaries are checked.',
        '',f'{sum(p["same_history"] for p in pairs)}/14 paired normalized full histories agree; {sum(c["same_selected_old_history"] for c in cases)}/28 retained baseline transfers agree. First divergences and inapplicable baselines, if any, are retained.',
        '', 'The pure-support result concerns any skew-symmetric completion of this fourteen-policy set matching the observed R row. Other pairs remain unmeasured and uniqueness is not claimed. It does not imply a universal best response, strength against new opponents, or immunity to wall-clock deadline changes. These executions check the conditional coupling result only at their recorded conditions. Final best.py and reserved D are unchanged.']
    with (A/'RESULTS.md').open('x') as f:f.write('\n'.join(lines)+'\n')
    inputs[str(A/'RESULTS.md')]=sha(A/'RESULTS.md');verify();assert all(sha(p)==h for p,h in inputs.items())
    result=dict(time_utc=stamp,all_passed=True,new_games=28,h1=h1,h2=h2,h3=h3,h4=h4,order=ORDER,
        fresh_external_calls=fresh_calls,extra_selector_calls=selector_calls,extra_reference_calls=reference_calls,
        support_certificate=support_certificate,cases=cases,pairs=pairs,input_sha256=inputs)
    atomic_json(A/'verification/full_games.json',result,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Two-round selector complete\n\nH1 branch/round {verdict(h1)}; H2 exact baseline transfers {verdict(h2)}; H3 predicted row {verdict(h3)}; H4 pure-R support certificate {verdict(h4)}.28newgames,{fresh_calls} fresh external calls,{selector_calls} extra R and{reference_calls} standalone component calls. Scope and exact outcomes: experiments/validation/analysis/two_round_wall_selector/RESULTS.md. No final-candidate change or reserved D use.\n')
    print(json.dumps({k:result[k] for k in ('time_utc','new_games','h1','h2','h3','h4','fresh_external_calls')}),flush=True)

def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['declare','branches','publish']);p.add_argument('--index',type=int,choices=[0,1,2]);a=p.parse_args()
    if a.mode=='branches':assert a.index is not None;branches(a.index)
    else:globals()[a.mode]()
if __name__=='__main__':main()

"""Declare and audit a round-three reserved-wall counter on the original engine."""
from collections import defaultdict
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from bot_research.bots.counters.two_round_wall_selector import TwoRoundWallSelector
from bot_research.bots.counters.wall_signal_repair import WallSignalRepair
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.policy_value_snapshot import freeze_state
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.wall_prefix_selector_check_v2 import canonical_records
from td_game.config import balanced_config
from td_game.engine import Engine

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
A=E/'analysis/late_reserved_wall_counter';D=E/'late-reserved-wall-counter-001.json'
ORDER=['R','L','G','B','N']
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def verify():
    d=read(D)
    for p,h in d['input_sha256'].items():assert sha(p)==h,p
    return d

def declare():
    prior=read(E/'two-round-wall-selector-001.json')
    policies={k:prior['policies'][k] for k in ORDER}
    policies['S']=dict(id='S',spec='bot_research.bots.counters.late_reserved_wall_guard:@make')
    modules={'bot_research.experiments.validation.'+s for s in (
        'late_reserved_wall_counter_check','run_data_development','audit_development_strict',
        'replay_audit','audit_data_archives','check_fixed_game_histories')}
    modules|={p['spec'].partition(':')[0] for p in policies.values()}
    paths=set(static_closure(modules))|{A/'PROOF.md',A/'PROTOCOL.md',Path('td_game/balanced.json'),Path('configs/balanced.json'),
        E/'analysis/two_round_wall_selector/PROOF.md',E/'analysis/reserved_wall_counter/PROOF.md',
        E/'two-round-wall-selector-001.json',E/'reserved-wall-counter-001.json',
        E/'reviews/late-reserved-wall-counter-review-001.md',
        E/'analysis/two_round_wall_selector/verification/full_games.json',
        E/'analysis/two_round_wall_selector/verification/context_supplement.json'}
    paths|={Path(p) for p in prior['input_sha256'] if '/data/' in p and p.endswith('.json')}
    pins={str(p):sha(p) for p in sorted(paths)};stamp=now();campaigns=[]
    for index,opponents in enumerate([ORDER[:3],ORDER[3:]]):
        name=f'late-reserved-wall-counter-{index:02d}-001'
        atomic_json(E/(name+'.json'),dict(declared_utc=stamp,candidates=[policies['S']],
            opponents=[policies[k] for k in opponents],input_sha256=pins,
            purpose='Selected development counter: two empty public rounds with round-four reservation; no reserved D.'),exclusive=True)
        campaigns.append(dict(name=name,opponents=opponents,expected=2*len(opponents)))
    atomic_json(D,dict(declared_utc=stamp,new_games=10,policy_calls_before_declaration=0,
        policies=policies,order=ORDER,campaigns=campaigns,input_sha256=pins,
        hypotheses=['H1 S wins both assignments against R','H2 R selects L in round3 and S/R equals S/L in each seat',
                    'H3 paired normalized full histories and outcomes agree for each opponent',
                    'H4 all ten games reach round4 with the exact declared opening and 261 gold / 11 factories before one tier4 action; early termination refutes this empirical premise']),exclusive=True)
    print(json.dumps(dict(time_utc=stamp,new_games=10,pins=len(pins),policy_calls_before_declaration=0)),flush=True)

def check():
    begin=time.perf_counter();d=verify();inputs={**d['input_sha256'],str(D):sha(D)}
    def checked_read(p):inputs[str(p)]=sha(p);return read(p)
    cases=[];fresh_calls=selector_calls=reference_calls=0;traces=[]
    for campaign in d['campaigns']:
        name,n=campaign['name'],campaign['expected'];root=R/name
        audits={k:checked_read(R/(name+'-'+k+'.json')) for k in ('strict','replay','data','fresh')}
        strict=audits['strict']
        assert strict['valid_conditions']==strict['expected_conditions']==n
        assert strict['attempt_counts']=={'valid':n} and not strict['unresolved'] and not strict['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count']==n and audits['data']['all_passed']
        fresh=audits['fresh']
        assert fresh['games']==n and all(fresh[k] for k in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'))
        for audit in audits.values():
            for p,h in audit.get('input_sha256',audit.get('inputs',{})).items():assert sha(p)==h;inputs[p]=h
        fresh_calls+=fresh['checked_calls']
        for job in checked_read(root/'jobs.json'):
            path=root/'results'/(job['id']+'.json');row=checked_read(path);clean=checked_row(str(path),inputs)
            side=row['condition']['candidate_side'];target=row['condition']['opponent_id'];rounds=row['rounds']
            assert row['condition']['candidate_spec']==d['policies']['S']['spec']
            assert row['condition']['opponent_spec']==d['policies'][target]['spec']
            replay=row['replay_path'];inputs[replay]=sha(replay)
            records=[json.loads(s) for s in Path(replay).read_text().splitlines()]
            assert rounds>=1 and len(records)==2*(rounds+1)
            assert all(rec['round']==i//2 and rec['player']==i%2 for i,rec in enumerate(records))
            assert all(rec.get('result') is None for rec in records[:-2])
            assert records[-1]['result'] is not None and records[-1]['result']==records[-2]['result']==row['result']
            first=[e['action'] for e in records[2+side]['event'] if e['kind']=='action']
            firstsnap=records[2+side]['snapshot']
            second=[e['action'] for e in records[4+side]['event'] if e['kind']=='action'] if rounds>=2 else None
            secondsnap=records[4+side]['snapshot'] if rounds>=2 else None
            third=records[6+side]['snapshot'] if rounds>=3 else None
            thirdactions=[e['action'] for e in records[6+side]['event'] if e['kind']=='action'] if rounds>=3 else None
            fourth=[e['action'] for e in records[8+side]['event'] if e['kind']=='action'] if rounds>=4 else None
            witness=next(w for w in read('bot_research/bots/counters/data/early_wall_guard_001.json')['witnesses'] if w['id']=='guard00')
            expectedthird=([dict(op='build_wall',x=x,y=y) for x,y in witness['walls']]
                +[dict(op='build_turret',**t) for t in witness['turrets']]+[dict(op='buy_factory')]*2)
            opening_ok=(first==[dict(op='buy_factory')]*5 and not firstsnap['buildings'] and not firstsnap['roster']
                and firstsnap['gold']==97 and firstsnap['n_factories']==5
                and secondsnap is not None and second==[dict(op='buy_factory')]*4
                and not secondsnap['buildings'] and not secondsnap['roster']
                and secondsnap['gold']==174 and secondsnap['n_factories']==9 and thirdactions==expectedthird)
            reservation_ok=(opening_ok and third is not None and fourth is not None and third['gold']==261
                and third['n_factories']==11 and fourth==[dict(op='buy_minion',type='tier4')])
            detail=dict(opponent=target,side=side,result=str(path),replay=replay,outcome=clean['outcome'],
                hp_S_first=clean['hp_candidate_first'],rounds=rounds,
                canonical_replay_sha256=clean['canonical_replay_sha256'],
                first_actions=first,second_actions=second,
                first_snapshot=firstsnap,second_snapshot=secondsnap,third_actions=thirdactions,opening_ok=opening_ok,
                third_snapshot=third,fourth_actions=fourth,reservation_ok=reservation_ok)
            if target=='R':
                selector=TwoRoundWallSelector();reference=WallSignalRepair();engine=Engine(balanced_config(),tuple(row['bot_specs']))
                assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
                trace=[]
                for rnd in range(1,rounds+1):
                    obs=engine.observation(1-side);saved=deepcopy(obs)
                    got=selector.decide(obs);assert obs==saved
                    arg=deepcopy(saved);expected=reference.decide(arg);assert arg==saved
                    pair=records[2*rnd:2*rnd+2]
                    actions=[[e['action'] for e in rec['event'] if e['kind']=='action'] for rec in pair]
                    assert got==expected==actions[1-side],(side,rnd,'selected actions')
                    assert freeze_state(vars(selector.l))==freeze_state(vars(reference)),(side,rnd,'selected values')
                    assert selector.selected==(None if rnd<3 else 'L')
                    assert selector.selection_round==(None if rnd<3 else 3)
                    assert normalized(engine.play_round(actions))==pair
                    trace.append(deepcopy(selector.trace[-1]))
                assert engine.result==row['result']
                selector_calls+=rounds;reference_calls+=rounds
                traces.append(dict(side=side,trace=trace,all_actions_agree=True,all_selected_values_agree=True))
            cases.append(detail)
    assert len(cases)==10 and fresh_calls==2*sum(c['rounds'] for c in cases)
    by=defaultdict(list)
    for c in cases:by[c['opponent']].append(c)
    pairs=[]
    for target in ORDER:
        x,y=sorted(by[target],key=lambda c:c['side']);assert (x['side'],y['side'])==(0,1)
        pairs.append(dict(opponent=target,same_outcome=x['outcome']==y['outcome'],
            same_history=canonical_records(x['replay'],0)==canonical_records(y['replay'],1)))
    transfers=[]
    for side in (0,1):
        o=next(c for c in by['R'] if c['side']==side);l=next(c for c in by['L'] if c['side']==side)
        oc,lc=canonical_records(o['replay'],side),canonical_records(l['replay'],side)
        same=oc==lc;div=None
        if not same:
            index=next((i for i in range(min(len(oc),len(lc))) if oc[i]!=lc[i]),min(len(oc),len(lc)))
            div=dict(index=index,R=oc[index] if index<len(oc) else None,L=lc[index] if index<len(lc) else None)
        transfers.append(dict(side=side,same_history=same,first_divergence=div))
    h1=all(c['outcome']=='W' for c in by['R'])
    h2=(len(traces)==2 and all(any(x.get('selected')=='L' and x.get('round')==3 for x in t['trace']) for t in traces)
        and all(t['same_history'] for t in transfers))
    h3=all(p['same_outcome'] and p['same_history'] for p in pairs)
    h4=all(c['reservation_ok'] for c in cases)
    stamp=now();verdict=lambda x:'CONFIRMED' if x else 'REFUTED'
    lines=['# Reserving the heavy purchase after two empty public rounds','',f'Completed {stamp}.','',
        f'H1 **{verdict(h1)}**: S wins both assignments against R.',
        f'H2 **{verdict(h2)}**: R selects L in round3 and both S/R histories equal their S/L controls.',
        f'H3 **{verdict(h3)}**: all five assignment pairs match in outcome and normalized full history.',
        f'H4 **{verdict(h4)}**: all ten games have the exact declared opening, reach261gold and11factories after round3 and buy exactly one tier4 in round4.','',
        'S keeps its buildings and roster empty through round2. In round3 it builds the guard00 walls and splash, then withholds two of the four affordable factories so that round4 starts with261gold and11factories. R therefore selects L before observing the construction. S retains the tier4 purchase in round4 and frozen Fortress38 from round5. The source proof establishes branch selection and the reservation arithmetic; victory is measured.','',
        '| Opponent | Seat0 outcome, HP | Seat1 outcome, HP | Rounds0/1 |','| --- | --- | --- | --- |']
    for target in ORDER:
        x,y=sorted(by[target],key=lambda c:c['side'])
        lines.append(f'| {target} | {x["outcome"]} {x["hp_S_first"][0]}:{x["hp_S_first"][1]} | {y["outcome"]} {y["hp_S_first"][0]}:{y["hp_S_first"][1]} | {x["rounds"]}/{y["rounds"]} |')
    lines+=['',f'All10 new games pass strict source/action checks, data archive checks, complete original-engine replay and {fresh_calls} fresh external decisions. The extra R/L audit adds {selector_calls} selector calls and {reference_calls} standalone L calls, with exact actions and selected logical values. Every stream has an explicit terminal boundary.',
        '', 'These selected standard-start conditions do not establish unseen strength. Any counterexample extends the finite policy set; it does not invalidate a certificate restricted to the previous set. Sources include wall-clock deadlines, so exact paired reproduction describes these executions. No final candidate or reserved D input is changed.']
    with (A/'RESULTS.md').open('x') as f:f.write('\n'.join(lines)+'\n')
    inputs[str(A/'RESULTS.md')]=sha(A/'RESULTS.md')
    verify();assert all(sha(p)==h for p,h in inputs.items())
    result=dict(time_utc=stamp,all_passed=True,new_games=10,h1=h1,h2=h2,h3=h3,h4=h4,cases=cases,pairs=pairs,
        transfers=transfers,selector_traces=traces,fresh_external_calls=fresh_calls,
        extra_selector_calls=selector_calls,extra_reference_calls=reference_calls,
        input_sha256=inputs,elapsed_seconds=time.perf_counter()-begin)
    atomic_json(A/'verification/full_games.json',result,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Late reserved-wall counter complete\n\nH1 S wins both R assignments {verdict(h1)}; H2 selects L and matches full S/L history {verdict(h2)}; H3 all five paired histories agree {verdict(h3)}; H4 reservation arithmetic {verdict(h4)}.10newgames,{fresh_calls} fresh external calls,{selector_calls} additional R and{reference_calls} L calls. Exact outcomes and scope: experiments/validation/analysis/late_reserved_wall_counter/RESULTS.md.\n')
    print(json.dumps({k:result[k] for k in ('time_utc','h1','h2','h3','h4','new_games','fresh_external_calls')}),flush=True)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['declare','check']);args=parser.parse_args()
    globals()[args.mode]()
if __name__=='__main__':main()

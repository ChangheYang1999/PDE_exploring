"""Protocol163: ten new V games, exact five-round audit, and finite hypotheses.

Declare is source-only. Mechanism makes only the declared first-five calls on
four recorded V/T,U histories. Check replays records and runs no policies.
"""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import os
import sys
import time

from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.wall_timing_transfer_check import (
    DATA, AUDIT_KINDS, now, safe_path, sha, read, require, pin, checked_read,
    make_spec, identity, validate_condition, verify_archive, canonical_records,
    canonical_sha, aggregate_verdict, inspect_case as inspect_original_case)

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E/'analysis/fourth_round_wall_counter'
D = E/'fourth-round-wall-counter-001.json'
NAME = 'fourth-round-wall-counter-00-001'
ROOT = R/NAME
ORDER = ['T', 'U', 'G', 'B', 'N']
GRID = [('V', opponent, side) for opponent in ORDER for side in (0, 1)]
COUNTER_KEYS = ('actual_V', 'actual_selector', 'reference_G', 'reference_L4')
NESTED_KEYS = ('internal_G', 'internal_L4', 'internal_H_model', 'reference_H_model', 'V_defender')
RUNNER_ROOTS = {'bot_research.experiments.validation.'+name for name in (
    'fourth_round_wall_counter_check', 'fourth_round_wall_counter_pipeline',
    'run_data_development', 'isolated_match', 'audit_development_strict', 'replay_audit',
    'audit_data_archives', 'check_fixed_game_histories', 'policy_value_snapshot',
    'required_sources', 'source_closure')}


def policy_specs():
    stem = 'bot_research.bots.counters.'
    specs = dict(V=make_spec(stem+'fourth_round_wall'),
        T=make_spec(stem+'third_round_wait'), U=make_spec(stem+'blind_fourth_round'),
        G=make_spec(stem+'early_wall_guard', witness='guard00'),
        B=make_spec('bot_research.experiments.lead.frozen.best_v9e'),
        N=make_spec('bot_research.experiments.lead.frozen.best_v9e', attack_share=1.0, catch_up_share=0.5),
        H=make_spec(stem+'hp_handoff', layout='empty', growth_rounds=6, bait=[],
            bait_round=2, tier='tier5', factory_cap=2000, purchase_cap=1000,
            replan_iters=5000, deadline=12, lead_from=8))
    return {k:dict(id=k,spec=v) for k,v in specs.items()}


def assert_environment():
    require(sys.flags.optimize == 0 and os.environ.get('PYTHONOPTIMIZE','') in ('','0'),
            'Assertions must remain enabled in inherited audit helpers.')


def declare(reviews):
    assert_environment()
    require(reviews, 'Independent source review required before declaration.')
    policies = policy_specs()
    require(sha('bot_research/experiments/lead/frozen/best_v9e.py') ==
            '70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87',
            'Frozen B/N parent bytes differ.')
    modules = RUNNER_ROOTS | {v['spec'].partition(':')[0] for v in policies.values()}
    # H is dynamic inside the model, so its module is an explicit root.
    paths = set(static_closure(modules)) | set(DATA) | {
        A/'PROOF.md', A/'PROTOCOL.md', A/'INDEX.md', A/'verification/policy_source_closure_final.json',
        E/'analysis/third_round_wait/PROOF.md', E/'analysis/blind_fourth_round/PROOF.md',
        Path('td_game/balanced.json'), Path('configs/balanced.json')}
    paths.update(safe_path(p) for p in reviews)
    pins = {str(p):sha(p) for p in sorted(paths)}
    manifest_path = E/(NAME+'.json')
    require(not D.exists() and not manifest_path.exists(), 'Do not overwrite a declaration.')
    stamp = now()
    manifest = dict(declared_utc=stamp,candidates=[policies['V']],opponents=[policies[k] for k in ORDER],
        expected_conditions=10,additional_source_modules=sorted(RUNNER_ROOTS),input_sha256=pins,
        purpose='Ten selected new V/T,U,G,B,N standard games; descriptive G/B/N controls; no reserved D.')
    atomic_json(manifest_path,manifest,exclusive=True)
    atomic_json(D,dict(declared_utc=stamp,protocol=163,new_games=10,retained_games=0,total_records=10,
        new_V_calls_before_declaration=0,policies=policies,order=ORDER,
        campaigns=[dict(name=NAME,manifest=str(manifest_path),manifest_sha256=sha(manifest_path),
                        opponents=ORDER,expected=10)], input_sha256=pins,retained_input_sha256={},
        static_roots=sorted(modules),explicit_data=[str(p) for p in DATA],reviews=list(map(str,reviews)),
        hypotheses=dict(H1='All four V/T,U games reach5 with exact first-five state and private chronology.',
            H2='V wins each of the four T/U games in both physical assignments.',
            H3='Complete V/T and V/U canonical histories match for each V physical assignment.'),
        mechanism_cases=[0,1,2,3],mechanism_round_limit=5,
        mechanism_scope='Fresh V and T/U plus G/L4 references on actual first-five observations only. '
            'One additional cold default F38 constructor per case, no defender decision calls. '
            'Normalized-name reference observations check the early name-ignoring state transitions.',
        fresh_scope='Both persistent external policies regenerated over all ten complete histories.',
        selftest_scope='Pure predicate corruption fixtures after declaration, zero policy decisions.',
        later_F38_scope='Source once-per-round delegation from6 plus ordinary full V fresh replay; '
            'no second full defender reference replay.'),exclusive=True)
    print(json.dumps(dict(time_utc=stamp,new_games=10,active_pins=len(pins))),flush=True)


def verify_declaration(inputs):
    assert_environment()
    d=checked_read(D,inputs)
    require(d['protocol']==163 and d['policies']==policy_specs() and d['order']==ORDER
        and d['new_games']==d['total_records']==10 and d['retained_games']==0, 'Declaration grid/spec differs.')
    require(d['mechanism_cases']==[0,1,2,3] and d['mechanism_round_limit']==5, 'Mechanism scope differs.')
    for field in ('input_sha256','retained_input_sha256'):
        for p,h in d[field].items(): pin(p,inputs,h)
    for p in set(static_closure(set(d['static_roots'])))|set(DATA):
        require(str(p) in d['input_sha256'],'Missing source/data pin: '+str(p))
    require(len(d['campaigns'])==1,'Exactly one campaign required.')
    c=d['campaigns'][0]
    require(c['name']==NAME and c['opponents']==ORDER and c['expected']==10,'Campaign identity differs.')
    m=checked_read(c['manifest'],inputs,c['manifest_sha256'])
    require(m['input_sha256']==d['input_sha256'] and m['candidates']==[d['policies']['V']]
        and m['opponents']==[d['policies'][k] for k in ORDER] and m['expected_conditions']==10,
        'Campaign manifest differs.')
    return d


def opening_check(records, opponent, side, rounds, witness):
    if opponent not in ('T','U'):
        return dict(applicable=False,passed=None,rounds=[],violations=[])
    F=dict(op='buy_factory'); X=dict(type='splash',x=1,y=3)
    W=[dict(type='wall',x=x,y=y) for x,y in witness['walls']]
    wa=[dict(op='build_wall',x=x,y=y) for x,y in witness['walls']]
    xa=dict(op='build_turret',**X)
    va=[[F]*5,[F]*4,[F]*8,wa+[xa]+[F]*10,[dict(op='buy_minion',type='tier4')]+[F]*9]
    sa=[wa+[F]*4,[F]*5,[xa]+[F]*5,[dict(op='buy_minion',type='tier2')]*6+[F],[F]*13]
    vv=[(97,5,22,800),(174,9,22,800),(291,17,22,800),(458,27,42,800),(605,36,42,800)]
    sv=[(100,4,40,800),(175,9,40,800),(267,14,42,800),(274,15,42,800),(476,28,42,740)]
    details=[]; violations=[]
    for rnd in range(1,6):
        if rnd>rounds:
            violations.append(dict(round=rnd,reason='round_not_reached'));details.append(dict(round=rnd,reached=False));continue
        rd=[]
        for role,physical in enumerate((side,1-side)):
            record=records[2*rnd+physical]; snapshot=record['snapshot']
            gold,factories,length,hp=(vv if role==0 else sv)[rnd-1]
            buildings=([] if rnd<4 else W+[X]) if role==0 else W+([] if rnd<3 else [X])
            roster=[]
            if role==0 and rnd==5:
                roster=[dict(id=0,type='tier4',bought_round=5,expires_after_round=16,remaining_rounds=11)]
            elif role==1 and rnd>=4:
                roster=[dict(id=i,type='tier2',bought_round=4,expires_after_round=15,remaining_rounds=15-rnd) for i in range(6)]
            expected=dict(gold=gold,n_factories=factories,length_path=length,hp=hp,buildings=buildings,
                roster=roster,n_walls=sum(b['type']=='wall' for b in buildings),
                n_turrets=sum(b['type']!='wall' for b in buildings))
            income=next(e for e in record['event'] if e['kind']=='income')
            combat=next(e for e in record['event'] if e['kind']=='combat')
            hits=int(role==0 and rnd==5);incoming=int(role==1 and rnd==5)
            spawned=(int(rnd==5) if role==0 else (6 if rnd>=4 else 0))
            killed=6 if role==1 and rnd>=4 else 0
            checks=dict(actions=actions(record)==(va if role==0 else sa)[rnd-1],
                all_actions_accepted=all(e['accepted'] for e in record['event'] if e['kind']=='action'),
                snapshot={k:v for k,v in snapshot.items() if k!='name'}==expected,
                income=income==dict(kind='income',path=length,factories=15*factories,hits=5*hits,total=length+15*factories+5*hits),
                combat=all(combat[k]==v for k,v in dict(outgoing_hits=hits,incoming_hits=incoming,
                    damage_dealt=60*hits,base_damage=60*incoming,spawned=spawned,killed=killed,cleared=0).items()))
            violations.extend(dict(round=rnd,role=role,reason=k) for k,v in checks.items() if not v)
            rd.append(dict(role=role,actions=actions(record),snapshot=snapshot,income=income,combat=combat,checks=checks))
        details.append(dict(round=rnd,reached=True,players=rd))
    return dict(applicable=True,passed=not violations,reached_round_five=rounds>=5,rounds=details,violations=violations)


def inspect_new_case(index,declaration,inputs,witness):
    candidate,opponent,side=GRID[index]
    p=ROOT/'results'/f'case{index:04d}.json'
    detail,history=inspect_original_case(candidate,opponent,side,p,declaration,inputs,witness)
    if history is not None:
        records=[json.loads(s) for s in safe_path(detail['replay']).read_text().splitlines()]
        detail['opening']=opening_check(records,opponent,side,detail['rounds'],witness)
    return detail,history


def finish_hashes(inputs):
    errors = []
    for path, expected in inputs.items():
        try:
            require(sha(path) == expected, 'Changed checked input: ' + path)
        except Exception as error:
            errors.append(public_diagnostic(str(error)))
    return errors


def actions(record):
    return [event['action'] for event in record['event'] if event['kind'] == 'action']


def audit_campaign(declaration, inputs):
    campaign = declaration['campaigns'][0]
    result = dict(name=NAME, expected=10, errors=[], receipts={}, checked_calls=0)
    audits = {}
    for kind in AUDIT_KINDS:
        path = R / (NAME + '-' + kind + '.json')
        try:
            audit = checked_read(path, inputs)
            audits[kind] = audit
            result['receipts'][kind] = str(path)
            for field in ('input_sha256', 'inputs', 'source_sha256'):
                for p, h in audit.get(field, {}).items():
                    pin(p, inputs, h)
        except Exception as error:
            result['errors'].append(dict(stage=kind, diagnostic=public_diagnostic(str(error))))
    try:
        freeze = checked_read(ROOT / 'freeze.json', inputs)
        require(freeze['manifest_sha256'] == campaign['manifest_sha256'], 'Freeze manifest differs.')
        for p, h in declaration['input_sha256'].items():
            require(freeze['source_sha256'].get(p) == h, 'Freeze omitted a declared active input.')
        verify_archive(ROOT, freeze, inputs, compare_current=True)
        jobs = checked_read(ROOT / 'jobs.json', inputs)
        require(len(jobs) == 10 and [identity(job['condition']) for job in jobs] == GRID, 'Ten-job order differs.')
        for job in jobs:
            validate_condition(job['condition'], *identity(job['condition']), declaration['policies'])
            require('prefixes' not in job, 'Only standard starts are declared.')
        strict, replay, data, fresh = [audits[k] for k in AUDIT_KINDS]
        for receipt, module in ((strict, 'audit_development_strict'), (data, 'audit_data_archives')):
            require(receipt['checker_sha256'] == declaration['input_sha256'][str(E / (module+'.py'))],
                    'Audit checker source differs.')
        for p in set(static_closure({'bot_research.experiments.validation.replay_audit'})) | {Path('td_game/balanced.json')}:
            require(replay['source_sha256'].get(str(p)) == declaration['input_sha256'][str(p)], 'Replay source edge absent.')
        for p, h in freeze['source_sha256'].items():
            require(fresh['input_sha256'].get(p) == h, 'Fresh source edge absent.')
        require(strict['valid_conditions'] == strict['expected_conditions'] == 10
                and strict['attempt_counts'] == {'valid': 10} and not strict['unresolved']
                and not strict['repeat_disagreements'], 'Strict attempt accounting failed.')
        require(len(strict['attempts']) == len(strict['cases']) == 10, 'Strict omitted attempts.')
        expected_paths = {str(ROOT / 'results' / (job['id']+'.json')) for job in jobs}
        require({c['result_path'] for c in strict['cases']} == expected_paths, 'Strict cases differ.')
        require(replay['all_passed'] and replay['count'] == 10 and not replay['source_changed_during_run']
                and len(replay['cases']) == 10 and all(c['passed'] for c in replay['cases'])
                and {identity(c['condition']) for c in replay['cases']} == set(GRID), 'Replay cases differ or fail.')
        require(data['all_passed'] and len(data['campaigns']) == 1, 'Data audit failed.')
        dc = data['campaigns'][0]
        require(dc['campaign'] == str(ROOT) and dc['results'] == 10 and dc['all_passed']
                and set(dc['explicit_data']) >= {str(p) for p in DATA}, 'Data campaign/count/certificates differ.')
        require(fresh['games'] == 10 and all(fresh[k] for k in (
            'all_passed', 'all_replayed', 'all_actions_legal', 'all_observations_unchanged')),
            'Fresh audit failed.')
        require(len(fresh['cases']) == 10 and {c['result'] for c in fresh['cases']} == expected_paths,
                'Fresh cases differ.')
        counted = 0
        for case in fresh['cases']:
            row = checked_read(case['result'], inputs)
            require(case['condition'] == row['condition'] and case['exact']
                    and len(case['rounds']) == row['rounds'], 'Fresh case incomplete or different.')
            for rnd, detail in enumerate(case['rounds'], 1):
                require(detail['round'] == rnd and len(detail['calls']) == 2
                        and {c['side'] for c in detail['calls']} == {0, 1}
                        and all(c['exact'] for c in detail['calls']), 'Fresh round/action count differs.')
                counted += 2
        require(fresh['checked_calls'] == counted, 'Fresh successful external call count differs.')
        result['checked_calls'] = counted
    except Exception as error:
        result['errors'].append(dict(stage='cross_receipt_checks', diagnostic=public_diagnostic(str(error))))
    result['passed'] = not result['errors']
    result['attempts'] = audits.get('strict', {}).get('attempts', [])
    result['unresolved'] = audits.get('strict', {}).get('unresolved', [])
    result['fresh_reported_calls'] = audits.get('fresh', {}).get('checked_calls')
    return result


def journal_event(stream, **values):
    stream.write(json.dumps(dict(time_utc=now(), **values), sort_keys=True, allow_nan=False) + '\n')
    stream.flush()
    os.fsync(stream.fileno())


def state_digest(value):
    return hashlib.sha256(repr(value).encode()).hexdigest()


def mutable_container_ids(value, seen=None):
    """Only inspect ordinary captured containers; never mutate policy state."""
    if seen is None:
        seen = set()
    if not isinstance(value, (dict, list, tuple)) or id(value) in seen:
        return set()
    seen.add(id(value))
    result = {id(value)} if isinstance(value, (dict, list)) else set()
    values = list(value.keys()) + list(value.values()) if isinstance(value, dict) else value
    for child in values:
        result.update(mutable_container_ids(child, seen))
    return result


def independent_snapshots(proposed, trace):
    values = [proposed, trace['submitted_actions']]
    values.extend(trace['proposed_actions'].values())
    values.extend(trace['discarded_proposals'].values())
    containers = [mutable_container_ids(value) for value in values]
    return all(not (first & second) for i, first in enumerate(containers) for second in containers[i+1:])

def forecast_geometry(saved, forecast, cfg):
    from bot_research.bots.counters.visible_search import player_from_snapshot
    from td_game.actions import apply_action
    from td_game.pathfinding import shortest_path
    enemy=player_from_snapshot(saved['players'][1-saved['player']])
    legal=[apply_action(enemy,a,saved['round'],cfg)['accepted'] for a in forecast]
    route=shortest_path(cfg.globals.width,cfg.globals.height,{(b.x,b.y) for b in enemy.buildings},cfg.globals.spawn,cfg.globals.base)
    require(route is not None,'Forecast route missing.')
    return dict(all_actions_accepted=all(legal),gold=enemy.gold,n_factories=enemy.n_factories,
        buildings=[dict(type=b.type,x=b.x,y=b.y) for b in enemy.buildings],
        active_roster=[e.type for e in enemy.roster if e.active(saved['round'])],
        length_path=len(route)-1,path=[list(p) for p in route])


def expected_forecast_route(rnd):
    if rnd == 4:
        return [[x,0] for x in range(12)]+[[11,y] for y in range(1,12)]
    return ([[x,0] for x in range(11)]+[[10,y] for y in (1,2)]
        +[[x,2] for x in range(9,-1,-1)]+[[0,y] for y in (3,4)]
        +[[x,4] for x in range(1,12)]+[[11,y] for y in range(5,12)])


def private_claim(record, witness):
    """Pure exact first-five mechanism predicate, separate from execution checks."""
    rnd=record['round']; F=dict(op='buy_factory')
    trace=record['selector_trace']; vt=record['V_trace']
    called=['G','L4'] if rnd<=3 else ['L4']
    selected=None if rnd<=3 else 'L4'
    forecast=([F]*[5,4,8][rnd-1] if rnd<=3 else
              [dict(op='build_turret',type='splash',x=10,y=1)]+[F]*11 if rnd==4 else [F]*22)
    checks=[record['passed'],trace['member_calls']==called,trace['selected']==selected,
        trace['selection_round']==(None if rnd<=3 else 4),trace['returned_member']==(selected or 'G'),
        record['model_last_round']==rnd,record['model_player']==record['V_side'],
        record['predicted_H_actions']==forecast,record['V_defender_profile_calls']==0,
        vt['phase']==('factory_opening' if rnd<=3 else 'wall_opening' if rnd==4 else 'heavy_opening'),
        vt['defender_called'] is False,vt['defender_calls']==0,vt['defender_last_round'] is None,
        vt['rejected_proposals']==[],vt['proposed_actions']==vt['submitted_actions'],
        record['nested_successful']==dict(internal_G=min(rnd,3),internal_L4=rnd,
            internal_H_model=rnd,reference_H_model=rnd,V_defender=0)]
    if rnd<=2:
        checks.append(trace['proposed_actions']['G']==trace['proposed_actions']['L4'])
    if rnd==3:
        checks.append(trace['discarded_proposals']=={'L4':[F]*8})
    if rnd>=4:
        checks.extend([trace['discarded_proposals']=={},
            record['L4_timing_trace']==dict(round=rnd,predicted_actions=forecast,attack_count=6 if rnd==4 else 0,
                attack_tier='tier2',forecast_attack_gain=72 if rnd==4 else 0,forecast_residual_damage=0),
            record['L4_repair_trace']==dict(round=rnd,original_predicted_damage=0,
                replacement_predicted_damage=None,selected=False,proposed_construction=[],proposed_actions_legal=None)])
        g=record['forecast_geometry']; W=[dict(type='wall',x=x,y=y) for x,y in witness['walls']]
        checks.append({k:v for k,v in g.items() if k!='path'}==dict(all_actions_accepted=True,
            gold=11 if rnd==4 else 18,n_factories=28 if rnd==4 else 49,
            buildings=[dict(type='splash',x=10,y=1)] if rnd==4 else W+[dict(type='splash',x=1,y=3)],
            active_roster=[],length_path=22 if rnd==4 else 42))
        checks.append(g['path']==expected_forecast_route(rnd))
    return all(checks)


def mechanism():
    begin=time.perf_counter(); inputs={}; declaration=verify_declaration(inputs)
    freeze=checked_read(ROOT/'freeze.json',inputs)
    for p,h in declaration['input_sha256'].items():
        require(freeze['source_sha256'].get(p)==h,'Mechanism freeze omitted active pin.')
    verify_archive(ROOT,freeze,inputs,compare_current=True)
    from bot_research.bots.counters.fourth_round_wall import FourthRoundWall
    from bot_research.bots.counters.third_round_wait import ThirdRoundWait
    from bot_research.bots.counters.blind_fourth_round import BlindFourthRound
    from bot_research.bots.counters.early_wall_guard import EarlyWallGuard
    from bot_research.bots.counters.wall_signal_repair import WallSignalRepair
    from bot_research.bots.defense.frozen.v38.fortress import make as make_defender
    from bot_research.bots.counters.visible_search import player_from_snapshot
    from bot_research.experiments.validation.policy_value_snapshot import freeze_state
    from bot_research.experiments.validation.replay_audit import normalized
    from td_game.actions import apply_action
    from td_game.config import balanced_config
    from td_game.engine import Engine
    witness=next(w for w in read(DATA[0])['witnesses'] if w['id']=='guard00')
    outdir=R/(NAME+'-mechanism');outdir.mkdir(exist_ok=False)
    journal_path=outdir/'calls.jsonl';checkpoints=[];cases=[]
    with journal_path.open('x') as journal:
        journal_event(journal,event='audit_started',declaration=str(D),declared_cases=4,round_limit=5)
        for index in range(4):
            _,opponent,side=GRID[index]
            detail=dict(index=index,opponent=opponent,side=side,result=str(ROOT/'results'/f'case{index:04d}.json'),
                completed=False,passed=False,rounds=[],errors=[],attempted={k:0 for k in COUNTER_KEYS},
                successful={k:0 for k in COUNTER_KEYS},nested_successful={k:0 for k in NESTED_KEYS},
                nested_attempt_counts_complete=True,constructors_completed=False)
            cases.append(detail);v=selector=refs=None;stage='load_case';profile_calls=0
            try:
                case,_=inspect_new_case(index,declaration,inputs,witness)
                require(case['audit_passed'],'Case source/replay invalid: '+repr(case['errors']))
                row=checked_read(detail['result'],inputs)
                records=[json.loads(s) for s in safe_path(case['replay']).read_text().splitlines()]
                detail.update(condition=row['condition'],expected_rounds=min(5,row['rounds']),replay=case['replay'])
                cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']))
                require(normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2],'Initial records differ.')
                stage='construct';journal_event(journal,event='construct_started',case=index)
                v=FourthRoundWall();selector=(ThirdRoundWait if opponent=='T' else BlindFourthRound)()
                refs={'G':EarlyWallGuard(witness='guard00'),'L4':WallSignalRepair()};refs['L4'].attack_round=4
                cold_reference=make_defender();cold_state=freeze_state(v.defender)
                require(cold_state==freeze_state(cold_reference),'Literal default defender initial closure differs.')
                require(all(freeze_state(vars(getattr(selector,'g' if k=='G' else 'l4')))==freeze_state(vars(refs[k])) for k in refs),
                        'Initial member states differ.')
                detail.update(constructors_completed=True,cold_defender_initial_sha256=state_digest(cold_state))
                journal_event(journal,event='construct_completed',case=index,V=1,selector=1,reference_G=1,reference_L4=1,
                              V_default_defender=1,additional_cold_default_defender=1)
                def invoke(label,policy,saved,rnd):
                    nonlocal stage,profile_calls
                    stage=label;detail['attempted'][label]+=1;ordinal=detail['attempted'][label]
                    journal_event(journal,event='call_started',case=index,round=rnd,label=label,ordinal=ordinal)
                    arg=deepcopy(saved);start=time.perf_counter();previous=sys.getprofile()
                    def profile(frame,event,arg):
                        nonlocal profile_calls
                        if event=='call' and frame.f_code is v.defender.__code__: profile_calls+=1
                    try:
                        if label=='actual_V':
                            require(previous is None,'Unexpected pre-existing profiler.');sys.setprofile(profile)
                        proposal=policy.decide(arg)
                    except Exception as error:
                        journal_event(journal,event='call_failed',case=index,round=rnd,label=label,ordinal=ordinal,
                            seconds=time.perf_counter()-start,diagnostic=public_diagnostic(str(error)))
                        raise
                    finally:
                        if label=='actual_V':sys.setprofile(previous)
                    detail['successful'][label]+=1
                    journal_event(journal,event='call_completed',case=index,round=rnd,label=label,ordinal=ordinal,
                        actions=proposal,observation_unchanged=arg==saved,seconds=time.perf_counter()-start)
                    return proposal,arg==saved
                for rnd in range(1,detail['expected_rounds']+1):
                    vobs=engine.observation(side);sobs=engine.observation(1-side)
                    vbefore=deepcopy(vobs);saved=deepcopy(sobs);enemy=saved['players'][side]
                    normalized_names=deepcopy(saved)
                    for physical,p in enumerate(normalized_names['players']):p['name']='V' if physical==side else 'selector'
                    called=['G','L4'] if rnd<=3 else ['L4'];returned='G' if rnd<=3 else 'L4'
                    members={'G':selector.g,'L4':selector.l4}
                    before={k:freeze_state(vars(x)) for k,x in members.items()}
                    lens={k:len(x.trace) for k,x in members.items()};repair_len=len(selector.l4.repair_trace)
                    vp,vi=invoke('actual_V',v,vobs,rnd)
                    sp,si=invoke('actual_selector',selector,saved,rnd)
                    reference={};ri=True
                    for k in called:
                        reference[k],immutable=invoke('reference_'+k,refs[k],normalized_names,rnd);ri=ri and immutable
                    stage='compare';pair=records[2*rnd:2*rnd+2];actual=[actions(r) for r in pair]
                    selected=None if rnd<=3 else 'L4'
                    expected_trace=dict(round=rnd,player=1-side,selected_before=None if rnd<=4 else 'L4',selected=selected,
                        selection_round=None if rnd<=3 else 4,opponent_buildings=len(enemy['buildings']),
                        opponent_roster=len(enemy['roster']),presence=bool(enemy['buildings'] or enemy['roster']),
                        member_calls=called,returned_member=returned,proposed_actions=reference,
                        discarded_proposals={k:x for k,x in reference.items() if k!=returned},submitted_actions=reference[returned])
                    checks=dict(observations_unchanged=vi and si and ri and vobs==vbefore and sobs==saved,
                        selector_snapshots_independent=independent_snapshots(sp,selector.trace[-1]),
                        V_snapshots_independent=all(not(mutable_container_ids(x)&mutable_container_ids(y))
                            for x,y in ((vp,v.trace[-1]['submitted_actions']),(vp,v.trace[-1]['proposed_actions']),
                                        (v.trace[-1]['submitted_actions'],v.trace[-1]['proposed_actions']))),
                        actual_actions_exact=vp==actual[side] and sp==actual[1-side],
                        selected_reference_actions_exact=sp==reference[returned],
                        selector_trace=selector.trace[-1]==expected_trace and len(selector.trace)==rnd,
                        wrapper_bookkeeping=v.last_round==selector.last_round==rnd and v.player==side and selector.player==1-side
                            and selector.selected==selected and selector.selection_round==(None if rnd<=3 else 4),
                        V_trace=len(v.trace)==rnd and v.trace[-1]['round']==rnd and v.trace[-1]['player']==side
                            and v.trace[-1]['submitted_actions']==vp and not v.filtered_proposals,
                        cold_defender=freeze_state(v.defender)==cold_state==freeze_state(cold_reference)
                            and v.defender_calls==profile_calls==0 and v.defender_last_round is None,
                        reference_states=all(freeze_state(vars(members[k]))==freeze_state(vars(refs[k])) for k in members),
                        inactive_unchanged=all(freeze_state(vars(members[k]))==before[k] for k in members if k not in called),
                        trace_increments=all(len(members[k].trace)-lens[k]==int(k in called) for k in members),
                        repair_increment=len(selector.l4.repair_trace)==repair_len+1,
                        model_round_player=selector.l4.model.last_round==rnd and selector.l4.model.player==side,
                        model_state=freeze_state(vars(selector.l4.model))==freeze_state(vars(refs['L4'].model)))
                    checks['proposals_legal']=True
                    for physical,proposal in [(side,vp),(1-side,sp)]+[(1-side,a) for a in reference.values()]:
                        own=player_from_snapshot(saved['players'][physical])
                        checks['proposals_legal'] &= all(apply_action(own,a,rnd,cfg)['accepted'] for a in proposal)
                    checks['engine_replay']=normalized(engine.play_round(actual))==pair
                    detail['nested_successful']=dict(internal_G=len(selector.g.trace),internal_L4=len(selector.l4.trace),
                        internal_H_model=selector.l4.model.last_round,reference_H_model=refs['L4'].model.last_round,V_defender=profile_calls)
                    forecast=deepcopy(selector.l4.trace[-1]['predicted_actions'])
                    rd=dict(round=rnd,V_side=side,checks=checks,passed=all(checks.values()),V_trace=deepcopy(v.trace[-1]),
                        selector_trace=deepcopy(selector.trace[-1]),reference_proposals=deepcopy(reference),
                        V_defender_profile_calls=profile_calls,cold_defender_state_sha256=state_digest(freeze_state(v.defender)),
                        component_state_sha256={k:state_digest(freeze_state(vars(x))) for k,x in members.items()},
                        reference_state_sha256={k:state_digest(freeze_state(vars(x))) for k,x in refs.items()},
                        model_last_round=selector.l4.model.last_round,model_player=selector.l4.model.player,
                        predicted_H_actions=forecast,actual_V_actions=actual[side],forecast_input_snapshot=deepcopy(enemy),
                        forecast_geometry=forecast_geometry(saved,forecast,cfg) if rnd>=4 else None,
                        L4_timing_trace=deepcopy(selector.l4.trace[-1]),L4_repair_trace=deepcopy(selector.l4.repair_trace[-1]),
                        forecast_equals_actual_V=forecast==actual[side],successful=deepcopy(detail['successful']),
                        nested_successful=deepcopy(detail['nested_successful']))
                    rd['private_claim']=private_claim(rd,witness)
                    detail['rounds'].append(rd);checkpoint=outdir/f'case{index:04d}-round{rnd:04d}.json'
                    atomic_json(checkpoint,rd,exclusive=True);checkpoints.append(str(checkpoint))
                    journal_event(journal,event='round_completed',case=index,round=rnd,checkpoint=str(checkpoint),passed=rd['passed'])
                detail.update(completed=True,passed=all(r['passed'] for r in detail['rounds']),
                    reached_five=row['rounds']>=5,private_claim=all(r['private_claim'] for r in detail['rounds']) and row['rounds']>=5)
            except Exception as error:
                detail['errors'].append(dict(stage=stage,diagnostic=public_diagnostic(str(error))))
                if selector is not None:
                    detail['nested_successful'].update(internal_G=len(selector.g.trace),internal_L4=len(selector.l4.trace),
                        internal_H_model=selector.l4.model.last_round,V_defender=profile_calls)
                if refs is not None:detail['nested_successful']['reference_H_model']=refs['L4'].model.last_round
                detail['nested_attempt_counts_complete']=False
                journal_event(journal,event='case_failed',case=index,stage=stage,errors=detail['errors'],
                    attempted=detail['attempted'],successful=detail['successful'],nested_successful_lower_bounds=detail['nested_successful'])
            cp=outdir/f'case{index:04d}.json';atomic_json(cp,detail,exclusive=True);checkpoints.append(str(cp))
            journal_event(journal,event='case_finished',case=index,receipt=str(cp),completed=detail['completed'])
        journal_event(journal,event='audit_finished',cases=len(cases))
    for p in [str(journal_path)]+checkpoints:pin(p,inputs)
    drift=finish_hashes(inputs)
    result=dict(time_utc=now(),elapsed_seconds=time.perf_counter()-begin,games=4,round_limit=5,cases=cases,
        audit_completed=all(c['completed'] for c in cases) and not drift,
        all_passed=all(c['passed'] for c in cases) and not drift,journal=str(journal_path),checkpoints=checkpoints,
        attempted={k:sum(c['attempted'][k] for c in cases) for k in COUNTER_KEYS},
        successful={k:sum(c['successful'][k] for c in cases) for k in COUNTER_KEYS},
        nested_successful={k:sum(c['nested_successful'][k] for c in cases) for k in NESTED_KEYS},
        constructors_completed=sum(c['constructors_completed'] for c in cases),
        nested_attempt_counts_complete=all(c['nested_attempt_counts_complete'] for c in cases),
        integrity_errors=drift,input_sha256=inputs,
        scope='Additional first-five V/T,U calls and independent G/L4 references on actual observations. '
            'Reference snapshot names normalized; no fabricated private histories. Nested calls are subsets. '
            'Cold default F38 constructed twice per case, original and uncalled reference; profiler checks zero original calls. '
            'Later private F38 transitions are not independently compared. Globals, clocks and alias identity are outside freeze_state.')
    atomic_json(R/(NAME+'-mechanism.json'),result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','audit_completed','all_passed','successful','nested_successful')}),flush=True)
    return 0 if result['all_passed'] else 2

def inspect_mechanism(declaration, inputs, witness):
    result=dict(authenticated=False,passed=False,errors=[],cases=[],successful={},attempted={},nested_successful={})
    try:
        receipt=checked_read(R/(NAME+'-mechanism.json'),inputs)
        for p,h in receipt['input_sha256'].items():pin(p,inputs,h)
        require(receipt['input_sha256'].get(str(D))==sha(D),'Mechanism declaration absent.')
        for p,h in declaration['input_sha256'].items():
            require(receipt['input_sha256'].get(p)==h,'Mechanism active input absent.')
        require(receipt['games']==4 and receipt['round_limit']==5 and len(receipt['cases'])==4,'Mechanism case count differs.')
        journal=R/(NAME+'-mechanism')/'calls.jsonl'
        require(receipt['journal']==str(journal) and str(journal) in receipt['input_sha256'],'Journal edge missing.')
        events=[json.loads(s) for s in journal.read_text().splitlines()]
        require(events[0]['event']=='audit_started' and events[-1]['event']=='audit_finished','Audit stream incomplete.')
        for e in events:
            if e['event'] in ('call_started','call_completed','call_failed'):
                require(type(e.get('case')) is int and 0<=e['case']<4 and e.get('label') in COUNTER_KEYS
                    and type(e.get('round')) is int and 1<=e['round']<=5,'Undeclared audit call.')
        expected_checkpoints=set()
        for index,c in enumerate(receipt['cases']):
            _,opponent,side=GRID[index];row=checked_read(ROOT/'results'/f'case{index:04d}.json',inputs)
            validate_condition(row['condition'],'V',opponent,side,declaration['policies'])
            require(c['index']==index and c['opponent']==opponent and c['side']==side
                and c['result']==str(ROOT/'results'/f'case{index:04d}.json'),'Mechanism case identity differs.')
            cp=R/(NAME+'-mechanism')/f'case{index:04d}.json'
            require(str(cp) in receipt['input_sha256'] and checked_read(cp,inputs)==c,'Case checkpoint differs.')
            expected_checkpoints.add(str(cp))
            records=[json.loads(s) for s in safe_path(row['replay_path']).read_text().splitlines()]
            require(receipt['input_sha256'].get(row['replay_path'])==sha(row['replay_path']),'Mechanism replay edge absent.')
            ce=[e for e in events if e.get('case')==index]
            for label in COUNTER_KEYS:
                starts=[e for e in ce if e['event']=='call_started' and e['label']==label]
                completed=[e for e in ce if e['event']=='call_completed' and e['label']==label]
                failed=[e for e in ce if e['event']=='call_failed' and e['label']==label]
                require(c['attempted'][label]==len(starts) and c['successful'][label]==len(completed),'Journal count differs.')
                require([e['ordinal'] for e in starts]==list(range(1,len(starts)+1)),'Journal ordinal differs.')
                require(sorted((e['ordinal'],e['round']) for e in starts)==
                    sorted((e['ordinal'],e['round']) for e in completed+failed),'Call termination absent or duplicated.')
            for rnd,rd in enumerate(c['rounds'],1):
                require(rd['round']==rnd<=min(5,row['rounds']) and rd['V_side']==side,'Mechanism round differs.')
                cp=R/(NAME+'-mechanism')/f'case{index:04d}-round{rnd:04d}.json'
                require(str(cp) in receipt['input_sha256'] and checked_read(cp,inputs)==rd,'Round checkpoint differs.')
                expected_checkpoints.add(str(cp))
                called=['G','L4'] if rnd<=3 else ['L4']
                completed=[e for e in ce if e['event']=='call_completed' and e['round']==rnd]
                require([e['label'] for e in completed]==['actual_V','actual_selector']+['reference_'+k for k in called],
                    'Ordered extra call schedule differs.')
                require(completed[0]['actions']==rd['V_trace']['submitted_actions']
                    and completed[1]['actions']==rd['selector_trace']['submitted_actions']
                    and {e['label'].removeprefix('reference_'):e['actions'] for e in completed[2:]}==rd['reference_proposals'],
                    'Journal proposal binding differs.')
                # Receipt flags are not substitutes for retained list/input bindings.
                require(rd['actual_V_actions']==actions(records[2*rnd+side])
                    and rd['forecast_input_snapshot']==records[2*(rnd-1)+side]['snapshot'],'Actual history binding differs.')
                require(rd['successful']==dict(actual_V=rnd,actual_selector=rnd,reference_G=min(rnd,3),reference_L4=rnd),
                    'Cumulative extra call count differs.')
                require(rd['passed']==all(rd['checks'].values()) and rd['private_claim']==private_claim(rd,witness),
                    'Mechanism predicate result differs.')
                require(rd['component_state_sha256']==rd['reference_state_sha256'] or not rd['checks']['reference_states'],
                    'State digest/equality flags disagree.')
                require(rd['cold_defender_state_sha256']==c['cold_defender_initial_sha256'] or not rd['checks']['cold_defender'],
                    'Cold closure digest flag disagrees.')
            if c['completed']:
                n=min(5,row['rounds'])
                require(c['expected_rounds']==n and len(c['rounds'])==n and c['constructors_completed'],
                    'Completed mechanism truncated.')
                require(c['successful']==c['attempted']==dict(actual_V=n,actual_selector=n,reference_G=min(n,3),reference_L4=n),
                    'Final external count differs.')
                require(c['nested_successful']==dict(internal_G=min(n,3),internal_L4=n,internal_H_model=n,
                    reference_H_model=n,V_defender=0),'Final nested count differs.')
                require(c['passed']==all(r['passed'] for r in c['rounds']) and
                    c['private_claim']==(row['rounds']>=5 and all(private_claim(r,witness) for r in c['rounds'])),
                    'Case predicate result differs.')
        require(set(receipt['checkpoints'])==expected_checkpoints and len(receipt['checkpoints'])==len(expected_checkpoints),
            'Checkpoint set differs.')
        for field,keys in (('attempted',COUNTER_KEYS),('successful',COUNTER_KEYS),('nested_successful',NESTED_KEYS)):
            require(receipt[field]=={k:sum(c[field][k] for c in receipt['cases']) for k in keys},'Aggregate calls differ.')
        require(receipt['all_passed']==(all(c['passed'] for c in receipt['cases']) and not receipt['integrity_errors'])
            and receipt['audit_completed']==(all(c['completed'] for c in receipt['cases']) and not receipt['integrity_errors']),
            'Aggregate success differs.')
        result.update(authenticated=True,passed=receipt['audit_completed'] and receipt['all_passed'],
            cases=receipt['cases'],attempted=receipt['attempted'],successful=receipt['successful'],
            nested_successful=receipt['nested_successful'],constructors_completed=receipt['constructors_completed'],
            receipt=str(R/(NAME+'-mechanism.json')))
    except Exception as error:
        result['errors'].append(public_diagnostic(str(error)))
        partial=R/(NAME+'-mechanism')
        if partial.exists():result['partial_artifacts']=[str(p) for p in sorted(partial.iterdir()) if p.is_file()]
    return result


def opening_fixture(witness,side):
    """Synthetic expected receipts only, never a game or strength observation."""
    F=dict(op='buy_factory');walls=[dict(type='wall',x=x,y=y) for x,y in witness['walls']]
    build=[dict(op='build_wall',x=x,y=y) for x,y in witness['walls']];X=dict(type='splash',x=1,y=3)
    va=[[F]*5,[F]*4,[F]*8,build+[dict(op='build_turret',**X)]+[F]*10,[dict(op='buy_minion',type='tier4')]+[F]*9]
    sa=[build+[F]*4,[F]*5,[dict(op='build_turret',**X)]+[F]*5,[dict(op='buy_minion',type='tier2')]*6+[F],[F]*13]
    vals=[[(97,5,22,800),(174,9,22,800),(291,17,22,800),(458,27,42,800),(605,36,42,800)],
          [(100,4,40,800),(175,9,40,800),(267,14,42,800),(274,15,42,800),(476,28,42,740)]]
    records=[{},{}]
    for rnd in range(1,6):
        pair=[None,None]
        for role,physical in enumerate((side,1-side)):
            gold,n,length,hp=vals[role][rnd-1]
            buildings=([] if rnd<4 else walls+[X]) if role==0 else walls+([] if rnd<3 else [X])
            roster=[]
            if role==0 and rnd==5:roster=[dict(id=0,type='tier4',bought_round=5,expires_after_round=16,remaining_rounds=11)]
            if role==1 and rnd>=4:roster=[dict(id=i,type='tier2',bought_round=4,expires_after_round=15,remaining_rounds=15-rnd) for i in range(6)]
            hits=int(role==0 and rnd==5);incoming=int(role==1 and rnd==5)
            snapshot=dict(name='synthetic',gold=gold,n_factories=n,length_path=length,hp=hp,buildings=deepcopy(buildings),
                roster=roster,n_walls=len([b for b in buildings if b['type']=='wall']),n_turrets=len([b for b in buildings if b['type']!='wall']))
            events=[dict(kind='action',action=deepcopy(a),accepted=True) for a in (va if role==0 else sa)[rnd-1]]
            events.extend([dict(kind='combat',outgoing_hits=hits,incoming_hits=incoming,damage_dealt=60*hits,base_damage=60*incoming,
                spawned=int(rnd==5) if role==0 else (6 if rnd>=4 else 0),killed=6 if role==1 and rnd>=4 else 0,cleared=0),
                dict(kind='income',path=length,factories=15*n,hits=5*hits,total=length+15*n+5*hits)])
            pair[physical]=dict(snapshot=snapshot,event=events)
        records+=pair
    return records


def private_fixture(witness,rnd):
    F=dict(op='buy_factory');forecast=[dict(op='build_turret',type='splash',x=10,y=1)]+[F]*11 if rnd==4 else [F]*22
    walls=[dict(type='wall',x=x,y=y) for x,y in witness['walls']]
    return dict(round=rnd,V_side=0,passed=True,model_last_round=rnd,model_player=0,predicted_H_actions=forecast,
        V_defender_profile_calls=0,V_trace=dict(phase='wall_opening' if rnd==4 else 'heavy_opening',defender_called=False,
            defender_calls=0,defender_last_round=None,rejected_proposals=[],proposed_actions=[],submitted_actions=[]),
        selector_trace=dict(member_calls=['L4'],selected='L4',selection_round=4,returned_member='L4',discarded_proposals={}),
        nested_successful=dict(internal_G=3,internal_L4=rnd,internal_H_model=rnd,reference_H_model=rnd,V_defender=0),
        L4_timing_trace=dict(round=rnd,predicted_actions=forecast,attack_count=6 if rnd==4 else 0,attack_tier='tier2',
            forecast_attack_gain=72 if rnd==4 else 0,forecast_residual_damage=0),
        L4_repair_trace=dict(round=rnd,original_predicted_damage=0,replacement_predicted_damage=None,selected=False,
            proposed_construction=[],proposed_actions_legal=None),
        forecast_geometry=dict(all_actions_accepted=True,gold=11 if rnd==4 else 18,n_factories=28 if rnd==4 else 49,
            buildings=[dict(type='splash',x=10,y=1)] if rnd==4 else walls+[dict(type='splash',x=1,y=3)],
            active_roster=[],length_path=22 if rnd==4 else 42,path=expected_forecast_route(rnd)))


def predicate_selftests(witness):
    tests={}
    for side in (0,1):
        fixture=opening_fixture(witness,side)
        tests['positive_opening_side'+str(side)]=opening_check(fixture,'T',side,5,witness)['passed']
        mutations={'gold':lambda r:r[10+side]['snapshot'].__setitem__('gold',606),
            'roster_expiry':lambda r:r[8+1-side]['snapshot']['roster'][0].__setitem__('expires_after_round',16),
            'killed':lambda r:r[8+1-side]['event'][-2].__setitem__('killed',5),
            'income':lambda r:r[10+side]['event'][-1].__setitem__('hits',0),
            'action':lambda r:r[6+side]['event'][0]['action'].__setitem__('op','bad_action'),
            'rejection':lambda r:r[2+side]['event'][0].__setitem__('accepted',False)}
        for name,mutate in mutations.items():
            changed=deepcopy(fixture);mutate(changed)
            tests[name+'_rejected_side'+str(side)]=not opening_check(changed,'T',side,5,witness)['passed']
        tests['early_terminal_rejected_side'+str(side)]=not opening_check(fixture,'T',side,4,witness)['passed']
        tests['wrong_physical_role_rejected_side'+str(side)]=not opening_check(fixture,'T',1-side,5,witness)['passed']
    for rnd in (4,5):
        fixture=private_fixture(witness,rnd);tests['positive_private'+str(rnd)]=private_claim(fixture,witness)
        mutations={'model_round':lambda r:r.__setitem__('model_last_round',1),
            'hidden_defender_call':lambda r:r.__setitem__('V_defender_profile_calls',1),
            'wrong_selected':lambda r:r['selector_trace'].__setitem__('selected','G'),
            'forecast_factory':lambda r:r['forecast_geometry'].__setitem__('n_factories',999),
            'forecast_path':lambda r:r['forecast_geometry']['path'].__setitem__(1,[0,1]),
            'forecast_action':lambda r:r['predicted_H_actions'].append(dict(op='buy_factory')),
            'repair':lambda r:r['L4_repair_trace'].__setitem__('selected',True),
            'filtered_action':lambda r:r['V_trace']['rejected_proposals'].append(dict(action='bad'))}
        for name,mutate in mutations.items():
            changed=deepcopy(fixture);mutate(changed);tests[name+'_rejected_round'+str(rnd)]=not private_claim(changed,witness)
    return tests


def selftest():
    inputs={};verify_declaration(inputs)
    witness=next(w for w in read(DATA[0])['witnesses'] if w['id']=='guard00')
    tests=predicate_selftests(witness);drift=finish_hashes(inputs)
    result=dict(time_utc=now(),tests=tests,count=len(tests),all_passed=all(tests.values()) and not drift,
        policy_calls=0,engine_calls=0,synthetic_receipts=True,integrity_errors=drift,input_sha256=inputs)
    atomic_json(R/(NAME+'-selftest.json'),result,exclusive=True)
    print(json.dumps(dict(selftest=result['all_passed'],count=len(tests))),flush=True)
    return 0 if result['all_passed'] else 2


def inspect_selftest(declaration,inputs,witness):
    result=dict(passed=False,errors=[])
    try:
        receipt=checked_read(R/(NAME+'-selftest.json'),inputs)
        for p,h in receipt['input_sha256'].items():pin(p,inputs,h)
        for p,h in declaration['input_sha256'].items():require(receipt['input_sha256'].get(p)==h,'Selftest source edge absent.')
        require(receipt['input_sha256'].get(str(D))==sha(D),'Selftest declaration absent.')
        expected=predicate_selftests(witness)
        require(receipt['tests']==expected and receipt['count']==len(expected) and receipt['policy_calls']==receipt['engine_calls']==0,
            'Selftest fixture identities/results differ.')
        require(receipt['all_passed'] and all(expected.values()) and not receipt['integrity_errors'],'Discriminative fixtures failed.')
        result.update(passed=True,count=len(expected),tests=expected)
    except Exception as error:result['errors'].append(public_diagnostic(str(error)))
    return result


def comparison(first,second,usable):
    equal=first==second if usable else None;divergence=None
    if equal is False:
        i=next((j for j in range(min(len(first),len(second))) if first[j]!=second[j]),min(len(first),len(second)))
        divergence=dict(record_index=i,first=first[i] if i<len(first) else None,second=second[i] if i<len(second) else None)
    return equal,divergence


def check():
    begin=time.perf_counter();inputs={};declaration=verify_declaration(inputs)
    (A/'verification').mkdir(exist_ok=True)
    witness=next(w for w in read(DATA[0])['witnesses'] if w['id']=='guard00')
    campaign=audit_campaign(declaration,inputs);mechanism_audit=inspect_mechanism(declaration,inputs,witness)
    selftests=inspect_selftest(declaration,inputs,witness)
    members={(c['opponent'],c['side']):c for c in mechanism_audit['cases']}
    cases=[];histories={}
    for index,(_,opponent,side) in enumerate(GRID):
        case,history=inspect_new_case(index,declaration,inputs,witness)
        case['verified']=case['audit_passed'] and campaign['passed'];case['campaign_audits_passed']=campaign['passed']
        member=members.get((opponent,side)) if mechanism_audit['authenticated'] else None
        if opponent in ('T','U'):
            if case['verified'] and not case['opening']['passed']:h1=False
            elif case['verified'] and member and member['completed'] and selftests['passed']:h1=member['private_claim'] and member['passed']
            else:h1=None
            case['H1_condition']=h1
            case['H2_condition']=case['outcome']=='W' if case['verified'] else None
        else:case['H1_condition']=case['H2_condition']=None
        cases.append(case);histories[opponent,side]=history
    by={(c['opponent'],c['side']):c for c in cases};transfers=[];pairs=[]
    for side in (0,1):
        usable=by['T',side]['verified'] and by['U',side]['verified']
        equal,divergence=comparison(histories['T',side],histories['U',side],usable)
        transfers.append(dict(V_side=side,T_result=by['T',side]['result'],U_result=by['U',side]['result'],
            verified=usable,same_complete_history=equal,first_divergence=divergence))
    for opponent in ORDER:
        a,b=by[opponent,0],by[opponent,1];usable=a['verified'] and b['verified']
        equal,divergence=comparison(histories[opponent,0],histories[opponent,1],usable)
        pairs.append(dict(opponent=opponent,verified=usable,same_complete_history=equal,
            same_outcome=a.get('outcome')==b.get('outcome') if usable else None,first_divergence=divergence))
    verdicts=dict(H1=aggregate_verdict([c['H1_condition'] for c in cases if c['opponent'] in ('T','U')]),
        H2=aggregate_verdict([c['H2_condition'] for c in cases if c['opponent'] in ('T','U')]),
        H3=aggregate_verdict([t['same_complete_history'] for t in transfers]))
    drift=finish_hashes(inputs)
    if drift:verdicts={k:'OPEN' for k in verdicts}
    completed=all(c['verified'] for c in cases) and mechanism_audit['passed'] and selftests['passed'] and not drift
    expected_fresh=2*sum(c.get('rounds',0) for c in cases)
    if campaign['passed']:require(campaign['checked_calls']==expected_fresh,'Fresh total differs from all ten histories.')
    result=dict(time_utc=now(),elapsed_seconds=time.perf_counter()-begin,audit_completed=completed,
        all_passed=completed and all(v=='CONFIRMED' for v in verdicts.values()),hypotheses=verdicts,
        new_games_declared=10,retained_games_declared=0,total_cases=10,verified_new_cases=sum(c['verified'] for c in cases),
        cases=cases,transfers=transfers,pairs=pairs,campaign_audit=campaign,mechanism_audit=mechanism_audit,selftests=selftests,
        original_new_game_external_calls_verified=sum(2*c['rounds'] for c in cases if c['verified']),
        ordinary_fresh_external_calls_verified=campaign['checked_calls'],ordinary_fresh_external_calls_expected=expected_fresh,
        additional_audit_successful_calls=mechanism_audit.get('successful',{}),
        additional_audit_attempted_calls=mechanism_audit.get('attempted',{}),
        nested_successful_calls=mechanism_audit.get('nested_successful',{}),final_checker_policy_calls=0,
        complete_engine_replays=sum('terminal_replay' in c for c in cases),integrity_errors=drift,input_sha256=inputs,
        scope='Ten selected standard development games. Full unchanged-engine and fresh external action audits; '
            'additional private comparison only first five of four T/U histories. Later default F38 once-per-round '
            'delegation is source checked and full returned actions reproduced, not separately measured private-state equivalence. '
            'H3 is finite clock-sensitive reproduction, not unconditional policy equivalence. G/B/N descriptive only. '
            'Nested member/model counts are subsets. No reserved D games or changes.',
        interrupted_fresh_limit='Inherited ordinary fresh checker retains detailed calls on successful completion; '
            'an interrupted child may retain only process output and original records. Additional mechanism calls are journaled before and after each call.')
    lines=['# Protocol163 results','', 'Completed UTC: '+result['time_utc']+'.','',
        'Audit completed: '+str(completed)+'. H1/H2/H3: '+json.dumps(verdicts,sort_keys=True)+'.','',
        'Ten selected development conditions were declared; '+str(result['verified_new_cases'])+' have all required ordinary audits.',
        '', '| Opponent | V seat | Outcome | Rounds | Verified |','| --- | ---: | --- | ---: | --- |']
    for c in cases:lines.append('| '+str(c['opponent'])+' | '+str(c['side'])+' | '+str(c.get('outcome','OPEN'))+' | '+str(c.get('rounds','OPEN'))+' | '+str(c['verified'])+' |')
    lines+=['','Ordinary fresh successful external calls: '+str(campaign['checked_calls'])+'. Additional successful calls: '+json.dumps(result['additional_audit_successful_calls'],sort_keys=True)+'.',
        'Nested successful subsets: '+json.dumps(result['nested_successful_calls'],sort_keys=True)+'.','',result['scope'],'',result['interrupted_fresh_limit'],'',
        'Missing, failed and unfavorable cases remain in verification/full_games.json. A false scientific hypothesis does not alone make audit_completed false.','']
    with (A/'RESULTS.md').open('x') as stream:stream.write('\n'.join(lines))
    result['results_sha256']=sha(A/'RESULTS.md')
    atomic_json(A/'verification/full_games.json',result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','audit_completed','hypotheses','ordinary_fresh_external_calls_verified')}),flush=True)
    return 0 if completed else 2


def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['declare','selftest','mechanism','check'])
    parser.add_argument('--review',action='append',default=[]);args=parser.parse_args()
    if args.mode=='declare':declare(args.review);return 0
    if args.mode=='selftest':return selftest()
    if args.mode=='mechanism':return mechanism()
    return check()


if __name__=='__main__':
    try:raise SystemExit(main())
    except Exception as error:
        destination=A/'verification'/'incomplete.json'
        destination.parent.mkdir(exist_ok=True)
        if not destination.exists():atomic_json(destination,dict(time_utc=now(),audit_completed=False,
            diagnostic=public_diagnostic(str(error)),policy_call_count_unknown_for_interrupted_phase=True),exclusive=True)
        print(public_diagnostic(str(error)),flush=True)
        raise SystemExit(2)

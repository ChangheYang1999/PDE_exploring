"""Cross-check exact attack certificates against unchanged combat functions."""
from __future__ import annotations
import argparse
from copy import deepcopy
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import random
import time
from td_game.actions import apply_action
from td_game.combat import combat_tick,spawn_schedule
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import Building,PlayerState,RosterEntry
from bot_research.bots.economy.frozen.v6.guarantee import bound as float_bound
from bot_research.experiments.validation.attack_certificate import certify,fraction_pair
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.source_closure import static_closure


def random_additions(player,count,rng,config):
    actions=[]
    for _ in range(count*8):
        kind=rng.choice(['wall']*4+['gun1','gun2','gun3','splash']*2)
        action={'op':'build_wall' if kind=='wall' else 'build_turret',
                'x':rng.randrange(12),'y':rng.randrange(12)}
        if kind!='wall':
            action['type']=kind
        event=apply_action(player,action,1,config)
        if event['accepted']:
            actions.append(action)
        if len(actions)>=count:
            break
    return actions


def cases(count,seed,config):
    rng=random.Random(seed)
    result=[]
    tiers=list(config.minions)
    for index in range(count):
        base=PlayerState('base',10**9,10**9)
        random_additions(base,rng.choice([0,0,1,3,5,12]),rng,config)
        gold=rng.choice([0,1,29,30,59,60,120,300,800,2000,20001])
        prefix=[rng.choice(tiers) for _ in range(rng.choice([0,1,80,200,249,250,500]))]
        kind=rng.choice(tiers)
        package=[kind if rng.random()<0.85 else rng.choice(tiers)
                 for _ in range(rng.choice([1,2,7,60,143,200,300]))]
        responses=[[]]
        for _ in range(3):
            defender=deepcopy(base)
            defender.gold=gold
            responses.append(random_additions(defender,rng.choice([1,6,30,60]),rng,config))
        result.append({'id':index,'buildings':[[b.x,b.y,b.type] for b in base.buildings],
                       'gold':gold,'prefix':prefix,'package':package,'responses':responses})
    # A small transparent fractional example precedes the seeded cases.
    result.insert(0,{'id':'single_gun_fraction','buildings':[[2,2,'gun1']],
                     'gold':0,'prefix':[],'package':['tier4'],'responses':[[]]})
    return result


def package_damage(case,response,config):
    defender=PlayerState('defender',10**9,case['gold'],
        buildings=[Building(*b) for b in case['buildings']])
    for action in response:
        event=apply_action(defender,action,1,config)
        assert event['accepted'],event
    blocked={(b.x,b.y) for b in defender.buildings}
    path=shortest_path(12,12,blocked,(0,0),(11,11))
    assert path is not None
    types=case['prefix']+case['package']
    prefix=len(case['prefix'])
    roster=[RosterEntry(i,kind,1,12) for i,kind in enumerate(types)]
    schedule=spawn_schedule(roster,1,250)
    entities=[]
    damage=0
    total=0
    for tick,spawning in enumerate(schedule):
        # Arrivals are resolved before attacks in the unchanged combat_tick.
        arriving=[e for e in entities if e.born_tick<tick and e.path_index+1==len(path)-1]
        damage+=sum(e.damage for e in arriving if e.roster_id>=prefix)
        entities,stats=combat_tick(tick,entities,spawning,path,defender,config)
        assert stats.damage==sum(e.damage for e in arriving)
        total+=stats.damage
    assert total==10**9-defender.hp
    return {'package_damage':damage,'total_damage':total,'path_length':len(path)-1}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--cases',type=int,default=100)
    parser.add_argument('--seed',type=int,default=20261031)
    parser.add_argument('--output',required=True)
    parser.add_argument('--max-seconds',type=float,default=480)
    args=parser.parse_args()
    output=Path(args.output)
    inputs=output.with_name(output.stem+'-inputs.json')
    config=balanced_config()
    rules=config.to_dict()
    declared=cases(args.cases,args.seed,config)
    atomic_json(inputs,{'seed':args.seed,'cases':declared},exclusive=True)
    source_paths=static_closure({'bot_research.experiments.validation.verify_attack_certificate'})
    frozen={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}
    started=time.perf_counter()
    results=[]
    for case in declared:
        if time.perf_counter()-started>args.max_seconds:
            break
        certificate=certify(case['buildings'],case['gold'],len(case['prefix']),case['package'],rules)
        rational=Fraction(**certificate['rational'])
        old=float_bound(case['buildings'],case['gold'],len(case['prefix']),case['package'],rules,
                        L_max=certificate['L_max'])
        tested=[package_damage(case,response,config) for response in case['responses']]
        violations=[i for i,row in enumerate(tested) if row['package_damage']<certificate['integer_lower_bound']]
        results.append({'id':case['id'],'certificate':certificate,'legacy_float':old,
                        'legacy_minus_exact':fraction_pair(Fraction.from_float(old)-rational),
                        'legacy_above_exact':Fraction.from_float(old)>rational,
                        'combat':tested,'violations':violations})
        print(json.dumps({'id':case['id'],'certificate':certificate['integer_lower_bound'],
                          'minimum_tested_package_damage':min(x['package_damage'] for x in tested),
                          'violations':violations}),flush=True)
    changed=[name for name,value in frozen.items() if hashlib.sha256(Path(name).read_bytes()).hexdigest()!=value]
    summary={'time_utc':now(),'runtime_seconds':time.perf_counter()-started,
             'declared_cases':len(declared),'completed_cases':len(results),
             'complete':len(declared)==len(results),'source_sha256':frozen,
             'source_changed_during_run':changed,
             'input':str(inputs),'input_sha256':hashlib.sha256(inputs.read_bytes()).hexdigest(),
             'tested_combat_responses':sum(len(x['combat']) for x in results),
             'violations':[x['id'] for x in results if x['violations']],
             'legacy_above_exact_cases':[x['id'] for x in results if x['legacy_above_exact']],
             'legacy_noninteger_cases':[x['id'] for x in results if not x['legacy_float'].is_integer()],
             'results':results,'scope':'Seeded finite cross-checks support the separate proof; not exhaustive construction-response enumeration.'}
    atomic_json(output,summary,exclusive=True)
    assert not summary['violations'] and not changed


if __name__=='__main__':
    main()

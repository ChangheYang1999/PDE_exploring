"""Check zero-kill covering maps and a namespace-only lead policy snapshot."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.actions import apply_action
from td_game.combat import combat_tick, spawn_schedule, simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry
from bot_research.harness import gamekit as gk
from bot_research.harness.match import resolve_spec
from bot_research.experiments.lead.v15 import _covering_turret
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.artifact_io import atomic_json


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--manifest',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    start=time.perf_counter()
    manifest=json.loads(Path(args.manifest).read_text())
    roots={'bot_research.experiments.validation.check_weak_covering_bluff', 'bot_research.experiments.lead.v23'}
    roots.update(manifest['additional_source_modules'])
    roots.update(x['spec'].partition(':')[0] for x in manifest['candidates']+manifest['opponents'])
    sources={str(p):digest(p) for p in static_closure(roots)}
    sources['td_game/balanced.json']=digest('td_game/balanced.json')
    inputs={args.manifest:digest(args.manifest),**manifest['input_sha256']}
    assert all(digest(p)==h for p,h in inputs.items())
    cfg=balanced_config()
    rules=gk.Rules.from_observation(Engine(cfg,('a','b')).observation(0))
    path0=shortest_path(12,12,set(),cfg.globals.spawn,cfg.globals.base)
    expected=[(x,0) for x in range(12)]+[(11,y) for y in range(1,12)]
    assert path0==expected
    maps=[]
    rosters=[[tier]*n for tier in cfg.minions for n in (1,2,249,250,251,500)]
    rosters.extend([[f'tier{i%5+1}' for i in range(n)] for n in (11,251,503)])
    cases=[]
    for x,y,covered in ((0,11,False),(0,2,True),(9,11,True)):
        defender=PlayerState('defender',800,100)
        assert apply_action(defender,dict(op='build_turret',type='gun1',x=x,y=y),1,cfg)['accepted']
        buildings=[dict(type='gun1',x=x,y=y)]
        path=shortest_path(12,12,{(x,y)},cfg.globals.spawn,cfg.globals.base)
        assert path==path0
        assert bool(_covering_turret(buildings,rules))==covered
        cells=[p for p in path[:-1] if (p[0]-x)**2+(p[1]-y)**2<=cfg.turrets['gun1'].range**2]
        assert len(cells)*cfg.turrets['gun1'].damage<min(t.hp for t in cfg.minions.values())
        maps.append(dict(position=[x,y],positive_coverage=covered,attackable_cells=cells,max_damage_per_copy=len(cells)*cfg.turrets['gun1'].damage))
        for kinds in rosters:
            attacker=PlayerState('attacker',800,0,roster=[RosterEntry(i,k,1,None) for i,k in enumerate(kinds)])
            schedule=spawn_schedule(attacker.roster,1,cfg.globals.ticks_per_round)
            blank=PlayerState('blank',800,0)
            d=deepcopy(defender)
            a,b=[],[]
            damage=0
            hp_difference_ticks=0
            for tick,born in enumerate(schedule):
                a,ta=combat_tick(tick,a,born,path0,blank,cfg)
                b,tb=combat_tick(tick,b,born,path,d,cfg)
                assert ta.killed==tb.killed==0
                assert ta.hits==tb.hits and ta.damage==tb.damage
                assert [(e.roster_id,e.path_index) for e in a]==[(e.roster_id,e.path_index) for e in b]
                hp_difference_ticks+=any(e.hp!=f.hp for e,f in zip(a,b))
                damage+=ta.damage
            direct=simulate_map(deepcopy(attacker),deepcopy(defender),path,1,cfg)
            assert direct.killed==0 and direct.damage==damage
            cases.append(dict(position=[x,y],count=len(kinds),tier=kinds[0] if len(set(kinds))==1 else 'mixed',damage=damage,hp_difference_ticks=hp_difference_ticks))
    prefixes=[]
    for candidate in manifest['candidates']:
        original_spec=candidate['spec'].replace('bot_research.bots.counters.snapshots.v23_candidate_001','bot_research.experiments.lead')
        for opponent in manifest['opponents']:
            for side in (0,1):
                original=resolve_spec(original_spec)
                frozen=resolve_spec(candidate['spec'])
                adversary=resolve_spec(opponent['spec'])
                engine=Engine(cfg,('a','b'))
                checked=0
                for rnd in range(1,10):
                    if engine.result is not None:break
                    obs=engine.observation(side)
                    before=deepcopy(obs)
                    action=frozen(obs)
                    assert obs==before
                    expected_action=original(deepcopy(obs))
                    assert action==expected_action, (candidate['id'],opponent['id'],side,rnd)
                    pair=[None,None]
                    pair[side]=action
                    pair[1-side]=adversary(engine.observation(1-side))
                    records=engine.play_round(pair)
                    assert all(e['accepted'] for r in records for e in r['event'] if e['kind']=='action')
                    checked+=1
                prefixes.append(dict(candidate=candidate['id'],opponent=opponent['id'],side=side,exact_rounds=checked))
                print(json.dumps(prefixes[-1]),flush=True)
    assert all(digest(p)==h for p,h in {**sources,**inputs}.items()), 'Source changed during component check.'
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        all_passed=True,source_sha256=sources,input_sha256=inputs,maps=maps,combat_cases=cases,matched_prefixes=prefixes,
        scope='Original combat on three fixed maps and declared rosters. Snapshot equality checked only on twelve actual-engine prefixes. No full-game strength claim follows.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps(dict(all_passed=True,combat_cases=len(cases),prefixes=len(prefixes),runtime_seconds=result['runtime_seconds'])),flush=True)


if __name__=='__main__':main()

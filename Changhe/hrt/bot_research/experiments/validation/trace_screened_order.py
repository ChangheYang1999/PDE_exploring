"""Observe the unchanged combat routine on three fixed roster permutations."""
from collections import Counter
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sys
from td_game.actions import apply_action
from td_game.combat import combat_tick, spawn_schedule
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure

E = Path('bot_research/experiments/validation')
A = E/'analysis/screened_order_mechanism'
O = Path('bot_research/runs/validation/screened-order-mechanism-001')
D = E/'screened-order-mechanism-001.json'
W = Path('bot_research/runs/validation/affordable-roster-coverage-001/witnesses/standard-02-side0-r6.jsonl')
ORDERS = {'screen': ['tier2','tier2','tier3'], 'middle': ['tier2','tier3','tier2'], 'front': ['tier3','tier2','tier2']}

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def now(): return datetime.now(timezone.utc).isoformat()

def declare():
    paths = set(static_closure({'bot_research.experiments.validation.trace_screened_order'})) | {W,A/'PROOF.md',Path('td_game/balanced.json')}
    pins = {str(p):sha(p) for p in sorted(paths)}
    atomic_json(D, dict(time_utc=now(), input_sha256=pins, orders=ORDERS,
        purpose='Explain three already known fixed-round outcomes. No new strength games or policy calls.'), exclusive=True)
    print(json.dumps(dict(time_utc=now(), pins=len(pins))))

def run():
    declaration=json.loads(D.read_text())
    def verify():
        assert all(sha(p)==h for p,h in declaration['input_sha256'].items())
    verify();O.mkdir(exist_ok=False)
    cfg=balanced_config();records=[json.loads(x) for x in W.read_text().splitlines()]
    names=tuple(r['snapshot']['name'] for r in records[:2]);engine=Engine(cfg,names)
    assert normalized(engine.initial_records(names))==records[:2]
    def actions(pair):return [[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
    for rnd in range(1,6):
        pair=records[2*rnd:2*rnd+2]
        assert normalized(engine.play_round(actions(pair)))==pair
    target=actions(records[12:14])[0]
    assert not [e for e in engine.players[1].roster if e.active(6)]
    evidence={str(D):sha(D)};cases=[]
    for label,order in ORDERS.items():
        attack=[dict(op='buy_minion',type=t) for t in order]
        probe=deepcopy(engine);round_records=normalized(probe.play_round([target,attack]))
        assert all(e['accepted'] for r in round_records for e in r['event'] if e['kind']=='action')
        pre=deepcopy(engine)
        for i in range(max(len(target),len(attack))):
            for side,submitted in enumerate((target,attack)):
                if i<len(submitted):assert apply_action(pre.players[side],submitted[i],6,cfg)['accepted']
        route=pre.path(0);attacker,defender=pre.players[1],pre.players[0]
        assert len(attacker.roster)==3
        types={e.id:e.type for e in attacker.roster};schedule=spawn_schedule(attacker.roster,6,250)
        entities=[];totals=Counter();traces=[];copy_totals={e.id:Counter() for e in attacker.roster}
        for tick,spawning in enumerate(schedule):
            before={e.roster_id:asdict(e) for e in entities}
            raw=entities
            entities,stats=combat_tick(tick,raw,spawning,route,defender,cfg)
            relevant=[e for e in raw if e.path_index < len(route)-1]
            assigned=Counter();gun_choices=[];splash_choices=[]
            for building in defender.buildings:
                if building.type=='wall':continue
                turret=cfg.turrets[building.type]
                inside=[]
                for e in relevant:
                    x,y=route[e.path_index];dx,dy=x-building.x,y-building.y
                    if (max(abs(dx),abs(dy))==1 if turret.aoe==8 else dx*dx+dy*dy<=turret.range**2):inside.append(e)
                if turret.aoe==8:
                    for e in inside:assigned[e.roster_id]+=turret.damage
                    splash_choices.append(dict(building=asdict(building),ids=[e.roster_id for e in inside],damage=turret.damage))
                elif inside:
                    chosen=max(inside,key=lambda e:e.path_index)
                    assigned[chosen.roster_id]+=turret.damage
                    gun_choices.append(dict(building=asdict(building),id=chosen.roster_id,damage=turret.damage))
            copies=[]
            for e in raw:
                hp_before=before[e.roster_id]['hp'] if e.roster_id in before else cfg.minions[types[e.roster_id]].hp
                arrived=e.path_index==len(route)-1
                expected=0 if arrived else assigned[e.roster_id]
                assert hp_before-e.hp==expected
                ct=copy_totals[e.roster_id];ct['damage_received']+=expected
                if arrived:ct['arrival_tick']=tick;ct['arrivals']+=1
                if not arrived and e.hp<=0:ct['death_tick']=tick;ct['deaths']+=1
                copies.append(dict(id=e.roster_id,type=types[e.roster_id],path_index=e.path_index,
                    cell=route[e.path_index],hp_before=hp_before,hp_after=e.hp,
                    damage=expected,arrived=arrived,killed=not arrived and e.hp<=0))
            for field in ('hits','damage','spawned','killed'):totals[field]+=getattr(stats,field)
            if raw:traces.append(dict(tick=tick,copies=copies,guns=gun_choices,splashes=splash_choices,totals=asdict(stats)))
        totals['cleared']=len(entities)
        event=next(e for e in round_records[1]['event'] if e['kind']=='combat')
        assert dict(totals)==dict(hits=event['outgoing_hits'],damage=event['damage_dealt'],spawned=event['spawned'],killed=event['killed'],cleared=event['cleared'])
        assert defender.hp==probe.players[0].hp
        trace=O/(label+'-ticks.json');atomic_json(trace,traces,exclusive=True);evidence[str(trace)]=sha(trace)
        replay=O/(label+'-round.jsonl')
        with replay.open('x') as stream:
            for r in records[:12]+round_records:stream.write(json.dumps(r,sort_keys=True)+'\n')
        evidence[str(replay)]=sha(replay)
        cases.append(dict(order_label=label,order=order,attack_cost=sum(cfg.minions[t].cost for t in order),
            route=route,buildings=[asdict(b) for b in pre.players[0].buildings],
            totals=dict(totals),target_hp=defender.hp,copies=[dict(id=k,type=types[k],**v) for k,v in copy_totals.items()],
            trace=str(trace),replay=str(replay)))
    assert all(c['route']==cases[0]['route'] and c['buildings']==cases[0]['buildings'] and c['attack_cost']==180 for c in cases)
    assert [c['totals']['damage'] for c in cases]==[26,0,0]
    verify();assert all(sha(p)==h for p,h in evidence.items())
    result=dict(time_utc=now(),all_checks_passed=True,cases=cases,source_sha256=declaration['input_sha256'],evidence_sha256=evidence,policy_calls=0,new_strength_games=0,original_component_ticks=750)
    atomic_json(A/'verification/full_check.json',result,exclusive=True)
    print(json.dumps(dict(time_utc=now(),cases=[{k:c[k] for k in ('order_label','totals','copies')} for c in cases])))

if __name__=='__main__': {'declare':declare,'run':run}[sys.argv[1]]()

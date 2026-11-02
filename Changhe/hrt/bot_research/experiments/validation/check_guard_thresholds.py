"""Exact pure-splash arrival formula versus original combat on the selected guards."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
import argparse, hashlib, json, time
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    start=time.perf_counter()
    wall_data=Path('bot_research/bots/counters/data/maze_layouts_001.json')
    guard_data=Path('bot_research/bots/counters/data/maze_guards_001.json')
    paths=set(static_closure({'bot_research.experiments.validation.check_guard_thresholds'}))|{wall_data,guard_data,Path('td_game/balanced.json'),Path('configs/balanced.json')}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    hashes={str(p):digest(p) for p in paths}
    walls={r['id']:r['walls'] for r in json.loads(wall_data.read_text())['layouts']}
    cfg=balanced_config();cases=[]
    for row in json.loads(guard_data.read_text())['layouts']:
        buildings=[Building(x,y,'wall') for x,y in walls[row['layout']]]
        x,y=row['selected']['cell'];buildings.append(Building(x,y,'splash'))
        path=shortest_path(cfg.globals.width,cfg.globals.height,[(b.x,b.y) for b in buildings],cfg.globals.spawn,cfg.globals.base)
        assert path==[tuple(c) for c in row['selected']['path']]
        exposure=cfg.turrets['splash'].damage*sum(max(abs(a-x),abs(b-y))==1 for a,b in path[:-1])
        assert exposure==row['selected']['splash_exposure']
        target=PlayerState('guard',800,0,buildings=buildings)
        for kind in cfg.minions:
            for n in (1,6,249,250,251,500):
                attacker=PlayerState('component attacker',800,0,roster=[RosterEntry(i,kind,1,None) for i in range(n)])
                expected=sum(i%cfg.globals.ticks_per_round+len(path)-1<cfg.globals.ticks_per_round for i in range(n)) if cfg.minions[kind].hp>exposure else 0
                result=simulate_map(attacker,deepcopy(target),path,1,cfg)
                assert result.hits==expected and result.damage==expected*cfg.minions[kind].damage
                cases.append(dict(layout=row['layout'],kind=kind,count=n,exposure=exposure,expected_hits=expected,original=asdict(result)))
        mixed=['tier1','tier2']*251
        attacker=PlayerState('mixed attacker',800,0,roster=[RosterEntry(i,t,1,None) for i,t in enumerate(mixed)])
        expected=[t for i,t in enumerate(mixed) if cfg.minions[t].hp>exposure and i%cfg.globals.ticks_per_round+len(path)-1<cfg.globals.ticks_per_round]
        result=simulate_map(attacker,deepcopy(target),path,1,cfg)
        assert result.hits==len(expected) and result.damage==sum(cfg.minions[t].damage for t in expected)
        cases.append(dict(layout=row['layout'],kind='alternating tier1/tier2',count=len(mixed),exposure=exposure,expected_hits=len(expected),original=asdict(result)))
    assert len(cases)==93 and all(digest(p)==h for p,h in hashes.items())
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,cases=cases,scope='Fixed selected pure-splash maps, five homogeneous tiers and one mixed roster per map. Checks exact arrival eligibility and strict HP threshold; not full-game strength.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({k:output[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()

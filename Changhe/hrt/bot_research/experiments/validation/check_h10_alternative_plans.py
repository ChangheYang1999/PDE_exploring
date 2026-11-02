"""Compare original-engine round-8 components from a recorded H10 loss."""
from copy import deepcopy
from datetime import datetime, timezone
from dataclasses import asdict
from pathlib import Path
import argparse, hashlib, json, time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.lead.v27 import P, _cost_of
from bot_research.harness import gamekit as gk
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p=argparse.ArgumentParser(); p.add_argument('--result', required=True); p.add_argument('--output', required=True); a=p.parse_args()
    start=time.perf_counter(); digest=lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
    hashes={str(f):digest(f) for f in static_closure({'bot_research.experiments.validation.check_h10_alternative_plans'})}
    hashes['td_game/balanced.json']=digest('td_game/balanced.json'); checked_row(a.result,hashes)
    row=json.loads(Path(a.result).read_text()); records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
    cfg=balanced_config(); engine=Engine(cfg,tuple(row['bot_specs'])); side=row['condition']['candidate_side']; assert side==0
    assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
    for rnd in range(1,8):
        pair=records[2*rnd:2*rnd+2]; actions=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
        assert normalized(engine.play_round(actions))==pair
    obs=engine.observation(side); rules=gk.Rules.from_observation(obs); budget=obs['players'][side]['gold']; assert budget==813
    comps=P.threat_compositions(obs); actual=['tier5']*4
    original=[e['action'] for e in records[16]['event'] if e['kind']=='action' and e['action']['op'] in ('build_wall','build_turret')]
    choices=[('recorded',original),('none',[])]
    for name,threat in [('all',comps),('actual4t5',[actual])]:
        for guns in (False,True):
            for partial in ('best','none'):
                choices.append((f'{name}_guns{int(guns)}_{partial}',P.plan_defense(deepcopy(obs),budget,threat_types=threat,allow_guns=guns,partial=partial)))
    cases=[]
    for name,actions in choices:
        state=player_from_snapshot(obs['players'][side]); assert all(apply_action(state,x,8,cfg)['accepted'] for x in actions)
        path=shortest_path(12,12,((b.x,b.y) for b in state.buildings),(0,0),(11,11)); outcomes=[]
        for comp in [actual,*comps]:
            attack=PlayerState('component attacker',800,0)
            attack.roster=[RosterEntry(i,t,8,19) for i,t in enumerate(comp)]
            totals=simulate_map(attack,deepcopy(state),path,8,cfg)
            outcomes.append(asdict(totals))
        cases.append(dict(name=name,actions=actions,cost=_cost_of(actions,rules),route_length=len(path)-1,actual_four_tier5=outcomes[0],sampled_outcomes=outcomes[1:]))
    assert all(digest(f)==h for f,h in hashes.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,condition=row['condition'],round=8,budget=budget,sampled_rosters=comps,cases=cases,scope='Local alternative plans on one fixed recorded pre-round state. Actual-only plans use hindsight. No full-policy outcome claim.')
    atomic_json(a.output,out,exclusive=True)
    print(json.dumps([{k:c[k] for k in ('name','cost','actual_four_tier5')} for c in cases]))

if __name__=='__main__':main()

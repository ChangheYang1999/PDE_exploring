"""Five predeclared wall interventions on one original-engine witness."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sys

from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
A=E/'analysis/screened_roster_wall_guard';D=E/'screened-roster-wall-guard-001.json'
W=R/'affordable-roster-coverage-001/witnesses/standard-02-side0-r6.jsonl'
O=R/'screened-roster-wall-guard-001'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def declare():
    bottom=[(0,4),(1,4),(2,4)]
    packages=[[],bottom,bottom+[(3,3)],bottom+[(3,3),(3,2)],bottom+[(3,3),(3,2),(3,1)]]
    paths=set(static_closure({'bot_research.experiments.validation.screened_roster_wall_guard'}))|{W,A/'PROOF.md',Path('td_game/balanced.json'),E/'analysis/affordable_roster_coverage/verification/full_check.json'}
    inputs={str(p):sha(p) for p in paths}
    atomic_json(D,dict(time_utc=now(),source_and_input_sha256=inputs,wall_packages=packages,purchase=['tier2','tier2','tier3'],candidate_side=0,counter_side=1,h1='An affordable legal package gives counter HP800 and target HP774.',prior_interventions=0),exclusive=True)
    print(json.dumps(dict(time_utc=now(),packages=len(packages),pins=len(inputs))))
def run():
    d=json.loads(D.read_text());inputs=d['source_and_input_sha256']
    assert all(sha(p)==h for p,h in inputs.items())
    rows=[json.loads(s) for s in W.read_text().splitlines()];cfg=balanced_config()
    names=tuple(r['snapshot']['name'] for r in rows[:2]);engine=Engine(cfg,names)
    assert normalized(engine.initial_records(names))==rows[:2]
    for rnd in range(1,6):
        pair=rows[2*rnd:2*rnd+2]
        acts=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
        assert normalized(engine.play_round(acts))==pair
    assert engine.players[1].gold==190 and cfg.wall_cost==1
    target=[e['action'] for e in rows[12]['event'] if e['kind']=='action']
    O.mkdir(exist_ok=False);results=[]
    for walls in d['wall_packages']:
        counter=[dict(op='buy_minion',type=t) for t in d['purchase']]+[dict(op='build_wall',x=x,y=y) for x,y in walls]
        probe=deepcopy(engine);pair=normalized(probe.play_round([target,counter]))
        checks=[e for r in pair for e in r['event'] if e['kind']=='action']
        legal=all(e['accepted'] for e in checks)
        path=O/f'walls-{len(walls)}.jsonl'
        with path.open('x') as f:
            for r in rows[:12]+pair:f.write(json.dumps(r,sort_keys=True)+'\n')
        blocked={(b.x,b.y) for b in probe.players[1].buildings}
        route=shortest_path(12,12,blocked,(0,0),(11,11))
        exposures=[dict(x=b.x,y=b.y,positions=sum(max(abs(x-b.x),abs(y-b.y))==1 for x,y in route[:-1])) for b in probe.players[1].buildings if b.type=='splash']
        hp=[probe.players[1].hp,probe.players[0].hp]
        results.append(dict(walls=walls,wall_cost=len(walls),total_purchase_cost=180+len(walls),all_actions_legal=legal,action_results=checks,counter_first_hp=hp,guard_succeeded=legal and hp==[800,774],route=route,splash_exposures=exposures,nominal_per_copy_splash=10*sum(e['positions'] for e in exposures),replay=str(path),replay_sha256=sha(path)))
    successful=[r for r in results if r['guard_succeeded']]
    chosen=min(successful,key=lambda r:r['wall_cost']) if successful else None
    assert all(sha(p)==h for p,h in inputs.items())
    result=dict(time_utc=now(),declaration_sha256=sha(D),source_and_input_sha256=inputs,interventions=5,policy_calls=0,full_original_prefix_replayed=True,rows=results,h1='CONFIRMED' if successful else 'REFUTED',minimum_successful_in_family=chosen,scope='Five declared wall packages on one selected fixed-action state. No global minimality or complete-policy result.')
    atomic_json(A/'verification/full_check.json',result,exclusive=True)
    lines=['# Screened roster wall guard results','',f"Completed {result['time_utc']}. H1: **{result['h1']}**.",'','All five packages are retained below. Each uses the same independently replayed original five-round prefix and fixed target action. No policy calls and no complete strength games were run.','','| Walls | All legal | Counter HP | Target HP | Nominal splash |','| --- | --- | --- | --- | --- |']
    for r in results:lines.append(f"| {r['wall_cost']} | {r['all_actions_legal']} | {r['counter_first_hp'][0]} | {r['counter_first_hp'][1]} | {r['nominal_per_copy_splash']} |")
    lines+=['','The minimum successful package, if any, is a minimum only within these five packages. All exact coordinates, routes, action results and six-round replays are linked in verification/full_check.json. A full-game continuation test is separate.','']
    with (A/'RESULTS.md').open('x') as f:f.write('\n'.join(lines))
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f"\n## {now()}: Cheap wall-guard component result\n\nClaim: one of five declared wall packages prevents the return hit while retaining the screened roster's26damage. Method: five original-engine interventions from the exact selected C02 round6 state, full prefix replay, zero policy calls. Result: H1{result['h1']}; successful costs{[r['wall_cost'] for r in successful]}. Verdict: {result['h1']} on this exact state and fixed target action; no full-game win claim or global minimality. Evidence: experiments/validation/analysis/screened_roster_wall_guard/RESULTS.md.\n")
    print(json.dumps(dict(time_utc=now(),h1=result['h1'],successful_costs=[r['wall_cost'] for r in successful])))
if __name__=='__main__':
    {'declare':declare,'run':run}[sys.argv[1]]()

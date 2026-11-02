"""Original-engine interventions at two selected AS1C loss states."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sys
import time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v17.freeplan import free_plan
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure
E=Path('bot_research/experiments/validation')
A=E/'analysis/screened_forecast_defense'
O=Path('bot_research/runs/validation/screened-forecast-defense-001')
D=E/'screened-forecast-defense-001.json'
R=Path('bot_research/runs/validation/screened-guard-transfer-00-001/results/case0000.json')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def actions(pair):return [[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
def declare():
    row=json.loads(R.read_text())
    paths=set(static_closure({'bot_research.experiments.validation.check_screened_forecast_defense'}))|{R,Path(row['replay_path']),A/'PROOF.md',Path('td_game/balanced.json')}
    atomic_json(D,dict(time_utc=now(),rounds=[10,11],methods=['original','visible','post_submission'],input_sha256={str(p):sha(p) for p in sorted(paths)}),exclusive=True)
    print(json.dumps(dict(time_utc=now(),pins=len(paths))))
def run():
    dec=json.loads(D.read_text())
    def verify():assert all(sha(p)==h for p,h in dec['input_sha256'].items())
    verify();O.mkdir(exist_ok=False)
    row=json.loads(R.read_text());records=[json.loads(x) for x in Path(row['replay_path']).read_text().splitlines()]
    cfg=balanced_config();names=tuple(row['bot_specs']);cases=[];evidence={str(D):sha(D)}
    for rnd in dec['rounds']:
        engine=Engine(cfg,names);assert normalized(engine.initial_records(names))==records[:2]
        for r in range(1,rnd):assert normalized(engine.play_round(actions(records[2*r:2*r+2])))==records[2*r:2*r+2]
        observation=engine.observation(0);original=actions(records[2*rnd:2*rnd+2])
        enemy=player_from_snapshot(observation['players'][1]);visible=[e.type for e in enemy.roster if e.active(rnd)]
        assert all(apply_action(enemy,a,rnd,cfg)['accepted'] for a in original[1])
        post=[e.type for e in enemy.roster if e.active(rnd)]
        for method in dec['methods']:
            before=time.perf_counter()
            proposed=original[0] if method=='original' else free_plan(deepcopy(observation),engine.players[0].gold,[visible if method=='visible' else post],partial='best',max_steps=30)
            seconds=time.perf_counter()-before
            own=deepcopy(engine.players[0]);assert all(apply_action(own,a,rnd,cfg)['accepted'] for a in proposed)
            trial=deepcopy(engine);last=normalized(trial.play_round([proposed,original[1]]))
            assert all(e['accepted'] for rr in last for e in rr['event'] if e['kind']=='action')
            if method=='original':assert last==records[2*rnd:2*rnd+2]
            full=records[:2*rnd]+last
            replay=Engine(cfg,names);assert normalized(replay.initial_records(names))==full[:2]
            for r in range(1,rnd+1):assert normalized(replay.play_round(actions(full[2*r:2*r+2])))==full[2*r:2*r+2]
            path=O/f'round{rnd}-{method}.jsonl'
            with path.open('x') as stream:
                for record in full:stream.write(json.dumps(record,sort_keys=True)+'\n')
            evidence[str(path)]=sha(path)
            combat=next(e for e in last[0]['event'] if e['kind']=='combat')
            cases.append(dict(round=rnd,method=method,actions=proposed,decision_seconds=seconds,gold_available=engine.players[0].gold,gold_spent=engine.players[0].gold-own.gold,visible_roster=visible,post_submission_roster=post,incoming_damage=combat['base_damage'],hp=[p.hp for p in trial.players],replay=str(path)))
            print(json.dumps({k:cases[-1][k] for k in ('round','method','decision_seconds','gold_spent','incoming_damage','hp')}),flush=True)
    lookup={(c['round'],c['method']):c for c in cases}
    h1=all(lookup[r,'post_submission']['incoming_damage']<lookup[r,'original']['incoming_damage'] for r in dec['rounds'])
    h2=lookup[10,'post_submission']['incoming_damage']<lookup[10,'visible']['incoming_damage']
    verify();assert all(sha(p)==h for p,h in evidence.items())
    result=dict(time_utc=now(),h1='CONFIRMED' if h1 else 'REFUTED',h2='CONFIRMED' if h2 else 'REFUTED',cases=cases,all_replayed=True,all_actions_accepted=True,input_sha256=dec['input_sha256'],evidence_sha256=evidence,new_strength_games=0,planner_calls=4,policy_calls=0)
    atomic_json(A/'verification/full_check.json',result,exclusive=True)
    lines=['# Selected forecast-defense results','',f'Completed {result["time_utc"]}. H1: **{result["h1"]}**. H2: **{result["h2"]}**.','', '| Round | Input | Gold spent | Incoming damage | Own:enemy HP | Planner seconds |','| --- | --- | --- | --- | --- | --- |']
    for c in cases:lines.append(f'| {c["round"]} | {c["method"]} | {c["gold_spent"]} | {c["incoming_damage"]} | {c["hp"][0]}:{c["hp"][1]} | {c["decision_seconds"]:.6f} |')
    lines+=['','These are six fixed-state interventions, with four local planner calls and zero complete strength games. Every alternative passes original-engine replay and action legality checks. The post-submission input uses the recorded enemy actions; it is not an admissible online information source. A separate public-state forecasting policy and complete-game evaluation are required.','']
    with (A/'RESULTS.md').open('x') as stream:stream.write('\n'.join(lines))
    print(json.dumps({k:result[k] for k in ('time_utc','h1','h2')}))
if __name__=='__main__':{'declare':declare,'run':run}[sys.argv[1]]()

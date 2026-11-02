"""Reconstruct early observations and evaluate the actual passive predicate."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.gamekit import Rules
from bot_research.experiments.lead.v24 import Insurer
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p=argparse.ArgumentParser();p.add_argument('--campaign',required=True);p.add_argument('--candidate',default='P5');p.add_argument('--output',required=True);a=p.parse_args();start=time.perf_counter()
    root=Path(a.campaign);digest=lambda path:hashlib.sha256(Path(path).read_bytes()).hexdigest()
    hashes={str(x):digest(x) for x in static_closure({'bot_research.experiments.validation.audit_passive_gates'})};rows=[]
    jobs=root/'jobs.json';hashes[str(jobs)]=digest(jobs)
    for job in json.loads(jobs.read_text()):
        c=job['condition']
        if c['candidate_id']!=a.candidate:continue
        result=root/'results'/(job['id']+'.json');checked=checked_row(str(result),hashes);row=json.loads(result.read_text());records=[json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
        cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']));assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
        side=c['candidate_side'];policy=Insurer(passive_until=5);rounds=[]
        for rnd in range(1,min(6,row['rounds'])+1):
            obs=engine.observation(side);rules=Rules.from_observation(obs);opp=obs['players'][1-side]
            cost=sum(rules.minions[e['type']]['cost'] for e in opp['roster'] if e['bought_round']>=2)
            turrets=sum(b['type'] in rules.turrets for b in opp['buildings']);gate=policy._passive(obs,rules)
            assert gate==(rnd<=5 and not turrets and cost<=40)
            pair=records[2*rnd:2*rnd+2];actions=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
            assert normalized(engine.play_round(actions))==pair
            rounds.append(dict(round=rnd,post_round1_roster_cost=cost,opponent_turrets=turrets,passive_predicate=gate,candidate_actions=actions[side]))
        rows.append(dict(result=str(result),condition=c,outcome=checked['outcome'],hp=checked['hp_candidate_first'],rounds=rounds))
    assert rows and all(digest(p)==h for p,h in hashes.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,cases=rows,scope='Exact passive predicate re-evaluated on original-engine reconstructions of reached observations. The recorded policy actions are retained; this does not instrument internal planner branches or establish a complete causal explanation.')
    atomic_json(a.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))
if __name__=='__main__':main()

"""Original-engine prefix and affordability check of the guarded heavy schedule."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.heavy_drip import HeavyDrip,DATA,DATA_SHA256
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.perf_counter()
 digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 paths=set(static_closure({'bot_research.experiments.validation.check_heavy_drip'}))|{DATA.relative_to(Path.cwd()),Path('td_game/balanced.json'),Path('configs/balanced.json')};inputs={str(p):digest(p) for p in paths};assert digest(DATA)==DATA_SHA256
 rows=json.loads(DATA.read_text())['schedule'];cases=[]
 for side in (0,1):
  bot=HeavyDrip();engine=Engine(balanced_config(),('a','b'));rounds=[]
  for row in rows:
   rnd=row['round'];obs=engine.observation(side);old=deepcopy(obs);actions=bot.decide(obs);assert obs==old and actions==row['actions']
   pair=[[],[]];pair[side]=actions
   if rnd==2:pair[1-side]=[dict(op='build_turret',type='gun1',x=10,y=1)]
   result=engine.play_round(pair);assert all(e['accepted'] for r in result for e in r['event'] if e['kind']=='action')
   own=engine.snapshot(side);assert own['gold']>=row['end_gold_lower_bound'] and own['length_path']==22
   rounds.append(dict(round=rnd,gold=own['gold'],lower_bound=row['end_gold_lower_bound']))
  cases.append(dict(side=side,rounds=rounds))
 assert all(digest(p)==h for p,h in inputs.items())
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=inputs,cases=cases,scope='Two nine-round original-engine prefixes. Full-game strength and survival against other policies are not inferred.')
 atomic_json(a.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()

"""Check common-prefix selection and round-by-round arm equality on the engine."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.public_opening_selector import PublicOpeningSelector
from bot_research.bots.counters.maze_grower import DATA as WALLS
from bot_research.bots.counters.staged_guard_maze import DATA as GUARDS
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args();start=time.perf_counter()
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    paths=set(static_closure({'bot_research.experiments.validation.check_public_opening_selector'}))|{WALLS.relative_to(Path.cwd()),GUARDS.relative_to(Path.cwd()),Path('td_game/balanced.json'),Path('configs/balanced.json')}
    inputs={str(p):digest(p) for p in paths};cases=[]
    for side in (0,1):
        reused=PublicOpeningSelector()
        for roster in ([],['tier1'],['tier1']*2,['tier1']*3,['tier1']*4,['tier2']):
            selector=reused;engine=Engine(balanced_config(),('a','b'));reference=Engine(balanced_config(),('a','b'));expected='bait' if roster==['tier1']*3 else 'guards'
            arm=getattr(PublicOpeningSelector(),expected);rounds=[]
            for rnd in range(1,10):
                if engine.result is not None:break
                obs=engine.observation(side);old=deepcopy(obs)
                if rnd==1:
                    assert selector.bait.decide(obs)==selector.guards.decide(obs)==[dict(op='buy_factory')]*5
                actions=selector.decide(obs);assert obs==old and actions==arm.decide(reference.observation(side))
                if rnd==1:assert selector.selected is None
                else:assert selector.selected==expected
                opponent=[dict(op='buy_minion',type=t) for t in roster] if rnd==1 else ([dict(op='buy_minion',type='tier1')] if rnd==2 else [])
                pair=[[],[]];pair[side]=actions;pair[1-side]=opponent
                result=engine.play_round(pair);other=reference.play_round(pair)
                assert result==other and engine.result==reference.result
                assert all(e['accepted'] for row in result for e in row['event'] if e['kind']=='action')
                rounds.append(rnd)
            cases.append(dict(side=side,opening=roster,selected=expected,verified_rounds=rounds))
    assert all(digest(p)==h for p,h in inputs.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=inputs,cases=cases,scope='Twelve original-engine prefixes, same first-round submission, immutable observations, sticky public selection and reset on reuse. This is not a full-game strength claim.')
    atomic_json(args.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()

"""Check public clones, independent target actions and combat on reached prefixes."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.early_wall_guard import EarlyWallGuard
from bot_research.bots.counters.stateful_public import StatefulPublicTiming
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.audit_adaptive_attacks import combat
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    start=time.perf_counter();digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    inputs={str(p):digest(p) for p in static_closure({'bot_research.experiments.validation.check_early_wall_component'})}
    for name in ('early_wall_guard_001.json',):
        p=Path('bot_research/bots/counters/data')/name;inputs[str(p)]=digest(p)
    for name in ('td_game/balanced.json','bot_research/experiments/validation/analysis/early_wall_policy/PROOF.md'):
        inputs[name]=digest(name)
    cases=[]
    for witness in ('guard00','guard01','guard02','guard03','guard04','guard05','guard06','guard07'):
        for rnd_attack,tier,defense_first in ((3,'tier2',False),):
            for side in (0,1):
                forecaster=StatefulPublicTiming(model_spec='bot_research.bots.counters.early_wall_guard:@make',
                    model_parameters={'witness':witness},attack_round=rnd_attack,tier=tier,
                    defense_first=defense_first,attack_share=1,count_cap=200)
                target=EarlyWallGuard(witness=witness)
                engine=Engine(balanced_config(),('prefix0','prefix1'));rounds=[]
                for rnd in range(1,6):
                    if engine.result is not None:break
                    own_obs=engine.observation(side);target_obs=engine.observation(1-side)
                    saved_own,saved_target=deepcopy(own_obs),deepcopy(target_obs)
                    actions=forecaster.decide(own_obs);other=target.decide(target_obs)
                    assert own_obs==saved_own and target_obs==saved_target
                    trace=forecaster.trace[-1]
                    assert trace['predicted_actions']==other
                    assert forecaster.model.last_round==rnd and forecaster.model.player==1-side
                    own=player_from_snapshot(saved_own['players'][side]);enemy=player_from_snapshot(saved_own['players'][1-side])
                    for state,chosen in ((own,actions),(enemy,other)):
                        assert all(apply_action(state,a,rnd,engine.config)['accepted'] for a in chosen)
                    incoming=combat(enemy,own,rnd,engine.config)
                    assert incoming==trace['forecast_residual_damage']
                    pair=[None,None];pair[side]=actions;pair[1-side]=other
                    records=engine.play_round(pair)
                    assert all(e['accepted'] for r in records for e in r['event'] if e['kind']=='action')
                    assert saved_own['players'][side]['hp']-engine.players[side].hp==incoming
                    rounds.append(dict(round=rnd,forecast_exact=True,incoming_damage=incoming,
                        actual_attack_count=trace['attack_count'],target_trace=target.trace[-1], target_filtered=len(target.filtered_proposals)))
                cases.append(dict(witness=witness,side=side,attack_round=rnd_attack,tier=tier,
                    defense_first=defense_first,rounds=rounds))
                print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),finished=len(cases),witness=witness,side=side,rounds=len(rounds))),flush=True)
    assert len(cases)==16 and all(digest(p)==h for p,h in inputs.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        all_passed=True,filtered_proposals=sum(c['rounds'][-1]['target_filtered'] for c in cases),prefixes=16,checked_rounds=sum(len(c['rounds']) for c in cases),cases=cases,input_sha256=inputs,
        scope='Sixteen early-wall prefixes through round five: exact public clones, independent target actions, legal submissions, unchanged observations and original incoming combat. Not full-game strength.')
    atomic_json(args.output,out,exclusive=True)
    print(json.dumps({k:v for k,v in out.items() if k not in ('cases','input_sha256')}),flush=True)

if __name__=='__main__':main()

"""Check H's public clone against independent original-engine prefixes."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import parse_qs
import hashlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.hp_handoff import HPHandoff
from bot_research.bots.counters.stateful_public import StatefulPublicTiming
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.audit_adaptive_attacks import combat
E=Path('bot_research/experiments/validation')
A=E/'analysis/hp_handoff_forecaster'

def main():
    start=time.perf_counter();d=json.loads((E/'hp-handoff-forecaster-campaigns-001.json').read_text())
    inputs=d['input_sha256'].copy()
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    for p,h in inputs.items():assert digest(p)==h,p
    inputs[str(E/'hp-handoff-forecaster-campaigns-001.json')]=digest(E/'hp-handoff-forecaster-campaigns-001.json')
    parameters={k:json.loads(v[0]) for k,v in parse_qs(d['target']['spec'].partition('?')[2]).items()}
    cases=[]
    for ar,tier,df in ((3,'tier2',False),(5,'tier4',True)):
        for side in (0,1):
            target=HPHandoff(**parameters)
            attacker=StatefulPublicTiming(model_spec='bot_research.bots.counters.hp_handoff:@make',model_parameters=parameters,
                attack_round=ar,tier=tier,defense_first=df,attack_share=1,count_cap=200)
            engine=Engine(balanced_config(),('prefix0','prefix1'));rr=[]
            for rnd in range(1,9):
                if engine.result is not None:break
                obs=engine.observation(side);otherobs=engine.observation(1-side)
                before,otherbefore=deepcopy(obs),deepcopy(otherobs)
                aa=attacker.decide(obs);bb=target.decide(otherobs)
                assert obs==before and otherobs==otherbefore
                trace=attacker.trace[-1];assert trace['predicted_actions']==bb
                own=player_from_snapshot(before['players'][side]);enemy=player_from_snapshot(before['players'][1-side])
                for state,actions in ((own,aa),(enemy,bb)):
                    assert all(apply_action(state,a,rnd,engine.config)['accepted'] for a in actions)
                incoming=combat(enemy,own,rnd,engine.config)
                assert incoming==trace['forecast_residual_damage']
                actions=[None,None];actions[side]=aa;actions[1-side]=bb
                result=engine.play_round(actions)
                assert all(e['accepted'] for row in result for e in row['event'] if e['kind']=='action')
                assert before['players'][side]['hp']-engine.players[side].hp==incoming
                rr.append(dict(round=rnd,prediction_exact=True,incoming_damage=incoming,
                    actual_attack_count=trace['attack_count'],target_switched=target.switched))
            assert not target.rejected_proposals
            cases.append(dict(attack_round=ar,tier=tier,defense_first=df,attacker_side=side,rounds=rr))
    assert len(cases)==4 and all(digest(p)==h for p,h in inputs.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        all_passed=True,prefixes=4,checked_rounds=sum(len(c['rounds']) for c in cases),filtered_proposals=0,
        cases=cases,input_sha256=inputs,scope='Original-engine prefixes only, not full-game strength.')
    atomic_json(A/'verification/component.json',out,exclusive=True)
    print(json.dumps({k:v for k,v in out.items() if k not in ('cases','input_sha256')}),flush=True)

if __name__=='__main__':main()

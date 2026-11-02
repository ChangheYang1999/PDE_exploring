"""Finite legal-prefix checks for the fourth-round purchase intervention."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.counters.early_wall_guard import EarlyWallGuard
from bot_research.bots.counters.early_wall_attack_ablation import EarlyWallAttackAblation
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.replay_audit import normalized

E=Path('bot_research/experiments/validation')
A=E/'analysis/early_wall_attack_ablation'


def grower(obs, mode):
    cfg=balanced_config(); state=player_from_snapshot(obs['players'][obs['player']]); actions=[]
    strike={'growth':None, 'early_t1':(1,'tier1',1), 'r3_t2':(3,'tier2',4), 'r4_t4':(4,'tier4',1)}[mode]
    if strike and obs['round']==strike[0]:
        for _ in range(strike[2]):
            action=dict(op='buy_minion',type=strike[1])
            if state.gold<cfg.minions[strike[1]].cost: break
            assert apply_action(state,action,obs['round'],cfg)['accepted']
            actions.append(action)
    while state.gold>=cfg.globals.factory_cost:
        action=dict(op='buy_factory'); assert apply_action(state,action,obs['round'],cfg)['accepted']
        actions.append(action)
    return actions


def run_prefix(policy, mode, side):
    cfg=balanced_config(); engine=Engine(cfg,('a','b')); output=[]
    for rnd in range(1,6):
        obs=engine.observation(side); saved=deepcopy(obs); own=policy.decide(obs)
        assert obs==saved
        other=grower(engine.observation(1-side),mode)
        actions=[own,other] if side==0 else [other,own]
        records=normalized(engine.play_round(actions))
        assert all(e['accepted'] for rec in records for e in rec['event'] if e['kind']=='action')
        assert engine.result is None
        output.append(dict(round=rnd,actions=actions,records=records))
    assert not policy.filtered_proposals
    return output


def main():
    start=time.perf_counter()
    declaration=json.loads((E/'early-wall-attack-campaigns-001.json').read_text())
    pins=declaration['component_input_sha256']
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    for p,h in pins.items():assert digest(p)==h,p
    controls=[];variants=[]
    for mode in ('growth','early_t1','r3_t2','r4_t4'):
        for side in (0,1):
            original=run_prefix(EarlyWallGuard('guard00'),mode,side)
            copy=run_prefix(EarlyWallAttackAblation('tier4'),mode,side)
            assert original==copy,(mode,side)
            controls.append(dict(mode=mode,side=side,identical=True,records=original))
            for tier in (None,'tier3'):
                new=run_prefix(EarlyWallAttackAblation(tier),mode,side)
                assert new[:3]==original[:3]
                variants.append(dict(mode=mode,side=side,round4_type=tier,records=new))
    for p,h in pins.items():assert digest(p)==h,p
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        all_passed=True,control_prefixes=8,variant_prefixes=16,rounds_per_prefix=5,
        exact_control_policy_calls=80,intervention_policy_calls=80,filtered_proposals=0,
        controls=controls,variants=variants,input_sha256=pins)
    atomic_json(A/'verification/component.json',result,exclusive=True)
    print(json.dumps({k:v for k,v in result.items() if k not in ('controls','variants','input_sha256')}))


if __name__=='__main__':main()

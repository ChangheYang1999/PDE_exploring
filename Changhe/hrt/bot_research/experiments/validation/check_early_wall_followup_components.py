"""Check the public-roster intervention on fixed legal six-round prefixes."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.early_wall_guard import EarlyWallGuard
from bot_research.bots.counters.early_wall_followup import EarlyWallFollowup
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.check_early_wall_attack_components import grower
from bot_research.experiments.validation.replay_audit import normalized

E = Path('bot_research/experiments/validation')
A = E/'analysis/early_wall_followup'


def run_prefix(policy, mode, side):
    cfg = balanced_config()
    engine = Engine(cfg, ('a','b'))
    records = []
    for rnd in range(1,7):
        obs = engine.observation(side)
        before = deepcopy(obs)
        actions = policy.decide(obs)
        assert obs == before
        state = player_from_snapshot(obs['players'][side])
        assert all(apply_action(state,a,rnd,cfg)['accepted'] for a in actions)
        other = grower(engine.observation(1-side), mode)
        pair = [actions,other] if side==0 else [other,actions]
        events = normalized(engine.play_round(pair))
        assert all(e['accepted'] for r in events for e in r['event'] if e['kind']=='action')
        assert engine.result is None
        records.append(dict(round=rnd,actions=pair,records=events))
    assert not policy.filtered_proposals
    return records


def main():
    start=time.perf_counter()
    declaration=json.loads((E/'early-wall-followup-campaigns-001.json').read_text())
    pins=declaration['component_input_sha256']
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    for p,h in pins.items():assert digest(p)==h,p
    controls=[]
    variants=[]
    for mode in ('growth','early_t1','r3_t2','r4_t4'):
        for side in (0,1):
            original=run_prefix(EarlyWallGuard('guard00'),mode,side)
            disabled=run_prefix(EarlyWallFollowup('disabled'),mode,side)
            assert original==disabled
            controls.append(dict(mode=mode,side=side,identical=True,records=original))
            for package in ('one_tier3','two_tier3','one_tier4'):
                policy=EarlyWallFollowup(package)
                changed=run_prefix(policy,mode,side)
                assert changed[:4]==original[:4]
                assert len(policy.followup_trace)==1
                trace=policy.followup_trace[0]
                assert trace['triggered']==(mode=='growth')
                if mode!='growth':assert changed==original
                else:assert trace['purchases']==list(policy.package)
                variants.append(dict(mode=mode,side=side,package=package,
                    trace=trace,records=changed,complete_control_agreement=changed==original))
    for p,h in pins.items():assert digest(p)==h,p
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        all_passed=True,control_prefixes=8,variant_prefixes=24,rounds_per_prefix=6,
        exact_control_policy_calls=96,intervention_policy_calls=144,filtered_proposals=0,
        controls=controls,variants=variants,input_sha256=pins)
    atomic_json(A/'verification/component.json',result,exclusive=True)
    print(json.dumps({k:v for k,v in result.items() if k not in ('controls','variants','input_sha256')}))


if __name__=='__main__':main()

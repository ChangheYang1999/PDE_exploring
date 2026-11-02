"""Check public round-five handoff components on three reached histories."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.delegated_defense import DelegatedRouteSelector
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')

def main():
    inputs={}
    def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    for path in static_closure({'bot_research.experiments.validation.check_delegated_component'}):inputs[str(path)]=digest(path)
    roots=[('emergency-prefix-001',{'baseline','flood'},'emergency_damage'),
           ('emergency-transfer-c001',{'lead_opening_g6_tier5'},'route_adaptive')]
    selected=[]
    for name,targets,counter in roots:
        root=R/name
        for job in json.loads((root/'jobs.json').read_text()):
            c=job['condition']
            if c['candidate_id'] in targets and c['opponent_id']==counter:
                selected.append((c,root/'results'/(job['id']+'.json')))
    assert len(selected)==6
    results=[]
    for condition,path in selected:
        checked_row(str(path),inputs);row=json.loads(path.read_text())
        records=[json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
        for delegate in ('template','econ20','fortress38'):
            cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']));side=1-condition['candidate_side']
            policy=DelegatedRouteSelector(delegate=delegate)
            assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
            for rnd in range(1,5):
                obs=engine.observation(side);saved=deepcopy(obs);fresh=policy.decide(obs)
                assert obs==saved
                pair=records[2*rnd:2*rnd+2]
                actions=[[event['action'] for event in rec['event'] if event['kind']=='action'] for rec in pair]
                assert fresh==actions[side]
                assert normalized(engine.play_round(actions))==pair
            obs=engine.observation(side);saved=deepcopy(obs);actions=policy.decide(obs);assert obs==saved
            local=player_from_snapshot(obs['players'][side]);gold=local.gold
            assert all(apply_action(local,action,5,cfg)['accepted'] for action in actions)
            pair=records[10:12]
            target_actions=[event['action'] for event in pair[1-side]['event'] if event['kind']=='action']
            submitted=[None,None];submitted[side]=actions;submitted[1-side]=target_actions
            actual=normalized(engine.play_round(submitted))
            incoming=next(event['base_damage'] for event in actual[side]['event'] if event['kind']=='combat')
            outgoing=next(event['base_damage'] for event in actual[1-side]['event'] if event['kind']=='combat')
            if delegate=='template':assert actual==pair
            results.append(dict(target=condition['candidate_id'],candidate_side=condition['candidate_side'],
                delegate=delegate,prefix_exact=True,observations_unchanged=True,actions_legal=True,
                delegate_started=policy.delegate_started,delegation=policy.delegation_trace[-1],actions=actions,
                total_spend=gold-local.gold,incoming_damage=incoming,outgoing_damage=outgoing,
                hp_counter_first=[actual[side]['snapshot']['hp'],actual[1-side]['snapshot']['hp']],
                resulting_map=actual[side]['snapshot']['buildings'],reference=str(path)))
            print(json.dumps({key:results[-1][key] for key in ('target','candidate_side','delegate','total_spend','incoming_damage','outgoing_damage','hp_counter_first')}),flush=True)
    assert all(digest(path)==sha for path,sha in inputs.items())
    atomic_json(E/'analysis/delegated_defense/verification/component.json',dict(time_utc=datetime.now(timezone.utc).isoformat(),
        all_passed=True,components=len(results),results=results,input_sha256=inputs,
        scope='Reached round-five components only. First four decisions exact, actions legal, original engine. No full-game strength claim.'),exclusive=True)

if __name__=='__main__':main()

"""Verify repair effects with fixed-opponent one-round engine interventions."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,traceback
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.counters.wall_signal_timing import WallSignalTiming
from bot_research.experiments.validation.artifact_io import atomic_json,public_diagnostic
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/wall_signal_repair'

def main():
    inputs={};digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):inputs[str(p)]=digest(p);return json.loads(Path(p).read_text())
    manifest=read(E/'wall-signal-repair-engine-001.json')
    for p,h in manifest['input_sha256'].items():assert digest(p)==h,p;inputs[p]=h
    full=read(A/'verification/full_games.json');assert full['all_passed']
    for p,h in full['input_sha256'].items():assert digest(p)==h,p;inputs[p]=h
    audit=read(R/'wall-signal-repair-001-forecasts.json');assert audit['all_passed'];cases=[]
    for case in audit['cases']:
        record=checked_row(case['result_path'],inputs);raw=read(case['result_path']);side=record['condition']['candidate_side'];target=record['condition']['opponent_id']
        cfg=balanced_config();engine=Engine(cfg,tuple(raw['bot_specs']));parent=WallSignalTiming(wall_count=20)
        records=[json.loads(s) for s in Path(raw['replay_path']).read_text().splitlines()]
        assert normalized(engine.initial_records(tuple(raw['bot_specs'])))==records[:2];rounds=[]
        for trace in case['rounds']:
            rnd=trace['round'];obs=engine.observation(side);saved=deepcopy(obs);old_actions=parent.decide(obs);assert obs==saved
            own=player_from_snapshot(obs['players'][side]);assert all(apply_action(own,a,rnd,cfg)['accepted'] for a in old_actions)
            pair=records[2*rnd:2*rnd+2];actual=[[e['action'] for e in row['event'] if e['kind']=='action'] for row in pair]
            assert parent.trace[-1]['predicted_actions']==trace['predicted_actions']
            selected=trace['repair']['selected'];before=obs['players'][side]['hp'];alternative_damage=None
            if selected:
                alternative=deepcopy(engine);old_pair=deepcopy(actual);old_pair[side]=old_actions
                alternative.play_round(old_pair);alternative_damage=before-alternative.players[side].hp
            assert normalized(engine.play_round(actual))==pair
            damage=before-engine.players[side].hp
            if rnd>=4 and target in ('J','H'):
                assert trace['model_matches'];assert damage==trace['forecast_residual_damage']
                if selected:
                    assert alternative_damage==trace['repair']['original_predicted_damage']
                    assert damage<alternative_damage
            rounds.append(dict(round=rnd,repair_selected=selected,actual_damage=damage,parent_intervention_damage=alternative_damage,predicted_final_damage=trace['forecast_residual_damage']))
        assert engine.result==raw['result'];cases.append(dict(result_path=case['result_path'],target=target,side=side,rounds=rounds))
    assert len(cases)==6 and all(digest(p)==h for p,h in inputs.items())
    stamp=datetime.now(timezone.utc).isoformat();calls=sum(len(c['rounds']) for c in cases);interventions=sum(r['repair_selected'] for c in cases for r in c['rounds'])
    result=dict(time_utc=stamp,all_passed=True,cases=cases,additional_parent_calls=calls,one_round_interventions=interventions,new_full_strength_games=0,input_sha256=inputs)
    atomic_json(A/'verification/engine_comparison.json',result,exclusive=True)
    with (A/'ENGINE_CHECK_RESULTS.md').open('x') as f:f.write(f'# Original-engine repair comparison\n\nChecked {stamp}. Claim: CONFIRMED on all checked H/J rounds and selected repairs. All six actual histories reproduce, {calls} separate parent-policy calls are legal and preserve observations, and {interventions} one-round interventions were executed. On H/J rounds from round four, every final residual prediction equals actual original-engine damage; every selected repair has strictly less damage than its parent-action intervention. I interventions are retained without a strict-reduction requirement because its actual policy differs from the private model. These are reached-state current-round checks, not new complete strength games or a long-run optimality claim. See ENGINE_CHECK_PROTOCOL.md and verification/engine_comparison.json.\n')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Original-engine comparison of selected wall-signal repairs\n\nClaim: conditional current-round reductions survive replacement of the private simulator by the unchanged engine. Method: six exact replays, {calls} separately regenerated parent actions, {interventions} fixed-enemy one-round interventions. Result: every H/J final damage prediction from round four is exact and every selected H/J repair strictly reduces damage. Verdict: CONFIRMED on these reached states only. No new full strength game. Evidence: experiments/validation/analysis/wall_signal_repair/ENGINE_CHECK_RESULTS.md.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','input_sha256')}),flush=True)
if __name__=='__main__':
    try:main()
    except Exception:
        print(public_diagnostic(traceback.format_exc()),flush=True);raise SystemExit(1)

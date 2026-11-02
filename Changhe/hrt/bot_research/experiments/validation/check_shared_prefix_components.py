"""Check legal shared-prefix selection against independent fixed responses."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib,json
from td_game.engine import Engine
from td_game.config import balanced_config
from td_game.actions import apply_action
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.counters.shared_prefix_selector import SharedPrefixSelector,make_h,make_i
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.isolated_match import resolve


def main():
    E=Path('bot_research/experiments/validation');d=json.loads((E/'shared-prefix-campaigns-001.json').read_text())
    cases=[]
    for target,reference_factory in [('G',make_h),('H',make_i),('I',make_i)]:
        for side in (0,1):
            selector=SharedPrefixSelector();reference=reference_factory()
            opponent=resolve({'spec':d['policies'][target]['spec']})
            engine=Engine(balanced_config(),('component_a','component_b'));rounds=[]
            for rnd in range(1,9):
                obs=engine.observation(side);before=deepcopy(obs)
                actual=selector.decide(obs);expected=reference.decide(deepcopy(before))
                assert obs==before and actual==expected,(target,side,rnd)
                other=engine.observation(1-side);other_before=deepcopy(other)
                response=opponent.decide(other);assert other==other_before
                pair=[None,None];pair[side]=actual;pair[1-side]=response
                for p,actions in enumerate(pair):
                    state=player_from_snapshot(engine.observation(p)['players'][p])
                    assert all(apply_action(state,x,rnd,engine.config)['accepted'] for x in actions)
                engine.play_round(pair)
                rounds.append(dict(round=rnd,branch=selector.selected,actions_equal=True))
                if engine.result is not None:break
            assert selector.selected==('H' if target=='G' else 'I')
            cases.append(dict(opponent=target,side=side,rounds=rounds))
    inputs={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [E/'shared-prefix-campaigns-001.json',Path(__file__).relative_to(Path.cwd())]}
    for p,h in d['input_sha256'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h;inputs[p]=h
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,cases=cases,input_sha256=inputs)
    atomic_json(E/'analysis/shared_prefix_response/verification/components.json',result,exclusive=True)
    print(json.dumps(dict(time_utc=result['time_utc'],all_passed=True,cases=len(cases),checked_rounds=sum(len(x['rounds']) for x in cases))),flush=True)


if __name__=='__main__':main()

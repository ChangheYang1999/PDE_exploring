"""Check the declared model-free controller through its first handoff round."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse, hashlib, json, time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.budget_handoff import BudgetHandoff
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    declaration = Path('bot_research/experiments/validation/budget-handoff-001.json')
    manifest = json.loads(declaration.read_text())
    hashes = dict(manifest['input_sha256'])
    paths = static_closure({'bot_research.experiments.validation.check_budget_handoff_opening'})
    paths += [declaration]
    hashes.update({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in hashes.items())
    cases = []
    for row in manifest['opponents']:
        params={k:json.loads(v[0]) for k,v in parse_qs(row['spec'].partition('?')[2]).items()}
        for side in (0,1):
            policy = BudgetHandoff(**params)
            target = resolve(manifest['candidates'][0]).decide
            policies = [target, policy.decide] if side==0 else [policy.decide, target]
            engine=Engine(balanced_config(), ('budget_component_a','budget_component_b'))
            rounds=[]
            for rnd in range(1, params['deadline']+1):
                observations=[engine.observation(s) for s in (0,1)]
                originals=deepcopy(observations)
                actions=[policies[s](observations[s]) for s in (0,1)]
                assert observations==originals
                if rnd>=params['deadline']:
                    assert all(a['op']!='buy_minion' for a in actions[1-side])
                records=engine.play_round(actions)
                assert all(e['accepted'] for rec in records for e in rec['event'] if e['kind']=='action')
                if rnd==5:
                    assert engine.players[side].hp==740 and engine.players[1-side].hp==755
                rounds.append(dict(round=rnd,records=records,trace=policy.trace[-1]))
            cases.append(dict(opponent_id=row['id'],target_side=side,rounds=rounds,
                observations_unchanged=True,all_actions_accepted=True,filtered_proposals=policy.filtered_proposals))
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in hashes.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-started,
        input_sha256=hashes,cases=cases,all_passed=True,
        scope='Original-engine bounded prefixes only. No full-game outcome inferred.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()

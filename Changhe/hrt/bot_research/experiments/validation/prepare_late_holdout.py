"""Prospective reserve for a revision selected after the existing pool B.

No candidate is loaded. Only prescribed opening histories are executed.
The reserve tests new parameters and histories within known policy families.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.scenarios import make_overrides
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def spec(entry, **params):
    return entry+'?'+urlencode({k:json.dumps(v,separators=(',',':')) for k,v in params.items()})


def main():
    profiles=[
        dict(growth_rounds=3,roster=['tier3','tier2','tier1'],defense='splash',defense_count=2,keep_investing=0.30),
        dict(growth_rounds=5,roster=['tier4','tier4','tier1'],defense='gun2',defense_count=2,pulse_period=4,pulse_phase=2),
        dict(growth_rounds=9,roster=['tier5','tier2'],defense='splash',defense_count=4,pulse_period=5,pulse_phase=1),
        dict(growth_rounds=1,roster=['tier1','tier2','tier1'],defense='gun1',defense_count=2,keep_investing=0.45)]
    factories=[
        spec('bot_research.bots.counters.pool:@random_legal',seed=7919,attack_bias=0.33,action_cap=37),
        spec('bot_research.bots.counters.pool:@mirror',attack_floor=0.31,defense_share=0.39),
        spec('bot_research.bots.counters.pool:@stacker',growth_rounds=9,tier='tier2',batch_cap=920),
        spec('bot_research.bots.counters.pool:@turtle',kind='splash',defense_share=0.43,max_towers=31),
        spec('bot_research.bots.counters.budget_timing:@make',tier='tier3',attack_round=4,budget_fraction=0.65),
        spec('bot_research.bots.counters.budget_timing:@make',tier='tier4',attack_round=6,budget_fraction=0.65),
        spec('bot_research.bots.counters.guard_geometry:@make',roster=['tier1'],x=9,y=2),
        spec('bot_research.bots.counters.guard_geometry:@make',roster=['tier2'],x=10,y=2)]
    scenarios=[]
    evidence=[]
    for name in ('mirror:7493:3','asym:8669:2'):
        overrides=make_overrides(name)
        e=Engine(balanced_config(),('prefix_candidate','prefix_opponent'))
        prefixes=[[],[]]
        records=[]
        for _ in range(int(name.rsplit(':',1)[1])):
            pair=[overrides[i](e.observation(i)) for i in (0,1)]
            assert all(isinstance(actions,list) for actions in pair)
            for i in (0,1):
                prefixes[i].append(pair[i])
            rr=e.play_round(pair)
            assert all(ev['accepted'] for rec in rr for ev in rec['event'] if ev['kind']=='action')
            records.extend(rr)
        assert e.result is None
        scenarios.append(dict(name=name.replace(':','_'),generator=name,prefixes=prefixes,
            semantics='Candidate-relative prescribed actions, swapped with player assignment. Policy calls are skipped during the prefix.'))
        evidence.append(dict(generator=name,rounds=e.round,records=records,
            ending_hp=[p.hp for p in e.players]))
    roots={'bot_research.experiments.validation.prepare_late_holdout',
           'bot_research.bots.counters.archetypes','bot_research.bots.counters.pool',
           'bot_research.bots.counters.budget_timing','bot_research.bots.counters.guard_geometry'}
    paths=set(static_closure(roots))|{Path('td_game/balanced.json'),Path('configs/balanced.json')}
    sources={str(p):digest(p) for p in sorted(paths)}
    stamp=datetime.now(timezone.utc).isoformat()
    check='bot_research/runs/validation/late-holdout-prefix-check-001.json'
    atomic_json(check,dict(time_utc=stamp,all_passed=True,original_engine_rounds=5,
        source_sha256=sources,cases=evidence,
        scope='Legal scripted histories only. No candidate or opponent policy was called.'),exclusive=True)
    out=dict(created_utc=stamp,pool='C',status='UNUSED',profiles=profiles,factory_specs=factories,
        scenarios=scenarios,planned_conditions=72,source_sha256=sources,prefix_check=check,
        prefix_check_sha256=digest(check),
        purpose='Late reserve for a candidate revised after seeing pool B. Do not run before a new explicit final freeze.',
        selection='Designed after pool A and the disclosed development studies. No candidate outcomes have been measured on these exact conditions.',
        interpretation_limit='Twelve held-out parameter settings within known implementation families, and two held-out candidate-relative scripted histories. Not independent random policy samples. Standard games and continuation stress are reported separately. Prefix calls are skipped; both physical assignments are paired controls.',
        retirement='Any revision informed by these results retires C from confirmatory use. Audit overlap with team experiments before labelling a condition held-out.')
    dest='bot_research/experiments/validation/late_holdout_manifest.json'
    atomic_json(dest,out,exclusive=True)
    print(json.dumps(dict(time_utc=stamp,manifest=dest,sha256=digest(dest),planned_conditions=72,all_prefix_checks_passed=True)))


if __name__=='__main__':
    main()

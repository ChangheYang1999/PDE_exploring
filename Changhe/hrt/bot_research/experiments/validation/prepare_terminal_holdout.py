"""Prospectively declare pool D without calling any candidate or opponent."""
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
from bot_research.experiments.validation.audit_terminal_separation import canonical


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def spec(entry, **parameters):
    return entry+'?'+urlencode({k:json.dumps(v,separators=(',',':')) for k,v in parameters.items()})


def main():
    profiles = [
        dict(growth_rounds=2,roster=['tier2','tier1','tier1'],defense='splash',defense_count=1,keep_investing=0.2),
        dict(growth_rounds=4,roster=['tier3','tier3','tier1'],defense='gun2',defense_count=2,pulse_period=3,pulse_phase=1),
        dict(growth_rounds=7,roster=['tier4','tier2','tier1'],defense='splash',defense_count=3,keep_investing=0.35),
        dict(growth_rounds=10,roster=['tier5','tier3'],defense='splash',defense_count=2,pulse_period=4,pulse_phase=3)]
    factories = [
        spec('bot_research.bots.counters.pool:@random_legal',seed=104729,attack_bias=0.47,action_cap=43),
        spec('bot_research.bots.counters.pool:@mirror',attack_floor=0.27,defense_share=0.46),
        spec('bot_research.bots.counters.pool:@stacker',growth_rounds=8,tier='tier3',initial_splash=False,batch_cap=840),
        spec('bot_research.bots.counters.pool:@turtle',kind='splash',defense_share=0.57,max_towers=29),
        spec('bot_research.bots.counters.budget_timing:@make',tier='tier1',attack_round=3,budget_fraction=0.8),
        spec('bot_research.bots.counters.budget_timing:@make',tier='tier3',attack_round=4,budget_fraction=0.8),
        spec('bot_research.bots.counters.budget_timing:@make',tier='tier4',attack_round=6,budget_fraction=0.8),
        spec('bot_research.bots.counters.budget_timing:@make',tier='tier5',attack_round=8,budget_fraction=0.8),
        spec('bot_research.bots.counters.guard_geometry:@make',roster=['tier1','tier1','tier1'],x=8,y=2),
        spec('bot_research.bots.counters.guard_geometry:@make',roster=['tier2','tier1'],x=9,y=3),
        spec('bot_research.bots.counters.guarded_schedule:@make',schedule=[[3,'tier2',3],[6,'tier4',2]],defense_first=False),
        spec('bot_research.bots.counters.guarded_schedule:@make',schedule=[[4,'tier3',2],[7,'tier5',2]],initial_threat=['tier1']*3,defense_first=True,saturate_round=18,max_factories=96)]
    normalized=[canonical({'profile':p}) for p in profiles]+[canonical({'spec':s}) for s in factories]
    assert len(set(normalized))==16
    scenarios, cases = [], []
    for name in ('mirror:104729:3', 'asym:130363:2'):
        overrides=make_overrides(name)
        engine=Engine(balanced_config(), ('prefix_candidate','prefix_opponent'))
        prefixes=[[],[]]
        records=[]
        for _ in range(int(name.rsplit(':',1)[1])):
            actions=[overrides[i](engine.observation(i)) for i in (0,1)]
            assert all(isinstance(a,list) for a in actions)
            for i in (0,1): prefixes[i].append(actions[i])
            rr=engine.play_round(actions)
            assert all(e['accepted'] for r in rr for e in r['event'] if e['kind']=='action')
            records.extend(rr)
        assert engine.result is None
        scenarios.append(dict(name=name.replace(':','_'),generator=name,prefixes=prefixes,
            semantics='Candidate-relative legal prescribed actions. Swapped with assignments. Both underlying policies are skipped during their prefixes.'))
        cases.append(dict(generator=name,rounds=engine.round,records=records,ending_hp=[p.hp for p in engine.players]))
    roots={'bot_research.experiments.validation.prepare_terminal_holdout',
           'bot_research.experiments.validation.terminal_validation',
           'bot_research.experiments.validation.audit_terminal_campaign',
           'bot_research.experiments.validation.audit_terminal_separation',
           'bot_research.experiments.validation.audit_terminal_scenario_separation',
           'bot_research.experiments.validation.render_terminal_summary',
           'bot_research.bots.counters.archetypes','bot_research.bots.counters.pool',
           'bot_research.bots.counters.budget_timing','bot_research.bots.counters.guard_geometry',
           'bot_research.bots.counters.guarded_schedule'}
    paths=set(static_closure(roots))|set(map(Path, ['td_game/balanced.json','configs/balanced.json',
        'bot_research/experiments/validation/analysis/terminal_reserved_validation/PROOF.md']))
    sources={str(p):digest(p) for p in sorted(paths)}
    stamp=datetime.now(timezone.utc).isoformat()
    check='bot_research/runs/validation/terminal-holdout-prefix-check-001.json'
    atomic_json(check,dict(time_utc=stamp,all_passed=True,source_sha256=sources,cases=cases,
        candidate_or_opponent_calls=0,scope='Original-engine legality of prescribed histories only.'),exclusive=True)
    manifest=dict(created_utc=stamp,pool='D',status='UNUSED',profiles=profiles,factory_specs=factories,
        scenarios=scenarios,planned_conditions=96,source_sha256=sources,prefix_check=check,
        prefix_check_sha256=digest(check),not_before_utc='2026-10-31T23:00:00+00:00',
        purpose='Terminal report of the final installed candidate; not a candidate-selection pool.',
        selection='Designed using prior development mechanisms; exact parameters and histories are not screened on any candidate.',
        interpretation_limit='Sixteen parameter settings within known families and two candidate-relative legal histories. No independent random policy sample. Standard-start strength and continuation stress are reported separately.',
        retirement='After any D result is inspected, no informed revision may claim untouched validation on D.')
    path='bot_research/experiments/validation/terminal_holdout_manifest.json'
    atomic_json(path,manifest,exclusive=True)
    print(json.dumps(dict(time_utc=stamp,manifest=path,sha256=digest(path),planned_conditions=96,all_prefix_checks_passed=True,candidate_or_opponent_calls=0)))


if __name__=='__main__':
    main()

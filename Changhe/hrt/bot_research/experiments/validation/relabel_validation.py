"""Finite public-label/index audit of the final policy on retained C histories."""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.source_closure import static_closure

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
CAMPAIGN = R / 'reserved-C-best-v9e-001'
OUTPUT = R / 'identity-invariance-001'
DECLARATION = E / 'identity-invariance-001.json'
ANALYSIS = E / 'analysis/identity_invariance'
EXPECTED_SHA = '70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87'


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def transform(observation, swap=False):
    out = deepcopy(observation)
    for player in out['players']:
        player['name'] = 'anonymous'
    if swap:
        out['players'].reverse()
        out['player'] = 1-out['player']
    return out


def declare():
    assert sha('bot_research/bots/best.py') == EXPECTED_SHA
    jobs = json.loads((CAMPAIGN/'jobs.json').read_text())
    assert len(jobs) == 72 and len({j['id'] for j in jobs}) == 72
    paths = set(static_closure({
        'bot_research.bots.best',
        'bot_research.experiments.validation.relabel_validation',
        'bot_research.experiments.validation.replay_audit',
        'bot_research.bots.counters.visible_search',
    }))
    paths.update((CAMPAIGN/'jobs.json', CAMPAIGN/'freeze.json',
                  Path('td_game/balanced.json'), ANALYSIS/'PROOF.md'))
    for job in jobs:
        paths.update((CAMPAIGN/'jobs'/(job['id']+'.json'),
                      CAMPAIGN/'results'/(job['id']+'.json'), Path(job['replay_path'])))
    sources = {str(path): sha(path) for path in sorted(paths)}
    fixture = {'player':0, 'players':[{'name':'A','gold':10}, {'name':'B','gold':30}],
               'round':7,'rules':{'some':'rule'}}
    unchanged = deepcopy(fixture)
    assert transform(transform(fixture, True), True) == transform(fixture)
    assert transform(fixture, True)['players'][1]['gold'] == 10
    assert fixture == unchanged
    declaration = dict(time_utc=now(), candidate='bot_research.bots.best:@make',
        candidate_sha256=EXPECTED_SHA, campaign=str(CAMPAIGN), output=str(OUTPUT),
        expected_cases=72, transformations=['anonymous_names','anonymous_names_and_swap'],
        source_and_input_sha256=sources, jobs=[j['id'] for j in jobs],
        actual_candidate_calls_before_declaration=0,
        scope='Finite robustness audit of retained selection histories; no new games or strength samples.',
        fixture_checks_passed=True)
    atomic_json(DECLARATION, declaration, exclusive=True)
    OUTPUT.mkdir(exist_ok=False)
    for child in ('cases','failures','logs'):
        (OUTPUT/child).mkdir()
    print(json.dumps({'declaration':str(DECLARATION),'pins':len(sources),'time_utc':now()}),flush=True)


def verify():
    declaration = json.loads(DECLARATION.read_text())
    for path, expected in declaration['source_and_input_sha256'].items():
        assert sha(path) == expected, path
    return declaration


def case(identifier):
    begin = time.perf_counter()
    declaration = verify()
    assert identifier in declaration['jobs']
    from bot_research.bots import best
    from bot_research.bots.counters.visible_search import player_from_snapshot
    from bot_research.experiments.validation.replay_audit import normalized
    from td_game.actions import apply_action
    from td_game.config import balanced_config
    from td_game.engine import Engine
    job = json.loads((CAMPAIGN/'jobs'/(identifier+'.json')).read_text())
    row = json.loads((CAMPAIGN/'results'/(identifier+'.json')).read_text())
    records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
    side = job['condition']['candidate_side']
    cfg = balanced_config()
    engine = Engine(cfg,tuple(row['bot_specs']))
    assert normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2]
    prefix = job.get('prefixes',[[],[]])[side]
    functions = [best.make(), best.make()]
    calls = [0,0]
    differences = []
    rounds = []
    for rnd in range(1,row['rounds']+1):
        pair = records[2*rnd:2*rnd+2]
        actions = [[event['action'] for event in rec['event'] if event['kind']=='action'] for rec in pair]
        observation = engine.observation(side)
        assert transform(transform(observation, True), True) == transform(observation)
        checks = []
        times = []
        for i, function in enumerate(functions):
            if rnd <= len(prefix):
                fresh = deepcopy(prefix[rnd-1])
                duration = 0.0
            else:
                argument = transform(observation, bool(i))
                before = deepcopy(argument)
                own_state = deepcopy(observation['players'][side]); own_state['name']='anonymous'
                assert argument['players'][argument['player']] == own_state
                start = time.perf_counter()
                fresh = json.loads(json.dumps(function(argument), allow_nan=False))
                duration = time.perf_counter()-start
                calls[i] += 1
                assert argument == before, ('observation_mutation',rnd,i)
                own = player_from_snapshot(before['players'][before['player']])
                assert isinstance(fresh,list)
                assert all(apply_action(own,a,rnd,cfg)['accepted'] for a in fresh), ('illegal_action',rnd,i)
            matched = fresh == actions[side]
            checks.append(matched)
            times.append(duration)
            if not matched:
                differences.append(dict(round=rnd,transformation=declaration['transformations'][i],
                                        expected=actions[side],actual=fresh))
        rounds.append(dict(round=rnd,policy_invoked=rnd>len(prefix),matches=checks,seconds=times))
        assert normalized(engine.play_round(actions)) == pair, ('original_engine_replay',rnd)
    assert engine.result == row['result']
    verify()
    result = dict(time_utc=now(), job=identifier, candidate_sha256=EXPECTED_SHA,
        declaration_sha256=sha(DECLARATION), condition=job['condition'],
        original_rounds=row['rounds'], skipped_prefix_rounds=len(prefix),
        actual_policy_calls=calls, transformations=declaration['transformations'],
        original_engine_replay_passed=True, observations_unchanged=True,
        generated_actions_legal=True, differences=differences, rounds=rounds,
        all_passed=not differences, elapsed_seconds=time.perf_counter()-begin)
    atomic_json(OUTPUT/'cases'/(identifier+'.json'),result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('job','all_passed','actual_policy_calls','elapsed_seconds')}),flush=True)


def run(shard, shards):
    declaration = verify()
    assert 0 <= shard < shards
    selected = [j for i,j in enumerate(declaration['jobs']) if i%shards==shard]
    for identifier in selected:
        target = OUTPUT/'cases'/(identifier+'.json')
        failure = OUTPUT/'failures'/(identifier+'.json')
        if target.exists() or failure.exists():
            continue
        verify()
        command = ['.venv/bin/python','-B','-m',
                   'bot_research.experiments.validation.relabel_validation','case','--job',identifier]
        try:
            process = subprocess.run(command,capture_output=True,text=True,timeout=300)
            text = public_diagnostic(process.stdout+process.stderr)
            (OUTPUT/'logs'/(identifier+'.log')).write_text(text)
            if process.returncode:
                atomic_json(failure,dict(time_utc=now(),job=identifier,
                    returncode=process.returncode,diagnostic=text[-12000:]),exclusive=True)
        except subprocess.TimeoutExpired:
            atomic_json(failure,dict(time_utc=now(),job=identifier,timeout_seconds=300),exclusive=True)
        print(json.dumps({'time_utc':now(),'job':identifier,'completed':target.exists(),
                          'failed':failure.exists()}),flush=True)
    print(json.dumps({'time_utc':now(),'shard_complete':shard,'planned':len(selected)}),flush=True)


def publish():
    declaration = verify()
    cases = []
    failures = []
    for identifier in declaration['jobs']:
        target = OUTPUT/'cases'/(identifier+'.json')
        failure = OUTPUT/'failures'/(identifier+'.json')
        if failure.exists():
            failures.append(json.loads(failure.read_text()))
        assert target.exists() or failure.exists(), identifier
        if target.exists():
            result = json.loads(target.read_text())
            assert result['job']==identifier and result['declaration_sha256']==sha(DECLARATION)
            cases.append(result)
    complete = len(cases)==declaration['expected_cases'] and not failures
    passed = complete and all(case['all_passed'] for case in cases)
    calls = [sum(case['actual_policy_calls'][i] for case in cases) for i in (0,1)]
    prefix = sum(case['skipped_prefix_rounds'] for case in cases)
    summary = dict(time_utc=now(), declaration_sha256=sha(DECLARATION),
        candidate_sha256=EXPECTED_SHA, expected_cases=72, completed_cases=len(cases),
        failed_attempts=failures, differences=sum(len(c['differences']) for c in cases),
        actual_policy_calls_by_transformation=calls, actual_policy_calls_total=sum(calls),
        skipped_prefix_rounds_per_transformation=prefix, all_passed=passed,
        case_sha256={str(OUTPUT/'cases'/(c['job']+'.json')):sha(OUTPUT/'cases'/(c['job']+'.json')) for c in cases},
        scope=declaration['scope'])
    atomic_json(ANALYSIS/'verification/full_check.json',summary,exclusive=True)
    verdict='CONFIRMED' if passed else ('REFUTED' if summary['differences'] else 'OPEN')
    text=f'''# Finite public-label and player-index check\n\nCompleted {summary['time_utc']}. Verdict: **{verdict}**.\n\nThe declared {len(cases)} of 72 C histories yielded {summary['differences']} action differences and {len(failures)} failed attempts. There were {calls[0]} actual candidate calls with both public names replaced by `anonymous`, and {calls[1]} calls with that replacement plus a swap of the player snapshots and observer index. The {prefix} prescribed prefix rounds per transformation were skipped, not counted as policy calls. Every completed case independently replayed its retained game through the original engine, checked observation preservation and checked generated action legality.\n\nThis checks metadata transformations of the selected best_v9e on retained selection histories. It adds no games, no W/D/L results and no independent strength evidence. Passing does not prove name independence on all reachable states or remove the engine's public identity information. See PROOF.md for the exact finite assertion and verification/full_check.json for source-bound evidence.\n'''
    with (ANALYSIS/'RESULTS.md').open('x') as file:
        file.write(text)
    with Path('bot_research/notes/validation.md').open('a') as file:
        file.write(f'''\n## {now()} Public labels and player indices on the frozen candidate\n\nClaim: anonymizing names, with or without swapping player indices, preserves the selected candidate's decisions on the complete 72-history retained C corpus.\n\nMethod: predeclared source/input hashes; two fresh factory instances in a fresh process per history; every retained round replayed through the unchanged Engine; prescribed prefixes skipped.\n\nResult: {len(cases)}/72 cases completed, {summary['differences']} differences, {len(failures)} failures, {calls[0]} + {calls[1]} actual policy calls. Evidence: experiments/validation/analysis/identity_invariance/RESULTS.md and verification/full_check.json.\n\nVerdict: {verdict} for this finite invariance assertion only. This is an audit of selected C histories, not new strength evidence or a theorem about every possible observation. No D condition was played.\n''')
    print(json.dumps({k:summary[k] for k in ('time_utc','completed_cases','differences','actual_policy_calls_total','all_passed')}),flush=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['declare','case','run','publish'])
    parser.add_argument('--job')
    parser.add_argument('--shard',type=int,default=0)
    parser.add_argument('--shards',type=int,default=1)
    args=parser.parse_args()
    if args.mode=='declare':declare()
    elif args.mode=='case':case(args.job)
    elif args.mode=='run':run(args.shard,args.shards)
    else:publish()


if __name__=='__main__':
    main()

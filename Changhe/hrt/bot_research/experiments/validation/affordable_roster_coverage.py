"""Exhaustive fixed-round purchase checks on retained small-budget histories."""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import time

from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.source_closure import static_closure

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
CAMPAIGN = R/'reserved-C-best-v9e-001'
OUTPUT = R/'affordable-roster-coverage-001'
DECLARATION = E/'affordable-roster-coverage-001.json'
ANALYSIS = E/'analysis/affordable_roster_coverage'
EXPECTED_SHA = '70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87'


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def enumerate_rosters(budget, costs, prefix=()):
    yield prefix
    for tier, cost in sorted(costs.items()):
        if cost <= budget:
            yield from enumerate_rosters(budget-cost, costs, prefix+(tier,))


def declare():
    from td_game.config import balanced_config
    assert sha('bot_research/bots/best.py') == EXPECTED_SHA
    jobs = json.loads((CAMPAIGN/'jobs.json').read_text())
    jobs = [job for job in jobs if job['id'].startswith('standard-')]
    assert len(jobs) == 24 and len({j['id'] for j in jobs}) == 24
    costs = {t:m.cost for t,m in balanced_config().minions.items()}
    sequences = list(enumerate_rosters(250, costs))
    assert len(sequences) == len(set(sequences)) == 2166
    assert all(sum(costs[t] for t in seq) <= 250 for seq in sequences)
    paths = set(static_closure({
        'bot_research.experiments.validation.affordable_roster_coverage',
        'bot_research.experiments.validation.replay_audit',
        'bot_research.bots.defense.frozen.v7.plan',
        'bot_research.harness.gamekit',
        'td_game.engine',
    }))
    paths.update((Path('bot_research/bots/best.py'), CAMPAIGN/'jobs.json', CAMPAIGN/'freeze.json',
                  Path('td_game/balanced.json'), ANALYSIS/'PROOF.md',
                  E/'identity-invariance-001.json',
                  E/'analysis/identity_invariance/verification/full_check.json'))
    for job in jobs:
        paths.update((CAMPAIGN/'jobs'/(job['id']+'.json'),
                      CAMPAIGN/'results'/(job['id']+'.json'), Path(job['replay_path'])))
    sources = {str(path):sha(path) for path in sorted(paths)}
    declaration = dict(time_utc=now(), candidate_sha256=EXPECTED_SHA,
        campaign=str(CAMPAIGN), output=str(OUTPUT), expected_jobs=24,
        rounds=[2,3,4,5,6], maximum_eligible_gold=250, enumeration_count_at_limit=2166,
        jobs=[job['id'] for job in jobs], source_and_input_sha256=sources,
        prior_policy_calls=0, prior_interventions=0,
        scope='Post-selection fixed-round diagnosis on retained C histories. No new games or policy calls.')
    atomic_json(DECLARATION,declaration,exclusive=True)
    OUTPUT.mkdir(exist_ok=False)
    for child in ('cases','failures','logs','enumerations','witnesses'):
        (OUTPUT/child).mkdir()
    with Path('bot_research/notes/validation.md').open('a') as file:
        file.write(f'''\n## {now()} Exact affordable-roster coverage declared\n\nClaim: H1 the sampled purchase lists attain worst incoming damage, and H2 zero sampled damage implies zero damage for every affordable ordered purchase, on all reached rounds2-6 of the24standard C histories with opponent gold at most250. Both OPEN. Method: enumerate every legal ordered purchase list with the entire actual budget, retain the candidate action list, and execute every intervention through the unchanged Engine. Source/input pins precede all interventions. This is component diagnosis of selected histories, no new policy calls or strength games. See experiments/validation/analysis/affordable_roster_coverage/PROOF.md.\n''')
    print(json.dumps({'time_utc':now(),'declaration':str(DECLARATION),'pins':len(sources),'jobs':len(jobs)}),flush=True)


def verify():
    declaration = json.loads(DECLARATION.read_text())
    for path, expected in declaration['source_and_input_sha256'].items():
        assert sha(path) == expected, path
    return declaration


def incoming(record):
    return next(event['base_damage'] for event in record['event'] if event['kind']=='combat')


def case(identifier):
    begin=time.perf_counter()
    declaration=verify()
    assert identifier in declaration['jobs']
    from bot_research.bots.defense.frozen.v7.plan import affordable_bundles
    from bot_research.harness.gamekit import Rules
    from bot_research.experiments.validation.replay_audit import normalized
    from td_game.config import balanced_config
    from td_game.engine import Engine
    job=json.loads((CAMPAIGN/'jobs'/(identifier+'.json')).read_text())
    row=json.loads((CAMPAIGN/'results'/(identifier+'.json')).read_text())
    records=[json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
    side=job['condition']['candidate_side']
    cfg=balanced_config()
    engine=Engine(cfg,tuple(row['bot_specs']))
    assert normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2]
    assert not any(job.get('prefixes',[[],[]]))
    costs={t:m.cost for t,m in cfg.minions.items()}
    @lru_cache(None)
    def count(budget):
        return 1+sum(count(budget-cost) for cost in costs.values() if cost<=budget)
    states=[]
    tested=0
    for rnd in range(1,row['rounds']+1):
        pair=records[2*rnd:2*rnd+2]
        actions=[[e['action'] for e in rec['event'] if e['kind']=='action'] for rec in pair]
        obs=engine.observation(side)
        gold=obs['players'][1-side]['gold']
        if rnd in declaration['rounds'] and gold<=declaration['maximum_eligible_gold']:
            rules=Rules.from_observation(obs)
            sampled=affordable_bundles(gold,rules) or [[]]
            sampled_tuples=[tuple(x) for x in sampled]
            enumeration=OUTPUT/'enumerations'/f'{identifier}-r{rnd}.jsonl.gz'
            values={}
            maximum=-1
            witness=None
            witness_key=None
            witness_round=None
            digest=hashlib.sha256()
            with gzip.open(enumeration,'xt',encoding='utf-8') as file:
                for seq in enumerate_rosters(gold,costs):
                    assert seq not in values
                    cost=sum(costs[t] for t in seq)
                    assert cost<=gold
                    probe=deepcopy(engine)
                    submissions=deepcopy(actions)
                    submissions[1-side]=[{'op':'buy_minion','type':t} for t in seq]
                    changed=probe.play_round(submissions)
                    assert all(e['accepted'] for rec in changed for e in rec['event'] if e['kind']=='action')
                    damage=incoming(changed[side])
                    values[seq]=damage
                    entry={'purchase':seq,'cost':cost,'damage':damage}
                    encoded=json.dumps(entry,sort_keys=True,separators=(',',':'))+'\n'
                    file.write(encoded);digest.update(encoded.encode())
                    key=(cost,len(seq),seq)
                    if damage>maximum or (damage==maximum and key<witness_key):
                        maximum=damage;witness=seq;witness_key=key;witness_round=changed
            assert len(values)==count(gold)
            assert all(seq in values for seq in sampled_tuples)
            sample_max=max(values[seq] for seq in sampled_tuples)
            assert maximum>=sample_max
            witness_path=None
            if maximum>sample_max:
                witness_path=OUTPUT/'witnesses'/f'{identifier}-r{rnd}.jsonl'
                with witness_path.open('x') as file:
                    for rec in records[:2*rnd]+normalized(witness_round):
                        file.write(json.dumps(rec,sort_keys=True)+'\n')
            state=dict(round=rnd,opponent_gold=gold,enumerated=len(values),
                sampled=[{'purchase':seq,'damage':values[seq]} for seq in sampled_tuples],
                sampled_max_damage=sample_max,exact_max_damage=maximum,
                maximizing_purchase=witness,maximizing_cost=witness_key[0],
                h1_passed=maximum==sample_max,h2_applicable=sample_max==0,
                h2_passed=sample_max!=0 or maximum==0,
                enumeration=str(enumeration),enumeration_sha256=sha(enumeration),
                enumeration_content_sha256=digest.hexdigest(),
                witness_replay=None if witness_path is None else str(witness_path),
                witness_replay_sha256=None if witness_path is None else sha(witness_path))
            states.append(state);tested+=len(values)
            print(json.dumps({'time_utc':now(),'job':identifier,**{k:state[k] for k in
                ('round','opponent_gold','enumerated','sampled_max_damage','exact_max_damage')}}),flush=True)
        assert normalized(engine.play_round(actions)) == pair, ('original_engine_replay',rnd)
    assert engine.result == row['result']
    verify()
    result=dict(time_utc=now(),job=identifier,candidate_side=side,
        declaration_sha256=sha(DECLARATION),eligible_states=len(states),
        original_rounds=row['rounds'],original_engine_replay_passed=True,
        interventions=tested,policy_calls=0,states=states,
        elapsed_seconds=time.perf_counter()-begin,
        h1_passed=all(s['h1_passed'] for s in states),
        h2_passed=all(s['h2_passed'] for s in states))
    atomic_json(OUTPUT/'cases'/(identifier+'.json'),result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('job','eligible_states','interventions','h1_passed','h2_passed','elapsed_seconds')}),flush=True)


def run(shard,shards):
    declaration=verify()
    assert 0<=shard<shards
    for index,identifier in enumerate(declaration['jobs']):
        if index%shards!=shard:continue
        target=OUTPUT/'cases'/(identifier+'.json')
        failure=OUTPUT/'failures'/(identifier+'.json')
        if target.exists() or failure.exists():continue
        verify()
        command=['.venv/bin/python','-B','-m',
            'bot_research.experiments.validation.affordable_roster_coverage','case','--job',identifier]
        try:
            child=subprocess.run(command,capture_output=True,text=True,timeout=500)
            text=public_diagnostic(child.stdout+child.stderr)
            (OUTPUT/'logs'/(identifier+'.log')).write_text(text)
            if child.returncode:
                atomic_json(failure,dict(time_utc=now(),job=identifier,returncode=child.returncode,
                    diagnostic=text[-12000:]),exclusive=True)
        except subprocess.TimeoutExpired:
            atomic_json(failure,dict(time_utc=now(),job=identifier,timeout_seconds=500),exclusive=True)
        print(json.dumps({'time_utc':now(),'job':identifier,'completed':target.exists(),
                          'failed':failure.exists()}),flush=True)
    print(json.dumps({'time_utc':now(),'shard_complete':shard}),flush=True)


def publish():
    declaration=verify()
    cases=[];failures=[]
    for identifier in declaration['jobs']:
        target=OUTPUT/'cases'/(identifier+'.json');failure=OUTPUT/'failures'/(identifier+'.json')
        assert target.exists() or failure.exists(),identifier
        if failure.exists():failures.append(json.loads(failure.read_text()))
        if target.exists():
            case=json.loads(target.read_text());assert case['declaration_sha256']==sha(DECLARATION)
            for state in case['states']:
                assert sha(state['enumeration'])==state['enumeration_sha256']
                if state['witness_replay']:
                    assert sha(state['witness_replay'])==state['witness_replay_sha256']
            cases.append(case)
    states=[dict(job=c['job'],candidate_side=c['candidate_side'],**s) for c in cases for s in c['states']]
    complete=len(cases)==24 and not failures
    counterexamples=[s for s in states if not s['h1_passed']]
    zero_states=[s for s in states if s['h2_applicable']]
    zero_counterexamples=[s for s in zero_states if not s['h2_passed']]
    h1='REFUTED' if counterexamples else ('CONFIRMED' if complete and states else 'OPEN')
    h2='REFUTED' if zero_counterexamples else ('CONFIRMED' if complete and zero_states else 'OPEN')
    summary=dict(time_utc=now(),declaration_sha256=sha(DECLARATION),complete=complete,
        expected_jobs=24,completed_jobs=len(cases),failed_attempts=failures,
        eligible_states=len(states),zero_sample_states=len(zero_states),
        interventions=sum(c['interventions'] for c in cases),policy_calls=0,
        h1_verdict=h1,h2_verdict=h2,h1_counterexamples=counterexamples,
        h2_counterexamples=zero_counterexamples,
        by_candidate_side={str(side):{'states':sum(s['candidate_side']==side for s in states),
            'interventions':sum(s['enumerated'] for s in states if s['candidate_side']==side)} for side in (0,1)},
        case_sha256={str(OUTPUT/'cases'/(c['job']+'.json')):sha(OUTPUT/'cases'/(c['job']+'.json')) for c in cases},
        scope=declaration['scope'])
    atomic_json(ANALYSIS/'verification/full_check.json',summary,exclusive=True)
    text=f'''# Exact affordable-roster coverage results\n\nCompleted {summary['time_utc']}. H1: **{h1}**. H2: **{h2}**.\n\nAll {len(cases)} of 24 retained standard C histories have completed checks; failed attempts: {len(failures)}. The declared selection rule yields {len(states)} eligible reached states, including {len(zero_states)} with zero damage against every sampled purchase. The original Engine executed {summary['interventions']} fixed-round interventions, enumerating every ordered purchase affordable with the actual opponent budget. It also independently replayed every original history. No policy was called and no new full strength game was run.\n\nThere are {len(counterexamples)} states where the exact damage maximum exceeds the sampled maximum, and {len(zero_counterexamples)} states where a defense stops every sampled list but an affordable omitted list causes damage. Each such state has its maximizing purchase and full original-engine witness replay recorded in verification/full_check.json. All purchase rows, including failures of the hypotheses, are retained in compressed enumeration files under runs/validation/affordable-roster-coverage-001.\n\nThis is a post-selection component statement about the specified small-budget early states. It gives no general bound for larger budgets or later states and no complete-policy strength guarantee. See PROOF.md for exact objects and the exhaustive-enumeration argument.\n'''
    with (ANALYSIS/'RESULTS.md').open('x') as file:file.write(text)
    with Path('bot_research/notes/validation.md').open('a') as file:
        file.write(f'''\n## {now()} Exact affordable-roster coverage complete\n\nClaim: H1 sampled purchase lists attain the true fixed-round maximum; H2 zero sampled damage implies zero exhaustive damage, on the declared reached states only. Method: all affordable ordered purchases at actual gold at most250, rounds2-6 of24retained standard C histories, original Engine for every intervention and full original replay. Result: {len(states)}states, {len(zero_states)}zero-sample states, {summary['interventions']}interventions, {len(counterexamples)}H1counterexamples, {len(zero_counterexamples)}H2counterexamples, {len(failures)}failures. Verdict: H1{h1}, H2{h2}. Evidence: experiments/validation/analysis/affordable_roster_coverage/RESULTS.md and verification/full_check.json. No new policy calls or full strength games. D remains unplayed.\n''')
    print(json.dumps({k:summary[k] for k in ('time_utc','complete','eligible_states','interventions','h1_verdict','h2_verdict')}),flush=True)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=('declare','case','run','publish'))
    parser.add_argument('--job');parser.add_argument('--shard',type=int,default=0);parser.add_argument('--shards',type=int,default=1)
    args=parser.parse_args()
    if args.mode=='declare':declare()
    elif args.mode=='case':case(args.job)
    elif args.mode=='run':run(args.shard,args.shards)
    else:publish()


if __name__=='__main__':main()

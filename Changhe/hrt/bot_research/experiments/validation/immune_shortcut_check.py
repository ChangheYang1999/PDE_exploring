"""Fresh state/action and original-engine audit of the native immune shortcut."""
from __future__ import annotations
import argparse
from copy import deepcopy
from dataclasses import fields, is_dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import time
from types import FunctionType
from bot_research.bots.counters.immune_runtime_shortcut import make as shortcut_make
from bot_research.experiments.lead.frozen.best_v9e import make as parent_make
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation import execution_context
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine

E = Path('bot_research/experiments/validation')
A = E/'analysis/immune_runtime_shortcut'
D = E/'immune-shortcut-001.json'
R = Path('bot_research/runs/validation/immune-shortcut-001')
C = Path('bot_research/runs/validation/reserved-C-best-v9e-001')
H = E/'analysis/visible_gold_runtime/sources'
EXPECTED = '70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87'


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def freeze(value):
    """Canonical complete values of the observed policy fields and closures."""
    if value is None or isinstance(value, (bool, int, float, str)):
        return (type(value).__name__, value)
    if isinstance(value, dict):
        return ('dict', tuple(sorted(((freeze(k), freeze(v)) for k, v in value.items()), key=repr)))
    if isinstance(value, (list, tuple)):
        return (type(value).__name__, tuple(freeze(v) for v in value))
    if isinstance(value, (set, frozenset)):
        return (type(value).__name__, tuple(sorted((freeze(v) for v in value), key=repr)))
    if is_dataclass(value):
        return ('dataclass', type(value).__module__, type(value).__qualname__,
                tuple((f.name, freeze(getattr(value, f.name))) for f in fields(value)))
    if isinstance(value, FunctionType):
        return ('function', value.__module__, value.__qualname__,
                tuple((name, freeze(cell.cell_contents))
                      for name, cell in zip(value.__code__.co_freevars, value.__closure__ or ())),
                freeze(value.__defaults__), freeze(value.__kwdefaults__), freeze(vars(value)))
    raise TypeError(f'unhandled persistent value type {type(value).__module__}.{type(value).__qualname__}')


def verify():
    d = json.loads(D.read_text())
    for p, expected in d['input_sha256'].items():
        assert sha(p) == expected, p
    return d


def declare():
    assert sha('bot_research/bots/best.py') == EXPECTED
    cases = []
    paths = set(static_closure({'bot_research.experiments.validation.immune_shortcut_check'}))
    paths.update([A/'PROOF.md', A/'PROOF_INITIAL.md', Path('td_game/balanced.json'),
                  Path('configs/balanced.json'), C/'jobs.json', C/'freeze.json',
                  E/'visible-gold-runtime-001.json', E/'visible-gold-runtime-amendment-001.json'])
    for side in (0, 1):
        record, replay = H/f'seat{side}-result.json', H/f'seat{side}.jsonl'
        cases.append(dict(id=f'high-{side}', kind='high_factory', side=side,
                          record=str(record), replay=str(replay)))
        paths.update([record, replay])
    jobs = json.loads((C/'jobs.json').read_text())
    assert len(jobs) == 72
    calls, prefixes = 100, 0
    for job in jobs:
        record, jobpath = C/'results'/(job['id']+'.json'), C/'jobs'/(job['id']+'.json')
        row = json.loads(record.read_text())
        j = json.loads(jobpath.read_text())
        side = j['condition']['candidate_side']
        prefix = len(j.get('prefixes', [[], []])[side])
        calls += row['rounds']-prefix
        prefixes += prefix
        cases.append(dict(id='C-'+job['id'], kind='selected_C', side=side,
                          record=str(record), job=str(jobpath), replay=row['replay_path']))
        paths.update([record, jobpath, Path(row['replay_path'])])
    assert calls == 1204 and prefixes == 120 and len(cases) == 74
    # Checker fixtures have no policy calls.
    def factory(n):
        state = {'x': n, 's': {1, 2}}
        def function():
            return state
        return function
    assert freeze(factory(1)) == freeze(factory(1))
    assert freeze(factory(1)) != freeze(factory(2))
    assert freeze({'a': 1, 'b': 2}) == freeze({'b': 2, 'a': 1})
    assert freeze([1, 2]) != freeze((1, 2))
    for name in ('cases', 'failures', 'logs'):
        (R/name).mkdir(parents=True, exist_ok=False)
    atomic_json(D, dict(time_utc=now(), cases=cases, candidate_sha256=EXPECTED,
        expected_calls_per_implementation=calls, expected_skipped_prefixes_per_implementation=prefixes,
        input_sha256={str(p): sha(p) for p in sorted(paths)}, shortcut_calls_before_declaration=0,
        hypotheses=['H1 exact actions and complete legitimate persistent state at all actual calls',
                    'H2 at least one shortcut call', 'H3 high-factory shortcut maximum process CPU below 3 seconds'],
        state_scope='Instance fields, recursively including dataclasses and function closures; shared module caches excluded.',
        call_order='Parent first on odd rounds, shortcut first on even rounds; shared process caches.',
        scope='74 reused development histories, no new games or held-out samples.',
        checker_fixtures_passed=True), exclusive=True)
    print(json.dumps(dict(time_utc=now(), cases=74, pins=len(paths), calls_per_implementation=calls)), flush=True)


def case(identifier):
    begin = time.perf_counter()
    d = verify()
    entry = next(c for c in d['cases'] if c['id'] == identifier)
    row = json.loads(Path(entry['record']).read_text())
    records = [json.loads(s) for s in Path(entry['replay']).read_text().splitlines()]
    cfg = balanced_config()
    side = entry['side']
    if entry['kind'] == 'high_factory':
        names = tuple(r['snapshot']['name'] for r in records[:2])
        engine = Engine(cfg, names)
        initial = normalized(engine.initial_records(names))
        extra = dict(research_specs=[row['spec_a'], row['spec_b']],
                     research_scenario=row['scenario'], research_metadata=row['metadata'])
        for record in initial:
            record['match'].update(extra)
        assert initial == records[:2]
        prefix = []
    else:
        job = json.loads(Path(entry['job']).read_text())
        names = tuple(row['bot_specs'])
        engine = Engine(cfg, names)
        assert normalized(engine.initial_records(names)) == records[:2]
        prefix = job.get('prefixes', [[], []])[side]
    policies = [parent_make(), shortcut_make()]
    assert freeze(vars(policies[0])) == freeze(vars(policies[1]))
    measurements, differences = [], []
    for rnd in range(1, row['rounds']+1):
        pair = records[2*rnd:2*rnd+2]
        actions = [[e['action'] for e in rec['event'] if e['kind'] == 'action'] for rec in pair]
        assert not any(e['kind'] == 'bot_error' or (e['kind'] == 'action' and not e['accepted'])
                       for rec in pair for e in rec['event'])
        if rnd <= len(prefix):
            assert prefix[rnd-1] == actions[side]
        else:
            obs = engine.observation(side)
            me = obs['players'][side]
            native = policies[1].alt is None and not (
                {(b['x'], b['y']) for b in me['buildings']} - policies[1].requested)
            fast = native and policies[1].eligible(obs)
            proposed = [None, None]
            times = [None, None]
            for i in ([0, 1] if rnd % 2 else [1, 0]):
                argument = deepcopy(obs)
                saved = deepcopy(argument)
                w, c = time.perf_counter(), time.process_time()
                proposed[i] = policies[i](argument)
                cpu, wall = time.process_time()-c, time.perf_counter()-w
                proposed[i] = json.loads(json.dumps(proposed[i], allow_nan=False))
                assert argument == saved, ('observation_mutation', rnd, i)
                own = player_from_snapshot(saved['players'][side])
                assert all(apply_action(own, a, rnd, cfg)['accepted'] for a in proposed[i]), ('illegal', rnd, i)
                times[i] = dict(wall_seconds=wall, cpu_seconds=cpu)
            action_match = proposed[0] == proposed[1] == actions[side]
            state_match = freeze(vars(policies[0])) == freeze(vars(policies[1]))
            if not action_match or not state_match:
                differences.append(dict(round=rnd, action_match=action_match, state_match=state_match,
                                        actions=proposed, expected=actions[side]))
            measurements.append(dict(round=rnd, native=native, shortcut=fast,
                                     action_match=action_match, state_match=state_match, times=times,
                                     action_count=[len(p) for p in proposed]))
        assert normalized(engine.play_round(actions)) == pair, ('engine_replay', rnd)
    if entry['kind'] == 'high_factory':
        assert [p.hp for p in engine.players] == [row['hp_a'], row['hp_b']]
        assert engine.result['winner'] == row['winner'] and engine.result['reason'] == row['reason']
    else:
        assert engine.result == row['result']
    verify()
    result = dict(time_utc=now(), id=identifier, kind=entry['kind'], side=side,
        all_passed=not differences, differences=differences, calls_per_implementation=len(measurements),
        skipped_prefixes_per_implementation=len(prefix), rounds=measurements,
        original_engine_replayed=True, observations_unchanged=True, generated_actions_legal=True,
        declaration_sha256=sha(D), execution=execution_context(),
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        elapsed_seconds=time.perf_counter()-begin)
    atomic_json(R/'cases'/(identifier+'.json'), result, exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','id','all_passed','calls_per_implementation','elapsed_seconds')}), flush=True)


def run(shard, shards):
    d = verify()
    assert 0 <= shard < shards
    for idx, entry in enumerate(d['cases']):
        if idx % shards != shard:
            continue
        name = entry['id']
        target, failure = R/'cases'/(name+'.json'), R/'failures'/(name+'.json')
        if target.exists() or failure.exists():
            continue
        verify()
        command = ['.venv/bin/python','-B','-m','bot_research.experiments.validation.immune_shortcut_check',
                   'case','--id',name]
        try:
            child = subprocess.run(command, capture_output=True, text=True, timeout=300)
            text = public_diagnostic(child.stdout+child.stderr)
            (R/'logs'/(name+'.log')).write_text(text)
            if child.returncode:
                atomic_json(failure, dict(time_utc=now(), id=name, returncode=child.returncode,
                                          diagnostic=text[-10000:]), exclusive=True)
        except subprocess.TimeoutExpired:
            atomic_json(failure, dict(time_utc=now(), id=name, timeout_seconds=300), exclusive=True)
        print(json.dumps(dict(time_utc=now(), id=name, completed=target.exists(), failed=failure.exists())), flush=True)
    print(json.dumps(dict(time_utc=now(), shard_complete=shard)), flush=True)


def publish():
    d = verify()
    failures = []
    cases = []
    for entry in d['cases']:
        p, f = R/'cases'/(entry['id']+'.json'), R/'failures'/(entry['id']+'.json')
        assert p.exists() or f.exists(), entry['id']
        if f.exists():
            failures.append(json.loads(f.read_text()))
        if p.exists():
            value = json.loads(p.read_text())
            assert value['id'] == entry['id'] and value['declaration_sha256'] == sha(D)
            cases.append(value)
    h1 = len(cases) == 74 and not failures and all(c['all_passed'] for c in cases)
    measured = [(case, rnd) for case in cases for rnd in case['rounds']]
    high = [(c, r) for c, r in measured if c['kind'] == 'high_factory']
    fast_calls = sum(r['shortcut'] for _, r in measured)
    foreign_calls = sum(not r['native'] for _, r in measured)
    totals = [{key:sum(r['times'][i][key] for _, r in measured)
               for key in ('wall_seconds','cpu_seconds')} for i in (0, 1)]
    maxima = []
    for i in (0, 1):
        maxima.append({key:dict(id=c['id'], round=r['round'], value=r['times'][i][key])
                       for key in ('wall_seconds','cpu_seconds')
                       for c, r in [max(high, key=lambda cr:cr[1]['times'][i][key])]} if high else {})
    h2 = fast_calls > 0
    h3 = len([c for c in cases if c['kind']=='high_factory']) == 2 and maxima[1]['cpu_seconds']['value'] < 3
    calls = sum(c['calls_per_implementation'] for c in cases)
    skipped = sum(c['skipped_prefixes_per_implementation'] for c in cases)
    if h1:
        assert calls == d['expected_calls_per_implementation'] and skipped == d['expected_skipped_prefixes_per_implementation']
    result = dict(time_utc=now(), h1=h1, h2=h2, h3=h3, all_passed=h1 and h2 and h3,
        completed_cases=len(cases), failures=failures, calls_per_implementation=calls,
        total_actual_calls=2*calls, skipped_prefixes_per_implementation=skipped,
        shortcut_calls=fast_calls, foreign_calls_per_implementation=foreign_calls,
        totals=totals, high_factory_maxima=maxima,
        differences=sum(len(c['differences']) for c in cases), new_games=0,
        input_sha256={str(D):sha(D), **{str(R/'cases'/(c['id']+'.json')):sha(R/'cases'/(c['id']+'.json')) for c in cases}})
    atomic_json(A/'verification/full_check.json', result, exclusive=True)
    lines = ['# Immune shortcut: finite action and state check', '', f'Completed {result["time_utc"]}.', '',
        f'H1 **{"CONFIRMED" if h1 else "OPEN"}**: {len(cases)}/74 retained histories completed; '
        f'{result["differences"]} differences and {len(failures)} failed attempts. '
        f'There were {calls} fresh calls per implementation ({2*calls} total), '
        f'with {skipped} prescribed prefix turns skipped per implementation.', '',
        f'H2 **{"CONFIRMED" if h2 else "REFUTED"}**: {fast_calls} calls used the shortcut. '
        f'{foreign_calls} calls per implementation entered the unchanged foreign path.', '',
        f'H3 **{"CONFIRMED" if h3 else "REFUTED"}**: both high-factory histories completed and '
        'the shortcut maximum process CPU time was below3 seconds.' if h3 else 'H3 did not pass.', '',
        '| Implementation | High-factory max wall s | High-factory max CPU s | All-call wall total s | All-call CPU total s |',
        '| --- | ---: | ---: | ---: | ---: |']
    for i, name in enumerate(('Unchanged parent', 'Research shortcut')):
        if maxima[i]:
            lines.append(f'| {name} | {maxima[i]["wall_seconds"]["value"]:.6f} | '
                         f'{maxima[i]["cpu_seconds"]["value"]:.6f} | '
                         f'{totals[i]["wall_seconds"]:.6f} | {totals[i]["cpu_seconds"]:.6f} |')
    lines += ['', 'Every completed case replays the complete retained history through the original Engine. '
        'Fresh actions are checked against each other and the recorded candidate actions, with legal application and no observation mutation. '
        'Persistent instance fields and foreign function closure values are compared after each actual call.', '',
        'These are existing development histories, not new strength games. '
        'The implementations share module caches within each per-history process; call order alternates by round. '
        'Measured times describe these executions and are not portable bounds. '
        'The native transition proof is in PROOF.md; foreign-history agreement is empirical because the unchanged fallback has a finite clock cutoff.', '',
        'The installed best_v9e and reserved terminal validation remain unchanged. '
        'This worker-owned research variant is a possible performance improvement, not a newly validated final candidate.']
    with (A/'RESULTS.md').open('x') as f:
        f.write('\n'.join(lines)+'\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {now()}: Protocol151 immune shortcut complete\n\n'
            f'Claim H1 exact actions and legitimate state on74 retained histories: {"CONFIRMED" if h1 else "OPEN"}. '
            f'Result: {calls} calls per implementation, {result["differences"]} differences, {len(failures)} failed attempts; '
            f'{fast_calls} shortcut calls, {foreign_calls} unchanged foreign calls per implementation. '
            f'H2 {"CONFIRMED" if h2 else "REFUTED"}; H3 high-factory max shortcut CPU<3s {"CONFIRMED" if h3 else "REFUTED"}. '
            f'High-factory maxima parent/shortcut: {json.dumps(maxima)}. '
            'Method, scope, original-engine checks and source-bound receipts: experiments/validation/analysis/immune_runtime_shortcut/RESULTS.md. '
            'Zero new games. Final candidate andDunchanged.\n')
    print(json.dumps({k:result[k] for k in ('time_utc','all_passed','completed_cases','calls_per_implementation','shortcut_calls','foreign_calls_per_implementation','differences')}), flush=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('mode', choices=['declare','case','run','publish'])
    p.add_argument('--id')
    p.add_argument('--shard', type=int, default=0)
    p.add_argument('--shards', type=int, default=1)
    a = p.parse_args()
    if a.mode == 'declare':
        declare()
    elif a.mode == 'case':
        case(a.id)
    elif a.mode == 'run':
        run(a.shard, a.shards)
    else:
        publish()


if __name__ == '__main__':
    main()

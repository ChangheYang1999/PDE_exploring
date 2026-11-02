"""Pinned stream-boundary checks and unpaired shortcut runtime reproduction."""
from __future__ import annotations
import argparse
from copy import deepcopy
import cProfile
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import resource
import time
from bot_research.bots.counters.immune_runtime_shortcut import make
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.lead.frozen import best_v9e as parent
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import execution_context
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine

E = Path('bot_research/experiments/validation')
A = E/'analysis/immune_shortcut_followup'
D = E/'immune-shortcut-followup-001.json'
PREVIOUS = E/'immune-shortcut-001.json'
OLD = Path('bot_research/runs/validation/immune-shortcut-001')
PARENT = Path('bot_research/runs/validation/visible-gold-runtime-001')
R = Path('bot_research/runs/validation/immune-shortcut-followup-001')


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    return json.loads(Path(p).read_text())


def verify():
    d = read(D)
    for p, h in d['input_sha256'].items():
        assert sha(p) == h, p
    return d


def declare():
    old = read(PREVIOUS)
    paths = set(map(Path, old['input_sha256']))
    for p, h in old['input_sha256'].items():
        assert sha(p) == h, p
    paths.update(static_closure({'bot_research.experiments.validation.immune_shortcut_followup'}))
    paths.update([PREVIOUS, A/'PROOF.md', E/'analysis/immune_runtime_shortcut/verification/full_check.json',
                  E/'reviews/immune-shortcut-checker-review-001.md'])
    paths.update(OLD/'cases'/(case['id']+'.json') for case in old['cases'])
    paths.update(PARENT/f'policy-seat{side}.json' for side in (0, 1))
    assert len(old['cases']) == 74
    assert read(E/'analysis/immune_runtime_shortcut/verification/full_check.json')['all_passed']
    R.mkdir(exist_ok=False)
    atomic_json(D, dict(time_utc=now(), cases=old['cases'], input_sha256={str(p):sha(p) for p in sorted(paths)},
        expected_policy_calls=100, expected_unprofiled_component_calls=1, expected_profiled_component_calls=1,
        policy_calls_before_declaration=0, hypotheses=['H1 all74 exact terminal boundaries',
            'H2 all100 fresh shortcut-only decisions match', 'H3 maximum shortcut CPU below3 seconds',
            'H4 unprofiled seat0 round50 worst_leak returns0 and CPU exceeds3 seconds'],
        limitation='Separate process per history; no external eligibility preflight or parent calls. Caches warm naturally across rounds.'), exclusive=True)
    print(json.dumps(dict(time_utc=now(), pins=len(paths), policy_calls_before_declaration=0)), flush=True)


def shape():
    begin = time.perf_counter()
    d = verify()
    rows = []
    for entry in d['cases']:
        summary = read(entry['record'])
        records = [json.loads(line) for line in Path(entry['replay']).read_text().splitlines()]
        rounds = summary['rounds']
        assert isinstance(rounds, int) and rounds > 0
        assert len(records) == 2*(rounds+1), entry['id']
        assert all(rec['round'] == index//2 and rec['player'] == index%2 for index, rec in enumerate(records))
        assert all(rec.get('result') is None for rec in records[:-2])
        terminal = records[-1]['result']
        assert terminal is not None and terminal == records[-2]['result']
        assert terminal['winner'] in (None, 0, 1)
        assert terminal['reason'] in ('round_limit', 'base_destroyed', 'both_destroyed')
        if entry['kind'] == 'high_factory':
            assert terminal == dict(winner=summary['winner'], reason=summary['reason'])
        else:
            assert terminal == summary['result']
        prior = read(OLD/'cases'/(entry['id']+'.json'))
        assert prior['all_passed'] and prior['original_engine_replayed']
        assert prior['declaration_sha256'] == sha(PREVIOUS)
        rows.append(dict(id=entry['id'], records=len(records), final_round=rounds, terminal=terminal, passed=True))
    verify()
    atomic_json(R/'shape.json', dict(time_utc=now(), all_passed=True, cases=rows,
        declaration_sha256=sha(D), policy_calls=0, elapsed_seconds=time.perf_counter()-begin), exclusive=True)
    print(json.dumps(dict(time_utc=now(), shape_cases=len(rows), all_passed=True)), flush=True)


def high_inputs(side):
    d = verify()
    entry = next(c for c in d['cases'] if c['id'] == f'high-{side}')
    row = read(entry['record'])
    records = [json.loads(line) for line in Path(entry['replay']).read_text().splitlines()]
    assert len(records) == 102 and row['rounds'] == 50
    cfg = balanced_config()
    names = tuple(r['snapshot']['name'] for r in records[:2])
    engine = Engine(cfg, names)
    initial = normalized(engine.initial_records(names))
    metadata = dict(research_specs=[row['spec_a'], row['spec_b']], research_scenario=row['scenario'],
                    research_metadata=row['metadata'])
    for rec in initial:
        rec['match'].update(metadata)
    assert initial == records[:2]
    return row, records, cfg, engine


def actions_of(pair):
    assert not any(e['kind'] == 'bot_error' or (e['kind'] == 'action' and not e['accepted'])
                   for rec in pair for e in rec['event'])
    return [[e['action'] for e in rec['event'] if e['kind'] == 'action'] for rec in pair]


def policy(side):
    begin = time.perf_counter()
    row, records, cfg, engine = high_inputs(side)
    bot = make()
    measurements = []
    for rnd in range(1, 51):
        pair = records[2*rnd:2*rnd+2]
        obs = engine.observation(side)
        saved = deepcopy(obs)
        # Do not classify eligibility or instantiate/call the parent before timing.
        w, c = time.perf_counter(), time.process_time()
        proposed = bot(obs)
        cpu, wall = time.process_time()-c, time.perf_counter()-w
        assert obs == saved
        proposed = json.loads(json.dumps(proposed, allow_nan=False))
        actions = actions_of(pair)
        assert proposed == actions[side], (side, rnd)
        own = player_from_snapshot(saved['players'][side])
        assert all(apply_action(own, a, rnd, cfg)['accepted'] for a in proposed)
        assert normalized(engine.play_round(actions)) == pair
        measurements.append(dict(side=side, round=rnd, action_count=len(proposed),
                                 cpu_seconds=cpu, wall_seconds=wall, exact=True))
    assert engine.result is not None
    assert engine.result == dict(winner=row['winner'], reason=row['reason'])
    assert [p.hp for p in engine.players] == [row['hp_a'], row['hp_b']]
    verify()
    result = dict(time_utc=now(), side=side, all_passed=True, policy_calls=50, calls=measurements,
        parent_policy_calls=0, eligibility_preflight_calls=0, complete_original_engine_replay=True,
        declaration_sha256=sha(D), execution=execution_context(),
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        elapsed_seconds=time.perf_counter()-begin)
    atomic_json(R/f'policy-seat{side}.json', result, exclusive=True)
    print(json.dumps(dict(time_utc=now(), side=side, policy_calls=50,
        maximum_cpu=max(m['cpu_seconds'] for m in measurements), all_passed=True)), flush=True)


def component():
    begin = time.perf_counter()
    _, records, _, engine = high_inputs(0)
    for rnd in range(1, 50):
        pair = records[2*rnd:2*rnd+2]
        assert normalized(engine.play_round(actions_of(pair))) == pair
    obs = engine.observation(0)
    saved = deepcopy(obs)
    rules = parent.gk.Rules.from_observation(obs)
    comps = parent.P.threat_compositions(obs)
    lengths = list(map(len, comps))
    w, c = time.perf_counter(), time.process_time()
    leak = parent._worst_leak(obs, rules, comps)
    cpu, wall = time.process_time()-c, time.perf_counter()-w
    assert obs == saved
    profiler = cProfile.Profile()
    w, c = time.perf_counter(), time.process_time()
    profiler.enable()
    profiled_leak = parent._worst_leak(obs, rules, comps)
    profiler.disable()
    profile_cpu, profile_wall = time.process_time()-c, time.perf_counter()-w
    assert obs == saved and profiled_leak == leak
    profiler.create_stats()
    stats = []
    for (filename, line, name), (primitive, calls, own, cumulative, callers) in profiler.stats.items():
        if filename.startswith('~') or filename.startswith('<'):
            public = filename
        else:
            try:
                public = str(Path(filename).resolve().relative_to(Path.cwd().resolve()))
            except ValueError:
                public = '<python>/'+Path(filename).name
        stats.append(dict(file=public, line=line, function=name, primitive_calls=primitive, calls=calls,
                          own_profile_seconds=own, cumulative_profile_seconds=cumulative))
    stats.sort(key=lambda s:s['cumulative_profile_seconds'], reverse=True)
    verify()
    result = dict(time_utc=now(), all_checks_passed=True, round=50, side=0, policy_calls=0,
        unprofiled_component_calls=1, profiled_component_calls=1, leak=leak, profiled_leak=profiled_leak,
        cpu_seconds=cpu, wall_seconds=wall, profile_cpu_seconds=profile_cpu, profile_wall_seconds=profile_wall,
        composition_lengths=lengths, total_type_slots=sum(lengths), maximum_length=max(lengths),
        profile=stats, declaration_sha256=sha(D), execution=execution_context(),
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, elapsed_seconds=time.perf_counter()-begin)
    atomic_json(R/'component.json', result, exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','leak','cpu_seconds','wall_seconds','profile_cpu_seconds')}), flush=True)


def publish():
    verify()
    paths = [R/'shape.json', R/'policy-seat0.json', R/'policy-seat1.json', R/'component.json']
    shape_result, p0, p1, comp = [read(p) for p in paths]
    assert all(read(p)['declaration_sha256'] == sha(D) for p in paths)
    h1 = shape_result['all_passed'] and len(shape_result['cases']) == 74
    h2 = all(p['all_passed'] and p['complete_original_engine_replay'] and p['policy_calls'] == 50 for p in (p0, p1))
    assert all(p['parent_policy_calls'] == 0 and p['eligibility_preflight_calls'] == 0 for p in (p0, p1))
    calls = p0['calls']+p1['calls']
    cpu = max(calls, key=lambda c:c['cpu_seconds'])
    wall = max(calls, key=lambda c:c['wall_seconds'])
    h3 = cpu['cpu_seconds'] < 3
    h4 = comp['leak'] == 0 and comp['cpu_seconds'] > 3
    oldcalls = [c for side in (0, 1) for c in read(PARENT/f'policy-seat{side}.json')['calls']]
    parent_cpu = max(oldcalls, key=lambda c:c['cpu_seconds'])
    parent_wall = max(oldcalls, key=lambda c:c['wall_seconds'])
    stamp = now()
    verdict = lambda h: 'CONFIRMED' if h else 'REFUTED'
    lines = ['# Boundary checks and shortcut-only timing', '', f'Completed {stamp}.', '',
        f'H1 **{verdict(h1)}**: all74 input streams have exactly2(r+1) ordered records, no earlier terminal result and identical non-null final results agreeing with their summaries. Together with protocol151\'s initial and per-round Engine checks, this closes its complete-stream claim.', '',
        f'H2 **{verdict(h2)}**: all100 shortcut-only calls match the retained actions, with legal actions, unchanged observations and two complete original-engine replays. There were0 parent policy calls and0 external eligibility preflights.', '',
        f'H3 **{verdict(h3)}**: maximum shortcut process CPU {cpu["cpu_seconds"]:.6f}s (seat{cpu["side"]}, round{cpu["round"]}); maximum wall time {wall["wall_seconds"]:.6f}s. Each50-call history used a fresh process, with caches naturally warming across rounds.', '',
        f'Protocol150\'s separate parent measurements reached {parent_cpu["cpu_seconds"]:.6f}s CPU and {parent_wall["wall_seconds"]:.6f}s wall. These were measured at a different time, so the comparison is descriptive. The151 paired measurements additionally included an untimed eligibility preflight before both calls; they are not cold-call benchmarks.', '',
        f'H4 **{verdict(h4)}**: the unprofiled seat0 round50 _worst_leak returned {comp["leak"]} in {comp["cpu_seconds"]:.6f}s CPU and {comp["wall_seconds"]:.6f}s wall. Its sampled rosters contain {comp["total_type_slots"]} type slots; construction was outside this timed interval.', '',
        f'The separate profiler call returned {comp["profiled_leak"]} and took {comp["profile_cpu_seconds"]:.6f}s CPU. Profiler overhead is included in the following function times and must not be added to or substituted for the unprofiled measurement.', '',
        '| Function | Calls | Own profiled s | Cumulative profiled s |', '| --- | ---: | ---: | ---: |']
    for s in comp['profile'][:12]:
        lines.append(f'| {s["file"]}:{s["line"]} {s["function"]} | {s["calls"]} | {s["own_profile_seconds"]:.6f} | {s["cumulative_profile_seconds"]:.6f} |')
    lines += ['', 'No new strength games, no final-candidate change and no terminal-pool use. Native transition equivalence retains the exact hypotheses of protocol151; foreign histories remain empirical checks. Neither runtime measurement is a portable upper bound. PROOF.md gives the complete argument and method.']
    with (A/'RESULTS.md').open('x') as f:
        f.write('\n'.join(lines)+'\n')
    result = dict(time_utc=stamp, h1=h1, h2=h2, h3=h3, h4=h4, all_passed=all((h1,h2,h3,h4)),
        stream_checks=74, policy_calls=100, unprofiled_component_calls=1, profiled_component_calls=1,
        new_games=0, maximum_shortcut_cpu=cpu, maximum_shortcut_wall=wall,
        component_cpu_seconds=comp['cpu_seconds'], component_leak=comp['leak'],
        input_sha256={str(D):sha(D), **{str(p):sha(p) for p in paths}})
    atomic_json(A/'verification/full_check.json', result, exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Runtime supplement complete\n\nClaim H1 exact74 terminal boundaries {verdict(h1)}; H2 all100 unpaired shortcut calls exact {verdict(h2)}; H3 shortcut maxCPU<3s {verdict(h3)} ({cpu["cpu_seconds"]:.6f}s); H4 round50 sampled-leak CPU>3s and result0 {verdict(h4)} ({comp["cpu_seconds"]:.6f}s, leak{comp["leak"]}). No parent policy calls or eligibility preflights in these shortcut processes. Separate profiler timings include overhead. Evidence: experiments/validation/analysis/immune_shortcut_followup/RESULTS.md. No new games or final/D changes.\n')
    print(json.dumps({k:result[k] for k in ('time_utc','all_passed','h1','h2','h3','h4','policy_calls')}), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['declare','shape','policy','component','publish'])
    parser.add_argument('--side', type=int, choices=[0,1])
    args = parser.parse_args()
    if args.mode == 'policy':
        assert args.side is not None
        policy(args.side)
    else:
        globals()[args.mode]()


if __name__ == '__main__':
    main()

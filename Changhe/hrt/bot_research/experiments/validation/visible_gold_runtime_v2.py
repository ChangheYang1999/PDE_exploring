"""Audit observed runtime on two existing high-factory public histories."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import resource
import time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.defense.frozen.v7 import plan as P
from bot_research.experiments.lead.frozen.best_v9e import make
from bot_research.harness import gamekit as gk
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import execution_context
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure
E = Path('bot_research/experiments/validation')
A = E/'analysis/visible_gold_runtime'
D = E/'visible-gold-runtime-001.json'
R = Path('bot_research/runs/validation/visible-gold-runtime-001')
AMENDMENT = E/'visible-gold-runtime-amendment-001.json'
SOURCE = Path('bot_research/runs/defense/x202a_fcap_vs_best9e/results.jsonl')
FROZEN = 'bot_research.experiments.lead.frozen.best_v9e:decide'


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_declaration():
    d = json.loads(D.read_text())
    for p, h in d['input_sha256'].items():
        assert sha(p) == h, p
    amendment = json.loads(AMENDMENT.read_text())
    for p, h in amendment['input_sha256'].items():
        assert sha(p) == h, p
    return d


def declare():
    R.mkdir(exist_ok=False)
    rows = [json.loads(s) for s in SOURCE.read_text().splitlines()]
    cases = []
    for row in rows:
        specs = [row['spec_a'], row['spec_b']]
        if row['scenario'] is not None or FROZEN not in specs:
            continue
        side = specs.index(FROZEN)
        if 'factory_cap=1200' not in specs[1-side]:
            continue
        assert row['rounds'] == 50 and row['log'] and not row['source_changed'] and not row['error']
        assert all(not p['n_rejected'] and not p['bot_errors'] for p in row['players'])
        assert row['sources']['bot_research/experiments/lead/frozen/best_v9e.py'] == sha('bot_research/experiments/lead/frozen/best_v9e.py')
        target = A/'sources'/f'seat{side}.jsonl'
        raw = Path(row['log']).read_bytes()
        with target.open('xb') as f:
            f.write(raw)
        rowpath = A/'sources'/f'seat{side}-result.json'
        atomic_json(rowpath, row, exclusive=True)
        cases.append(dict(side=side, record=str(rowpath), replay=str(target), original_replay=row['log'], original_sha256=hashlib.sha256(raw).hexdigest()))
    cases.sort(key=lambda c:c['side'])
    assert len(cases) == 2 and [c['side'] for c in cases] == [0, 1]
    paths = set(static_closure({'bot_research.experiments.validation.visible_gold_runtime'}))
    paths |= {A/'PROOF.md', Path('td_game/balanced.json'), Path('configs/balanced.json')}
    for c in cases:
        paths |= {Path(c['record']), Path(c['replay'])}
    inputs = {str(p):sha(p) for p in sorted(paths)}
    atomic_json(D, dict(time_utc=now(), source_results=str(SOURCE), source_results_sha256=sha(SOURCE), cases=cases,
        input_sha256=inputs, expected_fresh_candidate_calls=100, expected_component_calls=10,
        component_rounds=[10, 20, 30, 40, 50], purpose='Reproduction and runtime audit of existing games; no new game.'), exclusive=True)
    print(json.dumps(dict(time_utc=now(), cases=2, pins=len(inputs))), flush=True)


def run(index, component):
    started = time.perf_counter()
    d = read_declaration()
    case = d['cases'][index]
    row = json.loads(Path(case['record']).read_text())
    records = [json.loads(s) for s in Path(case['replay']).read_text().splitlines()]
    cfg = balanced_config()
    names = tuple(r['snapshot']['name'] for r in records[:2])
    engine = Engine(cfg, names)
    initial = normalized(engine.initial_records(names))
    extra = dict(research_specs=[row['spec_a'], row['spec_b']],
                 research_scenario=row['scenario'], research_metadata=row['metadata'])
    for record in initial:
        record['match'].update(extra)
    assert initial == records[:2]
    assert len(records) == 102
    side = case['side']
    policy = None if component else make()
    calls = []
    for rnd in range(1, 51):
        pair = records[2*rnd:2*rnd+2]
        obs = engine.observation(side)
        saved = deepcopy(obs)
        rules = gk.Rules.from_observation(obs)
        enemy = obs['players'][1-side]
        active = len(P.active_opponent_types(obs))
        exposure = P.splash_damage(obs['players'][side]['buildings'], rules)
        measured = dict(round=rnd, side=side, gold=enemy['gold'], enemy_factories=enemy['n_factories'],
                        active_opponent_entries=active, own_splash_exposure=exposure)
        if component and rnd in d['component_rounds']:
            begin_wall, begin_cpu = time.perf_counter(), time.process_time()
            comps = P.threat_compositions(obs)
            elapsed_cpu, elapsed_wall = time.process_time()-begin_cpu, time.perf_counter()-begin_wall
            lengths = list(map(len, comps))
            expected = active + enemy['gold']//rules.minions['tier1']['cost']
            assert max(lengths, default=0) == expected
            measured.update(wall_seconds=elapsed_wall, cpu_seconds=elapsed_cpu, lengths=lengths,
                total_type_slots=sum(lengths), maximum_length=max(lengths, default=0), expected_maximum=expected,
                maximum_hp=max((P.max_hp(c, rules) for c in comps), default=0))
            calls.append(measured)
            del comps
        elif not component:
            begin_wall, begin_cpu = time.perf_counter(), time.process_time()
            proposed = policy(obs)
            elapsed_cpu, elapsed_wall = time.process_time()-begin_cpu, time.perf_counter()-begin_wall
            measured.update(wall_seconds=elapsed_wall, cpu_seconds=elapsed_cpu, actions=len(proposed))
        assert obs == saved
        actions = [[e['action'] for e in record['event'] if e['kind'] == 'action'] for record in pair]
        assert not any(e['kind'] == 'bot_error' or (e['kind'] == 'action' and not e['accepted']) for r in pair for e in r['event'])
        if not component:
            measured['exact'] = proposed == actions[side]
            own = player_from_snapshot(saved['players'][side])
            assert all(apply_action(own, a, rnd, cfg)['accepted'] for a in proposed)
            calls.append(measured)
        assert normalized(engine.play_round(actions)) == pair
        if not component or rnd in d['component_rounds']:
            print(json.dumps(dict(time_utc=now(), mode='component' if component else 'policy', **measured)), flush=True)
    assert [p.hp for p in engine.players] == [row['hp_a'], row['hp_b']]
    assert engine.result['winner'] == row['winner'] and engine.result['reason'] == row['reason']
    assert len(calls) == (5 if component else 50)
    assert component or all(c['exact'] for c in calls)
    read_declaration()
    mode = 'component' if component else 'policy'
    result = dict(time_utc=now(), mode=mode, side=side, runtime_seconds=time.perf_counter()-started,
        all_passed=True, calls=calls, original_engine_replayed=True,
        candidate_calls=0 if component else len(calls), component_calls=len(calls) if component else 0,
        execution=execution_context(), peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        declaration_sha256=sha(D), amendment_sha256=sha(AMENDMENT), hp=[p.hp for p in engine.players], result=engine.result)
    atomic_json(R/f'{mode}-seat{side}.json', result, exclusive=True)


def publish():
    d = read_declaration()
    receipts = [R/f'{mode}-seat{side}.json' for mode in ('policy', 'component') for side in (0, 1)]
    data = [json.loads(p.read_text()) for p in receipts]
    assert all(r['all_passed'] and r['original_engine_replayed'] and r['declaration_sha256'] == sha(D) for r in data)
    assert all(r['amendment_sha256'] == sha(AMENDMENT) for r in data)
    assert sum(r['candidate_calls'] for r in data) == 100
    assert sum(r['component_calls'] for r in data) == 10
    pcalls = [c for r in data if r['mode'] == 'policy' for c in r['calls']]
    ccalls = [c for r in data if r['mode'] == 'component' for c in r['calls']]
    wall = max(pcalls, key=lambda c:c['wall_seconds'])
    cpu = max(pcalls, key=lambda c:c['cpu_seconds'])
    h2, h3 = wall['wall_seconds'] > 3, cpu['cpu_seconds'] > 3
    stamp = now()
    lines = ['# Visible-gold runtime on two retained histories', '', f'Completed {stamp}.', '',
        'H1 **CONFIRMED**: all100 fresh candidate decisions exactly match the recorded actions, and both histories replay through the unchanged engine. H2, a call takes more than3 wall-clock seconds: **'+('CONFIRMED' if h2 else 'REFUTED')+'**. H3, a call takes more than3 process-CPU seconds: **'+('CONFIRMED' if h3 else 'REFUTED')+'**.', '',
        f'Maximum wall time: {wall["wall_seconds"]:.6f}s, seat{wall["side"]} round{wall["round"]}; maximum CPU time: {cpu["cpu_seconds"]:.6f}s, seat{cpu["side"]} round{cpu["round"]}. These are measurements under the recorded core affinity and low priority, not portable bounds.', '',
        '| Seat | Round | Visible gold | Own splash S | Max list length | Total type slots | Component wall s | Component CPU s |',
        '| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
    for c in ccalls:
        lines.append(f'| {c["side"]} | {c["round"]} | {c["gold"]} | {c["own_splash_exposure"]} | {c["maximum_length"]} | {c["total_type_slots"]} | {c["wall_seconds"]:.6f} | {c["cpu_seconds"]:.6f} |')
    lines += ['', 'All10 component calls have maximum list length equal to active opponent entries plus floor(visible gold /15), as predicted by the source argument. The gun cap disables gun search but does not bound these allocated lists. An already immune map does not bypass their construction or the planner\'s initial list scan.', '',
        'The original checker stopped before any policy call because it omitted the harness research metadata in the initial headers. AMENDMENT.md documents the exact correction; no game record was edited.', '',
        'These are two previously recorded standard games against the x202a factory-cap1200 policy, with no new strength sample. Only the candidate action stream is freshly regenerated; the opponent\'s historical live source is not asserted identical to its current source. The existing result stays best_v9e790:785 in both assignments. Candidate bytes and poolD are unchanged. See PROOF.md and the pinned input/receipt hashes.']
    with (A/'RESULTS.md').open('x') as f:
        f.write('\n'.join(lines)+'\n')
    result = dict(time_utc=stamp, all_passed=True, h1=True, h2=h2, h3=h3, candidate_calls=100, component_calls=10,
        new_games=0, reused_games=2, maximum_wall_call=wall, maximum_cpu_call=cpu,
        maximum_peak_rss_kib=max(r['peak_rss_kib'] for r in data), input_sha256={str(D):sha(D),str(AMENDMENT):sha(AMENDMENT),**{str(p):sha(p) for p in receipts}})
    atomic_json(A/'verification/full_check.json', result, exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Visible-gold runtime audit complete\n\nClaim H1 exact candidate regeneration CONFIRMED:100calls,2original-engine replayed historical games,0new strength games. H2 call>3wallseconds {"CONFIRMED" if h2 else "REFUTED"}; H3 call>3CPUseconds {"CONFIRMED" if h3 else "REFUTED"}. Maxima {wall["wall_seconds"]:.6f}s wall and {cpu["cpu_seconds"]:.6f}s CPU. All10 sampled threat-list lengths equal active entries+floor(gold/15). Gun cap does not cap list construction. Scope and complete evidence: experiments/validation/analysis/visible_gold_runtime/RESULTS.md. Final candidate andDunchanged.\n')
    print(json.dumps(result), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['declare', 'policy', 'component', 'publish'])
    parser.add_argument('index', type=int, nargs='?', choices=[0, 1])
    args = parser.parse_args()
    if args.mode == 'declare':
        declare()
    elif args.mode == 'publish':
        publish()
    else:
        assert args.index is not None
        run(args.index, args.mode == 'component')


if __name__ == '__main__':
    main()

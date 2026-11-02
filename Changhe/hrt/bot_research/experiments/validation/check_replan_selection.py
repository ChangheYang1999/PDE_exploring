"""Audit fixed-splash accounting in the frozen v26 layout selector.

Recorded maps are read from completed games. This is a planner component
study, not a new strength match or a reserved-pool evaluation.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import time
from td_game.pathfinding import shortest_path
from bot_research.bots.defense.frozen.v26.replan import replan_layout
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.replay_audit import audit_record_sequence
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def describe(layout, buildings):
    fixed = {(b['x'], b['y']) for b in buildings}
    fixed_splashes = {(b['x'], b['y']) for b in buildings if b['type'] == 'splash'}
    slots = set(layout.splash_cells)
    walls = set(layout.wall_order)
    assert not (slots & walls or fixed & (slots | walls))
    added = list(layout.wall_order) + list(layout.splash_cells)
    blocked = set(fixed)
    # Every declared action prefix leaves a path under original pathfinding.
    for cell in added:
        assert cell not in ((0,0),(11,11)) and cell not in blocked
        blocked.add(cell)
        assert shortest_path(12,12,blocked,(0,0),(11,11)) is not None
    path = shortest_path(12,12,blocked,(0,0),(11,11))
    assert len(path)-1 == layout.final_len
    def exposure(cells):
        return 10 * sum(max(abs(c[0]-p[0]),abs(c[1]-p[1])) == 1
                        for c in cells for p in path[:-1])
    new, old = exposure(slots), exposure(fixed_splashes)
    assert new == 10 * sum(layout.final_adj[c] for c in layout.splash_cells)
    return dict(new_splash_exposure=new, fixed_splash_exposure=old,
                total_splash_exposure=new+old, route_length=len(path)-1,
                wall_order=layout.wall_order, splash_cells=layout.splash_cells,
                final_path=path, all_prefixes_have_route=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    manifest = json.loads(Path(args.manifest).read_text())
    source_paths = static_closure({'bot_research.bots.defense.frozen.v26.replan',
                                  'bot_research.experiments.validation.check_replan_selection'})
    sources = {str(p): digest(p) for p in source_paths}
    inputs = {args.manifest: digest(args.manifest)}
    loaded = {}
    results = []
    started = time.perf_counter()
    for fixture in manifest['fixtures']:
        name = fixture['result_path']
        if name not in loaded:
            row = json.loads(Path(name).read_text())
            replay = Path(row['replay_path'])
            assert digest(replay) == row['trajectory_sha256']
            records = [json.loads(line) for line in replay.read_text().splitlines()]
            audit_record_sequence(row, records)
            loaded[name] = (row, records)
            inputs[name] = digest(name)
            inputs[str(replay)] = digest(replay)
        row, records = loaded[name]
        record = next(r for r in records if r['round'] == fixture['round'] and r['player'] == fixture['side'])
        buildings = record['snapshot']['buildings']
        baseline = deepcopy(buildings)
        for seed in fixture['seeds']:
            options = []
            for objective in ('exposure','route'):
                t = time.perf_counter()
                layout = replan_layout(buildings, iters=manifest['iters']//2,
                                       seed=seed, time_budget=None, objective=objective)
                options.append(dict(objective=objective, runtime_seconds=time.perf_counter()-t,
                                    **describe(layout, buildings)))
            assert buildings == baseline
            by_new = max(options, key=lambda o:(o['new_splash_exposure'],o['route_length']))
            by_total = max(options, key=lambda o:(o['total_splash_exposure'],o['route_length']))
            item = dict(fixture=fixture['id'], round=fixture['round'], side=fixture['side'], seed=seed,
                existing_splashes=sum(b['type']=='splash' for b in buildings), options=options,
                selected_by_current_comparison=by_new['objective'],
                selected_by_total_exposure=by_total['objective'],
                selected_total_exposure=by_new['total_splash_exposure'],
                largest_total_exposure=by_total['total_splash_exposure'],
                loses_total_exposure=by_new['total_splash_exposure'] < by_total['total_splash_exposure'])
            if item['loses_total_exposure']:
                # Confirm the actual best entrypoint makes the predicted choice.
                layout = replan_layout(buildings, iters=manifest['iters'], seed=seed,
                                       time_budget=None, objective='best')
                selected = describe(layout, buildings)
                assert selected['wall_order'] == by_new['wall_order']
                assert selected['splash_cells'] == by_new['splash_cells']
                item['actual_best_call_confirmed'] = True
            results.append(item)
            print(json.dumps({k:item[k] for k in ('fixture','seed','existing_splashes','selected_total_exposure','largest_total_exposure','loses_total_exposure')}),flush=True)
    assert all(digest(p)==sha for p,sha in sources.items())
    output=dict(time_utc=now(),runtime_seconds=time.perf_counter()-started,
        source_sha256=sources,input_sha256=inputs,results=results,
        all_source_hashes_unchanged=True,full_replay_checks=len(loaded),
        scope='Frozen planner on recorded legal maps; exact original pathfinding and explicit splash-neighbor counts. No full-game strength inference. An exposure comparison is not a proof of globally optimal layout.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps(dict(comparisons=len(results),selection_counterexamples=sum(r['loses_total_exposure'] for r in results),runtime_seconds=output['runtime_seconds'])),flush=True)


if __name__ == '__main__':
    main()

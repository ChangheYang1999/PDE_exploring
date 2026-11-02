"""Finite original-engine search for a defended round-three heavy-strike budget."""
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json
import time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry
from bot_research.experiments.validation.source_closure import static_closure

AREA = Path('bot_research/experiments/validation/analysis/guarded_opening_budget')
DATA = Path('bot_research/bots/counters/data/maze_layouts_001.json')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    cfg = balanced_config()
    g = cfg.globals
    assert (g.initial_gold, g.factory_cost, g.factory_income, g.path_income_per_step) == (100,20,15,1)
    assert cfg.minions['tier4'].cost == 260
    paths = set(static_closure({'bot_research.experiments.validation.design_guarded_opening'}))
    paths.update((DATA, AREA/'PROOF.md', Path('configs/balanced.json'), Path('td_game/balanced.json')))
    digest = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    inputs = {str(p):digest(p) for p in paths}
    baseline = Engine(cfg, ('guard', 'striker'))
    for count in (5,4):
        rr = baseline.play_round([[{'op':'buy_factory'} for _ in range(count)] for _ in (0,1)])
        assert not any(e.get('accepted') is False for r in rr for e in r['event'])
    assert baseline.players[0].gold == 174 and baseline.players[0].n_factories == 9
    attacker = PlayerState('four_tier2', 800, 0, roster=[RosterEntry(i,'tier2',3,14) for i in range(4)])
    rows, winners, counts = [], [], Counter()
    for layout in json.loads(DATA.read_text())['layouts']:
        wall_cells = [tuple(c) for c in layout['walls']]
        blocked = set(wall_cells)
        cells = [(x,y) for x in range(g.width) for y in range(g.height)
                 if (x,y) not in blocked and (x,y) not in (tuple(g.spawn), tuple(g.base))]
        local = Counter()
        for n in (1,2):
            for positions in combinations(cells, n):
                route = shortest_path(g.width,g.height,blocked|set(positions),g.spawn,g.base)
                if route is None:
                    local['blocked_position_sets'] += 1
                    continue
                length = len(route)-1
                for kinds in product(('gun1','gun2','splash'), repeat=n):
                    local['legal_map_type_assignments'] += 1
                    cost = len(wall_cells)*cfg.wall_cost + sum(cfg.turrets[t].cost for t in kinds)
                    if cost > 174:
                        local['unaffordable_round3'] += 1
                        continue
                    factories = (174-cost)//g.factory_cost
                    next_gold = 309-cost-5*factories+length
                    if next_gold < cfg.minions['tier4'].cost:
                        local['unaffordable_round4'] += 1
                        continue
                    local['budget_feasible_maps'] += 1
                    buildings = [Building(x,y,'wall') for x,y in wall_cells]
                    buildings += [Building(x,y,t) for (x,y),t in zip(positions,kinds)]
                    defender = PlayerState('guard',800,0,buildings=buildings)
                    combat = simulate_map(attacker,defender,route,3,cfg)
                    local['original_combat_checks'] += 1
                    local['zero_damage_maps' if combat.damage == 0 else 'leaking_maps'] += 1
                    if combat.damage:
                        continue
                    winners.append(dict(layout=layout['id'], walls=[list(c) for c in wall_cells],
                        turrets=[dict(type=t,x=x,y=y) for (x,y),t in zip(positions,kinds)],
                        cost=cost,round3_new_factories=factories,round4_gold=next_gold,
                        path=[list(c) for c in route],length=length,combat=vars(combat)))
        counts.update(local)
        rows.append(dict(layout=layout['id'],counts=dict(local)))
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),layout=layout['id'],counts=dict(local))),flush=True)
    winners.sort(key=lambda w:(-w['round3_new_factories'],-w['round4_gold'],w['cost'],w['layout'],json.dumps(w['turrets'],sort_keys=True)))
    selected = winners[:8]
    for witness in selected:
        engine = deepcopy(baseline)
        actions = [dict(op='build_wall',x=x,y=y) for x,y in witness['walls']]
        actions += [dict(op='build_turret',**t) for t in witness['turrets']]
        actions += [dict(op='buy_factory') for _ in range(witness['round3_new_factories'])]
        rr = engine.play_round([actions,[dict(op='buy_minion',type='tier2') for _ in range(4)]])
        assert all(e.get('accepted',True) for r in rr for e in r['event'])
        assert engine.players[0].hp == 800 and engine.players[0].gold == witness['round4_gold']
        assert apply_action(deepcopy(engine.players[0]),dict(op='buy_minion',type='tier4'),4,cfg)['accepted']
        witness['round3_actions'] = actions
        witness['round3_records'] = rr
        checks = []
        for tier in ('tier1','tier2','tier3','tier4'):
            for count in (1,2,4,8):
                enemy = PlayerState('component',800,0,roster=[RosterEntry(i,tier,3,14) for i in range(count)])
                defender = deepcopy(engine.players[0])
                result = simulate_map(enemy,defender,[tuple(c) for c in witness['path']],3,cfg)
                checks.append(dict(tier=tier,count=count,**vars(result)))
        witness['components'] = checks
    assert all(digest(p)==h for p,h in inputs.items())
    stamp = datetime.now(timezone.utc).isoformat()
    result = dict(time_utc=stamp,runtime_seconds=time.perf_counter()-start,
        verdict='CONFIRMED' if winners else 'REFUTED',counts=dict(counts),layouts=rows,
        total_zero_damage_maps=len(winners),selected=selected,input_sha256=inputs,
        scope='All one/two-turret maps of the three affordable turret types on the twelve declared wall layouts. A component search, not a full-game strength claim.')
    with Path(args.output).open('x') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('selected','input_sha256','layouts')}),flush=True)


if __name__ == '__main__':
    main()

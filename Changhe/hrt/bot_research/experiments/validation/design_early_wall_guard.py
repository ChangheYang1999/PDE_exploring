"""Original-engine search for earlier walls and a defended heavy-strike budget."""
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

AREA = Path('bot_research/experiments/validation/analysis/guarded_opening_wall_timing')
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
    paths = set(static_closure({'bot_research.experiments.validation.design_early_wall_guard'}))
    paths.update((DATA, AREA/'PROOF.md', Path('configs/balanced.json'), Path('td_game/balanced.json')))
    digest = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    inputs = {str(p):digest(p) for p in paths}
    attacker = PlayerState('four_tier2', 800, 0, roster=[RosterEntry(i,'tier2',3,14) for i in range(4)])
    rows, winners, counts = [], [], Counter()
    layouts = json.loads(DATA.read_text())['layouts']
    for wall_round, layout in product((1,2), layouts):
        wall_cells = [tuple(c) for c in layout['walls']]
        baseline = Engine(cfg, ('guard', 'striker'))
        opening = []
        predicted_gold, predicted_factories = 100, 0
        for rnd in (1,2):
            walls = wall_cells if rnd == wall_round else []
            cost = len(walls)*cfg.wall_cost
            new_factories = (predicted_gold-cost)//20
            actions = [dict(op='build_wall',x=x,y=y) for x,y in walls]
            actions += [dict(op='buy_factory') for _ in range(new_factories)]
            enemy = [dict(op='buy_factory') for _ in range((5,4)[rnd-1])]
            rr = baseline.play_round([actions, enemy])
            assert all(e.get('accepted', True) for r in rr for e in r['event'])
            route = shortest_path(g.width,g.height,set(wall_cells) if rnd>=wall_round else set(),g.spawn,g.base)
            predicted_gold = predicted_gold-cost-5*new_factories+15*predicted_factories+len(route)-1
            predicted_factories += new_factories
            assert baseline.players[0].gold == predicted_gold
            assert baseline.players[0].n_factories == predicted_factories
            opening.append(dict(round=rnd,actions=actions,records=rr))
        gold3, factories3 = predicted_gold, predicted_factories
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
                    cost = sum(cfg.turrets[t].cost for t in kinds)
                    if cost > gold3:
                        local['unaffordable_round3'] += 1
                        continue
                    factories = (gold3-cost)//g.factory_cost
                    next_gold = gold3-cost-5*factories+15*factories3+length
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
                    winners.append(dict(wall_round=wall_round, gold3=gold3, factories3=factories3, opening=opening, layout=layout['id'], walls=[list(c) for c in wall_cells],
                        turrets=[dict(type=t,x=x,y=y) for (x,y),t in zip(positions,kinds)],
                        cost=cost,total_cost=cost+len(wall_cells)*cfg.wall_cost,total_factories=factories3+factories,round3_new_factories=factories,round4_gold=next_gold,
                        path=[list(c) for c in route],length=length,combat=vars(combat)))
        counts.update(local)
        rows.append(dict(wall_round=wall_round,layout=layout['id'],gold3=gold3,factories3=factories3,counts=dict(local)))
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),wall_round=wall_round,layout=layout['id'],counts=dict(local))),flush=True)
    winners.sort(key=lambda w:(-w['total_factories'],-w['round4_gold'],w['total_cost'],w['wall_round'],w['layout'],json.dumps(w['turrets'],sort_keys=True)))
    selected, seen = [], set()
    for w in winners:
        key = (w['wall_round'],w['layout'])
        if key not in seen and len(selected)<8:
            selected.append(w)
            seen.add(key)
    for witness in selected:
        engine = Engine(cfg, ('guard', 'striker'))
        for record in witness['opening']:
            rnd = record['round']
            engine.play_round([record['actions'],[dict(op='buy_factory') for _ in range((5,4)[rnd-1])]])
        actions = [dict(op='build_turret',**t) for t in witness['turrets']]
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
        scope='All one/two-turret maps of the three stated types on twelve declared wall layouts built in round one or two. A component search, not a full-game strength claim.')
    with Path(args.output).open('x') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('selected','input_sha256','layouts')}),flush=True)


if __name__ == '__main__':
    main()

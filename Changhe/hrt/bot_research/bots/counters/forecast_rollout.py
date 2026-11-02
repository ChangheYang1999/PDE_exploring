"""One-step deviations evaluated by complete known-policy continuations.

Every rollout starts from a new Engine reconstructed from the public
observation. The real engine, opponent instance and hidden submissions are
never accessed. The opponent is the archived public Planner v3. Future own
moves follow a fixed forecast-defense policy; this restriction is substantial.
The search is a counter to that known policy, not a general game solution.
"""
from __future__ import annotations
from td_game.config import config_from_dict
from td_game.engine import Engine
from bot_research.bots.counters.forecast_timing import predict
from bot_research.bots.counters.snapshots.lead_planner_003 import Planner, WALLS
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.defense_plan import defend, saturate
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.bots.economy.frozen.v2.threat import active_types


def reconstruct(observation):
    """Rebuild observable state. Next roster IDs may differ after an empty roster.

    IDs are bookkeeping labels. The policies here ignore them; every new ID
    remains distinct among active entries, preserving order and expiration.
    """
    game = Engine(config_from_dict(observation['rules']),
                  tuple(p['name'] for p in observation['players']))
    game.round = observation['round'] - 1
    game.players = [player_from_snapshot(p) for p in observation['players']]
    return game


class ForecastRollout:
    def __init__(self, model_lam=1.0, model_kappa=4.0, saturate_round=14,
                 max_factories=80, max_search_round=12, max_candidates=12,
                 max_minions=200):
        self.model = Planner(lam=float(model_lam), kappa=float(model_kappa))
        self.saturate_round = int(saturate_round)
        self.max_factories = int(max_factories)
        self.max_search_round = int(max_search_round)
        self.max_candidates = int(max_candidates)
        self.max_minions = int(max_minions)
        self.trace = []

    def complete_actions(self, obs, enemy, sequence=()):
        """Spend on the proposed attack, exact forecast defense, then factories."""
        rnd = obs['round']
        rules = obs['rules']
        me = obs['players'][obs['player']]
        gold = me['gold'] - sum(rules['minions'][t]['cost'] for t in sequence)
        if gold < 0:
            raise ValueError('Unaffordable local candidate.')
        actions = [{'op': 'buy_minion', 'type': t} for t in sequence]
        buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        threat = [e.type for e in enemy.roster if e.active(rnd)]
        more, buildings, gold, _ = defend(buildings, gold, threat, 0, rules, reserve=1600)
        actions += more
        if rnd >= self.saturate_round:
            more, buildings, gold, _ = saturate(buildings, gold, 1500, rules)
            actions += more
        if rnd < 48:
            count = min(self.max_factories, gold // rules['globals']['factory_cost'])
            actions += [{'op': 'buy_factory'}] * count
        return actions

    def choices(self, obs, enemy):
        rules = obs['rules']
        me = obs['players'][obs['player']]
        own_types = active_types(me['roster'], obs['round'])
        model = MapModel([(b.x, b.y, b.type) for b in enemy.buildings], rules)
        baseline = simulate(model, own_types, rules)[1]
        scored = []
        for tier, spec in rules['minions'].items():
            cap = min(self.max_minions, me['gold'] // spec['cost'])
            for count in sorted({1, 2, 4, 8, cap // 4, cap // 2, cap}):
                if count <= 0 or count > cap:
                    continue
                sequence = (tier,) * count
                gain = simulate(model, own_types + list(sequence), rules)[1] - baseline
                if gain > 0:
                    cost = count * spec['cost']
                    scored.append((gain / cost, gain, -cost, sequence))
        # Always keep the no-purchase continuation. The finite attack candidate
        # filter is deliberately explicit; it can miss a profitable deviation.
        scored.sort(reverse=True)
        return [()] + [row[-1] for row in scored[:max(0, self.max_candidates - 1)]]

    @staticmethod
    def saturated(game, opponent_side):
        rules = game.config.to_dict()
        threshold = max(m['hp'] for m in rules['minions'].values())
        if not set(WALLS).issubset({(b.x, b.y) for b in game.players[opponent_side].buildings}):
            return False
        return all(MapModel([(b.x, b.y, b.type) for b in p.buildings], rules).splash_total >= threshold
                   for p in game.players)

    def continuation(self, obs, initial, prediction):
        side = obs['player']
        game = reconstruct(obs)
        actions = [initial, prediction] if side == 0 else [prediction, initial]
        rejected = 0
        rounds = 0
        while True:
            records = game.play_round(actions)
            rounds += 1
            rejected += sum(1 for row in records for e in row['event']
                            if e['kind'] == 'action' and not e['accepted'])
            if rejected:
                raise ValueError('A rollout action was rejected by the unchanged engine.')
            if game.result is not None or self.saturated(game, 1-side):
                break
            current = game.observation(side)
            prediction, enemy = predict(current, self.model)
            own = self.complete_actions(current, enemy)
            actions = [own, prediction] if side == 0 else [prediction, own]
        hp = [p.hp for p in game.players]
        if game.result is not None:
            winner = game.result['winner']
            outcome = 0 if winner is None else (1 if winner == side else -1)
            reason = game.result['reason']
        else:
            diff = hp[side] - hp[1-side]
            outcome = (diff > 0) - (diff < 0)
            reason = 'both maps saturated under fixed continuation'
        # Winning and drawing dominate losing; the remaining ordering rewards
        # final HP margin and survival among continuations with the same result.
        score = (outcome, hp[side] - hp[1-side], hp[side])
        return score, {'score': list(score), 'hp': hp, 'end_round': game.round,
                       'reason': reason, 'simulated_rounds': rounds}

    def decide(self, obs):
        prediction, enemy = predict(obs, self.model)
        sequences = self.choices(obs, enemy) if obs['round'] <= self.max_search_round else [()]
        candidates = []
        if len(sequences) == 1:
            actions = self.complete_actions(obs, enemy)
            self.trace.append({'round': obs['round'], 'predicted_actions': prediction,
                               'evaluated_continuations': 0, 'selected_sequence': []})
            return actions
        best = None
        selected = None
        for sequence in sequences:
            actions = self.complete_actions(obs, enemy, sequence)
            score, detail = self.continuation(obs, actions, prediction)
            cost = sum(obs['rules']['minions'][t]['cost'] for t in sequence)
            key = score + (-cost,)
            candidates.append({'sequence': list(sequence), 'cost': cost, **detail})
            if best is None or key > best:
                best, selected = key, (actions, sequence)
        self.trace.append({'round': obs['round'], 'predicted_actions': prediction,
                           'evaluated_continuations': len(candidates), 'candidates': candidates,
                           'selected_sequence': list(selected[1])})
        return selected[0]


def make(**parameters):
    return ForecastRollout(**parameters).decide

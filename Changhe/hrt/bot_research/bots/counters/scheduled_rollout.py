"""Another exact policy-improvement pass around a fixed attack schedule.

The baseline action is always included. Unit mode additionally admits every
single affordable tier, even when it deals no immediate damage. This tests
whether the immediate-gain filter hides useful future pressure. Both modes
use complete original-engine continuations against a named frozen policy.
"""
from __future__ import annotations
from bot_research.bots.counters.known_policy import KnownRollout
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.bots.economy.frozen.v2.threat import active_types


class ScheduledRollout(KnownRollout):
    def __init__(self, baseline_schedule=(), candidate_mode='filtered', **parameters):
        super().__init__(**parameters)
        if candidate_mode not in ('filtered', 'unit', 'unit_filtered'):
            raise ValueError('Unknown candidate mode.')
        self.baseline_schedule = tuple((int(r), str(t), int(n)) for r, t, n in baseline_schedule)
        self.candidate_mode = candidate_mode

    def baseline_sequence(self, obs):
        gold = obs['players'][obs['player']]['gold']
        sequence = []
        for rnd, tier, requested in self.baseline_schedule:
            if rnd == obs['round']:
                cost = obs['rules']['minions'][tier]['cost']
                count = min(max(0, requested), gold // cost)
                sequence += [tier] * count
                gold -= count * cost
        return tuple(sequence)

    def complete_actions(self, obs, enemy, sequence=None):
        if sequence is None:
            sequence = self.baseline_sequence(obs)
        return super().complete_actions(obs, enemy, sequence)

    def choices(self, obs, enemy):
        if self.candidate_mode == 'filtered':
            sequences = super().choices(obs, enemy)
        else:
            gold = obs['players'][obs['player']]['gold']
            sequences = [()] + [(tier,) for tier, spec in obs['rules']['minions'].items()
                                if spec['cost'] <= gold]
        rules = obs['rules']
        current = active_types(obs['players'][obs['player']]['roster'], obs['round'])
        model = MapModel([(b.x, b.y, b.type) for b in enemy.buildings], rules)
        old_damage = simulate(model, current, rules)[1]
        self._choice_gains = {sequence: simulate(model, current + list(sequence), rules)[1] - old_damage
                              for sequence in sequences}
        if self.candidate_mode == 'unit_filtered':
            sequences = [sequence for sequence in sequences if not sequence or self._choice_gains[sequence] > 0]
        baseline = self.baseline_sequence(obs)
        if baseline not in self._choice_gains:
            self._choice_gains[baseline] = simulate(model, current + list(baseline), rules)[1] - old_damage
        if baseline not in sequences:
            sequences.append(baseline)
        return sequences

    def decide(self, obs):
        self._choice_gains = {}
        actions = super().decide(obs)
        self.trace[-1]['baseline_sequence'] = list(self.baseline_sequence(obs))
        if self.trace[-1]['evaluated_continuations'] == 0:
            self.trace[-1]['selected_sequence'] = list(self.baseline_sequence(obs))
        self.trace[-1]['selected_immediate_gain'] = self._choice_gains.get(tuple(self.trace[-1]['selected_sequence']))
        return actions


def make(**parameters):
    return ScheduledRollout(**parameters).decide

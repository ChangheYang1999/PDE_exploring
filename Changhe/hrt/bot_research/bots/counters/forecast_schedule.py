"""A cheap, frozen attack schedule extracted from the first rollout counter win.

Schedule: one tier2 in rounds 1 and 5, one tier4 in round 9, one tier5 in
round 12. Defense still forecasts the archived public Planner v3. This is a
known-policy counter, with no claim of robustness to different opponents.
"""
from __future__ import annotations
from bot_research.bots.counters.forecast_rollout import ForecastRollout
from bot_research.bots.counters.forecast_timing import predict

DEFAULT_SCHEDULE = ((1, 'tier2', 1), (5, 'tier2', 1),
                    (9, 'tier4', 1), (12, 'tier5', 1))


class ForecastSchedule(ForecastRollout):
    def __init__(self, schedule=DEFAULT_SCHEDULE, **parameters):
        super().__init__(**parameters)
        self.schedule = tuple((int(r), str(t), int(n)) for r, t, n in schedule)

    def decide(self, obs):
        prediction, enemy = predict(obs, self.model)
        gold = obs['players'][obs['player']]['gold']
        sequence = []
        for rnd, tier, count in self.schedule:
            if rnd != obs['round']:
                continue
            cost = obs['rules']['minions'][tier]['cost']
            n = min(max(0, count), gold // cost)
            sequence += [tier] * n
            gold -= n * cost
        actions = self.complete_actions(obs, enemy, sequence)
        self.trace.append({'round': obs['round'], 'predicted_actions': prediction,
                           'selected_sequence': sequence})
        return actions


def make(**parameters):
    return ForecastSchedule(**parameters).decide

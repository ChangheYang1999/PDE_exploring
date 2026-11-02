"""Keep the screened attack opening until a public HP lead, then defend."""
from bot_research.bots.counters.budget_handoff import BudgetHandoff


class TriggeredBudgetHandoff(BudgetHandoff):
    def __init__(self, lead_from=6, lead_margin=0, **parameters):
        if 'deadline' in parameters:
            raise ValueError('This policy uses an HP trigger, not a fixed deadline.')
        super().__init__(deadline=50, **parameters)
        self.lead_from = int(lead_from)
        self.lead_margin = int(lead_margin)
        if not self.strike_round < self.lead_from <= 50 or self.lead_margin < 0:
            raise ValueError('The nonnegative-margin HP trigger must follow the strike round.')
        self.triggered_round = None

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        own_hp = observation['players'][side]['hp']
        enemy_hp = observation['players'][1-side]['hp']
        if (self.triggered_round is None and rnd >= self.lead_from
                and own_hp > enemy_hp + self.lead_margin):
            self.triggered_round = rnd
        # An unswitched decision uses the opening even at the last round.
        # After switching, the inherited comparison always selects defense.
        self.deadline = self.triggered_round if self.triggered_round is not None else rnd + 1
        actions = super().decide(observation)
        self.trace[-1].update(triggered_round=self.triggered_round,
                             trigger_hp_self=own_hp, trigger_hp_enemy=enemy_hp)
        return actions


def make(**parameters):
    return TriggeredBudgetHandoff(**parameters).decide

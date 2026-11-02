"""Two opponents that play the same opening and then diverge (development; hypothesis H12, written 2026-10-31T18:56Z).

    bot_research.experiments.lead.prefix_fork:@make?continuation="grow"|"strike"&fork_round=4&tier="tier3"&...

Rounds before fork_round: hrt-w3's maze_grower (layout, growth_rounds, bait as given; default the no-bait grower on the
lead_opening walls with growth 6, which best_v9e's twin loses by 1240 in g9a-g9d). From fork_round on, "grow" keeps
playing the same grower and "strike" plays hrt-w3's budget_timing with attack_round=fork_round (all gold on the given
tier in that round if its simulated gain is positive, then its defence envelope at budget_fraction of our gold and
factories).

Why the pair is useful (proved from determinism and the observation contract): an observation of round r depends only
on the actions of both players in rounds before r. Both continuations submit the same actions in rounds before
fork_round against the same deterministic bot (by induction on the round), so that bot receives identical
observations up to and including the decision of round fork_round and submits identical actions in rounds
1..fork_round against both. Whatever it buys in those rounds, it faces both continuations from the same position.
"""
from bot_research.bots.counters.budget_timing import BudgetTiming
from bot_research.bots.counters.maze_grower import MazeGrower


class PrefixFork:
    def __init__(self, continuation="grow", fork_round=4, tier="tier3", budget_fraction=0.65, layout="lead_opening",
                 growth_rounds=6, bait=None, bait_round=2, grow_tier="tier5"):
        if continuation not in ("grow", "strike"):
            raise ValueError("continuation must be grow or strike")
        self.continuation = continuation
        self.fork_round = int(fork_round)
        self.grower = MazeGrower(layout=layout, growth_rounds=growth_rounds, bait=bait, bait_round=bait_round,
                                 tier=grow_tier, factory_cap=2000, purchase_cap=1000)
        self.striker = BudgetTiming(attack_round=self.fork_round, tier=tier, budget_fraction=budget_fraction)

    def decide(self, observation):
        if observation["round"] < self.fork_round or self.continuation == "grow":
            return self.grower.decide(observation)
        return self.striker.decide(observation)


def make(**parameters):
    return PrefixFork(**parameters).decide

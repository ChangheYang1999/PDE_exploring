"""Keep the screened opening and choose a fixed fresh round-seven delegate."""
from bot_research.bots.counters.screened_roster_guarded import ScreenedRosterGuarded
from bot_research.bots.defense.frozen.v38.fortress import make as make_f38
from bot_research.bots.defense.frozen.v41.fortress import make as make_f41
from bot_research.bots.economy.frozen.v29.econ29 import make as make_v29


class ScreenedContinuationRepair(ScreenedRosterGuarded):
    def __init__(self, continuation='fortress41'):
        super().__init__(continuation='fortress38')
        if continuation == 'fortress41':
            self.delegate = make_f41()
        elif continuation == 'fortress38_full':
            self.delegate = make_f38(spec_share=1.0, big_threat=140)
        elif continuation == 'v29_g1':
            self.delegate = make_v29(free_fallback='zero', foreign_attack_from=11,
                doom='next', fac_cap=400, sat_reach=True, replan=True,
                foreign_sat_from=11, replan_gain=400, replan_base=True,
                own_in_layout='replan', own_min_s=1200, min_cap=3000,
                active_cap=4000, fill=True, fill_reserve=True, fill_threat=True,
                attack_from=7)
        else:
            raise ValueError('Unknown screened continuation.')


def make(**parameters):
    return ScreenedContinuationRepair(**parameters).decide

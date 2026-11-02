"""Commit in round four using a public, no-enemy-action HP projection."""
from copy import deepcopy
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import config_from_dict
from td_game.pathfinding import shortest_path
from bot_research.bots.counters.template_handoff import TemplateHandoff
from bot_research.bots.counters.guard_handoff import GuardHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot


def project_early(observation, actions):
    side, rnd = observation['player'], observation['round']
    cfg = config_from_dict(observation['rules'])
    own = player_from_snapshot(observation['players'][side])
    enemy = player_from_snapshot(observation['players'][1-side])
    for action in actions:
        if not apply_action(own, action, rnd, cfg)['accepted']:
            raise RuntimeError('The early proposal contains an illegal action.')
    def path(state):
        g = cfg.globals
        route = shortest_path(g.width, g.height, [(b.x,b.y) for b in state.buildings], tuple(g.spawn), tuple(g.base))
        if route is None:
            raise RuntimeError('A legal state must retain a route.')
        return route
    incoming = simulate_map(enemy, own, path(own), rnd, cfg).damage
    outgoing = simulate_map(own, enemy, path(enemy), rnd, cfg).damage
    has_gun = any(a == dict(op='build_turret',type='gun1',x=10,y=1) for a in actions)
    has_heavy = any(a == dict(op='buy_minion',type='tier4') for a in actions)
    lead = own.hp - incoming - enemy.hp + outgoing
    return dict(incoming_damage=incoming,outgoing_damage=outgoing,
                projected_lead=lead,projected_own_hp=own.hp-incoming,
                package_present=has_gun and has_heavy,
                choose_early=has_gun and has_heavy and own.hp-incoming>0 and lead>0)


class ProjectedLeadSelector:
    def __init__(self,mode='adaptive'):
        if mode not in ('adaptive','early','growth'):
            raise ValueError('Unknown selector mode.')
        self.mode=mode
        common=dict(layout='empty',growth_rounds=6,bait=[],bait_round=2,tier='tier5',factory_cap=2000,purchase_cap=1000)
        self.early=TemplateHandoff(**common,upgrade_round=9,strike_round=4,strike_tier='tier4',strike_count=1,max_new=120,numerator=1,denominator=2,lead_from=5,lead_margin=0,early_gun=True,planner='template')
        self.growth=GuardHandoff(**common,handoff_round=10,replan_iters=5000)
        self.selected=None
        self.trace=[]

    def decide(self,observation):
        rnd=observation['round'];projection=None
        if self.selected is None and rnd<4:
            early=self.early.decide(deepcopy(observation))
            growth=self.growth.decide(deepcopy(observation))
            if early!=growth:
                raise RuntimeError('The common three-round prefix diverged.')
            actions=early
        elif self.selected is None:
            if rnd==4:
                early=self.early.decide(deepcopy(observation))
                projection=project_early(observation,early)
                self.selected=('early' if projection['choose_early'] else 'growth') if self.mode=='adaptive' else self.mode
                actions=early if self.selected=='early' else self.growth.decide(deepcopy(observation))
            else:
                self.selected='growth'
                actions=self.growth.decide(deepcopy(observation))
        else:
            actions=getattr(self,self.selected).decide(deepcopy(observation))
        self.trace.append(dict(round=rnd,selected=self.selected,projection=projection))
        return actions


def make(**parameters):
    return ProjectedLeadSelector(**parameters).decide

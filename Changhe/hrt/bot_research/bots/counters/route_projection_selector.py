"""Gate the round-four early strike on a visible, extended enemy route."""
from copy import deepcopy
from td_game.config import config_from_dict
from td_game.pathfinding import shortest_path
from bot_research.bots.counters.projected_lead_selector import (
    ProjectedLeadSelector, project_early,
)


def route_feature(observation):
    cfg = config_from_dict(observation['rules']).globals
    enemy = observation['players'][1 - observation['player']]
    spawn, base = tuple(cfg.spawn), tuple(cfg.base)
    blocked = [(building['x'], building['y']) for building in enemy['buildings']]
    route = shortest_path(cfg.width, cfg.height, blocked, spawn, base)
    if route is None:
        raise ValueError('The visible enemy map must retain a route.')
    length = len(route) - 1
    distance = abs(spawn[0] - base[0]) + abs(spawn[1] - base[1])
    return dict(enemy_route_length=length, unobstructed_distance=distance,
                extended_enemy_route=length > distance)


class RouteGatedSelector(ProjectedLeadSelector):
    def decide(self, observation):
        if self.selected is not None or observation['round'] != 4:
            return super().decide(observation)
        early = self.early.decide(deepcopy(observation))
        projection = project_early(observation, early)
        projection['positive_projection'] = projection['choose_early']
        projection.update(route_feature(observation))
        projection['choose_early'] = (
            projection['positive_projection'] and projection['extended_enemy_route']
        )
        if self.mode == 'adaptive':
            self.selected = 'early' if projection['choose_early'] else 'growth'
        else:
            self.selected = self.mode
        actions = early if self.selected == 'early' else self.growth.decide(deepcopy(observation))
        self.trace.append(dict(round=4, selected=self.selected, projection=projection))
        return actions


def make(**parameters):
    return RouteGatedSelector(**parameters).decide

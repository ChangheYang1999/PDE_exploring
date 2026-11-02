"""A fixed guard-growth opening followed by a frozen map-aware defender."""
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.screened_guard_maze import ScreenedGuardMaze
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.defense.frozen.v34.fortress import make as make_defender


class GuardHandoff:
    def __init__(self,handoff_round=12,replan_iters=5000,**parameters):
        self.handoff_round=int(handoff_round)
        if not 10<=self.handoff_round<=50:raise ValueError('Handoff follows the round9 gun extension.')
        if int(parameters.get('upgrade_round',9))!=9:raise ValueError('This opening extends the guard in round9.')
        parameters['upgrade_round']=9
        self.opening=ScreenedGuardMaze(**parameters)
        self.defender=make_defender(attack='none',round1_poke=0,replan_iters=int(replan_iters))
        self.rejected_proposals=[]

    def decide(self,observation):
        if observation['round']<self.handoff_round:return self.opening.decide(observation)
        proposed=self.defender(observation);state=player_from_snapshot(observation['players'][observation['player']]);cfg=config_from_dict(observation['rules']);actions=[]
        for action in proposed:
            event=apply_action(state,action,observation['round'],cfg)
            if event['accepted']:actions.append(action)
            else:self.rejected_proposals.append(dict(round=observation['round'],action=action,reason=event['reason']))
        return actions


def make(**parameters):return GuardHandoff(**parameters).decide

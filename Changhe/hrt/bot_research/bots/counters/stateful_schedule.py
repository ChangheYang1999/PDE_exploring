"""A declared purchase schedule with one persistent public opponent model.

The inherited policy predicts once per reached round, including rounds before
its first scheduled purchase. The target must start in its ordinary fresh
state at standard round 1. This wrapper does not implement scenario warmup.
"""
from __future__ import annotations
from bot_research.bots.counters.public_factory import DEFAULT_MODEL
from bot_research.bots.counters.public_schedule import PublicSchedule
from bot_research.bots.counters.stateful_public import PersistentFactoryModel


class StatefulSchedule(PublicSchedule):
    def __init__(self, model_spec=DEFAULT_MODEL, model_parameters=None, **parameters):
        super().__init__(model_spec=model_spec, model_parameters=model_parameters, **parameters)
        self.model = PersistentFactoryModel(model_spec, model_parameters)


def make(**parameters):
    return StatefulSchedule(**parameters).decide

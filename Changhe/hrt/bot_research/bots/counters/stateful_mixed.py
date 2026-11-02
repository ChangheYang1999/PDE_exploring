"""A mixed-tier timing search with a retained public opponent model.

The model starts at the target's ordinary round-one state and advances once
per reached round. Prefix scenarios require separate model-state warmup.
"""
from __future__ import annotations
from bot_research.bots.counters.public_factory import DEFAULT_MODEL
from bot_research.bots.counters.mixed_timing import MixedTiming
from bot_research.bots.counters.stateful_public import PersistentFactoryModel


class StatefulMixed(MixedTiming):
    def __init__(self, model_spec=DEFAULT_MODEL, model_parameters=None, **parameters):
        super().__init__(**parameters)
        self.model = PersistentFactoryModel(model_spec, model_parameters)


def mixed(**parameters):
    return StatefulMixed(**parameters).decide

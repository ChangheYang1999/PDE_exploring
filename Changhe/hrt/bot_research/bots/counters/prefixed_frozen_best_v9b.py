"""Known call-through prefixes for the immutable best_v9b module.

Target and private model have separate state. Both are called every round,
including rounds whose output is replaced by the declared opening.
"""
from bot_research.experiments.lead.frozen import best_v9b as best
from bot_research.bots.counters.prefixed_v4 import OpeningPolicy
from bot_research.bots.counters.free_forecast import FreeForecast

MODEL = 'bot_research.bots.counters.prefixed_frozen_best_v9b:@private_model'


def target(scenario=None):
    return OpeningPolicy(best.decide, scenario)


def private_model(scenario=None):
    return OpeningPolicy(best.make(), scenario)


def timing(scenario=None, **parameters):
    counter = FreeForecast(model_spec=MODEL,
                           model_parameters={'scenario': scenario}, **parameters)
    return OpeningPolicy(counter, scenario).decide


def schedule(scenario=None, **parameters):
    return timing(scenario=scenario, **parameters)

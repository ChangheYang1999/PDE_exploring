"""Known-prefix tests of the frozen best entry point and an independent model.

The target calls best.decide. Its private model owns a separate best.make()
instance. Both execute every round before the opening override is selected.
A campaign must freeze best.py and its dependency closure before use.
"""
from bot_research.bots import best
from bot_research.bots.counters.prefixed_v4 import OpeningPolicy
from bot_research.bots.counters.free_forecast import FreeForecast

MODEL = 'bot_research.bots.counters.prefixed_best_v9b:@private_model'


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

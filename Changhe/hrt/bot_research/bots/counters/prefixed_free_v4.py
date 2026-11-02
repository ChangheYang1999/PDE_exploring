"""Known-prefix V4 counter, differing only in its defensive fallback."""
from bot_research.bots.counters.prefixed_v4 import OpeningPolicy, MODEL
from bot_research.bots.counters.free_forecast import FreeForecast


def timing(scenario=None, **parameters):
    counter = FreeForecast(model_spec=MODEL, model_parameters={'scenario': scenario}, **parameters)
    return OpeningPolicy(counter, scenario).decide


def schedule(scenario=None, **parameters):
    return timing(scenario=scenario, **parameters)

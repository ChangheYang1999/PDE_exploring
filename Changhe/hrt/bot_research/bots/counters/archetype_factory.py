"""Factory-spec adapter for the predeclared deterministic archetypes."""
from bot_research.bots.counters.archetypes import make as make_archetype


def make(name):
    return make_archetype(name).decide

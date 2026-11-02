"""A public observation-guarded trajectory with a permanent fallback.

The data file is part of this policy, not information about a live opponent.
No target decisions are simulated. Exact structural comparisons protect
against using a recorded action list on a different observed state.
"""
from __future__ import annotations
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from bot_research.bots.defense.frozen.v15.fortress import make as fortress15
from bot_research.bots.economy.frozen.v9.econ9 import make as economy9


def canonical_observation(observation):
    side = observation['player']
    players = [{key: deepcopy(value) for key, value in observation['players'][p].items()
                if key != 'name'} for p in (side, 1 - side)]
    # Convert configuration tuples to their JSON representation.
    return json.loads(json.dumps({'round': observation['round'],
                                  'rules': observation['rules'], 'players': players},
                                 allow_nan=False))


class CompiledPlan:
    def __init__(self, plan_file, plan_sha256, fallback='fortress15', fallback_parameters=None):
        path = Path(plan_file)
        if path.is_absolute() or '..' in path.parts or path.parts[:4] != ('bot_research', 'bots', 'counters', 'plans'):
            raise ValueError('Use a fixed policy data file in the counters plans directory.')
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != plan_sha256:
            raise ValueError('Compiled policy data does not match its declared digest.')
        data = json.loads(raw)
        if data['schema_version'] != 1:
            raise ValueError('Unknown compiled policy data schema.')
        self.rounds = {entry['round']: entry for entry in data['rounds']}
        if sorted(self.rounds) != list(range(1, len(data['rounds']) + 1)):
            raise ValueError('The plan must have exactly one entry per consecutive round.')
        factories = {'fortress15': fortress15, 'economy9': economy9, 'idle': lambda **kw: lambda obs: []}
        if fallback not in factories:
            raise ValueError('Unknown fallback.')
        self.fallback_name = fallback
        self.fallback_factory = factories[fallback]
        self.fallback_parameters = dict(fallback_parameters or {})
        self.fallback = self.fallback_factory(**self.fallback_parameters)
        self.switched = False
        self.trace = []

    def decide(self, observation):
        rnd = observation['round']
        if rnd == 1:
            self.switched = False
            self.trace = []
            self.fallback = self.fallback_factory(**self.fallback_parameters)
        entry = self.rounds.get(rnd)
        matched = not self.switched and entry is not None and canonical_observation(observation) == entry['observation']
        if matched:
            actions = deepcopy(entry['actions'])
        else:
            self.switched = True
            actions = self.fallback(observation)
        self.trace.append({'round': rnd, 'plan_matched': matched,
                           'fallback': self.fallback_name if self.switched else None})
        return actions


def make(**parameters):
    return CompiledPlan(**parameters).decide

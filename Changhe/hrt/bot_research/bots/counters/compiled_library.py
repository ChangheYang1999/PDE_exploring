"""Compatible public-observation plans, with permanent mismatch fallback."""
from __future__ import annotations
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from bot_research.bots.counters.compiled_plan import canonical_observation
from bot_research.bots.defense.frozen.v15.fortress import make as fortress15
from bot_research.bots.economy.frozen.v9.econ9 import make as economy9


class CompiledLibrary:
    def __init__(self, data_file, data_sha256, fallback='fortress15', fallback_parameters=None):
        path = Path(data_file)
        if path.is_absolute() or '..' in path.parts or path.parts[:4] != ('bot_research', 'bots', 'counters', 'plans'):
            raise ValueError('Use fixed policy data in the counters plans directory.')
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != data_sha256:
            raise ValueError('Compiled library differs from its declared digest.')
        data = json.loads(raw)
        if data['schema_version'] != 2 or not data['plans']:
            raise ValueError('Unsupported or empty compiled library.')
        self.plans = {}
        for plan in data['plans']:
            key = plan['id']
            table = {entry['round']: entry for entry in plan['rounds']}
            if key in self.plans or sorted(table) != list(range(1, len(plan['rounds']) + 1)):
                raise ValueError('Duplicate plan or nonconsecutive rounds.')
            self.plans[key] = table
        factories = {'fortress15': fortress15, 'economy9': economy9, 'idle': lambda **kw: lambda obs: []}
        if fallback not in factories:
            raise ValueError('Unknown fallback.')
        self.fallback_name = fallback
        self.fallback_factory = factories[fallback]
        self.fallback_parameters = dict(fallback_parameters or {})
        self.reset()

    def reset(self):
        self.active = list(self.plans)
        self.switched = False
        self.fallback = self.fallback_factory(**self.fallback_parameters)
        self.trace = []

    def decide(self, observation):
        rnd = observation['round']
        if rnd == 1:
            self.reset()
        if not self.switched:
            observed = canonical_observation(observation)
            self.active = [key for key in self.active if rnd in self.plans[key]
                           and self.plans[key][rnd]['observation'] == observed]
            self.switched = not self.active
        if self.switched:
            actions = self.fallback(observation)
        else:
            actions = self.plans[self.active[0]][rnd]['actions']
            if any(self.plans[key][rnd]['actions'] != actions for key in self.active[1:]):
                raise ValueError('Conflicting public histories in compiled data.')
            actions = deepcopy(actions)
        self.trace.append({'round': rnd, 'active': list(self.active),
                           'fallback': self.fallback_name if self.switched else None})
        return actions


def make(**parameters):
    return CompiledLibrary(**parameters).decide

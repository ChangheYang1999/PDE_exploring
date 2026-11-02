"""One independent match in one fresh Python interpreter.

Input and output are JSON files. This runner does not import the lead harness.
It supports original loader functions and explicit factory specifications.
"""
from __future__ import annotations
import argparse
import importlib
import json
from copy import deepcopy
from pathlib import Path
from urllib.parse import parse_qsl

from td_bots.protocol import load_bot
from bot_research.bots.counters.archetypes import Archetype, Profile
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.artifact_io import atomic_json


class CallableBot:
    def __init__(self, function):
        self.decide = function


def resolve(description):
    if 'profile' in description:
        values = dict(description['profile'])
        values['roster'] = tuple(values['roster'])
        return Archetype(Profile(**values))
    spec = description['spec']
    module_name, _, function = spec.partition(':')
    if not function.startswith('@'):
        return load_bot(spec)
    name, _, query = function[1:].partition('?')
    parameters = {}
    for key, text in parse_qsl(query, keep_blank_values=True):
        try:
            parameters[key] = json.loads(text)
        except json.JSONDecodeError:
            parameters[key] = text
    return CallableBot(getattr(importlib.import_module(module_name), name)(**parameters))


class OpeningPrefix:
    """A legal prescribed prefix; the underlying policy starts afterward.

    Skipping calls can expose a policy's initialization assumptions. Such runs
    are labeled continuation stress tests and excluded from standard strength.
    """
    def __init__(self, bot, opening):
        self.bot = bot
        self.opening = opening

    def decide(self, observation):
        if observation['round'] <= len(self.opening):
            return deepcopy(self.opening[observation['round'] - 1])
        return self.bot.decide(observation)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--job', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    job = json.loads(Path(args.job).read_text())
    bots = [resolve(description) for description in job['bots']]
    if 'prefixes' in job:
        bots = [OpeningPrefix(bot, prefix) for bot, prefix in zip(bots, job['prefixes'])]
    result = evaluate(tuple(job['names']), bots=bots, replay_path=job.get('replay_path'),
                      condition=job['condition'])
    side = job['condition'].get('candidate_side')
    if side is not None:
        winner = result['result']['winner']
        result['candidate_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
    atomic_json(args.output, result, exclusive=True)


if __name__ == '__main__':
    main()

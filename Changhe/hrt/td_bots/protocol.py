"""Adapter boundary: isolate observations, normalize JSON, report bot errors."""
from __future__ import annotations

import importlib
import json
from copy import deepcopy
from typing import Any, Protocol


class Bot(Protocol):
    def decide(self, observation: dict[str, Any]) -> list[dict[str, Any]]: ...


def load_bot(spec: str) -> Bot:
    """Load module or module:function, for example my_bot:decide."""
    module_name, separator, function_name = spec.partition(":")
    module = importlib.import_module(module_name)
    function = getattr(module, function_name if separator else "decide")
    if not callable(function):
        raise ValueError(f"{spec} does not provide a callable decide function")

    class FunctionBot:
        def decide(self, observation):
            return function(observation)

    return FunctionBot()


def idle(observation: dict[str, Any]) -> list[dict[str, Any]]:
    """Return empty submissions for infrastructure smoke runs."""
    return []


def collect_actions(bots: list[Bot], observations: list[dict]) -> tuple[list[list], list[str | None]]:
    """Collect both submissions without applying either to the world."""
    if len(bots) != 2 or len(observations) != 2:
        raise ValueError("two bots and observations required")
    # Create both copies before invoking either bot, including nested state.
    inputs = [deepcopy(observation) for observation in observations]
    submissions, errors = [], []
    for bot, observation in zip(bots, inputs):
        try:
            actions = bot.decide(observation)
            if not isinstance(actions, list):
                raise ValueError("decide must return a list of JSON actions")
            # Unsupported objects/nonfinite numbers invalidate the entire return.
            # JSON primitives within the list remain individual rejected actions.
            actions = json.loads(json.dumps(actions, allow_nan=False))
            submissions.append(actions)
            errors.append(None)
        except Exception as exc:
            submissions.append([])
            errors.append(f"{type(exc).__name__}: {exc}")
    return submissions, errors

"""Authoritative single-match runner for bot research.

Every match is played by the unchanged ``td_game.runner.run_match`` on the
bundled rules (``td_game.config.balanced_config``). This module only

* resolves bot specifications into fresh callables,
* wraps each callable with a timer (the wrapper passes the observation
  through unchanged and returns the bot's list unchanged),
* reads the authoritative JSONL log written by ``run_match`` and extracts
  outcomes, HP difference, ending round, rejected actions and bot errors.

Bot specification strings
-------------------------
``module:function``            the function is used directly (module state is shared
                               between both sides of a self-play match; bots that
                               keep state must key it by ``observation["player"]``).
``module:@factory``            ``factory()`` is called once per side per match and
                               must return a ``decide`` callable (fresh state).
``module:@factory?k=v&k2=v2``  as above with keyword arguments; values are parsed
                               as JSON when possible, otherwise kept as strings.

Scenarios
---------
A scenario replaces the first ``k`` rounds of both players' submissions with
scripted openings (see ``bot_research.harness.scenarios``). The scripted list is
computed from a private deep copy of the observation before the bot is called,
so a bot cannot change it by mutating its observation; the bot is still called
in those rounds (it sees every observation) but its return is discarded and an
exception it raises there is recorded in ``scenario_errors`` instead of
replacing the scripted list. This only changes the initial position, never the
rules.

Version records
---------------
Each row records the full SHA-256 of both entry modules, a ``version`` digest
per side (all ``.py`` files in the entry module's directory plus
``bot_research/harness/``), and the hashes of every loaded module from
``bot_research``, ``td_game`` and ``td_bots``. The digests are taken before and
after the match; ``source_changed`` is true if any of them moved.
"""
from __future__ import annotations

import ast
import copy
import hashlib
import importlib
import json
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any, Callable
from urllib.parse import parse_qsl

from td_game.config import balanced_config
from td_game.runner import run_match

ROOT = Path(__file__).resolve().parents[2]


def _parse_value(text: str) -> Any:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


def resolve_spec(spec: str) -> Callable[[dict], list]:
    """Return a fresh decide callable for ``spec`` (see module docstring)."""
    module_name, _, rest = spec.partition(":")
    function_name, _, query = rest.partition("?")
    module = importlib.import_module(module_name)
    if function_name.startswith("@"):
        factory = getattr(module, function_name[1:])
        kwargs = {k: _parse_value(v) for k, v in parse_qsl(query, keep_blank_values=True)}
        decide = factory(**kwargs)
    else:
        if query:
            raise ValueError("parameters require the module:@factory form")
        decide = getattr(module, function_name or "decide")
    if not callable(decide):
        raise ValueError(f"{spec} does not resolve to a callable")
    return decide


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module_hash(spec: str) -> str:
    """Full SHA-256 of the bot entry module source."""
    module_name = spec.partition(":")[0]
    module = importlib.import_module(module_name)
    path = getattr(module, "__file__", None)
    if not path:
        return "unknown"
    return _file_hash(Path(path))


def _module_file(name: str) -> Path | None:
    base = ROOT.joinpath(*name.split("."))
    for cand in (base.with_suffix(".py"), base / "__init__.py"):
        if cand.is_file():
            return cand.resolve()
    return None


def import_closure(module_name: str) -> list[Path]:
    """Source files of ``module_name`` and every bot_research module it imports, transitively
    (static parse of import statements, including package __init__ files)."""
    seen: dict[str, Path] = {}
    todo = [module_name]
    while todo:
        name = todo.pop()
        if name in seen or not name.startswith("bot_research"):
            continue
        path = _module_file(name)
        if path is None:
            continue
        seen[name] = path
        parts = name.split(".")
        for i in range(1, len(parts)):
            todo.append(".".join(parts[:i]))
        package = name if path.name == "__init__.py" else ".".join(parts[:-1])
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                todo.extend(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    pkg = package.split(".")
                    pkg = pkg[:len(pkg) - (node.level - 1)]
                    target = ".".join(pkg + ([node.module] if node.module else []))
                else:
                    target = node.module or ""
                todo.append(target)
                todo.extend(f"{target}.{a.name}" for a in node.names)
    return sorted(set(seen.values()))


def spec_version(spec: str) -> str:
    """Digest of the entry module's static bot_research import closure plus bot_research/harness/*.py."""
    module_name = spec.partition(":")[0]
    files = set(import_closure(module_name)) | {f.resolve() for f in (ROOT / "bot_research" / "harness").glob("*.py")}
    if not files:
        return "unknown"
    digest = hashlib.sha256()
    for f in sorted(files):
        rel = f.relative_to(ROOT).as_posix() if ROOT in f.parents else f.name
        digest.update(f"{rel}\0{_file_hash(f)}\n".encode())
    return digest.hexdigest()


def loaded_sources() -> dict:
    """Hashes of loaded modules from bot_research, td_game and td_bots (relative paths)."""
    out = {}
    for name, module in list(sys.modules.items()):
        if not name.split(".")[0] in ("bot_research", "td_game", "td_bots"):
            continue
        path = getattr(module, "__file__", None)
        if not path:
            continue
        p = Path(path).resolve()
        if ROOT in p.parents and p.exists():
            out[p.relative_to(ROOT).as_posix()] = _file_hash(p)
    return dict(sorted(out.items()))


class TimedBot:
    """Adapter object with ``decide``; records wall time per call."""

    def __init__(self, decide: Callable[[dict], list], override: Callable[[dict], list | None] | None = None):
        self._decide = decide
        self._override = override
        self.times: list[float] = []
        self.scenario_errors: list[dict] = []

    def decide(self, observation: dict) -> list:
        scripted = None
        if self._override is not None:
            scripted = self._override(copy.deepcopy(observation))
        start = time.perf_counter()
        try:
            actions = self._decide(observation)
        except Exception as exc:
            if scripted is None:
                raise
            self.scenario_errors.append({"round": observation.get("round"),
                                         "error": f"{type(exc).__name__}: {exc}"})
            actions = None
        finally:
            self.times.append(time.perf_counter() - start)
        return scripted if scripted is not None else actions


def read_log(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream]


def summarize_log(records: list[dict]) -> dict:
    """Extract per-player statistics from an authoritative match log."""
    rounds: dict[int, dict[int, dict]] = {}
    for record in records:
        rounds.setdefault(record["round"], {})[record["player"]] = record
    last = max(rounds)
    final = rounds[last]
    result = final[0].get("result")
    players = []
    for p in (0, 1):
        rejected = Counter()
        accepted = Counter()
        errors = []
        damage_dealt = 0
        hits = 0
        spent = Counter()
        first_damage_taken_round = None
        for r in range(1, last + 1):
            for event in rounds[r][p]["event"]:
                kind = event["kind"]
                if kind == "action":
                    action = event["action"]
                    op = action.get("op") if isinstance(action, dict) else None
                    if event["accepted"]:
                        accepted[str(op)] += 1
                        key = op if op in ("buy_factory", "build_wall") else f"{op}:{action.get('type')}"
                        spent[key] += event.get("cost", 0)
                    else:
                        rejected[event.get("reason", "?")] += 1
                elif kind == "bot_error":
                    errors.append({"round": r, "reason": event.get("reason")})
                elif kind == "combat":
                    damage_dealt += event["damage_dealt"]
                    hits += event["outgoing_hits"]
                    if event["base_damage"] > 0 and first_damage_taken_round is None:
                        first_damage_taken_round = r
        snap = final[p]["snapshot"]
        players.append({
            "name": snap["name"], "hp": snap["hp"], "gold": snap["gold"],
            "n_factories": snap["n_factories"], "n_turrets": snap["n_turrets"],
            "n_walls": snap.get("n_walls"), "length_path": snap["length_path"],
            "accepted": dict(accepted), "rejected": dict(rejected),
            "n_rejected": sum(rejected.values()), "bot_errors": errors,
            "damage_dealt": damage_dealt, "hits": hits, "spent": dict(spent),
            "first_damage_taken_round": first_damage_taken_round,
        })
    return {"rounds": last, "result": result, "players": players}


def play_match(spec_a: str, spec_b: str, output: str | Path, *, scenario: str | None = None,
               metadata: dict | None = None) -> dict:
    """Play one authoritative match and return a result row.

    ``output`` must be a new file path (``run_match`` creates it exclusively).
    """
    from . import scenarios  # local import keeps the default path minimal

    output = Path(output)
    config = balanced_config()
    overrides = scenarios.make_overrides(scenario) if scenario else (None, None)
    bots = [TimedBot(resolve_spec(spec_a), overrides[0]), TimedBot(resolve_spec(spec_b), overrides[1])]
    versions_before = (spec_version(spec_a), spec_version(spec_b))
    sources_before = loaded_sources()
    extra = {"research_specs": [spec_a, spec_b], "research_scenario": scenario}
    if metadata:
        extra["research_metadata"] = metadata
    start = time.perf_counter()
    engine = run_match(config, bots, (spec_a, spec_b), output, match_metadata=extra)
    wall = time.perf_counter() - start
    summary = summarize_log(read_log(output))
    winner = engine.result["winner"]
    sources_after = loaded_sources()
    source_changed = (versions_before != (spec_version(spec_a), spec_version(spec_b))
                      or any(sources_after.get(k) != v for k, v in sources_before.items()))
    row = {
        "spec_a": spec_a, "spec_b": spec_b, "scenario": scenario,
        "hash_a": module_hash(spec_a), "hash_b": module_hash(spec_b),
        "version_a": versions_before[0], "version_b": versions_before[1],
        "winner": winner, "reason": engine.result["reason"], "rounds": engine.round,
        "hp_a": engine.players[0].hp, "hp_b": engine.players[1].hp,
        "hp_diff_a": engine.players[0].hp - engine.players[1].hp,
        "wall_seconds": round(wall, 3),
        "decide_seconds": [round(sum(b.times), 4) for b in bots],
        "decide_max_seconds": [round(max(b.times, default=0.0), 4) for b in bots],
        "log": output.relative_to(ROOT).as_posix() if output.is_absolute() and ROOT in output.parents else str(output),
        "players": summary["players"],
        "scenario_errors": [b.scenario_errors for b in bots],
        "sources": sources_after,
        "source_changed": source_changed,
    }
    if metadata:
        row["metadata"] = metadata
    return row


def main(argv=None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Play one research match on the unchanged engine")
    parser.add_argument("--bot-a", required=True)
    parser.add_argument("--bot-b", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--scenario")
    args = parser.parse_args(argv)
    row = play_match(args.bot_a, args.bot_b, args.output, scenario=args.scenario)
    printable = {k: v for k, v in row.items() if k != "players"}
    print(json.dumps(printable, indent=1))
    for p, info in enumerate(row["players"]):
        print(f"player {p}: hp={info['hp']} dealt={info['damage_dealt']} rejected={info['n_rejected']} "
              f"errors={len(info['bot_errors'])} spent={info['spent']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

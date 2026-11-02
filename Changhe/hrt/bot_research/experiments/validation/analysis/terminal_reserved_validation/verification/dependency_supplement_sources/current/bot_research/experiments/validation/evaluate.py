"""Independent authoritative-engine evaluator, with paired player assignments.

Run from the project root with `python -B -m ...evaluate`.  No hidden engine
state is passed to a policy.  Timings are excluded from the trajectory hash.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from td_bots.protocol import collect_actions, load_bot
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.archetypes import Archetype, PROFILES, make


class TimedBot:
    def __init__(self, bot):
        self.bot = bot
        self.times: list[float] = []

    def decide(self, observation):
        started = time.perf_counter()
        try:
            return self.bot.decide(observation)
        finally:
            self.times.append(time.perf_counter() - started)


def source_hashes() -> dict[str, str]:
    root = Path.cwd()
    sources = {Path('td_game/balanced.json'), Path(__file__).relative_to(root)}
    for module in list(sys.modules.values()):
        filename = getattr(module, '__file__', None)
        if not filename:
            continue
        path = Path(filename)
        try:
            relative = path.resolve().relative_to(root)
        except ValueError:
            continue
        if relative.parts[0] in ('td_game', 'td_bots', 'bot_research') and path.suffix == '.py':
            sources.add(relative)
    return {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(sources)}


def bot_from_spec(spec: str):
    return make(spec) if spec in PROFILES else load_bot(spec)


def evaluate(bot_specs: tuple[str, str], bots=None, replay_path: str | None = None,
             condition: dict | None = None) -> dict:
    config = balanced_config()
    engine = Engine(config, bot_specs)
    bots = [TimedBot(bot) for bot in (bots if bots is not None else map(bot_from_spec, bot_specs))]
    records = engine.initial_records(bot_specs)
    source_start = source_hashes()
    digest = hashlib.sha256()
    replay = Path(replay_path).open('x') if replay_path else None
    started = time.perf_counter()
    rejected = [Counter(), Counter()]
    accepted = [Counter(), Counter()]
    bot_errors = [[], []]
    history = []

    def record(items):
        for item in items:
            raw = json.dumps(item, sort_keys=True, separators=(',', ':'), allow_nan=False)
            digest.update(raw.encode())
            digest.update(b'\n')
            if replay:
                replay.write(raw + '\n')
                replay.flush()

    record(records)
    try:
        while engine.result is None:
            observations = [engine.observation(p) for p in (0, 1)]
            actions, errors = collect_actions(bots, observations)
            records = engine.play_round(actions, errors)
            record(records)
            summary = {'round': engine.round, 'players': []}
            for p, row in enumerate(records):
                events = row['event']
                for event in events:
                    if event['kind'] == 'action':
                        if event['accepted']:
                            key = event['action']['op'] + ':' + event['action'].get('type', '')
                            accepted[p][key] += 1
                        else:
                            rejected[p][event['reason']] += 1
                    elif event['kind'] == 'bot_error':
                        bot_errors[p].append({'round': engine.round, 'reason': event['reason']})
                snapshot = row['snapshot']
                summary['players'].append({k: snapshot[k] for k in ('hp', 'gold', 'n_factories', 'n_turrets', 'n_walls', 'length_path')})
                summary['players'][-1]['roster'] = dict(Counter(e['type'] for e in snapshot['roster']))
                summary['players'][-1]['combat'] = next(e for e in events if e['kind'] == 'combat')
                summary['players'][-1]['income'] = next(e for e in events if e['kind'] == 'income')
            history.append(summary)
    finally:
        if replay:
            replay.close()
    elapsed = time.perf_counter() - started
    hp = [p.hp for p in engine.players]
    source_end = source_hashes()
    changed = sorted(k for k in source_start if source_start[k] != source_end.get(k))
    return {'time_utc': datetime.now(timezone.utc).isoformat(), 'bot_specs': list(bot_specs),
            'condition': condition or {'initial_state': 'standard', 'engine_seed': None},
            'rules': config.to_dict(), 'result': engine.result, 'rounds': engine.round,
            'hp': hp, 'hp_difference_p0': hp[0] - hp[1],
            'accepted_actions': [dict(x) for x in accepted],
            'rejected_actions': [dict(x) for x in rejected], 'bot_errors': bot_errors,
            'runtime_seconds': elapsed,
            'decision_seconds': [{'total': sum(b.times), 'max': max(b.times, default=0), 'calls': len(b.times)} for b in bots],
            'trajectory_sha256': digest.hexdigest(), 'source_sha256': source_start,
            'source_sha256_at_end': source_end,
            'source_changed_during_match': changed, 'history': history, 'replay_path': replay_path}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--a', nargs='+', required=True)
    parser.add_argument('--b', nargs='+', required=True)
    parser.add_argument('--paired', action='store_true')
    parser.add_argument('--output', required=True)
    parser.add_argument('--replay-dir')
    args = parser.parse_args()
    pairs = [(a, b) for a in args.a for b in args.b]
    if args.paired:
        pairs = [p for a, b in pairs for p in ((a, b), (b, a))]
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    if args.replay_dir:
        Path(args.replay_dir).mkdir(parents=True, exist_ok=True)
    with output.open('x') as stream:
        for i, pair in enumerate(pairs):
            path = str(Path(args.replay_dir) / f'match-{i:04d}.jsonl') if args.replay_dir else None
            result = evaluate(pair, replay_path=path)
            stream.write(json.dumps(result, sort_keys=True) + '\n')
            stream.flush()
            print(json.dumps({k: result[k] for k in ('bot_specs', 'result', 'hp', 'rounds', 'runtime_seconds', 'rejected_actions', 'bot_errors')}), flush=True)


if __name__ == '__main__':
    main()

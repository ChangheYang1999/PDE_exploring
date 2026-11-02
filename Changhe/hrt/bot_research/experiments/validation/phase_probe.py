"""Mechanics-only exact checks of modulo filling and cutoff losses."""
from __future__ import annotations
from collections import Counter
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.phase_search import phase_candidates
from bot_research.bots.counters.visible_search import score_sequences, purchase_sequences


def main():
    cfg = balanced_config()
    rows = []
    # Existing tier1 entries are synthetic probe conditions, not tournament
    # starting states. New actions are ordinary catalog purchases.
    for count in (0, 210, 225, 228, 240, 248):
        for gold in (650, 1300, 3000):
            obs = Engine(cfg, ('synthetic_attacker', 'empty_defender')).observation(0)
            own = obs['players'][0]
            own['gold'] = gold
            own['roster'] = [{'id': i, 'type': 'tier1', 'bought_round': 1,
                              'expires_after_round': 12} for i in range(count)]
            plain = score_sequences(obs, purchase_sequences(obs, gold, 1000))
            phase = score_sequences(obs, phase_candidates(obs, gold, 1000))
            key = lambda r: (r['damage'], r['hits'], -r['cost'])
            best_plain, best_phase = max(plain, key=key), max(phase, key=key)
            for result in phase:
                full = ['tier1'] * count + list(result['sequence'])
                analytic = sum(cfg.minions[t].damage for i, t in enumerate(full) if i % 250 + 22 < 250)
                assert analytic == result['damage'], (count, gold, result)
            rows.append({'existing_tier1': count, 'gold': gold,
                'plain': dict(best_plain, sequence=dict(Counter(best_plain['sequence']))),
                'phase': dict(best_phase, sequence=dict(Counter(best_phase['sequence']))),
                'improvement': best_phase['damage'] - best_plain['damage'],
                'analytic_no_defense_checked': len(phase)})
    output = {'time_utc': datetime.now(timezone.utc).isoformat(), 'scope': 'synthetic static-map mechanics probe; not game-strength evidence',
        'rules': cfg.to_dict(), 'rows': rows,
        'source_sha256': {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in (
            'td_game/combat.py', 'bot_research/bots/counters/phase_search.py',
            'bot_research/bots/counters/visible_search.py', 'bot_research/experiments/validation/phase_probe.py')}}
    with Path('bot_research/runs/validation/phase-probe-001.json').open('x') as stream:
        json.dump(output, stream, indent=2, sort_keys=True)
        stream.write('\n')
    for row in rows:
        if row['improvement']:
            print(json.dumps(row), flush=True)


if __name__ == '__main__':
    main()

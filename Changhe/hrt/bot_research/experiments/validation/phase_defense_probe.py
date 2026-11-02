"""Test late-phase cheap fillers on fixed defended maps using the engine."""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.phase_search import phase_candidates
from bot_research.bots.counters.visible_search import score_sequences, purchase_sequences


def main():
    cfg = balanced_config()
    rows = []
    layouts = {
        'splash1': [('splash', 1, 1)],
        'gun3_cluster': [('gun3', x, 1) for x in (1, 2, 3)],
        'splash4': [('splash', x, 1) for x in (1, 4, 7, 10)],
    }
    for name, buildings in layouts.items():
        for count in (210, 220, 225, 228, 235, 240, 248):
            for gold in (650, 1300, 3000):
                obs = Engine(cfg, ('synthetic_attacker', 'defender')).observation(0)
                own, enemy = obs['players']
                own['gold'] = gold
                own['roster'] = [{'id': i, 'type': 'tier1', 'bought_round': 1,
                                  'expires_after_round': 12} for i in range(count)]
                enemy['buildings'] = [{'type': t, 'x': x, 'y': y} for t, x, y in buildings]
                plain = score_sequences(obs, purchase_sequences(obs, gold, 1000))
                phase = score_sequences(obs, phase_candidates(obs, gold, 1000))
                key = lambda r: (r['damage'], r['hits'], -r['cost'])
                best_plain, best_phase = max(plain, key=key), max(phase, key=key)
                row = {'map': name, 'buildings': enemy['buildings'], 'existing_tier1': count, 'gold': gold,
                       'plain': best_plain, 'phase': best_phase,
                       'improvement': best_phase['damage'] - best_plain['damage']}
                rows.append(row)
                if row['improvement']:
                    print(json.dumps({k: row[k] for k in ('map', 'existing_tier1', 'gold', 'improvement')}), flush=True)
    files = ('td_game/combat.py', 'bot_research/bots/counters/phase_search.py',
             'bot_research/bots/counters/visible_search.py',
             'bot_research/experiments/validation/phase_defense_probe.py')
    output = {'time_utc': datetime.now(timezone.utc).isoformat(), 'scope': 'synthetic fixed-map mechanics, not match strength',
              'rules': cfg.to_dict(), 'rows': rows,
              'sources': {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in files}}
    with Path('bot_research/runs/validation/phase-defense-probe-001.json').open('x') as stream:
        json.dump(output, stream, sort_keys=True, indent=2)
        stream.write('\n')


if __name__ == '__main__':
    main()

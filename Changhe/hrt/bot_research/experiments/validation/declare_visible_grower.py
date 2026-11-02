"""Declare the visible-roster information ablation of the exact-model grower."""
from datetime import datetime, timezone
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    source = json.loads(Path('bot_research/experiments/validation/forecast-grower-001.json').read_text())
    candidates = []
    for turret_round in (0, 2):
        for defend_from in (1, 4, 6, 8):
            spec = ('bot_research.bots.counters.visible_grower:@make?'
                    f'turret_round={turret_round}&defend_from={defend_from}'
                    '&growth_rounds=6&tier="tier5"')
            candidates.append({'id': f'visible_turret{turret_round}_defend{defend_from}', 'spec': spec})
    output = {'declared_utc': datetime.now(timezone.utc).isoformat(),
              'purpose': 'Development information ablation: replace exact model defense with current visible-roster defense, preserving growth and flood spending rules.',
              'candidates': candidates, 'opponents': source['opponents'],
              'comparison_campaign': 'bot_research/experiments/validation/forecast-grower-001.json',
              'scope': 'Sixteen standard-start games, both assignments. The empty predicted action list is an explicitly inexact no-new-purchases assumption; forecast mismatches are expected, not invalid games. No reserved pool.'}
    atomic_json('bot_research/experiments/validation/visible-grower-001.json', output, exclusive=True)
    print(json.dumps({'declared_utc': output['declared_utc'], 'games': 16}))


if __name__ == '__main__':
    main()

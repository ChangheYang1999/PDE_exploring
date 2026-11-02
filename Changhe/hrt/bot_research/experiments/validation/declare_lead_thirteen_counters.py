"""Declare targeted mid-tier timing and repeated-wave screens of Lead13."""
from datetime import datetime, timezone
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def spec(entry, params):
    return entry + '?' + '&'.join(k + '=' + json.dumps(v, separators=(',', ':'))
                                  for k, v in params.items())


def main():
    model = 'bot_research.bots.counters.snapshots.lead_thirteen_001:@make'
    base = dict(big_threat=100, gun_cap=120, poke_until=3, poke_reactive='turret',
                big_partial=True, r1_poke=3, attack_mode='adaptive')
    variants = {'splash': {'splash_insurance': True},
                'fortress4': {'fortress_n': 4}, 'fortress2': {'fortress_n': 2}}
    for label, changes in variants.items():
        params = {**base, **changes}
        shared = dict(model_spec=model, model_parameters=params, count_cap=1000)
        candidates = []
        for tier, rnd in [('tier3', 3), ('tier3', 4), ('tier3', 5),
                          ('tier4', 4), ('tier4', 5), ('tier4', 6), ('tier4', 7)]:
            args = {**shared, 'tier': tier, 'attack_round': rnd, 'attack_share': 1.0}
            candidates.append({'id': f'timing_{tier}_r{rnd}',
                'spec': spec('bot_research.bots.counters.stateful_public:@timing', args)})
        schedules = {f'opening1_tier4_r{rnd}': [[1, 'tier1', 1], [rnd, 'tier4', 1000]]
                     for rnd in (4, 5, 6)}
        schedules.update({
            'tier4_drip_r4_to9': [[rnd, 'tier4', 1] for rnd in range(4, 10)],
            'tier3_drip_r3_to8': [[rnd, 'tier3', 1] for rnd in range(3, 9)],
            'tier3_r3_tier4_r6': [[3, 'tier3', 3], [6, 'tier4', 1000]],
        })
        for name, schedule in schedules.items():
            args = {**shared, 'schedule': schedule, 'defense_first': False}
            candidates.append({'id': name,
                'spec': spec('bot_research.bots.counters.stateful_schedule:@make', args)})
        manifest = {'declared_utc': datetime.now(timezone.utc).isoformat(),
            'purpose': 'Development screen of splash-only insurance against mid-tier timings and repeated purchases, with persistent public models.',
            'candidates': candidates,
            'opponents': [{'id': 'lead13_' + label, 'spec': spec(model, params)}],
            'scope': 'Twenty-six predeclared standard-start conditions per model setting, both player assignments. No reserved pool. This is a targeted development screen, not an independent final validation.'}
        filename = Path(f'bot_research/experiments/validation/lead-thirteen-{label}-001.json')
        atomic_json(filename, manifest, exclusive=True)
        print(json.dumps({'manifest': str(filename), 'declared_utc': manifest['declared_utc'], 'games': 26}))


if __name__ == '__main__':
    main()

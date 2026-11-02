"""Inspect a completed lead campaign for missed fixed-map capacity attacks.

This script does not run a policy or alter its recorded actions. It reports
hypothetical current-map certificates and marks their response scope.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from td_game.config import balanced_config
from bot_research.bots.counters.fixed_capacity import describe, certified_purchase
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--needle', default='v15')
    args = parser.parse_args()
    campaign = Path(args.campaign)
    rows = [json.loads(line) for line in campaign.read_text().splitlines()]
    selected = []
    inputs = {str(campaign): hashlib.sha256(campaign.read_bytes()).hexdigest()}
    for row in rows:
        if args.needle not in row['spec_a'] and args.needle not in row['spec_b']:
            continue
        log = Path(row['log'])
        if not log.exists():
            selected.append({'log': str(log), 'status': 'missing retained replay'})
            continue
        inputs[str(log)] = hashlib.sha256(log.read_bytes()).hexdigest()
        records = [json.loads(line) for line in log.read_text().splitlines()]
        if any(e.get('kind') == 'bot_error' or e.get('kind') == 'action' and not e['accepted']
               for r in records for e in r['event']):
            raise ValueError('Cannot use a log with errors or rejections.')
        cases = []
        for offset in range(0, len(records)-2, 2):
            pair = records[offset:offset+2]
            rnd = pair[0]['round']+1
            snapshots = [r['snapshot'] for r in pair]
            for side, spec in enumerate((row['spec_a'], row['spec_b'])):
                if args.needle not in spec:
                    continue
                observation = {'round': rnd, 'player': side, 'players': snapshots,
                               'rules': balanced_config().to_dict()}
                defender = snapshots[1-side]
                mapping = describe(defender['buildings'], observation['rules'])
                certificate = certified_purchase(observation, snapshots[side]['gold'], defender['hp'], require_full=False)
                if certificate is None:
                    continue
                own = describe(snapshots[side]['buildings'], observation['rules'])
                recorded = records[offset+2+side]
                bought = Counter(e['action'].get('type') for e in recorded['event']
                                 if e['kind'] == 'action' and e['action']['op'] == 'buy_minion')
                combat = next(e for e in recorded['event'] if e['kind'] == 'combat')
                cases.append({'round': rnd, 'side': side, 'candidate_gold': snapshots[side]['gold'],
                              'defender_hp': defender['hp'], 'defender_mapping': {
                                  'full': mapping.full, 'splash': mapping.splash, 'length': mapping.length},
                              'own_splash': own.splash, 'certificate': certificate,
                              'actual_bought': dict(bought), 'actual_damage': combat['damage_dealt']})
        selected.append({'log': str(log), 'spec_a': row['spec_a'], 'spec_b': row['spec_b'], 'cases': cases})
    sources = set(static_closure({'bot_research.experiments.validation.probe_lead_capacity'}))
    sources.add(Path('td_game/balanced.json'))
    result = {'time_utc': now(), 'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
              'input_sha256': inputs, 'matches': selected,
              'scope': 'Hypothetical homogeneous purchases from recorded public states. Capacity applies to the current fixed map; only full maps prevent all further construction. Budget is pre-action gold, so a certificate does not by itself permit the actual policy to skip defense or construction. No new game outcome.'}
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({'matches': len(selected), 'certificate_states': sum(len(r.get('cases', [])) for r in selected)}))


if __name__ == '__main__':
    main()

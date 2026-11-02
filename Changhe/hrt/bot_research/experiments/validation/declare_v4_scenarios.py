"""Declare known-prefix, stateful V4 timing and schedule development cases."""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode
from bot_research.experiments.validation.artifact_io import atomic_json


def spec(factory, **parameters):
    return 'bot_research.bots.counters.prefixed_v4:@'+factory+'?'+urlencode({
        k: json.dumps(v, separators=(',', ':')) for k, v in parameters.items()})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    cases = []
    for scenario in ('mirror:1:2', 'asym:3:2', 'mirror:22:3', 'asym:23:2'):
        prefix = scenario.replace(':', '_')
        strategies = (
            ('tier3_r5', spec('timing', scenario=scenario, tier='tier3', attack_round=5,
                             attack_share=1.0, count_cap=1000)),
            ('tier4_r7', spec('timing', scenario=scenario, tier='tier4', attack_round=7,
                             attack_share=1.0, count_cap=1000)),
            ('tier4_drip_r5_9', spec('schedule', scenario=scenario, count_cap=1000,
                                   schedule=[[r, 'tier4', 1] for r in range(5, 10)])))
        for label, candidate_spec in strategies:
            cases.append({'scenario': scenario,
                          'candidate': {'id': prefix+'__'+label, 'spec': candidate_spec},
                          'opponent': {'id': prefix+'__V4', 'spec': spec('lead15', scenario=scenario)}})
    source = Path('bot_research/bots/counters/snapshots/lead_fifteen_001.py')
    value = {'declared_utc': datetime.now(timezone.utc).isoformat(),
             'purpose': 'Known legal-prefix counter development against stateful V4. Both policies and the private model advance during opening rounds.',
             'scope': 'Four previously published development openings, three counter policies, both assignments. Excluded from standard-start strength totals. No reserved pool.',
             'cases': cases, 'target_source': str(source),
             'target_sha256': hashlib.sha256(source.read_bytes()).hexdigest()}
    atomic_json(args.output, value, exclusive=True)
    print(json.dumps({'declared_utc': value['declared_utc'], 'conditions': 2*len(cases)}))


if __name__ == '__main__':
    main()

"""Declare focused V4 forecast-component interventions before their games."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qsl, urlencode
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    path = Path('bot_research/experiments/validation/lead-fifteen-V4-standard-001.json')
    source = json.loads(path.read_text())
    selected = ('timing_tier3_r3', 'timing_tier3_r5', 'timing_tier4_r5', 'timing_tier4_r6')
    candidates, comparisons = [], []
    for projection in ('minions', 'nonminions', 'opening'):
        for c in source['candidates']:
            if c['id'] not in selected:
                continue
            root, _, query = c['spec'].partition('?')
            assert root == 'bot_research.bots.counters.stateful_public:@timing'
            parameters = parse_qsl(query) + [('projection', json.dumps(projection))]
            if projection == 'opening':
                parameters = [(k,v) for k,v in parameters if k not in ('model_spec', 'model_parameters')]
            candidate = dict(id=projection+'_'+c['id'], spec='bot_research.bots.counters.projected_forecast:@timing?'+urlencode(parameters))
            candidates.append(candidate)
            comparisons.append(dict(exact_id=c['id'], intervention_id=candidate['id'], projection=projection,
                                    exact_spec=c['spec'], intervention_spec=candidate['spec']))
    result = dict(declared_utc=datetime.now(timezone.utc).isoformat(), candidates=candidates,
                  opponents=source['opponents'], comparisons=comparisons,
                  comparison_manifest=str(path), comparison_manifest_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  purpose='Separate minion-purchase prediction, non-minion prediction, and a fixed three-tier1 opening prior against V4.',
                  hypothesis='Predicting incoming purchases suffices for the three observed exact-model timing wins; exact construction prediction may be unnecessary.',
                  selection='Four conditions selected after the first twelve exact-model games: three winning timings and one drawing timing. This is a focused mechanism test, not an unbiased strength estimate.',
                  scope='24 standard-start development conditions, both assignments. No reserved opponents. Full underlying private-model predictions must match actual actions for both projection modes.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps(dict(declared_utc=result['declared_utc'], conditions=2*len(candidates))))


if __name__ == '__main__':
    main()

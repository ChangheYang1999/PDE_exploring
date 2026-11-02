"""Declare the matched V4 timing/schedule information ablation."""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qsl, urlencode
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    source = Path('bot_research/experiments/validation/lead-fifteen-V4-standard-001.json')
    original = json.loads(source.read_text())
    comparisons = []
    for candidate in original['candidates']:
        old_id, old_spec = candidate['id'], candidate['spec']
        root, _, query = old_spec.partition('?')
        factory = {'bot_research.bots.counters.stateful_public:@timing':'timing',
                   'bot_research.bots.counters.stateful_schedule:@make':'schedule'}[root]
        parameters = [(k,v) for k,v in parse_qsl(query) if k not in ('model_spec','model_parameters')]
        candidate['id'] = 'visible_'+old_id
        candidate['spec'] = 'bot_research.bots.counters.visible_forecast_v2:@'+factory+'?'+urlencode(parameters)
        comparisons.append(dict(exact_id=old_id, visible_id=candidate['id'], exact_spec=old_spec, visible_spec=candidate['spec']))
    original.update(declared_utc=datetime.now(timezone.utc).isoformat(),
        purpose='Replace the exact stateful V4 forecast by an empty opponent submission while preserving timing and spending rules.',
        hypothesis='Some V4 timing and drip counter wins survive without an exact opponent model.',
        comparison_manifest=str(source), comparison_manifest_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        comparisons=comparisons, scope='26 paired standard-start development conditions; deliberate forecast errors do not invalidate game outcomes. No reserved opponents.')
    atomic_json(args.output, original, exclusive=True)
    print(json.dumps(dict(declared_utc=original['declared_utc'], conditions=2*len(original['candidates']))))


if __name__ == '__main__':
    main()

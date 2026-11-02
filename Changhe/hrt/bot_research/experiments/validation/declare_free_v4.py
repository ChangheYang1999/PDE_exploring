"""Declare the legal-cell fallback intervention before any full-game run."""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    source = Path('bot_research/experiments/validation/lead-fifteen-V4-scenarios-001.json')
    original = json.loads(source.read_text())
    for case in original['cases']:
        case['candidate']['spec'] = case['candidate']['spec'].replace(
            'bot_research.bots.counters.prefixed_v4:@',
            'bot_research.bots.counters.prefixed_free_v4:@')
        case['candidate']['id'] += '__free'
    original.update(declared_utc=datetime.now(timezone.utc).isoformat(),
        purpose='Paired legal-cell defensive fallback intervention against V4 on known development openings.',
        hypothesis='Template-constrained defense contributes to prefix losses; a deterministic legal-cell fallback can improve survival with attack timing and schedules fixed.',
        comparison_manifest=str(source), comparison_manifest_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        scope='24 declared development conditions; compare all with original template defense, including failures and unchanged cases. No reserved pool.')
    atomic_json(args.output, original, exclusive=True)
    print(json.dumps(dict(declared_utc=original['declared_utc'], conditions=2*len(original['cases']))))


if __name__ == '__main__':
    main()

"""Apply strict source checks retrospectively to completed development files."""
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation_strict import read_result, now


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', nargs='+', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    checked, failures, hashes = [], [], {}
    for filename in args.inputs:
        directory = Path(filename)
        frozen = json.loads((directory / 'freeze.json').read_text())['source_sha256']
        jobs = json.loads((directory / 'jobs.json').read_text())
        for suffix in ('freeze.json', 'jobs.json'):
            path = directory / suffix
            hashes[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        for job in jobs:
            path = directory / 'results' / (job['id'] + '.json')
            if not path.exists() or (directory / 'results' / (job['id'] + '.failure.json')).exists():
                continue
            hashes[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
            try:
                read_result(path, job, frozen)
            except (ValueError, KeyError, TypeError, OSError) as error:
                failures.append({'result': str(path), 'error': public_diagnostic(str(error))})
            else:
                checked.append(str(path))
    output = {'time_utc': now(), 'input_sha256': hashes,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'checked': checked, 'failures': failures, 'all_passed': not failures,
              'scope': 'Completed artifacts only. Failed or unfinished matches remain excluded.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'checked': len(checked), 'failures': failures, 'all_passed': not failures}))
    assert not failures


if __name__ == '__main__':
    main()

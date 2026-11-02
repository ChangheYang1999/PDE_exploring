"""Compare hash promises in archived declarations with execution freezes.

This complements per-game source checks: a consistent execution freeze can
still differ from an earlier declaration. No game or policy is executed.
"""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time

from bot_research.experiments.validation.artifact_io import atomic_json


FIELDS = ('input_sha256', 'snapshot_sha256')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    inputs, campaigns, differences = {}, [], []
    for freeze_path in sorted(Path('bot_research/runs/validation').glob('*/freeze.json')):
        metadata = json.loads(freeze_path.read_text())
        expected = metadata.get('manifest_sha256')
        frozen = metadata.get('source_sha256', {})
        if expected is None:
            continue
        directory = freeze_path.parent
        matches = [name for name, value in frozen.items() if value == expected and name.endswith('.json')]
        if len(matches) != 1:
            campaigns.append(dict(directory=str(directory), status='manifest_not_uniquely_located', matches=matches))
            continue
        manifest_path = directory/'sources'/matches[0]
        if not manifest_path.is_file() or digest(manifest_path) != expected:
            raise ValueError('Archived declaration missing or changed: '+str(manifest_path))
        inputs[str(freeze_path)] = digest(freeze_path)
        inputs[str(manifest_path)] = expected
        manifest = json.loads(manifest_path.read_text())
        claims = []
        for field in FIELDS:
            for name, promised in manifest.get(field, {}).items():
                if not isinstance(promised, str) or len(promised) != 64:
                    continue
                if name not in frozen:
                    claims.append(dict(field=field, source=name, status='not_in_execution_freeze'))
                    continue
                archived = directory/'sources'/name
                if not archived.is_file() or digest(archived) != frozen[name]:
                    raise ValueError('Archived execution source missing or changed: '+str(archived))
                inputs[str(archived)] = frozen[name]
                status = 'equal' if promised == frozen[name] else 'different'
                claim = dict(field=field, source=name, declared_sha256=promised,
                             executed_freeze_sha256=frozen[name], status=status)
                claims.append(claim)
                if status == 'different':
                    differences.append(dict(directory=str(directory), **claim))
        campaigns.append(dict(directory=str(directory), manifest=matches[0],
            started_utc=metadata.get('started_utc'), declared_utc=manifest.get('declared_utc'),
            status='checked', claims=claims))
    for path, value in inputs.items():
        if digest(path) != value:
            raise ValueError('Audit input changed: '+path)
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        checker_sha256=digest(__file__), input_sha256=inputs, campaigns=campaigns,
        declaration_execution_differences=differences,
        scope='Top-level independent-validation execution freezes with archived declarations. Only input_sha256 and snapshot_sha256 claims covered by the execution freeze are compared. This neither certifies all descriptive metadata nor treats a retired or failed campaign as a strength result.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(campaigns=len(campaigns), differences=differences, runtime_seconds=output['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()

"""Inventory and hash-validate saved regional reductions, without new PDE work."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

lane = Path(__file__).resolve().parents[1]
root = lane / 'verification'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
rows = []
for regional in sorted(root.glob('*/REGIONAL_RESIDUALS.json')):
    folder = regional.parent
    table = json.loads(regional.read_text())
    result_path = folder / 'results.json'
    assert sha(result_path) == table['source_results_sha256'], str(regional)
    results = json.loads(result_path.read_text())
    states = {s['label']: s for s in results['states']}
    for item in table['states']:
        state = states[item['label']]
        archive = Path(state['snapshot'])
        if not archive.is_absolute():
            archive = folder / archive
        assert sha(archive) == item['source_sha256'] == state['sha256'], str(archive)
        for run in item['runs']:
            arrays = folder / (item['label'] + '_' + run['kind'] + '.npz')
            assert sha(arrays) == run['raw_arrays_sha256'], str(arrays)
            pairs = {(r['field'], r['r_min']) for r in run['regions']}
            assert pairs == {(field, low) for field in ['F', 'G', 'Theta', 'Omega']
                             for low in [0, .03, .3, 3, 30, 300]}, str(arrays)
        rows.append({'label': item['label'], 'archive': str(archive.relative_to(lane)),
                     'archive_sha256': state['sha256'],
                     'regional_table': str(regional.relative_to(lane)),
                     'regional_table_sha256': sha(regional),
                     'source_results_sha256': sha(result_path),
                     'points': state.get('points'), 'beta': state.get('metadata', {}).get('beta'),
                     'forcing_description': state.get('forcing_description')})
unique = sorted(set(r['archive_sha256'] for r in rows))
output = Path(sys.argv[1])
output.parent.mkdir(parents=True, exist_ok=True)
data = {'utc': datetime.now(timezone.utc).isoformat(), 'status': 'CONFIRMED',
        'folders': len(set(r['regional_table'] for r in rows)), 'state_evaluations': len(rows),
        'unique_archive_sha256': len(unique),
        'scope': 'Unique serialized coefficient archives with complete six-region self/transport F/G/Theta/Omega tables. Includes the manufactured_picard control and one L2.5 transplant; none is accepted as a B2 candidate.',
        'script_sha256': sha(Path(__file__)), 'states': rows}
output.write_text(json.dumps(data, indent=2) + '\n')
print(json.dumps({k:v for k,v in data.items() if k != 'states'}, indent=2))

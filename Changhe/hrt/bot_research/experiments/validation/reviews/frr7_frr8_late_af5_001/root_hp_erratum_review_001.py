"""Root authentication and independent terminal recount of the preserved HP erratum."""
from datetime import datetime, timezone
import copy
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001')
ERR = ROOT / 'hp_erratum_001'
OUT = ROOT / 'root_hp_erratum_review_001.json'
def sha(b): return hashlib.sha256(b).hexdigest()
def stamp(): return datetime.now(timezone.utc).isoformat()
def load(p): return json.loads(p.read_text())
def pin(p, rec):
    b = p.read_bytes()
    assert sha(b) == rec['sha256'], str(p)
    if 'bytes' in rec: assert len(b) == rec['bytes'], str(p)
    return b

def canonical(records):
    out = copy.deepcopy(records)
    for record in out:
        record.pop('match', None)
        for player in record.get('snapshot', {}).get('players', []):
            player.pop('name', None)
    return out

started = stamp()
assert not OUT.exists()
assert sha((ERR / 'seal.json').read_bytes()) == '49f8a77e03df0431b0b5a34132314da97b77b19291fc1809af97d675d5ed363c'
seal = load(ERR / 'seal.json')
for name, rec in seal['outputs'].items(): pin(ERR / name, rec)
evidence = load(ERR / 'EVIDENCE.json')
assert not seal['errors'] and not evidence['errors']
assert sha((ROOT / 'seal_001.json').read_bytes()) == evidence['original_seal_sha256']
original = load(ROOT / 'seal_001.json')
for name, rec in original['outputs'].items(): pin(ROOT / name, rec)
for name, rec in evidence['input_sha256_and_bytes'].items(): pin(Path(name), rec)
archive_records = {}
for name, rec in evidence['archive_edges'].items():
    packed = (ROOT / rec['archive']).read_bytes()
    assert sha(packed) == rec['archive_sha256'] and len(packed) == rec['archive_bytes']
    data = gzip.decompress(packed)
    assert sha(data) == rec['sha256'] and len(data) == rec['bytes']
    assert Path(name).read_bytes() == data
    archive_records[name] = [json.loads(line) for line in data.splitlines()]
for rec in evidence['preserved_error_and_detection_bytes']:
    packed = (ERR / rec['archive']).read_bytes()
    assert sha(packed) == rec['archive_sha256'] and len(packed) == rec['archive_bytes']
    data = gzip.decompress(packed)
    assert sha(data) == rec['sha256'] and len(data) == rec['bytes']
    assert Path(rec['path']).read_bytes() == data
results = []
for condition in evidence['conditions']:
    seat = condition['physical_AF5_or_G1_side']
    af5 = archive_records[condition['frr8_log']]
    g1 = archive_records[condition['frr5_log']]
    assert len(af5) == len(g1) == 102
    assert canonical(af5) == canonical(g1)
    hp = [af5[-1]['snapshot']['players'][side]['hp'] for side in (seat, 1-seat)]
    assert hp == [790, 735] == condition['terminal_HP_AF5_first']
    row = condition['frr8_row']
    assert [row['hp_a'], row['hp_b']][seat] == 790
    assert [row['hp_a'], row['hp_b']][1-seat] == 735
    assert row['winner'] == seat and row['rounds'] == 50
    results.append({'physical_AF5_side': seat, 'HP_AF5_first': hp, 'margin': hp[0]-hp[1],
                    'rounds': row['rounds'], 'full_canonical_records_equal_to_g1': len(af5),
                    'frr8_log': condition['frr8_log'], 'frr5_log': condition['frr5_log']})
assert sorted(r['physical_AF5_side'] for r in results) == [0, 1]
assert '795:740' in (ROOT/'REVIEW.md').read_text()
assert '790:735' in (ERR/'ERRATUM.md').read_text()
receipt = {'schema': 'root-hp-erratum-review-001', 'started_utc': started, 'completed_utc': stamp(),
 'verdict': 'CONFIRMED', 'erratum_seal_sha256': sha((ERR/'seal.json').read_bytes()),
 'erratum_outputs_authenticated': len(seal['outputs']), 'original_outputs_unchanged': len(original['outputs']),
 'input_files_authenticated': len(evidence['input_sha256_and_bytes']),
 'original_archive_edges_authenticated': len(archive_records),
 'preserved_error_or_detection_archives_authenticated': len(evidence['preserved_error_and_detection_bytes']),
 'results': results, 'scope': 'Prose correction and retained full-history comparison only. The original numerical data were correct. No fresh policy execution, gameplay, or clock-invariance claim.',
 'independent_recount': 'Standard-library parsing of archived rows and records, without importing the reviewed checker, policy or engine.',
 'script_sha256': sha(Path(__file__).read_bytes())}
OUT.write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps({'receipt':str(OUT),'sha256':sha(OUT.read_bytes()),'completed_utc':receipt['completed_utc'], 'verdict':receipt['verdict']},indent=2))

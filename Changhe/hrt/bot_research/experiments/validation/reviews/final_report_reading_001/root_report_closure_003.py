"""Verify the captured final report delta using retained receipts only."""
from pathlib import Path
from datetime import datetime, timezone
import gzip
import hashlib
import json


def sha(data):
    return hashlib.sha256(data).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


start = now()
base = Path('bot_research/experiments/validation/reviews/final_report_reading_001')
out = base / 'closure_003'
assert not (out / 'RECEIPT.json').exists()
capture_bytes = (out / 'CAPTURE.json').read_bytes()
capture = json.loads(capture_bytes)
packed = Path(capture['archive']).read_bytes()
new = gzip.decompress(packed)
assert sha(packed) == capture['archive_sha256']
assert sha(new) == capture['sha256'] == 'f7879a3ae3bebb8224b8baf5b174625e6a74c58f2de28a4d16ccc28fd698769b'
assert sha((out / 'changes.diff').read_bytes()) == capture['diff_sha256']
pins = {
    str(base / 'closure_001/RECEIPT.json'): 'e2fd1d86f08d832033462545532f228c51affb9f38c9faddd38f07a6046531af',
    'bot_research/experiments/validation/reviews/economy_final_gate_001/root_development_afs3_review_015.json': '34a0499bc4fd8c0d56fed7a1142530b0456e54e9ae2addb171b9486d4b3d5e69',
    'bot_research/runs/validation/final-checks-001.json': '0cecd0f0558c560715ab7a036deee29094905b4d4fd965cff2bf4e1805bee33b',
    'bot_research/bots/best.py': '70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87',
    'bot_research/tests/test_best.py': '07ec39bb28f9daa245741bfe2d852c105f35b3e035f53b7b744377a822e19010',
}
inputs = {}
for name, expected in pins.items():
    raw = Path(name).read_bytes()
    assert sha(raw) == expected, name
    inputs[name] = raw
for name in ('integrity_2.json', 'integrity_3.json', 'integrity_3.out', 'hashes_after.txt'):
    path = Path('bot_research/runs/lead/final') / name
    inputs[str(path)] = path.read_bytes()
lead2 = inputs['bot_research/runs/lead/final/integrity_2.json']
lead3 = inputs['bot_research/runs/lead/final/integrity_3.json']
assert lead2 == lead3
integrity = json.loads(lead3)
assert integrity['baseline_comparison']['identical_to_baseline'] is True
assert integrity['baseline_comparison']['differences'] == {}
assert integrity['missing_count'] == 1002
assert integrity['changed'] == ['td_game/combat.py', 'tests/test_engine.py', 'tests/test_rules.py']
assert integrity['files_outside_bot_research'] == 40
for path, digest in integrity['current_hashes'].items():
    assert sha(Path(path).read_bytes()) == digest, path
text = new.decode()
assert '48, 146, 162, 264, 238 and 228' in text
assert "af3's 146-0-144 and af4's 162-2-126" in text
assert 'development evidence' in text
assert '2026-11-01T00:06:39Z to 00:06:49Z' in text
notes = Path('../hrt-lead/NOTES_FOR_TEAM.md').read_bytes()
assert b'00:06:39Z to 00:06:49Z' in notes
inputs['../hrt-lead/NOTES_FOR_TEAM.md'] = notes
inputs[str(out / 'CAPTURE.json')] = capture_bytes
inputs[str(out / 'changes.diff')] = (out / 'changes.diff').read_bytes()
archives = []
for number, (name, raw) in enumerate(inputs.items(), 1):
    path = out / f'input-{number:02d}.gz'
    with path.open('xb') as stream:
        stream.write(gzip.compress(raw, mtime=0))
    assert gzip.decompress(path.read_bytes()) == raw
    archives.append({'source': name, 'sha256': sha(raw), 'bytes': len(raw),
                     'archive': str(path), 'archive_sha256': sha(path.read_bytes())})
receipt = {
    'schema': 'root-report-closure-003',
    'started_utc': start, 'completed_utc': now(), 'actual_model': 'GPT-6 Astra',
    'report_sha256': sha(new), 'capture': capture,
    'verdict': 'CONFIRMED for the bounded captured delta',
    'inputs': archives, 'protected_source_hashes_directly_checked': 40,
    'manual_review': 'Root read the full changes.diff. The only changes are report dates, completed AF3 development counts, the corresponding validation citations, and the final lead integrity statement.',
    'checks': {
        'af3_and_six_sweep_counts_match_independent_receipt': True,
        'lead_integrity_3_equals_2': True,
        'lead_integrity_3_matches_current_40_protected_files': True,
        'best_and_test_hashes_match_final_hash_log': True,
        'reported_integrity_times_match_lead_coordination_note': True,
    },
    'limitations': [
        'Integrity run clock times are attributed to the archived lead note; this reader did not independently time that run.',
        'The capture was equal to the lane report copy at capture time; this is not a promise about later edits.',
        'Closure002 stopped on a changing live report hash before archiving; its failure record is preserved. Closure003 certifies separately captured stable bytes.',
        'No policy, Engine, game, replay or test was executed. This is not a new full-report semantic audit.'
    ],
    'script_sha256': sha(Path(__file__).read_bytes()),
}
path = out / 'RECEIPT.json'
path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
print(json.dumps({'receipt': str(path), 'sha256': sha(path.read_bytes()), 'completed_utc': receipt['completed_utc']}, indent=2))

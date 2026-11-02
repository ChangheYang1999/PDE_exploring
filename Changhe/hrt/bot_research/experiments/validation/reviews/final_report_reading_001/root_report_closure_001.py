"""Seal the manually reviewed final report correction diff; no game imports."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import gzip
import hashlib
import json


def sha(data):
    return hashlib.sha256(data).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


start = now()
base = Path('bot_research/experiments/validation/reviews/final_report_reading_001')
out = base / 'closure_001'
assert not out.exists()
oldp = base / 'status_addendum_001/REPORT.snapshot.md'
report = Path('bot_research/reports/REPORT.md')
old = oldp.read_bytes()
new = report.read_bytes()
assert sha(old) == '5aa07ad836f4acfb4314c6299f34b27b74eaebcdd19b95650d7d9f197ad0a02f'
assert sha(new) == 'b006e7cabd89e5119d5d812e77a5b76fa8192b29bb47596e1466055f9daf7379'
assert new == report.read_bytes()
assert new == Path('../hrt-lead/FINAL_REPORT.md').read_bytes()
pins = {
    str(base / 'root_status_addendum_review_001.json'): '0515c2a0fbfe30dbeb0e4fec54bc488d2024048198f88e255f799fdcf788f552',
    'bot_research/experiments/validation/reviews/economy_final_gate_001/root_development_afs4_review_014.json': 'aced7f3074f3023a04e754a108ac4aba2cb5e87575f2c9a0668b6f9d040c4100',
    'bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001/af5_matrix_extension/PROOF.md': '2d82fbdb2c2fc1f91f0f09656ab07489c73f60dc6a758432fe9ee3453e5d0240',
    'bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001/root_review_002.json': '2494c99caf1970368b043be9cd89f72679d8a002f15866a6ce3109ea1753e5b0',
}
inputs = [(str(oldp), old), (str(report), new)]
for name, expected in pins.items():
    data = Path(name).read_bytes()
    assert sha(data) == expected, name
    inputs.append((name, data))
text = new.decode()
checks = {
    'chronology_exact_table': 'selected for fresh validation at 22:43:35Z; recommended for the standard start after the completed gate, announced at 23:34:38Z' in text,
    'g1_former_recommendation': "the lane's former standalone recommendation" in text,
    'outdated_proof_phrase_absent': 'not proved by hand' not in text,
    'conditional_proof_cited': 'af5_matrix_extension/PROOF.md' in text and 'conditional on the finite table' in text,
    'development_sweep_counts': '48, 162, 264, 238 and 228' in text and "af4's 162-2-126" in text,
    'foreign_shared_guard_phrase_absent': 'no attack, finish or doom purchase' not in text,
}
assert all(checks.values()), checks
out.mkdir()
archives = []
for number, (name, data) in enumerate(inputs, 1):
    archive = out / f'input-{number:02d}.gz'
    packed = gzip.compress(data, mtime=0)
    archive.write_bytes(packed)
    assert gzip.decompress(archive.read_bytes()) == data
    archives.append({'source': name, 'sha256': sha(data), 'bytes': len(data), 'archive': str(archive), 'archive_sha256': sha(packed)})
diff = ''.join(difflib.unified_diff(old.decode().splitlines(keepends=True), text.splitlines(keepends=True), fromfile='report-snapshot-235653', tofile='report-snapshot-0001', n=3))
(out / 'reviewed_changes.diff').write_text(diff)
receipt = {
    'schema': 'root-final-report-correction-closure-001',
    'started_utc': start, 'completed_utc': now(),
    'actual_model': 'GPT-6 Astra', 'verdict': 'CONFIRMED',
    'report_sha256': sha(new), 'previous_report_sha256': sha(old),
    'lane_final_report_copy_equal': True, 'two_immediate_report_reads_equal': True,
    'checks': checks, 'inputs': archives,
    'diff_sha256': sha(diff.encode()),
    'manual_review': 'Root read the complete diff before sealing it and checked its new sweep counts against the independently reproduced AF4 receipt. Earlier six corrections remain covered by the dated addendum.',
    'scope': 'Closes the reported chronology and proof-status corrections for these exact report bytes. Not a new semantic audit of the whole report or a guarantee about later edits. No policy, game, engine, replay or test execution.',
    'script_sha256': sha(Path(__file__).read_bytes()),
}
path = out / 'RECEIPT.json'
path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
print(json.dumps({'receipt': str(path), 'sha256': sha(path.read_bytes()), 'completed_utc': receipt['completed_utc'], 'checks': checks}, indent=2))

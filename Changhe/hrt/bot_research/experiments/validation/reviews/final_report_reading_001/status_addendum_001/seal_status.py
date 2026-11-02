"""Seal a dated source-only status addendum without changing prior reviews."""
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path

BASE = Path('bot_research/experiments/validation/reviews/final_report_reading_001/status_addendum_001')
assert os.sched_getaffinity(0) == {28}
assert os.getpriority(os.PRIO_PROCESS, 0) == 19
started = datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write_new(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)

capture_bytes = (BASE / 'CAPTURE.json').read_bytes()
capture = json.loads(capture_bytes)
report = (BASE / 'REPORT.snapshot.md').read_bytes()
assert sha(report) == capture['sha256'] == '5aa07ad836f4acfb4314c6299f34b27b74eaebcdd19b95650d7d9f197ad0a02f'
inputs = []
sources = [
    ('bot_research/experiments/validation/reviews/final_report_reading_001/REVIEW.md', 'b62205f58a74058e646754add79f00ecc58cdff96c7b467fa19a9da5aa9f998d'),
    ('bot_research/experiments/validation/reviews/final_report_reading_001/INPUT_BINDINGS.json', 'b5512ccd84163aa7102efe38583658c0fc182500a1c09296dc4e6b9eaadf4887'),
    ('bot_research/experiments/validation/reviews/final_report_reading_001/inputs/retained/bot_research/notes/economy.md', None),
    ('bot_research/notes/economy.md', None),
    ('bot_research/experiments/validation/reviews/economy_final_gate_001/root_repeat_narrative_review_012.json', 'bfe5d12e0b956f03e7e4f3e1015827f73a7dbbb2e56dcfee732aed141bb0cf94'),
    ('bot_research/experiments/validation/reviews/economy_final_gate_001/CHRONOLOGY_CLARIFICATION_001.md', None),
    ('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001/af5_matrix_extension/PROOF.md', '2d82fbdb2c2fc1f91f0f09656ab07489c73f60dc6a758432fe9ee3453e5d0240'),
    ('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001/root_review_002.json', '2494c99caf1970368b043be9cd89f72679d8a002f15866a6ce3109ea1753e5b0'),
]
for source, expected in sources:
    raw = Path(source).read_bytes()
    digest = sha(raw)
    if expected:
        assert digest == expected, source
    archive = BASE / 'inputs' / (source + '.gz')
    packed = gzip.compress(raw, mtime=0)
    write_new(archive, packed)
    assert gzip.decompress(archive.read_bytes()) == raw
    inputs.append({'source': source, 'sha256': digest, 'bytes': len(raw), 'archive': str(archive), 'archive_sha256': sha(packed), 'expected_prior_hash': expected, 'prior_hash_matches': digest == expected if expected else None})

historical_economy = Path(sources[2][0]).read_text()
for phrase in ['22:43:35Z', 'is still open.', '2026-10-31T23:34:38Z', '23:33:35Z', 'this makes af5 the']:
    assert phrase in historical_economy, phrase

review = f'''# Report correction status addendum 001

Prepared at {started}. This source-only GPT-6 Astra review is fixed to the [report snapshot](REPORT.snapshot.md) captured at {capture['captured_at']}, SHA256 `{capture['sha256']}`. It is not a statement about edits made after that capture. Exact historical and current economy-note bytes and the cited receipts are losslessly archived in [INPUT_BINDINGS.json](INPUT_BINDINGS.json). Actual Opus 5.5 collaboration is through the lead and economy lanes' notes and root's exchange of findings.

The six corrections in the [earlier review](../REVIEW.md) are substantively incorporated in this snapshot. The replacement recommendation dates introduce one chronology qualification.

| Earlier correction | Status in the preserved snapshot |
| --- | --- |
| 1. Current standalone recommendation and round-1 scope | The table adds af5's two +410 wins at round 50, calls g1 former, and limits the round-1 explanation to the named earlier policies. Lines 1804–1822 resolve the substantive omission. The new 22:43 recommendation date needs the qualification below. |
| 2. “Every candidate” loses the round-2 strike | Lines 2205–2208 name the earlier tested variants and explicitly give AS1C, g0, g1, V29 and af5 their 40 TIMING2 wins. Resolved. |
| 3. afrep labeled a replay | Lines 2096–2097 call it two new games after afrr and distinguish reproduction from engine replay. Resolved. The separate [root history comparison](../../economy_final_gate_001/root_repeat_narrative_review_012.json) supports equality of 102 retained seat-0 events and snapshots; it does not identify private reasoning or the cause of elapsed-time differences. |
| 4. Project-root reproduction paths | Lines 2367–2368 and 2410–2412 give all four result-file arguments the `bot_research/` prefix. Line 2391 explicitly gives the historical freeze command's working directory. Resolved by source reading; no command was executed. |
| 5. Eleven-policy zero-coordinate count | Line 2103 now says all seven remaining policies have zero weight. Resolved. |
| 6. Integrity inventory exclusion | Lines 2451–2452 explicitly exclude both `bot_research` and `.venv` from the 40-file inventory and distinguish the 903-entry checkpoint. Resolved. |

## Remaining chronology qualification

The new table says af5 was the standalone recommendation “from 22:43Z” and g1 the recommendation “until 22:43Z.” Economy notes 18.26, dated 22:47:11Z, identify 22:43:35Z as the sweep selection for fresh evaluation and explicitly say the condition for recommending af5 is still open. They also add the second gate safeguard. Notes 18.32, dated 23:34:38Z after the second gate ended at 23:33:35Z, announce that the completed conditions make af5 the standard-start recommendation. The separately dated [chronology clarification](../../economy_final_gate_001/CHRONOLOGY_CLARIFICATION_001.md) also records the still-open gate before completion.

**Verdict: CONFIRMED chronology distinction.** Minimum wording: af5 was “selected for fresh validation at 22:43:35Z; recommended for standard starts after the completed gate, announced at 23:34:38Z.” Call g1 the “former standalone recommendation,” without the unsupported 22:43 cutoff. This preserves the difference between choosing a candidate to test and recommending it after the criterion passes. It makes no new claim about whether an earlier rule was established before all possible exposure.

## Newly completed proof status

Line 2101 still describes the eleven-policy conclusion as “not proved by hand.” A complete, conditional [standalone AF5 finite-matrix proof](../../frr7_frr8_late_af5_001/af5_matrix_extension/PROOF.md) and its [root record and exact-arithmetic review](../../frr7_frr8_late_af5_001/root_review_002.json) now exist. Minimum update: link that proof and keep the theorem conditional on the retained finite payoffs and imposed zero diagonal. The phrase can remain only if clearly scoped to the earlier numerical computation. This is a newly completed proof-status update, not a new numerical counterexample.

No policy import, constructor, decision, Engine call, game, replay, simulation or test was executed. The receipt authenticates retained bytes at the stated times, not continuous historical source identity, full transitive runtime provenance or absence of erased attempts. No later mutable report state is certified here.
'''
write_new(BASE / 'REVIEW.md', review.encode())
completed = datetime.datetime.now(datetime.timezone.utc).isoformat()
receipt = {
    'schema': 'report-correction-status-addendum-001',
    'started_utc': started, 'completed_utc': completed,
    'actual_model': 'GPT-6 Astra',
    'affinity': sorted(os.sched_getaffinity(0)), 'nice': os.getpriority(os.PRIO_PROCESS, 0),
    'report_capture': capture, 'capture_receipt_sha256': sha(capture_bytes),
    'prior_six_corrections_substantively_incorporated': True,
    'remaining_qualification': '22:43:35 sweep selection differs from recommendation announced at 23:34:38 after the completed gate.',
    'newly_completed_proof_status_update': True,
    'inputs': inputs,
    'review_sha256': sha((BASE / 'REVIEW.md').read_bytes()),
    'script_sha256': sha(Path(__file__).read_bytes()),
    'policy_constructor_engine_game_replay_simulation_test_calls': 0,
    'scope': 'Source-only dated correction status, conditional on the preserved report snapshot and retained receipts. No later report state certified.',
}
write_new(BASE / 'INPUT_BINDINGS.json', (json.dumps(receipt, indent=2, sort_keys=True) + '\n').encode())
print(json.dumps({'completed_utc': completed, 'review_sha256': receipt['review_sha256'], 'receipt_sha256': sha((BASE / 'INPUT_BINDINGS.json').read_bytes()), 'script_sha256': receipt['script_sha256'], 'input_count': len(inputs)}, indent=2))

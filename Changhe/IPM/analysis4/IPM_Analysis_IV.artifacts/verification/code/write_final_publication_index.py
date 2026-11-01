"""Summarize the latest completed finite publication inventories."""
from pathlib import Path
from datetime import datetime,timezone
import json
base=Path('artifacts/final_audit')
def latest(pattern):
 p=max(base.glob(pattern),key=lambda x:x.stat().st_mtime_ns)
 return p,json.loads(p.read_text())
ep,e=latest('*/admission_reference_checks.json');lp,l=latest('*/local_reference_inventory.json');xp,x=latest('expanded_text_hygiene_*.json');cp,c=latest('compressed_text_*.json');pp,p=latest('*/publication_projection_checks.json')
assert set(e['status_counts'])<={'match','match_lossless_archive','historical_proof_snapshot_match','historical_snapshot_match','historical_delta_match'}
assert l['markdown_link_counts'].get('missing',0)==0 and l['ledger_evidence_counts'].get('missing',0)==0
assert x['files_with_hits']==4 and not x['decoding_errors']
assert c['complete'] and not c['files_with_hits'] and not c['errors']
assert p['all_checks_pass'] and len(p['rows'])==4
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
hist=sum(v for k,v in e['status_counts'].items() if k.startswith('historical'))
ledger=sum(l['ledger_evidence_counts'].values());changed=sum(len(r['changed_lines']) for r in p['rows']);unchanged=sum(r['unchanged_lines'] for r in p['rows'])
Path('PUBLICATION_INDEX.md').write_text(f'''# Publication file selection

Updated {now}. Every inventory below records its actual execution time and finite scope.

Publish the verifier reports, research proofs and selected evidence. The task specifications `PROMPT.md` and `SHIFT_PROMPT.md`, raw shift transcripts and scratch directory are operational records. Do not include them as report material.

Four original producer transcripts contain local paths in runtime warnings and tracebacks. Preserve the originals locally for their admission hashes. Publish the matching copies listed in [the projection manifest](artifacts/publication/source_projection_manifest.json). The [projection check]({pp}), recorded {p['at']}, confirms all four original and publication hashes, {changed} changed diagnostic lines and {unchanged} unchanged lines. Every numerical output line and completion footer is unchanged. A projected file must not be substituted when checking an original source hash.

The [expanded text scan]({xp}), completed {x['at']}, checks {x['checked_files']} uncompressed files and {x['checked_bytes']} bytes. Its only matches are the four original transcripts above; there are no other local-path or em-dash matches and no UTF-8 errors. It includes small artifact JSON and JSONL. V648 explicitly rejects the earlier faulty prototype result at 23:46:20Z; V649 confirms the corrected scanner with positive and negative path controls. The prototype is retained only as superseded evidence.

The [compressed and large-text scan]({cp}), completed {c['at']}, checks {c['checked_files']} files and {c['checked_decompressed_bytes']} decompressed bytes. It finds no local-path or em-dash matches and no archive-read errors. This scan examines bytes; it does not independently validate every text encoding.

These scans exclude source code, operational shift logs and binary checkpoints. They are finite text checks, not a complete audit of a future assembled publication package.

The [local-reference inventory]({lp}), recorded {l['at']}, finds all {l['markdown_link_counts'].get('exists',0)} real Markdown links present and all {ledger} explicitly named ledger paths present or registered in lossless archives. Twenty inspected mathematical expressions are excluded from link counts. This checks existence and reconstruction routes, not link anchors or mathematical claims.

The [admission-reference audit]({ep}), completed {e['checked_at_utc']}, checks {e['admission_count']} retained JSON receipts and {e['reference_count']} embedded references. There are {e['status_counts'].get('match',0)} direct matches, {e['status_counts'].get('match_lossless_archive',0)} lossless archive matches and {hist} documented historical matches, with no unexplained mismatch. Historical matches use frozen proof snapshots or exact reconstructible text deltas. The original receipts remain unchanged. This inventory covers the retained JSON admission receipts, not every prose-only early ledger entry, and it does not replay every old arithmetic computation.

V655 checks the reading-index structure: all 307 numbered topic folders have a nonempty standalone `PROOF.md`, and every proof has its relative index link after the topic 298 hyperlink repair. Reading coverage for the 135 proofs in the final claim map is recorded in V652 and again in V674: the 142 final rereads include every mapped proof plus seven supporting proofs. V674 also accepts the final lead report hashes and the three final numerical status-cell updates.
''')
print(now,ep,lp,xp,cp,pp)

"""Authenticate the source-only report correction addendum after root reading."""
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
BASE=Path('bot_research/experiments/validation/reviews/final_report_reading_001')
SUB=BASE/'status_addendum_001'
OUT=BASE/'root_status_addendum_review_001.json'
def sha(b):return hashlib.sha256(b).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
started=now()
assert not OUT.exists()
b=(SUB/'INPUT_BINDINGS.json').read_bytes()
assert sha(b)=='870760715b9b930338ff4cf8ed778f64a2b7916919d195f3ed2e608813f59f9b'
s=json.loads(b)
assert sha((SUB/'REVIEW.md').read_bytes())==s['review_sha256']=='bba4b8965b3fd65cb0d63e86a012e3b3dec57b0807ff89784554ca08594c65da'
assert sha((SUB/'seal_status.py').read_bytes())==s['script_sha256']
assert sha((SUB/'CAPTURE.json').read_bytes())==s['capture_receipt_sha256']
assert sha((SUB/'REPORT.snapshot.md').read_bytes())==s['report_capture']['sha256']
checked=[]
for e in s['inputs']:
 z=Path(e['archive']).read_bytes(); raw=gzip.decompress(z)
 assert sha(z)==e['archive_sha256'] and sha(raw)==e['sha256'] and len(raw)==e['bytes'],e['source']
 if e['expected_prior_hash']:assert sha(raw)==e['expected_prior_hash']
 checked.append(e['source'])
report=(SUB/'REPORT.snapshot.md').read_text()
for phrase in ["recommendation from 22:43Z", "recommendation until 22:43Z", "all seven remaining policies", "a reproduction run, not an engine replay", "AS1C, g0, g1, V29 and af5 win all 40 TIMING2", "903-entry checkpoints include the pre-existing environment"]:
 assert phrase in report,phrase
for phrase in ['matrix bot_research/runs/lead/NAME/results.jsonl','check_runs.py bot_research/runs/lead/NAME/results.jsonl','rr_table.py bot_research/runs/lead/frr1/results.jsonl','rr_nash.py bot_research/runs/lead/frr1/results.jsonl']:
 assert phrase in report,phrase
e=next(e for e in s['inputs'] if e['source']=='bot_research/notes/economy.md')
text=gzip.decompress(Path(e['archive']).read_bytes()).decode()
selection=text.split('### 18.26 ',1)[1].split('\n### ',1)[0]
recommendation=text.split('### 18.32 ',1)[1].split('\n### ',1)[0]
assert '(2026-10-31T22:47:11Z)' in selection and '22:43:35Z' in selection and 'is still open.' in selection
assert '(2026-10-31T23:34:38Z)' in recommendation and '23:33:35Z' in recommendation and 'this makes af5 the' in recommendation
r={'schema':'root-report-status-addendum-review-001','started_utc':started,'completed_utc':now(),'verdict':'CONFIRMED','actual_model':'GPT-6 Astra','addendum_receipt_sha256':sha(b),'report_snapshot_sha256':s['report_capture']['sha256'],'archives_checked':len(checked),'prior_six_corrections_substantively_applied':True,'remaining_corrections':['Distinguish 22:43:35 candidate selection from recommendation announced at 23:34:38 after gate completion.','Link the now completed conditional AF5 matrix proof; scope not proved by hand to the earlier computation, or remove that phrase.'],'manual_review':'Root read the addendum, sealing script, archived economy entries18.26 and18.32 and all relevant report line ranges, verifying substantive wording and finite-evidence scope.','scope':'The preserved report snapshot only; later report edits require separate inspection. No commands from the report, project code, policy, engine, games, replay or tests executed.','script_sha256':sha(Path(__file__).read_bytes())}
OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));print('RECEIPT_SHA256',sha(OUT.read_bytes()))

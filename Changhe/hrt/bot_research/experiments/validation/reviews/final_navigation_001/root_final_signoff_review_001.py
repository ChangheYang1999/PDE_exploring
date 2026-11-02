"""Authenticate navigation archives and independently traverse their retained graph."""
from datetime import datetime,timezone
import gzip
import hashlib
import json
from pathlib import Path
BASE=Path('bot_research/experiments/validation/reviews/final_navigation_001')
SUB=BASE/'final_signoff_001'
OUT=BASE/'root_final_signoff_review_001.json'
def sha(b):return hashlib.sha256(b).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
started=now();assert not OUT.exists()
b=(SUB/'RECEIPT.json').read_bytes()
assert sha(b)=='4247b434048dd30dc6988aad92d12e8fb5a9f017eabcb661c56bbbe48a0d93e2'
s=json.loads(b)
assert sha((SUB/'REVIEW.md').read_bytes())==s['review_sha256']=='0c1e11594fe178c7d1b54322aadcf8264abc2935911d080096387a5bceb4b422'
assert sha((SUB/'seal_signoff.py').read_bytes())==s['script_sha256']
scans=[];narchives=0
for item in s['inspections_authenticated']:
 b=Path(item['path']).read_bytes();assert sha(b)==item['sha256'];obj=json.loads(b)
 for path,e in obj['input_documents'].items():
  z=Path(e['archive']).read_bytes();raw=gzip.decompress(z)
  assert sha(z)==e['archive_sha256'] and sha(raw)==e['sha256'] and len(raw)==e['bytes'],path
  narchives+=1
 assert len(obj['input_documents'])==item['markdown_archive_edges_authenticated']
 scans.append(obj)
for e in s['additional_archived_inputs']:
 z=Path(e['archive']).read_bytes();raw=gzip.decompress(z)
 assert sha(z)==e['archive_sha256'] and sha(raw)==e['sha256'] and len(raw)==e['bytes'],e['source']
 assert sha(Path(e['source']).read_bytes())==e['sha256'],e['source']
for e in s['explicit_prior_pins_authenticated']:assert sha(Path(e['path']).read_bytes())==e['sha256']
index='bot_research/experiments/validation/analysis/README.md'
previous=scans[0]['input_documents'][index]['sha256']
for pub in s['publication_chain']:
 b=Path(pub['path']).read_bytes();assert sha(b)==pub['sha256'];r=json.loads(b)
 assert r['index_before_sha256']==previous
 p=Path(pub['path']).parent
 before=gzip.decompress((p/'index_before.md.gz').read_bytes());after=gzip.decompress((p/'index_after.md.gz').read_bytes())
 assert sha(before)==previous and sha(after)==r['index_after_sha256'] and after.startswith(before)
 for e in r['added_links']:assert sha(Path(e['project_path']).read_bytes())==e['sha256']
 previous=sha(after)
assert sha(Path(index).read_bytes())==previous
final=scans[-1];docs=final['input_documents'];graph={}
assert final['counts']==s['final_counts']
assert not final['missing_links'] and not final['missing_anchors']
for edge in final['edges']:
 assert edge['exists'] and Path(edge['resolved']).exists() and not edge['outside_project']
 if edge['resolved'] in docs:
  graph.setdefault(edge['source'],set()).add(edge['resolved'])
  if edge['fragment']:assert edge['fragment'] in docs[edge['resolved']]['anchors']
reachable=set();todo=[index]
while todo:
 p=todo.pop()
 if p not in reachable:
  reachable.add(p);todo.extend(graph.get(p,set())-reachable)
proofs={p for p in docs if Path(p).name=='PROOF.md'}
results={p for p in docs if Path(p).name=='RESULTS.md'}
assert len(proofs)==169 and proofs<=reachable
assert len(docs)==392 and len(final['edges'])==372
assert len(results)==98 and len(results-reachable)==82
assert set(scans[0]['input_documents'])<=set(docs)
changes=[p for p in scans[0]['input_documents'] if docs[p]['sha256']!=scans[0]['input_documents'][p]['sha256']]
assert set(changes)<={index,'bot_research/reports/REPORT.md'}
current=[p for p,e in docs.items() if sha(Path(p).read_bytes())!=e['sha256']]
assert set(current)<={'bot_research/reports/REPORT.md'}
r={'schema':'root-final-navigation-signoff-review-001','started_utc':started,'completed_utc':now(),'verdict':'CONFIRMED_WITH_DECLARED_INVENTORY_SCOPE','actual_model':'GPT-6 Astra','signoff_receipt_sha256':sha((SUB/'RECEIPT.json').read_bytes()),'markdown_archive_edges_checked':narchives,'additional_archives_checked':len(s['additional_archived_inputs']),'explicit_pins_checked':len(s['explicit_prior_pins_authenticated']),'append_only_publications_checked':len(s['publication_chain']),'final_documents':len(docs),'final_edges':len(final['edges']),'reachable_identified_proofs':len(proofs),'result_pages':len(results),'unlinked_result_pages':len(results-reachable),'index_sha256':previous,'current_differences_from_final_snapshot':current,'scope':'Static archived graph and publication-chain check after root reading both reader scripts and the full signoff. All identified proofs reachable in that bounded inventory.82older RESULTS pages remain unlinked. No browser rendering, complete CommonMark interpretation, new strength evidence, policy/game/engine/replay/test execution or renewed semantic verification of every older proof.','script_sha256':sha(Path(__file__).read_bytes())}
OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));print('RECEIPT_SHA256',sha(OUT.read_bytes()))

"""Independent authentication and retained-log comparison for review012."""
from pathlib import Path
from datetime import datetime, timezone
import gzip, hashlib, json
R = Path('bot_research/experiments/validation/reviews/economy_final_gate_001')
def sha(b): return hashlib.sha256(b).hexdigest()
def js(b): return json.loads(b)
def rows(b): return [js(l) for l in b.splitlines() if l.strip()]
def stamp(): return datetime.now(timezone.utc).isoformat()
started = stamp()
mraw=(R/'repeat_narrative_review_manifest_012.json').read_bytes()
assert sha(mraw)=='9f4b9815ea7f8d85435df41b8362c1e858573f221354d6c244e40e3de2182b33'
m=js(mraw)
for p,v in m['files'].items():
 b=Path(p).read_bytes();assert sha(b)==v['sha256'] and len(b)==v['bytes'],p
phase=R/'repeat-narrative-20261031T234512248491Z';ins=js((phase/'inspection.json').read_bytes());pins=js((phase/'inputs.json').read_bytes());raw={}
for p,v in pins['inputs'].items():
 b=Path(v['snapshot']).read_bytes();assert sha(b)==v['gzip_sha256'];d=gzip.decompress(b);assert sha(d)==v['sha256'] and len(d)==v['bytes'];raw[p]=d
assert len(raw)==68 and not ins['problems']
logs={k:rows(raw[v['path']]) for k,v in ins['retained_log_identities'].items()}
for k,stream in logs.items():
 assert len(stream)==102
 assert {(x['round'],x['player']) for x in stream}=={(r,s) for r in range(51) for s in (0,1)}
idx={k:{(x['round'],x['player']):x for x in stream} for k,stream in logs.items()}
for key in idx['afrr']:
 assert idx['afrr'][key]['event']==idx['afrep'][key]['event']
 assert idx['afrr'][key]['snapshot']==idx['afrep'][key]['snapshot']
for turn in range(5):
 for seat in (0,1):
  a,b=idx['afrr'][turn,seat],idx['g1'][turn,seat]
  assert a['event']==b['event']
  assert {k:v for k,v in a['snapshot'].items() if k!='name'}=={k:v for k,v in b['snapshot'].items() if k!='name'}
# Original completed results are authenticated transitively by the retained006 map.
oldmap=js(raw[str(R/'afrr-20261031T233750162131Z/inputs.json')])
v=oldmap['inputs']['bot_research/runs/economy/afrr/results.jsonl'];packed=Path(v['snapshot']).read_bytes();assert sha(packed)==v['gzip_sha256'];b=gzip.decompress(packed);assert sha(b)==v['sha256'] and len(b)==v['bytes'];rr=rows(b)
line,maxrow=max(enumerate(rr,1),key=lambda x:x[1]['decide_max_seconds'][x[1]['candidate_side']]);maximum=maxrow['decide_max_seconds'][maxrow['candidate_side']]
assert line==8 and maxrow['candidate_side']==1 and maximum==3.0694 and maxrow['decide_max_seconds']==[2.9157,3.0694]
assert 'largest decide call of af5 0.8 s' in js((phase/'reviewed_section.json').read_bytes())['text']
receipt={'schema':'root-repeat-narrative-review-012','started_utc':started,'completed_utc':stamp(),'verdict':'CONFIRMED_CORRECTION_AND_RETAINED_LOG_COMPARISONS','manifest_sha256':sha(mraw),'sealed_files_authenticated':len(m['files']),'archive_edges_authenticated':len(raw),'afrr_afrep_equal_complete_events_and_snapshots':102,'afrr_g1_equal_name_normalized_entries_through_round4':10,'afrr_maximum_elapsed_wall_seconds':maximum,'max_result_line':line,'maximum_candidate_side':1,'scope':'No policy, Engine, game or replay. 006 authenticated summary values, not absence of winning histories. New raw logs authenticated at this later review time; equality does not identify private reasoning or causal timing effects.','script_sha256':sha(Path(__file__).read_bytes())}
out=R/'root_repeat_narrative_review_012.json';assert not out.exists();out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'receipt':str(out),'sha256':sha(out.read_bytes()),'completed_utc':receipt['completed_utc']},indent=2))

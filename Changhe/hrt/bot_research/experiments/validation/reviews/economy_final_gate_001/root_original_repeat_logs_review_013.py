"""Authenticate newly retained original AF5 histories, without policy or Engine calls."""
from datetime import datetime, timezone
from pathlib import Path
import gzip, hashlib, json
R=Path('bot_research/experiments/validation/reviews/economy_final_gate_001')
def sha(b):return hashlib.sha256(b).hexdigest()
def js(b):return json.loads(b)
def rows(b):return [js(l) for l in b.splitlines() if l.strip()]
def stamp():return datetime.now(timezone.utc).isoformat()
started=stamp();mraw=(R/'original_repeat_logs_review_manifest_013.json').read_bytes();assert sha(mraw)=='8568658586c62e999094c1e4f49c0e9f51ef382fcbf2044c2721d5e3f396d169';m=js(mraw)
for p,v in m['files'].items():
 b=Path(p).read_bytes();assert sha(b)==v['sha256'] and len(b)==v['bytes'],p
phase=R/'original-repeat-logs-20261031T234649772765Z';ins=js((phase/'inspection.json').read_bytes());pins=js((phase/'inputs.json').read_bytes());raw={}
for p,v in pins['inputs'].items():
 packed=Path(v['snapshot']).read_bytes();assert sha(packed)==v['gzip_sha256'];b=gzip.decompress(packed);assert sha(b)==v['sha256'] and len(b)==v['bytes'];raw[p]=b
assert len(raw)==29 and not ins['problems'];oldmap=js(raw[str(R/'afrr-20261031T233750162131Z/inputs.json')]);assert not any('/afrr/logs/' in p for p in oldmap['inputs'])
v=oldmap['inputs']['bot_research/runs/economy/afrr/results.jsonl'];b=Path(v['snapshot']).read_bytes();assert sha(b)==v['gzip_sha256'];b=gzip.decompress(b);assert sha(b)==v['sha256'] and len(b)==v['bytes'];results=rows(b);assert len(results)==20
entries=wins=0
for r in results:
 stream=rows(raw[r['log']]);entries+=len(stream);wins+=r['winner']==r['candidate_side'];index={(e['round'],e['player']):e for e in stream};assert len(index)==len(stream)==2*(r['rounds']+1);assert set(index)=={(t,s) for t in range(r['rounds']+1) for s in (0,1)}
 for (t,s),e in index.items():
  assert e['schema_version']==1 and e['snapshot']['name']==r['spec_a' if s==0 else 'spec_b']
  if t==0:assert e['match']['research_specs']==[r['spec_a'],r['spec_b']] and e['match']['research_metadata']==r['metadata'] and e['match']['research_scenario'] is None
  if t==r['rounds']:
   for field in ['hp','gold','n_factories','n_turrets','n_walls','length_path']:assert e['snapshot'][field]==r['players'][s][field]
assert entries==1884 and wins==16
source=raw['bot_research/harness/tournament.py'];assert sha(source)==oldmap['inputs']['bot_research/harness/tournament.py']['sha256']=='561ac17b8e7467dacfd98e820a83d424d286101f3f568e40294339573221e151'
text=source.decode();assert '"first_of_pair": scenario == scenarios[0]' in text and 'keep == "losses" and cand_won and not task.get("first_of_pair")' in text
receipt={'schema':'root-original-repeat-logs-013','started_utc':started,'completed_utc':stamp(),'verdict':'CONFIRMED','sealed_files_authenticated':len(m['files']),'archive_edges_authenticated':len(raw),'original_afrr_games':20,'winning_logs':wins,'parsed_records':entries,'original006_history_logs_authenticated':0,'tournament_source_sha256':sha(source),'scope':'Current retained histories authenticated against result metadata. Original006 was result-only; all20 histories are authenticated later. No Engine replay, policy regeneration, continuous history or causal timing claim.','script_sha256':sha(Path(__file__).read_bytes())}
out=R/'root_original_repeat_logs_review_013.json';assert not out.exists();out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'receipt':str(out),'sha256':sha(out.read_bytes()),'completed_utc':receipt['completed_utc']},indent=2))

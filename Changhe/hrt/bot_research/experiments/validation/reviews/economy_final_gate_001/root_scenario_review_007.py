"""Root finite-scenario recount from retained JSON. No project imports."""
import collections, datetime, gzip, hashlib, json
from pathlib import Path
B=Path('bot_research/experiments/validation/reviews/economy_final_gate_001')
H=lambda b:hashlib.sha256(b).hexdigest()
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
manifest=json.loads((B/'scenario_review_manifest_007.json').read_bytes())
for path,pin in manifest['files'].items():
 raw=Path(path).read_bytes();assert H(raw)==pin['sha256'] and len(raw)==pin['bytes']
phase=B/'scenario-control-20261031T234828252397Z'
inputs=json.loads((phase/'inputs.json').read_bytes())['inputs'];raws={}
for path,pin in inputs.items():
 z=Path(pin['snapshot']).read_bytes();raw=gzip.decompress(z)
 assert H(z)==pin['gzip_sha256'] and H(raw)==pin['sha256'] and len(raw)==pin['bytes'],path
 raws[path]=raw
assert len(inputs)==85
inspection=json.loads((phase/'inspection.json').read_bytes())
assert inspection['status']=='COMPLETE_SCENARIO_REVIEW' and not inspection['problems']
expected={(o,s,side) for o in inspection['opponents'] for s in inspection['scenarios'] for side in [0,1]}
assert len(expected)==120
specs=inspection['specs'];tables={t:{} for t in specs};refs={t:{} for t in specs};selected=[];counts={};sourcepins={}
for run,tag in [('hs3','v29'),('hs4','v29'),('hs34g1','g1'),('scnaf5','af5')]:
 path='bot_research/runs/economy/'+run+'/results.jsonl';rows=[json.loads(x) for x in raws[path].splitlines()];n=0
 for line,r in enumerate(rows,1):
  side=r['candidate_side'];candidate=r['spec_a' if side==0 else 'spec_b'];opp=r['spec_b' if side==0 else 'spec_a']
  key=(opp,r['scenario'],side)
  if candidate!=specs[tag] or opp not in inspection['opponents']:continue
  assert key in expected and key not in tables[tag]
  assert not r.get('error') and not r.get('source_changed') and not any(r.get('scenario_errors',[]))
  assert not any(p['n_rejected'] or p['bot_errors'] for p in r['players'])
  assert r['experiment']==run and r['metadata']['candidate_side']==side and r['metadata']['pair']==r['pair']
  assert r['hp_a']-r['hp_b']==r['hp_diff_a']
  score=.5 if r['winner'] is None else 1.0 if r['winner']==side else 0.0
  value=(score,(r['hp_a']-r['hp_b'])*(1 if side==0 else -1),r['rounds'])
  tables[tag][key]=value;refs[tag][key]={'run':run,'line':line};selected.append(r);n+=1
  for p,h in r['sources'].items():
   if p in sourcepins:assert sourcepins[p]==h
   sourcepins[p]=h
 counts[run]={'all_rows':len(rows),'selected':n}
assert counts=={'hs3':{'all_rows':816,'selected':60},'hs4':{'all_rows':612,'selected':60},'hs34g1':{'all_rows':408,'selected':120},'scnaf5':{'all_rows':120,'selected':120}}
assert all(set(t)==expected for t in tables.values()) and tables['af5']==tables['g1']==tables['v29']
for row in inspection['joined_conditions']:
 key=(row['opponent'],row['scenario'],row['candidate_side'])
 for tag in specs:assert list(tables[tag][key])==row['values'][tag] and refs[tag][key]==row['refs'][tag]
wdl={tag:[sum(v[0]==score for v in table.values()) for score in [1,.5,0]] for tag,table in tables.items()}
assert all(v==[113,0,7] for v in wdl.values()) and wdl==inspection['wdl']
for scenario in inspection['scenarios']:
 for tag,table in tables.items():
  count=[sum(v[0]==score for k,v in table.items() if k[1]==scenario) for score in [1,.5,0]]
  assert count==inspection['by_scenario'][scenario]['wdl'][tag]
for p,h in sourcepins.items():assert H(Path(p).read_bytes())==h,p
rows=[json.loads(x) for x in raws['bot_research/runs/economy/scnaf5/results.jsonl'].splitlines()]
maximum=max((r['decide_max_seconds'][r['candidate_side']],i) for i,r in enumerate(rows,1))
assert maximum==(1.7023,104)
assert H(Path('bot_research/runs/economy/scnaf5/results.jsonl').read_bytes())==inputs['bot_research/runs/economy/scnaf5/results.jsonl']['sha256']
r={'started_utc':started,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_model':'GPT-6 Astra','verdict':'CONFIRMED','H18_31a':True,'sealed_files_verified':len(manifest['files']),'archived_inputs_verified':len(inputs),'selected_rows':len(selected),'exact_conditions':120,'counts':counts,'wdl':wdl,'same_winner_margin_rounds_all_conditions':True,'current_recorded_source_paths_verified':len(sourcepins),'maximum_AF5_wall_seconds':maximum[0],'maximum_result_line':maximum[1],'scope':'Exact recorded outcomes, candidate-oriented HP margins and ending rounds. No full history equality, unrestricted transfer, new policy/Engine/replay run or independent strength sample. No D tuning or change to installed best.py.','input_sha256':{str(p):H(p.read_bytes()) for p in [B/'root_scenario_review_007.py',B/'scenario_review_manifest_007.json',phase/'inspection.json',phase/'inputs.json',B/'SCENARIO_REVIEW_007.md']}}
p=B/'root_scenario_review_007.json'
with p.open('x') as f:json.dump(r,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'receipt':str(p),'sha256':H(p.read_bytes()),'completed_utc':r['completed_utc'],'verdict':r['verdict']}))

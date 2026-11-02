"""Independent retained-record reduction of a completed development sweep."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import random

BASE=Path('bot_research/experiments/validation/reviews/economy_final_gate_001')
def sha(b):return hashlib.sha256(b).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
p=argparse.ArgumentParser()
p.add_argument('--manifest',required=True)
p.add_argument('--manifest-sha',required=True)
p.add_argument('--output',required=True)
a=p.parse_args()
started=now()
out=BASE/a.output
assert not out.exists()
manifest_raw=(BASE/a.manifest).read_bytes()
assert sha(manifest_raw)==a.manifest_sha
manifest=json.loads(manifest_raw)
for name,e in manifest['files'].items():
 b=Path(name).read_bytes();assert sha(b)==e['sha256'] and len(b)==e['bytes'],name
phase=Path(manifest['phase'])
inspection=json.loads((phase/'inspection.json').read_bytes())
assert inspection['status']=='COMPLETED_DEVELOPMENT_SWEEP' and inspection['audit_completed_without_findings'] and not inspection['problems']
assert inspection['campaign_status']['complete_condition_and_completion_evidence']
inputs=json.loads((phase/'inputs.json').read_bytes())['inputs']
raws={}
for name,e in inputs.items():
 z=Path(e['snapshot']).read_bytes();b=gzip.decompress(z)
 assert sha(z)==e['gzip_sha256'] and sha(b)==e['sha256'] and len(b)==e['bytes'],name
 raws[name]=b
specs=inspection['specs'];tag=inspection['candidate'];run=inspection['run']
assert tag in ['af4','af3'] and specs[tag]==specs['v29']+'&attack_from='+tag[-1]
expected={(opp,None,side) for opp in inspection['exact_sweep_specs'] for side in [0,1]}
assert len(expected)==290
assert set(line.strip() for line in raws['bot_research/experiments/economy/opp_afsweep.txt'].decode().splitlines() if line.strip() and not line.startswith('#'))==set(inspection['exact_sweep_specs'])
tables={name:{} for name in specs};cache={};nrows=0;sourcepins={}
for entry in inspection['joined_conditions']:
 key=(entry['opponent'],entry['scenario'],entry['candidate_side']);assert key in expected
 for name,ref in entry['refs'].items():
  if ref['path'] not in cache:cache[ref['path']]=[json.loads(line) for line in raws[ref['path']].splitlines()]
  row=cache[ref['path']][ref['line']-1];side=row['candidate_side']
  candidate=row['spec_a' if side==0 else 'spec_b'];opp=row['spec_b' if side==0 else 'spec_a']
  assert (opp,row.get('scenario'),side)==key and candidate==specs[name]
  assert not row.get('error') and not row.get('source_changed') and not any(row.get('scenario_errors',[]))
  assert all(not x['n_rejected'] and not x['bot_errors'] for x in row['players'])
  assert row['metadata']['candidate_side']==side and row['metadata']['pair']==row['pair']
  assert row['hp_a']-row['hp_b']==row['hp_diff_a']
  score=.5 if row['winner'] is None else float(row['winner']==side)
  value=(score,(row['hp_a']-row['hp_b'])*(1 if side==0 else -1),row['rounds'])
  assert list(value)==entry['values'][name] and key not in tables[name]
  tables[name][key]=value;nrows+=1
  for path,h in row['sources'].items():
   assert path not in sourcepins or sourcepins[path]==h
   sourcepins[path]=h
assert all(set(t)==expected for t in tables.values())
for path,h in sourcepins.items():assert sha(raws[path])==h and sha(Path(path).read_bytes())==h,path
wdl={name:[sum(v[0]==s for v in t.values()) for s in [1,.5,0]] for name,t in tables.items()}
assert wdl==inspection['wdl']
pools=json.loads(raws['bot_research/experiments/economy/opp_afsweep_pools.json'])
assert sum(len(v) for v in pools.values())==145
for pool,opps in pools.items():
 keys={k for k in expected if k[0] in opps}
 counts={name:[sum(t[k][0]==s for k in keys) for s in [1,.5,0]] for name,t in tables.items()}
 assert inspection['pool_tables'][pool]['wdl']==counts
for opp in inspection['exact_sweep_specs']:assert tables[tag][opp,None,0]==tables[tag][opp,None,1]

def bootstrap(keys,name):
 opponents=sorted({k[0] for k in keys})
 values={opp:[tables[tag][k][0]-tables[name][k][0] for k in sorted(keys) if k[0]==opp] for opp in opponents}
 rng=random.Random(1);sample_values=[]
 for unused in range(4000):
  sample=[rng.choice(opponents) for opp in opponents]
  sample_values.append(sum(sum(values[o]) for o in sample)/sum(len(values[o]) for o in sample))
 sample_values.sort()
 return sum(sum(v) for v in values.values())/len(keys),sample_values[100],sample_values[3899]
for name,pair in inspection['paired_comparisons'].items():
 assert pair['better_wdl']==sum(tables[tag][k][0]>tables[name][k][0] for k in expected)
 assert pair['worse_wdl']==sum(tables[tag][k][0]<tables[name][k][0] for k in expected)
 assert pair['equal_wdl']==sum(tables[tag][k][0]==tables[name][k][0] for k in expected)
 assert pair['equal_wdl_hp_rounds']==sum(tables[tag][k]==tables[name][k] for k in expected)
 actual=bootstrap(expected,name);e=pair['interval']
 assert actual==(e['mean'],e['lo'],e['hi'])
strike=bootstrap({k for k in expected if k[0] in pools['strike1']},'af5')
e=inspection['strike1_candidate_minus_af5_interval'];assert strike==(e['mean'],e['lo'],e['hi'])
path='bot_research/runs/economy/'+run+'/results.jsonl'
rows=cache[path]
maximum=max((r['decide_max_seconds'][r['candidate_side']],line) for line,r in enumerate(rows,1))
assert maximum==(inspection['max_candidate_call']['seconds'],inspection['max_candidate_call']['line'])
assert Path(path).read_bytes()==raws[path]
assert len(rows)==290
assert inspection['H18_31b_candidate_component']==(wdl[tag][0]<wdl['af5'][0])
if tag=='af3':assert inspection['H18_31b_combined_af4_and_af3']==(wdl['af3'][0]<wdl['af5'][0] and wdl['af4'][0]<wdl['af5'][0])
r={'schema':'root-development-review-014','started_utc':started,'completed_utc':now(),'verdict':'CONFIRMED','actual_model':'GPT-6 Astra','run':run,'candidate':tag,'manifest_sha256':sha(manifest_raw),'sealed_files_checked':len(manifest['files']),'archive_inputs_checked':len(inputs),'selected_rows_checked':nrows,'unique_conditions':len(expected),'current_source_paths_checked':len(sourcepins),'wdl':wdl,'candidate_minus_af5':inspection['paired_comparisons']['af5'],'strike1_candidate_minus_af5_interval':inspection['strike1_candidate_minus_af5_interval'],'max_candidate_call':inspection['max_candidate_call'],'H18_31b_candidate_component':inspection['H18_31b_candidate_component'],'H18_31b_combined_af4_and_af3':inspection['H18_31b_combined_af4_and_af3'],'scope':'Development on145 exact opponent specs selected for V29/g1 disagreement, both seats. Finite joins and declared descriptive bootstrap independently reproduced. No unrestricted generalization, causal load inference, new games, policy/engine/replay calls, or D tuning.','script_sha256':sha(Path(__file__).read_bytes()),'inspection_sha256':sha((phase/'inspection.json').read_bytes()),'inputs_sha256':sha((phase/'inputs.json').read_bytes())}
out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2));print('RECEIPT_SHA256',sha(out.read_bytes()))

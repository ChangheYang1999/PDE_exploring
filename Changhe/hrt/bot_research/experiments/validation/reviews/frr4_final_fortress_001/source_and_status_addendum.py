"""Supplement archived record checks with static identity and dated incomplete-run status."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import gzip, hashlib, json

OUT=Path('bot_research/experiments/validation/reviews/frr4_final_fortress_001')
UTC=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda b:hashlib.sha256(b).hexdigest()
m=json.loads((OUT/'input_manifest_001.json').read_text())
a=json.loads((OUT/'record_audit_001.json').read_text())
def read(name):
 e=m['files'][name];z=(OUT/e['archive']).read_bytes();b=gzip.decompress(z)
 if sha(b)!=e['sha256'] or sha(z)!=e['archive_sha256'] or len(b)!=e['bytes']:raise ValueError(name)
 return b

def rr(run):return [json.loads(x) for x in read(run+'/results.jsonl').splitlines()]
def normkey(r):
 s=r['candidate_side'];opp=r['spec_b' if s==0 else 'spec_a']
 if opp=='bot_research.experiments.lead.frozen.best_v9e:decide':opp='bot_research.experiments.lead.frozen.best_v9e:@make'
 return (opp,r['scenario'],s)
def outcome(r):
 s=r['candidate_side'];return {'wdl':'D' if r['winner'] is None else ('W' if r['winner']==s else 'L'),
   'hp_candidate':r['hp_a' if s==0 else 'hp_b'],'hp_opponent':r['hp_b' if s==0 else 'hp_a'],'rounds':r['rounds']}
res={'schema':1,'created_utc':UTC(),'reviewer_model':'GPT-6 Astra','static_and_record_reads_only':True,
     'input_manifest_sha256':sha((OUT/'input_manifest_001.json').read_bytes()),'record_audit_sha256':sha((OUT/'record_audit_001.json').read_bytes())}
res['terminal_outcome_arithmetic']={}
for run in ['bot_research/runs/lead/frr4','bot_research/runs/lead/frr5']:
 checked=0;errors=[]
 for row in rr(run):
  records=[json.loads(x) for x in read(row['log']).splitlines()]
  for rnd in range(1,row['rounds']+1):
   recs=[r for r in records if r['round']==rnd];hp=[next(r for r in recs if r['player']==s)['snapshot']['hp'] for s in (0,1)]
   if hp[0]<=0 and hp[1]<=0:expected={'winner':None,'reason':'both_bases_destroyed'}
   elif min(hp)<=0:expected={'winner':0 if hp[1]<=0 else 1,'reason':'base_destroyed'}
   elif rnd>=50:expected={'winner':None if hp[0]==hp[1] else (0 if hp[0]>hp[1] else 1),'reason':'round_limit'}
   else:expected=None
   for rec in recs:
    if rec.get('result')!=expected:errors.append({'log':row['log'],'round':rnd,'side':rec['player'],'actual':rec.get('result'),'expected':expected})
   if expected is not None and rnd!=row['rounds']:errors.append({'log':row['log'],'reason':'records continue after terminal'})
   checked+=1
 res['terminal_outcome_arithmetic'][run]={'rounds_checked':checked,'errors':errors,
    'method':'Integer comparisons on retained snapshots following td_game/engine.py lines 111-119, without importing or executing that module'}
res['wrapper_normalized_comparisons']={}
x=rr('bot_research/runs/defense/x215_v46_lead');mx={normkey(r):r for r in x}
for run in ['bot_research/runs/lead/frr3','bot_research/runs/lead/frr4']:
 rr2=rr(run);my={normkey(r):r for r in rr2};common=sorted(set(mx)&set(my),key=str)
 res['wrapper_normalized_comparisons'][run]={'common_conditions':len(common),'comparisons':[{'opponent':k[0],'scenario':k[1],'candidate_side':k[2],
    'x215':outcome(mx[k]),'lead':outcome(my[k]),'same':outcome(mx[k])==outcome(my[k])} for k in common]}
res['wrapper_scope']='best_v9e:decide renews a default Insurer at round 1 for each player; :@make creates the same default Insurer before play. Both submit one call per reached round, including forced openings. Their full strings and timed constructor locations differ; equal observed outcomes do not prove equal complete histories under another policy wall-clock cutoff.'
res['frozen_sha256sums']={}
for v in ['v46','v48']:
 p=f'bot_research/bots/defense/frozen/{v}/SHA256SUMS';errors=[];count=0
 for line in read(p).decode().splitlines():
  fields=line.split()
  if len(fields)!=2:continue
  digest,name=fields;count+=1;q=f'bot_research/bots/defense/frozen/{v}/{name}'
  if m['files'].get(q,{}).get('sha256')!=digest:errors.append(q)
 res['frozen_sha256sums'][v]={'entries':count,'errors':errors}
res['active_source_paths']={}
for row in rr('bot_research/runs/lead/frr4')+rr('bot_research/runs/lead/frr5'):
 for p in row['sources']:res['active_source_paths'][p]=m['files'][p]['sha256']
 for spec in [row['spec_a'],row['spec_b']]:
  for p in m['current_static_versions'][spec]['closure_paths']:res['active_source_paths'][p]=m['files'][p]['sha256']
res['active_source_paths']['td_game/balanced.json']=a['rules_source']['sha256']
res['active_source_drift_at_addendum']=[p for p,d in res['active_source_paths'].items() if not Path(p).is_file() or sha(Path(p).read_bytes())!=d]
res['archive_recheck_count']=0
for name in m['files']:read(name);res['archive_recheck_count']+=1
res['completed_utc']=UTC()
with (OUT/'source_addendum_001.json').open('x') as f:json.dump(res,f,indent=2,sort_keys=True);f.write('\n')

status={'schema':1,'inspection_started_utc':UTC(),'scope':'Dated status extension only; no new full-game raw audit beyond input_manifest_001 snapshot',
        'files':{},'absent':[],'runs':{}}
for name in ['bot_research/runs/lead/frr5/results.jsonl','bot_research/runs/lead/frr5/summary.md','bot_research/runs/lead/frr5.out',
             'bot_research/runs/lead/frr6/results.jsonl','bot_research/runs/lead/frr6/summary.md','bot_research/runs/lead/frr6.out',
             'bot_research/runs/lead/queue_h19.log']:
 p=Path(name)
 if not p.exists():status['absent'].append({'path':name,'time':UTC()});continue
 stat=p.stat();b=p.read_bytes();stat2=p.stat();q=OUT/'inputs'/f'{sha(b)}.gz'
 if not q.exists():
  with q.open('xb') as f:f.write(gzip.compress(b,compresslevel=6,mtime=0))
 z=q.read_bytes()
 if gzip.decompress(z)!=b:raise ValueError('status archive mismatch '+name)
 status['files'][name]={'sha256':sha(b),'bytes':len(b),'archive':q.relative_to(OUT).as_posix(),'archive_sha256':sha(z),'archive_bytes':len(z),
    'read_utc':UTC(),'mtime_utc':datetime.fromtimestamp(stat2.st_mtime,timezone.utc).isoformat(),
    'stat_stable_during_read':(stat.st_size,stat.st_mtime_ns)==(stat2.st_size,stat2.st_mtime_ns)}
 if name.endswith('results.jsonl'):
  if b and not b.endswith(b'\n'):raise ValueError('incomplete status line')
  rows=[json.loads(line) for line in b.splitlines()];run=name.rsplit('/',1)[0]
  keys=Counter(normkey(r) for r in rows);w=Counter(outcome(r)['wdl'] for r in rows)
  status['runs'][run]={'completed_result_rows':len(rows),'planned_rows':20 if run.endswith('frr5') else 24,'prefix_wdl':dict(w),
    'distinct_conditions':len(keys),'duplicate_count':sum(n-1 for n in keys.values()),
    'full_source_specs':sorted({r[k] for r in rows for k in ['spec_a','spec_b']}),
    'rows_have_errors':sum(r.get('error') is not None for r in rows),'recorded_source_changed':sum(r.get('source_changed') is not False for r in rows)}
status['inspection_finished_utc']=UTC()
with (OUT/'status_snapshot_002.json').open('x') as f:json.dump(status,f,indent=2,sort_keys=True);f.write('\n')
print('terminal',res['terminal_outcome_arithmetic'])
print('wrapper',[(k,v['common_conditions'],sum(c['same'] for c in v['comparisons'])) for k,v in res['wrapper_normalized_comparisons'].items()])
print('active_source_count',len(res['active_source_paths']),'drift',res['active_source_drift_at_addendum'])
print('status',status['inspection_finished_utc'],status['runs'])
print('source_addendum_sha256',sha((OUT/'source_addendum_001.json').read_bytes()))
print('status_sha256',sha((OUT/'status_snapshot_002.json').read_bytes()))

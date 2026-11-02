"""Seal only this review; authenticate archived bytes and recheck current source identities."""
import gzip,hashlib,json,os
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
OUT=Path('bot_research/experiments/validation/reviews/frr5_frr6_final_fortress_001');UTC=lambda:datetime.now(timezone.utc).isoformat();sha=lambda b:hashlib.sha256(b).hexdigest()
manifests={p.name:json.loads(p.read_bytes()) for p in sorted(OUT.glob('input_manifest_*.json'))};final=manifests['input_manifest_final.json']
a=json.loads((OUT/'record_audit_final.json').read_bytes());s=json.loads((OUT/'supplementary_checks_final.json').read_bytes())
errors=[];archive_edges=0;archives={};active={};record_changes=[]
for name,m in manifests.items():
 for p,e in m['files'].items():
  z=(OUT/e['archive']).read_bytes();b=gzip.decompress(z);archive_edges+=1
  if sha(z)!=e['archive_sha256'] or sha(b)!=e['sha256'] or len(b)!=e['bytes']:errors.append({'manifest':name,'path':p,'error':'archive identity'})
  archives[e['archive']]=len(z)
for run,c in a['campaigns'].items():
 if c['observed_rows']!=c['planned_conditions'] or c['missing_conditions'] or c['unexpected_conditions'] or c['duplicates'] or c['metadata_errors']:
  errors.append({'run':run,'error':'condition accounting'})
 if not c['summary_present']:errors.append({'run':run,'error':'summary absent'})
 logs=set(final['snapshot_runs'][run]['log_directory_files']);expected={d['log'] for d in c['conditions']}
 if logs!=expected:errors.append({'run':run,'error':'log directory accounting','missing':sorted(expected-logs),'extra':sorted(logs-expected)})
 for d in c['conditions']:
  if d['raw_check']['errors'] or d['source_check']['errors']:errors.append({'run':run,'condition':d['condition'],'error':'raw/source audit'})
 for d in c['conditions']:
  # Archived rows bind all source identities; no policy invocation.
  pass
for v in a['frozen_packages'].values():
 if not all(x['matches'] for x in v):errors.append({'error':'frozen package manifest mismatch'})
for run,r in s['summary_checks'].items():
 if r['errors']:errors.append({'run':run,'error':'summary accounting'})
if s['finite_matrix_extension']['errors']:errors.append({'error':'finite matrix exact row checks'})
for run in a['campaigns']:
 rp='bot_research/runs/lead/'+run+'/results.jsonl';e=final['files'][rp];b=gzip.decompress((OUT/e['archive']).read_bytes())
 for r in (json.loads(x) for x in b.splitlines()):active.update(r['sources'])
for spec,v in final['current_static_versions'].items():
 for p in v['closure_paths']:active[p]=final['files'][p]['sha256']
for p in ['bot_research/bots/best.py','td_game/balanced.json']:active[p]=final['files'][p]['sha256']
active_mismatches=[p for p,h in active.items() if not Path(p).is_file() or sha(Path(p).read_bytes())!=h]
if active_mismatches:errors.append({'error':'current active source drift','paths':active_mismatches})
for p,e in final['files'].items():
 if '/runs/lead/frr' in p and (p.endswith('.jsonl') or p.endswith('/summary.md')):
  if not Path(p).is_file() or sha(Path(p).read_bytes())!=e['sha256']:record_changes.append(p)
if record_changes:errors.append({'error':'closed retained record drift','paths':record_changes})
# All own inputs are already bound; avoid a recursive self hash.
outputs={p.relative_to(OUT).as_posix():{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size}
 for p in OUT.rglob('*') if p.is_file() and 'inputs' not in p.relative_to(OUT).parts and p.name!='seal_001.json'}
report={'schema':1,'sealed_utc':UTC(),'reviewer_model':'GPT-6 Astra','verdict':'CONFIRMED' if not errors else 'OPEN',
 'execution':'source and retained JSON only; zero policy constructors, decisions, engines, replays, existing checkers or new games',
 'archive_edge_count':archive_edges,'unique_archives':len(archives),'compressed_archive_bytes':sum(archives.values()),
 'active_current_paths_checked':len(active),'active_current_mismatches':active_mismatches,'closed_record_changes':record_changes,
 'errors':errors,'outputs':outputs}
p=OUT/'seal_001.json'
with p.open('x') as f:json.dump(report,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'path':p.as_posix(),'sha256':sha(p.read_bytes()),'sealed_utc':report['sealed_utc'],'verdict':report['verdict'],
 'archive_edge_count':archive_edges,'unique_archives':len(archives),'compressed_archive_bytes':sum(archives.values()),'active_current_paths_checked':len(active),'errors':errors},indent=2))

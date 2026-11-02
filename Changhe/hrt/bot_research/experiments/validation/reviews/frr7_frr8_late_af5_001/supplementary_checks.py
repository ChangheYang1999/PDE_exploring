"""Pure stdlib checks of archived summaries, source identities and the finite matrix witness."""
import ast,gzip,hashlib,json,shlex,sys
from collections import Counter,defaultdict
from datetime import datetime,timezone
from fractions import Fraction as F
from pathlib import Path
OUT=Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001');label=sys.argv[1]
sha=lambda b:hashlib.sha256(b).hexdigest();UTC=lambda:datetime.now(timezone.utc).isoformat()
p=OUT/('input_manifest_'+label+'.json');m=json.loads(p.read_bytes());audit_label=sys.argv[2] if len(sys.argv)>2 else label;a=json.loads((OUT/('record_audit_'+audit_label+'.json')).read_bytes())
def read(name):
 e=m['files'][name];z=(OUT/e['archive']).read_bytes();b=gzip.decompress(z)
 if sha(z)!=e['archive_sha256'] or sha(b)!=e['sha256'] or len(b)!=e['bytes']:raise ValueError(name)
 return b
def result(row,side):return 'D' if row['winner'] is None else ('W' if row['winner']==side else 'L')
def require(x,desc,errors):
 if not x:errors.append(desc)
out={'schema':1,'started_utc':UTC(),'reviewer_model':'GPT-6 Astra','input_manifest_sha256':sha(p.read_bytes()),'summary_checks':{}}
for run in ['frr2','frr4','frr5','frr6','frr7','frr8']:
 base='bot_research/runs/lead/'+run
 if base+'/summary.md' not in m['files']:continue
 rr=[json.loads(x) for x in read(base+'/results.jsonl').splitlines()];errors=[];tables=[];table=[]
 for line in read(base+'/summary.md').decode().splitlines()+['']:
  if line.startswith('|'):table.append([x.strip() for x in line.strip().strip('|').split('|')])
  elif table:tables.append(table);table=[]
 require(len(tables)==3,'three summary tables',errors)
 groups=defaultdict(list)
 for r in rr:
  s=r['candidate_side'];groups[(r['spec_a' if s==0 else 'spec_b'],r['spec_b' if s==0 else 'spec_a'])].append(r)
 parsed={(r[0],r[1]):r[2:] for r in tables[0][2:]}
 require(set(parsed)==set(groups),'pair summary rows',errors)
 for k,rows in groups.items():
  w=Counter(result(r,r['candidate_side']) for r in rows);diff=[r['hp_diff_a']*(1-2*r['candidate_side']) for r in rows]
  vals=[str(len(rows)),str(w['W']),str(w['D']),str(w['L']),f'{sum(diff)/len(rows):.1f}',str(min(diff)),f'{sum(r["rounds"] for r in rows)/len(rows):.1f}',
    str(sum(r['players'][r['candidate_side']]['n_rejected'] for r in rows)),
    str(sum(len(r['players'][r['candidate_side']]['bot_errors']) for r in rows)),
    str(sum(len(r['players'][1-r['candidate_side']]['bot_errors']) for r in rows)),
    f'{sum(r["decide_seconds"][r["candidate_side"]] for r in rows)/len(rows):.2f} ({max(r["decide_max_seconds"][r["candidate_side"]] for r in rows):.2f})']
  require(parsed.get(k)==vals,'pair summary fields '+str(k),errors)
 candidates=defaultdict(list)
 for r in rr:candidates[r['spec_a' if r['candidate_side']==0 else 'spec_b']].append(r)
 parsed={r[0]:r[1:] for r in tables[1][2:]};require(set(parsed)==set(candidates),'candidate table rows',errors)
 for cand,rows in candidates.items():
  w=Counter(result(r,r['candidate_side']) for r in rows)
  vals=[str(len(rows)),str(w['W']),str(w['D']),str(w['L']),f'{(w["W"]+w["D"]/2)/len(rows):.3f}']
  require(parsed.get(cand)==vals,'candidate totals '+cand,errors)
 perspectives=defaultdict(list)
 for r in rr:
  for s in (0,1):perspectives[r['spec_a' if s==0 else 'spec_b']].append((r,s))
 parsed={r[0]:r[1:] for r in tables[2][2:]};require(set(parsed)==set(perspectives),'all-bot summary rows',errors)
 for spec,rs in perspectives.items():
  w=Counter(result(r,s) for r,s in rs);diff=[r['hp_diff_a']*(1-2*s) for r,s in rs]
  vals=[str(len(rs)),str(w['W']),str(w['D']),str(w['L']),f'{(w["W"]+w["D"]/2)/len(rs):.3f}',f'{sum(diff)/len(rs):.1f}']
  require(parsed.get(spec)==vals,'all-bot summary fields '+spec,errors)
 out['summary_checks'][run]={'errors':errors,'rows':len(rr),'pair_rows':len(groups),'all_perspective_rows':len(perspectives)}
# Exact source comparison, without compiling or importing any source.
v46='bot_research/bots/defense/frozen/v46/fortress.py';v48='bot_research/bots/defense/frozen/v48/fortress.py'
out['fortress_sources']={'v46_sha256':sha(read(v46)),'v48_sha256':sha(read(v48)),'bytes_equal':read(v46)==read(v48)}
best='bot_research/bots/best.py';frozen='bot_research/experiments/lead/frozen/best_v9e.py'
out['installed_entrypoint']={'best_sha256':sha(read(best)),'best_v9e_sha256':sha(read(frozen)),'bytes_equal':read(best)==read(frozen),
 'fortress_v48_is_installed_best':read(best)==read(v48)}
# Verify recorded maxima, without claiming a per-round timing trace exists.
out['fortress_maxima_by_run']={}
for run in ['frr1','frr2','frr3','frr4','frr5','frr6']:
 name='bot_research/runs/lead/'+run+'/results.jsonl'
 if name not in m['files']:continue
 rr=[json.loads(x) for x in read(name).splitlines()];mx=defaultdict(float)
 for r in rr:
  for s in (0,1):
   spec=r['spec_a' if s==0 else 'spec_b']
   if spec in [a['specs'][k] for k in ['V41','V46','V48']]:mx[spec]=max(mx[spec],r['decide_max_seconds'][s])
 out['fortress_maxima_by_run'][run]=dict(mx)
out['af5_spec_exact_match']=a['specs']['AF5']==read('bot_research/experiments/economy/specs/af5.spec').decode().strip()
out['finished_utc']=UTC();p=OUT/('supplementary_checks_'+label+'.json')
with p.open('x') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'path':p.as_posix(),'sha256':sha(p.read_bytes()),'finished_utc':out['finished_utc'],
 'summary_checks':out['summary_checks'],'installed_entrypoint':out['installed_entrypoint'],'af5_spec_exact_match':out['af5_spec_exact_match']},indent=2))

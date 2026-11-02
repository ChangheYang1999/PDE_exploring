"""Pure stdlib checks of archived summaries, source identities and the finite matrix witness."""
import ast,gzip,hashlib,json,shlex,sys
from collections import Counter,defaultdict
from datetime import datetime,timezone
from fractions import Fraction as F
from pathlib import Path
OUT=Path('bot_research/experiments/validation/reviews/frr5_frr6_final_fortress_001');label=sys.argv[1]
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
for run in ['frr3','frr4','frr5','frr6']:
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
# Rejoin the base matrix by full specifications. No raw frr1 replay or checker execution here.
name='bot_research/experiments/validation/analysis/frr1_equilibrium/verification/independent_audit_001.json'
if name in m['files']:
 receipt=json.loads(read(name));order=['BEST_V9E','BEST_V9F','AF2G','P5TNUBM','V41','V29','G1','GUARD00','TDEF','AS1C'];M=[[0]*10 for _ in range(10)];seen=defaultdict(list);errors=[]
 rr=[json.loads(x) for x in read('bot_research/runs/lead/frr1/results.jsonl').splitlines()]
 index={a['specs'][k]:i for i,k in enumerate(order)}
 for r in rr:
  i=index[r['spec_a']];j=index[r['spec_b']];w={'W':1,'D':0,'L':-1}[result(r,0)]
  seen[(i,j)].append(w);M[i][j]=w
 require(len(rr)==90 and len(seen)==90 and all(len(v)==1 for v in seen.values()),'90 unique full-spec ordered pairs',errors)
 require(all(M[i][j]==-M[j][i] for i in range(10) for j in range(10)),'skew base payoffs',errors)
 require(M==receipt['matrix_row_payoff_WDL'],'prior exact base matrix',errors)
 require(sha(read('bot_research/runs/lead/frr1/results.jsonl'))==receipt['input_hashes']['bot_research/runs/lead/frr1/results.jsonl'],'prior base result identity',errors)
 z=[F(1,3) if i in [6,7,9] else F(0) for i in range(10)];dual=[sum(F(M[i][j])*z[j] for j in range(10)) for i in range(10)];add={}
 for run in ['frr3','frr5']:
  by=defaultdict(list)
  for d in a['campaigns'][run]['conditions']:by[index[d['condition'][0]]].append({'W':1,'D':0,'L':-1}[d['outcome']])
  row=[by[i][0] for i in range(10)]
  require(all(len(by[i])==2 and len(set(by[i]))==1 for i in range(10)),run+' both-seat equality',errors)
  require(row==M[4],run+' v41 row agreement',errors)
  add[run]={'row':row,'payoff_against_z':str(sum(F(row[j])*z[j] for j in range(10)))}
 out['finite_matrix_extension']={'errors':errors,'base_input_sha256':sha(read('bot_research/runs/lead/frr1/results.jsonl')),
 'prior_receipt_sha256':sha(read(name)),'base_matrix':M,'z':[str(x) for x in z],'base_dual':[str(x) for x in dual],
 'added_rows':add,'unplayed_mutual_entry':'arbitrary real q; skew transpose -q; no assumed draw',
 'conditional_proof':'finite_matrix_extension/PROOF.md'}
out['finished_utc']=UTC();p=OUT/('supplementary_checks_'+label+'.json')
with p.open('x') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'path':p.as_posix(),'sha256':sha(p.read_bytes()),'finished_utc':out['finished_utc'],
 'summary_checks':out['summary_checks'],'installed_entrypoint':out['installed_entrypoint'],
 'finite_matrix_errors':out.get('finite_matrix_extension',{}).get('errors')},indent=2))

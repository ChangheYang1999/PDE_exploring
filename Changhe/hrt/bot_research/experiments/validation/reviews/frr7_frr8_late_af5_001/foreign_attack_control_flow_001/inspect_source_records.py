"""Source and retained-record inspection only. Does not import any project module."""
import ast, gzip, hashlib, json, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
BASE=Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001')
OUT=BASE/'foreign_attack_control_flow_001'
START=datetime.now(timezone.utc).isoformat()
sha=lambda b:hashlib.sha256(b).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
inputs={}; errors=[]; edges={}
(OUT/'inputs').mkdir(exist_ok=True)
def require(ok,msg):
 if not ok:errors.append(msg)
def read(p,keep=True):
 p=Path(p);b=p.read_bytes();e={'sha256':sha(b),'bytes':len(b),'read_utc':now()}
 if keep:
  z=gzip.compress(b,mtime=0);a=OUT/'inputs'/(sha(b)+'.gz')
  if not a.exists():a.write_bytes(z)
  e.update(archive=a.relative_to(OUT).as_posix(),archive_sha256=sha(z),archive_bytes=len(z))
 inputs[p.as_posix()]=e
 return b
def save(p,value):
 b=(json.dumps(value,indent=2,sort_keys=True)+'\n').encode()
 with p.open('xb') as f:f.write(b)
 return {'sha256':sha(b),'bytes':len(b)}
source_path='bot_research/bots/economy/frozen/v29/econ29.py'
source=read(source_path).decode();tree=ast.parse(source)
notes_path='bot_research/notes/economy.md';notes=read(notes_path).decode()
section=notes.split('### 18.35 ',1)[1].split('\n### ',1)[0]
claim='no attack, finish or doom purchase before foreign_attack_from=11'
require(claim in section,'exact reviewed 18.35 phrase still present in captured bytes')
for p in ['bot_research/experiments/lead/rr_specs.sh','bot_research/experiments/economy/specs/af5.spec',
 'bot_research/bots/defense/frozen/v15/plan.py','bot_research/bots/defense/frozen/v15/templates.py',
 'bot_research/harness/match.py','bot_research/harness/scenarios.py']:
 read(p)
manifest=json.loads(read(BASE/'input_manifest_final_001.json'))
prior=json.loads(read(BASE/'seal_001.json'))
audit=json.loads(read(BASE/'record_audit_final_001.json'))
require(inputs[source_path]['sha256']==manifest['files'][source_path]['sha256'],'frozen econ29 agrees with original sealed identity')
specs={k:audit['specs'][k] for k in ['V29','AF5','G1']}
make=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='make')
defaults={a.arg:ast.literal_eval(d) for a,d in zip(make.args.args[-len(make.args.defaults):],make.args.defaults)}
resolved={}
for name,sp in specs.items():
 options={k:json.loads(v) for k,v in (part.split('=',1) for part in sp.partition('?')[2].split('&'))}
 resolved[name]={**defaults,**options}
require(resolved['AF5']['attack_from']==5 and resolved['G1']['attack_from']==7,'distinct attack_from specs')
for name in ['AF5','G1']:
 for k,v in {'foreign_attack_from':11,'foreign_open':True,'hold_income':None,'lift_idle':None,'finish':'opt','doom':'next',
             'none_from':4,'none_first':True,'none_frac':1.0,'r1_units':1,'r1_tier':'tier1','layout':'lead_v3',
             'r1_guard':0,'guard_gold':0,'early_threat':None,'late_round':6,'sat_from':None}.items():
  require(resolved[name][k]==v,'resolved '+name+' '+k)
require(Path('bot_research/experiments/economy/specs/af5.spec').read_text().strip()==specs['AF5'],'economy AF5 and lead exact spec')
decide=next(x for x in make.body if isinstance(x,ast.FunctionDef) and x.name=='decide')
parents={child:node for node in ast.walk(tree) for child in ast.iter_child_nodes(node)}
def ancestors(node):
 out=[]
 while node in parents:
  node=parents[node]
  if isinstance(node,(ast.FunctionDef,ast.If)):
   out.append({'kind':type(node).__name__,'line':node.lineno,'end_line':node.end_lineno,
    'name_or_test':node.name if isinstance(node,ast.FunctionDef) else ast.unparse(node.test)})
 return out
buys=[]
for node in ast.walk(decide):
 if isinstance(node,ast.Constant) and node.value=='buy_minion':
  buys.append({'line':node.lineno,'ancestors':ancestors(node)})
attack=next(x for x in decide.body if isinstance(x,ast.FunctionDef) and x.name=='attack')
require(isinstance(attack.body[0],ast.If) and ast.unparse(attack.body[0].test)=='hold' and
        len(attack.body[0].body)==1 and isinstance(attack.body[0].body[0],ast.Return),'attack begins with hold return')
finish=next(x for x in decide.body if isinstance(x,ast.If) and ast.unparse(x.test).startswith('finish and'))
doom=next(x for x in decide.body if isinstance(x,ast.If) and ast.unparse(x.test).startswith('doom and'))
open_branch=next(x for x in decide.body if isinstance(x,ast.If) and 'none_first' in ast.unparse(x.test))
require(not any(isinstance(x,ast.Name) and x.id=='hold' for x in ast.walk(finish)),'finish subtree has no hold reference')
require(not any(isinstance(x,ast.Name) and x.id=='hold' for x in ast.walk(doom)),'doom subtree has no hold reference')
require(finish.lineno<open_branch.lineno<doom.lineno,'finish/open/doom ordering')
require(isinstance(open_branch.body[0],ast.Expr) and ast.unparse(open_branch.body[0].value)=='attack(none_frac)','open calls gated helper')
require(ast.unparse(open_branch.body[1])=='attacked = True','open sets attacked regardless of helper proposal')
segments={name:{'line':lo,'end_line':hi,'text':'\n'.join(source.splitlines()[lo-1:hi])}
 for name,lo,hi in [('defaults',493,508),('foreign_and_hold',559,576),('reservation_and_add',588,601),('ordinary_attack',668,681),
 ('opening',718,737),('finish',738,756),('open_case',757,761),('defense_and_saturation',762,803),('doom_and_return',805,846),('historical_explicit_finish_exception',234,242)]}

def archive_original(name):
 e=manifest['files'][name];z=read(BASE/e['archive'],False);b=gzip.decompress(z)
 require(sha(z)==e['archive_sha256'] and sha(b)==e['sha256'] and len(b)==e['bytes'],'original archive '+name)
 current=read(name,False);require(current==b,'current original '+name);edges[name]=e
 return b

# Retained histories only. No attempted reconstruction of discarded policy proposals.
new_rows=[json.loads(x) for x in read('bot_research/runs/economy/scnaf5/results.jsonl').splitlines()]
require(len(new_rows)==120,'scnaf5 completed result rows')
retained=[];missing=[];foreign_certificates=[];early_buys=[]
for campaign,rows in [('scnaf5',new_rows),('frr7',[json.loads(x) for x in archive_original('bot_research/runs/lead/frr7/results.jsonl').splitlines()])]:
 for row in rows:
  side=row['candidate_side'];sp=row['spec_a' if side==0 else 'spec_b']
  require(sp==specs['AF5'],'AF5 original specification '+campaign)
  lp=row.get('log')
  if not lp or not Path(lp).is_file():
   missing.append({'campaign':campaign,'scenario':row['scenario'],'side':side,'opponent':row['spec_b' if side==0 else 'spec_a'],'log':lp})
   continue
  # Archive scnaf5 kept originals; frr7 originals already have immutable local archives.
  b=read(lp) if campaign=='scnaf5' else archive_original(lp)
  rr=[json.loads(x) for x in b.splitlines()];by={(x['round'],x['player']):x for x in rr}
  require(len(by)==len(rr),'unique record keys '+lp)
  require(row['sources'].get(source_path)==inputs[source_path]['sha256'] and row['source_changed'] is False,'recorded frozen source '+lp)
  require(row.get('error') is None and row['scenario_errors']==[[],[]],'successful original calls '+lp)
  k=int(row['scenario'].rsplit(':',1)[1])
  first=by[(0,side)]['snapshot'];opfirst=by[(0,1-side)]['snapshot']
  # At round one, default lead_v3 stage zero can request only (0,1),(11,3).
  # All other construction branches are inactive on the empty initial observation.
  # The retained snapshot gives buildings via action events, so use accepted round-one build cells.
  cells=[(e['action']['x'],e['action']['y']) for e in by[(1,side)]['event']
    if e['kind']=='action' and e['accepted'] and e['action']['op'] in ('build_wall','build_turret')]
  alien=sorted(set(cells)-{(0,1),(11,3)})
  initial_ok=(first['n_walls']==first['n_turrets']==opfirst['n_walls']==opfirst['n_turrets']==0
   and first['n_factories']==opfirst['n_factories']==0)
  foreign=initial_ok and bool(alien)
  cert={'campaign':campaign,'log':lp,'candidate_side':side,'scenario':row['scenario'],
        'initial_empty_counts':initial_ok,'round_one_accepted_cells_outside_possible_own_request':alien,
        'foreign_latches_on_round_two_under_static_initial_call_argument':foreign}
  foreign_certificates.append(cert)
  counts=[]
  for rnd in range(k+1,min(10,row['rounds'])+1):
   rec=by[(rnd,side)]
   purchases=[e for e in rec['event'] if e['kind']=='action' and e['accepted'] and e['action']['op']=='buy_minion']
   if purchases:
    e={'campaign':campaign,'log':lp,'scenario':row['scenario'],'side':side,'round':rnd,
       'minions':dict(Counter(x['action']['type'] for x in purchases)), 'accepted_events':purchases,
       'foreign_latched_by_round_two':foreign,'branch_identity_recorded':False}
    counts.append(e);early_buys.append(e)
  retained.append({'campaign':campaign,'log':lp,'sha256':sha(b),'records':len(rr),'side':side,
     'scenario':row['scenario'],'scripted_rounds':k,'through_round':min(10,row['rounds']),
     'postscript_pre11_purchase_rounds':counts})

# Preserve the original outputs and prior seals. Dynamic economy notes are snapshot-bound only.
prior_checks=[]
for rel,e in prior['outputs'].items():
 same=sha((BASE/rel).read_bytes())==e['sha256'];require(same,'prior output unchanged '+rel)
 prior_checks.append({'path':rel,'unchanged':same})
for p,e in inputs.items():
 if p!=notes_path:require(sha(Path(p).read_bytes())==e['sha256'],'end source/input identity '+p)
finish_time=now()
data={'schema':1,'started_utc':START,'completed_utc':finish_time,'reviewer_model':'GPT-6 Astra',
 'execution':'Static AST/source reads and retained JSON only. No policy constructors or calls, Engine/game/replay, or existing project checker execution.',
 'errors':errors,'audit_completed':not errors,'input_manifest':inputs,'prior_archive_edges':edges,
 'captured_economy_18_35':section,'literal_claim':claim,'full_specs':specs,'resolved_parameters':resolved,
 'source_segments':segments,'buy_minion_syntax_sites':buys,'branch_tests':{'finish':ast.unparse(finish.test),'doom':ast.unparse(doom.test),'open':ast.unparse(open_branch.test)},
 'prior_outputs_unchanged':prior_checks,'retained_history_scan':retained,'not_retained_rows':missing,
 'foreign_latch_source_certificates':foreign_certificates,'postscript_pre11_purchases':early_buys,
 'counts':{'scnaf5_result_rows':120,'scnaf5_retained_histories_scanned':sum(x['campaign']=='scnaf5' for x in retained),
 'scnaf5_unavailable_histories':sum(x['campaign']=='scnaf5' for x in missing),'frr7_retained_histories_scanned':sum(x['campaign']=='frr7' for x in retained),
 'postscript_pre11_purchase_rounds':len(early_buys),'certified_foreign_pre11_purchase_rounds':sum(x['foreign_latched_by_round_two'] for x in early_buys)},
 'scope':'A missing hold test in a source branch is not by itself a reachable-game counterexample. Retained action events do not identify which internal purchase branch produced them. Absent winning logs are not filled or reconstructed.'}
save(OUT/'EVIDENCE.json',data)
print(json.dumps({'completed_utc':finish_time,'errors':errors,'counts':data['counts'],'purchases':early_buys},indent=2))

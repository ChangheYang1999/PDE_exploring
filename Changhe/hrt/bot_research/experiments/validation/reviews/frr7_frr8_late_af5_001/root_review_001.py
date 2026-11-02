"""Independent retained-byte, record and rational review. No game imports."""
import collections, datetime, gzip, hashlib, json
from fractions import Fraction as F
from pathlib import Path
B=Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001')
H=lambda b:hashlib.sha256(b).hexdigest()
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
seal=json.loads((B/'seal_001.json').read_bytes())
assert seal['verdict']=='CONFIRMED' and not seal['errors']
for name,pin in seal['outputs'].items():
 raw=(B/name).read_bytes();assert H(raw)==pin['sha256'] and len(raw)==pin['bytes'],name
cache={};edges=0

def archive(pin, external=False):
 global edges
 path=Path(pin['archive']) if external else B/pin['archive']
 if path not in cache:
  z=path.read_bytes();cache[path]=(z,gzip.decompress(z))
 z,raw=cache[path];edges+=1
 assert H(z)==pin.get('archive_sha256',pin.get('compressed_sha256')) and H(raw)==pin['sha256'] and len(raw)==pin['bytes'],str(path)
 if 'archive_bytes' in pin:assert len(z)==pin['archive_bytes']
 return raw
manifests={}
for p in sorted(B.glob('input_manifest_*.json')):
 d=json.loads(p.read_bytes());manifests[p.name]=d
 for pin in d['files'].values():archive(pin)
final=manifests['input_manifest_final_001.json']
read=lambda name:cache[B/final['files'][name]['archive']][1]
MI=json.loads((B/'af5_matrix_extension/verification/inputs.json').read_bytes())
for pin in MI['files'].values():archive(pin)
for pin in MI['afrr_original_archive_edges']:archive(pin,True)
extra=json.loads((B/'af5_matrix_extension/verification/additional_source_bindings_001.json').read_bytes())
for pin in extra['files'].values():archive(pin)
for name in ['report_discrepancy_001.json','root_report_discrepancy_001.json']:
 d=json.loads((B/name).read_bytes())
 for key in ['archived_report','report_archive','report']:
  if key in d and isinstance(d[key],dict) and 'archive' in d[key]:archive(d[key])
active=dict(MI['current_source_hashes'])
for item in final['current_static_versions'].values():
 for path in item['closure_paths']:active[path]=final['files'][path]['sha256']
for path,pin in final['files'].items():
 if path=='bot_research/bots/best.py' or path.startswith(('td_game/','data/')) or path=='bot_research/bots/counters/data/early_wall_guard_001.json':active[path]=pin['sha256']
counts={};allrecords=allaccepted=0;tables={};rawvalues={};rowsbyrun={}
audit=json.loads((B/'record_audit_final_001.json').read_bytes());specs=audit['specs']
for run in ['frr2','frr4','frr5','frr6','frr7','frr8']:
 path='bot_research/runs/lead/'+run+'/results.jsonl'
 rows=[json.loads(x) for x in read(path).splitlines()];rowsbyrun[run]=rows
 assert H(Path(path).read_bytes())==final['files'][path]['sha256']
 table={};wdl=collections.Counter();accepted=records=0
 for r in rows:
  active.update(r['sources'])
  raw=read(r['log']);assert H(Path(r['log']).read_bytes())==H(raw)
  logs=[json.loads(x) for x in raw.splitlines()]
  assert len(logs)==2*(r['rounds']+1)
  assert sorted((v['round'],v['player']) for v in logs)==[(t,p) for t in range(r['rounds']+1) for p in [0,1]]
  n=sum(e['accepted'] for v in logs for e in v.get('event',[]) if e['kind']=='action')
  assert n==sum(sum(p['accepted'].values()) for p in r['players'])
  assert not any(p['n_rejected'] or p['bot_errors'] for p in r['players'])
  normalized=[]
  for v in sorted(logs,key=lambda x:(x['round'],x['player'])):
   u={k:a for k,a in v.items() if k!='match'}
   if 'snapshot' in u:u['snapshot']={k:a for k,a in u['snapshot'].items() if k!='name'}
   normalized.append(u)
  canonical=H(json.dumps(normalized,sort_keys=True,separators=(',',':')).encode())
  rawvalues[r['log']]=canonical
  for side in [0,1]:
   actor=r['spec_a' if side==0 else 'spec_b'];other=r['spec_b' if side==0 else 'spec_a']
   k=(actor,other,r['scenario'],side)
   outcome=0 if r['winner'] is None else 1 if r['winner']==side else -1
   value=(outcome,r['hp_a' if side==0 else 'hp_b'],r['hp_b' if side==0 else 'hp_a'],r['rounds'],canonical)
   assert k not in table;table[k]=value
   if side==r['candidate_side']:wdl[{1:'W',0:'D',-1:'L'}[outcome]]+=1
  accepted+=n;records+=len(logs)
 a=audit['campaigns'][run]
 assert a['complete_grid'] and not any(a[k] for k in ['duplicates','metadata_errors','missing_conditions','unexpected_conditions'])
 assert len(rows)==a['observed_rows'] and records==a['sum_records'] and accepted==a['accepted_total']
 assert {k:wdl[k] for k in ['W','D','L']}==a['wdl_of_declared_first_pair_member']
 counts[run]={'games':len(rows),'records':records,'accepted_actions':accepted,'wdl':dict(wdl)}
 tables[run]=table;allrecords+=records;allaccepted+=accepted
assert allrecords==9234 and allaccepted==2739683
assert counts['frr7']['wdl']=={'W':13,'L':11,'D':4} and counts['frr8']['wdl']=={'W':2}
assert sum(counts[r]['records'] for r in ['frr7','frr8'])==1804
assert sum(counts[r]['accepted_actions'] for r in ['frr7','frr8'])==504024
for path,h in active.items():assert H(Path(path).read_bytes())==h,path
combined={}
for run in ['frr2','frr4','frr6']:
 for key,val in tables[run].items():
  if key in combined:assert combined[key]==val
  combined[key]=val
comparisons={};sets={}
af={k[1:]:v for k,v in tables['frr7'].items() if k[0]==specs['AF5']}
for alias in ['V29','G1','V46','V48']:
 base={k[1:]:v for k,v in combined.items() if k[0]==specs[alias]}
 common=set(af)&set(base);assert len(common)==24
 eq=sum(af[k]==base[k] for k in common)
 scores=collections.Counter('better' if af[k][0]>base[k][0] else 'worse' if af[k][0]<base[k][0] else 'same' for k in common)
 assert (eq==24 if alias in ['V29','G1'] else eq==0)
 if alias in ['V46','V48']:assert scores=={'same':13,'worse':11}
 sets[alias]=common;comparisons[alias]={'common_conditions':24,'complete_canonical_equal':eq,'AF5_WDL_comparison':dict(scores)}
assert len(sets['V29']&sets['G1'])==20 and len(sets['V29']|sets['G1'])==28
for key,value in tables['frr8'].items():
 if key[0]==specs['AF5']:
  assert value[:4]==(1,795,740,50)
  assert value==tables['frr5'][(specs['G1'],*key[1:])]
# Reconstruct all measured finite-matrix entries from their archived result rows.
MC=json.loads((B/'af5_matrix_extension/verification/matrix.json').read_bytes())
M=MC['matrix'];names=MC['names'];full=MC['full_specs'];lookup={v:k for k,v in full.items()}
assert len(lookup)==len(full)
mi_paths={}
for pin in MI['files'].values():mi_paths.setdefault(pin['path'],[]).append(pin)
def mread(path):
 pins=mi_paths[path];assert len({p['sha256'] for p in pins})==1,path
 return cache[B/pins[0]['archive']][1]
mr={}
for run in ['frr1','afrr','frr3','frr5','frr8']:
 path='bot_research/runs/'+('economy/' if run=='afrr' else 'lead/')+run+'/results.jsonl'
 mr[run]=[json.loads(x) for x in mread(path).splitlines()]
 assert H(Path(path).read_bytes())==H(mread(path))
assert sum(map(len,mr.values()))==152
measured=collections.defaultdict(list)
for e in MC['source_conditions']:
 r=mr[e['run']][e['line']-1]
 for key in ['spec_a','spec_b','candidate_side','scenario','hp_a','hp_b','winner','rounds','log']:assert e[key]==r[key]
 a,b=lookup[r['spec_a']],lookup[r['spec_b']]
 assert a==e['name_a'] and b==e['name_b'] and r['scenario'] is None
 payoff=0 if r['winner'] is None else 1 if r['winner']==0 else -1
 assert payoff==e['row_player0_payoff']
 measured[(a,b)].append(payoff);measured[(b,a)].append(-payoff)
 if e['raw_log_present']:assert H(Path(r['log']).read_bytes())==H(mread(r['log']))
for i,a in enumerate(names):
 for j,b in enumerate(names):
  if i==j:assert M[i][j]==0
  else:assert len(measured[a,b])==2 and set(measured[a,b])=={M[i][j]}
  assert M[i][j]==-M[j][i]
for alias,row in MC['fortress_rows_against_original_ten'].items():
 assert row==M[4][:10]
 for j,name in enumerate(names[:10]):assert len(measured[alias,name])==2 and set(measured[alias,name])=={row[j]}
assert set(measured['AF5','V48'])=={1} and len(measured['AF5','V48'])==2
assert not measured['AF5','V46'] and not measured['V46','V48']
afrr_records=afrr_actions=0
for r in mr['afrr']:
 logs=[json.loads(x) for x in mread(r['log']).splitlines()]
 assert len(logs)==2*(r['rounds']+1)
 n=sum(e['accepted'] for v in logs for e in v.get('event',[]) if e['kind']=='action')
 assert n==sum(sum(p['accepted'].values()) for p in r['players'])
 afrr_records+=len(logs);afrr_actions+=n
assert (afrr_records,afrr_actions)==(1884,336324)
# Exact dual strictness and affine primal certificate; read PROOF.md supplies necessity.
z=[F(0)]*11
for k in [7,9,10]:z[k]=F(1,3)
dual=[sum(F(M[i][j])*z[j] for j in range(11)) for i in range(11)]
assert dual==list(map(F,[-1,'-2/3',-1,0,-1,-1,'-1/3',0,-1,0,0]))
assert {i for i,t in enumerate(dual) if t==0}=={3,7,9,10}
vertices=[]
for c in [F(0),F(1,3)]:
 x=[F(0)]*11;x[3]=F(1,3)-c;x[7]=x[10]=F(1,3);x[9]=c
 pay=[sum(x[i]*M[i][j] for i in range(11)) for j in range(11)]
 assert pay==[F(2,3)+c,F(2,3),F(2,3)+c,0,F(2,3)+c,1,F(1,3),0,1,0,0]
 vertices.append({'AS1C':str(c),'payoff':[str(t) for t in pay]})
 for alpha in [F(-1),F(1)]:
  # F's row against z is strictly negative, irrespective of mutual F entries.
  assert (-2-alpha)/3<=F(-1,3)
  s=M[4][:10]
  against_F=-sum(x[i]*s[i] for i in range(10))+x[10]*alpha
  assert against_F==(1+alpha)/3+c and against_F>=0
for old_extra in [1,3,9]:
 x=[F(0)]*10;x[6]=x[7]=F(1,3);x[old_extra]=F(1,3)
 assert sum(M[10][i]*x[i] for i in range(10))==F(1,3)+2*x[1]>0
receipt={'schema':1,'started_utc':started,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_model':'GPT-6 Astra','verdict':'CONFIRMED','sealed_files_verified':len(seal['outputs']),'archive_edges_verified':edges,'unique_archive_paths_verified':len(cache),'current_source_paths_verified':len(active),'campaigns':counts,'main_raw_records':allrecords,'main_accepted_actions':allaccepted,'comparisons':comparisons,'V29_G1_common_intersection':20,'V29_G1_common_union':28,'matrix_rows_independently_joined':152,'afrr_records':afrr_records,'afrr_accepted_actions':afrr_actions,'strict_dual':[str(v) for v in dual],'optimal_vertices':vertices,'informal_proof_review':'Necessity follows from strict dual support restriction and a>=t>=b>=a. Sufficiency is affine in AS1C weight. Fortress dual is strictly negative uniformly over alpha in [-1,1], independent of arbitrary skew mutual entries. The previous optimum has AF5 exploit 1/3+2*BEST_V9F weight.','scope':'Conditional recorded finite WDL matrix, zero self-play diagonals imposed. No unrestricted game, HP objective, timing invariance, fresh policy regeneration or new strength sample.','execution':'Root independently parsed retained bytes using standard library; no policy, Engine, replay, project checker or new game.','input_sha256':{str(B/p):H((B/p).read_bytes()) for p in ['root_review_001.py','seal_001.json','REVIEW.md','aggregate_records.py','supplementary_checks.py','record_audit_final_001.json','af5_matrix_extension/PROOF.md','af5_matrix_extension/verification/check_matrix.py','af5_matrix_extension/verification/receipt.json','af5_matrix_extension/verification/inputs.json','af5_matrix_extension/verification/matrix.json']}}
p=B/'root_review_001.json'
with p.open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'receipt':str(p),'sha256':H(p.read_bytes()),'completed_utc':receipt['completed_utc'],'verdict':receipt['verdict'],'archive_edges':edges,'campaigns':counts}))

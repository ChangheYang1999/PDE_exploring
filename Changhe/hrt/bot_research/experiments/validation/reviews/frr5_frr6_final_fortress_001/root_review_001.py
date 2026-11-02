"""Root archive and independent raw-count review; no game/project imports."""
import collections, datetime, gzip, hashlib, json
from pathlib import Path
from fractions import Fraction
B=Path('bot_research/experiments/validation/reviews/frr5_frr6_final_fortress_001')
H=lambda b:hashlib.sha256(b).hexdigest()
seal=json.loads((B/'seal_001.json').read_bytes()); assert seal['verdict']=='CONFIRMED' and not seal['errors']
for name,pin in seal['outputs'].items():
 raw=(B/name).read_bytes(); assert len(raw)==pin['bytes'] and H(raw)==pin['sha256'],name
cache={};edges=0;manifests={}
for phase in ['initial','supporting','final']:
 m=json.loads((B/f'input_manifest_{phase}.json').read_bytes());manifests[phase]=m
 for source,pin in m['files'].items():
  path=pin['archive']
  if path not in cache:
   packed=(B/path).read_bytes();cache[path]=(packed,gzip.decompress(packed))
  packed,raw=cache[path]
  assert H(packed)==pin['archive_sha256'] and len(packed)==pin['archive_bytes'],source
  assert H(raw)==pin['sha256'] and len(raw)==pin['bytes'],source
  edges+=1
assert edges==seal['archive_edge_count']==658
assert len(cache)==seal['unique_archives']==191
m=manifests['final']
def read(name):return cache[m['files'][name]['archive']][1]
def key(r):
 s=r['candidate_side'];return (r['spec_b' if s==0 else 'spec_a'],r['scenario'],s)
counts={};tables={};accepted=records_count=0
for run in ['frr3','frr4','frr5','frr6']:
 rows=[json.loads(x) for x in read('bot_research/runs/lead/'+run+'/results.jsonl').splitlines()]
 table={};wdl=collections.Counter();naccepted=nrecords=nrounds=0
 for row in rows:
  k=key(row);assert k not in table
  side=row['candidate_side']; outcome='D' if row['winner'] is None else 'W' if row['winner']==side else 'L'
  logs=[json.loads(x) for x in read(row['log']).splitlines()]
  assert len(logs)==2*(1+row['rounds'])
  rawaccepted=sum(e['accepted'] for rec in logs for e in rec.get('event',[]) if e['kind']=='action')
  assert rawaccepted==sum(sum(p['accepted'].values()) for p in row['players'])
  assert not any(p['n_rejected'] or p['bot_errors'] for p in row['players'])
  normalized=[]
  for rec in sorted(logs,key=lambda x:(x['round'],x['player'])):
   value={k:v for k,v in rec.items() if k!='match'}
   if 'snapshot' in value:value['snapshot']={k:v for k,v in value['snapshot'].items() if k!='name'}
   normalized.append(value)
  canonical=H(json.dumps(normalized,sort_keys=True,separators=(',',':')).encode())
  table[k]=(outcome,row['hp_a' if side==0 else 'hp_b'],row['hp_b' if side==0 else 'hp_a'],row['rounds'],canonical)
  wdl[outcome]+=1;naccepted+=rawaccepted;nrecords+=len(logs);nrounds+=row['rounds']
 counts[run]={'conditions':len(rows),'wdl':{k:wdl[k] for k in ['W','D','L']},'raw_records':nrecords,'accepted_actions':naccepted,'rounds':nrounds}
 tables[run]=table;accepted+=naccepted;records_count+=nrecords
assert tables['frr3']==tables['frr5'] and tables['frr4']==tables['frr6']
assert records_count==6272 and accepted==2652072
assert counts['frr5']['wdl']=={'W':4,'D':4,'L':12} and counts['frr6']['wdl']=={'W':22,'D':2,'L':0}
audit=json.loads((B/'record_audit_final.json').read_bytes())
for run,c in counts.items():
 a=audit['campaigns'][run]
 assert c['conditions']==a['observed_rows'] and c['wdl']==a['wdl'] and c['raw_records']==a['sum_records'] and c['accepted_actions']==a['accepted_total']
cert=json.loads((B/'finite_matrix_extension/verification/row_certificate.json').read_bytes())['exact_certificate']
M=cert['base_matrix'];z=[Fraction(v) for v in cert['z']]
assert sum(z)==1 and all(t>=0 for t in z)
assert all(M[i][j]==-M[j][i] for i in range(10) for j in range(10))
assert [sum(Fraction(M[i][j])*z[j] for j in range(10)) for i in range(10)]==[Fraction(v) for v in cert['base_dual']]
assert all(sum(Fraction(a['row'][j])*z[j] for j in range(10))==-1 and a['row']==M[4] for a in cert['added_rows'].values())
r={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_model':'GPT-6 Astra','verdict':'CONFIRMED','archive_edges_verified':edges,'unique_archives_verified':len(cache),'sealed_files_verified':len(seal['outputs']),'independently_recounted_campaigns':counts,'matched_complete_canonical_histories':44,'raw_records':records_count,'accepted_actions':accepted,'method':'Root read the complete two inspector sources, review and standalone proof, verified archived inputs/seal and independently parsed all88 raw logs, counted actions and compared canonical histories. Exact Fraction dual arithmetic agrees. No Engine, policy or project-checker execution.','proof_scope':'Conditional finite skew-symmetric payoff matrix with imposed zero diagonals and empirical rows. Arbitrary unplayed mutual q is permitted; no unrestricted-game or load-invariance claim.','input_sha256':{str(B/name):H((B/name).read_bytes()) for name in ['root_review_001.py','seal_001.json','REVIEW.md','aggregate_records.py','supplementary_checks.py','finite_matrix_extension/PROOF.md','finite_matrix_extension/verification/row_certificate.json','record_audit_final.json','supplementary_checks_final.json','input_manifest_initial.json','input_manifest_supporting.json','input_manifest_final.json']}}
p=B/'root_review_001.json'
with p.open('x') as f:json.dump(r,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'receipt':str(p),'sha256':H(p.read_bytes()),'created_utc':r['created_utc'],'counts':counts,'verdict':r['verdict']}))

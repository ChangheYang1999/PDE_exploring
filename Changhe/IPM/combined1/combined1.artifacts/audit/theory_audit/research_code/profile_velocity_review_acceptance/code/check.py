from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,time
B=Path(__file__).resolve().parents[1];start=time.monotonic()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text())
assert sha(B/'PROOF.md')==m['proof_sha256']
for rel,d in m['inputs'].items():assert sha(B/rel)==d,rel
peer=json.loads((B/'source/peer_result.json').read_text())
orig=json.loads((B/'source/original_result.json').read_text())
assert len(peer['A'])==15 and all(v is True for v in peer['A'].values())
assert peer['D']['t4_375_review_results_sha256']==sha(B/'source/peer_375_result.json')
checks=16;rows=[]
for row in orig['rows']:
 name=row['candidate'];p=peer['B'][name]
 assert len(p['matches_result_json'])==7 and all(v is True for v in p['matches_result_json'].values());checks+=7
 assert Q(p['l1'])==Q(row['trace_l1_exact']);checks+=1
 assert Q(p['l1'])<Q(583,1000)**2;checks+=1
 assert Q(row['det_S'])>0;checks+=1
 rows.append({'candidate':name,'all_peer_exact_checks':True,'l1_matches_original':True,'l1_below_583_1000_squared':True})
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'rows':rows,'foreign_code_executed':False,'verdict':'CONFIRMED original T4-402; finite-radius and full CI closure remain OPEN'}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))

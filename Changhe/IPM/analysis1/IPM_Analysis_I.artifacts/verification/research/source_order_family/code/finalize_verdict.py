"""Freeze topic92 after actual whole-bundle reviews and independent audit."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_order_family';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text())
assert c['status']=='PASS_SOURCE_ORDER_FAMILY_CONSTANTS' and a['status']=='PASS_FRESH_SOURCE_ORDER_AUDIT' and a['checks']==92
assert c['counts']['dependency_file_pins']==387 and c['counts']['directed_interval_inequalities']==78
assert sha(D/'PROOF.md')==json.loads((E/'proof_first.json').read_text())['proof_sha256']
for z in [c,a]:
 for p,h in z['files'].items():assert sha(B/p)==h,p
row=[v for v in c['rows'] if F(v['s'])==F(153,50)][0]
assert F(row['K_upper'])==F(500000000,1593611657)>F('0.31375')
assert F(row['K_upper'])<F(row['K_decimal_ceiling'])==F('0.313753')
reviews={};files={}
for kind in ['proof','closure']:
 tag='source_order_family_'+kind;m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'] and ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 assert ('accept the analytic scope' in ans.lower()) if kind=='proof' else ('**ACCEPT**' in ans and 'inward and rejected' in ans)
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
for p in c['files']:files[p]=sha(B/p)
v={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_SOURCE_ORDER_FAMILY','s_interval':c['interval'],'at_3_06':{k:v for k,v in row.items() if k!='engines'},'whole_interval_K1_ceiling':'3181/10000','whole_interval_d_lower':'6141/2000','counts':c['counts']|{'fresh_audit_checks':a['checks']},'reviews':reviews,'scope':'Variable-order theorem and actual local coefficient smallness on previously verified normalized trial. Exact source hypotheses and derivative data imported from frozen independently audited dependencies. K1 is local forcing coefficient, not auxiliary inverse norm. Mandatory addenda clarify norm and distribution scope.','open':['Unevaluated R_s in auxiliary inverse norm','Physical rank-one denominator','Outer matching, global IPM inverse, residual norm and contraction','Every decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'utc':v['utc'],'status':v['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))

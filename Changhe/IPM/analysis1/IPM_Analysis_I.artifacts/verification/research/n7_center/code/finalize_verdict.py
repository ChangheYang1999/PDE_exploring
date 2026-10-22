"""Bind exact data, two independent methods, remote moment, and whole Opus reviews."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import sys,json,hashlib
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n7_center';E=D/'evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();files={}
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());r=json.loads((E/'remote_checks.json').read_text())
assert c['status']=='PASS_N7_EXACT_CENTER' and a['status']=='PASS_INDEPENDENT_NPY_LAURENT_AUDIT' and r['status']=='PASS_N7_NONZERO_EXTERIOR_CHANGE'
assert c['counts']=={'mask_zeros':1026,'unchanged_complement':794,'changed_coefficients':1026,'symbolic_identities':56,'join_entries':49,'primary_engine_enclosures':12}
assert a['counts']=={'exact_binary64_values_compared':3648,'full_npz_hashes':2,'mask_zeros':1026,'unchanged_complement':794,'density_Laurent_frequencies':522,'residual_Laurent_frequencies':524,'full_ball_contains':6}
assert r['counts']=={'unchanged_NPY_members':16,'independent_exact_moment_equalities':4,'symbolic_identities':10} and Q(r['exact']['S'])<0
for obj in [c,a,r]:
 for p,h in obj['files'].items():assert sha(B/p)==h,p;files[p]=h
first=json.loads((E/'proof_first.json').read_text());assert first['code_files']==[] and first['proof_sha256']==sha(D/'PROOF.md')
af=json.loads((E/'addendum_first.json').read_text());assert not af['additional_code_exists'] and af['addendum_sha256']==sha(D/'ADDENDUM.md')
run=json.loads((E/'local_run.json').read_text());assert run['resumed_worker'] and run['commands'][0]['returncode']==0
run=json.loads((E/'retry_run.json').read_text());assert run['resumed_worker'] and all(x['returncode']==0 for x in run['commands'])
run=json.loads((E/'remote_run.json').read_text());assert run['resumed_worker'] and run['returncode']==0
inputs=json.loads((E/'exact_inputs.json').read_text())
for item in inputs['data'].values():
 with Path(item['path']).open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==item['sha256']
for p,h in inputs['source_files'].items():assert sha(p)==h
reviews={};R=B/'notes/reviews'
for tag in ['n7_center_proof','n7_center_corrected','n7_center_closure']:
 m=json.loads((R/(tag+'_metadata.json')).read_text());req=(R/(tag+'_request.txt')).read_text();raw=json.loads((R/(tag+'_response.json')).read_text());ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and len(ans)>200
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 def content(f):
  if tag=='n7_center_proof' and f=='research/n7_center/PROOF.md':return (E/'rejected_proof_v1.md').read_text()
  return (B/f).read_text()
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+content(f) for f in m['files'])
 if tag=='n7_center_proof':assert 'NOT ACCEPTED' in ans
 if tag=='n7_center_corrected':assert 'ACCEPT_ANALYTIC_SCOPE' in ans
 if tag=='n7_center_closure':assert 'ACCEPT_N7_CENTER_SCOPE' in ans[:200] and ('retract' in ans.lower() or 'withdraw' in ans.lower())
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_N7_CENTER_AND_NONZERO_REMOTE_CHANGE','confirmed':['All1026forbidden D terms removed exactly;794complementcoefficients unchanged; all3648selectedbinary64values independently parsed to exactrationals.','Local factor C9 not C10; density C12 not C13; firstnonpolynomialdensityhomogeneity13. No claim across joins.','Under canonical exactnormalization, residual C12 not C13, firstnonpolynomialhomogeneity13, highestfrequency523 coefficientpositive about1.041857526e9.','Scaled remaining D5 maximum<6.9e-11. This is not a physical r13 residual-coefficient bound.','C6correction matrix hasdet24883200; correction finiteness/uniqueness proved, no claim storedfloatEi exactlyjoins.','16otherNPYmembers unchanged. Exact highmodeGreenmoment S<0 proves nonzero canonicalexteriorvelocitychange atfrequency522, including aftermode0normalization.','Homogeneitythreshold13>(6.45+3.07-1),margin4.48, is only the local powerinequality.'],'arithmetic':{'primary':c['counts'],'independent':a['counts'],'remote':r['counts']},'data_inputs':{tag:{k:v[k] for k in ['path','sha256']} for tag,v in inputs['data'].items()},'reviews':reviews,'rejected_history':'Initial inconsistent stream convention archived and corrected beforecode. FirstindependentNPYaudit rejected Fortranlayout; exactstridereorderingrepairretainsallinputsandendpointrequirements. Correctedreviewincidentalnegativecoefficientremark retracted inclosure.','open':['ActualnormalizedN7S1/middleresidualcertificate independent fullrerun','N7innerresidualnorm and highorderPdisc bounds','Globalclassmembership/inverse/rankonedenominator/nonlinearclosure and everydecisiveendpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))

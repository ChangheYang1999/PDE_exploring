"""Publish the radial defect criterion and illustrative exact-rational audit."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/radial_defect';E=D/'evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();files={}
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text())
assert c['status']=='PASS_RADIAL_DEFECT_IDENTITIES_AND_MOMENTS' and c['counts']=={'symbolic_identities':20,'parameter_rows':20,'moment_cases':100,'primary_engine_enclosures':240,'primary_inequalities':400}
assert a['status']=='PASS_EXACT_RATIONAL_RADIAL_MOMENTS' and a['counts']=={'moment_cases':100,'geometric_tail_checks':98,'full_enclosure_contains':120}
first=json.loads((E/'proof_first.json').read_text());assert first['code_files']==[] and first['proof_sha256']==sha(D/'PROOF.md')
for result in [c,a]:
 for p,h in result['files'].items():assert sha(B/p)==h,p;files[p]=h
run=json.loads((E/'local_run.json').read_text());assert run['resumed_worker'] and len(run['commands'])==2 and all(x['returncode']==0 for x in run['commands'])
reviews={};R=B/'notes/reviews'
for tag in ['radial_defect_proof','radial_defect_closure']:
 m=json.loads((R/(tag+'_metadata.json')).read_text());req=(R/(tag+'_request.txt')).read_text();raw=json.loads((R/(tag+'_response.json')).read_text());ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and len(ans)>200
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 assert 'ACCEPT_RADIAL_DEFECT_CRITERION' in ans[:200]
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_RADIAL_DEFECT_CRITERION_AND_ILLUSTRATIVE_MOMENTS','confirmed':['Canonical P/R radial ODEs diagonalize to qplus prime=(l-2)qplus-f and qminus prime=-(l+2)qminus+f.','Forcing exponent in P/R ODE is alpha+2; alpha+4 belongs to A/B equations.','Variation of constants gives the proved defect bound with retained anchor error and positive monotone moments.','Exact rational signed series with geometric tail independently lies inside the hull of primary Arb512/iv180 moment enclosures in all illustrative cases.'],'scope':'Abstract criterion and illustrative arithmetic only. Hull containment is a consistency audit, not containment inside each primary engine separately. Actual finite-annulus flow remains OPEN.','arithmetic':c['counts'],'fresh_audit':a['counts'],'reviews':reviews,'open':['Actual Green anchor enclosures and all forcing coefficients','Actual candidate P/R polynomial defect bounds in every cell and mode','All angular coefficients and full field inequalities','Global inverse and every decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))

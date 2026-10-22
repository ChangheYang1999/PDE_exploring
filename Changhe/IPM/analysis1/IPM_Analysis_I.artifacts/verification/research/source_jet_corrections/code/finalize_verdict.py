"""Bind local source-jet theorem, previous scalar dependency and full reviews."""
import sys,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_jet_corrections';E=D/'evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());run=json.loads((E/'local_run.json').read_text())
assert c['status']=='PASS_NEW_JET_AND_FACE_SCALARS' and a['status']=='PASS_FRESH_JET_SCALARS'
assert a['checks_sha256']==sha(E/'checks.json') and a['self_sha256']==sha(D/'code/audit_output.py')
assert a['source_sha256']==sha(B/'research/modal_source/evidence/source_result.json')
for p,h in c['files'].items():assert sha(B/p)==h,p
assert len(c['symbolic_identities'])==14 and c['counts']=={'strict_exact_consequences':6,'arb512_exact_corner_contains':8,'iv180_exact_corner_contains':8}
assert a['counts']=={'exact_extrema_equal':8,'fresh_corner_contains':24,'fresh_alternative_root_contains':4}
assert run['resumed_worker'] and len(run['commands'])==2 and all(x['returncode']==0 for x in run['commands'])
assert sha(D/'PROOF.md')==json.loads((E/'proof_repair.json').read_text())['proof_sha256']
assert sha(D/'ADDENDUM.md')==json.loads((E/'addendum_before_code.json').read_text())['sha256']
files={};reviews={}
for tag in ['source_jet_proof','source_jet_closure']:
 root=B/'notes/reviews';m=json.loads((root/(tag+'_metadata.json')).read_text());request=(root/(tag+'_request.txt')).read_text();ans=(root/(tag+'_response.md')).read_text();raw=json.loads((root/(tag+'_response.json')).read_text())
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and len(ans)>200
 assert hashlib.sha256(request.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n'
 mark='\n\nFILE '+m['files'][0]+'\n';assert request.count(mark)==1
 rebuilt=request.split(mark,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']);assert rebuilt==request,tag
 if tag=='source_jet_closure':assert ans.startswith('# FINAL ANSWER: ACCEPT_STATED_LOCAL_SCOPE')
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=root/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
files.update(c['files']);files['PROMPT.md']=sha(B/'PROMPT.md')
old=json.loads((B/'research/modal_source/evidence/output_audit.json').read_text())
p=B/'research/modal_source/code/audit_output.py';assert sha(p)==old['audit_source_sha256'];files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_LOCAL_SOURCE_JET_AND_NORMALIZED_OBSTRUCTION','confirmed':['Exact stationary-axis first-derivative identity at the unique certified trial source P.','No exact normalized solution lies in the four specified density/velocity jet ball of radius2.2e-8 about the trial. This is not an X3 uncertainty neighbourhood.','Exact coefficient C>30.0229 and C<30.0230; smaller printed coefficient rejected. D>6.70e-7 and positive margin>9.69e-9 at radius2.2e-8.','Normalized face coefficient uses RAW strain sigma and equals2sigma(2G1-xG1prime)/3. Trial factor2g-xstar*gprime>57.1.','For b>2 remote parity bumps have constant L2(|y|^-2b) norm but normalized velocity coupling grows like R^(b-2) on a fixed interior patch where this factor is nonzero.','Explicit local pure-transport C1 forcing and C1 solution with non-Dini derivative modulus; Dini is not necessary in that model.'],'arithmetic':{'symbolic_identities':14,'exact_strict_consequences':6,'primary_Arb512_iv180_corner_contains':16,'fresh_fmpq_extrema_equal':8,'fresh_Arb1536_corner_contains':24,'fresh_alternative_root_contains':4},'dependency':'The previous independently integrated all261-mode canonical source certificate, exact root bisection and import/output audits remain explicit dependencies. This note recomputes the new expressions, not the integration.','scope_clarification':'The local exclusion is tested at the fixed trial point P. A perturbed exact solution may have a different source location; the identity needs no source at P for the perturbed field. The review final phrase no varying-source result is read only as no source-continuation theorem.','reviews':reviews,'open':['Certified placement of X3 or a meaningful branch uncertainty neighbourhood in this topology','A full canonical velocity realization and global inverse on the proposed weighted completion','All global matching, nonlinear closing inequalities, and decisive IPM endpoints'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))

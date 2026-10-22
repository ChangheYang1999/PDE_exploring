"""Publish a superseding canonical sign correction, preserving original audit files."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_strain_sign';E=D/'evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();files={}
c=json.loads((E/'checks.json').read_text());assert c['status']=='PASS_CANONICAL_SIGN_CORRECTION' and c['counts']=={'symbolic_identities':18,'independent_exact_boundary_checks':3,'distinct_rankone_denominators':2}
first=json.loads((E/'proof_first.json').read_text());assert first['code_files']==[] and first['proof_sha256']==sha(D/'PROOF.md')
for p,h in c['files'].items():assert sha(B/p)==h,p;files[p]=h
for topic in ['source_local_estimate','source_semigroup']:
 p=B/'research'/topic/'evidence/verdict.json';dep=json.loads(p.read_text());files[str(p.relative_to(B))]=sha(p)
 for f,h in dep['files'].items():assert sha(B/f)==h,f;files[f]=h
reviews={};R=B/'notes/reviews'
for tag in ['canonical_strain_sign','canonical_strain_closure']:
 m=json.loads((R/(tag+'_metadata.json')).read_text());req=(R/(tag+'_request.txt')).read_text();raw=json.loads((R/(tag+'_response.json')).read_text());ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and len(ans)>200
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 assert 'ACCEPT_CANONICAL_CORRECTION' in ans[:200]
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
run=B/'research/n7_center/evidence/retry_run.json';rr=json.loads(run.read_text());assert rr['resumed_worker'] and any(x['file']=='research/canonical_strain_sign/code/check_signs.py' and x['returncode']==0 for x in rr['commands']);files[str(run.relative_to(B))]=sha(run)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CANONICAL_SIGN_CORRECTION','refuted':['Topics77/78identifystrainofDelta psi_minus=partial_x hwithcanonicalstrainof-Delta psi=partial_x h. Theyare negatives.','Old-functionalplusdenominator1+sigma_minus[Aop^-1ell]is notthecanonicalphysicaldenominator.'],'confirmed':['Canonicalrawstrain=-h_y(0)/4-PV(K_s*h)(0),K_s=y(3x²-y²)/(pi r6).','Velocitysymbol/kernelsin77/78unchanged; K1-K4 transferwithidenticalconstantsbecauseeverystrainestimateisabsolute.','Aop,maximaldomain,generator,semigroup,inverseandnormboundin78unchanged.','Canonicalrankonedenominator1+sigma[Aop^-1ell]=1-sigma_minus[Aop^-1ell],withellinHs;algebraicinverse/nullvectorcriterionandnormboundhold.'],'scope':'Thiscorrection supersedesonlythecanonicalstrainidentification/signandthephysicalold-functionaldenominatorin77/78. Originalfinalfilespreserved. Noactualnonvanishingcertificateexisted.','arithmetic':c['counts'],'reviews':reviews,'open':['ActualcoefficientboundE<kappa','Actualcanonicalrankonedenominatornonzero','Globalinverse/residual/nonlinearclosure andeverydecisiveendpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))

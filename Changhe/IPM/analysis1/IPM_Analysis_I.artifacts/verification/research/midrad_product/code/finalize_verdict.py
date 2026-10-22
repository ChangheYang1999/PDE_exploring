"""Bind the explicitly conditional theorem to its completed evidence."""
import json,hashlib,sys
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/midrad_product/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=json.loads((E/'checks.json').read_text());audit=json.loads((E/'output_audit.json').read_text());run=json.loads((E/'local_run.json').read_text())
assert checks['status']==audit['status']=='PASS'
assert checks['code_sha256']==sha(B/'research/midrad_product/code/check_bounds.py') and checks['proof_sha256']==sha(B/'research/midrad_product/PROOF.md')
assert audit['code_sha256']==sha(B/'research/midrad_product/code/audit_output.py') and audit['proof_sha256']==checks['proof_sha256'] and audit['input_sha256']==sha(E/'checks.json')
assert audit['containments']==136 and audit['selected_exact_identities']==68 and checks['positive_exact_checks']==4095
assert run['resumed_worker'] and len(run['commands'])==2 and all(x['returncode']==0 for x in run['commands'])
files={};reviews={}
for p,h in checks['source_pins'].items():assert sha(B/p)==h;files[p]=h
for tag in ['midrad_product_proof','midrad_product_closure']:
 m=json.loads((B/f'notes/reviews/{tag}_metadata.json').read_text());req=(B/f'notes/reviews/{tag}_request.txt').read_text();ans=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']=='claude-opus-5-5' and m['stop_reason']=='end_turn' and len(ans)>200
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 for f in m['files']:
  part=req.split('FILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]
  assert part==(B/f).read_text(),(tag,f)
 if tag.endswith('closure'):assert 'ACCEPT' in ans
 reviews[tag]={'actual_model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suffix in ['metadata.json','request.txt','response.md','response.json']:
  p=f'notes/reviews/{tag}_{suffix}';files[p]=sha(B/p)
for p in [B/'research/midrad_product/PROOF.md',*sorted((B/'research/midrad_product/code').glob('*.py')),*sorted(E.glob('*.json')),*sorted(E.glob('*.log'))]:
 if p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_ARITHMETIC_THEOREM','matrix_K':[2,1024],'sum_weighted_K':[1,1024],'required_hypotheses':'Finite binary64 RN with gradual underflow and no overflow; each of FIVE matrix products is a K-product addition tree with optional FMA, path length at mostK; sum reductions are addition trees. Actual BLAS and numpy implementation model not proved.','confirmed':['Composed matrix radius including all auxiliary rounding and subnormal contributions.','MR.sum formula.','TMArr.sup and polysup nonnegative weighted-sum formula with already valid upper-bound inputs.'],'evidence':{'exact_positive_inequalities':4095,'selected_K':17,'fresh1536_containments':136,'selected_exact_identities':68},'reviews':reviews,'review_limit':'Text reviews did not execute code or check hashes. Local finalizer checks bundles. Incidental reviewer claim that all flow products haveK13 is not used: angular mode products haveK261. No source-range extrapolation.','open':['Actual library evaluation tree and runtime provenance','Other source operations and analytic flow construction','Independent complete finite-flow numerical reproduction','Every PDE existence/exclusion endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pin_count':len(files),'verdict_sha256':sha(E/'verdict.json')}))

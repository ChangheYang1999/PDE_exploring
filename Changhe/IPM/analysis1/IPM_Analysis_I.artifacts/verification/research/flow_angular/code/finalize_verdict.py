"""Bind the finite angular claims to checked source and output records."""
import sys,json,hashlib,re
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_angular/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());r=json.loads((E/'runtime_remainders.json').read_text());run=json.loads((E/'audit_retry_run.json').read_text());first=json.loads((E/'first_local_run.json').read_text())
assert c['status']==a['status']==r['status']=='PASS'
assert c['code_sha256']==sha(B/'research/flow_angular/code/check_angular.py') and c['proof_sha256']==sha(B/'research/flow_angular/PROOF.md')
assert a['code_sha256']==sha(B/'research/flow_angular/code/audit_output.py') and a['proof_sha256']==c['proof_sha256'] and a['input_sha256']==sha(E/'checks.json')
assert r['source_code_sha256']==sha(B/'research/flow_angular/code/runtime_remainder_check.py')
assert c['arrays_sha256']==a['arrays_sha256']==r['arrays_sha256']==sha(E/'finite_arrays.npz')
assert c['nodes']==a['geometry_nodes_reconstructed']==51000 and c['geometry_containments']==306000
assert c['coefficient_containments']==2*a['coefficient_containments']==1038258 and c['selected_centers']==221 and c['exact_remainder_checks']==a['exact_remainder_checks']==r['finite_values']==4176
assert r['bitwise_reproduction'] and r['rounding_mode_before']==r['rounding_mode_after']==0
assert first['commands'][0]['name']=='check_angular' and first['commands'][0]['returncode']==0
assert run['resumed_worker'] and len(run['commands'])==1 and run['commands'][0]['returncode']==0
files={}
for p,h in c['source_pins'].items():assert sha(B/p)==h;files[p]=h
# Recreate, without executing the source, every context-search line used in closure.
pat=re.compile(r'ctx|workprec|extraprec|setattr|\beval\s*\(|\bexec\s*\(')
text=(E/'complete_context_search.txt').read_text()
for name in ['cert_flow.py','cert_resid.py','cert_resid_regions.py','midrad.py']:
 p=B/'research/flow_certificate/evidence/source'/name;h=sha(p);assert name+' SHA256 '+h in text;files[str(p.relative_to(B))]=h
 for i,line in enumerate(p.read_text().splitlines(),1):
  if pat.search(line):assert f'{i}: {line}\n' in text
reviews={}
for tag in ['flow_angular_proof','flow_angular_closure','flow_angular_replica','flow_angular_replica2','flow_angular_replica3']:
 meta=json.loads((B/f'notes/reviews/{tag}_metadata.json').read_text());request=(B/f'notes/reviews/{tag}_request.txt').read_text();answer=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert meta['actual_response_model']=='claude-opus-5-5' and meta['stop_reason']=='end_turn' and len(answer)>200
 assert hashlib.sha256(request.encode()).hexdigest()==meta['input_sha256']
 marker='\n\nFILE '+meta['files'][0]+'\n'
 assert request.count(marker)==1,tag
 preamble=request.split(marker,1)[0]
 rebuilt=preamble+'\n\n'+'\n\n'.join('FILE '+p+'\n'+(B/p).read_text() for p in meta['files'])
 assert request==rebuilt,tag
 if tag=='flow_angular_replica3':assert answer.startswith('# FINAL ANSWER: ACCEPT')
 reviews[tag]={'actual_model':meta['actual_response_model'],'stop_reason':meta['stop_reason'],'end_utc':meta['end_utc']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=B/f'notes/reviews/{tag}_{suffix}';files[str(p.relative_to(B))]=sha(p)
for p in [B/'research/flow_angular/PROOF.md',B/'research/flow_angular/ADDENDUM.md',*sorted((B/'research/flow_angular/code').glob('*.py')),*sorted(E.iterdir())]:
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FINITE_ANGULAR_RESULT','confirmed':['Exact trigonometric identities, third-derivative majorants and drift velocity formulas, including continuous axis extensions.','Primary Arb512 and iv180 enclose every replicated Arb128 tree endpoint and half-width for51000 possible nodes; keys have no collisions. Fresh auditor checks node/index coverage, keys and8 widths.','All4176 finite remainder values satisfy exact rational inequalities and reproduce bitwise in a separately recorded verifier runtime.','Only221 actual source center calls:200 base centers plus21 specified refined centers. All519129 saved boxes independently checked by Arb512,iv180,and fresh Arb1536 complex recurrence.'],'source_model':'Standalone pinned source at ctx.prec128, ntheta200,maxdepth7,261 modes, trusted imported interval/numerical libraries and no external context mutation. Node/remainder expressions are replicated; key,factors,up,succ are direct source calls. No historical execution provenance claim.','conversion_theorem':'Conditional nearest binary64 finite conversion and gradual-underflow arithmetic model; reference python-flint0.9.0 source supports it. Independent finite comparisons do not infer binary provenance from source download.','evidence_counts':{'nodes':51000,'primary_geometry_containments':306000,'coefficient_boxes':519129,'primary_coefficient_containments':1038258,'fresh_coefficient_containments':519129,'exact_remainder_inequalities':4176},'reviews':reviews,'failures_preserved':['First fresh audit terminated for repeated NPZ decompression.','Second fresh audit failed an initialization typo introduced in the performance repair.','Third fresh audit completed and resumed the background worker.','Source excerpt omissions raised by Opus were supplied and accepted in the final follow-up.'],'review_limit':'Text reviews do not execute hashes or code. Local finalizer verifies current bundles. The broad reviewer phrase no aliasing is possible from a text search is not a general theorem used here; the concrete four files were inspected.','open':['Other50779 potential center coefficient evaluations','Radial Taylor models and full flow aggregates','Actual BLAS paths and historical numerics provenance','Full linear inverse, nonlinear closing inequality, and every PDE endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'verdict_sha256':sha(E/'verdict.json')}))

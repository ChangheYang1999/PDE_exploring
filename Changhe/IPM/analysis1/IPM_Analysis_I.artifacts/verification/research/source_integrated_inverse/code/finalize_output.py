"""Final current-file and complete actual Opus5.5 gates for topic97."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from functools import lru_cache
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_integrated_inverse';E=D/'evidence';R=B/'notes/reviews';files={};pins=0
@lru_cache(None)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
objects={}
for name,status in [('checks.json','PASS_INTEGRATED_CUTOFF_AUXILIARY_INVERSE'),('output_audit.json','PASS_THIRD_EXACT_QUADRATURE_AND_FRESH_OUTPUT_AUDIT'),('closure_guard.json','PASS_STRICT_FINITE_NUMERIC_LINKAGE_AND_REQUESTED_SCALES'),('requested_scales.json','PASS_EXACT_OUTWARD_REQUESTED_SCALE_TABLE')]:
 v=json.loads((E/name).read_text());objects[name]=v;assert v['status']==status
 for f,h in v['files'].items():assert sha(str(B/f))==h,f;files[f]=h;pins+=1
c=objects['checks.json'];a=objects['output_audit.json'];g=objects['closure_guard.json'];t=objects['requested_scales.json']
assert sha(str(D/'PROOF.md'))==json.loads((E/'proof_first.json').read_text())['proof_sha256']
assert c['counts']['two_method_exact_integrals']==60 and c['counts']['exact_full_tensor_polynomial_equalities']==20
assert a['counts']['third_exact_piece_integrals']==60 and a['counts']['exact_quadrature_moment_checks']==19
assert g['counts']['nonfinite_fault_rejections']==6 and g['counts']['positive_finite_exported_boxes']==4880
assert g['counts']['arb_fresh_scalar_containments']==g['counts']['iv_fresh_scalar_containments']==2440
assert g['counts']['explicit_low_constant_links']==5 and g['counts']['explicit_source_box_links']==6
for f,h in json.loads((B/'research/n8_coefficient_closure/evidence/verdict.json').read_text())['files'].items():assert sha(str(B/f))==h;pins+=1
lookup={(x['s'],x['ell']):x for x in t['rows']};seen=set();tablechecks=0
for line in (D/'REQUESTED_SCALES.md').read_text().splitlines():
 if not line.startswith('| 3.'):continue
 cells=[x.strip() for x in line.split('|')[1:-1]];assert len(cells)==5
 key=(str(F(cells[0])),str(F(cells[1])));assert key in lookup and key not in seen;seen.add(key)
 for name,word in zip(('R','N_inverse','H_inverse'),cells[2:]):assert F(word)==F(lookup[key]['ceilings'][name]['strict_ceiling_exact']);tablechecks+=1
assert len(seen)==10 and tablechecks==30
for s,cap in [('61/20','608'),('153/50','554'),('31/10','473')]:assert F(c['best_of_81_scales'][s]['N_inverse']['upper_exact'])<F(cap)
assert F(c['best_of_81_scales']['uniform']['N_inverse']['upper_exact'])<922
reviews={}
for kind in ('proof','closure','final'):
 tag='source_integrated_inverse_'+kind;m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn' and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 assert 'accept' in ans.lower()
 reviews[tag]={k:m[k] for k in ('start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256')}
 for suffix in ('request.txt','metadata.json','response.json','response.md'):
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(str(p))
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(str(p))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_INTEGRATED_CUTOFF_DILATED_AUXILIARY_INVERSE','dependency_pin_comparisons':pins,'printed_table_exact_comparisons':tablechecks,'scope':'Same actual modal_v2 and compact C4 auxiliary operator of95. Exact radial tensor integrals, imported derivative bounds and96dilation. Maximal-domain inverse for each fixed3.05<=s<=3.1. Read PROOF,ADDENDUM,AUDIT_METHOD,CLOSURE_NOTES,REVIEW_ARITHMETIC,PUBLICATION,REQUESTED_SCALES together.','N500_named_strict_ceilings':{'3.05':'608','3.06':'554','3.1':'473'},'N500_uniform_strict_ceiling':'922','Hs_named_strict_ceilings':{'3.06_at_ell3/1000':'5.743e10','3.1_at_ell11/4000':'6.968e10'},'Hs_uniform_strict_ceiling_at_ell3/1000':'1.223e11','producing_counts':c['counts'],'audit_counts':a['counts'],'strict_closure_counts':g['counts'],'reviews':reviews,'open':['Physical rank-one denominator','Outer matching and global IPM inverse','Certified localized forcing in these norms','Nonlinear closing inequalities','Any decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(files),'sha256':sha(str(E/'verdict.json'))},indent=2))

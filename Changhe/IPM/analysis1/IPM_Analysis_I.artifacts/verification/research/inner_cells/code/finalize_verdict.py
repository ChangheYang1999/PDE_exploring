"""Bind the complete inner certificate to source, runtime, and final review."""
import sys, os, json, hashlib, argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
B=Path(__file__).resolve().parents[3]; E=B/'research/inner_cells/evidence'
assert sys.flags.optimize==0 and os.environ.get('PYTHONOPTIMIZE') is None

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
 def bad(x): raise ValueError(('nonfinite JSON',x))
 return json.loads(Path(p).read_bytes(),parse_constant=bad)
def strictdecimal(q,places):
 q=F(q); assert q>=0; den=10**places; n=q.numerator*den//q.denominator+1
 assert F(n,den)>q
 s=str(n).zfill(places+1); return s[:-places]+'.'+s[-places:]
def run(tag,review_tag,preview):
 assert tag=='full_q16'
 paths={name:E/(tag+'_'+name) for name in ['manifest.json','summary.json','audit.json','cells.jsonl','tail.json']}
 m,s,a,t=[load(paths[name]) for name in ['manifest.json','summary.json','audit.json','tail.json']]
 assert m['status']=='PREPARED_EXACT_PARTITION' and s['status']=='COMPUTED_COMPLETE_REQUIRES_OUTPUT_AUDIT' and a['status']=='PASS_COMPLETE_REQUIRES_FINAL_REVIEW'
 assert a['cells_checked']==s['cells_complete']==s['cells_required']==54
 assert a['coefficient_overlap_checks']==s['coefficient_overlap_checks']==54*17226==930204
 assert a['exact_Green_scalar_checks']==s['exact_Green_scalar_checks']==m['exact_Green_scalar_checks']==7845
 assert a['integral_contract_checks']==s['integral_contract_checks']==m['integral_contract_checks']==7
 assert a['manifest_sha256']==s['manifest_sha256']==sha(paths['manifest.json'])
 assert a['summary_sha256']==sha(paths['summary.json'])
 assert a['cell_file_sha256']==s['cell_file_sha256']==sha(paths['cells.jsonl'])
 assert a['tail_sha256']==s['tail_sha256']==sha(paths['tail.json'])
 assert a['pins']==s['pins']==m['pins']
 pinned=set(a['pins'])
 for p,h in a['pins'].items(): assert sha(B/p)==h
 assert a['source_sha256']==sha(B/'research/inner_cells/code/audit_covering.py')
 c=load(E/'contracts.json')
 assert c['status']=='PASS_CONTRACTS' and c['exact_Green_scalar_checks']==7845 and c['integral_contract_checks']==7 and c['upper_rows_each']==260
 for p,h in c['dependency_pins'].items(): assert sha(B/p)==h; pinned.add(p)
 control=load(E/'full_serialized_run.json')
 assert control['status']=='COMPLETED' and control['tag']==tag and control['resumed_middle'] is True
 assert control['controller_source_sha256']==sha(B/'research/inner_cells/code/serialize_full.py')=='934a53ad9e7975d4d779f0c07aa2cb27f7deb159cf1736bc791a970731d27c40'
 assert [r['stage'] for r in control['stages']]==['covering','audit']
 for r,source,runtime in zip(control['stages'],['run_covering.py','audit_covering.py'],[m['runtime'],a['runtime']]):
  assert r['returncode']==0 and r['child_pid']==runtime['pid']
  assert r['observed_cmdline']==r['expected_argv'] and r['observed_cmdline'][1:]==['research/inner_cells/code/'+source,'--tag',tag]
  assert r['observed_cmdline'][0]==runtime['executable']
  assert r['observed_executable']==str(Path(runtime['executable']).resolve())
  assert r['PYTHONOPTIMIZE']==runtime['PYTHONOPTIMIZE']=='unset' and runtime['optimize']==0
  assert '-O' not in r['observed_cmdline'] and '-OO' not in r['observed_cmdline']
  assert r['start_utc']<r['end_utc']<=control['end_utc']
 assert t['T_exact']=='7' and t['base_majorant_T_exact']=='5/2' and t['overlap_checks']==6
 assert t['status']=='PASS_REQUIRES_SOURCE_REVIEW' and t['inner_verdict_sha256']=='69923605fab0dad07205705e32b52f26770053cf7392cfd919d1fb2ff415a0fc'
 assert t['source_sha256']==sha(B/'research/inner_cells/code/tail_disk.py') and t['proof_sha256']==m['pins']['research/inner_cells/PROOF.md']
 old=load(B/'research/inner_majorant/evidence/verdict.json'); assert old['status']=='CONFIRMED'
 for p,h in t['dependency_pins'].items(): assert sha(B/p)==h==old['files'][p]; pinned.add(p)
 base=max(F(next(q for q in load(B/p)['cases'] if q['T_exact']=='5/2')['values']['B5']['upper_exact']) for p in ['research/inner_majorant/evidence/inner_result.json','research/inner_majorant/evidence/inner_iv_audit.json'])
 assert base==F(t['B5_upper_exact'])
 for key,row in t['values'].items():
  lo=[F(row[engine]['lower_exact']) for engine in ['arb','iv']]; hi=[F(row[engine]['upper_exact']) for engine in ['arb','iv']]
  assert all(0<=l<=h for l,h in zip(lo,hi)) and max(lo)<=min(hi) and F(row['upper_exact'])==max(hi)
 expected={'W','W_over_m','weighted_0','weighted_1/2','weighted_2888063583571445/9007199254740992'}
 assert set(a['full_inner_maxima'])==set(a['finite_inner_maxima'])==set(s['maxima'])==expected and set(t['values'])==expected|{'L2_squared'}
 public={}; joins={}; comparisons=0
 for key in sorted(expected):
  row=a['full_inner_maxima'][key]
  assert row['finite_audit']==a['finite_inner_maxima'][key] and row['finite_driver']==s['maxima'][key] and row['tail_upper_exact']==t['values'][key]['upper_exact']
  sources=[F(row['finite_audit']['upper_exact']),F(row['finite_driver']['upper_exact']),F(row['tail_upper_exact'])]
  hi=max(sources); assert F(row['upper_exact'])==hi
  bound=strictdecimal(hi,24 if key=='W' else 16)
  assert all(F(bound)>q for q in sources); comparisons+=3
  public[key]={'strict_upper_decimal':bound,'authoritative_upper_exact':str(hi),'finite_audit_location':row['finite_audit'],'finite_driver_location':row['finite_driver'],'tail_upper_exact':row['tail_upper_exact']}
  joins[key]={'finite_audit_upper_exact':str(sources[0]),'finite_driver_upper_exact':str(sources[1]),'tail_upper_exact':str(sources[2]),'whole_upper_exact':str(hi)}
 tail_sq=F(t['values']['L2_squared']['upper_exact']); assert tail_sq>=0 and tail_sq==F(a['tail_L2_squared_upper_exact'])==F(s['tail_L2_squared_upper_exact'])
 finite_sq=[F(a['finite_inner_L2_squared_upper_exact']),F(s['finite_inner_L2_squared_upper_exact'])]; assert min(finite_sq)>=0
 joined=max(finite_sq)+tail_sq
 assert joined==F(a['full_inner_L2_squared_upper_exact']) and finite_sq[1]+tail_sq==F(s['full_inner_L2_squared_upper_exact'])
 root=F(a['full_inner_L2_upper_exact']); assert root>=0 and root*root>=joined
 bound=strictdecimal(root,18); assert F(bound)>root and F(bound)**2>joined; comparisons+=2
 public['L2']={'strict_upper_decimal':bound,'authoritative_upper_exact':str(root)}
 rejection=load(E/'rejections.json'); assert rejection['status']=='PASS_REJECTIONS' and rejection['count']==7
 assert rejection['auditor_sha256']==sha(B/'research/inner_cells/code/audit_covering.py') and rejection['source_sha256']==sha(B/'research/inner_cells/code/check_audit_rejections.py')
 assert len(rejection['fixtures'])==7 and len({r['test'] for r in rejection['fixtures']})==7 and all(r['status']=='REJECTED' for r in rejection['fixtures'])
 for row in rejection['fixtures']:
  for suffix,key in [('manifest.json','manifest_sha256'),('summary.json','summary_sha256'),('cells.jsonl','cells_sha256')]:
   fixture=E/'rejection_fixtures'/row['test']/('assembly_smoke2_'+suffix)
   assert sha(fixture)==row[key]; pinned.add(str(fixture.relative_to(B)))
  fixture=E/'rejection_fixtures'/row['test']/'contracts.json'
  assert sha(fixture)==sha(E/'contracts.json'); pinned.add(str(fixture.relative_to(B)))
 smoke=load(E/'assembly_smoke2_audit.json'); assert smoke['status']=='PASS_PARTIAL_SMOKE' and smoke['cells_checked']==2 and smoke['coefficient_overlap_checks']==34452 and smoke['source_sha256']==a['source_sha256']
 for name in ['manifest.json','summary.json','cells.jsonl']:
  p=E/('assembly_smoke2_'+name); key={'manifest.json':'manifest_sha256','summary.json':'summary_sha256','cells.jsonl':'cell_file_sha256'}[name]
  assert sha(p)==smoke[key]; pinned.add(str(p.relative_to(B)))
 tags=['inner_cells_theorem','inner_cells_primary','inner_cells_independent','inner_cells_closure','inner_cells_assembly','inner_cells_pin_closure','inner_cells_finalizer_source']
 if not preview: tags.append(review_tag)
 reviews=[]
 for tag1 in tags:
  meta=B/'notes/reviews'/f'{tag1}_metadata.json'; reply=B/'notes/reviews'/f'{tag1}_response.md'; v=load(meta)
  assert v['actual_response_model']=='claude-opus-5-5' and v['stop_reason']=='end_turn' and reply.exists()
  reviews.append({'tag':tag1,'actual_model':v['actual_response_model'],'end_utc':v['end_utc'],'metadata_sha256':sha(meta),'response_sha256':sha(reply)})
  pinned.update([str(meta.relative_to(B)),str(reply.relative_to(B))])
 pinned.update(str(p.relative_to(B)) for p in paths.values())
 pinned.update('research/inner_cells/'+p for p in ['code/finalize_verdict.py','code/serialize_full.py','code/check_audit_rejections.py','evidence/full_serialized_run.json','evidence/assembly_smoke2_audit.json','evidence/rejections.json'])
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_FINAL_OUTPUT_REVIEW' if preview else 'CONFIRMED','tag':tag,'cells':54,'coefficient_overlap_checks':930204,'exact_Green_scalar_checks':7845,'exact_integer_convolutions':432,'integral_contract_checks':7,'disk_tail_scalar_overlap_checks':6,'corrupt_artifact_rejections':7,'public_strict_rational_comparisons':comparisons,'public_bounds':public,'sup_tail_joins':joins,'L2_join_squared_upper_exact':str(joined),'files':{p:sha(B/p) for p in sorted(pinned)},'reviews':reviews,'runtime_provenance':'Actual cmdline, executable and optimization environment captured for both covering and auditor children by the pinned controller. Both self-report optimize=0 and PYTHONOPTIMIZE unset. The middle worker was paused and then resumed.','method':'Arb384 physical Green ODEs versus iv160 density moment ODEs, independent center integrals, full-frequency versus compressed-index exact integer interval convolution and Bernstein bounds. Fresh iv192 output audit verifies partition, weights and squared integrals.','shared_dependencies':'The audited exact modal density, canonical boundary moment enclosures and exact strain normalization, plus the previously proved Taylor remainder theorem. The six disk scalar expressions use the same accepted B5 upper endpoint, evaluated with different interval factorizations. The output auditor checks saved aggregation, not unsaved Taylor coefficients. The two cell methods compute different valid upper majorants, so only the underlying coefficients are required to overlap.','scope':'Exact normalized modal trial on 0<=r<=exp(t_a). W is the true residual sine coefficient absolute sum. With u=r/L, m=u^3(1+u^2)^((k-3)/2), weighted_delta means (1+u)^delta W/m. L2 is ||epsilon/m|| with measure dX/(1+u^2). Quotients at the origin use the proved limiting bound. No derivative norm, X3 distance, inverse estimate, existence, exclusion or decisive endpoint.'}
 destination=E/('final_review_packet.json' if preview else 'verdict.json')
 destination.open('x').write(json.dumps(result,indent=2)+'\n')
 if not preview:
  text='# Complete inner zeroth residual certificate\n\n'+result['utc']+'; CONFIRMED.\n\nFor the exact normalized modal trial, on every 0<=r<=R=exp(t_a), put u=r/L and m=u^3(1+u^2)^((k-3)/2). W is the angular sine coefficient absolute sum of the true residual. The origin is interpreted by the limiting estimate.\n\n| Quantity | Strict upper bound |\n|---|---|\n'
  for key,row in public.items(): text+='| '+key+' | '+row['strict_upper_decimal']+' |\n'
  text+='\nThe L2 row is ||epsilon/m|| in L2(dX/(1+u^2)) on this disk. The 54 adjoining log cells cover -7<=log(r/R)<=0, and a separate analytic bound covers log(r/R)<=-7. There are 930204 coefficient comparisons, 7845 exact Green scalar identities, 432 integer convolutions, seven integral contract checks and six disk scalar comparisons. Seven deliberately corrupted artifact sets were rejected.\n\n'+result['method']+'\n\nShared dependencies: '+result['shared_dependencies']+'\n\nAll inputs, sources, results and actual Opus 5.5 review records are pinned in evidence/verdict.json. This is a zeroth residual certificate for the modal trial. The global middle region, derivative norms, distance to X3 and inverse theorem are separate obligations.\n'
  (B/'research/inner_cells/RESULT.md').open('x').write(text)
 print(json.dumps({'utc':result['utc'],'status':result['status'],'bounds':{k:v['strict_upper_decimal'] for k,v in public.items()},'output_sha256':sha(destination)},indent=2))
if __name__=='__main__':
 ap=argparse.ArgumentParser(); ap.add_argument('--tag',default='full_q16'); ap.add_argument('--review-tag',default='inner_cells_final_output'); ap.add_argument('--preview',action='store_true'); args=ap.parse_args(); run(args.tag,args.review_tag,args.preview)

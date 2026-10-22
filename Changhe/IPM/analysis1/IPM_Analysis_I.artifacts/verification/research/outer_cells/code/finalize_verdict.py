"""Close the full exterior audit; never infer success from partial rows."""
import sys,json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];E=B/'research/outer_cells/evidence'
assert sys.flags.optimize==0

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
 def bad(x):raise ValueError(('nonfinite JSON',x))
 return json.loads(Path(p).read_bytes(),parse_constant=bad)
def strictdecimal(q,places=14):
 q=F(q);assert q>=0;den=10**places;n=(q.numerator*den)//q.denominator+1;assert F(n,den)>q
 s=str(n).zfill(places+1);return s[:-places]+'.'+s[-places:]
def run(tag,review_tag):
 auditpath=E/(tag+'_audit.json');summarypath=E/(tag+'_summary.json');a=load(auditpath);s=load(summarypath);manifestpath=E/(tag+'_manifest.json');m=load(manifestpath)
 assert a['status']=='PASS_COMPLETE_REQUIRES_FINAL_REVIEW' and s['status']=='COMPUTED_COMPLETE_REQUIRES_OUTPUT_AUDIT'
 assert a['cells_checked']==s['cells_complete']==s['cells_required']==89 and a['coefficient_overlap_checks']==s['coefficient_overlap_checks']==1533114 and a['exact_Green_scalar_checks']==17748
 assert a['summary_sha256']==sha(summarypath) and a['manifest_sha256']==sha(manifestpath) and a['cell_file_sha256']==sha(E/(tag+'_cells.jsonl'))
 assert a['pins']==s['pins']==m['pins']
 for p,h in a['pins'].items():assert sha(B/p)==h
 assert a['source_sha256']==sha(B/'research/outer_cells/code/audit_covering.py')
 serialized=load(E/'full_serialized_run.json');assert serialized['status']=='COMPLETED' and serialized['covering_returncode']==serialized['audit_returncode']==0 and serialized['resumed_middle'] is True and serialized['tag']==tag
 runtime=load(E/'full_runtime_provenance.json');assert runtime['PYTHONOPTIMIZE']=='unset' and runtime['observer_optimize']==0 and '-O' not in runtime['cmdline'] and '-OO' not in runtime['cmdline']
 assert runtime['versions']=={'mpmath':'1.3.0','python-flint':'0.9.0'}
 snap=load(E/'full_serialized_covering_start_snapshot.json');assert snap['status']=='RUNNING_COVERING' and snap['child_pid']==runtime['pid'] and snap['controller_pid']==serialized['controller_pid']
 assert runtime['covering_snapshot_sha256']==sha(E/'full_serialized_covering_start_snapshot.json') and runtime['controller_source_sha256']==sha(B/'research/outer_cells/code/serialize_full.py')
 # The controller passed its unchanged environment and sys.executable to both
 # children. Its source records no -O flag and no environment optimization change.
 assert runtime['cmdline'][1:]==['research/outer_cells/code/run_covering.py','--tag',tag]
 tail=load(E/(tag+'_tail_l2.json'));assert a['tail_l2_sha256']==s['tail_l2_sha256']==sha(E/(tag+'_tail_l2.json')) and tail['moment_overlap_checks']==3508 and tail['T_exact']=='17'
 assert tail['published_upper_exact']==a['tail_L2_upper_exact']==s['tail_L2_upper_exact']
 joined_sq=max(F(a['finite_exterior_L2_squared_upper_exact']),F(s['finite_exterior_L2_squared_upper_exact']))+F(tail['published_upper_exact'])**2
 assert F(a['full_exterior_L2_squared_upper_exact'])>=joined_sq
 leading_path=B/'research/outer_leading_cancellation/evidence/verdict.json';leading=load(leading_path)
 assert leading['status']=='CONFIRMED' and sha(leading_path)==a['leading_verdict_sha256']==tail['leading_verdict_sha256']=='6a56059e5b9e2041ad94aed5be982b19b94d0b23f0c00563a20452b314ba89f9'
 assert runtime['controller_source_sha256']=='2378ffda9809a08affa81a86b99909ea9e113ffef96f77058c1da071024f7ff8'
 tail_rows={r['quantity']:r for r in leading['public_bounds'] if r['T_exact']=='17'}
 mapping={'W':'absolute_W','W_over_m':'weighted_delta_0','weighted_0':'weighted_delta_0','weighted_1/2':'weighted_delta_1/2','weighted_2888063583571445/9007199254740992':'weighted_delta_2888063583571445/9007199254740992'}
 assert set(a['full_exterior_maxima'])==set(s['maxima'])==set(mapping)
 public={};comparisons=0;tail_joins={}
 for key,quantity in mapping.items():
  row=tail_rows[quantity];tail_hi=F(row['strict_public_upper_exact']);assert tail_hi>max(F(row['primary_upper_exact']),F(row['independent_upper_exact']))
  finite_hi=max(F(a['finite_exterior_maxima'][key]['upper_exact']),F(s['maxima'][key]['upper_exact']))
  assert tail_hi<=finite_hi and F(a['full_exterior_maxima'][key]['upper_exact'])>=F(a['finite_exterior_maxima'][key]['upper_exact'])
  tail_joins[key]={'tail_strict_upper_exact':str(tail_hi),'finite_upper_exact':str(finite_hi),'tail_le_finite':True}

 for key,row in a['full_exterior_maxima'].items():
  hi=max(F(row['upper_exact']),F(s['maxima'][key]['upper_exact']));bound=strictdecimal(hi)
  assert F(bound)>F(row['upper_exact']) and F(bound)>F(s['maxima'][key]['upper_exact']);comparisons+=2
  public[key]={'strict_upper_decimal':bound,'authoritative_upper_exact':str(hi),'audit_maximum_location':row['where'],'driver_finite_maximum_location':s['maxima'][key]}
 hi=F(a['full_exterior_L2_upper_exact']);assert hi>=0 and hi*hi>=F(a['full_exterior_L2_squared_upper_exact']);bound=strictdecimal(hi);assert F(bound)>hi;comparisons+=1
 public['L2']={'strict_upper_decimal':bound,'authoritative_upper_exact':str(hi)}
 tags=['outer_cells_theorem','outer_cells_source','outer_cells_assembly','outer_cells_pin_closure','outer_cells_final_output',review_tag];reviews=[];paths=set(a['pins'])
 for t in tags:
  meta=B/'notes/reviews'/f'{t}_metadata.json';reply=B/'notes/reviews'/f'{t}_response.md';v=load(meta);assert v['actual_response_model']=='claude-opus-5-5' and v['stop_reason']=='end_turn' and reply.exists()
  reviews.append({'tag':t,'actual_model':v['actual_response_model'],'end_utc':v['end_utc'],'metadata_sha256':sha(meta),'response_sha256':sha(reply)});paths.update([str(meta.relative_to(B)),str(reply.relative_to(B))])
 for suffix in ['audit.json','summary.json','manifest.json','cells.jsonl','tail_l2.json']:paths.add('research/outer_cells/evidence/'+tag+'_'+suffix)
 paths.update(['research/outer_cells/evidence/full_serialized_run.json','research/outer_cells/evidence/full_runtime_provenance.json','research/outer_cells/evidence/full_serialized_covering_start_snapshot.json','research/outer_cells/code/serialize_full.py','research/outer_cells/code/finalize_verdict.py','research/outer_leading_cancellation/evidence/verdict.json'])
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','tag':tag,'cells':89,'coefficient_overlap_checks':1533114,'exact_Green_scalar_checks':17748,'exact_integer_convolutions':89*8,'tail_moment_overlap_checks':3508,'public_strict_rational_comparisons':comparisons,'public_bounds':public,'sup_tail_joins':tail_joins,'L2_join_squared_upper_exact':str(joined_sq),'files':{p:sha(B/p) for p in sorted(paths)},'reviews':reviews,'runtime_provenance':'Actual covering cmdline/executable/environment checked live, PYTHONOPTIMIZE unset; auditor provenance follows from the separately reviewed controller source hash2378ffda9809a08affa81a86b99909ea9e113ffef96f77058c1da071024f7ff8 using the same interpreter and unchanged optimization environment for both children. Auditor live environment was not separately captured; assertions enabled by this source and runtime chain.','method':'Arb384 full-frequency Taylor convolution versus iv160 Taylor models, independently rebuilt exact Green polynomials, compressed angular indices and exact integer interval convolution/Bernstein; independent iv192 coverage/weight/L2 output audit.','shared_dependencies':'Audited exact affine density coefficients, the z enclosure and canonical transient intervals, radial decomposition and Taylor-remainder theorem. The output auditor rechecks coverage, hashes, aggregation and scalar consequences; it does not itself reconstruct residual coefficient bounds.','scope':'The exact normalized modal trial on r>=R=exp(t_b). W is the residual sine coefficient absolute sum. Weights use u=r/L and m=u^3(1+u^2)^((k-3)/2). L2 is ||epsilon/m|| with measure dX/(1+u^2). Zeroth residual only. No derivative, X3-distance, global inverse, existence or exclusion conclusion.'}
 (E/'verdict.json').write_text(json.dumps(result,indent=2)+'\n')
 text='# Complete exterior zeroth residual certificate\n\n'+result['utc']+'; CONFIRMED.\n\nFor the exact normalized modal trial, on every r>=R=exp(t_b), the following strict bounds hold. Put u=r/L, m=u^3(1+u^2)^((k-3)/2). W is the angular sine coefficient absolute sum of the true residual.\n\n| Quantity | Strict upper bound |\n|---|---|\n'
 for key,row in public.items():text+='| '+key+' | '+row['strict_upper_decimal']+' |\n'
 text+='\nThe L2 row means ||epsilon/m||_(L2(dX/(1+u^2))) on this exterior. The89 exactly adjoining log-cells cover0<=log(r/R)<=17; the independently audited complete tail covers log(r/R)>=17. There are1533114 residual coefficient comparisons,17748 exact Green scalar equalities and3508 tail-moment comparisons. All inputs, sources, output rows, audits and actual Opus5.5 review records are pinned in evidence/verdict.json.\n\n'+result['method']+'\n\nShared dependencies: '+result['shared_dependencies']+'\n\nThis gives no derivative norm, rigorous distance to X3, inverse estimate or decisive endpoint.\n'
 (B/'research/outer_cells/RESULT.md').write_text(text);print(json.dumps({'utc':result['utc'],'status':result['status'],'bounds':{k:v['strict_upper_decimal'] for k,v in public.items()},'verdict_sha256':sha(E/'verdict.json')},indent=2))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='full_q16');ap.add_argument('--review-tag',default='outer_cells_final_closure');args=ap.parse_args();run(args.tag,args.review_tag)

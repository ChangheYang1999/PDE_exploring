"""Complete a preserved valid norm after a rational decimal parsing error."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json,time
from flint import fmpq as Q, arb, ctx
R=Path(__file__).resolve().parents[3];B=R/'research/reference_difference';ctx.prec=2048
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(x):return arb(x.p)/arb(x.q)
def main():
 start=time.monotonic(); stem='C1-N1-021-heldin14-legqs25p50_minus_C1-N1-020-legqs25p50-quot013_2048';src=B/f'verification/{stem}.json';out=B/f'verification/{stem}_complete_v2.json';assert not out.exists()
 d=json.loads(src.read_text());checks={};bindings={}
 for rel,h in d['inputs'].items():assert sha(R/rel)==h;bindings[rel]=h
 fixture=json.loads((B/'verification/fixtures.json').read_text());assert all(fixture['checks'].values())
 for rel,h in fixture['inputs'].items():assert sha(R/rel)==h;bindings[rel]=h
 checks['all_saved_inputs_and_fixtures_bound']=True
 assert d['potential_prefix_equal'] and all(x['equal'] and not x['difference'] and x['first']==x['second'] for x in d['prefix']);checks['all_four_complete_potential_prefixes']=True
 assert all(x['value']=='0' for x in d['endpoint_checks']);checks['early_field_endpoints_zero']=True
 point=d['point_checks'];assert point['value_count']==9 and point['minimum_accuracy_bits']>150
 assert all(v['overlap'] and arb(v['compact']).overlaps(arb(v['Cartesian'])) for p in point['points'] for v in p['fields'].values());checks['nine_saved_cartesian_overlaps']=True
 n=d['norm'];assert n['group_count']==14 and len(n['groups'])==14 and n['ordered_pairs']==834 and n['norm_accuracy_bits']>150 and n['minimum_group_accuracy_bits']>150
 total=arb(0)
 for row in n['groups']:
  assert Q(row['b'])>-1 and row['integral_accuracy_bits']>150
  value=arb(row['integral_ball']);assert value.is_finite();total+=value
 assert total.overlaps(arb(n['sum_ball']));checks['fourteen_admissible_groups_and_saved_sum']=True
 square=arb(n['square_ball']);norm=arb(n['norm_ball']);assert square>0 and square.overlaps(arb.pi()/2*total) and square.sqrt().overlaps(norm)
 tau=Q(n['tau_upper_exact']);assert norm<ar(tau);checks['positive_square_sqrt_and_outward_tau']=True
 parentpath=R/'research/candidate020_weak_peer/verification/result.json';p=json.loads(parentpath.read_text());assert p['candidate']==d['parent'] and p['verdict'].startswith('CONFIRMED')
 for rel,h in p['own_inputs'].items():assert sha(R/rel)==h;bindings[rel]=h
 for rel,info in p['frozen_or_retained_sources'].items():assert sha(R/rel)==info['stored_sha256'];bindings[rel]=info['stored_sha256']
 rawkey=next(rel for rel in d['inputs'] if rel.endswith('legqs25p50_gpu_m16_exact.json'))
 assert bindings[rawkey]==d['parent_raw_sha256'];checks['accepted_parent_raw_and_all_bindings']=True
 row=next(x for x in p['rows'] if x['n']==19 and x['K']==1800);floor=Q(row['strict_floor']);screens=[]
 for name,b in [('graded',Q(25,54684)),('sharpw_unrestricted_safe_ceiling',Q(28496,10**10)),('TB_sharp_safe_ceiling',Q(3793,10**9))]:
  margin=floor-b;passes=margin>=0 and square<=ar(margin*margin);failed=margin>=0 and square>ar(margin*margin);taupass=tau<=margin;assert not taupass or passes
  screens.append({'ceiling_id':name,'b':str(b),'strict_parent_distance_floor':str(floor),'d_minus_b':str(margin),'tau_upper_exact':str(tau),'certified_square_below_margin_squared':passes,'certified_square_above_margin_squared':failed,'tau_below_margin':taupass,'successor_exclusion_by_this_screen':False,'scope':'Own actual-pair result pending independent reproduction. A failed sufficient comparison is no existence or nonexistence result.'})
 assert all(x['certified_square_above_margin_squared'] and not x['tau_below_margin'] for x in screens);checks['all_three_screen_comparisons_fail']=True
 for path in [src,Path(__file__),B/'PROOF_POSTPROCESS.md',B/'verification/DEVELOPMENT.md',R/'logs/reference_difference_actual021.log',parentpath,R/'research/candidate020_weak_peer/PROOF.md']:
  bindings[str(path.relative_to(R))]=sha(path)
 d['postprocessing']={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'check_count':len(checks),'complete_source_bindings':bindings,'failed_initial_result_sha256':sha(src),'norm_recomputed':False,'decimal_parser_failure_repaired_only':True}
 d['screens']=screens;d['status']='COMPLETE OWN exact density difference; all three reference-screen comparisons fail; independent actual-pair reproduction OPEN';d['verdict']='OPEN independent actual-pair reproduction';d['parent_evidence_record_sha256']=sha(parentpath)
 with out.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
 print('COMPLETE',sha(out),d['postprocessing']['utc'],'seconds',d['postprocessing']['elapsed_seconds'],'checks',len(checks),'bindings',len(bindings),'norm',n['norm_ball'],flush=True)
if __name__=='__main__':main()

"""Reciprocal finite acceptance of T4-466/467/470; no peer execution."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,sys,time
from fractions import Fraction
from flint import fmpq as Q,arb,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_reciprocal_audits'
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def aq(q):
 q=Q(q);return arb(q.numerator)/arb(q.denominator)
def main():
 ctx.prec=2048;start=time.monotonic();inputs={};external={};checks={}
 def ck(k,v):
  assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);got=sha(p);key=str(p.relative_to(R))
  assert h is None or got==h,(key,h,got)
  assert key not in inputs or inputs[key]==got;inputs[key]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 def ex(p,h):
  p=Path(p);ck('external:'+str(p),sha(p)==h) if str(p) not in external else None
  assert str(p) not in external or external[str(p)]==h;external[str(p)]=h
 first=read(B/'verification/PROOF_FIRST.json');bind(B/'PROOF.md',first['proof_sha256']);bind(Path(__file__))
 mf=read(B/'source/MANIFEST.json',first['manifest_sha256'])
 for name,v in mf['files'].items():bind(B/'source'/name,v['sha256']);ex(v['original_path'],v['sha256'])
 review=read(B/'source/T4_466_review.json')
 ck('466_proof_identity',review['proof_sha256']==sha(B/'source/T4_466_PROOF.md'))
 ck('466_no_numerical_execution',not review['foreign_code_executed'] and not review['new_candidate_numerics_accepted'])
 expected={k:'CONFIRMED' for k in ['functional_domain','origin_and_cutoff','cutoff_wording','finite_test_sum','polar_energy','residual_pairing','directed_quotients','ordering_scope']}
 expected.update(lower_below_upper_implies_upper='REFUTED',new016numerics='OPEN')
 ck('466_exact_claim_scopes',{v['claim']:v['verdict'] for v in review['claims']}==expected)
 for row in review['inputs']:
  ex(R.parent/'c1-t4/research/negative_norm_dual_audit'/row['local'],row['sha256'])
 results={num:read(B/f'source/T4_{num}_result.json') for num in [467,470]}
 for num,topic in [(467,'candidate016_complete_forcing_audit'),(470,'candidate016_dual_replay_audit')]:
  d=results[num];root=R.parent/'c1-t4/research'/topic
  ck(f'{num}_complete_checklist',d['check_count']==len(d['checks'])==({467:8874,470:2099}[num]) and len(set(d['checks']))==len(d['checks']))
  ck(f'{num}_proof_identity',d['proof_sha256']==sha(B/f'source/T4_{num}_PROOF.md'))
  ck(f'{num}_checker_identity',d['checker_sha256']==sha(B/f'source/T4_{num}_check.py'))
  ck(f'{num}_manifest_identity',d['manifest_sha256']==sha(B/f'source/T4_{num}_manifest.json'))
  for row in read(B/f'source/T4_{num}_manifest.json'):
   p=root/row['local'];ex(p,row['sha256'])
   if 'decoded_sha256' in row:
    ck(f'{num}_decoded:'+str(p),sha256(gzip.decompress(p.read_bytes())).hexdigest()==row['decoded_sha256']);ex(row['original'],row['decoded_sha256'])
  graph=read(B/f'source/T4_{num}_bindings.json');graph=graph['records'] if isinstance(graph,dict) else graph
  for row in graph:ex(row.get('original',row.get('source')),row['sha256'])
  ck(f'{num}_no_foreign_execution',not d['foreign_code_executed'])
 own=read(R/'research/candidate016_full_forcing/verification/result_v03.json','cb7906f600202359c4d33a5cfc9afd1e9b338aaf903407253ebf57f0ca8b70f1')
 accepted=read(R/'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json','a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc')
 dual=read(R/'research/candidate016_dual_lower/verification/result.json','e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa')
 archive=read(R/'research/candidate016_pairing_archive/verification/result.json','c3e148aaab94ed6b50920f114c80260cb7f0061756398a90f6f444fa6b0367c6')
 for d in [own,accepted,dual,archive]:
  ck('ownaccepted:'+d['utc'],all(d['checks'].values()))
  for rel,h in d['inputs'].items():bind(R/rel,h)
 for row in archive['rows']:bind(R/row['group_record'],row['group_sha256'])
 d=results[467];ck('467_same393',d['N4_393_sha256']==sha(R/'research/candidate016_full_forcing/verification/result_v03.json'))
 ck('467_ordered_hessian',d['complete_hessian_multiplicities']==[1,2,1])
 b=Q(1)
 for j in range(57):b*= (Q(4,5)-j)/(j+1)
 eps=abs(b)*Q(3,5)**57/Q(2,5);ck('467_exact_binomial_remainder',eps==Q(d['exact_binomial_error']))
 for name,row in d['components'].items():
  old=accepted['norms'][name];lo,hi=Q(row['strict_lower_exact']),Q(row['strict_upper_exact'])
  ck(name+'_same_component_endpoints',lo==Q(old['accepted_lower_exact']) and hi==Q(old['accepted_upper_exact']))
  ck(name+'_directed_component_interval',aq(lo)<arb(row['lower_recomputed']).lower() and arb(row['upper_recomputed']).upper()<aq(hi))
  ck(name+'_complete_groups',row['groups']==31 and row['ordered_pair_count']=={'G0':14960,'rF':14960,'G1':30176,'P2':45648}[name])
 ck('467_ten_instances',len(d['instances'])==len(own['instances'])==10)
 for row,old in zip(d['instances'],own['instances']):
  label=row['framework'];ck(label+'_same_forcing_lower',label==old['framework'] and row['kind']==old['kind'] and Q(row['strict_lower_exact'])==Q(old['forcing_lower_comparison']['strict_lower_exact']))
  ck(label+'_test_failure',Q(row['strict_lower_exact'])>Q(old['threshold_exact'])>0)
  ck(label+'_directed_ratio',Q(row['strict_factor_exact'])==Q(old['ratio_lower_comparison']['strict_lower_exact']) and aq(Q(row['strict_factor_exact']))<arb(row['factor_ball']).lower())
 ck('467_five_XSW_orders',len(d['actual_XSW_orderings'])==len(own['XSW_pair_ordering'])==5)
 for row,old in zip(d['actual_XSW_orderings'],own['XSW_pair_ordering']):
  label=row['framework'];gap=Q(row['candidate016_lower_exact'])-Q(row['baseline007_upper_exact'])
  ck(label+'_exact_XSW_identity',all(row[k]==old[k] for k in ['framework','candidate016_lower_exact','baseline007_upper_exact']))
  ck(label+'_actual_positive_gap',gap==Q(row['exact_gap'])==Q(Fraction(row['gap_decimal']).numerator,Fraction(row['gap_decimal']).denominator) and gap>0)
 td=results[470];sum2=Q(0)
 for row in td['rows']:
  n=row['n'];old=read(R/f'research/candidate016_dual_lower/verification/mode_{n:03d}.json')
  ck(f'{n}_full_mode_identity',row['complete_projection_sha256']==old['complete_projection_sha256'])
  ck(f'{n}_same_vector_size',row['coefficient_count']==old['coefficient_count'] and row['beta_groups']==old['beta_group_count']==13 and row['ordered_energy_pairs']==169)
  den=Q(old['gradient_energy_over_pi_exact'])
  ck(f'{n}_exact_positive_denominator',den>0 and sha256(str(den).encode()).hexdigest()==row['gradient_energy_over_pi_sha256'])
  ck(f'{n}_all_exact_energy_groups',len(row['gradient_group_checks'])==len(old['gradient_energy_groups'])==row['exact_gradient_groups'])
  for j,(g,h) in enumerate(zip(row['gradient_group_checks'],old['gradient_energy_groups'])):
   ck(f'{n}_energygroup{j}',g['exponent']==h['exponent'] and g['degree']==h['degree'] and g['integral_over_pi_sha256']==sha256(h['integral_over_pi_exact'].encode()).hexdigest())
  ck(f'{n}_all_pairing_groups',row['pairing_groups_checked']==len(old['pairing_groups'])==len(row['pairing_group_evidence']))
  for j,(g,h) in enumerate(zip(row['pairing_group_evidence'],old['pairing_groups'])):
   ck(f'{n}_pairinggroup{j}',g['exponent']==h['exponent_before_order'] and g['order']==h['endpoint_order'] and Q(g['exponent'])+g['order']>-1)
  floor=Q(row['strict_quotient_floor']);ck(f'{n}_same_floor',floor==Q(old['quotient_strict_lower_exact']) and floor>0);sum2+=floor**2
  ar=next(v for v in archive['rows'] if v['kind']=='dual' and v['n']==n)
  p=arb(ar['pairing_replayed_ball']);wide=arb(row['pairing_final_certificate']);ck(f'{n}_archive_inside_T4_pairing',wide.lower()<p.lower() and p.upper()<wide.upper())
  quotient=abs(p)/(arb.pi()*aq(den)).sqrt();ck(f'{n}_floor_from_repaired_archive',aq(floor)<quotient.lower())
  ck(f'{n}_historical_display_scope',row['coarse_group_sum_cannot_certify_pairing'] and not row['new_pairing_integral'])
 ck('470_H_square_same',sum2==Q(td['H_lower_square_exact'])==Q(dual['H_lower_square_exact']))
 hf=Q(td['H_strict_lower_exact']);ck('470_directed_H_floor',hf==Q(dual['H_strict_lower_exact']) and hf**2<sum2)
 L={k:Q(accepted['norms'][k]['accepted_lower_exact']) for k in ['G0','G1','P2']}
 E=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2+Q(20,21)*2**18*sum2
 ef=Q(td['E2_strict_lower_exact']);baseline=Q(td['007_E2_strict_upper_exact'])
 ck('470_directed_E2_floor',E==Q(td['E2_lower_square_exact'])==Q(dual['E2_lower_square_exact']) and ef==Q(dual['E2_strict_lower_exact']) and ef**2<E)
 ck('470_actual_E2_gap',baseline==Q(dual['baseline007_E2_strict_upper_exact']) and ef>baseline and ef-baseline==Q(td['strict_E2_gap']))
 ck('470_no_pairing_repetition_claim',not td['candidate_pairing_integrals_repeated'] and not td['coarse_group_sum_is_a_pairing_reproduction'])
 for rel,h in inputs.items():assert sha(R/rel)==h,rel
 for path,h in external.items():assert sha(path)==h,path
 result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'inputs':inputs,'external_bindings':external,'checks':checks,'check_count':len(checks),'peer_code_executed':False,'candidate_integrals_repeated':False,'accepted_reviews':['T4-466 analytic domain and dual formula','T4-467 complete component and forcing finite assembly','T4-470 exact energy and same-E2 comparison'],'archive_repair':'N4-399 replaces the original coarse-group replay limitation; original audits unchanged','H_strict_lower_exact':str(hf),'E2_strict_lower_exact':str(ef),'actual_E2_gap_exact':str(ef-baseline),'verdict':'CONFIRMED reciprocal scope and finite evidence; original moment/derivative/commutator premises retained'}
 with(B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',len(inputs),'ownbindings',len(external),'external',result['elapsed_seconds'],sha(B/'verification/result.json'),flush=True)
if __name__=='__main__':main()

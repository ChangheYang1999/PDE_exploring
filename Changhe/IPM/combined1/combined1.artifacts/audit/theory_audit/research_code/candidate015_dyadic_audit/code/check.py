"""T4 finite audit of exact origin, projected energies and complete dyadic cells."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,gzip,sys,time
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(1000000)
B=Path(__file__).resolve().parents[1];ctx.prec=1024
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def A(q):q=Q(q);return arb(q.numerator)/arb(q.denominator)
def read(rel):
 p=B/rel;raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def main():
 start=time.monotonic();checks={};sources=read('data/manifest.json')
 def check(label,test):
  assert label not in checks,label
  assert test,label
  checks[label]=True
 for z in sources:
  p=B/z['local'];check('binding:'+z['local'],sha(p)==z['sha256'])
  if z['decoded_sha256']:check('decoded:'+z['local'],sha256(gzip.decompress(p.read_bytes())).hexdigest()==z['decoded_sha256'])
 pars=read('data/parameters.json');own=read('source/N4_production.json');m=read('source/N4_manifest.json');comp=read('source/N4_comparison.json');can=read('source/canonical.json.gz');peer=read('source/N3_wlap_modes.json.gz');bridge=read('source/T4_canonical_agreement.json');external=read('data/external_bindings.json')
 check('all_33_external_hashes_observed',external['all_matched'] and len(external['bindings'])==33)
 check('accepted_comparison_hash','24bdc65df109a3002e4bdd6ac8676e955a606466c3fb046a4d04bcd91e741266'==sha(B/'source/N4_comparison.json'))
 check('candidate_ids',comp['candidate']==own['candidate']==m['candidate']==peer['id']=='C1-N1-015-pairQ-quot013')
 check('raw_source',comp['raw_sha256']==can['source_sha256']==pars['raw_sha256'])
 check('canonical_json',comp['canonical_sha256']==pars['canonical_sha256']==sha256(gzip.decompress((B/'source/canonical.json.gz').read_bytes())).hexdigest())
 check('accepted_T4_N4_canonical_agreement',bridge['termwise_rational_map_equal'] and bridge['exact_c_origin_strain_slope_equal'] and pars['canonical_sha256'] in bridge['inputs'].values())
 check('no_upper_norm_claim',not own['complete_upper_norm'] and not comp['complete_upper_norm'])
 check('complete_selected_modes',own['selected_modes']==comp['projection_modes']==peer['only_modes']==[1,3])
 check('comparison_flags',comp['check_count']==len(comp['checks']) and all(comp['checks'].values()))
 c=Q(pars['c']);gamma=1/c;delta=1-gamma;check('same_c',c==Q(can['cl'])==Q(m['c_exact']))
 pairs=[(tuple(k),Q(v)) for k,v in zip(can['order'],can['coefficients'],strict=True)]
 check('canonical_term_count',len(pairs)==1922==bridge['nonzero_terms'])
 check('no_duplicate_coefficient_keys',len({k for k,v in pairs})==len(pairs))
 check('positive_integral_indices_and_nonzero_coefficients',all(len(k)==3 and all(isinstance(i,int) and i>=0 for i in k) and k[2]>=k[1] and v for k,v in pairs))
 serial=''.join(','.join(map(str,k))+':'+str(v)+'\n' for k,v in sorted(pairs))
 check('coefficient_serialization',sha256(serial.encode()).hexdigest()==can['canonical_serialization_sha256']==peer['canonical_sha256']==pars['canonical_serialization_sha256'])
 xy=Q(0);yy=Q(0);retained=0
 for (j,mn,k),b in pairs:
  if k>2:continue
  p=(3+gamma-j*delta)/2;alpha=p-k;count=2-k;coef=Q(1)
  for i in range(count):coef*= (alpha-i)/(i+1)
  xy+=b*coef*[2,0,-6][mn];yy+=b*coef*[1,-1,1][mn];retained+=1
 strain=4*xy;a0=-strain-24*yy
 check('origin_strain_exact',strain==1-c==Q(can['strain'])==Q(m['strain_exact']))
 check('origin_slope_exact',a0==Q(can['a0'])==Q(m['a0_exact'])==Q(own['a0_exact']))
 check('origin_slope_margin',a0-(5*c-4)==Q(own['origin_threshold_margin']) and a0>=5*c-4 and 1<c<2)
 d=c-1;disc=(2*d-3)**2+16*d;star=(A(2*d-3)+A(disc).sqrt())/8
 check('H_critical_point_domain',0<star and star<A(d))
 H=(A(d)-star)*(4*arb.pi()*star*(1+star)).sqrt()
 check('H_critical_value',H>0 and H.overlaps(arb(own['H_max'])) and star.overlaps(arb(own['s_maximizer'])))
 records={n:read(f'source/N4_mode{n}.json') for n in [1,3]}
 for n,z in records.items():
  key=f'mode{n}:'
  check(key+'record_hash',sha(B/f'source/N4_mode{n}.json')==own['mode_result_sha256'][str(n)])
  check(key+'manifest_hash',z['manifest_sha256']==own['manifest_sha256']==sha(B/'source/N4_manifest.json'))
  check(key+'complete_derivative_flags',z['exact_Cartesian_polar_trace_equal'] and z['exact_mixed_derivatives_equal'])
  check(key+'all_eight_weights',[Q(r['a']) for r in z['weights']]==[Q(k,4) for k in range(8)])
  check(key+'all_endpoint_branches',[r['ell'] for r in z['endpoints']]==list(range(1,17)))
  margins={}
  for e in z['endpoints']:
   margin=e['ell']*delta+2*e['order']-2
   check(key+f"endpoint_integrability_{e['ell']}",margin>0)
   margins[e['ell']]=margin
  for ell in margins:
   for k in margins:
    # Twice the cross denominator at a=0 is the sum of diagonal margins.
    check(key+f'cross_integrability_{ell}_{k}',(margins[ell]+margins[k])/2>0)
  for r in z['weights']:
   en=arb(r['energy']);check(key+'positive_energy_at_'+r['a'],en>0 and en.sqrt().overlaps(arb(r['norm'])))
 check('N3_decoded_source',sha256(gzip.decompress((B/'source/N3_wlap_modes.json.gz').read_bytes())).hexdigest()==comp['peer_source_files']['N3_wlap_modes.json.gz']['original_sha256'])
 check('N3_code_binding',peer['code_sha256']==comp['peer_source_files']['N3_wlap_modes.py']['original_sha256'])
 weights=[Q(k,4) for k in range(1,8)];check('all_peer_positive_weights',set(peer['per_a'])==set(map(str,weights)))
 norms={};energyrows=[]
 for a in weights:
  key='a='+str(a)+':' ;p=peer['per_a'][str(a)];squares=[Q(r['N_a_mode_sq_over_pi_exact']) for r in p['modes']];total=Q(p['sq_over_pi_exact'])
  check(key+'exact_modes',[r['mode'] for r in p['modes']]==[1,3])
  check(key+'exact_positive_sum',all(z>0 for z in squares) and sum(squares,Q(0))==total)
  ownsum=arb(0);joined=next(z for z in comp['weights'] if Q(z['a'])==a)
  for n,rat in zip([1,3],squares,strict=True):
   prod=next(z for z in records[n]['weights'] if Q(z['a'])==a);ownen=arb(prod['energy']);en=arb.pi()*A(rat);ownsum+=ownen
   check(key+f'complete_energy_{n}',ownen.overlaps(en))
   compn=next(z for z in joined['mode_energy_comparisons'] if z['mode']==n)
   check(key+f'comparison_energy_{n}',en.overlaps(arb(compn['peer_exact_energy'])) and ownen.overlaps(arb(compn['own_energy'])))
  norm=(arb.pi()*A(total)).sqrt();ons=ownsum.sqrt();check(key+'exact_total_vs_independent_sum',norm.overlaps(ons))
  check(key+'directed_N3_endpoints',arb(p['N_a_LB']).lower()<norm.lower() and norm.upper()<arb(p['N_a_UB']).upper())
  check(key+'saved_total',norm.overlaps(arb(joined['peer_exact_norm'])) and ons.overlaps(arb(joined['own_sum_norm'])))
  norms[str(a)]=ons;energyrows.append({'a':str(a),'own_sum_norm':ons.str(100),'exact_N3_sum_norm':norm.str(100)})
 cap=1+1/c;points=[Q(k,4) for k in range(7)]+[cap]
 check('cell_parameter_range',Q(3,2)<cap<Q(7,4)<2)
 cells=[]
 for i,(lo,hi) in enumerate(zip(points[:-1],points[1:],strict=True)):
  e=hi if i<6 else Q(7,4);check(f'cell{i}:evaluation_beyond_right',e>=hi)
  norm=norms[str(e)];lhs=arb(5)**A((lo-2)/2)*norm;rhs=H*A((1+c-c*lo)/(1+lo));ratio=lhs/rhs;gap=lhs-rhs
  saved=comp['cells'][i];prod=own['seven_cells'][i];floor=Q(saved['strict_ratio_floor'])
  check(f'cell{i}:saved_endpoints',Q(saved['left'])==Q(prod['left'])==lo and Q(saved['right'])==Q(prod['right'])==hi and Q(saved['norm_evaluation_at'])==Q(prod['norm_evaluation_at'])==e)
  check(f'cell{i}:strict_gap',rhs>0 and gap>0 and ratio>A(floor)>1)
  check(f'cell{i}:saved_ratio',ratio.overlaps(arb(saved['ratio'])) and ratio.overlaps(arb(prod['ratio'])))
  check(f'cell{i}:saved_gap',gap.overlaps(arb(saved['gap'])) and gap.overlaps(arb(prod['gap'])))
  check(f'cell{i}:saved_positive_verdicts',saved['excluded'] and prod['excluded'])
  cells.append({'left':str(lo),'right':str(hi),'evaluation_at':str(e),'ratio':ratio.str(100),'strict_floor':str(floor),'gap':gap.str(100)})
 floor=min(Q(z['strict_floor']) for z in cells)
 check('minimum_strict_floor',floor==Q(pars['minimum_ratio_floor'])==Q(comp['minimum_strict_ratio_floor']))
 check('whole_interval_coverage',len(cells)==7 and Q(cells[0]['left'])==0 and Q(cells[-1]['right'])==cap and all(cells[i]['right']==cells[i+1]['left'] for i in range(6)))
 for z in sources:check('unchanged:'+z['local'],sha(B/z['local'])==z['sha256'])
 result={'utc':now(),'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'candidate':own['candidate'],'origin_terms_retained':retained,'origin_strain_exact':str(strain),'origin_slope_exact':str(a0),'origin_slope_margin_exact':str(a0-(5*c-4)),'s_maximizer':star.str(100),'H_max':H.str(100),'energy_rows':energyrows,'cells':cells,'minimum_strict_ratio_floor':str(floor),'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'elapsed_seconds':time.monotonic()-start,'new_field_integration':False,'foreign_code_executed':False,'L2_distance_used':False,'complete_upper_norm':False,'verdict':'CONFIRMED conditional candidate015 seven-cell FW-T-DYADIC-Y-v1 exclusion, retaining all actual inverse, origin, canonical velocity, low realization, input hyperplane, fixed partition and absorption hypotheses. Exact finite source/energy/cell replay only. No profile nonexistence or existence closure.'}
 with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],'CHECKS',len(checks),'SECONDS',result['elapsed_seconds'],'SHA',sha(B/'verification/result.json'))
 print('minimum strict ratio',floor,'origin retained',retained)
if __name__=='__main__':main()

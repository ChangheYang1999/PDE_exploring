from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import gzip, json, sys, time
from flint import arb, ctx, fmpq as Q
ROOT=Path(__file__).resolve().parents[3]; B=ROOT/'research/candidate024_weak_peer'; PEER=ROOT.parent/'c1-t4/research'
sys.set_int_max_str_digits(0);ctx.prec=2048
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator

def main():
 start=time.monotonic();target=B/'verification/result.json';assert not target.exists()
 name='C1-N1-024-rulem32-legqs25';raw=ROOT/f'research/candidate_audits/data/{name}/quot013_legqs25_m9to15_gpu_m32_exact.json'
 objective_path=ROOT/'research/candidate024_holdout/verification/objective_for_weak.json';objective=json.loads(objective_path.read_text())
 ownpaths=[B/'verification/PREPARE.json',raw,objective_path,ROOT/'research/candidate024_holdout/PROOF.md',ROOT/'research/candidate024_peer/verification/result.json',ROOT/'research/candidate024_shape_peer/verification/result.json',raw.parent/'MANIFEST.json',B/'PROOF.md',Path(__file__)]
 for n,K in [(19,1800)]:
  p=ROOT/f'research/scaled_factored_weak/verification/{name}_n{n:03d}_K{K:05d}.json';ownpaths.append(p)
  for rel,h in json.loads(p.read_text())['inputs'].items():
   q=ROOT/rel;assert sha(q)==h;ownpaths.append(q)
 for rel,h in objective['inputs'].items():
  p=ROOT/rel;assert sha(p)==h;ownpaths.append(p)
 known={sha(p):p for p in ownpaths};frozen={};bindings={}
 prior=json.loads((ROOT/'research/candidate021_weak_peer/verification/result.json').read_text())
 for rel,e in prior['frozen_or_retained_sources'].items():
  if not e['gzip'] and sha(ROOT/rel)==e['sha256']:known[e['sha256']]=ROOT/rel
 assert sha(B/'PROOF.md')==json.loads((B/'verification/PREPARE.json').read_text())['proof_sha256']
 def freeze(p,expected=None):
  p=Path(p);blob=p.read_bytes();h=sha256(blob).hexdigest();assert expected is None or expected==h,(str(p),h,expected)
  if h in known:dest=known[h];compressed=False;assert sha(dest)==h
  else:
   dest=B/'source'/p.relative_to(PEER);compressed=len(blob)>1000000
   if compressed:dest=dest.with_name(dest.name+'.gz')
   dest.parent.mkdir(parents=True,exist_ok=True);stored=gzip.compress(blob,mtime=0) if compressed else blob
   if dest.exists():assert dest.read_bytes()==stored
   else:
    with dest.open('xb') as f:f.write(stored)
   if not compressed:known[h]=dest
  frozen[str(dest.relative_to(ROOT))]={'original':str(p),'sha256':h,'stored_sha256':sha(dest),'gzip':compressed};bindings[str(p)]=True
  return json.loads(blob) if p.suffix=='.json' else None
 checks={'raw_identity':sha(raw)==objective['raw_sha256']=='3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d','registered_before_snapshot':datetime.fromisoformat(json.loads((ROOT/'research/candidate024_holdout/verification/result.json').read_text())['registered_public_utc'])<datetime.fromisoformat(json.loads((raw.parent/'MANIFEST.json').read_text())['created_utc'])}
 rows=[]
 for n,K in [(19,1800)]:
  tag=f'{n}_{K}';peerpath=PEER/f'candidate024_weak/verification/n{n}_K{K}.json';peer=freeze(peerpath)
  assert sha(peerpath)==json.loads((B/'verification/PREPARE.json').read_text())['target_peer_result']
  for p,h in peer['inputs'].items():freeze(p,h)
  own=json.loads((ROOT/f'research/scaled_factored_weak/verification/{name}_n{n:03d}_K{K:05d}.json').read_text())
  checks[tag+'_identity']=peer['candidate']==own['candidate']==name and (peer['n'],peer['K'])==(own['n'],own['K'])==(n,K) and peer['source_sha256']==own['raw_sha256']==sha(raw)
  checked=[r for r in objective['probe_rows'] if (r['n'],r['K'])==(n,K)]
  checks[tag+'_registered_holdout']=len(checked)==1 and checked[0]['outside_span'] and [n,K] in json.loads((ROOT/'research/heldout_probe_register/verification/register.json').read_text())['pairs'] and own['probe_objective_status']=='HELD_OUT: outside audited objective span'
  for key in ['pairing','pairing_by_parts','M2','C2','M','C','D','radius']:checks[tag+'_'+key]=arb(peer[key]).overlaps(arb(own[key]))
  I,Ip,M2,C2,M,C,D=(arb(peer[k]) for k in ['pairing','pairing_by_parts','M2','C2','M','C','D'])
  checks[tag+'_scalar_identities']=I.overlaps(Ip) and M2>0 and C2>0 and M>0 and C>0 and M2.sqrt().overlaps(M) and C2.sqrt().overlaps(C) and (M+C).overlaps(D)
  H=Q(own['H_upper_exact']);floor=Q(own['strict_lower_exact'])
  checks[tag+'_same_H_floor']=Q(peer['H_upper_exact'])==H and Q(peer['strict_lower_exact'])==floor and H>0 and floor>Q(25,54684)
  A,Dk=2*K+1,2*K+4;aa=Dk*(K+3);bb=(K+2)*A+(K+1)*Dk;cc=K*A;disc=bb*bb-4*aa*cc;assert disc>0
  roots=[(bb-arb(disc).sqrt())/(2*aa),(bb+arb(disc).sqrt())/(2*aa)];angular=ar(Q(K,K+2))
  amplitudes=[abs(t**K*(1-t)**2*(A-Dk*t)) for t in roots]+[n*angular**K*(1-angular)**2]
  grad=peer['gradient_certificate'];own_grad=own['gradient_certificate']
  checks[tag+'_gradient_polynomial']=grad['quadratic_coefficients']==[aa,-bb,cc] and grad['discriminant']==disc and grad['complete_critical_point_check']
  checks[tag+'_gradient_global']=all(0<t and t<1 for t in roots) and all(v<ar(H) for v in amplitudes) and all(v.overlaps(arb(w)) for v,w in zip(amplitudes,grad['amplitude_caps'],strict=True)) and all(v.overlaps(arb(w)) for v,w in zip(amplitudes,[own_grad['amplitudes'][1],own_grad['amplitudes'][0],own_grad['amplitudes'][2]],strict=True))
  checks[tag+'_gradient_roots']=all(t.overlaps(arb(v)) for t,v in zip(roots,grad['roots'],strict=True)) and all((1-t).overlaps(arb(v)) for t,v in zip(roots,list(reversed(own_grad['radial_roots'])),strict=True))
  radius=2*abs(I)/(D+(D*D+4*ar(H)*abs(I)).sqrt())
  checks[tag+'_root']=radius.overlaps(arb(own['radius'])) and radius.overlaps(arb(peer['radius'])) and ar(floor)<radius
  counts={};minbits=1000000;minimum_b=None;denominator_records=[]
  for key,factor in [('M_moments',1),('C_moments',4),('direct_moments',1),('parts_moments',1)]:
   our={int(r['ell']):r for r in own[key]};theirs={int(r['label'].split(':')[-1]):r for r in peer[key]}
   checks[tag+'_'+key+'_indices']=set(our)==set(theirs)
   for ell,p in theirs.items():
    o=our[ell];prefix=f'{tag}_{key}_{ell}';b=Q(p['b']);minimum_b=b if minimum_b is None else min(minimum_b,b)
    checks[prefix+'_endpoint']=b>-1 and b==Q(o['b']) and p['L']+1==o['m']
    if p.get('exact_zero',False):
     checks[prefix+'_zero']=arb(o['integral']).is_zero();continue
    minbits=min(minbits,p['accuracy_bits'],o['relative_accuracy_bits'])
    checks[prefix+'_crt']=p['exact_CRT_replay'] and o['exact_decomposition_replayed'] and p['accuracy_bits']>150 and o['relative_accuracy_bits']>150
    checks[prefix+'_integral']=arb(p['value']).overlaps(factor*arb(o['integral']))
    op=dict(o['factors']);pp=p['denominator_powers']
    checks[prefix+'_denominator']=len(pp)==2 and all(isinstance(k,int) and k>=0 for k in pp) and set(op)<={'624'} and pp[1]==0 and all(isinstance(k,int) and k>0 for k in op.values())
    denominator_records.append({'kind':key,'ell':ell,'own_factors':o['factors'],'peer_powers':pp,'identical_powers':pp==[op.get('624',0),op.get('2499',0)]})
    checks[prefix+'_pole_checks']=all(z['direct_overlap'] and z['recurrence_accuracy_bits']>150 and z['direct_accuracy_bits']>150 for vv in o['pole_power_checks'].values() for z in vv)
   counts[key]=len(theirs)
  expected_fixtures=[([0,0],3,Q(-1,3)),([1,0],2,Q(1,5)),([3,0],5,Q(-3,7)),([0,2],4,Q(2,7)),([2,1],3,Q(7,3)),([2,3],6,Q(-2,5))]
  checks[tag+'_fixtures']=len(peer['fixtures'])==6
  for i,(r,(powers,L,b)) in enumerate(zip(peer['fixtures'],expected_fixtures,strict=True)):
   checks[f'{tag}_fixture_{i}']=r['denominator_powers']==powers and r['L']==L and Q(r['b'])==b and r['expanded_localization_overlap'] and r['exact_CRT_replay'] and r['accuracy_bits']>150
  freeze(PEER/'new_successor_weak/code/check.py')
  rational_source=(PEER/'candidate024_weak/code/rational.py').read_text()
  checks[tag+'_two_pole_class']='SCALES = (Q(624), Q(2499))' in rational_source
  checks[tag+'_actual_R25_only_moments']=all(all(r.get('exact_zero',False) or r['denominator_powers'][1]==0 for r in peer[key]) and any(not r.get('exact_zero',False) and r['denominator_powers'][0]>0 for r in peer[key]) for key in ['M_moments','C_moments','direct_moments','parts_moments'])
  checks[tag+'_moment_counts']=counts=={'M_moments':16,'C_moments':15,'direct_moments':16,'parts_moments':16}
  checks[tag+'_peer_flags']=peer['R1_full_fields_exact'] and all(peer['actual_candidate_point_checks'].values()) and len(peer['actual_candidate_point_checks'])==6 and all(peer['comparisons'].values()) and peer['exceeds_original_graded_ceiling'] and own['whole_plane'] and own['all_background_modes_retained']
  rows.append({'n':n,'K':K,'strict_floor':str(floor),'radius_recomputed':radius.str(100),'H_upper_exact':str(H),'minimum_endpoint_b':str(minimum_b),'minimum_group_accuracy_bits':minbits,'complete_group_counts':counts,'denominator_representations':denominator_records,'nonidentical_denominator_count':sum(not d['identical_powers'] for d in denominator_records),'peer_result_sha256':sha(peerpath),'peer_runtime_seconds':peer['elapsed_seconds']})
 shape=json.loads((ROOT/'research/candidate024_shape_peer/verification/result.json').read_text());checks['independent_shape_acceptance']=shape['raw_sha256']==sha(raw) and shape['potential_dimension']==shape['density_dimension']==2174 and all(shape['checks'].values())
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for local,d in frozen.items():assert sha(ROOT/local)==d['stored_sha256']
 output={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'rows':rows,'checks':checks,'comparison_count':len(checks)+len(bindings),'peer_input_bindings':bindings,'frozen_or_retained_sources':frozen,'own_inputs':{str(p.relative_to(ROOT)):sha(p) for p in ownpaths},'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-344 (19,1800) complete weak distance through T4 independent polar and direct hypergeometric path; registered objective scope342/independent427; point343/independent428 and sectors have separate certificates'}
 with target.open('x') as f:json.dump(output,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bindings),'bindings',sha(target),'seconds',output['elapsed_seconds'])
if __name__=='__main__':main()

from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import gzip, json, sys, time
from flint import arb, ctx, fmpq as Q
ROOT=Path(__file__).resolve().parents[3]; B=ROOT/'research/candidate019_weak_peer'; PEER=ROOT.parent/'c1-t4/research'
sys.set_int_max_str_digits(0);ctx.prec=2048
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator

def main():
 start=time.monotonic();target=B/'verification/result.json';assert not target.exists()
 name='C1-N1-019-legqs50-cont12';raw=ROOT/f'research/candidate_audits/data/{name}/quot013_legqs50_cont12_cpu_m16_exact.json'
 objective_path=ROOT/'research/candidate019_holdout/verification/result.json';objective=json.loads(objective_path.read_text())
 ownpaths=[raw,objective_path,ROOT/'research/candidate019_holdout/PROOF.md',ROOT/'research/candidate019_point_peer/verification/result.json',B/'PROOF.md',Path(__file__)]
 for n,K in [(19,1800)]:
  p=ROOT/f'research/scaled50_factored_weak/verification/{name}_n{n:03d}_K{K:05d}.json';ownpaths.append(p)
  for rel,h in json.loads(p.read_text())['inputs'].items():
   q=ROOT/rel;assert sha(q)==h;ownpaths.append(q)
 for rel,h in objective['inputs'].items():
  p=ROOT/rel;assert sha(p)==h;ownpaths.append(p)
 known={sha(p):p for p in ownpaths};frozen={};bindings={}
 def freeze(p,expected=None):
  p=Path(p);blob=p.read_bytes();h=sha256(blob).hexdigest();assert expected is None or expected==h,(str(p),h,expected)
  if h in known:dest=known[h];compressed=False
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
 checks={'raw_identity':sha(raw)==objective['raw_sha256']=='ca0fffafe2aa7ea3c6049e0b5a83651113451087027b0783800c046ae170d419','registered_before_snapshot':datetime.fromisoformat(objective['registration_utc'])<datetime.fromisoformat(objective['snapshot_utc'])}
 rows=[]
 for n,K in [(19,1800)]:
  tag=f'{n}_{K}';peerpath=PEER/f'candidate019_weak/verification/n{n}_K{K}.json';peer=freeze(peerpath)
  for p,h in peer['inputs'].items():freeze(p,h)
  own=json.loads((ROOT/f'research/scaled50_factored_weak/verification/{name}_n{n:03d}_K{K:05d}.json').read_text())
  checks[tag+'_identity']=peer['candidate']==own['candidate']==name and (peer['n'],peer['K'])==(own['n'],own['K'])==(n,K) and peer['source_sha256']==own['raw_sha256']==sha(raw)
  checked=[r for r in objective['probe_rows'] if (r['n'],r['K'])==(n,K)]
  checks[tag+'_registered_holdout']=len(checked)==1 and checked[0]['outside_span'] and checked[0]['member_of_25_register'] and own['probe_objective_status']=='HELD_OUT: outside audited objective span'
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
  counts={};minbits=1000000;minimum_b=None
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
    checks[prefix+'_denominator']=p['denominator_powers'][1]==0
   counts[key]=len(theirs)
  priorpath=ROOT/'research/candidate017_weak19_peer/verification/result.json';prior=json.loads(priorpath.read_text());ownpaths.append(priorpath)
  priorfile=ROOT/'research/candidate017_weak19_peer/source/candidate017_weak/verification/n19_K1800.json';priorpeer=json.loads(priorfile.read_text());ownpaths.append(priorfile)
  assert sha(priorfile)==prior['rows'][0]['peer_result_sha256']
  for local,item in prior['frozen_or_retained_sources'].items():
   pp=ROOT/local;assert sha(pp)==item['stored_sha256'];ownpaths.append(pp)
  oldprefix=str(PEER/'candidate017_weak');newprefix=str(PEER/'candidate019_weak')
  for suffix in ['/code/polar.py','/code/rational.py']:
   assert priorpeer['inputs'][oldprefix+suffix]==peer['inputs'][newprefix+suffix]
  legacy=str(PEER/'weak_probe_audit/code/reproduce.py');assert priorpeer['inputs'][legacy]==peer['inputs'][legacy]
  oldcode=(ROOT/'research/candidate017_weak19_peer/source/candidate017_weak/code/check.py').read_text();newcode=(PEER/'candidate019_weak/code/check.py').read_text()
  preflight="    for relative in ['PROOF.md', 'code/polar.py', 'code/rational.py',\n                     'code/C_SYMMETRY.md', 'source/N4_PROOF.md',\n                     'source/N4_moments_PROOF.md', 'source/N4_weak.py']:\n        assert (B / relative).is_file(), relative\n"
  expected=oldcode.replace('t4_polar017','t4_polar019').replace('data/candidate017.json','data/candidate019.json').replace('7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114','ca0fffafe2aa7ea3c6049e0b5a83651113451087027b0783800c046ae170d419').replace('    ctx.prec = args.bits\n',preflight+'    ctx.prec = args.bits\n')
  checks[tag+'_complete_backend_identity']=expected==newcode and not peer['fixtures']
  checks[tag+'_fixtures']=len(priorpeer['fixtures'])==4 and all(r['expanded_localization_overlap'] and r['exact_CRT_replay'] and r['accuracy_bits']>150 for r in priorpeer['fixtures'])
  ownpaths.append(B/'verification/DEVELOPMENT_CORRECTION.json')
  checks[tag+'_peer_flags']=peer['R1_full_fields_exact'] and all(peer['actual_candidate_point_checks'].values()) and len(peer['actual_candidate_point_checks'])==6 and all(peer['comparisons'].values()) and peer['exceeds_original_graded_ceiling'] and own['whole_plane'] and own['all_background_modes_retained']
  rows.append({'n':n,'K':K,'strict_floor':str(floor),'radius_recomputed':radius.str(100),'H_upper_exact':str(H),'minimum_endpoint_b':str(minimum_b),'minimum_group_accuracy_bits':minbits,'complete_group_counts':counts,'peer_result_sha256':sha(peerpath),'peer_runtime_seconds':peer['elapsed_seconds']})
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for local,d in frozen.items():assert sha(ROOT/local)==d['stored_sha256']
 output={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'rows':rows,'checks':checks,'comparison_count':len(checks)+len(bindings),'peer_input_bindings':bindings,'frozen_or_retained_sources':frozen,'own_inputs':{str(p.relative_to(ROOT)):sha(p) for p in ownpaths},'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-282 (19,1800) complete weak distance through T4 independent polar and direct hypergeometric path; registered objective scope280; point279 and sectors have separate certificates'}
 with target.open('x') as f:json.dump(output,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bindings),'bindings',sha(target),'seconds',output['elapsed_seconds'])
if __name__=='__main__':main()

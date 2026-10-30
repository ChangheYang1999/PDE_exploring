"""Accept the independent full polar density-difference certificate."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from collections import defaultdict
import gzip, json, sys, time
from flint import fmpq as Q, arb, ctx
R=Path(__file__).resolve().parents[3];B=R/'research/candidate021_reference_peer';P=R.parent/'c1-t4/research';ctx.prec=2048;sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
def rows(d):
 out={}
 for g in d['generators']:
  key=g['j'],g['m'],tuple(g['spec']);assert key not in out;out[key]=Q(g['coef'])
 return out

def main():
 start=time.monotonic();target=B/'verification/result.json';assert not target.exists()
 op=R/'research/reference_difference/verification/C1-N1-021-heldin14-legqs25p50_minus_C1-N1-020-legqs25p50-quot013_2048_complete_v3.json';own=json.loads(op.read_text())
 ap=R/'research/candidate020_weak_peer/verification/result.json';parent=json.loads(ap.read_text())
 ownpaths=[Path(__file__),B/'PROOF.md',B/'verification/PREPARE.json',op,ap]
 for rel,h in own['inputs'].items():p=R/rel;assert sha(p)==h;ownpaths.append(p)
 for rel,h in own['postprocessing']['complete_source_bindings'].items():p=R/rel;assert sha(p)==h;ownpaths.append(p)
 for rel,h in parent['own_inputs'].items():p=R/rel;assert sha(p)==h;ownpaths.append(p)
 known={sha(p):p for p in ownpaths};frozen={};bindings={}
 for priorpath in [ap,R/'research/candidate021_weak_peer/verification/result.json']:
  prior=json.loads(priorpath.read_text())
  for rel,e in prior['frozen_or_retained_sources'].items():
   assert sha(R/rel)==e['stored_sha256']
   if not e['gzip']:known[e['sha256']]=R/rel
 def freeze(p,expected=None):
  p=Path(p);blob=p.read_bytes();h=sha256(blob).hexdigest();assert expected is None or h==expected,(p,h,expected)
  if h in known:dest=known[h];compressed=False
  else:
   dest=B/'source'/p.relative_to(P);compressed=len(blob)>1000000
   if compressed:dest=dest.with_name(dest.name+'.gz')
   dest.parent.mkdir(parents=True,exist_ok=True);stored=gzip.compress(blob,mtime=0) if compressed else blob
   if dest.exists():assert dest.read_bytes()==stored
   else:
    with dest.open('xb') as f:f.write(stored)
   if not compressed:known[h]=dest
  frozen[str(dest.relative_to(R))]={'original':str(p),'sha256':h,'stored_sha256':sha(dest),'gzip':compressed};bindings[str(p)]=h
  return json.loads(blob) if p.suffix=='.json' else None
 peerpath=P/'candidate021_difference/verification/result.json';peer=freeze(peerpath,'5ec953335a564483d210e86b9165478f3bf33fa80d10c07df4c3f779139baba7')
 for p,h in peer['inputs'].items():freeze(p,h)
 exact=freeze(P/'candidate021_difference/data/exact_difference.json',peer['exact_difference_sha256'])
 checks={};prep=json.loads((B/'verification/PREPARE.json').read_text())
 checks['proof_before_code']=sha(B/'PROOF.md')==prep['proof_sha256'] and sha(P/'candidate021_difference/PROOF.md')==prep['peer_general_proof_sha256']
 rawpaths=[R/'research/candidate_audits/data/C1-N1-020-legqs25p50-quot013/quot013_legqs25p50_m9to15_cpu_m16_exact.json',R/'research/candidate_audits/data/C1-N1-021-heldin14-legqs25p50/legqs25p50_heldin14_gpu_m16_exact.json']
 raw=[json.loads(p.read_text()) for p in rawpaths];old,new=map(rows,raw);diff={k:new.get(k,Q(0))-old.get(k,Q(0)) for k in set(old)|set(new)};diff={k:v for k,v in diff.items() if v}
 ownrawpath=R/'research/reference_difference/data/C1-N1-021-heldin14-legqs25p50_minus_C1-N1-020-legqs25p50-quot013.json';ownraw=json.loads(ownrawpath.read_text())
 checks['all_exact_difference_coefficients']=rows(exact)==rows(ownraw)==diff and len(diff)==peer['nonzero_generator_differences']==own['difference_nonzero_generator_count']==2286
 checks['raw_identities']=sha(rawpaths[0])==own['parent_raw_sha256']=='bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf' and sha(rawpaths[1])==own['successor_raw_sha256']=='c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8'
 c=Q(4076476460239181,2251799813685248);delta=1-1/c;checks['c_delta']=all(Q(d['cl_exact'])==c for d in [*raw,exact,ownraw]) and Q(2,5)<delta<Q(1,2)
 prefix=defaultdict(Q)
 for (j,m,spec),a in diff.items():
  q=spec[3] if spec[0] in ['legq','legqs'] else 0
  if j<4 and q==0:prefix[j,m]+=a
 checks['complete_P']=all(v==0 for v in prefix.values()) and peer['prefix_P_verified'] and own['potential_prefix_equal'] and all(r['equal'] and not r['difference'] for r in own['prefix'])
 checks['all_peer_prefix_sums']=[[j,m,str(v)] for (j,m),v in sorted(prefix.items())]==peer['prefix_checks']
 checks['endpoint_flags']=all(Q(r[3])==0 and r[0] in ['rho','psi'] and 1<=r[1]<=4 for r in peer['endpoint_checks']) and all(Q(r['value'])==0 for r in own['endpoint_checks'])
 ourrho={(r['ell'],r['n']) for r in own['endpoint_checks'] if r['field']=='rho'};peerrho={(r[1],r[2]) for r in peer['endpoint_checks'] if r[0]=='rho'};checks['density_endpoint_indices']=ourrho==peerrho
 checks['density_count']=own['fields']['rho']['component_count']==peer['density_terms']==226 and peer['stream_terms']==226
 ourpoints={(r['x'],r['y'],k):v for r in own['point_checks']['points'] for k,v in r['fields'].items()};peerpoints={(r['x'],r['y'],r['field']):r for r in peer['point_checks']};checks['point_indices']=set(ourpoints)==set(peerpoints) and len(ourpoints)==9
 for key,v in ourpoints.items():
  w=peerpoints[key];checks['point_'+str(key)]=arb(v['compact']).overlaps(arb(w['value'])) and arb(v['Cartesian']).overlaps(arb(w['value'])) and v['accuracy_bits']>150 and w['overlap']
 ours={g['ell_sum']:g for g in own['norm']['groups']};theirs={g['ell_sum']:g for g in peer['groups']};checks['group_indices']=set(ours)==set(theirs) and len(ours)==own['norm']['group_count']==peer['group_count']==14
 checks['ordered_pairs']=own['norm']['ordered_pairs']==peer['ordered_pairs']==834
 total=arb(0);minbits=1000000;representations=[]
 for ell,p in theirs.items():
  o=ours[ell];b=Q(p['b']);tag=f'group_{ell}'
  checks[tag+'_endpoint']=b==Q(o['b'])==ell*delta/2-3+p['endpoint_v_order'] and b>-1 and p['endpoint_v_order']==o['endpoint_v_order']
  checks[tag+'_integral']=arb(p['value']).is_finite() and arb(p['value']).overlaps(arb(o['integral_ball'])) and p['exact_CRT_replay'] and p['peer_overlap']
  minbits=min(minbits,p['accuracy_bits'],o['integral_accuracy_bits']);checks[tag+'_accuracy']=minbits>150
  vals=[Q(v) for v in p['numerator_after_stripping']];h=sha256();h.update(str(len(vals)).encode()+b'\n')
  for q in vals:h.update(str(q).encode()+b'\n')
  samepowers=o['powers']==[0,p['denominator_powers'][0],p['denominator_powers'][1],0];samehash=h.hexdigest()==o['numerator_v_sha256']
  representations.append({'ell_sum':ell,'denominator_powers_match':samepowers,'numerator_hash_matches':samehash})
  checks[tag+'_exact_representation']=samepowers and samehash and len(vals)-1==o['degree_v']
  total+=arb(p['value'])
 square=arb.pi()/2*total;norm=square.sqrt();tau=Q(peer['tau_upper_exact']);floor=Q(next(r for r in parent['rows'] if (r['n'],r['K'])==(19,1800))['strict_floor'])
 checks['sum_identity']=total.overlaps(arb(peer['sum'])) and total.overlaps(arb(own['norm']['sum_ball']))
 checks['norm_identity']=square>0 and square.overlaps(arb(peer['square'])) and square.overlaps(arb(own['norm']['square_ball'])) and norm.overlaps(arb(peer['norm'])) and norm.overlaps(arb(own['norm']['norm_ball']))
 checks['tau']=tau==Q(own['norm']['tau_upper_exact'])==Q(3674626624859862044982741129,500000000000000000000000000000) and norm<ar(tau)
 checks['parent_floor']=floor==Q(231921834680339,125000000000000000) and own['parent_evidence_record_sha256']==sha(ap)
 ourscreen={r['ceiling_id']:r for r in own['screens']};screens=[]
 for p in peer['screens']:
  o=ourscreen[p['ceiling_id']];b=Q(p['b']);margin=floor-b;passed=bool(square<=ar(margin**2));failed=bool(square>ar(margin**2))
  checks['screen_'+p['ceiling_id']]=b==Q(o['b']) and floor==Q(p['parent_floor'])==Q(o['strict_parent_distance_floor']) and margin==Q(p['margin'])==Q(o['d_minus_b']) and margin>0 and failed and not passed and p['certified_square_above_margin_squared'] and not p['screen_passed'] and not o['certified_square_below_margin_squared'] and not o['tau_below_margin']
  screens.append({'id':p['ceiling_id'],'ceiling':str(b),'margin':str(margin),'screen_failed':failed})
 checks['three_screens']=len(screens)==3
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for rel,e in frozen.items():assert sha(R/rel)==e['stored_sha256']
 out={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'peer_input_bindings':bindings,'frozen_or_retained_sources':frozen,'own_inputs':{str(p.relative_to(R)):sha(p) for p in ownpaths+rawpaths+[ownrawpath]},'coefficient_count':len(diff),'prefix_sum_count':len(prefix),'endpoint_count':len(peer['endpoint_checks']),'point_count':len(ourpoints),'group_count':len(ours),'ordered_pairs':834,'representations':representations,'minimum_group_accuracy_bits':minbits,'norm':norm.str(100),'tau_upper_exact':str(tau),'screens':screens,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-313 general compatibility via T4-393 and complete actual021-minus020 norm via T4-394; all three sufficient transfer screens fail; no new exclusion'}
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bindings),'bindings',sha(target),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

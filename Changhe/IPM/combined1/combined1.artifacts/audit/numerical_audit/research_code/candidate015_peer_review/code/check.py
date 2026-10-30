from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,sys,time,os,signal
from flint import arb,ctx,fmpq as Q
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/candidate015_peer_review';PEER=ROOT.parent/'c1-t4/research'
sys.set_int_max_str_digits(0);ctx.prec=2048
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
def canonical(d):return {tuple(k):Q(v) for k,v in zip(d['order'],d['coefficients'],strict=True) if Q(v)}
def main():
 start=time.monotonic();name='C1-N1-015-pairQ-quot013';dest=BASE/'verification/result.json';assert not dest.exists()
 ownpoint=ROOT/f'research/generator_sector_audit/verification/{name}_direct.json'
 ownweak=ROOT/f'research/scaled_factored_weak/verification/{name}_n019_K00600.json'
 owncan=ROOT/f'research/candidate_audits/data/{name}/canonical.json'
 ownraw=ROOT/f'research/candidate_audits/data/{name}/quot013_pairQ_cpu_m16_exact.json'
 retained=[ownpoint,ownweak,owncan,ownraw,ROOT/'research/scaled_factored_weak/PROOF.md',ROOT/'research/scaled_factored_weak/code/check_candidates.py',ROOT/'research/candidate015_holdout/verification/result.json',ROOT/'research/candidate_audits/reviews/T4_014/source/localized_probe_audit/code/reproduce.py']
 known={sha(p):p for p in retained if p.exists()};bindings={};frozen={}
 def freeze(p,expected=None):
  p=Path(p);b=p.read_bytes();h=sha256(b).hexdigest();assert expected is None or h==expected,(p,h,expected)
  if h in known:
   target=known[h];compressed=False
  else:
   rel=p.relative_to(PEER);compressed=len(b)>1000000;target=BASE/'source'/str(rel)
   if compressed:target=target.with_name(target.name+'.gz')
   target.parent.mkdir(parents=True,exist_ok=True)
   packed=gzip.compress(b,compresslevel=6,mtime=0) if compressed else b
   if target.exists():assert target.read_bytes()==packed
   else:
    with target.open('xb') as f:f.write(packed)
   if not compressed:known[h]=target
  local=str(target.relative_to(ROOT));frozen[local]={'original':str(p),'sha256':h,'stored_sha256':sha(target),'gzip':compressed}
  bindings[str(p)]=True
  return json.loads(b) if p.suffix=='.json' else None
 pp=PEER/'candidate015_point';pr=freeze(pp/'verification/results.json');point=json.loads(ownpoint.read_text())
 for rel,h in pr['inputs'].items():freeze(pp/rel,h)
 checks={'same_candidate':pr['candidate']==point['candidate']==name,'same_point':pr['point']==point['point'],'same_c':Q(pr['c_exact'])==Q(point['c_exact']),'raw_identity':sha(ownraw)==point['generator_sha256']}
 for k,z in pr['fields'].items():checks['point_'+k]=arb(z).overlaps(arb(point['fields'][k]))
 for k in ['uniform_graded_upper','uniform_graded_gap']:checks[k]=arb(pr[k]).overlaps(arb(point[k]))
 checks['graded_positive']=arb(pr['uniform_graded_gap'])>0
 assert len(pr['ball_exclusions'])==len(point['ball_exclusions'])==6
 for row,old in zip(pr['ball_exclusions'],point['ball_exclusions'],strict=True):
  key=row['framework'];checks[key+'_framework']=key==old['framework'];checks[key+'_s']=Q(row['s'])==Q(old['s'])
  if old.get('radius_squared') is not None:checks[key+'_radius']=Q(row['radius_squared'])==Q(old['radius_squared'])
  else:checks[key+'_radius']=Q(row['radius'])==Q(old['radius'])
  for k in ['upper','gap','necessary_H2s_radius_lower']:
   if k in old:checks[key+'_'+k]=arb(row[k]).overlaps(arb(old[k]))
  checks[key+'_positive']=arb(row['gap'])>0
 checks['peer_point_flags']=all(pr['field_overlaps'].values())
 theta=(arb(point['fields']['gradient_norm'])-arb(point['fields']['rho_y']))/2
 checks['theta']=theta.overlaps(arb(pr['theta']))
 checks['theta_gap']=(theta-ar(Q(point['c_exact'])-1)).overlaps(arb(pr['theta_minus_c_minus_one']))
 wr=PEER/'candidate015_heldout';pa=freeze(wr/'verification/ACCEPTANCE.json');peer=freeze(wr/'verification/015_n19_k600.json');own=json.loads(ownweak.read_text())
 for p,h in pa['inputs'].items():freeze(p,h)
 scalar={'source_sha256':PEER/'new_successor_weak/data/015/canonical.json','build_sha256':PEER/'new_successor_weak/verification/015_build.json','proof_sha256':wr/'PROOF.md','code_sha256':wr/'code/check.py','helper_sha256':PEER/'localized_probe_audit/code/reproduce.py','probe_sha256':wr/'data/probe_19_600.json'}
 for k,p in scalar.items():freeze(p,peer[k])
 peercan=freeze(scalar['source_sha256'],peer['source_sha256']);owncanon=json.loads(owncan.read_text())
 checks['exact_canonical_maps']=canonical(peercan)==canonical(owncanon)
 checks['canonical_raw_identity']=peercan['source_sha256']==owncanon['source_sha256']==sha(ownraw)==own['raw_sha256']
 checks['weak_n_K']=peer['angular_mode']==own['n']==19 and peer['radial_power']==own['K']==600
 for k in ['pairing','pairing_by_parts','M','C','D']:checks['weak_'+k]=arb(peer[k]).overlaps(arb(own[k]))
 checks['M2']=arb(peer['normM2']).overlaps(arb(own['M2']));checks['C2']=arb(peer['normC2']).overlaps(arb(own['C2']))
 checks['direct_parts']=peer['direct_parts_overlap'] and own['direct_parts_overlap']
 H=Q(own['H_upper_exact']);checks['finer_H']=all(arb(v)<ar(H) for v in peer['sup_certificate']['amplitude_caps'])
 I=abs(arb(peer['pairing']));D=arb(peer['D']);radius=2*I/(D+(D*D+4*ar(H)*I).sqrt())
 checks['root_overlap']=radius.overlaps(arb(own['radius'])) and radius.overlaps(arb(pa['radius_with_peer_H']))
 checks['strict_floor']=ar(own['strict_lower_exact'])<radius and Q(own['strict_lower_exact'])==Q(pa['peer_strict_floor_independently_verified'])
 checks['all_endpoints_integrable']=Q(peer['minimum_endpoint_exponent'])>-1
 checks['peer_weak_flags']=all(pa['checks'].values())
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 owninputs={str(p.relative_to(ROOT)):sha(p) for p in retained if p.exists()}
 owninputs.update({str(p.relative_to(ROOT)):sha(p) for p in [Path(__file__),BASE/'PROOF.md']})
 for local,item in frozen.items():assert sha(ROOT/local)==item['stored_sha256']
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'checks':checks,'comparison_count':len(checks)+len(bindings),'peer_input_bindings':bindings,'frozen_or_retained_sources':frozen,'own_inputs':owninputs,'weak_strict_floor':own['strict_lower_exact'],'weak_root_with_same_H':radius.str(100),'point_residual':pr['fields']['residual'],'uniform_graded_gap':pr['uniform_graded_gap'],'peer_point_runtime_seconds':pr['elapsed_seconds'],'peer_weak_runtime_seconds':peer['elapsed_seconds'],'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-234 and the n19K600 part of N4-237 after T4-299 and T4-298 independent reproductions'}
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bindings),'bindings',sha(dest),'seconds',out['elapsed_seconds'])
if __name__=='__main__':main()

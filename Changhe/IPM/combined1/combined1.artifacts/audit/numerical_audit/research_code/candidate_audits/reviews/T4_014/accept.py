from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,sys,os,signal,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[4];PEER=ROOT.parent/'c1-t4/research'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
sys.set_int_max_str_digits(0);ctx.prec=2048
name='C1-N1-014-pairB-from007';PB=ROOT/'research/candidate_audits/reviews/T4_014';WB=ROOT/'research/successor_factored_weak/reviews/T4_014'
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def fraction_interval(z):return ar(z['lower']).union(ar(z['upper']))
def canonical(d):return {tuple(k):Q(v) for k,v in zip(d['order'],d['coefficients'],strict=True)}
owncanon=ROOT/f'research/candidate_audits/data/{name}/canonical.json';ownpoint=ROOT/f'research/candidate_audits/verification/{name}_point.json';ownunif=ROOT/f'research/candidate_audits/verification/{name}_uniform_point.json';ownext=ROOT/f'research/candidate_audits/verification/{name}_point_extensions.json';ownweak=ROOT/f'research/successor_factored_weak/verification/{name}_n021_K00522.json'
known={sha(p):p for p in [owncanon,ownpoint,ownunif,ownext,ownweak,ROOT/'research/successor_factored_weak/PROOF.md',ROOT/'research/successor_factored_weak/code/check.py']}
frozen={}
def freeze(p):
 p=Path(p);h=sha(p)
 if h in known:return str(known[h].relative_to(ROOT)),h
 rel=p.relative_to(PEER);target=PB/'source'/rel;target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists():assert target.read_bytes()==p.read_bytes()
 else:target.write_bytes(p.read_bytes())
 assert sha(target)==h;known[h]=target
 return str(target.relative_to(ROOT)),h
def bind(paths):
 flags={}
 for p,h in paths.items():
  flags[str(p)]=sha(p)==h;assert flags[str(p)],str(p)
  rel,digest=freeze(p);frozen[rel]=digest
 return flags
def state(pid):
 try:return Path(f'/proc/{pid}/stat').read_text().split()[2]
 except FileNotFoundError:return None
start=time.monotonic();begin=datetime.now(timezone.utc).isoformat();stopped=[]
try:
 pid=286853;s=state(pid)
 if s and s not in ['T','Z','X']:os.kill(pid,signal.SIGSTOP);stopped.append(pid)
 if s:
  f=Path(f'/proc/{pid}/task/{pid}/children')
  for txt in f.read_text().split() if f.exists() else []:
   ch=int(txt);s=state(ch)
   if s and s not in ['T','Z','X']:os.kill(ch,signal.SIGSTOP);stopped.append(ch)
 pointroot=PEER/'candidate014_point';prpath=pointroot/'verification/results.json';pr=json.loads(prpath.read_text());prep_path=pointroot/'verification/preparation.json';prep=json.loads(prep_path.read_text())
 point=json.loads(ownpoint.read_text());uniform=json.loads(ownunif.read_text());ext=json.loads(ownext.read_text());can=json.loads(owncanon.read_text())
 flags=bind({pointroot/p:h for p,h in pr['inputs'].items()});flags.update(bind(prep['inputs']))
 for p in [prpath,prep_path,pointroot/'verification/MANIFEST.json',pointroot/'verification/manifest.json',pointroot/'verification/run_schema_failure.log']:
  rel,h=freeze(p);frozen[rel]=h
 pcpath=PEER/'new_successor_weak/data/014/canonical.json';pccan=json.loads(pcpath.read_text())
 checks={'same_candidate':pr['candidate']==point['candidate']==name,'same_point':pr['point']==point['point'], 'same_c':Q(pr['c_exact'])==Q(can['cl'])==Q(pccan['cl']),'exact_canonical_coefficients':canonical(can)==canonical(pccan) and len(canonical(can))==1922,'raw_source_binding':pccan['source_sha256']==point['generator_sha256']==sha(pointroot/'data/candidate014.json'),'canonical_source_binding':sha(owncanon)==point['canonical_sha256'],'prepared_schema_binding':prep['output_sha256']==sha(pointroot/'source/N4_result.json'),'preparation_flags':prep['exact_canonical_maps_equal'] and prep['source_binding_verified']}
 for k,z in pr['fields'].items():checks['field_'+k]=arb(z).overlaps(arb(point['fields'][k]))
 for k in ['uniform_graded_upper','uniform_graded_gap']:checks[k]=arb(pr[k]).overlaps(arb(uniform[k]))
 checks['uniform_positive']=arb(pr['uniform_graded_gap'])>0
 for row,old in zip(pr['ball_exclusions'][:5],point['ball_exclusions'],strict=True):
  assert row['framework']==old['framework']
  for a,b in [('upper','necessary_upper'),('gap','gap'),('necessary_H2s_radius_lower','necessary_H2s_radius_lower')]:checks[row['framework']+'_'+a]=arb(row[a]).overlaps(arb(old[b]))
  checks[row['framework']+'_positive']=arb(row['gap'])>0
 for row,old in zip(pr['ball_exclusions'][5:],uniform['sharp_boxes'],strict=True):
  assert row['framework']==old['framework']
  checks[row['framework']+'_upper']=arb(row['upper']).overlaps(arb(old['point_upper']))
  checks[row['framework']+'_gap']=arb(row['gap']).overlaps(arb(old['gap'])) and arb(row['gap'])>0
 for k,uk,ek in [('theta','point_theta','theta_at_point'),('theta_minus_c_minus_one','point_theta_minus_c_minus_one','theta_minus_c_minus_1')]:
  checks[k]=arb(pr[k]).overlaps(arb(uniform[uk])) and arb(pr[k]).overlaps(fraction_interval(ext[ek]))
 checks['all_peer_flags']=all(pr['field_overlaps'].values()) and pr['all_extension_intervals_overlap']
 assert all(checks.values()),checks
 out={'utc':datetime.now(timezone.utc).isoformat(),'peer_result_sha256':sha(prpath),'own_point_sha256':sha(ownpoint),'own_uniform_sha256':sha(ownunif),'own_extensions_sha256':sha(ownext),'acceptance_code_sha256':sha(__file__),'review_sha256':sha(PB/'REVIEW.md'),'input_bindings':flags,'frozen_or_retained_sources':dict(frozen),'checks':checks,'comparison_count':len(flags)+len(checks),'peer_runtime_seconds':pr['elapsed_seconds'],'verdict':'CONFIRMED N4-213 after T4-279 independent polar reproduction'}
 with (PB/'ACCEPTANCE.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('point',out['comparison_count'],sha(PB/'ACCEPTANCE.json'),flush=True)
 wr=PEER/'candidate014_weak';ap=wr/'verification/ACCEPTANCE.json';pa=json.loads(ap.read_text());wp=wr/'verification/014_n21_k522.json';peer=json.loads(wp.read_text());own=json.loads(ownweak.read_text())
 flags=bind(pa['inputs'])
 scalar_paths={'source_sha256':pcpath,'build_sha256':PEER/'new_successor_weak/verification/014_build.json','proof_sha256':wr/'PROOF.md','code_sha256':wr/'code/check.py','helper_sha256':PEER/'localized_probe_audit/code/reproduce.py','probe_sha256':wr/'data/probe_21_522.json'}
 flags.update(bind({p:peer[k] for k,p in scalar_paths.items()}));rel,h=freeze(ap);frozen[rel]=h
 checks={k:arb(peer[k]).overlaps(arb(own[k])) for k in ['pairing','pairing_by_parts','M','C','D','radius']}
 checks.update({'M2':arb(peer['normM2']).overlaps(arb(own['M2'])),'C2':arb(peer['normC2']).overlaps(arb(own['C2'])),'same_H':Q(peer['sup_certificate']['H_upper_exact'])==Q(own['H_upper_exact']),'direct_parts':peer['direct_parts_overlap'] and own['direct_parts_overlap'],'both_strict_floors':ar(own['strict_lower_exact'])<arb(peer['radius']) and ar(own['strict_lower_exact'])<arb(own['radius']),'all_endpoints_integrable':Q(peer['minimum_endpoint_exponent'])>-1,'n21_K522':peer['angular_mode']==21 and peer['radial_power']==522,'design_provenance':own['probe_was_in_candidate014_optimization'] and pa['peer_probe_was_in_objective'],'canonical_binding':peer['source_sha256']==sha(pcpath) and own['canonical_sha256']==sha(owncanon),'all_peer_checks':all(pa['checks'].values()) and pa['same_H']})
 assert all(checks.values()),checks
 out={'utc':datetime.now(timezone.utc).isoformat(),'peer_result_sha256':sha(wp),'peer_acceptance_sha256':sha(ap),'own_result_sha256':sha(ownweak),'point_source_acceptance_sha256':sha(PB/'ACCEPTANCE.json'),'acceptance_code_sha256':sha(__file__),'review_sha256':sha(WB/'REVIEW.md'),'input_bindings':flags,'frozen_or_retained_sources':frozen,'checks':checks,'comparison_count':len(flags)+len(checks),'strict_lower_exact':own['strict_lower_exact'],'peer_runtime_seconds':peer['elapsed_seconds'],'verdict':'CONFIRMED N4-214 after T4-280 independent polar reproduction'}
 with (WB/'ACCEPTANCE.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('weak',out['comparison_count'],sha(WB/'ACCEPTANCE.json'),flush=True)
finally:
 for pid in reversed(stopped):
  try:os.kill(pid,signal.SIGCONT)
  except ProcessLookupError:pass
 pause={'began_utc':begin,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'stopped_and_resumed_pids':stopped}
 with (PB/'pause.json').open('x') as f:json.dump(pause,f,indent=2);f.write('\n')

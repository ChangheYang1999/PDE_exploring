from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
import json,time
from flint import arb,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_low_order_forcing_peer';sha=lambda p:sha256(p.read_bytes()).hexdigest()
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def main():
 start=time.monotonic();ctx.prec=1024;inputs={};checks={};target=B/'verification/result.json';assert not target.exists()
 def bind(p,h=None):
  p=Path(p);x=sha(p);assert h is None or x==h,(str(p),x,h);inputs[str(p.relative_to(R))]=x;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 proof_first=read(B/'verification/PROOF_FIRST.json');assert not proof_first['comparison_code_written']
 bind(B/'PROOF.md',proof_first['proof_sha256']);bind(Path(__file__))
 manifest=read(B/'source/MANIFEST.json',proof_first['manifest_sha256'])
 for z in manifest['files'].values():bind(R/z['local'],z['sha256'])
 def peer(rel):return read(R/manifest['files'][rel]['local'],manifest['files'][rel]['sha256'])
 p=peer('verification/result.json');own=read(R/'research/candidate016_low_order_forcing/verification/result.json',proof_first['own_result_sha256'])
 for rel,h in own['inputs'].items():bind(R/rel,h)
 pm=peer('data/manifest.json');att=peer('verification/PEER_SOURCE_ATTESTATION.json')
 checks['all_peer_manifest_files_bound']=all(manifest['files'][rel]['sha256']==h for rel,h in pm['inputs'].items())
 checks['result_code_proof_manifest_bound']=p['checker_sha256']==manifest['files']['code/check.py']['sha256'] and p['proof_sha256']==manifest['files']['PROOF.md']['sha256'] and p['manifest_sha256']==manifest['files']['data/manifest.json']['sha256']
 checks['current_59_attestation_matches_own']=att['hashes']==own['inputs'] and len(att['hashes'])==59 and att['all_59_hashes_match'] and att['peer_result_sha256']==proof_first['own_result_sha256']==p['peer_sha256']
 checks['recorded318_assertions']=len(p['checks'])==p['check_count']==318 and p['precision_bits']==1024 and p['verdict'].startswith('CONFIRMED') and not p['candidate_integrals_repeated'] and not p['foreign_code_executed']
 acc=peer('source/G1_acceptance.json');partial=peer('source/N4_partial.json');comp=peer('data/components.json');parameters=peer('data/parameters.json')
 checks['exact_candidate']=all(z['candidate']=='C1-N1-016-legqs25-quot013' and z['raw_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42' for z in [own,acc,partial,comp,parameters]) and Q(partial['cl_exact'])==Q(4076476460239181,2251799813685248)
 lower={};norms={}
 for label in ['G0','G1']:
  a=acc['norms'][label];z=p['norm_consistency'][label];ell=Q(comp['components'][label]['lower_exact']);hi=Q(comp['components'][label]['upper_exact']);lower[label]=ell
  checks[label+'_strict_endpoints']=ell==Q(z['accepted_lower'])==Q(a['accepted_lower_exact']) and hi==Q(z['accepted_upper'])==Q(a['accepted_upper_exact']) and ar(ell)<arb(a['own_lower_ball']).lower() and ar(hi)>arb(a['own_upper_ball']).upper()
  checks[label+'_norm_overlap']=arb(z['from_saved_moments']).overlaps(arb(a['own_lower_ball'])) and arb(z['from_saved_moments']).overlaps(arb(a['own_upper_ball']))
  n=partial['norms'][label];summed=sum((arb(g['integral_ball']) for g in n['groups']),arb(0));norm=(arb.pi()*summed/2).sqrt()
  checks[label+'_saved_sum']=norm.overlaps(arb(z['from_saved_moments'])) and len(n['groups'])==z['groups']==31
  checks[label+'_recorded_accuracy']=min(g['integral_accuracy_bits'] for g in n['groups'])==z['minimum_recorded_accuracy_bits']
  norms[label]={'from_saved_moments':norm.str(100),'accepted_lower_exact':str(ell),'accepted_upper_exact':str(hi)}
 ours={z['framework']:z for z in own['instances']};checks['ten_instances']=len(p['instances'])==len(ours)==10;rows=[]
 for z in p['instances']:
  name=z['framework'];o=ours[name];w1,w2=z['weights'];threshold=Q(z['threshold_exact']);square=w1*lower['G1']**2+w2*lower['G0']**2;energy=ar(square).sqrt();factor=energy/ar(threshold)
  checks[name+'_exact_parameters']=z['kind']==o['kind'] and Q(z['s_exact'])==Q(o['s_exact'])>=0 and threshold==Q(o['sufficient_threshold_exact'])>0 and z['weights']==o['weights'] and w1>0 and w2>0
  checks[name+'_exact_square']=square==Q(z['square_exact'])==Q(o['low_order_square_exact'])
  checks[name+'_energy_overlap']=energy.overlaps(arb(z['forcing'])) and energy.overlaps(arb(o['forcing_lower_comparison']['ball']))
  checks[name+'_factor_overlap']=factor.overlaps(arb(z['factor'])) and factor.overlaps(arb(o['threshold_ratio_lower_comparison']['ball']))
  checks[name+'_strict_lower']=Q(z['strict_forcing_lower_exact'])==Q(o['forcing_lower_comparison']['strict_lower_exact']) and ar(z['strict_forcing_lower_exact'])<energy and Q(z['strict_integer_factor'])==Q(o['threshold_ratio_lower_comparison']['strict_lower_exact']) and factor>ar(z['strict_integer_factor'])>1
  rows.append({'framework':name,'square_exact':str(square),'forcing':energy.str(100),'ratio':factor.str(100),'strict_factor':z['strict_integer_factor']})
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for rel,h in inputs.items():assert sha(R/rel)==h
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'candidate':own['candidate'],'raw_sha256':own['raw_sha256'],'precision_bits':ctx.prec,'checks':checks,'check_count':len(checks),'inputs':inputs,'peer_file_bindings':manifest['files'],'norm_consistency':norms,'instances':rows,'peer_result_sha256':manifest['files']['verification/result.json']['sha256'],'candidate_integrals_repeated':False,'foreign_code_executed':False,'verdict':'CONFIRMED T4-451 reciprocal inequality and all ten sufficient scalar forcing failures; no correction-distance, dyadic, H equality or fractional upper implication'}
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('PASS',len(checks),'checks',len(inputs),'inputs',sha(target),out['utc'],out['elapsed_seconds'])
if __name__=='__main__':main()

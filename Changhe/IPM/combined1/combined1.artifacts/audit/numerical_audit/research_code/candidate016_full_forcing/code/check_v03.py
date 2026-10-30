"""Finite own component assembly; refuses incomplete all-four acceptance."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from hashlib import sha256
import json, time
from flint import arb, ctx
R=Path(__file__).resolve().parents[3]; B=R/'research/candidate016_full_forcing'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(x):
 q=Q(x);return arb(q.numerator)/q.denominator
def outward(x,digits=12):
 scale=10**digits
 lm,le=x.lower().man_exp();um,ue=x.upper().man_exp()
 lq=Q(int(lm))*Q(2)**int(le)*scale;uq=Q(int(um))*Q(2)**int(ue)*scale
 lo=Q(lq.numerator//lq.denominator-1,scale)
 hi=Q(-(-uq.numerator//uq.denominator)+1,scale)
 assert ar(lo)<x.lower() and x.upper()<ar(hi)
 return {'ball':x.str(100),'strict_lower_exact':str(lo),'strict_upper_exact':str(hi)}
def main():
 start=time.monotonic();ctx.prec=2048;target=B/'verification/result_v03.json';assert not target.exists();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);v=sha(p);assert h is None or v==h,(str(p),v,h);inputs[str(p.relative_to(R))]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE_v02.json');assert prep['proof_written_before_code']
 for p,h in prep['inputs'].items():bind(R/p,h)
 bind(Path(__file__))
 bind(B/'ENDPOINT_PROOF_v03.md')
 complete=read(R/prep['future_required_result'])
 assert complete['verdict'].startswith('CONFIRMED') and all(complete['checks'].values()) and set(complete['norms'])=={'G0','rF','G1','P2'}
 for p,h in complete['inputs'].items():bind(R/p,h)
 fullpath=R/'research/candidate016_scaled_norm_peer/source/N4_norms_complete_v01.json';own=read(fullpath)
 assert own['status'].startswith('COMPLETE OWN') and set(own['norms'])=={'G0','rF','G1','P2'}
 for p,h in own['inputs'].items():bind(R/p,h)
 checks['all_four_independent_components_accepted']=True
 pars=read(B/'source/parameters.json')
 checks['same_candidate_and_raw']=complete['candidate']==own['candidate']==pars['candidate']=='C1-N1-016-legqs25-quot013' and complete['raw_sha256']==own['raw_sha256']==pars['raw_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 checks['same_c_and_delta']=own['cl_exact']=='4076476460239181/2251799813685248' and own['delta_exact']=='1824676646553933/4076476460239181'
 comp={}
 for label in ['G0','G1','P2','rF']:
  a=complete['norms'][label];z=own['norms'][label];lo=Q(a['accepted_lower_exact']);hi=Q(a['accepted_upper_exact'])
  assert 0<lo<hi and z['status'].startswith('COMPLETE')
  checks[label+'_accepted_outward_endpoints']=ar(lo)<arb(z['norm_lower_ball']).lower() and arb(z['norm_upper_ball']).upper()<ar(hi) and a['whole_plane_no_quadrature'] and a['peer_40digit_endpoint_balls_contain_own']
  comp[label]=(ar(lo),ar(hi))
 prior=read(R/'research/candidate016_registered_assembly/verification/result.json');assert all(prior['checks'].values())
 for p,h in prior['inputs'].items():bind(R/p,h)
 baselinebase=R/'research/registered_norm_assembly';baseline=read(baselinebase/'verification/result.json')
 for p,h in baseline['inputs'].items():bind(baselinebase/p,h)
 checks['baseline007_raw']=baseline['generator_sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
 assert len(baseline['instances'])==5
 def energy(w1,w2):return tuple((comp['P2'][i]**2+w1*comp['G1'][i]**2+w2*comp['G0'][i]**2).sqrt() for i in [0,1])
 star=energy(16384,262144);e2=(star[0],(star[1]**2+ar(Q(262144*20,21))*comp['rF'][1]**2).sqrt())
 rows=[]
 for name,ss,tt,unused in pars['Ns']+[pars['legacy_X3']]:
  s=Q(ss);thr=Q(tt);assert 0<s<Q(1,34) and thr>0
  kind='X3' if name==pars['legacy_X3'][0] else 'Ns';p=next(z for z in prior['instances'] if z['framework']==name)
  assert Q(p['s_exact'])==s and Q(p['threshold_exact'])==thr and p['kind']==kind
  lower=(1-ar(34*s))*star[0];ratio=lower/ar(thr)
  assert ratio>1
  rows.append({'framework':name,'kind':kind,'s_exact':str(s),'threshold_exact':str(thr),'forcing_lower_comparison':outward(lower),'ratio_lower_comparison':outward(ratio,0),'sufficient_test_fails':True,'fractional_upper':'OPEN; Q3 unavailable'})
 checks['four_Ns_and_legacy_parameters_and_failures']=True
 ordering=[]
 for spec,label in zip(pars['XSW'],['sharp','sharpw','bL7_5','bL1','trans'],strict=True):
  name,ss,w1,w2,cw,tt=spec;s=Q(ss);thr=Q(tt);assert 0<1-Q(48,25)*s and thr>0
  old=next(z for z in prior['instances'] if z['framework']==name);base=next(z for z in baseline['instances'] if z['label']==label)
  assert Q(old['s_exact'])==Q(base['s_exact'])==s and old['weights']==[base['w1'],base['w2']]==[w1,w2]
  assert Q(old['threshold_exact'])==Q(base['threshold_exact'])==thr and Q(old['Cw_exact'])==Q(base['Cw_exact'])==Q(cw)
  ew=energy(w1,w2);lower=(1-ar(Q(48,25)*s))*ew[0];ratio=lower/ar(thr);assert ratio>1
  lowerdata=outward(lower);baseupper=Q(base['upper_comparison']['strict_upper_exact'])
  assert arb(base['upper_comparison']['ball']).upper()<ar(baseupper)
  gap=ar(Q(lowerdata['strict_lower_exact'])-baseupper);strict=gap>0
  ordering.append({'framework':name,'baseline007_upper_exact':str(baseupper),'candidate016_lower_exact':lowerdata['strict_lower_exact'],'lower_minus_upper':outward(gap),'strict_007_less_than_016':bool(strict),'verdict':'CONFIRMED these two weighted forcing norms only' if strict else 'OPEN from these enclosures'})
  rows.append({'framework':name,'kind':'XSW','s_exact':str(s),'weights':[w1,w2],'Cw_exact':str(Q(cw)),'threshold_exact':str(thr),'E_lower':outward(ew[0]),'E_upper':outward(ew[1]),'forcing_lower_comparison':lowerdata,'ratio_lower_comparison':outward(ratio,0),'sufficient_test_fails':True,'fractional_upper':'OPEN; Q3 unavailable'})
 checks['five_XSW_identical_parameters_and_failures']=True
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for p,h in inputs.items():assert sha(R/p)==h
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'candidate':pars['candidate'],'raw_sha256':pars['raw_sha256'],'inputs':inputs,'checks':checks,'check_count':len(checks),'component_acceptance':'CONFIRMED complete own all-four production and peer comparison','E_star':{'lower':outward(star[0]),'upper':outward(star[1])},'E2_with_Hardy_proxy':{'lower':outward(e2[0]),'upper':outward(e2[1]),'actual_H_computed':False,'H_upper_source':'H<=rF by parity and circle Poincare'},'instances':rows,'XSW_pair_ordering':ordering,'all_five_pair_orderings_strict':all(z['strict_007_less_than_016'] for z in ordering),'integral_recomputed_here':False,'foreign_code_executed':False,'limitations':['No actual H value or Q3','No fractional norm upper bound for016','No cross-candidate distance ordering','No dyadic exclusion','No inverse or existence closure','N4-347 imported-fixture provenance qualification retained','Saved peer40-digit endpoint containing balls only'],'verdict':'CONFIRMED complete-component scalar forcing assembly; pairwise XSW orderings only as individually recorded; no correction-distance or existence conclusion'}
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('PASS',len(checks),'checks',len(inputs),'inputs',sha(target),out['utc'],out['elapsed_seconds'],flush=True)
 for row in rows:print(row['framework'],row['forcing_lower_comparison']['ball'],row['ratio_lower_comparison']['strict_lower_exact'])
 for z in ordering:print(z['framework'],z['strict_007_less_than_016'],z['lower_minus_upper']['ball'])
if __name__=='__main__':main()

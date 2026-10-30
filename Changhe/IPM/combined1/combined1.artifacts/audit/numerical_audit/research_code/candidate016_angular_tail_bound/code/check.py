"""Complete angular-tail bound from own source-certified mode groups and full rF."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
from flint import fmpq as Q,arb,ctx
import argparse,json,os,sys,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_angular_tail_bound';HB=R/'research/candidate016_mode_hardy'
CID='C1-N1-016-legqs25-quot013';RAW='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
sys.set_int_max_str_digits(0)
def aq(q):
 q=Q(q);return arb(q.numerator)/arb(q.denominator)
def endpoint(x,upper=False):
 m,e=(x.upper() if upper else x.lower()).man_exp();m,e=int(m),int(e)
 return Q(m*2**e) if e>=0 else Q(m,2**(-e))
def floorq(x,digits=30):
 q=endpoint(x);d=10**digits;out=Q((q*d).floor()-1,d);assert aq(out)<x.lower();return out

def ceilq(x,digits=30):
 q=endpoint(x,True);d=10**digits;out=Q((q*d).ceil()+1,d);assert x.upper()<aq(out);return out

def contains(a,b):return a.lower()<=b.lower() and b.upper()<=a.upper()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prefix',type=int,required=True);ap.add_argument('--version',required=True);ap.add_argument('--multimode',action='store_true');args=ap.parse_args()
 assert args.prefix in range(1,320,2) and args.version.isalnum();ctx.prec=4096;started=time.monotonic();inputs={};checks={}
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);got=sha(p);rel=str(p.relative_to(R));assert h is None or got==h,(rel,h,got);assert rel not in inputs or inputs[rel]==got;inputs[rel]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 first=read(B/'verification/PROOF_FIRST.json');ck('proof_before_code',not first['checker_exists']);bind(B/'PROOF.md',first['proof_sha256']);bind(B/'REPLAY_SCOPE_v02.md');bind(Path(__file__))
 bind(HB/'PROOF.md','c467c5f54204ba8135d36b5352de630689273a049ab5fefeeb7aeb93cefb8675')
 bind(HB/'code/check.py','9ac1413f4133dad1eb4ccf33c1b58c2bdb8a1eb75122fe131942a5348ed494d0')
 acceptance=read(R/'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json','a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc')
 ck('complete392accepted',all(acceptance['checks'].values()) and acceptance['candidate']==CID and acceptance['raw_sha256']==RAW)
 for rel,h in acceptance['inputs'].items():bind(R/rel,h)
 prod=read(R/'research/candidate016_scaled_norm_peer/source/N4_norms_partial_v01.json','7e7b51a4473936d0ee9803fb12df45851ab42a10c0974787feed7c6728e0a58c')
 for rel,h in prod['inputs'].items():bind(R/rel,h)
 full=prod['fields']['D0_0'];components=full['components'];modes=sorted({c['key'][2] for c in components})
 ck('complete160sinemodes',full['component_count']==len(components)==1360 and modes==list(range(1,320,2)) and all(c['key'][1]=='s' for c in components))
 ck('all_declared_modes_in_prefix',args.prefix in modes)
 peer=read(HB/'source/N3_hardy.json');peerby={v['n']:v for v in peer['modes']}
 delta=Q(1824676646553933,4076476460239181);Qsum=arb(0);Ssum=arb(0);records=[];all_lower=Q(0);all_upper=Q(0)
 for n in range(1,args.prefix+1,2):
  path=HB/f'verification/mode_{n:03d}.json';row=read(path)
  for rel,h in row['inputs'].items():bind(R/rel,h)
  ck(f'n{n}_identity',row['status']=='CONFIRMED complete own mode integral' and row['candidate']==CID and row['raw_sha256']==RAW and row['n']==n and row['F_representation_sha256']==full['representation_sha256'])
  branches=[c for c in components if c['key'][2]==n];ells=[c['key'][0] for c in branches]
  ck(f'n{n}_complete_paircount',row['component_count']==len(branches) and row['ordered_pair_count']==len(branches)**2)
  ck(f'n{n}_complete_groups',row['group_count']==len(row['groups']) and [g['ell_sum'] for g in row['groups']]==sorted({e+f for e in ells for f in ells}))
  balls=[]
  for j,g in enumerate(row['groups']):
   e=Q(g['b']);dec=g['decomposition'];factors=[[str(scale),power] for scale,power in zip([99,624,2499,9999],g['powers']) if power]
   ck(f'n{n}_g{j}_integrable',g['endpoint_v_order']>=0 and e==g['ell_sum']*delta/2-4+g['endpoint_v_order'] and e>-1)
   ck(f'n{n}_g{j}_positive_poles',all(p>=0 for p in g['powers']) and dec['factors']==factors and dec['denominator_degree']==sum(g['powers']))
   ck(f'n{n}_g{j}_source_integral',dec['exact_reconstruction'] and Q(dec['b'])==e and g['integral_accuracy_bits']>150 and len(g['numerator_v_sha256'])==64)
   ball=arb(g['integral_ball']);ck(f'n{n}_g{j}_valid_ball',ball.is_finite() and ball.rel_accuracy_bits()>150);balls.append(ball)
  radius=sum((x.rad() for x in balls),arb(0));q=sum(balls,arb(0))*arb.pi()/2;saved=arb(row['rF_n_sq'])
  ck(f'n{n}_absolute_radius',radius.upper()<aq(Q(1,10**100)))
  ck(f'n{n}_positive_replay',q>0 and q.rel_accuracy_bits()>150)
  ck(f'n{n}_production_consistency',q.overlaps(saved) and q.sqrt().overlaps(arb(row['rF_n'])) and (q.sqrt()/n).overlaps(arb(row['H_n_UB'])))
  ck(f'n{n}_peer_display_contains_replay',contains(arb(peerby[n]['rF_n_sq']),q) and contains(arb(peerby[n]['rF_n']),q.sqrt()) and contains(arb(peerby[n]['H_n_UB']),q.sqrt()/n))
  Qsum+=q;Ssum+=q/n**2;lo,hi=endpoint(q),endpoint(q,True);all_lower+=lo;all_upper+=hi
  records.append({'n':n,'record':str(path.relative_to(R)),'sha256':sha(path),'group_count':len(balls),'q_replay_ball':q.str(650),'q_lower_exact':str(lo),'q_upper_exact':str(hi),'sum_absolute_radii_ball':radius.str(650),'accuracy_bits':q.rel_accuracy_bits(),'source_final_contains_replay':contains(saved,q),'replay_contains_source_final':contains(q,saved)})
 L={k:Q(v['accepted_lower_exact']) for k,v in acceptance['norms'].items()};U={k:Q(v['accepted_upper_exact']) for k,v in acceptance['norms'].items()}
 ck('positive_full_rF_interval',0<L['rF']<U['rF'])
 total_lower,total_upper=L['rF']**2,U['rF']**2
 ck('prefix_not_larger_than_total',all_lower<total_upper)
 if args.prefix<319:
  m=args.prefix+2;tail_upper=total_upper-all_lower
  positive_upper=total_upper/(m*m)+sum((Q(rec['q_upper_exact'])*(Q(1,rec['n']**2)-Q(1,m*m)) for rec in records),Q(0))
  split_upper=sum((Q(rec['q_upper_exact'])/rec['n']**2 for rec in records),Q(0))+tail_upper/(m*m)
  ck('nonnegative_full_tail_upper',tail_upper>0)
  ck('positive_coefficient_formula_tighter',positive_upper<=split_upper)
  upper=min(positive_upper,split_upper);tail_lower=max(Q(0),total_lower-all_upper)
 else:
  m=None;tail_upper=tail_lower=Q(0);positive_upper=split_upper=upper=sum((Q(rec['q_upper_exact'])/rec['n']**2 for rec in records),Q(0))
  ck('complete_rF_consistency',Qsum.sqrt().overlaps(arb(acceptance['norms']['rF']['own_lower_ball'])))
 lower=sum((Q(rec['q_lower_exact'])/rec['n']**2 for rec in records),Q(0))
 ck('positive_M2_bounds',0<lower<upper)
 archive=read(R/'research/candidate016_pairing_archive/verification/result.json','c3e148aaab94ed6b50920f114c80260cb7f0061756398a90f6f444fa6b0367c6')
 dual=read(R/'research/candidate016_dual_lower/verification/result.json','e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa')
 cross=read(R/'research/candidate016_solenoidal_upper/verification/result.json','e97891e271837201e3f4a0d18f96732825238604cbad65fc8b31923e36463603')
 for d in [archive,dual,cross]:
  ck('accepted:'+d['utc'],all(d['checks'].values()))
  for rel,h in d['inputs'].items():bind(R/rel,h)
 jfloor=sum((Q(r['strict_floor_exact']) for r in archive['rows'] if r['kind']=='cross'),Q(0));hfloor2=sum((Q(r['strict_floor_exact'])**2 for r in archive['rows'] if r['kind']=='dual'),Q(0))
 selected_modes=[1,3]
 if args.multimode:
  multi=read(R/'research/candidate016_multimode_dual_cross/verification/result.json');ck('multimode_complete',all(multi['checks'].values()) and len(multi['modes'])==16 and multi['candidate']==CID and multi['raw_sha256']==RAW)
  for rel,h in multi['inputs'].items():bind(R/rel,h)
  for row in multi['modes']:bind(R/row['record'],row['sha256'])
  jnew=Q(multi['selected_improvement_sum_strict_lower_exact']);hnew=Q(multi['selected_H_lower_square_exact'])
  ck('multimode_not_weaker',jnew>=jfloor and hnew>=hfloor2);jfloor,hfloor2=jnew,hnew;selected_modes=[row['n'] for row in multi['modes']]
 improved=upper-jfloor
 ck('nontrivial_consistent_improved_upper',0<hfloor2<improved<upper)
 hardupper=ceilq(aq(upper).sqrt());hupper=ceilq(aq(improved).sqrt());hlower=floorq(aq(hfloor2).sqrt())
 loE=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2+Q(20,21)*2**18*hfloor2
 hiE=U['P2']**2+2**14*U['G1']**2+2**18*U['G0']**2+Q(20,21)*2**18*improved
 elower=floorq(aq(loE).sqrt(),12);eupper=ceilq(aq(hiE).sqrt(),12)
 ck('positive_consistent_energy',0<loE<hiE and elower<eupper)
 ck('actual_E2_ordering007_less_than016',elower>Q(dual['baseline007_E2_strict_upper_exact']))
 for rel,h in inputs.items():assert sha(R/rel)==h,rel
 result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':CID,'raw_sha256':RAW,'prefix':args.prefix,'mode_count_replayed':len(records),'complete_field_mode_count':160,'complete_field_component_count':1360,'F_representation_sha256':full['representation_sha256'],'inputs':inputs,'check_count':len(checks),'checks':checks,'modes':records,'Q_prefix_ball':Qsum.str(650),'S_prefix_ball':Ssum.str(650),'full_rF_square_lower_exact':str(total_lower),'full_rF_square_upper_exact':str(total_upper),'tail_rF_square_lower_exact':str(tail_lower),'tail_rF_square_upper_exact':str(tail_upper),'smallest_omitted_mode':m,'M2_lower_exact':str(lower),'M2_upper_exact':str(upper),'split_formula_upper_exact':str(split_upper),'positive_coefficient_formula_upper_exact':str(positive_upper),'plain_H_strict_upper_exact':str(hardupper),'selected_improvement_modes':selected_modes,'selected_improvement_sum_lower_exact':str(jfloor),'H_lower_square_exact':str(hfloor2),'improved_H_square_upper_exact':str(improved),'H_strict_lower_exact':str(hlower),'conditional_improved_H_strict_upper_exact':str(hupper),'E2_lower_square_exact':str(loE),'conditional_E2_upper_square_exact':str(hiE),'E2_strict_lower_exact':str(elower),'conditional_E2_strict_upper_exact':str(eupper),'complete_uncomputed_tail_retained':True,'all160_individual_mode_integrals_replayed':args.prefix==319,'peer_code_executed':False,'new_mode_integrals_performed':False,'elapsed_seconds':time.monotonic()-started,'verdict':'CONFIRMED finite complete-field angular-tail bound from own accepted group certificates. Improved-upper numerical assembly CONDITIONAL on separately accepted Opus review of the divergence-free theorem and this application; no exact H or existence conclusion.'}
 out=B/f'verification/result_{args.version}.json'
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],len(checks),'checks',sha(out),'prefix',args.prefix,'H lower',str(hlower),'H conditional upper',str(hupper),'E2',str(elower),str(eupper),'seconds',result['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

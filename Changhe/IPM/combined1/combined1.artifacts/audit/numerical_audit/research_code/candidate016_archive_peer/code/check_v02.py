"""Reciprocal finite comparison and complete saved-group replay; no peer execution."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from flint import fmpq as Q,arb,ctx
import gzip,json,sys,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_archive_peer';T=R.parent/'c1-t4/research/candidate016_cross_archive_audit'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();qsha=lambda q:sha256(str(Q(q)).encode()).hexdigest()
sys.set_int_max_str_digits(0)
def aq(q):q=Q(q);return arb(q.numerator)/arb(q.denominator)
def contains(a,b):return a.lower()<=b.lower() and b.upper()<=a.upper()
def main():
 ctx.prec=4096;start=time.monotonic();inputs={};external={};checks={}
 def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);got=sha(p);rel=str(p.relative_to(R));assert h is None or got==h,(rel,h,got);assert rel not in inputs or inputs[rel]==got;inputs[rel]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 def ex(p,h):
  p=Path(p);key=str(p.resolve());assert sha(p)==h,(key,h);assert key not in external or external[key]==h;external[key]=h
 first=read(B/'verification/PROOF_FIRST.json');bind(B/'PROOF.md',first['proof_sha256']);bind(Path(__file__));bind(B/'MANIFEST_SCOPE_v02.md');ck('proof_before_checker',not first['checker_exists'])
 mf=read(B/'source/MANIFEST.json',first['manifest_sha256'])
 for name,row in mf['files'].items():bind(B/'source'/name,row['sha256']);ex(row['original'],row['sha256'])
 peer=read(B/'source/T4_result.json');manifest=read(B/'source/T4_manifest.json')
 ck('complete3113peerchecks',peer['check_count']==len(peer['checks'])==len(set(peer['checks']))==3113)
 ck('peerproofcodebinding',peer['proof_sha256']==sha(B/'source/T4_PROOF.md') and peer['checker_sha256']==sha(B/'source/T4_check.py') and peer['manifest_sha256']==sha(B/'source/T4_manifest.json'))
 ck('peernoexecutionclaims',not peer['foreign_code_executed'] and not peer['candidate_moment_integrals_repeated'] and peer['new650digit_groups_independently_resummed'])
 for row in manifest:
  path=T/row['local'];ex(path,row['sha256'])
  if 'decompressed_sha256' in row:
   ck('decompressed:'+row['local'],sha256(gzip.decompress(path.read_bytes())).hexdigest()==row['decompressed_sha256']);ex(row['source'],row['decompressed_sha256'])
  elif row.get('source'):
   if Path(row['source']).is_absolute():ex(row['source'],row['sha256'])
   else:ck('source_label:'+row['local'],row['source']=='own frozen accepted dependency')
 for row in read(B/'source/T4_bindings.json')['rows']:ex(row['source'],row['sha256'])
 archive=read(R/'research/candidate016_pairing_archive/verification/result.json','c3e148aaab94ed6b50920f114c80260cb7f0061756398a90f6f444fa6b0367c6')
 dual=read(R/'research/candidate016_dual_lower/verification/result.json','e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa')
 cross=read(R/'research/candidate016_solenoidal_upper/verification/result.json','e97891e271837201e3f4a0d18f96732825238604cbad65fc8b31923e36463603')
 old=read(R/'research/candidate016_reciprocal_audits/verification/result.json','db9c1fd53efbc78c8de3bb3b5031dce0ca99b26c27d74d09c1024b370d1be35f')
 for d in [archive,dual,cross,old]:
  ck('ownaccepted:'+d['utc'],all(d['checks'].values()))
  for rel,h in d['inputs'].items():bind(R/rel,h)
 by={(v['n'],v['kind']):v for v in archive['rows']};rows=[];lower2=Q(0);improvement=Q(0);groupcount=0
 ck('fourpairings',[(v['n'],v['kind']) for v in peer['rows']]==[(1,'dual'),(1,'cross'),(3,'dual'),(3,'cross')])
 for v in peer['rows']:
  n,kind=v['n'],v['kind'];label=f'{n}_{kind}';a=read(R/f'research/candidate016_solenoidal_upper/verification/mode_{n:03d}.json');d=read(R/f'research/candidate016_dual_lower/verification/mode_{n:03d}.json');source=by[(n,kind)]
  aa=Q(a['a_over_pi_exact']);dd=Q(d['gradient_energy_over_pi_exact'])
  ck(label+'_exact_positive_energy_identity',aa>0 and dd>0 and v['a_over_pi_sha256']==qsha(aa) and v['d_over_pi_sha256']==qsha(dd) and dd==Q(a['old_d_over_pi_exact']))
  ag={r['exponent']:Q(r['value']) for r in a['a_group_integrals_over_pi']};dg={r['exponent']:Q(r['integral_over_pi_exact']) for r in d['gradient_energy_groups']}
  ck(label+'_complete_energy_groups',len(ag)==len(dg)==v['exact_energy_groups']==({1:39,3:43}[n]) and set(ag)==set(dg)=={r['exponent'] for r in v['exact_energy_checks']})
  ck(label+'_exact_energy_sum',sum(ag.values(),Q(0))==aa and sum(dg.values(),Q(0))==dd)
  for i,e in enumerate(v['exact_energy_checks']):ck(label+f'_energy{i}',e['a_sha256']==qsha(ag[e['exponent']]) and e['d_sha256']==qsha(dg[e['exponent']]))
  gs=read(R/source['group_record'],source['group_sha256']);groups=gs['groups'];ck(label+'_allgroups',gs['inputs']==archive['inputs'] and gs['saved_ball_digits']==650 and len(groups)==v['group_count']==len(v['group_metadata'])==source['group_count']==({1:58,3:73}[n]))
  total=arb(0);radii=arb(0)
  for j,(g,p) in enumerate(zip(groups,v['group_metadata'],strict=True)):
   e=Q(g['exponent']);order=g['endpoint_order'];ball=arb(g['integral_ball']);info=g['decomposition']
   ck(label+f'_g{j}_metadata',g['exponent']==p['exponent'] and order==p['order'] and g['numerator_sha256']==p['numerator_sha256'])
   ck(label+f'_g{j}_integrable',order>=0 and e+order>-1 and Q(info['b'])==e+order and info['exact_reconstruction'])
   ck(label+f'_g{j}_positive_poles',all(Q(a) in [99,624,2499,9999] and isinstance(k,int) and k>0 for a,k in info['factors']))
   ck(label+f'_g{j}_ball',ball.is_finite() and ball.rel_accuracy_bits()>150 and contains(arb(p['saved_absolute_radius']),ball.rad()))
   total+=ball;radii+=ball.rad();groupcount+=1
  pairing=total*arb.pi()/2
  ck(label+'_replay_accuracy',pairing.rel_accuracy_bits()>700 and radii.upper()<aq(Q(1,10**250)))
  ck(label+'_peer_displays_contain_replay',contains(arb(v['pairing_from_saved_groups']),pairing) and contains(arb(v['sum_absolute_radii']),radii))
  ck(label+'_own_final_consistency',pairing.overlaps(arb(source['pairing_replayed_ball'])) and contains(arb(source['original_pairing_ball']),pairing) and contains(pairing,arb(source['pairing_full_precision_ball'])))
  ck(label+'_certified_sign',pairing>0 if kind=='dual' else pairing<0)
  val=abs(pairing)/(arb.pi()*aq(dd)).sqrt() if kind=='dual' else pairing**2/(arb.pi()*aq(aa));floor=Q(source['strict_floor_exact'])
  ck(label+'_same_directed_floor',0<floor==Q(v['strict_floor']) and aq(floor)<val.lower() and contains(arb(v['quotient_or_improvement']),val))
  ck(label+'_old_archive_insufficient',arb(v['old_coarse_group_sum']).rad()>1)
  if kind=='dual':lower2+=floor**2
  else:improvement+=floor
  rows.append({'n':n,'kind':kind,'groups':len(groups),'pairing_replay_ball':pairing.str(200),'relative_accuracy_bits':pairing.rel_accuracy_bits(),'strict_floor_exact':str(floor),'energy_group_count':len(ag)})
 ck('all262groups',groupcount==262)
 ck('same_lower_and_improvement',lower2==Q(peer['H_lower_square_exact'])==Q(dual['H_lower_square_exact']) and improvement==Q(peer['improvement_sum_strict_lower_exact'])==Q(cross['improvement_sum_strict_lower_exact']))
 ck('same_Hfloor',Q(peer['H_strict_lower_exact'])==Q(dual['H_strict_lower_exact']) and Q(peer['H_strict_lower_exact'])**2<lower2)
 ck('same_energy_square',Q(peer['E2_lower_square_exact'])==Q(dual['E2_lower_square_exact']))
 lo,hi=Q(peer['E2_strict_lower_exact']),Q(peer['007_E2_strict_upper_exact'])
 ck('actual_energy_order',lo==Q(dual['E2_strict_lower_exact']) and lo**2<Q(peer['E2_lower_square_exact']) and hi==Q(dual['baseline007_E2_strict_upper_exact']) and lo-hi==Q(peer['strict_E2_gap'])>0)
 for rel,h in inputs.items():assert sha(R/rel)==h,rel
 for path,h in external.items():assert sha(path)==h,path
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'external_inputs':external,'check_count':len(checks),'checks':checks,'rows':rows,'H_lower_square_exact':str(lower2),'improvement_sum_strict_lower_exact':str(improvement),'H_strict_lower_exact':peer['H_strict_lower_exact'],'E2_strict_lower_exact':str(lo),'baseline007_E2_strict_upper_exact':str(hi),'strict_E2_gap':str(lo-hi),'peer_code_executed':False,'new_candidate_integrals':False,'verdict':'CONFIRMED reciprocal exact energy identities, complete262-group replay, strict floors and actual identical E2 ordering. Complete moment soundness, source projection and347 fixture scope retained. Numerical improved upper remains a separate acceptance.'}
 with(B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'own',len(external),'external',sha(B/'verification/result.json'),out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

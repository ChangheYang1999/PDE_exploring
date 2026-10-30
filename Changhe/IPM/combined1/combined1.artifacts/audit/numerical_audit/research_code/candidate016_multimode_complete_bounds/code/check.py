"""Exact complete-field assembly from source-certified multimode records."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction
from flint import fmpq as Q,arb,ctx
import argparse,json,os,re,sys,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_multimode_complete_bounds'
MB=R/'research/candidate016_multimode_dual_cross'
CID='C1-N1-016-legqs25-quot013';RAW='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def aq(v):
 v=Q(v);return arb(v.numerator)/arb(v.denominator)
def q(v):
 v=Fraction(v);return Q(v.numerator,v.denominator)
def decinterval(s):
 m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',s);assert m,s
 a,b=q(m[1]),q(m[2]);assert b>0;return a-b,a+b
def roundout(v,digits,up):
 v=Q(v);d=10**digits;return Q((v*d).ceil()+1,d) if up else Q((v*d).floor()-1,d)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tail-version',required=True);ap.add_argument('--version',required=True);a=ap.parse_args()
 assert a.tail_version.isalnum() and a.version.isalnum();start=time.monotonic();ctx.prec=4096;inputs={};checks={}
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 def ck(k,v):
  assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);v=sha(p);key=str(p.relative_to(R));assert h is None or v==h,(key,h,v)
  assert key not in inputs or inputs[key]==v;inputs[key]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 def accepted(j,key):
  ck('accepted:'+key,all(j['checks'].values()))
  for rel,h in j['inputs'].items():bind(R/rel,h)
 first=read(B/'verification/PROOF_FIRST.json');ck('proof_before_checker',not first['checker_exists'])
 bind(B/'PROOF.md',first['proof_sha256']);bind(Path(__file__))
 deps=read(B/'source/dependencies.json',first['dependencies_sha256']);dd={}
 for rel,h in deps.items():
  j=read(R/rel,h);accepted(j,rel);dd[Path(rel).parts[1]]=j
 norms=dd['candidate016_scaled_norm_peer'];old=dd['candidate016_reviewed_upper'];base=dd['negative_norm_forcing_assembly']
 ck('general_reviews_accepted',dd['candidate016_upper_opus_reciprocal']['both_general_Opus_reviews_accepted'])
 ck('old_complete_review',old['general_analytic_review_condition_discharged'] and old['full160_mode_field_covered'])
 multi=read(MB/'verification/result.json');accepted(multi,'multi')
 ck('multimode_identity',multi['candidate']==CID and multi['raw_sha256']==RAW and multi['precision_bits']==4096 and multi['saved_ball_digits']==650)
 ck('sixteen_modes',[r['n'] for r in multi['modes']]==list(range(1,32,2)))
 archive=read(R/'research/candidate016_pairing_archive/verification/result.json','c3e148aaab94ed6b50920f114c80260cb7f0061756398a90f6f444fa6b0367c6');accepted(archive,'archive')
 oldL={r['n']:Q(r['strict_floor_exact']) for r in archive['rows'] if r['kind']=='dual'}
 oldJ={r['n']:Q(r['strict_floor_exact']) for r in archive['rows'] if r['kind']=='cross'}
 L2=Q(0);J=Q(0);trialL2=Q(0);trialJ=Q(0);groupcount=0;records=[]
 for row in multi['modes']:
  n=row['n'];r=read(R/row['record'],row['sha256'])
  for rel,h in r['inputs'].items():bind(R/rel,h)
  ck(f'n{n}_identity',r['n']==n and [g['kind'] for g in r['group_records']]==['dual','cross'])
  d,a0=Q(r['d_over_pi_exact']),Q(r['a_over_pi_exact'])
  ck(f'n{n}_exact_positive_energies',d>0 and a0>0 and d==sum((Q(g['integral_exact']) for g in r['d_groups']),Q(0)) and a0==sum((Q(g['integral_exact']) for g in r['a_groups']),Q(0)))
  vals={}
  for g in r['group_records']:
   kind=g['kind'];v=read(R/g['record'],g['sha256']);groupcount+=len(v['groups'])
   for rel,h in v['inputs'].items():bind(R/rel,h)
   ck(f'n{n}_{kind}_identity',v['n']==n and v['kind']==kind and v['saved_ball_digits']==650 and len(v['groups'])==g['group_count'])
   balls=[]
   for i,c in enumerate(v['groups']):
    b=arb(c['integral_ball']);e=Q(c['exponent'])+c['endpoint_order'];dec=c['decomposition']
    ck(f'n{n}_{kind}_g{i}_endpoint',e>-1 and Q(dec['b'])==e and dec['exact_reconstruction'])
    ck(f'n{n}_{kind}_g{i}_ball',b.is_finite() and b.rel_accuracy_bits()>150 and len(c['numerator_sha256'])==64)
    balls.append(b)
   radius=sum((b.rad() for b in balls),arb(0));v0=sum(balls,arb(0))*arb.pi()/2
   ck(f'n{n}_{kind}_replay',v0.rel_accuracy_bits()>600 and radius.upper()<aq(Q(1,10**200)) and v0.overlaps(arb(g['pairing_ball'])))
   vals[kind]=v0
  quotient=abs(vals['dual'])/(arb.pi()*aq(d)).sqrt();improvement=vals['cross']**2/(arb.pi()*aq(a0))
  lf,jf=Q(r['quotient_strict_lower_exact']),Q(r['improvement_strict_lower_exact'])
  ck(f'n{n}_strict_floors',lf>0 and jf>0 and aq(lf)<quotient.lower() and aq(jf)<improvement.lower())
  sl,sj=max(lf,oldL.get(n,Q(0))),max(jf,oldJ.get(n,Q(0)))
  ck(f'n{n}_selection',sl==Q(r['selected_quotient_strict_lower_exact'])==Q(row['selected_quotient_strict_lower_exact']) and sj==Q(r['selected_improvement_strict_lower_exact'])==Q(row['selected_improvement_strict_lower_exact']))
  trialL2+=lf*lf;trialJ+=jf;L2+=sl*sl;J+=sj;records.append({'n':n,'selected_lower':str(sl),'selected_improvement':str(sj),'record':row['record'],'sha256':row['sha256']})
 ck('exact_trial_totals',trialL2==Q(multi['H_lower_square_exact']) and trialJ==Q(multi['improvement_sum_strict_lower_exact']))
 ck('exact_selected_totals',L2==Q(multi['selected_H_lower_square_exact']) and J==Q(multi['selected_improvement_sum_strict_lower_exact']))
 tail=read(R/f'research/candidate016_angular_tail_bound/verification/result_{a.tail_version}.json');accepted(tail,'tail')
 N=tail['prefix'];ck('complete_tail_identity',tail['candidate']==CID and tail['raw_sha256']==RAW and tail['complete_field_mode_count']==160 and tail['complete_field_component_count']==1360 and tail['complete_uncomputed_tail_retained'])
 ck('complete_prefix',N in range(31,320,2) and [r['n'] for r in tail['modes']]==list(range(1,N+1,2)))
 S=Q(norms['norms']['rF']['accepted_upper_exact'])**2;ck('same_complete_R2',S==Q(tail['full_rF_square_upper_exact']))
 V=Q(0) if N==319 else S/(N+2)**2
 for row in tail['modes']:
  n=row['n'];lo,hi=Q(row['q_lower_exact']),Q(row['q_upper_exact']);bind(R/row['record'],row['sha256'])
  coef=Q(1,n*n) if N==319 else Q(1,n*n)-Q(1,(N+2)**2)
  ck(f'prefix{n}_positive_coefficient',coef>0 and 0<lo<hi);V+=coef*hi
 ck('complete_M2_formula',V==Q(tail['M2_upper_exact'])==Q(tail['positive_coefficient_formula_upper_exact']))
 ck('same_selection_as_tail',tail['selected_improvement_modes']==list(range(1,32,2)) and J==Q(tail['selected_improvement_sum_lower_exact']) and L2==Q(tail['H_lower_square_exact']))
 U2=V-J;ck('strict_positive_H_interval',0<L2<U2 and U2==Q(tail['improved_H_square_upper_exact']))
 ck('stronger_than_old_complete_bounds',L2>Q(old['H_lower_square_exact']) and U2<Q(old['H_upper_square_exact']))
 lo={k:Q(norms['norms'][k]['accepted_lower_exact']) for k in ['G0','G1','P2']};hi={k:Q(norms['norms'][k]['accepted_upper_exact']) for k in lo}
 EL=lo['P2']**2+2**14*lo['G1']**2+2**18*lo['G0']**2+Q(20,21)*2**18*L2
 EU=hi['P2']**2+2**14*hi['G1']**2+2**18*hi['G0']**2+Q(20,21)*2**18*U2
 ck('exact_E2_assembly',EL==Q(tail['E2_lower_square_exact']) and EU==Q(tail['conditional_E2_upper_square_exact']) and 0<EL<EU)
 hl,hu=Q(tail['H_strict_lower_exact']),Q(tail['conditional_improved_H_strict_upper_exact'])
 el,eu=Q(tail['E2_strict_lower_exact']),Q(tail['conditional_E2_strict_upper_exact'])
 ck('strict_exact_endpoints',0<hl*hl<L2<U2<hu*hu and 0<el*el<EL<EU<eu*eu)
 bl,bh=decinterval(base['H_input_lower_ball']);e07=Q(base['E_upper']['strict_upper_exact'])
 ck('same007_bound',base['candidate']=='C1-N1-007-d2w-j7-e2bal' and e07==Q(multi['baseline007_E2_strict_upper_exact']) and base['E_upper']['strict_bounds_verified'])
 hg,eg=bl-hu,el-e07;ck('opposite_actual_norm_orders',hg>0 and eg>0)
 display={'H_lower':str(roundout(hl,9,False)),'H_upper':str(roundout(hu,9,True)),'E2_lower':str(roundout(el,6,False)),'E2_upper':str(roundout(eu,6,True)),'H007_minus_H016_lower':str(roundout(hg,9,False)),'E2016_minus_E2007_lower':str(roundout(eg,6,False))}
 for rel,h in inputs.items():assert sha(R/rel)==h,rel
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':CID,'raw_sha256':RAW,'inputs':inputs,'checks':checks,'check_count':len(checks),'prefix':N,'trial_mode_count':len(records),'pairing_group_count':groupcount,'selected_modes':records,'complete_M2_upper_exact':str(V),'selected_improvement_sum_lower_exact':str(J),'H_lower_square_exact':str(L2),'H_upper_square_exact':str(U2),'E2_lower_square_exact':str(EL),'E2_upper_square_exact':str(EU),'H_strict_lower_exact':str(hl),'H_strict_upper_exact':str(hu),'E2_strict_lower_exact':str(el),'E2_strict_upper_exact':str(eu),'H007_minus_H016_strict_lower_exact':str(hg),'E2016_minus_E2007_strict_lower_exact':str(eg),'display_bounds_exact':display,'all160_source_modes_covered':True,'individually_integrated_Hardy_modes':len(tail['modes']),'general_and_tail_reviews_completed':True,'peer_code_executed':False,'new_source_integrals':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED complete candidate016 H/E2 bounds and opposite same-norm007 comparisons. No inverse, correction distance or existence.'}
 p=B/f'verification/result_{a.version}.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'bindings',sha(p),'prefix',N,'groups',groupcount,'H',str(hl),str(hu),'E2',str(el),str(eu),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

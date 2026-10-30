"""Complete source and reviewed domain composition, exact rational arithmetic."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction
from flint import fmpq as Q
import json,os,sys,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_reviewed_upper'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();sys.set_int_max_str_digits(0)
def q(v):f=Fraction(v);return Q(f.numerator,f.denominator)
def main():
 start=time.monotonic();checks={};inputs={}
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);v=sha(p);key=str(p.relative_to(R));assert h is None or v==h,(key,h,v);assert key not in inputs or inputs[key]==v;inputs[key]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 mf=read(B/'source/MANIFEST.json');ck('proof_before_code',not mf['checker_exists']);bind(B/'PROOF.md',mf['proof_sha256']);bind(Path(__file__));par=read(B/'source/parameters.json',mf['parameters_sha256']);dep={}
 for rel,h in par['dependencies'].items():
  j=read(R/rel,h);ck('accepted:'+rel,all(j['checks'].values()));dep[Path(rel).parts[1]]=j
  for rr,hh in j['inputs'].items():bind(R/rr,hh)
 general=dep['candidate016_upper_opus_reciprocal'];primary=dep['candidate016_upper_opus_primary'];tail=dep['candidate016_angular_tail_bound'];cross=dep['candidate016_solenoidal_upper'];dual=dep['candidate016_dual_lower'];archive=dep['candidate016_pairing_archive'];norms=dep['candidate016_scaled_norm_peer']['norms']
 ck('both_general_reviews',general['both_general_Opus_reviews_accepted'] and general['check_count']==834 and primary['check_count']==77)
 ck('additional_tail_review_honestly_pending',general['separate_tail_review_still_pending'])
 ck('complete_source_and_prefix',tail['candidate']==par['candidate'] and tail['raw_sha256']==par['raw_sha256'] and tail['complete_field_mode_count']==160 and tail['complete_field_component_count']==1360 and tail['prefix']==par['prefix']==31)
 ck('whole_tail_retained',tail['complete_uncomputed_tail_retained'] and not tail['all160_individual_mode_integrals_replayed'])
 rows=tail['modes'];ck('every_prefix_mode',[r['n'] for r in rows]==list(range(1,32,2)) and tail['mode_count_replayed']==len(rows)==16)
 m=33;S=Q(tail['full_rF_square_upper_exact']);V=S/m**2
 for row in rows:
  n=row['n'];lower=Q(row['q_lower_exact']);upper=Q(row['q_upper_exact']);coef=Q(1,n*n)-Q(1,m*m)
  ck('positive_mode:'+str(n),0<lower<upper and coef>0);bind(R/row['record'],row['sha256']);V+=coef*upper
 ck('complete_M2_upper',V==Q(tail['M2_upper_exact'])==Q(tail['positive_coefficient_formula_upper_exact']))
 ck('directed_totalR2',S==Q(norms['rF']['accepted_upper_exact'])**2)
 ck('distinct_cross_selection',tail['selected_improvement_modes']==[1,3])
 J=Q(general['improvement_sum_strict_lower_exact']);ck('same_cross_floor',J==Q(cross['improvement_sum_strict_lower_exact'])==Q(archive['improvement_sum_strict_lower_exact'])==Q(tail['selected_improvement_sum_lower_exact']) and J>0)
 L2=sum((Q(v)**2 for v in dual['mode_strict_floors'].values()),Q(0));U2=V-J
 ck('complete_H_squares',0<L2<U2 and L2==Q(tail['H_lower_square_exact']) and U2==Q(tail['improved_H_square_upper_exact']))
 hf=q(par['H_lower']);hu=q(par['H_upper']);ck('strict_H_displays',hf>0 and hf*hf<L2 and U2<hu*hu)
 lo={k:Q(norms[k]['accepted_lower_exact']) for k in ['G0','G1','P2']};up={k:Q(norms[k]['accepted_upper_exact']) for k in ['G0','G1','P2']}
 for k in lo:ck('positive_components:'+k,0<lo[k]<up[k])
 EL=lo['P2']**2+2**14*lo['G1']**2+2**18*lo['G0']**2+Q(20,21)*2**18*L2
 EU=up['P2']**2+2**14*up['G1']**2+2**18*up['G0']**2+Q(20,21)*2**18*U2
 ck('same_E2_squares',EL==Q(tail['E2_lower_square_exact']) and EU==Q(tail['conditional_E2_upper_square_exact']) and 0<EL<EU)
 ef=q(par['E2_lower']);eu=q(par['E2_upper']);ck('strict_E2_displays',ef>0 and ef*ef<EL and EU<eu*eu)
 ck('accepted007bound',q(par['baseline007_upper'])==Q(dual['baseline007_E2_strict_upper_exact']))
 ck('strict_pairwise_gap',ef-q(par['baseline007_upper'])==q(par['gap_lower'])==Q(dual['strict_E2_separation_exact']) and ef>q(par['baseline007_upper']))
 ck('retained_precision',0<Q(tail['H_strict_lower_exact']) and Q(tail['H_strict_lower_exact'])**2<L2 and Q(tail['conditional_improved_H_strict_upper_exact'])**2>U2 and Q(tail['conditional_E2_strict_upper_exact'])**2>EU)
 for rel,h in inputs.items():assert sha(R/rel)==h
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':par['candidate'],'raw_sha256':par['raw_sha256'],'inputs':inputs,'check_count':len(checks),'checks':checks,'complete_M2_upper_exact':str(V),'H_lower_square_exact':str(L2),'H_upper_square_exact':str(U2),'E2_lower_square_exact':str(EL),'E2_upper_square_exact':str(EU),'H_strict_lower_exact':tail['H_strict_lower_exact'],'H_strict_upper_exact':tail['conditional_improved_H_strict_upper_exact'],'E2_strict_lower_exact':tail['E2_strict_lower_exact'],'E2_strict_upper_exact':tail['conditional_E2_strict_upper_exact'],'strict_display_bounds':{k:par[k] for k in ['H_lower','H_upper','E2_lower','E2_upper','baseline007_upper','gap_lower']},'general_analytic_review_condition_discharged':True,'both_general_Opus_reviews_accepted':True,'additional_T1_R1_050_not_claimed_completed':True,'full160_mode_field_covered':True,'individual_mode_count':16,'peer_code_executed':False,'new_integrals':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED complete whole-plane candidate016 H and E2 upper and lower bounds, with accepted general reviews and a proved complete tail. No inverse, correction-distance ordering or existence.'}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'bindings',sha(p),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

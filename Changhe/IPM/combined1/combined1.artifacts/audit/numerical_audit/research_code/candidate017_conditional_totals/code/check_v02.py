"""Conditional interval arithmetic only; source premises remain unaccepted."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import json,re,sys,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate017_conditional_totals';S=R/'research/candidate017_dual_residual_replay/source'
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ball(s):
 m=re.fullmatch(r'\[([0-9.eE+\-]+) \+/- ([0-9.eE+\-]+)\]',s)
 if not m:
  if re.fullmatch(r'[0-9.eE+\-]+',s):return Q(s),Q(s)
  raise ValueError('not a complete real ball or exact decimal: '+s[:95])
 a,r=Q(m[1]),Q(m[2]);assert r>=0;return a-r,a+r
add=lambda a,b:(a[0]+b[0],a[1]+b[1])
sub=lambda a,b:(a[0]-b[1],a[1]-b[0])
div=lambda a,n:(a[0]/n,a[1]/n)
def sq(a):
 assert 0<=a[0]<=a[1],a;return a[0]**2,a[1]**2
def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
def main():
 t=time.monotonic();inputs={};checks={}
 def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);v=sha(p);assert h is None or v==h,(str(p),h,v);k=str(p.relative_to(R));assert k not in inputs or inputs[k]==v;inputs[k]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 first=read(B/'verification/PROOF_FIRST.json');ck('proof_before_code',not first['checker_exists']);bind(B/'PROOF.md',first['proof_sha256']);bind(Path(__file__))
 revision=read(B/'verification/PROOF_FIRST_v02.json');ck('revision_proof_before_code',not revision['checker_v02_exists']);bind(B/'PROOF_v02.md',revision['proof_sha256']);bind(B/'verification/FAILED_v01.json',revision['failed_record_sha256']);bind(B/'code/diagnose_v01.py',revision['diagnostic_checker_sha256'])
 par=read(B/'source/parameters.json',first['parameters_sha256'])
 for p,h in par['inputs'].items():bind(R/p,h)
 d=read(S/'N3_dual.json');r=read(S/'N3_hres.json');h=read(S/'N3_hardy.json');a=read(S/'N3_norms.json')
 for k,j in [('dual',d),('residual',r),('Hardy',h),('norms',a)]:ck('common_source_'+k,j['source_sha256']==par['source_sha256'])
 ck('same_c_delta',Q(a['cl'])==Q(4076476460239181,2251799813685248) and Q(a['delta'])==1-1/Q(a['cl']))
 ck('dual_current_code_matches',d['code_sha256']==sha(S/'N3_legqs_hdual.py'))
 ck('residual_historical_code_distinct',r['code_sha256']=='1944bedcb3a59dd38633cf10507f4dfb530f06118c2ae82e65db87fee7cab0dd' and sha(S/'N3_legqs_hres.py')=='615478fe9ebdff3b07f0d74b061a2c5c7933ffc1ae2f84ea8a9349dbe55afdef' and r['code_sha256']!=sha(S/'N3_legqs_hres.py'))
 dm={x['n']:x for x in d['modes']};rm={x['n']:x for x in r['modes']};hm={x['n']:x for x in h['modes']}
 ck('sixteen_unique_dual_modes',list(dm)==list(range(1,32,2)) and len(dm)==len(d['modes'])==16)
 ck('sixteen_unique_residual_modes',list(rm)==list(range(1,32,2))==r['modes_computed'] and len(rm)==len(r['modes'])==16)
 ck('complete_claimed_Hardy_mode_list',list(hm)==list(range(1,320,2)) and len(hm)==len(h['modes'])==160)
 totalq=(Q(0),Q(0));hardysq=(Q(0),Q(0));othersq=(Q(0),Q(0));usq=(Q(0),Q(0));dualsq=(Q(0),Q(0));rows=[]
 for n,rr in hm.items():
  qn=ball(rr['rF_n_sq']);rn=ball(rr['rF_n']);hn=ball(rr['H_n_UB']);ck(f'positive_q_{n}',0<qn[0]<=qn[1]);ck(f'Hardy_square_consistency_{n}',overlap(qn,sq(rn)) and overlap(div(qn,n*n),sq(hn)))
  totalq=add(totalq,qn);hardysq=add(hardysq,div(qn,n*n))
  if n not in rm:othersq=add(othersq,div(qn,n*n));usq=add(usq,div(qn,n*n));continue
  rr=rm[n];dr=dm[n];grad=ball(rr['grad_psi']);res=ball(rr['residual_r_g']);du=ball(dr['LB']);up=add(grad,div(res,n));up2=sq(up)
  ck(f'positive_trial_{n}',0<grad[0] and 0<res[0] and 0<du[0])
  ck(f'residual_division_consistency_{n}',overlap(div(res,n),ball(rr['residual_over_n'])))
  ck(f'residual_upper_consistency_{n}',overlap(up,ball(rr['UB_n'])))
  ck(f'residual_lower_consistency_{n}',overlap(sub(grad,div(res,n)),ball(rr['LB2_n'])))
  ck(f'dual_lower_not_above_Hardy_{n}',du[0]*du[0]<qn[1]/(n*n))
  ck(f'no_different_basis_double_count_{n}',len(dr['betas'])==9 and len(rr['betas'])==8 and '2' in dm[1]['betas'])
  dualsq=add(dualsq,sq(du));mode=(min(up2[0],qn[0]/(n*n)),min(up2[1],qn[1]/(n*n)));usq=add(usq,mode)
  rows.append({'n':n,'dual_lower_exact':str(du[0]),'residual_upper_exact':str(up[1]),'mode_H_square_upper_exact':str(mode[1]),'source_integrals_reproduced_in_this_check':False})
 ck('rF_total_consistency',overlap(totalq,(sq(ball(a['norms']['rF']['norm_lower']))[0],sq(ball(a['norms']['rF']['norm_upper']))[1])))
 ck('Hardy_total_consistency',overlap(hardysq,sq(ball(h['H_upper_ball']))))
 ck('dual_total_consistency',overlap(dualsq,sq(ball(d['H_lower_ball']))))
 ck('residual_other_total_consistency',overlap(othersq,ball(r['other_modes_hardy_sq'])))
 ck('stored_endpoint_is_conservative_over_recomputed_upper',usq[1]<Q(r['H_upper_new'])**2<Q(par['H_upper'])**2)
 L=dualsq[0];U=usq[1];ck('conditional_H_display_squares',0<Q(par['H_lower'])**2<L<U<Q(par['H_upper'])**2)
 lo={k:ball(a['norms'][k]['norm_lower'])[0] for k in ['G0','G1','P2']};up={k:ball(a['norms'][k]['norm_upper'])[1] for k in lo}
 for k in lo:ck('conditional_norm_positive_'+k,0<lo[k]<up[k] and a['norms'][k]['status']=='FINITE')
 EL=lo['P2']**2+2**14*lo['G1']**2+2**18*lo['G0']**2+Q(20,21)*2**18*L
 EU=up['P2']**2+2**14*up['G1']**2+2**18*up['G0']**2+Q(20,21)*2**18*U
 ck('conditional_E2_display_squares',0<Q(par['E2_lower'])**2<EL<EU<Q(par['E2_upper'])**2)
 old=read(R/'research/negative_norm_forcing_assembly/verification/result.json');ck('accepted007',all(old['checks'].values()))
 for p,hh in old['inputs'].items():bind(R/p,hh)
 gap=Q(old['E_lower']['strict_lower_exact'])-Q(par['E2_upper']);ck('conditional_pairwise_gap',gap>Q(par['gap_lower'])>0)
 rejected=[]
 for k,j in [('dual',d),('residual',r)]:
  for field in ['H_upper_hardy','E2_lower_without_H','E2_upper_with_mode_hardy_H']:
   if field in j:
    try:ball(j[field])
    except ValueError:rejected.append(k+'.'+field)
 ck('truncated_diagnostic_strings_not_used',len(rejected)==4)
 for p,hh in inputs.items():assert sha(R/p)==hh
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'checks':checks,'check_count':len(checks),'candidate':'C1-N1-017-legqs50-quot013','raw_sha256':par['source_sha256'],'modes':rows,'uncomputed_tail_mode_count':144,'conditional_H_square_lower_exact':str(L),'conditional_H_square_upper_exact':str(U),'conditional_E2_square_lower_exact':str(EL),'conditional_E2_square_upper_exact':str(EU),'conditional_display':{k:par[k] for k in ['H_lower','H_upper','E2_lower','E2_upper','gap_lower']},'conditional007_minus017_gap_exact':str(gap),'stored_H_upper_square_conservative_slack_exact':str(Q(r['H_upper_new'])**2-U),'diagnostic_incomplete_strings_rejected':rejected,'source_premises_C1_C2_C3_accepted_here':False,'actual017_H_or_E2_certified_here':False,'actual017_less_than007_certified_here':False,'peer_code_executed':False,'new_integrals':False,'historical_hres_code_observed':False,'elapsed_seconds':time.monotonic()-t,'verdict':'CONFIRMED conditional finite total arithmetic and coarse outward displays. OPEN source premises C1-C3 and actual017 narrow norms/ordering.'}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'bindings',sha(p),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

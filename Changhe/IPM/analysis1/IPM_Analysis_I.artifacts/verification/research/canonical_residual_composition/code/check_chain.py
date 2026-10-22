"""Exact boundary and tail dependency graph, independent polynomial identities."""
from check import *
import copy

def rejected(fn):
 try:fn()
 except (ValueError,KeyError,TypeError,ZeroDivisionError):return 1
 raise ValueError('negative contract unexpectedly accepted')

def main():
 start=now();tic=time.monotonic();v=load(E/'checks.json');need(v['status']=='PASS_COMPLETE_CANONICAL_RESIDUAL_PREMISE_COMPOSITION_REQUIRES_ACTUAL_REVIEW','complete main application');pins={};merge(pins,v);pin(pins,'research/canonical_residual_composition/evidence/checks.json');d146=load(B/DEPS['146'][0]);edges=[]
 def get(n):
  n='research/'+n;need(n in d146['files'],'actual inherited file '+n);pin(pins,n,d146['files'][n]);return load(B/n)
 def edge(parent,child):
  p=get(parent);n='research/'+child;need(n in p['files'] and p['files'][n]==d146['files'][n]==sha(B/n),'exact inherited edge');edges.append({'parent':'research/'+parent,'child':n,'sha256':p['files'][n]})
 graph={
 'inner_cells/evidence/verdict.json':['inner_majorant/evidence/verdict.json','inner_majorant/evidence/inner_result.json','inner_majorant/evidence/inner_iv_audit.json','inner_majorant/evidence/exact_inner_coefficients.json','inner_cells/evidence/full_q16_tail.json','inner_cells/code/cell_arb.py','inner_cells/code/cell_integer_iv.py','inner_cells/code/tail_disk.py'],
 'inner_majorant/evidence/verdict.json':['inner_majorant/evidence/inner_result.json','inner_majorant/evidence/inner_iv_audit.json','inner_majorant/evidence/exact_inner_coefficients.json'],
 'outer_cells/evidence/verdict.json':['outer_majorant/evidence/verdict.json','outer_majorant/evidence/outer_result.json','outer_majorant/evidence/exact_outer_coefficients.json','outer_leading_cancellation/evidence/verdict.json','outer_cells/evidence/full_q16_tail_l2.json','outer_cells/code/cell_arb.py','outer_cells/code/cell_integer_iv.py','outer_cells/code/tail_l2.py'],
 'outer_leading_cancellation/evidence/verdict.json':['outer_majorant/evidence/verdict.json','outer_majorant/evidence/outer_result.json','outer_majorant/evidence/exact_outer_coefficients.json','outer_leading_cancellation/evidence/leading_result.json','outer_leading_cancellation/evidence/leading_iv_audit.json','outer_leading_cancellation/code/combine_leading.py','outer_leading_cancellation/code/audit_leading_iv.py'],
 'outer_majorant/evidence/verdict.json':['outer_majorant/evidence/outer_result.json','outer_majorant/evidence/outer_iv_audit.json','outer_majorant/evidence/exact_outer_coefficients.json','outer_majorant/evidence/final_span.json','outer_majorant/evidence/final_span_extract.json']}
 for parent,children in graph.items():
  for child in children:edge(parent,child)
 inn=get('inner_majorant/evidence/inner_result.json');ina=get('inner_majorant/evidence/inner_iv_audit.json');ico=get('inner_majorant/evidence/exact_inner_coefficients.json');it=get('inner_cells/evidence/full_q16_tail.json');out=get('outer_majorant/evidence/outer_result.json');oca=get('outer_majorant/evidence/outer_iv_audit.json');oco=get('outer_majorant/evidence/exact_outer_coefficients.json');lead=get('outer_leading_cancellation/evidence/leading_result.json');ot=get('outer_cells/evidence/full_q16_tail_l2.json')
 def ih(n):return sha(B/'research'/n)
 need(inn['coefficient_sha256']==ih('inner_majorant/evidence/exact_inner_coefficients.json') and ina['primary_result_sha256']==ih('inner_majorant/evidence/inner_result.json') and ina['status']=='PASS','inner dependency identities')
 need(out['coefficient_sha256']==ih('outer_majorant/evidence/exact_outer_coefficients.json') and oca['primary_result_sha256']==ih('outer_majorant/evidence/outer_result.json') and oca['status']=='PASS','outer dependency identities')
 need(ico['input_sha256']==oco['input_sha256']==SSHA and F(ico['ta_exact'])==JOINS[0] and F(oco['tb_exact'])==JOINS[1],'analytic tails same trial and boundaries')
 need(oco['correction_parameter_exact_interval']==lead['normalization_interval_exact']==v['Z_exact'],'same exact common normalization interval')
 need([r['j'] for r in ico['rows']]==[r['j'] for r in oco['rows']]==list(range(262)),'complete analytic density modes')
 need(it['inner_verdict_sha256']==ih('inner_majorant/evidence/verdict.json'),'inner tail source verdict')
 for n,h in it['dependency_pins'].items():need(h==pins[n]==sha(B/n),'inner tail direct data edge')
 b5=max(ff(next(c for c in x['cases'] if c['T_exact']=='5/2')['values']['B5']['upper_exact']) for x in [inn,ina]);need(b5>0 and b5==ff(it['B5_upper_exact']) and ff(it['T_exact'])==7 and ff(it['base_majorant_T_exact'])==F(5,2),'actual complete inner tail restriction')
 need(lead['outer_verdict_sha256']==ih('outer_majorant/evidence/verdict.json') and lead['outer_result_sha256']==ih('outer_majorant/evidence/outer_result.json') and lead['exact_coefficients_sha256']==ih('outer_majorant/evidence/exact_outer_coefficients.json'),'improved leading actual source edges')
 need(ot['leading_verdict_sha256']==ih('outer_leading_cancellation/evidence/verdict.json') and ot['leading_result_sha256']==ih('outer_leading_cancellation/evidence/leading_result.json') and ot['outer_result_sha256']==ih('outer_majorant/evidence/outer_result.json') and ff(ot['T_exact'])==17 and ot['moment_overlap_checks']==3508,'actual outer half-line source edges')
 gam=2*K-1;need(gam<0 and K-F(1,2)<0 and ff(lead['gamma_star_exact'])==gam,'exact weighted far-field rates');gamma_rows=0;monomials=0
 for row in out['majorant']:
  g=ff(row['gamma_exact']);need(g<=gam and K-g>0,'every tail exponent decays');cs=[ff(x['upper_exact']) for x in row['coefficients']];need(all(x>=0 for x in cs),'every outer majorant coefficient nonnegative');monomials+=len(cs)
  if g==gam:gamma_rows+=1;need(len(cs)==1 and ff(lead['new_C_star']['upper_exact'])>=0,'single entire leading replacement')
 need(len(out['majorant'])==1864 and monomials==3508 and gamma_rows==1,'complete outer tail monomial contract')
 beta=list(map(ff,oco['beta_exact']));need(len(beta)==11 and beta[0]==K and 0<K<F(1,2) and L>0,'exterior exact scalar parameters')
 coeff=[[[tuple(map(ff,x)) for x in c] for c in row['basis']] for row in oco['rows']];need(all(len(row)==11 and all(len(c)==(7 if b==10 else 1) for b,c in enumerate(row)) for row in coeff) and all(p==(F(0),F(0)) for c in coeff[-1] for p in c),'all affine density coefficient shapes')
 identities=0
 # Check saved particular polynomials by their differential equation, not the producer inverse recursion.
 for n,green in enumerate(out['green'],1):
  need(green['n']==n,'ordered exterior Green modes');m=2*n
  for b,be in enumerate(beta):
   cm,cp=coeff[n-1][b],coeff[n][b];need(len(cm)==len(cp),'neighbor polynomial degrees')
   for key,lam,sgn in [('plus_exact',be+1+m,1),('minus_exact',be+1-m,-1)]:
    need(lam!=0,'no exterior inverse resonance');saved=[tuple(map(ff,x)) for x in green[key][b]];need(len(saved)==len(cm),'particular polynomial shape')
    for j,q in enumerate(saved):
     for z in range(2):
      deriv=(j+1)*(cm[j+1][z]+cp[j+1][z]) if j+1<len(cm) else F(0);force=((be+1-m)*cm[j][z]+(be+1+m)*cp[j][z]+deriv)/2
      lhs=lam*q[z]+((j+1)*saved[j+1][z] if j+1<len(saved) else F(0));need(lhs==sgn*force,'exact saved particular differential identity')
      native=fmpq(str(lam))*fmpq(str(q[z]))+(fmpq(j+1)*fmpq(str(saved[j+1][z])) if j+1<len(saved) else fmpq(0));nf=((fmpq(str(be))+1-m)*fmpq(str(cm[j][z]))+(fmpq(str(be))+1+m)*fmpq(str(cp[j][z]))+(fmpq(j+1)*(fmpq(str(cm[j+1][z]))+fmpq(str(cp[j+1][z]))) if j+1<len(cm) else fmpq(0)))/2;need(native==sgn*nf and qf(native)==lhs,'second exact polynomial identity');identities+=1
 need(identities==17748,'all exact affine Green scalar equations')
 headers={}
 for topic in ['middle_residual','middle_second']:
  n='research/'+topic+'/evidence/full_q16_cells.jsonl';need(n in d146['files'] and sha(B/n)==d146['files'][n],'complete middle stream inherited pin')
  with (B/n).open() as f:headers[topic]=parse(next(f))
 ph,sh=headers['middle_residual'],headers['middle_second'];need(ph['knot_input_sha256']==ASHA and ph['modal_input_sha256']==SSHA and sh['primary_header']==ph,'identical primary header in complete second stream')
 for n,h in sh['pins'].items():need(pins[n]==h and sha(B/n)==h,'second middle input edge')
 for h in headers.values():need(h['cells_required']==7809 and F(h['k_exact'])==K and F(h['L_exact'])==L,'complete middle parameters')
 need(sh['spans_required']==1558 and sh['region_boundary_joins']['inner']=={'log_radius_exact':str(JOINS[0]),'relative_cell_boundary_exact':'0','verdict_sha256':ih('inner_cells/evidence/verdict.json')} and sh['region_boundary_joins']['outer']=={'log_radius_exact':str(JOINS[1]),'relative_cell_boundary_exact':'0','verdict_sha256':ih('outer_cells/evidence/verdict.json')},'both closed annulus joins bound to same end regions')
 rejects={}
 for tag in ['146','156']:
  old=load(B/DEPS[tag][0]);gate=gate146 if tag=='146' else gate156;cases=[]
  x=copy.deepcopy(old);x['status']='PENDING';cases.append(x)
  if tag=='146':
   x=copy.deepcopy(old);x['cells']['middle']=7808;cases.append(x)
  else:
   x=copy.deepcopy(old);x['moment_targets']-=1;cases.append(x)
  if tag=='156':
   for n in [SOURCE,ARCHIVE,ZPATH]:x=copy.deepcopy(old);x['files'][n]='0'*64;cases.append(x)
  else:x=copy.deepcopy(old);x['actual_full_middle_verdict_sha256']='0'*64;cases.append(x)
  rejects[tag]=sum(rejected(lambda x=x:gate(x)) for x in cases)
 rejects['duplicate_nonfinite_json']=sum(rejected(lambda s=s:parse(s)) for s in ['{"a":1,"a":2}','{"x":NaN}','{"x":Infinity}','{"x":-Infinity}'])
 bad={'schema':'arb-dyadic-mid-radius-v1','mid_m':'0','mid_e':'0','rad_m':'-1','rad_e':'0'};rejects['negative_ball_radius']=rejected(lambda:ball(bad))
 need(rejects=={'146':3,'156':5,'duplicate_nonfinite_json':4,'negative_ball_radius':1},'all expected negative tests executed')
 for n in ['code/check_chain.py','REVIEW_RESOLUTION.md']:pin(pins,str((D/n).relative_to(B)))
 value={'start_utc':start,'utc':now(),'status':'PASS_COMPLETE_DECLARED_BOUNDARY_AND_TAIL_INPUT_CHAIN','main_checks_sha256':sha(E/'checks.json'),'edges':edges,'counts':{'direct_parent_edges':len(edges),'outer_particular_scalar_equations_each_exact_engine':identities,'outer_exponents':1864,'outer_monomials':monomials,'middle_complete_headers':2},'common_Z_exact':v['Z_exact'],'inner_tail_B5_exact':str(b5),'decay_rates_exact':{'largest_gamma':str(gam),'largest_weighted_rate':str(K-F(1,2))},'headers':headers,'rejections':rejects,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tic,'scope':'Transitive declared data contracts, manual input-code review and fresh exact exterior ODE checks. The accepted regional computations and analytic tail proofs remain dependencies; this is not a regional rerun.'};write(E/'chain_checks.json',value);print(json.dumps({k:value[k] for k in ['utc','status','counts','rejections','seconds']}))
if __name__=='__main__':main()

"""Exact operator diagnostics and current short-run binding. No full result."""
from common import *
from audit import ball
from copy import deepcopy
from math import comb
import importlib.util

def main():
 p,deps=base();geometry,targets=coordinates();cases=[]
 def case(name,fn,reject=False):
  try:fn()
  except ValueError as e:ok=reject;detail=str(e)
  else:ok=not reject;detail='accepted diagnostic only'
  cases.append({'case':name,'expected_rejection':reject,'pass':ok,'detail':detail})
 spec=importlib.util.spec_from_file_location('accepted_engine_diagnostic',B/ENGINE);g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
 # Check the partial and reverse polynomial transformations as identities at nine
 # rational points, more than their degree. The particular recurrence is exact.
 for seed in range(1,7):
  P=[Q((-1)**k*(seed+k),seed+2*k+1) for k in range(8)];xi=Q(seed,seed+1);h=Q(seed+3,seed+9)
  forward=[v*xi**k for k,v in enumerate(P)];reverse=[(-(1-xi))**j*sum(P[k]*comb(k,j) for k in range(j,8)) for j in range(8)]
  for i in range(9):
   u=Q(i,8);need(sum(forward[k]*u**k for k in range(8))==sum(P[k]*(xi*u)**k for k in range(8)),'partial forward exact polynomial identity');need(sum(reverse[k]*u**k for k in range(8))==sum(P[k]*(1-(1-xi)*u)**k for k in range(8)),'partial backward exact polynomial identity')
  for rate in [-526,-6,-2,2]:
   zeta=rate*h;q=[Q(0)]*9
   for k in reversed(range(8)):q[k]=((k+1)*q[k+1]-h*P[k])/zeta
   need(all((k+1)*q[k+1]-zeta*q[k]==h*P[k] for k in range(8)),'exact particular coefficient equation')
  exact=Q(2,7)+h*sum(P[k]/(k+1) for k in range(8));lo,hi=g.ends(g.step(g.ii(g.q(Q(2,7))),list(map(g.q,P)),g.q(h),0));need(Q(str(lo))<=exact<=Q(str(hi)),'n2 exact zero-rate primitive contained')
  lo,hi=g.ends(g.step(g.ii(0),[g.fmpq(0)]*8,g.q(h),-518));need(lo==hi==0,'zero J261 invariant')
 cases.append({'case':'six exact partial/reverse/particular and zero-rate families','expected_rejection':False,'pass':True,'detail':'108 polynomial evaluations,192 coefficient equalities,6 zero-rate primitives,6 zero invariants'})
 good={'schema':'arb-dyadic-mid-radius-v1','mid_m':'-3','mid_e':-5,'rad_m':'1','rad_e':-8};case('strict exact dyadic ball control',lambda:need(ball(good)==(Q(-25,256),Q(-23,256)),'ball values'))
 for key,val in [('schema','other'),('mid_m','1.0'),('mid_e',True),('rad_m','-1'),('rad_e',1.5)]:
  bad=deepcopy(good);bad[key]=val;case('reject malformed ball '+key,lambda bad=bad:ball(bad),True)
 case('reject extra ball key',lambda:ball(dict(good,extra=1)),True)
 s={'status':'COMPUTED_COMPLETE_CENTERS_REQUIRES_INDEPENDENT_AUDIT','full_run':True,'counts':deepcopy(COUNTS),'center_cells':{'I':CELLS,'J':list(reversed(CELLS))},'iv_dps':200,'anchor_checks':3915,'output_sha256':'EXPLICIT_SYNTHETIC_FIXTURE','worst_relative_margins':{'EXPLICIT_FIXTURE':True},'minimum_nonzero_abs_zeta_exact':'1/20'}
 a={'status':'PASS_COMPLETE_CENTER_SAVED_PAIR_NEWTON_DENSITY_AND_ANCHOR_AUDIT','full_run':True,'counts':deepcopy(COUNTS),'all_saved_moment_pairs':6786,'independent_exact_density_coefficients':27248,'independent_exact_anchors':783,'center_cells':deepcopy(s['center_cells']),'output_sha256':s['output_sha256'],'worst_relative_margins':s['worst_relative_margins'],'minimum_nonzero_abs_zeta_exact':s['minimum_nonzero_abs_zeta_exact']};q={'status':'COMPLETE_CENTER_COMPUTATION_AND_AUDIT_REQUIRES_REVIEW'}
 case('labeled complete-field gate control',lambda:output_fields(s,a,q))
 for obj,index in [(s,0),(a,1),(q,2)]:
  for key,value in obj.items():
   items=[deepcopy(s),deepcopy(a),deepcopy(q)];items[index][key]=(not value) if type(value) is bool else value+1 if type(value) is int else {} if type(value) is dict else 'WRONG_FIXTURE';case('reject output field '+str(index)+'.'+key,lambda items=items:output_fields(*items),True)
 for index in [0,1]:
  for key in COUNTS:
   items=[deepcopy(s),deepcopy(a),deepcopy(q)];items[index]['counts'][key]+=1;case('reject complete count '+str(index)+'.'+key,lambda items=items:output_fields(*items),True)
 need(all(v['pass'] for v in cases),'actual preparation diagnostics all pass')
 smoke=load(E/'smoke_summary.json');audit=load(E/'smoke_output_audit.json');expected=dict.fromkeys(COUNTS,0);expected.update(spans_I=1,spans_J=1,full_steps_I=261,full_steps_J=261,H_coefficients=27248,exact_anchors=783)
 for family,si in [('I',0),('J',1557)]:expected['center_steps_'+family]=expected[family+'_targets']=261*sum(v['span']==si for v in geometry)
 need(smoke['status']=='OPEN_SHORT_CENTER_PROPAGATION_DIAGNOSTIC' and audit['status']=='PASS_SHORT_CENTER_DIAGNOSTIC_AND_COMPLETE_EXACT_DENSITY_ANCHOR_AUDIT' and smoke['full_run'] is audit['full_run'] is False and smoke['counts']==audit['counts']==expected,'actual short diagnostic extent');need(smoke['output_sha256']==audit['output_sha256']==sha(E/'smoke_centers.jsonl.gz') and audit['summary_sha256']==sha(E/'smoke_summary.json') and smoke['producer_sha256']==sha(D/'code/full.py') and audit['auditor_sha256']==sha(D/'code/audit.py') and smoke['engine_sha256']==sha(B/ENGINE) and audit['Newton_source_sha256']==sha(B/NEWTON),'actual smoke source/output binding');need(smoke['code_birth_sha256']==audit['code_birth_sha256']==sha(D/'data_exact/code_birth.json') and smoke['preflight_sha256'] is audit['preflight_sha256'] is None,'preparation cannot use future acceptance');chronology(load(D/'data_exact/code_birth.json')['utc'],smoke['start_utc'],smoke['utc'],audit['start_utc'],audit['utc']);need(not(E/'full_summary.json').exists() and not(E/'full_centers.jsonl.gz').exists() and not(E/'verdict.json').exists(),'no future full output at preparation')
 need(load(D/'data_exact/review_files.json')=={'preparation':mandatory(False),'actual':mandatory(True)},'fixed complete review bundles')
 for n in ['smoke_summary.json','smoke_output_audit.json','smoke_centers.jsonl.gz']:pin(p,E/n)
 out={'utc':now(),'status':'PASS_CENTER_PREPARATION_AND_SHORT_DIAGNOSTICS_ONLY','cases':cases,'case_count':len(cases),'expected_rejections':sum(v['expected_rejection'] for v in cases),'failures':[],'source_geometry':geometry,'actual_smoke':smoke,'actual_smoke_audit':audit,'future_full_counts_required':COUNTS,'full_result_exists':False,'files':dict(sorted(p.items())),'scope':'Exact identities and malformed-record diagnostics, a short real iv200 propagation and independent exact density/anchor audit. No full integration accepted.'};rehash(p);write(E/'preparation_checks.json',out)
 x={'utc':now(),'status':'EXACT_CENTER_PREPARATION_PROJECTION_ONLY','preparation_sha256':sha(E/'preparation_checks.json'),'preparation':{k:v for k,v in out.items() if k!='files'}};write(E/'preparation_extract.json',x);print(json.dumps({'utc':out['utc'],'status':out['status'],'cases':len(cases),'pins':len(p),'sha256':sha(E/'preparation_checks.json')}))
if __name__=='__main__':main()

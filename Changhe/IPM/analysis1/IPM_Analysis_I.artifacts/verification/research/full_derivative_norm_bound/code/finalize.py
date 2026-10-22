from protocol import *
p,deps,f=source();x=load(OUT/'actual_extract.json');s=load(OUT/'full_summary.json');a=load(OUT/'full_audit.json');r=load(OUT/'full_replay.json');q=load(OUT/'queue_status.json');prep=load(OUT/'preparation_acceptance.json')
assert s['status']=='COMPUTED_COMPLETE_DERIVATIVE_NORM_BOUNDS_REQUIRES_INDEPENDENT_AUDIT' and s['cells']==7809 and s['full_middle'] is True
assert a['status']=='PASS_COMPLETE_SAVED_DERIVATIVE_STREAM_AND_EXACT_REDUCTION' and a['cells']==7809 and a['full_middle'] is True
assert r['status']=='PASS_COMPLETE_SELECTED_DERIVATIVE_CELLS_AND_ALL_TAILS_REPLAY' and r['full_middle'] is True
assert q['status']=='COMPLETE_DERIVATIVE_NORM_COMPUTATION_AUDIT_REPLAY_REQUIRES_ACTUAL_REVIEW'
expected={'status':'EXACT_COMPLETE_DERIVATIVE_NORM_REVIEW_PROJECTION','summary':{k:v for k,v in s.items() if k!='files'},'audit':{k:v for k,v in a.items() if k!='files'},'replay':r,'queue':q,'parents':deps,'source_freeze_sha256':sha(OUT/'source_freeze.json'),'preparation_sha256':sha(OUT/'preparation_acceptance.json')}
assert {k:v for k,v in x.items() if k!='utc'}==expected
for name,key in [('full_summary.json','summary_sha256'),('full_audit.json','audit_sha256'),('full_replay.json','replay_sha256')]:assert q[key]==sha(OUT/name)
assert a['summary_sha256']==r['summary_sha256']==sha(OUT/'full_summary.json') and r['audit_sha256']==sha(OUT/'full_audit.json')
assert a['required_replay_cells']==r['required_cells']==[v['cell'] for v in r['results']]
assert s['all_product_coefficient_equalities']==a['all_product_coefficient_equalities']
rehash(s['files']);rehash(prep['files'])
for n,h in prep['files'].items():pin(p,n,h)
for name in ['preparation_acceptance.json','full_summary.json','full_audit.json','full_replay.json','full_rows.jsonl','full_tails.json','full_restarts.jsonl','queue_status.json','actual_extract.json']:pin(p,OUT/name)
files=load(DIR/'review_files.json')['actual'];rev=auth(p,'full_derivative_norm_actual','CONFIRM_COMPLETE_CANONICAL_PHYSICAL_DERIVATIVE_NORM_BOUNDS',files,(DIR/'actual_question.txt').read_text());po=post(p,'full_derivative_norm_actual',rev,'POSTREVIEW_ADJUDICATION')
assert when(q['utc'])<when(x['utc'])<when(rev['start_utc']);rehash(p)
out={'utc':now(),'status':'CONFIRMED_COMPLETE_CANONICAL_PHYSICAL_DERIVATIVE_NORM_BOUNDS','parents':deps,'cells':7809,'strict_decimal_ceilings':s['strict_decimal_ceilings'],'all_product_coefficient_equalities':s['all_product_coefficient_equalities'],'replayed_cells':r['required_cells'],'tail_weight_pairs':3508,'actual_output_review':rev,'own_postreview':po,'files':dict(sorted(p.items())),'scope':'Numerical upper bounds for canonical eps and eps-D eps in the stated weak weighted H1 norm over the complete plane, including the entire inner and outer regions. New direct bounds, not verification of old annular W targets. No inverse, published X3 distance, nonlinear closing estimate or decisive IPM existence/exclusion endpoint.'}
write(OUT/'verdict.json',out);print(canonical({'utc':out['utc'],'status':out['status'],'pins':len(p),'sha256':sha(OUT/'verdict.json'),'strict_decimal_ceilings':out['strict_decimal_ceilings']}))

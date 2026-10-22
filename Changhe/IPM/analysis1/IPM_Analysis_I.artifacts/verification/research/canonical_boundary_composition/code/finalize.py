from common import *
EXPECTED_COUNTS={'spans':1558,'child_cells':7809,'boundaries':7810,'H_shapes':3265568,'moment_shapes':813276,'zero_H_coefficients_two_routes':12464,'zero_J_targets_two_routes':1558,'original_row_hashes':1558,'green_counts_each_engine':4076820,'selected_green_coordinates':436}
def required():
 own=['PROOF.md','evidence/proof_first.json','REVIEW_RESOLUTION.md','code/check.py','code/common.py','code/finalize.py','code/extract.py','code/launch_actual.py','evidence/review_extract.json']
 parents=['research/modal_repair/PROOF.md','research/modal_green/PROOF.md','research/full_green_linkage/PROOF.md','research/canonical_three_cell_linkage/PROOF.md','research/canonical_archive_second/PROOF.md','research/canonical_archive_second/ADDENDUM.md','research/canonical_archive_second/POSTREVIEW_ADJUDICATION.md','notes/reviews/canonical_archive_second_actual_response.md','notes/reviews/full_green_actual_complete_response.md','notes/reviews/canonical_three_cell_actual_v2_response.md','notes/reviews/canonical_boundary_composition_proof_response.md']
 return [str((D/n).relative_to(B)) for n in own]+parents

def complete():
 p={};v=load(E/'checks.json');need(v['status']=='PASS_CANONICAL_BOUNDARIES_AND_THREE_RADIAL_CELLS_COMPOSITION_REQUIRES_ACTUAL_REVIEW' and v['counts']==EXPECTED_COUNTS,'actual full composition checks');merge(p,v)
 s=v['symbolic_checks'];need(s['modes']==261 and s['identities_per_mode']==6 and s['scalar_coefficients_each_method']==9396 and s['normalization_jets_each_method']==7 and s['mode2_zero_rate_included'] is True,'full symbolic checks')
 need([a['cell'] for a in v['three_cells']]==[0,4102,7808] and v['direct157_dependencies']==EDGES,'exact accepted selected consequence')
 for tag,(n,h) in DEPS.items():need(v['accepted_dependencies'][tag]['path']==n and v['accepted_dependencies'][tag]['sha256']==h,'fixed current parent verdict');pin(p,n,h);merge(p,load(B/n))
 for n in D.rglob('*'):
  if n.is_file() and n.name not in ['verdict.json','postreview_record.json','POSTREVIEW_ADJUDICATION.md']:pin(p,n)
 pr=auth(p,'canonical_boundary_composition_proof','CONFIRM_CONDITIONAL_BOUNDARY_COMPOSITION_PROOF',load(D/'proof_files.json'));return p,v,pr

if __name__=='__main__':
 p,v,pr=complete();x=load(E/'review_extract.json');need(x['status']=='ACTUAL_COMPLETE_BOUNDARY_COMPOSITION_EXTRACT_REQUIRES_REVIEW' and x['checks_sha256']==sha(E/'checks.json') and x['checks']=={k:a for k,a in v.items() if k!='files'},'actual complete extract binding');need(when(v['utc'])<when(x['utc']),'extract after actual checks')
 for tag,(n,h) in DEPS.items():d=load(B/n);need(x['dependencies'][tag]=={k:a for k,a in d.items() if k!='files'} and x['verdict_sha256'][tag]==h,'unchanged dependency extract')
 need(set(load(D/'actual_files.json'))==set(required()),'independently fixed complete actual bundle');tag='canonical_boundary_composition_actual';r=auth(p,tag,'CONFIRM_CANONICAL_BOUNDARIES_AND_THREE_RADIAL_CELLS',required());need(when(x['utc'])<when(r['start_utc']) and when(pr['end_utc'])<when(r['start_utc']),'actual review after all output and proof')
 postrec=post(p,tag,r,E/'postreview_record.json',D/'POSTREVIEW_ADJUDICATION.md')
 for n,h in p.items():need(sha(B/n)==h,'unchanged final pins')
 out={'utc':now(),'status':'CONFIRMED_CANONICAL_BOUNDARIES_AND_THREE_RADIAL_CELLS','source_sha256':SSHA,'archive_sha256':ASHA,'normalization_sha256':ZSHA,'counts':v['counts'],'symbolic_checks':s if False else v['symbolic_checks'],'cells':[0,4102,7808],'modes':261,'degree':12,'accepted_dependencies':v['accepted_dependencies'],'checks_sha256':sha(E/'checks.json'),'actual_proof_review':pr,'actual_output_review':r,'postreview':postrec,'files':dict(sorted(p.items())),'scope':v['scope']+' Mandatory REVIEW_RESOLUTION and separately later own adjudication retained.'};write(E/'verdict.json',out);print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(p),'sha256':sha(E/'verdict.json')}))

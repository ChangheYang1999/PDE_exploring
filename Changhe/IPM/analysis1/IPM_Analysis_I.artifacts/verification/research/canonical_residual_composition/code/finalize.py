from common import *
from extract import build

def complete():
 pins={};main=load(E/'checks.json');chain=load(E/'chain_checks.json');scope=load(E/'scope_checks.json')
 need(main['status']=='PASS_COMPLETE_CANONICAL_RESIDUAL_PREMISE_COMPOSITION_REQUIRES_ACTUAL_REVIEW' and chain['status']=='PASS_COMPLETE_DECLARED_BOUNDARY_AND_TAIL_INPUT_CHAIN' and scope['status']=='PASS_PRIMARY_JOINT_REGIONAL_AND_BOTH_GLOBAL_CEILINGS','all actual application stages')
 need(main['counts']=={'spans':1558,'child_cells':7809,'H_shapes':3265568,'moment_shapes':813276,'endpoint_H_two_exact_boxes':4192,'endpoint_moment_two_exact_boxes':1044,'exact_knot_geometry':4674} and chain['counts']=={'direct_parent_edges':31,'outer_particular_scalar_equations_each_exact_engine':17748,'outer_exponents':1864,'outer_monomials':3508,'middle_complete_headers':2} and chain['rejections']=={'146':3,'156':5,'duplicate_nonfinite_json':4,'negative_ball_radius':1},'complete exact application counts')
 need(chain['main_checks_sha256']==sha(E/'checks.json') and when(main['utc'])<when(chain['start_utc'])<when(chain['utc'])<when(scope['start_utc'])<when(scope['utc']),'sequential actual application')
 for v in [main,chain,scope]:merge(pins,v)
 for n in ['checks.json','chain_checks.json','scope_checks.json']:pin(pins,E/n)
 for key,(n,h) in DEPS.items():
  dep=load(B/n);pin(pins,n,h);need(main['accepted_dependencies'][key]=={'path':n,'sha256':h,'utc':dep['utc']} and when(dep['utc'])<when(main['start_utc']),'application after actual accepted inputs')
 need(load(E/'completion_extract.json')==build(),'literal complete evidence projection')
 for p in D.rglob('*'):
  if p.is_file() and p.name not in ['verdict.json','postreview_record.json','POSTREVIEW_ADJUDICATION.md']:pin(pins,p)
 proof=auth(pins,'canonical_residual_composition_proof','CONFIRM_CONDITIONAL_COMPOSITION_PROOF',load(D/'proof_files.json'))
 return pins,main,chain,scope,proof
if __name__=='__main__':
 pins,main,chain,scope,proof=complete();tag='canonical_residual_composition_actual';review=auth(pins,tag,'CONFIRM_CANONICAL_RESIDUAL_ARCHIVE_PREMISE_DISCHARGED',load(D/'actual_files.json'));need(when(scope['utc'])<when(review['start_utc']) and when(proof['end_utc'])<when(review['start_utc']),'actual review after all new evidence and proof objections')
 postrec=post(pins,tag,review,E/'postreview_record.json',D/'POSTREVIEW_ADJUDICATION.md')
 for n,h in pins.items():need(sha(B/n)==h,'all unchanged final pins')
 x={'utc':now(),'status':'CONFIRMED_CANONICAL_RESIDUAL_ARCHIVE_PREMISE_DISCHARGED','counts':main['counts'],'chain_counts':chain['counts'],'public_suprema':scope['public_suprema'],'public_norms':scope['public_norms'],'accepted_dependencies':main['accepted_dependencies'],'actual_output_review':review,'proof_review':proof,'postreview':postrec,'files':dict(sorted(pins.items())),'scope':main['scope']+' The same premise is also discharged separately for primary31, joint46, inner45, outer43 and primary assembly124, with SCOPE_ADDENDUM and all inherited qualifications.'};write(E/'verdict.json',x);print(json.dumps({'utc':x['utc'],'status':x['status'],'pins':len(pins),'sha256':sha(E/'verdict.json')}))

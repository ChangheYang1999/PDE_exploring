"""Separate source acceptance and complete actual numerical application gates."""
from common import *
import argparse,subprocess,ast
import replay

def review(stage,mode=None):
 fs=load(D/'review_files.json')['workflow'];question=(D/'workflow_question.txt').read_text();tag='derivative_regional_workflow'
 if stage=='actual':
  assert mode in MODES
  fs=fs+[str((E/mode/'actual_extract.json').relative_to(ROOT))]
  question=(D/'actual_question.txt').read_text()+f'\nApplication mode: {mode}.\n';tag='derivative_regional_'+mode+'_actual'
 assert len(fs)==len(set(fs)) and not (REV/(tag+'_request.txt')).exists()
 cmd=[sys.executable,'-B',str(REV/'focused_review.py'),'--tag',tag,'--max-tokens','15000','--question',question]
 for n in fs:cmd+=['--file',n]
 raise SystemExit(subprocess.run(cmd,cwd=ROOT,timeout=555).returncode)

def projection(mode):
 p=E/mode;x=load(p/'inputs.json');current=extract(mode);assert {k:v for k,v in x.items() if k!='utc'}==current
 sc=load(p/'checks.json');r=load(p/'replay.json');f=load(p/'input_freeze.json')
 assert sc['status']=='COMPUTED_REGIONAL_SCALAR_COMPOSITION_REQUIRES_REPLAY_AND_ACTUAL_REVIEW' and r['status']=='PASS_INTEGER_REGIONAL_EXTRACTION_SUMS_ROOT_ENDPOINTS_AND_DECIMAL_REPLAY'
 assert sc['mode']==r['mode']==mode and sc['inputs_sha256']==r['inputs_sha256']==f['inputs_sha256']==sha(p/'inputs.json') and r['checks_sha256']==sha(p/'checks.json')
 assert r['source_sha256']==sha(D/'code/replay.py') and replay.inspect(x,sc)==r['counts']
 assert f['source_freeze_sha256']==sc['source_freeze_sha256']==sha(E/'source_freeze.json')
 assert when(x['utc'])<when(f['utc'])<when(sc['start_utc'])<when(sc['utc'])<when(r['utc'])
 return {'status':'EXACT_COMPLETE_REGIONAL_COMPOSITION_REVIEW_PROJECTION','mode':mode,'inputs':{k:v for k,v in x.items() if k!='files'},'checks':sc,'replay':r,'input_freeze':f,'inherited_pin_count':len(x['files'])}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['workflow','freeze','extract_actual','actual','finalize']);ap.add_argument('--mode',choices=MODES);args=ap.parse_args()
 if args.stage=='workflow':assert args.mode is None;review('workflow')
 if args.stage=='freeze':
  assert args.mode is None
  for n in FIXED:
   if n.endswith('.py'):ast.parse((D/n).read_text())
  p={};files=load(D/'review_files.json')['workflow'];assert {str((D/n).relative_to(ROOT)) for n in FIXED}<=set(files) and len(files)==len(set(files))
  sc=load(E/'selfcheck.json');assert sc['source_sha256']==sha(D/'code/selfcheck.py') and sc['status']=='PASS_REGIONAL_SCALAR_WORKFLOW_SELF_CHECKS'
  rev=auth(p,'derivative_regional_workflow','CONFIRM_REGIONAL_COMPOSITION_SOURCE_PENDING_PARENT_FINALS',files,(D/'workflow_question.txt').read_text());post(p,'derivative_regional_workflow',rev,D/'WORKFLOW_ADJUDICATION')
  write(E/'source_freeze.json',{'utc':now(),'status':'IMMUTABLE_REGIONAL_COMPOSITION_SOURCE_BEFORE_PARENT_EXTRACTION','files':dict(sorted({str((D/n).relative_to(ROOT)):sha(D/n) for n in FIXED}.items()))});print('SOURCE_FROZEN_NO_NUMERICAL_APPLICATION');return
 assert args.mode in MODES;mode=args.mode;p=E/mode
 if args.stage=='actual':assert (p/'actual_extract.json').exists();review('actual',mode)
 xp=projection(mode)
 if args.stage=='extract_actual':write(p/'actual_extract.json',{'utc':now(),**xp});return
 old=load(p/'actual_extract.json');assert {k:v for k,v in old.items() if k!='utc'}==xp
 pins=source();inputs=load(p/'inputs.json')
 for n,h in inputs['files'].items():pin(pins,n,h)
 for n in ['inputs.json','input_freeze.json','checks.json','replay.json','actual_extract.json']:pin(pins,p/n)
 tag='derivative_regional_'+mode+'_actual';fs=load(D/'review_files.json')['workflow']+[str((p/'actual_extract.json').relative_to(ROOT))];question=(D/'actual_question.txt').read_text()+f'\nApplication mode: {mode}.\n'
 rev=auth(pins,tag,'CONFIRM_COMPLETE_CANONICAL_REGIONAL_DERIVATIVE_COMPOSITION',fs,question);ad=post(pins,tag,rev,p/'POSTREVIEW_ADJUDICATION');assert when(old['utc'])<when(rev['start_utc'])
 rehash(pins);c=xp['checks'];v={'utc':now(),'status':'CONFIRMED_COMPLETE_CANONICAL_REGIONAL_DERIVATIVE_COMPOSITION','mode':mode,'parents':inputs['parents'],'norms':inputs['norms'],'geometry_exact':inputs['geometry_exact'],'regions':inputs['regions'],'region_sq_upper_exact':inputs['region_sq_upper_exact'],'regional_squared_ceilings':c['regional_squared_ceilings'],'published_whole_plane_norm_ceilings':c['published_whole_plane_norm_ceilings'],'sharper_exact_parent_norm_ceilings':c['sharper_exact_parent_norm_ceilings'],'original179_whole_plane_ceilings':inputs['original179_whole_plane_ceilings'],'actual_review':rev,'own_postreview':ad,'files':dict(sorted(pins.items())),'scope':'Upper bounds for canonical epsilon and epsilon-D epsilon in the stated weak weighted H1 norm. Printed regional squares and their displayed-sum whole-plane ceilings are consistent. No old19389W validation, inverse, X3 distance, nonlinear closure or decisive endpoint.'}
 write(p/'verdict.json',v);print(json.dumps({k:v[k] for k in ['utc','status','mode','published_whole_plane_norm_ceilings']}))
if __name__=='__main__':main()

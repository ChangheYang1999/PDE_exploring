"""Freeze, review and accept only concrete complete evidence."""
from protocol import *
import argparse,subprocess,ast

def extract(tag):
 p,deps=source();s=load(OUT/(tag+'_summary.json'));a=load(OUT/(tag+'_audit.json'));r=load(OUT/(tag+'_replay.json'));indices=SMOKE if tag=='smoke' else list(range(89))
 assert s['status']=='COMPUTED_OUTER_DERIVATIVE_CELLS_REQUIRES_AUDIT_AND_REVIEW' and s['indices']==indices and s['cells']==len(indices) and s['full_exterior']==(tag=='full')
 assert a['status']=='PASS_COMPLETE_EXTERIOR_SAVED_OUTPUT_AUDIT' and a['indices']==indices and a['cells']==len(indices) and a['full_exterior']==s['full_exterior']
 assert a['required_replay_cells']==(SMOKE if tag=='smoke' else sorted(set(REPLAY+a['maximum_contribution_cells'])))
 assert r['status']=='PASS_SELECTED_COMPLETE_EXTERIOR_DERIVATIVE_REPLAY' and r['full_exterior']==s['full_exterior'] and r['required_cells']==a['required_replay_cells']==[v['cell'] for v in r['results']]
 assert a['summary_sha256']==r['summary_sha256']==sha(OUT/(tag+'_summary.json')) and r['audit_sha256']==sha(OUT/(tag+'_audit.json')) and a['rows_sha256']==s['rows_sha256']==sha(OUT/(tag+'_rows.jsonl'))
 assert when(s['utc'])<when(a['start_utc'])<when(a['utc'])<when(r['start_utc'])<when(r['utc'])
 rehash(s['files']);rehash(r['pieces'])
 for n,h in r['pieces'].items():pin(p,n,h)
 for name in ['summary.json','audit.json','replay.json','rows.jsonl','restarts.jsonl']:pin(p,OUT/(tag+'_'+name))
 x={'status':'EXACT_EXTERIOR_DERIVATIVE_REVIEW_PROJECTION','full_exterior':s['full_exterior'],'summary':{k:v for k,v in s.items() if k!='files'},'audit':a,'replay':r,'parents':deps,'source_freeze_sha256':sha(OUT/'source_freeze.json')}
 if tag=='full':
  prep=load(OUT/'preparation_acceptance.json');assert prep['status']=='CONFIRMED_OUTER_DERIVATIVE_CELL_PREPARATION_ONLY';rehash(prep['files']);q=load(OUT/'queue_status.json');assert q['status']=='COMPLETE_OUTER_DERIVATIVE_COMPUTATION_AUDIT_REPLAY_REQUIRES_ACTUAL_REVIEW'
  for n,key in [('summary.json','summary_sha256'),('audit.json','audit_sha256'),('replay.json','replay_sha256')]:assert q[key]==sha(OUT/('full_'+n))
  assert when(r['utc'])<when(q['utc']);x['queue']=q;x['preparation_sha256']=sha(OUT/'preparation_acceptance.json');pin(p,OUT/'preparation_acceptance.json');pin(p,OUT/'queue_status.json')
  for n,h in prep['files'].items():pin(p,n,h)
 return p,x

def main():
 ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['freeze','extract_preparation','preparation','accept','extract_actual','actual','finalize']);args=ap.parse_args()
 if args.stage=='freeze':
  p,deps=parents()
  for n in ['code/engine_arb.py','code/engine_iv.py']:assert sha(DIR/n)==sha(ROOT/'research/outer_derivative_cells'/n)
  for n in OWN:
   if n.endswith('.py'):ast.parse((DIR/n).read_text())
  assert load(OUT/'proof_first.json')['sha256']==sha(DIR/'PROOF.md') and load(OUT/'proof_first.json')['code_files']==[]
  r=auth(p,'outer_derivative_cells_engines','CONFIRM_OUTER_DERIVATIVE_CELL_ENGINES_ONLY');post(p,'outer_derivative_cells_engines',r,'ENGINE_ADJUDICATION');cells()
  write(OUT/'parent_manifest.json',{'utc':now(),'parents':deps,'files':dict(sorted(parents()[0].items()))})
  write(OUT/'source_freeze.json',{'utc':now(),'status':'IMMUTABLE_EXTERIOR_DERIVATIVE_SOURCE_BEFORE_SMOKE','files':dict(sorted({str((DIR/n).relative_to(ROOT)):sha(DIR/n) for n in OWN}.items()))});print('SOURCE_FROZEN');return
 if args.stage in ['preparation','actual']:
  tag='outer_derivative_cells_v2_'+args.stage;assert not (REV/(tag+'_request.txt')).exists();fs=load(DIR/'review_files.json')[args.stage]
  cmd=[sys.executable,'-B',str(REV/'focused_review.py'),'--tag',tag,'--max-tokens','15000','--question',(DIR/(args.stage+'_question.txt')).read_text()]
  for n in fs:cmd+=['--file',n]
  raise SystemExit(subprocess.run(cmd,cwd=ROOT,timeout=555).returncode)
 full=args.stage in ['extract_actual','finalize'];tag='full' if full else 'smoke';p,x=extract(tag);name='actual' if full else 'preparation'
 if args.stage.startswith('extract_'):write(OUT/(name+'_extract.json'),{'utc':now(),**x});return
 old=load(OUT/(name+'_extract.json'));assert {k:v for k,v in old.items() if k!='utc'}==x;pin(p,OUT/(name+'_extract.json'))
 reviewtag='outer_derivative_cells_v2_'+name;verdict='CONFIRM_COMPLETE_CANONICAL_EXTERIOR_DERIVATIVE_NORM_BOUNDS' if full else 'CONFIRM_OUTER_DERIVATIVE_CELL_PREPARATION_ONLY'
 r=auth(p,reviewtag,verdict,load(DIR/'review_files.json')[name],(DIR/(name+'_question.txt')).read_text());po=post(p,reviewtag,r,'POSTREVIEW_ADJUDICATION' if full else 'PREFLIGHT_ADJUDICATION');assert when(old['utc'])<when(r['start_utc']);rehash(p)
 z={'utc':now(),'status':'CONFIRMED_COMPLETE_CANONICAL_EXTERIOR_DERIVATIVE_NORM_BOUNDS' if full else 'CONFIRMED_OUTER_DERIVATIVE_CELL_PREPARATION_ONLY','full_exterior':full,'cells':89 if full else 3,'source_freeze_sha256':sha(OUT/'source_freeze.json'),'strict_decimal_ceilings':x['summary']['norms']['strict_decimal_ceilings'],'actual_review':r,'own_postreview':po,'parents':x['parents'],'files':dict(sorted(p.items())),'scope':'Two new X norm upper bounds for canonical eps and eps-D eps on r>=exp(b). Numerical claim only if full_exterior is true. No oldW validation, inverse or endpoint.'}
 out=OUT/('verdict.json' if full else 'preparation_acceptance.json');write(out,z);print(json.dumps({'utc':z['utc'],'status':z['status'],'pins':len(p),'sha256':sha(out),'strict_decimal_ceilings':z['strict_decimal_ceilings']}),flush=True)
if __name__=='__main__':main()

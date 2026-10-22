from protocol import *
import argparse,subprocess
ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['preparation','extract_actual','actual']);args=ap.parse_args()
if args.stage=='extract_actual':
    p,deps,f=source();s=load(OUT/'full_summary.json');a=load(OUT/'full_audit.json');r=load(OUT/'full_replay.json');q=load(OUT/'queue_status.json');prep=load(OUT/'preparation_acceptance.json')
    assert s['full_middle'] is a['full_middle'] is r['full_middle'] is True and s['cells']==a['cells']==7809
    assert q['status']=='COMPLETE_DERIVATIVE_NORM_COMPUTATION_AUDIT_REPLAY_REQUIRES_ACTUAL_REVIEW'
    for name,key in [('full_summary.json','summary_sha256'),('full_audit.json','audit_sha256'),('full_replay.json','replay_sha256')]:assert q[key]==sha(OUT/name)
    assert a['summary_sha256']==r['summary_sha256']==sha(OUT/'full_summary.json') and r['audit_sha256']==sha(OUT/'full_audit.json')
    assert when(s['utc'])<when(a['start_utc'])<when(a['utc'])<when(r['start_utc'])<when(r['utc'])<when(q['utc'])
    rehash(s['files']);rehash(prep['files'])
    write(OUT/'actual_extract.json',{'utc':now(),'status':'EXACT_COMPLETE_DERIVATIVE_NORM_REVIEW_PROJECTION','summary':{k:v for k,v in s.items() if k!='files'},'audit':{k:v for k,v in a.items() if k!='files'},'replay':r,'queue':q,'parents':deps,'source_freeze_sha256':sha(OUT/'source_freeze.json'),'preparation_sha256':sha(OUT/'preparation_acceptance.json')})
else:
    tag='full_derivative_norm_'+args.stage;assert not (REV/(tag+'_request.txt')).exists();files=load(DIR/'review_files.json')[args.stage]
    cmd=[sys.executable,str(REV/'focused_review.py'),'--tag',tag,'--max-tokens','15000','--question',(DIR/(args.stage+'_question.txt')).read_text()]
    for n in files:cmd+=['--file',n]
    raise SystemExit(subprocess.run(cmd,cwd=ROOT,timeout=555).returncode)

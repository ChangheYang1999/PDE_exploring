"""Self-test of the step runners (run_g2_steps_v5.sh and later, run_g3_steps.sh) with the verifier's 31 fixtures (adapted from c4-ver/scripts/check_g2_runner_v4_semantics.py;
SPEC v9.10) plus 6 typed guard-record negatives (lead ruling 9) = 37 cases. N11 (lead 10:58Z): the typed negatives discriminate: typed_returncode_bool uses False (== 0 in
Python, so an untyped comparison would accept it) and typed_finish_before_start swaps started/finished with the step mtime inside [min, max]; for every typed_* case the
runner's stated reason must appear in its output (recorded per case as reason_found). The result records the sha256 of the runner source and of this script (E10).
Usage: runner_selftest_v5.py [runner path]   (env FIXTURE_STEPS='t2 t26' selects the two step names; G3 runner: FIXTURE_STEPS='selftest selftest2' and G2_OUTROOT-style paths are the runner's own)  -> outputs/g2/runner_selftest_v5/<utc>/result.json; exit 0 only if all 37 cases (the verifier's 31 fixtures plus 6 typed negatives) match the strict requirement.
Original header: Independent local fixtures for the captured v4 G2 shell runner.

No scientific provider is executed. Only two literal lane-root substitutions
are made. All fixtures stay in this verifier lane. No JS/TS, servers, listeners,
RLScience, remote compute, Lean/lake, git mutation or external messaging.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import os
import subprocess
import time

import sys
ROOT=Path(__file__).resolve().parents[1]
SOURCE=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'bin/run_g2_steps_v5.sh'
OUT=ROOT/'outputs/g2/runner_selftest_v5'/time.strftime('%Y%m%dT%H%M%SZ',time.gmtime())
assert not OUT.exists()
OUT.mkdir(parents=True)
source=SOURCE.read_bytes()
(OUT/'runner.source.sh').write_bytes(source)
started=dt.datetime.now(dt.timezone.utc).isoformat(); tick=time.monotonic()
STUB=r'''import json, os, sys, time
from pathlib import Path
args=sys.argv[1:]; mode=os.environ['FIXTURE_MODE']
sess=Path(args[args.index('--session-dir')+1]); root=sess.parents[2]
with (root/'guard_calls.jsonl').open('a') as f: f.write(json.dumps(args)+'\n')
if args[0]=='init':
 if mode=='init_refusal': sys.exit(73)
 (sess/'runs').mkdir(parents=True)
 if mode in ('guard_refusal_stale','zero_new_stale'):
  p=sess/'runs/20000101_g2_t2';p.mkdir();(p/'result.json').write_text(json.dumps({'success':True,'returncode':0}))
 sys.exit(0)
if mode=='guard_refusal_stale': sys.exit(73)
cmd=args[args.index('--')+1:]; label=args[args.index('--label')+1]
if mode=='zero_new_stale': sys.exit(0)
st=time.time(); p=sess/'runs'/('20990101_'+label); p.mkdir()
if mode=='two_new': (sess/'runs'/('20990102_'+label)).mkdir()
out=Path(cmd[3]); out.parent.mkdir(parents=True,exist_ok=True)
sj={'passed':True,'fixture':mode,'checks':[{'check':'fixture_check','passed':True}]}
if mode=='step_passed_false':sj['passed']=False
if mode=='step_check_false':sj['checks'][0]['passed']=False
if mode=='step_check_string_false':sj['checks'][0]['passed']='false'
if mode=='step_check_integer_one':sj['checks'][0]['passed']=1
if mode=='step_check_missing_passed':sj['checks']=[{'check':'fixture_check'}]
if mode=='step_missing_checks':sj.pop('checks')
if mode=='step_empty_checks':sj['checks']=[]
if mode=='step_null_checks':sj['checks']=None
if mode=='step_passed_integer_one':sj['passed']=1
if mode!='missing_output': out.write_text(json.dumps(sj)+'\n')
if mode=='step_malformed':out.write_text('{broken\n')
ft=time.time()
# Positive fixtures declare an exact midpoint timestamp independently of the filesystem clock.
if out.exists(): os.utime(out,((st+ft)/2,(st+ft)/2))
if mode=='predates_move':
 st=st-2; os.utime(out,(ft-1,ft-1))
if mode=='old_output': os.utime(out,(st-10,st-10))
if mode=='just_before_interval': os.utime(out,(st-0.5,st-0.5))
if mode=='just_after_interval': os.utime(out,(ft+0.5,ft+0.5))
rec={'success':mode!='unsuccessful','returncode':7 if mode=='failed_returncode' else 0,
     'command':cmd+['unexpected'] if mode=='mismatched_command' else cmd,
     'started_time':st,'finished_time':ft,'wall_seconds':ft-st,'run_id':p.name,
     'stop_reasons':['guard pressure stop'] if mode=='stop_reasons' else []}
if mode=='typed_returncode_bool': rec['returncode']=False     # N11: False == 0 in Python; only a typed check refuses it
if mode=='typed_success_int': rec['success']=1
if mode=='typed_stop_reasons_none': rec['stop_reasons']=None
if mode=='typed_started_bool': rec['started_time']=True
if mode=='typed_wall_negative': rec['wall_seconds']=-1.0
if mode=='typed_finish_before_start': rec['finished_time']=st; rec['started_time']=ft    # N11: swapped; the step mtime (st+ft)/2 stays inside [min, max]
if mode!='missing_result': (p/'result.json').write_text(json.dumps(rec)+'\n')
if mode=='malformed_result': (p/'result.json').write_text('{broken\n')
sys.exit(73 if mode=='guard_nonzero_new_success' else 0)
'''
cases=[('success',0),('success_replaces_stale',0),('init_refusal',1),
       ('preexisting_session',2),('manifest_mismatch',3),('malformed_manifest',3),
       ('guard_refusal_stale',4),('guard_nonzero_new_success',4),
       ('zero_new_stale',5),('two_new',5),('mismatched_command',6),
       ('missing_output',6),('old_output',6),('unsuccessful',6),
       ('failed_returncode',6),('stop_reasons',6),('missing_result',6),
       ('malformed_result',6),('just_before_interval',6),('just_after_interval',6),('predates_move',0),('step_passed_false',6),('step_check_false',6),('step_check_string_false',6),('step_check_integer_one',6),('step_check_missing_passed',6),('step_missing_checks',6),('step_empty_checks',6),('step_null_checks',6),('step_passed_integer_one',6),('step_malformed',6),('typed_returncode_bool',6),('typed_success_int',6),('typed_stop_reasons_none',6),('typed_started_bool',6),('typed_wall_negative',6),('typed_finish_before_start',6)]
rows=[]
for mode,expected in cases:
 fix=OUT/mode
 for rel in ('env/bin','work/research/hardware','work/research860/tests','outputs/manifests','tmp'):
  (fix/rel).mkdir(parents=True,exist_ok=True)
 (fix/'env/bin/python').symlink_to(ROOT/'env/bin/python')
 (fix/'work/research/hardware/guard.py').write_text(STUB)
 text=source.decode();old=str(ROOT);assert text.count(old)==2, text.count(old)
 script=fix/'runner.sh';script.write_text(text.replace(old,str(fix)))
 manifest={'files':[],'frozen_181_closure':[]}
 if mode=='manifest_mismatch': manifest['files']=[{'path':'missing','sha256':'0'*64}]
 mf=fix/'outputs/manifests/code_manifest_fixture.json'
 mf.write_text('{broken\n' if mode=='malformed_manifest' else json.dumps(manifest)+'\n')
 (fix/'policy.json').write_text('{}\n')
 if mode=='preexisting_session': (fix/os.environ.get('FIXTURE_OUTROOT','outputs/g2')/'session_fixture_s1/runs').mkdir(parents=True)
 if mode in ('success_replaces_stale','guard_refusal_stale','predates_move'):
  p=fix/os.environ.get('FIXTURE_OUTROOT','outputs/g2')/'fixture'/(os.environ.get('FIXTURE_STEPS','t2 t26').split()[0]+'.json');p.parent.mkdir(parents=True,exist_ok=True)
  p.write_text('{"stale":true}\n')
 env=os.environ.copy()
 for key in ('G2_GUARD','G2_OUTROOT','G2_TESTDIR'):env.pop(key,None)
 env.update(FIXTURE_MODE=mode,PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(fix/'tmp'),
            OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
 steps=os.environ.get('FIXTURE_STEPS','t2 t26').split(); command=['bash',str(script),'fixture','s1','1',str(fix/'policy.json')]+steps
 t=time.monotonic();p=subprocess.run(command,cwd=ROOT,env=env,capture_output=True,text=True,timeout=30)
 (fix/'stdout.txt').write_text(p.stdout);(fix/'stderr.txt').write_text(p.stderr)
 callsfile=fix/'guard_calls.jsonl'
 calls=[json.loads(line) for line in callsfile.read_text().splitlines()] if callsfile.exists() else []
 runs=[row for row in calls if row[0]=='run']
 chainsafe=(len(runs)<=1) if expected else len(runs)==2
 TYPED_REASONS={'typed_returncode_bool':'is not the int 0','typed_success_int':'success','typed_stop_reasons_none':'stop_reasons','typed_started_bool':'timing fields','typed_wall_negative':'timing fields','typed_finish_before_start':'start <= finish'}
 runlog=''
 for lg in fix.glob(os.environ.get('FIXTURE_OUTROOT','outputs/g2')+'/fixture/run.log'): runlog+=lg.read_text()
 reason_found=(TYPED_REASONS[mode] in (p.stdout+p.stderr+runlog)) if mode in TYPED_REASONS else None
 row={'case':mode,'returncode':p.returncode,'expected_strict_returncode':expected,
      'matches_strict_requirement':p.returncode==expected and chainsafe and (reason_found is not False),'reason_found':reason_found,'expected_reason':TYPED_REASONS.get(mode),
      'guard_run_calls':len(runs),'seconds':time.monotonic()-t,
      'moved_stale_files':[str(f.relative_to(fix)) for f in fix.glob(os.environ.get('FIXTURE_OUTROOT','outputs/g2')+'/fixture/*.stale_*')]}
 rows.append(row);print(json.dumps(row),flush=True)
result={'started_utc':started,'finished_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
        'seconds':time.monotonic()-tick,'source':str(SOURCE),
        'source_sha256':hashlib.sha256(source).hexdigest(),'source_unchanged':source==SOURCE.read_bytes(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'patch_scope':'Exactly two literal lane-root substitutions per fixture; unchanged control flow.',
        'scientific_provider_executed':False,'cases':rows,
        'strict_failures':[r['case'] for r in rows if not r['matches_strict_requirement']]}
(OUT/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2)); print('SELFTEST V5 PASS' if not result['strict_failures'] else 'SELFTEST V5 FAIL'); sys.exit(0 if not result['strict_failures'] else 1)

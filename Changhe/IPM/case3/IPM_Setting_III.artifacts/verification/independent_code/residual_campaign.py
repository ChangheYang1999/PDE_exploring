from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,json,os,argparse
ap=argparse.ArgumentParser();ap.add_argument('--tag',default='corrected');ap.add_argument('--levels',default='0,1,2');ap.add_argument('--files',nargs='+');ap.add_argument('--points-file');args=ap.parse_args()
files=args.files or ['coupled_N48_a1','res_p23_N96M16','res_p23_N192M24','res_p23_N256M32']
for level in [int(v) for v in args.levels.split(',')]:
 for stem in files:
    log=Path('runs')/(stem+'_'+args.tag+'_q'+str(level)+'.log')
    cmd=[sys.executable,'independent_code/run_candidate_residuals.py','evidence/'+stem+'.npz','--level',str(level),'--tag',args.tag,'--all-points']
    if args.points_file:cmd+=['--points-file',args.points_file]
    print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'start':cmd,'log':str(log)}),flush=True)
    with log.open('w') as stream:
        p=subprocess.run(cmd,stdout=stream,stderr=subprocess.STDOUT,timeout=3500)
    print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'finished':stem,'level':level,'returncode':p.returncode}),flush=True)
    if p.returncode:sys.exit(p.returncode)

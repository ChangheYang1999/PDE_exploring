"""Single-core continuation, waiting for the already running positive-sign worker."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,time,os
ROOT=Path(__file__).resolve().parents[1]
PY='python3'
ENV=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
BASE=ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/verification'
def run(args,log,limit=535):
 print(datetime.now(timezone.utc).isoformat(),'START',args,flush=True)
 with (ROOT/log).open('w') as f:
  p=subprocess.run([PY]+args,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=limit,env=ENV)
 assert p.returncode==0,(args,p.returncode)
 print(datetime.now(timezone.utc).isoformat(),'DONE',args,flush=True)
started=time.monotonic()
while not all((BASE/f'a50_n32768_m256_v2_s1_r{i}_{i+8192}.json').exists() for i in range(0,32768,8192)):
 assert time.monotonic()-started<600,'Positive worker did not complete in time'
 time.sleep(5)
run(['code/run_projection_refinement.py','1'],'11_lattice_pole_constraints/axis_projection_stieltjes/verification/refinement_worker1.log')
run(['code/combine_projection_lower.py','a50_n32768_m256_v2'],'11_lattice_pole_constraints/axis_projection_stieltjes/verification/refinement_combination.log')
for part in ['plus','mid','minus']:
 base='11_lattice_pole_constraints/axis_clamped_layercake/verification/a99_b1_'+part+'_131072'
 if (ROOT/(base+'.json')).exists():continue
 run(['code/certify_axis_clamp_layercake.py','--alpha','99/100','--b','1','--part',part,'--cells','131072','--out',base+'.json'],base+'.log')
run(['code/combine_axis_clamp_layercake.py','a99_b1'],'11_lattice_pole_constraints/axis_clamped_layercake/verification/a99_b1_combination.log')
run(['code/check_full_range_profile_v2.py'],'07_diagonal_identity_term/full_range_profile/verification/independent_diagnostics_v2.log')
print(datetime.now(timezone.utc).isoformat(),'COMPLETE',flush=True)

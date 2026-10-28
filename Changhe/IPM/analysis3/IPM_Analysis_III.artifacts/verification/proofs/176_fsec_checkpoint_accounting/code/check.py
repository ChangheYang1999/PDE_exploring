import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
import numpy as np
TOP=Path(__file__).resolve().parents[1]; LANE=TOP.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rd=LANE.parent/'s2-num/work/runs/S1'
snap=json.loads((TOP/'evidence/initial_snapshot.json').read_text())
for group in snap['groups']:
 for row in group['files']:assert sha(rd/row['name'])==row['sha256']
assert not list(rd.glob('base_*.npz'))
parts=sorted(rd.glob('part_*.npz'));ckpts=sorted(rd.glob('ckpt_*.npz'))
assert len(parts)==len(ckpts)==4
full=set(range(1569)); all_seen=set();rows=[]
for wid in range(4):
 schedule=set(range(wid,1569,4))
 with np.load(rd/f'part_{wid}.npz',allow_pickle=False) as z:
  diag=json.loads(str(z['diag']));assert diag['cells']==len(schedule)
 cp=[p for p in ckpts if p.name.startswith(f'ckpt_{wid}_')];assert len(cp)==1
 with np.load(cp[0],allow_pickle=False) as z:
  done=[int(x) for x in z['done']];diag=json.loads(str(z['diag']))
 assert len(done)==len(set(done))==diag['cells'];assert done==sorted(schedule)[:len(done)]
 assert not all_seen.intersection(schedule);all_seen.update(schedule)
 rows.append({'worker':wid,'full_count':len(schedule),'duplicate_prefix_count':len(done)})
assert all_seen==full
correct=F(10,2);duplicate=F(11,3);missing=F(9)
assert correct==5 and duplicate!=correct and missing!=correct
old_base={0}; latest_checkpoint={1}; desired={0,1}; scheduled=desired-latest_checkpoint
assert scheduled & old_base
out={'date':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_ACCOUNTING_COUNTEREXAMPLES','actual_parts_only_partition':'PASS','actual_checkpoint_overlap':'PASS','workers':rows,'scalar_squared_singular_values':{'correct':str(correct),'duplicate_prefix':str(duplicate),'missing_base':str(missing)},'repeat_resume_recomputes_old_base':'PASS','proof_sha256':sha(TOP/'PROOF.md'),'script_sha256':sha(Path(__file__)),'snapshot_sha256':sha(TOP/'evidence/initial_snapshot.json'),'code_snapshots':{p.name:sha(p) for p in (TOP/'evidence').glob('*.py')}}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

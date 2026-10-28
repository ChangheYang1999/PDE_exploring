import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,subprocess
import numpy as np
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1];NUM=LANE.parent/'s2-num';snap=ROOT/'evidence/fsec_assemble_v2.py';shutil.copy2(NUM/'work/fsec_assemble.py',snap)
notes=(NUM/'NOTES_FOR_TEAM.md').read_text();note=notes[notes.index('## 2026-10-28 12:38Z'):notes.index('## 2026-10-28 10:16Z')];(ROOT/'evidence/note24.md').write_text(note)
rows=[]
for tag,ids in [('wrong_same_cardinality',[1,2]),('incomplete',[0]),('correct',[0,1])]:
 rd=ROOT/'evidence'/tag;rd.mkdir(exist_ok=True)
 meta={'tag':tag,'new':[['rem','fixture',1],['rem','fixture',2]],'cvec':[0,0],'nworkers':1,'NMAX':2,'Mh':3,'stride':1};(rd/'meta.json').write_text(json.dumps(meta)+'\n');np.savez(rd/'part_0.npz',GZ=np.eye(2),BY=np.eye(2),done=np.array(ids),diag=json.dumps({'cells':len(ids)}))
 p=subprocess.run(['python3','-B',str(snap),str(rd),'2'],capture_output=True,text=True,timeout=30,env=os.environ.copy());(rd/'stdout.log').write_text(p.stdout);(rd/'stderr.log').write_text(p.stderr);assert p.returncode==0 and (rd/'fsec_result.json').exists()
 rows.append({'tag':tag,'done':ids,'expected':[0,1],'returncode':p.returncode,'result_written':True,'warned':'WARNING' in p.stdout,'set_equality':set(ids)=={0,1}})
obj={'date':datetime.now(timezone.utc).isoformat(),'verdict':'REFUTED_GENERIC_UNION_EQUALITY_CHECK','fixtures':rows,'snapshot_sha256':hashlib.sha256(snap.read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(ROOT/'evidence/check.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))

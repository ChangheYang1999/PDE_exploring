import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
import numpy as np
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1];NUM=LANE.parent/'s2-num';E=ROOT/'evidence'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
snap=E/'fsec_assemble_v3.py';shutil.copyfile(NUM/'work/fsec_assemble.py',snap);prod=E/'fsec_producer_v3.py';shutil.copyfile(NUM/'work/fsec.py',prod)
notes=(NUM/'NOTES_FOR_TEAM.md').read_text();start=notes.index('## 2026-10-28 13:00Z');end=notes.index('\n## ',start+3);(E/'num_note26.md').write_text(notes[start:end]+'\n')
cases=[('correct',{'part_0.npz':[0,1]},False,True),('wrong_equal_count',{'part_0.npz':[1,2]},False,False),('missing',{'part_0.npz':[0]},False,False),('extra',{'part_0.npz':[0,1,2]},False,False),('overlap',{'base_0.npz':[0],'part_0.npz':[0,1]},False,False),('duplicate_inside',{'part_0.npz':[0,0,1]},False,False),('explicit_partial',{'part_0.npz':[0]},True,True)]
rows=[]
for tag,blocks,partial,success in cases:
 rd=E/tag;rd.mkdir(exist_ok=True)
 meta={'tag':tag,'new':[['rem','fixture',1],['rem','fixture',2]],'cvec':[0,0],'nworkers':1,'NMAX':2,'Mh':3,'stride':1,'cells_expected':[0,1]};(rd/'meta.json').write_text(json.dumps(meta)+'\n')
 for name,ids in blocks.items():np.savez(rd/name,GZ=np.eye(2),BY=np.eye(2),done=np.array(ids),diag=json.dumps({'cells':len(ids)}))
 env=os.environ.copy();env.pop('FSEC_PARTIAL',None)
 if partial:env['FSEC_PARTIAL']='1'
 run=subprocess.run(['python3','-B',str(snap),str(rd),'2'],env=env,capture_output=True,text=True,timeout=30)
 (rd/'stdout.log').write_text(run.stdout);(rd/'stderr.log').write_text(run.stderr)
 result=rd/'fsec_result.json';assert (run.returncode==0)==success and result.exists()==success
 if success:
  x=json.loads(result.read_text());assert x['partial']==partial and x['missing_cells']==int(partial)
 rows.append({'tag':tag,'returncode':run.returncode,'result_written':result.exists(),'expected_success':success,'partial':partial})
source=prod.read_text();assert 'VM[m] = qx' in source and 'qx[:m] = [2.0 * ((-1) ** (m - 1 - j)) * (2 * m - 2 * j - 1) for j in range(m)]' in source
out={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED_REPAIRS','fixtures':rows,'scope':'cell accounting checks and exact input templates only; no numerical operator certificate','hashes':{str(p.relative_to(LANE)):sha(p) for p in (ROOT/'PROOF.md',Path(__file__),snap,prod,E/'num_note26.md')}}
(E/'check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

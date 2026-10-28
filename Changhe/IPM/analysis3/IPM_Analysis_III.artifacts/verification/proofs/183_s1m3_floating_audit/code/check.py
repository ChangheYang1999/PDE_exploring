import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil
import numpy as np
from scipy.linalg import eigh
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1];NUM=LANE.parent/'s2-num';run=NUM/'work/runs/S1M3'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files=sorted(run.glob('part_*.npz'));ckpts=sorted(run.glob('ckpt_*.npz'));assert len(files)==4;assert not list(run.glob('base_*.npz'))
allids=[];rows=[];G=np.zeros((84,84));B=G.copy();C=G.copy();D=G.copy();ckids=[]
for p in files+ckpts:
 with np.load(p,allow_pickle=False) as z:
  diag=json.loads(str(z['diag']))
  if 'done' in z.files:ids=list(map(int,z['done']))
  else:
   assert p in files
   wid=int(p.stem.split('_')[1]);ids=list(range(wid,1569,4));assert diag['cells']==len(ids)
  g=z['GZ'];b=z['BY'];assert len(ids)==len(set(ids));assert np.isfinite(g).all() and np.isfinite(b).all();assert g.shape==b.shape==(84,84)
  if p in files:allids+=ids;G+=g;B+=b
  else:ckids+=ids;C+=g;D+=b
  rows.append({'name':p.name,'cells':len(ids),'cell_ids':ids,'sha256':sha(p),'IDs_source':'stored' if 'done' in z.files else 'legacy full-run round-robin assignment and final worker count'})
 shutil.copy2(p,ROOT/'evidence/source'/p.name)
assert len(allids)==1569 and set(allids)==set(range(1569));assert len(set(ckids))==len(ckids);assert set(ckids)<=set(allids)
meta=json.loads((run/'meta.json').read_text());new=meta['new'];G=(G+G.T)/2;B=(B+B.T)/2;ans={}
selections={'m1':[i for i,x in enumerate(new) if x[2]==1],'m2':[i for i,x in enumerate(new) if x[2]==2],'pure_splines':[i for i,x in enumerate(new) if 'out' not in x[1] and 'in' not in x[1]],'all':list(range(84))}
for name,idx in selections.items():
 g=G[np.ix_(idx,idx)];b=B[np.ix_(idx,idx)];ev,vec=eigh(b,g);x=vec[:,0];x/=np.linalg.norm(x);gq=float(x@g@x);bq=float(x@b@x);di=np.sqrt(np.diag(g));diB=np.sqrt(np.diag(b));erG=float(1.3e-12*(abs(x)@di)**2);erB=float(1.3e-12*(abs(x)@diB)**2);top=np.argsort(-abs(x))[:10];eg=np.linalg.eigvalsh(g/np.outer(di,di))
 ans[name]={'n':len(idx),'singular_values_float':np.sqrt(np.maximum(ev[:8],0)).tolist(),'G_normalized_smallest_eigenvalue':float(eg[0]),'G_normalized_condition':float(eg[-1]/eg[0]),'gq':gq,'bq':bq,'unproved_rounding_model_G':erG,'unproved_rounding_model_B':erB,'weakest_coefficients':[[new[idx[j]],float(x[j])] for j in top],'full_vector':x.tolist(),'indices':idx}
old=NUM/'work/runs/S1';GG=np.zeros((42,42));BB=GG.copy()
for p in sorted(old.glob('part_*.npz')):
 with np.load(p,allow_pickle=False) as z:GG+=z['GZ'];BB+=z['BY']
i=selections['m1'];m1G=G[np.ix_(i,i)];m1B=B[np.ix_(i,i)];comp={'G_relative_frobenius_difference':float(np.linalg.norm(m1G-GG)/np.linalg.norm(GG)),'B_relative_frobenius_difference':float(np.linalg.norm(m1B-BB)/np.linalg.norm(BB))}
for name in ['fsec.py','fsec_assemble.py','s1_robust.py']:
 shutil.copy2(LANE/'proofs/176_fsec_checkpoint_accounting/evidence'/name,ROOT/'evidence/source'/name)
for p in [run/'meta.json',run/'fsec_result.json',NUM/'logs/s1m3_assemble.log',NUM/'logs/s1m3_robust.log']:shutil.copy2(p,ROOT/'evidence/source'/p.name)
log=(NUM/'logs/s1m3_prod.log').read_text();assert 'sampling: 1569 cells over 4 workers' in log;assert 'resume:' not in log
for wid in range(4):
 assert f'worker {wid} done: {len(range(wid,1569,4))} cells' in log
 pp=next(p for p in ckpts if p.name.startswith(f'ckpt_{wid}_'))
 with np.load(pp,allow_pickle=False) as z:assert list(map(int,z['done']))==list(range(wid,1569,4))[:len(z['done'])]
shutil.copy2(NUM/'logs/s1m3_prod.log',ROOT/'evidence/source/s1m3_prod.log')
obj={'date':datetime.now(timezone.utc).isoformat(),'verdict':'PASS_FOR_ACCOUNTING_AND_FLOAT_RECOMPUTATION_ONLY','parts_coverage':'exactly1569 cells0..1568 once','checkpoint_duplicate_cells':len(ckids),'files':rows,'results':ans,'m1_S1_comparison':comp,'source_files':{p.name:sha(p) for p in (ROOT/'evidence/source').iterdir() if p.is_file()},'proof_sha256':sha(ROOT/'PROOF.md'),'code_sha256':sha(Path(__file__)),'scope':'FLOATING numerical observations; no certified operator singular value, injectivity, or complement inverse'}
(ROOT/'evidence/check.json').write_text(json.dumps(obj,indent=2)+'\n');np.savez(ROOT/'evidence/parts_matrices.npz',G=G,B=B)
print('Coverage1569, checkpointduplicates',len(ckids));print(comp)
for name,row in ans.items():print(name,row['singular_values_float'][:4],'normalized cond',row['G_normalized_condition'],'b/heuristic_error',row['bq']/row['unproved_rounding_model_B'],'top',row['weakest_coefficients'][:4])

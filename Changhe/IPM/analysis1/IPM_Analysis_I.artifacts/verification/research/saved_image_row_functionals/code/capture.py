"""Read-only source capture and exact JSON export of six preselected saved directions."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import numpy as np,json,gzip,hashlib
B=Path(__file__).resolve().parents[3];D=B/'research/saved_image_row_functionals';NUM=B.parent/'ipmA-num'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def exact(v):return str(F.from_float(float(v)))
selection=[('M16_s8_o40_p4','L2q',[0,2,4]),('M16_s8_o40_p4','H1q',[0]),('M24_s16_o40_p4','L2q',[0]),('M24_s16_o40_p4','H1q',[0])];pins={};sources=[];out=[];scalars=0
for case,row,indices in selection:
 stem='c2gram2_'+case+'_H1m_NJ1_rows'+row
 for suffix in ['_vec.npz','_imgeval_Fminus.json']:
  original=NUM/'runs/c2'/(stem+suffix);target=D/'sources'/(stem+suffix);data=original.read_bytes();digest=hashlib.sha256(data).hexdigest()
  with target.open('xb') as f:f.write(data)
  need(sha(original)==sha(target)==digest,'stable source capture');pins[str(target.relative_to(B))]=digest;sources.append({'original':str(original.resolve()),'captured':str(target.relative_to(B)),'sha256':digest,'bytes':len(data)})
 with np.load(D/'sources'/(stem+'_vec.npz'),allow_pickle=False) as z:
  n=int(z['Ne']);M=int(z['Mout']);t=z['t_eval'];w=z['w_i'];fi=z['Fminus_img'];g=z['Fminus_hGh'];sigma=z['Fminus_sigma'];need(t.shape==w.shape==(n,) and fi.shape==(n*M,5) and g.shape==sigma.shape==(5,) and str(z['ROWS'])==row and M==40 and int(z['NJ'])==1,'saved source shapes/types');need(all(a.dtype==np.dtype('float64') and np.all(np.isfinite(a)) for a in [t,w,fi,g,sigma]),'finite original binary64 arrays');need(np.all(np.diff(t)>0) and np.all(w>0) and np.all(g>0),'positive saved geometry');saved=json.loads((D/'sources'/(stem+'_imgeval_Fminus.json')).read_text());need(saved['section']=='Fminus' and saved['rows_mode_of_run']==row and saved['vec']=='runs/c2/'+stem+'_vec.npz' and saved['sigma_saved']==sigma.tolist(),'actual saved diagnostic identity')
  rec={'case':case,'row_mode':row,'stem':stem,'Ne':n,'Mout':M,'t_exact':[exact(x) for x in t],'w_exact':[exact(x) for x in w],'directions':[]};scalars+=2*n
  for j in indices:
   rec['directions'].append({'index':j,'g_exact':exact(g[j]),'sigma_exact':exact(sigma[j]),'image_exact':[[exact(fi[i*M+N,j]) for N in range(M)] for i in range(n)],'saved_quotients_exact':{r:exact(saved['quotients'][r][j]) for r in ['L2','L2q','H1','H1q']}});scalars+=n*M+6
  out.append(rec)
source=NUM/'src/c2_img_eval.py';target=D/'sources/c2_img_eval.py';data=source.read_bytes()
with target.open('xb') as f:f.write(data)
need(sha(source)==sha(target),'stable evaluator snapshot');pins[str(target.relative_to(B))]=sha(target);sources.append({'original':str(source.resolve()),'captured':str(target.relative_to(B)),'sha256':sha(target),'bytes':len(data)})
with gzip.open(D/'data_exact/selected_arrays.json.gz','xt') as f:json.dump(out,f,separators=(',',':'));f.write('\n')
for p in [D/'data_exact/selected_arrays.json.gz',D/'PROOF.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
manifest={'utc':datetime.now(timezone.utc).isoformat(),'status':'CAPTURED_EXACT_FINITE_ARRAYS_NOT_A_CERTIFICATE','selection':selection,'sources':sources,'selected_directions':6,'selected_image_values':174160,'exported_scalars':scalars,'files':dict(sorted(pins.items()))};need(sum(x['Ne']*x['Mout']*len(x['directions']) for x in out)==174160,'all selected image values')
with (D/'data_exact/manifest.json').open('x') as f:json.dump(manifest,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in manifest.items() if k not in ['sources','files']},indent=2))

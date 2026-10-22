from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,shutil,numpy as np
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT.parents[1]; NUM=BASE.parent/'ipmA-num'
ROWS={'L2':'NJ0','L2q':'NJ1_rowsL2q','H1':'NJ1_rowsH1','H1q':'NJ1_rowsH1q'}
KEYS=['k','L','tmin','t0','Mh','nF','ntot','next','A0','Bm','col_m','col_kind','col_label','G_diag','G_ref_cols','G_Jinner_col','G_KP_TAU_cols','ref_names','ref_ta_tb']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest={'utc':datetime.now(timezone.utc).isoformat(),'sources':{},'copied':{},'vectors':{},'metadata':{},'source_arrays':{}}
def pin(p,copy=False):
 rel=str(p.relative_to(BASE.parent));manifest['sources'][rel]=sha(p)
 if copy:
  target=ROOT/'sources'/p.name
  assert not target.exists();shutil.copyfile(p,target);manifest['copied'][str(target.relative_to(BASE))]=sha(target)
 return rel
for nm in ['c2_gram2.py','c2_fminus.py']:pin(NUM/'src'/nm,True)
meta=[]
for stem in ['p2_re','p4_re2','p6_re']:
 p=NUM/'runs/c2'/f'c2raw_M16_s16_{stem}_cols.pkl';key=pin(p,True);meta.append(p.read_bytes());manifest['metadata'][stem]=key
assert meta[0]==meta[1]==meta[2]
all_rows={};retained={};base_arrays=None;array_count=0;payload_bytes=0
for row,tail in ROWS.items():
 vals=[];retained[row]=[]
 for ppc,stem in [(2,'p2'),(4,'p4_re2'),(6,'p6')]:
  p=NUM/'runs/c2'/f'c2gram2_M16_s16_{stem}_H1m_{tail}.json';pin(p,True);d=json.loads(p.read_text());sec=d['sections']['Fminus']
  assert (d['Mh'],d['stride'],d['Mout'],d['ppc'],d['rows_mode'],d['mode'])==(16,16,40,ppc,row,'H1m')
  assert d['thresh']==1e-10 and d['NJ']==(0 if row=='L2' else 1)
  assert len(sec['sigma_small5'])==5 and all(x>0 for x in sec['sigma_small5'])
  vals.append([F(x) for x in sec['sigma_small5']])
  counts=[sec[k] for k in ['ncol','n_constraints','constraint_rank','nfree','n_kept','n_kept_at_1em12']]
  assert counts==([1955,32,32,1923,1866,1887] if row=='L2' else [1955,64,64,1891,1834,1855])
  retained[row].append({'ppc':ppc,'counts':counts,'Ne':d['Ne'],'nrows':d['nrows'],'n_collocation_rows':d['n_collocation_rows']})
  vp=p.with_name(p.stem+'_vec.npz');key=pin(vp);manifest['vectors'][f'{row}_{ppc}']=key
  with np.load(vp,allow_pickle=False) as z:
   arrays={k:(z[k].shape,z[k].dtype.str,z[k].tobytes(order='C')) for k in KEYS}
  if base_arrays is None:base_arrays=arrays
  assert arrays==base_arrays
  manifest['source_arrays'][f'{row}_{ppc}']={k:{'shape':list(sh),'dtype':ty,'sha256':hashlib.sha256(v).hexdigest(),'bytes':len(v)} for k,(sh,ty,v) in arrays.items()}
  array_count+=len(arrays);payload_bytes+=sum(len(v[2]) for v in arrays.values())
 all_rows[row]=vals
records=[];maxima=[]
for row,vals in all_rows.items():
 for i,(p,q) in enumerate([(2,4),(4,6)]):
  rs=[]
  for j,(a,b) in enumerate(zip(vals[i],vals[i+1])):
   delta=b-a;rel=abs(delta)/a;assert delta!=0;rs.append(rel)
   records.append(dict(row=row,p=p,q=q,j=j,old=str(a),new=str(b),delta=str(delta),relative=str(rel),relative_to_new=str(abs(delta)/b)))
  M=max(rs);n=(M*10**12).__floor__()
  maxima.append(dict(row=row,p=p,q=q,index=rs.index(M),maximum=str(M),window=[str(F(n,10**12)),str(F(n+1,10**12))]))
(ROOT/'data_exact/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_LITERAL_COMPARISONS',comparisons=len(records),nonzero=len(records),array_comparisons=array_count,payload_bytes=payload_bytes,keys=KEYS,retained=retained,records=records,maxima=maxima)
(ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('records','keys','retained')},indent=2))

"""Capture immutable completed vector inputs and bind their metadata to frozen columns."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,os,sys,pickle,io
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/saved_vector_external_constraints'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def need(v,s):
 if not v:raise ValueError(s)
class Reader(pickle.Unpickler):
 def find_class(self,m,n):
  if m in ['numpy.core.multiarray','numpy._core.multiarray'] and n in ['_reconstruct','scalar']:return getattr(np._core.multiarray,n)
  if m=='numpy' and n in ['ndarray','dtype']:return getattr(np,n)
  raise ValueError('unsupported pickle global')
oldp=B/'research/external_constraint_rank/evidence/verdict.json';old=json.loads(oldp.read_text());need(sha(oldp)=='e569bd20c174f863d6ba47ef3e16070870f3ea10fcff6ea79d5f2c98ed433542','accepted exact source matrix');pins=dict(old['files']);pins[str(oldp.relative_to(B))]=sha(oldp)
for n,h in pins.items():need(sha(B/n)==h,'inherited digest')
rows=[]
for M,stride,nf in [(16,16,1953),(24,8,5257)]:
 name='c2gram2_M%d_s%d_p4_H1m_NJ1_rowsH1q_vec.npz'%(M,stride);p=B.parent/'ipmA-num/runs/c2'/name;raw=p.read_bytes();digest=hashlib.sha256(raw).hexdigest();need(sha(p)==digest,'stable source vector capture');target=D/'sources'/name
 with target.open('xb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
 colsrel='research/gram_internal_jumps/sources/c2raw_M%d_s%d_p4_cols.pkl'%(M,stride);cols=Reader(io.BytesIO((B/colsrel).read_bytes())).load()['cols'];need(len(cols)==nf,'frozen column count')
 with np.load(target,allow_pickle=False) as v:
  need(int(v['Mh'])==M and int(v['nF'])==nf and int(v['NJ'])==1 and str(v['ROWS'])=='H1q','metadata family');h=v['Fminus_h'];need(h.shape==(int(v['next']),5) and h.dtype==np.dtype('float64') and np.isfinite(h).all(),'five finite coefficient vectors');need((v['col_m']==np.array([r[0] for r in cols])).all() and (v['col_label']==np.array([r[2] for r in cols])).all(),'mode and label arrays');need(int(v['ntot'])==nf+2+M and int(v['next'])==nf+2+M+4,'saved extended coordinate count');need(np.count_nonzero(h[nf+2:])==0,'Fminus coordinates beyond KP/TAU are zero')
  row={'M':M,'stride':stride,'nF':nf,'n_extended':int(v['next']),'vector_path':str(target.relative_to(B)),'vector_sha256':digest,'original_path':str(p),'cols_path':colsrel,'cols_sha256':sha(B/colsrel),'joins_hex':[float(v[x]).hex() for x in ['tmin','t0']],'script_sha256_claim':str(v['script_sha256']),'shape':list(h.shape),'column_dtype':h.dtype.str,'scope':'Source hash is a saved metadata claim, not execution attestation.'}
  src=B/'notes/constraint_rank_watch/c2_gram2.py';row['matches_frozen_source_snapshot']=row['script_sha256_claim']==sha(src);need(row['matches_frozen_source_snapshot'],'claimed source matches inspected snapshot')
 pins[str(target.relative_to(B))]=digest;rows.append(row)
proof=json.loads((D/'evidence/proof_first.json').read_text());need(proof['proof_sha256']==sha(D/'PROOF.md'),'prior proof')
for p in [D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'final pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SAVED_VECTOR_CAPTURE_AND_METADATA_BINDING_ONLY','families':rows,'files':dict(sorted(pins.items())),'scope':'Metadata and frozen-input binding only. No trace arithmetic, saved-vector exact constraint membership or execution attestation yet.'}
with (D/'data_exact/manifest.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'families':[{k:r[k] for k in ['M','nF','n_extended','shape','matches_frozen_source_snapshot']} for r in rows]}))

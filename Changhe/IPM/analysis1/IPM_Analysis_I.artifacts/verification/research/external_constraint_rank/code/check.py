"""Separate selected-source import, elimination and permutation determinant check."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from itertools import permutations
import pickle,io,json,hashlib,sys,os
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/external_constraint_rank'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def need(v,s):
 if not v:raise ValueError(s)
class Reader(pickle.Unpickler):
 def find_class(self,m,n):
  if m in ['numpy.core.multiarray','numpy._core.multiarray'] and n in ['_reconstruct','scalar']:return getattr(np._core.multiarray,n)
  if m=='numpy' and n in ['ndarray','dtype']:return getattr(np,n)
  raise ValueError('forbidden pickle global')
a=json.loads((D/'data_exact/minors.json').read_text());need(a['status']=='COMPUTED_EXACT_EXTERNAL_MINOR_INPUTS_REQUIRES_INDEPENDENT_CHECK','primary status');pins=dict(a['files']);checks={'source_columns':0,'matrix_entries':0,'permutation_terms':0,'elimination_pivots':0}
for n,h in pins.items():need(sha(B/n)==h,'source digest')
for rec in a['records']:
 cols=Reader(io.BytesIO((B/rec['source']).read_bytes())).load()['cols'];M=rec['M'];need(len(rec['blocks'])==M and rec['external_rank']==4*M and rec['external_kernel_coefficient_dimension']==len(cols)+2-4*M,'family dimensions');indices=[]
 for m,block in enumerate(rec['blocks']):
  need(block['mode']==m,'mode identity');mat=[[F(0)]*4 for _ in range(4)]
  for j,entry in enumerate(block['columns']):
   idx=entry['column_index'];mode,pc,label=cols[idx];need(mode==m and label==['in1','in2','out1','out2'][j]==entry['label'] and len(pc)==1,'original selected entry');start,end,alpha,coeff=pc[0];need(list(map(F,map(float,coeff)))==[F(1)] and F(float(alpha))==F(entry['exponent_exact']),'exact coefficient/exponent');row=0 if j<2 else 2;sign=1 if j<2 else -1;join=end if j<2 else start;need(F(float(join))==F(rec['joins_exact'][row//2])==F(entry['join_exact']),'exact join');need(np.isneginf(start) if j<2 else np.isposinf(end),'half-line support');mat[row][j]=F(sign);mat[row+1][j]=sign*F(float(alpha));indices.append(idx);checks['source_columns']+=1
  expected=[list(map(F,row)) for row in block['minor_exact']];need(mat==expected,'source-derived minor');checks['matrix_entries']+=16;det=F(0)
  for perm in permutations(range(4)):
   inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4));term=F((-1)**inv)
   for i in range(4):term*=mat[i][perm[i]]
   det+=term;checks['permutation_terms']+=1
  need(det==F(block['determinant_exact']) and det!=0,'permutation determinant');r=[row[:] for row in mat];product=F(1)
  for j in range(4):
   pivot=next(i for i in range(j,4) if r[i][j]);
   if pivot!=j:r[j],r[pivot]=r[pivot],r[j];product=-product
   value=r[j][j];product*=value;checks['elimination_pivots']+=1
   for i in range(j+1,4):
    fac=r[i][j]/value;r[i]=[x-fac*y for x,y in zip(r[i],r[j])]
  need(product==det,'elimination determinant')
 need(len(indices)==len(set(indices))==4*M,'disjoint selected columns')
need(checks=={'source_columns':160,'matrix_entries':640,'permutation_terms':960,'elimination_pivots':160},'counts')
for p in [D/'data_exact/minors.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'final input digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_EXTERNAL_RANK_SOURCE_ELIMINATION_AND_DETERMINANT_CHECK','counts':checks,'families':[{k:r[k] for k in ['M','raw_function_columns','Fminus_columns_including_KP_TAU','external_rank','external_kernel_coefficient_dimension','joins_exact']} for r in a['records']],'files':dict(sorted(pins.items())),'scope':a['scope']}
with (D/'evidence/output_audit.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:out[k] for k in ['utc','status','counts','families']}))

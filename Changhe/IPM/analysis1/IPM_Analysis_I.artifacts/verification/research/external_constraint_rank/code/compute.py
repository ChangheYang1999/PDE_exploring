"""Exact export and block-minor check of selected stored exponential columns."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import pickle,io,json,hashlib,sys,os
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/external_constraint_rank';pins={}
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
class Reader(pickle.Unpickler):
 def find_class(self,m,n):
  allowed={('numpy._core.multiarray','_reconstruct'):np._core.multiarray._reconstruct,('numpy.core.multiarray','_reconstruct'):np._core.multiarray._reconstruct,('numpy','ndarray'):np.ndarray,('numpy','dtype'):np.dtype,('numpy._core.multiarray','scalar'):np._core.multiarray.scalar,('numpy.core.multiarray','scalar'):np._core.multiarray.scalar};check((m,n) in allowed,'pickle global');return allowed[m,n]
def pin(p,h=None):
 n=str(p.relative_to(B));actual=sha(p);check(h is None or actual==h,'source pin');check(n not in pins or pins[n]==actual,'conflict');pins[n]=actual
vpath=B/'research/gram_internal_jumps/evidence/verdict.json';pin(vpath,'73a8e425d304e46d23f10dc1b8e08131b8fc5df381cd670a813374a90529fe5e');v=json.loads(vpath.read_text())
for n,h in v['files'].items():pin(B/n,h)
records=[]
for M,name in [(16,'c2raw_M16_s16_p4_cols.pkl'),(24,'c2raw_M24_s8_p4_cols.pkl')]:
 p=B/'research/gram_internal_jumps/sources'/name;check(str(p.relative_to(B)) in pins,'accepted original columns');raw=Reader(io.BytesIO(p.read_bytes())).load();cols=raw['cols'];by={(int(m),lab):(i,pc) for i,(m,pc,lab) in enumerate(cols)};check(len(by)==len(cols),'unique mode labels');check(set(int(m) for m,pc,lab in cols)==set(range(M)),'all angular modes');blocks=[];joins=set()
 for m in range(M):
  selected=[];exponents=[]
  for label in ['in1','in2','out1','out2']:
   index,pc=by[m,label];check(len(pc)==1,'one entire exponential piece');a,b,alpha,c=pc[0];check(len(c)==1 and F(float(c[0]))==1,'unit pure exponential');alpha=F(float(alpha));exponents.append(alpha)
   if label.startswith('in'):check(np.isneginf(a) and np.isfinite(b),'inner support');join=F(float(b));side='LEFT';other='-infinity'
   else:check(np.isfinite(a) and np.isposinf(b),'outer support');join=F(float(a));side='RIGHT';other='+infinity'
   selected.append({'column_index':index,'mode':m,'label':label,'support_side':side,'join_exact':str(join),'other_endpoint':other,'exponent_exact':str(alpha),'constant_exact':'1'})
  aa,bb,cc,dd=exponents;check(aa!=bb and cc!=dd,'distinct exponents');check(selected[0]['join_exact']==selected[1]['join_exact'] and selected[2]['join_exact']==selected[3]['join_exact'],'same within-pair joins');left,right=F(selected[0]['join_exact']),F(selected[2]['join_exact']);check(left<right,'ordered joins');joins.add((left,right));det=(bb-aa)*(dd-cc);check(det!=0,'nonzero block determinant');blocks.append({'mode':m,'columns':selected,'minor_exact':[['1','1','0','0'],[str(aa),str(bb),'0','0'],['0','0','-1','-1'],['0','0',str(-cc),str(-dd)]],'determinant_exact':str(det)})
 check(len(joins)==1,'all modes same joins');records.append({'M':M,'source':str(p.relative_to(B)),'raw_function_columns':len(cols),'Fminus_columns_including_KP_TAU':len(cols)+2,'external_rank':4*M,'external_kernel_coefficient_dimension':len(cols)+2-4*M,'joins_exact':list(map(str,next(iter(joins)))),'blocks':blocks})
for p in [D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__)]:pin(p)
check(json.loads((D/'evidence/proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md'),'proof-first bytes')
for n,h in pins.items():check(sha(B/n)==h,'final digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_EXACT_EXTERNAL_MINOR_INPUTS_REQUIRES_INDEPENDENT_CHECK','records':records,'counts':{'mode_blocks':40,'selected_columns':160},'files':dict(sorted(pins.items())),'scope':'Exact external trace matrix only. No retained-Q, numerical singular spectrum, internal matching, Sobolev membership or endpoint assertion.'}
with (D/'data_exact/minors.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'families':[{k:r[k] for k in ['M','external_rank','external_kernel_coefficient_dimension']} for r in records]}))

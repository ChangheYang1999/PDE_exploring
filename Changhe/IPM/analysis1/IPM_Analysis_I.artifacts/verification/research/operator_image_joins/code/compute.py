from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import hashlib, io, json, pickle, sys
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3]; D=B/'research/operator_image_joins'
def sha(p):
 with p.open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()
def check(v,s):
 if not v: raise ValueError(s)
def enc(q): return str(q.numerator)+'/'+str(q.denominator)
def horner(c,t):
 z=F(0)
 for a in reversed(c): z=z*t+a
 return z
class Reader(pickle.Unpickler):
 def find_class(self,m,n):
  allow={('numpy._core.multiarray','_reconstruct'):np._core.multiarray._reconstruct,('numpy.core.multiarray','_reconstruct'):np._core.multiarray._reconstruct,('numpy','ndarray'):np.ndarray,('numpy','dtype'):np.dtype,('numpy._core.multiarray','scalar'):np._core.multiarray.scalar,('numpy.core.multiarray','scalar'):np._core.multiarray.scalar}
  check((m,n) in allow,'pickle global'); return allow[m,n]
prior=B/'research/gram_conforming_repair/evidence/verdict.json'; pinrecord=json.loads(prior.read_text()); pins={}
for n,s in pinrecord['files'].items(): check(sha(B/n)==s,'prior hash '+n); pins[n]=s
p=B/'research/gram_conforming_repair/evidence/compute.json'; saved=json.loads(p.read_text()); records=[]; totals={'columns':0,'pieces':0,'derivative_traces':0,'joins':0,'nonzero_joins':0,'columns_with_jump':0,'value_traces':0}
for rec in saved['records']:
 meta=Reader(io.BytesIO((B/rec['source']).read_bytes())).load(); rows=[]; maxjump=F(0); nz=0
 for col in rec['columns']:
  m,pcs,label=meta['cols'][col['column_index']]; check(m==0 and label==col['label'],'column binding'); check(len(pcs)==len(col['pieces']),'piece count')
  values=[]; derivatives=[]; nodes=[]
  for (a,b,al,cc),q in zip(pcs,col['pieces']):
   a,b=F(float(a)),F(float(b)); w=b-a; c=[F(float(v)) for v in cc]; d0=F(q['correction_constant']); d1=F(q['correction_linear'])
   check(al==0 and w>0 and a==F(q['a_exact']) and b==F(q['b_exact']),'piece binding')
   repaired=c.copy(); repaired[0]+=d0; repaired[1]+=d1
   vl,vr=repaired[0],horner(repaired,w); check(vl==F(q['beta_left']) and vr==F(q['beta_right']),'exact repaired values')
   dc=[j*repaired[j] for j in range(1,len(repaired))]; dl,dr=dc[0],horner(dc,w)
   values.append((vl,vr)); derivatives.append((dl,dr)); nodes.append(a); totals['pieces']+=1; totals['derivative_traces']+=2; totals['value_traces']+=2
  nodes.append(b); check(values[0][0]==values[-1][1]==0 and all(values[j-1][1]==values[j][0] for j in range(1,len(values))),'C0 includes supports')
  jumps=[derivatives[0][0]]+[derivatives[j][0]-derivatives[j-1][1] for j in range(1,len(pcs))]+[-derivatives[-1][1]]
  jnz=[j for j,z in enumerate(jumps) if z]; check(len(jnz)>0,'claim every selected repair has a derivative jump'); nz+=len(jnz); maxjump=max(maxjump,*map(abs,jumps)); totals['columns']+=1; totals['columns_with_jump']+=bool(jnz); totals['joins']+=len(jumps); totals['nonzero_joins']+=len(jnz)
  rows.append({'column_index':col['column_index'],'label':label,'nodes_exact':list(map(enc,nodes)),'derivative_traces_exact':[[enc(a),enc(b)] for a,b in derivatives],'derivative_jumps_exact':list(map(enc,jumps)),'nonzero_join_indices':jnz,'first_witness':{'join_index':jnz[0],'t_exact':enc(nodes[jnz[0]]),'jump_exact':enc(jumps[jnz[0]])}})
 records.append({'source':rec['source'],'M':rec['M'],'N':rec['N'],'columns':rows,'nonzero_joins':nz,'max_abs_derivative_jump_exact':enc(maxjump),'max_abs_derivative_jump_float_orientation_only':float(maxjump),'single_mode_images_outside_H1':rec['M']*len(rows)})
for p in [prior,p,D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__)]: pins[str(p.relative_to(B))]=sha(p)
check(json.loads((D/'evidence/proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md'),'proof first')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_C0_REPAIRED_DERIVATIVE_JUMP_AUDIT','totals':totals,'records':records,'files':dict(sorted(pins.items())),'scope':'Every audited single angular column has a local H1 image obstruction under PROOF hypotheses. No retained subspace, numerical spectrum, inverse or endpoint conclusion.'}
p=D/'evidence/compute.json'; check(not p.exists(),'immutable output'); p.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({'utc':out['utc'],'status':out['status'],'totals':totals,'records':[{k:r[k] for k in ['M','N','nonzero_joins','max_abs_derivative_jump_float_orientation_only','single_mode_images_outside_H1']} for r in records]}))

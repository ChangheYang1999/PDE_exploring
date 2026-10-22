from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,pickle,io,ast,sys
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_jump_rank'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
class Reader(pickle.Unpickler):
 globals=[]
 def find_class(self,m,n):
  self.globals.append([m,n])
  allow={('numpy._core.multiarray','_reconstruct'):np._core.multiarray._reconstruct,('numpy.core.multiarray','_reconstruct'):np._core.multiarray._reconstruct,('numpy','ndarray'):np.ndarray,('numpy','dtype'):np.dtype,('numpy._core.multiarray','scalar'):np._core.multiarray.scalar,('numpy.core.multiarray','scalar'):np._core.multiarray.scalar}
  check((m,n) in allow,'unapproved pickle global');return allow[m,n]
def q(x):return F(float(x))
def enc(x):return str(x.numerator)+'/'+str(x.denominator)
def horner(c,x):
 v=F(0)
 for z in reversed(c):v=v*x+q(z)
 return v
V=B/'research/gram_internal_jumps';prior=json.loads((V/'evidence/verdict.json').read_text());check(prior['status']=='CONFIRMED_SAVED_POLYNOMIAL_JUMPS_AND_NONCONFORMING_EXTERNAL_JOIN_KERNEL','prior verdict');pins={}
for n,h in prior['files'].items():check(sha(B/n)==h,'prior pin');pins[n]=h
records=[]
def canon(pcs):return [(float(a).hex(),float(b).hex(),float(al).hex(),tuple(float(z).hex() for z in c)) for a,b,al,c in pcs]
for stem in ['c2raw_M16_s16_p4_cols','c2raw_M24_s8_p4_cols']:
 p=V/'sources'/(stem+'.pkl');data=Reader(io.BytesIO(p.read_bytes())).load();cols=data['cols'];lo,hi=data['cells'][0],data['cells'][-1];modes=sorted(set(m for m,pcs,lab in cols));check(modes==list(range(len(modes))),'contiguous modes');M=len(modes);selected=[]
 for ci,(m,pcs,lab) in enumerate(cols):
  if m!=0 or not lab.startswith('sp') or not pcs or not all(lo<a<b<hi and al==0 for a,b,al,c in pcs):continue
  check(all(pcs[i][1]<=pcs[i+1][0] for i in range(len(pcs)-1)),'pieces disjoint');jump={}
  for t in sorted({x for a,b,al,c in pcs for x in [a,b]}):jump[q(t)]=sum((q(c[0]) for a,b,al,c in pcs if a==t),F(0))-sum((horner(c,q(t)-q(a)) for a,b,al,c in pcs if b==t),F(0))
  piv=min(t for t,v in jump.items() if v);check(piv==q(pcs[0][1]) and q(pcs[0][3][0])==0,'first interior pivot');selected.append((piv,ci,lab,pcs,jump))
 selected.sort();check(len({x[0] for x in selected})==len(selected),'distinct pivot radii');N=len(selected);r=[];zeros=0
 for j,(t,ci,lab,pcs,jump) in enumerate(selected):
  for i in range(j):check(jump.get(selected[i][0],F(0))==0,'exact upper zero');zeros+=1
  copy_indices=[]
  for m in modes:
   found=[(idx,pcc) for idx,(mm,pcc,ll) in enumerate(cols) if mm==m and ll==lab];check(len(found)==1 and canon(found[0][1])==canon(pcs),'exact angular replication');copy_indices.append(found[0][0])
  r.append({'label':lab,'column_indices':copy_indices,'pivot_hex':float(t).hex(),'pivot_exact':enc(t),'diagonal_exact':enc(jump[t]),'support_start_hex':float(pcs[0][0]).hex(),'support_end_hex':float(pcs[-1][1]).hex()})
 caps={'Fminus':len(cols)+2-M*N,'Fminus_noJ':len(cols)+1-M*N,'free':len(cols)+2+M-M*N,'free_noJ':len(cols)+1+M-M*N};ncols={name:cap+M*N for name,cap in caps.items()}
 check(all(x>=0 for x in caps.values()),'dimension nonnegative');records.append({'source':str(p.relative_to(B)),'source_sha256':sha(p),'M':M,'N':N,'selected_coordinate_columns':M*N,'n_function_columns':len(cols),'tested_upper_zeros':zeros,'conforming_dimension_upper_bounds':caps,'section_column_counts':ncols,'pivots':r})
reports=[];caps=records[0]['conforming_dimension_upper_bounds'];ncols=records[0]['section_column_counts']
for p in sorted((B/'research/gram_reference_space/sources').glob('*M16_s16*H1m*.json')):
 z=json.loads(p.read_text());check(z['mode']=='H1m' and z['Mh']==16 and z['stride']==16,'report definition');check(set(z['sections'])==set(caps),'section names')
 for name,sec in z['sections'].items():check(sec['ncol']==ncols[name] and sec['n_kept']>caps[name],'reported orthonormal count exceeds dimension')
 reports.append({'file':str(p.relative_to(B)),'sha256':sha(p),'ppc':z['ppc'],'NJ':z['NJ'],'retained':{name:sec['n_kept'] for name,sec in z['sections'].items()},'conforming_dimension_upper_bounds':caps});pins[str(p.relative_to(B))]=sha(p)
check(len(reports)==6,'six H1m count reports')
for p in [D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__),V/'evidence/verdict.json']:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_TRIANGULAR_JUMP_RANK_AND_REPORTED_COUNT_COMPARISON','method':'Exact rational Horner matrix, all upper-triangle entries, exact mode-copy comparison, finite reported count extraction','records':records,'reported_counts':reports,'files':pins,'scope':'No actual Q assertion; impossibility of X-orthonormal list of stated length within the exact encoded spans. No reconstruction or PDE result.'};p=D/'evidence/compute.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'records':[{k:r[k] for k in ['M','N','selected_coordinate_columns','tested_upper_zeros','conforming_dimension_upper_bounds']} for r in records],'reports':len(reports)}))

from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,pickle,io,ast,sys
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_internal_jumps'
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
manifest=json.loads((D/'evidence/manifest.json').read_text());pins={}
for r in manifest['files']:
 p=B/r['copy'];check(sha(p)==r['sha256'] and p.stat().st_size==r['bytes'],'source pin');pins[r['copy']]=r['sha256']
rows=[];cache={}
for rr in manifest['files'][:4]:
 data=Reader(io.BytesIO((B/rr['copy']).read_bytes())).load();check(set(data)=={'cols','kp_pieces','tau_pieces','cells'},'metadata keys')
 cells=data['cells'];check(cells.ndim==1 and cells.dtype.kind=='f' and cells.dtype.itemsize==8 and len(cells)<1000 and np.all(np.isfinite(cells)),'cells');check(np.all(cells[1:]>cells[:-1]),'ordered cells')
 lo,hi=map(float,[cells[0],cells[-1]]);stats={'columns':len(data['cols']),'eligible_m0_interior_sp_columns':0,'tested_endpoints':0,'nonzero_endpoints':0,'columns_with_nonzero_jump':0};witness=None
 for ci,(m,pcs,lab) in enumerate(data['cols']):
  if int(m)!=0 or not lab.startswith('sp'):continue
  for a,b,alpha,c in pcs:check(c.ndim==1 and c.dtype.kind=='f' and c.dtype.itemsize==8 and len(c)<=8 and np.all(np.isfinite(c)),'polynomial data')
  if not pcs or not all(lo<a<b<hi and alpha==0 for a,b,alpha,c in pcs):continue
  check(all(pcs[i][1]<=pcs[i+1][0] for i in range(len(pcs)-1)),'disjoint sorted')
  stats['eligible_m0_interior_sp_columns']+=1;bad=False
  for t in sorted({float(x) for a,b,al,c in pcs for x in [a,b]}):
   left=sum((horner(c,q(t)-q(a)) for a,b,al,c in pcs if b==t),F(0));right=sum((q(c[0]) for a,b,al,c in pcs if a==t),F(0));delta=right-left
   stats['tested_endpoints']+=1
   if delta:
    bad=True;stats['nonzero_endpoints']+=1
    if witness is None and pcs[0][0]<t<pcs[-1][1]:
     witness={'column_index_zero_based':ci,'mode':int(m),'label':lab,'tmin_hex':lo.hex(),'t0_hex':hi.hex(),'tstar_hex':t.hex(),'pieces':[{'a_hex':float(a).hex(),'b_hex':float(b).hex(),'alpha_hex':float(al).hex(),'coefficients_hex':[float(x).hex() for x in c]} for a,b,al,c in pcs],'left_exact':enc(left),'right_exact':enc(right),'delta_right_minus_left_exact':enc(delta),'delta_float_for_orientation_only':float(delta),'abs_delta_lower':'1/10000000000000000000000','abs_delta_upper':'1/100000000000000'}
     check(F(1,10**22)<abs(delta)<F(1,10**14),'strict illustrative rational bound')
  stats['columns_with_nonzero_jump']+=int(bad)
 check(witness is not None,'actual interior witness');rows.append({'source':rr['copy'],'source_sha256':rr['sha256'],'tmin_hex':lo.hex(),'t0_hex':hi.hex(),'statistics':stats,'witness':witness})
# Source facts only. No execution of the numerical lane source.
tree=ast.parse((D/'sources/src__c2_gram.py').read_text());cons=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='constraints'];check(len(cons)==1,'constraints unique')
join=[n for n in ast.walk(cons[0]) if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='join'];check(len(join)==1 and ast.dump(join[0].iter)==ast.dump(ast.parse('(tmin,t00)',mode='eval').body),'only external joins')
sub=ast.get_source_segment((D/'sources/src__c2_gram.py').read_text(),cons[0]);check('gi < nF' in sub and 'piece_jet(pcs, join, "-", nu) - piece_jet(pcs, join, "+", nu)' in sub,'function only constraints')
lin=(D/'sources/src__lin_assembly.py').read_text();check('sel = (t >= a) & (t < b); sig = t[sel] - a' in lin and 'pv = pv * sig + cc[j]' in lin and 'np.exp(alpha * sig) * pv' in lin,'piece convention')
check('Q = (N @ QN) * Ds[:, None]' in (D/'sources/src__c2_gram.py').read_text(),'postconstraint eigencut scope')
for p in [D/'PROOF.md',D/'evidence/manifest.json',D/'evidence/proof_first.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_HORNER_INTERNAL_JUMP_WITNESSES','method':'Restricted NumPy pickle loader; exact Fraction binary64 values and Horner; AST and source text audit, no lane code or SVD execution','loaded_globals':Reader.globals,'records':rows,'source_scope':'Assuming exterior joins equal metadata cells endpoints; raw NPZ scalar linkage not yet checked. No conclusion about the retained eigenspace.','files':pins}
check(not (D/'evidence/compute.json').exists(),'immutable');(D/'evidence/compute.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'records':[{k:r[k] for k in ['source','statistics']}|{'witness_index':r['witness']['column_index_zero_based'],'witness_label':r['witness']['label'],'delta_float':r['witness']['delta_float_for_orientation_only']} for r in rows]}))

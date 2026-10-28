"""Exact T1-plus-repair coordinates and diagnostic of the floating constraint rows."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from datetime import datetime,timezone
from math import comb
import json,hashlib,sys
sys.set_int_max_str_digits(0)
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
base=ROOT.parent/'s1-num/research/data/n12_m10_exact.json'
trial=ROOT.parent/'s1-num/research/data/nb_test_result.json'
repair=HERE/'algebraic_n12_m10_k16.json'
b=json.loads(base.read_text());r=json.loads(repair.read_text());t=json.loads(trial.read_text())
assert hashlib.sha256(base.read_bytes()).hexdigest()==json.loads((ROOT/'research/08_refits/verification/n12_m10_audit.json').read_text())['source_sha256']
A=defaultdict(Q)
for g in b['generators']:A[g['j'],g['m'],tuple(g['spec'])]+=Q(g['coef'])
for (j,m,k),v in zip(r['additions_order'],r['additions_coefficients']):A[j,m,('mono',k-m)]+=Q(v)
A={k:v for k,v in A.items() if v}
can=defaultdict(Q)
for (j,m,s),a in A.items():
 if s[0]=='mono':can[j,m,m+s[1]]+=a
 else:
  _,w,n=s
  for i in range(n+1):can[j,m,m+w+i]+=a*(-1)**(n-i)*comb(n,i)*comb(n+i,i)
can={k:v for k,v in can.items() if v}
assert can=={tuple(k):Q(v) for k,v in zip(r['canonical_order'],r['canonical_coefficients'])}
keys=[(g['j'],g['m'],tuple(g['spec'])) for g in t['gens']]
assert len(keys)==len(set(keys));assert set(A)<=set(keys)
coefs=[A.get(k,Q(0)) for k in keys]
assert max(map(abs,coefs))<136
C=np.array(t['constraints_rows']);rhs=np.array(t['constraints_rhs']);vec=np.array([float(x) for x in coefs])
canmap={(j,m,('mono',k-m)):Q(v) for (j,m,k),v in zip(r['canonical_order'],r['canonical_coefficients'])}
cvec=np.array([float(canmap.get(k,Q(0))) for k in keys])
stableres=C@vec-rhs;canres=C@cvec-rhs
# Independently check exact leading and first-descendant moments directly in T1.
mom=defaultdict(Q);desc=defaultdict(Q)
c=Q(r['cl']);ps=[(3+1/c-j*(1-1/c))/2 for j in range(6)]
for (j,m,s),a in A.items():
 h=s[1] if s[0]=='mono' else s[1]+s[2]*(s[2]+1)
 mom[j,m]+=a;desc[j,m]+=(ps[j]-m-h)*a
assert all(v==0 for (j,m),v in desc.items() if j<=1)
tail=json.loads((ROOT/'research/10_tail_splice/verification/state131_splice.json').read_text())
want={(int(n)-1,int(m)//2):Q(v) for n,d in tail['homogeneous_potential_orders'].items() for m,v in d['cosine_coefficients'].items()}
assert all(mom.get(k,Q(0))==want.get(k,Q(0)) for k in set(mom)|set(want))
# Direct exact origin strain from canonical fourth-order coefficients.
def strain(j,m,k):
 p=ps[j]
 return {(0,0):4*p*(p-1),(0,1):8*(p-1),(0,2):Q(8),(2,2):Q(-24)}.get((m,k),Q(0))
center=sum((v*strain(j,m,k) for (j,m,k),v in can.items()),Q(0));assert center==1-c
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
out={'utc':now,'status':'EXACT_IDENTITY_CONFIRMED_FLOAT_INITIALIZER','gens':t['gens'],'coefs':vec.tolist(),'exact_coefs':[str(x) for x in coefs],'cl':str(c),'source_hashes':{str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in (base,trial,repair)},'exact_reconstruction_equal':True,'exact_all_six_moments':True,'exact_j01_descendants':True,'exact_center':str(center),'float_max_coefficient':float(np.max(np.abs(vec))),'canonical_float_max_coefficient':float(np.max(np.abs(cvec))),'float_max_constraint_defect':float(np.max(np.abs(stableres))),'canonical_float_max_constraint_defect':float(np.max(np.abs(canres))),'float_worst_rows':[{'row':int(i),'stable_defect':float(stableres[i]),'canonical_defect':float(canres[i])} for i in np.argsort(np.abs(canres))[-15:][::-1]],'scope':'Exact same repaired potential in stable T1-plus-addition coordinates. Float coefs are for LM initialization only; exact_coefs define the audited reference.'}
(HERE/'algebraic_n12_m10_k16_stable_init.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('gens','coefs','exact_coefs')},indent=2))

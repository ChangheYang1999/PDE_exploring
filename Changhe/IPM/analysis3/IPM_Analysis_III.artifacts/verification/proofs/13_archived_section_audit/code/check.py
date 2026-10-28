from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
import numpy as np
root=Path(__file__).resolve().parents[1]; lane=root.parents[1]
base=lane/'research_copy/analysis1/IPM_Analysis_I.artifacts'
p=base/'numerics/data/trial_v2_h0.008.npz'; data=np.load(p,allow_pickle=False)
a=[F.from_float(float(x)) for x in data['Aout'][:,0]];M=len(a)
full=[F(0)]*(M+1)
for m,value in enumerate(a):
    full[abs(m-1)]+=value/2
    full[m+1]+=value/2
encoded=[F(0)]*(M+1);encoded[0]=a[1]/2;encoded[1]=a[0]+a[2]/2
for j in range(2,M):encoded[j]=(a[j-1]+a[j+1])/2 if j+1<M else a[j-1]/2
assert full[:-1]==encoded[:-1] and encoded[-1]==0
assert full[-1]==F(-8059128652303703,20769187434139310514121985316880384)
assert M==260
files=['c2_fminus.py','c2_gram2.py','lin_assembly.py','lin_fast.py']
out={'date':datetime.now(timezone.utc).isoformat(),'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'source_hashes':{name:hashlib.sha256((base/'numerics/src'/name).read_bytes()).hexdigest() for name in files},'tail_mode':M,'last_background_coefficient':str(a[-1]),'omitted_product_coefficient':str(full[-1]),'angular_product_check':'PASS','scope':'exact coefficient and static source audit; no continuum singular value'}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

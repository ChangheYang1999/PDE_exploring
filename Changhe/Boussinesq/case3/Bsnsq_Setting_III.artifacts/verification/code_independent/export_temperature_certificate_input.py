"""Serialize and independently compare exact masked coefficients with NPZ input."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,sys
import numpy as np
from r2_state_values import R2State
archive=Path(sys.argv[1]);out=Path(sys.argv[2]);state=R2State(archive)
assert state.bb==3
coeff=state.rawF.reshape(state.K,state.nb).copy()
for k in range(state.K):coeff[k,:k//2]=0
q=lambda x:str(Q.from_float(float(x)))
data={'schema':'bq3_b3_temperature_rational_v1','basis_exponent':'3','L':q(state.L),'degree':state.degree,'knots':[q(t) for t in state.knots],'coefficients':[[q(v) for v in row] for row in coeff],'archive_path':str(archive.resolve()),'archive_sha256':state.sha256,'archive_metadata':{k:state.meta[k] for k in ['Nt','K','deg','grade','L','beta','beta_basis']}}
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(data,indent=2)+'\n')
# Compare the written exact JSON directly with archive arrays and reconstruction.
w=json.loads(out.read_text())
with np.load(archive,allow_pickle=False) as a:
 K=int(a['K']);degree=int(a['deg']);Nt=int(a['Nt']);grade=float(a['grade'])
 knots=np.concatenate((np.zeros(degree),np.linspace(0,1,Nt+1)**grade,np.ones(degree)))
 raw=a['cF'].reshape(K,len(knots)-degree-1)
 assert [Q(t) for t in w['knots']]==[Q.from_float(float(t)) for t in knots]
 for k in range(K):
  for j in range(raw.shape[1]):assert Q(w['coefficients'][k][j])==(Q(0) if j<k//2 else Q.from_float(float(raw[k,j])))
 assert Q(w['L'])==Q.from_float(float(a['L'])) and float(a['beta_basis'])==3
 assert w['archive_sha256']==hashlib.sha256(archive.read_bytes()).hexdigest()
print(json.dumps({'input':str(out),'archive_sha256':state.sha256,'input_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'modes':state.K,'positive_spans':state.Nt,'correspondence':'exact rational knots and masked coefficients checked against archive'},indent=2))

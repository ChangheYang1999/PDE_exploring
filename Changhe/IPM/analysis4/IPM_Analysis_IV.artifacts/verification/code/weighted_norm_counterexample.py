"""Exact Cartesian checks for the convergent potential-series counterexample."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
from laurent_log_audit import L,Poly,Q,parse

root=Path('research/83_weighted_norm_nonnecessity');start=time.monotonic()
records=[];F={};G={}
for n in range(1,73):
 q=Q(4)-Q(2*n,3);k=max(0,(n-1)//3-1);a=Q(-27,400)
 H=Poly([0]*k+[a])
 op=lambda v,p:v*p+p.derivative()
 gf=op(q,op(q-2,H))/2
 ff=-op(q-2,op(q,op(q,H)))
 C=L(q,0,[Poly([v]) for v in H.coeffs()])
 # Y=-i partial_y in the real Laurent representation; sine arrays represent i sin.
 cartG=C.X().Y().scale(-1)
 lap=C.X().X()-C.Y().Y()
 cartF=lap.Y()
 expectedG=parse(q-2,{2:gf.coeffs()})
 expectedF=parse(q-3,{1:ff.coeffs()})
 assert (cartG-expectedG).zero(),('stream',n)
 assert (cartF-expectedF).zero(),('density',n)
 assert (expectedG.X().X().scale(-1)+expectedG.Y().Y()-expectedF.X()).zero(),('poisson',n)
 if n%3==0 and n>=6:
  m=int(-(q-2));idx=expectedG.M+m
  coeff=expectedG.a[0][idx] if expectedG.a else Q(0)
  assert not coeff,('resonant constant',n)
 records.append(dict(n=n,degree=k,stream_cartesian_identity=True,density_cartesian_identity=True,poisson_identity=True))
 F[n],G[n]=expectedF,expectedG
J=G[1].X()*F[1].Y()-G[1].Y()*F[1].X()
res=J-F[2].scale(2)
expected=parse(Q(-1,3),{1:['-79/100'],3:['-1/20']})
assert (res-expected).zero()
assert not res.zero()
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),orders=records,
 actual_elapsed_s=time.monotonic()-start,stationary_order2_residual={'1':'-79/100','3':'-1/20'},
 nonstationary_confirmed=True,source_sha256={})
for name in ['weighted_norm_counterexample.py','laurent_log_audit.py']:
 raw=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(raw);result['source_sha256'][name]=sha256(raw).hexdigest()
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(orders=len(records),actual_elapsed_s=result['actual_elapsed_s'],nonstationary=True)))

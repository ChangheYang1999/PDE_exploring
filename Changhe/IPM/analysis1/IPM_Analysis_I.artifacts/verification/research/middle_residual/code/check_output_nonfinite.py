"""Reject the concrete non-finite-to-zero failure found during source review."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
from mpmath import iv
from audit_full_output import ends,fr
cases=['inf','-inf','nan'];checked=[]
for text in cases:
 x=iv.mpf(text)
 try:ends(x)
 except AssertionError:checked.append('interval:'+text)
 else:raise AssertionError('non-finite interval accepted:'+text)
 for index,v in enumerate(x._mpi_):
  if v[3]<0:
   try:fr(v)
   except AssertionError:checked.append('tuple:'+text+':'+str(index))
   else:raise AssertionError('non-finite endpoint accepted:'+text)
assert ends(iv.mpf(0))==(0,0)
assert ends(iv.mpf([-1,2]))==(-1,2)
p=Path(__file__);e=p.parents[1]/'evidence'
r={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','rejected':checked,'finite_controls':2,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'auditor_sha256':hashlib.sha256((p.parent/'audit_full_output.py').read_bytes()).hexdigest()}
(e/'nonfinite_guard_checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))

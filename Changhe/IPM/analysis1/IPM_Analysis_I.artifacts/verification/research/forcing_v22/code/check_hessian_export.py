"""Repair only the verifier's auxiliary constant-zero Hessian export."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,math,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
old=D/'evidence/cutoff_hessian_bounds.json';data=D/'source/runs/forcing/v22_p9_merged.json'
assert sha(old)=='65d617bbee62bc9753f83487ca2cbba08aba7d725a4d17befe06088332edef38'
assert sha(data)=='b5f597c90a0928dd9a5ea87af12953bcc33f46321ef60c3d5b014d9bef3a7201'
a=json.loads(old.read_text());b=json.loads(data.read_text());fixed=[];changes=[]
assert a['rows']==len(a['T2F'])==len(b['cells'])==43949
for i,(x,row) in enumerate(zip(a['T2F'],b['cells'])):
 assert math.isfinite(x) and math.isfinite(row['T2F']) and 0<=x and 0<=row['T2F']
 if x>row['T2F']:
  assert Q.from_float(x)==Q(1,2**1074) and row['T2F']==0
  assert Q.from_float(row['dmax'])<=Q(231,8000) and row['regime']=='inside'
  x=0.;changes.append(i)
 assert 0<=x<=row['T2F'];fixed.append(x)
assert len(changes)==26079
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_AUXILIARY_HESSIAN_EXPORT_WITH_PROVED_CONSTANT_ZEROS',rows=43949,checks=43949,constant_zero_repairs=len(changes),repair_indices_sha256=hashlib.sha256(json.dumps(changes).encode()).hexdigest(),old_sha256=sha(old),data_sha256=sha(data),code_sha256=sha(Path(__file__)),T2F=fixed,scope='Auxiliary export only. Constant cutoffs have Hessian0 exactly; remaining outward endpoints are unchanged. No physical residual or full forcing conclusion.')
(D/'evidence/cutoff_hessian_bounds_checked.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print(out['utc'],out['status'],len(changes),'repairs')

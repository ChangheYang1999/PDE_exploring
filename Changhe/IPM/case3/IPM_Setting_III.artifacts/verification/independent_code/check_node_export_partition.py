from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,time
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();start=datetime.now(timezone.utc).isoformat();tick=time.perf_counter()
paths=[Path(__file__).resolve().relative_to(Path.cwd()),R/'PURE_RELATIVE_AND_PARTITION_PROOF.md',V/'HIGH_BASIS_CHECKS.json']+[Path('independent_code')/k for k in ['node_export_ratio_partition.py','node_export_high_basis_reference.py','independent_hydrostatic.py','hydrostatic_power_tail.py']];bindings={str(p):sha(p)for p in paths}
import numpy as np
from node_export_ratio_partition import RatioPowerVerticalInverse,ratio_nodes
from hydrostatic_power_tail import PowerVerticalInverse
from node_export_high_basis_reference import slowjet,slow_reference
checks=[];rows=[];relative=[];zeros=0
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:
  (V/'PARTITION_FAILURE.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),checks=checks,bindings=bindings),indent=2)+'\n');raise AssertionError((n,e))
a=json.loads((V/'HIGH_BASIS_CHECKS.json').read_text());ck('182 highbasis completed',a['count']==len(a['checks'])==182 and all(z['passed']for z in a['checks']))
for p,h in a['bindings'].items():ck('inherited binding '+p,sha(p)==h);bindings[p]=h
for row in a['jet_rows']:
 for j,(got,ref)in enumerate(zip(row['computed'],row['reference']['values'])):
  if ref:
   err=abs(got-ref)/abs(ref);ck('pure relative manufacture '+str((row['x'],row['y'],j)),err<2e-10,err);relative.append(dict(x=row['x'],y=row['y'],component=j,error=err))
  else:zeros+=1;ck('manufacture zero reference '+str((row['x'],row['y'],j)),got==0)
for lo,hi in [(0.,0.),(0.,1.),(.123,17.),(17.,1e9)]:
 z,w=ratio_nodes(lo,hi,8,.125);ck('partition finite '+str((lo,hi)),np.isfinite(z).all()and np.isfinite(w).all());ck('partition interval and positive weights '+str((lo,hi)),np.all(z>lo)and np.all(z<hi)and np.all(w>0));ck('constant partition integral '+str((lo,hi)),abs(float(w.sum())-(hi-lo))<=32*np.finfo(float).eps*max(hi-lo,1))
 for power in [1,2,3]:
  want=(hi**(power+1)-lo**(power+1))/(power+1);ck('polynomial partition '+str((lo,hi,power)),abs(float(w@(z**power))-want)<=64*np.finfo(float).eps*max(abs(want),1))
points=[(z['x'],z['y'])for z in a['jet_rows']]
for x,y in points:
 for kind,order,tail,scale in [('dyadic',48,160,64.),('dyadic',64,192,128.),('ratio',88,256,512.)]:
  cls=PowerVerticalInverse if kind=='dyadic'else RatioPowerVerticalInverse;z=cls(slowjet,.5,order,tail,scale,.125).at(x,y);a70=slow_reference(x,y,z['R_split'],70);b=slow_reference(x,y,z['R_split'],100);errors={}
  for name in b:
   ck('MP closed reference '+str((x,y,kind,order,name)),np.array_equal(a70[name],b[name]));got,ref=np.atleast_1d(z[name]),np.atleast_1d(b[name]);err=abs(got-ref)/np.maximum(abs(ref),1e-6);ck('production rule absolute floor '+str((x,y,kind,order,name)),np.all(err<2e-10),err.tolist());nz=ref!=0;pure=abs(got[nz]-ref[nz])/abs(ref[nz]);ck('production rule pure relative '+str((x,y,kind,order,name)),np.all(pure<2e-10),pure.tolist());ck('production rule exact zeros '+str((x,y,kind,order,name)),np.all(got[~nz]==0));errors[name]=dict(floored=err.tolist(),pure_nonzero=pure.tolist(),zero_count=int((~nz).sum()))
  rows.append(dict(x=x,y=y,kind=kind,computed=z,reference=b,errors=errors))
for p,h in list(bindings.items()):ck('stable '+p,sha(p)==h)
out=dict(status='PASS_PRODUCTION_RULES_AND_PURE_RELATIVE_JETS',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_monotonic_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=bindings,jet_relative=relative,jet_zero_count=zeros,rows=rows,scope='Finite manufactures only. Pure relative metrics supplement floors. No candidate inverse or certified error bound.')
(V/'PARTITION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['elapsed_monotonic_seconds'])

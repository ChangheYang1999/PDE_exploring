"""Finite manufacture gates only, with pre-import input bindings."""
from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,time
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=datetime.now(timezone.utc).isoformat();tick=time.perf_counter();paths=[Path(__file__),R/'SHIFTED_HIGH_DEGREE_PROOF.md',R/'SLOW_TAIL_DERIVATIVE_CORRECTION.md',V/'HIGH_LOCAL_BASIS.json']+[Path('independent_code')/s for s in ['node_export_high_basis_reference.py','q_local_checkpoint.py','q_checkpoint_reader.py','independent_hydrostatic.py','hydrostatic_power_tail.py']];bindings={str(p):sha(p)for p in paths}
from fractions import Fraction as F
import numpy as np
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from hydrostatic_power_tail import PowerVerticalInverse
from node_export_high_basis_reference import global_polynomials,power_polynomial,reference,slowjet,slow_reference
checks=[];jetrows=[];slowrows=[];fdrows=[]
def ck(name,b,e=None):
 checks.append(dict(name=name,passed=bool(b),evidence=e))
 if not b:
  (V/'HIGH_BASIS_FAILURE.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),checks=checks,bindings=bindings),indent=2)+'\n');raise AssertionError((name,e))
d=json.loads((V/'HIGH_LOCAL_BASIS.json').read_text());p=V/'high_local_basis.npz';np.savez_compressed(p,N=d['N'],M=d['M'],L=float(F(d['L'])),p=float(F(d['Pmap'])),cl=float(F(d['cl'])),basis=d['basis'],tk=np.array([float(F(z))for z in d['tk']]),u=np.array([float(F(z))for row in d['coefficients']for z in row]));bindings[str(p)]=sha(p)
q=QLocalCheckpoint(p);cart=CartesianQJet(q);polys=global_polynomials(d)
ck('dimensions4/3/2',list(map(len,d['coefficients']))==[5,4,3])
for k,row in enumerate(q.exact_coefficients()):
 wanted=polys[k];got=power_polynomial(row);ck('independent ordinary power polynomial '+str(k),got==wanted)
 for i,(a,b)in enumerate(zip(got,wanted)):ck('exact coefficient '+str((k,i)),a==b)
 if k:ck('nontrivial affine second derivative '+str(k),2/(1-F(d['tk'][k]))!=1 and len(wanted)>=3 and wanted[-1]!=0)
points=[(0.,0.),(.137,.219),(-.137,.219),(.137,-.219),(0.,1.1),(1.3,0.),(3.,.2),(.2,3.),(30.,1.),(2000.,65.),(1.,2000.),(.2,30.),(1000.,5e7),(5e7,1000.),(5e7,5e7),(.004,.0003)]
for x,y in points:
 a=reference(polys,x,y,70);b=reference(polys,x,y,100);wanted=np.array(b['values']);got=cart.jet(x,y);err=abs(got-wanted)/np.maximum(abs(wanted),1e-5)
 ck('MP70/100 rounded jets '+str((x,y)),a['values']==b['values']);ck('Cartesian shifted jets '+str((x,y)),np.all(err<2e-10),err.tolist());ck('shifted Clenshaw density '+str((x,y)),abs(float(q.rho(x,y))-wanted[0])<2e-11*max(abs(wanted[0]),1e-5));jetrows.append(dict(x=x,y=y,computed=got.tolist(),reference=b,relative_floor_error=err.tolist()))
 for px,py,signs in [(-x,y,[1,-1,1,1]),(x,-y,[-1,-1,1,-1])]:
  e=abs(cart.jet(px,py)-got*np.array(signs))/np.maximum(abs(got),1e-5);ck('Cartesian parity '+str((x,y,px,py)),np.all(e<2e-10),e.tolist())
tested=0;skipped=0
for x,y in [(.137,.219),(.2,3.),(3.,.2)]:
 wanted=np.array(reference(polys,x,y,100)['values'][1:]);rr=[]
 for h in [.008,.004]:
  f=lambda a,b:float(q.rho(a,b));a,b,c,e,z=f(x+h,y),f(x-h,y),f(x,y+h),f(x,y-h),f(x,y);got=np.array([(a-b)/(2*h),(c-e)/(2*h),(a-2*z+b)/(h*h)]);bound=128*np.finfo(float).eps*np.array([(abs(a)+abs(b))/(2*h),(abs(c)+abs(e))/(2*h),(abs(a)+2*abs(z)+abs(b))/(h*h)]);rr.append(dict(h=h,absolute_error=abs(got-wanted).tolist(),roundoff_allowance=bound.tolist()))
 for j in range(3):
  e0,e1=rr[0]['absolute_error'][j],rr[1]['absolute_error'][j];b0=rr[0]['roundoff_allowance'][j]
  if e0>20*b0:tested+=1;ck('nonvacuous FD '+str((x,y,j)),.15*e0<=e1<=.4*e0,dict(coarse=e0,fine=e1,ratio=e1/e0,roundoff_allowance=b0))
  else:skipped+=1
 fdrows.append(dict(x=x,y=y,rows=rr))
ck('at least6FD components',tested>=6)
for x,y in points[-4:]:
 for order,tail,scale in [(32,96,16.),(64,192,128.)]:
  z=PowerVerticalInverse(slowjet,.5,order,tail,scale,.125).at(x,y);a=slow_reference(x,y,z['R_split'],70);b=slow_reference(x,y,z['R_split'],100);errors={}
  for name in b:
   ck('extended slow MP '+str((x,y,order,name)),np.array_equal(a[name],b[name]));e=abs(np.asarray(z[name])-b[name])/np.maximum(abs(np.asarray(b[name])),1e-6);errors[name]=np.atleast_1d(e).tolist();ck('extended slow closed '+str((x,y,order,name)),np.all(e<2e-10),errors[name])
  slowrows.append(dict(x=x,y=y,computed=z,reference=b,relative_floor_error=errors))
for p,h in bindings.items():ck('stable preimport binding '+p,sha(p)==h)
out=dict(status='PASS_SHIFTED_HIGH_DEGREE_AND_EXTENDED_SLOW_TAIL',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_monotonic_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=bindings,jet_rows=jetrows,fd_rows=fdrows,fd_tested=tested,fd_skipped=skipped,slow_rows=slowrows,scope='Manufactures only. Finite working-precision references, no certified inverse error, no candidate computation.')
(V/'HIGH_BASIS_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['elapsed_monotonic_seconds'],tested,skipped)

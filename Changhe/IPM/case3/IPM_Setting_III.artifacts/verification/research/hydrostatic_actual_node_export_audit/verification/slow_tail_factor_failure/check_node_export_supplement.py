"""Slow-tail and local-basis gates. No candidate is evaluated."""
from pathlib import Path
from datetime import datetime,timezone
import os,hashlib,json,time,sys
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
started=datetime.now(timezone.utc).isoformat();tick=time.perf_counter()
paths=[Path(__file__),R/'SLOW_TAIL_AND_LOCAL_BASIS_PROOF.md',V/'LOCAL_BASIS_MANUFACTURE.json',V/'MANUFACTURES_EXPANDED.json']+[Path('independent_code')/s for s in ['hydrostatic_power_tail.py','independent_hydrostatic.py','q_checkpoint_reader.py','q_local_checkpoint.py','node_export_arithmetic_strict.py','node_export_arithmetic.py','node_export_manufactured_fields.py']]
binds={str(p):sha(p)for p in paths}
from fractions import Fraction as F
import math,random
import numpy as np
import mpmath as mp
from hydrostatic_power_tail import PowerVerticalInverse
from independent_hydrostatic import CartesianQJet
from q_local_checkpoint import QLocalCheckpoint
from node_export_manufactured_fields import algebraic_reference
from node_export_arithmetic_strict import decomposition
checks=[];rows=[];basis=[];fdrows=[]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:
  (V/'SUPPLEMENT_FAILURE.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),checks=checks,bindings=binds),indent=2)+'\n');raise AssertionError((n,e))
def slowjet(x,y):
 x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));a=1+x*x+y*y
 return np.stack([y*a**(-.25),-.5*x*y*a**(-1.25),a**(-.25)-.5*y*y*a**(-1.25),-.5*y*a**(-1.25)+.625*x*x*y*a**(-2.25)],axis=-1)
def ref(x,y,r,dps):
 with mp.workdps(dps):
  x,y,r=map(mp.mpf,[x,y,r]);a=1+x*x;A=a+y*y;B=a+r*r
  I=lambda q:y*a**(-q)*mp.hyp2f1(mp.mpf('.5'),q,mp.mpf('1.5'),-y*y/a)
  i=I(mp.mpf('.25'));j=I(mp.mpf('1.25'))
  z=dict(V=[x*A**(-mp.mpf('.25')),-i+x*x*j/2],Phi=-x*i,dV2_dy=-A**(-mp.mpf('.25'))+x*x*A**(-mp.mpf('1.25'))/2,tail_V=[x*B**(-mp.mpf('.25')),y*(-B**(-mp.mpf('.25'))+x*x*B**(-mp.mpf('1.25'))/2)])
  return {k:[float(a)for a in v]if isinstance(v,list)else float(v)for k,v in z.items()}
points=[(0.,0.),(.137,.219),(-.137,.219),(.137,-.219),(0.,1.1),(1.3,0.),(3.,.2),(.2,3.),(30.,1.),(2000.,65.),(1.,2000.),(.2,30.)]
for x,y in points:
 for order,tail,scale in [(32,96,16.),(64,192,128.)]:
  z=PowerVerticalInverse(slowjet,.5,order,tail,scale,.125).at(x,y);a=ref(x,y,z['R_split'],70);b=ref(x,y,z['R_split'],100);errs={}
  for name in b:
   ck(f'slow MP70/100 {x,y,order,name}',np.array_equal(a[name],b[name]))
   err=abs(np.asarray(z[name])-b[name])/np.maximum(abs(np.asarray(b[name])),1e-6);errs[name]=np.atleast_1d(err).tolist();ck(f'slow closed inverse {x,y,order,name}',np.all(err<2e-10),errs[name])
  rows.append(dict(x=x,y=y,computed=z,reference=b,relative_floor_error=errs))
d=json.loads((V/'LOCAL_BASIS_MANUFACTURE.json').read_text());path=V/'local_basis_manufacture.npz'
np.savez_compressed(path,N=d['N'],M=d['M'],L=float(F(d['L'])),p=float(F(d['Pmap'])),cl=float(F(d['cl'])),basis=d['basis'],tk=np.array([float(F(z))for z in d['tk']]),u=np.array([float(F(z))for row in d['coefficients']for z in row]))
binds[str(path)]=sha(path);q=QLocalCheckpoint(path);cart=CartesianQJet(q)
ck('exact local to global all coefficient identity',q.exact_coefficients()==[[F(z)for z in row]for row in d['global_coefficients']])
for x,y in points:
 a=algebraic_reference(x,y,90);wanted=np.array(a['values']);got=cart.jet(x,y);err=abs(got-wanted)/np.maximum(abs(wanted),1e-5)
 ck(f'local loader Cartesian jets {x,y}',np.all(err<2e-10),err.tolist());ck(f'local loader Clenshaw density {x,y}',abs(float(q.rho(x,y))-wanted[0])<2e-11*max(abs(wanted[0]),1e-5));basis.append(dict(x=x,y=y,computed=got.tolist(),reference=a,relative_floor_error=err.tolist()))
fdskipped=0;fdtested=0
for x,y in [(.137,.219),(.2,3.),(3.,.2)]:
 wanted=np.array(algebraic_reference(x,y,90)['values'][1:]);rr=[]
 for h in [.008,.004]:
  f=lambda a,b:float(q.rho(a,b));fxp,fxm,fyp,fym,f0=f(x+h,y),f(x-h,y),f(x,y+h),f(x,y-h),f(x,y)
  z=np.array([(fxp-fxm)/(2*h),(fyp-fym)/(2*h),(fxp-2*f0+fxm)/(h*h)])
  bound=128*np.finfo(float).eps*np.array([(abs(fxp)+abs(fxm))/(2*h),(abs(fyp)+abs(fym))/(2*h),(abs(fxp)+2*abs(f0)+abs(fxm))/(h*h)])
  rr.append(dict(h=h,absolute_error=abs(z-wanted).tolist(),roundoff_allowance=bound.tolist(),normalized_error=(abs(z-wanted)/np.maximum(abs(wanted),1e-3)).tolist()))
 for j in range(3):
  e0,e1=rr[0]['absolute_error'][j],rr[1]['absolute_error'][j];b0=rr[0]['roundoff_allowance'][j]
  if e0>20*b0:
   fdtested+=1;ck(f'nonvacuous FD refinement {x,y,j}',.15*e0<=e1<=.40*e0,dict(coarse=e0,fine=e1,ratio=e1/e0,roundoff_allowance=b0))
  else:fdskipped+=1
 fdrows.append(dict(x=x,y=y,rows=rr))
ck('FD manufacture has tested components',fdtested>=6)
# Underflow labels refer to closed reference components, with log coefficients.
underflows=[];threshold=math.log(float(np.nextafter(0.,1.)))-math.log(2.)
for row in json.loads((V/'MANUFACTURES_EXPANDED.json').read_text())['inverse_rows']:
 if row['family']!='gaussian':continue
 x,y=row['x'],row['y'];r=row['R_split'];qq=math.sqrt(math.pi)*math.erf(y)/2
 coeffs={'V0':(x,-x*x-y*y),'V1':((2*x*x-1)*qq,-x*x),'Phi':(-x*qq,-x*x),'dV2_dy':(2*x*x-1,-x*x-y*y),'tailV0':(x,-x*x-r*r),'tailV1':(y*(2*x*x-1),-x*x-r*r)}
 vals=dict(V0=row['reference']['V'][0],V1=row['reference']['V'][1],Phi=row['reference']['Phi'],dV2_dy=row['reference']['dV2_dy'],tailV0=row['reference']['tail_V'][0],tailV1=row['reference']['tail_V'][1]);out={}
 for name,(coef,exponent)in coeffs.items():
  logmag=None if coef==0 else math.log(abs(coef))+exponent
  out[name]=dict(exact_zero=coef==0,reference_underflow=coef!=0 and logmag<threshold,log_absolute_magnitude=logmag,binary64_reference=vals[name])
  ck(f'Gaussian zero classification {x,y,r,name}',(vals[name]==0)if(coef==0 or logmag<threshold)else vals[name]!=0)
 underflows.append(dict(x=x,y=y,R_split=r,components=out))
rng=random.Random(309);telescope=0;zero=0
for i in range(80):
 vals=[F(rng.randrange(-20,21),rng.randrange(1,13))for j in range(13)];z=decomposition(vals[:3],vals[3:6],vals[6:8],vals[8:10],*vals[10:13])
 if z['common_denominator']:telescope+=1
 else:zero+=1
ck('exact telescope counts',telescope==80 and zero==0)
for p,h in binds.items():ck('stable preimport input '+p,sha(p)==h)
out=dict(status='PASS_SLOW_TAIL_AND_LOCAL_BASIS_MANUFACTURES',started_utc=started,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_monotonic_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=binds,slow_tail_rows=rows,local_basis_rows=basis,finite_differences=fdrows,fd_tested=fdtested,fd_skipped=fdskipped,gaussian_underflow=underflows,telescope_tested=telescope,telescope_skipped_zero=zero,floors=dict(inverse=1e-6,jet=1e-5,finite_difference_diagnostic=1e-3),scope='Manufactures only. Working-precision references, no certified inverse error or candidate execution. Pre-import hashes checked in this process only.')
(V/'SUPPLEMENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks),out['elapsed_monotonic_seconds'],fdtested,fdskipped)

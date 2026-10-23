"""Expanded pre-export gates. No candidate arrays are loaded or evaluated."""
import os
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys,random
import numpy as np
import scipy,mpmath
from hydrostatic_power_tail import PowerVerticalInverse
from node_export_arithmetic_strict import residual,decomposition,exact,array64
from node_export_manufactured_fields import rational,gaussian,closed_inverse,basis_object,algebraic_reference

def main():
 R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';V.mkdir(parents=True,exist_ok=True)
 sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();started=datetime.now(timezone.utc).isoformat()
 paths=[Path('independent_code/check_node_export_manufactures_expanded.py'),Path('independent_code/node_export_arithmetic_strict.py'),Path('independent_code/node_export_arithmetic.py'),Path('independent_code/node_export_manufactured_fields.py'),Path('independent_code/hydrostatic_power_tail.py'),Path('independent_code/independent_hydrostatic.py'),Path('independent_code/q_checkpoint_reader.py'),R/'PROOF.md',R/'DESIGN_REVIEW_RESOLUTION_PROOF.md',V/'BASIS_MANUFACTURE.json',V/'MANUFACTURES.json']
 binds={str(p):sha(p)for p in paths};checks=[];rows=[];basis_rows=[]
 def ck(n,b,e=None):
  checks.append(dict(name=n,passed=bool(b),evidence=e))
  if not b:
   (V/'EXPANDED_FAILURE.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=binds),indent=2)+'\n');raise AssertionError((n,e))
 for family,jet in [('rational',rational),('gaussian',gaussian)]:
  points=[(0.,0.),(.137,.219),(-.137,.219),(.137,-.219),(-.137,-.219),(0.,1.1),(1.3,0.),(3.,.2),(.2,3.),(30.,1.),(2000.,65.),(1.,2000.),(.2,30.),(-30.,.2),(.2,-30.)]
  for x,y in points:
   J=jet(x,y);ck(f'{family} parity{x,y}',np.array_equal(jet(-x,y),J*np.array([1,-1,1,1]))and np.array_equal(jet(x,-y),J*np.array([-1,-1,1,-1])))
   for order,tail,scale in [(32,96,16.),(64,192,128.)]:
    got=PowerVerticalInverse(jet=jet,p=.5,order=order,tail_order=tail,tail_scale=scale,inner_scale=.125).at(x,y);want=closed_inverse(family,x,y,got['R_split'])
    ck(f'{family} split{x,y,order}',got['R_split']>abs(y)and got['tail_power']==2)
    errors={}
    for name in ['V','Phi','dV2_dy','tail_V']:
     a=np.atleast_1d(got[name]);b=np.atleast_1d(want[name]);absolute=np.abs(a-b);scaled=absolute/np.maximum(np.abs(b),1e-6)
     ck(f'{family} {name}{x,y,order}',np.all(scaled<2e-10),dict(absolute=absolute.tolist(),relative_floor=scaled.tolist()))
     errors[name]=dict(absolute=absolute.tolist(),relative_floor=scaled.tolist())
    d=residual(J,got['V'],2,x,y);ck(f'{family} denominator bounds{x,y,order}',abs(d['R'])<=d['Nf']and abs(d['R'])<=2*d['Nv']and(d['Nf']!=0 or d['R']==0)and(d['Nv']!=0 or d['R']==0))
    if x==y==0:ck(f'{family} zero ratios{order}',d['R']==0 and d['Rf']is None and d['Rv']is None)
    rows.append(dict(family=family,x=x,y=y,options=dict(order=order,tail_order=tail,tail_scale=scale,inner_scale=.125),R_split=got['R_split'],tail_power=got['tail_power'],computed=got,reference=want,errors=errors))
 data=json.loads((V/'BASIS_MANUFACTURE.json').read_text());ck('exact basis data',data['L']=='1'and data['Pmap']=='2'and data['coefficients']==[['1','1/4','-1/8'],['3/8','-1/4'],['-1/16']]);q,cart=basis_object(data)
 for x,y in [(0.,0.),(.01,.02),(.137,.219),(-.137,.219),(.137,-.219),(0.,1.1),(1.3,0.),(3.,.2),(.2,3.),(30.,1.),(2000.,65.),(1.,2000.)]:
  lo=algebraic_reference(x,y,70);hi=algebraic_reference(x,y,100);want=np.array(hi['values']);got=cart.jet(x,y)
  ck(f'basis MP70/100{x,y}',np.array_equal(lo['values'],want))
  err=abs(got-want)/np.maximum(abs(want),1e-5);ck(f'basis Cartesian analytic{x,y}',np.all(err<2e-10),dict(error=err.tolist(),computed=got.tolist(),reference=want.tolist()))
  ck(f'basis density Clenshaw{x,y}',abs(float(q.rho(x,y))-want[0])<2e-11*max(abs(want[0]),1e-5))
  ck(f'basis parity{x,y}',np.allclose(cart.jet(-x,y),got*np.array([1,-1,1,1]),rtol=2e-13,atol=0)and np.allclose(cart.jet(x,-y),got*np.array([-1,-1,1,-1]),rtol=2e-13,atol=0))
  basis_rows.append(dict(x=x,y=y,computed=got.tolist(),reference70=lo,reference100=hi,relative_floor_error=err.tolist()))
 for x,y in [(.137,.219),(.2,3.),(3.,.2)]:
  ref=cart.jet(x,y);errs=[]
  for h in [4e-4,2e-4]:
   f=lambda a,b:float(q.rho(a,b));fd=np.array([(f(x+h,y)-f(x-h,y))/(2*h),(f(x,y+h)-f(x,y-h))/(2*h),(f(x+h,y)-2*f(x,y)+f(x-h,y))/(h*h)])
   err=abs(fd-ref[1:])/np.maximum(abs(ref[1:]),1e-3);errs.append(err)
   ck(f'basis independent finite differences{x,y,h}',np.all(err<8e-5),dict(derivatives=fd.tolist(),relative_floor_error=err.tolist()))
  ck(f'basis finite difference refinement{x,y}',np.all(errs[1]<=.65*errs[0]+3e-6),[z.tolist()for z in errs])
 # Strict arithmetic and export schema gates.
 for value in [np.float32(1),True,'1',np.int64(4),float('inf'),float('nan')]:
  try:exact(value);rejected=False
  except(TypeError,ValueError):rejected=True
  ck('reject '+repr(value)+' '+str(type(value)),rejected)
 ck('large integer exact',exact(2**70+1)==F(2**70+1))
 ck('binary64 exact',exact(np.float64(.1))==F(*float(.1).as_integer_ratio()))
 for a,shape in [(np.ones(3,dtype=np.float32),(3,)),(np.ones(3),(1,3)),(np.array([np.nan]),(1,)),(np.ones(3,dtype='>f8'),(3,))]:
  try:array64(a,shape);rejected=False
  except(TypeError,ValueError):rejected=True
  ck('reject array '+str(a.dtype)+str(shape),rejected)
 ck('accept binary64 finite shape',array64(np.array([1.,2.]),(2,)).shape==(2,))
 rng=random.Random(309)
 for i in range(80):
  vals=[F(rng.randrange(-20,21),rng.randrange(1,13))for j in range(13)];J=vals[:3];JP=vals[3:6];Q=vals[6:8];M=vals[8:10];c,x,y=vals[10:13]
  d=decomposition(J,JP,Q,M,c,x,y);z=residual(J,Q,c,x,y)
  ck('exact two split identity'+str(i),d['identity']and d['alternate_identity'])
  ck('exact denominator bounds'+str(i),abs(z['R'])<=z['Nf']and abs(z['R'])<=max(abs(c),1)*z['Nv']and(z['Nf']!=0 or z['R']==0)and(z['Nv']!=0 or z['R']==0))
  if d['common_denominator']:
   den=d['common_denominator'];ck('exact common normalized telescope'+str(i),d['difference']/den==d['velocity_term']/den+d['jet_term']/den)
 d=decomposition([F(2),F(3),F(5)],[F(7),F(11),F(13)],[F(23),F(29)],[F(17),F(19)],2,31,37)
 ck('split contributions not unique',d['velocity_term']!=d['alternate_velocity_term']and d['jet_term']!=d['alternate_jet_term'])
 for p,h in binds.items():ck('unchanged '+p,sha(p)==h)
 obj=dict(status='PASS_EXPANDED_MANUFACTURES_ONLY',started_utc=started,finished_utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,inverse_rows=rows,basis_rows=basis_rows,bindings=binds,versions=dict(python=sys.version,executable=sys.executable,sys_path0=sys.path[0],numpy=np.__version__,scipy=scipy.__version__,mpmath=mpmath.__version__),scope='No candidate export admitted or evaluated. Manufactured inverse and coefficient-to-jet checks; no rigorous inverse error enclosure. Primary full-plane IPM unresolved.')
 (V/'MANUFACTURES_EXPANDED.json').write_text(json.dumps(obj,indent=2)+'\n');print(obj['status'],obj['count'],obj['finished_utc'])
if __name__=='__main__':main()

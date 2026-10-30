"""Manufactured Cartesian jets and exact polynomial specialization."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import sys, json, time
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx
from fields import Rat, ScaledRadial, TR, VR, LINEARS, T, V, ar, field_hash
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/scaled_weak_backend'
sys.path.insert(0,str(ROOT/'research/multiscale_generators/code'))
from cartesian import GeneratorJet
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import Radial
sys.set_int_max_str_digits(0)
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()

def main():
 start=time.monotonic();ctx.prec=2048
 a=Rat(Poly([1,2,3]),(2,3));b=Rat(Poly([2,-1]),(1,2));before=a.record()
 for t in [Q(0),Q(1,10),Q(1,2),Q(1)]:
  assert (a+b).exact_value(t)==a.exact_value(t)+b.exact_value(t)
  assert (a*b).exact_value(t)==a.exact_value(t)*b.exact_value(t)
 assert a.record()==before and (a+b)-b==a
 N,D=a.P,LINEARS[0]**2*LINEARS[1]**3
 derivative=Rat(N.derivative()*D-N*D.derivative(),(4,6))
 assert derivative==a.derivative()
 cancellation=Rat(D,(2,3));assert cancellation==1 and cancellation.derivative()==0
 assert (a*TR**4).divide_t(4)==a
 fixtures=[
  {'cl_exact':'7/4','generators':[
   {'j':0,'m':0,'spec':['mono',0],'coef':'2/7'},
   {'j':1,'m':1,'spec':['leg',2,3],'coef':'-3/11'},
   {'j':2,'m':2,'spec':['legq',1,4,2],'coef':'5/13'},
   {'j':0,'m':0,'spec':['legqs',5,3,4,10],'coef':'-7/17'},
   {'j':3,'m':3,'spec':['legqs',2,4,4,100],'coef':'11/19'},
   {'j':2,'m':1,'spec':['legqs',4,2,0,100],'coef':'-13/23'},
   {'j':1,'m':2,'spec':['legqs',3,0,1,10],'coef':'17/29'}]},
  {'cl_exact':'9/5','generators':[
   {'j':0,'m':0,'spec':['legqs',0,0,0,10],'coef':'1'},
   {'j':0,'m':2,'spec':['legqs',0,3,2,100],'coef':'-2/3'},
   {'j':2,'m':1,'spec':['legqs',0,2,1,10],'coef':'4/5'}]},
 ]
 rows=[]
 for index,data in enumerate(fixtures):
  tick=time.monotonic();model=ScaledRadial(data);mixed=0
  for x in range(1,5):
   for y in range(1,5-x):
    previous=model.deriv(x-1,y);alternate=model.differentiate(previous,x+y-1,'s' if y%2 else 'c','x')
    assert alternate==model.deriv(x,y);mixed+=1
  for x in range(5):
   for y in range(5-x):model.fields[f'chi_{x}_{y}']=(model.deriv(x,y),x+y,'s' if y%2 else 'c')
  points=[]
  for xs,ys in [('1/2','1/3'),('3','4'),('60','80')]:
   direct=GeneratorJet(data,xs,ys,4);expected=direct.fields();actual=model.evaluate(xs,ys)
   checks={key:actual[key].overlaps(expected[key]) for key in ['rho','u1','u2','rho_x','rho_y','residual']}
   for x in range(5):
    for y in range(5-x):checks[f'chi_{x}_{y}']=actual[f'chi_{x}_{y}'].overlaps(direct.chi(x,y))
   assert all(checks.values()),(index,xs,ys,checks)
   points.append({'x':xs,'y':ys,'all_21_point_checks':checks})
  rows.append({'fixture':index,'exact_input':data,'mixed_derivative_checks':mixed,'points':points,'elapsed_seconds':time.monotonic()-tick})
  print('fixture',index,'passed',rows[-1]['elapsed_seconds'],flush=True)
 src=ROOT/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json'
 old=Radial(src);new=ScaledRadial(src);comparisons={}
 for label in ['rho','u1','u2','rx','ry']:
  left,right=getattr(old,label),getattr(new,label);assert set(left)==set(right)
  comparisons[label]=all(Rat(P)==right[k] for k,P in left.items());assert comparisons[label]
  assert all(v.powers==(0,0) for v in right.values())
 checks=len(old.derivatives)
 for key,left in old.derivatives.items():
  right=new.deriv(*key);assert set(left)==set(right) and all(Rat(P)==right[k] for k,P in left.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'all_passed':True,'precision_bits':ctx.prec,'rational_arithmetic_checks':True,'manufactured':rows,'candidate007_exact_field_comparisons':comparisons,'candidate007_derivative_maps_checked':checks,'canonical_sha256':H(src),'inputs':{str(p.relative_to(ROOT)):H(p) for p in [src,BASE/'PROOF.md',BASE/'code/fields.py',Path(__file__),ROOT/'research/multiscale_generators/code/cartesian.py',ROOT/'research/radial_fourier/code/radial.py']},'candidate007_field_sha256':{label:field_hash(getattr(new,label)) for label in ['rho','u1','u2','rx','ry']},'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent peer; exact field and independent Cartesian fixture checks pass'}
 with (BASE/'verification/fields.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('DONE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

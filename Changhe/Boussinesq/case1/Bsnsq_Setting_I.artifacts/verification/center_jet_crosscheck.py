"""Independent finite-difference check of the bivariate Taylor residuals."""
import datetime,json
from pathlib import Path
import numpy as np
from read_polar_data import PolarData
from high_order_jets import compute,evaluate
from independent_residuals import derivative
rows=[]
for name,base in [('chain240','polar_chain240_verification'),('res2','polar_res2_verification')]:
 obj=PolarData(Path('runs')/base/'source_coefficients.npz',radial_order=224)
 result,T,O,P,RT,RO=compute(obj,nquad=128,return_polys=True)
 for phi in [.0,.413,.917,np.pi/2]:
  for r in [.04,.02,.01,.005]:
   x=np.array([r*np.cos(phi)],np.longdouble);y=np.array([r*np.sin(phi)],np.longdouble)
   u=obj.U_modal(x,y);w=u+obj.beta*np.stack([x,y],axis=-1)
   row={'candidate':name,'r':r,'phi':phi,'RT_series':float(evaluate(RT,x[0],y[0])),'RO_series':float(evaluate(RO,x[0],y[0])),'finite_difference':[]}
   for h0 in [2e-4,8e-5,3.2e-5]:
    h=np.array([h0],np.longdouble)
    tx=derivative(obj.Theta,x,y,h,0,1);ty=derivative(obj.Theta,x,y,h,1,1);ox=derivative(obj.Omega,x,y,h,0,1);oy=derivative(obj.Omega,x,y,h,1,1)
    rt=w[:,0]*tx+w[:,1]*ty-(obj.beta-2)*obj.Theta(x,y);ro=w[:,0]*ox+w[:,1]*oy+obj.Omega(x,y)-tx
    row['finite_difference'].append({'h':h0,'RT':float(rt[0]),'RO':float(ro[0]),'RT_difference':float(rt[0])-row['RT_series'],'RO_difference':float(ro[0])-row['RO_series']})
   rows.append(row)
Path('runs/high_order_jets/finite_difference_crosscheck.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':rows},indent=2)+'\n')

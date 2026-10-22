"""Physical log-radius quadrature and independent circle projections for center moments."""
import json,datetime,math
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
from high_order_jets import compute
from jet_recurrence_check import reconstruct
from read_polar_data import PolarData
D=np.longdouble
rows=[]
for name,base in [('chain240','polar_chain240_verification'),('res2','polar_res2_verification')]:
 obj=PolarData(Path('runs')/base/'source_coefficients.npz',radial_order=192)
 angular=[];phi=2*np.arccos(D(-1))*np.arange(512,dtype=D)/512
 for r in [.5,1.,3.,10.]:
  vals=obj.Omega(r*np.cos(phi),r*np.sin(phi));modes=obj.radial_modes(np.array([r]))
  for m in [4,6,8,10,12]:angular.append({'r':r,'mode':m,'difference':float(2*np.mean(vals*np.sin(m*phi))-modes[m//2-1,0])})
 physical=[]
 for n in [24,40,64]:
  zz,ww=roots_legendre(n);edges=np.linspace(np.log(1e-9),np.log(1e7),65);tt=(edges[1:,None]+edges[:-1,None])/2+(edges[1:,None]-edges[:-1,None])/2*zz
  weight=(edges[1:,None]-edges[:-1,None])/2*ww;r=np.exp(np.asarray(tt,D));modes=obj.radial_modes(r)
  for m in [4,6,8,10,12]:
   value=np.sum(weight*r**(2-m)*modes[m//2-1])/(2*m);cs=np.sum(abs(obj.cO[m//2-1]));delta=D(1)/obj.beta
   near=cs*D('1e-9')**2/(4*m*D(obj.L)**m);tail=cs*D(obj.L)**delta*D('1e7')**(2-m-delta)/(2*m*(m-2+delta))
   physical.append({'n_panel':n,'panels':64,'r_min':1e-9,'r_max':1e7,'mode':m,'value':float(value),'absolute_near_omission_bound':float(near),'absolute_tail_omission_bound':float(tail)})
 reconstructed=[]
 for n in [64,96,144]:
  jet=compute(obj,nquad=n);blocks,et,eo=reconstruct(obj.beta,obj.a0,jet['harmonic_Green_moments'])
  reconstructed.append({'nquad':n,'moments':jet['harmonic_Green_moments'],'blocks':blocks,'max_RT_coefficient':et,'max_RO_coefficient':eo})
 rows.append({'candidate':name,'sha256':obj.sha256,'circle_projection':angular,'physical_moments':physical,'recurrence_refinement':reconstructed})
 print(json.dumps({'candidate':name,'circle_projection_max_error':max(abs(a['difference']) for a in angular),'physical_moments':physical,'jacobi_moments':reconstructed[-1]['moments']}),flush=True)
Path('runs/high_order_jets/moment_crosscheck.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Quadrature-independent, representation-dependent check on frozen finite-basis approximants; omission bounds apply to those stored mathematical fields only, not to any unknown exact solution.','rows':rows},indent=2)+'\n')

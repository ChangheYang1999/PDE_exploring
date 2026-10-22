from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import numpy as np
from gaussian_characteristics import GaussianFlow
from finite_difference import derivative
from cartesian_inverse import CartesianInverse,InverseSettings
start=time.monotonic();g=GaussianFlow();p=np.array([[.07,.03],[.35,-.7],[.7,1.1],[1.8,2.2],[4.,-2.],[7.,4.]])
out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Independent epsilon0 forced Gaussian flow, not a B2 candidate','parameters':{k:float(v) for k,v in vars(g).items()},'source_sha256':hashlib.sha256(Path('code_independent/gaussian_characteristics.py').read_bytes()).hexdigest(),'points':p.tolist(),'inverse':[],'characteristics':[]}
for order in (24,48,96):
 inv=CartesianInverse(g.external_omega,InverseSettings(radius=16.,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1.))
 row={'order':order,'maximum_error':float(np.max(abs(inv.relative(p)-g.velocity(p))))};out['inverse'].append(row);print('inverse',row,flush=True)
for rin in (1e-3,3e-4,1e-4):
 rows=[g.evaluate(q,r_in=rin) for q in p];out['characteristics'].append({'r_in':rin,'rows':rows});print('char',rin,[(q.get('Theta'),q.get('Omega'),q['status']) for q in rows],flush=True)
# Independent coordinate finite differences check the propagated gradients and equations.
base=out['characteristics'][-1]['rows'];v=g.velocity(p);W=g.beta*p+v
for step in (.004,.002):
 def values(x,y,key):
  shape=np.broadcast(x,y).shape;q=np.column_stack((np.broadcast_to(x,shape).ravel(),np.broadcast_to(y,shape).ravel()));return np.array([g.evaluate(z,r_in=1e-4,rtol=3e-10)[key] for z in q]).reshape(shape)
 tx=derivative(lambda x,y:values(x,y,'Theta'),p,0,step,radius=2);ty=derivative(lambda x,y:values(x,y,'Theta'),p,1,step,radius=2)
 ox=derivative(lambda x,y:values(x,y,'Omega'),p,0,step,radius=2);oy=derivative(lambda x,y:values(x,y,'Omega'),p,1,step,radius=2)
 th=np.array([z['Theta'] for z in base]);om=np.array([z['Omega'] for z in base]);gr=np.array([z['gradient'] for z in base]);row={'step':step,'gradient_error':float(np.max(abs(np.column_stack((tx,ty))-gr))),'R_Theta':(W[:,0]*tx+W[:,1]*ty-(g.beta-2)*th).tolist(),'R_Omega':(W[:,0]*ox+W[:,1]*oy+om-tx).tolist()};out.setdefault('finite_differences',[]).append(row);print('fd',row,flush=True)
 Path('verification/gaussian_characteristic_tests_partial.json').write_text(json.dumps(out,indent=2)+'\n')
out['ended_utc']=datetime.now(timezone.utc).isoformat();out['elapsed_seconds']=time.monotonic()-start;Path('verification/gaussian_characteristic_tests.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)

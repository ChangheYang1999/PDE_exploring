import json
from pathlib import Path
import numpy as np
from characteristic_check import reconstruct

class LinearTest:
    beta=3.;a0=3.;eps=.07
    def U_modal(self,x,y):return np.stack([2*x,-2*y],axis=-1)
    def Theta(self,x,y):return self.a0*y+self.eps*x*x*y
    def Omega(self,x,y):return 2*self.eps*x*y/(2*self.beta+1)
obj=LinearTest();points=np.array([[.3,.2],[.7,.9],[3.1,1.7]])
rows=[]
for tol in [1e-7,1e-10,1e-12]:
 result=reconstruct(obj,points,times=(1.,3.,6.),rtol=tol,atol=tol*1e-3)
 for row in result['rows']:
  t=row['time'];expected=obj.eps*points[:,0]**2*points[:,1]*(np.exp(-2*(obj.beta+2)*t)-1)
  row['theta_error_against_exact_defect']=float(np.max(np.abs(np.array(row['theta_finite_defect'])-expected)))
  row['omega_error_against_exact_identity']=float(np.max(np.abs(row['omega_finite_defect'])))
 rows.append(result)
print([(r['rtol'],max(x['theta_error_against_exact_defect'] for x in r['rows']),max(x['omega_error_against_exact_identity'] for x in r['rows'])) for r in rows])
assert max(x['theta_error_against_exact_defect'] for x in rows[-1]['rows'])<1e-9
assert max(x['omega_error_against_exact_identity'] for x in rows[-1]['rows'])<1e-9
Path('runs/characteristic_manufactured.json').write_text(json.dumps({'scope':'manufactured transport test only; velocity contains a prescribed affine field and is not an admissible full-plane inverse','cases':rows},indent=2)+'\n')

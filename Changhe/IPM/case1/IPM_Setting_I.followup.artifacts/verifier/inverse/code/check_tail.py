"""Independent slow-growth test of full-plane normalization and outer cutoffs."""
import sys,json,time
from pathlib import Path
import numpy as np
from density import growing_manufactured,growing_velocity,potential_manufactured,potential_velocity,gradient_fd
from realspace import velocity

out={'method':'centered log-polar kernel on explicit potential data','rows':[]}
for k in [.2,.6,.9]:
 for point in [(1.,.5),(2.,1.)]:
  exact=growing_velocity(*point,k=k);p=(k+1)/2;C=-4*p*(p+1)
  rho=lambda x,y:growing_manufactured(x,y,k=k)
  for radius in [1e2,1e4,1e6,1e8,1e10,1e12]:
   u,_=velocity(rho,point,nang=512,order=16,panel=.25,rmax=radius)
   lead=C/4*np.array(point)*radius**(k-1)
   row={'k':k,'point':point,'rmax':radius,'U':u.tolist(),'exact':exact.tolist(),
        'error':(u-exact).tolist(),'predicted_missing_tail':lead.tolist(),
        'tail_subtracted_error':(u+lead-exact).tolist()}
   out['rows'].append(row)
for point in [(.3,.7),(1.2,.4),(2.,1.)]:
 g=gradient_fd(potential_manufactured,*point)
 grad_u=np.array([gradient_fd(lambda x,y:potential_velocity(x,y)[i],*point) for i in [0,1]])
 out.setdefault('elliptic_stencil',[]).append({'point':point,'div':float(np.trace(grad_u)),
     'E_minus_curl_minus_rhox':float(-grad_u[1,0]+grad_u[0,1]-g[0])})
Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'rows':len(out['rows']),'largest_compensated_error_at_rmax_1e4':max(max(abs(x) for x in row['tail_subtracted_error']) for row in out['rows'] if row['rmax']==1e4),'elliptic_stencil':out['elliptic_stencil']},indent=2))

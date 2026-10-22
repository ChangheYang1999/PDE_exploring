"""Physical Cartesian checks of the independent proper-chart construction."""
from pathlib import Path
from datetime import datetime,timezone
import time,json,hashlib
import numpy as np
from r2_state_values import R2State
from proper_temperature_chart import TemperatureChart
from finite_difference import stencil
root=Path('research/103_proper_temperature_chart/verification');start=time.monotonic();nodes,weights=stencil();out={'started_utc':datetime.now(timezone.utc).isoformat(),'cases':[]}
archive=Path('verification/lambda097_K16_20261021T0025/blam16f_lambda0.97.npz')
for tag,state,gamma in [('radial',None,0.),('radial_with_trace',None,.17),('archive_with_trace',R2State(archive),-.09)]:
 c=TemperatureChart(state,gamma);rows=[]
 # First derivative of q: independent Cartesian differences over several scales.
 de=[]
 for radius in [1e-4,.1,1.,10.,1e3,1e6]:
  for th in [.31,1.2,-.72]:
   x=radius*np.cos(th);y=radius*np.sin(th);qv=c.qdata(x,y);h=1e-4*max(1.,radius)
   fd=[sum(w*c.qdata(x+(h*z if a==0 else 0),y+(h*z if a==1 else 0))[0] for z,w in zip(nodes,weights))/h for a in [0,1]]
   err=max(abs(np.asarray(fd)-qv[1:]))/(1+max(abs(qv[1:])));de.append(float(err));assert err<2e-8
 for x,y in [(.3,-.4),(1.1,.6),(2.1,-1.2)]:
  v=c.physical(x,y);row={'point':[x,y],'q':v['q'],'J':v['J'],'steps':[]}
  for h in [4e-4,2e-4]:
   dx=[c.physical(x+h*z,y) for z in nodes];dy=[c.physical(x,y+h*z) for z in nodes]
   partial=lambda data,key:sum(w*d[key] for w,d in zip(weights,data))/h
   wx=partial(dx,'W');wy=partial(dy,'W');px=partial(dx,'psi');py=partial(dy,'psi');tx=partial(dx,'Theta');ty=partial(dy,'Theta')
   qx=partial(dx,'q');qy=partial(dy,'q');ex=partial(dx,'eta');ey=partial(dy,'eta')
   err={'area':float(abs(qx*ey-qy*ex-1)),'divergence':float(abs(wx[0]+wy[1]-6)),'transport':float(abs(v['W']@np.array([tx,ty])-v['Theta'])),'stream':float(np.max(abs(np.array([-py,px])-(v['W']-3*np.array([x,y])))))}
   assert max(err.values())<3e-5,(tag,x,y,h,err)
   row['steps'].append({'h':h,**err})
  rows.append(row)
 # Explicit y=0 trace verifies the retained free odd integration function.
 q=.6;x=c.X(q,0.);v=c.physical(x,0.);target=(5.5*3-.5*6)*gamma*q*q/v['J'];assert abs(v['W'][1]-target)<2e-12
 # This finite sample is only a numerical illustration of proved properness.
 escaping=[{'q':q,'y':y,'x':c.X(q,float(y)),'eta':float(c.S_eta(q,float(y))[1])} for y in [-20.,-5.,0.,5.,20.]]
 out['cases'].append({'tag':tag,'gamma':gamma,'archive_sha256':state.sha256 if state is not None else None,'derivative_max_error':max(de),'physical_checks':rows,'trace_error':float(abs(v['W'][1]-target)),'escaping_samples':escaping,'quadrature_error_estimate_max':c.max_quad_error,'quadrature_failures':c.quad_failures,'max_root_scaled_error':c.max_root_error,'integral_calls':c.integral_calls})
 print(tag,'physical check passed','max derivative error',max(de),'quadrature estimate',c.max_quad_error,flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,scope='Finite Cartesian manufactured checks plus one stored temperature coordinate map. Optional transport field is not a B2 candidate; no inverse closure or vorticity PDE checked.',code_hashes={n:hashlib.sha256(Path('code_independent',n).read_bytes()).hexdigest() for n in ['proper_temperature_chart.py','test_proper_temperature_chart.py']});(root/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)

"""Independent checks of P220 cutoff derivatives, geometry and saved cubatures."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import numpy as np
import sympy as s
from compact_foliation_inverse_test import fields,cutoff
from compact_foliation_duffy import ymap,vmap
vdir=Path('research/220_compact_foliation_manufactured/verification');start=time.monotonic();checks={};records=[]
def ck(k,b):checks[k]=bool(b)
v,k,y,A,B,t,z=s.symbols('v k y A B t z',real=True)
h=v/(1-v*v)**4;ck('rational_map_derivative',s.simplify(s.diff(h,v)-(1+7*v*v)/(1-v*v)**5)==0)
a=s.sqrt(1+y*y);matrix=s.Matrix([[s.diff(k*a,k),s.diff(k*a,y)],[0,1]]);ck('foliation_jacobian',s.simplify(matrix.det()-a)==0)
for q in [s.Matrix([A*t,B*t*z]),s.Matrix([A*t*z,B*t])]:ck('duffy_signed_jacobian_'+str(q[0]),s.simplify(q.jacobian([t,z]).det()**2-A*A*B*B*t*t)==0)
for yy in [-100,-10,-1,-.3,0,.3,1,10,100]:ck('height_inverse_'+str(yy),abs(ymap(vmap(yy))-yy)<2e-11*max(1,abs(yy)))
# The source formula is verified through a different differentiation method.
coef=np.array([-1,9,-45,0,45,-9,1])/60;shifts=np.arange(-3,4)
points=np.array([[.1,.3],[1,1],[2.3,0],[3.8,1],[30,10],[3000,1000],[1e5,2e5],[-3.8,1],[2.05,0],[2.98,0]])
for x,yv in points:
 om=float(fields(x,yv)[1]);errs=[]
 for rel in [1e-5,5e-6]:
  delta=rel*max(1,np.hypot(x,yv));dx=np.sum(fields(x+shifts*delta,yv)[0][:,1]*coef)/delta;dy=np.sum(fields(x,yv+shifts*delta)[0][:,0]*coef)/delta;errs.append(float(abs(om+dx-dy)/(1+abs(om))))
 ck('source_negative_curl_'+str([x,yv]),max(errs)<2e-8);records.append({'point':[float(x),float(yv)],'omega':om,'normalized_curl_gaps':errs})
ss=np.array([4.001,4.1,4.3,4.7,5.5,6.5,7.5,8.3,8.7,8.9,8.999]);delta=1e-5;vals,cp,cpp=cutoff(ss);allc,allcp,_=cutoff(ss[:,None]+delta*shifts);dcp=allc@coef/delta;dcpp=allcp@coef/delta;ck('cutoff_first_derivative',np.max(abs(dcp-cp))<1e-9);ck('cutoff_second_derivative',np.max(abs(dcpp-cpp))<1e-9)
probe=np.array([[.8,.3],[-.8,.3],[2.3,0],[-2.3,0]])
for i in [0,2]:
 up,op=fields(*probe[i]);un,on=fields(*probe[i+1]);ck('x_parity_'+str(i),np.max(abs(un-up*np.array([-1,1])))==0 and op==-on)
initial=json.loads((vdir/'initial_direct_inverse.json').read_text());new=json.loads((vdir/'duffy_inverse.json').read_text());target=np.array(new['analytic_velocity'])
ck('same_target_points',new['points']==initial['points']);ck('same_analytic_velocities',new['analytic_velocity']==initial['exact_velocity_float']);ck('five_orders',[q['order']for q in new['levels']]==[12,20,32,48,72]);errs=[]
for level in new['levels']:
 e=np.max(abs(np.array(level['velocity'])-target));errs.append(float(e));ck('raw_max_order_'+str(level['order']),e==level['max_abs_error'])
ck('monotone_errors',all(a>b for a,b in zip(errs[:-1],errs[1:])));ck('last_error_below_1e-11',errs[-1]<1e-11);ck('same_duffy_panel_counts',all([g['duffy_panels']for g in q['geometry']]==[4,4,4,4,4,0]for q in new['levels']));ck('initial_failure_retained',initial['levels'][-1]['max_abs_error']>2)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'all_passed':all(checks.values()),'curl_checks':records,'cutoff_first_gap':float(np.max(abs(dcp-cp))),'cutoff_second_gap':float(np.max(abs(dcpp-cpp))),'duffy_max_errors':errs,'scope':'Finite manufactured consistency and exact symbolic coordinate identities. No rigorous numerical inverse enclosure; no B2 profile.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(vdir/'geometry_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(len(checks),out['all_passed'],[k for k,b in checks.items()if not b]);assert out['all_passed']

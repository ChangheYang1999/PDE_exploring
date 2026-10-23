"""Independent finite-grid q, gradient and strain lower estimates near the core."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,math
import numpy as np
from angular_log_inverse import QAngular,AngularLogInverse
ap=argparse.ArgumentParser();ap.add_argument('diagnostic');ap.add_argument('--tag',required=True);args=ap.parse_args()
old=json.loads(Path(args.diagnostic).read_text());model=QAngular(old['snapshot'])
out=Path('evidence/q_local_refinement')/args.tag;out.mkdir(parents=True,exist_ok=True)
result=dict(started_utc=datetime.now(timezone.utc).isoformat(),source=args.diagnostic,snapshot=old['snapshot'],metadata=model.meta,a=model.a,c=model.c,rows=[])

def sample(logr,theta,order,label):
 field=AngularLogInverse(model,order).fields(logr,theta)
 quotient=np.empty_like(field['H']);nonaxis=theta!=0
 quotient[:,nonaxis]=1+field['H'][:,nonaxis]/(model.a*np.sin(theta[nonaxis]))
 quotient[:,~nonaxis]=1+field['Htheta'][:,~nonaxis]/model.a
 row=dict(grid=label,inverse_order=order,radii=len(logr),angles=len(theta),log10_radius_window=[float(logr[0]/math.log(10)),float(logr[-1]/math.log(10))],theta_window=[float(theta[0]),float(theta[-1])])
 for name,values in [('q',quotient),('gradient',field['gradient_norm']),('strain',field['strain'])]:
  i,j=np.unravel_index(np.argmax(values),values.shape)
  row[name]=dict(value=float(values[i,j]),log10_radius=float(logr[i]/math.log(10)),theta=float(theta[j]))
 row['strain_above_D']=row['strain']['value']-(model.cl-1)
 row['gradient_relative_excess']=row['gradient']['value']/abs(model.a)-1
 row['q_excess']=row['q']['value']-1
 result['rows'].append(row);result['updated_utc']=datetime.now(timezone.utc).isoformat()
 (out/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(row),flush=True)
 return row

logr=np.unique(np.concatenate((model.log_core+np.linspace(-16,26,505),np.arange(-160,301,4)*math.log(10))))
theta=np.linspace(0,math.pi/2,8*model.M+65)
base=sample(logr,theta,128,'wide')
# Each maximum gets its own physical neighborhood. Retain the same
# nodes while changing inverse order, so quadrature error is visible.
for name in ['q','gradient','strain']:
 ctr=base[name];lg=ctr['log10_radius'];th=ctr['theta']
 rr=np.linspace(lg-.25,lg+.25,101)*math.log(10)
 tt=np.linspace(max(0,th-.14),min(math.pi/2,th+.14),129)
 for order in [128,192,256]:sample(rr,tt,order,'local_'+name)
result['status']='COMPUTED';result['finished_utc']=datetime.now(timezone.utc).isoformat()
result['scope']='Independent density and canonical inverse. Maxima over explicit finite grids are lower estimates of global suprema, with inverse quadrature refinement at fixed nodes. No interval enclosure. Exact gradient witnesses and canonical center moments are recorded separately.'
(out/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')

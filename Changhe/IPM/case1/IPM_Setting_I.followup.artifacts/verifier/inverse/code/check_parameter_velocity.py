"""Finite parameter perturbations through the independently implemented inverse."""
import copy,json,sys,time
from pathlib import Path
import numpy as np
from collocation import NodalDensity
from density import gradient_fd
from gpu import Kernel,GPUField
from linearized import direction_coefficients
from strain import strain
source=NodalDensity('numerics/data/dnSB_n120m48.npz')
with np.load('verifier/inverse/verification/dnSB_directions.npz') as z:V=z['V'];labels=z['labels'].tolist()
co=direction_coefficients(source,V)
reference=json.loads(Path('verifier/inverse/verification/dnSB_actions_4096.json').read_text())
point=[.20794827803092428,9.99783764189357]
ref=next(r for r in reference['rows'] if r['point']==point)
ker=Kernel(GPUField(source),4096,24,.12,rmax=1e16)
rows=[];path=Path(sys.argv[1])
for j in [0,3,6]:
 for eps in [.01,.003,.001]:
  vals=[];start=time.monotonic()
  for sign in [-1,1]:
   f=copy.copy(source);f.co=source.co+sign*eps*co[:,:,j];f.cl=source.cl+sign*eps*V[-2,j];f.k=1/f.cl
   ker.f=GPUField(f);u=ker.velocity(point);g=gradient_fd(f,*point,relative_step=.0005);rho=float(f(*point));W=f.cl*np.array(point)+u
   c,_=strain(f,1024,20,.16,rmax=1e16)
   vals.append({'U':u,'R':float(W@g-rho),'origin_c':c})
  fdU=(vals[1]['U']-vals[0]['U'])/(2*eps);fdR=(vals[1]['R']-vals[0]['R'])/(2*eps);fdc=(vals[1]['origin_c']-vals[0]['origin_c'])/(2*eps)
  exactU=np.array(ref['velocity_action'][j]);exactR=ref['transport_action'][j]
  row={'direction':labels[j],'index':j,'eps':eps,'point':point,'velocity_fd':fdU.tolist(),'velocity_linear':exactU.tolist(),'velocity_difference':(fdU-exactU).tolist(),'transport_fd':fdR,'transport_linear':exactR,'transport_difference':fdR-exactR,'c_fd':fdc,'linear_identity_defect_3dcl_dc':3*V[-2,j]-fdc,'seconds':time.monotonic()-start}
  rows.append(row);path.write_text(json.dumps({'source_md5':source.md5,'rows':rows},indent=2)+'\n');print(json.dumps(row),flush=True)

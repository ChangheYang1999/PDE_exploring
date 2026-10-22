"""Whole-plane center strain of the independent forced characteristic field.
Gauss quadrature after r=L(t^(-beta)-1), independent angular nodes; adaptive
DOP853 characteristics and analytic Gaussian inverse. This tests epsilon0,
not the self-consistent PDE. A converged quadrature is not an existence proof.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,math,hashlib,os,sys
import numpy as np
from numpy.polynomial.legendre import leggauss
from gaussian_characteristics import GaussianFlow
start=time.monotonic();g=GaussianFlow();root=Path(sys.argv[1] if len(sys.argv)>1 else 'verification/gaussian_feedback');root.mkdir(exist_ok=True)
configs=[(12,16,1.5,3e-4),(18,24,1.5,3e-4),(26,36,1.5,3e-4),(26,36,.75,3e-4),(26,36,3.,3e-4),(26,36,1.5,1e-4)]
if len(sys.argv)>2:configs=json.loads(Path(sys.argv[2]).read_text())
out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Independent forced epsilon0 feedback, not a B2 candidate','pid':os.getpid(),'parameters':vars(g),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'characteristic_source_sha256':hashlib.sha256(Path('code_independent/gaussian_characteristics.py').read_bytes()).hexdigest(),'configs':configs,'runs':[]}
(root/'status.json').write_text(json.dumps(out,indent=2)+'\n')
for nr,na,L,rin in configs:
 z,w=leggauss(nr);t=(z+1)/2;wr=w/2;radius=L*(t**(-g.beta)-1);wr=wr*L*g.beta*t**(-g.beta-1)/radius
 z,w=leggauss(na);angles=np.pi*z/2;wa=np.pi*w/2
 values=[];bad=[];begin=time.monotonic();path=root/f'points_r{nr}_a{na}_L{L:g}_rin{rin:g}.jsonl';total=nr*na
 with path.open('w') as log:
  for ir,(r,rweight) in enumerate(zip(radius,wr)):
   for ia,(angle,aweight) in enumerate(zip(angles,wa)):
    point=[float(r*math.cos(angle)),float(r*math.sin(angle))];res=g.evaluate(point,r_in=rin,rtol=2e-9)
    term=2/math.pi*rweight*aweight*math.sin(angle)*math.cos(angle)*res['Omega'] if 'Omega' in res else float('nan')
    row={'ir':ir,'ia':ia,'point':point,'term':float(term),**res};log.write(json.dumps(row)+'\n');values.append(float(term))
    if res['status'] not in ('COMPLETE','LOCAL_JET'):bad.append(row)
    if len(values)%32==0:
     log.flush();status={**out,'current':{'nr':nr,'na':na,'L':L,'r_in':rin,'completed_points':len(values),'total_points':total,'elapsed_run':time.monotonic()-begin,'failures':len(bad)}};(root/'status.json').write_text(json.dumps(status,indent=2)+'\n');print('progress',nr,na,L,rin,len(values),total,'sum',math.fsum(values),'seconds',round(time.monotonic()-begin,1),flush=True)
 row={'nr':nr,'na':na,'L':L,'r_in':rin,'c_self':math.fsum(values),'c_input':g.c,'closure_defect':math.fsum(values)-g.c,'maximum_sample_radius':float(max(radius)),'minimum_sample_radius':float(min(radius)),'failed_points':len(bad),'elapsed_seconds':time.monotonic()-begin,'point_file':str(path)};out['runs'].append(row);(root/'status.json').write_text(json.dumps(out,indent=2)+'\n');print('RUN_COMPLETE',row,flush=True)
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='COMPLETE');(root/'status.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)

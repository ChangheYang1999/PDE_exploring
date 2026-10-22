"""Independent full-plane scalar feedback for a positive slow-tail forcing.
No fitted num code, finite cutoff or modal inverse; each point is evaluated
by independent adaptive characteristic integration. Exploratory numerics.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,os,sys,time
import numpy as np
from numpy.polynomial.legendre import leggauss
from shifted_power_flow import ShiftedPowerFlow

root=Path(sys.argv[1] if len(sys.argv)>1 else 'verification/shifted_power_feedback');root.mkdir(exist_ok=True)
configs=json.loads(Path(sys.argv[2]).read_text()) if len(sys.argv)>2 else [[2.5,12,16,1.,1e-4],[3.,12,16,1.,1e-4],[4.,12,16,1.,1e-4],[6.,12,16,1.,1e-4]]
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Exploratory forced fields. Scalar feedback alone cannot establish closure or existence.','pid':os.getpid(),'sources':{p:hashlib.sha256(Path('code_independent',p).read_bytes()).hexdigest() for p in ('shifted_power_feedback.py','shifted_power_flow.py','gaussian_characteristics.py')},'configs':configs,'runs':[]}
def save(extra=None):
 (root/'status.json').write_text(json.dumps({**out,**(extra or {})},indent=2)+'\n')
save()
for beta,nr,na,Lfactor,rin in configs:
 f=ShiftedPowerFlow(beta);L=f.L*Lfactor;z,w=leggauss(nr);t=(z+1)/2;r=L*(t**(-beta)-1);wr=w/2*L*beta*t**(-beta-1)/r
 z,w=leggauss(na);ang=z*np.pi/2;wa=w*np.pi/2;terms=[];bad=0;begin=time.monotonic();path=root/f'b{beta:g}_r{nr}_a{na}_L{Lfactor:g}_rin{rin:g}.jsonl'
 with path.open('w') as stream:
  for ir,(rr,rw) in enumerate(zip(r,wr)):
   for ia,(phi,aw) in enumerate(zip(ang,wa)):
    point=[float(rr*math.cos(phi)),float(rr*math.sin(phi))];v=f.evaluate(point,r_in=rin,rtol=2e-9,max_time=240.)
    term=2/math.pi*rw*aw*math.cos(phi)*math.sin(phi)*v['Omega'] if 'Omega' in v else float('nan');terms.append(term)
    if v['status'] not in ('COMPLETE','LOCAL_JET'):bad+=1
    stream.write(json.dumps({'ir':ir,'ia':ia,'point':point,'term':term,**v})+'\n')
    if len(terms)%24==0:
     stream.flush();save({'current':{'beta':beta,'completed':len(terms),'total':nr*na,'elapsed_seconds':time.monotonic()-begin,'failures':bad}});print(beta,len(terms),nr*na,'partial',math.fsum(terms),flush=True)
 row={'beta':beta,'nr':nr,'na':na,'Lfactor':Lfactor,'L':L,'r_in':rin,'c_input':f.c,'c_self':math.fsum(terms),'closure_defect':math.fsum(terms)-f.c,'failed_points':bad,'minimum_radius':float(min(r)),'maximum_radius':float(max(r)),'elapsed_seconds':time.monotonic()-begin,'point_file':str(path),'parameters':vars(f)};out['runs'].append(row);save();print('RUN_COMPLETE',row,flush=True)
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='COMPLETE');save();print('COMPLETE',out['elapsed_seconds'],flush=True)

"""Independent exact represented-spline shell integral plus physical-radius check."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,shutil,hashlib,time
import numpy as np
from scipy.interpolate import BSpline,PPoly
from scipy.integrate import quad
from r2_state_values import R2State
root=Path(sys.argv[1]);manifest=json.loads((root/'manifest.json').read_text())
started=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'states':[]}
for item in manifest['states']:
 s=R2State(root/item['snapshot']);d=s.Gs.c[:,1]-(s.Gs.c[:,3] if s.K>3 else 0)
 spl=BSpline(s.knots,d,s.degree);pp=PPoly.from_spline(spl)
 roots=pp.roots(extrapolate=False);roots=roots[np.isfinite(roots)&(roots>0)&(roots<1)]
 cuts=np.unique(np.r_[s.edges,roots]);absint=sum(abs(spl.integrate(a,b)) for a,b in zip(cuts[:-1],cuts[1:]))
 c=-s.bb*s.L/4*spl.integrate(0,1);cabs=s.bb*s.L/4*absint
 theta=2*np.pi*(np.arange(96)+.271)/96
 def H2(r):
  return 2*np.mean(s.omega(r*np.sin(theta),-r*np.cos(theta))*np.sin(2*theta))
 def physical_tail(R):
  def f(u):
   if u==0:return -s.bb*float((s.L**(1+1/s.bb)/2)*spl(1))*R**(-1/s.bb)/2
   r=R*u**(-s.bb)
   return -s.bb*.5*H2(r)/u
  return quad(f,0,1,epsabs=3e-10,epsrel=3e-10,limit=300)
 row={'label':item['label'],'sha256':s.sha256,'beta':s.beta,'L':s.L,'a0':s.meta.get('a0'),
      'eps':s.meta.get('eps'),'c':float(c),'c_abs':float(cabs),'cancellation_ratio':float(cabs/abs(c)),
      'a2':float(s.L**(1+1/s.bb)*spl(1)/2),'roots_count':len(roots),'roots':roots.tolist(),'shells':[]}
 for R in [1,3,10,30,100,1000,1e4,1e8]:
  delta=np.exp(-np.log1p((R/s.L)**2)/(2*s.bb));t=1-delta
  exact=-s.bb*s.L/4*spl.integrate(t,1)
  direct,error=physical_tail(R)
  final=None
  if t>=s.edges[-2]:
   from math import factorial
   final=-s.bb*s.L/4*sum((-1)**j*spl.derivative(j)(1)*delta**(j+1)/factorial(j+1) for j in range(s.degree+1))
  row['shells'].append({'R':R,'C_outside':float(exact),'fraction':float(exact/c),'physical_angular_quad':direct,'quad_error_estimate':error,'difference':float(exact-direct),'tail_leading':float(-s.bb*row['a2']/2*R**(-1/s.bb)),'last_cell_polynomial':float(final) if final is not None else None})
 out['states'].append(row)
 print(item['label'],'c',c,'C_abs/c',cabs/abs(c),'max physical diff',max(abs(a['difference']) for a in row['shells']),flush=True)
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-started,status='COMPLETE',scope='Exact formulas evaluated in floating point for represented fields; no interval certificate or PDE inference.',code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n');shutil.copyfile(__file__,root/'strain_shell_audit_snapshot.py')

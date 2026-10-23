"""Result208: frozen finite trace coefficients, no producer code."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,time
import numpy as np
import mpmath as mp
import torch
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from hydrostatic_trace_coefficients import *
torch.set_num_threads(1)
v=Path('research/hydrostatic_trace_compatibility_diagnostic/verification');gate=json.loads((v/'MANUFACTURED.json').read_text());assert gate['fail_count']==0
assert gate['module_sha256']==hashlib.sha256(Path('independent_code/hydrostatic_trace_coefficients.py').read_bytes()).hexdigest()
inputs=json.loads((v/'INPUTS.json').read_text());out=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',states=[],module_sha256=gate['module_sha256']);t0=time.monotonic()
def save():(v/'STATES.json').write_text(json.dumps(out,indent=2)+'\n')
for row in inputs['states']:
 path=Path(row['file']);assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256']
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(path)
 b,bp=stored_endpoint_data(q);P=Fraction(q.kappa);p=1-1/P;L=Fraction(q.L)
 item=dict(tag=row['tag'],sha256=row['sha256'],N=q.N,M=q.M,c=q.cl,P_exact=str(P),p_exact=str(p),precision=[],trace_limits=[])
 for digits in [70,100]:
  with mp.workdps(digits):
   pref=exactmp(L)**(1/exactmp(P))/2;a=monomials(b,pref);val=moments(a,p);val['Cp_over_K']=val['Cp']/val['K'];val['c_p_minus1']=exactmp(Fraction(q.cl)*p-1)
   A2m=[exactmp(L)**(2/exactmp(P))*(-exactmp(t)/(8*exactmp(P))-k*exactmp(t)/4-exactmp(db)/2)for k,(t,db)in enumerate(zip(b,bp))]
   item['precision'].append(dict(digits=digits,values={k:mp.nstr(t,digits-5)for k,t in val.items()}))
   if digits==100:
    item['Cp_over_K']=float(val['Cp_over_K']);item['K']=float(val['K']);item['Q']=float(val['Q']);item['Cp']=float(val['Cp'])
    jet=CartesianQJet(q)
    for rad in [1e4,1e6,1e8]:
     for theta in [.23,.71,1.31,np.pi/2]:
      if theta==np.pi/2:x=0.;y=rad;th=mp.pi/2
      else:x=rad*np.cos(theta);y=rad*np.sin(theta);th=exactmp(theta)
      density=float(jet.jet(x,y)[0]);actual=exactmp(density)/exactmp(rad)**exactmp(p)
      lim=trace_at(th,b,pref);nextval=trace_at(th,A2m);err=actual-lim;scaled=err*exactmp(rad)**(1/exactmp(P))
      item['trace_limits'].append(dict(r=rad,theta=theta,density=density,trace=float(lim),scaled_density=float(actual),absolute_trace_error=float(abs(err)),first_correction=float(scaled),predicted_A2=float(nextval),first_correction_error=float(abs(scaled-nextval))))
 with mp.workdps(110):
  d0=item['precision'][0]['values'];d1=item['precision'][1]['values'];item['precision_absolute_changes']={k:mp.nstr(abs(mp.mpf(d0[k])-mp.mpf(d1[k])),20)for k in d0}
  assert all(mp.mpf(e)<mp.mpf('1e-40')*(1+abs(mp.mpf(d1[k])))for k,e in item['precision_absolute_changes'].items())
 out['states'].append(item);save();print(row['tag'],item['Cp_over_K'],'K',item['K'],flush=True)
out.update(status='DONE',finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0);save()
lines=['# Independent finite trace coefficients','',f"Computed {out['finished_utc']}. K and Cp below are from exact stored binary coefficients, evaluated at70and100digits. They are finite-data diagnostics, not profiles.",'','| State | N x M | K | Cp/K |','|---|---:|---:|---:|']
for s in out['states']:lines.append(f"| {s['tag']} | {s['N']} x {s['M']} | {s['K']:.9g} | {s['Cp_over_K']:.12g} |")
lines+=['','The c2 N128 field is the frozen40-iteration-cap state, not a later continuation. Formal Cp compatibility does not by itself bound finite-radius residuals uniformly under refinement. Trace limit and A2 approach checks are in STATES.json.']
(v/'TABLE.md').write_text('\n'.join(lines)+'\n');print(out['finished_utc'],'DONE',out['elapsed_seconds'],flush=True)

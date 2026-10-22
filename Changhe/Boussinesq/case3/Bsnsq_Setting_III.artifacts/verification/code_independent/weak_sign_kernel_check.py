"""Manufactured angular inverse check. No B2 candidate or proof certificate."""
from pathlib import Path
from datetime import datetime,timezone
import time,json,hashlib
import numpy as np
from numpy.polynomial.legendre import leggauss
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'angular Green middle-row versus exact Fourier inverse; no profile claim','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':[]}
eps=.7
for beta in [2.,2.5,3.,4.,10.,100.]:
 k=2-1/beta
 exact=(1+eps**2/4)/(k*k-1)-(eps**2/4)/(k*k-9)
 for n in [12,24,48]:
  x,w=leggauss(n);total=0.
  for lo,hi in [(-np.pi/2,0),(0,np.pi/2)]:
   s=(hi+lo)/2+(hi-lo)*x/2
   kernel=np.sin(k*np.pi/2)*np.sin(k*(np.pi/2-np.abs(s)))/(-k*np.sin(k*np.pi))
   a=np.cos(s)*(1+eps*np.sin(s))**2
   total+=(hi-lo)/2*np.dot(w,kernel*a)
  out['rows'].append({'beta':beta,'k':k,'order':n,'integral':total,'exact_modal':exact,'absolute_error':abs(total-exact)})
out.update(status='COMPLETE',elapsed_seconds=time.monotonic()-start,ended_utc=datetime.now(timezone.utc).isoformat())
Path('research/56_weak_sign_extrema/verification/kernel_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'elapsed_seconds':out['elapsed_seconds'],'max_error':max(r['absolute_error'] for r in out['rows']),'max_error_order48':max(r['absolute_error'] for r in out['rows'] if r['order']==48)},indent=2))

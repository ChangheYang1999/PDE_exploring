from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp,time,json
from generating_function_values import derivatives,physical
mp.mp.dps=85;start=time.monotonic();checks=[]
for beta in map(mp.mpf,['2.2','3','4.7']):
 a0=mp.mpf('1.3')
 for h in [mp.mpf('.17'),-4*a0/(beta*(beta+6))]:
  f=lambda q,y:q*y+h*q**3/3
  for q,y in [(mp.mpf('.3'),mp.mpf('-.6')),(mp.mpf('1.2'),mp.mpf('2.3'))]:
   exact={'x':q,'J':mp.mpf(1),'Omega':-h*(beta+6)*q,'W1':(beta/2-1)*q,'W2':(3*beta/2+1)*y+h*(beta/2+3)*q*q,'residual':-(h*beta*(beta+6)/2+2*a0)*q}
   for n in [9,11]:
    result=physical(derivatives(f,q,y,mp.mpf('.001'),n),q,y,beta,a0)
    err=max(abs(result[k]-v)for k,v in exact.items());assert err<mp.mpf('1e-60'),err
    checks.append({'beta':str(beta),'h':str(h),'q':str(q),'y':str(y),'stencil':n,'max_error':str(err)})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','checks':checks,'elapsed_seconds':time.monotonic()-start};Path('research/105_independent_generating_function_evaluator/verification/manufactured.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks),out['elapsed_seconds'])

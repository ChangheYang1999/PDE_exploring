from pathlib import Path
from datetime import datetime,timezone
import sys,time,json,numpy as np
from local_circle_batch_exchange import transport_batch_exchange
from local_circle_greedy import transport_greedy
from local_circle_exchange import transport_exchange
from certify_local_circles_greedy import angular_data,UNIT
from flint import arb

def main():
 rows=[];started=time.monotonic()
 for n in [64,128,256]:
  for r in [.02,.1,.25,.45]:
   for phase in [0,8,12,16,24,32]:
    a=arb(str(r));phi=arb.pi()*phase/32;m,tv,arcs,mids=angular_data(a,a,phi,n)
    atom=int(float(.25*np.sqrt(2*r))*UNIT);m +=[-atom,atom]
    points=[.5+r*complex(float(z.real.mid()),float(z.imag.mid())) for z in mids];points +=[-z for z in points];points +=[.5,-.5]
    cs={};times={};infos={}
    for name,fn in [('greedy',transport_greedy),('batch',transport_batch_exchange)]:
     t=time.monotonic();plan,info=fn(m,points,.5);times[name]=time.monotonic()-t;infos[name]=info
     cs[name]=sum(mass/UNIT*abs(points[i]-points[j])**.5 for (i,j),mass in plan.items())
    assert cs['batch']<=cs['greedy']+1e-12
    row=dict(n=n,r=r,phase=phase,costs=cs,times=times,info=infos);rows.append(row)
    print(n,r,phase,cs,times,flush=True)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-started,rows=rows,status='Float plan quality diagnostics; exact marginals checked for every plan. No operator bound.')
 Path('data/batch_exchange_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()

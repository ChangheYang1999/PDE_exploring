"""Compare candidate plans on actual extracted diagonal masses. Diagnostic."""
from pathlib import Path
from datetime import datetime,timezone
import time,json
from flint import arb,ctx
from certify_local_circles_greedy import angular_data,UNIT
from local_circle_greedy import transport_greedy
from local_circle_exchange import transport_exchange
from local_circle_exact_plan import transport
ctx.prec=160
rows=[]
for n in [64,128]:
 for r in [.02,.1,.25,.45]:
  for phase in [0,8,12,16,24,32]:
   a=arb(r);b=a+arb(1)/512;masses,tv,arcs,mids=angular_data(a,b,arb.pi()*phase/32,n)
   atom=int(((a*UNIT).lower()).floor().unique_fmpz());masses+= [-atom,atom]
   z=[.5+r*complex(float(v.real.mid()),float(v.imag.mid())) for v in mids];z+=[-x for x in z];z += [.5,-.5]
   costs={};times={}
   for name,fun in [('greedy',transport_greedy),('exchange',transport_exchange),('LP',transport)]:
    start=time.monotonic();plan,info=fun(masses,z,.5);times[name]=time.monotonic()-start
    costs[name]=sum(m/UNIT*abs(z[i]-z[j])**.5 for (i,j),m in plan.items())
   row=dict(n=n,r=r,phase=phase,costs=costs,times=times);rows.append(row);print(row,flush=True)
Path('data/local_exchange_diagnostic.json').write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=rows,status='Float plan-selection costs only, not operator estimates'),indent=2)+'\n')

"""FLOAT diagnostic; produces no certified bound."""
from pathlib import Path
from datetime import datetime,timezone
import time,json
import numpy as np
from geometry import derive
B=Path(__file__).resolve().parents[1]
start=time.monotonic();rows=[]
theta=np.linspace(0,np.pi/2,20001)
for name in ('007','013','014'):
 j=json.loads((B/f'data/{name}_endpoint.json').read_text())
 q,p,s,va,vb,t=derive(j)
 values=sum(float(v)*np.cos(n*theta) for n,v in t.items())
 k=int(np.argmax(values))
 rows.append({'candidate':name,'q':str(q),'max_frequency':max(t),'FLOAT_max_T':float(values[k]),'FLOAT_E':float(np.sqrt(values[k])),'FLOAT_angle':float(theta[k]),'l1_T_upper_FLOAT':sum(abs(float(v)) for v in t.values())})
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'status':'FLOAT diagnostic only','rows':rows}
(B/'verification/scout.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

from pathlib import Path
from datetime import datetime,timezone
import json,numpy as np
root=Path(__file__).resolve().parents[1];v=root/'verification';k=.2;a2=(k+1)/(4*(1-k)*(k+3));a4=-1/(8*(k+5));out={'date':datetime.now(timezone.utc).isoformat(),'scope':'manufactured inverse asymptotics, not a profile or interval certificate','rows':[]}
lo=json.loads((v/'inverse1024.json').read_text());hi=json.loads((v/'inverse2048.json').read_text())
for old,row in zip(lo['rows'],hi['rows']):
 x,y=row['point'];r=np.hypot(x,y);th=np.arctan2(y,x);er=np.array([x,y])/r;et=np.array([-y,x])/r
 exact=-(2*a2*np.cos(2*th)+4*a4*np.cos(4*th))*er+(k+1)*(a2*np.sin(2*th)+a4*np.sin(4*th))*et
 u=np.array(row['U'])/r**k;out['rows'].append({'r':r,'theta':th,'scaled_U':u.tolist(),'homogeneous_U':exact.tolist(),'max_difference':float(np.max(abs(u-exact))),'refinement_change':float(np.max(abs(u-np.array(old['U'])/r**k)))})
(v/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
for row in out['rows']:print(row['r'],row['theta'],row['max_difference'],row['refinement_change'])

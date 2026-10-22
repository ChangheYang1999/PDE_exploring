import datetime,json,time
from pathlib import Path
import numpy as np
from read_polar_data import PolarData
from characteristic_check import reconstruct
out=Path('runs/polar_characteristics');out.mkdir(parents=True,exist_ok=True)
points=np.array([[.31,.77],[1.1,.2],[.4,1.7],[3.1,2.3],[7.3,.41],[0.,1.17],[1.17,0.]])
rows=[]
for tol,n in [(1e-7,48),(1e-9,72),(1e-11,96)]:
 start=time.monotonic();obj=PolarData('runs/polar_prelim_b3_verification/source_coefficients.npz',radial_order=n)
 row=reconstruct(obj,points,rtol=tol,atol=tol*1e-4,hrel=.001)
 row['radial_order']=n;row['seconds']=time.monotonic()-start;row['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
 rows.append(row);(out/'verification.json').write_text(json.dumps(rows,indent=2)+'\n')
 last=row['rows'][-1]
 print(json.dumps({'utc':row['utc'],'seconds':row['seconds'],'rtol':tol,'nfev':row['nfev'],'theta_origin_defect':last['theta_origin_defect'],'omega_finite_defect':last['omega_finite_defect']}),flush=True)
(out/'finished.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),'status':'complete; no endpoint'},indent=2)+'\n')

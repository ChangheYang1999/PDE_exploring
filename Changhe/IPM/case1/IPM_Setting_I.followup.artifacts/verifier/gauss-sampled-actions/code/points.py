from pathlib import Path
from datetime import datetime,timezone
import numpy as np,json,hashlib
R=Path(__file__).resolve().parents[1];z,w=np.polynomial.legendre.leggauss(8);a=np.log(.05);b=np.log(100.);r=np.exp((a+b)/2+(b-a)*z/2);t=np.pi*(1+z)/4
pts=[[float(x*np.cos(y)),float(x*np.sin(y))] for x in r for y in t];weights=[float(x*y/4) for x in w for y in w]
out={'utc':datetime.now(timezone.utc).isoformat(),'points':pts,'weights':weights,'radial_nodes':r.tolist(),'angle_nodes':t.tolist(),'sum_weights':sum(weights),'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest(),'scope':'Prescribed before velocity evaluation. Saved binary64points andweights define the actual finite matrices.'}
path=R/'verification/points.json';assert not path.exists();path.write_text(json.dumps(out,indent=2)+'\n');print('POINTS_FROZEN',out['utc'],out['sum_weights'])

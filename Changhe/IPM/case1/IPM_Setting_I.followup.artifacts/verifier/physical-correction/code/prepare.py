from pathlib import Path
from datetime import datetime,timezone
import numpy as np,json,hashlib
root=Path(__file__).resolve().parents[1]
source=Path('numerics/data/dnSB_n120m48.npz');old=np.load(source)
action=Path('verifier/inverse/verification/dnSB_actions_2048.json');d=json.loads(action.read_text());fit=d['rows'][:8]
J=np.array([r['transport_action_over_Nv'] for r in fit]);F=np.array([r['base_R']/r['Nv'] for r in fit]);U,S,Vh=np.linalg.svd(J,full_matrices=False);good=S>1e-5;step=-Vh[good].T@((U[:,good].T@F)/S[good])
dirs=Path('verifier/inverse/verification/dnSB_directions.npz');dv=np.load(dirs)['V'];dz=dv@step
points=[r['point'] for r in fit]
for r in [.5,3.,6.,10.,30.,100.]:
 for theta in [.15,.75,1.4]:points.append([float(r*np.cos(theta)),float(r*np.sin(theta))])
ptstr=';'.join(','.join(format(x,'.17g') for x in pt) for pt in points)
(root/'verification/points.txt').write_text(ptstr+'\n');(root/'verification/points.json').write_text(json.dumps(points,indent=2)+'\n')
meta={'date':datetime.now(timezone.utc).isoformat(),'source_md5':hashlib.md5(source.read_bytes()).hexdigest(),'action_md5':hashlib.md5(action.read_bytes()).hexdigest(),'direction_md5':hashlib.md5(dirs.read_bytes()).hexdigest(),'fit_points':points[:8],'holdout_points':points[8:],'singular_values':S.tolist(),'cutoff':1e-5,'step_coefficients':step.tolist(),'node_step_norm':float(np.linalg.norm(dz)),'dcl':float(dz[-2]),'base_fit_norm':float(np.linalg.norm(F)),'predicted_fit_norm_full_step':float(np.linalg.norm(F+J@step)),'trials':[]}
for t in [.25,.5,1.]:
 tag='t'+str(t).replace('.','p');b=old['b'].copy();b[1:]+=t*dz[:-2].reshape(120,48);cl=float(old['c_l'])+t*dz[-2];C=float(old['C'])+t*dz[-1]
 assert cl>1 and np.array_equal(b[0],np.ones(48))
 path=root/'data'/('physical_'+tag+'.npz')
 payload={k:old[k] for k in ['N','M','L','beta','q','theta']};payload.update(b=b,c_l=cl,C=C,tag='physical_'+tag,formulation='independent reduced physical residual correction; not an orbit solve')
 np.savez_compressed(path,**payload)
 meta['trials'].append({'tag':tag,'path':str(path),'t':t,'cl':cl,'C_aux':C,'md5':hashlib.md5(path.read_bytes()).hexdigest(),'linear_prediction':(F+t*J@step).tolist()})
(root/'verification/setup.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta,indent=2))

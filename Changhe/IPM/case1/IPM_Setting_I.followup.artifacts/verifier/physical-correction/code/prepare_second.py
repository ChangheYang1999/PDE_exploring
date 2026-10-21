from pathlib import Path
from datetime import datetime,timezone
import numpy as np,json,hashlib
root=Path(__file__).resolve().parents[1];v=root/'verification'
source=root/'data/physical_t1p0.npz';old=np.load(source);action=v/'t1p0_actions2048.json';d=json.loads(action.read_text());fit=d['rows'];assert len(fit)==26
J=np.array([r['transport_action_over_Nv'] for r in fit]);F=np.array([r['base_R']/r['Nv'] for r in fit]);U,S,Vh=np.linalg.svd(J,full_matrices=False);good=S>1e-5;step=-Vh[good].T@((U[:,good].T@F)/S[good])
dirs=Path('verifier/inverse/verification/dnSB_directions.npz');dv=np.load(dirs)['V'];dz=dv@step
points=[r['point'] for r in fit];hold=[]
for r in [.2,2.,8.,15.,50.,300.]:
 for theta in [.4,1.2,1.52]:hold.append([float(r*np.cos(theta)),float(r*np.sin(theta))])
points+=hold
for label,pp in [('points_second',points),('holdouts_second',hold)]:
 (v/(label+'.json')).write_text(json.dumps(pp,indent=2)+'\n');(v/(label+'.txt')).write_text(';'.join(','.join(format(x,'.17g') for x in pt) for pt in pp)+'\n')
meta={'date':datetime.now(timezone.utc).isoformat(),'source_md5':hashlib.md5(source.read_bytes()).hexdigest(),'action_md5':hashlib.md5(action.read_bytes()).hexdigest(),'direction_md5':hashlib.md5(dirs.read_bytes()).hexdigest(),'fit_points':points[:26],'fresh_holdouts':hold,'singular_values':S.tolist(),'cutoff':1e-5,'step_coefficients':step.tolist(),'node_step_norm':float(np.linalg.norm(dz)),'dcl':float(dz[-2]),'base_fit_norm':float(np.linalg.norm(F)),'predicted_fit_norm_full_step':float(np.linalg.norm(F+J@step)),'trials':[]}
for t in [.25,.5,1.]:
 tag='s2_t'+str(t).replace('.','p');b=old['b'].copy();b[1:]+=t*dz[:-2].reshape(120,48);cl=float(old['c_l'])+t*dz[-2];C=float(old['C'])+t*dz[-1]
 assert cl>1 and np.array_equal(b[0],np.ones(48))
 path=root/'data'/('physical_'+tag+'.npz');payload={k:old[k] for k in ['N','M','L','beta','q','theta']};payload.update(b=b,c_l=cl,C=C,tag='physical_'+tag,formulation='independent second sampled physical correction; not an orbit solve');np.savez_compressed(path,**payload)
 meta['trials'].append({'tag':tag,'path':str(path),'t':t,'cl':cl,'C_aux':C,'md5':hashlib.md5(path.read_bytes()).hexdigest(),'linear_prediction':(F+t*J@step).tolist()})
(v/'setup_second.json').write_text(json.dumps(meta,indent=2)+'\n');print('S',S,'stepnorm',np.linalg.norm(dz),'dcl',dz[-2],'pred',np.linalg.norm(F+J@step))

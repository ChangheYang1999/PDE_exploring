from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,time,hashlib
import numpy as np
from r2_state_values import R2State
started=time.monotonic()
root=Path('verification/serialized_axis_tails_20261020T1955');root.mkdir(parents=True,exist_ok=True)
roots=[Path('verification/farfield_grid_20261020T1930'),Path('verification/cont25_eps004_20261020T1953')]
rows=[]
for rr in roots:
 manifest=json.loads((rr/'manifest.json').read_text())
 for item in manifest['states']:
  s=R2State(rr/item['snapshot']);rows.append(row:={'label':item['label'],'snapshot':str((rr/item['snapshot']).resolve()),'sha256':s.sha256,'beta':s.beta,'eps_metadata':float(s.meta.get('eps',1.)),'a0_stored':s.center()['F']['value']})
  # Clamped B-splines at1 select the final exact stored coefficients.
  endF=s.rawF.reshape(s.K,s.nb)[:,-1];endG=s.rawG.reshape(s.K,s.nb)[:,-1]
  assert np.array_equal(endF,s.Fs(1.)) and np.array_equal(endG,s.Gs(1.))
  row['exact_endpoint_polynomial_samples']=[]
  for eta in [Fraction(k,4) for k in range(-4,5)]:
   ck=[Fraction(1),eta]
   while len(ck)<s.K:ck.append(2*eta*ck[-1]-ck[-2])
   fsum=sum((Fraction.from_float(float(v))*c for v,c in zip(endF,ck)),Fraction(0))
   gsum=sum((Fraction.from_float(float(v))*c for v,c in zip(endG,ck)),Fraction(0))
   row['exact_endpoint_polynomial_samples'].append({'cos_phi':str(eta),'F_unscaled_exact':str(fsum),'G_unscaled_exact':str(gsum),'F_sign':int(fsum>0)-int(fsum<0),'G_sign':int(gsum>0)-int(gsum<0),'h_over_cos2':float(fsum)*s.L**(1+2/s.bb),'a_over_cos':float(gsum)*s.L**(1+1/s.bb)})
  row['axis']={}
  for side,eta in [('upper',-1),('lower',1)]:
   coeff=eta**np.arange(s.K)
   Pinfty=float(2*s.L**(1+2/s.bb)*np.dot(endF,coeff));Qinfty=float(s.L**(1+1/s.bb)*np.dot(endG,coeff))
   y=np.geomspace(10,1e8,15)*(1 if side=='upper' else -1)
   P=2*abs(y)**(1+2/s.beta)*s.divided(np.zeros_like(y),y,'F')
   Q=abs(y)**(1+1/s.beta)*s.divided(np.zeros_like(y),y,'G')
   row['axis'][side]={'P_basis_limit':Pinfty,'Q_basis_limit':Qinfty,'radii':abs(y).tolist(),'scaled_Theta_xx':P.tolist(),'scaled_Omega_x':Q.tolist()}
  row['sampled_axis_radial_velocity']={}
  for kind in ['transport','self']:
   with np.load(rr/(item['label']+'_'+kind+'.npz')) as z:
    pts=z['points'];w=z['W'];ix=np.flatnonzero(pts[:,0]==0)
    for side,sgn in [('upper',1),('lower',-1)]:
     ii=ix[sgn*pts[ix,1]>0];ratio=w[ii,1]/pts[ii,1];j=ii[np.argmin(ratio)]
     row['sampled_axis_radial_velocity'][kind+'_'+side]={'minimum_b_over_y':float(np.min(ratio)),'radius_at_minimum':float(abs(pts[j,1])),'nonpositive_samples':int(np.sum(ratio<=0)),'samples':len(ii)}
out={'written_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-started,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'states':rows,'scope':'Exact endpoint polynomial signs for exact stored binary coefficients, plus floating-point radial samples. Matching axis and angular limits is built into this basis and is not a PDE validation. Positivity and b/y samples do not prove absence of other equilibria. All states have forced equations distinct from B2.'}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
for row in rows:print(row['label'],'P/Q upper',row['axis']['upper']['P_basis_limit'],row['axis']['upper']['Q_basis_limit'],'P/Q lower',row['axis']['lower']['P_basis_limit'],row['axis']['lower']['Q_basis_limit'],'negative F angular',[v['cos_phi'] for v in row['exact_endpoint_polynomial_samples'] if v['F_sign']<0],flush=True)
print('COMPLETE',out['elapsed_seconds'])

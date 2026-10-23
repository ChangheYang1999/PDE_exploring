import json,sys,argparse
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from candidate_reader import Candidate
from direct_inverse import cartesian_gradient

ap=argparse.ArgumentParser();ap.add_argument('checkpoints',nargs='+');ap.add_argument('--tag',default='');args=ap.parse_args()
out=[]
for name in args.checkpoints:
 c=Candidate(name)
 jets=c.endpoint_t_jets(4)
 drdt=c.meta['L']*2**(-c.meta['p'])
 b_r_modes=jets[1]/drdt
 # Interpolation reproduction at the exact mathematical nodes.
 N,M=c.meta['N'],c.meta['M']
 # Avoid radii which overflow for unusually large map power.
 r=c.meta['L']*(1+c.nodes)/(1-c.nodes)**c.meta['p']
 th=(np.arange(M)+.5)*np.pi/(2*M)
 rr,tt=np.meshgrid(r,th,indexing='ij')
 rho=c.rho(rr*np.cos(tt),rr*np.sin(tt))
 weights=(1+rr*rr/c.meta['L']**2)**((c.meta['gamma']-1)/2)
 recon=np.divide(rho,rr*np.sin(tt)*weights,out=np.broadcast_to(jets[0,0],rho.shape).copy(),where=rr>0)
 err=np.max(np.abs(recon-c.values))
 # Far-field amplitude and a0 are evaluated without PDE enforcement.
 a0=float(jets[0,0]); binf=np.polynomial.chebyshev.chebval(1,c.coefficients)
 baxis=float(np.sum(binf*(-1.)**np.arange(M)))
 K=c.meta['L']**(1-c.meta['gamma'])*baxis
 row={'utc':datetime.now(timezone.utc).isoformat(),'checkpoint':c.meta,'node_reconstruction_max_error':float(err),'a0':a0,'endpoint_nonconstant_b0_modes_max':float(np.max(np.abs(jets[0,1:]))),'b_r_zero_modes':b_r_modes.tolist(),'b_r_zero_max_mode':float(np.max(np.abs(b_r_modes))),'K_for_encoded_exponent':K,'mean_b_infinity':float(binf[0]),'t_jets':jets.tolist(),'regularity_verdict':'The encoded interpolant is not proved C2 unless its first radial jet vanishes exactly; these are floating point estimates, not coefficient enclosures.'}
 out.append(row)
 print(json.dumps({k:v for k,v in row.items() if k not in ['t_jets','b_r_zero_modes']}),flush=True)
 c.save_snapshot(Path('evidence')/(Path(name).stem+'.npz'))
Path('evidence/checkpoint_regularity'+args.tag+'.json').write_text(json.dumps(out,indent=2)+'\n')

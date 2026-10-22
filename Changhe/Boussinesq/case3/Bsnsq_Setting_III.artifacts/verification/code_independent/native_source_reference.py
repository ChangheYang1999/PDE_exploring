"""Independent physical-radius source probes for a future solver interpolation comparison."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib,numpy as np
from r2_state_values import R2State
from adaptive_modal_inverse import R2ModeSource,AdaptiveModalInverse,ModalSettings
root=Path('verification/fixed_velocity_block_20261021T0056');start=time.monotonic();stamp=datetime.now(timezone.utc).isoformat()
s=R2State(root/'archive_schema_manufacture_unknown3.003.npz');source=R2ModeSource(s,kind='native_seed')
radii=np.unique(np.r_[np.geomspace(1e-5,1e8,49),.3,.7,1.3,2.7,4.1,7.3])
angles=np.r_[0.,.137,.719,1.271,1.913,2.711,np.pi,-.137,-.719,-1.913]
sn=np.sin(angles);sn[np.isin(angles,[0.,np.pi])]=0.
pts=np.stack((radii[:,None]*sn,-radii[:,None]*np.cos(angles)),axis=-1).reshape(-1,2)
inv=AdaptiveModalInverse(source,s.K,ModalSettings(1/float(s.meta['beta_seed']),2e-11,2e-11))
v=inv.relative(pts);v[pts[:,0]==0.,0]=0. # exact x-reflection identity
pairs=[inv.radial(r) for r in radii];pr=np.array([p[0] for p in pairs]);dp=np.array([p[1] for p in pairs])
np.savez_compressed(root/'source_velocity_reference.npz',points=pts,radii=radii,angles=angles,velocity_unscaled=v,Psi_over_r=pr,dPsi_dr=dp,source_omega=pts[:,0]*s.divided(*pts.T,'native_seed'),source_beta=float(s.meta['beta_seed']),source_coefficients=s.seed_defectG)
meta=dict(started_utc=stamp,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,points=len(pts),radii=len(radii),source_seed_sha256='483d3af008fa13ece17ad735c59e7c2d9de75e03f7dc615b91eb99aa06ff04c0',source_description='Unscaled cG_ext-cG of original fb30g_eps0 seed, in original beta_basis=3, Nt40 K12 degree5 grade1.5 L1.5 geometry; exact geometry below',geometry={k:s.meta[k] for k in ['Nt','K','deg','grade','L','beta_seed','rmap']},quadrature=inv.evidence,all_inverse_flags_zero=all(q['inner_success'] and q['outer_success'] for q in inv.evidence),limitations='Floating-point whole-plane adaptive quadrature, not rigorous error bounds. These are reference probes for source interpolation, not candidate fields. Source lambda is not applied.',code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(root/'source_velocity_reference.json').write_text(json.dumps(meta,indent=2)+'\n')
print('COMPLETE',meta['elapsed_seconds'],meta['all_inverse_flags_zero'],flush=True)

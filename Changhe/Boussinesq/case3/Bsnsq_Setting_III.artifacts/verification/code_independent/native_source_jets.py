"""Native seed center moments by independent physical-radius quadrature."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,numpy as np,time,hashlib,shutil
from scipy.integrate import quad
from r2_state_values import R2State
from adaptive_modal_inverse import R2ModeSource
root=Path('verification/fixed_velocity_block_20261021T0056');start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'rows':[]}
for tag,name in [('blam12v','fb30g_eps0.npz'),('blam16v','fb30g16_eps0.npz')]:
 path=Path('../numerics/runs')/name;dest=root/name;shutil.copyfile(path,dest)
 with np.load(dest,allow_pickle=False) as z:d={k:z[k].copy() for k in z.files}
 d.update(cG_f=d['cG_ext']-d['cG'],cG_f_effective=np.zeros(0),source_mode=np.array('fixed_velocity_block'),beta_seed=d['beta_basis'],lam=np.array(1.),eps=np.array(1.))
 p=root/(tag+'_jet_schema_manufacture.npz');np.savez_compressed(p,**d);s=R2State(p);mode=R2ModeSource(s,kind='native_seed');beta=float(s.meta['beta_seed'])
 calc={};errors={}
 for n in [2,3,4]:
  # r=(u/(1-u))^beta regularizes the slowest infinite-radius tail.
  def f(u):
   r=(u/(1-u))**beta
   return mode(r)[n-1]*r**(1-n)*beta*u**(beta-1)/(1-u)**(beta+1)
  ee=s.edges[1:-1];rr=s.L*np.sqrt(np.expm1(-2*beta*np.log1p(-ee)));uu=rr**(1/beta);edges=np.r_[0.,uu/(1+uu),1.]
  val=0.;err=0.
  for left,right in zip(edges[:-1],edges[1:]):
   piece=quad(f,left,right,epsabs=2e-13/len(edges),epsrel=2e-12,limit=400,full_output=1)
   if len(piece)!=3:raise RuntimeError(str(piece[3]))
   val+=piece[0];err+=piece[1]
  calc[f'h{n}0']=val/(2*n);errors[f'h{n}0']=err/(2*n)
 calc['c']=float(s.strain('native_seed'));calc['G0']=float(s.SDs(0)[0]);calc['g1p']=float(s.SDs(0)[1]/s.L)
 log=Path('../numerics/runs')/(tag+'.log');lines=log.read_text().splitlines();line=next(v for v in lines if 'Source centre data:' in v);logged=ast.literal_eval(line.split('Source centre data:',1)[1].strip())
 dif={k:calc[k]-logged[k] for k in logged};maximum=max(abs(v) for v in dif.values())
 assert maximum<2e-9,(tag,dif)
 out['rows'].append(dict(tag=tag,source_seed=dest.name,source_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),computed=calc,logged=logged,difference=dif,quadrature_error_estimates=errors,max_difference=maximum))
 print(tag,maximum,calc,flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,limitations='Independent sampled floating-point center moments of two real seed defects. Comparison is against log text, not proof of solver runtime provenance. No candidate or interval certificate.')
(root/'source_jet_results.json').write_text(json.dumps(out,indent=2)+'\n');shutil.copyfile(Path(__file__),root/Path(__file__).name)
print('COMPLETE',out['elapsed_seconds'],flush=True)

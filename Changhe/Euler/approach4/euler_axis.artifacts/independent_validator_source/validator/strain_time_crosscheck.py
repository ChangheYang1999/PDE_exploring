#!/usr/bin/env python3
"""Compare radial q/q_z with event-resolved finite-time characteristic data."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from scipy.interpolate import make_interp_spline
from fast_native_field import FastNativeField
from repaired_native_field import RepairedNativeField
from piecewise_source_transport import source_transport
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parent

def main():
 p=argparse.ArgumentParser();p.add_argument('--level',type=int,choices=[1,2],required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--rtol',type=float,default=2e-10);p.add_argument('--cutoffs',type=float,nargs='+',default=[32.,48.,64.]);p.add_argument('--bands',type=int,nargs='+',default=[1,2,3,4,5,6]);a=p.parse_args()
 if a.output.exists() or not a.output.resolve().is_relative_to(ROOT.parent):raise ValueError('Fresh output in lane required')
 start=time.perf_counter();cpu=time.process_time();directory=ROOT/f'results/strain_l{a.level}_n257_h010_s2.5e-05';progress=json.loads((directory/'progress.json').read_text())
 candidate=ROOT/'external_exports'/('T1_ladder_L1_20261028T232238Z' if a.level==1 else 'T1_ladder_L2_20261028T235434Z')/'coeffs.npz'
 assert sha256(candidate)==progress['candidate_sha256'];base=FastNativeField.load(candidate);field=RepairedNativeField(base,progress['source']);K=progress['config']['K'];points=[];references=[];inputs={}
 for band in a.bands:
  path=directory/f'band_{band:02d}.npz';inputs[str(path.relative_to(ROOT.parent))]=sha256(path)
  with np.load(path,allow_pickle=False) as z:
   mu=z['mu'];h=z['h'];rho=float(z['radius']);k=make_interp_spline(mu,h,k=5).derivative()(mu)
   indices=np.array([0,48,128,208,256]);m=mu[indices];r=rho*np.sqrt(1-m*m);zz=field.z0+rho*m;s=r*r;jet=field.jets(s,zz,2)['phi'];Wr=r*(field.c_l-jet[0,1]);Wz=field.c_l*zz+2*jet[0,0]+2*s*jet[1,0];F=(r*Wr+rho*m*Wz)/rho**2;v=(Wz/rho-m*F)/F;b=(1-2*jet[0,1])/F;q=K*np.exp(h[indices]);qz=q/rho*(-m*b+(1-m*m-m*v)*k[indices])
   for j,index in enumerate(indices):points.append([float(r[j]),float(zz[j])]);references.append(dict(band=band,radius=rho,mu=float(m[j]),angular_index=int(index),q=float(q[j]),q_z=float(qz[j])))
 points=np.asarray(points);sources=[Path(__file__),ROOT/'fast_native_field.py',ROOT/'repaired_native_field.py',ROOT/'src/piecewise_source_transport.py',ROOT.parent/'research/source_time_crosscheck/PROOF.md'];hashes={str(p.relative_to(ROOT.parent)):sha256(p) for p in sources}
 result=dict(created_utc=datetime.now(timezone.utc).isoformat(),candidate_sha256=sha256(candidate),level=a.level,source=progress['source'],source_sha256=hashes,input_sha256=inputs,references=references,phase='initialized',scope='Finite-time event-resolved q and q_z versus radial remapping at selected points; not a global convergence or basin certificate.')
 def save(phase):
  for path,value in hashes.items():
   if sha256(ROOT.parent/path)!=value:raise RuntimeError('Source changed during check')
  result.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu);atomic_json(a.output,result)
 def callback(row,state):
  q=np.asarray(row['q']);qz=np.asarray(row['gradient_q'])[:,1];qr=np.array([r['q'] for r in references]);qzr=np.array([r['q_z'] for r in references]);result.setdefault('cutoff_rows',[]).append(dict(cutoff=row['cutoff'],q=row['q'],q_z=qz.tolist(),terminal_a=row['terminal_a'],terminal_points=row['terminal_points'],q_absolute_difference=(q-qr).tolist(),q_relative_difference=((q-qr)/np.maximum(abs(q),1e-300)).tolist(),qz_absolute_difference=(qz-qzr).tolist(),qz_scaled_difference=((qz-qzr)/np.maximum(np.maximum(abs(qz),abs(qzr)),1e-10)).tolist(),state=state));save('cutoff_complete');print(json.dumps(dict(cutoff=row['cutoff'],wall_seconds=result['wall_seconds'],max_abs_q=float(np.max(abs(q-qr))),max_abs_qz=float(np.max(abs(qz-qzr))),max_terminal_a=float(np.max(np.abs(row['terminal_a']))))),flush=True)
 save('initialized');data=source_transport(field,points,K,cutoffs=a.cutoffs,rtol=a.rtol,atol=a.rtol*.01,max_step=.3,callback=callback);result['transport']=data;result['success']=data['success'];save('complete' if data['success'] else 'transport_failed')
 print(json.dumps(dict(output=str(a.output),phase=result['phase'],wall_seconds=result['wall_seconds'])),flush=True)
if __name__=='__main__':main()

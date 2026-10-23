"""Whole-plane, off-grid residual checks with independent Cartesian differences."""
import argparse,json,time
from pathlib import Path
from datetime import datetime,timezone
from dataclasses import asdict
import numpy as np
from candidate_reader import Candidate
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient

ap=argparse.ArgumentParser();ap.add_argument('checkpoint');ap.add_argument('--tag',default='initial');ap.add_argument('--level',type=int,default=0);ap.add_argument('--all-points',action='store_true');ap.add_argument('--points-file');ap.add_argument('--forced',action='store_true');args=ap.parse_args()
c=Candidate(args.checkpoint,project_center=True)
if args.forced and 'mu' not in c.meta:raise ValueError('Forced evaluation requires encoded mu')
mu=c.meta.get('mu',0.) if args.forced else 0.
forcing_width=c.meta.get('forcing_width',c.meta.get('Lf',c.meta.get('eps',c.meta['L'])))
length=c.meta['L']*2**(-c.meta['p'])
configs=[(16,64,48,2.),(24,128,96,4.),(40,256,144,8.),(64,512,224,4.),(80,1024,288,8.)]
nr,nt,ne,factor=configs[args.level]
conf=Quadrature(nr,nt,ne,factor,length,c.meta['gamma'],16.,c.meta['p'])
inverse=DirectInverse(c.rho,conf)
radii=[1e-9,1e-7,1e-5,.03,.7,4.,100.]
angles=[.013,.413,1.4] if args.all_points else [.413]
points=[(r*np.cos(t),r*np.sin(t)) for r in radii for t in angles]
points += [(0.,v) for v in [length/1000,length/100,length/10,.7,100.]]
if args.all_points:points += [(v,0.) for v in [1e-7,.7,100.]]
if args.points_file: points=[tuple(q) for q in json.loads(Path(args.points_file).read_text())]
out=Path('evidence/residuals');out.mkdir(exist_ok=True)
dest=out/(Path(args.checkpoint).stem+'_'+args.tag+'_q'+str(args.level)+'.json')
result={'started_utc':datetime.now(timezone.utc).isoformat(),'metadata':c.meta,'forced_equation_checked':bool(args.forced),'mu':mu,'forcing_width':forcing_width,'config':asdict(conf),'representation_note':'Nonconstant endpoint modes are projected by subtracting their reconstructed values; the maximum change is in metadata.max_projected_mode. This removes a floating-point first-derivative floor but does not remove higher radial jet defects.','points':[]}
start=time.time()
for x,y in points:
    t0=time.time();u,parts=inverse.velocity(x,y,parts=True)
    rho=float(c.rho(x,y));grads=[];residuals=[]
    source=mu*y/(1+(np.hypot(x,y)/forcing_width)**2)**2
    for h in [.006,.003,.0015]:
        gx,gy=cartesian_gradient(c.rho,x,y,h,0. if x or y else length);gx=float(gx);gy=float(gy)
        tx=(c.meta['cl']*x+u[0])*gx;ty=(c.meta['cl']*y+u[1])*gy
        r=tx+ty-rho;nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(x*gx+y*gy)+abs(u[0]*gx+u[1]*gy)
        grads.append({'relative_step':h,'rho_x':gx,'rho_y':gy})
        residuals.append({'relative_step':h,'R':float(r),'Nf':float(nf),'Nv':float(nv),'abs_R_over_Nf':float(abs(r)/nf) if nf else None,'abs_R_over_Nv':float(abs(r)/nv) if nv else None})
    for row in residuals:
        rf=row['R']-source
        row.update({'Rforced':rf,'abs_Rforced_over_Nf':abs(rf)/row['Nf'] if row['Nf'] else None,'abs_Rforced_over_Nv':abs(rf)/row['Nv'] if row['Nv'] else None})
    item={'x':x,'y':y,'radius':float(np.hypot(x,y)),'source':source,'rho':rho,'U':u.tolist(),'parts':parts,'gradients':grads,'residuals':residuals,'seconds':time.time()-t0}
    result['points'].append(item);result['last_update_utc']=datetime.now(timezone.utc).isoformat();result['elapsed_seconds']=time.time()-start
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'x':x,'y':y,'U':u.tolist(),'R':residuals[-1]['R'],'R_over_Nf':residuals[-1]['abs_R_over_Nf'],'R_over_Nv':residuals[-1]['abs_R_over_Nv'],'point_seconds':time.time()-t0,'elapsed':time.time()-start}),flush=True)
result['finished_utc']=datetime.now(timezone.utc).isoformat();dest.write_text(json.dumps(result,indent=2)+'\n')

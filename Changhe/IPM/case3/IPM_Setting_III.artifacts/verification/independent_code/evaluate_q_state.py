"""Independent checks of published Q/QL finite smooth interpolants."""
import argparse,json,time
from pathlib import Path
from datetime import datetime,timezone
from dataclasses import asdict
import numpy as np
from q_checkpoint_reader import QCheckpoint
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient
from evaluate_smooth_state import summary

def main():
    ap=argparse.ArgumentParser();ap.add_argument('state');ap.add_argument('--level',type=int,default=0);ap.add_argument('--tag');ap.add_argument('--far-axis',action='store_true');ap.add_argument('--resume',action='store_true');ap.add_argument('--points-file');ap.add_argument('--log-tail',action='store_true');args=ap.parse_args()
    if args.log_tail:
        from log_radius_inverse import LogRadiusQCheckpoint,LogTailInverse
        reader=LogRadiusQCheckpoint;inverse=LogTailInverse
    else:
        reader=QCheckpoint;inverse=DirectInverse
    c=reader(args.state);tag=args.tag or Path(args.state).stem
    dest=Path('evidence/q_evaluations')/tag;dest.mkdir(parents=True,exist_ok=True)
    c.save_snapshot(dest/'snapshot.npz')
    configs=[(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)]
    nr,nt,ne,of=configs[args.level];length=c.L*2**(-c.kappa)
    q=Quadrature(nr,nt,ne,of,length,c.p,16*c.L,c.kappa);inv=inverse(c.rho,q)
    radii=np.array([1e-6,1e-3,.029,.31,1.13,4.7,80.,1e4,1e8])*c.L
    angles=[.003,.229,.791,1.491]
    points=[(float(r*np.cos(t)),float(r*np.sin(t))) for r in radii for t in angles]
    points +=[(0.,float(r)) for r in radii]
    points +=[(0.,c.Lf*v) for v in (.17,.61,1.71)]
    points +=[(float(r),0.) for r in radii[::2]]+[(0.,0.)]
    if args.far_axis:
        points=[(0.,10.**k*c.L) for k in (2,4,6,9,12,15,18)]
    if args.points_file:
        points=[tuple(map(float,row)) for row in json.loads(Path(args.points_file).read_text())]
    ct=c.center_and_tail();start=time.time()
    result={'started_utc':datetime.now(timezone.utc).isoformat(),'metadata':c.meta,'quadrature':asdict(q),'log_radius_exterior':args.log_tail,'center_and_tail':ct,'node_B_reconstruction_error':c.node_reconstruction_error(),'scope':'Independent scalar coefficient reader, safeguarded radial Newton, Cartesian FD8 and full-plane cancellation kernel. Producer inverse, differentiation and velocity matrices not used. Exact x-axis ratios geometrically excluded, all near-axis data retained. Pointwise sampled results only. The actual map tail exponent governs the inverse and far-field checks.','points':[]}
    output=dest/(('axis_' if args.far_axis else '')+'q'+str(args.level)+'.json')
    if args.resume and output.exists():
        previous=json.loads(output.read_text())
        assert previous['metadata']['sha256']==c.meta['sha256']
        assert previous['quadrature']==result['quadrature']
        assert previous.get('log_radius_exterior',False)==args.log_tail
        saved=previous['points']
        assert [(v['x'],v['y']) for v in saved]==points[:len(saved)]
        result['points']=saved
        result['resumed_previous_start_utc']=previous['started_utc']
        result['resumed_point_count']=len(saved)
        result['reader_repair']='Zero radius handled exactly before Newton; off-origin formula unchanged.'
    for i,(x,y) in enumerate(points):
        if i<len(result['points']):continue
        tick=time.time();rho=float(c.rho(x,y));u,parts=inv.velocity(x,y,parts=True)
        r=float(np.hypot(x,y));den=float(np.hypot(c.Lf,r));source=c.mu*c.Lf*(c.Lf/den)**3*(y/den)
        residuals=[]
        for step in (.003,.0015,.00075):
            gx,gy=cartesian_gradient(c.rho,x,y,step,length if x==y==0. else 0.)
            gx=float(gx);gy=float(gy);tx=(c.cl*x+u[0])*gx;ty=(c.cl*y+u[1])*gy
            R=tx+ty-rho;Rf=R-source;nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(x*gx+y*gy)+abs(u[0]*gx+u[1]*gy)
            row={'relative_step':step,'rho_x':gx,'rho_y':gy,'R':float(R),'Rforced':float(Rf),'abs_R':float(abs(R)),'abs_Rforced':float(abs(Rf)),'Nf':float(nf),'Nv':float(nv)}
            for nm,val in [('R',R),('Rforced',Rf)]:
                for dm,den in [('Nf',nf),('Nv',nv)]:row[nm+'_'+dm]=float(abs(val)/den) if den else None
            residuals.append(row)
        item={'x':x,'y':y,'radius':r,'rho':rho,'U':u.tolist(),'inverse_parts':parts,'source':source,'residuals':residuals,'parity':{'even_x_error':float(c.rho(-x,y)-rho),'odd_y_error':float(c.rho(x,-y)+rho)},'seconds':time.time()-tick}
        if x==0 and y>0:item.update(axis_scaled_rho_actual=rho/y**c.p,axis_scaled_rho_requested=rho/y**(1/c.cl),axis_dilation_exponent=y*residuals[-1]['rho_y']/rho if rho else None,scaled_U2=float(u[1]/y**c.p))
        result['points'].append(item);result['last_update_utc']=datetime.now(timezone.utc).isoformat();result['elapsed_seconds']=time.time()-start
        output.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({'utc':result['last_update_utc'],'point':i,'total':len(points),'radius':r,'R_Nf':residuals[-1]['R_Nf'],'Rforced_Nf':residuals[-1]['Rforced_Nf'],'seconds':time.time()-tick}),flush=True)
    result['summary']=summary(result['points']);result['finished_utc']=datetime.now(timezone.utc).isoformat();output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'center_and_tail':ct,'summary':result['summary']},indent=2),flush=True)
if __name__=='__main__':main()

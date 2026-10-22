"""P202 native inverse refinement and analytic scalar-map parameter sensitivity."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import os,time,json,hashlib,traceback
import numpy as np
from scipy.integrate import quad_vec
from r2_state_values import R2State
from moment_modal_inverse import exact_moment2,R2DifferentiableModes,MomentModalInverse
from adaptive_modal_inverse import ModalSettings,AdaptiveModalInverse
import adaptive_modal_inverse as original_module
from sensitive_modal_flow import C2ModalFlow,reconstruct_sensitivity
from smooth_modal_flow import reconstruct
from cartesian_inverse import CartesianInverse,InverseSettings

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/202_moment_inverse_and_flow_sensitivity/verification'
PREV=ROOT/'research/200_projected_characteristic_response/verification'
SOURCE=ROOT/'research/197_vertex_mapscale_audit/verification/certificates/archives/mbb_b3.0952_lambda0.989973.npz'

def now():return datetime.now(timezone.utc).isoformat()
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(path,val):
    temp=path.with_suffix('.tmp');temp.write_text(json.dumps(val,indent=2)+'\n');temp.replace(path)

def main():
    start=time.monotonic();s=R2State(SOURCE);sp=R2State(PREV/'projected_self.npz');sd=R2State(PREV/'direction_self.npz')
    lam=float(s.meta['lam']);a0=float(s.center()['F']['value']);mf=R2DifferentiableModes(s,native=True)
    mb=R2DifferentiableModes(sp);md=R2DifferentiableModes(sd);N=max(mf.count,mb.count)
    def pad(v):return np.pad(v,(0,N-len(v)))
    def base(r):return pad(mb(r))+lam*pad(mf(r))
    def direction(r):return pad(md(r))+pad(mf(r))
    def base_derivative(r):return pad(mb.derivative(r))+lam*pad(mf.derivative(r))
    def direction_derivative(r):return pad(md.derivative(r))+pad(mf.derivative(r))
    Mbase=exact_moment2(sp)+Fraction(lam)*exact_moment2(s,native=True)
    Mdir=exact_moment2(sd)+exact_moment2(s,native=True)
    knots=[]
    for field in [s,s.seed_field]:
        t=field.edges[1:-1];knots.extend(field.L*np.sqrt(np.expm1(-2*field.bb*np.log1p(-t))))
    knots=np.unique(knots);decay=min(1/s.bb,1/s.seed_field.bb)
    ib=MomentModalInverse(base,N,ModalSettings(decay,2e-13,2e-11),Mbase,knots)
    idr=MomentModalInverse(direction,N,ModalSettings(decay,2e-13,2e-11),Mdir,knots)
    out={'started_utc':now(),'pid':os.getpid(),'priority':os.getpriority(os.PRIO_PROCESS,0),'status':'RUNNING',
        'source_sha256':s.sha256,'base_moment2_exact':str(Mbase),'direction_moment2_exact':str(Mdir),
        'base_moment2_float':float(Mbase),'direction_moment2_float':float(Mdir),
        'a0':a0,'NUM_metadata_a0':float(s.meta['a0']),'native_source_basis':s.meta['beta_seed'],
        'code_hashes':{name:digest(ROOT/'code_independent'/name) for name in
            ['native_moment_sensitivity.py','moment_modal_inverse.py','sensitive_modal_flow.py','r2_state_values.py']}}
    def save():out['elapsed_seconds']=time.monotonic()-start;out['updated_utc']=now();write(OUT/'native_results.json',out)
    # Re-run selected original quadratures with their full status messages retained.
    captured=[]
    def logged_quad(*args,**kwargs):
        ans=quad_vec(*args,**kwargs);info=ans[2]
        captured.append({'success':bool(info.success),'status':int(info.status),'message':str(info.message),
            'neval':int(info.neval),'error_estimate':float(ans[1])})
        return ans
    original_module.quad_vec=logged_quad
    old=AdaptiveModalInverse(direction,N,ModalSettings(decay,2e-13,2e-11))
    out['original_failure_replays']=[]
    for r in [1e-5,.0003,.003,.03,.1,.3,3.]:
        old.settings.epsabs=2e-12*min(r,.1);idr.settings.epsabs=old.settings.epsabs
        before=len(captured);po,do=old.radial(r);pn,dn=idr.radial(r)
        out['original_failure_replays'].append({'r':r,'original_status':captured[before:],
            'moment_status':idr.evidence[-1],'pr_difference':float(max(abs(po-pn))),
            'dp_difference':float(max(abs(do-dn)))})
        save();print(now(),'pilot',r,'old statuses',[z['status'] for z in captured[before:]],
            'stable',idr.evidence[-1]['inner_success'],idr.evidence[-1]['outer_success'],flush=True)
    original_module.quad_vec=quad_vec
    with np.load(PREV/'native_inverse_nodes.npz',allow_pickle=False) as z:
        radii=z['radii'].copy();old_pb=z['pr_base'].copy();old_db=z['dp_base'].copy();old_pd=z['pr_dir'].copy();old_dd=z['dp_dir'].copy()
    vals=[[],[],[],[],[],[],[],[]]
    out.update(stage='moment_inverse_nodes',fine_nodes=len(radii),node_evidence=[])
    for i,r in enumerate(radii):
        for inv in [ib,idr]:inv.settings.epsabs=2e-12*min(r,.1)
        p,d=ib.radial(r);q,e=idr.radial(r)
        for v,a in zip(vals,[p,d,base(r),base_derivative(r),q,e,direction(r),direction_derivative(r)]):v.append(a)
        out['node_evidence'].append({'index':i,'base':ib.evidence[-1],'direction':idr.evidence[-1]})
        if i%20==0 or i+1==len(radii):
            out['nodes_completed']=i+1;save();np.savez_compressed(OUT/'inverse_nodes.npz',radii=radii,
                **dict(zip(['pr_base','dp_base','H_base','Hp_base','pr_dir','dp_dir','H_dir','Hp_dir'],[np.asarray(v) for v in vals])))
            print(now(),'nodes',i+1,'/',len(radii),'elapsed',out['elapsed_seconds'],flush=True)
    pb,db,hb,hpb,pd,dd,hd,hpd=[np.asarray(v) for v in vals]
    out['node_comparison']={label:float(np.max(abs(a-b))) for label,a,b in
        [('pr_base',pb,old_pb),('dp_base',db,old_db),('pr_direction',pd,old_pd),('dp_direction',dd,old_dd)]}
    def flow(h=0.,coarse=False):
        sl=slice(None,None,2 if coarse else 1)
        return C2ModalFlow(s.beta,radii[sl],(pb+h*pd)[sl],(db+h*dd)[sl],(hb+h*hd)[sl],(hpb+h*hpd)[sl])
    fine=flow();coarse=flow(coarse=True);vf=C2ModalFlow(0.,radii,pd,dd,hd,hpd)
    vc=C2ModalFlow(0.,radii[::2],pd[::2],dd[::2],hd[::2],hpd[::2])
    points=np.array([[.2,.1],[.8,.4],[1.,1.],[.3,3.],[3.,1.]])
    out.update(stage='interpolation_checks',interpolation_checks=[]);save()
    for X in np.r_[points,[[r*np.sin(ph),-r*np.cos(ph)] for r in [.0004,.004,.04,.4,4.,20.] for ph in [.37,1.61,2.43]]]:
        wf,dwf,of=fine.values(X);wc,dwc,oc=coarse.values(X);wd,_,od=vf.values(X)
        eb=s.beta*X+ib.relative(X[None])[0];ed=idr.relative(X[None])[0]
        theta=np.arctan2(X[0],-X[1]);r=np.hypot(*X);sn=np.sin(np.arange(1,N+1)*theta)
        out['interpolation_checks'].append({'point':X.tolist(),'base_velocity_error':float(max(abs(wf-eb))),
            'direction_velocity_error':float(max(abs(wd-ed))),'DW_resolution_difference':float(np.max(abs(dwf-dwc))),
            'source_error':float(abs(of-base(r)@sn)),'source_direction_error':float(abs(od-direction(r)@sn)),
            'divergence_error':float(abs(np.trace(dwf)-2*s.beta))})
    def omega_base(x,y):return sp.omega(x,y)+lam*np.asarray(x)*s.divided(x,y,'native_seed')
    def omega_dir(x,y):return sd.omega(x,y)+np.asarray(x)*s.divided(x,y,'native_seed')
    out['Cartesian_inverse']=[]
    for label,fn,inv in [('base',omega_base,ib),('direction',omega_dir,idr)]:
        exact=inv.relative(points[[0,2,4]])
        for order in [24,36]:
            setting=InverseSettings(radius=12.,core_radial_order=order,core_angular_order=3*order,
                exterior_radial_order=4*order,exterior_angular_order=4*order,decay_power=decay)
            value=CartesianInverse(fn,setting).relative(points[[0,2,4]])
            out['Cartesian_inverse'].append({'field':label,'order':order,'points':points[[0,2,4]].tolist(),
                'absolute_error':abs(value-exact).tolist(),'settings':setting.__dict__})
            save();print(now(),'Cartesian',label,order,'maxerror',np.max(abs(value-exact)),flush=True)
    out.update(stage='sensitivities',sensitivity=[],parameter_differences=[]);save()
    for X in points:
        for cutoff,grid,tol in [(.003,'fine',1e-10),(.001,'fine',1e-10),(.0003,'fine',1e-10),
            (.001,'coarse',1e-10),(.001,'fine',1e-12)]:
            row=reconstruct_sensitivity(fine if grid=='fine' else coarse,vf if grid=='fine' else vc,X,
                s.beta,a0,cutoff=cutoff,rtol=tol,atol=tol*.01)
            row.update(grid=grid);out['sensitivity'].append(row);save()
        for step in [2e-4,1e-4]:
            rows=[reconstruct(flow(j*step),X,s.beta,a0,cutoff=.001,rtol=1e-12,atol=1e-14,compatible_seed=True) for j in [-2,-1,1,2]]
            row={'point':X.tolist(),'step':step,'evaluations':rows}
            if all(v['status']=='COMPLETE' for v in rows):
                values=[np.r_[v['Theta'],v['gradient'],v['Omega']] for v in rows]
                d=(values[0]-8*values[1]+8*values[2]-values[3])/(12*step)
                row.update(status='COMPLETE',derivative=d.tolist())
            else:row['status']='FAILED'
            out['parameter_differences'].append(row);save()
        print(now(),'sensitivity point',X.tolist(),'elapsed',out['elapsed_seconds'],flush=True)
    out.update(status='COMPLETE',ended_utc=now(),stage='finished',
        scope='Finite-cutoff prescribed-velocity scalar response, independent inverse and ODE discretization. No fitted coefficient Jacobian, root, enclosure, infinite-cutoff theorem, or B2 endpoint.')
    save();print(now(),'COMPLETE elapsed',out['elapsed_seconds'],flush=True)

if __name__=='__main__':
    try:main()
    except Exception:
        (OUT/'failure.txt').write_text(now()+'\n'+traceback.format_exc());raise

"""Reproducible independent probe of coefficient data, never a YES certificate.

No fitting code imports. This script stores its source snapshot, individual
samples, denominators, independent full-plane velocities and convergence.
Run one instance at a time with single-threaded numerical libraries.
"""
import argparse,json,time,hashlib,platform
import scipy
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.optimize import brentq
from profile_data import CoefficientProfile,snapshot
from inverse import Quadrature,PanelQuadrature,velocity_panels,center_strain
from residuals import cartesian,divided,summary,cartesian_from_factors,differentiate
from duffy_inverse import DuffyQuadrature,velocity_duffy


def serialize(fields):return {k:np.asarray(v).tolist() for k,v in fields.items()}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('source');parser.add_argument('tag')
    parser.add_argument('--orders',default='64,128,192')
    parser.add_argument('--method',choices=['polar','duffy'],default='duffy')
    parser.add_argument('--elliptic',action='store_true')
    args=parser.parse_args()
    if any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-' for c in args.tag):
        raise ValueError('tag must be a simple file label')
    start=time.monotonic();stamp=lambda:datetime.now(timezone.utc).isoformat()
    target=Path('data/control_snapshots')/(args.tag+'.npz')
    if not target.exists():snapshot(args.source,target)
    p=CoefficientProfile(target);orders=[int(v) for v in args.orders.split(',')]
    if p.tail_power<=0:raise ValueError('This quadrature requires a positive decay exponent')
    record=dict(timestamp_start=stamp(),source=str(target),source_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                metadata=p.metadata(),inverse_method=args.method,
                software=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
                source_code_sha256={str(q):hashlib.sha256(q.read_bytes()).hexdigest() for q in Path(__file__).resolve().parent.glob('*.py')},
                derivative_method='eighth-order centered finite differences; separate raw and parity-factored forms',
                limitations=['Exploratory probe, not full candidate verification','No interval error certificate',
                             'Inverse scale changes do not replace independent fit-domain studies'])
    output=Path('runs')/(args.tag+'_audit.json')
    def checkpoint():
        record['last_update']=stamp();record['elapsed_seconds']=time.monotonic()-start
        output.write_text(json.dumps(record,indent=2,allow_nan=True)+'\n')
    # Locate the first sign change on an independent logarithmic axis grid.
    # The grid cannot exclude missed oscillatory zeros, so retain its samples.
    def make_config(order,scale):
        return (DuffyQuadrature(order,p.tail_power,scale) if args.method=='duffy' else
                PanelQuadrature(order,p.tail_power,scale,min(1,p.length/4)))
    get_velocity=velocity_duffy if args.method=='duffy' else velocity_panels
    cheap=make_config(min(orders),p.length)
    scan_x=np.geomspace(1e-3*min(1,p.length),100*p.length,45)
    scan_p=np.column_stack([scan_x,np.zeros(len(scan_x))])
    scan_u=get_velocity(p.omega,scan_p,cheap)
    scan_w=p.beta*scan_x+scan_u[:,0]
    crossing=np.flatnonzero((scan_w[:-1]<0)&(scan_w[1:]>=0))
    bracket=[float(scan_x[crossing[0]]),float(scan_x[crossing[0]+1])] if len(crossing) else None
    record['axis_scan']=dict(x=scan_x.tolist(),w=scan_w.tolist(),bracket=bracket,
                            caveat='First sampled negative-to-positive crossing; not certified first zero')
    L0=sum(bracket)/2 if bracket else max(1,p.length)
    if bracket:
        root_cfg=make_config(max(orders),p.length)
        root_w=lambda x:float(p.beta*x+get_velocity(p.omega,[[x,0]],root_cfg)[0,0])
        try:
            L0=brentq(root_w,*bracket,xtol=1e-9,rtol=1e-10,maxiter=40)
            record['axis_scan']['refined_reference_root']=L0
        except ValueError:
            record['axis_scan']['reference_root_error']='Finest inverse did not retain sampled bracket'
    # Between-node points chosen independently, including exact axes.
    rng=np.random.default_rng(20261020)
    regions={
        'origin_axes':np.array([[0,0],[1e-4*L0,0],[0,1e-4*L0],[.01*L0,0],[0,.03*L0],[.04*L0,.003*L0]]),
        'near_stagnation':np.array([[q*L0,y*L0] for q,y in [(1,0),(.98,.001),(1.02,.003),(1,.03)]]),
        'bulk':L0*np.exp(rng.uniform(np.log(.05),np.log(3),(8,2))),
        'far':np.array([[r*p.length*np.cos(phi),r*p.length*np.sin(phi)]
                       for r in [5,20,80] for phi in [.13,.6,1.25]])}
    points=np.concatenate(list(regions.values()));offset=0;region_ids={}
    for key,v in regions.items():region_ids[key]=list(range(offset,offset+len(v)));offset+=len(v)
    dp=np.array([[0,0],[.002*L0,0],[.03*L0,0],[0,.03*L0],[L0,0],[0,L0],[.3*L0,.4*L0]])
    record.update(points=points.tolist(),regions=region_ids,divided_points=dp.tolist(),rows=[])
    checkpoint()
    for order in orders:
        cfg=make_config(order,p.length)
        u=lambda x:get_velocity(p.omega,x,cfg)
        cq=min(512,max(128,order*2)) if args.method=='duffy' else order*20
        c=center_strain(p.omega,Quadrature(cq,cq,p.tail_power,p.length))
        raw=cartesian(p.theta,p.omega,p.beta,points,u=u,elliptic=False)
        # Share the same already computed U, keeping derivative generators independent.
        fact=cartesian_from_factors(p.a,p.G,p.beta,points,lambda x:raw['U'])
        div=divided(p.theta,p.omega,p.beta,dp,u=u)
        row=dict(order=order,radial_scale=p.length,center_strain=float(c),
                 center_defect=float(c-(2*p.beta+2)),
                 jet_defect=float((2*p.beta+1)*p.G([[0,0]])[0]-2*p.a([[0,0]])[0]),
                 fields=serialize(raw),factored_fields=serialize(fact),divided_fields=serialize(div),
                 summary=summary(raw),factored_summary=summary(fact),divided_summary=summary(div),
                 regions={key:summary({name:values[indices] for name,values in fact.items()}) for key,indices in region_ids.items()})
        if bracket:
            w=lambda x:float(p.beta*x+u([[x,0]])[0,0])
            try:
                root=brentq(w,*bracket,xtol=1e-9,rtol=1e-10,maxiter=40)
                derivative=differentiate(u,[[root,0]],0,relative_step=.001)[0,0]+p.beta
                row['stagnation']=dict(x=root,mu=float(derivative),mu_defect=float(derivative-(p.beta+2)),
                                       f=float(p.theta([[root,.0001]])[0]/.0001),
                                       root_residual=w(root),meaning='Root in recorded sampled bracket')
            except ValueError:row['stagnation']={'error':'Bracket not retained at this quadrature order'}
        if args.elliptic:
            ep=L0*np.array([[.1,.1],[.8,.03],[1.2,.5]])
            ef=cartesian(p.theta,p.omega,p.beta,ep,u=u,elliptic=True)
            row['elliptic']=dict(points=ep.tolist(),fields=serialize(ef),summary=summary(ef),
                                 caveat='Curl and divergence of independent velocity, not a supplied-stream-function Laplacian')
        record['rows'].append(row);checkpoint()
        print(json.dumps(dict(order=order,center_defect=row['center_defect'],
                              max_R_omega=row['summary']['R_omega']['max_abs'],
                              max_R_theta=row['summary']['R_theta']['max_abs'],
                              max_div_omega=row['divided_summary']['R_omega_div']['max_abs'],
                              max_div_theta=row['divided_summary']['R_theta_div']['max_abs'],
                              stagnation=row.get('stagnation'),elapsed_seconds=time.monotonic()-start)),flush=True)
    # Change the radial compactification scale independently at fixed resolution.
    checks=points[[5,9,14,len(points)-2]]
    record['inverse_scale_tests']=[]
    for scale in [.5*p.length,p.length,2*p.length]:
        cfg=make_config(max(orders),scale)
        uv=get_velocity(p.omega,checks,cfg)
        record['inverse_scale_tests'].append(dict(scale=scale,points=checks.tolist(),U=uv.tolist()))
        checkpoint()
    # Tail amplitudes: distinguish the declared power from vanishing leading coefficients.
    phi=np.linspace(0,np.pi/2,129)
    def leading(c,sigma):return p.leading_amplitude(c,sigma,phi)
    record['far_coefficients']=dict(phi=phi.tolist(),
        theta=(np.cos(phi)**2*np.sin(phi)*leading(p.ca,p.sigma_a)).tolist(),
        omega=(np.cos(phi)*np.sin(phi)*leading(p.cg,p.sigma_g)).tolist(),
        expected_temperature_power=1-2/p.beta,expected_vorticity_power=-1/p.beta)
    record['timestamp_end']=stamp();record['verdict']='OPEN as a candidate audit; consult measured defects. No endpoint certified.'
    checkpoint()

if __name__=='__main__':main()

"""Reproducible independent validation, with measured numerical intervals."""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import time
import numpy as np
from core import (differentiate,residuals,stats,summarize,holdout_regions,cylindrical_residual,
                  affine_fit,angular_diagnostics,symmetry_diagnostics,axis_diagnostics,
                  exponent_sensitivity,directional_dependence,uniform_shell,to_cylindrical,sha256,vector_group_average,volume_angular_spectra)
from models import Affine,Seed,Polynomial

ROOT=Path(os.environ.get('E1_VER_ROOT',str(Path(__file__).resolve().parents[1]))).resolve()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def atomic_json(path,data):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_suffix(path.suffix+f'.{os.getpid()}.tmp')
    temp.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
    os.replace(temp,path)


class Interval:
    """An active interval encloses numerical work only; idle/setup is excluded."""
    def __init__(self,experiment,configuration,input_hash=None):
        self.experiment=experiment; self.configuration=configuration; self.input_hash=input_hash
    def __enter__(self):
        self.start=utc(); self.clock=time.monotonic()
        self.id=f'{self.experiment}-{os.getpid()}-{time.time_ns()}'
        self.append(dict(event='start',interval_id=self.id,experiment_id=self.experiment,start_utc=self.start,
                         configuration_sha256=hashlib.sha256(json.dumps(self.configuration,sort_keys=True).encode()).hexdigest(),
                         checkpoint_sha256=self.input_hash,machine=os.uname().nodename,precision='FP64',
                         workers=1,device='CPU',nice=os.getpriority(os.PRIO_PROCESS,0),pid=os.getpid(),
                         code_sha256={p.name:sha256(p) for p in (Path(__file__).resolve().parent).glob('*.py')}))
        return self
    def __exit__(self,typ,err,tb):
        self.end=utc(); self.seconds=time.monotonic()-self.clock
        self.append(dict(event='stop',interval_id=self.id,experiment_id=self.experiment,start_utc=self.start,
                         end_utc=self.end,active_seconds=self.seconds,completed=(typ is None),error=str(err) if err else None))
        return False
    def append(self,record):
        with (ROOT/'VALIDATION_LEDGER.jsonl').open('a') as stream:
            stream.write(json.dumps(record,allow_nan=False)+'\n');stream.flush();os.fsync(stream.fileno())


def tail_check(model,rng,n=96,order=6):
    directions=rng.normal(size=(n,3));directions/=np.linalg.norm(directions,axis=1)[:,None]
    d=1-1/model.c_l
    results=[]
    for R in [8.,16.,32.,64.,128.,256.,512.,1024.,2048.,4096.]:
        points=R*directions
        f,J,H=differentiate(model,points,step=.002,order=order)
        r=residuals(points,f,J,H,model.c_l,model.C)
        num=stats(r['momentum'])['rms']
        denom=sum(stats(t)['rms'] for t in r['momentum_terms'])
        nonlinear_denom=stats(r['momentum_terms'][3])['rms']+stats(r['grad_P'])['rms']
        results.append(dict(radius=R,velocity_rms=stats(r['U'])['rms'],vorticity_rms=stats(r['Omega'])['rms'],
                            gradient_rms=stats(r['J'])['rms'],momentum_rms=num,
                            linear_term_relative=(num/denom if denom else None),
                            nonlinear_term_relative=(num/nonlinear_denom if nonlinear_denom else None),
                            scaled_velocity_rms=stats(r['U']/R**d)['rms'],
                            scaled_vorticity_rms=stats(r['Omega']/R**(d-1))['rms'],
                            momentum_scaled_by_R_2d_minus_1=num/R**(2*d-1),
                            pressure_poisson_rms=stats(r['pressure_poisson'])['rms']))
    radii=np.array([r['radius'] for r in results])
    slopes={}
    for key in ['velocity_rms','vorticity_rms','gradient_rms','momentum_rms']:
        vals=np.array([r[key] for r in results])
        slopes[key]=np.diff(np.log(vals)).tolist() if np.all(vals>0) else None
        if slopes[key] is not None:
            slopes[key]=(np.diff(np.log(vals))/np.diff(np.log(radii))).tolist()
    return dict(expected_velocity_degree=d,expected_vorticity_degree=d-1,nonlinear_residual_degree=2*d-1,
                points_per_sphere=n,spheres=results,successive_log_slopes=slopes,
                scope='directional sampled sphere RMS; not a volume norm or an infinite-domain guarantee')


def residual_spectra(model,ntheta=128):
    theta=np.arange(ntheta)*2*math.pi/ntheta
    rings=[]
    for radius in [.5,1.,2.,4.]:
        for z in [-.7,.2]:
            x=np.column_stack([radius*np.cos(theta),radius*np.sin(theta),np.full(ntheta,z)])
            f,J,H=differentiate(model,x,step=.002,order=6,hessian=False)
            r=residuals(x,f,J,H,model.c_l,model.C)
            rc=to_cylindrical(r['momentum'],theta)
            coeff=np.fft.fft(rc,axis=0)/ntheta;energy=np.sum(abs(coeff)**2,axis=1)
            rings.append(dict(r=radius,z=z,total_residual_energy=float(energy.sum()),
                              modes={str(k):float(energy[k]+(energy[-k] if k else 0)) for k in range(17)},
                              top_quarter_frequency_energy=float(energy[ntheta//4:3*ntheta//4+1].sum())))
    return dict(ntheta=ntheta,rings=rings,scope='full residual evaluated before Fourier analysis; no Galerkin truncation')


def geometry(model,rng):
    from scipy.optimize import root,minimize
    def v(x):
        val=model(np.asarray(x)[None,:])[0,:3]+model.c_l*np.asarray(x)
        val[2]+=model.C
        return val
    points=np.concatenate([np.zeros((1,3)),uniform_shell(rng,24,0,2),np.array([[0,0,z] for z in [-4,-2,-1,1,2,4]])])
    zeros=[]
    for p in points:
        sol=root(v,p)
        x=sol.x
        if np.all(np.isfinite(x)) and np.linalg.norm(v(x))<1e-8 and np.linalg.norm(x)<100:
            if not any(np.linalg.norm(x-q)<1e-5 for q in zeros):
                zeros.append(x)
    records=[]
    for x in zeros:
        f,J,H=differentiate(model,x[None,:],step=.001,order=6)
        r=residuals(x[None,:],f,J,H,model.c_l,model.C)
        JV=J[0,:3]+model.c_l*np.eye(3); S=(JV+JV.T)/2
        ev,evec=np.linalg.eigh(S)
        outgoing=[]
        for h in [1e-4,1e-3,1e-2,.1]:
            direction=evec[:,0]; vv=v(x+h*direction)
            outgoing.append(dict(radius=h,quadratic_ratio=float(vv@direction/h)))
        eigenvalues=np.linalg.eigvals(JV)
        singular_values=np.linalg.svd(JV,compute_uv=False)
        _,jhalf,_=differentiate(model,x[None,:],step=.0005,order=6,hessian=False)
        jacobian_refinement=float(np.linalg.norm(jhalf[0,:3]-J[0,:3],ord=2))
        local_tests=[]
        for radius in [.001,.01,.1]:
            converged=[];distinct=[]
            for direction in np.concatenate([np.eye(3),-np.eye(3)]):
                probe=root(v,x+radius*direction)
                if np.all(np.isfinite(probe.x)) and np.linalg.norm(v(probe.x))<1e-8:
                    separation=float(np.linalg.norm(probe.x-x));converged.append(separation)
                    if separation>1e-5:distinct.append(probe.x.tolist())
            local_tests.append(dict(start_radius=radius,starts=6,converged=len(converged),
                max_distance_from_original_root=max(converged) if converged else None,other_roots=distinct))
        qx=x*np.array([-1.,-1.,1.])
        records.append(dict(point=x.tolist(),transport_norm=float(np.linalg.norm(v(x))),Omega=r['Omega'][0].tolist(),
                            grad_V=JV.tolist(),symmetric_eigenvalues=ev.tolist(),
                            symmetric_eigenvalues_definition='eigenvalues of sym(grad V), retained legacy key',
                            strain_U_eigenvalues=(ev-model.c_l).tolist(),
                            transport_eigenvalues=[dict(real=float(e.real),imag=float(e.imag)) for e in eigenvalues],
                            transport_singular_values=singular_values.tolist(),transport_determinant=float(np.linalg.det(JV)),
                            jacobian_step_halving_operator_difference=jacobian_refinement,
                            sampled_jacobian_nonsingular=bool(singular_values[-1]>100*jacobian_refinement and singular_values[-1]>1e-8),
                            Q_partner_distance_to_located_set=min(float(np.linalg.norm(qx-z)) for z in zeros),
                            nearby_start_root_tests=local_tests,
                            local_topology_scope='Finite differences and finite root probes support numerical isolation only. No interval inverse theorem or complete zero-set certificate.',
                            quadratic_probe=outgoing,vorticity_residual=r['vorticity'][0].tolist()))
    # Refine sampled vorticity peaks. This is an approximate local maximum only.
    samples=uniform_shell(rng,192,0,4)
    def omega_at(points):
        f,J,H=differentiate(model,points,step=.0015,order=6,hessian=False)
        from core import curl
        return curl(J[:,:3])
    oo=omega_at(samples); mag=np.sum(oo**2,axis=1)
    peaks=[]
    for index in np.argsort(mag)[-2:]:
        def objective(x):
            om=omega_at(np.asarray(x)[None,:])[0]
            return -float(om@om)
        sol=minimize(objective,samples[index],method='Nelder-Mead',options=dict(maxiter=180,xatol=2e-6,fatol=1e-10))
        x=sol.x
        if np.linalg.norm(x)>100:
            continue
        f,J,H=differentiate(model,x[None,:],step=.0015,order=6)
        r=residuals(x[None,:],f,J,H,model.c_l,model.C)
        om=r['Omega'][0];den=float(om@om)
        strain=float(om@J[0,:3]@om)
        peaks.append(dict(point=x.tolist(),optimizer_success=bool(sol.success),vorticity_squared=den,
                          stretching=strain,stretching_ratio=(strain/den if den else None),
                          grad_vorticity_squared=(2*r['J_Omega'][0].T@om).tolist(),
                          vorticity_residual=r['vorticity'][0].tolist(),scope='numerically refined local extremum; no global maximum certificate'))
    return dict(stagnation_points=records,initial_guesses=len(points),peak_vorticity=peaks,
                scope='finite multistart numerical search; unlocated zeros or peaks remain possible')


def assess(result):
    reasons=[]
    regions=result['regions']
    worst=max(regions,key=lambda k:regions[k]['momentum']['relative_rms'] or 0)
    if any(r['momentum']['relative_rms'] is None for r in regions.values()):
        reasons.append('zero momentum normalization denominator on at least one region')
    if (regions[worst]['momentum']['relative_rms'] or 0)>1e-3:
        reasons.append('independent regional momentum screening threshold 1e-3 is not met')
    if result['core_affine_fit']['relative_remainder'] is None or result['core_affine_fit']['relative_remainder']<1e-4:
        reasons.append('zero or effectively affine field on the sampled core')
    if (result['angular']['n2_fraction'] or 0)<1e-6:
        reasons.append('n=2 energy not resolved by the screening threshold')
    if result['symmetry']['Q_velocity_relative'] is None or result['symmetry']['Q_velocity_relative']>1e-8:
        reasons.append('Q-equivariance not resolved')
    if result['model_metadata'].get('kind','').startswith(('affine','localized','manufactured')):
        reasons.append('calibration or initializer, not a trained candidate')
    for name,threshold in [('divergence',1e-6),('vorticity',1e-3),('pressure_poisson',1e-3)]:
        if any(reg.get(name,{}).get('relative_rms') is None or reg[name]['relative_rms']>threshold for reg in regions.values()):
            reasons.append('independent '+name+' screening threshold '+str(threshold)+' is not met or its denominator vanishes')
    tail=result['tail']['spheres'][-1]
    if tail['nonlinear_term_relative'] is None or tail['nonlinear_term_relative']>1e-2:
        reasons.append('outermost sampled tail fails the nonlinear-balance screening threshold 1e-2')
    if result.get('volume_angular'):
        if all((v['fields']['velocity']['n2_fraction'] or 0)<1e-6 for v in result['volume_angular'].values()):
            reasons.append('n=2 energy unresolved in physical-volume Fourier quadrature')
    if result['core_directional_dependence']['minimum_fraction'] is None or result['core_directional_dependence']['minimum_fraction']<1e-6:
        reasons.append('three-dimensional dependence unresolved on sampled core')
    return dict(status=('NO ACCEPTABLE CANDIDATE FOUND IN THIS SEARCH' if reasons else 'PRELIMINARY CANDIDATE REQUIRING FURTHER GATES'),
                reasons=reasons,worst_sampled_region=worst,
                worst_momentum_relative=regions[worst]['momentum']['relative_rms'],
                unresolved_gates=['whole-space pressure with tail','refinement/capacity/domain stability',
                                  'free exponent refit and tail-model sensitivity','nondegeneracy after penalties removed',
                                  'exact existence, stability, and finite-energy blowup are not established'])


def evaluate(model,experiment,n=512,seed=736291,checkpoint_hash=None):
    region_points=holdout_regions(seed,n)
    rng=np.random.default_rng(seed+917)
    config=dict(n=n,holdout_seed=seed,model_metadata=model.metadata)
    output=dict(experiment_id=experiment,created_utc=utc(),model_metadata=model.metadata,checkpoint_sha256=checkpoint_hash,
                c_l=model.c_l,C=model.C,config=config,regions={},execution=dict(
                    source_directory=str(Path(__file__).resolve().parent),numpy_version=np.__version__,
                    code_sha256={p.name:sha256(p) for p in Path(__file__).resolve().parent.glob('*.py')}),methods=dict(
                    forward='independent NumPy reconstruction',derivatives='physical Cartesian centered sixth-order finite differences',
                    precision='FP64',samples='independent physical-volume shells plus Cartesian grid and axis line',
                    norms='vector Euclidean magnitude RMS, with volume factors for shell L2 estimates',
                    maxima='sampled maxima only'))
    with Interval(experiment,config,checkpoint_hash) as interval:
        core=None
        for name,(points,volume) in region_points.items():
            f,J,H=differentiate(model,points,step=.002,order=6)
            r=residuals(points,f,J,H,model.c_l,model.C)
            output['regions'][name]=summarize(r,volume)
            if name=='shell_0.25_1':
                core=(points,r)
        points,r=core
        output['core_affine_fit']=affine_fit(points,r['U'])
        output['core_directional_dependence']=directional_dependence(r)
        output['c_l_fixed_field_sensitivity']=exponent_sensitivity(points,r,model.c_l,model.C)
        output['symmetry']=symmetry_diagnostics(model,points)
        output['vector_group_average']=vector_group_average(model,points[:128])
        output['angular']=angular_diagnostics(model)
        output['volume_angular']={f'ball_or_shell_{lo:g}_{hi:g}':volume_angular_spectra(model,lo,hi) for lo,hi in [(0,1),(0,2),(2,4),(8,16)]}
        output['axis']=axis_diagnostics(model,order=6)
        output['tail']=tail_check(model,rng)
        output['coordinate_plane_tails']=coordinate_plane_tails(model)
        output['residual_angular']=residual_spectra(model)
        output['geometry']=geometry(model,rng)
        # Step sweep uses the same fixed points but fresh derivative evaluations.
        sweep_points=points[:96]
        values=[]
        for order,step in [(4,.004),(4,.002),(4,.001),(6,.004),(6,.002),(6,.001)]:
            f,J,H=differentiate(model,sweep_points,step=step,order=order)
            rr=residuals(sweep_points,f,J,H,model.c_l,model.C)
            values.append((order,step,rr))
        reference=values[-1][2]
        output['derivative_step_sweep']=[]
        for order,step,rr in values:
            record=dict(order=order,step=step)
            for key in ['J','H','momentum','divergence','vorticity','pressure_poisson']:
                record[key+'_difference_to_sixth_order_h001']=stats(rr[key]-reference[key])
            output['derivative_step_sweep'].append(record)
        away=points[np.hypot(points[:,0],points[:,1])>.1][:96]
        f,J,H=differentiate(model,away,step=.001,order=6)
        rr=residuals(away,f,J,H,model.c_l,model.C)
        cr,cd=cylindrical_residual(model,away,model.c_l,model.C,step=.001,order=6)
        output['cartesian_cylindrical']=dict(momentum_difference=stats(cr-rr['momentum']),divergence_difference=stats(cd-rr['divergence']),sample_count=len(away))
        output['assessment']=assess(output)
    output['numerical_interval']=dict(start_utc=interval.start,end_utc=interval.end,active_seconds=interval.seconds)
    return output


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--model',choices=['seed','affine','polynomial'],default='seed')
    parser.add_argument('--c-l',type=float,default=.45)
    parser.add_argument('--a',type=float,default=.2);parser.add_argument('--b',type=float,default=-.4);parser.add_argument('--b2',type=float,default=.7)
    parser.add_argument('--n',type=int,default=512);parser.add_argument('--holdout-seed',type=int,default=736291)
    parser.add_argument('--experiment',default='seed-calibration-c045')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.model=='polynomial':
        model=Polynomial(c_l=args.c_l)
    else:
        model=(Seed if args.model=='seed' else Affine)(c_l=args.c_l,a=args.a,b=args.b,b2=args.b2)
    output=evaluate(model,args.experiment,args.n,args.holdout_seed)
    dest=args.output or ROOT/'evidence'/(args.experiment+'.json')
    atomic_json(dest,output)
    print(json.dumps(dict(output=str(dest),assessment=output['assessment'],active_seconds=output['numerical_interval']['active_seconds']),indent=2))



def coordinate_plane_tails(model):
    """Probe thin angular layers using coordinatewise physical FD scales."""
    records=[]
    for R in [16.,64.,256.,1024.]:
        points=[]
        for j in range(3):
            rest=[k for k in range(3) if k!=j]
            for small in [0.,.001,.01,.1,1.]:
                for sign in [-1.,1.]:
                    p=np.zeros(3);p[j]=small;p[rest[0]]=R;p[rest[1]]=sign*.37*R;points.append(p)
            for sign in [-1.,1.]:
                p=np.zeros(3);p[j]=sign*R;points.append(p)
        x=np.array(points);values=[]
        for step in [.004,.002]:
            h=step*np.maximum(1.,abs(x))
            f,J,H=differentiate(model,x,order=6,hessian=False,steps=h)
            r=residuals(x,f,J,H,model.c_l,model.C)
            values.append(r)
        r=values[-1];d=1-1/model.c_l;radius=np.linalg.norm(x,axis=1)
        nonlinear=sum(stats(t)['rms'] for t in [r['momentum_terms'][3],r['grad_P']])
        records.append(dict(radius_parameter=R,points=x.tolist(),velocity_scaled_by_r_d=stats(r['U']/radius[:,None]**d),
                            gradient_scaled_by_r_d_minus_1=stats(r['J']/radius[:,None,None]**(d-1)),
                            momentum=summarize(r)['momentum'],divergence=summarize(r)['divergence'],
                            nonlinear_relative_momentum=stats(r['momentum'])['rms']/nonlinear if nonlinear else None,
                            gradient_step_difference=stats(values[0]['J']-r['J']),
                            momentum_step_difference=stats(values[0]['momentum']-r['momentum'])))
    return dict(records=records,method='coordinate planes, near-plane strips, and axes; step_j = h max(1, abs(y_j))',
                scope='selected angular transition layers, first derivative check only; no uniform tail certificate')


if __name__=='__main__':
    main()

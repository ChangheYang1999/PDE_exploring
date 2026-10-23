"""Fixed 20-parameter grid refinement; immutable local numerical components.

Only sampling changes from 13x13 to 25x25. The pointwise residual, derivative,
physical bounds and Stage-IV frozen column maps are retained. No plotting.
"""
from ipm_portable import output_dir, peak_rss_mib
import argparse
import hashlib
import importlib
import json
from pathlib import Path
import resource
import signal
import time
from types import SimpleNamespace

import numpy as np
import psutil
from scipy.optimize import least_squares, minimize_scalar
from threadpoolctl import threadpool_info, threadpool_limits
import stage4_engine as v

t=v.t
s=t.s
ROOT=Path(__file__).resolve().parent
OUT = output_dir()
save=t.save


def problem(n):
    x,y=s.e.polar_grid(n,n,8.)
    return s.Problem(3,4,x,y,'fractional2',True)


def case_at(p,prob,n,label):
    return dict(t.case_at(p,prob,label),nr=n,nt=n)


def load(name):
    path=OUT/(name+'.json')
    if not path.exists():path=ROOT/'inputs'/('start_'+name+'.json')
    return json.loads(path.read_text())


def objective(case,n):
    prob=problem(n);r=prob.fun(t.parameters(case))
    nonorigin=(prob.x!=0)|(prob.y!=0)
    return {'grid':n,'points':len(r),'cost':float(r@r/2),
            'rms':float(np.sqrt(np.mean(r*r))),
            'rms_nonorigin':float(np.sqrt(np.mean(r[nonorigin]**2))),
            'max_fitting_residual':float(max(abs(r))),
            'origin_rows':int(sum(~nonorigin)),
            'origin_fitting_residual_max':float(max(abs(r[~nonorigin])))}


def holdout(n):
    angles=np.r_[0,1e-6,.001,(np.arange(n)+.37)*np.pi/(2*n),np.pi/2-.001,np.pi/2-1e-6,np.pi/2]
    return s.polar(np.geomspace(16.48,128,n),angles)


def verify(args):
    grids={}
    radii={n:np.r_[0.,np.geomspace(.08,8.,n-1)] for n in (13,25)}
    for n in (13,25):
        x,y=s.e.polar_grid(n,n,8.)
        grids[str(n)]={'radii':radii[n].tolist(),'angles':np.linspace(0,np.pi/2,n).tolist(),
                       'x':x.tolist(),'y':y.tolist(),'points':len(x),
                       'coordinate_sha256':hashlib.sha256(np.column_stack((x,y)).tobytes()).hexdigest()}
    shared=[float(r) for r in radii[13] if np.any(np.isclose(r,radii[25],rtol=1e-12,atol=1e-14))]
    grids['comparison']={'shared_radial_nodes':shared,'radially_nested':len(shared)==13,
                         'angles_nested':bool(np.array_equal(np.linspace(0,np.pi/2,13),np.linspace(0,np.pi/2,25)[::2]))}
    for n in (17,33,65):
        x,y=holdout(n)
        grids['H'+str(n)]={'points':len(x),'coordinate_sha256':hashlib.sha256(np.column_stack((x,y)).tobytes()).hexdigest()}
    assert len(shared)==3 and grids['comparison']['angles_nested']
    save('grids.json',grids)
    records={}
    for name in ('S0','B'):
        initial=load(name);p=t.parameters(initial);prob=problem(13)
        saved=case_at(p,prob,13,name+'_13')
        save(name+'_13.json',saved)
        oldchecks=json.loads((ROOT/'inputs'/(name+'_checks.json')).read_text())
        costs={str(n):objective(initial,n) for n in (13,25)}
        difference=costs['13']['cost']-initial['optimizer']['cost']
        assert abs(difference)<1e-12,(name,difference)
        assert np.array_equal(prob.coefficients(p),np.array(initial['coefficients']))
        hchecks={}
        for n in (17,33,65):
            x,y=holdout(n);row=s.diagnostic(initial,x,y)
            old=oldchecks['common_H_'+str(n)]
            differences={k:row[k]-old[k] for k in ('max_abs_Rf','max_abs_Rrho','max_normalized_Rf','max_normalized_Rrho')}
            assert max(abs(a) for a in differences.values())<1e-12
            hchecks[str(n)]={'diagnostic':row,'differences_from_stage4':differences}
        J=t.hybrid_jac(prob,p)
        records[name]={'objectives':costs,'cost13_difference_from_stage4':difference,
                       'coefficient_reconstruction_error':float(max(abs(prob.coefficients(p)-initial['coefficients']))),
                       'holdouts':hchecks,'derivative_check_13':v.direction_checks(prob,p,J)}
    save('verification.json',records)
    print(json.dumps({'grid_comparison':grids['comparison'],
                      'objectives':{n:v['objectives'] for n,v in records.items()}},indent=2))


class ChunkEnd(Exception):pass


def fit(args):
    wall0,cpu0=time.monotonic(),time.process_time()
    n=25;prob=problem(n);initial=load(args.basin)
    mapping=json.loads((ROOT/'inputs'/('map_'+args.basin+'.json')).read_text())
    anchor,D=np.array(mapping['anchor_parameters']),np.array(mapping['column_scale'])
    previous=load(args.resume) if args.resume else None
    if previous:
        assert previous['basin']==args.basin and previous['nr']==25
        assert previous['mapping']==mapping,'Continuation map changed'
        z0=np.array(previous['coordinate_vector'])
        assert np.array_equal(anchor+D*z0,t.parameters(previous)),'Continuation physical vector changed'
        calls,states,trials=previous['history'],previous['accepted_states'],previous['trials']
        nj=[previous['optimizer']['jacobian_calls']]
    else:
        z0=(t.parameters(initial)-anchor)/D
        calls,states,trials=[],[],[];nj=[0]
    prior_calls=len(calls)
    accepted_z=[z0.copy()]
    current=[case_at(anchor+D*z0,prob,n,args.label)]
    phase=['base'];radius=[None]
    record={**current[0],'basin':args.basin,'resume_from':args.resume,'mapping':mapping,
            'initial_coefficients':initial['coefficients'],'initial_cl':initial['cl'],
            'settings':{'grid':25,'rmax':8.,'max_total_actual_calls':args.calls,
                        'per_basin_ceiling':1200,'software_chunk_seconds':10.,
                        'ftol':1e-12,'xtol':1e-12,'gtol':1e-12,
                        'physical_bounds':[t.LOW.tolist(),t.HIGH.tolist()],
                        'jacobian':'unchanged Stage III/IV hybrid, cl relative step 1e-4',
                        'initial_map_roundtrip_error':float(max(abs(anchor+D*z0-(t.parameters(previous) if previous else t.parameters(initial))))),
                        'continuation_trust_radius_restarted':bool(previous)},'interrupted':True}
    stop_reason=['running']
    def checkpoint(reason,alias=False):
        record.update(current[0]);record['coordinate_vector']=accepted_z[0].tolist()
        record.update(history=calls,accepted_states=states,trials=trials,
                      optimizer={'stop':reason,'actual_residual_calls':len(calls),'jacobian_calls':nj[0],
                                 'accepted_steps':sum(a['accepted'] for a in trials),
                                 'rejected_steps':sum(not a['accepted'] for a in trials),
                                 'cost':states[-1]['cost'] if states else None,
                                 'segment_actual_calls':len(calls)-prior_calls,
                                 'segment_wall_seconds':time.monotonic()-wall0,
                                 'segment_cpu_seconds':time.process_time()-cpu0})
        save(args.label+'.json',record)
        if alias:save(args.basin+'_25.json',dict(record,label=args.basin+'_25'))
    def signal_stop(signum,frame):
        record['interrupted']=True
        checkpoint('guard SIGTERM; last accepted physical vector and map preserved',True)
        raise SystemExit(2)
    signal.signal(signal.SIGTERM,signal_stop)
    def fun(p):
        if len(calls)>=min(args.calls,1200):
            stop_reason[0]='actual evaluation cap, not stationarity';raise ChunkEnd()
        if phase[0]!='jacobian_probe' and time.monotonic()-wall0>10.:
            stop_reason[0]='software checkpoint time, not stationarity';raise ChunkEnd()
        r=prob.fun(p)
        calls.append({'evaluation':len(calls)+1,'phase':phase[0],'cost':float(r@r/2),
                      'rms':float(np.sqrt(np.mean(r*r))),**prob.metadata(p),
                      'segment_wall_seconds':time.monotonic()-wall0})
        return r
    cache={}
    def fz(z):
        p=anchor+D*z;r=fun(p);cache[tuple(z)]=r
        return r
    def jz(z):
        p=anchor+D*z;r=cache[tuple(z)]
        # A Jacobian callback identifies an accepted point, even at a cap.
        current[0]=case_at(p,prob,n,args.label);accepted_z[0]=z.copy()
        event='restart_initial' if previous and len(states) and np.array_equal(np.array(states[-1]['parameters']),p) else 'accepted'
        row={**current[0],'parameters':p.tolist(),'coordinate_vector':z.tolist(),
             'cost':float(r@r/2),'rms':float(np.sqrt(np.mean(r*r))),
             'event':event,'actual_calls':len(calls),'segment_wall_seconds':time.monotonic()-wall0,
             'derivative_pending':True}
        states.append(row)
        checkpoint('accepted; derivative pending')
        if len(calls)+4>min(args.calls,1200):
            stop_reason[0]='actual evaluation cap; accepted derivative pending';raise ChunkEnd()
        phase[0]='jacobian_probe'
        try:J=t.hybrid_jac(prob,p,fun)
        finally:phase[0]='base'
        nj[0]+=1
        g=J.T@r;d=1/np.linalg.norm(J,axis=0)
        raw=np.linalg.svd(J,compute_uv=False)
        U,eq,_=np.linalg.svd(J*d,full_matrices=False)
        mapped=np.linalg.svd(J*D,compute_uv=False)
        row.update(actual_calls=len(calls),jacobian_calls=nj[0],derivative_pending=False,
                   physical_gradient_inf=float(max(abs(g))),
                   column_scaled_gradient_inf=float(max(abs(d*g))),
                   coordinate_gradient_inf=float(max(abs(D*g))),
                   whitened_gradient_norm=float(np.linalg.norm(U.T@r)),
                   whitened_gradient_per_sqrtN=float(np.linalg.norm(U.T@r)/np.sqrt(len(r))),
                   relative_projected_residual=float(np.linalg.norm(U.T@r)/np.linalg.norm(r)),
                   raw_condition=float(raw[0]/raw[-1]),column_condition=float(eq[0]/eq[-1]),
                   mapped_condition=float(mapped[0]/mapped[-1]),trust_radius=radius[0])
        checkpoint('running')
        return J*D
    trf=importlib.import_module('scipy.optimize._lsq.trf');original=trf.update_tr_radius
    def update(delta,actual,predicted,stepnorm,boundhit):
        new,ratio=original(delta,actual,predicted,stepnorm,boundhit);radius[0]=float(new)
        trials.append({'trial':len(trials)+1,'actual_calls':len(calls),'accepted':bool(actual>0),
                       'actual_reduction':float(actual),'predicted_reduction':float(predicted),
                       'ratio':float(ratio),'radius_before':float(delta),'radius_after':float(new),
                       'coordinate_step_norm':float(stepnorm),'bound_hit':bool(boundhit)})
        return new,ratio
    checkpoint('initial checkpoint')
    trf.update_tr_radius=update
    try:
        result=least_squares(fz,z0,jac=jz,bounds=((t.LOW-anchor)/D,(t.HIGH-anchor)/D),
                             ftol=1e-12,xtol=1e-12,gtol=1e-12,max_nfev=min(args.calls,1200))
        stop_reason[0]='scipy '+result.message
        record['scipy_result']={'success':bool(result.success),'status':int(result.status),
                                'nfev':result.nfev,'njev':result.njev}
    except ChunkEnd:pass
    finally:trf.update_tr_radius=original
    record['interrupted']=False
    checkpoint(stop_reason[0],True)
    last=states[-1]
    print(json.dumps({'label':args.label,'cl':record['cl'],'a0':record['a0'],'optimizer':record['optimizer'],
                      'gradients':{k:x for k,x in last.items() if 'gradient' in k or 'condition' in k}},indent=2))


def assess(args):
    v.assess(args)
    case=load(args.label)
    records=load(args.label+'_checks')
    records['origin']=s.diagnostic(case,np.array([0.]),np.array([0.]))
    records['shared_objectives']={str(n):objective(case,n) for n in (13,25)}
    for n in (13,25):
        prob=problem(n)
        records['shared_fit_'+str(n)]=s.diagnostic(case,prob.x,prob.y)
    save(args.label+'_checks.json',records)


def analyze(args):
    case=load(args.label);n=case['nr'];t.problem=lambda:problem(n)
    v.analyze(args)
    a=load(args.label+'_conditioning');j=a['jacobians']
    a['grid']=n;a['points']=n*n
    a['jacobians']['raw_singular_values_per_sqrtN']=(np.array(j['raw_singular_values'])/n).tolist()
    a['jacobians']['field_metric_J_singular_values_per_sqrtN']=(np.array(j['field_metric_J_singular_values'])/n).tolist()
    a['stationarity']['whitened_gradient_per_sqrtN']=a['stationarity']['whitened_gradient_norm']/n
    save(args.label+'_conditioning.json',a)


def validate(args):
    case=load(args.label);t.problem=lambda:problem(case['nr'])
    v.validate(args)


def compare(args):
    records=[]
    for reference,candidate in (('S0_13','S0_25'),('B_13','B_25'),('S0_25','B_25')):
        a,b=load(reference),load(candidate)
        regions={}
        for region,x,y in [('inner',*s.polar(np.geomspace(.05,8,23),np.linspace(0,np.pi/2,15))),
                           ('exterior',*holdout(65))]:
            f=s.fields(a,x,y)['f'];norm=np.linalg.norm(f)
            def error(loglam):
                values=s.fields(b,x/np.exp(loglam),y/np.exp(loglam))['f']
                return float(np.linalg.norm(values-f)/norm)
            original=error(0.)
            opt=minimize_scalar(error,bounds=(np.log(.25),np.log(4)),method='bounded',options={'xatol':1e-9})
            improved=opt.fun<original
            regions[region]={'relative_L2_f_unaligned':original,
                             'relative_L2_f_aligned':float(opt.fun) if improved else original,
                             'lambda':float(np.exp(opt.x)) if improved else 1.,
                             'points':len(x),'alignment_uses_amplitude':False}
        # Transfer the INNER alignment to the exterior as a separate check.
        x,y=holdout(65);lam=regions['inner']['lambda']
        f=s.fields(a,x,y)['f'];bf=s.fields(b,x/lam,y/lam)['f']
        records.append({'reference':reference,'candidate':candidate,'cl_difference':b['cl']-a['cl'],
                        'a0_difference':b['a0']-a['a0'],'regions':regions,
                        'exterior_relative_L2_f_at_inner_lambda':float(np.linalg.norm(bf-f)/np.linalg.norm(f))})
    save('shape_comparisons.json',records)
    sampling={}
    for label in ('S0_13','S0_25','B_13','B_25'):
        sampling[label]={}
        for n in (13,25):
            prob=problem(n);r=prob.fun(t.parameters(load(label))).reshape(n,n)
            contributions=r*r/2;cost=float(np.sum(contributions))
            j=int(np.argmax(abs(r)))
            sampling[label][str(n)]={'cost':cost,
                'axis_columns_cost_fraction':float(np.sum(contributions[:,[0,-1]])/cost),
                'outer_radius_cost_fraction':float(np.sum(contributions[-1])/cost),
                'maximum_fitting_residual':float(np.max(abs(r))),
                'maximum_location':[float(prob.x[j]),float(prob.y[j])],
                'sample_fraction_axis_columns':2/n,'sample_fraction_outer_radius':1/n,
                'cost_by_angular_column':np.sum(contributions,axis=0).tolist(),
                'cost_by_radial_row':np.sum(contributions,axis=1).tolist()}
    save('sampling_contributions.json',sampling)
    print(json.dumps(records,indent=2))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['verify','fit','assess','analyze','validate','compare'])
    parser.add_argument('--label',default='preflight')
    parser.add_argument('--basin',choices=['S0','B'],default='S0')
    parser.add_argument('--calls',type=int,default=200)
    parser.add_argument('--resume')
    parser.add_argument('--start',default='S0')
    args=parser.parse_args()
    try:
        with threadpool_limits(limits=1):globals()[args.mode](args)
    finally:
        usage=resource.getrusage(resource.RUSAGE_SELF)
        save(args.mode+'_'+args.label+'_process.json',{'peak_rss_mib':peak_rss_mib(usage),
             'cpu_seconds':usage.ru_utime+usage.ru_stime,'threads_at_exit':psutil.Process().num_threads(),
             'nice':psutil.Process().nice(),'threadpools':threadpool_info()})


if __name__=='__main__':main()

"""Stage VI: fixed family, original sum versus normalized log-polar quadrature.
No holdout enters fitting or weights. All numerical components are local copies.
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
from scipy.linalg import null_space
from scipy.optimize import least_squares, minimize_scalar
from threadpoolctl import threadpool_info, threadpool_limits
import stage4_engine as v

t=v.t
s=t.s
ROOT=Path(__file__).resolve().parent
OUT = output_dir()
save=t.save
ORIGINAL_JAC=t.hybrid_jac


def quadrature(n):
    # n radial rows: ZERO followed by n-1 positive geometric radii.
    # Positive log-radius interval has n-2 trapezoidal subintervals.
    radial=np.r_[0.,np.ones(n-1)/(n-2)]
    radial[1]*=.5;radial[-1]*=.5
    angular=np.ones(n)/(n-1)
    angular[0]*=.5;angular[-1]*=.5
    return np.outer(radial,angular).ravel()


def weights_from_actual_coordinates(n):
    """General trapezoids on the actual Stage-V log-radius/angular knots."""
    # The coordinate generator is the frozen engine's actual implementation.
    x,y=s.e.polar_grid(n,n,8.)
    logs=np.log(x.reshape(n,n)[1:,0])
    angles=np.arctan2(y.reshape(n,n)[-1],x.reshape(n,n)[-1])
    def factors(nodes):
        result=np.empty(len(nodes))
        result[0]=(nodes[1]-nodes[0])/2
        result[-1]=(nodes[-1]-nodes[-2])/2
        result[1:-1]=(nodes[2:]-nodes[:-2])/2
        return result/(nodes[-1]-nodes[0])
    return np.outer(np.r_[0.,factors(logs)],factors(angles)).ravel()


def weights(args):
    rows={}
    for n in (13,25,49,97):
        exact=weights_from_actual_coordinates(n);used=quadrature(n)
        error=float(max(abs(exact-used)))
        assert error<1e-15
        rows[str(n)]={'max_weight_difference_actual_coordinate_trapezoids':error,
                       'actual_coordinate_weight_mass':float(exact.sum()),
                       'used_weight_mass':float(used.sum()),'origin_mass':float(exact[:n].sum())}
    save('actual_coordinate_weight_check.json',rows)
    print(json.dumps(rows,indent=2))


class AggregatedProblem(s.Problem):
    def __init__(self,n,aggregation):
        x,y=s.e.polar_grid(n,n,8.)
        super().__init__(3,4,x,y,'fractional2',True)
        self.n,self.aggregation=n,aggregation
        self.root=np.sqrt(quadrature(n)) if aggregation=='W' else np.ones(n*n)
        self.last_raw=None;self.last_parameters=None
    def fun(self,p):
        self.last_raw=super().fun(p)
        self.last_parameters=p.copy()
        return self.root*self.last_raw if self.aggregation=='W' else self.last_raw


def hybrid_jac(prob,p,fun=None,cl_step=1e-4):
    if not isinstance(prob,AggregatedProblem):
        return ORIGINAL_JAC(prob,p,fun,cl_step)
    # Keep ALL raw derivative formulas and cl probes unchanged, then multiply
    # every row ONCE by sqrt(weight). Never divide by zero origin weights.
    def raw(pp):
        if fun is None:return s.Problem.fun(prob,pp)
        fun(pp)
        assert np.array_equal(prob.last_parameters,pp)
        return prob.last_raw
    return prob.root[:,None]*ORIGINAL_JAC(prob,p,raw,cl_step)


t.hybrid_jac=hybrid_jac


def problem(n,aggregation='U'):return AggregatedProblem(n,aggregation)


def case_at(p,prob,n,label):
    return dict(t.case_at(p,prob,label),nr=n,nt=n,optimization_objective=prob.aggregation)


def load(name):
    path=OUT/(name+'.json')
    if not path.exists():path=ROOT/'inputs'/('start_'+name+'.json')
    return json.loads(path.read_text())


def holdout(n):
    theta=np.r_[0,1e-6,.001,(np.arange(n)+.37)*np.pi/(2*n),np.pi/2-.001,np.pi/2-1e-6,np.pi/2]
    return s.polar(np.geomspace(16.48,128,n),theta)


class ChunkEnd(Exception):pass


def fit(args):
    wall0,cpu0=time.monotonic(),time.process_time()
    n=args.grid;prob=problem(n,args.objective);initial=load(args.initial)
    mapping=json.loads((ROOT/'inputs'/('map_'+args.basin+'.json')).read_text())
    if args.objective=='W':
        mapping=dict(mapping,column_scale=(np.array(mapping['column_scale'])*n).tolist(),
                     normalized_objective_coordinate_factor=n)
    anchor,D=np.array(mapping['anchor_parameters']),np.array(mapping['column_scale'])
    previous=load(args.resume) if args.resume else None
    if previous:
        assert previous['basin']==args.basin and previous['nr']==n and previous['optimization_objective']==args.objective
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
    record={**current[0],'basin':args.basin,'initial_source':args.initial,'resume_from':args.resume,'mapping':mapping,
            'initial_coefficients':initial['coefficients'],'initial_cl':initial['cl'],
            'settings':{'grid':n,'rmax':8.,'max_total_actual_calls':args.calls,
                        'per_fit_ceiling':1200,'software_chunk_seconds':8.,
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
        if alias:save(args.candidate+'.json',dict(record,label=args.candidate))
    def signal_stop(signum,frame):
        record['interrupted']=True
        checkpoint('guard SIGTERM; last accepted physical vector and map preserved',True)
        raise SystemExit(2)
    signal.signal(signal.SIGTERM,signal_stop)
    def fun(p):
        if len(calls)>=min(args.calls,1200):
            stop_reason[0]='actual evaluation cap, not stationarity';raise ChunkEnd()
        if phase[0]!='jacobian_probe' and time.monotonic()-wall0>8.:
            stop_reason[0]='software checkpoint time, not stationarity';raise ChunkEnd()
        r=prob.fun(p)
        calls.append({'evaluation':len(calls)+1,'phase':phase[0],'cost':float(r@r/2),
                      'aggregation_rms':float(np.linalg.norm(r) if args.objective=='W' else np.sqrt(np.mean(r*r))),**prob.metadata(p),
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
             'cost':float(r@r/2),'aggregation_rms':float(np.linalg.norm(r) if args.objective=='W' else np.sqrt(np.mean(r*r))),
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
                   whitened_gradient_per_root_mass=float(np.linalg.norm(U.T@r)/np.linalg.norm(prob.root)),
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


def verify(args):
    results={'quadrature':{},'reproduction':{},'jacobians':{}}
    for n in (13,25,49,97):
        weights=quadrature(n).reshape(n,n)
        ss=np.r_[0.,np.linspace(0,1,n-1)][:,None]
        tt=np.linspace(0,1,n)[None,:]
        row={'mass':float(weights.sum()),'origin_mass':float(weights[0].sum()),
             'axis_mass':float(weights[:,[0,-1]].sum()),'outer_mass':float(weights[-1].sum()),
             'log_linear_error':float(abs(np.sum(weights*ss)-.5)),
             'angle_linear_error':float(abs(np.sum(weights*tt)-.5)),
             'bilinear_error':float(abs(np.sum(weights*ss*tt)-.25)),
             'log_quadratic_error':float(np.sum(weights*ss**2)-1/3),
             'angle_quadratic_error':float(np.sum(weights*tt**2)-1/3),
             'exp_log_error':float(np.sum(weights*np.exp(ss))-(np.e-1))}
        assert abs(row['mass']-1)<1e-14 and row['origin_mass']==0
        assert max(row[k] for k in ('log_linear_error','angle_linear_error','bilinear_error'))<1e-14
        assert abs(row['log_quadratic_error']-1/(6*(n-2)**2))<1e-14
        assert abs(row['angle_quadratic_error']-1/(6*(n-1)**2))<1e-14
        results['quadrature'][str(n)]=row
    for basin in ('S0','B'):
        for n in (13,25):
            name=f'U{n}_{basin}';case=load(name);p=t.parameters(case);prob=problem(n)
            r=prob.fun(p);old=load(name+'_checks')
            expected=old['shared_objectives'][str(n)]['cost']
            difference=float(r@r/2-expected)
            assert abs(difference)<1e-12
            save(name+'.json',dict(case,label=name,optimization_objective='U'))
            x,y=holdout(65);h=s.diagnostic(case,x,y)
            dh={k:h[k]-old['common_H_65'][k] for k in ('max_abs_Rf','max_abs_Rrho','max_normalized_Rf','max_normalized_Rrho')}
            assert max(abs(v) for v in dh.values())<1e-12
            results['reproduction'][name]={'cost_difference':difference,'holdout_differences':dh}
        # An independent weighted directional FD, plus exact row-chain equality.
        case=load(f'U25_{basin}');p=t.parameters(case)
        for n in (13,25,49):
            raw=problem(n,'U');weighted=problem(n,'W')
            ju=hybrid_jac(raw,p);jw=hybrid_jac(weighted,p)
            assert np.array_equal(jw,weighted.root[:,None]*ju)
            direction=np.cos(np.arange(20)+.31);direction/=np.linalg.norm(direction)
            step=1e-5
            fd=(weighted.fun(p+step*direction)-weighted.fun(p-step*direction))/(2*step)
            error=float(np.linalg.norm(fd-jw@direction)/np.linalg.norm(fd))
            assert error<2e-4
            results['jacobians'][f'W{n}_{basin}']={'row_chain_error':0.,'directional_FD_relative_error':error,
                'origin_J_max':float(abs(jw[:n]).max())}
    save('verification.json',results)
    print(json.dumps(results,indent=2))


def raw_values(case,x,y,batch=512):
    """Same frozen pointwise evaluator, batched only to bound assessment memory."""
    p=t.parameters(case);answer=np.empty(len(x))
    for lo in range(0,len(x),batch):
        hi=min(len(x),lo+batch)
        prob=s.Problem(3,4,x[lo:hi],y[lo:hi],'fractional2',True)
        answer[lo:hi]=prob.fun(p)
    return answer


def cross(args):
    case=load(args.label);rows={}
    for n in (13,25,49,97):
        x,y=s.e.polar_grid(n,n,8.)
        e=raw_values(case,x,y);w=quadrature(n);u=e*e/2;q=w*u
        uma=u.reshape(n,n);qma=q.reshape(n,n)
        index=int(np.argmax(abs(e)))
        rows[str(n)]={'points':len(e),'unweighted_cost':float(u.sum()),
                      'unweighted_RMS':float(np.sqrt(2*u.mean())),
                      'weighted_cost':float(q.sum()),'weighted_RMS':float(np.sqrt(2*q.sum())),
                      'max_pointwise_fitting_residual':float(abs(e[index])),
                      'max_location':[float(x[index]),float(y[index])],
                      'quadrature_mass':float(w.sum()),'origin_quadrature_mass':float(sum(w[:n])),
                      'axis_cost_fraction_U':float(uma[:,[0,-1]].sum()/u.sum()),
                      'axis_cost_fraction_W':float(qma[:,[0,-1]].sum()/q.sum()),
                      'outer_cost_fraction_U':float(uma[-1].sum()/u.sum()),
                      'outer_cost_fraction_W':float(qma[-1].sum()/q.sum()),
                      'coordinate_sha256':hashlib.sha256(np.column_stack((x,y)).tobytes()).hexdigest()}
    save(args.label+'_cross.json',{'label':args.label,'optimization_objective':case.get('optimization_objective','U'),
                                 'fit_grid':case['nr'],'grids':rows,'grid97_assessment_only':True,'batch_points':512})
    print(json.dumps({'label':args.label,'weighted_cost97':rows['97']['weighted_cost']},indent=2))


def assess(args):
    # All physical diagnostics ignore the aggregation used to fit the candidate.
    v.assess(args)
    case=load(args.label);records=load(args.label+'_checks')
    records['origin']=s.diagnostic(case,np.array([0.]),np.array([0.]))
    save(args.label+'_checks.json',records)


def validate(args):
    case=load(args.label)
    t.problem=lambda:problem(case['nr'],case['optimization_objective'])
    v.validate(args)


def analyze(args):
    case=load(args.label);p=t.parameters(case)
    prob=problem(case['nr'],case['optimization_objective']);J=hybrid_jac(prob,p)
    D=1/np.linalg.norm(J,axis=0);U,sv,Vt=np.linalg.svd(J*D,full_matrices=False)
    raw=np.linalg.svd(J,compute_uv=False);r=prob.fun(p);g=J.T@r
    theta=np.r_[0,1e-6,.001,(np.arange(17)+.37)*np.pi/34,np.pi/2-.001,np.pi/2-1e-6,np.pi/2]
    x,y=s.polar(np.geomspace(.035,8.,17),theta);x,y=np.r_[0.,x],np.r_[0.,y]
    ff,design=t.field_design(prob,p,x,y);target=t.scale_target(case,x,y,ff)
    a0=float(ff['f'][0]);normal=max(1,abs(a0))*np.sqrt(3*len(x));rad=1+np.hypot(x,y)
    B=np.vstack([design['f'],design['psix']/rad[:,None],design['psiy']/rad[:,None]])/normal
    exact=np.r_[target['f'],target['psix']/rad,target['psiy']/rad]/normal
    _,sb,vb=np.linalg.svd(B,full_matrices=False)
    field=np.linalg.svd(J@(vb.T/sb[None,:]),compute_uv=False)
    a0gradient=design['f'][0]
    Z=null_space(a0gradient[None,1:])
    fit=np.linalg.lstsq(B[:,1:]@Z,exact,rcond=1e-12)[0]
    tangent=np.r_[0.,Z@fit];eq_tangent=tangent/D
    def cosine(a,b):return float(abs(a@b)/(np.linalg.norm(a)*np.linalg.norm(b)))
    weak=[]
    for k in (1,2,3):
        direction=D*Vt[-k];direction/=np.linalg.norm(B@direction)
        weak.append({'rank_from_smallest':k,'parameters_per_unit_field':direction.tolist(),
                     'delta_cl_per_unit_field':float(direction[0]),
                     'delta_a0_per_unit_field':float(a0gradient@direction),
                     'field_cosine_with_exact_scaling_tangent':cosine(B@direction,exact),
                     'coordinate_overlap_projected_scaling':cosine(Vt[-k],eq_tangent)})
    result={'label':args.label,'grid':case['nr'],'optimization_objective':case['optimization_objective'],
            'cl':p[0],'a0':a0,'raw_condition':float(raw[0]/raw[-1]),
            'column_condition':float(sv[0]/sv[-1]),'field_condition':float(field[0]/field[-1]),
            'raw_singular_values':raw.tolist(),'column_singular_values':sv.tolist(),'field_singular_values':field.tolist(),
            'normalization_root_mass':float(np.linalg.norm(prob.root)),
            'raw_singular_values_normalized':(raw/np.linalg.norm(prob.root)).tolist(),
            'field_singular_values_normalized':(field/np.linalg.norm(prob.root)).tolist(),
            'physical_gradient_inf':float(max(abs(g))),'column_scaled_gradient_inf':float(max(abs(D*g))),
            'whitened_gradient_norm':float(np.linalg.norm(U.T@r)),
            'relative_projected_residual':float(np.linalg.norm(U.T@r)/np.linalg.norm(r)),
            'projected_exact_scaling_tangent_error':float(np.linalg.norm(B@tangent-exact)/np.linalg.norm(exact)),
            'scale_projection_delta_cl':0.,'scale_projection_delta_a0':float(a0gradient@tangent),
            'weak_directions':weak,'right_singular_vectors_column_coordinates':Vt.tolist()}
    save(args.label+'_conditioning.json',result)
    print(json.dumps({k:result[k] for k in ('label','raw_condition','column_condition','field_condition','whitened_gradient_norm')},indent=2))


def compare(args):
    paths=[]
    for basin in (args.basin,):
        paths.extend([(f'U13_{basin}',f'U25_{basin}'),(f'U25_{basin}',f'U49_{basin}'),
                      (f'W13_{basin}',f'W25_{basin}'),(f'W25_{basin}',f'W49_{basin}'),
                      (f'U49_{basin}',f'W49_{basin}')])
    records=[]
    for reference,candidate in paths:
        a,b=load(reference),load(candidate);regions={}
        for name,(x,y) in [('inner',s.polar(np.geomspace(.05,8,23),np.linspace(0,np.pi/2,15))),('exterior',holdout(65))]:
            f=s.fields(a,x,y)['f'];norm=np.linalg.norm(f)
            def error(logscale):
                value=s.fields(b,x/np.exp(logscale),y/np.exp(logscale))['f']
                return float(np.linalg.norm(value-f)/norm)
            before=error(0.);fit=minimize_scalar(error,bounds=(np.log(.25),np.log(4)),method='bounded',options={'xatol':1e-8})
            better=fit.fun<before
            regions[name]={'unaligned_relative_L2_f':before,'aligned_relative_L2_f':float(fit.fun) if better else before,
                           'lambda':float(np.exp(fit.x)) if better else 1.,'amplitude_adjusted':False,'points':len(x)}
        x,y=holdout(65);f=s.fields(a,x,y)['f'];lam=regions['inner']['lambda']
        transferred=s.fields(b,x/lam,y/lam)['f']
        records.append({'reference':reference,'candidate':candidate,'cl_difference':b['cl']-a['cl'],
                        'a0_difference':b['a0']-a['a0'],'regions':regions,
                        'exterior_error_at_inner_lambda':float(np.linalg.norm(transferred-f)/np.linalg.norm(f))})
    save('shape_comparisons_'+args.basin+'.json',records)
    print(json.dumps(records,indent=2))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['verify','weights','fit','cross','assess','validate','analyze','compare'])
    parser.add_argument('--label',default='preflight')
    parser.add_argument('--candidate',default='U49_S0')
    parser.add_argument('--basin',choices=['S0','B'],default='S0')
    parser.add_argument('--grid',choices=[13,25,49],type=int,default=49)
    parser.add_argument('--objective',choices=['U','W'],default='U')
    parser.add_argument('--initial',default='U25_S0')
    parser.add_argument('--calls',type=int,default=160)
    parser.add_argument('--resume')
    args=parser.parse_args()
    try:
        with threadpool_limits(limits=1):globals()[args.mode](args)
    finally:
        usage=resource.getrusage(resource.RUSAGE_SELF)
        save(args.mode+'_'+args.label+'_process.json',{'peak_rss_mib':peak_rss_mib(usage),
             'cpu_seconds':usage.ru_utime+usage.ru_stime,'threads_at_exit':psutil.Process().num_threads(),
             'nice':psutil.Process().nice(),'threadpools':threadpool_info()})


if __name__=='__main__':main()



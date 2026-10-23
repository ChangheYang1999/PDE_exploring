"""Stage IV: fixed-model optimization, counted trials, reversible right maps.

Frozen engines retain the Stage III trial family, nodes, objective and assessors.
No direction is truncated; singular-value floors only bound invertible maps.
"""
from ipm_portable import output_dir, peak_rss_mib
import argparse
import importlib
import json
import math
from pathlib import Path
import resource
import signal
import time
from types import SimpleNamespace

import numpy as np
import psutil
from scipy.optimize import least_squares, minimize_scalar
from threadpoolctl import threadpool_info, threadpool_limits
import stage3_engine as t

ROOT = Path(__file__).resolve().parent
OUT = output_dir()
s = t.s
save = t.save


def load(name):
    p = OUT/(name+'.json')
    return json.loads((p if p.exists() else ROOT/'inputs'/('start_'+name+'.json')).read_text())


def direction_checks(prob, p, j):
    """Separate central directional differences; include a weak, units-scaled mode."""
    d = 1/np.linalg.norm(j, axis=0)
    _, _, vt = np.linalg.svd(j*d, full_matrices=False)
    directions = {'mixed': np.cos(np.arange(20)+.37), 'cl': np.eye(20)[0],
                  'weak_eq': d*vt[-1]}
    result = {}
    for name, v in directions.items():
        v = v/np.linalg.norm(v)
        rows = []
        for h in (1e-3, 3e-4, 1e-4, 3e-5):
            fd = (prob.fun(p+h*v)-prob.fun(p-h*v))/(2*h)
            expected = j@v
            rows.append({'h': h, 'relative_error': float(np.linalg.norm(fd-expected)/max(1e-30,np.linalg.norm(expected))),
                         'absolute_error': float(np.linalg.norm(fd-expected)), 'Jv_norm': float(np.linalg.norm(expected))})
        result[name] = rows
    half = t.hybrid_jac(prob,p,cl_step=5e-5)
    result['cl_step_half_relative'] = float(np.linalg.norm(j[:,0]-half[:,0])/np.linalg.norm(j[:,0]))
    return result


def verify(args):
    records = {}
    for name in ('S0','F','G'):
        case, prob = load(name), t.problem()
        p = t.parameters(case)
        r = prob.fun(p)
        j = t.hybrid_jac(prob,p)
        supplied = case['optimizer']['cost']
        check = {'cost': float(r@r/2), 'recorded_cost': supplied,
                 'cost_abs_difference': float(abs(r@r/2-supplied)),
                 'physical_gradient_inf': float(max(abs(j.T@r))),
                 'cl': float(p[0]), 'a0': prob.metadata(p)['a0'],
                 'coefficient_reconstruction_max': float(max(abs(prob.coefficients(p)-case['coefficients']))),
                 'directional_checks': direction_checks(prob,p,j)}
        assert check['cost_abs_difference'] < 1e-12
        assert check['coefficient_reconstruction_max'] < 1e-11
        records[name] = check
        save(name+'.json',t.case_at(p,prob,name))
    save('verification.json', records)
    print(json.dumps({name:{k:v for k,v in row.items() if k!='directional_checks'} for name,row in records.items()},indent=2))


class Budget(Exception):
    pass


def fit(args):
    wall0, cpu0 = time.monotonic(), time.process_time()
    prob = t.problem()
    initial = load(args.start)
    p = t.parameters(initial)
    calls, states, trials = [], [], []
    previous = load(args.resume) if args.resume else None
    if previous:
        assert previous['method']==args.method and previous['start']==args.start
        p = t.parameters(previous)
        calls, states, trials = previous['history'], previous['accepted_states'], previous['trials']
    previous_calls = len(calls)
    phase = ['base']
    nj = [previous['optimizer']['jacobian_calls'] if previous else 0]
    refreshes = previous.get('refreshes',[]) if previous else []
    radius = previous.get('radius',None) if previous else None
    P = np.array(previous['right_map']) if previous and 'right_map' in previous else None
    since = previous.get('accepted_since_refresh',0) if previous else 0
    current = t.case_at(p,prob,args.label)
    record = {**current,'method':args.method,'start':args.start,'resume_from':args.resume,
              'initial_physical_parameters': t.parameters(initial).tolist(),
              'initial_coefficients': initial['coefficients'],
              'settings': {'total_actual_call_cap':args.calls,'physical_bounds':[t.LOW.tolist(),t.HIGH.tolist()],
                           'objective_nodes_unchanged':True,'refresh_accepted_interval':8,'refresh_condition_threshold':30,
                           'first_order_whitened_target':1e-8,'first_order_physical_target':1e-5},
              'interrupted':True}
    def checkpoint(reason):
        record.update(current)
        record.update(history=calls,accepted_states=states,trials=trials,refreshes=refreshes,
                      radius=radius,right_map=P.tolist() if P is not None else None,
                      accepted_since_refresh=since,
                      optimizer={'stop':reason,'actual_residual_calls':len(calls),'jacobian_calls':nj[0],
                                 'accepted_steps':max(0,len(states)-1),'rejected_steps':sum(not a['accepted'] for a in trials),
                                 'cost':states[-1]['cost'] if states else None,
                                 'segment_actual_calls':len(calls)-previous_calls,
                                 'segment_wall_seconds':time.monotonic()-wall0,'segment_cpu_seconds':time.process_time()-cpu0})
        save(args.label+'.json',record)
    def stop(signum,frame):
        checkpoint('SIGTERM: last accepted point preserved')
        raise SystemExit(2)
    signal.signal(signal.SIGTERM,stop)
    def fun(pp):
        if len(calls)>=args.calls: raise Budget()
        rr=prob.fun(pp)
        calls.append({'evaluation':len(calls)+1,'phase':phase[0],'cost':float(rr@rr/2),
                      **prob.metadata(pp),'segment_wall_seconds':time.monotonic()-wall0})
        return rr
    def jac(pp):
        if len(calls)+4>args.calls: raise Budget()
        phase[0]='jacobian_probe'
        try: jj=t.hybrid_jac(prob,pp,fun)
        finally: phase[0]='base'
        nj[0]+=1
        return jj
    def state(pp,rr,jj,coord=None):
        nonlocal current
        current=t.case_at(pp,prob,args.label)
        ss=np.linalg.svd(jj,compute_uv=False)
        dd=1/np.linalg.norm(jj,axis=0)
        uu,se,_=np.linalg.svd(jj*dd,full_matrices=False)
        gg=jj.T@rr
        row={**current,'parameters':pp.tolist(),'cost':float(rr@rr/2),
             'actual_calls':len(calls),'jacobian_calls':nj[0],
             'physical_gradient_inf':float(max(abs(gg))),
             'column_scaled_gradient_inf':float(max(abs(dd*gg))),
             'whitened_gradient_norm':float(np.linalg.norm(uu.T@rr)),
             'raw_condition':float(ss[0]/ss[-1]),'equilibrated_condition':float(se[0]/se[-1]),
             'trust_radius':radius,'segment_wall_seconds':time.monotonic()-wall0}
        if coord is not None:
            row['coordinate_condition']=float(np.linalg.cond(jj@coord))
            row['coordinate_gradient_inf']=float(max(abs(coord.T@gg)))
        if states and np.array_equal(np.array(states[-1]['parameters']),pp): states[-1]=row
        else: states.append(row)
        checkpoint('running')
        return row
    reason='evaluation budget'
    try:
        if args.method in ('stage3_frozen','stage3_tight'):
            # Keep Stage III's ORIGINAL anchor and column units for its continuation.
            anchor=load('S1') if args.start in ('F','G') else load('S0')
            pa=t.parameters(anchor)
            ja=jac(pa)
            D=1/np.linalg.norm(ja,axis=0)
            P=np.diag(D)
            z0=(p-pa)/D
            cache={}
            def fz(z):
                rr=fun(pa+D*z);cache[tuple(z)]=rr
                return rr
            def jz(z):
                nonlocal p,current
                p=pa+D*z
                current=t.case_at(p,prob,args.label)
                # A derivative request identifies an accepted TRF point.
                if len(calls)+4>args.calls:
                    states.append({**current,'parameters':p.tolist(),'cost':float(cache[tuple(z)]@cache[tuple(z)]/2),
                                   'actual_calls':len(calls),'jacobian_calls':nj[0],'derivative_pending':True})
                jj=jac(p)
                state(p,cache[tuple(z)],jj,P)
                return jj*D
            trf=importlib.import_module('scipy.optimize._lsq.trf')
            original=trf.update_tr_radius
            def update(delta,actual,predicted,stepnorm,boundhit):
                nonlocal radius
                new,ratio=original(delta,actual,predicted,stepnorm,boundhit)
                radius=float(new)
                trials.append({'trial':len(trials)+1,'actual_calls':len(calls),'accepted':bool(actual>0),
                               'actual_reduction':float(actual),'predicted_reduction':float(predicted),
                               'ratio':float(ratio),'radius_before':float(delta),'radius_after':float(new),
                               'coordinate_step_norm':float(stepnorm),'bound_hit':bool(boundhit)})
                return new,ratio
            trf.update_tr_radius=update
            try:
                tol=1e-12 if args.method=='stage3_tight' else 1e-8
                record['settings']['ftol_xtol_gtol']=tol
                result=least_squares(fz,z0,jac=jz,bounds=((t.LOW-pa)/D,(t.HIGH-pa)/D),
                                     ftol=tol,xtol=tol,gtol=tol,max_nfev=args.calls)
                reason='scipy '+result.message
                record['scipy_result']={'status':int(result.status),'success':bool(result.success),
                                        'nfev':result.nfev,'njev':result.njev}
            finally: trf.update_tr_radius=original
        else:
            rr=fun(p);jj=jac(p)
            if radius is None: radius=max(1e-6,.1*np.linalg.norm(rr))
            row=state(p,rr,jj,P)
            failures=0
            while True:
                # Reserve one trial and its four derivative probes so that every
                # saved accepted point has a complete fresh Jacobian diagnostic.
                if len(calls)+5>args.calls: raise Budget()
                if row['whitened_gradient_norm']<1e-8 and row['physical_gradient_inf']<1e-5:
                    reason='first-order target (requires independent validation)';break
                cond=float(np.linalg.cond(jj@P)) if P is not None else float('inf')
                refresh=P is None or (args.method=='refresh_svd' and (since>=8 or cond>30 or failures>=5))
                if refresh:
                    dd=1/np.linalg.norm(jj,axis=0)
                    _,sv,vt=np.linalg.svd(jj*dd,full_matrices=False)
                    P=dd[:,None]*vt.T/np.maximum(sv,sv[0]*1e-12)[None,:]
                    refreshes.append({'actual_calls':len(calls),'accepted_index':len(states)-1,
                                      'previous_coordinate_condition':cond if math.isfinite(cond) else None,
                                      'reason':'initial' if since==0 and not refreshes else 'interval/condition/rejections',
                                      'smallest_equilibrated_singular':float(sv[-1])})
                    since=0;failures=0
                    radius=min(radius,max(1e-6,.5*np.linalg.norm(rr)))
                A=jj@P
                U,sv,Vt=np.linalg.svd(A,full_matrices=False)
                v=U.T@rr
                def dy(mu): return -Vt.T@((sv/(sv*sv+mu))*v)
                step=dy(0.);mu=0.
                if np.linalg.norm(step)>radius:
                    lo,hi=0.,max(1e-20,sv[0]**2)
                    while np.linalg.norm(dy(hi))>radius: hi*=4
                    for _ in range(55):
                        mid=(lo+hi)/2
                        if np.linalg.norm(dy(mid))>radius: lo=mid
                        else: hi=mid
                    mu=hi;step=dy(mu)
                dp=P@step
                positive=dp>0;negative=dp<0
                fraction=min(1.,float(np.min(.995*(t.HIGH[positive]-p[positive])/dp[positive])) if any(positive) else 1.,
                             float(np.min(.995*(t.LOW[negative]-p[negative])/dp[negative])) if any(negative) else 1.)
                dp*=fraction;step*=fraction
                pred=-float((jj.T@rr)@dp)-.5*float(np.linalg.norm(jj@dp)**2)
                if pred<=1e-24 or np.array_equal(p,p+dp):
                    reason='trust/model collapse, not stationarity';break
                trial=fun(p+dp)
                actual=float((rr@rr-trial@trial)/2);ratio=actual/pred
                oldradius=radius
                if ratio<.25: radius*=.25
                elif ratio>.75 and np.linalg.norm(step)>.8*radius: radius*=2
                accepted=actual>0 and ratio>1e-4
                trials.append({'trial':len(trials)+1,'actual_calls':len(calls),'accepted':bool(accepted),
                               'actual_reduction':actual,'predicted_reduction':pred,'ratio':ratio,
                               'radius_before':oldradius,'radius_after':radius,'damping':mu,
                               'coordinate_step_norm':float(np.linalg.norm(step)),
                               'physical_step_norm':float(np.linalg.norm(dp)),
                               'coordinate_condition':float(sv[0]/sv[-1]),'bound_fraction':fraction})
                if accepted:
                    p=p+dp;rr=trial;since+=1;failures=0
                    # Preserve accepted vectors even if the next derivative hits its budget.
                    current=t.case_at(p,prob,args.label)
                    checkpoint('accepted; derivative pending')
                    jj=jac(p);row=state(p,rr,jj,P)
                else:
                    failures+=1;checkpoint('rejected trial')
                if radius<1e-14:
                    reason='trust radius collapse, not stationarity';break
    except Budget:
        reason='actual residual evaluation budget, not stationarity'
    record['interrupted']=False
    checkpoint(reason)
    print(json.dumps({'label':args.label,'cl':current['cl'],'a0':current['a0'],
                      'optimizer':record['optimizer'],'last_state':{k:v for k,v in states[-1].items()
                                                                 if 'gradient' in k or 'condition' in k}},indent=2))


def assess(args):
    # Frozen Cartesian evaluator + independent polar inverse, unchanged Stage II regions.
    s.assess(SimpleNamespace(label=args.label,common_grid_batch=False,compare=None))
    case=load(args.label)
    records=json.loads((OUT/(args.label+'_checks.json')).read_text())
    for n in (17,33,65):
        angles=np.r_[0,1e-6,.001,(np.arange(n)+.37)*np.pi/(2*n),np.pi/2-.001,np.pi/2-1e-6,np.pi/2]
        x,y=s.polar(np.geomspace(16.48,128,n),angles)
        records['common_H_'+str(n)]=s.diagnostic(case,x,y)
    save(args.label+'_checks.json',records)


def analyze(args):
    t.analyze(args)
    case=load(args.label);prob=t.problem();p=t.parameters(case);j=t.hybrid_jac(prob,p)
    record=json.loads((OUT/(args.label+'_conditioning.json')).read_text())
    r=prob.fun(p);dd=1/np.linalg.norm(j,axis=0)
    U,sv,_=np.linalg.svd(j*dd,full_matrices=False)
    record['stationarity']={'cost':float(r@r/2),'physical_gradient_inf':float(max(abs(j.T@r))),
                             'column_scaled_gradient_inf':float(max(abs(dd*(j.T@r)))),
                             'whitened_gradient_norm':float(np.linalg.norm(U.T@r)),
                             'relative_projected_residual':float(np.linalg.norm(U.T@r)/np.linalg.norm(r)),
                             'directional_checks':direction_checks(prob,p,j)}
    save(args.label+'_conditioning.json',record)


def compare(args):
    names=args.labels.split(',')
    x,y=s.polar(np.geomspace(.05,8,23),np.linspace(0,np.pi/2,15))
    records=[]
    for i,name in enumerate(names):
        ca=load(name);ref=s.fields(ca,x,y)['f']
        for other in names[i+1:]:
            cb=load(other)
            def error(loglam):
                v=s.fields(cb,x/np.exp(loglam),y/np.exp(loglam))['f']
                return np.linalg.norm(v-ref)/np.linalg.norm(ref)
            res=minimize_scalar(error,bounds=(math.log(.25),math.log(4)),method='bounded')
            before=float(error(0));better=res.fun<before
            records.append({'reference':name,'candidate':other,'cl_difference':cb['cl']-ca['cl'],
                            'a0_difference':cb['a0']-ca['a0'],'shape_before':before,
                            'shape_after':float(res.fun) if better else before,
                            'lambda':float(np.exp(res.x)) if better else 1.,
                            'alignment_includes_identity':True})
    save('shape_comparisons.json',records)
    # Track changes of weak directions in the same sampled physical-field metric.
    weak=[]
    for path in (('S0','S0_mid','S0_refresh_600'),('F','F_mid','F_refresh_600'),
                 ('G','G_mid','G_refresh_600'),('G','G_tight_mid','G_tight_900')):
        previous=None
        for name in path:
            cond=json.loads((OUT/(name+'_conditioning.json')).read_text())
            pp=t.parameters(load(name));prob=t.problem()
            theta=np.r_[0,1e-6,.001,(np.arange(17)+.37)*np.pi/34,np.pi/2-.001,np.pi/2-1e-6,np.pi/2]
            xx,yy=s.polar(np.geomspace(.035,8.,17),theta)
            xx,yy=np.r_[0.,xx],np.r_[0.,yy]
            _,B=t.field_design(prob,pp,xx,yy)
            v=np.array(cond['weak_directions'][0]['physical_unit_field_direction_parameters'])
            radial=1+np.hypot(xx,yy)
            bv=np.r_[B['f']@v,(B['psix']@v)/radial,(B['psiy']@v)/radial]
            cosine=None if previous is None else float(abs(bv@previous)/(np.linalg.norm(bv)*np.linalg.norm(previous)))
            weak.append({'path':list(path),'label':name,'physical_field_cosine_previous':cosine})
            previous=bv
    save('weak_direction_changes.json',weak)
    print(json.dumps(records,indent=2))


def validate(args):
    """Residual-value directional differentiation, independent of hybrid formulas.

    Compare gradients in ONE fixed whitened metric, so changing units cannot
    hide derivative uncertainty. No validation points are used to fit a profile.
    """
    prob=t.problem();case=load(args.label);p=t.parameters(case)
    count=[0];jcount=[0]
    def fun(pp):
        count[0]+=1
        return prob.fun(pp)
    def jac(pp,step=1e-4):
        jcount[0]+=1
        return t.hybrid_jac(prob,pp,fun,cl_step=step)
    r=fun(p);j=jac(p);cost=float(r@r/2)
    D=1/np.linalg.norm(j,axis=0)
    _,sv,vt=np.linalg.svd(j*D,full_matrices=False)
    P=D[:,None]*vt.T/sv[None,:]
    g=P.T@(j.T@r)
    metrics=[]
    for hcl in (2e-4,5e-5,2.5e-5):
        ja=jac(p,hcl);ga=P.T@(ja.T@r)
        metrics.append({'cl_relative_step':hcl,'whitened_gradient_norm':float(np.linalg.norm(ga)),
                        'gradient_change_norm':float(np.linalg.norm(ga-g))})
    rows=[]
    for hphysical in (1e-3,5e-4):
        fdcols=[];curvatures=[];cost_directionals=[];jv_errors=[]
        for k in range(20):
            v=P[:,k];h=hphysical/np.linalg.norm(v)
            values=[fun(p+a*h*v) for a in (2,1,-1,-2)]
            df=(-values[0]+8*values[1]-8*values[2]+values[3])/(12*h)
            fdcols.append(df)
            cv=[float(a@a/2) for a in values]
            cost_directionals.append((-cv[0]+8*cv[1]-8*cv[2]+cv[3])/(12*h))
            curvatures.append((cv[1]-2*cost+cv[2])/h**2)
            jv_errors.append(float(np.linalg.norm(df-j@v)))
        fd=np.column_stack(fdcols)
        fdg=fd.T@r
        rows.append({'physical_direction_step':hphysical,'whitened_gradient_norm_from_fd_residuals':float(np.linalg.norm(fdg)),
                     'fd_gradient_change_norm':float(np.linalg.norm(fdg-g)),
                     'fd_cost_gradient_norm':float(np.linalg.norm(cost_directionals)),
                     'fd_cost_gradient_components':cost_directionals,
                     'fd_gradient_components':fdg.tolist(),'Jv_absolute_errors':jv_errors,
                     'sampled_coordinate_curvatures':curvatures})
    # Safeguarded GN predictions provide a concrete size for the remaining step.
    dp=-P@g
    probes=[]
    for factor in (1.,.5,.25,.1,-.1):
        pp=p+factor*dp
        if np.all(pp>t.LOW) and np.all(pp<t.HIGH):
            rr=fun(pp)
            probes.append({'factor':factor,'cost':float(rr@rr/2),'cost_change':float(rr@rr/2-cost),
                           'cl_change':float(factor*dp[0]),'physical_step_norm':float(np.linalg.norm(factor*dp))})
    result={'cost':cost,'hybrid_whitened_gradient_norm':float(np.linalg.norm(g)),
            'relative_projected_residual':float(np.linalg.norm(g)/np.linalg.norm(r)),
            'predicted_GN_cost_decrease':float(g@g/2),'GN_parameter_step':dp.tolist(),
            'cl_column_sensitivity':metrics,'independent_directional_checks':rows,'GN_trial_probes':probes,
            'actual_residual_calls':count[0],'jacobian_calls':jcount[0],
            'diagnostic_coordinate_map':P.tolist()}
    save(args.label+'_stationarity.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('diagnostic_coordinate_map','GN_parameter_step','independent_directional_checks')},indent=2))


def curvature(args):
    """Full objective Hessian probe, not merely J^T J, in a fixed right metric.

    Finite differences of the gradient at two physical step sizes diagnose
    residual-weighted curvature and its sensitivity. This is not a certificate.
    """
    prob=t.problem();p=t.parameters(load(args.label));calls=[0];nj=[0]
    def fun(pp):
        calls[0]+=1
        return prob.fun(pp)
    def jac(pp):
        nj[0]+=1
        return t.hybrid_jac(prob,pp,fun,cl_step=5e-5)
    j=jac(p);D=1/np.linalg.norm(j,axis=0)
    _,sv,vt=np.linalg.svd(j*D,full_matrices=False)
    P=D[:,None]*vt.T/sv[None,:]
    def grad(pp):
        rr=fun(pp);jj=jac(pp)
        return P.T@(jj.T@rr)
    rows=[];matrices=[]
    for physical_h in ((2.5e-3,1.25e-3) if args.fine else (1e-2,5e-3)):
        columns=[]
        for k in range(20):
            v=P[:,k];h=physical_h/np.linalg.norm(v)
            columns.append((grad(p+h*v)-grad(p-h*v))/(2*h))
        H=np.column_stack(columns);sym=(H+H.T)/2
        eig=np.linalg.eigvalsh(sym)
        rows.append({'physical_step':physical_h,'eigenvalues':eig.tolist(),
                     'asymmetry_spectral_norm':float(np.linalg.norm((H-H.T)/2,ord=2)),
                     'symmetric_hessian':sym.tolist()})
        matrices.append(sym)
    richardson=(4*matrices[1]-matrices[0])/3
    result={'levels':rows,'symmetric_level_difference_spectral_norm':float(np.linalg.norm(matrices[1]-matrices[0],ord=2)),
            'richardson_eigenvalues':np.linalg.eigvalsh(richardson).tolist(),
            'actual_residual_calls':calls[0],'jacobian_calls':nj[0]}
    save(args.label+('_curvature_fine.json' if args.fine else '_curvature.json'),result)
    print(json.dumps({k:v for k,v in result.items() if k!='levels'},indent=2))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['verify','fit','assess','analyze','compare','validate','curvature'])
    parser.add_argument('--label',default='preflight')
    parser.add_argument('--start',default='S0')
    parser.add_argument('--method',choices=['stage3_frozen','stage3_tight','frozen_svd','refresh_svd'],default='refresh_svd')
    parser.add_argument('--calls',type=int,default=600)
    parser.add_argument('--resume')
    parser.add_argument('--labels',default='S0,F,G')
    parser.add_argument('--fine',action='store_true')
    args=parser.parse_args()
    try:
        with threadpool_limits(limits=1): globals()[args.mode](args)
    finally:
        usage=resource.getrusage(resource.RUSAGE_SELF)
        save(args.mode+'_'+args.label+'_process.json',{'peak_rss_mib':peak_rss_mib(usage),
            'cpu_seconds':usage.ru_utime+usage.ru_stime,'threads_at_exit':psutil.Process().num_threads(),
            'nice':psutil.Process().nice(),'threadpools':threadpool_info()})


if __name__=='__main__': main()

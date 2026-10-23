"""One secondary strategy: SLSQP with a frozen full Jacobian whitening.

Physical box bounds become exact linear constraints in invertible coordinates.
No residual penalty, gauge, clipping or weak-direction removal is introduced.
This file is executed in stage8's namespace, like the primary fit implementation.
"""
from ipm_portable import output_dir, peak_rss_mib
from scipy.optimize import minimize,LinearConstraint

def secondary(args):
    started=time.monotonic();prob=JointProblem(.1);initial=load(args.initial)
    assert initial['family']=='fractional3'
    previous=load(args.resume) if args.resume else None
    history=[] if previous is None else previous['history']
    states=[] if previous is None else previous['accepted_states']
    nj=[0 if previous is None else previous['optimizer']['jacobian_calls']]
    phase=['base'];cache={};accepted=[None];reason=['running']
    class EndSecondary(Exception):pass
    def physical_fun(p):
        if len(history)>=args.calls:reason[0]='matched secondary actual-call ceiling';raise EndSecondary()
        if phase[0]!='jacobian_probe' and time.monotonic()-started>8:
            reason[0]='secondary software checkpoint; not stationarity';raise EndSecondary()
        if not (np.all(p>=t.LOW-1e-8) and np.all(p<=t.HIGH+1e-8)):
            reason[0]='secondary physical bound trial refused before PDE evaluation; check stopped'
            save(args.label+'_refused_trial.json',dict(parameters=p.tolist(),PDE_evaluated=False,
                 completed_residual_calls=len(history),max_bound_violation=float(max(np.max(t.LOW-p),np.max(p-t.HIGH)))))
            raise EndSecondary()
        r=prob.fun(p)
        history.append(dict(evaluation=len(history)+1,phase=phase[0],cost=float(r@r/2),**prob.metadata(p),**prob.objectives()))
        with (OUT/(args.label+'_evaluation_journal.jsonl')).open('a') as stream:
            stream.write(json.dumps(dict(history[-1],parameters=p.tolist()),separators=(',',':'))+'\n')
        return r
    if previous is None:
        anchor=parameters(initial);r0=physical_fun(anchor);phase[0]='jacobian_probe'
        try:J0=hybrid_jac(prob,anchor,physical_fun)
        finally:phase[0]='base'
        nj[0]+=1;D=1/np.linalg.norm(J0,axis=0);_,sv,Vt=np.linalg.svd(J0*D,full_matrices=False)
        assert sv[-1]>0
        F=np.asfortranarray((D[:,None]*Vt.T/sv[None,:])*np.linalg.norm(r0))
        cost_scale=float(r0@r0/2)
        mapping=dict(anchor_parameters=anchor.tolist(),full_coordinate_map=F.tolist(),frozen=True,
                     cost_scale=cost_scale,smallest_equilibrated_sigma=float(sv[-1]),coordinate_map_condition=float(np.linalg.cond(F)),
                     physical_bounds_transformed_to_exact_linear_constraints=True,setup_residual_calls=5)
        q0=np.zeros(24)
        (ROOT/'inputs'/('map_'+args.candidate+'.json')).write_text(json.dumps(mapping,indent=2))
    else:
        mapping=previous['mapping'];anchor=np.array(mapping['anchor_parameters']);F=np.array(mapping['full_coordinate_map'],order='F')
        cost_scale=mapping['cost_scale'];q0=np.array(previous['coordinate_vector'])
        assert np.array_equal(anchor+F@q0,parameters(previous))
    accepted[0]=q0.copy()
    record=dict(basin=args.basin,far_weight=.1,initial_source=args.initial,initial_coefficients=initial['coefficients'],
                mapping=mapping,history=history,accepted_states=states,trials=[],
                settings={'method':'SLSQP, frozen full-Jacobian coordinates, exact linear physical bounds',
                    'software_chunk_seconds':8.,'actual_call_ceiling':args.calls,'ftol':1e-14,'maxiter_per_segment':300,
                    'BFGS_curvature_restarted_on_continuation':bool(previous),'unchanged_pointwise_objective':True})
    def checkpoint(stop,alias=True):
        p=anchor+F@accepted[0];record.update(case_at(p,prob,49,args.label))
        record.update(coordinate_vector=accepted[0].tolist(),history=history,accepted_states=states,
              optimizer=dict(stop=stop,actual_residual_calls=len(history),jacobian_calls=nj[0],
                 cost=states[-1]['cost'] if states else cost_scale,segment_wall_seconds=time.monotonic()-started))
        save(args.label+'.json',record)
        if alias:save(args.candidate+'.json',dict(record,label=args.candidate))
    def stop(signum,frame):checkpoint('guard SIGTERM; last accepted secondary point');raise SystemExit(2)
    signal.signal(signal.SIGTERM,stop)
    def fq(q):
        p=anchor+F@q;r=physical_fun(p);cache.clear();cache[tuple(q)]=(r,prob.objectives())
        return float(r@r/2/cost_scale)
    def jq(q):
        p=anchor+F@q
        if tuple(q) not in cache:fq(q)
        r,obj=cache[tuple(q)]
        if len(history)+4>args.calls:reason[0]='secondary cap before complete Jacobian';raise EndSecondary()
        phase[0]='jacobian_probe'
        try:J=hybrid_jac(prob,p,physical_fun)
        finally:phase[0]='base'
        nj[0]+=1;g=J.T@r
        if states and states[-1]['parameters']==p.tolist():
            states[-1].update(physical_gradient_inf=float(max(abs(g))),
                full_coordinate_gradient_inf=float(max(abs(F.T@g))),derivative_pending=False)
        return F.T@g/cost_scale
    def callback(q):
        if tuple(q) not in cache:fq(q)
        r,obj=cache[tuple(q)];p=anchor+F@q;accepted[0]=q.copy()
        states.append(dict(**case_at(p,prob,49,args.label),parameters=p.tolist(),coordinate_vector=q.tolist(),
              cost=float(r@r/2),**obj,event='accepted',derivative_pending=True,actual_calls=len(history)))
        checkpoint('secondary accepted checkpoint')
    checkpoint('secondary initial checkpoint')
    try:
        result=minimize(fq,q0,jac=jq,method='SLSQP',constraints=[LinearConstraint(F,t.LOW-anchor,t.HIGH-anchor)],
                callback=callback,options={'ftol':1e-14,'maxiter':300,'disp':False})
        reason[0]='SLSQP '+result.message
        record['scipy_result']=dict(success=bool(result.success),status=int(result.status),nit=int(result.nit))
    except EndSecondary:pass
    checkpoint(reason[0])
    print(json.dumps(dict(cl=record['cl'],a0=record['a0'],optimizer=record['optimizer'])))

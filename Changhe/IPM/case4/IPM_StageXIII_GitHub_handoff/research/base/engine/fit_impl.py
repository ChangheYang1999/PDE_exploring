"""Stage VI frozen-column fit, adapted only for Stage VII joint rows and maps."""
from ipm_portable import output_dir, peak_rss_mib
class ChunkEnd(Exception):pass


def fit(args):
    wall0,cpu0=time.monotonic(),time.process_time()
    n=49;prob=JointProblem(args.weight);initial=load(args.initial)
    assert all(load('nest_'+args.basin+'_'+part)['passed'] for part in ('main','bands'))
    assert load('setup_'+args.basin)['jacobian_verified']
    mapping=json.loads((ROOT/'inputs'/('map_'+args.candidate+'.json')).read_text())
    anchor,D=np.array(mapping['anchor_parameters']),np.array(mapping['column_scale'])
    previous=load(args.resume) if args.resume else None
    if previous:
        assert previous['basin']==args.basin and previous['far_weight']==args.weight
        assert previous['mapping']==mapping,'Continuation map changed'
        z0=np.array(previous['coordinate_vector'])
        assert np.array_equal(anchor+D*z0,t.parameters(previous)),'Continuation physical vector changed'
        calls,states,trials=previous['history'],previous['accepted_states'],previous['trials']
        nj=[previous['optimizer']['jacobian_calls']]
    else:
        z0=(t.parameters(initial)-anchor)/D
        calls,states,trials=list(mapping['setup_history']),[],[];nj=[1]
    prior_calls=len(calls)
    # Keep an immutable segment input, then journal deltas rather than rewriting
    # the growing history twice at every accepted point in the Dropbox folder.
    if previous:
        with gzip.open(OUT/(args.label+'_resume_input.json.gz'),'wt') as stream:json.dump(previous,stream,separators=(',',':'))
    def journal(kind,value):
        with (OUT/(args.label+'_'+kind+'.jsonl')).open('a') as stream:
            stream.write(json.dumps(value,separators=(',',':'))+'\n')
    accepted_z=[z0.copy()]
    current=[case_at(anchor+D*z0,prob,n,args.label)]
    phase=['base'];radius=[None]
    record={**current[0],'basin':args.basin,'far_weight':args.weight,'initial_source':args.initial,'resume_from':args.resume,'mapping':mapping,
            'initial_coefficients':initial['coefficients'],'initial_cl':initial['cl'],
            'settings':{'grid':n,'rmax':8.,'far_rmin':8.,'far_rmax':64.,'max_total_actual_calls':args.calls,
                        'per_fit_ceiling':2400,'software_chunk_seconds':8.,
                        'ftol':1e-12,'xtol':1e-12,'gtol':1e-12,
                        'physical_bounds':[t.LOW.tolist(),t.HIGH.tolist()],
                        'jacobian':'Stage III/IV hybrid, cl relative step '+str(CL_STEP_DEFAULT),
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
        if states:journal('accepted_journal',{'record_index':len(states)-1,'reason':reason,'state':states[-1]})
        save(args.label+'_checkpoint.json',dict(current[0],coordinate_vector=accepted_z[0].tolist(),
              mapping=mapping,reason=reason,actual_residual_calls=len(calls),accepted_records=len(states),
              trial_records=len(trials),resume_input=args.label+'_resume_input.json.gz' if previous else None,
              residual_journal=args.label+'_residual_journal.jsonl',accepted_journal=args.label+'_accepted_journal.jsonl',
              trial_journal=args.label+'_trial_journal.jsonl'))
        if alias:
            save(args.label+'.json',record)
            save(args.candidate+'.json',dict(record,label=args.candidate))
    def signal_stop(signum,frame):
        record['interrupted']=True
        checkpoint('guard SIGTERM; last accepted physical vector and map preserved',True)
        raise SystemExit(2)
    signal.signal(signal.SIGTERM,signal_stop)
    def fun(p):
        if len(calls)>=min(args.calls,2400):
            stop_reason[0]='actual evaluation cap, not stationarity';raise ChunkEnd()
        if phase[0]!='jacobian_probe' and time.monotonic()-wall0>8.:
            stop_reason[0]='software checkpoint time, not stationarity';raise ChunkEnd()
        r=prob.fun(p)
        calls.append({'evaluation':len(calls)+1,'phase':phase[0],'cost':float(r@r/2),
                      'aggregation_rms':float(np.linalg.norm(r) if args.objective=='W' else np.sqrt(np.mean(r*r))),**prob.metadata(p),**prob.objectives(),
                      'segment_wall_seconds':time.monotonic()-wall0})
        journal('residual_journal',calls[-1])
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
             'cost':float(r@r/2),**prob.objectives(),'aggregation_rms':float(np.linalg.norm(r) if args.objective=='W' else np.sqrt(np.mean(r*r))),
             'event':event,'actual_calls':len(calls),'segment_wall_seconds':time.monotonic()-wall0,
             'derivative_pending':True}
        states.append(row)
        checkpoint('accepted; derivative pending')
        if len(calls)+4>min(args.calls,2400):
            stop_reason[0]='actual evaluation cap; accepted derivative pending';raise ChunkEnd()
        phase[0]='jacobian_probe'
        try:J=hybrid_jac(prob,p,fun)
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
        journal('trial_journal',trials[-1])
        return new,ratio
    checkpoint('initial checkpoint')
    trf.update_tr_radius=update
    try:
        result=least_squares(fz,z0,jac=jz,bounds=((t.LOW-anchor)/D,(t.HIGH-anchor)/D),
                             ftol=1e-12,xtol=1e-12,gtol=1e-12,max_nfev=min(args.calls,2400))
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


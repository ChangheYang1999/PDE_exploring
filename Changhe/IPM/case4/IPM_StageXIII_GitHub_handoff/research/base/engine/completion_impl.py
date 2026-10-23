"""Additional verification and diagnostics; no change to the fitted equations."""
from ipm_portable import output_dir, peak_rss_mib
def saved_finish(args):
    case=load('saved');fp=a.fingerprint(case);st=load('saved_stationarity_scale4');local=load('saved_local')
    assert st['physical_vector_sha256']==fp and local['physical_vector_sha256']==fp
    assert load('saved_cross_grid')['physical_vector_sha256']==fp
    coords=load('assessment_grids');allrows={}
    for part in ['main','bands']:
        assert load('saved_'+part+'_source')['physical_vector_sha256']==fp
        allrows.update(load('saved_'+part+'_diagnostics'))
    assert set(allrows)==set(coords)
    assert load('saved_independent')['physical_vector_sha256']==fp
    assert max(abs(float(x)) for x in local['jet']['high_precision']['constraints'])<1e-10
    assert load('final')['fit_residual_calls']==97 and load('final')['fit_jacobian_calls']==14
    chart=v.Chart();mapping=load('fit_map');p=params(case);D=np.array(mapping['column_scale']);anchor=np.array(mapping['anchor'])
    z=(p[chart.free]-anchor)/D;reconstructed=chart.lift(anchor+D*z)
    error=float(max(abs(reconstructed-p)));assert error<1e-12
    save('saved_assessment_ready.json',{'physical_vector_sha256':fp,'all_25_regions_complete':True,
        'independent_gradient_complete':True,'near_stationary':st['near_stationary'],'starting_fit_calls':97,
        'completed_historical_Jacobians':14,'frozen_map_roundtrip_max_abs':error,
        'roundtrip_bitwise':bool(np.array_equal(reconstructed,p)),
        'no_historical_incomplete_Jacobian_promoted':True,'quadratic_high_precision_verified':True})
    print(json.dumps({'saved_assessment_complete':True,'near_stationary':st['near_stationary'],'roundtrip_error':error}))

def reduced_verify(args):
    case=load(args.label);p=params(case);chart=v.Chart();prob=factory(97);q=p[chart.free]
    lifted,R=chart.lift(q,True);assert max(abs(lifted-p))<1e-12
    J=hybrid(prob,p,cl_step=v.CL_STEP);jq=J@R;rows=[];rng=np.random.default_rng(10097)
    for i in range(2):
        direction=rng.normal(size=22);direction/=np.linalg.norm(R@direction)
        for h in [.00025,.000125]:
            vals=[prob.fun(chart.lift(q+k*h*direction)) for k in [2,1,-1,-2]]
            fd=(-vals[0]+8*vals[1]-8*vals[2]+vals[3])/(12*h)
            rows.append({'direction':i,'physical_step':h,'relative_error':float(np.linalg.norm(fd-jq@direction)/np.linalg.norm(fd))})
    C,G=constraint(p,True)
    result={'physical_vector_sha256':a.fingerprint(case),'errors':rows,'pair_condition':float(np.linalg.cond(G[:,chart.z])),
        'constraint_tangent_error':float(np.linalg.norm(G@R)),'max_error':max(r['relative_error'] for r in rows)}
    save(args.label+'_reduced_derivative_verification.json',result)
    assert result['max_error']<1e-5
    print(json.dumps({'label':args.label,'max_reduced_derivative_error':result['max_error']}))

def fourth_probes(args):
    base=load('final');analysis=load('final_fourth_analysis');p=params(base);dp=np.array(analysis['linearized_correction'])
    prob=factory(97);chart=v.Chart();B,mr,ff,D=v.metric(prob,p);r=prob.fun(p);J=hybrid(prob,p,cl_step=v.CL_STEP)
    C4,G4=fourth(p,True);rows=[]
    for fraction in [1.,.5,.25,.125]:
        try:
            pp=chart.lift(p[chart.free]+fraction*dp[chart.free]);case=make(pp,prob,'linear_probe');rr=prob.fun(pp)
            rows.append({'fraction':fraction,'predicted_C4':(C4+fraction*G4@dp).tolist(),
                'actual_C4':fourth(pp).tolist(),'quadratic_constraints':constraint(pp).tolist(),
                'predicted_J':float(np.linalg.norm(r+fraction*J@dp)**2/2),'actual_J':float(rr@rr/2),
                'measured_field_distance':v.field_distance(case,base,mr),
                'linear_field_size':float(fraction*np.linalg.norm(B@dp)),
                'delta_cl':float(pp[0]-p[0]),'delta_a0':float(case['a0']-base['a0']),
                'pair_condition':float(np.linalg.cond(constraint(pp,True)[1][:,chart.z]))})
        except ValueError as exc:rows.append({'fraction':fraction,'refused':str(exc)})
    save('fourth_linearized_probes.json',{'physical_vector_sha256':a.fingerprint(base),
        'feasibility_only':True,'PDE_objective_not_optimized':True,'rows':rows})
    print(json.dumps({'fourth_probes':rows}))

def compare_final(args):
    original=load('original');case=load('final');prob=factory(97);p=params(case);B,mr,ff,D=v.metric(prob,p)
    delta=params(case)-params(original)
    local=load('final_local');st=load('final_stationarity_scale4')
    assert st['near_stationary'] and st['physical_vector_sha256']==a.fingerprint(case)
    save('grid_stability.json',{'original_fingerprint':a.fingerprint(original),'refined_fingerprint':a.fingerprint(case),
        'delta_parameters':delta.tolist(),'delta_coefficients':(np.array(case['coefficients'])-original['coefficients']).tolist(),
        'delta_cl':case['cl']-original['cl'],'delta_a0':case['a0']-original['a0'],
        'relative_delta_cl':case['cl']/original['cl']-1,'relative_delta_a0':case['a0']/original['a0']-1,
        'historical_field_distance':v.field_distance(case,original,mr),
        'field_normalizer_reference_a0':original['a0'],'field_nodes':len(mr[0]),
        'original_GN_uncertainty_marker':load('original_stationarity_scale4').get('GN_correction_marker'),
        'refined_GN_uncertainty_marker':st['GN_correction_marker'],
        'original_cross_grid':load('original_cross_grid'),'refined_cross_grid':load('final_cross_grid'),
        'interpretation':'one-step refinement stability, not an asymptotic convergence theorem'})
    print(json.dumps({'field_distance':v.field_distance(case,original,mr),'delta_cl':delta[0]}))

def cl_study(args):
    case=load(args.label);p=params(case);prob=factory(97);r=prob.fun(p);B,mr,ff,D=v.metric(prob,p)
    _,sb,vb=np.linalg.svd(B,full_matrices=False);F=vb.T/sb;C,G=constraint(p,True);T=F@null_space(G@F)
    rows=[];reference=None
    for factor in [1.,.5,2.]:
        J=hybrid(prob,p,cl_step=v.CL_STEP*factor);U,sv,Vt=np.linalg.svd(J@T,full_matrices=False)
        if reference is None:reference=J[:,0].copy()
        rows.append({'relative_cl_step':v.CL_STEP*factor,
            'cl_column_relative_change':float(np.linalg.norm(J[:,0]-reference)/np.linalg.norm(reference)),
            'hybrid_relative':float(np.linalg.norm(U.T@r)/np.linalg.norm(r))})
        save(args.label+'_cl_step_study.json',{'physical_vector_sha256':a.fingerprint(case),'rows':rows,'production_cl_step_unchanged':True})
    print(json.dumps({'label':args.label,'cl_step_study':rows}))

def precision_probe(args):
    tag='precision_candidate_'+str(args.batch)
    if (OUT/(tag+'_check.json')).exists():print('Completed precision probe preserved');return
    base=load('primary_floor');p=params(base);chart=v.Chart();prob=factory(97)
    data=np.load(OUT/'primary_history/final_stationarity_arrays.npz');assert np.array_equal(data['p'],p)
    r0=data['r'];Z=data['Z'];JZ=data['JZ'];g=JZ.T@r0;direction=-Z@g
    fraction=[1.,.5,.1][args.batch];pp=chart.lift(p[chart.free]+fraction*direction[chart.free])
    B,mr,ff,D=v.metric(prob,p);assert np.linalg.norm(B@(pp-p))<1e-4
    current=load('final');calls=current['fit_residual_calls'];jc=current['fit_jacobian_calls']
    def counted(q,kind='precision_cl_probe'):
        nonlocal calls
        assert calls<2400
        rr=prob.fun(q);calls+=1
        with (OUT/'fit_evaluations.jsonl').open('a') as stream:
            stream.write(json.dumps({'call':calls,'p':q.tolist(),'cost':float(rr@rr/2),'type':kind,'precision_fraction':fraction})+'\n')
        current['fit_residual_calls']=calls;save('final.json',current)
        return rr
    rr=counted(pp,'precision_GN_base');obj=prob.objectives();J=hybrid(prob,pp,fun=counted,cl_step=v.CL_STEP)
    C,G=constraint(pp,True);_,sb,vb=np.linalg.svd(B,full_matrices=False);F=vb.T/sb;T=F@null_space(G@F)
    U,sv,Vt=np.linalg.svd(J@T,full_matrices=False);gamma=float(np.linalg.norm(U.T@rr)/np.linalg.norm(rr));jc+=1
    current['fit_jacobian_calls']=jc;save('final.json',current)
    case=make(pp,prob,tag);case.update(fit_residual_calls=calls,fit_jacobian_calls=jc,reduced_frozen_map=load('fit_map'),stop_reason='single feasible GN precision check')
    save(tag+'.json',case);jet=v.jet_report(case);obs=load('precision_obstruction')
    result={'physical_vector_sha256':a.fingerprint(case),'fraction':fraction,'hybrid_relative':gamma,
        'actual_reduction':float((r0@r0-rr@rr)/2),'predicted_reduction':float((fraction-fraction**2/2)*(g@g)),
        'cost_difference_from_primary':float((rr@rr-r0@r0)/2),
        'within_empirical_cost_resolution':bool((rr@rr-r0@r0)/2<=obs['objective_comparison_allowance']),
        'field_distance':v.field_distance(case,base,mr),'pair_condition':float(np.linalg.cond(G[:,chart.z])),
        'delta_cl':float(pp[0]-p[0]),'delta_a0':case['a0']-base['a0'],'jet':jet,'fit_calls_total':calls,'fit_J_total':jc}
    save(tag+'_check.json',result)
    print(json.dumps({k:val for k,val in result.items() if k!='jet'}))

def precision_select(args):
    records=[load('precision_candidate_'+str(i)+'_check') for i in range(3)]
    eligible=[(i,row) for i,row in enumerate(records) if row['within_empirical_cost_resolution'] and max(abs(float(v)) for v in row['jet']['high_precision']['constraints'])<1e-10]
    assert eligible,'No candidate compatible with observed cost resolution and quadratic feasibility'
    index,row=min(eligible,key=lambda z:z[1]['hybrid_relative']);case=load('precision_candidate_'+str(index));current=load('final')
    case.update(fit_residual_calls=current['fit_residual_calls'],fit_jacobian_calls=current['fit_jacobian_calls'])
    save('polish.json',case);save('precision_selection.json',{'selected_index':index,'selected':row,'all_probe_records':records,
        'independent_validation_required':True,'threshold_unchanged':1e-5,'single_secondary_check':True})
    print(json.dumps({'selected_fraction':row['fraction'],'hybrid_relative':row['hybrid_relative']}))

def precision_promote(args):
    st=load('polish_stationarity_scale4');case=load('polish')
    assert st['near_stationary'] and st['physical_vector_sha256']==a.fingerprint(case)
    assert load('polish_reduced_derivative_verification')['physical_vector_sha256']==a.fingerprint(case)
    current=load('final');case.update(label='final',fit_residual_calls=current['fit_residual_calls'],fit_jacobian_calls=current['fit_jacobian_calls'])
    save('final.json',case)
    import shutil
    for path in OUT.glob('polish_*'):
        suffix=path.name[len('polish_'):]
        if path.is_file():shutil.copy2(path,OUT/('final_'+suffix))
    with (OUT/'accepted_vectors.jsonl').open('a') as stream:
        stream.write(json.dumps({'call':case['fit_residual_calls'],'p':params(case).tolist(),'C':constraint(params(case)).tolist(),
           'cost':load('polish_local')['objectives']['J_joint'],'method':'independently verified feasible GN precision check; cost difference unresolved'})+'\n')
    save('precision_promotion.json',{'physical_vector_sha256':a.fingerprint(case),'independent_stationarity_passed':True,
        'primary_endpoint_preserved_in':'primary_history','cost_improvement_not_claimed_below_observed_noise':True,
        'fit_calls_total':case['fit_residual_calls'],'fit_J_total':case['fit_jacobian_calls']})
    print('Independently verified precision endpoint retained; frozen map/chart/objective unchanged')

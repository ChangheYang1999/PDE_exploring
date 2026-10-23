"""Runtime helpers executed in stage10's namespace; no side effects at import."""
from ipm_portable import output_dir, peak_rss_mib
def algebra(args):
    import polynomial_check
    save('polynomial_formulation_verification.json',polynomial_check.check());print('Formal s,t polynomial identities verified')

def fdstudy(args):
    case=load(args.label);n=49 if args.label=='original' else 97;chart=v.Chart();prob=factory(n)
    data=np.load(OUT/(args.label+'_stationarity_arrays.npz'));p=data['p'];r=data['r'];Z=data['Z'];JZ=data['JZ'];q=p[chart.free]
    assert np.array_equal(p,params(case));indices=[[0,3],[20,21]][args.batch]
    path=OUT/(args.label+'_step_study'+str(args.batch)+'.json');rows=json.loads(path.read_text()) if path.exists() else []
    for i in indices:
        direction=Z[:,i];norm=np.linalg.norm(direction)
        for step in [.004,.002,.001,.0005,.00025]:
            if any(row['direction']==i and row['physical_step']==step for row in rows):continue
            h=step/norm;vv=[];ratios=[]
            for k in [2,1,-1,-2]:
                pp=chart.lift(q+k*h*direction[chart.free]);vv.append(prob.fun(pp));ratios.append(float(np.linalg.norm(pp-p)/(abs(k)*step)))
            fd=(-vv[0]+8*vv[1]-8*vv[2]+vv[3])/(12*h)
            rows.append({'direction':i,'physical_step':step,'coordinate_step':h,'linear_physical_step':float(h*norm),
                         'actual_to_linear_physical_step_ratios':ratios,'relative_J_error':float(np.linalg.norm(fd-JZ[:,i])/np.linalg.norm(JZ[:,i])),
                         'FD_gradient_over_rnorm':float(fd@r/np.linalg.norm(r)),'hybrid_gradient_over_rnorm':float(JZ[:,i]@r/np.linalg.norm(r))})
            save(path.name,rows)
    print('Step study',args.label,indices)

def validate_batch(args):
    case=load(args.label);n=49 if args.label=='original' else 97;prob=factory(n);chart=v.Chart();group=4 if n==49 else 2
    data=np.load(OUT/(args.label+'_stationarity_arrays.npz'));p=data['p'];r=data['r'];Z=data['Z'];JZ=data['JZ'];q=p[chart.free]
    assert a.fingerprint(case)==load(args.label+'_stationarity_setup')['fingerprint'] and np.array_equal(p,params(case))
    tag='' if args.fd_scale==1 else '_scale'+str(args.fd_scale);path=OUT/(args.label+'_FD'+tag+'_batch'+str(args.batch)+'.json')
    rows=json.loads(path.read_text()) if path.exists() else []
    for i in range(group*args.batch,min(22,group*(args.batch+1))):
        if any(row['direction']==i for row in rows):continue
        direction=Z[:,i];norm=np.linalg.norm(direction);dots=[];errors=[]
        for step in [args.fd_scale*.001,args.fd_scale*.0005]:
            h=step/norm;rr=[prob.fun(chart.lift(q+k*h*direction[chart.free])) for k in [2,1,-1,-2]]
            fd=(-rr[0]+8*rr[1]-8*rr[2]+rr[3])/(12*h);errors.append(float(np.linalg.norm(fd-JZ[:,i])/np.linalg.norm(JZ[:,i])));dots.append(float(fd@r))
        rows.append({'direction':i,'relative_jacobian_errors':errors,'FD_gradient':dots});save(path.name,rows)
    print('Independent feasible FD',args.label,'batch',args.batch,'directions',len(rows))

def validate_finish(args):
    case=load(args.label);n=49 if args.label=='original' else 97;chart=v.Chart();prob=factory(n)
    data=np.load(OUT/(args.label+'_stationarity_arrays.npz'));p=data['p'];r=data['r'];Z=data['Z'];JZ=data['JZ']
    assert np.array_equal(p,params(case)) and a.fingerprint(case)==load(args.label+'_stationarity_setup')['fingerprint']
    tag='' if args.fd_scale==1 else '_scale'+str(args.fd_scale);rows=[]
    for b in range(6 if n==49 else 11):rows+=load(args.label+'_FD'+tag+'_batch'+str(b))
    rows.sort(key=lambda row:row['direction']);assert [row['direction'] for row in rows]==list(range(22))
    fd=np.array([row['FD_gradient'] for row in rows]);ratios=np.linalg.norm(fd,axis=0)/np.linalg.norm(r)
    setup=load(args.label+'_stationarity_setup');local=load(args.label+'_local');C,G=constraint(p,True)
    orth=float(np.linalg.norm(JZ.T@JZ-np.eye(22)));tangent=float(np.linalg.norm(G@Z))
    correction=-Z@(JZ.T@r);probes=[]
    for factor in [1.,.5,.1,.01,.001,-.001]:
        try:
            pp=chart.lift(p[chart.free]+factor*correction[chart.free]);rr=prob.fun(pp)
            pred=float((r@r-(r-factor*JZ@(JZ.T@r))@(r-factor*JZ@(JZ.T@r)))/2)
            probes.append({'factor':factor,'predicted_reduction':pred,'actual_reduction':float((r@r-rr@rr)/2),'C':constraint(pp).tolist()})
        except ValueError as exc:probes.append({'factor':factor,'refused':str(exc)})
    jets=v.jet_report(case);passed=setup['hybrid_relative']<=1e-5 and max(ratios)<=1e-5 and max(abs(float(x)) for x in jets['high_precision']['constraints'])<1e-10 and local['bounds_strict']
    B,mr,ff,D=v.metric(prob,p)
    def uncertainty(dp):return {'delta_cl':float(dp[0]),'delta_a0':float(D['f'][0]@dp),'physical_field_linear_norm':float(np.linalg.norm(B@dp)),'parameter_norm':float(np.linalg.norm(dp))}
    save(args.label+'_stationarity'+tag+'.json',{'near_stationary':bool(passed),'hybrid_relative':setup['hybrid_relative'],'FD_relative':ratios.tolist(),
         'physical_FD_steps':[args.fd_scale*.001,args.fd_scale*.0005],'max_directional_J_error':max(max(row['relative_jacobian_errors']) for row in rows),
         'residual_whitening_orthogonality_error':orth,'linear_tangent_constraint_error':tangent,
         'step_normalization':'coordinate h=physical_length/norm(Z[:,i]); Z=field_tangent @ residual_right_vectors / residual_singular_values',
         'GN_predicted_decrease':float(np.linalg.norm(JZ.T@r)**2/2),'GN_correction_marker':uncertainty(correction),
         'FD_GN_markers':[uncertainty(-Z@fd[:,k]) for k in [0,1]],'GN_probes':probes,'jet':jets,'physical_vector_sha256':a.fingerprint(case)})
    print(json.dumps({'case':args.label,'passed':bool(passed),'hybrid':setup['hybrid_relative'],'FD':ratios.tolist()}))

def baseline_finish(args):
    original=load('original');main=load('original_main_diagnostics');bands=load('original_bands_diagnostics')
    for part,rows in [('main',main),('bands',bands)]:
        previous=load('prior_final_'+part+'_diagnostics')
        assert all(rows[name]==value for name,value in previous.items())
    st=load('original_stationarity_scale4');assert st['near_stationary']
    old=load('prior_final_stationarity_scale4')
    assert abs(st['hybrid_relative']-old['hybrid_relative'])<1e-10 and max(abs(np.array(st['FD_relative'])-old['FD_relative']))<1e-8
    save('baseline_ready.json',{'all_historical_residual_diagnostics_bitwise':True,'gradient_reproduced':True,'quadratic_precision_verified':True,
          'physical_vector_sha256':a.fingerprint(original),'independent_inverse_checks_repeated':bool(load('original_independent'))})
    print('Complete Stage IX baseline reproduction verified before refinement fitting')

def fourth(p,jac=False):
    cl=p[0];c=v.coefficients(p);M=v.jet.matrices(cl);values=M@c
    aa,b,cy,d,ee,g,h,u,vv,w,z,k=values
    out=np.array([4*(2*cl-1)*d+b*u+5*aa*w,4*cl*ee-5*b*vv+9*cy*u+3*aa*z,4*g+3*cy*vv+aa*k])
    if not jac:return out
    strain=v.strain(cl);D=M[:,1:]-M[:,:1]*strain[None,1:]/strain[0]
    G=np.vstack([4*(2*cl-1)*D[3]+u*D[1]+b*D[7]+5*w*D[0]+5*aa*D[9],
                 4*cl*D[4]-5*vv*D[1]-5*b*D[8]+9*u*D[2]+9*cy*D[7]+3*z*D[0]+3*aa*D[10],
                 4*D[5]+3*vv*D[2]+3*cy*D[8]+k*D[0]+aa*D[11]])
    zz=cl+1e-25j;MM=v.jet.matrices(zz);ss=MM[6];cc=np.r_[(1-zz-ss[1:20]@p[1:20]-ss[20:]@p[20:])/ss[0],p[1:]]
    av,bv,cv,dv,ev,gv,hv,uv,vv,wv,zv,kv=MM@cc
    gc=np.imag([4*(2*zz-1)*dv+bv*uv+5*av*wv,4*zz*ev-5*bv*vv+9*cv*uv+3*av*zv,4*gv+3*cv*vv+av*kv])/1e-25
    return out,np.column_stack([gc,G])

def fourth_analysis(args):
    if args.label=='final':
        st=load('final_stationarity_scale4');assert st['near_stationary'] and st['physical_vector_sha256']==a.fingerprint(load('final'))
    case=load(args.label);p=params(case);prob=factory(97);chart=v.Chart();B,mr,ff,D=v.metric(prob,p);C,G=constraint(p,True);C4,G4=fourth(p,True)
    R=np.zeros((24,22));R[chart.free]=np.eye(22);R[chart.z]=-np.linalg.solve(G[:,chart.z],G[:,chart.free])
    _,sb,Vb=np.linalg.svd(B@R,full_matrices=False);T=R@(Vb.T/sb)
    raw=G4@R;field=G4@T;row_scale=1/np.maximum(1.,np.linalg.norm(raw,axis=1))
    spectra={};directions={}
    for name,M in [('raw_chart',raw),('row_scaled_chart',row_scale[:,None]*raw),('physical_field',field),('row_scaled_physical_field',row_scale[:,None]*field)]:
        U,sv,Vt=np.linalg.svd(M,full_matrices=False);spectra[name]={'singular_values':sv.tolist(),'condition':float(sv[0]/sv[-1]),'rank':int(sum(sv>sv[0]*1e-10)),
                    'left_vectors':U.tolist(),'right_vectors':Vt.tolist()}
    correction=T@np.linalg.lstsq(field,-C4,rcond=None)[0]
    for i in range(3):
        target=np.eye(3)[i];dp=T@np.linalg.lstsq(field,target,rcond=None)[0]
        directions[str(i+1)]={'physical_norm':float(np.linalg.norm(B@dp)),'parameters':dp.tolist(),'C2_change':(G@dp).tolist(),'C4_change':(G4@dp).tolist(),
                            'delta_cl':float(dp[0]),'delta_a0':float(D['f'][0]@dp)}
    checks=[];rng=np.random.default_rng(10404);q=p[chart.free]
    for i in range(4):
        dq=rng.normal(size=22);dq/=np.linalg.norm(R@dq)
        for h in [.001,.0005]:
            vv=[fourth(chart.lift(q+k*h*dq)) for k in [2,1,-1,-2]];fd=(-vv[0]+8*vv[1]-8*vv[2]+vv[3])/(12*h)
            checks.append({'direction':i,'step':h,'relative_error':float(np.linalg.norm(fd-raw@dq)/np.linalg.norm(raw@dq))})
    save(args.label+'_fourth_derivative_attempt.json',{'fingerprint':a.fingerprint(case),'checks':checks})
    assert max(x['relative_error'] for x in checks)<1e-7
    predicted=p+correction
    result={'physical_vector_sha256':a.fingerprint(case),'fourth':C4.tolist(),'row_scale':row_scale.tolist(),'row_scaling':'inverse max(1, raw chart row Euclidean norm), frozen at evaluation profile',
         'spectra':spectra,'full_DC4':G4.tolist(),'constraint_tangent_chart':R.tolist(),'independent_feasible_derivative_checks':checks,'adjustment_directions':directions,
         'linearized_correction':correction.tolist(),'predicted_field_norm':float(np.linalg.norm(B@correction)),'predicted_delta_cl':float(correction[0]),
         'predicted_delta_a0':float(D['f'][0]@correction),'linear_trial_box_feasible':bool(np.all(predicted>=LOW) and np.all(predicted<=HIGH)),
         'pair_condition':float(np.linalg.cond(G[:,chart.z])),'linearized_remaining_C4':(C4+G4@correction).tolist()}
    result['physical_field_tangent']=T.tolist()
    u4,s4,vt4=np.linalg.svd(field,full_matrices=False);physical_weak=[]
    for i in range(3):
        dp=T@vt4[i]
        physical_weak.append({'sigma':float(s4[i]),'parameters':dp.tolist(),
            'delta_cl':float(dp[0]),'delta_a0':float(D['f'][0]@dp),'C4_response':(G4@dp).tolist(),
            'physical_norm':float(np.linalg.norm(B@dp))})
    result['physical_singular_directions']=physical_weak
    critical=[]
    for i,item in enumerate(physical_weak):
        dp=np.array(item['parameters']);expected=G4@dp
        for physical_step in [.001,.0005]:
            hh=physical_step/np.linalg.norm(dp)
            vals=[fourth(chart.lift(q+factor*hh*dp[chart.free])) for factor in [2,1,-1,-2]]
            fd=(-vals[0]+8*vals[1]-8*vals[2]+vals[3])/(12*hh)
            critical.append({'singular_direction':i+1,'physical_parameter_step':physical_step,
                'relative_error':float(np.linalg.norm(fd-expected)/np.linalg.norm(expected)),
                'expected_C4_derivative':expected.tolist(),'FD_C4_derivative':fd.tolist()})
    result['critical_singular_direction_checks']=critical
    save(args.label+'_fourth_critical_derivative_attempt.json',result)
    assert max(row['relative_error'] for row in critical)<1e-5
    # Compare physical adjustment directions against the main PDE's weak physical vectors.
    local=load(args.label+'_local');weak=local['weak_directions']
    for value in directions.values():
        dp=np.array(value['parameters']);value['weak_field_cosines']=[float(abs((B@dp)@(B@np.array(w['p'])))/(np.linalg.norm(B@dp)*np.linalg.norm(B@np.array(w['p'])))) for w in weak]
    save(args.label+'_fourth_analysis.json',result)
    print(json.dumps({'profile':args.label,'physical_singular_values':spectra['physical_field']['singular_values'],'linear_field_correction':result['predicted_field_norm']}))

def five_feasible(args):
    st=load('final_stationarity_scale4');base=load('final');assert st['near_stationary'] and st['physical_vector_sha256']==a.fingerprint(base)
    analysis=load('final_fourth_analysis');assert analysis['spectra']['physical_field']['rank']==3 and analysis['linear_trial_box_feasible'] and analysis['predicted_field_norm']<.01
    prob=factory(97);p0=params(base);chart=v.Chart();B,mr,ff,D=v.metric(prob,p0)
    p=params(load('five_checkpoint')) if (OUT/'five_checkpoint.json').exists() else p0.copy();q=p[chart.free];history=load('five_feasibility_path') if (OUT/'five_feasibility_path.json').exists() else [];began=time.monotonic()
    for iteration in range(18):
        p,R=chart.lift(q,True);C4,G4=fourth(p,True);hist={'iteration':iteration,'C4':C4.tolist(),'C2':constraint(p).tolist(),'p':p.tolist()};history.append(hist)
        case=make(p,prob,'five');save('five_checkpoint.json',case);save('five_feasibility_path.json',history)
        if max(abs(C4))<5e-11:break
        _,sb,Vb=np.linalg.svd(B@R,full_matrices=False);T=R@(Vb.T/sb);dp=T@np.linalg.lstsq(G4@T,-C4,rcond=None)[0]
        for fraction in [1.,.5,.25,.125,.0625,.03125,.015625]:
            try:trial=chart.lift(q+fraction*dp[chart.free])
            except ValueError:continue
            if np.linalg.norm(fourth(trial))<np.linalg.norm(C4):q=trial[chart.free];break
        else:save('five_failure.json',{'reason':'no decreasing box-feasible chart step','path':history});print('Five-condition local search unresolved');return
        if time.monotonic()-began>8:
            save('five_checkpoint.json',make(chart.lift(q),prob,'five'));save('five_resume.json',{'q':q.tolist(),'path':history});print('Feasibility checkpoint');return
    p=chart.lift(q);case=make(p,prob,'five');j=v.jet_report(case);hp=j['high_precision'];maxhp=max(abs(float(x)) for x in hp['constraints']+hp['fourth'])
    result={'success':maxhp<1e-10,'independent_high_precision_max_five_defects':maxhp,'jet':j,'path':history,
        'physical_field_distance_from_refined':v.field_distance(case,base,mr),'cl_change':case['cl']-base['cl'],'a0_change':case['a0']-base['a0'],
        'PDE_objective_not_optimized':True,'physical_vector_sha256':a.fingerprint(case)}
    save('five.json',case);save('five_feasibility.json',result);print(json.dumps({k:val for k,val in result.items() if k not in ['path','jet']}))

def near_origin(args):
    records={}
    for label in ['original','final']+(['five'] if (OUT/'five.json').exists() else []):
        case=load(label);jets=v.jet_report(case);C=np.array(jets['constraints']);D=np.array(jets['fourth']);rows=[]
        for radius in [.08,.04,.02,.01,.005]:
            for theta in [0.,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2]:
                x,y=radius*np.cos(theta),radius*np.sin(theta);f=s.fields(case,[x],[y]);rf=(case['cl']*x-f['psiy'][0])*f['fx'][0]+(case['cl']*y+f['psix'][0])*f['fy'][0]+(case['cl']-1+f['ratio'][0])*f['f'][0]
                quad=C[0]*x*x+C[1]*y*y;four=D[0]*x**4+D[1]*x*x*y*y+D[2]*y**4;pred=quad+four
                rows.append({'radius':radius,'theta':float(theta),'Rf_engine':float(rf),'quadratic_prediction':float(quad),'fourth_prediction':float(four),
                             'full_prediction':float(pred),'absolute_difference':float(abs(rf-pred)),'difference_over_r6':float((rf-pred)/radius**6)})
        records[label]={'physical_vector_sha256':a.fingerprint(case),'rows':rows,'warning':'At smallest radii, engine rounding and cancellation can dominate r^6 differences; raw coefficients are not normalized residual percentages.'}
    save('near_origin_Taylor_validation.json',records);print('Near-origin physical residual versus Taylor scaling retained')


def overlap_audit(args):
    coords=load('assessment_grids');radial=np.sort(np.r_[np.geomspace(.08,8.,96),np.geomspace(8.,64.,97)]);angular=np.linspace(0,np.pi/2,97);rows={}
    for name,row in coords.items():
        x=np.array(row['x']);y=np.array(row['y']);r=np.hypot(x,y);th=np.arctan2(y,x)
        near_angle=np.min(abs(th[:,None]-angular[None,:]),axis=1)<1e-12
        index=np.clip(np.searchsorted(radial,r),1,len(radial)-1);near_radial=np.minimum(abs(radial[index]-r),abs(radial[index-1]-r))<1e-12*np.maximum(1,r)
        count=int(sum((near_angle&near_radial)|(r==0)))
        label='independent shifted validation' if name.startswith('independent_shifted_') else ('true outside holdout' if name.startswith('true_H') else ('historical training-overlap diagnostic' if count else 'historical matched diagnostic; coverage may overlap fitted radial band'))
        rows[name]={'geometric_fitting_node_overlap_count':count,'label':label,'coordinate_sha256':load('grid_design')[name]['coordinate_sha256']}
    assert rows['inner_validation97']['geometric_fitting_node_overlap_count']==9409
    for name in ['independent_shifted_inner','independent_shifted_far']:assert rows[name]['geometric_fitting_node_overlap_count']==0
    save('assessment_overlap_audit.json',rows);print('Historical interior97 training overlap and shifted-grid independence verified')

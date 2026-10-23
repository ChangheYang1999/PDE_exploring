"""Exact quadratic Taylor constraints, unchanged Stage VIII PDE residual."""
from ipm_portable import output_dir, peak_rss_mib
import argparse,json,time,resource,signal,math,itertools
from pathlib import Path
from functools import lru_cache
import numpy as np
import psutil
from scipy.linalg import null_space
from threadpoolctl import threadpool_limits,threadpool_info
import stage8 as a
import taylor_jet as jet
ROOT=Path(__file__).resolve().parent;OUT = output_dir();save=a.save
LOW=a.t.LOW;HIGH=a.t.HIGH
CL_STEP=2.5e-5

def load(name):
    path=ROOT/'inputs'/(name+'.json')
    return json.loads(path.read_text()) if path.exists() else a.load(name)
def params(case):return a.parameters(case)
def make(p,prob,label):
    d=a.case_at(p,prob,label=label);d['jacobian_cl_relative_step']=CL_STEP
    return d

@lru_cache(maxsize=128)
def strain(cl):
    items=a.s.basis(cl,3,5,'fractional3')
    return np.array([a.e.evaluate(b['ratio'],[0],[0])[0] for b in items])

def coefficients(p):
    s=strain(p[0]);return np.r_[(1-p[0]-s[1:20]@p[1:20]-s[20:]@p[20:])/s[0],p[1:]]

def constraint(p,jac=False):
    cl=p[0];c=coefficients(p);M=jet.matrices(cl);v=M@c
    aa,b,cy,d,e,g,h,u,vv,w,z,k=v
    C=np.array([2*(2*cl-1)*b+3*aa*u,2*cy+aa*vv])
    if not jac:return C
    s=strain(cl);D=M[:,1:]-M[:,:1]*s[None,1:]/s[0]
    G=np.vstack([2*(2*cl-1)*D[1]+3*u*D[0]+3*aa*D[7],2*D[2]+vv*D[0]+aa*D[8]])
    # Analytic complex-step of the independent series and underlying center formula.
    zz=cl+1e-25j;MM=jet.matrices(zz);ss=MM[6]
    cc=np.r_[(1-zz-ss[1:20]@p[1:20]-ss[20:]@p[20:])/ss[0],p[1:]]
    aa,bb,ccy,_,_,_,_,uu,vvv,*_=MM@cc
    gc=np.imag([2*(2*zz-1)*bb+3*aa*uu,2*ccy+aa*vvv])/1e-25
    return C,np.column_stack([gc,G])

def metric(prob,p):
    theta=np.r_[0,1e-6,.001,(np.arange(17)+.37)*np.pi/34,np.pi/2-.001,np.pi/2-1e-6,np.pi/2]
    x,y=a.s.polar(np.geomspace(.035,8,17),theta);x,y=np.r_[0.,x],np.r_[0.,y]
    ff,D=a.field_design(prob,p,x,y);rad=1+np.hypot(x,y);scale=max(1,abs(ff['f'][0]))*np.sqrt(3*len(x))
    B=np.vstack([D['f'],D['psix']/rad[:,None],D['psiy']/rad[:,None]])/scale
    return B,(x,y,scale),ff,D

def field_distance(case,original,metric_record):
    x,y,scale=metric_record;scale=max(1,abs(original['a0']))*np.sqrt(3*len(x));f=a.s.fields(case,x,y);g=a.s.fields(original,x,y);rad=1+np.hypot(x,y)
    return float(np.linalg.norm(np.r_[f['f']-g['f'],(f['psix']-g['psix'])/rad,(f['psiy']-g['psiy'])/rad])/scale)

def jet_report(case):
    j,C,F,P=jet.values(case['cl'],case['coefficients']);hp=jet.high_precision(case['cl'],case['coefficients'])
    return {'jets':{k:float(v) for k,v in j.items()},'constraints':C.tolist(),'fourth':F.tolist(),'poisson':P.tolist(),
            'center':float(case['cl']+j['h']-1),'high_precision':hp,
            'scaled_constraints':[float(C[0]/max(1,abs(2*(2*case['cl']-1)*j['b']),abs(3*j['a']*j['u']))),float(C[1]/max(1,abs(2*j['c']),abs(j['a']*j['v'])))],
            'float_vs_high_precision_constraints':(C-np.array(list(map(float,hp['constraints'])))).tolist()}

def verify(args):
    base=load('original');p=params(base);C,G=constraint(p,True);r=jet_report(base)
    old=load('S0_24_independent_checks')['taylor']
    assert max(abs(C-[old['Rf_x2'],old['Rf_y2']]))<1e-8
    errors=[]
    for step in (1e-3,5e-4):
        fd=[]
        for i in range(24):
            h=step*max(1,abs(p[i]));vv=[]
            for k in (2,1,-1,-2):q=p.copy();q[i]+=k*h;vv.append(constraint(q))
            fd.append((-vv[0]+8*vv[1]-8*vv[2]+vv[3])/(12*h))
        fd=np.array(fd).T;errors.append({'relative_step':step,'relative_frobenius':float(np.linalg.norm(fd-G)/np.linalg.norm(G)),
                                       'max_absolute':float(max(abs(fd-G).ravel()))})
    assert max(abs(np.array(list(map(float,r['high_precision']['poisson'])))))<1e-55
    assert max(abs(np.array(r['float_vs_high_precision_constraints'])))<1e-9
    save('jet_verification.json',{'original':r,'existing_engine_constraints':[old['Rf_x2'],old['Rf_y2']],
                                'constraint_Jacobian':G.tolist(),'derivative_checks':errors})
    print(json.dumps({'C':C.tolist(),'derivatives':errors,'high_precision':r['high_precision']['constraints']}))

def geometry(args):
    if (OUT/'chart.json').exists():
        print('Existing feasible chart preserved; geometry not recreated');return
    prob=a.JointProblem(.1);base=load('original');p=params(base);B,mr,ff,D=metric(prob,p);C,G=constraint(p,True)
    _,sb,vb=np.linalg.svd(B,full_matrices=False);F=vb.T/sb
    sv=np.linalg.svd(G@F,compute_uv=False);correction=F@np.linalg.lstsq(G@F,-C,rcond=None)[0]
    # Physical minimum-norm Newton correction with exact box and monotone feasibility.
    q=p.copy();path=[]
    for it in range(12):
        c,g=constraint(q,True);path.append({'iteration':it,'C':c.tolist(),'p':q.tolist()})
        if max(abs(c))<2e-12:break
        dp=F@np.linalg.lstsq(g@F,-c,rcond=None)[0]
        for fraction in [1.,.5,.25,.125,.0625,.03125,.015625]:
            trial=q+fraction*dp
            if np.all(trial>=LOW) and np.all(trial<=HIGH) and np.linalg.norm(constraint(trial))<np.linalg.norm(c):q=trial;break
        else:raise RuntimeError('No feasible local Newton correction')
    assert max(abs(constraint(q)))<1e-10
    feasible=make(q,prob,'feasible');save('feasible.json',feasible)
    # Choose only by two-column constraint conditioning and feasible local geometry.
    _,gg=constraint(q,True);pairs=[]
    for pair in itertools.combinations(range(1,24),2):
        z=gg[:,pair];norm=np.linalg.norm(z,axis=0);zz=z/norm
        ss=np.linalg.svd(zz,compute_uv=False)
        if ss[-1]<1e-5:continue
        # Unit-field cost of individually moving the two selected coefficients.
        amplification=float(np.linalg.norm(B[:,pair]@np.linalg.inv(z),2))
        pairs.append({'pair':pair,'column_condition':float(ss[0]/ss[-1]),'raw_condition':float(np.linalg.cond(z)),
                      'field_amplification':amplification,'score':float(ss[0]/ss[-1])*amplification})
    pairs.sort(key=lambda z:z['score']);chosen=pairs[0]['pair']
    save('constraint_geometry.json',{'original_raw_singular_values':np.linalg.svd(G,compute_uv=False).tolist(),
         'original_field_singular_values':sv.tolist(),'rank':2,'physical_metric_singular_values':sb.tolist(),
         'linear_minimum_field_correction':correction.tolist(),'newton_path':path,'pair_ranking':pairs,
         'chosen_pair':chosen,'feasible_jet':jet_report(feasible),'physical_field_distance':field_distance(feasible,base,mr),
         'cl_change':q[0]-p[0],'a0_change':feasible['a0']-base['a0']})
    save('chart.json',{'pair':chosen,'free':[i for i in range(24) if i not in chosen], 'anchor':q.tolist(),
                       'max_pair_condition':1e5,'branch_radius':20.,'constraint_abs_tolerance':1e-10})
    print(json.dumps({'pair':chosen,'field_sv':sv.tolist(),'C':constraint(q).tolist(),'field_distance':field_distance(feasible,base,mr)}))

class Chart:
    def __init__(self,record=None):
        self.record=record or load('chart');self.z=np.array(self.record['pair']);self.free=np.array(self.record['free']);self.anchor=np.array(self.record['anchor'])
    def lift(self,q,derivative=False):
        p=self.anchor.copy();p[self.free]=q
        if np.any(p<LOW) or np.any(p>HIGH):raise ValueError('free variable outside physical box')
        for i in range(14):
            C,G=constraint(p,True);gz=G[:,self.z]
            if np.linalg.cond(gz)>self.record['max_pair_condition']:raise ValueError('implicit pair lost invertibility')
            if max(abs(C))<2e-12:break
            dz=np.linalg.solve(gz,-C)
            for frac in [1.,.5,.25,.125,.0625,.03125]:
                pp=p.copy();pp[self.z]+=frac*dz
                if np.all(pp>=LOW) and np.all(pp<=HIGH) and np.linalg.norm(constraint(pp))<np.linalg.norm(C):p=pp;break
            else:raise ValueError('implicit solve loses local feasibility')
        if max(abs(constraint(p)))>self.record['constraint_abs_tolerance']:raise ValueError('constraint solve inaccurate')
        if max(abs(p[self.z]-self.anchor[self.z]))>self.record['branch_radius']:raise ValueError('implicit branch radius exceeded')
        if not derivative:return p
        C,G=constraint(p,True);T=np.zeros((24,22));T[self.free]=np.eye(22);T[self.z]=-np.linalg.solve(G[:,self.z],G[:,self.free])
        return p,T


def chartcheck(args):
    if (OUT/'fit_map.json').exists():
        assert (OUT/'implicit_derivative_verification.json').exists()
        print('Existing frozen reduced map preserved');return
    prob=a.JointProblem(.1);chart=Chart();case=load('feasible');p=params(case);q=p[chart.free]
    p,T=chart.lift(q,True);r=prob.fun(p);J=a.hybrid_jac(prob,p,cl_step=CL_STEP);Jq=J@T
    rng=np.random.default_rng(90210);errors=[]
    for i in range(4):
        dq=rng.normal(size=22);dq/=np.linalg.norm(T@dq)
        for h in (.00025,.000125):
            vv=[prob.fun(chart.lift(q+k*h*dq)) for k in (2,1,-1,-2)]
            fd=(-vv[0]+8*vv[1]-8*vv[2]+vv[3])/(12*h)
            errors.append({'direction':i,'step':h,'relative_error':float(np.linalg.norm(fd-Jq@dq)/np.linalg.norm(fd))})
    save('implicit_derivative_attempt.json',{'checks':errors})
    assert max(v['relative_error'] for v in errors)<1e-5
    save('implicit_derivative_verification.json',{'checks':errors,'tangent_constraint_error':float(np.linalg.norm(constraint(p,True)[1]@T)),
          'pair_condition':float(np.linalg.cond(constraint(p,True)[1][:,chart.z])),'constraints':constraint(p).tolist()})
    D=1/np.linalg.norm(Jq,axis=0)
    save('fit_map.json',{'anchor':q.tolist(),'column_scale':D.tolist(),'chart':chart.record,'fixed':True,'setup_residual_calls':5})
    prob.fun(p)
    print(json.dumps({'max_error':max(v['relative_error'] for v in errors),'objectives':prob.objectives()}))

class CheckpointStop(Exception):pass

def fit(args):
    if (OUT/'final.json').exists():
        for name in ['final_stationarity','final_stationarity_scale4']:
            if not (OUT/(name+'.json')).exists():continue
            record=load(name)
            if record.get('near_stationary') and record.get('physical_vector_sha256')==a.fingerprint(load('final')):
                print('Independently checked candidate preserved; no optimization');return
    from scipy.optimize import least_squares
    assert (OUT/'implicit_derivative_verification.json').exists()
    prob=a.JointProblem(.1);mapping=load('fit_map');chart=Chart(mapping['chart'])
    anchor=np.array(mapping['anchor']);D=np.array(mapping['column_scale'])
    old=load('final') if (OUT/'final.json').exists() else load('feasible')
    p=params(old);q0=(p[chart.free]-anchor)/D
    calls=old.get('fit_residual_calls',0);jc=old.get('fit_jacobian_calls',0);local=0
    journals={name:[] for name in ['fit_evaluations','accepted_vectors','trajectory','trials']}
    def journal(name,row):journals[name].append(row)
    def flush():
        for name,rows in journals.items():
            if rows:
                with (OUT/(name+'.jsonl')).open('a') as f:f.write(''.join(json.dumps(r)+'\n' for r in rows))
                rows.clear()
    state={'p':p.copy(),'r':None,'objectives':None};began=time.monotonic();deadline=began+8.
    def checkpoint():
        flush()
        case=make(state['p'],prob,'final');case.update(fit_residual_calls=calls,fit_jacobian_calls=jc,
                reduced_frozen_map=mapping,stop_reason=state.get('reason','software checkpoint'))
        if state['objectives'] is not None:case['objectives']=state['objectives']
        save('final.json',case)
    def stopping(signum,frame):
        state['reason']='hardware supervisor signal';checkpoint();raise CheckpointStop()
    signal.signal(signal.SIGTERM,stopping)
    def fun(z):
        nonlocal calls,local
        if time.monotonic()>deadline or calls>=2400:raise CheckpointStop()
        pp=chart.lift(anchor+D*z);rr=prob.fun(pp);calls+=1;local+=1
        journal('fit_evaluations',{'call':calls,'p':pp.tolist(),'cost':float(rr@rr/2),'C':constraint(pp).tolist()})
        return rr
    def jac(z):
        nonlocal jc
        pp,T=chart.lift(anchor+D*z,True);rr=counted_physical(pp,'jacobian_base')
        state.update(p=pp.copy(),r=rr.copy(),objectives=prob.objectives())
        journal('accepted_vectors',{'call':calls,'p':pp.tolist(),'C':constraint(pp).tolist(),'cost':float(rr@rr/2)})
        checkpoint()
        J=a.hybrid_jac(prob,pp,fun=lambda p:counted_physical(p),cl_step=CL_STEP);Jq=J@T
        jc+=1;U,sv,Vt=np.linalg.svd(Jq*D,full_matrices=False)
        row={'actual_calls':calls,'jacobian_calls':jc,'cost':float(rr@rr/2),'p':pp.tolist(),
             'cl':float(pp[0]),'a0':prob.metadata(pp)['a0'],'C':constraint(pp).tolist(),
             'hybrid_relative_projected_residual':float(np.linalg.norm(U.T@rr)/np.linalg.norm(rr)),
             'column_condition':float(sv[0]/sv[-1]),'objectives':state['objectives']}
        journal('trajectory',row)
        checkpoint();return Jq*D
    def counted_physical(pp,kind='full_J_cl_probe'):
        nonlocal calls,local
        if time.monotonic()>deadline or calls>=2400:raise CheckpointStop()
        rr=prob.fun(pp);calls+=1;local+=1
        # These cl probes are unconstrained residual evaluations used for the full Jacobian.
        journal('fit_evaluations',{'call':calls,'p':pp.tolist(),'cost':float(rr@rr/2),'type':kind})
        return rr
    import importlib
    trf=importlib.import_module('scipy.optimize._lsq.trf');previous_update=trf.update_tr_radius
    def update(delta,actual,predicted,stepnorm,boundhit):
        new,ratio=previous_update(delta,actual,predicted,stepnorm,boundhit)
        journal('trials',{'actual_calls':calls,'accepted':bool(actual>0),'actual_reduction':float(actual),'predicted_reduction':float(predicted),'ratio':float(ratio),'radius_before':float(delta),'radius_after':float(new),'bound_hit':bool(boundhit)})
        return new,ratio
    trf.update_tr_radius=update
    try:
        result=least_squares(fun,q0,jac=jac,bounds=((LOW[chart.free]-anchor)/D,(HIGH[chart.free]-anchor)/D),
                             ftol=1e-12,xtol=1e-12,gtol=1e-12,max_nfev=500,method='trf')
        pp=chart.lift(anchor+D*result.x);state['p']=pp;counted_physical(pp,'optimizer_final_confirmation');state['objectives']=prob.objectives();state['reason']=str(result.message)
    except CheckpointStop:state.setdefault('reason','8-second software checkpoint or 2400-call cap')
    except ValueError as exc:state['reason']='feasibility/chart rejection: '+str(exc)
    finally:trf.update_tr_radius=previous_update
    checkpoint()
    save('fit_checkpoint_'+str(calls)+'.json',load('final'))
    print(json.dumps({'calls':calls,'J_calls':jc,'new_calls':local,'reason':state['reason'],'cl':state['p'][0]}))

def algebra(args):
    import algebra_check
    save('algebra_check.json',algebra_check.check());print('Exact rational polynomial expansion passed')

def assess(args):
    a.assess(args)
def cross(args):a.cross(args)
def independent(args):a.independent(args)

def local(args):
    case=load(args.label);prob=a.JointProblem(.1);p=params(case);B,mr,ff,D=metric(prob,p)
    C,G=constraint(p,True);_,sb,vb=np.linalg.svd(B,full_matrices=False);F=vb.T/sb
    sv=np.linalg.svd(G@F,compute_uv=False);N=null_space(G@F);T=F@N
    J=a.hybrid_jac(prob,p,cl_step=CL_STEP);r=prob.fun(p)
    U,sr,Vt=np.linalg.svd(J@T,full_matrices=False);raw=np.linalg.svd(J,compute_uv=False)
    col=np.linalg.svd(J/np.linalg.norm(J,axis=0),compute_uv=False)
    chart=Chart();R=np.zeros((24,22));R[chart.free]=np.eye(22);R[chart.z]=-np.linalg.solve(G[:,chart.z],G[:,chart.free]);jq=J@R
    ccol=np.linalg.svd(jq/np.linalg.norm(jq,axis=0),compute_uv=False)
    target=a.scale_target(case,*mr[:2],ff);rad=1+np.hypot(*mr[:2]);scale=mr[2]
    exact=np.r_[target['f'],target['psix']/rad,target['psiy']/rad]/scale
    scale_dp=np.linalg.lstsq(B,exact,rcond=None)[0]
    weak=[]
    for k in (1,2,3):
        dp=T@Vt[-k];field=B@dp
        weak.append({'rank_from_smallest':k,'p':dp.tolist(),'delta_cl':float(dp[0]),'delta_a0':float(D['f'][0]@dp),
                     'scale_cosine':float(abs(field@exact)/(np.linalg.norm(field)*np.linalg.norm(exact)))})
    g=J.T@r;mu=np.linalg.lstsq((G@F).T,-F.T@g,rcond=None)[0]
    out={'physical_vector_sha256':a.fingerprint(case),'jet':jet_report(case),'constraint_raw_singular_values':np.linalg.svd(G,compute_uv=False).tolist(),
         'constraint_field_singular_values':sv.tolist(),'rank':2,'pair_condition':float(np.linalg.cond(G[:,chart.z])),
         'full_raw_singular_values':raw.tolist(),'full_column_singular_values':col.tolist(),
         'restricted_field_singular_values':sr.tolist(),'restricted_column_singular_values':ccol.tolist(),
         'full_field_singular_values':np.linalg.svd(J@F,compute_uv=False).tolist(),
         'hybrid_relative_projected_residual':float(np.linalg.norm(U.T@r)/np.linalg.norm(r)),
         'predicted_GN_decrease':float(np.linalg.norm(U.T@r)**2/2),'Lagrange_multipliers':mu.tolist(),
         'physical_KKT_inf':float(max(abs(g+G.T@mu))), 'field_KKT_norm':float(np.linalg.norm(F.T@(g+G.T@mu))),
         'full_physical_gradient_inf':float(max(abs(g))),'weak_directions':weak,
         'scale_projection_defect':float(np.linalg.norm(B@scale_dp-exact)/np.linalg.norm(exact)),
         'scale_projected_constraint_change':(G@scale_dp).tolist(),
         'exact_scale_constraint_change':(-2*C).tolist(),
         'physical_field_distance_from_original':field_distance(case,load('original'),mr),
         'bounds_strict':bool(np.all(p>=LOW) and np.all(p<=HIGH)), 'objectives':prob.objectives()}
    save(args.label+'_local.json',out)
    # Reduced Jacobian whitening kept fixed for independent FEASIBLE directional checks.
    Z=T@Vt.T/sr
    np.savez(OUT/(args.label+'_stationarity_arrays.npz'),p=p,r=r,Z=Z,JZ=J@Z,free=chart.free)
    save(args.label+'_stationarity_setup.json',{'fingerprint':a.fingerprint(case),'hybrid_relative':out['hybrid_relative_projected_residual'],
                                            'directions':22,'steps':[.001,.0005]})
    print(json.dumps({'label':args.label,'C':C.tolist(),'gamma':out['hybrid_relative_projected_residual'],'field_condition':sr[0]/sr[-1]}))

def validate_batch(args):
    case=load(args.label);chart=Chart();prob=a.JointProblem(.1)
    data=np.load(OUT/(args.label+'_stationarity_arrays.npz'));p=data['p'];r=data['r'];Z=data['Z'];JZ=data['JZ'];q=p[chart.free]
    assert a.fingerprint(case)==load(args.label+'_stationarity_setup')['fingerprint']
    tag='' if args.fd_scale==1 else '_scale'+str(args.fd_scale)
    path=OUT/(args.label+'_FD'+tag+'_batch'+str(args.batch)+'.json');rows=json.loads(path.read_text()) if path.exists() else []
    for i in range(args.batch*4,min(22,args.batch*4+4)):
        if any(row['direction']==i for row in rows):continue
        dz=Z[:,i];norm=np.linalg.norm(dz);errs=[];dots=[]
        for step in (args.fd_scale*.001,args.fd_scale*.0005):
            h=step/norm;rr=[]
            for k in (2,1,-1,-2):rr.append(prob.fun(chart.lift(q+k*h*dz[chart.free])))
            fd=(-rr[0]+8*rr[1]-8*rr[2]+rr[3])/(12*h)
            errs.append(float(np.linalg.norm(fd-JZ[:,i])/np.linalg.norm(JZ[:,i])));dots.append(float(fd@r))
        rows.append({'direction':i,'relative_jacobian_errors':errs,'FD_gradient':dots})
        save(path.name,rows)
    print('Feasible FD directions',len(rows),args.batch)

def validate_finish(args):
    case=load(args.label);data=np.load(OUT/(args.label+'_stationarity_arrays.npz'));p=data['p'];r=data['r'];Z=data['Z'];JZ=data['JZ']
    assert a.fingerprint(case)==load(args.label+'_stationarity_setup')['fingerprint'] and np.array_equal(p,params(case))
    rows=[]
    tag='' if args.fd_scale==1 else '_scale'+str(args.fd_scale)
    for b in range(6):rows+=load(args.label+'_FD'+tag+'_batch'+str(b))
    assert len(rows)==22
    rows.sort(key=lambda x:x['direction']);fd=np.array([row['FD_gradient'] for row in rows])
    ratios=np.linalg.norm(fd,axis=0)/np.linalg.norm(r);setup=load(args.label+'_stationarity_setup');local=load(args.label+'_local')
    chart=Chart();prob=a.JointProblem(.1);direction=-Z@(JZ.T@r);probes=[]
    for factor in (1.,.5,.1,.01,.001,-.001):
        try:
            pp=chart.lift(p[chart.free]+factor*direction[chart.free]);rr=prob.fun(pp)
            pred=float((r@r-(r+factor*JZ@(-JZ.T@r))@(r+factor*JZ@(-JZ.T@r)))/2)
            probes.append({'factor':factor,'predicted_reduction':pred,'actual_reduction':float((r@r-rr@rr)/2),'C':constraint(pp).tolist()})
        except ValueError as exc:probes.append({'factor':factor,'refused':str(exc)})
    hp=jet_report(case);passed=setup['hybrid_relative']<=1e-5 and max(ratios)<=1e-5 and max(abs(np.array(list(map(float,hp['high_precision']['constraints'])))))<1e-10 and local['bounds_strict']
    save(args.label+'_stationarity'+tag+'.json',{'physical_FD_steps':[args.fd_scale*.001,args.fd_scale*.0005],'hybrid_relative':setup['hybrid_relative'],'FD_relative':ratios.tolist(),'near_stationary':bool(passed),
            'max_relative_directional_J_error':max(max(row['relative_jacobian_errors']) for row in rows),'GN_probes':probes,'jet':hp,'physical_vector_sha256':a.fingerprint(case)})
    print(json.dumps({'passed':bool(passed),'hybrid':setup['hybrid_relative'],'FD':ratios.tolist()}))

def precision(args):
    records={}
    for label in ['original','feasible','final']:
        case=load(label);j=jet_report(case);items=a.s.basis(case['cl'],3,5,'fractional3')
        old={}
        for key,field,nx,ny,factor in [('a','f',0,0,1),('b','f',2,0,2),('c','f',0,2,2),('d','f',4,0,24),('e','f',2,2,4),('g','f',0,4,24),
                                     ('h','ratio',0,0,1),('u','ratio',2,0,6),('v','ratio',0,2,2),('w','ratio',4,0,120),('z','ratio',2,2,12),('k','ratio',0,4,24)]:
            terms=a.e.merged(items,case['coefficients'],field)
            for axis,n in [(0,nx),(1,ny)]:
                for _ in range(n):terms=a.e.derivative(terms,axis)
            old[key]=float(a.e.evaluate(terms,[0.],[0.])[0]/factor)
        hp=[jet.high_precision(case['cl'],case['coefficients'],prec) for prec in [50,70,90]]
        errors={k:old[k]-j['jets'][k] for k in old}
        assert max(abs(x) for x in errors.values())<1e-8
        p=params(case);C,G=constraint(p,True);checks=[]
        rng=np.random.default_rng(90211)
        for i in range(3):
            v=np.eye(24)[0] if i==0 else rng.normal(size=24);v=v/np.linalg.norm(v)
            for h in [.001,.0005]:
                cc=[constraint(p+k*h*v) for k in [2,1,-1,-2]];fd=(-cc[0]+8*cc[1]-8*cc[2]+cc[3])/(12*h)
                checks.append({'direction':i,'step':h,'relative_error':float(np.linalg.norm(fd-G@v)/np.linalg.norm(G@v))})
        records[label]={'physical_vector_sha256':a.fingerprint(case),'engine_symbolic_jets':old,'jet_differences':errors,'high_precision':hp,'constraint_directional_checks':checks}
    save('precision_checks.json',records);print('Independent symbolic jets, 50/70/90-digit precision and nearby constraint derivatives verified')

def fdstudy(args):
    case=load('final');chart=Chart();prob=a.JointProblem(.1)
    data=np.load(OUT/'final_stationarity_arrays.npz');p=data['p'];r=data['r'];Z=data['Z'];JZ=data['JZ'];q=p[chart.free]
    rows=[]
    for i in [0,3,20,21]:
        v=Z[:,i];norm=np.linalg.norm(v)
        for step in [.004,.002,.001,.0005,.00025]:
            h=step/norm;rr=[prob.fun(chart.lift(q+k*h*v[chart.free])) for k in [2,1,-1,-2]]
            fd=(-rr[0]+8*rr[1]-8*rr[2]+rr[3])/(12*h)
            rows.append({'direction':i,'physical_step':step,'relative_J_error':float(np.linalg.norm(fd-JZ[:,i])/np.linalg.norm(JZ[:,i])),
                         'FD_gradient_over_rnorm':float(fd@r/np.linalg.norm(r)),'hybrid_gradient_over_rnorm':float(JZ[:,i]@r/np.linalg.norm(r))})
            save('final_FD_step_study.json',rows)
    print(json.dumps(rows))

def scalecheck(args):
    rows={}
    for label in ['original','feasible','final']:
        case=load(label);prob=a.JointProblem(.1);p=params(case);B,mr,ff,D=metric(prob,p);C,G=constraint(p,True)
        _,sb,vb=np.linalg.svd(B,full_matrices=False);F=vb.T/sb;rad=1+np.hypot(*mr[:2]);scale=mr[2]
        target=a.scale_target(case,*mr[:2],ff);exact=np.r_[target['f'],target['psix']/rad,target['psiy']/rad]/scale
        variants={}
        for name,rowsC in [('full',np.zeros((0,24))),('constraint_tangent',G),('constraint_tangent_with_scale_invariants',np.vstack([G,np.eye(24)[0],D['f'][0]]))]:
            T=F@null_space(rowsC@F) if len(rowsC) else F
            BT=B@T;dp=T@(BT.T@exact)
            variants[name]={'relative_projection_defect':float(np.linalg.norm(B@dp-exact)/np.linalg.norm(exact)),
                    'delta_cl':float(dp[0]),'delta_a0':float(D['f'][0]@dp),'constraint_change':(G@dp).tolist()}
        rows[label]={'physical_vector_sha256':a.fingerprint(case),'exact_scale_constraint_derivative':(-2*C).tolist(),
                     'exact_delta_cl':0.,'exact_delta_a0':0.,'projections':variants,'projection_constraints_are_diagnostic_only':True}
    save('scaling_analysis.json',rows);print(json.dumps(rows))

def verify_final(args):
    case=load('final');j=jet_report(case);hp=j['high_precision'];p=params(case)
    assert max(abs(float(v)) for v in hp['constraints'])<1e-10
    assert abs(float(hp['center']))<1e-10
    assert np.all(p>=LOW) and np.all(p<=HIGH) and abs(float(hp['jets']['a']))>1e-12
    save('independent_final_constraint_recheck.json',{'passed':True,'physical_vector_sha256':a.fingerprint(case),
         'independent_series_only':True,'saved_coefficients_re_solved_or_rounded':False,'jet':j})
    print(json.dumps({'independent_saved_coefficient_check':'passed','C_70_digits':hp['constraints']}))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode');parser.add_argument('--label',default='original');parser.add_argument('--part',default='main');parser.add_argument('--batch',type=int,default=0);parser.add_argument('--fd-scale',type=int,default=1,choices=[1,4])
    args=parser.parse_args()
    try:
        with threadpool_limits(limits=1):globals()[args.mode](args)
    finally:
        use=resource.getrusage(resource.RUSAGE_SELF)
        save(args.mode+'_'+args.label+'_process.json',{'peak_rss_mib':peak_rss_mib(use),'cpu_seconds':use.ru_utime+use.ru_stime,
               'threads_at_exit':psutil.Process().num_threads(),'nice':psutil.Process().nice(),'threadpools':threadpool_info()})
if __name__=='__main__':main()

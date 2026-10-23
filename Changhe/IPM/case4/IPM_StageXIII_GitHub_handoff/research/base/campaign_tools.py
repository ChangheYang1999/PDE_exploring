"""Guarded Stage XII embedding, derivative, screening and performance checks."""
import argparse
import resource
from stage12_model import *
from scipy.sparse.linalg import lsmr


def modes_for(family, level='A'):
    # Identical old core and dimensional budgets for A-family comparisons.
    # Combined hierarchy keeps every previous function with identical labels.
    centers0=[.5+i for i in range(9)]
    locals0=[{'family':'local','m':m,'center':s,'width':.9}
             for m in range(9) for s in centers0]
    # m=3,n=0 is exactly old m=3 offsets(0,1,2) with coefficients
    # (1,-2,1). It is excluded before selecting the enlarged space.
    globals0=[{'family':'global','m':m,'n':n,'sigma':0.}
              for m in range(9) for n in range(9) if (m,n)!=(3,0)]
    globals0.append({'family':'global','m':9,'n':0,'sigma':0.})
    if family=='global':
        return ([{'family':'global','m':m,'n':n,'sigma':0.}
                 for m in range(9) for n in range(18) if (m,n)!=(3,0)]
                +[{'family':'global','m':9,'n':0,'sigma':0.}])
    if family=='local':
        return [{'family':'local','m':m,'center':s,'width':.6}
                for m in range(9) for s in [.25+.5*i for i in range(18)]]
    result=globals0+locals0
    if level in ('B','C'):
        result += [{'family':'global','m':m,'n':n,'sigma':0.}
                   for m in range(15) for n in range(15) if m>=9 or n>=9]
        result += [{'family':'local','m':m,'center':s,'width':.9}
                   for m in range(9,15) for s in centers0]
        result += [{'family':'local','m':m,'center':float(s),'width':.65}
                   for m in range(15) for s in range(1,9)]
    if level=='C':
        result += [{'family':'global','m':m,'n':n,'sigma':0.}
                   for m in range(23) for n in range(23) if m>=15 or n>=15]
        result += [{'family':'local','m':m,'center':s,'width':.9}
                   for m in range(15,23) for s in centers0]
        result += [{'family':'local','m':m,'center':float(s),'width':.65}
                   for m in range(15,23) for s in range(1,9)]
        result += [{'family':'local','m':m,'center':.75+.5*i,'width':.45}
                   for m in range(23) for i in range(16)]
    # The replacement m=9,n=0 is already present when B reaches m=14.
    # Preserve the exact A prefix and append each genuinely new mode once.
    unique=[];seen=set()
    for mode in result:
        key=json.dumps(mode,sort_keys=True)
        if key not in seen:unique.append(mode);seen.add(key)
    return unique


def old_map(prob,p):
    ch=chart(p);t=ch.base_tangent
    j=prob.jacobian(p,np.zeros(len(prob.modes)))[:,:24]@t
    _,s,vt=np.linalg.svd(j,full_matrices=False)
    if len(s)!=19 or min(s)<=0: raise ValueError('old feasible Jacobian lost rank')
    return vt.T/s, s


def preflight(label,workers=1):
    p=initial_parameters(); modes=modes_for('combined')
    prob=SpectralProblem(modes,workers=workers);z=np.zeros(len(modes));native=e.GridProblem(97)
    r=prob.fun(p,z);old=native.fun(p)
    checks={'zero_extra_residual_bitwise':bool(np.array_equal(r,old)),
            'old_HP':hp_report(p)['max_abs']<1e-10,
            'frozen_assessment_design_exists':(ROOT/'inputs/assessment_design.json').exists()}
    # The structural gate is required regardless of the design-file naming.
    designs=list((ROOT/'inputs').glob('*assessment*'))+list((ROOT/'results').glob('*design*'))
    checks['frozen_assessment_design_exists']=bool(designs)
    j=prob.jacobian(p,z);native_j=native.hybrid(p,cl_step=e.v.CL_STEP)
    core_error=float(np.linalg.norm(j[:,:24]-native_j)/np.linalg.norm(native_j))
    checks['old_hybrid_derivative_convention_agreement']=core_error<1e-4
    old_transform,old_sv=old_map(prob,p)
    t=chart(p).base_tangent@old_transform
    scale=1/np.maximum(np.linalg.norm(j[:,24:],axis=0),1e-300)
    rng=np.random.default_rng(120021)
    extra=rng.normal(size=len(modes))*scale*1e-5/np.sqrt(len(modes))
    jr=prob.jacobian(p,extra)
    checks['nonzero_extra_HP_invariance']=hp_report(p)['max_abs']<1e-10
    rows=[]
    # Every original feasible direction plus fixed random coefficient/block
    # directions and cl dependence, independently checked at two step sizes.
    directions=[]
    for i in range(19):
        a=np.zeros(19);a[i]=1;directions.append(('old_'+str(i),a,np.zeros(len(modes))))
    for i in range(8):
        b=rng.normal(size=len(modes));b/=np.linalg.norm(b)
        directions.append(('extra_random_'+str(i),np.zeros(19),b))
    directions.append(('mixed',rng.normal(size=19)/np.sqrt(19),rng.normal(size=len(modes))/np.sqrt(len(modes))))
    for name,a,b in directions:
        dp=t@a;dc=scale*b
        analytic=jr[:,:24]@dp+jr[:,24:]@dc
        physical=np.linalg.norm(dp)
        steps=[min(2e-5,.008/max(physical,1e-300)),min(1e-5,.004/max(physical,1e-300))]
        for h in steps:
            values=[];defects=[]
            ch=chart(p)
            for factor in [2,1,-1,-2]:
                pp=ch.lift_delta(old_transform@(factor*h*a))
                defects.append(hp_report(pp)['max_abs'])
                values.append(prob.fun(pp,extra+factor*h*dc))
            fd=(-values[0]+8*values[1]-8*values[2]+values[3])/(12*h)
            error=float(np.linalg.norm(fd-analytic)/max(np.linalg.norm(analytic),1e-300))
            rows.append({'direction':name,'h':h,'relative_error':error,'max_HP':max(defects)})
    max_error=max(row['relative_error'] for row in rows)
    checks['all_19_old_and_9_extra_mixed_two_step_derivatives']=max_error<1e-3
    checks['all_feasible_stencils']=max(row['max_HP'] for row in rows)<1e-10
    d={'schema':'stage12-preflight-v1','label':label,'passed':all(checks.values()),'checks':checks,
       'objective':objectives(r),'old_native_residual_max_difference':float(np.max(abs(r-old))),
       'core_hybrid_relative_difference':core_error,'derivative_checks':rows,
       'maximum_directional_relative_error':max_error,'old_reduced_singular_values':old_sv.tolist(),
       'modes':modes,'nonzero_test_coefficients':extra.tolist(),'source_sha256':source_identity(),'provenance':provenance()}
    atomic(OUT/(label+'_preflight.json'),d)
    print({'passed':d['passed'],'checks':checks,'max_derivative_error':max_error},flush=True)
    if not d['passed']:raise SystemExit(1)


def benchmark(label,level):
    p=initial_parameters();modes=modes_for('combined',level);rows=[];reference=None
    for workers in [1,8,16]:
        before=resource.getrusage(resource.RUSAGE_CHILDREN);own=resource.getrusage(resource.RUSAGE_SELF)
        began=time.time();prob=SpectralProblem(modes,workers=workers);values=prob.basis(p[0])
        wall=time.time()-began
        after=resource.getrusage(resource.RUSAGE_CHILDREN);end=resource.getrusage(resource.RUSAGE_SELF)
        hashes={key:array_hash(value) for key,value in values.items()}
        difference=0 if reference is None else max(float(np.max(abs(values[k]-reference[k]))) for k in values)
        if reference is None: reference={key:value.copy() for key,value in values.items()}
        rows.append({'workers':workers,'wall_seconds':wall,'basis_seconds':prob.last_basis_seconds,
                     'cpu_seconds':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime+end.ru_utime+end.ru_stime-own.ru_utime-own.ru_stime,
                     'max_abs_difference_from_single':difference,'field_sha256':hashes,
                     'BLAS_threads_per_process':1,'cache_bytes':sum(v.nbytes for v in values.values())*2})
        del prob,values
    selected=min(rows,key=lambda row:row['wall_seconds'])['workers']
    d={'schema':'stage12-parallel-benchmark-v1','label':label,'level':level,'modes':len(modes),
       'rows':rows,'selected_workers':selected,'passed':all(row['max_abs_difference_from_single']==0 for row in rows),
       'source_sha256':source_identity(),'provenance':provenance()}
    atomic(OUT/(label+'_benchmark.json'),d);print(d,flush=True)
    if not d['passed']:raise SystemExit(1)


def screen(label,workers):
    p=initial_parameters();base=e.GridProblem(97).fun(p);ch=chart(p)
    records={}
    for family in ['global','local','combined']:
        modes=modes_for(family);prob=SpectralProblem(modes,workers=workers)
        j=prob.jacobian(p,np.zeros(len(modes)));a=j[:,:24]@ch.base_tangent
        q,ra=np.linalg.qr(a,mode='reduced');v=j[:,24:]
        perpendicular=v-q@(q.T@v);rn=base-q@(q.T@base)
        norms=np.linalg.norm(v,axis=0);novel=np.linalg.norm(perpendicular,axis=0)
        scale=1/np.maximum(norms,1e-300)
        projected=perpendicular*scale
        sv=np.linalg.svd(projected,compute_uv=False)
        solution=lsmr(projected,-rn,damp=1e-4,atol=1e-11,btol=1e-10,maxiter=4*len(modes))
        response=projected@solution[0]
        predicted=float((-rn@response-response@response/2))
        predictions=(base@perpendicular)**2/(2*np.maximum(novel**2,1e-300))
        fields=prob.basis(p[0]);radius=np.hypot(prob.x,prob.y)
        physical=np.sqrt(np.mean(fields['f']**2+fields['psix']**2/(1+radius[:,None])**2+fields['psiy']**2/(1+radius[:,None])**2,axis=0))
        records[family]={'modes':modes,'new_modes':len(modes),'independent_parameters':24+len(modes),
            'feasible_variables':19+len(modes),'novelty_fraction':(novel/np.maximum(norms,1e-300)).tolist(),
            'individual_predicted_decrease':predictions.tolist(),'physical_field_column_RMS':physical.tolist(),
            'projected_scaled_singular_values':sv.tolist(),'projected_numerical_rank':int(np.sum(sv>sv[0]*max(projected.shape)*np.finfo(float).eps)),
            'joint_regularized_linear_prediction':predicted,'prediction_damping':1e-4,'LSMR_iterations':int(solution[2]),
            'maximum_individual_prediction':float(max(predictions)),'basis_seconds':prob.last_basis_seconds}
        atomic(OUT/(label+'_screening.json'),{'schema':'stage12-screening-v1','baseline_objective':objectives(base),
            'families':records,'holdout_values_used_for_selection':False,'all_columns_retained':True,
            'source_sha256':source_identity(),'provenance':provenance()})
        print({'family':family,'dimension':19+len(modes),'joint_predicted_decrease':predicted,'rank':records[family]['projected_numerical_rank']},flush=True)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['preflight','benchmark','screen'])
    parser.add_argument('--label',required=True);parser.add_argument('--level',default='A',choices=['A','B','C'])
    parser.add_argument('--workers',type=int,default=1);args=parser.parse_args()
    from threadpoolctl import threadpool_limits
    with threadpool_limits(limits=1):
        if args.mode=='preflight':preflight(args.label,args.workers)
        elif args.mode=='benchmark':benchmark(args.label,args.level)
        else:screen(args.label,args.workers)


if __name__=='__main__':main()

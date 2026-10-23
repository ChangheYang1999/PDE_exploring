"""Guarded mathematical tests for the Stage XIII all-column trust solver."""
from absolute_common import ROOT,OUT,np,atomic,digest,provenance
from stage13_solver import DenseTrustModel,trust_region_step


def main():
    path=OUT/'stage13_solver_tests.json'
    if path.exists():raise ValueError('Refusing to overwrite solver tests')
    rng=np.random.default_rng(130021);rows=[]
    for exponent in (0,8,14):
        q,_=np.linalg.qr(rng.normal(size=(31,12)))
        v,_=np.linalg.qr(rng.normal(size=(12,12)))
        values=np.geomspace(1.,10.**(-exponent),12)
        A=(q*values)@v.T;r=rng.normal(size=31)
        model=DenseTrustModel(A,r);previous=None
        for radius in (1e-8,1e-4,.1,10.):
            step,info=model.step(radius);response=A@step
            damping=info['damping'];gradient=A.T@r
            kkt=A.T@(r+response)+damping*damping*step
            scale=max(np.linalg.norm(gradient),np.linalg.norm(A.T@response),damping*damping*np.linalg.norm(step),1e-300)
            error=float(np.linalg.norm(kkt)/scale)
            cost=float(np.linalg.norm(r+response)**2/2)
            competitors=[]
            for i in range(48):
                trial=rng.normal(size=12);trial*=radius*rng.random()**(1/12)/np.linalg.norm(trial)
                competitors.append(float(np.linalg.norm(r+A@trial)**2/2))
            feasible=bool(np.linalg.norm(step)<=radius*(1+5e-12))
            best=bool(cost<=min(competitors)+1e-11*max(1.,cost))
            monotone=bool(previous is None or cost<=previous+1e-12*max(1.,cost))
            positive=info['positive_singular_values_used']==12
            passed=bool(feasible and best and monotone and positive and error<1e-10)
            rows.append({'spectrum_exponent':exponent,'radius':radius,'matrix_KKT_relative':error,
                'feasible':feasible,'lower_cost_than_48_independent_feasible_samples':best,
                'frontier_monotone':monotone,'all12_positive_directions_used':positive,'passed':passed})
            previous=cost
    # Exact rank deficiency is retained as a minimum-norm zero coordinate,
    # rather than deleting a small positive singular direction by threshold.
    s=np.asarray([1.,1e-14,0.]);u=np.asarray([1.,1.,1.]);vt=np.eye(3)
    step,info=trust_region_step(s,u,vt,1.)
    rows.append({'exact_zero_case':True,'small_positive_retained':info['positive_singular_values_used']==2,
        'exact_zero_minimum_norm_coordinate':float(step[2]),
        'passed':bool(info['positive_singular_values_used']==2 and info['exact_zero_singular_values']==1 and step[2]==0)})
    result={'schema':'stage13_solver_mathematical_tests_v1','passed':all(x['passed'] for x in rows),
        'tests':rows,'source_sha256':{name:digest(ROOT/name) for name in ['stage13_solver.py','stage13_solver_tests.py']},
        'environment':provenance(),'optimization_performed':False}
    atomic(path,result)
    print(__import__('json').dumps({'path':str(path),'passed':result['passed'],'tests':len(rows)}),flush=True)
    if not result['passed']:raise SystemExit(2)


if __name__=='__main__':main()

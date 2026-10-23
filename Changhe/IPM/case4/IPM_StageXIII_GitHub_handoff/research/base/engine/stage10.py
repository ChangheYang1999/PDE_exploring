"""Stage X: fixed-basis constrained grid refinement and separate fourth-order feasibility."""
from ipm_portable import output_dir, peak_rss_mib
import argparse,json,time,resource,signal,math
from pathlib import Path
import numpy as np
from scipy.linalg import null_space
from threadpoolctl import threadpool_limits,threadpool_info
import psutil
import stage9 as v

a=v.a;e=a.e;s=a.s;ROOT=Path(__file__).resolve().parent;OUT = output_dir();save=a.save
load=v.load;params=v.params;constraint=v.constraint;LOW=v.LOW;HIGH=v.HIGH
OLD_JOINT=a.JointProblem;OLD_JAC=a.hybrid_jac
EVALUATION_COUNTS={}

def grids(n):
    xi,yi=e.polar_grid(n,n,8.);xf,yf,wf=a.far_grid(n)
    return xi,yi,xf,yf,a.w.quadrature(n),wf

class GridProblem:
    """At most one 2048-point field cache, with full residual/Jacobian outputs only."""
    def __init__(self,n=97,batch=2048):
        xi,yi,xf,yf,self.wi,self.wf=grids(n)
        self.x=np.r_[xi,xf];self.y=np.r_[yi,yf];self.root=np.sqrt(np.r_[self.wi,.1*self.wf])
        self.n=n;self.far_weight=.1;self.batch=batch;self.center=a.Raw24(np.array([0.]),np.array([0.]));self.last_raw=None
    def coefficients(self,p):return self.center.coefficients(p)
    def metadata(self,p):return self.center.metadata(p)
    def fun(self,p):
        raw=np.empty(len(self.x))
        for lo in range(0,len(raw),self.batch):
            hi=min(len(raw),lo+self.batch);block=a.Raw24(self.x[lo:hi],self.y[lo:hi]);raw[lo:hi]=block.fun(p)
        self.last_raw=raw;self.last_parameters=p.copy();return self.root*raw
    objectives=OLD_JOINT.objectives
    def hybrid(self,p,fun=None,cl_step=None):
        if cl_step is None:cl_step=v.CL_STEP
        J=np.empty((len(self.x),24))
        for lo in range(0,len(J),self.batch):
            hi=min(len(J),lo+self.batch);block=a.Raw24(self.x[lo:hi],self.y[lo:hi]);mats,strain=block.data(p[0]);c=block.coefficients(p)
            ff={k:a.dot(M,c) for k,M in mats.items()}
            dc={k:M[:,1:]-M[:,:1]*strain[None,1:]/strain[0] for k,M in mats.items()}
            qm=mats['ratio']-strain[None,:];q=a.dot(qm,c);dq=qm[:,1:]-qm[:,:1]*strain[None,1:]/strain[0]
            wx=p[0]*block.x-ff['psiy'];wy=p[0]*block.y+ff['psix']
            aa=wx*ff['fx'];bb=wy*ff['fy'];dd=q*ff['f']
            da=wx[:,None]*dc['fx']-ff['fx'][:,None]*dc['psiy']
            db=wy[:,None]*dc['fy']+ff['fy'][:,None]*dc['psix']
            de=q[:,None]*dc['f']+ff['f'][:,None]*dq
            ww=(1+block.x**2+block.y**2)**((1/p[0]-1)/2)
            den=np.sqrt(aa*aa+bb*bb+dd*dd+(1e-8*ww)**2);rr=(aa+bb+dd)/den
            J[lo:hi,1:]=self.root[lo:hi,None]*((da+db+de)/den[:,None]-rr[:,None]*(aa[:,None]*da+bb[:,None]*db+dd[:,None]*de)/den[:,None]**2)
            del mats,dc,qm,dq,da,db,de,ff,block
        h=cl_step*max(1,abs(p[0]));f=self.fun if fun is None else fun;rr=[]
        for k in [2,1,-1,-2]:pp=p.copy();pp[0]+=k*h;rr.append(f(pp))
        J[:,0]=(-rr[0]+8*rr[1]-8*rr[2]+rr[3])/(12*h)
        return J

def factory(n):
    prob=OLD_JOINT(.1) if n==49 else GridProblem(n)
    original_fun=prob.fun
    def counted(p):
        key=str(n)+'_residual_values';EVALUATION_COUNTS[key]=EVALUATION_COUNTS.get(key,0)+1
        return original_fun(p)
    prob.fun=counted
    return prob
def hybrid(prob,p,fun=None,cl_step=None):
    key=str(prob.n)+'_full_jacobians';EVALUATION_COUNTS[key]=EVALUATION_COUNTS.get(key,0)+1
    return prob.hybrid(p,fun,cl_step) if isinstance(prob,GridProblem) else OLD_JAC(prob,p,fun,cl_step)

def make(p,prob,label):
    d=a.case_at(p,prob,n=getattr(prob,'n',97),label=label);d['jacobian_cl_relative_step']=v.CL_STEP;return d

def design(args):
    if (OUT/'design_complete.json').exists():print('Fixed grid design preserved');return
    fitting={};tests={}
    for n in [49,97]:
        xi,yi,xf,yf,wi,wf=grids(n);fitting[str(n)]={'inner':{'x':xi.tolist(),'y':yi.tolist()},'far':{'x':xf.tolist(),'y':yf.tolist()}}
        row={}
        for region,x,y,w,nr in [('inner',xi,yi,wi,n-2),('far',xf,yf,wf,n-1)]:
            positive=np.hypot(x,y)>0;rad=np.hypot(x[positive],y[positive]);u=np.log(rad/rad.min())/np.log(rad.max()/rad.min());theta=np.arctan2(y[positive],x[positive])/(np.pi/2)
            wp=w[positive];quad=float(wp@(u*u));qtheta=float(wp@(theta*theta))
            row[region]={'weight_sum':float(math.fsum(w)),'origin_mass':float(sum(w[~positive])),'linear_radius':float(wp@u),'linear_angle':float(wp@theta),
                         'linear_product':float(wp@(u*theta)),'quadratic_radius':quad,'quadratic_angle':qtheta,
                         'quadratic_radius_error':quad-1/3,'quadratic_angle_error':qtheta-1/3,
                         'expected_quadratic_radius_error':1/(6*nr**2),'expected_quadratic_angle_error':1/(6*(n-1)**2),
                         'coordinate_record':a.grid_record(x,y),'radial_endpoint_normalized_weights':[1/(2*nr),1/(2*nr)],'angular_endpoint_normalized_weights':[1/(2*(n-1))]*2}
            assert abs(math.fsum(w)-1)<2e-14 and abs(math.fsum(w[~positive]))==0
            assert max(abs(row[region][k]-val) for k,val in [('linear_radius',.5),('linear_angle',.5),('linear_product',.25)])<2e-14
            assert abs(quad-1/3-1/(6*nr**2))<2e-14 and abs(qtheta-1/3-1/(6*(n-1)**2))<2e-14
        tests[str(n)]=row
    old=json.loads((ROOT/'inputs/fitting_grid49.json').read_text());assert fitting['49']==old
    save('fitting_grids.json',fitting)
    historical=load('assessment_grids_historical');assessment=dict(historical)
    th=(np.arange(96)+.5)*np.pi/(2*96)
    for name,rlo,rhi in [('independent_shifted_inner',.08,8.),('independent_shifted_far',8.,64.)]:
        rad=np.exp(np.log(rlo)+(np.arange(96)+.5)*np.log(rhi/rlo)/96);x,y=s.polar(rad,th)
        assessment[name]={'x':x.tolist(),'y':y.tolist()}
    hashes={name:a.grid_record(np.array(r['x']),np.array(r['y'])) for name,r in assessment.items()}
    train=np.column_stack([np.r_[fitting['97']['inner']['x'],fitting['97']['far']['x']],np.r_[fitting['97']['inner']['y'],fitting['97']['far']['y']]])
    # Exact-coordinate and nearest angular-knot checks; no dense point-pair matrices.
    pointset={tuple(row) for row in train};overlap={}
    for name,row in assessment.items():
        xx=np.array(row['x']);yy=np.array(row['y']);angles=np.arctan2(yy,xx);dist=np.min(abs(angles[:,None]-np.linspace(0,np.pi/2,97)[None,:]),axis=1)
        overlap[name]={'exact_coordinate_overlap_count':sum((x,y) in pointset for x,y in zip(xx,yy)),
                       'minimum_angle_distance_to_fitting_knots':float(min(dist)),
                       'classification':'new independent shifted validation' if name.startswith('independent_shifted_') else ('true exterior holdout' if name.startswith('true_H') else 'historical matched diagnostic; may overlap fitting nodes or fitted radial band')}
    for name in ['independent_shifted_inner','independent_shifted_far']:assert overlap[name]['exact_coordinate_overlap_count']==0 and overlap[name]['minimum_angle_distance_to_fitting_knots']>1e-5
    for name in historical:assert assessment[name]==historical[name]
    save('assessment_grids.json',assessment);save('grid_design.json',hashes)
    save('design_complete.json',{'quadrature_tests':tests,'assessment_overlap':overlap,'before_any_optimization':True,'points97':len(train),'historical_coordinates_unchanged':True})
    print('Fixed grids, trapezoids, polynomial moments and independent validation verified')

def cross(args):
    case=load(args.label);p=params(case);objects={}
    for n in [49,97]:
        prob=factory(n);r=prob.fun(p);obj=prob.objectives();raw=prob.last_raw;num=n*n
        for name,sl in [('inner',slice(0,num)),('far',slice(num,None))]:
            i=int(np.argmax(abs(raw[sl])))+(0 if name=='inner' else num)
            obj['max_abs_ef_'+name]=float(abs(raw[i]));obj['max_ef_location_'+name]=[float(prob.x[i]),float(prob.y[i])]
        obj.update(RMS_inner=float(np.sqrt(2*obj['J_inner'])),RMS_far=float(np.sqrt(2*obj['J_far'])))
        objects[str(n)]=obj
    save(args.label+'_cross_grid.json',{'physical_vector_sha256':a.fingerprint(case),'grids':objects})
    print(json.dumps({'label':args.label,**objects}))

def baseline(args):
    case=load('original');p=params(case);prob=factory(49);r=prob.fun(p);reference=np.load(ROOT/'inputs/prior_stationarity_arrays.npz')['r']
    assert np.array_equal(prob.coefficients(p),case['coefficients']) and np.array_equal(r,reference)
    old=load('prior_final_objectives')['fit49'];obj=prob.objectives()
    assert max(abs(obj[k]-old[k]) for k in obj)<1e-20
    j=v.jet_report(case);assert max(abs(float(x)) for x in j['high_precision']['constraints'])<1e-10
    save('baseline_reproduction.json',{'physical_vector_bitwise':True,'center_coefficient_bitwise':True,'fitting_vector_bitwise':True,'objectives':obj,'jet':j})
    print('Stage IX physical vector, center coefficient, 49 residual vector and objectives reproduced bitwise')

def verify_jac(args):
    prob=factory(97);case=load('original');p=params(case);chart=v.Chart();q=p[chart.free];p,T=chart.lift(q,True)
    J=hybrid(prob,p,cl_step=v.CL_STEP);r=prob.fun(p);jq=J@T
    roundtrip=float(max(abs(p-params(case))));assert roundtrip<1e-10
    mapping=load('fit_map');D=np.array(mapping['column_scale']);sv=np.linalg.svd(jq*D,compute_uv=False)
    old=np.array(load('prior_final_local')['restricted_column_singular_values'])
    # Separate batched-value comparison uses same basis/rounded exponents and coefficients.
    alternative=GridProblem(97,1024);other=alternative.fun(p)
    delta=float(max(abs(other-r)));assert delta<1e-10
    errors=[];rng=np.random.default_rng(10097)
    for i in range(2):
        dq=rng.normal(size=22);dq/=np.linalg.norm(T@dq)
        for h in [.00025,.000125]:
            vv=[prob.fun(chart.lift(q+k*h*dq)) for k in [2,1,-1,-2]];fd=(-vv[0]+8*vv[1]-8*vv[2]+vv[3])/(12*h)
            errors.append({'direction':i,'step':h,'relative_error':float(np.linalg.norm(fd-jq@dq)/np.linalg.norm(fd))})
    save('refined_derivative_verification.json',{'errors':errors,'chart_lift_roundtrip_max_abs':roundtrip,'initial97_relative_projected_residual':float(np.linalg.norm(np.linalg.svd(jq,full_matrices=False)[0].T@r)/np.linalg.norm(r)),'batch_1024_vs_2048_max_residual_difference':delta,'frozen_map_condition97':float(sv[0]/sv[-1]),
         'Stage_IX_restricted_column_condition':float(old[0]/old[-1]),'map_rebuilt':False})
    assert max(row['relative_error'] for row in errors)<1e-5
    save('implicit_derivative_verification.json',load('refined_derivative_verification'))
    if not (OUT/'final.json').exists():
        seed=make(params(case),factory(97),'final');seed.update(fit_residual_calls=0,fit_jacobian_calls=0);save('final.json',seed)
    print(json.dumps({'maximum_direction_error':max(row['relative_error'] for row in errors),'frozen_map_condition97':sv[0]/sv[-1]}))

# Existing verified TRF and implicit chart are reused through explicit problem dispatch.
def dispatch(args,fn):
    n=49 if args.label=='original' else 97
    oldjoint=a.JointProblem;oldjac=a.hybrid_jac;oldmake=v.make
    a.JointProblem=lambda weight=.1:factory(n);a.hybrid_jac=hybrid;v.make=make
    try:return fn(args)
    finally:a.JointProblem=oldjoint;a.hybrid_jac=oldjac;v.make=oldmake

def fit(args):
    assert (OUT/'baseline_ready.json').exists() and (OUT/'refined_derivative_verification.json').exists()
    assert (OUT/'saved_assessment_ready.json').exists(), 'Assess the exact saved checkpoint before fitting'
    return dispatch(args,v.fit)
def local(args):return dispatch(args,v.local)
def validate_batch(args):return dispatch(args,v.validate_batch)
def validate_finish(args):return dispatch(args,v.validate_finish)
def assess(args):return v.assess(args)
def independent(args):return v.independent(args)
def verify_final(args):return v.verify_final(args)

exec(compile((ROOT/'diagnostics_impl.py').read_text(),str(ROOT/'diagnostics_impl.py'),'exec'))
exec(compile((ROOT/'completion_impl.py').read_text(),str(ROOT/'completion_impl.py'),'exec'))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode');parser.add_argument('--label',default='original');parser.add_argument('--part',default='main');parser.add_argument('--batch',type=int,default=0);parser.add_argument('--fd-scale',type=int,default=4,choices=[1,4])
    args=parser.parse_args()
    def terminate(signum,frame):raise SystemExit(143)
    signal.signal(signal.SIGTERM,terminate)
    try:
        with threadpool_limits(limits=1):globals()[args.mode](args)
    finally:
        use=resource.getrusage(resource.RUSAGE_SELF)
        with (OUT/'numerical_evaluation_counts.jsonl').open('a') as stream:
            stream.write(json.dumps({'time':time.time(),'mode':args.mode,'label':args.label,'part':args.part,'batch':args.batch,'counts':EVALUATION_COUNTS,'note':'Full global residual/Jacobian calls; analytic point-block operations and independent Green/field checks are separate.'})+'\n')
        save(args.mode+'_'+args.label+'_process.json',{'pid':__import__('os').getpid(),'peak_rss_mib':peak_rss_mib(use),'cpu_seconds':use.ru_utime+use.ru_stime,
            'threads_at_exit':psutil.Process().num_threads(),'nice':psutil.Process().nice(),'threadpools':threadpool_info()})
if __name__=='__main__':main()

"""Independent guarded qualification of analytic absolute-loss fields.

No fitting, projection, objective minimization, or candidate write occurs.
"""
import argparse
import math
from decimal import Decimal,localcontext
from absolute_common import *
from absolute_fields import prepare_candidate,fields,residual,center_data,CORE_ORDER,core_matrices
from highprecision_origin import origin_diagnostics,field_series,residual_series,evaluate_series
from basis_tests import Jet,potential_jet

D=Decimal


def independent_fields(prepared,x,y,precision=85):
    """Different Cartesian Taylor arithmetic at the actual evaluation point."""
    with localcontext() as ctx:
        ctx.prec=precision
        L=D.from_float(float(prepared['parameters'][0]));xx=D.from_float(float(x));yy=D.from_float(float(y))
        X=Jet({(0,0):xx,(1,0):1},5);Y=Jet({(0,0):yy,(0,1):1},5);q=X*X+Y*Y;logR=(1+q).log()
        gamma=1/L;delta=(1-gamma)/2;A=(3+gamma)/2;offset=[D(0),D(1),D(2),delta,2*delta,3*delta]
        chi=Jet.constant(0,5)
        for j,(m,k) in enumerate(CORE_ORDER):
            H=Jet.constant(0,5)
            for l in range(m+1):H=H+X.integer_power(2*m-2*l)*Y.integer_power(2*l)*D((-1)**l*math.comb(2*m,2*l))
            chi=chi+H*(logR*(A-m-offset[k])).exp()*D(prepared['center_metadata']['coefficients_decimal'][j])
        for coef,mode in zip(prepared['extra'],prepared['modes']):
            if coef:chi=chi+potential_jet(x,y,float(L),mode,5)*D.from_float(float(coef))
        rho=-(chi.derivative(2,1)+chi.derivative(0,3));rhox=-(chi.derivative(3,1)+chi.derivative(1,3));rhoy=-(chi.derivative(2,2)+chi.derivative(0,4))
        if yy:
            f=rho/yy;fx=rhox/yy;fy=rhoy/yy-rho/(yy*yy);ratio=chi.derivative(2,1)/yy
        else:
            f=-(chi.derivative(2,2)+chi.derivative(0,4));fx=-(chi.derivative(3,2)+chi.derivative(1,4));fy=D(0);ratio=chi.derivative(2,2)
        result={'f':f,'fx':fx,'fy':fy,'psi':chi.derivative(1,1),'psix':chi.derivative(2,1),'psiy':chi.derivative(1,2),'ratio':ratio}
        result['q']=L-1+ratio
        result['Rf']=(L*xx-result['psiy'])*fx+(L*yy+result['psix'])*fy+result['q']*f
        return {k:float(v) for k,v in result.items()}


def run(args):
    began=time.time();checks=[];profiles={};allpass=True
    labels=args.candidates or ['stage11','combined','local','global']
    for label in labels:
        case=load_case(label);model=prepare_candidate(case,'center_chart');literal=prepare_candidate(case,'literal')
        rows=[]
        for point in [(.31,.27),(1e6,.3e6)]:
            ref=independent_fields(model,*point)
            got=fields(model,[point[0]],[point[1]]);got['Rf']=residual(model,[point[0]],[point[1]])
            for key in ref:
                v=float(got[key][0]);error=abs(v-ref[key])/max(1.,abs(ref[key]));passed=error<2e-8
                rows.append({'point':point,'field':key,'value':v,'reference_85digit':ref[key],'scaled_error':error,'tolerance':2e-8,'passed':passed})
                allpass &=passed
        # Cross the Taylor/native switch; both calculations must independently agree.
        overlap=[]
        for rr in [.005,.01,.02]:
            theta=np.linspace(0,np.pi/2,17);x=rr*np.cos(theta);y=rr*np.sin(theta)
            p12=residual_series(model,12)['residual'];p16=residual_series(model,16)['residual']
            a=evaluate_series(p12,x,y);b=evaluate_series(p16,x,y)
            reference=independent_fields(model,float(x[7]),float(y[7]))['Rf']
            error=abs(float(a[7])-reference);tol=1e-18+1e-7*abs(reference);passed=error<tol
            overlap.append({'radius':rr,'order12_vs16_absolute_max':float(np.max(abs(a-b))),'reference_point':7,'direct_85digit_Rf':reference,'order12_Rf':float(a[7]),'error':error,'tolerance':tol,'passed':passed})
            allpass &=passed
        # Analytic complete cl dependence and old/new coefficient chain, two steps.
        x=np.array([1e-5,.01,.020001,.3,1.,4.,40.,1e5]);y=.37*x
        raw,jac=residual(model,x,y,True);p=model['p'];extra=model['extra'];count=len(p)+len(extra)
        rng=np.random.default_rng(71317);directions=[np.r_[1.,np.zeros(count-1)]]
        random=rng.normal(size=count);random[0]*=.01;random/=np.linalg.norm(random);directions.append(random)
        if len(extra):
            v=np.zeros(count);v[24:]=rng.normal(size=len(extra));v/=np.linalg.norm(v);directions.append(v)
        fd=[]
        for k,direction in enumerate(directions):
            for h in [2e-5,1e-5]:
                vals=[]
                for factor in [2,1,-1,-2]:
                    state=np.r_[p,extra]+factor*h*direction
                    pert=prepare_candidate(case,'center_chart',parameters=state[:24],extra=state[24:])
                    vals.append(residual(pert,x,y))
                difference=(-vals[0]+8*vals[1]-8*vals[2]+vals[3])/(12*h);analytic=jac@direction
                err=float(np.linalg.norm(difference-analytic)/max(1.,np.linalg.norm(analytic)));passed=err<2e-6
                fd.append({'direction':k,'step':h,'relative_or_absolute_l2_error':err,'tolerance':2e-6,'passed':passed});allpass &=passed
        origin=origin_diagnostics(model,.02,A_REF)
        literal_origin=origin_diagnostics(literal,.02,A_REF)
        profiles[label]={'metadata':model['metadata'],'independent_spot_checks':rows,'origin_overlap_checks':overlap,'analytic_complete_cl_and_coefficient_fd':fd,
            'origin':origin,'literal_origin':literal_origin,'literal_origin_divergent':literal_origin['rows'][0]['divergent_at_origin']}
        atomic(OUT/'field_tests.partial.json',{'complete':False,'profiles':profiles})
    result={'complete':True,'passed':bool(allpass),'profiles':profiles,'fixed_reference_amplitude':A_REF,
        'reference_method':'85-digit Cartesian Taylor algebra about actual point; no production radial/harmonic derivative formulas',
        'unrounded_potential_semantics':True,'no_candidate_write':True,'seconds':time.time()-began,'provenance':provenance(),'sources':sources()}
    atomic(OUT/'field_tests.json',result)
    print(json.dumps({'passed':result['passed'],'seconds':result['seconds'],'profiles':list(profiles)}))
    if not allpass:raise SystemExit(1)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--candidates',nargs='*');run(parser.parse_args())

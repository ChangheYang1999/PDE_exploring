"""Read-only arithmetic/model-interpretation comparisons of saved candidates.

The frozen original loss is rerun exactly, with its recorded summation groups.
This worker does not fit, repair, project, normalize, or overwrite any candidate.
All finite-domain absolute integrals are explicitly quadrature approximations;
none removes the literal nonzero origin constant or its divergent whole loss.
"""
import argparse
import math
from absolute_common import *
from absolute_fields import prepare_candidate,fields,residual,KEYS
from stage12_model import core_fields
from nested_model import NestedSpectralProblem
from spectral_basis import evaluate_modes

VIEW_NAMES=('native_literal','unrounded_literal','analytic_center_chart')
PAIRS=(('native_literal','unrounded_literal'),('unrounded_literal','analytic_center_chart'),('native_literal','analytic_center_chart'))


def native_saved_fields(case,x,y,block_size=2048):
    """Frozen rounded core plus exact recorded contiguous extra sum groups."""
    p=np.asarray(case.get('core_parameters',[case['cl']]+case['coefficients'][1:]));extra=np.asarray(case.get('extra_coefficients',[]));modes=case.get('modes',[])
    groups=case.get('sum_groups',[len(extra)] if len(extra) else [])
    if sum(groups)!=len(extra) or any(isinstance(g,bool) or not isinstance(g,int) or g<=0 for g in groups):raise ValueError('Invalid recorded summation groups')
    x=np.asarray(x,float);y=np.asarray(y,float);out={k:np.empty(len(x)) for k in KEYS+('q',)}
    for lo in range(0,len(x),block_size):
        hi=min(len(x),lo+block_size);xx=x[lo:hi];yy=y[lo:hi]
        ff=core_fields(p,xx,yy,core_coefficients=case['coefficients']);start=0
        for count in groups:
            stop=start+count;cc=np.ascontiguousarray(extra[start:stop])
            if np.any(cc):
                vv=evaluate_modes(xx,yy,float(p[0]),modes[start:stop])
                for k in KEYS:ff[k]+=np.ascontiguousarray(vv[k])@cc
                ff['q']+=np.ascontiguousarray(vv['ratio'])@cc
            start=stop
        for k in out:out[k][lo:hi]=ff[k]
    return out


def physical_rf(cl,ff,x,y):
    return (cl*x-ff['psiy'])*ff['fx']+(cl*y+ff['psix'])*ff['fy']+(cl-1+ff['ratio'])*ff['f']


def trapezoid(nodes):
    nodes=np.asarray(nodes,float)
    if len(nodes)<2 or np.any(np.diff(nodes)<=0):return None
    w=np.empty(len(nodes));w[0]=(nodes[1]-nodes[0])/2;w[-1]=(nodes[-1]-nodes[-2])/2;w[1:-1]=(nodes[2:]-nodes[:-2])/2
    return w


def logpolar_weights(x,y):
    rr=np.hypot(x,y);edge=np.r_[0,np.flatnonzero(abs(np.diff(rr))>1e-12*np.maximum(1.,rr[:-1]))+1,len(rr)];lens=np.diff(edge)
    if len(lens)<2 or not np.all(lens==lens[0]) or lens[0]<2:return None
    nr,nt=len(lens),int(lens[0]);r=rr.reshape(nr,nt)[:,0];theta=np.arctan2(y,x).reshape(nr,nt)[-1]
    if np.any(np.diff(r)<=0):return None
    positive=r>0
    rw=trapezoid(np.log(r[positive]));tw=trapezoid(theta)
    if rw is None or tw is None:return None
    weights=np.zeros((nr,nt));weights[positive]=np.outer(rw,tw)
    return weights.ravel()


def compare_values(reference,other,x,y):
    reference=np.asarray(reference);other=np.asarray(other);delta=other-reference;mag=np.abs(reference)
    floor=1e-12*max(1.,float(np.max(mag)));resolved=mag>floor;k=int(np.argmax(abs(delta)))
    relative=np.zeros_like(mag);relative[resolved]=abs(delta[resolved])/mag[resolved]
    kr=int(np.argmax(relative))
    return {'max_absolute_difference':float(abs(delta[k])),'max_absolute_location':[float(x[k]),float(y[k])],
       'relative_l2_difference':float(np.linalg.norm(delta)/max(np.linalg.norm(reference),1e-300)),
       'max_difference_divided_by_max1_reference':float(np.max(abs(delta))/max(1.,float(np.max(mag)))),
       'pointwise_relative_reference_floor':floor,'resolved_reference_points':int(np.sum(resolved)),
       'max_pointwise_relative_difference_where_resolved':float(relative[kr]) if np.any(resolved) else None,
       'max_pointwise_relative_location':[float(x[kr]),float(y[kr])] if np.any(resolved) else None,
       'near_zero_relative_difference_is_not_meaningful':True}


def origin_literal(case):
    ff=native_saved_fields(case,np.array([0.]),np.array([0.]));cl=case['cl'];d=cl-1+ff['ratio'][0]
    return {'native_binary64_center_identity_defect':float(d),'native_binary64_physical_Rf0':float(d*ff['f'][0]),
        'native_stabilized_q0':float(ff['q'][0]),
        'stabilized_q_is_not_literal_physical_center_constant':True}


def run(args):
    output=OUT/'arithmetic_comparison.json';artifact=OUT/'arithmetic_comparison_arrays.npz'
    if output.exists() or artifact.exists():raise ValueError('Diagnostic results already exist; use a new worker/result version')
    oldgrids=read(BASE/'inputs/assessment_grids_stage12.json');results={};saved={};allpass=True;began=time.time()
    for label in ('stage11','combined','local','global'):
        case=load_case(label);literal=prepare_candidate(case,'literal');chart=prepare_candidate(case,'center_chart')
        p=chart['p'];extra=chart['extra'];modes=chart['modes'];groups=case.get('sum_groups',[len(extra)] if len(extra) else [])
        prob=NestedSpectralProblem(modes,n=97,workers=1,sum_groups=groups);native_r=prob.fun(p,extra)
        fresh={'J_inner':float(native_r[:97*97]@native_r[:97*97]/2),'J_far':float(native_r[97*97:]@native_r[97*97:]/.2),'J_joint':float(native_r@native_r/2)}
        reference=case['objectives'];diff=fresh['J_joint']-reference['J_joint'];tol=1e-13+1e-6*abs(reference['J_joint']);passed=abs(diff)<=tol;allpass &=passed
        original={'fresh':fresh,'saved':reference,'J_joint_difference':diff,'unchanged_historical_comparison_tolerance':tol,'passed':passed,
            'sum_groups':groups,'workers':1,'native_derived_c0':float(prob.original.coefficients(p)[0]),'saved_c0':case['coefficients'][0],
            'native_derived_c0_exactly_matches_saved':float(prob.original.coefficients(p)[0]).hex()==float(case['coefficients'][0]).hex(),
            'original_stabilized_relative_objective_retained':True,'physical_absolute_loss_is_separate':True}
        grids={'original97_inner':{'x':prob.x[:97*97],'y':prob.y[:97*97]},'original97_far':{'x':prob.x[97*97:],'y':prob.y[97*97:]}}
        grids.update({k:oldgrids[k] for k in ('true_H65','near_origin','near_axis','origin','x_axis','y_axis')})
        region_results={}
        for region,row in grids.items():
            x=np.asarray(row['x']);y=np.asarray(row['y']);native=native_saved_fields(case,x,y);unrounded=fields(literal,x,y);center=fields(chart,x,y)
            views={'native_literal':native,'unrounded_literal':unrounded,'analytic_center_chart':center}
            native['Rf']=physical_rf(case['cl'],native,x,y);unrounded['Rf']=residual(literal,x,y);center['Rf']=residual(chart,x,y)
            # The unrounded providers form physical q before binary64 rounding,
            # using independent high-precision polynomials on the origin branch.
            values={};weights=logpolar_weights(x,y) if region in ('original97_inner','original97_far','true_H65') else None
            for name,v in views.items():
                k=int(np.argmax(abs(v['Rf'])));r=np.hypot(x,y);density=np.divide(abs(y*v['Rf']),r,out=np.zeros_like(r),where=r>0)
                values[name]={'sampled_max_absolute_Rf':float(abs(v['Rf'][k])),'location':[float(x[k]),float(y[k])],
                    'sampled_max_absolute_Rf_over_fixed_a_ref':float(np.max(abs(v['Rf']))/A_REF),
                    'sampled_max_absolute_Rrho_over_r_fixed_a_ref':float(np.max(density)/A_REF),
                    'finite_domain_absolute_log_integral':None if weights is None else float(weights@(v['Rf']**2)/(math.pi*A_REF*A_REF)),
                    'finite_domain_quadrature_only':True,'whole_radius_loss_claimed':False}
                saved[label+'__'+region+'__'+name+'__Rf']=v['Rf']
                for k in KEYS:saved[label+'__'+region+'__'+name+'__'+k]=v[k]
            comparisons={}
            for first,second in PAIRS:
                key=first+'__to__'+second
                comp={k:compare_values(views[first][k],views[second][k],x,y) for k in KEYS+('Rf',)}
                a=values[first]['finite_domain_absolute_log_integral'];b=values[second]['finite_domain_absolute_log_integral']
                comp['finite_domain_absolute_integral_difference']=None if a is None else b-a
                comp['finite_domain_absolute_integral_relative_difference']=None if a is None else (b-a)/max(abs(a),1e-300)
                comparisons[key]=comp
            saved[label+'__'+region+'__x']=x;saved[label+'__'+region+'__y']=y
            region_results[region]={'points':len(x),'coordinate_sha256':array_hash(np.column_stack((x,y))),
                'minimum_radius':float(np.min(np.hypot(x,y))),'maximum_radius':float(np.max(np.hypot(x,y))),
                'views':values,'comparisons':comparisons,'sampled_maxima_only':True,
                'log_integral_weights':'unscaled trapezoids on actual ds and theta knots; origin row receives zero quadrature weight' if weights is not None else None}
        results[label]={'original_objective':original,'origin':origin_literal(case),'analytic_center_metadata':chart['metadata'],
            'literal_unrounded_center_metadata':literal['metadata'],'regions':region_results,
            'literal_whole_radius_J_abs':'infinite because physical Rf(0) is nonzero under literal saved analytic-potential interpretation',
            'analytic_center_view_is_a_distinct_model_interpretation':True}
        atomic(OUT/'arithmetic_comparison.partial.json',{'completed':False,'candidates':results})
    npz(artifact,**saved)
    report={'schema':'absolute_arithmetic_model_interpretation_comparison_v1','completed':True,'passed':bool(allpass),'candidates':results,
       'views':{'native_literal':'frozen rounded-derivative core, saved c0, recorded extra BLAS groups; raw physical cl-1+ratio in Rf',
                'unrounded_literal':'unrounded analytic-potential derivatives with the identical serialized c0/free coefficients/extras',
                'analytic_center_chart':'unrounded analytic potential with c0 defined by the exact center identity; all other independent coefficients unchanged'},
       'comparison_attribution':'native-to-unrounded differences include exponent rounding, derivative arithmetic and summation order; not attributed solely to one cause',
       'predetermined_sampling':'unchanged original97 fitting grids and frozen true_H65/near_origin/near_axis/origin/x_axis/y_axis; no candidate-based coordinate selection',
       'candidate_overwrite_refit_projection_or_optimization':False,'fixed_reference_amplitude':A_REF,
       'finite_domain_integrals_never_claimed_exactly_scale_invariant':True,'literal_origin_constant_retained':True,
       'artifact':str(artifact),'artifact_sha256':digest(artifact),'seconds':time.time()-began,'provenance':provenance(),'sources':sources()}
    atomic(output,report);print(json.dumps({'completed':True,'passed':report['passed'],'seconds':report['seconds']}))
    if not allpass:raise SystemExit(1)

if __name__=='__main__':
    parser=argparse.ArgumentParser();args=parser.parse_args();run(args)

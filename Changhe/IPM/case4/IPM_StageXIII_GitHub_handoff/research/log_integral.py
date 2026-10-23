"""Refined log-radius quadrature with separately reported endpoint estimates.

No finite window is labelled exactly invariant. Uniform analytic outer
inequalities are evaluated in binary64, while the origin remainder and
quadrature errors are refinement estimates, not interval certificates.
"""
import math
from absolute_common import *
from absolute_fields import prepare_candidate,residual
from highprecision_origin import origin_diagnostics
from tail_envelope import outer_envelope


DESIGN={'origin_physical_radius':.02,'initial_upper_log_radius':12.,
        'expansion_log_width':8.,'maximum_upper_log_radius':100.,
        'absolute_tolerance':2e-13,'relative_tolerance':1e-7,
        'panel_width':1.,'radial_orders':[8,16,32,64],
        'angular_intervals':[64,128,256],
        'origin_orders':[12,16],
        'error_scope':'refinement estimates plus uniform analytic infinity envelope evaluated in binary64; no outward-rounded whole-line certificate'}


def rule(lo,hi,order=16,angles=128,angular_method='trapezoid'):
    edges=np.linspace(lo,hi,max(1,int(math.ceil((hi-lo)/DESIGN['panel_width'])))+1)
    z,w=np.polynomial.legendre.leggauss(order)
    ss=np.concatenate([(a+b)/2+(b-a)*z/2 for a,b in zip(edges[:-1],edges[1:])])
    sw=np.concatenate([(b-a)*w/2 for a,b in zip(edges[:-1],edges[1:])])
    if angular_method=='trapezoid':
        th=np.linspace(0,np.pi/2,angles+1);tw=np.full(angles+1,np.pi/(2*angles));tw[[0,-1]]*=.5
    elif angular_method=='gauss':
        z,w=np.polynomial.legendre.leggauss(angles);th=(z+1)*np.pi/4;tw=w*np.pi/4
    else:raise ValueError('unknown angular rule')
    s,t=np.meshgrid(ss,th,indexing='ij')
    return s.ravel(),t.ravel(),np.outer(sw,tw).ravel()


def finite(prepared,lo,hi,order=16,angles=128,dilation=1.,angular_method='trapezoid',keep_vectors=False):
    began=time.time();s,t,w=rule(lo,hi,order,angles,angular_method)
    vals=np.empty(len(s));factor=float(dilation)
    for start in range(0,len(s),8192):
        stop=min(start+8192,len(s));r=np.exp(s[start:stop])/factor
        vals[start:stop]=residual(prepared,r*np.cos(t[start:stop]),r*np.sin(t[start:stop]))
    integral=float(w@(vals*vals)/(np.pi*A_REF*A_REF));index=int(np.argmax(abs(vals)))
    row={'s_min':lo,'s_max':hi,'radius_min':math.exp(lo),'radius_max':math.exp(hi),
         'base_radius_min':math.exp(lo)/factor,'base_radius_max':math.exp(hi)/factor,
         'dilation':factor,'radial_order':order,'angular_intervals_or_order':angles,
         'angular_method':angular_method,'nodes':len(s),'J_abs_finite':integral,
         'sampled_max_abs_Rf_over_a_ref':float(max(abs(vals))/A_REF),
         'sampled_max_location_polar':[float(math.exp(s[index])),float(t[index])],
         'mesh_sha256':array_hash(np.column_stack([s,t,w])),
         'residual_sha256':array_hash(vals),'seconds':time.time()-began}
    return (row,{'s':s,'theta':t,'weights':w,'Rf':vals}) if keep_vectors else row


def integrate(prepared,dilation=1.):
    began=time.time();lam=float(dilation);lo=math.log(DESIGN['origin_physical_radius']);hi=DESIGN['initial_upper_log_radius']
    # Whole origin tail is evaluated in the base variable r/lambda, never
    # by deleting a nonzero physical residual constant from a literal profile.
    origin=origin_diagnostics(prepared,math.exp(lo)/lam,A_REF,tuple(DESIGN['origin_orders']))
    if any(row['divergent_at_origin'] for row in origin['rows']):
        return {'finite_whole_axis':False,'J_abs':'infinite_due_nonzero_origin_constant',
                'origin':origin,'literal_profile_changed':False}
    origin_value=origin['rows'][-1]['polynomial_origin_integral']
    expansions=[];pieces=[]
    while True:
        left=lo if not expansions else hi-DESIGN['expansion_log_width']
        part=finite(prepared,left,hi,8,64,lam);pieces.append(part['J_abs_finite'])
        bound=outer_envelope(prepared,math.exp(hi)/lam,A_REF)
        total=math.fsum(pieces)+origin_value
        tol=DESIGN['absolute_tolerance']+DESIGN['relative_tolerance']*abs(total)
        expansions.append({'upper_log_radius':hi,'added_shell':part,'partial_J_abs':total,
            'uniform_outer_integral_bound':bound['integral_upper_bound'],'requested_error':tol})
        if bound['integral_upper_bound']<tol/8 or hi>=DESIGN['maximum_upper_log_radius']:break
        hi=min(hi+DESIGN['expansion_log_width'],DESIGN['maximum_upper_log_radius'])
    refinements=[]
    coarse=finite(prepared,lo,hi,8,128,lam);refinements.append(coarse)
    for order in [16,32,64]:
        row=finite(prepared,lo,hi,order,128,lam);refinements.append(row)
        delta=abs(row['J_abs_finite']-refinements[-2]['J_abs_finite'])
        tol=DESIGN['absolute_tolerance']+DESIGN['relative_tolerance']*abs(row['J_abs_finite']+origin_value)
        if delta<tol/8:break
    fine,vectors=finite(prepared,lo,hi,refinements[-1]['radial_order'],256,lam,keep_vectors=True)
    gauss=finite(prepared,lo,hi,refinements[-1]['radial_order'],96,lam,'gauss')
    angular_error=max(abs(fine['J_abs_finite']-refinements[-1]['J_abs_finite']),abs(fine['J_abs_finite']-gauss['J_abs_finite']))
    radial_error=abs(refinements[-1]['J_abs_finite']-refinements[-2]['J_abs_finite'])
    origin_error=origin['successive_order_integral_difference']
    error_estimate=radial_error+angular_error+origin_error+bound['integral_upper_bound']
    value=fine['J_abs_finite']+origin_value
    tol=DESIGN['absolute_tolerance']+DESIGN['relative_tolerance']*abs(value)
    record={'finite_whole_axis':True,'center_convention':prepared['convention'],
       'dilation':lam,'a_ref':A_REF,'J_abs_estimate':value,'finite_interval_integral':fine['J_abs_finite'],
       'origin_polynomial_integral_estimate':origin_value,
       'infinity_integral_included_in_point_estimate':0.,
       'infinity_integral_upper_envelope':bound['integral_upper_bound'],
       'origin_tail_error_estimate':origin_error,'radial_quadrature_error_estimate':radial_error,
       'angular_quadrature_error_estimate':angular_error,'total_error_diagnostic':error_estimate,
       'requested_error':tol,'numerical_error_checks_passed':bool(error_estimate<tol),
       'rigorous_continuous_whole_axis_error_certificate':False,
       'limitation':'Origin analytic remainder and quadrature error are estimated by independent overlap/order/refinement checks; infinity envelope is conservatively derived but evaluated without outward rounding. The number is a numerical whole-radius approximation, not an exactly invariant finite-window loss.',
       'origin':origin,'interval_expansions':expansions,'radial_refinements':refinements,
       'final_quadrature':fine,'independent_angular_gauss_check':gauss,
       'infinity_envelope':bound,'seconds':time.time()-began}
    return record,vectors

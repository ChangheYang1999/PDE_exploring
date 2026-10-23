"""Independent qualification of conditional high-angular delta-tail modes.

The frozen evaluator and earlier tests are not changed.  References use the
85-digit Cartesian Taylor algebra from basis_tests, including direct analytic
c_l differentiation of the potential before its spatial derivatives.  Execute
only through the verified Stage XII resource supervisor.
"""
import os
import time

if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Stage XII numerical work requires the verified resource supervisor')

import numpy as np
from basis_tests import D, Jet, independent_fields, localcontext, potential_jet
from spectral_basis import evaluate_modes, metadata
from stage12_common import OUT, ROOT, atomic, digest, provenance


TOLERANCE=2e-8
CL=1.88359472051
MODES=[{'family':'global','m':m,'n':n,'sigma':'delta'} for m,n in
       [(0,0),(0,1),(0,2),(1,0),(1,2),(5,2),(14,2),(22,2),
        (29,0),(29,1),(29,2),(45,0),(45,1),(45,2)]]
POINTS=[(.13,.21),(1.2,.7),(3.,4.),(17.,9.),(256.,150.),
        (2.,0.),(0.,2.),(1e-10,1.3),(1.3,1e-10),
        (1e7,0.),(0.,1e7),(1e7,.3e7),
        (1e13,0.),(0.,1e13),(1e13,.3e13)]
GROWTH_RADII=(1e6,1e7)


def independent_cl_fields(x,y,cl,mode):
    """Spatial fields of the independently differentiated potential.

    This is the same defining Cartesian differential identity as the original
    independent_fields reference.  Its input potential is d(chi)/d(c_l), not
    the native radial/harmonic derivative implementation or a finite difference.
    """
    z=potential_jet(x,y,cl,mode,cl_derivative=True)
    y=D.from_float(float(y))
    rho=-(z.derivative(2,1)+z.derivative(0,3))
    rhox=-(z.derivative(3,1)+z.derivative(1,3))
    rhoy=-(z.derivative(2,2)+z.derivative(0,4))
    if y:
        f=rho/y;fx=rhox/y;fy=rhoy/y-rho/(y*y)
        ratio=z.derivative(2,1)/y
    else:
        f=-(z.derivative(2,2)+z.derivative(0,4))
        fx=-(z.derivative(3,2)+z.derivative(1,4))
        fy=D(0);ratio=z.derivative(2,2)
    return {key:float(value) for key,value in
        {'chi':z.derivative(0,0),'f':f,'fx':fx,'fy':fy,
         'psi':z.derivative(1,1),'psix':z.derivative(2,1),
         'psiy':z.derivative(1,2),'ratio':ratio}.items()}


def scaled_error(actual,reference):
    return abs(actual-reference)/max(1.,abs(reference))


def growth_checks():
    """Check the declared delta-tail leading powers without a radial cutoff.

    With gamma=1/c_l and sigma=delta=(1-gamma)/2, the global potential has
    leading degree 2+2gamma, independently of m,n.  Spatial derivatives give
    the listed field powers.  Angular vector norms avoid choosing a zero of a
    particular harmonic.  This finite-radius comparison is an evaluator
    regression test; the analytic growth identity establishes canonicity.
    """
    gamma=1/CL
    exponents={'chi':2+2*gamma,'f':2*gamma-2,
               'fx':2*gamma-3,'fy':2*gamma-3,'psi':2*gamma,
               'psix':2*gamma-1,'psiy':2*gamma-1,'ratio':2*gamma-2}
    theta=(np.arange(97)+.37)*np.pi/(2*97)
    values=[]
    for radius in GROWTH_RADII:
        values.append(evaluate_modes(radius*np.cos(theta),radius*np.sin(theta),CL,MODES))
    rows=[];ratio=GROWTH_RADII[1]/GROWTH_RADII[0]
    for j,mode in enumerate(MODES):
        for key,exponent in exponents.items():
            left=float(np.linalg.norm(values[0][key][:,j]))
            right=float(np.linalg.norm(values[1][key][:,j]))
            prediction=left*ratio**exponent
            error=abs(right-prediction)/max(abs(prediction),np.finfo(float).tiny)
            measured=float(np.log(right/left)/np.log(ratio)) if left>0 and right>0 else None
            rows.append({'mode':j,'field':key,'expected_power':exponent,
                'measured_two_radius_power':measured,'first_angular_norm':left,
                'second_angular_norm':right,'asymptotic_power_ratio_relative_error':float(error)})
    return rows,exponents


def main():
    began=time.time()
    x=np.array([point[0] for point in POINTS]);y=np.array([point[1] for point in POINTS])
    values,cl_derivatives=evaluate_modes(x,y,CL,MODES,cl_derivative=True)
    spatial=[];cl_rows=[];origin=[]
    with localcontext() as ctx:
        ctx.prec=85
        for j,mode in enumerate(MODES):
            for i,(px,py) in enumerate(POINTS):
                exact=independent_fields(px,py,CL,mode)
                dexact=independent_cl_fields(px,py,CL,mode)
                for key in exact:
                    actual=float(values[key][i,j]);dactual=float(cl_derivatives[key][i,j])
                    spatial.append({'mode':j,'point':i,'field':key,'value':actual,
                        'reference':exact[key],'scaled_error':scaled_error(actual,exact[key])})
                    cl_rows.append({'mode':j,'point':i,'field':key,'value':dactual,
                        'reference':dexact[key],'scaled_error':scaled_error(dactual,dexact[key])})
            for derivative in (False,True):
                jet=potential_jet(0.,0.,CL,mode,8,derivative)
                maximum=max((abs(value) for value in jet.c.values()),default=D(0))
                origin.append({'mode':j,'cl_derivative':derivative,
                    'maximum_potential_Taylor_degree_0_through_8':str(maximum),
                    'identically_zero':not jet.c})
        # A genuinely nonzero combined coefficient vector has the same zero jet.
        combination=Jet.constant(0,8)
        for j,mode in enumerate(MODES):
            combination=combination+potential_jet(0.,0.,CL,mode,8)*D(j+1)/D(7)
        combined_zero=not combination.c
    parity=[]
    signs_template={'chi':lambda sx,sy:1,'f':lambda sx,sy:1,
        'fx':lambda sx,sy:sx,'fy':lambda sx,sy:sy,
        'psi':lambda sx,sy:sx*sy,'psix':lambda sx,sy:sy,
        'psiy':lambda sx,sy:sx,'ratio':lambda sx,sy:1}
    for sx,sy in [(-1,1),(1,-1),(-1,-1)]:
        reflected,dreflected=evaluate_modes(sx*x,sy*y,CL,MODES,cl_derivative=True)
        for derivative,original,reflected_values in (
                [(False,values,reflected),(True,cl_derivatives,dreflected)]):
            for key,sign in signs_template.items():
                expected=sign(sx,sy)*original[key]
                error=float(np.max(abs(reflected_values[key]-expected)/np.maximum(1.,abs(expected))))
                parity.append({'sx':sx,'sy':sy,'cl_derivative':derivative,
                    'field':key,'maximum_scaled_error':error})
    origin_values,origin_derivatives=evaluate_modes(np.array([0.]),np.array([0.]),CL,MODES,True)
    zero=all(np.array_equal(matrix,np.zeros_like(matrix))
             for fields in (origin_values,origin_derivatives) for matrix in fields.values())
    finite=all(np.all(np.isfinite(matrix))
               for fields in (values,cl_derivatives) for matrix in fields.values())
    growth,exponents=growth_checks()
    maximum=max(row['scaled_error'] for row in spatial)
    cl_maximum=max(row['scaled_error'] for row in cl_rows)
    parity_maximum=max(row['maximum_scaled_error'] for row in parity)
    growth_maximum=max(row['asymptotic_power_ratio_relative_error'] for row in growth)
    minimum_degree=min(2*max(5,mode['m']) for mode in MODES)
    canonical=exponents['psi']<2
    passed=bool(maximum<TOLERANCE and cl_maximum<TOLERANCE
        and parity_maximum<TOLERANCE and growth_maximum<TOLERANCE
        and finite and zero and all(row['identically_zero'] for row in origin)
        and combined_zero and minimum_degree>=10 and canonical)
    output={'schema':'stage12-high-angular-delta-basis-qualification-v1','passed':passed,
        'tolerance':TOLERANCE,'tolerance_scope':'All scaled independent spatial/cl derivative errors, parity errors and finite-radius leading-power ratio errors; no PDE optimization tolerance changed.',
        'reference':'85-digit Cartesian bivariate Taylor algebra; no native harmonic/radial spatial or c_l derivative formulas',
        'cl':CL,'modes':MODES,'points':POINTS,'metadata':metadata(MODES),
        'maximum_scaled_spatial_error':maximum,'maximum_scaled_cl_derivative_error':cl_maximum,
        'maximum_scaled_parity_error':parity_maximum,'maximum_asymptotic_power_ratio_error':growth_maximum,
        'spatial_checks':spatial,'analytic_cl_derivative_checks':cl_rows,'parity_checks':parity,
        'origin_checks':origin,'origin_fields_and_cl_derivatives_bitwise_zero':zero,
        'nonzero_combination_potential_jet_degree0_through8_zero':combined_zero,
        'minimum_potential_origin_degree':minimum_degree,'five_Taylor_conditions_unchanged_by_origin_vanishing':minimum_degree>=10,
        'finite_through_coordinate_scale_1e13_including_axes':finite,
        'maximum_sampled_radius':float(max(np.hypot(px,py) for px,py in POINTS)),
        'far_tail_coverage_scope':'Representative coordinate scale 1e13 covers the approximate largest compactified Green nodes at quadrature order192 for this c_l; no finite radial truncation is introduced.',
        'growth_radii':list(GROWTH_RADII),'growth_expected_powers':exponents,'growth_checks':growth,
        'canonical_streamfunction_power_strictly_below_two':canonical,
        'qualification_scope':'Evaluator coverage for conditional delta bands through m45,n2. These tests do not select a hierarchy, impose formal nonlinear recursion, launch optimization, or establish a PDE residual bound.',
        'source_sha256':{name:digest(ROOT/name) for name in
            ['spectral_basis.py','basis_tests.py','basis_high_angular_tests.py']},
        'elapsed_seconds':time.time()-began,'provenance':provenance()}
    atomic(OUT/'basis_high_angular_tests.json',output)
    print({'passed':passed,'maximum_scaled_spatial_error':maximum,
           'maximum_scaled_cl_derivative_error':cl_maximum,
           'maximum_asymptotic_power_ratio_error':growth_maximum},flush=True)
    if not passed:raise SystemExit(1)


if __name__=='__main__':main()

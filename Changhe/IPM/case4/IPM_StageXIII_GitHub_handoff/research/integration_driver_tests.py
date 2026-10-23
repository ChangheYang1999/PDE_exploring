#!/usr/bin/env python3
"""Exercise the actual adaptive whole-radius driver against analytic references.

Monkeypatches are local to this worker process. No production source, saved
candidate, or research campaign is edited. This tests driver accounting and
quadrature separately from the IPM field evaluator and tail-envelope algebra.
"""
import math
import sys

sys.dont_write_bytecode = True
from absolute_common import ROOT, OUT, A_REF, np, atomic, digest, provenance
import log_integral as driver
from manufactured_reference import radial_integral_tails, whole_axis_loss


def synthetic_residual(prepared, x, y):
    x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float))
    radius=np.hypot(x,y)
    q=radius*radius
    # Independent rational implementation of the synthetic residual.
    radial=(q/(1+q))**3/(1+q)
    return radial*np.cos(2*np.arctan2(y,x))+prepared.get('constant_defect',0.)


def synthetic_origin(prepared,radius,a_ref,orders):
    defect=prepared.get('constant_defect',0.)
    if defect:
        return {'radius':radius,'rows':[{'order':order,'divergent_at_origin':True,
                'constant_residual_decimal':str(defect),'polynomial_origin_integral':None}
                for order in orders],'successive_order_integral_difference':None,
                'reference_is_exact_synthetic_integral':True}
    reference=radial_integral_tails(math.log(radius),math.log(radius)+1)
    value=float(reference['origin'])/(4*a_ref*a_ref)
    return {'radius':radius,'rows':[{'order':order,'divergent_at_origin':False,
            'constant_residual_decimal':'0','polynomial_origin_integral':value}
            for order in orders],'successive_order_integral_difference':0.,
            'reference_is_exact_synthetic_integral':True,
            'meaning':'Uses exact synthetic inner integral to isolate integration-driver accounting.'}


def synthetic_outer(prepared,radius,a_ref):
    reference=radial_integral_tails(math.log(radius)-1,math.log(radius))
    value=float(reference['infinity'])/(4*a_ref*a_ref)
    return {'radius':radius,'integral_upper_bound':value,
            'reference_is_exact_synthetic_outer_integral':True,
            'outward_rounded_numerical_certificate':False,
            'meaning':'Analytic synthetic reference evaluated as binary64; not a model field envelope.'}


def run():
    target=OUT/'integration_driver_tests.json'
    if target.exists():
        raise FileExistsError('Preserve prior integration-driver tests')
    original=(driver.residual,driver.outer_envelope,driver.origin_diagnostics)
    rows=[];checks=[]
    expected=whole_axis_loss(A_REF)
    try:
        driver.residual=synthetic_residual
        driver.outer_envelope=synthetic_outer
        driver.origin_diagnostics=synthetic_origin
        for dilation in [1.,2.,16.,256.,1024.]:
            result,vectors=driver.integrate({'convention':'manufactured'},dilation=dilation)
            error=abs(result['J_abs_estimate']-expected)
            allowance=result['total_error_diagnostic']+5e-13*expected
            checks.extend([
                {'name':'exact_whole_axis_reference_with_reported_tail','dilation':dilation,
                 'error':error,'allowance':allowance,'passed':error<=allowance},
                {'name':'driver_numerical_error_gate','dilation':dilation,
                 'passed':result['numerical_error_checks_passed']},
                {'name':'factor_pi_fixed_reference_and_no_interval_normalization','dilation':dilation,
                 'relative_error':error/expected,'passed':error/expected<2e-7},
                {'name':'positive_product_quadrature_weights','dilation':dilation,
                 'passed':bool(np.all(vectors['weights']>0))},
                {'name':'physical_window_and_base_window_differ','dilation':dilation,
                 'passed':abs(result['final_quadrature']['base_radius_max']*dilation
                              -result['final_quadrature']['radius_max'])
                         <=2e-15*result['final_quadrature']['radius_max']}
            ])
            rows.append({'dilation':dilation,'exact_reference':expected,
                         'observed_error':error,'driver_result':result})
        values=[row['driver_result']['J_abs_estimate'] for row in rows]
        difference=max(values)-min(values)
        allowance=max(row['driver_result']['total_error_diagnostic'] for row in rows)*2+5e-13*expected
        checks.append({'name':'scale_invariance_with_independent_tail_accounting',
                       'max_pairwise_difference':difference,'allowance':allowance,
                       'passed':difference<=allowance,
                       'finite_windows_claimed_exactly_invariant':False})
        negative=driver.integrate({'convention':'manufactured_literal','constant_defect':1e-30})
        checks.append({'name':'negative_constant_defect_early_rejection',
                       'passed':isinstance(negative,dict) and negative.get('finite_whole_axis') is False
                                and negative.get('J_abs')=='infinite_due_nonzero_origin_constant',
                       'result':negative})
        checks.append({'name':'adaptive_window_expansion_actually_exercised',
                       'passed':any(len(row['driver_result']['interval_expansions'])>1 for row in rows)})
    finally:
        driver.residual,driver.outer_envelope,driver.origin_diagnostics=original
    result={'schema':'absolute_loss_actual_integration_driver_tests_v1',
            'synthetic_residual':'r^6/(1+r^2)^4 cos(2theta); not an IPM profile',
            'reference_amplitude':A_REF,'reference_whole_axis_loss':expected,
            'process_local_monkeypatch_only':True,'production_files_modified':False,
            'isolation':'Tests actual log_integral.integrate with exact independent synthetic origin/outer references and rational residual evaluator.',
            'driver_design':driver.DESIGN,'results':rows,'checks':checks,
            'source_sha256':{name:digest(ROOT/name) for name in ['integration_driver_tests.py','manufactured_reference.py','log_integral.py']},
            'provenance':provenance(),'passed':all(row['passed'] for row in checks)}
    atomic(target,result)
    print({'output':str(target),'passed':result['passed'],'checks':len(checks)},flush=True)
    return 0 if result['passed'] else 1


if __name__=='__main__':
    raise SystemExit(run())

#!/usr/bin/env python3
"""Numerical qualification of independently derived uniform tail inequalities.

Sample checks detect algebra/coding errors; they do not turn binary64 formulas
into rigorous continuous upper-bound certificates.
"""
import math
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from absolute_common import ROOT, A_REF, np, read, atomic, digest, provenance
from absolute_fields import prepare_candidate, fields
from spectral_basis import evaluate_modes
from outer_envelopes import mode_field_constants, FIELDS
from tail_envelope import outer_envelope


def run():
    target = ROOT/'results/tail_envelope_tests.json'
    if target.exists():
        raise FileExistsError('Preserve prior tail test output')
    tests = []
    mode_rows = []
    modes = [{'family': 'global', 'm': m, 'n': n, 'sigma': sigma}
             for m, n, sigma in [(0,0,0), (0,2,'delta'), (1,2,0), (5,2,0),
                                  (14,2,'delta'), (22,22,0), (29,2,'delta'), (45,2,'delta')]]
    modes += [{'family': 'local', 'm': m, 'center': center, 'width': width}
              for m, center, width in [(0,.5,.9), (3,8.5,.9), (8,8.75,.45), (22,8.5,.9)]]
    for cl in [1.4, 1.8835947205126689, 2.5]:
        beta, alpha = 1/cl-1, 1/cl
        exponents = {'f': beta, 'fx': beta-1, 'fy': beta-1,
                     'psix': alpha, 'psiy': alpha, 'ratio': alpha-1}
        for radius in [1.,16.,256.,math.exp(20)]:
            radii = radius*np.array([1.,1.0001,2.,16.,1024.])
            angles = np.linspace(0,math.pi/2,33)
            rr,tt = np.meshgrid(radii,angles,indexing='ij')
            x,y = (rr*np.cos(tt)).ravel(),(rr*np.sin(tt)).ravel()
            values = evaluate_modes(x,y,cl,modes)
            for index,mode in enumerate(modes):
                constants = mode_field_constants(mode,cl,radius)
                for field in FIELDS:
                    permitted = constants[field]*rr.ravel()**exponents[field]
                    actual = abs(values[field][:,index])
                    excess = float(np.max(actual-permitted))
                    ratio = float(np.max(np.divide(actual,permitted,out=np.zeros_like(actual),where=permitted>0)))
                    tolerance = float(5e-12*max(float(np.max(permitted)),np.finfo(float).tiny))
                    passed = bool(excess <= tolerance)
                    row={'cl':cl,'radius':radius,'mode':mode,'field':field,
                         'max_observed_fraction_of_bound':ratio,'max_excess':excess,
                         'comparison_tolerance':tolerance,'passed':passed}
                    mode_rows.append(row)
                    tests.append({'name':'pointwise_mode_field_bound',**row})
    candidates=[]
    for label in ['stage11','combined','local','global']:
        case=read(ROOT/'inputs'/f'{label}.json')
        prepared=prepare_candidate(case,'center_chart')
        cl=float(prepared['parameters'][0])
        previous=None
        for radius in [1.,16.,256.,math.exp(20),math.exp(60),math.exp(100)]:
            envelope=outer_envelope(prepared,radius,A_REF)
            value=envelope['integral_upper_bound']
            tests.append({'name':'finite_decreasing_outer_envelope','candidate':label,'radius':radius,
                          'value':value,'previous':previous,
                          'passed':bool(math.isfinite(value) and value>=0 and (previous is None or value<=previous*(1+1e-12)))})
            previous=value
            if radius<=256:
                radii=radius*np.array([1.,2.,16.,1024.])
                angles=np.linspace(0,math.pi/2,33)
                rr,tt=np.meshgrid(radii,angles,indexing='ij')
                ff=fields(prepared,(rr*np.cos(tt)).ravel(),(rr*np.sin(tt)).ravel())
                for field in FIELDS:
                    permitted=envelope['field_constants'][field]*rr.ravel()**envelope['field_exponents'][field]
                    actual=abs(ff[field])
                    ratio=float(np.max(np.divide(actual,permitted,out=np.zeros_like(actual),where=permitted>0)))
                    tests.append({'name':'pointwise_candidate_field_bound','candidate':label,'radius':radius,
                                  'field':field,'max_observed_fraction_of_bound':ratio,
                                  'passed':bool(np.all(actual<=permitted*(1+5e-12)+np.finfo(float).tiny))})
            candidates.append({'candidate':label,'radius':radius,'integral_upper_bound':value,
                               'field_constants':envelope['field_constants'],
                               'residual_constants':envelope['residual_constants']})
    result={'schema':'absolute_loss_tail_envelope_tests_v1','provenance':provenance(),
            'source_sha256':{name:digest(ROOT/name) for name in ['tail_envelope.py','outer_envelopes.py','tail_envelope_tests.py','absolute_fields.py']},
            'sampled_qualification_only':True,'outward_rounded_numerical_certificate':False,
            'mode_count':len(modes),'mode_checks':mode_rows,'candidate_envelopes':candidates,
            'checks':tests,'passed':all(row['passed'] for row in tests)}
    atomic(target,result)
    print({'output':str(target),'passed':result['passed'],'checks':len(tests)},flush=True)
    return 0 if result['passed'] else 1


if __name__=='__main__':
    raise SystemExit(run())

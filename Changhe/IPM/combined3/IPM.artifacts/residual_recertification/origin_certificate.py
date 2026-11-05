#!/usr/bin/env python3
"""Validated origin-disk residual bounds from exact Candidate 007/013 sources.

This is a primary calculation, not a consumer of historical norm endpoints.
All intermediate polynomial arithmetic is rational; all transcendental
quantities and remainder sums use Arb.  Exact dyadic enclosure endpoints are
retained in the JSON output.
"""
import argparse
from collections import defaultdict
from hashlib import sha256
import json
import math
from pathlib import Path
import sys
import time

from flint import arb, fmpq as Q, ctx

sys.set_int_max_str_digits(0)


def enclosure(x):
    assert x.is_finite()
    return [str(x.lower().fmpq()), str(x.upper().fmpq())]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ipm-root', type=Path,
                        default=Path('/mnt/d/Changhe_D/PDE_exploring/Changhe/IPM'))
    parser.add_argument('--radius', default='1/100000000')
    parser.add_argument('--degree', type=int, default=16)
    parser.add_argument('--precision', type=int, default=384)
    parser.add_argument('--output', type=Path,
                        default=Path('/tmp/residual_recertification/origin_certificate.json'))
    args = parser.parse_args()
    started = time.monotonic()
    sys.path.insert(0, str(args.ipm_root/'combined3/IPM.artifacts/coercivity_residual'))
    from fields013 import Evaluator, C, SOURCE_HASHES, rational_arb, BASE007, PHI013
    from asymptotics013 import Expansion

    ctx.prec = args.precision
    radius_exact = Q(args.radius)
    assert radius_exact > 0
    radius = arb(radius_exact)
    evaluator = Evaluator(precision=args.precision,
                          max_density_order=4, max_velocity_order=3)
    expansion = Expansion(evaluator, 'origin', degree=args.degree)
    N = args.degree + 1
    assert N >= 2*7  # Four density derivatives require seven potential derivatives.
    z = radius*radius/arb(expansion.radius)
    assert z < arb(1)/4

    raw = {}
    field_bounds = {}
    for name, max_order in [('rho', 4), ('u1', 3), ('u2', 3)]:
        for total in range(max_order+1):
            for i in range(total+1):
                j = total-i
                finite_by_power = defaultdict(Q)
                for (_, _, power), coefficient in expansion.field(name, i, j).items():
                    assert power >= 0
                    finite_by_power[power] += abs(coefficient)
                tail_by_power = defaultdict(lambda: arb(0))
                for coefficient, power in expansion.remainder_terms(name, i, j, radius):
                    assert power >= 0
                    tail_by_power[power] += coefficient
                finite_sum = arb(0)
                finite_rows = []
                for power, coefficient in sorted(finite_by_power.items()):
                    term = arb(coefficient)*radius**rational_arb(power)
                    finite_sum += term
                    finite_rows.append({'power_exact': str(power),
                                        'coefficient_abs_sum_enclosure_exact': enclosure(arb(coefficient)),
                                        'endpoint_term_enclosure_exact': enclosure(term)})
                tail_sum = arb(0)
                tail_rows = []
                for power, coefficient in sorted(tail_by_power.items()):
                    term = coefficient*radius**rational_arb(power)
                    tail_sum += term
                    tail_rows.append({'power_exact': str(power),
                                      'coefficient_enclosure_exact': enclosure(coefficient),
                                      'endpoint_term_enclosure_exact': enclosure(term)})
                bound = (finite_sum+tail_sum).upper()
                field_bounds[name, i, j] = bound
                key = f'{name},{i},{j}'
                raw[key] = {'finite_terms': finite_rows, 'tail_terms': tail_rows,
                            'finite_sum_enclosure_exact': enclosure(finite_sum),
                            'tail_sum_enclosure_exact': enclosure(tail_sum),
                            'uniform_abs_upper_exact': str(bound.fmpq())}
                print('field', key, 'bound', bound.str(20),
                      'elapsed', round(time.monotonic()-started, 2), flush=True)

    # Leibniz expansion of cX.grad rho-rho plus u.grad rho.
    residual_bounds = {}
    residual_raw = {}
    c = arb(C)
    for total in range(4):
        for i in range(total+1):
            j = total-i
            dilation = c*radius*(field_bounds['rho', i+1, j]
                                 + field_bounds['rho', i, j+1])
            dilation += abs(arb(C*total-1))*field_bounds['rho', i, j]
            products = []
            nonlinear = arb(0)
            for a in range(i+1):
                for b in range(j+1):
                    combinatorial = math.comb(i, a)*math.comb(j, b)
                    term = combinatorial*(field_bounds['u1', a, b]
                            *field_bounds['rho', i-a+1, j-b]
                            + field_bounds['u2', a, b]
                            *field_bounds['rho', i-a, j-b+1])
                    nonlinear += term
                    products.append({'velocity_derivative': [a,b],
                                     'multiplicity': combinatorial,
                                     'term_enclosure_exact': enclosure(term)})
            B = (dilation+nonlinear).upper()
            residual_bounds[i,j] = B
            residual_raw[f'{i},{j}'] = {
                'dilation_enclosure_exact': enclosure(dilation),
                'nonlinear_products': products,
                'nonlinear_sum_enclosure_exact': enclosure(nonlinear),
                'uniform_abs_upper_exact': str(B.fmpq())}

    area = arb.pi()*radius*radius
    l2_energy = area*residual_bounds[0,0]**2
    tensor_bounds = []
    tensor_rows = []
    for total in range(4):
        norm_square_bound = arb(0)
        rows = []
        for i in range(total+1):
            j = total-i
            B = residual_bounds[i,j]
            Gx = 2*radius*B
            Gy = 2*radius*B
            if i:
                Gx += 2*i*residual_bounds[i-1,j]
            if j:
                Gy += 2*j*residual_bounds[i,j-1]
            multiplicity = math.comb(total,i)
            term = multiplicity*(B*B+Gx*Gx+Gy*Gy)
            norm_square_bound += term
            rows.append({'derivative': [i,j], 'ordered_multiplicity': multiplicity,
                         'G_component_uniform_uppers_exact':
                            [str(v.upper().fmpq()) for v in [B,Gx,Gy]],
                         'point_tensor_sum_enclosure_exact': enclosure(term)})
        energy = area*norm_square_bound
        tensor_bounds.append(energy.upper())
        tensor_rows.append({'order': total, 'terms': rows,
                            'energy_enclosure_exact': enclosure(energy),
                            'energy_upper_exact': str(energy.upper().fmpq())})
    # Regional integration by parts would introduce boundary terms.  Bound
    # the positive local integrands directly instead of using regional
    # binomial Sobolev sums.  The trace of a Hessian in dimension two is
    # bounded by sqrt(2) times the ordered Hessian tensor norm.
    E2 = (tensor_bounds[0].sqrt()+(2*tensor_bounds[2]).sqrt())**2
    E3 = E2+(tensor_bounds[1].sqrt()+(2*tensor_bounds[3]).sqrt())**2
    dependencies = {}
    for path in [BASE007, PHI013,
                 args.ipm_root/'combined3/IPM.artifacts/coercivity_residual/fields013.py',
                 args.ipm_root/'combined3/IPM.artifacts/coercivity_residual/asymptotics013.py']:
        dependencies[str(path.resolve())] = sha256(path.read_bytes()).hexdigest()
    out = {
        'status': 'VALIDATED_ORIGIN_DISK_PRIMARY_ENCLOSURE',
        'source_sha256': SOURCE_HASHES, 'dependency_sha256': dependencies,
        'fixed_c_exact': str(C), 'radius_exact': str(radius_exact),
        'domain': 'closed disk r <= radius; boundary circles are null sets',
        'degree': args.degree, 'precision_bits': args.precision,
        'analytic_factor_cauchy_radius_exact': str(expansion.radius),
        'cauchy_tail_ratio_enclosure_exact': enclosure(z),
        'field_uniform_enclosures': raw,
        'residual_uniform_enclosures': residual_raw,
        'disk_area_enclosure_exact': enclosure(area),
        'F_L2_energy_enclosure_exact': enclosure(l2_energy),
        'F_L2_energy_upper_exact': str(l2_energy.upper().fmpq()),
        'G_definition': '(F,2*x*F,2*y*F)',
        'G_ordered_tensor_energies': tensor_rows,
        'G_E2_definition': 'integral_disk |(1-Delta)G|^2',
        'G_E3_definition': 'integral_disk (|(1-Delta)G|^2+|gradient(1-Delta)G|^2)',
        'G_E2_energy_upper_exact': str(E2.upper().fmpq()),
        'G_E3_energy_upper_exact': str(E3.upper().fmpq()),
        'G_E2_triangle_enclosure_exact': enclosure(E2),
        'G_E3_triangle_enclosure_exact': enclosure(E3),
        'code_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'elapsed_seconds': time.monotonic()-started,
        'scope': 'Primary source-derived origin bounds; no inherited residual energy used.'}
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    print('L2 energy', l2_energy.str(30), flush=True)
    print('G E2 energy', E2.str(30), flush=True)
    print('G E3 energy', E3.str(30), flush=True)
    print('OUTPUT', args.output, flush=True)


if __name__ == '__main__':
    main()

"""Exact whole-plane assembly, outward integer roots and NR-25 inputs."""
from fractions import Fraction
from math import isqrt

ORDERS = (4, 5, 6)
MU = ('41', '83/2', '42', '45', '46', '48', '52', '56', '64', '80')


def exact(value):
    assert isinstance(value, str) and value
    result = Fraction(value)
    assert str(result) == value, 'Canonical exact rational required'
    return result


def intervals(rows):
    assert isinstance(rows, list) and len(rows) == 3
    assert all(type(row['order']) is int for row in rows)
    assert [row['order'] for row in rows] == list(ORDERS)
    result = []
    for row in rows:
        lower, upper = exact(row['lower_exact']), exact(row['upper_exact'])
        assert 0 <= lower <= upper
        result.append((lower, upper))
    return result


def integer_root(value, order):
    assert type(value) is int and value >= 0
    assert type(order) is int and order in (2, 10)
    if order == 2:
        result = isqrt(value)
    else:
        lower, upper = 0, 1 << ((value.bit_length() + order - 1) // order)
        while upper - lower > 1:
            middle = (lower + upper) // 2
            if middle ** order <= value:
                lower = middle
            else:
                upper = middle
        result = lower
    assert result ** order <= value < (result + 1) ** order
    return result


def root_decimals(value, order, digits=24):
    assert isinstance(value, Fraction) and value >= 0
    assert type(digits) is int and 1 <= digits <= 40
    scale = 10 ** digits
    k = integer_root((value.numerator * scale ** order) // value.denominator, order)
    lower = k - 1 if k and Fraction(k, scale) ** order == value else k
    upper = k + 1
    assert Fraction(lower, scale) ** order <= value < Fraction(upper, scale) ** order
    def display(n):
        return str(n // scale) + '.' + str(n % scale).zfill(digits)
    return display(lower), display(upper)


def assemble(blocks, jobs, source, origin, exterior, digits=24):
    assert len(blocks) == len(jobs) == 5
    assert [j['id'] for j in jobs] == ['n0', 'n1', 'n2', 'n3', 'n4']
    assert [b['job'] for b in blocks] == [j['id'] for j in jobs]
    seen = []
    regions = [intervals(origin['laplacian_energies'])]
    assert origin['radius_exact'] == '1/4096' and exterior['radius_exact'] == '10000'
    assert origin['source'] == exterior['source'] == source
    for i, (block, job) in enumerate(zip(blocks, jobs, strict=True)):
        expected = list(range(i, 561, 5))
        assert job['indices'] == expected and block['block'] == job
        assert block['status'] == 'ADMITTED_NEAR_BLOCK' and block['source'] == source
        assert block['complete_requested_assignment'] is True
        assert type(block['panel_count']) is int and block['panel_count'] == len(expected)
        assert block['precision_bits'] == 2048 and block['chunk_count'] == (len(expected) + 7) // 8
        seen.extend(expected)
        regions.append(intervals(block['laplacian_energies']))
    assert sorted(seen) == list(range(561))
    regions.append(intervals(exterior['laplacian_energies']))
    output = []
    for k, order in enumerate(ORDERS):
        lower = sum((region[k][0] for region in regions), Fraction(0))
        upper = sum((region[k][1] for region in regions), Fraction(0))
        lo, _ = root_decimals(lower, 2, digits)
        _, hi = root_decimals(upper, 2, digits)
        assert Fraction(lo) ** 2 <= lower <= upper < Fraction(hi) ** 2
        output.append({'order': order, 'energy_lower_exact': str(lower),
                       'energy_upper_exact': str(upper), 'norm_lower_decimal': lo,
                       'norm_upper_decimal': hi})
    return output


def moments(norms, pi_lower, digits=24):
    assert [row['order'] for row in norms] == list(ORDERS)
    p = exact(pi_lower)
    assert 3 < p < 4
    energies, uppers = {}, {}
    for row in norms:
        m = row['order']
        lower, upper = exact(row['energy_lower_exact']), exact(row['energy_upper_exact'])
        lo, hi = Fraction(row['norm_lower_decimal']), Fraction(row['norm_upper_decimal'])
        assert 0 <= lo <= hi and lo * lo <= lower <= upper < hi * hi
        energies[m], uppers[m] = upper, hi
    first = (uppers[4] * uppers[6] + uppers[5] ** 2) / (2 * p)
    second = uppers[4] * uppers[6] / p
    square = min(first, second)
    _, m4 = root_decimals(square, 2, digits)
    assert Fraction(m4) ** 2 > square
    tails = []
    for mu_text in MU:
        mu = exact(mu_text)
        for ratio in (Fraction(1, 2), Fraction(3, 4)):
            v = ratio * mu
            methods = []
            for m in ORDERS:
                gap = Fraction(m) - Fraction(31, 10)
                assert gap > 0
                bound = (energies[m] / (4 * p * gap)) ** 5 * v ** (31 - 10 * m)
                _, upper = root_decimals(bound, 10, digits)
                assert Fraction(upper) ** 10 > bound
                methods.append({'derivative_order': m, 'tenth_power_upper_exact': str(bound),
                                'tail_upper_decimal': upper})
            chosen = min(methods, key=lambda row: Fraction(row['tail_upper_decimal']))
            tails.append({'mu_exact': mu_text, 'threshold_ratio_exact': str(ratio),
                          'threshold_exact': str(v), 'p_exact': '21/10', 'methods': methods,
                          'chosen_derivative_order': chosen['derivative_order'],
                          'tail_upper_decimal': chosen['tail_upper_decimal']})
    return {'fourier_normalization': '(2*pi)^(-2) with nonunitary forward transform',
            'pi_lower_exact': pi_lower,
            'M4_squared_upper_options_exact': [str(first), str(second)],
            'M4_squared_upper_exact': str(square), 'M4_upper_decimal': m4,
            'tail_rows': tails,
            'scope': 'NR-25 Fourier L1 moment and tail inputs only; no full near price.'}

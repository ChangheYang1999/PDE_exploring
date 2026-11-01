#!/usr/bin/env python3
"""Exact rational component supersolutions for the general-Q majorant."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time

BASE = Path('research/134_general_component_radius')


def polynomial_product(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai*bj
    return out


def shifted_tail_value(poly, degree, z):
    return sum((v*z**(j-degree) for j, v in enumerate(poly) if j >= degree), F(0))


class Majorant:
    def __init__(self, period, a, kappa, lower):
        self.period, self.a, self.kappa, self.lower = period, F(a), F(kappa), F(lower)
        self.L = F(period, 2)
        self.x = [F(0)] + [F(comb(2*(j-1), j-1), j) * (self.kappa*self.L)**(j-1) * self.a**j
                          for j in range(1, period+1)]
        self.square = polynomial_product(self.x, self.x)
        self.truncated_squares = {}
        for r in range(1, period+1):
            pr = [F(0) if j < r else xj for j, xj in enumerate(self.x)]
            self.truncated_squares[r] = polynomial_product(pr, pr)
        zero = [F(0)] * (period+1)
        self.constant = self.phi(F(0), zero)
        self.J = [[F(0) for _ in zero] for _ in zero]
        for j in range(period+1):
            unit = zero.copy()
            unit[j] = F(1)
            column = self.phi(F(0), unit)
            for i in range(period+1):
                self.J[i][j] = column[i]-self.constant[i]
        assert all(self.J[i][j] == 0 for i in range(period+1) for j in range(i, period+1))
        assert all(v >= 0 for row in self.J for v in row)
        self.T = [[F(0) for _ in zero] for _ in zero]
        for j in range(period+1):
            unit = zero.copy()
            unit[j] = F(1)
            column = self.precondition(unit)
            for i in range(period+1):
                self.T[i][j] = column[i]
        self.Y0 = self.precondition(self.constant)
        assert all(v > 0 for v in self.Y0)
        arbitrary = [F(j+2, j+1) for j in range(period+1)]
        expected = [self.constant[i] + sum((self.J[i][j]*arbitrary[j] for j in range(period+1)), F(0))
                    for i in range(period+1)]
        assert self.phi(F(0), arbitrary) == expected

    def phi(self, z, y):
        q, L, kap, x = self.period, self.L, self.kappa, self.x
        w, eta = y[0], y[-1]
        p = sum((x[j]*z**j for j in range(1, q+1)), F(0))
        result = [kap*L*shifted_tail_value(self.square, q+1, z)
                  + 2*kap*L*p*w + kap*L*z**(q+1)*w*w
                  + kap*eta*(p+z**(q+1)*w)]
        for r in range(1, q+1):
            ar = shifted_tail_value(self.truncated_squares[r], q+r+1, z)
            ar += 2*sum((x[j]*z**(j-r) for j in range(r, q+1)), F(0))*w
            ar += z**(q+1-r)*w*w
            term = L*ar + z**(q+1-r)*eta*w
            term += 2*L*sum((x[j]*y[r-j] for j in range(1, r)), F(0))
            result.append(kap*term/(self.lower if r == q else 1))
        return result

    def precondition(self, rhs):
        out = []
        for i, value in enumerate(rhs):
            out.append(value + sum((self.J[i][j]*out[j] for j in range(i)), F(0)))
        return out

    def transformed(self, z, y):
        atz, atzero = self.phi(z, y), self.phi(F(0), y)
        rem = [v-v0 for v, v0 in zip(atz, atzero)]
        assert all(v >= 0 for v in rem)
        added = self.precondition(rem)
        return [v0+v for v0, v in zip(self.Y0, added)]


def stringify(v):
    if isinstance(v, F):
        return str(v)
    if isinstance(v, list):
        return [stringify(x) for x in v]
    if isinstance(v, dict):
        return {k: stringify(x) for k, x in v.items()}
    return v


def certificate(name, period, a, kappa, lower):
    m = Majorant(period, a, kappa, lower)
    box = [2*v for v in m.Y0]
    trials = []
    for power in range(0, 402, 2):
        z0 = F(1, 2**power)
        vals = m.transformed(z0, box)
        ratios = [v/b for v, b in zip(vals, box)]
        success = max(ratios) <= 1
        trials.append({'power': power, 'maximum_component_ratio': max(ratios), 'passes': success})
        if success:
            assert max(ratios) < 1
            return {'name': name, 'period': period, 'a': F(a), 'kappa': F(kappa), 'L': m.L,
                    'response_lower': F(lower), 'low_coefficients': m.x[1:],
                    'constant': m.constant, 'J': m.J, 'T': m.T, 'Y0': m.Y0, 'box': box,
                    'z0': z0, 'power': power, 'exterior_radius_power': power*period//2,
                    'map_on_box': vals, 'component_ratios': ratios, 'trials': trials}
    raise RuntimeError('No successful box on the specified grid')


def main():
    start = time.monotonic()
    old = json.loads(Path('research/124_tuned_component_radius/verification/checks.json').read_text())
    q3 = []
    for oldrow in old['rows']:
        m = Majorant(3, oldrow['a'], oldrow['kappa'], oldrow['sigma_lower'])
        for attr, key in [('J', 'J'), ('T', 'Q'), ('Y0', 'Y0')]:
            assert stringify(getattr(m, attr)) == oldrow[key], (oldrow['name'], key)
        box = [F(v) for v in oldrow['box']]
        vals = m.transformed(F(oldrow['z0']), box)
        assert stringify(vals) == oldrow['map_on_box']
        row = certificate(oldrow['name'], 3, oldrow['a'], oldrow['kappa'], oldrow['sigma_lower'])
        assert row['power'] == oldrow['power']
        q3.append({'name': oldrow['name'], 'J_T_Y0_and_map_exactly_equal': True,
                   'first_successful_even_power': row['power']})
    bounds = json.loads(Path('research/133_six_period_five_profiles/verification/response_bounds.json').read_text())
    alist = [F(149,100), F(1049,1000), F(563,500), F(1213,1000), F(329,250), F(39,25)]
    rows = []
    for source, a in zip(bounds['rows'], alist):
        lo, hi = map(F, source['root_interval'])
        assert 1+max(abs(lo), abs(hi)) < a
        row = certificate('period_five_root_'+str(source['root_index']), 5, a, F(156,5),
                          source['uniform_response_lower_bound'])
        row['root_index'] = source['root_index']
        row['root_interval'] = source['root_interval']
        row['input_norm_bound_verified'] = True
        rows.append(row)
        print(json.dumps({'root_index': source['root_index'], 'z_power': row['power'],
                          'radius_power': row['exterior_radius_power'],
                          'maximum_box_ratio_approx': float(max(row['component_ratios'])),
                          'actual_elapsed_s': time.monotonic()-start}), flush=True)
    assert all(F(8,5) >= r['a'] and F(1,8388608) <= r['response_lower'] for r in rows)
    rows.append(certificate('period_five_all_roots_common', 5, F(8,5), F(156,5), F(1,8388608)))
    result = {'checked_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
              'all_checks_pass': True, 'q3_independent_comparisons': q3,
              'q5_certificates': rows, 'actual_elapsed_s': time.monotonic()-start}
    (BASE/'verification/checks.json').write_text(json.dumps(stringify(result), indent=2)+'\n')
    (BASE/'sources/general_component_radius.py').write_bytes(Path(__file__).read_bytes())
    manifest = {}
    for p in BASE.rglob('*'):
        if p.is_file() and p.name != 'MANIFEST.json':
            b=p.read_bytes()
            manifest[str(p.relative_to(BASE))] = {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
    (BASE/'verification/MANIFEST.json').write_text(json.dumps({'files': manifest}, indent=2)+'\n')
    print(json.dumps({'all_checks_pass': True, 'common_radius_power': rows[-1]['exterior_radius_power'],
                      'actual_elapsed_s': time.monotonic()-start}), flush=True)


if __name__ == '__main__':
    main()

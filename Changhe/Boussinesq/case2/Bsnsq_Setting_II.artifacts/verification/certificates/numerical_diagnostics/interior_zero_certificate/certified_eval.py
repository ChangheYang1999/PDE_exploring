"""Independent outward real-ball evaluator for the full-plane finite inverse.

The analytic recurrence and remainder are proved in PROOF.md. No fitting
code is imported. Exact input coefficients are supplied by registered JSON.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from flint import arb, arb_poly, ctx


def rational(a, b=1):
    return arb(int(a)) / int(b)


def read_compiled(path):
    d = json.loads(Path(path).read_text())
    for k in ('beta', 'M', 'N', 'denominator'):
        d[k] = int(d[k])
    for k in ('A', 'C'):
        d[k] = [[int(v) for v in row] for row in d[k]]
    for row in d['modes']:
        for k in ('k', 'L', 'J'):
            row[k] = int(row[k])
        for k in ('P', 'Q', 'moment'):
            row[k] = [int(v) for v in row[k]]
    assert d['beta'] == 2 and d['denominator'] > 0
    assert len(d['modes']) == len(d['A']) == len(d['C']) == d['M']
    assert [r['k'] for r in d['modes']] == list(range(1, d['M'] + 1))
    for row in d['modes']:
        assert row['L'] == 4 * (row['k'] + 1) - 1
        assert row['J'] == 4 * (row['k'] - 1) + 1
        assert row['moment'][1] > 0
    return d


def store(v):
    assert isinstance(v, arb) and v.is_finite()
    def dyadic(x):
        m, e = x.man_exp()
        return {'mantissa': str(m), 'exponent_two': int(e)}
    return {'lower': dyadic(v.lower()), 'upper': dyadic(v.upper()),
            'display': v.str(26)}


def upper_abs(v):
    return max(abs(v.lower()), abs(v.upper()))


def plus_error(v, e):
    assert e >= 0
    return v + arb(0, e.upper())


class LocalInverse:
    """Cache exact-polynomial shifts and certified Taylor coefficients."""
    def __init__(self, comp, t0_numerator=13, t0_denominator=50):
        self.comp = comp
        self.t0 = rational(t0_numerator, t0_denominator)
        assert 0 < self.t0 < 1
        self.variable = arb_poly([self.t0, 1])
        self.scalar = {}
        self.scalar_derivative = {}
        for key in ('A', 'C'):
            polys = [arb_poly([arb(v) for v in co])(self.variable)
                     for co in comp[key]]
            self.scalar[key] = polys
            self.scalar_derivative[key] = [p.derivative() for p in polys]
        self.modes = []
        for source in comp['modes']:
            p, L, J = source['P'], source['L'], source['J']
            degree = max(len(p) - 1, L, 160)
            shift = arb_poly([arb(v) for v in p])(self.variable)
            primitive = arb_poly([-rational(v, j - L) if j != L else arb(0)
                                  for j, v in enumerate(p)])
            b0 = primitive(self.t0) + self.t0 ** L * rational(*source['moment'])
            if L < len(p):
                b0 -= p[L] * self.t0 ** L * self.t0.log()
            coefficients = [b0]
            for j in range(degree + 1):
                coefficients.append(((L - j) * coefficients[j] - shift[j])
                                    / (self.t0 * (j + 1)))
            outer = arb_poly([rational(v, j + J)
                              for j, v in enumerate(source['Q'])])(self.variable)
            self.modes.append({'k': source['k'], 'degree': degree,
                               'polynomial': arb_poly(coefficients[:-1]),
                               'next': coefficients[-1], 'outer': outer})

    def radial(self, t):
        q = 1 - t ** 4
        assert 0 < t < 1 and 0 < q < 1
        delta = t - self.t0
        bound = upper_abs(delta)
        ratio = bound / self.t0
        assert ratio < 1
        data = {'t': t, 'q': q, 'A': [], 'C': [], 'At': [], 'Ct': [],
                'X': [], 'Y': [], 'remainders': []}
        D = self.comp['denominator']
        for key in ('A', 'C'):
            data[key] = [p(delta) / D for p in self.scalar[key]]
            data[key + 't'] = [p(delta) / D for p in self.scalar_derivative[key]]
        for mode in self.modes:
            k, degree = mode['k'], mode['degree']
            error = (upper_abs(mode['next']) * bound ** (degree + 1)
                     / (1 - ratio)).upper()
            inner = plus_error(mode['polynomial'](delta), error)
            outer = mode['outer'](delta)
            data['X'].append(q ** (-k) * inner / (4 * D))
            data['Y'].append(q ** k * outer / (4 * D))
            data['remainders'].append(error)
        return data

    def evaluate(self, x, y):
        x, y = arb(x), arb(y)
        r2 = x * x + y * y
        assert r2 > 0 and x > 0 and y > 0
        r = r2.sqrt()
        t = 1 / (1 + r2).sqrt().sqrt()
        v = self.radial(t)
        q, D = v['q'], self.comp['denominator']
        phi = (y / x).atan()
        cs = [(2 * j * phi).cos() for j in range(self.comp['M'] + 1)]
        sn = [(2 * j * phi).sin() for j in range(self.comp['M'] + 1)]
        a = at = ap = C = arb(0)
        for m, (am, amt, cm) in enumerate(zip(v['A'], v['At'], v['C'])):
            qm = q ** m
            a += qm * am * cs[m]
            at += qm * (amt - 4 * m * t ** 3 * am / q) * cs[m]
            ap -= 2 * m * qm * am * sn[m]
            C += qm * cm * cs[m]
        tx, ty = -x * t ** 5 / 2, -y * t ** 5 / 2
        ax, ay = at * tx - ap * y / r2, at * ty + ap * x / r2
        theta = x * x * y * t ** 6 * a
        thx = 2 * x * y * t ** 6 * a + x * x * y * (6 * t ** 5 * tx * a + t ** 6 * ax)
        thy = x * x * t ** 6 * a + x * x * y * (6 * t ** 5 * ty * a + t ** 6 * ay)
        omega = x * y * t ** 5 * C
        psi = pr = pp = prr = prp = ppp = arb(0)
        for k, (X, Y) in enumerate(zip(v['X'], v['Y']), 1):
            n = 2 * k
            h = t ** (-3) * (X + Y) / (4 * k)
            hp = t ** (-3) * (-X + Y) / (2 * r)
            cp = v['C'][k + 1] if k + 1 < self.comp['M'] else arb(0)
            dk = rational(1, 2 if k == 1 else 4)
            Bn = q * t * (dk * q ** (k - 1) * v['C'][k - 1] - q ** (k + 1) * cp / 4)
            hpp = -hp / r + n * n * h / r2 - Bn
            psi += h * sn[k]
            pr += hp * sn[k]
            pp += n * h * cs[k]
            prr += hpp * sn[k]
            prp += n * hp * cs[k]
            ppp -= n * n * h * sn[k]
        ec, es = x / r, y / r
        mixed, transverse = prp / r - pp / r2, pr / r + ppp / r2
        hxx = prr * ec ** 2 - 2 * mixed * ec * es + transverse * es ** 2
        hxy = (prr - transverse) * ec * es + mixed * (ec ** 2 - es ** 2)
        hyy = prr * es ** 2 + 2 * mixed * ec * es + transverse * ec ** 2
        u1, u2 = -(es * pr + ec * pp / r), ec * pr - es * pp / r
        w1, w2 = 2 * x + u1, 2 * y + u2
        return {'x': x, 'y': y, 't': t, 'Theta': theta, 'Theta_x': thx, 'Theta_y': thy,
                'Omega': omega, 'Psi': psi, 'U1': u1, 'U2': u2, 'W1': w1, 'W2': w2,
                'DW00': 2 - hxy, 'DW01': -hyy, 'DW10': hxx, 'DW11': 2 + hxy,
                'Psi_xx': hxx, 'Psi_xy': hxy, 'Psi_yy': hyy,
                'elliptic_identity_interval': -hxx - hyy - omega,
                'R_Theta': w1 * thx + w2 * thy,
                'largest_inner_series_remainder': max(v['remainders'])}

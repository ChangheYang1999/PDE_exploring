"""Exact compact radial rational functions and Cartesian derivatives."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import json
from flint import fmpq as Q, fmpq_poly as Poly, arb, arb_poly, acb, ctx

T = Poly([0, 1])
V = Poly([1, -1])
SCALES = (Q(624), Q(2499), Q(9999))
ZEROS = (0,) * len(SCALES)
LINEARS = tuple(1+a*V for a in SCALES)


def rational(value):
    if isinstance(value, float):
        raise TypeError('an exact rational is required')
    x = Fraction(str(value))
    return Q(x.numerator, x.denominator)


def ar(q):
    q = Q(q)
    return arb(q.numerator)/arb(q.denominator)


def aspoly(value):
    if isinstance(value, Poly):
        return value
    return Poly([Q(value)])


class Rat:
    __slots__ = ('P', 'powers', '_v', '_arb')

    def __init__(self, P=0, powers=ZEROS):
        if isinstance(P, Rat):
            assert powers == ZEROS
            self.P, self.powers = P.P, P.powers
        else:
            self.P = aspoly(P)
            assert len(powers) == len(SCALES) and all(isinstance(k, int) and k >= 0 for k in powers)
            self.powers = tuple(powers) if self.P else ZEROS
        self._v = None
        self._arb = {}

    def __bool__(self):
        return bool(self.P)

    def __neg__(self):
        return Rat(-self.P, self.powers)

    def __add__(self, other):
        other = Rat(other)
        if not self:
            return other
        if not other:
            return self
        powers = tuple(max(a, b) for a, b in zip(self.powers, other.powers))
        left, right = self.P, other.P
        for L, p, a, b in zip(LINEARS, powers, self.powers, other.powers):
            left = left * L**(p-a)
            right = right * L**(p-b)
        return Rat(left+right, powers)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-Rat(other))

    def __rsub__(self, other):
        return Rat(other) + (-self)

    def __mul__(self, other):
        other = Rat(other)
        return Rat(self.P*other.P, tuple(a+b for a, b in zip(self.powers, other.powers)))

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        q = Q(scalar)
        assert q
        return Rat(self.P/q, self.powers)

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        return Rat(self.P**n, tuple(p*n for p in self.powers))

    def __eq__(self, other):
        try:
            return not (self-Rat(other))
        except (TypeError, ValueError):
            return False

    def derivative(self):
        result = Rat(self.P.derivative(), self.powers)
        for i, (a, power) in enumerate(zip(SCALES, self.powers)):
            if power:
                powers = list(self.powers)
                powers[i] += 1
                result += Rat(a*power*self.P, tuple(powers))
        return result

    def divide_t(self, k):
        assert k >= 0 and all(self.P[i] == 0 for i in range(k))
        return Rat(Poly(list(self.P)[k:]), self.powers)

    def numerator_v(self):
        if self._v is None:
            self._v = self.P(V)
        return self._v

    def evaluate(self, t, v):
        endpoint = bool(t >= arb('0.5'))
        key = (ctx.prec, endpoint)
        if key not in self._arb:
            P = self.numerator_v() if endpoint else self.P
            self._arb[key] = arb_poly([ar(q) for q in P])
        result = self._arb[key](v if endpoint else t)
        for a, k in zip(SCALES, self.powers):
            if k:
                result /= (1+ar(a)*v)**k
        return result

    def exact_value(self, t):
        t = Q(t)
        value = self.P(t)
        for L, k in zip(LINEARS, self.powers):
            value /= L(t)**k
        return value

    def record(self):
        return {'numerator': [str(q) for q in self.P], 'powers': list(self.powers)}


TR, VR = Rat(T), Rat(V)


def add(out, key, value):
    if value:
        out[key] = out.get(key, Rat()) + value


def fold(out, j, n, value, kind):
    if n == 0 and kind == 's':
        return
    if n < 0:
        n, value = -n, (-value if kind == 's' else value)
    add(out, (j, n), value)


def combine(left, right, scale=1):
    out = left.copy()
    for key, value in right.items():
        add(out, key, value*scale)
    return {k: v for k, v in out.items() if v}


def legendre(n):
    p0 = Poly([1])
    if n == 0:
        return p0
    p1 = T
    for k in range(1, n):
        p0, p1 = p1, ((2*k+1)*T*p1-k*p0)/(k+1)
    return p1


def generator(m, spec):
    kind = spec[0]
    w = int(spec[1])
    n = int(spec[2]) if kind != 'mono' else 0
    q = int(spec[3]) if kind in ['legq', 'legqs'] else 0
    R = rational(spec[4]) if kind == 'legqs' else Q(1)
    assert kind in ['mono', 'leg', 'legq', 'legqs'] and min(m, w, n, q) >= 0
    a = R*R-1
    assert a == 0 or a in SCALES
    L = 1+a*V
    polynomial = legendre(n)
    numerator = sum((coefficient*(2*T-L)**k*L**(n-k)
                     for k, coefficient in enumerate(polynomial)), Poly([]))
    numerator *= T**(m+w)*(R*R*V)**q
    powers = [0] * len(SCALES)
    if a:
        powers[SCALES.index(a)] = w+q+n
    return Rat(numerator, tuple(powers))


class ScaledRadial:
    def __init__(self, data):
        if isinstance(data, (str, Path)):
            data = json.loads(Path(data).read_text())
        self.state = data
        self.c = rational(data.get('cl', data.get('cl_exact')))
        self.g = 1/self.c
        self.delta = 1-self.g
        assert self.c > 1
        if 'generators' in data:
            generators = data['generators']
        else:
            generators = [{'j': j, 'm': m, 'spec': ['mono', k-m], 'coef': a}
                          for (j, m, k), a in zip(data['order'], data['coefficients'], strict=True)]
        self.p = {int(g['j']): (3+self.g-int(g['j'])*self.delta)/2 for g in generators}
        fields, cache = {}, {}
        for g in generators:
            a = rational(g['coef'])
            if not a:
                continue
            j, m = int(g['j']), int(g['m'])
            key = (m, tuple(g['spec']))
            if key not in cache:
                cache[key] = generator(m, g['spec'])
            add(fields, (j, 2*m), cache[key]*a)
        self.derivatives = {(0, 0): {k: v for k, v in fields.items() if v}}
        self.rho = {k: -v for k, v in combine(self.deriv(2, 1), self.deriv(0, 3)).items()}
        self.u1 = {k: -v for k, v in self.deriv(1, 2).items()}
        self.u2 = self.deriv(2, 1)
        self.rx = {k: -v for k, v in combine(self.deriv(3, 1), self.deriv(1, 3)).items()}
        self.ry = {k: -v for k, v in combine(self.deriv(2, 2), self.deriv(0, 4)).items()}
        self.fields = {'rho': (self.rho, 3, 's'), 'u1': (self.u1, 3, 'c'),
                       'u2': (self.u2, 3, 's'), 'rho_x': (self.rx, 4, 's'),
                       'rho_y': (self.ry, 4, 'c')}

    def differentiate(self, field, d, kind, axis):
        target = ('c' if kind == 's' else 's') if axis == 'y' else kind
        out = {}
        for (j, n), A in field.items():
            TA = A.derivative()*TR
            common = TA+(A*self.p[j]-TA)*TR
            minus, plus = common+A*Q(n-d, 2), common-A*Q(n+d, 2)
            if axis == 'y':
                minus *= 1 if kind == 's' else -1
                plus *= -1 if kind == 's' else 1
            fold(out, j, n-1, minus, target)
            fold(out, j, n+1, plus, target)
        return {k: v for k, v in out.items() if v}

    def deriv(self, x, y):
        if (x, y) not in self.derivatives:
            previous = (x, y-1) if y else (x-1, y)
            field = self.deriv(*previous)
            kind = 's' if previous[1]%2 else 'c'
            self.derivatives[x, y] = self.differentiate(field, sum(previous), kind, 'y' if y else 'x')
        return self.derivatives[x, y]

    def evaluate(self, xs, ys):
        x, y = ar(rational(xs)), ar(rational(ys))
        r2 = x*x+y*y
        r = r2.sqrt()
        assert r > 0
        v, t = 1/(1+r2), r2/(1+r2)
        z = acb(x/r, y/r)
        maximum = max(n for fields, d, kind in self.fields.values() for j, n in fields)
        powers = [acb(1)]
        for k in range(maximum):
            powers.append(powers[-1]*z)
        radial_powers = {j: (1+r2)**ar(p) for j, p in self.p.items()}
        values = {}
        for label, (field, d, kind) in self.fields.items():
            answer = arb(0)
            for (j, n), A in field.items():
                trig = powers[n].real if kind == 'c' else powers[n].imag
                answer += radial_powers[j]*r**(-d)*A.evaluate(t, v)*trig
            values[label] = answer
        values['residual'] = (ar(self.c)*x+values['u1'])*values['rho_x']+(ar(self.c)*y+values['u2'])*values['rho_y']-values['rho']
        return values


def field_hash(field):
    h = sha256()
    for key, A in sorted(field.items()):
        h.update((json.dumps([key, A.record()], separators=(',', ':'))+'\n').encode())
    return h.hexdigest()

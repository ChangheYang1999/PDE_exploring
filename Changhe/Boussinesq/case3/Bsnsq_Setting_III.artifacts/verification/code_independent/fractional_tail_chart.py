"""Own packet116 chart, retaining the determined constant vertical tail.

The exact decoder uses Python Fraction; the fit evaluates our packet114
physical derivative matrices. No NUM code or state lineage is used here.
"""
from collections import OrderedDict
from fractions import Fraction as Q
import numpy as np
from stream_basis import StreamBasis
from free_beta_stream import prepare_divided, divided_fields


def keys(n, J, stream=True):
    out = [(0, j, 0) for j in range(J)]
    out += [(i, j, d) for d in (0, 1) for i in range(1, n)
            for j in range(J + d)]
    pivots = {(1, 0, 0), (2, 0, 0), (1, 1, 0)} if stream else {(1, 0, 0)}
    return [key for key in out if key not in pivots]


def labels(n, J):
    return [(i, j, d) for d in (0, 1) for i in range(n) for j in range(J+1)]


def cheb_center(j):
    v = 0 if j % 2 else (-1)**(j//2)
    w = 0 if not j % 2 else j*(-1)**((j-1)//2)
    return v, w


def moments(beta, cs, n, J, stream=True):
    s = 1/beta
    gamma = strain = b0 = beta*0
    for coefficient, (i, j, d) in zip(cs, labels(n, J)):
        v, w = cheb_center(j)
        gamma += coefficient*v
        if stream:
            strain += coefficient*w
            b0 -= coefficient*(4*(1-s-d-2*i*i*s)-j*j)*v
    return (gamma, strain, b0) if stream else gamma


def decode_field(beta, eta, a0, n, J, free, stream=True):
    """Scalar-generic exact formulas; use Fraction inputs for exact output."""
    if not 2 < beta < 3 or n < 3 or J < 2 or not a0:
        raise ValueError('packet116 requires 2<beta<3, n>=3, J>=2, a0!=0')
    free_keys = keys(n, J, stream)
    if len(free) != len(free_keys):
        raise ValueError('chart dimension mismatch')
    zero = beta*0
    cs = [zero for _ in labels(n, J)]
    ind = {key: k for k, key in enumerate(labels(n, J))}
    s = 1/beta
    power = 1-s if stream else -1-2*s
    def core(i, j, d, value):
        cs[ind[i, j, d]] += value
        cs[ind[0, j, d]] -= (-1)**i*value
    for (i, j, d), value in zip(free_keys, free):
        if i:
            core(i, j, d, value)
        else:
            cs[ind[0, j, 0]] += value
            if j == 0:
                cs[ind[0, 1, 1]] += value*eta/beta*power
            else:
                cs[ind[0, j-1, 1]] += value*eta/beta*(power+j)/2
                cs[ind[0, j+1, 1]] += value*eta/beta*(power-j)/2
    if stream:
        gamma, strain, b0 = moments(beta, cs, n, J)
        v1 = (-eta-gamma)/2
        v3 = (1+beta/2-strain)/2
        v2 = (4*a0/beta-b0+8*(1-2*s)*v1)/(32*s)
        core(1, 0, 0, v1)
        core(2, 0, 0, v2)
        core(1, 1, 0, v3)
    else:
        center = moments(beta, cs, n, J, False)
        core(1, 0, 0, (a0-center)/2)
    return cs


def exact_state(beta, eta, a0, n, J, freeC, freeD):
    beta, eta, a0 = map(Q, (beta, eta, a0))
    uc, ud = list(map(Q, freeC)), list(map(Q, freeD))
    C = decode_field(beta, eta, a0, n, J, uc, True)
    D = decode_field(beta, eta, a0, n, J, ud, False)
    assert moments(beta, C, n, J) == (-eta, 1+beta/2, 4*a0/beta)
    assert moments(beta, D, n, J, False) == a0
    return {'beta': str(beta), 'eta': str(eta), 'a0': str(a0), 'ni': n,
            'nj': J+1, 'leading_angular_count': J, 'shifts': [0, 1],
            'labels': labels(n, J), 'C': list(map(str, C)), 'D': list(map(str, D)),
            'freeC': list(map(str, uc)), 'freeD': list(map(str, ud)),
            'representation': 'packet116 rationally reconstructed fractional-tail center chart'}


def verify_exact_state(data):
    """Reload all chart inputs and compare the complete reconstructed fields."""
    rebuilt = exact_state(data['beta'], data['eta'], data['a0'], data['ni'],
                          data['leading_angular_count'], data['freeC'], data['freeD'])
    import json
    for key, value in json.loads(json.dumps(rebuilt)).items():
        if data.get(key) != value:
            raise ValueError('exact chart mismatch: '+key)
    return True


class BetaCase:
    def __init__(self, beta, n, J, points, reference_beta=2.5, a0=1.):
        self.beta, self.n, self.J, self.a0 = float(beta), n, J, a0
        self.basis = StreamBasis(beta, n, J+1, a0=a0)
        self.data = prepare_divided(self.basis, points)
        self.nc, self.nd = len(keys(n, J)), len(keys(n, J, False))
        self.size = self.nc+self.nd
        self.maps = {}
        for name, count, stream in [('C', self.nc, True), ('D', self.nd, False)]:
            maps = []
            for eta in [0., 1.]:
                base = np.asarray(decode_field(self.beta, eta, a0, n, J, np.zeros(count), stream))
                mat = np.stack([np.asarray(decode_field(self.beta, eta, a0, n, J, np.eye(count)[k], stream))-base for k in range(count)], axis=1)
                maps.append((base, mat))
            b0, m0 = maps[0]
            self.maps[name] = b0, m0, maps[1][0]-b0, maps[1][1]-m0
        rad = np.sqrt(1+np.sum(np.asarray(points)**2, axis=1))
        self.wF = rad**(1+3/reference_beta)/a0/np.sqrt(len(rad))
        self.wG = rad**(1+2/reference_beta)/a0/np.sqrt(len(rad))
        self.last = None

    def coefficients(self, eta, u):
        result = []
        for name, part in [('C', u[:self.nc]), ('D', u[self.nc:])]:
            b0, m0, b1, m1 = self.maps[name]
            result.append(b0+eta*b1+(m0+eta*m1)@part)
        return result

    def residual(self, eta, u):
        C, D = self.coefficients(eta, u)
        q = divided_fields(self.basis, self.data, C, D)
        self.last = (eta, u.copy(), q)
        return np.r_[self.wF*q['RF'], self.wG*q['RG']]

    def jacobian_eta_coefficients(self, eta, u):
        if self.last is None or self.last[0] != eta or not np.array_equal(self.last[1], u):
            self.residual(eta, u)
        q = self.last[2]
        directions = {}
        for name, part in [('C', u[:self.nc]), ('D', u[self.nc:])]:
            b0, m0, b1, m1 = self.maps[name]
            cols = np.zeros((len(b0), 1+self.size))
            cols[:, 0] = b1+m1@part
            sl = slice(1, 1+self.nc) if name == 'C' else slice(1+self.nc, 1+self.size)
            cols[:, sl] = m0+eta*m1
            directions[name] = {k: mat@cols for k, mat in self.data[name].items()}
        c, d = directions['C'], directions['D']
        x = self.data['points'][:, 0, None]
        col = lambda k: q[k][:, None]
        df = (c['aV']*(2*col('f')+x*col('fx'))
              + col('A')*(2*d['f']+x*d['fx'])
              + c['U2']*col('fy') + col('B')*d['fy'] - (self.beta-2)*d['f'])
        dg = (c['aV']*(col('g')+x*col('gx'))
              + col('A')*(c['g']+x*c['gx']) + c['U2']*col('gy')
              + col('B')*c['gy'] + c['g'] - (2*d['f']+x*d['fx']))
        return np.vstack((self.wF[:, None]*df, self.wG[:, None]*dg))


class FractionalTailProblem:
    def __init__(self, n, J, points, reference_beta=2.5, a0=1.):
        self.n, self.J, self.points = n, J, np.asarray(points, float)
        self.reference_beta, self.a0 = reference_beta, a0
        self.cache = OrderedDict()
        self.rebuilds = 0

    def case(self, beta):
        beta = float(beta)
        if beta not in self.cache:
            self.cache[beta] = BetaCase(beta, self.n, self.J, self.points, self.reference_beta, self.a0)
            self.rebuilds += 1
        self.cache.move_to_end(beta)
        while len(self.cache) > 3:
            self.cache.popitem(last=False)
        return self.cache[beta]

    def residual(self, z):
        return self.case(z[0]).residual(z[1], z[2:])

    def jacobian(self, z):
        beta, eta = z[:2]
        jac = self.case(beta).jacobian_eta_coefficients(eta, z[2:])
        h = min(1e-5*max(1., beta), (beta-2)/4, (3-beta)/4)
        jb = (self.case(beta+h).residual(eta, z[2:])-self.case(beta-h).residual(eta, z[2:]))/(2*h)
        return np.column_stack((jb, jac))

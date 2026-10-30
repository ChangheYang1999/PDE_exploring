"""Exact scaled-generator origin and homogeneous residual coefficients."""
from pathlib import Path
from collections import defaultdict
from math import comb
import sys
sys.set_int_max_str_digits(0)
from flint import fmpq as Q

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/multiscale_generators/code'))
sys.path.insert(0, str(ROOT / 'research/sector_audit/code'))
from moments import coefficients, homogenized_legendre, choose
from cartesian import spec_parts, rational
from sectors_flint import dx, dy, add, product_cs


def origin_radial(p, m, spec, order):
    """Coefficients of s^0,...,s^order, excluding the harmonic polynomial."""
    w, n, q, R = spec_parts(spec)
    out = [Q(0)] * (order + 1)
    if w > order:
        return out
    A = homogenized_legendre(n)
    for l in range(order - w + 1):
        out[l+w] = (-1)**n * R**(-2*w) * sum(
            (A[h] * R**(-2*h) * choose(p-m, j)
             * choose(Q(-w-q-n), l-h-j) * R**(-2*(l-h-j))
             for h in range(min(l, A.degree())+1)
             for j in range(l-h+1)), Q(0))
    return out


def origin(data):
    c = rational(data.get('cl', data.get('cl_exact')))
    gamma, delta = 1/c, 1-1/c
    b22, b04 = Q(0), Q(0)
    for g in data['generators']:
        m, j, a = int(g['m']), int(g['j']), rational(g['coef'])
        if m > 2 or not a:
            continue
        p, l = (3+gamma-j*delta)/2, 2-m
        value = a * origin_radial(p, m, g['spec'], l)[l]
        for k in range(m+1):
            for t in range(l+1):
                term = value * (-1)**k * comb(2*m, 2*k) * comb(l, t)
                if k+t == 1:
                    b22 += term
                if k+t == 2:
                    b04 += term
    return {'strain': 4*b22, 'a0': -4*b22-24*b04,
            'x2y2_coefficient': b22, 'y4_coefficient': b04}


def sectors(data, qmax=1, hmax=None):
    c = rational(data.get('cl', data.get('cl_exact')))
    assert c > 1 and qmax >= 1
    gamma, delta = 1/c, 1-1/c
    generators = data['generators']
    J = max(int(g['j']) for g in generators)
    hstop = 2*J+1 if hmax is None else min(hmax, 2*J+1)
    assert hstop >= 0
    assert all(int(g['j']) >= 0 and int(g['m']) >= 0 for g in generators)
    C = {(j,q): {} for j in range(J+1) for q in range(qmax+1)}
    cache = {}
    for g in generators:
        j, m, a = int(g['j']), int(g['m']), rational(g['coef'])
        key = (j, m, tuple(g['spec']))
        if key not in cache:
            w,n,qd,R = spec_parts(g['spec'])
            p = (3+gamma-j*delta)/2
            cache[key] = coefficients(p,m,w,n,qd,R,qmax)
        for q,value in enumerate(cache[key]):
            if a*value:
                C[j,q][2*m] = C[j,q].get(2*m,Q(0)) + a*value
    C = {key:{n:v for n,v in poly.items() if v} for key,poly in C.items()}
    alpha = lambda j,q: gamma-j*delta-2*q
    G,V1,V2,X,Y = {},{},{},{},{}
    for key,poly in C.items():
        s = alpha(*key)+3
        lap = {n:(s*s-n*n)*v for n,v in poly.items()}
        G[key] = {n:-v for n,v in dy(lap,s-2,'c').items()}
        xy = dy(dx(poly,s,'c'),s-1,'c')
        V1[key] = {n:-v for n,v in dy(xy,s-2,'s').items()}
        V2[key] = dx(xy,s-2,'s')
        X[key] = dx(G[key],s-3,'s')
        Y[key] = dy(G[key],s-3,'s')
    E = {}
    for h in range(hstop+1):
        for q in range(qmax+1):
            value = {n:(c*alpha(h,q)-1)*v for n,v in G.get((h,q),{}).items()}
            for i in range(J+1):
                j = h-i-1
                if not 0 <= j <= J:
                    continue
                for u in range(q+1):
                    v = q-u
                    value = add(value, product_cs(V1[i,u],X[j,v]))
                    value = add(value, product_cs(Y[j,v],V2[i,u]))
            E[h,q] = {n:v for n,v in value.items() if v}
    grouped = {}
    for key,value in E.items():
        exponent = alpha(*key)
        grouped[exponent] = add(grouped.get(exponent,{}),value)
    leading = next(((exponent,poly) for exponent,poly in
                    sorted(grouped.items(),reverse=True) if poly), None)
    omitted_maximum = gamma-2*(qmax+1)
    if hstop < 2*J+1:
        omitted_maximum = max(omitted_maximum, gamma-(hstop+1)*delta)
    summary = {
        'all_forbidden_zero': omitted_maximum < -2 and all(not poly for a,poly in grouped.items() if a>=-2),
        'forbidden_prefix_complete': omitted_maximum < -2,
        'hmax': hstop,
        'qmax': qmax,
        'forbidden_exponent_count': sum(a>=-2 for a in grouped),
        'formal_sector_count': len(E),
        'distinct_exponent_count': len(grouped),
        'omitted_exponent_upper_bound': str(omitted_maximum),
        'leading_exponent': str(leading[0]) if leading else None,
        'leading_certified_by_complete_prefix': bool(leading and leading[0]>omitted_maximum),
        'maximum_scale': str(max(spec_parts(g['spec'])[3] for g in generators)),
    }
    return alpha,C,G,E,grouped,summary

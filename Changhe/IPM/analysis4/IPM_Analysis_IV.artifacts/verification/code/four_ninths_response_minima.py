"""Exact four-ninths response-minimum audit with independent finite recurrences."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import ast
import gzip
import json
import sys
import time
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from flint import fmpq, fmpq_poly, arb, ctx
import sympy as sp
import tuned_cartesian_exact as ce
from compact_response_bounds import Response
from pure_cartesian_ball import refine_root
from general_rational_majorant import RationalMajorant
from general_component_radius import stringify

ROOT = Path('research/164_four_ninths_response_minima')
START = time.monotonic()
b, k = sp.symbols('b k')
ce.p = lambda n: 1-ce.K(4)*n/9


def put(name, data):
    raw = (json.dumps(stringify(data), indent=2, default=str)+'\n').encode()
    path = ROOT/'verification'/name
    path.write_bytes(gzip.compress(raw, mtime=0) if name.endswith('.gz') else raw)


def imul(a, z):
    values = [x*y for x in a for y in z]
    return min(values), max(values)


def ev(a, interval):
    v = (F(0), F(0))
    for c in reversed(a):
        lo, hi = imul(v, interval)
        v = lo+c, hi+c
    return v


def ab(v):
    lo, hi = v
    assert lo > 0 or hi < 0, ('unresolved sign', str(v))
    return v if lo > 0 else (-hi, -lo)


def coeff(expr, var=b):
    p = sp.Poly(expr, var, domain=sp.QQ)
    return [F(str(p.nth(j))) for j in range(p.degree()+1)]


def flpoly(expr):
    return fmpq_poly([fmpq(str(v)) for v in coeff(expr, k)])


def loadfield(data):
    return ce.F(ce.K.from_expr(sp.sympify(data['radial_exponent'])),
                {ast.literal_eval(m): ce.R.from_expr(sp.sympify(v))
                 for m, v in data['signed_laurent'].items()})


def small_response(kvalue, lowf, lowg):
    n = 9*kvalue
    e = ce.sine(ce.p(n)+1, 4*kvalue-2)
    density, stream = {}, {}
    for r in range(1, 10):
        total = ce.adv(e, lowf[r])
        for s in range(1, r):
            total = total+ce.adv(stream[s], lowf[r-s])+ce.adv(lowg[r-s], density[s])
        density[r] = total.scale(ce.K(5)/(4*(n+r-1)))
        density[r].check_sine()
        if r < 9:
            stream[r] = ce.poisson(density[r])
    return coeff(density[9].sine(4*kvalue+1).as_expr())


def run():
    ctx.prec = 768
    source = Path('../a4-lead/code/tuned/tq_sigma_Q9h2.cache.json')
    raw = source.read_bytes()
    cache = json.loads(raw)
    frozen = ROOT/'sources/lead_generic_cache.json.gz'
    frozen.write_bytes(gzip.compress(raw, mtime=0))
    assert gzip.decompress(frozen.read_bytes()) == raw
    dependencies = {str(source): dict(sha256=sha256(raw).hexdigest(), bytes=len(raw))}
    degree = max(j for i, j, p, q in cache['num'])
    bdegree = max(i for i, j, p, q in cache['num'])
    cc = [[fmpq(0)]*(degree+1) for _ in range(bdegree+1)]
    for i, j, p, q in cache['num']:
        cc[i][j] = fmpq(int(p), int(q))
    columns = [fmpq_poly(row) for row in cc]
    dd = [fmpq(0)]*(max(j for j, p, q in cache['den'])+1)
    for j, p, q in cache['den']:
        dd[j] = fmpq(int(p), int(q))
    den = fmpq_poly(dd)
    common = den
    for p in columns:
        common = common.gcd(p)
    original_degree = den.degree()
    quotients = []
    for p in columns+[den]:
        quotient, remainder = divmod(p, common)
        assert not remainder
        quotients.append(quotient)
    columns, den = quotients[:-1], quotients[-1]
    if den[den.degree()] < 0:
        columns, den = [-p for p in columns], -den
    put('reduced_generic.json.gz', dict(original_degree=original_degree,
        canceled_degree=common.degree(), denominator=[str(x) for x in den.coeffs()],
        numerator_by_b_degree=[[str(x) for x in p.coeffs()] for p in columns],
        canceled_factor=[str(x) for x in common.coeffs()], source=dependencies))
    edgechecks = []
    for mode, col in [(1, 0), (3, 9)]:
        path = Path(f'research/146_four_ninths_profiles/verification/mode{mode}_generic.json')
        data = json.loads(path.read_text())
        expr = sp.sympify(data['sigma'])
        nn, dd = sp.fraction(expr)
        assert columns[col]*flpoly(dd) == den*flpoly(nn)
        dependencies[str(path)] = dict(sha256=sha256(path.read_bytes()).hexdigest())
        edgechecks.append(dict(mode=mode, b_degree=col, rational_functions_exactly_equal=True))
    path = Path('research/144_general_rational_response_limit/verification/h2_Q9.json')
    lowdata = json.loads(path.read_text())
    dependencies[str(path)] = dict(sha256=sha256(path.read_bytes()).hexdigest())
    limit = coeff(sp.sympify(lowdata['sigma_infinity']))
    assert len(limit) == bdegree+1
    assert all(F(str(p[den.degree()]/den[den.degree()])) == v for p, v in zip(columns, limit))
    assert all(p.degree() <= den.degree() for p in columns)
    lowf = {int(n): loadfield(v) for n, v in lowdata['low_density'].items()}
    lowg = {int(n): loadfield(v) for n, v in lowdata['low_stream'].items()}
    small = {}
    completed_path = ROOT/'verification/small_responses.json'
    if completed_path.exists():
        completed = json.loads(completed_path.read_text())
        small = {int(row['k']): [F(value) for value in row['coefficients']]
                 for row in completed['rows']}
    for j in range(1, 10):
        if j in small:
            print(json.dumps(dict(stage='reused_exact_small', k=j)), flush=True)
            continue
        small[j] = small_response(j, lowf, lowg)
        put('small_responses.json', dict(rows=[dict(k=q, coefficients=a) for q, a in small.items()]))
        print(json.dumps(dict(stage='independent_small', k=j,
                              actual_elapsed_s=time.monotonic()-START)), flush=True)
    def fixed(j):
        if j in small:
            return small[j]
        denominator = den(j)
        assert denominator
        return [F(str(p(j)/denominator)) for p in columns]
    shifts = {}
    def shifted(K):
        if K not in shifts:
            argument = fmpq_poly([K, 1])
            d = den(argument)
            nn = [p(argument) for p in columns]
            dd = [F(str(x)) for x in d.coeffs()]
            assert all(x > 0 for x in dd)
            mat = [[F(str(p[j])) for p in nn] for j in range(len(dd))]
            shifts[K] = mat, dd
        return shifts[K]
    rootsource = Path('research/146_four_ninths_profiles/verification/algebraic_certificates.json')
    rootdata = json.loads(rootsource.read_text())
    dependencies[str(rootsource)] = dict(sha256=sha256(rootsource.read_bytes()).hexdigest())
    rows = []
    for index, (rootinfo, targetk, K) in enumerate(zip(rootdata['real_roots'], [7,4,13,None,5], [10,10,24,10,10]), 1):
        rootball, interval = refine_root(rootdata['primitive_coefficients'], rootinfo['interval'], 320)
        I = tuple(map(F, interval))
        response = Response(2, 9, rootball)
        direct = []
        for j in list(range(1, 10))+[10, 11, 12, 13, 14, 23, 24, 50]:
            value = response.full(j)
            exact = ev(fixed(j), I)
            expected = arb(fmpq(str(exact[0]))).union(arb(fmpq(str(exact[1]))))
            assert value.overlaps(expected), ('Cartesian comparison', index, j)
            direct.append(dict(k=j, cartesian=value.str(45, radius=True),
                               exact_interval=list(map(str, exact))))
        targetraw = limit if targetk is None else fixed(targetk)
        raw = ev(targetraw, I)
        sign = 1 if raw[0] > 0 else -1
        target = [sign*x for x in targetraw]
        target_iv = ev(target, I)
        assert target_iv[0] > 0
        limit_iv = ev(limit, I)
        tail_sign = 1 if limit_iv[0] > 0 else -1
        ab(limit_iv)
        if targetk is not None:
            assert ab(limit_iv)[0] > target_iv[1]
        finite = []
        for j in range(1, K):
            signed = ev(fixed(j), I)
            absolute = ab(signed)
            gap = F(0) if j == targetk else absolute[0]-target_iv[1]
            assert j == targetk or gap > 0, ('finite gap', index, j)
            finite.append(dict(k=j, signed_interval=signed, absolute_interval=absolute,
                               gap_lower=gap))
        mat, shifted_den = shifted(K)
        tail = []
        zero_coefficients = []
        for j, (column, denominator) in enumerate(zip(mat, shifted_den)):
            diff = [tail_sign*v-denominator*(target[m] if m < len(target) else 0)
                    for m, v in enumerate(column)]
            exact_zero = all(v == 0 for v in diff)
            bound = ev(diff, I)
            if exact_zero:
                zero_coefficients.append(j)
            else:
                assert bound[0] > 0, ('tail coefficient', index, j)
            tail.append(dict(t_degree=j, bound=bound, denominator=denominator,
                             exact_zero=exact_zero))
        assert tail[0]['bound'][0] > 0
        assert zero_coefficients == ([len(tail)-1] if targetk is None else [])
        scale = 1
        while target_iv[0]*scale < 100:
            scale *= 10
        s = F((target_iv[0]*scale).__floor__(), scale)
        assert 0 < s < target_iv[0]
        norm = 1+max(map(abs, I))
        a = F((norm*100).__floor__()+1, 100)
        m = RationalMajorant(2, 9, 4, a, s)
        box = [2*v for v in m.Y0]
        q = 1
        while any(v >= w for v, w in zip(m.transformed(F(1, 2**q), box), box)):
            q *= 2
        lo, hi = q//2, q
        while hi-lo > 1:
            qmid = (lo+hi)//2
            if all(v < w for v, w in zip(m.transformed(F(1, 2**qmid), box), box)):
                hi = qmid
            else:
                lo = qmid
        q = hi
        image = m.transformed(F(1, 2**q), box)
        previous = m.transformed(F(1, 2**(q-1)), box)
        assert all(v < w for v, w in zip(image, box))
        assert any(v >= w for v, w in zip(previous, box))
        row = dict(root_index=index, root_interval=I, unique_minimizer=targetk,
            infimum_attained=targetk is not None, infimum_polynomial=target,
            infimum_interval=target_iv, infimum_approx=float(sum(target_iv)/2),
            finite_checks=finite, tail_from_k=K, tail_sign=tail_sign,
            tail_coefficients=tail, exact_zero_coefficients=zero_coefficients,
            full_cartesian_comparisons=direct, uniform_lower_bound=s,
            a=a, norm_upper=norm, z_dyadic_exponent=q, radius_dyadic_exponent=F(9*q,4),
            constant=m.constant, J=m.J, Y0=m.Y0, box=box, image=image,
            previous_image=previous, max_component_ratio=max(v/w for v,w in zip(image,box)))
        put(f'root{index}_certificate.json.gz', row)
        brief = {key:value for key,value in row.items() if key in ['root_index','root_interval',
            'unique_minimizer','infimum_attained','infimum_approx','uniform_lower_bound',
            'a','z_dyadic_exponent','radius_dyadic_exponent','max_component_ratio','tail_from_k']}
        rows.append(brief)
        put('checks.partial.json', dict(rows=rows))
        print(json.dumps(stringify(dict(root=index, k=targetk, minimum=row['infimum_approx'],
            s=s, q=q, radius=F(9*q,4), actual_elapsed_s=time.monotonic()-START))), flush=True)
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                  all_checks_pass=True, rows=rows, edge_function_checks=edgechecks,
                  limiting_polynomial_exactly_equal=True,
                  original_generic_degree=original_degree, canceled_degree=common.degree(),
                  reduced_generic_degree=den.degree(), dependencies=dependencies,
                  actual_elapsed_s=time.monotonic()-START)
    put('checks.json', result)
    for name in ['four_ninths_response_minima.py','tuned_cartesian_exact.py',
                 'compact_response_bounds.py','pure_cartesian_ball.py',
                 'general_rational_majorant.py','general_component_radius.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    (ROOT/'sources/lead_tq_radiush.py').write_bytes(Path('../a4-lead/code/tuned/tq_radiush.py').read_bytes())
    files = {str(p.relative_to(ROOT)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest())
             for p in ROOT.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and p.suffix!='.log'}
    put('MANIFEST.json', dict(files=files))
    print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)

if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        import traceback
        failure = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
            error_type=type(exc).__name__, error=str(exc), actual_elapsed_s=time.monotonic()-START,
            frames=[dict(file=Path(v.filename).name,line=v.lineno)
                    for v in traceback.extract_tb(exc.__traceback__)])
        put('FAILURE.json', failure)
        print(json.dumps(failure),flush=True)
        raise SystemExit(1)

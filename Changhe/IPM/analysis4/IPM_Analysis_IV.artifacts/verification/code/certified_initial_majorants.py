"""Use independently computed low coefficients in the proved rational majorant."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse
import json
import sys
import time
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from flint import arb, ctx
from gmpy2 import mpq
from pure_cartesian_ball import Tuning, sine, ball, refine_root
from general_rational_majorant import RationalMajorant, scalar_prefix, polynomial_rhs
from general_component_radius import polynomial_product, stringify

ROOT = Path('research/168_certified_initial_majorants')


def initial_majorant(h,Q,B,initial,s,improved=False,improved_poisson=False):
    assert len(initial) == Q and all(v>0 for v in initial)
    m = object.__new__(RationalMajorant)
    m.h,m.Q,m.B,m.a,m.s = h,Q,B,F(initial[0]),F(s)
    m.L = F(3*Q*Q,4*(3*Q-1)) if improved_poisson else F(Q,2)
    m.kappa = F(B*(Q-2*h),h)*(3-F(2*h,Q))
    if improved:
        delta = F(2*h,Q)
        m.kappa = B*(2-delta+max(delta,1-delta))*(1-delta)/delta*F(Q+1,Q)
    m.x = [F(0)]+list(map(F,initial))
    m.square = polynomial_product(m.x,m.x)
    m.squares = {r:polynomial_product([F(0)]*r+m.x[r:],[F(0)]*r+m.x[r:])
                for r in range(1,Q+1)}
    d = Q+1
    zero = [F(0)]*d
    m.constant = m.phi(F(0),zero)
    m.J = [[F(0)]*d for _ in range(d)]
    for j in range(d):
        e = zero.copy(); e[j] = F(1)
        col = m.phi(F(0),e)
        for i in range(d): m.J[i][j] = col[i]-m.constant[i]
    assert all(m.J[i][j] == 0 for i in range(d) for j in range(i,d))
    assert all(v>=0 for row in m.J for v in row)
    m.Y0 = m.precondition(m.constant)
    assert all(v>0 for v in m.Y0)
    test = [F(j+2,j+1) for j in range(d)]
    assert m.phi(F(0),test) == [m.constant[i]+sum(m.J[i][j]*test[j] for j in range(d)) for i in range(d)]
    coefficients = scalar_prefix(m,3)
    assert coefficients == polynomial_rhs(m,coefficients,3)
    return m


def pack(v):
    m,e = v.mid().man_exp(); r,re = v.rad().man_exp()
    return [str(m),int(e),str(r),int(re)]


def endpoints(v):
    m,e,r,re = pack(v)
    center,radius = F(int(m))*F(2)**e,F(int(r))*F(2)**re
    return center-radius,center+radius


def round_up(v):
    assert v>0
    scale = F(1)
    while v*scale<1000: scale*=10
    while v*scale>=10000: scale/=10
    return F((v*scale).__floor__()+1)/scale


def box_certificate(m):
    box = [2*v for v in m.Y0]
    q = 1
    while any(v>=w for v,w in zip(m.transformed(F(1,2**q),box),box)): q*=2
    lo,hi = q//2,q
    while hi-lo>1:
        k = (lo+hi)//2
        if all(v<w for v,w in zip(m.transformed(F(1,2**k),box),box)): hi=k
        else: lo=k
    image = m.transformed(F(1,2**hi),box)
    previous = m.transformed(F(1,2**(hi-1)),box)
    assert all(v<w for v,w in zip(image,box))
    assert any(v>=w for v,w in zip(previous,box))
    return dict(q=hi,radius_exponent=F(9*hi,4),constant=m.constant,J=m.J,Y0=m.Y0,
                box=box,image=image,previous_image=previous,
                maximum_ratio=max(v/w for v,w in zip(image,box)))


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--family', choices=['two_mode','candidate'], default='two_mode')
    parser.add_argument('--roots',default='1,2,3,4,5')
    parser.add_argument('--improved-kappa',action='store_true')
    parser.add_argument('--improved-poisson',action='store_true')
    parser.add_argument('--response',choices=['proved','sharp'],default='proved')
    args = parser.parse_args()
    start = time.monotonic();ctx.prec = 768
    rows = []
    for index in map(int,args.roots.split(',')):
        begin = time.monotonic()
        if args.family == 'two_mode':
            root_path = Path('research/146_four_ninths_profiles/verification/algebraic_certificates.json')
            roots = json.loads(root_path.read_text())
            b,I = refine_root(roots['primitive_coefficients'],roots['real_roots'][index-1]['interval'],832)
            initial = sine(mpq(5,9),1,arb(1))+sine(mpq(5,9),3,b)
            B = 4
            sharp_path = Path(f'research/164_four_ninths_response_minima/verification/root{index}_certificate.json.gz')
            if args.response == 'sharp':
                assert sharp_path.exists()
                import gzip
                response_data = json.loads(gzip.decompress(sharp_path.read_bytes()))
                s = F(response_data['uniform_lower_bound'])
                response_source = str(sharp_path)
            else:
                s = [F(1,2**29),F(1,2**24),F(1,2**25),F(1,2**14),F(1)][index-1]
                response_source = 'research/150_four_ninths_radii/PROOF.md'
        else:
            root_path = Path('research/156_candidate_shaped_compatibility/verification/checks.json')
            roots = json.loads(root_path.read_text())
            data = json.loads(Path('research/156_candidate_shaped_compatibility/verification/polynomial.json').read_text())
            b,I = refine_root(data['primitive_coefficients_ascending'],roots['roots'][index-1]['interval'],832)
            initial = sine(mpq(5,9),3,b)
            for mode,amplitude in data['fixed_normalized_coefficients'].items():
                initial = initial+sine(mpq(5,9),int(mode),ball(mpq(amplitude)))
            B = 20
            response_path = Path(f'research/{"158_candidate_shaped_response" if index==3 else "163_other_candidate_shaped_roots"}/verification/root{index}_checks.json')
            response_data = json.loads(response_path.read_text())
            assert response_data['all_index_lower_bound_proved']
            s = F(response_data['lower_bound'])
            response_source = str(response_path)
        solver = Tuning(2,9,B)
        f = {1:initial}; g = {1:solver.poisson(initial,1)}
        for n in range(2,10):
            f[n] = solver.order(n,f,g)
            if n<9: g[n] = solver.poisson(f[n],n)
        assert f[9].sine(1).contains(0)
        initial_rows = []
        d = []
        for n in range(1,10):
            value = f[n].norm()*n
            interval = endpoints(value)
            upper = round_up(interval[1])
            assert interval[1]<upper
            d.append(upper)
            initial_rows.append(dict(n=n,norm_times_n=value.str(60,radius=True),
                exact_dyadic=pack(value),exact_interval=interval,rational_upper=upper))
        m = initial_majorant(2,9,B,d,s,args.improved_kappa,args.improved_poisson)
        old = RationalMajorant(2,9,B,d[0],s)
        assert all(x<=y for x,y in zip(m.x,old.x))
        box = box_certificate(m)
        row = dict(root_index=index,family=args.family,root_interval=I,root_ball=b.str(65,radius=True),
            initial_bounds=initial_rows,response_lower_bound=s,response_source=response_source,
            improved_kappa=args.improved_kappa,improved_poisson=args.improved_poisson,response_selection=args.response,
            root_source_sha256=sha256(root_path.read_bytes()).hexdigest(),B=B,L=m.L,kappa=m.kappa,
            scalar_polynomial_coefficient_checks=40,counts=solver.counts,box=box,
            checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
            actual_elapsed_s=time.monotonic()-begin,all_checks_pass=True)
        if args.family == 'candidate':
            amplitude = F(data['original_amplitude'])
            assert amplitude**9<2**38
            row['restored_amplitude_sufficient_integer_exponent'] = (9*box['q']+38)//4+1
        suffix = ('_improved' if args.improved_kappa else '')+('_poisson' if args.improved_poisson else '')+('_sharp' if args.response=='sharp' else '')
        path = ROOT/'verification'/f'{args.family}_root{index}{suffix}.json'
        path.write_text(json.dumps(stringify(row),indent=2,default=str)+'\n')
        brief = dict(root=index,family=args.family,q=box['q'],radius_exponent=str(box['radius_exponent']),
            maximum_ratio=float(box['maximum_ratio']),actual_elapsed_s=row['actual_elapsed_s'])
        rows.append(brief)
        print(json.dumps(brief),flush=True)
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
        family=args.family,rows=rows,improved_kappa=args.improved_kappa,improved_poisson=args.improved_poisson,response_selection=args.response,all_checks_pass=True,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'{args.family}{suffix}_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['certified_initial_majorants.py','pure_cartesian_ball.py',
                 'general_rational_majorant.py','general_component_radius.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(result),flush=True)


if __name__ == '__main__':
    try: run()
    except Exception as exc:
        import traceback
        fail = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
            error_type=type(exc).__name__,error=str(exc),
            frames=[dict(file=Path(x.filename).name,line=x.lineno) for x in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n')
        print(json.dumps(fail),flush=True);raise SystemExit(1)

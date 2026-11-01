"""Independent Cartesian and exact algebraic certificate at delta=3/5."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import json
import sys
import time
import traceback
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
import sympy as sp
from flint import nmod_poly
import tuned_cartesian_exact as ce
from exact_polynomial_certificates import (primitive, sturm, sturm_finite, sturm_infinity,
    evaluate, modtrim, modmul, irreducibility_certificate)
ROOT = Path('research/200_three_fifths_tuning')
START = time.monotonic()
b, k = sp.symbols('b k')
ce.p = lambda n: 1-ce.K(3)*n/5


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def put(name, data):
    (ROOT/'verification'/name).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(dict(stage=name,checked_at_utc=stamp(),actual_elapsed_s=time.monotonic()-START)),flush=True)


def low(mode=None):
    ff = {1: ce.sine(ce.p(1),1)+ce.sine(ce.p(1),3,ce.b) if mode is None else ce.sine(ce.p(1),mode)}
    gg = {1: ce.poisson(ff[1])}
    for n in range(2,11):
        acc = ce.F(ce.p(n),{})
        for i in range(1,n):
            acc = acc+ce.adv(gg[i],ff[n-i])
        ff[n] = acc.scale(ce.K(2)/(3*(n-1)))
        ff[n].check_sine()
        assert all(a==0 and m%2 and abs(m)<=4*n-1 for a,m in ff[n].v)
        if n < 10:
            gg[n] = ce.poisson(ff[n])
    return ff,gg


def response(t, ff, gg, mode):
    n = 10*t
    symbolic = t == ce.k
    e = ce.sine(ce.p(n)+1,(6,-2) if symbolic else 6*int(t)-2)
    density,stream = {},{}
    for r in range(1,11):
        acc = ce.adv(e,ff[r])
        for s in range(1,r):
            acc = acc+ce.adv(stream[s],ff[r-s])+ce.adv(gg[r-s],density[s])
        density[r] = acc.scale(ce.K(2)/(3*(n+r-1)))
        density[r].check_sine()
        if r < 10:
            stream[r] = ce.poisson(density[r])
        if symbolic:
            for slope,offset in density[r].v:
                assert abs(slope)==6
                assert abs(offset+2 if slope==6 else offset-2)<=4*r-1
            print(json.dumps(dict(stage='generic_response',mode=mode,r=r,terms=len(density[r].v),
                                  checked_at_utc=stamp(),actual_elapsed_s=time.monotonic()-START)),flush=True)
    return 2*density[10].v.get((6,3) if symbolic else (0,6*int(t)+3),ce.R.zero)


def main():
    ff,gg = low()
    O = sp.Poly(ff[10].sine(3).as_expr(),b,domain=sp.QQ)
    assert O.degree()==10
    P = primitive([Fraction(str(O.nth(i))) for i in range(11)])
    if P[-1]<0:
        P=[-v for v in P]
    source = Path('../a4-lead/code/tuned/tq_certh_Q10h3.log')
    raw = source.read_bytes()
    lines = raw.decode().splitlines()
    leadP = sp.Poly(sp.sympify(next(s[4:] for s in lines if s.startswith('P = '))),b,domain=sp.QQ)
    leadscale = sp.sympify(next(s.split('O = P * ',1)[1] for s in lines if s.startswith('O = P * ')))
    assert leadP==sp.Poly(sum(sp.Integer(v)*b**i for i,v in enumerate(P)),b,domain=sp.QQ)
    assert sp.expand(O.as_expr()-leadP.as_expr()*leadscale)==0
    seq = sturm(P)
    infinity = [sturm_infinity(seq,negative) for negative in [True,False]]
    roots=[]
    for interval,multiplicity in sp.polys.polytools.intervals(leadP,eps=sp.Rational(1,10**40)):
        lo,hi = map(lambda x:Fraction(str(x)),interval)
        v=[sturm_finite(seq,x) for x in [lo,hi]]
        assert multiplicity==1 and v[0]-v[1]==1 and evaluate(P,lo) and evaluate(P,hi)
        roots.append(dict(interval=list(map(str,[lo,hi])),sturm_variations=v,approx=float((lo+hi)/2)))
    assert infinity[0]-infinity[1]==len(roots)==4
    prime=53
    assert P[-1]%prime
    reduction=modtrim(P,prime)
    modular=irreducibility_certificate(reduction,prime)
    put('obstruction_checks.json',dict(checked_at_utc=stamp(),all_checks_pass=True,O10=str(O.as_expr()),
        primitive_coefficients=list(map(str,P)),sturm_sequence=[list(map(str,a)) for a in seq],
        infinity_variations=infinity,real_roots=roots,modular_irreducibility=modular,
        source_path=str(source),source_sha256=sha256(raw).hexdigest(),obstruction_exactly_matches=True,
        ordered_low_products=45,poisson_identity_orders=list(range(1,10)),actual_elapsed_s=time.monotonic()-START))
    (ROOT/'sources/lead_initial_output.txt').write_bytes(raw)
    del ff,gg
    generic,small={},{}
    for mode,col in [(1,0),(3,10)]:
        ff,gg=low(mode)
        assert sp.cancel(ff[10].sine(3).as_expr()-O.nth(col))==0
        small[mode]=[]
        for t in range(1,9):
            value=sp.factor(response(t,ff,gg,mode).as_expr())
            small[mode].append(dict(k=t,sigma=str(value)))
            put(f'mode{mode}_small.json',dict(rows=small[mode]))
        value=sp.factor(response(ce.k,ff,gg,mode).as_expr())
        for t in [7,8]:
            assert sp.cancel(value.subs(k,t)-sp.sympify(small[mode][t-1]['sigma']))==0
        limit=sp.factor(sp.limit(value,k,sp.oo))
        assert limit.is_Rational
        generic[mode]=value
        put(f'mode{mode}_generic.json',dict(sigma=str(value),limit=str(limit),tail_starts=7,
            direct_comparisons=[7,8],all_checks_pass=True,actual_elapsed_s=time.monotonic()-START))
    criterion=sp.factor(O.nth(10)*generic[1]-O.nth(0)*generic[3])
    numerator,denominator=sp.fraction(criterion)
    N,D=sp.Poly(numerator,k,domain=sp.QQ),sp.Poly(denominator,k,domain=sp.QQ)
    assert not N.is_zero
    trials=[]
    certificate=None
    for K in [7,8,10,12,16,24,32,48,64,96,128,256,512,1024,2048]:
        ns,ds=N.shift(K),D.shift(K)
        sn,sd=sp.sign(ns.LC()),sp.sign(ds.LC())
        okay=all(sn*v>=0 for v in ns.all_coeffs()) and sn*ns.nth(0)>0 and all(sd*v>=0 for v in ds.all_coeffs()) and sd*ds.nth(0)>0
        trials.append(dict(K=K,passes=bool(okay)))
        if okay:
            certificate=dict(K=K,numerator_sign=int(sn),denominator_sign=int(sd),
                shifted_numerator_descending=list(map(str,ns.all_coeffs())),shifted_denominator_descending=list(map(str,ds.all_coeffs())))
            break
    assert certificate is not None, 'No positive shifted polynomial certificate found.'
    smallchecks=[]
    for t in range(1,7):
        val=sp.cancel(O.nth(10)*sp.sympify(small[1][t-1]['sigma'])-O.nth(0)*sp.sympify(small[3][t-1]['sigma']))
        assert val!=0, ('Finite edge criterion zero; full response needed.',t)
        smallchecks.append(dict(k=t,criterion=str(val)))
    remaining=[]
    for t in range(7,certificate['K']):
        nv,dv=N.eval(t),D.eval(t)
        assert nv and dv, ('Tail edge criterion zero or pole; further analysis needed.',t)
        remaining.append(dict(k=t,numerator_sign=int(sp.sign(nv)),denominator_sign=int(sp.sign(dv))))
    limiting=sp.factor(sp.limit(criterion,k,sp.oo))
    assert limiting.is_Rational and limiting!=0
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,criterion=str(criterion),
        numerator_degree=N.degree(),denominator_degree=D.degree(),finite_edge_checks=smallchecks,
        tail_integer_checks=remaining,positive_shift_certificate=certificate,shift_trials=trials,
        limiting_edge_criterion=str(limiting),all_four_uniform_response_infima_positive=True,
        actual_elapsed_s=time.monotonic()-START)
    put('response_checks.json',result)
    for name in ['three_fifths_tuning.py','tuned_cartesian_exact.py','exact_polynomial_certificates.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(ROOT)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest())
           for p in ROOT.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    put('MANIFEST.json',dict(checked_at_utc=stamp(),files=files))
    print(json.dumps({key:value for key,value in result.items() if key not in ['criterion','finite_edge_checks','positive_shift_certificate']}),flush=True)

if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        failure=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),
            frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-START)
        put('FAILURE.json',failure)
        print(json.dumps(failure),flush=True)
        raise SystemExit(1)

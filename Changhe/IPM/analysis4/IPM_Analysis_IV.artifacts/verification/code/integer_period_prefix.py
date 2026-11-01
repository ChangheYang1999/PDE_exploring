"""Exact h=1 prefix majorants, seeded by independently enclosed Cartesian data."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from gmpy2 import mpq
import sympy as sp
from pure_cartesian_ball import Tuning,sine,refine_root
from certified_prefix_majorant import PrefixMajorant,certificate,roundup,upper
from resonance_block_majorant import clean
from certified_initial_majorants import pack
ROOT=Path('research/175_integer_period_prefix')


def constants(Q,N):
    d=F(2,Q)
    return F(3*Q*Q,4*(3*Q-1)),4*(2-d+max(d,1-d))*(1-d)/d*F(N+1,N)


def inputs(Q):
    paths={3:('120_tuned_explicit_radius/sources/algebraic_roots.json','123_tuned_response_minimum/verification/checks.json'),
        4:('142_period_four_tuning/verification/root_response_certificates.json','143_period_four_response_bounds/verification/checks.json'),
        5:('130_period_five_tuning/verification/irreducibility_sturm_checks.json','139_period_five_response_minima/verification/checks.json'),
        6:('154_period_six_tuning/verification/root_response_certificates.json','155_period_six_response_infima/verification/checks.json')}
    rootpath,responsepath=[Path('research',v) for v in paths[Q]]
    rd,sd=[json.loads(p.read_text()) for p in [rootpath,responsepath]]
    if Q==3:
        b=sp.Symbol('b');coeff=[str(v) for v in reversed(sp.Poly(sp.sympify(rd['sturm_sequence'][0]),b).all_coeffs())]
        intervals=[r['root_interval'] for r in sd['rows']]
        lower=[]
        for row in sd['rows']:
            v=-F(row['sigma4']['upper']);scale=F(1)
            while v*scale<100:scale*=10
            lower.append(F((v*scale).__floor__())/scale)
    else:
        coeff=rd['primitive_coefficients_ascending'];intervals=[r['interval'] for r in rd['real_roots']]
        key={4:'sharper_lower',5:'simple_uniform_lower_bound',6:'three_digit_lower'}[Q]
        lower=[F(r[key]) for r in sd['rows']]
    assert all(s>0 for s in lower)
    return coeff,intervals,lower,[rootpath,responsepath]


def main():
    start=time.monotonic();ctx.prec=768;generic=[];rows=[]
    for Q in [3,4,5,6]:
        for M in [2,3]:
            N=M*Q;L,kap=constants(Q,N)
            d=[F(j+2,j+1) for j in range(1,N+1)];e=[F(0)]+[F(a+1,a+2) for a in range(2,M)]
            m=PrefixMajorant(1,Q,4,d,e,F(3,5),L,kap);result=certificate(m,2)
            (ROOT/'verification'/f'generic_Q{Q}_M{M}.json').write_text(json.dumps(clean(result),indent=2)+'\n')
            generic.append(dict(Q=Q,M=M,scalar_coefficient_checks=result['scalar_coefficient_checks']))
        coeff,intervals,lowers,paths=inputs(Q)
        for index,(interval,s) in enumerate(zip(intervals,lowers),1):
            begin=time.monotonic();b,I=refine_root(coeff,interval,832);solver=Tuning(1,Q,4);N=2*Q
            f={1:sine(solver.p(1),1,arb(1))+sine(solver.p(1),3,b)};g={1:solver.poisson(f[1],1)}
            for n in range(2,N+1):
                fn=solver.order(n,f,g)
                if n==N:
                    obstruction=fn.sine(1);assert obstruction.contains(0)
                    fn=fn.project(4*n-1,1,solver.counts,zero_mode=1)
                f[n]=fn;g[n]=solver.poisson(fn,n)
            initial=[];d=[]
            for n in range(1,N+1):
                norm=f[n].norm()*n;up=upper(norm);bound=roundup(up);assert bound>up
                d.append(bound);initial.append(dict(n=n,exact_ball=pack(norm),bound=bound))
            L,kap=constants(Q,N);m=PrefixMajorant(1,Q,4,d,[F(0)],s,L,kap)
            result=certificate(m,2)
            result.update(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
                root_index=index,root_interval=I,root=b.str(60,radius=True),initial_certificates=initial,
                first_obstruction=pack(obstruction),cartesian_counts=solver.counts,
                inputs={str(p):sha256(p.read_bytes()).hexdigest() for p in paths},actual_elapsed_s=time.monotonic()-begin)
            (ROOT/'verification'/f'Q{Q}_root{index}.json').write_text(json.dumps(clean(result),indent=2)+'\n')
            brief={key:result[key] for key in ['Q','N','root_index','s','w_dyadic_exponent','radius_exponent','scalar_coefficient_checks','actual_elapsed_s']}
            rows.append(brief);print(json.dumps(clean(brief)),flush=True)
            (ROOT/'verification/partial.json').write_text(json.dumps(clean(dict(generic=generic,rows=rows)),indent=2)+'\n')
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
        arithmetic_bits=768,generic=generic,rows=rows,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/checks.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    for name in ['integer_period_prefix.py','certified_prefix_majorant.py','resonance_block_majorant.py','pure_cartesian_ball.py','certified_initial_majorants.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(clean(result)),flush=True)

if __name__=='__main__':main()

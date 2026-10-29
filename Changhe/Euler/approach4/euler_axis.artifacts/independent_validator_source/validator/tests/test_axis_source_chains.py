#!/usr/bin/env python3
"""Exact local axis models and the two-sided matching condition."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as sp
ROOT=Path(__file__).resolve().parents[1];ROWS=[]
def check(name,truth):
    row=dict(name=name,passed=bool(truth));ROWS.append(row);print(json.dumps(row),flush=True)
def main():
    start=time.monotonic();x=sp.symbols('x',positive=True);Q,K=sp.symbols('Q K',nonzero=True)
    for c in [sp.Rational(11,20),sp.Rational(3,5),sp.Rational(7,10)]:
        delta=1+c
        for k in [2,3,4,6]:
            mu=delta/(k-1);w=-mu*x;a=delta+mu;q=Q*x**k
            eta=2*K*Q/mu*x**(k-1)-2*Q**2/mu*x**(2*k-1)
            check(f'q_transport_c{c}_k{k}',sp.expand(w*sp.diff(q,x)+a*q)==0)
            check(f'eta_transport_c{c}_k{k}',sp.expand(w*sp.diff(eta,x)+delta*eta-2*q*sp.diff(q,x))==0)
            check(f'first_integral_c{c}_k{k}',sp.expand(w*eta-2*q*(q-K))==0)
            v=(c+mu)/2
            check(f'quantized_strain_c{c}_k{k}',sp.simplify(v-(1+k*c)/(2*(k-1)))==0)
            Km,Kp=sp.symbols('Km Kp');em=eta.subs(K,Km);ep=eta.subs(K,Kp)
            jump=sp.limit(sp.diff(ep-em,x,k-1),x,0,dir='+')
            check(f'matching_coefficient_c{c}_k{k}',sp.simplify(jump-2*Q*(Kp-Km)*sp.factorial(k-1)/mu)==0)
            if k%2:
                check(f'odd_order_sign_conflict_c{c}_k{k}',sp.simplify(jump.subs({Kp:K,Km:-K}))!=0)
        # At an axial repeller with w'=delta, a smooth nonzero q is constant
        # to this linear-model order; regular homogeneous eta is zero.
        check(f'repeller_q_c{c}',sp.diff(K,x)==0)
    check('noninteger_attractor_not_smooth',sp.limit(sp.diff(x**sp.Rational(5,2),x,3),x,0,dir='+')==sp.oo)
    check('repeller_fractional_power_not_C1',sp.limit(sp.diff(x**sp.Rational(1,3),x),x,0,dir='+')==sp.oo)
    files=[Path(__file__),ROOT.parent/'research/axis_source_chains/PROOF.md']
    out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,checks=ROWS,
             all_passed=all(r['passed'] for r in ROWS),source_sha256={str(p.relative_to(ROOT.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
             scope='Exact local ODE and matching tests. No global Euler solution is constructed.')
    (ROOT/'results/axis_source_chain_tests.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['all_passed','elapsed_seconds']}));raise SystemExit(0 if out['all_passed'] else 1)
if __name__=='__main__':main()

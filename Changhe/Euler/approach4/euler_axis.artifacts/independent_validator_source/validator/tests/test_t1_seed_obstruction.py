#!/usr/bin/env python3
"""Exact source/tail incompatibility of the fixed rational T1 seed family."""
import datetime,json,time
from pathlib import Path
import sympy as sp
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.perf_counter();rows=[];error=None
    def check(name,expr):
        rem=sp.factor(expr);rows.append({'name':name,'remainder':str(rem),'passed':rem==0})
        if rem!=0:raise AssertionError(rows[-1])
    try:
        s,z,a,p,K,delta=sp.symbols('s z a p K delta',positive=True)
        phi=z*(1+3*z*z)/(2*(1+a*s+z*z)**(p+1))
        ps=sp.diff(phi,s,z).subs({s:0,z:0})
        pz=sp.diff(phi,z,3).subs({s:0,z:0})/6
        check('source radial cubic',ps+a*(p+1)/2)
        check('source axial cubic',pz-(2-p)/2)
        K2=delta**2*(4*a*(p+1)/(3*(2-p))-1)
        check('source closure substitution',(ps+3*pz*(1+K*K/delta**2)/4).subs(K*K,K2))
        alpha=2*p-1;leading=sp.Rational(3,2)*z**3/(a*s+z*z)**(p+1)
        eta=-8*sp.diff(leading,s)-4*s*sp.diff(leading,s,2)-sp.diff(leading,z,2)
        coeff=sp.simplify(eta.subs(s,0)*z**(1+2*p))
        check('upper axis homogeneous coefficient',coeff-sp.Rational(3,2)*(8*a*(p+1)-alpha*(alpha+1)))
        lower=3*(2-p)/(4*(p+1));upper=p*(2*p-1)/(4*(p+1))
        check('bound separation identity',4*(p+1)*(lower-upper)-(6-2*p-2*p*p))
        for pv in [sp.Rational(2,3),sp.Rational(3,4),sp.Rational(4,5),sp.Rational(9,10),sp.Integer(1)]:
            difference=sp.factor((lower-upper).subs(p,pv))
            rows.append({'name':'positive bound separation p='+str(pv),'value':str(difference),'passed':bool(difference>0)})
            if not rows[-1]['passed']:raise AssertionError(rows[-1])
    except Exception as ex:
        import traceback;traceback.print_exc();error=repr(ex)
    out={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_passed':error is None,
         'case_count':len(rows),'rows':rows,'exception':error,'wall_seconds':time.perf_counter()-start,
         'source_sha256':sha256(Path(__file__)),'proof_sha256':sha256(ROOT.parent/'research/t1_seed_obstruction/PROOF.md')}
    atomic_json(ROOT/'results/t1_seed_obstruction_tests.json',out)
    print(json.dumps({k:out[k] for k in ['all_passed','case_count','exception','wall_seconds']}),flush=True)
    raise SystemExit(0 if error is None else 1)
if __name__=='__main__':main()

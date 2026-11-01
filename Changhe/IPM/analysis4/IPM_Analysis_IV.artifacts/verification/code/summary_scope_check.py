"""Recompute the order-three obstruction to a pure tuned potential."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys,traceback
sys.dont_write_bytecode=True
ROOT=Path('research/230_summary_scope_counterexamples')
def main():
    start=time.monotonic()
    import tuned_cartesian_exact as tc
    import sympy as sp
    ff,gg=tc.orders(3)
    b=sp.Symbol('b');actual=sp.expand(ff[3].sine(1).as_expr())
    expected=-sp.Rational(3,64)*b**3+sp.Rational(1161,17920)*b**2-sp.Rational(573,44800)*b+sp.Rational(1,6400)
    assert actual==expected
    P=176703765525000*b**6-222533688701250*b**5+96180432855375*b**4-20675598499400*b**3+2783057141280*b**2-243275209320*b+10532171936
    gcd=sp.gcd(sp.Poly(P,b),sp.Poly(actual,b));assert gcd.degree()==0
    # An explicit Bezout certificate proves nonvanishing at every root of P.
    s,t,h=sp.gcdex(sp.Poly(P,b,domain=sp.QQ),sp.Poly(actual,b,domain=sp.QQ));assert h==1
    assert sp.expand(s.as_expr()*P+t.as_expr()*actual)==1
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
      density_order3_sine1=str(actual),gcd_degree=0,bezout_P=str(s.as_expr()),bezout_A=str(t.as_expr()),
      exact_identity='bezout_P*P+bezout_A*A=1',first_order_pole_counterexample=dict(Q=5,n=1,claimed_bound=-1,actual_pole_order=0),
      actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['summary_scope_check.py','tuned_cartesian_exact.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if not k.startswith('bezout_')}),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);raise SystemExit(1)

"""Finite and compact-response probes for f1=sin(11 theta), delta=4/9."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
from gmpy2 import mpq
from flint import arb,ctx
from pure_cartesian_ball import Tuning,Field,sine,ball
from compact_response_bounds import Response,low
from certified_initial_majorants import pack
from three_fifths_response_bounds import exact_lower
from resonance_block_majorant import clean
ROOT=Path('research/227_single_eleven_convergence')
def restrict_support(field, allowed):
    coefficients=field.poly.coeffs()
    for j,v in enumerate(coefficients):
        if field.lo+j not in allowed:
            assert v.contains(0), ('support_exclusion',field.lo+j,str(v))
            coefficients[j]=arb(0)
    return Field(field.degree,field.lo,coefficients)

class HighModeResponse(Response):
    def __init__(self,mode=11):
        self.h=2;self.Q=9;self.B=mode+1;self.delta=mpq(4,9);self.solver=Tuning(self.h,self.Q,self.B)
        self.f={1:sine(self.solver.p(1),mode,arb(1))};self.g={1:self.solver.poisson(self.f[1],1)}
        for n in range(2,self.Q+1):
            allowed_f={mode*k+e for k in range(-n,n+1,2) for e in range(1-n,n,2)}
            self.f[n]=restrict_support(self.solver.order(n,self.f,self.g),allowed_f)
            if n<self.Q:
                allowed_g={mode*k+e for k in range(-n,n+1,2) for e in range(-n,n+1,2)}
                self.g[n]=restrict_support(self.solver.poisson(self.f[n],n),allowed_g)
        assert self.f[self.Q].sine(1).is_zero()
        self.fxy={j:(low(f.derivative()),low(f.derivative(True))) for j,f in self.f.items()}
        self.gxy={j:(low(g.derivative()),low(g.derivative(True))) for j,g in self.g.items()}

def main():
    start=time.monotonic();ctx.prec=1024;response=HighModeResponse();rows=[]
    for k in range(1,41):
        v=response.full(k);row=dict(k=k,enclosure=pack(v),display=v.str(40,radius=True),separated=exact_lower(v)>0)
        if k>=28:
            compact=response.compact(ball(mpq(1,4*k-2)));assert compact is not None and compact.overlaps(v)
            row['compact']=pack(compact)
        rows.append(row);print(json.dumps(clean(row)),flush=True)
    limit=response.compact(arb(0));assert limit is not None
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
        mode=11,delta='4/9',B=12,K=28,arithmetic_bits=1024,rows=rows,limit=pack(limit),limit_display=limit.str(50,radius=True),
        all_separated=all(r['separated'] for r in rows) and exact_lower(limit)>0,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/probe.json').write_text(json.dumps(clean(result),indent=2)+'\n')
    for name in ['single_eleven_probe.py','compact_response_bounds.py','pure_cartesian_ball.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(clean({k:v for k,v in result.items() if k!='rows'})),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        import traceback
        failure=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n')
        print(json.dumps(failure),flush=True)
        raise SystemExit(1)

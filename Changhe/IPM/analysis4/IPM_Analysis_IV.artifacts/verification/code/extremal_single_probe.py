"""Independent finite response probe for the automatically compatible high mode."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import gcd
import argparse,json,sys,time,traceback
sys.dont_write_bytecode=True
from gmpy2 import mpq
from flint import arb,ctx
from pure_cartesian_ball import Tuning,Field,sine,ball
from compact_response_bounds import Response,low
from certified_initial_majorants import pack
from three_fifths_response_bounds import exact_lower
from resonance_block_majorant import clean
ROOT=Path('research/231_extremal_single_harmonics')
class ExtremalResponse(Response):
    def __init__(self,h,Q):
        assert h>=2 and Q>2*h and Q%2 and gcd(h,Q)==1
        mode=Q+2*h-2;self.mode=mode;self.h=h;self.Q=Q;self.B=mode+1;self.delta=mpq(2*h,Q);self.solver=Tuning(h,Q,self.B)
        self.f={1:sine(self.solver.p(1),mode,arb(1))};self.g={1:self.solver.poisson(self.f[1],1)}
        self.projected_zero_count=0
        def restrict(v,allowed):
            a=v.poly.coeffs()
            for j,c in enumerate(a):
                if v.lo+j not in allowed:
                    assert c.contains(0),('excluded_support',v.lo+j,str(c));a[j]=arb(0);self.projected_zero_count+=1
            return Field(v.degree,v.lo,a)
        for n in range(2,Q+1):
            allowed={mode*k+e for k in range(-n,n+1,2) for e in range(1-n,n,2)}
            self.f[n]=restrict(self.solver.order(n,self.f,self.g),allowed)
            if n<Q:
                allowed={mode*k+e for k in range(-n,n+1,2) for e in range(-n,n+1,2)}
                self.g[n]=restrict(self.solver.poisson(self.f[n],n),allowed)
        assert self.f[Q].sine(2*h-3).is_zero()
        self.fxy={j:(low(f.derivative()),low(f.derivative(True))) for j,f in self.f.items()}
        self.gxy={j:(low(g.derivative()),low(g.derivative(True))) for j,g in self.g.items()}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--h',type=int,default=2);ap.add_argument('--Q',type=int,default=7);a=ap.parse_args()
    start=time.monotonic();ctx.prec=1024;r=ExtremalResponse(a.h,a.Q);K=(r.B*r.Q+2+2*r.h-1)//(2*r.h);rows=[]
    for k in range(1,K+8):
        v=r.full(k);row=dict(k=k,enclosure=pack(v),display=v.str(45,radius=True),separated=exact_lower(v)>0)
        if k>=K:
            c=r.compact(ball(mpq(1,2*r.h*k-2)));assert c is not None and c.overlaps(v);row['compact']=pack(c)
        rows.append(row);print(json.dumps(clean(row)),flush=True)
    limit=r.compact(arb(0));assert limit is not None
    out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,h=r.h,Q=r.Q,mode=r.mode,B=r.B,K=K,rows=rows,arithmetic_bits=1024,first_compatibility_identically_zero=True,
      projected_zero_count=r.projected_zero_count,limit=pack(limit),limit_display=limit.str(60,radius=True),all_separated=all(x['separated'] for x in rows) and exact_lower(limit)>0,actual_elapsed_s=time.monotonic()-start,
      scope='Finite and limiting-response evidence only; not an all-integer certificate.')
    (ROOT/'verification'/f'h{r.h}_Q{r.Q}_probe.json').write_text(json.dumps(clean(out),indent=2)+'\n')
    for name in ['extremal_single_probe.py','compact_response_bounds.py','pure_cartesian_ball.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(clean({k:v for k,v in out.items() if k!='rows'})),flush=True)
if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)

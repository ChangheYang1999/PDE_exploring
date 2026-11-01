"""Validate jet arithmetic then measure actual compact-response enclosures."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
from flint import arb,ctx
from gmpy2 import mpq
from pure_cartesian_ball import ball
from single_eleven_probe import HighModeResponse
from taylor_response_enclosure import Jet,enclose
from certified_initial_majorants import pack
from discrete_response_cover import lower
ROOT=Path('research/234_taylor_response_enclosures')
class Rational:
    def compact(self,t):
        if (1-t).contains(0):return None
        return 1/(1-t)
def main():
    started=time.monotonic();ctx.prec=768;example=Rational();count=0
    for d in [1,2,3,4]:
        value=example.compact(Jet([ball(mpq(0)).union(ball(mpq(1,4))),arb(1)],d))
        for j in range(d+1):
            assert value.c[j].contains(ball(mpq(1))) and value.c[j].contains(ball(mpq(4,3)**(j+1)));count+=2
        bounded=enclose(example,F(0),F(1,4),d);assert bounded.contains(1) and bounded.contains(ball(mpq(4,3)))
        assert enclose(example,F(0),F(2),d) is None
    response=HighModeResponse();rows=[]
    for d,depth in [(1,8),(2,8),(3,8),(3,4),(3,0),(4,4),(4,0)]:
        t0=time.monotonic();a=F(0);b=F(1,110*2**depth);value=enclose(response,a,b,d)
        row=dict(degree=d,depth=depth,a=str(a),b=str(b),enclosure=pack(value) if value is not None else None,display=value.str(35,radius=True) if value is not None else None,lower_bound=str(lower(value)) if value is not None else None,actual_elapsed_s=time.monotonic()-t0)
        rows.append(row);print(json.dumps(row),flush=True)
        (ROOT/'verification/probe.json').write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),jet_arithmetic_checks=count,rows=rows,actual_elapsed_s=time.monotonic()-started),indent=2)+'\n')
    for name in ['taylor_response_enclosure.py','taylor_response_probe.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        (ROOT/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)

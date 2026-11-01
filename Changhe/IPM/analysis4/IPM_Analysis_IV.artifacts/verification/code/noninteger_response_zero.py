"""Check the real response crossing between integer indices513 and514."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time,traceback
sys.dont_write_bytecode=True
from flint import arb,ctx
from gmpy2 import mpq
from single_eleven_probe import HighModeResponse
from pure_cartesian_ball import ball
from taylor_response_enclosure import Jet
from certified_initial_majorants import pack
ROOT=Path('research/236_noninteger_response_zero')
def main():
 start=time.monotonic();ctx.prec=1024;r=HighModeResponse();a=F(1,2054);b=F(1,2050)
 left=r.compact(ball(mpq(str(a))));right=r.compact(ball(mpq(str(b))))
 assert left>0 and right<0
 whole=r.compact(Jet([ball(mpq(str(a))).union(ball(mpq(str(b)))),arb(1)],1))
 assert whole is not None and isinstance(whole,Jet)
 derivative=whole.c[1];unique=bool(derivative<0)
 out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
  bits=1024,a=str(a),b=str(b),left=pack(left),right=pack(right),left_display=left.str(45,radius=True),right_display=right.str(45,radius=True),
  all_interval_denominators_separated=True,real_zero_exists=True,real_index_interval=[513,514],
  derivative=pack(derivative),derivative_display=derivative.str(45,radius=True),unique_zero_in_interval=unique,actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
 for name in ['noninteger_response_zero.py','single_eleven_probe.py','taylor_response_enclosure.py','compact_response_bounds.py']:
  (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps({k:v for k,v in out.items() if k not in ['left','right','derivative']}),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as e:
  out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);raise SystemExit(1)

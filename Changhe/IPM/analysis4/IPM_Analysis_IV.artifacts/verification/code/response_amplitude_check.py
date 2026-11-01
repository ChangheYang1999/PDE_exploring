"""Directed counterexample to amplitude-independent response lower bounds."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
from flint import ctx,arb
from gmpy2 import mpq
from extremal_single_probe import ExtremalResponse
from compact_response_bounds import low
from pure_cartesian_ball import ball
from certified_initial_majorants import pack
from unpack_dyadic4 import unpack
ROOT=Path('research/250_response_amplitude_normalization')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def main():
 started=time.monotonic();rows=[]
 for bits in [512,1024]:
  ctx.prec=bits;ball.cache_clear();r=ExtremalResponse(2,5);scaled=object.__new__(ExtremalResponse);scaled.__dict__=r.__dict__.copy()
  scaled.f={n:f.scale(arb(1)/2**n) for n,f in r.f.items()};scaled.g={n:g.scale(arb(1)/2**n) for n,g in r.g.items()}
  scaled.fxy={n:(low(f.derivative()),low(f.derivative(True))) for n,f in scaled.f.items()};scaled.gxy={n:(low(g.derivative()),low(g.derivative(True))) for n,g in scaled.g.items()}
  for k in range(1,4):
   v=r.full(k);w=scaled.full(k);assert w.overlaps(v/32)
   if k==1:
    assert v>arb(1)/2**20 and w>0 and w<arb(1)/2**20 and w>arb(1)/2**25
   rows.append(dict(bits=bits,k=k,unit=pack(v),scaled=pack(w),unit_display=v.str(45,radius=True),scaled_display=w.str(45,radius=True)))
 p=Path('research/231_extremal_single_harmonics/verification/h2_Q5_probe.json');raw=p.read_bytes();src=json.loads(raw)
 for row in rows:
  assert arb(*unpack(row['unit'])).overlaps(arb(*unpack(src['rows'][row['k']-1]['enclosure'])))
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,h=2,Q=5,mode=7,epsilon='1/2',unit_bound='1/1048576',scaled_bound='1/33554432',counterexample_index=1,rows=rows,source=dict(path=str(p),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-started)
 (ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
 (ROOT/'sources/response_amplitude_check.py').write_bytes(Path('code/response_amplitude_check.py').read_bytes())
 print(json.dumps(out),flush=True)
if __name__=='__main__':main()

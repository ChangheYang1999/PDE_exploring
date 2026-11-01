from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import time,sys,json,os
sys.dont_write_bytecode=True
os.sched_setaffinity(0,{18});os.nice(19)
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from flint import arb,ctx
from gmpy2 import mpq
from extremal_single_probe import ExtremalResponse
from taylor_response_enclosure import Jet,enclose
from pure_cartesian_ball import ball
from certified_initial_majorants import pack
ctx.prec=768;r=ExtremalResponse(3,13);start=time.monotonic();rows=[]
for a,b,degree in [(F(0),F(0),4),(F(0),F(1,238*16),3),(F(0),F(1,238*16),4),(F(0),F(1,238*16),5),(F(0),F(1,238*4),5)]:
 t=time.monotonic()
 if a==b:
  v=r.compact(Jet([ball(mpq(str(a))),arb(1)],degree));row=dict(a=str(a),b=str(b),degree=degree,coefficients=[x.str(20,radius=True) for x in v.c])
 else:
  v=enclose(r,a,b,degree);row=dict(a=str(a),b=str(b),degree=degree,value=v.str(30,radius=True),nonzero=not v.contains(0),enclosure=pack(v))
 row.update(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),elapsed_s=time.monotonic()-t);rows.append(row);print(json.dumps(row),flush=True)
 Path('research/242_single_seventeen_six_thirteenths/verification/jet_probe.json').write_text(json.dumps(dict(rows=rows,actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')

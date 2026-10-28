"""Reproduce old interval counterexamples and check repaired snapshots."""
import sys, argparse, json, hashlib
from pathlib import Path
from datetime import datetime,timezone
p=argparse.ArgumentParser();p.add_argument('--sources',required=True);p.add_argument('--output',required=True);a=p.parse_args()
ROOT=Path(__file__).resolve().parents[1];src=ROOT/a.sources
sys.path.insert(0,str(src))
import certify_note14 as C
from flint import arb,ctx
ctx.prec=80;C.setup('3/4','3/4','-3/10','50/53')
x=arb('0.995','0.01');y=arb('0.01');xp=arb('0.986')
box=C.G.sigma(x,y);point=C.G.sigma(xp,y)
q=C.PI/2;r=arb('1e-26');t1=q.mid();t2=q.upper()
extreme=C.m_cell((arb(1)/2,arb(0)),r/2,r,t1,t2,0,0)
with ctx.workprec(160):
 true_q=arb.pi()/2;theta=true_q+r/2
 exterior=bool(t1<theta<t2 and abs(theta.cos())<3*r/4)
tiny=C.m_cell((arb(1)/2,arb(0)),arb('5e-31'),arb('1e-30'),q.lower(),q.upper(),0,0)
pby=C.P_bounds(arb(0),arb(1),arb('.01'))
assert x.contains(xp) and point>0 and exterior
result=dict(time_utc=datetime.now(timezone.utc).isoformat(),sources=str(src),precision_bits=ctx.prec,
 sign=dict(interval=str(x),point=str(xp),box_sign=str(box),point_sign=str(point),wrong_certified_sign=box is not None and bool(box<0)),
 extremum=dict(strict_exterior_point=True,result=str(extreme[0]),cells=extreme[1],incorrect_zero_skip=bool(extreme[0]==0 and extreme[1]==0)),
 partial=dict(result=str(tiny[0]),cells=tiny[1],finite=tiny[0].is_finite()),
 smooth_profile_bounds=None if pby is None else [str(v) for v in pby],
 source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in src.glob('*.py')})
out=ROOT/a.output;out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

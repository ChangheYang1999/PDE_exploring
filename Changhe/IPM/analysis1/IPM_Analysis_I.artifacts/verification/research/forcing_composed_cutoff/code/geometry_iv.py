"""Independent iv80 geometry using squared-distance and exact dyadic weights."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,time,hashlib
import numpy as np
from mpmath import iv
D=Path(__file__).resolve().parents[1];B=D.parents[1];iv.dps=100;start=time.monotonic()
def ff(x):return F.from_float(float(x))
def b(x):return iv.mpf(x.numerator)/x.denominator
def mpf(x):
 s,m,e,_=x
 return (-1 if s else 1)*F(m)*(F(2)**e)
def low(x):return mpf(x._mpi_[0])
def high(x):return mpf(x._mpi_[1])
def box(a,z):return iv.mpf([b(a).a,b(z).b])
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for v in iter(lambda:f.read(1024*1024),b''):h.update(v)
 return h.hexdigest()
raw=json.loads((D/'source/runs/forcing/v21_p9_merged.json').read_text());primary=json.loads((B/'research/localized_forcing/evidence/geometry_arb.json').read_text())
rows={(r['ci'],r['q'],32*r['bs']+r['ks'],4*r['bp']+r['kp']):r for r in raw['cells']};assert len(rows)==43949
p=Path(primary['green_path']);pin=sha(p);assert pin==primary['green_sha256']
with np.load(p) as z:tb=z['tb'][4096:4110].copy();tr=z['tb_rad'][4096:4110].copy()
xs=box(*map(ff,raw['x_star_bracket']));rout=F(297,8000);dth=ff(raw['theta_max'])/16;w=ff(primary['w_up']);dw=ff(primary['wk']);assert 8*dw>=2*w>=dth
angs={}
for q in range(16):
 c=dth*F(2*q+1,2)
 for j in range(8):
  a=max(F(0),c-w+j*dw);z=min(c+w,c-w+(j+1)*dw)
  angs[q,j]=(a,z,xs*iv.cos(b(a)),xs*iv.sin(b(a)),xs*iv.cos(b(z)),xs*iv.sin(b(z)))
fail=[];nr=no=0;radials=0
# Avoid producer radial rounding: use iv enclosures of exact knot-box endpoints
# directly. These are contained in the outward producer radial bounds checked
# by the first engine, but this method never reads those radial bounds.
for ix,ci in enumerate(range(4096,4109)):
 c=primary['cells'][ix];assert c['ci']==ci and ff(c['tb'])==ff(tb[ix]) and ff(c['tb_rad'])==ff(tr[ix]);h=ff(c['h_up']);hk=ff(c['hk'])
 assert h>=ff(tb[ix+1])+ff(tr[ix+1])-ff(tb[ix])+ff(tr[ix]) and 64*hk>=h
 rr=[]
 for ks in range(64):
  r1=iv.exp(b(ff(tb[ix])-ff(tr[ix])+ks*hk));r2=iv.exp(b(ff(tb[ix])+ff(tr[ix])+(ks+1)*hk));rr.append((b(low(r1)),b(high(r2))));radials+=1
 for (q,j),(a,z,xc,ys,xb,yb) in angs.items():
  ym=max(F(0),low(ys));ym2=ym*ym
  for ks,(r1,r2) in enumerate(rr):
   gap=max(F(0),low(r1-xc),low(xc-r2));d2low=gap*gap+ym2
   # Squared comparisons avoid sqrt entirely.
   d2high=max(high((r1-xb)**2+yb**2),high((r2-xb)**2+yb**2));area=high((r2*r2-r1*r1)*b(z-a))
   key=ci,q,ks,j;row=rows.get(key)
   if row is None:
    no+=1
    if d2low<rout*rout:fail.append({'kind':'omission','key':key})
   else:
    nr+=1
    if (ff(row['dmin'])>0 and ff(row['dmin'])**2>d2low) or ff(row['dmax'])**2<d2high or ff(row['area'])<area:fail.append({'kind':'saved','key':key})
assert nr==43949 and no==62547 and sha(p)==pin
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_V21_GEOMETRY_SECOND_METHOD' if not fail else 'OPEN_FAILURES',seconds=time.monotonic()-start,engine='mpmath.iv100; exact rational squared comparisons; no producer radial bound or MR computation',included=nr,omitted=no,radial_exp_boxes=radials,green_sha256=pin,failures=fail[:30],failure_count=len(fail),scope='Finite geometry conditional on correct canonical knot enclosure; no residual derivative or full forcing acceptance.')
(D/'evidence/geometry_iv.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],nr,no,out['seconds']);assert not fail,fail[:2]

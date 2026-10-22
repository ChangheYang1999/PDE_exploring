"""Check saved geometry on restricted Bernstein domains using Arb256.

No producer Certifier or Taylor-model arithmetic is executed. Reading only
14 knot midpoints/radii from the NPZ avoids loading its large arrays.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time,math
import numpy as np
from flint import arb,ctx
D=Path(__file__).resolve().parents[1];ctx.prec=256;start=time.monotonic()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while True:
   b=f.read(1024*1024)
   if not b:break
   h.update(b)
 return h.hexdigest()
def ff(v):return F.from_float(float(v))
def bf(v):return arb(v.numerator)/v.denominator
def lo(v):return F(str(v.lower().fmpq()))
def hi(v):return F(str(v.upper().fmpq()))
def succ(x):return np.nextafter(x,np.inf)
def pred(x):return np.nextafter(x,-np.inf)
raw=json.loads((D/'source/runs/forcing/p9_K64_n16_P8_merged.json').read_text())
rows={tuple(r[k] for k in ['ci','q','ks','kp']):r for r in raw['cells']}
p=Path('numerics/data/cert_green.npz');pin=sha(p)
with np.load(p) as data:
 tb=data['tb'][4096:4110].copy();tr=data['tb_rad'][4096:4110].copy()
assert len(tb)==len(tr)==14
# Isolated source primitive MR merely reconstructs the producer's h_up.
# Each resulting h_up is independently checked against exact knot-box width.
ns={'__name__':'isolated_midrad'};exec(compile((D/'source/src/midrad.py').read_text(),'frozen_midrad','exec'),ns);MR=ns['MR']
u=2.0**-53;dth=F.from_float(raw['theta_max'])/16; w_up=float(succ(float(dth/2)));wk=float(succ(2*w_up/8));w=ff(w_up);dw=ff(wk)
assert 8*dw>=2*w and w>=dth/2
xslo,xshi=map(ff,raw['x_star_bracket']);xs=bf(xslo).union(bf(xshi));rout=F(33,2000)*F(9,4)
# Point/radius interval used by the original producer encloses this bracket.
xstar=0.5*(float(xslo)+float(xshi));xrad=float(succ(max(float(xshi)-xstar,xstar-float(xslo))));assert ff(xstar)-ff(xrad)<=xslo and ff(xstar)+ff(xrad)>=xshi
power_checks=0
for j in range(1,19):assert ff(succ(w_up**j*(1+2*j*u)))>=w**j;power_checks+=1
angles={}
for q in range(16):
 centre=dth*F(2*q+1,2)
 for kp in range(8):
  aa=max(F(0),centre-w+kp*dw);bb=min(centre+w,centre-w+(kp+1)*dw)
  assert aa<bb and bb<F(1,100)
  sa,ca=bf(aa).sin_cos();sb,cb=bf(bb).sin_cos()
  angles[q,kp]=(aa,bb,ca,sa,cb,sb)
checked=omitted=0;fail=[];outcells=[];min_dmin_slack=None;min_dmax_slack=None;min_area_slack=None;min_omitted_gap=None
for idx,ci in enumerate(range(4096,4109)):
 h=(MR(tb[idx+1],tr[idx+1])-MR(tb[idx],tr[idx])).mag();hh=float(h);hF=ff(hh)
 true_width_upper=ff(tb[idx+1])+ff(tr[idx+1])-ff(tb[idx])+ff(tr[idx]);assert hF>=true_width_upper>0
 hk=float(succ(hh/64));hkF=ff(hk);assert 64*hkF>=hF
 for j in range(1,27):assert ff(succ(hh**j*(1+2*j*u)))>=hF**j;power_checks+=1
 tball=bf(ff(tb[idx])-ff(tr[idx])).union(bf(ff(tb[idx])+ff(tr[idx])))
 # Recreate only the original rounded radial bounds at128bits, then verify
 # them independently with the exact knot interval at256bits.
 rr=[]
 for ks in range(64):
  a=tball+bf(ks*hkF);b=tball+bf((ks+1)*hkF)
  emin=a.exp();emax=b.exp()
  ctx.prec=128; ta128=arb(float(tb[idx]),float(tr[idx])); cell128=(ta128+arb(hk)*ks).union(ta128+arb(hk)*(ks+1));exp128=cell128.exp()
  rlo=float(pred(float(exp128.lower())));rhi=float(succ(float(exp128.upper())));ctx.prec=256
  assert ff(rlo)<=lo(emin) and ff(rhi)>=hi(emax)
  rr.append((bf(ff(rlo)),bf(ff(rhi))))
 for q in range(16):
  for kp in range(8):
   aa,bb,ca,sa,cb,sb=angles[q,kp];xc=xs*ca;ys=xs*sa;yc=xs*sb;xb=xs*cb;ym=max(F(0),lo(ys));ym2=bf(ym)**2
   for ks,(r1,r2) in enumerate(rr):
    gap=max(F(0),lo(r1-xc),lo(xc-r2));dmlo=lo((bf(gap)**2+ym2).sqrt())
    dmhi=max(hi(((r1-xb)**2+yc**2).sqrt()),hi(((r2-xb)**2+yc**2).sqrt()))
    area_hi=hi((r2*r2-r1*r1)*bf(bb-aa))
    key=(ci,q,ks,kp);row=rows.get(key)
    if row is None:
     omitted+=1;gapout=dmlo-rout;min_omitted_gap=gapout if min_omitted_gap is None else min(min_omitted_gap,gapout)
     if gapout<0:fail.append({'kind':'omitted_possible_support','key':key,'lower_distance':str(dmlo),'gap':str(gapout)})
    else:
     checked+=1
     dl=dmlo-ff(row['dmin']);dh=ff(row['dmax'])-dmhi;da=ff(row['area'])-area_hi
     min_dmin_slack=dl if min_dmin_slack is None else min(min_dmin_slack,dl)
     min_dmax_slack=dh if min_dmax_slack is None else min(min_dmax_slack,dh)
     min_area_slack=da if min_area_slack is None else min(min_area_slack,da)
     if min(dl,dh,da)<0:fail.append({'kind':'included_row','key':key,'dmin_slack':str(dl),'dmax_slack':str(dh),'area_slack':str(da)})
 outcells.append(dict(ci=ci,tb=float(tb[idx]),tb_rad=float(tr[idx]),next_tb=float(tb[idx+1]),next_tb_rad=float(tr[idx+1]),h_up=hh,hk=hk))
assert checked==len(rows) and checked+omitted==13*16*64*8
assert sha(p)==pin
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_FINITE_GEOMETRY_PRIMARY_ONLY' if not fail else 'OPEN_GEOMETRY_FAILURES',seconds=time.monotonic()-start,green_path=str(p),green_sha256=pin,rows_checked=checked,omitted_cells_checked=omitted,all_cells=checked+omitted,power_checks=power_checks,w_up=w_up,wk=wk,exact_geometry_shift=str(w-dth/2),minimum_dmin_slack=str(min_dmin_slack),minimum_dmax_slack=str(min_dmax_slack),minimum_area_slack=str(min_area_slack),minimum_omitted_support_gap=str(min_omitted_gap),failures=fail[:30],failure_count=len(fail),cells=outcells,scope='Finite geometry and power weights only. Residual fields, Taylor coefficients, canonical inputs and full forcing bound remain OPEN.')
(D/'evidence/geometry_arb.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],'all',out['all_cells'],'failures',len(fail),'seconds',out['seconds']);assert not fail,fail[:2]

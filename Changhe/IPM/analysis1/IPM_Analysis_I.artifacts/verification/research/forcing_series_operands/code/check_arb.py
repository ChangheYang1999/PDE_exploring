"""Arb512 Horner coefficient bound, binomial recurrence and direct geometry."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time,sys
import numpy as np
from flint import arb,ctx
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];ctx.prec=512;tic=time.monotonic();ff=lambda x:Q.from_float(float(x))
def ar(x):return arb(x.numerator)/x.denominator
def lo(x):return Q(str(x.lower().fmpq()))
def hi(x):return Q(str(x.upper().fmpq()))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.loads((D/'evidence/blocks.json').read_text());raw=json.loads((B/'research/forcing_composed_cutoff/source/runs/forcing/v21_p9_merged.json').read_text())
with np.load(D/'evidence/operands.npz',allow_pickle=False) as z:d={k:z[k].copy() for k in z.files}
xsp=list(map(ff,raw['x_star_bracket']));xs=ar(xsp[0]).union(ar(xsp[1]));dtheta=ff(raw['theta_max'])/16;fails=[];coeffs=0;terms=0;minlo=minhi=None;records=[]
for n,r in enumerate(rows):
 H,W,c,U,x=map(ff,[r[k] for k in ['H','W','c0','Umax','xr']]);hb=ar(H);wb=ar(W);bb=arb(0)
 for i in range(12,-1,-1):
  v=arb(0)
  for j in range(8,-1,-1):v=v*wb+ar(abs(ff(d['uq_mid'][n,i,j]))+ff(d['uq_rad'][n,i,j]));terms+=1
  bb=bb*hb+v
 bb+=ar(ff(d['uq_rem'][n]));assert hi(bb)<=U,(n,'Horner Umax')
 assert hi(ar(U)/ar(c))<=x,(n,'ratio')
 if r['active']:
  tail=(ar(x)**17)/((1-ar(x))*ar(c).sqrt());assert hi(tail)<=ff(r['tail']),(n,'tail')
  coeff=1/ar(c).sqrt()
  for k in range(17):
   if k:coeff=-(coeff*(2*k-1))/(2*k*ar(c))
   m,rad=ff(d['coef_mid'][n,k]),ff(d['coef_rad'][n,k]);assert m-rad<=lo(coeff)<=hi(coeff)<=m+rad,(n,k);coeffs+=1
 # Direct physical q range, independent of the geometric Taylor model.
 # Radial upper endpoint is clipped to the original parent enclosure.
 center=dtheta*Q(2*r['q']+1,2);w=ff(r['w']);wk=ff(r['wk']);a=max(Q(0),center-w+4*r['bp']*wk);b=min(center+w,center-w+4*(r['bp']+1)*wk);assert 0<=a<b<Q(1,100)
 tlo=ff(r['tb'])-ff(r['tb_rad'])+r['bs']*H;thi=ff(r['tb'])+ff(r['tb_rad'])+min((r['bs']+1)*H,ff(r['h']))
 r1=ar(lo(ar(tlo).exp()));r2=ar(hi(ar(thi).exp()));sa,ca=ar(a).sin_cos();sb,cb=ar(b).sin_cos();xc=xs*ca;ys=xs*sa;xb=xs*cb;yb=xs*sb
 gap=max(Q(0),lo(r1-xc),lo(xc-r2));yl=max(Q(0),lo(ys));dl=max(Q(0),lo((ar(gap)**2+ar(yl)**2).sqrt()));dh=max(hi(((r1-xb)**2+yb**2).sqrt()),hi(((r2-xb)**2+yb**2).sqrt()))
 qlo=dl*dl;qhi=dh*dh;ml=qlo-c*(1-x);mh=c*(1+x)-qhi
 if min(ml,mh)<0:fails.append({'index':n,'key':[r[k] for k in ['ci','q','bs','bp']],'lower_margin':str(ml),'upper_margin':str(mh),'active':r['active']})
 minlo=ml if minlo is None else min(minlo,ml);minhi=mh if minhi is None else min(minhi,mh)
 records.append({'index':n,'B_interval':[str(lo(bb)),str(hi(bb))],'q_lower':str(qlo),'q_upper':str(qhi),'q_ratio_lower_margin':str(ml),'q_ratio_upper_margin':str(mh)})
assert terms==97344 and coeffs==13413
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-tic,'status':'PASS_ARB512_SERIES_AND_DIRECT_GEOMETRY' if not fails else 'OPEN_DIRECT_GEOMETRY_FAILURES','blocks':832,'coefficient_intervals':coeffs,'polynomial_terms':terms,'active_tails':789,'direct_geometry_boxes':832,'minimum_q_ratio_lower_margin':str(minlo),'minimum_q_ratio_upper_margin':str(minhi),'direct_geometry_failures':fails,'records':records,'operands_sha256':sha(D/'evidence/operands.npz'),'blocks_sha256':sha(D/'evidence/blocks.json'),'scope':'Finite contemporary scalar operands and uniform physical q ranges; no residual evaluation or historical-array acceptance.'}
(D/'evidence/arb.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],len(fails));print('minimum_q_margins',float(minlo),float(minhi));assert not fails,fails[:2]

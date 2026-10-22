"""Arb256 direct radii, distance square roots, area and exact regime margins."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time,sys
import numpy as np
from flint import arb,ctx
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];ctx.prec=256;start=time.monotonic()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def ff(x):return F.from_float(float(x))
def ar(x):return arb(x.numerator)/x.denominator
def lo(x):return F(str(x.lower().fmpq()))
def hi(x):return F(str(x.upper().fmpq()))
x=json.loads((D/'source/runs/forcing/v21_p9_merged.json').read_text());prior=B/'research/localized_forcing/evidence/geometry_arb.json';pg=json.loads(prior.read_text())
p=Path(pg['green_path']);assert sha(p)==pg['green_sha256']
with np.load(p,allow_pickle=False) as z:tb=z['tb'][4096:4110].copy();tr=z['tb_rad'][4096:4110].copy()
rows={tuple([r['ci'],r['q'],32*r['bs']+r['ks'],4*r['bp']+r['kp']]):r for r in x['cells']};assert len(rows)==43949
xs=ar(ff(x['x_star_bracket'][0])).union(ar(ff(x['x_star_bracket'][1])));dth=ff(x['theta_max'])/16;w=ff(pg['w_up']);dw=ff(pg['wk']);rin=F(231,8000);rout=F(297,8000)
assert 2*w>=dth and 8*dw>=2*w
angs={}
for q in range(16):
 c=dth*F(2*q+1,2)
 for j in range(8):
  a=max(F(0),c-w+j*dw);b=min(c+w,c-w+(j+1)*dw);assert 0<=a<b<F(1,100)
  sa,ca=ar(a).sin_cos();sb,cb=ar(b).sin_cos();angs[q,j]=(a,b,xs*ca,xs*sa,xs*cb,xs*sb)
count=omit=regcheck=0;regimes={k:0 for k in ['inside','transition','straddle']};mins={k:None for k in ['dmin','dmax','area','omission','sigma_low','sigma_high']}
def minimum(k,z):mins[k]=z if mins[k] is None else min(mins[k],z)
for ix,ci in enumerate(range(4096,4109)):
 cell=pg['cells'][ix];assert cell['ci']==ci and ff(cell['tb'])==ff(tb[ix]) and ff(cell['tb_rad'])==ff(tr[ix]);h=ff(cell['h_up']);hk=ff(cell['hk'])
 assert h>=ff(tb[ix+1])+ff(tr[ix+1])-ff(tb[ix])+ff(tr[ix]) and 64*hk>=h
 radial=[]
 for ks in range(64):
  r1=ar(lo(ar(ff(tb[ix])-ff(tr[ix])+ks*hk).exp()));r2=ar(hi(ar(ff(tb[ix])+ff(tr[ix])+(ks+1)*hk).exp()));radial.append((r1,r2))
 for (q,j),(a,b,xc,ys,xb,yb) in angs.items():
  ym=max(F(0),lo(ys));ym2=ar(ym)**2
  for ks,(r1,r2) in enumerate(radial):
   gap=max(F(0),lo(r1-xc),lo(xc-r2));low=lo((ar(gap)**2+ym2).sqrt());high=max(hi(((r1-xb)**2+yb**2).sqrt()),hi(((r2-xb)**2+yb**2).sqrt()));area=hi((r2*r2-r1*r1)*ar(b-a))
   row=rows.get((ci,q,ks,j))
   if row is None:
    assert low>rout,(ci,q,ks,j,'omission',low);minimum('omission',low-rout);omit+=1;continue
   dl=low-ff(row['dmin']);dh=ff(row['dmax'])-high;da=ff(row['area'])-area
   assert min(dl,dh,da)>=0,(ci,q,ks,j,dl,dh,da)
   minimum('dmin',dl);minimum('dmax',dh);minimum('area',da)
   slo,shi=map(ff,row['sigma']);actual_lo=(ff(row['dmin'])-rin)*F(4000,33);actual_hi=(ff(row['dmax'])-rin)*F(4000,33)
   assert slo<=actual_lo<=actual_hi<=shi;minimum('sigma_low',actual_lo-slo);minimum('sigma_high',shi-actual_hi)
   regime=row['regime'];regimes[regime]+=1
   if regime=='inside':assert shi<=0 and ff(row['dmax'])<=rin
   elif regime=='transition':assert 0<=slo<=shi<=1 and rin<=ff(row['dmin']) and ff(row['dmax'])<=rout
   else:assert shi>0
   regcheck+=1;count+=1
assert count==43949 and omit==62547 and regcheck==count
assert regimes=={k:x['regime_count'][k] for k in regimes};assert sha(p)==pg['green_sha256']
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-start,'status':'PASS_V21_GEOMETRY_AND_REGIMES_ARB','precision_bits':256,'source_sha256':sha(D/'source/runs/forcing/v21_p9_merged.json'),'green_sha256':pg['green_sha256'],'prior_geometry_sha256':sha(prior),'included':count,'omitted':omit,'regime_checks':regcheck,'regimes':regimes,'minimum_margins_exact':{k:str(v) for k,v in mins.items()},'scope':'Restricted physical parent subcells; exact dyadic source bracket and canonical-knot enclosure are inherited, physical residual models OPEN.'}
(D/'evidence/geometry_arb.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],'seconds')

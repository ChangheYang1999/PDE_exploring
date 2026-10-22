"""Every scalar inequality by exact rationals; iv160 coefficient verification."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time,math,sys
import numpy as np
from mpmath import iv
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];iv.dps=160;tic=time.monotonic();ff=lambda x:Q.from_float(float(x))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def vi(x):return iv.mpf(x.numerator)/x.denominator
def ep(t):
 s,m,e,_=t;return Q(-m if s else m)*Q(2)**e
def lo(x):return ep(x._mpi_[0])
def hi(x):return ep(x._mpi_[1])
rows=json.loads((D/'evidence/blocks.json').read_text());reg=json.loads((D/'evidence/regeneration.json').read_text());assert len(rows)==832
with np.load(D/'evidence/operands.npz',allow_pickle=False) as z:d={k:z[k].copy() for k in z.files}
assert d['uq_mid'].shape==d['uq_rad'].shape==(832,13,9)
fail=[];terms=0;ncoef=ntail=0;minU=minX=minT=None;records=[]
for n,r in enumerate(rows):
 assert tuple(d['indices'][n])==tuple(r[k] for k in ['ci','q','bs','bp']);H,W,c,U,x=map(ff,[r[k] for k in ['H','W','c0','Umax','xr']]);assert c>0 and x>=0
 hp=[H**i for i in range(13)];wp=[W**j for j in range(9)];bounds=Q(0)
 for i in range(13):
  for j in range(9):
   m,rad=ff(d['uq_mid'][n,i,j]),ff(d['uq_rad'][n,i,j]);assert rad>=0;bounds+=(abs(m)+rad)*hp[i]*wp[j];terms+=1
 bounds+=ff(d['uq_rem'][n]);assert bounds>0
 if U<bounds:fail.append({'block':n,'kind':'Umax','margin':str(U-bounds)})
 if c*x<U:fail.append({'block':n,'kind':'ratio','margin':str(c*x-U)})
 mu=(U-bounds)/bounds;mx=(c*x-U)/U;minU=mu if minU is None else min(minU,mu);minX=mx if minX is None else min(minX,mx)
 if r['active']:
  R=ff(r['tail']);assert 0<=x<Q(3,5) and R>0
  margin=R*R*c*(1-x)**2-x**34
  if margin<0:fail.append({'block':n,'kind':'tail','margin':str(margin)})
  rel=margin/x**34;minT=rel if minT is None else min(minT,rel);ntail+=1
  true_tail=vi(x)**17/(iv.sqrt(vi(c))*(1-vi(x)));assert hi(true_tail)<=R,(n,'iv tail',str(hi(true_tail)-R))
  for k in range(17):
   m,rad=ff(d['coef_mid'][n,k]),ff(d['coef_rad'][n,k]);assert rad>=0
   sign=(-1)**k;L=sign*m-rad;V=sign*m+rad;assert 0<L<=V
   a=Q(math.comb(2*k,k),4**k)*c**(-k);assert L*L*c<=a*a<=V*V*c,(n,k,'coefficient exact')
   exact=sign*vi(a)/iv.sqrt(vi(c));assert m-rad<=lo(exact)<=hi(exact)<=m+rad,(n,k,'coefficient iv');ncoef+=1
  records.append({'index':n,'key':[r[k] for k in ['ci','q','bs','bp']],'Umax_relative_margin':str(mu),'ratio_relative_margin':str(mx),'tail_squared_relative_margin':str(rel)})
assert ntail==789 and ncoef==13413 and terms==97344
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-tic,'status':'PASS_EXACT_SERIES_OPERANDS_AND_IV160' if not fail else 'OPEN_FAILED_SCALAR_TESTS','blocks':832,'polynomial_terms':terms,'active_tails':ntail,'coefficient_intervals_exact_and_iv':ncoef,'minimum_relative_Umax_margin':str(minU),'minimum_relative_ratio_margin':str(minX),'minimum_relative_squared_tail_margin':str(minT),'failures':fail,'records':records,'operands_sha256':sha(D/'evidence/operands.npz'),'blocks_sha256':sha(D/'evidence/blocks.json'),'scope':'Contemporary saved scalar operands. Model and historical execution scope remains restricted.'}
(D/'evidence/exact_iv.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],len(fail));print('minimum_relative_margins',float(minU),float(minX),float(minT));assert not fail,fail[:3]

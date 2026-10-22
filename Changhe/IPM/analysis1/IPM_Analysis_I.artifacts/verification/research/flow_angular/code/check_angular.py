"""Finite angular audit: source odd modes versus independent even modes."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,time,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_angular/evidence';SRC=B/'research/flow_certificate/evidence/source'
sys.path.insert(0,str(SRC));import cert_flow as source
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def ivarb(x):
 m,e=x.man_exp();return iv.mpf(int(m))*iv.mpf(2)**int(e)
def encl_iv(ball,ref):return bool(abs(ref-ivarb(ball.mid()))<=ivarb(ball.rad()))
def direct(theta,method):
 cv=arb if method=='arb' else iv.mpf;co=cv(0);de=cv(0);ha=cv(0);ao=cv(0);ad=cv(0);ah=cv(0);out=[]
 for n in range(1,262):
  x=2*n*theta;c=x.cos() if method=='arb' else iv.cos(x);s=x.sin() if method=='arb' else iv.sin(x)
  dc=-2*n*s;hc=-2*n*n*c;sg=(-1)**n;pre=-sg
  out.append(((c,dc,hc),(1+c+2*co,dc+2*de,hc+2*ha),(pre*(1+sg*c+2*ao),pre*(sg*dc+2*ad),pre*(sg*hc+2*ah))))
  co+=c;de+=dc;ha+=hc;ao+=sg*c;ad+=sg*dc;ah+=sg*hc
 return out

def main():
 start=time.monotonic();ctx.threads=1;ctx.prec=128;iv.dps=180
 hp=arb.pi()/2;stack=[]
 for i in range(200):stack.append((hp*i/200,hp*(i+1)/200,128*i,128*(i+1),0))
 ctx.prec=512;pi=arb.pi();ar=[pi*i/51200 for i in range(25601)];ir=[iv.pi*i/51200 for i in range(25601)]
 aw={w:pi*w/102400 for w in [1,2,4,8,16,32,64,128]};iw={w:iv.pi*w/102400 for w in aw}
 keys={};nodes=[];dvals=[];keyrows=[];selected=[];geocount=0
 while stack:
  a,b,l,r,depth=stack.pop();ctx.prec=128
  key=source.AngCache.key(None,a,b);width=r-l;dh=(b-a)/2;d=source.up(dh)
  assert key not in keys or keys[key]==(l,r),(l,r,keys.get(key));keys[key]=(l,r)
  if depth==0 or (depth>0 and l in (0,12800,25600-width)):selected.append((a,b,l,r,depth))
  if depth<7:
   m=(a+b)/2;mid=(l+r)//2;assert 2*mid==l+r
   stack.append((a,m,l,mid,depth+1));stack.append((m,b,mid,r,depth+1))
  ctx.prec=512
  for ball,ra,ri in [(a,ar[l],ir[l]),(b,ar[r],ir[r]),(dh,aw[width],iw[width])]:
   assert ball.contains(ra) and encl_iv(ball,ri),(l,r,depth);geocount+=2
  assert arb(d)>aw[width] and iv.mpf(d)>iw[width]
  nodes.append((l,r,depth));dvals.append(d);keyrows.append(key)
 assert len(nodes)==len(keys)==51000 and len(selected)==221
 ns=np.arange(1,262).astype(float);prefcos=(2*ns)**3;prefcs=2*ns+6*ns**2+8*ns**3+4*ns**4
 for n,p,q in zip(range(1,262),prefcos,prefcs):assert F(float(p))==(2*n)**3 and F(float(q))==4*n**4+8*n**3+6*n*n+2*n
 remainder_checks=0;ds=sorted(set(dvals));remarrays=[]
 for d in ds:
  row=[]
  for pref in [prefcos,prefcs]:
   rr=source.succ(pref*source.succ(d**3)/6*(1+16*source.U));row.append(rr)
   for n,rem in enumerate(rr,1):
    pre=(2*n)**3 if pref is prefcos else 4*n**4+8*n**3+6*n*n+2*n
    assert F(float(rem))>=pre*F(d)**3/6;(remainder_checks:=remainder_checks+1)
  remarrays.append(row)
 print(json.dumps({'utc':utc(),'stage':'geometry','nodes':len(nodes),'geometry_containments':geocount,'distinct_d':len(ds),'remainder_checks':remainder_checks}),flush=True)
 selected.sort(key=lambda x:(x[4],x[2]));mids=np.empty((221,3,3,261));rads=np.empty_like(mids);bounds=[];count=0;cache=source.AngCache(np.arange(1,262))
 for j,(a,b,l,r,depth) in enumerate(selected):
  ctx.prec=128;fac=cache.factors(a,b)
  for family,name in enumerate(['cos','C','S']):
   for derivative in range(3):mids[j,family,derivative]=fac[name][derivative].m;rads[j,family,derivative]=fac[name][derivative].r
  assert np.all(np.isfinite(mids[j])) and np.all(np.isfinite(rads[j])) and np.all(rads[j]>=0)
  ctx.prec=512;ra=direct(pi*(l+r)/102400,'arb');ri=direct(iv.pi*(l+r)/102400,'iv')
  for n in range(261):
   for fam in range(3):
    for k in range(3):
     m=float(mids[j,fam,k,n]);rad=float(rads[j,fam,k,n]);assert abs(ra[n][fam][k]-arb(m)).upper()<=arb(rad),(j,n,fam,k,'arb')
     assert abs(ri[n][fam][k]-iv.mpf(m))<=iv.mpf(rad),(j,n,fam,k,'iv');count+=2
  bounds.append((l,r,depth))
  if j%20==0:print(json.dumps({'utc':utc(),'stage':'coefficients','centers_done':j+1,'centers_total':221,'containments':count}),flush=True)
 np.savez(E/'finite_arrays.npz',nodes=np.asarray(nodes,dtype=np.int32),half_widths=np.asarray(dvals),keys=np.asarray(keyrows),selected=np.asarray(bounds,dtype=np.int32),midpoints=mids,radii=rads,distinct_half_widths=np.asarray(ds),remainder_arrays=np.asarray(remarrays))
 pins={str(p.relative_to(B)):sha(p) for p in [SRC/'cert_flow.py',SRC/'cert_resid.py',SRC/'midrad.py']}
 obj={'utc':utc(),'status':'PASS','code_sha256':sha(__file__),'proof_sha256':sha(B/'research/flow_angular/PROOF.md'),'source_pins':pins,'arrays_sha256':sha(E/'finite_arrays.npz'),'nodes':51000,'no_cache_collisions':True,'geometry_containments':geocount,'selected_centers':221,'modes':261,'coefficients_per_center':2349,'coefficient_containments':count,'distinct_half_widths':len(ds),'exact_remainder_checks':remainder_checks,'seconds':time.monotonic()-start,'methods':'Source Arb128 odd-frequency factors; independent Arb512 and iv180 even-frequency polynomial formulas. All node geometry checked in both independent interval systems.','scope':'Angular identities and enumerated finite values only. Radial TMs, all other refined-center values, full flow and inverse OPEN.'}
 (E/'checks.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj),flush=True)
if __name__=='__main__':main()

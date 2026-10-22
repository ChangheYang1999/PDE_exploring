"""Finite scalar reconstruction, exact dyadics, Arb512 and independent iv180."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'): os.environ[key]='1'
import sys,json,time,hashlib,platform,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import numpy as np
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3]; E=B/'research/flow_scalars/evidence'
sys.path.insert(0,str(B/'research/flow_certificate/evidence/source'))
from midrad import MR,succ,U
from cert_resid import bernstein_matrix
ctx.threads=1;iv.dps=180
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def qa(q):
 q=F(q);return arb(fmpq(q.numerator,q.denominator))
def qi(q):
 q=F(q);return iv.mpf(q.numerator)/q.denominator
def af(x):
 m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def vf(x):
 s,m,e,_=x;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def bounds(x):
 return (af(x.lower()),af(x.upper())) if isinstance(x,arb) else tuple(vf(z) for z in x._mpi_)
def muq(r):return F(1129,1000)+(F(238,25)-F(1129,1000))/(1+(r/6)**4)
def mua(r):return qa(F(1129,1000))+(qa(F(238,25))-qa(F(1129,1000)))/(1+(r/6)**4)
def mui(r):return qi(F(1129,1000))+(qi(F(238,25))-qi(F(1129,1000)))/(1+(r/6)**4)
def exact_points(part):
 pts=[]
 for sp in part['spans']:
  a,b=F(sp['a_exact']),F(sp['b_exact']);n=sp['count'];assert sp['first_cell']==len(pts)
  if pts:assert pts[-1]<a
  pts.extend(a+(b-a)*i/n for i in range(n))
 pts.append(F(part['spans'][-1]['b_exact']));return pts

def main():
 start=time.monotonic();counts=Counter();arrays={};stats={};hp_seen=set();const=[]
 files=[Path(__file__),B/'research/flow_scalars/PROOF.md',B/'research/flow_scalars/evidence/proof_first.json',B/'research/middle_residual/evidence/partition_exact.json']
 files += [B/'research/flow_certificate/evidence/source'/n for n in ['midrad.py','cert_resid.py','cert_flow.py']]
 files += [E/'source'/n for n in ['cert_green_outer.py','flow_outer.json','flow_inner.json']]
 files += [B/'research/flow_certificate/evidence/flow_middle.json']
 paths={reg:B.parent/'ipmA-num/data'/name for reg,name in [('middle','cert_green.npz'),('outer','cert_outer_green.npz'),('inner','cert_inner_green.npz')]}
 trial=B.parent/'ipmA-num/data/trial_v2_h0.008.npz';files += list(paths.values())+[trial]
 pins={str(p):sha(p) for p in files}
 assert pins[str(paths['middle'])]=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
 part=json.loads((B/'research/middle_residual/evidence/partition_exact.json').read_text());middle_pts=exact_points(part)
 tr=np.load(trial);k=float(tr['k']);ctx.prec=128
 GP=arb(1129)/1000;S=arb(129)/20+arb(307)/100
 def murep(r):return GP+(S-GP)/(1+(r/arb(6.0))**4)
 def ccheck(name,q,m,r):
  lo,hi=F(float(m))-F(float(r)),F(float(m))+F(float(r));assert lo<=q<=hi,(name,q,lo,hi)
  counts['rational_constant_contains']+=1;const.append({'name':name,'exact':str(q),'mid_hex':float(m).hex(),'rad_hex':float(r).hex()})
 for j in range(1,14):ccheck('inv_'+str(j),F(1,j),1.0/j,succ(U/j))
 for n in range(1,262):ccheck('inv4n_'+str(n),F(1,4*n),1.0/(4*n),succ(U/(4*n)))
 ccheck('cl',1/F(k),1.0/k,succ(U*abs(1.0/k)))
 BM=bernstein_matrix(12)
 for row in range(13):
  for col in range(13):ccheck('Bern_%d_%d'%(row,col),F(math.comb(row,col),math.comb(12,col)) if col<=row else F(0),BM.m[row,col],BM.r[row,col])
 for reg,nc in [('middle',7809),('outer',8948),('inner',2632)]:
  d=np.load(paths[reg]);base=F(0);base_rad=F(0)
  if reg=='middle':tm=d['tb'];rr=d['tb_rad'];pts=middle_pts
  else:
   tm=d['tau'];rr=d['tau_rad'];base=F(float(d['t0' if reg=='outer' else 'tmin']));base_rad=F(float(d['t0_rad' if reg=='outer' else 'tmin_rad']))
   assert base_rad==0
   pts=[base+(F(17*i,nc) if reg=='outer' else F(-5)+F(5*i,nc)) for i in range(nc+1)]
   assert base==(middle_pts[-1] if reg=='outer' else middle_pts[0])
  assert len(tm)==len(rr)==len(pts)==nc+1
  for i,t in enumerate(pts):assert base+F(float(tm[i]))-F(float(rr[i]))<=t<=base+F(float(tm[i]))+F(float(rr[i]));counts['partition_point_contains']+=1
  src=json.loads((B/'research/flow_certificate/evidence/flow_middle.json' if reg=='middle' else E/'source'/('flow_'+reg+'.json')).read_text())
  assert src['done'] and src['complete_region'] and src['nc_total']==len(src['rows'])==nc and src['selection']==[0,None]
  tmr=MR(tm,rr);out=np.empty((nc,36));matched=0
  for i in range(nc):
   ctx.prec=128
   h=(tmr[i+1]-tmr[i]).mag()
   ta=arb(float(tm[i]),float(rr[i]))
   if reg!='middle':ta=arb(float(base),float(base_rad))+ta
   EE=MR.from_arb([ta.exp()])[0]
   II=MR(1/EE.m,succ(EE.r/(EE.mig()**2)+U*abs(1/EE.m)))
   hp=np.array([1.0]+[succ(h**j*(1+2*j*U)) for j in range(1,27)])
   rl=float(-succ(-np.asarray(EE.m-EE.r,float)))
   rh=float(succ((EE.m+EE.r)*succ(1+h+h*h)))
   MM=MR.from_arb([murep(arb(rh)).union(murep(arb(rl)))])[0]
   vec=[float(h),float(EE.m),float(EE.r),float(II.m),float(II.r),rl,rh,float(MM.m),float(MM.r)]+hp.tolist()
   assert len(vec)==36 and all(math.isfinite(v) for v in vec)
   out[i]=vec
   hh,em,er,im,ir,rlo,rhi,mm,mr=map(F,vec[:9]);elo,ehi=em-er,em+er;ilo,ihi=im-ir,im+ir
   assert 0<pts[i+1]-pts[i]<=hh<F(1,522);counts['positive_cell_width_and_ode_hypothesis']+=1
   assert rlo>0 and elo>0 and er>=0 and ir>=0 and mr>=0
   assert ilo<=1/ehi and 1/elo<=ihi,(reg,i,'reciprocal');counts['exact_reciprocal_endpoint_contains']+=2
   for j,powup in enumerate(vec[9:]):assert F(powup)>=hh**j,(reg,i,'hpow',j);counts['exact_power_upper_comparisons']+=1
   hp_seen.add(float(h).hex())
   ml,mh=mm-mr,mm+mr
   assert ml<=muq(rhi)<=muq(rlo)<=mh,(reg,i,'rational_mu');counts['exact_mu_endpoint_contains']+=2
   ctx.prec=512
   tl=base+F(float(tm[i]))-F(float(rr[i]));th=base+F(float(tm[i]))+F(float(rr[i]))
   for engine,convert,exp,mu in [('arb512',qa,lambda z:z.exp(),mua),('iv180',qi,iv.exp,mui)]:
    for t in (tl,th):
     a,b=bounds(exp(convert(t)));assert elo<=a<=b<=ehi,(reg,i,'E',engine);counts[engine+'_E_endpoint_contains']+=1
    a,b=bounds(exp(convert(pts[i])));assert rlo<=a,(reg,i,'rlo',engine)
    a,b=bounds(exp(convert(pts[i+1])));assert b<=rhi,(reg,i,'rhi',engine);counts[engine+'_radial_endpoint_contains']+=2
    for r in (rlo,rhi):
     a,b=bounds(mu(convert(r)));assert ml<=a<=b<=mh,(reg,i,'mu',engine);counts[engine+'_mu_endpoint_contains']+=1
   row=src['rows'][i];assert row['ci']==i and row['region']==reg
   if row['r_lo']==rl and row['r_hi']==rh:matched+=1
   # Independently check the recorded historical geometry, without requiring identical reconstruction.
   assert qa(F(row['r_lo']))<=qa(pts[i]).exp() and qa(pts[i+1]).exp()<=qa(F(row['r_hi']));counts['recorded_radial_endpoint_contains']+=2
   if (i+1)%1000==0:
    msg={'utc':datetime.now(timezone.utc).isoformat(),'region':reg,'cells_complete':i+1,'cells_required':nc,'seconds':time.monotonic()-start};(E/'primary_progress.json').write_text(json.dumps(msg,indent=2)+'\n');print(json.dumps(msg),flush=True)
  arrays[reg]=out
  stats[reg]={'cells':nc,'r_hull_bitwise_matches_to_recorded':matched,'exact_first':str(pts[0]),'exact_last':str(pts[-1]),'max_h':float(out[:,0].max()),'max_reciprocal_radius':float(out[:,4].max())}
  d.close()
 assert counts['positive_cell_width_and_ode_hypothesis']==19389
 np.savez_compressed(E/'scalar_arrays.npz',**arrays)
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FINITE_RECONSTRUCTED_SCALARS_ONLY','counts':dict(counts),'regions':stats,'unique_h':len(hp_seen),'constants':const,'columns':['h','e_mid','e_rad','inv_mid','inv_rad','r_lo','r_hi','mu_mid','mu_rad']+['hpow_'+str(j) for j in range(27)],'array_sha256':sha(E/'scalar_arrays.npz'),'files':pins,'runtime':{'python':sys.version,'numpy':np.__version__,'platform':platform.platform(),'libc':platform.libc_ver()},'seconds':time.monotonic()-start}
 # Reject changes to any input while the checker ran.
 for p,v in pins.items():assert sha(p)==v,p
 (E/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('utc','status','counts','regions','unique_h','seconds')}),flush=True)
if __name__=='__main__':main()

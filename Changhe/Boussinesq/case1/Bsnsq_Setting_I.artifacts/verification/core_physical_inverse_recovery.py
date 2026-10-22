"""Localize strict inverse failures and validate only failed points with scalar MP."""
from pathlib import Path
import numpy as np
import mpmath as mp
from core_cartesian_residual import CorePhysicalModel,LD
from core_generating_mp import from_data
from check_core_dense_extrema import inverse
class RecoveredPhysicalModel(CorePhysicalModel):
 def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs);self.inverse_fallbacks=[]
 def invert(self,x,y,**kwargs):
  xx,yy=np.broadcast_arrays(np.asarray(x,dtype=LD),np.asarray(y,dtype=LD));shape=xx.shape;xx,yy=xx.ravel(),yy.ravel();ee=np.empty_like(xx);diags=[]
  def mpnum(t):
   n,d=LD(t).as_integer_ratio();return mp.mpf(n)/d
  def solve(idx):
   try:
    e,d=super(RecoveredPhysicalModel,self).invert(xx[idx],yy[idx],**kwargs);ee[idx]=e;diags.append(d)
   except ArithmeticError as exc:
    if len(idx)>1:
     n=len(idx)//2;solve(idx[:n]);solve(idx[n:]);return
    i=int(idx[0]);seed,seeddiag=super(RecoveredPhysicalModel,self).invert(xx[i],yy[i],tol=LD('1e-12'));checks=[];prev=None
    for dps in [100,140]:
     with mp.workdps(dps):
      G,a=from_data(self.data);xr,yr=mpnum(xx[i]),mpnum(yy[i]);er,defect,it=inverse(G,xr,yr,mpnum(seed),dps)
      err=abs(defect/yr) if yr else abs(defect);assert err<mp.mpf('1e-70')
      agreement=abs(er-mp.mpf(prev))/abs(er) if prev and er else None
      if agreement is not None:assert agreement<mp.mpf('1e-60')
      val=mp.nstr(er,175);checks.append({'dps':dps,'eta':val,'inverse_relative_y_defect':mp.nstr(err,150),'precision_relative_difference':mp.nstr(agreement,100) if agreement is not None else None,'iterations':it});prev=val
    ee[i]=LD(prev);z=self.mixed(xx[i],ee[i]);lddef=abs(z['y']-yy[i])/abs(yy[i]) if yy[i] else abs(z['y'])
    with mp.workdps(170):actual=mp.nstr(abs(mpnum(ee[i])-mp.mpf(prev))/abs(mp.mpf(prev)),100)
    self.inverse_fallbacks.append({'x':str(xx[i]),'y':str(yy[i]),'initial_failure':str(exc),'loose_seed':str(seed),'loose_seed_diagnostics':seeddiag,'references':checks,'rounded_eta':str(ee[i]),'actual_rounded_eta_relative_error':actual,'LD_reconstructed_y_defect':str(lddef)})
  solve(np.arange(len(xx)));return ee.reshape(shape),{'strict_subcall_diagnostics':diags,'fallback_count_total':len(self.inverse_fallbacks),'acceptance':'Strict original LDsubcalls; failedscalar MP100/140agreement1e-60 andcomposition1e-70'}

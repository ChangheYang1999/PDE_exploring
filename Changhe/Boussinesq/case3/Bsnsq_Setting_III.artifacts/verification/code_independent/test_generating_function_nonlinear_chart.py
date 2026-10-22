"""Manufacture with an explicitly invertible nonlinear physical chart.

Independent reference differentiates the explicit physical Psi(x,y), not the
mixed-coordinate Laplacian formulas. No lead code is imported.
"""
import sys,time,json
from pathlib import Path
import mpmath as mp
from generating_function_values import derivatives,physical
mp.mp.dps=85
start=time.monotonic();out=[]
for beta0 in ['2.3','3','5']:
 beta=mp.mpf(beta0);p=beta/2-1;a0=mp.mpf('1.7');d=mp.mpf('.13');h=mp.mpf('-.07')
 def S(q,y):return (y+d*y*y/2)*mp.sinh(q)+h*q**3/3
 def psi(x,y):
  q=mp.asinh(x/(1+d*y));sv=S(q,y);sq=(y+d*y*y/2)*mp.cosh(q)+h*q*q;sy=(1+d*y)*mp.sinh(q)
  return 2*beta*sv-p*q*sq-beta*y*sy
 def pd(i,j,x,y):return mp.diff(lambda xx:mp.diff(lambda yy:psi(xx,yy),y,j),x,i)
 for q0,y0 in [('.17','-.4'),('.6','.7'),('-.3','.2')]:
  q=mp.mpf(q0);y=mp.mpf(y0);x=(1+d*y)*mp.sinh(q);om=-pd(2,0,x,y)-pd(0,2,x,y);ox=-pd(3,0,x,y)-pd(1,2,x,y);oy=-pd(2,1,x,y)-pd(0,3,x,y);w1=beta*x-pd(0,1,x,y);w2=beta*y+pd(1,0,x,y);thx=2*a0*q/((1+d*y)*mp.cosh(q));res=w1*ox+w2*oy+om-thx;norm=abs(w1*ox)+abs(w2*oy)+abs(om)+abs(thx)
  for step in ['.001','.0005']:
   got=physical(derivatives(S,q,y,mp.mpf(step),13),q,y,beta,a0);errors={key:mp.nstr(abs(got[key]-val)/max(1,abs(val)),20)for key,val in [('Omega',om),('W1',w1),('W2',w2),('Theta_x',thx),('residual',res),('normalizer',norm),('ratio',abs(res)/norm)]};worst=max(mp.mpf(v)for v in errors.values());assert worst<mp.mpf('1e-23'),(beta0,q0,y0,step,errors);out.append(dict(beta=beta0,q=q0,y=y0,step=step,relative_errors=errors))
result={'status':'CONFIRMED','checks':out,'elapsed_seconds':time.monotonic()-start,'method':'explicit physical q=asinh(x/(1+d*y)); MP physical Psi derivatives versus independent mixed value-only finite differences'}
Path('research/105_independent_generating_function_evaluator/verification/nonlinear_chart_tests.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'],len(out),'checks','max_error',max(float(v)for row in out for v in row['relative_errors'].values()),'elapsed',result['elapsed_seconds'])

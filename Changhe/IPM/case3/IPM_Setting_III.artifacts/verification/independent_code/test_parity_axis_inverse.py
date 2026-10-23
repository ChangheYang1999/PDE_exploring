from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json
import numpy as np
from direct_inverse import DirectInverse,Quadrature
from parity_axis_inverse import interpolate_vertical
nodes=[F(1),F(1,4),F(1,16),F(1,64)];rational=[]
for z in [F(0),F(1,1000000),F(1,64),F(1,400)]:
 weights=[]
 for i,v in enumerate(nodes):
  w=F(1)
  for j,u in enumerate(nodes):
   if i!=j:w*=(z-u)/(v-u)
  weights.append(w)
 for k in range(4):assert sum((w*v**k for w,v in zip(weights,nodes)),F(0))==z**k
 rational.append(dict(z=str(z),weights=list(map(str,weights)),l1=str(sum(map(abs,weights)))))
def rho(x,y):
 s=np.asarray(x)**2+np.asarray(y)**2
 return -y*(4+3.5*s)*(1+s)**(-1.25)
def exact(x,y):
 s=x*x+y*y
 return (1+s)**(-.25)-.5*x*x*(1+s)**(-1.25)
rows=[]
for level,config in [(1,Quadrature(40,256,144,4.,1.,.5,16.,2.)),(2,Quadrature(64,512,224,8.,1.,.5,16.,2.))]:
 inv=DirectInverse(rho,config)
 for x in [.002,1.,50.]:
  y=x*1e-10;truth=exact(x,y)
  raw=inv.velocity(x,y)[1]/y
  for h in [.008,.004,.002]:
   v=interpolate_vertical(inv,x,y,h);v.update(level=level,x=x,y=y,exact_quotient=truth,raw_quotient=float(raw),absolute_error=abs(v['vertical_quotient']-truth),raw_error=abs(raw-truth));rows.append(v)
   print(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),level=level,x=x,h=h,error=v['absolute_error'],raw_error=v['raw_error'])),flush=True)
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS' if max(r['absolute_error'] for r in rows if r['level']==2)<1e-7 else 'OPEN',rational_checks=rational,rows=rows,scope='Manufactured Poisson pair and finite direct-inverse checks. Tolerance1e-7 is an empirical gate, not an interval certificate.')
Path('research/parity_inverse_verification/verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['rows','rational_checks']},indent=2))
if result['status']!='PASS':raise RuntimeError('Manufactured direct-parity inverse accuracy gate unresolved')

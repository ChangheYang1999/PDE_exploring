"""Direct finite-square kernel quadrature for Omega=sin(x), NOT a B2 profile.
The y kernel integral is elementary; remaining x integration is independent
of the boundary identity used in the proof. No infinite exterior is set to0.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,time
import numpy as np
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Conditional inverse manufacture. Finite-square integrals are explicitly truncated diagnostics, not physical box inverses.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'runs':[]}
def vertical_integrated(s,x,y,R):
 a=s-x
 if a==0:return 0.
 return math.copysign(1.,a)/(2*math.pi)*(math.atan((R-y)/abs(a))+math.atan((R+y)/abs(a)))
for x,y in ((.7,1.2),(2.3,-.9),(-.4,2.1)):
 for R in (8.,16.,32.,64.,128.,256.,512.,1024.):
  def ky(s):return math.sin(s)*(vertical_integrated(s,x,y,R)-vertical_integrated(s,0.,0.,R))
  def kx(s):
   a=s-x
   return math.sin(s)*math.log1p(4*R*y/((R-y)**2+a*a))/(4*math.pi)
  edges=sorted([-R,0.,x,R]);val=[];errors=[]
  for fun in (kx,ky):
   terms=[quad(fun,l,r,epsabs=2e-11,epsrel=2e-11,limit=3000) for l,r in zip(edges[:-1],edges[1:]) if r>l]
   val.append(math.fsum(v for v,e in terms));errors.append(math.fsum(e for v,e in terms))
  target=[0.,math.cos(x)-1];out['runs'].append({'point':[x,y],'R':R,'truncated_value':val,'target':target,'max_error':max(abs(v-t) for v,t in zip(val,target)),'quad_error_estimates':errors})
# Absolute tail restricted to the strip s>10, eta in[s,2s], X=(0,1.2).
# The kernel has one sign here, so its y-integral is also its absolute integral.
g,w=leggauss(24);out['absolute_strip']=[]
for R in (32.,64.,128.,256.,512.,1024.,2048.,4096.):
 edges=np.r_[10.,np.pi*np.arange(math.floor(10/math.pi)+1,math.ceil(R/math.pi)),R];edges=np.unique(edges[(edges>=10)&(edges<=R)])
 s=(edges[:-1,None]+edges[1:,None])/2+np.diff(edges)[:,None]*g/2;delta=1.2/s
 integrated=(np.arctan(-delta/(5-2*delta))-np.arctan(-delta/(2-delta)))/(2*math.pi)
 value=float(np.sum(np.diff(edges)[:,None]/2*w*np.abs(np.sin(s))*integrated))
 out['absolute_strip'].append({'R':R,'integral':value})
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
Path('verification/sublinear_inverse_shear.json').write_text(json.dumps(out,indent=2)+'\n')
print('finest errors',[r['max_error'] for r in out['runs'] if r['R']==1024.]);print('strip',out['absolute_strip']);print('COMPLETE',out['elapsed_seconds'])

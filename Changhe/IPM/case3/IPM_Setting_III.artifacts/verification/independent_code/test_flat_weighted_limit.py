"""Independent rational Schur-tail certificate and shifted-matrix audit."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
alpha=lambda r:F(1,4*(2*r+1))
N=8;tau=2*alpha(N+1);hi=F(363427799,10**9);lo=F(363427798,10**9)
def pivots(lam,tail):
 p={N:lam-alpha(N)**2/(lam-tau) if tail else lam}
 for r in range(N-1,0,-1):p[r]=lam-alpha(r)**2/p[r+1]
 p[0]=lam-2*alpha(0)**2/p[1]
 return p
up=pivots(hi,True);low=pivots(lo,False)
assert hi>tau and all(v>0 for v in up.values())
assert all(low[r]>0 for r in range(1,N+1)) and low[0]<0
identities=0
for m in range(3,202,2):
 J=(m-1)//2
 for j in range(1,2*m+5):
  q=2*j;k=j-J-1;bb=F(m*m+q*q,4*abs(q*q-m*m))
  target=F(1,4*abs(2*k+1));difference=bb/m-target
  assert difference==F((1 if q>m else -1)*q,4*m*(q+m))
  assert abs(difference)<=F(1,4*m)
  identities+=1
 for k in range(-2*m,-J-1):assert F(1,4*abs(2*k+1))<=F(1,4*m)
 bnear=F(m*m+(m+1)**2,4*(2*m+1));assert bnear>F(1,2)
# Supporting spectra; exact bounds above do not use these decimals.
spectra=[]
for radius in (4,8,16,32):
 ks=np.arange(-radius,radius);edges=1/(4*np.abs(2*ks+1))
 val=float(np.linalg.eigvalsh(np.diag(edges,1)+np.diag(edges,-1))[-1])
 spectra.append({'kind':'limit_truncation','radius':radius,'top':val})
 if radius>=8:assert float(lo)<val<float(hi)
for m in (3,9,31,101):
 count=m+32;j=np.arange(1,count);edges=(m*m+4*j*j)/(4*np.abs(4*j*j-m*m))
 diag=np.full(count,.5);diag[0]=.25
 for sign in (1,-1):
  val=float(np.linalg.eigvalsh(np.diag(sign*diag)+np.diag(edges,1)+np.diag(edges,-1))[-1])/m
  spectra.append({'kind':'scaled_weighted_truncation','m':m,'size':count,'diagonal_sign':sign,'top':val})
  assert val<float(hi)+1/m
res={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','N':N,'lambda_lower':str(lo),'lambda_upper':str(hi),'tail_upper':str(tau),'upper_pivots':{str(k):str(v) for k,v in up.items()},'finite_lower_pivots':{str(k):str(v) for k,v in low.items()},'reciprocal_lower':str(1/hi),'reciprocal_upper':str(1/lo),'exact_shift_identity_checks':identities,'supporting_spectra':spectra,'scope':'Two-sided exact bounds for the full infinite limiting Jacobi matrix. The tail is bounded analytically; floating spectra are only support. Profile conclusions require flatness, with additional cap only where stated.'}
Path('research/flat_weighted_limit/verification/checks.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'status':'PASS','lambda_lower':str(lo),'lambda_upper':str(hi),'exact_shift_checks':identities,'spectra':len(spectra)}),flush=True)

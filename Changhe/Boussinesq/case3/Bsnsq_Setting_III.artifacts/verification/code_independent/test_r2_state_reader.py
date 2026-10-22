from pathlib import Path
import json,time
from datetime import datetime,timezone
import numpy as np
from r2_state_values import R2State
from finite_difference import derivative
start=time.monotonic();root=Path('verification/r2_reader_manufacture');root.mkdir(exist_ok=True)
beta=2.5;L=2.;Nt=10;degree=5;K=4;grade=1.5
edges=np.linspace(0,1,Nt+1)**grade;knots=np.r_[np.zeros(degree),edges,np.ones(degree)];nb=len(knots)-degree-1
greville=np.array([np.mean(knots[j+1:j+degree+1]) for j in range(nb)])
aF=np.array([1.,.3,-.2,.15]);aG=np.array([.8,-.7,.6,-.4])
def coeff(a):return np.array([a[0]*np.ones(nb),a[1]*np.ones(nb),a[2]*greville,a[3]*greville]).ravel()
path=root/'state.npz';np.savez(path,cF=coeff(aF),cG=coeff(aG),beta=beta,beta_basis=beta,L=L,Nt=Nt,deg=degree,K=K,grade=grade,mreg=2,rmap='r2',scheme='mask',eps=1.)
state=R2State(path)
def exact(x,y,a,power):
 x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float));r2=x*x+y*y;S=L*L+r2
 logz=-np.log1p(r2/(L*L))/(2*beta);t=-np.expm1(logz)
 tr2=np.divide(t,r2,out=np.full_like(r2,1/(2*beta*L*L)),where=r2!=0)
 return np.exp(power*logz)*(a[0]-a[1]*y/np.sqrt(S)+a[2]*tr2*(y*y-x*x)+a[3]*tr2*y*(3*x*x-y*y)/np.sqrt(S))
rng=np.random.default_rng(203119);points=np.vstack((rng.normal(size=(200,2))*3,rng.normal(size=(100,2))*1e-5,[[0,0],[0,2],[0,-2]]))
errF=float(np.max(abs(state.divided(*points.T,'F')-exact(*points.T,aF,beta+2))))
errG=float(np.max(abs(state.divided(*points.T,'G')-exact(*points.T,aG,beta+1))))
c_expected=-beta*L*(aG[1]-aG[3]/2)/4
out={'utc':datetime.now(timezone.utc).isoformat(),'value_errors':[errF,errG],'strain_error':state.strain()-c_expected,'center':state.center(),'expected_Fdy':-aF[1]/L,'expected_Gdy':-aG[1]/L,'scope':'Manufactured exact constant/linear spline identities, not a B2 profile','elapsed_seconds':time.monotonic()-start}
(root/'result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
assert max(errF,errG)<3e-15
assert abs(state.strain()-c_expected)<1e-14

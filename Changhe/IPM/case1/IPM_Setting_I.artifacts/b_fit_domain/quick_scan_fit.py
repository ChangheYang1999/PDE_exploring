"""Common-grid transport comparison without retaining large field exports.
Fit-convention version (lead, 2026-10-18; VERIFY_REPORT G64 (b)): the inverse domain is the shape's stored R_shape
(closure at R_shape L, as in the fit), not R = 1000. Identical to quick_scan.py for shapes with R_shape = 1000."""
import sys,json
from pathlib import Path
import numpy as np
from centre_fit import load_shape
from metrics import residual_table

path=sys.argv[1]
nr=int(sys.argv[2]) if len(sys.argv)>2 else 2560
nt=int(sys.argv[3]) if len(sys.argv)>3 else 640
with np.load(path) as _z:
    Rsh=float(_z["R_shape"]) if "R_shape" in _z else 1000.
s,z=load_shape(path,nr,nt,R=Rsh)
_,f,L2,res,den=s.evaluate(z)
cen=s.centre(z,f,L2)
source=s.source(f,L2,1/z[0]);L=np.sqrt(L2)
rho=L**3*f["rho"];R=rho*res
W1=(1/z[0]+L2*f["ux"])*L*s.p.rr*s.p.ct
W2=(1/z[0]+L2*f["uy"])*L*s.p.rr*s.p.st
rx=L2*f["fx"];ry=L2*(s.p.st*f["rt"]+s.p.ct*f["ra"])/s.p.rr
dd=np.abs(W1*rx)+np.abs(W2*ry)+np.abs(rho)
wa=1/z[0]+L2*f["ux"];wb=1/z[0]+L2*f["uy"]
ad=np.stack([np.abs(wa[:,0]*(2+f["ht"][:,0]))+np.abs(wb[:,0])+1,
             np.abs(2*wa[:,-1])+np.abs(wb[:,-1]*(1+f["ht"][:,-1]))+1],axis=1)
tab=residual_table(s.p.r*L,s.p.theta,rho,R,dd,np.abs(rho)*den,
                   res[:,[0,-1]]/ad,(res/den)[:,[0,-1]])
ans=dict(file=path,nr=nr,nt=nt,cl=1/z[0],L=L,xstar=float(np.exp(source[0])*L),
         hP=source[1],centre=cen,bands=tab)
with np.load(path) as saved:
    saved_L=float(saved["L"])
ans["centre_fixed_scale"]=s.centre(z,f,saved_L**2)
ans["saved_L"]=saved_L
ans["R_inverse_shape_units"]=Rsh
ans["inverse_c_at_saved_scale"]=saved_L**2*f["c"]
fdlog=(np.abs(wa*(2+f["ht"]*s.p.ct**2-f["ha"]*s.p.ct*s.p.st))+
       np.abs(wb*(1+f["ht"]*s.p.st**2+f["ha"]*s.p.ct*s.p.st))+1)
signed=res/fdlog
physical=s.p.r*L
mask=(physical>6.5)&(physical<10.5)
profiles=[]
for theta in (0.,.025,.05,.1,.2,.3,.5):
    j=int(np.argmin(np.abs(s.p.theta-theta)))
    a=signed[mask,j]
    profiles.append(dict(theta=float(s.p.theta[j]),r=physical[mask].tolist(),
                         residual=a.tolist(),max=float(np.max(np.abs(a))),
                         r_at_max=float(physical[mask][np.argmax(np.abs(a))]),
                         sign_changes=int(np.sum(a[:-1]*a[1:]<0))))
ans["near_P_profiles"]=profiles
output=sys.argv[4] if len(sys.argv)>4 else path.replace("_shape.npz","_scan.json")
Path(output).write_text(json.dumps(ans,indent=2))
print(json.dumps(ans,indent=2))

"""Exact knot insertion / zero angular extension, with transfer evidence.
refine_band.py: as refine.py, with the radial band given in physical radius: SRC DST radial RLO RHI
(midpoints of the knot intervals whose midpoint radius lies in (RLO, RHI) are inserted)."""
import json
import sys
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline
from centre_fit import load_shape
from trial import Trial

src,dst,kind=sys.argv[1:4]
rlo,rhi=(float(v) for v in sys.argv[4:6])
old=np.load(src)
knots=np.unique(old["spline_knots"])
mid=(knots[:-1]+knots[1:])/2
insert=[]
angular=int(old["angular"])
kk,LL=float(old["k"]),float(old["L"])
qlo,qhi=(1-(1+(v/LL)**2)**(-(1-kk)/2) for v in (rlo,rhi))
if kind=="radial":
    insert=mid[(mid>qlo)&(mid<qhi)].tolist()
elif kind=="angular":
    angular+=20
elif kind=="both":
    insert=mid[(mid>.25)&(mid<.325)].tolist()
    angular+=20
else:
    raise ValueError(kind)
s,z=load_shape(src,angular=angular,insert=insert)
s.save(dst,z)
oldtrial,newtrial=Trial(src),Trial(dst)
radius=np.geomspace(.00077,7652,501)
theta=np.linspace(0,np.pi/2,121)
err=[]
for start in range(0,len(radius),25):
    rr=radius[start:start+25,None];tt=theta[None,:]
    a=oldtrial.fields(rr,tt,second=True)
    b=newtrial.fields(rr,tt,second=True)
    err.append([float(np.max(np.abs(x-y))) for x,y in zip(a,b)])
errors=np.max(err,axis=0)
ans=dict(source=src,output=dst,kind=kind,band_r=[rlo,rhi],band_q=[qlo,qhi],inserted_knots=insert,
         old_degree=int(old["degree"]),new_degree=s.degree,old_angular=int(old["angular"]),
         new_angular=angular,physical_derivative_errors=dict(zip(
             ("H","Ht","Htheta","Htt","Hthetatheta","Htthetatheta"),errors.tolist())))
Path(dst.replace("_shape.npz","_transfer.json")).write_text(json.dumps(ans,indent=2))
print(json.dumps(ans,indent=2))

"""Exact knot insertion / zero angular extension, with transfer evidence."""
import json
import sys
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline
from centre_fit import load_shape
from trial import Trial

src,dst,kind=sys.argv[1:4]
old=np.load(src)
knots=np.unique(old["spline_knots"])
mid=(knots[:-1]+knots[1:])/2
insert=[]
angular=int(old["angular"])
if kind=="radial":
    insert=mid[(mid>.25)&(mid<.325)].tolist()
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
ans=dict(source=src,output=dst,kind=kind,inserted_knots=insert,
         old_degree=int(old["degree"]),new_degree=s.degree,old_angular=int(old["angular"]),
         new_angular=angular,physical_derivative_errors=dict(zip(
             ("H","Ht","Htheta","Htt","Hthetatheta","Htthetatheta"),errors.tolist())))
Path(dst.replace("_shape.npz","_transfer.json")).write_text(json.dumps(ans,indent=2))
print(json.dumps(ans,indent=2))

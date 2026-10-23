"""Independent canonical inverse and both residual ratios on a nodal ray."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient
out=Path('research/critical_far_field_zeros/verification/nonprofile_T1.json')
rows=[]
for a in [1.,-1.]:
    tau=-2+2.5*a
    def rho(x,y):
        x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));r2=x*x+y*y
        return a*y*(1+r2)**(-.25)*(1-2*x*x/(1+r2))+4*tau*x*x*y*np.exp(-r2)
    levels=[]
    for level,config in enumerate([(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)]):
        nr,nt,ne,of=config;inv=DirectInverse(rho,Quadrature(nr,nt,ne,of,1.,.5,16.,2.))
        hh=np.array([.08,.04,.02,.01,.005]);slopes=np.array([inv.velocity(0.,h)[1]/h for h in hh])
        extrap=np.polynomial.polynomial.polyfit(hh*hh,slopes,3)[0]
        far=[]
        for r in [100.,1e4,1e6]:
            x=y=r/np.sqrt(2.);value=float(rho(x,y));u=inv.velocity(x,y);FD=[]
            for step in [.003,.0015,.00075]:
                gx,gy=cartesian_gradient(rho,x,y,step,0.);gx=float(gx);gy=float(gy)
                tx=(2*x+u[0])*gx;ty=(2*y+u[1])*gy;R=tx+ty-value
                nf=abs(tx)+abs(ty)+abs(value);nv=abs(value)+abs(x*gx+y*gy)+abs(u[0]*gx+u[1]*gy)
                FD.append({'step':step,'R':R,'Nf':nf,'Nv':nv,'R_Nf':abs(R)/nf,'R_Nv':abs(R)/nv})
            far.append({'radius':r,'rho':value,'U':u.tolist(),'FD8':FD})
        entry={'level':level,'center_h':hh.tolist(),'U2_over_y':slopes.tolist(),'center_extrapolation':float(extrap),'far':far}
        levels.append(entry);rows.append({'a':a,**entry});out.write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'points':rows},indent=2)+'\n')
        print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'a':a,'level':level,'c_extrapolated':float(extrap),'far_R':far[-1]['FD8'][-1]['R'],'far_Nv':far[-1]['FD8'][-1]['R_Nv']}),flush=True)
    assert abs(levels[-1]['center_extrapolation']+1)<2e-8
    assert abs(levels[-1]['far'][-1]['FD8'][-1]['R']+6*np.sqrt(2)/7)<2e-5
    assert abs(levels[-1]['far'][-1]['FD8'][-1]['R_Nv']-1)<2e-5
out.write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','points':rows,'scope':'Canonical non-profile manufactured test; it deliberately fails transport. It tests inverse strain and shows that Nf can decay while Nv tends to one on a far nodal ray.'},indent=2)+'\n')

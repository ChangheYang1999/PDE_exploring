"""Cartesian scalar-field FD with Omega differentiated independently of Psi.

The scalar provider supplies physical Psi, Theta and Omega. This checker takes
first and second Omega differences, so it does not define Omega by its own
Poisson stencil. No artificial denominator floors.
"""
import numpy as np
from physical_cartesian_fd import LD,difference,ratios


def evaluate(provider,points,beta,hrel,batch=12):
    pts=np.asarray(points,dtype=LD);x,y=pts.T;n=len(pts);b=LD(beta)
    h=LD(str(hrel))*np.maximum(LD(1),np.hypot(x,y));nodes=np.arange(-4,5,dtype=LD)
    specs={'Psi':[(0,0,''),(1,0,'_x'),(0,1,'_y'),(2,0,'_xx'),(1,1,'_xy'),(0,2,'_yy')],
           'Theta':[(0,0,''),(1,0,'_x'),(0,1,'_y'),(2,0,'_xx'),(1,1,'_xy'),(2,1,'_xxy')],
           'Omega':[(0,0,''),(1,0,'_x'),(0,1,'_y'),(1,1,'_xy')]}
    deriv={};diags=[]
    for start in range(0,n,batch):
        p=pts[start:start+batch];hs=h[start:start+batch]
        xx=p[:,0,None,None]+hs[:,None,None]*nodes[None,:,None]
        yy=p[:,1,None,None]+hs[:,None,None]*nodes[None,None,:]
        xx,yy=np.broadcast_arrays(xx,yy);v,info=provider(xx,yy);diags.append(info)
        for name,orders in specs.items():
            for dx,dy,suffix in orders:
                key=name+suffix
                if key not in deriv:deriv[key]=np.empty(n,dtype=LD)
                z=difference(np.asarray(v[name],dtype=LD),dx,1)
                z=difference(z,dy,1)/hs**(dx+dy)
                deriv[key][start:start+len(p)]=z
    d=deriv;u=-d['Psi_y'];v=d['Psi_x'];W1=b*x+u;W2=b*y+v
    wx=b-d['Psi_xy'];wy=b+d['Psi_xy'];o=d['Omega'];ox=d['Omega_x'];oy=d['Omega_y'];oxy=d['Omega_xy']
    th=d['Theta'];tx=d['Theta_x'];ty=d['Theta_y']
    TT=np.stack([W1*tx,W2*ty,-(b-2)*th],axis=-1)
    OT=np.stack([W1*ox,W2*oy,o,-tx],axis=-1)
    DT=np.zeros_like(TT);DO=np.zeros_like(OT)
    ix=x!=0;iy=y!=0;off=ix&iy
    DT[iy]=TT[iy]/y[iy,None]
    z=~iy;DT[z]=np.stack([W1[z]*d['Theta_xy'][z],wy[z]*ty[z],-(b-2)*ty[z]],axis=-1)
    DO[off]=OT[off]/(x[off]*y[off])[:,None]
    z=ix&~iy;DO[z]=np.stack([W1[z]*oxy[z]/x[z],wy[z]*oy[z]/x[z],oy[z]/x[z],-d['Theta_xy'][z]/x[z]],axis=-1)
    z=~ix&iy;DO[z]=np.stack([wx[z]*ox[z]/y[z],W2[z]*oxy[z]/y[z],ox[z]/y[z],-d['Theta_xx'][z]/y[z]],axis=-1)
    z=~ix&~iy;DO[z]=np.stack([wx[z]*oxy[z],wy[z]*oxy[z],oxy[z],-d['Theta_xxy'][z]],axis=-1)
    E=-d['Psi_xx']-d['Psi_yy']-o;NE=abs(d['Psi_xx'])+abs(d['Psi_yy'])+abs(o)
    out=dict(points=pts,h=h,U1=u,U2=v,W1=W1,W2=W2,Omega=o,Omega_x=ox,Omega_y=oy,Omega_xy=oxy,
             Theta=th,Theta_x=tx,Theta_y=ty,Theta_xxy=d['Theta_xxy'],c=d['Psi_xy'],
             E=E,NE=NE,R_Theta=TT.sum(axis=-1),N_Theta=abs(TT).sum(axis=-1),
             R_Omega=OT.sum(axis=-1),N_Omega=abs(OT).sum(axis=-1),
             D_Theta=DT.sum(axis=-1),ND_Theta=abs(DT).sum(axis=-1),
             D_Omega=DO.sum(axis=-1),ND_Omega=abs(DO).sum(axis=-1))
    summary={'hrel':str(hrel),'derivative_method':'9x9 Cartesian exact-rational stencil, paired parity sums; Omega supplied independently of Psi FD laplacian','provider_diagnostics':diags}
    for field,den in [('R_Theta','N_Theta'),('R_Omega','N_Omega'),('D_Theta','ND_Theta'),('D_Omega','ND_Omega'),('E','NE')]:
        r,info=ratios(out[field],out[den]);out[field+'_ratio']=r
        summary[field]={'max_abs':float(np.max(abs(out[field]))),'max_ratio':float(np.max(r)),'zero_handling':info}
    return out,summary,d

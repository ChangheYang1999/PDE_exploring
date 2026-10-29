"""Independent native-basis evaluator and source-centred transport coefficients.

No primary-lane evaluator is imported. The reference is our Taylor evaluator.
"""
from __future__ import annotations
import numpy as np
from scipy.special import eval_jacobi
from numpy.polynomial import legendre as leg,chebyshev as cheb,polynomial as poly
from piecewise_precision import expand_ball


class NativePhi:
    def __init__(self,field):
        if field.dilation!=1.:raise ValueError('Use native coordinates')
        self.field=field;self.c_l=field.c_l;self.elements=field.elements;self.interfaces=field.interfaces
        self.calls=0;self.points=0
        exact=expand_ball(field.metadata,field.coefficients)["phi"]
        C=np.zeros((1+max(a for a,b in exact),1+max(b for a,b in exact)))
        for ab,value in exact.items():C[ab]=float(value)
        self.cartesian={ab:poly.polyder(poly.polyder(C,m=ab[0],axis=0),m=ab[1],axis=1) for ab in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]}
        self.data=[]
        for i,e in enumerate(self.elements):
            C=field.matrices[i,'phi'].copy();L=C.shape[0]-1
            identity=np.eye(L+1)
            D1=leg.legder(identity,axis=0);D2=leg.legder(identity,m=2,axis=0)
            row=dict(C=C,D1=D1,D2=D2,L=L)
            if e['kind']=='shell':
                row.update(C1=cheb.chebder(C,axis=1),C2=cheb.chebder(C,m=2,axis=1))
            elif e['kind']=='exterior':row['powers']=np.array(field.radial_keys[i,'phi'])
            elif e.get('radial')!='jacobi':raise ValueError('Jacobi ball required')
            self.data.append(row)

    def jet(self,s,z):
        s,z=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(z,dtype=float));shape=s.shape
        sf=s.ravel();zf=z.ravel();R=np.sqrt(sf+zf*zf);out={ab:np.zeros_like(R) for ab in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]}
        self.calls+=1;self.points+=R.size
        near=R<.1*float(self.elements[0]['Rhi'])
        if np.any(near):
            for ab in out:out[ab][near]=poly.polyval2d(sf[near],zf[near],self.cartesian[ab])
        ids=np.searchsorted(self.interfaces,R,side='left')
        for i,e in enumerate(self.elements):
            hit=(ids==i)&~near
            if not np.any(hit):continue
            rad=R[hit];mu=zf[hit]/rad;d=self.data[i];C=d['C'];L=d['L'];V=leg.legvander(mu,L)
            V1=V[:,:d['D1'].shape[0]]@d['D1'];V2=V[:,:d['D2'].shape[0]]@d['D2']
            if e['kind']=='ball':
                Rb=float(e['Rhi']);x=2*(rad/Rb)**2-1;xp=4*rad/Rb**2;xpp=4/Rb**2
                A=np.zeros((len(rad),L+1));Ar=A.copy();Arr=A.copy()
                for n in range(L+1):
                    active=np.flatnonzero(C[n]!=0)
                    if not len(active):continue
                    kval=active[None,:];beta=n+.5
                    J=eval_jacobi(kval,0.,beta,x[:,None])
                    J1=np.zeros_like(J);mask=active>=1
                    if np.any(mask):J1[:,mask]=.5*(active[mask]+beta+1)*eval_jacobi(active[mask][None,:]-1,1.,beta+1,x[:,None])
                    J2=np.zeros_like(J);mask=active>=2
                    if np.any(mask):J2[:,mask]=.25*(active[mask]+beta+1)*(active[mask]+beta+2)*eval_jacobi(active[mask][None,:]-2,2.,beta+2,x[:,None])
                    w=C[n,active];f=J@w;fx=J1@w;fxx=J2@w;t=(rad/Rb)**n
                    A[:,n]=t*f
                    Ar[:,n]=t*(n*f/rad+fx*xp)
                    Arr[:,n]=t*(n*(n-1)*f/rad**2+2*n*fx*xp/rad+fxx*xp*xp+fx*xpp)
            elif e['kind']=='shell':
                logr=np.log(float(e['Rhi'])/float(e['Rlo']));x=2*np.log(rad/float(e['Rlo']))/logr-1
                xp=2/(logr*rad);xpp=-xp/rad
                A=cheb.chebval(x,C.T).T;Ax=cheb.chebval(x,d['C1'].T).T;Axx=cheb.chebval(x,d['C2'].T).T
                Ar=Ax*xp[:,None];Arr=Axx*xp[:,None]**2+Ax*xpp[:,None]
            else:
                powers=d['powers'];f=(rad[:,None]/float(e['Rlo']))**(-powers[None,:]);A=f@C.T
                Ar=(f*(-powers)[None,:])@C.T/rad[:,None]
                Arr=(f*(powers*(powers+1))[None,:])@C.T/rad[:,None]**2
            P=np.sum(A*V,axis=1);Pr=np.sum(Ar*V,axis=1);Pm=np.sum(A*V1,axis=1)
            Prr=np.sum(Arr*V,axis=1);Prm=np.sum(Ar*V1,axis=1);Pmm=np.sum(A*V2,axis=1)
            Rs=.5/rad;Rz=mu;ms=-.5*mu/rad**2;mz=(1-mu*mu)/rad
            out[0,0][hit]=P;out[1,0][hit]=Pr*Rs+Pm*ms;out[0,1][hit]=Pr*Rz+Pm*mz
            out[2,0][hit]=Prr*Rs*Rs+2*Prm*Rs*ms+Pmm*ms*ms-Pr/(4*rad**3)+Pm*3*mu/(4*rad**4)
            out[1,1][hit]=Prr*Rs*Rz+Prm*(Rs*mz+ms*Rz)+Pmm*ms*mz-Pr*mu/(2*rad**2)+Pm*(3*mu*mu-1)/(2*rad**3)
            out[0,2][hit]=Prr*Rz*Rz+2*Prm*Rz*mz+Pmm*mz*mz+Pr*(1-mu*mu)/rad-Pm*3*mu*(1-mu*mu)/rad**2
        return {ab:a.reshape(shape) for ab,a in out.items()}


class SourceCoefficients:
    def __init__(self,phi,K=3.5,repair_radius=.3):
        self.phi=phi;self.K=K;self.c_l=phi.c_l;self.repair_radius=repair_radius
        z=float(phi.field.metadata.get('z0',0.))
        for _ in range(30):
            p=phi.jet(0.,z);step=float((self.c_l*z+2*p[0,0])/(self.c_l+2*p[0,1]));z-=step
            if abs(step)<1e-14:break
        p=phi.jet(0.,z);self.z0=z;self.epsilon=float(.5-p[0,1]);self.hz=float(2*p[0,2]/(1+self.c_l))
        self.eta0=float(4*K*K*p[0,2]/(1+self.c_l)**2)
        self.source=dict(z0=z,epsilon=self.epsilon,repair_radius=repair_radius,phi_zz=float(p[0,2]),hz=self.hz,eta0=self.eta0,
                         raw_Wz=float(self.c_l*z+2*p[0,0]),source_root_certified=False)
        self.minimum_F=np.inf

    def __call__(self,x,mu):
        mu=np.asarray(mu,dtype=float)
        if np.max(np.abs(mu))>1+1e-8:raise ValueError('angular characteristic escaped')
        mu=np.clip(mu,-1,1);rho=np.exp(x);s=rho*rho*(1-mu*mu);t=rho*mu;z=self.z0+t
        p=self.phi.jet(s,z);delta2=self.repair_radius**2;E=self.epsilon*np.exp(-(s+t*t)/delta2)
        p[0,0]+=t*E;p[1,0]-=t*E/delta2;p[0,1]+=E*(1-2*t*t/delta2)
        p[2,0]+=t*E/delta2**2;p[1,1]-=E*(1-2*t*t/delta2)/delta2;p[0,2]+=E*(-6*t/delta2+4*t**3/delta2**2)
        A=self.c_l-p[0,1];a=1-2*p[0,1];Wz=self.c_l*z+2*p[0,0]+2*s*p[1,0]
        sm=-2*rho*rho*mu;phizm=p[1,1]*sm+p[0,2]*rho;Am=-phizm;am=-2*phizm
        Wzm=self.c_l*rho+4*sm*p[1,0]+2*rho*p[0,1]+2*s*sm*p[2,0]+2*s*rho*p[1,1]
        F=(1-mu*mu)*A+mu*Wz/rho;G=(1-mu*mu)*(Wz/rho-mu*A)
        Fm=-2*mu*A+(1-mu*mu)*Am+Wz/rho+mu*Wzm/rho
        Gm=-2*mu*(Wz/rho-mu*A)+(1-mu*mu)*(Wzm/rho-A-mu*Am)
        self.minimum_F=min(self.minimum_F,float(np.min(F)))
        if np.any(F<=0):raise ValueError('Nonpositive source-centred radial transport speed')
        return dict(v=G/F,b=a/F,vm=(Gm*F-G*Fm)/(F*F),bm=(am*F-a*Fm)/(F*F),lam=(1+self.c_l)/F,F=F,rho=rho)

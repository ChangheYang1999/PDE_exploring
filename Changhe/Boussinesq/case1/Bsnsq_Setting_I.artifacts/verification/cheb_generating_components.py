"""Unit-scale second derivative components for exact anisotropic evaluation.
Copied from the verifier's own original scalar recurrence, which remains unchanged.
See research/scaled_generating_evaluator/PROOF.md. No teammate code imports.
"""
import numpy as np
from cheb_generating_data import Model, LD


def recurrence3(z,n):
    z=np.asarray(z,dtype=LD).ravel()
    r=np.zeros((4,n+1,z.size),dtype=LD);r[0,0]=1
    if n:r[0,1]=z;r[1,1]=1
    for j in range(2,n+1):
        for k in range(4):
            r[k,j]=2*z*r[k,j-1]-r[k,j-2]
            if k:r[k,j]+=2*k*r[k-1,j-1]
    return r


class ComponentsModel(Model):
    def third_polynomial(self,t,w):
        a=recurrence3(2*t-1,self.J);b=recurrence3(2*w-1,self.K)
        contracted=[self.c.T@a[j]*(2**j) for j in range(4)]
        return {(i,j):np.sum(contracted[i]*b[j],axis=0)*(2**j)
                for i in range(4) for j in range(4-i)}

    def mixed_vorticity(self,x,e,diagnostic=False):
        x,e=np.broadcast_arrays(np.asarray(x,dtype=LD),np.asarray(e,dtype=LD))
        shape=x.shape;x=x.ravel();e=e.ravel()
        E=1+x*x+e**6;q=LD(1)/3;d=-q;T=E**(-LD(1)/6)
        w=e*e*E**d
        if self.alpha==0:
            t=T;l=-T/6;l2=T/36;l3=-T/216
        else:
            aa=self.alpha;ea=np.exp(aa);k=np.expm1(aa);DD=1+(1-T)*k
            t=1-np.log1p((1-T)*k)/aa
            l=-k*T/(6*aa*DD);l2=k*ea*T/(36*aa*DD**2)
            l3=-k*ea*T/(216*aa*DD**2)-k*k*ea*T*T/(108*aa*DD**3)
        z=self.third_polynomial(t,w)
        P,Pt,Pw,Ptt,Ptw,Pww,Pttt,Pttw,Ptww,Pwww=[
            z[k] for k in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3)]]
        DP=l*Pt+d*w*Pw
        D2P=l2*Pt+l*l*Ptt+2*l*d*w*Ptw+d*d*w*Pw+d*d*w*w*Pww
        D3P=(l3*Pt+3*l*l2*Ptt+l**3*Pttt
             +3*d*w*(l2+l*d)*Ptw+3*l*l*d*w*Pttw
             +3*l*d*d*w*w*Ptww+d**3*w*Pw
             +3*d**3*w*w*Pww+d**3*w**3*Pwww)
        f=E**q*P
        fE=E**(q-1)*(q*P+DP)
        fEE=E**(q-2)*(q*(q-1)*P+(2*q-1)*DP+D2P)
        fEEE=E**(q-3)*(q*(q-1)*(q-2)*P
                       +(3*q*q-6*q+2)*DP+(3*q-3)*D2P+D3P)
        DPw=l*Ptw+d*w*Pww
        D2Pw=l2*Ptw+l*l*Pttw+2*l*d*w*Ptww+d*d*w*Pww+d*d*w*w*Pwww
        fe=2*e*Pw
        fee=2*Pw+4*e*e*E**d*Pww
        feee=12*e*E**d*Pww+8*e**3*E**(2*d)*Pwww
        fEe=2*e/E*DPw
        fEEe=2*e/E**2*(-DPw+D2Pw)
        fEee=2/E*DPw+4*e*e*E**(-LD(4)/3)*(d*Pww+l*Ptww+d*w*Pwww)
        Ee=6*e**5;Eee=30*e**4;Eeee=120*e**3
        Ft=fE*Ee+fe
        Ftt=fEE*Ee**2+fE*Eee+2*fEe*Ee+fee
        Fttt=(fEEE*Ee**3+3*fEEe*Ee**2+3*fEee*Ee+feee
              +3*fEE*Ee*Eee+3*fEe*Eee+fE*Eeee)
        Ge=x*(f+e*Ft);Gee=x*(2*Ft+e*Ftt);Geee=x*(3*Ftt+e*Fttt)
        S=f+2*x*x*fE
        Se=(fE+2*x*x*fEE)*Ee+fe+2*x*x*fEe
        See=(fEE+2*x*x*fEEE)*Ee**2+(fE+2*x*x*fEE)*Eee+2*(fEe+2*x*x*fEEe)*Ee+fee+2*x*x*fEee
        y=e*S;A=S+e*Se;Ae=2*Se+e*See
        B=e*(6*x*fE+4*x**3*fEE)
        Ax=6*x*fE+4*x**3*fEE+e*((6*x*fEE+4*x**3*fEEE)*Ee+6*x*fEe+4*x**3*fEEe)
        Bx=e*(6*fE+24*x*x*fEE+8*x**4*fEEE)
        M=5*Ge-e*Gee;V=M/A
        Ve=((4*Gee-e*Geee)*A-M*Ae)/A**2
        Vx=((5*A-e*Ae)*A-M*Ax)/A**2
        Omega=(1+B*B)/A*Ve-B*Vx-(Bx-B*Ax/A)*V-e*(Ax-B*Ae/A)+B
        # Independent algebraic arrangement, but sharing G derivative inputs.
        b=B/A;bx=(Bx*A-B*Ax)/A**2;be=(Ax*A-B*Ae)/A**2
        pe=3*x*A-M;pxx=3*x*Bx+e*Ax
        pxe=-2*A+3*x*Ax+e*Ae;pee=3*x*Ae-4*Gee+e*Geee
        O2=-pxx+2*b*pxe-(b*b+1/A**2)*pee+(bx-b*be+Ae/A**3)*pe
        U1naive=V-3*x;U2naive=B*V+e*A-3*y
        # Evaluate the analytically canceled stream function before taking its
        # first/second derivatives. Constant P manufactures otherwise subtract
        # O(x) terms to obtain velocities that can decay to zero.
        zz=1-1/E;LL=l*zz;DL=l2*zz+l/E;D2L=l3*zz+2*l2/E-l/E
        J=w*Pw-P
        DJ=w*l*Ptw+d*w*w*Pww-l*Pt
        D2J=(w*l2*Ptw+w*l*l*Pttw+2*d*l*w*w*Ptww
             +2*d*d*w*w*Pww+d*d*w**3*Pwww-l2*Pt-l*l*Ptt)
        DPt=l*Ptt+d*w*Ptw
        D2Pt=l2*Ptt+l*l*Pttt+2*l*d*w*Pttw+d*d*w*Ptw+d*d*w*w*Ptww
        H=6*LL*Pt+2/E*J
        DH=6*(DL*Pt+LL*DPt)+2/E*(DJ-J)
        D2H=6*(D2L*Pt+2*DL*DPt+LL*D2Pt)+2/E*(D2J-2*DJ+J)
        Hw=6*LL*Ptw+2/E*w*Pww
        Hww=6*LL*Ptww+2/E*(Pww+w*Pwww)
        DHw=6*(DL*Ptw+LL*(l*Pttw+d*w*Ptww))+2/E*((d-1)*w*Pww+w*l*Ptww+d*w*w*Pwww)
        ss=E**q*H
        sE=E**(q-1)*(q*H+DH)
        sEE=E**(q-2)*(q*(q-1)*H+(2*q-1)*DH+D2H)
        se=2*e*Hw;sEe=2*e/E*DHw;see=2*Hw+4*e*e*E**d*Hww
        st=sE*Ee+se;stt=sEE*Ee**2+sE*Eee+2*sEe*Ee+see
        sx=e*(ss+2*x*x*sE);sephys=x*(ss+e*st)
        sxx=e*(6*x*sE+4*x**3*sEE)
        sxe=ss+2*x*x*sE+e*((sE+2*x*x*sEE)*Ee+se+2*x*x*sEe)
        seephys=x*(2*st+e*stt)
        physical_xx=sxx-2*b*sxe+b*b*seephys-(bx-b*be)*sephys
        physical_yy=seephys/A**2-Ae/A**3*sephys
        stableOmega=-sxx+2*b*sxe-(b*b+1/A**2)*seephys+(bx-b*be+Ae/A**3)*sephys
        U1=-sephys/A;U2=sx-b*sephys
        out=dict(x=x,eta=e,y=y,A=A,Omega=stableOmega,Psi_xx=physical_xx,Psi_yy=physical_yy,Omega_alternate=O2,
                 Omega_uncanceled=Omega,U1=U1,U2=U2,U1_uncanceled=U1naive,U2_uncanceled=U2naive,
                 Psi=x*e*ss,
                 normalized_A=A/E**q,Theta=self.a*e,Theta_x=-self.a*B/A,Theta_y=self.a/A)
        if diagnostic:
            out.update(Ge=Ge,Gee=Gee,Geee=Geee,B=B,Ae=Ae,Ax=Ax,Bx=Bx,V=V,Ve=Ve,Vx=Vx)
        return {k:np.asarray(v).reshape(shape) for k,v in out.items()}

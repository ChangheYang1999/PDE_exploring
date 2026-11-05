#!/usr/bin/env python3
"""Independent FLOAT check of the exact x/Jq nonlinear energy decomposition."""
import json,time
from pathlib import Path
import numpy as np
from scipy.fft import fft2,ifft2,fftfreq
n=1024;R=24;dx=2*R/n;q=2.1
x=np.arange(n)*dx-R;xx,yy=np.meshgrid(x,x);rr=xx*xx+yy*yy;W=np.sqrt(1+4*rr)
g=np.sin(1.7*yy)*np.cos(.6*xx)*np.exp(-rr/3)
k=.03*np.sin(.9*yy)*np.cos(1.3*xx)*np.exp(-rr/7)
kk=2*np.pi*fftfreq(n,dx);kx,ky=np.meshgrid(kk,kk);s=kx*kx+ky*ky;J=np.sqrt(1+s)
U1=np.zeros_like(s);U2=np.zeros_like(s);U1[s>0]=kx[s>0]*ky[s>0]/s[s>0];U2[s>0]=-kx[s>0]**2/s[s>0]
kh=fft2(k);a1=ifft2(U1*kh).real;a2=ifft2(U2*kh).real

def Jpow(h,p):return ifft2(J**p*fft2(h)).real
def deriv(h,axis):return ifft2(1j*(kx if axis==0 else ky)*fft2(h)).real
def T(h):return a1*deriv(h,0)+a2*deriv(h,1)
def D(h,axis):return q*deriv(Jpow(h,q-2),axis)
def dot(f,h):return float(np.sum(f*h)*dx*dx)

f=Jpow(g,q);Tg=T(g);direct=dot(W*Jpow(Tg,q),W*f)
rhs=dot(Jpow(Tg,q),f);maxidentity=0.
for axis,coord,vel in [(0,xx,a1),(1,yy,a2)]:
 X=coord*f;Z=D(g,axis);h=coord*g;Y=Jpow(h,q)
 comm=Jpow(T(h),q)-T(Y)
 value=T(X)-T(Z)+comm-Jpow(vel*g,q)+D(Tg,axis)
 maxidentity=max(maxidentity,float(np.max(abs(coord*Jpow(Tg,q)-value))))
 rhs+=4*dot(value,X)
z={'status':'FLOAT_IDENTITY_CHECK_ONLY','direct_Q_nonlinear_energy':direct,'expanded_energy':rhs,'absolute_energy_difference':abs(direct-rhs),'max_pointwise_commuted_identity_error':maxidentity,'grid':n,'radius':R,'q':q}
p=Path(__file__).resolve().parent/'Qnorm_identity_float_check.json';p.write_text(json.dumps(z,indent=2)+'\n');print(json.dumps(z,indent=2))

"""Exact finite-mode far coefficients plus an independent Cartesian inverse check.

Uses coefficient endpoint sums, explicit trigonometric convolution and FD8.
No fitted velocity, matrix surrogate, or numerical-lane implementation is used.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[key]='1'
import argparse, json, hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from evaluate_smooth_state import ReconstructedSmooth
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient


def sine_modes(c):
    a=np.zeros(2*len(c));a[1]=c[0]
    for k in range(1,len(c)):
        a[2*k+1]+=c[k]/2;a[2*k-1]-=c[k]/2
    return a


def evaluate(a,theta,derivative=0):
    n=np.arange(len(a));theta=np.asarray(theta)
    return np.sum(a*n**derivative*np.sin(theta[...,None]*n+derivative*np.pi/2),axis=-1)


def angular_coefficients(obj):
    j=np.arange(obj.N+1,dtype=float)
    theta0=sine_modes(obj.L**(1-obj.p)*np.sum(obj.coeff,axis=1))
    theta1=sine_modes(-2*obj.L**(2*(1-obj.p))*(obj.coeff@(j*j)))
    source=np.zeros(len(theta0)+1)
    for n in range(1,len(theta0),2):
        source[n+1]+=(obj.p-n)*theta0[n]/2
        if n>1:source[n-1]+=(obj.p+n)*theta0[n]/2
    phi=np.zeros_like(source)
    for m in range(2,len(source),2):phi[m]=source[m]/(m*m-(obj.p+1)**2)
    return theta0,theta1,phi


def laurent_sin(a):
    out={}
    for n in range(1,len(a)):
        if a[n]:out[n]=a[n]/(2j);out[-n]=-a[n]/(2j)
    return out


def product(a,b):
    out={}
    for n,x in a.items():
        for m,y in b.items():out[n+m]=out.get(n+m,0)+x*y
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('state');ap.add_argument('--level',type=int,default=1);ap.add_argument('--tag')
    args=ap.parse_args();path=Path(args.state);obj=ReconstructedSmooth(path)
    a,b,phi=angular_coefficients(obj);D=obj.cl-1
    th0=laurent_sin(a);ph=laurent_sin(phi)
    ur={n:-1j*n*v for n,v in ph.items()};ut={n:(obj.p+1)*v for n,v in ph.items()}
    first=product(ur,th0);second=product(ut,{n:1j*n*v for n,v in th0.items()})
    F={n:obj.p*first.get(n,0)+second.get(n,0) for n in set(first)|set(second)}
    degrees=max(max(F,default=0),len(b)-1);e=np.zeros(degrees+1)
    imaginary_error=0.
    for n in range(1,degrees+1):
        c=2j*F.get(n,0);imaginary_error=max(imaginary_error,abs(c.imag))
        e[n]=c.real-(D*b[n] if n<len(b) else 0)
    grids=[]
    for nt in (129,257,513):
        theta=np.r_[np.linspace(.0002,np.pi/2,nt),.003,.219,.771,1.499]
        t0=evaluate(a,theta);t1=evaluate(b,theta)
        u0r=-evaluate(phi,theta,1);u0t=(obj.p+1)*evaluate(phi,theta)
        forcing=obj.p*u0r*t0+u0t*evaluate(a,theta,1);defect=forcing-D*t1
        direct=evaluate(e,theta)
        scale=abs(forcing)+abs(D*t1)
        relative=np.divide(abs(defect),scale,out=np.zeros_like(scale),where=scale>0)
        imax=int(np.argmax(abs(defect)));ir=int(np.argmax(relative))
        grids.append({'angular_points':len(theta),'max_abs_coefficient_defect':float(abs(defect[imax])),'angle_abs_max':float(theta[imax]),
          'max_relative_coefficient_defect':float(relative[ir]),'angle_relative_max':float(theta[ir]),
          'independent_convolution_max_error':float(np.max(abs(defect-direct))),
          'max_abs_Theta0':float(np.max(abs(t0))),'max_abs_Theta1':float(np.max(abs(t1))),
          'max_abs_predicted_Theta1':float(np.max(abs(forcing))/D)})
    nr,nt,ne,factor=[(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)][args.level]
    inv=DirectInverse(obj.rho,Quadrature(nr,nt,ne,factor,obj.L,obj.p,16*obj.L,1/(1-obj.p)))
    samples=[]
    for r in np.array([100.,1e4,1e6])*obj.L:
        for th in (.003,.219,.771,1.499,np.pi/2):
            x,y=r*np.cos(th),r*np.sin(th)
            if th==np.pi/2:x=0.
            rho=float(obj.rho(x,y));u=inv.velocity(x,y);gx,gy=cartesian_gradient(obj.rho,x,y,.00075)
            rx,ry=float(gx),float(gy);R=(obj.cl*x+u[0])*rx+(obj.cl*y+u[1])*ry-rho
            t0=float(evaluate(a,th));t1=float(evaluate(b,th));u0r=-float(evaluate(phi,th,1));u0t=(obj.p+1)*float(evaluate(phi,th))
            u0=np.array([u0r*np.cos(th)-u0t*np.sin(th),u0r*np.sin(th)+u0t*np.cos(th)])
            residual_coefficient=float(evaluate(e,th));q=2*obj.p-1
            samples.append({'r':float(r),'theta':th,'rho':rho,'U':u.tolist(),'R':float(R),
              'density_first_coefficient_measured':float((rho/r**obj.p-t0)/r**(obj.p-1)),
              'density_first_coefficient_formula':t1,
              'velocity_leading_scaled_error':float(np.max(abs(u/r**obj.p-u0))),
              'R_scaled_by_r_to_q':float(R/r**q),'R_coefficient_formula':residual_coefficient,
              'R_coefficient_difference':float(R/r**q-residual_coefficient)})
    result={'utc':datetime.now(timezone.utc).isoformat(),'source':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
      'cl':obj.cl,'p':obj.p,'L':obj.L,'N':obj.N,'M':obj.M,'quadrature_level':args.level,
      'Theta0_sine_coefficients':a.tolist(),'Theta1_sine_coefficients':b.tolist(),'Phi0_sine_coefficients':phi.tolist(),
      'R_leading_coefficient_sine_modes':e.tolist(),'convolution_imaginary_error':imaginary_error,
      'max_coefficient_outside_density_angular_support':float(np.max(abs(e[len(a):]))) if len(e)>len(a) else 0.,
      'grids':grids,'samples':samples,
      'scope':'Sampled and finite-coefficient checks only. E=F-(ell-1)Theta1 is the leading residual coefficient at order r^(2p-1). Its normalized physical residual decays at infinity even when E is nonzero; E is not itself a normalized PDE residual. The canonical inverse uses a separately implemented Cartesian singular integral, with exterior integration to infinity.'}
    dest=Path('evidence/smooth_far_field')/(args.tag or path.parent.name);dest.mkdir(parents=True,exist_ok=True)
    (dest/('q'+str(args.level)+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'utc':result['utc'],'state':str(path),'grids':grids,'samples':samples},indent=2),flush=True)

if __name__=='__main__':main()

"""FLOAT evaluation of the actual full-matrix Riesz residual quadratic form.

Source radial values/derivatives come from cancellation-resolved exact-source
Arb evaluation.  Quintic radial interpolation, smooth localization, finite-box
Fourier transforms, quadrature, and all tails remain uncertified here.
"""
import argparse,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.interpolate import BPoly
from scipy.fft import fft2,ifft2,fftfreq
from scipy.ndimage import map_coordinates
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'finite_rank'))
from full_remainder_screen import mesh
from fields013 import C

def source_grid(data,xx,yy,cutoff):
    rows=data['rows'];r=np.array([q['r']for q in rows]);F=np.array([q['F']for q in rows]);Fr=np.array([q['Fr']for q in rows]);Frr=np.array([q['Frr']for q in rows])
    spline=BPoly.from_derivatives(np.log(r),np.stack([F,r[:,None]*Fr,r[:,None]*Fr+r[:,None]**2*Frr],axis=1))
    out=np.zeros_like(xx);ns=F.shape[1]
    for i in range(0,xx.shape[0],32):
        x,y=xx[i:i+32],yy[i:i+32];radius=np.sqrt(x*x+y*y);theta=np.arctan2(y,x)
        coeff=spline(np.log(np.maximum(radius,r[0])));sn=np.sin(theta);cs=np.cos(theta);sn2=np.sin(2*theta);cs2=np.cos(2*theta)
        values=np.zeros_like(radius)
        for j in range(ns):
            values+=coeff[...,j]*sn
            sn,cs=sn*cs2+cs*sn2,cs*cs2-sn*sn2
        values[radius==0]=0
        out[i:i+32]=np.sqrt(1+4*radius**2)*values*np.exp(-(radius/cutoff)**16)
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--background',type=Path,default=HERE.parent/'finite_rank/radial_mesh_cache.float.json');ap.add_argument('--grid',type=int,default=1024);ap.add_argument('--matrix-grid',type=int,default=512);ap.add_argument('--radius',type=float,default=16);ap.add_argument('--cutoff',type=float,default=12);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    tick=time.monotonic();source=json.loads(args.source.read_text());bg=json.loads(args.background.read_text());N=args.grid;L=args.radius;dx=2*L/N;x=np.arange(N)*dx-L;xx,yy=np.meshgrid(x,x,indexing='xy');r2=xx*xx+yy*yy
    f=source_grid(source,xx,yy,args.cutoff);print('source ready',time.monotonic()-tick,flush=True)
    Ng=min(args.matrix_grid,N);xg=np.arange(Ng)*(2*L/Ng)-L;xg,yg=np.meshgrid(xg,xg,indexing='xy');rg2=xg*xg+yg*yg
    profile=mesh(bg,xg,yg);c=float(C);q=2.1
    Vx=c*xg+profile['u1',0,0];Vy=c*yg+profile['u2',0,0];aw=(Vx*xg+Vy*yg)/(.25+rg2)
    A=c+1+aw-q*(c+profile['u1',1,0])+profile['rho',0,1]
    D=c+1+aw-q*(c+profile['u2',0,1]);B=-q*(profile['u1',0,1]+profile['u2',1,0])/2-profile['rho',1,0]/2
    if Ng!=N:
        coords=np.meshgrid(np.arange(N)*Ng/N,np.arange(N)*Ng/N,indexing='ij')
        A=map_coordinates(A,coords,order=3,mode='nearest');B=map_coordinates(B,coords,order=3,mode='nearest');D=map_coordinates(D,coords,order=3,mode='nearest')
    determinant=A*D-B*B;mineig=(A+D)/2-np.hypot((A-D)/2,B)
    print('matrix ready',time.monotonic()-tick,flush=True)
    k=2*np.pi*fftfreq(N,d=dx);kx,ky=np.meshgrid(k,k,indexing='xy');k2=kx*kx+ky*ky;inverse=np.zeros_like(k2);inverse[k2>0]=1/np.sqrt(k2[k2>0])
    fh=fft2(f);hh=(1+k2)**(q/2)*fh;h=ifft2(hh).real;v1=ifft2(1j*kx*inverse*hh).real;v2=ifft2(1j*ky*inverse*hh).real
    hnorm=float(np.sqrt(np.sum(h*h)*dx*dx));vnorm=float(np.sqrt(np.sum(v1*v1+v2*v2)*dx*dx))
    h2norm=float(np.sqrt(np.sum(np.abs(fh)**2*(1+k2)**2)*dx*dx/N**2))
    h3norm=float(np.sqrt(np.sum(np.abs(fh)**2*(1+k2)**3)*dx*dx/N**2))
    dual2=float(np.sum((D*v1*v1-2*B*v1*v2+A*v2*v2)/determinant)*dx*dx)
    beta=.704955805507
    out={'status':'FLOAT_NOT_A_CERTIFICATE','source_file':str(args.source),'grid':N,'matrix_grid':Ng,'box_radius':L,'dx':dx,'cutoff_definition':f'exp(-(r/{args.cutoff})^16)','source_mean':float(np.sum(f)*dx*dx),'Hq_norm_screen':hnorm,'Riesz_Hq_norm_screen':vnorm,'full_matrix_dual_squared_screen':dual2,'full_matrix_dual_screen':math.sqrt(dual2),'effective_source_screen':math.sqrt(beta*dual2),'effective_source_ratio_to_global_Cauchy':math.sqrt(beta*dual2)/hnorm,'point_matrix_min_eigenvalue_screen':float(mineig.min()),'elapsed_seconds':time.monotonic()-tick,'open_errors':['quintic source interpolation','background interpolation','smooth cutoff error','periodic Riesz images','Fourier truncation and aliasing','spatial quadrature and full-plane tails','floating roundoff']}
    out.update(H2_norm_screen=h2norm,H3_norm_screen=h3norm)
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()

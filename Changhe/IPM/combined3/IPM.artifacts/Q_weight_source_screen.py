#!/usr/bin/env python3
"""FLOAT main-campaign Galerkin screen of the Q weight-source operator."""
import argparse,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.fft import fft2,ifft2,fftfreq
from scipy.special import eval_hermite
HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'finite_rank'))
from full_remainder_screen import mesh

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--grid',type=int,default=512)
    ap.add_argument('--radius',type=float,default=24)
    ap.add_argument('--alpha',type=float,default=1)
    ap.add_argument('--degree',type=int,default=15)
    ap.add_argument('--weight-a',type=float,default=2)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    z=json.loads((HERE/'finite_rank/radial_mesh_cache.float.json').read_text())
    z['rows']=[{k:v for k,v in row.items() if k in ['rho,1,0','rho,0,1']}
               for row in z['rows']]
    N=args.grid;R=args.radius;dx=2*R/N
    assert z['rmax']>=math.sqrt(2)*R
    x=np.arange(N)*dx-R;xx,yy=np.meshgrid(x,x,indexing='xy')
    r2=xx*xx+yy*yy;r=np.sqrt(r2);W=np.sqrt(1+args.weight_a**2*r2)
    fields=mesh(z,xx,yy);bx=fields['rho',1,0];by=fields['rho',0,1]
    k=2*np.pi*fftfreq(N,d=dx);kx,ky=np.meshgrid(k,k,indexing='xy')
    k2=kx*kx+ky*ky;J=np.sqrt(1+k2);inv=np.zeros_like(k2)
    inv[k2>0]=1/np.sqrt(k2[k2>0])
    R1=1j*kx*inv;R2=1j*ky*inv
    U1=kx*ky*inv*inv;U2=-kx*kx*inv*inv
    ids=[(m,n) for total in range(args.degree+1) for m in range(total+1)
         for n in [total-m] if m%2==0 and n%2==1]
    phi=[];r1=[];r2v=[];ux=[];uy=[];ewx=[];ewy=[];pp=[]
    for m,n in ids:
        f=args.alpha/math.sqrt(math.pi*2**(m+n)*math.factorial(m)*
                math.factorial(n))*eval_hermite(m,args.alpha*xx)*(
                eval_hermite(n,args.alpha*yy))*np.exp(-args.alpha**2*r2/2)
        fh=fft2(f);ch=fft2(f/W)
        u1=ifft2(U1*fh).real;u2=ifft2(U2*fh).real
        phi.append(f.ravel());r1.append(ifft2(R1*fh).real.ravel())
        r2v.append(ifft2(R2*fh).real.ravel())
        ux.append(u1.ravel());uy.append(u2.ravel())
        ewx.append((W*ifft2(U1*ch).real-u1).ravel())
        ewy.append((W*ifft2(U2*ch).real-u2).ravel())
        pp.append(ifft2(fh/J).real.ravel())
    phi,r1,r2v,ux,uy,ewx,ewy,pp=map(np.asarray,
                                      [phi,r1,r2v,ux,uy,ewx,ewy,pp])
    metric=pp@pp.T*dx*dx
    vals,V=np.linalg.eigh(metric);Pinv=(V/np.sqrt(vals))@V.T
    rows=[]
    for cutoff in [None,1,3,10,20]:
        if cutoff is None:eta=np.ones_like(r)
        else:
            s=np.clip((r-cutoff)/cutoff,0,1)
            eta=(1+np.cos(np.pi*s))/2
        ax=(eta*bx).ravel();ay=(eta*by).ravel()
        ew=((ewx*ax+ewy*ay)@phi.T)*dx*dx;ew=(ew+ew.T)/2
        src=((ux*ax+uy*ay)@phi.T)*dx*dx;src=(src+src.T)/2
        src+=((r1*ay)@r1.T-(r1*ax/2)@r2v.T-
              (r2v*ax/2)@r1.T)*dx*dx
        joint=ew+src
        record={'near_cut_R':cutoff}
        for name,A in [('Ew',ew),('Cvs3',src),('joint',joint)]:
            eig=np.linalg.eigvalsh(A)
            record[name]={'lambda_min':float(eig[0]),
                          'lambda_max':float(eig[-1]),
                          'captured_HS_squared':float(np.sum(A*A)),
                          'relative_p2_eigenvalues_extreme':
                              np.linalg.eigvalsh(Pinv@A@Pinv)[[0,-1]].tolist()}
        rows.append(record);print(record,flush=True)
    out={'status':'FLOAT_GALERKIN_SCREEN_NO_CERTIFICATE',
         'grid':N,'radius':R,'alpha':args.alpha,'degree':args.degree,
         'weight_a':args.weight_a,
         'rank':len(ids),'basis_L2_gram_error':float(np.max(np.abs(
                 phi@phi.T*dx*dx-np.eye(len(ids))))),
         'rows':rows,'elapsed_seconds':time.monotonic()-start,
         'warnings':['finite periodic box','uncontrolled field interpolation',
                     'no continuum operator tail','floating arithmetic',
                     'not the independent residual-pairing experiment']}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()

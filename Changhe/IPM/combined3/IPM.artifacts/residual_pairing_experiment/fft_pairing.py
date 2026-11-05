"""Isolated FLOAT screen for Q=||W J^2.1 F|| and D=||J^2.1 W²J^2.1 F||.

Reuses only READONLY Arb-resolved residual modal coefficients. All FFTs use
physical angular frequency 2*pi*fftfreq and scipy's backward normalization.
"""
import argparse, hashlib, json, math, os, sys, time
from pathlib import Path
import numpy as np
from scipy.fft import fft2, ifft2, fftfreq
from scipy.interpolate import BPoly, make_interp_spline

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'coercivity_residual/residual_modal_v02.float.json'
R=4.549261e-7
M=.387

def source_grid(source,N,L,cutoff,spline_degree=7,interpolation='bspline'):
    data=json.loads(source.read_text());rows=data['rows']
    rr=np.array([q['r'] for q in rows]);F=np.array([q['F'] for q in rows])
    if interpolation=='hermite':
        Fr=np.array([q['Fr'] for q in rows]);Frr=np.array([q['Frr'] for q in rows])
        spline=BPoly.from_derivatives(np.log(rr),np.stack([F,rr[:,None]*Fr,rr[:,None]*Fr+rr[:,None]**2*Frr],axis=1))
    else:spline=make_interp_spline(np.log(rr),F,k=spline_degree)
    dx=2*L/N;x=np.arange(N)*dx-L
    out=np.zeros((N,N));r2=x[:,None]**2+x[None,:]**2
    # Ignore modes that are exactly absent at every cached radius.
    present=np.flatnonzero(np.max(abs(F),axis=0)>0)
    maxmode=int(present[-1]);Fmax=np.max(abs(F),axis=0)
    for i in range(0,N,8):
        xx=x[None,:];yy=x[i:i+8,None];radius=np.sqrt(xx*xx+yy*yy)
        theta=np.arctan2(yy,xx)
        coeff=spline(np.log(np.maximum(radius,rr[0])))
        sn=np.sin(theta);cs=np.cos(theta);sn2=np.sin(2*theta);cs2=np.cos(2*theta)
        values=np.zeros_like(radius)
        for j in range(maxmode+1):
            if Fmax[j]>0:values+=coeff[...,j]*sn
            sn,cs=sn*cs2+cs*sn2,cs*cs2-sn*sn2
        values[radius==0]=0
        if cutoff:values*=np.exp(-(radius/cutoff)**16)
        out[i:i+8]=values
    return out,r2,dx,{'mode_max':2*maxmode+1,'cache_rows':len(rows),'rmin':rr[0],'rmax':rr[-1]}

def run(args):
    start=time.monotonic();N=args.grid;L=args.radius
    f,r2,dx,meta=source_grid(args.source,N,L,args.cutoff,args.degree,args.interpolation)
    print('source_ready',N,L,time.monotonic()-start,flush=True)
    k=2*np.pi*fftfreq(N,d=dx);k2=k[:,None]**2+k[None,:]**2
    J=(1+k2)**1.05;fh=fft2(f,workers=1);h=ifft2(J*fh,workers=1).real
    w2=1+4*r2;g=w2*h
    if args.second_cutoff:g*=np.exp(-(np.sqrt(r2)/args.second_cutoff)**16)
    gh=fft2(g,workers=1)
    Q=math.sqrt(float(np.sum(w2*h*h))*dx*dx)
    D=math.sqrt(float(np.sum(abs(gh)**2*J**2))*dx*dx/N**2)
    fL2=math.sqrt(float(np.sum(f*f))*dx*dx)
    edge=np.zeros((N,N),bool);edge[:4,:]=edge[-4:,:]=True;edge[:,:4]=edge[:,-4:]=True
    nyq=np.max(abs(k));high=k2>(.7*nyq)**2
    out={'status':'FLOAT_NOT_CERTIFIED','source':str(args.source),'source_sha256':hashlib.sha256(args.source.read_bytes()).hexdigest(),
         'grid':N,'box_radius':L,'dx':dx,'frequency':'2*pi*fftfreq(N,d=dx)','cutoff':args.cutoff,'second_cutoff':args.second_cutoff,
         'interpolation':args.interpolation,'spline_degree':args.degree,'Q':Q,'D_cutoff':D,'fL2_cutoff':fL2,'Q_times_M':Q*M,'D_times_R':D*R,
         'improvement_ratio':D*R/(Q*M),'D_competitive_threshold_from_Q':Q*M/R,
         'Q_high_frequency_fraction':float(np.sum(abs(fh[high])**2*J[high]**2)/np.sum(abs(fh)**2*J**2)),
         'D_high_frequency_fraction':float(np.sum(abs(gh[high])**2*J[high]**2)/np.sum(abs(gh)**2*J**2)),
         'h_edge_max':float(abs(h[edge]).max()),'g_edge_max':float(abs(g[edge]).max()),'f_max':float(abs(f).max()),
         'Q_tail_r_gt_Lover2':math.sqrt(float(np.sum((w2*h*h)[r2>(L/2)**2]))*dx*dx),
         'elapsed_seconds':time.monotonic()-start,**meta}
    if args.splits:
        splitrows=[]
        for lam in map(float,args.splits.split(',')):
            lo=np.exp(-k2/(2*lam*lam));hi=-np.expm1(-k2/(2*lam*lam))
            hl=ifft2(J*lo*fh,workers=1).real
            Qlo=math.sqrt(float(np.sum(w2*hl*hl))*dx*dx)
            hh=ifft2(J*hi*fh,workers=1).real;gg=w2*hh
            if args.second_cutoff:gg*=np.exp(-(np.sqrt(r2)/args.second_cutoff)**16)
            ggh=fft2(gg,workers=1)
            Dh=math.sqrt(float(np.sum(abs(ggh)**2*J**2))*dx*dx/N**2)
            splitrows.append({'lambda':lam,'Q_low_cutoff':Qlo,'D_high_cutoff':Dh,
                              'bound_cutoff':M*Qlo+R*Dh,'ratio_to_QM_cutoff':(M*Qlo+R*Dh)/(M*Q),
                              'D_high_frequency_fraction':float(np.sum(abs(ggh[high])**2*J[high]**2)/np.sum(abs(ggh)**2*J**2))})
        out['gaussian_splits']=splitrows
        out['best_gaussian_split']=min(splitrows,key=lambda q:q['bound_cutoff'])
        out['elapsed_seconds']=time.monotonic()-start
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,default=SOURCE);p.add_argument('--grid',type=int,default=512);p.add_argument('--radius',type=float,default=8);p.add_argument('--cutoff',type=float,default=6);p.add_argument('--second-cutoff',type=float,default=0);p.add_argument('--degree',type=int,default=7);p.add_argument('--interpolation',choices=['bspline','hermite'],default='bspline');p.add_argument('--splits',default='');p.add_argument('--out',type=Path,required=True);run(p.parse_args())

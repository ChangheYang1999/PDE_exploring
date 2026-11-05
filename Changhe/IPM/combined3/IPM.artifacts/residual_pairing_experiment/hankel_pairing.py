"""Independent radial FFTLog check of Q and Gaussian frequency splitting.

Fourier-Bessel identities, with H_n=integral f_n(r) J_n(kr) r dr:
 Q²=pi integral [k²h²+4h_t²+4n²h²] dt, h=(1+k²)^1.05 H_n,
 D²=pi integral (1+k²)^2.1 [h-4(h_tt-n²h)/k²]² k² dt.
All results are FLOAT screens. k is physical angular frequency (Bessel kr).
"""
import argparse,json,math,time
from pathlib import Path
import numpy as np
from scipy.fft import fht,fhtoffset
from scipy.interpolate import make_interp_spline
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'coercivity_residual/residual_modal_v02.float.json'
R=4.549261e-7;M=.387

def smoothstep(t):
    t=np.asarray(t);a=np.zeros_like(t);b=np.zeros_like(t)
    mid=(t>0)&(t<1);a[mid]=np.exp(-1/t[mid]);b[mid]=np.exp(-1/(1-t[mid]))
    out=np.zeros_like(t);out[t>=1]=1;out[mid]=a[mid]/(a[mid]+b[mid]);return out

def derivative(y,dt,order=1):
    if order==1:
        out=(np.roll(y,2)-8*np.roll(y,1)+8*np.roll(y,-1)-np.roll(y,-2))/(12*dt)
    else:out=(-np.roll(y,2)+16*np.roll(y,1)-30*y+16*np.roll(y,-1)-np.roll(y,-2))/(12*dt*dt)
    return out

def run(args):
    tick=time.monotonic();data=json.loads(args.source.read_text());rows=data['rows']
    if args.extended:
        farrows=json.loads((HERE/'far_radial_cache.json').read_text())['rows']
        selected=farrows[::args.far_stride]
        if selected[-1]['r']!=farrows[-1]['r']:selected.append(farrows[-1])
        rows=rows+selected
    rr=np.array([q['r']for q in rows]);ff=np.array([q['F']for q in rows]);order=np.argsort(rr);rr=rr[order];ff=ff[order]
    spl=make_interp_spline(np.log(rr),ff,k=args.degree)
    r=np.geomspace(args.rmin,args.rmax,args.nodes);dt=math.log(r[1]/r[0]);fv=spl(np.log(np.clip(r,rr[0],rr[-1])))
    # Exact residual Taylor polynomial avoids a low-regularity join at the
    # first cache radius. A C-infinity transition preserves spline C6.
    origin=json.loads((HERE/'exact_origin_result.json').read_text())
    inner=r<4*rr[0];poly=np.zeros((int(np.sum(inner)),fv.shape[1]))
    for term in origin['terms']:poly[:,(term['n']-1)//2]+=term['float']*r[inner]**term['power']
    blend=smoothstep((r[inner]-2*rr[0])/(2*rr[0]))
    fv[inner]=poly*(1-blend[:,None])+fv[inner]*blend[:,None]
    if args.extended:
        asym=json.loads((HERE/'exact_far_result.json').read_text())
        mask=r>rr[-1]/10;tail=np.zeros((int(np.sum(mask)),fv.shape[1]))
        for p in asym['powers']:
            for c in p['coefficients']:tail[:,(c['n']-1)//2]+=c['float']*r[mask]**p['power']
        blend=smoothstep(np.log10(r[mask]/(rr[-1]/10)))
        fv[mask]=fv[mask]*(1-blend[:,None])+tail*blend[:,None]
    else:fv[r>rr[-1]]=0
    if args.cutoff:
        window=np.zeros_like(r);inside=r<2*args.cutoff
        window[inside]=np.exp(-(r[inside]/args.cutoff)**16)
        fv*=window[:,None]
    lambdas=list(map(float,args.splits.split(',')));acc=np.zeros((len(lambdas),3));Q2=0.;D2=0.;f2=math.pi*np.sum(fv*fv*r[:,None]**2)*dt
    contributions=[]
    for j in range(fv.shape[1]):
        n=2*j+1
        if np.max(abs(fv[:,j]))<1e-30:continue
        offset=fhtoffset(dt,mu=n,initial=0.,bias=args.bias);k=np.exp(offset)/r[::-1]
        A=fht(r*fv[:,j],dt,mu=n,offset=offset,bias=args.bias)
        h=(1+k*k)**1.05*A/k
        # Explicit k range excludes only unresolved roundoff / log-wrap tails;
        # varying it is a required numerical diagnostic.
        mask=(k>=args.kmin)&(k<=args.kmax)
        ht=derivative(h,dt);htt=derivative(h,dt,2)
        q2=math.pi*np.sum((k*k*h*h+4*ht*ht+4*n*n*h*h)[mask])*dt
        dterm=h-4*(htt-n*n*h)/(k*k)
        d2=math.pi*np.sum(((1+k*k)**2.1*dterm*dterm*k*k)[mask])*dt
        Q2+=q2;D2+=d2
        contributions.append({'n':n,'Q2':q2,'D2_with_kmin':d2})
        for l,lam in enumerate(lambdas):
            x=k*k/(2*lam*lam);lo=np.exp(-x);hi=-np.expm1(-x)
            # Derivatives computed for products analytically to avoid
            # subtracting two similar FFTLog samples in the infrared.
            lot=-2*x*lo;lott=4*x*(x-1)*lo
            hl=lo*h;hlt=lo*ht+lot*h
            ql2=math.pi*np.sum((k*k*hl*hl+4*hlt*hlt+4*n*n*hl*hl)[mask])*dt
            hh=hi*h;hhtt=hi*htt-2*lot*ht-lott*h
            dht=hh-4*(hhtt-n*n*hh)/(k*k)
            dh2=math.pi*np.sum(((1+k*k)**2.1*dht*dht*k*k)[mask])*dt
            acc[l,0]+=ql2;acc[l,1]+=dh2
    results=[]
    for (lam,(ql2,dh2,_))in zip(lambdas,acc):
        ql=math.sqrt(ql2);dh=math.sqrt(dh2);results.append({'lambda':lam,'Q_low':ql,'D_high':dh,'bound':ql*M+dh*R,'Q_low_times_M':ql*M,'D_high_times_R':dh*R})
    out={'status':'FLOAT_FFTLOG_NOT_CERTIFIED','D_with_kmin_warning':'Unmodified full-source D is infinite; this raw infrared-conditioned diagnostic is not a finite norm. Use only Gaussian high-pass D values.','origin_extension':'exact Taylor9 with C-infinity blend','far_extension':'exact asymptotic powers >= -4 with C-infinity blend over 1e9..1e10','source':str(args.source),'far_stride':args.far_stride,'nodes':args.nodes,'rmin':args.rmin,'rmax':args.rmax,'kmin':args.kmin,'kmax':args.kmax,'cutoff':args.cutoff,'extended':args.extended,'bias':args.bias,'spline_degree':args.degree,'Q':math.sqrt(Q2),'D_with_kmin':math.sqrt(D2),'fL2':math.sqrt(f2),'gaussian_splits':results,'top_Q_modes':sorted(contributions,key=lambda q:q['Q2'],reverse=True)[:12],'elapsed_seconds':time.monotonic()-tick}
    if results:out['best_gaussian_split']=min(results,key=lambda q:q['bound'])
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,default=SOURCE);p.add_argument('--far-stride',type=int,default=1);p.add_argument('--nodes',type=int,default=16384);p.add_argument('--rmin',type=float,default=1e-7);p.add_argument('--rmax',type=float,default=1e10);p.add_argument('--kmin',type=float,default=1e-8);p.add_argument('--kmax',type=float,default=1000.);p.add_argument('--bias',type=float,default=0.);p.add_argument('--degree',type=int,default=7);p.add_argument('--extended',action='store_true');p.add_argument('--cutoff',type=float,default=0.);p.add_argument('--splits',default='');p.add_argument('--out',type=Path,required=True);run(p.parse_args())

"""Compute export exterior-closure error by direct quadrature of the trial tail."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ[key]="1"
import resource
resource.setrlimit(resource.RLIMIT_AS,(1900*1024**2,1900*1024**2))
import sys,json
from pathlib import Path
import numpy as np
from numpy.polynomial.chebyshev import chebval,chebder
from scipy.fft import dst
sys.path.insert(0,"c7")
from trial import Trial
path="c6g_shape.npz"
export="c6gx_fields.npz"
t=Trial(path); k=t.k; L=t.L; R=1e4*L
nt=int(sys.argv[1]) if len(sys.argv)>1 else 1024
order=int(sys.argv[2]) if len(sys.argv)>2 else 24
th=np.linspace(0,np.pi/2,nt+1)
c,s=np.cos(th),np.sin(th); c[-1]=0; s[0]=0
m=np.arange(t.angular+1); jj=np.maximum(m-1,0); ell=2*np.arange(1,nt)
cs=np.cos(2*np.outer(th,m)); sn=np.sin(2*np.outer(th,m))
v=c**(t.p3-2)*s*s
vp=2*c**(t.p3-1)*s-(t.p3-2)*c**(t.p3-3)*s**3
fac=c*c*s; facp=c**3-2*c*s*s

def fields(r):
    u=r/L; uu=u*u; ss=uu/(1+uu); chi=uu/(uu+t.origin**2)
    q=-np.expm1(-(1-k)/2*np.log1p(uu)); qt=(1-k)*ss*(1-q)
    b=t.spline(q); bt=t.spline(q,nu=1)*qt
    bm=chi**jj*b; btm=chi**jj*(bt+2*jj*(1-chi)*b)
    H=(k-3)/2*np.log1p(uu)+cs@bm
    Ht=(k-3)*ss+cs@btm
    Ha=sn@(-2*m*bm)
    poly=chebval(2*q-1,t.singular); pd=chebval(2*q-1,chebder(t.singular))
    sg=ss**(t.p3/2)*poly
    sgt=t.p3*(1-ss)*sg+2*ss**(t.p3/2)*pd*qt
    H+=sg*v; Ht+=sgt*v; Ha+=sg*vp
    rr=r**3*np.exp(H)
    rho=rr*fac; rt=(3+Ht)*rho; ra=rr*(facp+fac*Ha)
    return rho,rt,ra,H,Ht,Ha

def project(a):
    return dst(a[1:-1],type=1)/nt

rho,rt,ra,*_=fields(R)
# Radial derivative of ra is obtained by angular differentiation of rt.
# A spectral derivative of rt is exact up to angular truncation.
odd=np.arange(1,2*nt,2)
weights=np.ones(nt+1)*2/nt; weights[[0,-1]]*=.5
odd_sin=np.sin(np.outer(th,odd)); odd_cos=np.cos(np.outer(th,odd))
rho_coeff=(rho*weights)@odd_sin
rt_coeff=(rt*weights)@odd_sin
second=(rt_coeff-k*rho_coeff)/(k-1)
tail_coeff=[rho_coeff-second,second]
alphas=[k,2*k-1]
tail_sources=[]
for alpha,coeff in zip(alphas,tail_coeff):
    tail_sources.append(((alpha-ell+1)*coeff[:-1]+(alpha+ell+1)*coeff[1:])/(2*R))

nodes,weights=np.polynomial.legendre.leggauss(order)
breaks=[0,.0005,.002,.008,.03,.1,.3,1,3,8,20,40]
dB=np.zeros(nt-1)
for lo,hi in zip(breaks[:-1],breaks[1:]):
    xs=(lo+hi)/2+(hi-lo)/2*nodes
    ws=(hi-lo)/2*weights
    for x,w in zip(xs,ws):
        r=R*np.exp(x)
        rh,rr,ra,*_=fields(r)
        actual=project((c*rr-s*ra)/r)
        approx=sum(f*np.exp((alpha-1)*x) for alpha,f in zip(alphas,tail_sources))
        dB+=w*np.exp((2-ell)*x)*(actual-approx)
print("tail integrated",nt,order,flush=True)

z=np.load(export)
rall=z["r"]; tq=z["theta"]
targets=[1000,2000,4701,7998,9503]
ri=np.array([np.argmin(abs(rall-u*L)) for u in targets])
ci=np.array([len(tq)-2,np.argmin(abs(tq-.818))])
# Read each large array individually and retain only the requested samples.
values={}
for name in ["rho","rho_x","rho_y","U1","U2","residual","denominator"]:
    arr=z[name]
    values[name]=arr[np.ix_(ri,ci)].copy()
    del arr
rows=[]
for ii,ir in enumerate(ri):
    r=rall[ir]; aR=r/R
    dmode=R/2*dB*aR**(ell-1)
    for jj,ic in enumerate(ci):
        theta=tq[ic]
        dur=-np.dot(dmode,np.cos(ell*theta))
        dut=np.dot(dmode,np.sin(ell*theta))
        dux=dur*np.cos(theta)-dut*np.sin(theta)
        duy=dur*np.sin(theta)+dut*np.cos(theta)
        rx=values["rho_x"][ii,jj]; ry=values["rho_y"][ii,jj]
        den=values["denominator"][ii,jj]
        old=values["residual"][ii,jj]
        adv=values["U1"][ii,jj]*rx+values["U2"][ii,jj]*ry
        dadv=dux*rx+duy*ry
        newden=den-abs(adv)+abs(adv+dadv)
        rows.append(dict(r_over_L=float(r/L),theta=float(theta),
            exported=float(old/den),tail_correction_over_den=float(dadv/den),
            corrected=float((old+dadv)/newden),
            delta_Ur=float(dur),delta_Utheta=float(dut)))
out=dict(nt=nt,order=order,c_l=float(z["c_l"]),c_l_stored=float(z["c_l_stored"]),
         rows=rows,max_dB=float(np.max(abs(dB))))
Path(__file__).with_name(f"tail_closure_{nt}_{order}.json").write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))

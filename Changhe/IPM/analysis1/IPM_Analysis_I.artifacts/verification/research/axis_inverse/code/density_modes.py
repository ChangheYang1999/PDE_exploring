"""Independent floating full-plane inverse from density-mode integrals.
No density differentiation in the inverse. No claimed error certificate.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,time,json,argparse,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.fft import dst
from scipy.special import roots_legendre
BASE=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from x3_independent import X3
class Inverse:
    def __init__(self,nq=12,na=1024,nm=256):
        self.x=X3();self.nm=nm;self.na=na;self.nq=nq
        self.knots=np.unique(self.x.t);self.node,self.weight=roots_legendre(nq)
        self.theta=(np.arange(na)+.5)*np.pi/(2*na)
        self.m=2*np.arange(1,nm+1)
        mids=(self.knots[:-1]+self.knots[1:])/2;halfs=np.diff(self.knots)/2
        self.q=(mids[:,None]+halfs[:,None]*self.node).ravel()
        self.w=(halfs[:,None]*self.weight).ravel()
        self.r,self.den,self.coeff=self.density_coeff(self.q)
        self.cs=float(np.sum(self.w*self.coeff[:,1]/(self.r*self.den)))
    def density_coeff(self,q):
        x=self.x;s=-np.expm1(x.b*np.log1p(-q));r=x.L*np.sqrt(s)*np.exp(-np.log1p(-q)/(1-x.k));den=(1-x.k)*s*(1-q)
        S=x.compact(q,self.theta)
        H=(3-x.k)*np.log1p(-q)[:,None]/(1-x.k)+S
        rh=r[:,None]**3*(np.cos(self.theta)**2*np.sin(self.theta))*np.exp(H)
        co=dst(rh,type=4,axis=1)/self.na
        return r,den,co[:,:self.nm+1]
    def moments(self,rstar):
        x=self.x;qstar=-np.expm1(-(1-x.k)*np.log1p((rstar/x.L)**2)/2)
        cell=np.searchsorted(self.knots,qstar,side='right')-1
        inds=np.arange(len(self.q));keep=(inds//self.nq!=cell)
        qq=[];ww=[]
        for lo,hi in [(self.knots[cell],qstar),(qstar,self.knots[cell+1])]:
            if hi>lo:qq.extend((lo+hi)/2+(hi-lo)*self.node/2);ww.extend((hi-lo)*self.weight/2)
        qq=np.asarray(qq);ww=np.asarray(ww);rr,dd,cc=self.density_coeff(qq)
        q=np.concatenate([self.q[keep],qq]);r=np.concatenate([self.r[keep],rr]);den=np.concatenate([self.den[keep],dd]);co=np.concatenate([self.coeff[keep],cc]);w=np.concatenate([self.w[keep],ww])
        inside=q<qstar;outside=~inside
        I=np.sum((w[inside]/den[inside])[:,None]*(r[inside,None]/rstar)**(self.m+1)*co[inside,:self.nm],axis=0)
        J=np.sum((w[outside]/den[outside])[:,None]*(rstar/r[outside,None])**(self.m-1)*co[outside,1:self.nm+1],axis=0)
        astar=self.density_coeff(np.array([qstar]))[2][0]
        return I,J,astar
    def axis(self,rstar):
        I,J,a=self.moments(rstar);m=self.m;cl=1/self.x.k
        w=cl*rstar+np.sum((m/2)*(I-J))
        wp=cl+np.sum(m/(2*rstar)*(a[:self.nm]+a[1:self.nm+1]-(m+1)*I-(m-1)*J))
        rho=self.x.polar(np.array([rstar]),np.array([0.]))
        g=float(rho["rho_y"][0,0]);q=-np.expm1(-(1-self.x.k)*np.log1p((rstar/self.x.L)**2)/2)
        Ht=(self.x.k-3)*(rstar/self.x.L)**2/(1+(rstar/self.x.L)**2)+self.x.compact(np.array([q]),np.array([0.]),True)[1][0,0]
        gp=g*(2+Ht)/rstar
        return {"w":float(w),"wprime":float(wp),"b":float(2*cl-wp),"g":g,"gprime":float(gp),"axis_residual":float(w*gp+(2*cl-wp-1)*g)}
    def velocity(self,rstar,angles):
        I,J,astar=self.moments(rstar)
        angles=np.asarray(angles)
        ur=((self.m/2)*(I-J))@np.cos(self.m[:,None]*angles)
        ut=((self.m/2)*(I+J)-(astar[:self.nm]+astar[1:self.nm+1])/2)@np.sin(self.m[:,None]*angles)
        u1=ur*np.cos(angles)-ut*np.sin(angles);u2=ur*np.sin(angles)+ut*np.cos(angles)
        return u1,u2

def main(args):
    start=time.monotonic();inv=Inverse(args.nq,args.na,args.nm)
    rows=[]
    for r in [.001,.1,1.,5.,8.5999,8.600064,8.6002,10.,100.]:
        angles=np.array([0.,.2,.7,1.2]);u1,u2=inv.velocity(r,angles);rho=inv.x.polar(np.array([r]),angles)
        xx=r*np.cos(angles);yy=r*np.sin(angles);cl=1/inv.x.k
        residual=(cl*xx+u1)*rho['rho_x'][0]+(cl*yy+u2)*rho['rho_y'][0]-rho['rho'][0]
        rows.append({'r':r,'theta':angles.tolist(),'u1':u1.tolist(),'u2':u2.tolist(),'residual':residual.tolist(),'axis_w':float(cl*r+u1[0]),'axis_g':float(rho['rho_y'][0,0])})
    from scipy.optimize import brentq
    root=brentq(lambda r:inv.axis(r)['w'],8.5999,8.6002,xtol=4e-15,rtol=1e-15)
    source=inv.axis(root);source['x_star']=root
    out={'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source':source,'utc':datetime.now(timezone.utc).isoformat(),'settings':vars(args),'method':'density sine modes via DST4 and per-spline-span Gaussian compact integrals','strain':inv.cs,'rows':rows,'seconds':time.monotonic()-start,'status':'FLOATING_POINT_EVIDENCE_ONLY'}
    (BASE/'research/axis_inverse/evidence'/f'density_modes_{args.nq}_{args.na}_{args.nm}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out),flush=True)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--nq',type=int,default=12);ap.add_argument('--na',type=int,default=1024);ap.add_argument('--nm',type=int,default=256);main(ap.parse_args())

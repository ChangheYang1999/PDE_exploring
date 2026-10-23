"""Independent scalar reconstruction, Cartesian FD8, and full-plane inverse.

No generator derivative, precomputed velocity matrix, or numerics-lane code is
used. The density uses Cartesian complex powers and a separate Clenshaw loop.
"""
import argparse,json,time,hashlib
from pathlib import Path
from datetime import datetime,timezone
from dataclasses import asdict
import numpy as np
from scipy.integrate import quad
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient

class ReconstructedSmooth:
    def __init__(self,path):
        data=np.load(path,allow_pickle=False)
        self.N=int(data['radial']);self.M=int(data['angular'])
        self.p=float(data['exponent']);self.L=float(data['length'])
        self.a=(1-self.p)/2;self.cl=float(data['cl'])
        self.mu=float(data['mu']) if 'mu' in data.files else 0.
        self.coeff=np.array(data['coefficients']).reshape(self.M,self.N+1)
    def polynomial(self,k,t):
        if k>=self.M:return np.zeros_like(t,dtype=float)
        b1=np.zeros_like(t,dtype=float);b2=np.zeros_like(t,dtype=float)
        for ck in self.coeff[k,:0:-1]:
            b0=ck+2*t*b1-b2;b2,b1=b1,b0
        return self.coeff[k,0]+t*b1-b2
    def rho(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float))
        # Normalize before squaring for stable large-radius evaluation.
        scale=np.maximum(self.L,np.hypot(x,y))
        xx=x/scale;yy=y/scale;ll=self.L/scale
        den=ll*ll+xx*xx+yy*yy
        logden=2*np.log(scale/self.L)+np.log(den)
        w=np.exp(-self.a*logden);t=1-2*w
        z=(xx+1j*yy)**2/den;power=np.ones_like(z)
        total=np.zeros_like(x)
        for k in range(self.M):
            total+=power.real*self.polynomial(k,t);power*=z
        return y*w*total
    def polar_density(self,r,theta):
        r=np.asarray(r);theta=np.asarray(theta)
        return self.rho(r[:,None]*np.cos(theta),r[:,None]*np.sin(theta))
    def center_and_tail(self):
        signs=(-1.)**np.arange(self.N+1)
        D=self.coeff@signs
        E=self.coeff@np.where(np.arange(self.N+1)==0,0.,-signs*np.arange(self.N+1)**2)
        a0=float(D[0]);d1=float(D[1]) if self.M>1 else 0.
        common=self.a*(-D[0]+2*E[0])/self.L**2
        def integrands(s):
            ld=float(np.logaddexp(0.,2*s));w=np.exp(-self.a*ld)
            sig=-np.expm1(-ld);t=1-2*w
            return (.5*w*sig*(self.polynomial(1,t)-sig*self.polynomial(2,t)),
                    2/self.L**2*w*sig*np.exp(-ld)*(self.polynomial(2,t)-sig*self.polynomial(3,t)))
        center=[]
        for tol in (1e-8,1e-10,1e-12):
            m,err=quad(lambda s:integrands(s)[0],-np.inf,np.inf,epsabs=tol,epsrel=tol,limit=250)
            hh,herr=quad(lambda s:integrands(s)[1],-np.inf,np.inf,epsabs=tol,epsrel=tol,limit=250)
            center.append({'requested_tolerance':tol,'c':-a0/4+m,'c_quad_error_estimate':err,'H':-d1/(4*self.L**2)+hh,'H_quad_error_estimate':herr})
        c=center[-1]['c'];h=center[-1]['H'];b=common+d1/self.L**2;e=common-d1/self.L**2
        delta=self.cl+c-1;A=2*self.cl-1
        return {'a0':a0,'b':b,'e':e,'adaptive_logradius_center':center,
          'Delta':delta,'source_eigenvalues':[self.cl-c,self.cl+c],
          'unforced_center_defect':delta,'forced_center_defect':a0*delta-self.mu,
          'forced_cubic_T1':(a0-2*A+delta)*b-3*(2+3*delta)*e-8*self.mu/self.L**2,
          'forced_cubic_T2':(a0-4*A+2*delta)*b-3*a0*h-4*self.mu/self.L**2,
          'axis_K':float(self.L**(1-self.p)*np.sum((-1.)**np.arange(self.M)*np.sum(self.coeff,axis=1))),
          'far_mean_dimensionless_B0':float(np.sum(self.coeff[0]))}

def summary(points):
    regions=[('center',0,.01),('core',.01,1),('middle',1,100),('far',100,float('inf'))]
    out={}
    for name,lo,hi in [('all',0,float('inf'))]+regions:
        selected=[p for p in points if lo<=p['radius']<hi]
        good=[p for p in selected if p['y']!=0.]
        row={'point_count':len(selected),'nonaxis_count':len(good),'exact_xaxis_excluded_from_ratios':len(selected)-len(good)}
        for field in ('abs_R','abs_Rforced','R_Nf','R_Nv','Rforced_Nf','Rforced_Nv'):
            candidates=selected if field.startswith('abs_') else good
            candidates=[p for p in candidates if p['residuals'][-1][field] is not None]
            if candidates:
                winner=max(candidates,key=lambda p:p['residuals'][-1][field]);row[field]={'maximum':winner['residuals'][-1][field],'x':winner['x'],'y':winner['y']}
        for field in ('Nf','Nv'):
            row['minimum_'+field+'_nonaxis']=min((p['residuals'][-1][field] for p in good),default=None)
        out[name]=row
    return out

def main(reconstructor=ReconstructedSmooth,output_root='evidence/smooth_evaluations'):
    ap=argparse.ArgumentParser();ap.add_argument('state');ap.add_argument('--level',type=int,default=0);ap.add_argument('--tag');ap.add_argument('--points-file');args=ap.parse_args()
    state=Path(args.state);obj=reconstructor(state)
    configs=[(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)]
    nr,nt,ne,factor=configs[args.level]
    q=Quadrature(nr,nt,ne,factor,obj.L,obj.p,16*obj.L,1/(1-obj.p))
    inv=DirectInverse(obj.rho,q)
    radii=np.array([1e-7,1e-4,.013,.19,.91,2.7,11.,100.,1e4,2e5])*obj.L
    angles=[.003,.219,.771,1.499]
    points=[(float(r*np.cos(t)),float(r*np.sin(t))) for r in radii for t in angles]
    points+=[(0.,float(r)) for r in radii]
    points+=[(float(r),0.) for r in radii[::2]]
    points+=[(0.,0.)]
    if args.points_file:points=[tuple(p) for p in json.loads(Path(args.points_file).read_text())]
    tag=args.tag or state.parent.name;dest=Path(output_root)/tag;dest.mkdir(parents=True,exist_ok=True)
    output=dest/('q'+str(args.level)+'.json');start=time.time()
    result={'started_utc':datetime.now(timezone.utc).isoformat(),'source':str(state),'sha256':hashlib.sha256(state.read_bytes()).hexdigest(),'quadrature':asdict(q),'cl':obj.cl,'mu':obj.mu,'branch':getattr(obj,'branch','PRIMARY y-leading'),'basis':{'N':obj.N,'M':obj.M,'p':obj.p,'L':obj.L},'center_and_tail':obj.center_and_tail(),'scope':'Sampled data, not rigorous bounds. Full plane at each split; exterior integral to infinity. FD8 at three steps, no generator derivatives or matrix reused. R is unforced, Rforced subtracts the stated source. Exact x-axis ratios excluded geometrically; raw values retained. Near-axis points are retained without denominator cutoff.','points':[]}
    for i,(x,y) in enumerate(points):
        tick=time.time();rho=float(obj.rho(x,y));u,parts=inv.velocity(x,y,parts=True)
        source=obj.mu*y/(1+(np.hypot(x,y)/obj.L)**2)**2
        residuals=[]
        for step in (.003,.0015,.00075):
            gx,gy=cartesian_gradient(obj.rho,x,y,step,obj.L if x==y==0. else 0.)
            gx=float(gx);gy=float(gy);tx=(obj.cl*x+u[0])*gx;ty=(obj.cl*y+u[1])*gy
            R=tx+ty-rho;Rf=R-source;nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(x*gx+y*gy)+abs(u[0]*gx+u[1]*gy)
            row={'relative_step':step,'rho_x':gx,'rho_y':gy,'R':float(R),'Rforced':float(Rf),'abs_R':float(abs(R)),'abs_Rforced':float(abs(Rf)),'Nf':float(nf),'Nv':float(nv)}
            for nm,val in [('R',R),('Rforced',Rf)]:
                for dm,den in [('Nf',nf),('Nv',nv)]:row[nm+'_'+dm]=float(abs(val)/den) if den>0 else None
            residuals.append(row)
        parity={'even_x_error':float(obj.rho(-x,y)-rho),'odd_y_error':float(obj.rho(x,-y)+rho)}
        result['points'].append({'x':x,'y':y,'radius':float(np.hypot(x,y)),'rho':rho,'U':u.tolist(),'inverse_parts':parts,'source':float(source),'parity':parity,'residuals':residuals,'seconds':time.time()-tick})
        result['last_update_utc']=datetime.now(timezone.utc).isoformat();result['elapsed_seconds']=time.time()-start
        output.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({'point':i,'total':len(points),'utc':result['last_update_utc'],'x':x,'y':y,'Rforced_Nf':residuals[-1]['Rforced_Nf'],'seconds':time.time()-tick}),flush=True)
    result['summary']=summary(result['points']);result['finished_utc']=datetime.now(timezone.utc).isoformat()
    output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result['summary'],indent=2),flush=True)
if __name__=='__main__':main()

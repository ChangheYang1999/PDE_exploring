#!/usr/bin/env python3
"""Independent saved-rational-field derivatives and point transport.

Only metadata and optional comparison arrays are read from the lead export.
No foreign Python module is imported or executed.
"""
from pathlib import Path
from datetime import datetime,timezone
from math import comb, factorial
import argparse,json,time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import poch
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parent

class RationalT1:
    def __init__(self,metadata):
        self.meta=metadata;self.c_l=float(metadata['c']);self.p=1/(2*self.c_l)
        self.terms=[]
        for C,j,k,d,a,b in metadata['terms']:
            n=round(d-self.p-j-k)
            if min(j,k,n)<0 or j!=int(j) or k!=int(k) or min(a,b)<=0 or abs(d-self.p-j-k-n)>1e-12:
                raise ValueError('unsupported rational exponent')
            self.terms.append((float(C),int(j),int(k),self.p+j+k+n,float(a),float(b),int(n)))
        self.ps=float(self.F(0.,0.,1,0));self.pz=float(self.F(0.,0.,0,1))
        if abs(float(self.F(0.,0.))-.5)>1e-12:raise ValueError('source strain normalization')
    def F(self,s,t,ds=0,dt=0):
        s,t=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(t,dtype=float));out=np.zeros_like(s)
        for C,j,k,d,a,b,n in self.terms:
            u=1+a*s+b*t
            for js in range(min(ds,j)+1):
                for kt in range(min(dt,k)+1):
                    h=ds+dt-js-kt
                    coeff=C*comb(ds,js)*factorial(j)/factorial(j-js)*comb(dt,kt)*factorial(k)/factorial(k-kt)
                    coeff*=(-1)**h*poch(d,h)*a**(ds-js)*b**(dt-kt)
                    out+=coeff*s**(j-js)*t**(k-kt)*u**(-d-h)
        return out
    def jets(self,r,z):
        r,z=np.broadcast_arrays(np.asarray(r,dtype=float),np.asarray(z,dtype=float));s=r*r;t=z*z
        F=self.F(s,t);Fs=self.F(s,t,1,0);Ft=self.F(s,t,0,1)
        Fss=self.F(s,t,2,0);Fst=self.F(s,t,1,1);Ftt=self.F(s,t,0,2)
        pz=F+2*t*Ft;psz=Fs+2*t*Fst;pzz=2*z*(3*Ft+2*t*Ftt)
        ar=self.c_l-pz;az=self.c_l+2*F+2*s*Fs
        return dict(phi=z*F,phi_z=pz,eta_phi=-z*(8*Fs+4*s*Fss+6*Ft+4*t*Ftt),
            log_r_speed=ar,log_z_speed=az,A=2*pz-1,A_r=4*r*psz,A_z=2*pzz,
            Drr=ar-2*s*psz,Drz=-r*pzz,Dzr=8*r*z*Fs+4*r*s*z*Fss,Dzz=az+4*t*Ft+4*s*t*Fst)
    def axis_coefficient(self):
        value=0.
        for C,j,k,d,a,b,n in self.terms:
            if n:continue
            if j==0:value+=C*b**(-d)*(8*d*a/b-2*self.p*(2*self.p-1))
            elif j==1:value-=8*C*b**(-d)
        return value

def transport(field,r,z,source_radius=1e-5,rtol=3e-9,atol=3e-11):
    r,z=np.broadcast_arrays(np.asarray(r,dtype=float),np.asarray(z,dtype=float));shape=r.shape
    if np.any(r<=0) or np.any(z<=0):raise ValueError('positive coordinates required')
    r=r.ravel();z=z.ravel();count=r.size;target=np.stack([np.log(r),np.log(z)])
    def backward(t,y):
        rr,zz=np.exp(y.reshape(2,count));d=field.jets(rr,zz)
        return np.stack([d['log_r_speed'],d['log_z_speed']]).ravel()
    def event(t,y):
        logs=y.reshape(2,count)
        return float(np.max(.5*np.logaddexp(2*logs[0],2*logs[1]))-np.log(source_radius))
    event.terminal=True;event.direction=-1
    back=solve_ivp(backward,(0,-220),target.ravel(),method='DOP853',events=event,rtol=rtol,atol=atol)
    if not back.success or not len(back.t_events[0]):raise RuntimeError('source not reached')
    logs=back.y[:,-1].reshape(2,count);rr,zz=np.exp(logs);delta=1+field.c_l
    A=field.ps/(field.c_l-.5);B=3*field.pz/delta;E=6*field.pz/delta**2
    h=1+A*rr*rr+B*zz*zz
    if np.any(h<=0):raise ValueError('invalid Taylor source value')
    y0=np.concatenate([logs,np.stack([np.log(h),2*A*rr/h,2*B*zz/h,E*zz])])
    def forward(t,y):
        y=y.reshape(6,count);rr,zz=np.exp(y[:2]);d=field.jets(rr,zz);H,gr,gz,e=y[2:]
        return np.stack([d['log_r_speed'],d['log_z_speed'],d['A'],
            d['A_r']-d['Drr']*gr-d['Dzr']*gz,d['A_z']-d['Drz']*gr-d['Dzz']*gz,
            2*np.exp(2*H)*gz-delta*e]).ravel()
    sol=solve_ivp(forward,(float(back.t[-1]),0),y0.ravel(),method='DOP853',rtol=rtol,atol=atol)
    if not sol.success:raise RuntimeError('forward transport failed')
    y=sol.y[:,-1].reshape(6,count)
    return dict(h=np.exp(y[2]).reshape(shape),e=y[5].reshape(shape),
        endpoint_log_error=float(np.max(abs(y[:2]-target))),backward_duration=-float(back.t[-1]),
        backward_nfev=int(back.nfev),forward_nfev=int(sol.nfev),source_radius=source_radius,rtol=rtol,atol=atol)

def derivative_test():
    import sympy as S
    s,t=S.symbols('s t');terms=[[.5,0,0,5/6,1.,2.],[.7,1,0,11/6,1.,2.],[-.3,0,2,17/6,1.,2.]]
    f=RationalT1(dict(c=.6,terms=terms));exact=sum(S.Rational(str(C))*s**j*t**k*(1+S.Rational(str(a))*s+S.Rational(str(b))*t)**(-S.Rational(5,6)-j-k) for C,j,k,d,a,b in terms)
    ss=np.array([0,.01,.1,.3,1.,4.]);tt=np.array([0,.2,.05,.4,2.,.1]);rows=[]
    for ds,dt in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
        reference=S.lambdify((s,t),S.diff(exact,s,ds,t,dt),'numpy')(ss,tt)
        error=float(np.max(abs(f.F(ss,tt,ds,dt)-reference)))
        rows.append(dict(ds=ds,dt=dt,max_abs_error=error,passed=error<3e-13))
    if not all(x['passed'] for x in rows):raise AssertionError(rows)
    return rows

def main():
    ap=argparse.ArgumentParser();ap.add_argument('export',type=Path);ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--transport',action='store_true');ap.add_argument('--levels',nargs='+',type=int,default=[31,61,91])
    a=ap.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside lane')
    if out.exists():raise FileExistsError('preserve previous audit')
    out.parent.mkdir(parents=True,exist_ok=True);start=time.perf_counter();cpu=time.process_time()
    meta_path=a.export/'metadata.json';grid_path=a.export/'grid.npz';meta=json.loads(meta_path.read_text());field=RationalT1(meta)
    hashes={str(p.resolve()):sha256(p) for p in [Path(__file__),meta_path,grid_path]}
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),source_hashes=hashes,
        derivative_tests=derivative_test(),c_l=field.c_l,p_s=field.ps,p_z=field.pz,T_phi=field.axis_coefficient(),
        scope='Prescribed potential and independent source-normalized transport, not Euler closure or a rigorous numerical enclosure.')
    def checkpoint(phase):
        if any(sha256(p)!=value for p,value in hashes.items()):raise RuntimeError('source changed')
        result.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        atomic_json(out,result);print(json.dumps({k:result[k] for k in ['phase','updated_utc','elapsed_seconds','T_phi']}),flush=True)
    with np.load(grid_path,allow_pickle=False) as g:
        # This checks only the documented potential values, before transporting.
        R=np.exp(g['x'])[:,None];mu=g['m'][None,:];ss=R*R*(1-mu*mu);z=R*mu
        result['saved_phi_max_abs_error']=float(np.max(abs(z*field.F(ss,z*z)-g['phi'])))
    R=np.array([1e2,1e3,1e4,1e5]);values=field.jets(np.zeros_like(R),R)['eta_phi']*R**(1+2*field.p)
    result['axis_limit_samples']=[dict(z=float(z),scaled_eta=float(v)) for z,v in zip(R,values)]
    checkpoint('quick_checks_complete')
    if a.transport:
        rows=[]
        for n in a.levels:
            angles={31:21,61:41,91:81}.get(n,n)
            x=np.linspace(-4,3,n);mu=np.linspace(.02,.98,angles);R=np.exp(x)[:,None]
            r=R*np.sqrt(1-mu[None,:]**2);z=R*mu[None,:]
            got=transport(field,r,z);eta_phi=field.jets(r,z)['eta_phi'];eta=float(meta['K2'])*got['e']
            defect=float(np.sqrt(np.mean((eta_phi-eta)**2)/(np.mean(eta_phi**2)+np.mean(eta**2))))
            diag={key:value for key,value in got.items() if key not in ['h','e']}
            row=dict(radial_count=n,angular_count=angles,relative_vorticity_mismatch=defect,transport=diag)
            arrays=out.with_name(out.stem+f'_n{n}.npz')
            np.savez_compressed(arrays,x=x,mu=mu,h=got['h'],e=got['e'],eta_phi=eta_phi)
            row.update(arrays_file=str(arrays),arrays_sha256=sha256(arrays));rows.append(row);result['transport_levels']=rows
            checkpoint('transport_'+str(n))
    checkpoint('complete')
if __name__=='__main__':main()

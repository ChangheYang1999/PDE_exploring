"""Independent positive-source moment exploration, packet86.
This uses the analytic Gaussian whole-plane inverse, not numerics-lane code.
Conditional kinematic diagnostics only; no global flow or profile claim.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, math, os, time
import numpy as np
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss
from gaussian_characteristics import GaussianFlow


def theta_from_backward(g, point, rin=3e-4, rtol=2e-9, max_time=250.):
    x,y=map(float,point)
    if math.hypot(x,y)<=rin:
        return {'Theta_unit':x*x*(1+g.f01*y),'status':'LOCAL_JET','time':0.,'nfev':0}
    def fun(t,z):
        xx,yy,integ=z;Y=yy-g.y0;B,bp,_=g.B(xx*xx+Y*Y)
        W1=xx*(g.beta-2*g.fac*Y*bp)
        W2=g.beta*yy+g.fac*(B+2*xx*xx*bp)-g.u0
        Q=-(g.beta+2)+4*g.fac*Y*bp
        return [-W1,-W2,Q]
    def event(t,z):return math.hypot(z[0],z[1])-rin
    event.terminal=True;event.direction=-1
    sol=solve_ivp(fun,(0.,max_time),[x,y,0.],method='DOP853',rtol=rtol,
                  atol=np.array([rin*rtol*.01,rin*rtol*.01,rtol*.01]),events=event)
    status='COMPLETE' if sol.success and len(sol.t_events[0]) else 'UNFINISHED'
    row={'status':status,'time':float(sol.t[-1]),'nfev':sol.nfev,'last_point':sol.y[:2,-1].tolist()}
    if status=='COMPLETE':
        local=1+g.f01*sol.y[1,-1]
        row['Theta_unit']=float(x*x*local*math.exp(sol.y[2,-1]))
    return row


def geometry(g,x,y):
    x,y=np.broadcast_arrays(x,y);Y=y-g.y0;S=x*x+Y*Y;z=g.a*S
    B=np.empty_like(S);bp=np.empty_like(S);m=z<.03
    zz=z[m];v=np.zeros_like(zz);d=np.zeros_like(zz)
    for k in range(14,-1,-1):v=v*zz+(-1.)**k/math.factorial(k+1)
    for k in range(14,0,-1):d=d*zz+k*(-1.)**k/math.factorial(k+1)
    B[m]=g.a*v;bp[m]=g.a**2*d
    ss=S[~m];zz=z[~m];e=np.exp(-zz)
    B[~m]=-np.expm1(-zz)/ss;bp[~m]=((zz+1)*e-1)/ss**2
    v1=-2*g.fac*x*Y*bp;v2=g.fac*(B+2*x*x*bp)-g.u0
    om=g.A*x*np.exp(-z)
    return v1,v2,om


def source_moments(g,nr,na,L=2.):
    z,w=leggauss(nr);t=(z+1)/2;r=L*t/(1-t);wr=w/2*L/(1-t)**2
    z,w=leggauss(na);ph=np.pi*z/2;wp=np.pi*w/2
    x=r[:,None]*np.cos(ph);y=r[:,None]*np.sin(ph);v1,v2,om=geometry(g,x,y)
    q=x*x+y*y;K=x*y/q**2;kx=y*(q-4*x*x)/q**3;ky=x*(q-4*y*y)/q**3
    weights=2*wr[:,None]*wp[None,:]*r[:,None]
    return {'nr':nr,'na':na,'L':L,'N':float(np.sum(weights*om*(v1*kx+v2*ky))),
            'c_integral':float(np.sum(weights*K*om)/np.pi)}


def run(root, configs):
    root.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    out={'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat(),'pid':os.getpid(),
         'scope':'Positive prescribed Gaussian source, conditional exact-temperature strain diagnostic. Not a B2 candidate.',
         'source_hashes':{p:hashlib.sha256(Path('code_independent',p).read_bytes()).hexdigest() for p in ['positive_gaussian_moment.py','gaussian_characteristics.py']},'runs':[]}
    (root/'status.json').write_text(json.dumps(out,indent=2)+'\n')
    for case in configs:
        beta=case.get('beta',3.);b=case['b'];g=GaussianFlow(c=1+beta/2,y0=b)
        a0=beta*g.A*math.exp(-g.a*b*b)/4
        nr=case.get('nr',20);na=case.get('na',24);L=case.get('L',1.5);power=case.get('power',beta);rin=case.get('rin',3e-4)
        row={'config':case,'a0':a0,'A':g.A,'u0':g.u0,'source_moments':[source_moments(g,n,2*n) for n in (64,128)]}
        points=np.array([[.07,.03],[.35,-.7],[.7,1.1],[1.8,2.2],[4.,-2.]])
        vec=geometry(g,*points.T);ref=g.velocity(points)
        row['velocity_vectorized_difference']=float(np.max(abs(np.column_stack(vec[:2])-ref)))
        # A separately propagated gradient/temperature calculation validates the new single-pass integral.
        row['temperature_method_comparison']=[]
        for q in points[:3]:
            new=theta_from_backward(g,q,rin=rin);old=g.evaluate(q,r_in=rin)
            row['temperature_method_comparison'].append({'point':q.tolist(),'new':new,'old_status':old['status'],
                 'difference':new.get('Theta_unit',float('nan'))-old.get('Theta',float('nan'))})
        radius=np.geomspace(1e-6,1e4,181);phi=np.linspace(-np.pi/2,np.pi/2,257)
        x=radius[:,None]*np.cos(phi);y=radius[:,None]*np.sin(phi);v1,v2,_=geometry(g,x,y)
        rad=beta+(x*v1+y*v2)/(x*x+y*y);j=np.unravel_index(np.argmin(rad),rad.shape)
        row['sampled_minimum_radial_W_over_r2']={'value':float(rad[j]),'point':[float(x[j]),float(y[j])]}
        z,w=leggauss(nr);t=(z+1)/2;rat=t/(1-t);r=L*rat**power;wr=w/2*L*power*rat**(power-1)/(1-t)**2
        z,w=leggauss(na);phi=np.pi*z/2;wa=np.pi*w/2
        path=root/f"points_b{b:g}_r{nr}_a{na}_p{power:g}_rin{rin:g}_L{L:g}.jsonl";values=[];bad=[];ct=time.monotonic()
        with path.open('w') as log:
            for ir,(rr,rw) in enumerate(zip(r,wr)):
                for ia,(ph,aw) in enumerate(zip(phi,wa)):
                    q=[float(rr*math.cos(ph)),float(rr*math.sin(ph))];res=theta_from_backward(g,q,rin=rin,rtol=case.get('rtol',2e-9))
                    term=2*rw*aw*math.sin(ph)*(1-4*math.cos(ph)**2)/rr**2*a0*res.get('Theta_unit',float('nan'))
                    item={'ir':ir,'ia':ia,'point':q,'term_I':float(term),**res};log.write(json.dumps(item)+'\n');values.append(float(term))
                    if res['status'] not in ('COMPLETE','LOCAL_JET'):bad.append(item)
                log.flush()
                if ir%4==0:
                    print('progress',b,nr,na,ir+1,'/',nr,'I',math.fsum(values),'failed',len(bad),flush=True)
                    current={'config':case,'completed':len(values),'total':nr*na,'failed':len(bad),'elapsed':time.monotonic()-ct}
                    (root/'status.json').write_text(json.dumps({**out,'current':current},indent=2)+'\n')
        I=math.fsum(values);N=row['source_moments'][-1]['N']
        row.update(I=I,D=N-I-np.pi*g.c,failed_points=len(bad),point_file=str(path),elapsed_seconds=time.monotonic()-ct,
                   radius_min=float(min(r)),radius_max=float(max(r)))
        out['runs'].append(row);(root/'status.json').write_text(json.dumps(out,indent=2)+'\n')
        print('RUN_COMPLETE',b,'N',N,'I',I,'D',row['D'],'bad',len(bad),'seconds',row['elapsed_seconds'],flush=True)
    out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
    (root/'status.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('output');ap.add_argument('configs');args=ap.parse_args()
    run(Path(args.output),json.loads(Path(args.configs).read_text()))

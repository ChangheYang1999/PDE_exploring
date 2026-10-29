#!/usr/bin/env python3
"""Fresh Sobol samples and bounded searches for missed reduced-residual peaks."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from scipy.optimize import minimize
from scipy.stats import qmc
from piecewise_loading import load_piecewise
from independent_artifacts import atomic_json,sha256,verify_source_identity
ROOT=Path(__file__).resolve().parent


def trace_residual(field,r,z,element):
    d=field.jets(r*r,z,3,element=element);p,q=d['phi'],d['q'];s=r*r
    eta=-8*p[1,0]-4*s*p[2,0]-p[0,2]
    es=-12*p[2,0]-4*s*p[3,0]-p[1,2];ez=-8*p[1,1]-4*s*p[2,1]-p[0,3]
    Wr=r*(field.c_l-p[0,1]);Wz=field.c_l*z+2*p[0,0]+2*s*p[1,0]
    return {'q':(1-2*p[0,1])*q[0,0]+2*r*Wr*q[1,0]+Wz*q[0,1],
            'eta':(1+field.c_l)*eta+2*r*Wr*es+Wz*ez-2*q[0,0]*q[0,1]}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--registered',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True);ap.add_argument('--sample-power',type=int,default=11)
    ap.add_argument('--starts',type=int,default=2);a=ap.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent) or out.exists():raise ValueError('fresh output inside lane required')
    start=time.perf_counter();cpu=time.process_time();f,gauge=load_piecewise(a.candidate).reporting_gauge()
    registered=json.loads(a.registered.read_text());seed=731829
    paths=[Path(__file__),ROOT/'src/piecewise_adapter.py',ROOT/'src/piecewise_jacobi.py',ROOT/'src/piecewise_loading.py',ROOT/'src/independent_fields.py']
    hashes={str(p.relative_to(ROOT)):sha256(p) for p in paths}
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),candidate_sha256=sha256(a.candidate),registered_sha256=sha256(a.registered),
                source_sha256=hashes,gauge=gauge,seed=seed,rows=[],interface_traces=[],accepted_as_A=False,
                scope='Finite peak search, never a global upper bound. Denominators are frozen from the previous registered Gauss sets. No pressure is computed.')
    def save(phase):
        verify_source_identity(ROOT,hashes)
        if sha256(a.candidate)!=result['candidate_sha256'] or sha256(a.registered)!=result['registered_sha256']:raise RuntimeError('input changed')
        result.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        atomic_json(out,result);print(phase,result['elapsed_seconds'],flush=True)
    selected=[row for row in registered['rows'] if row['set']=='shell_gauss']
    if len(selected)!=19:raise ValueError('complete registered shells and origin required')
    for j,row in enumerate(selected):
        lo,hi=row['lower'],row['upper'];sample=qmc.Sobol(2,scramble=True,seed=seed+j).random_base2(a.sample_power)
        R=(lo**3+(hi**3-lo**3)*sample[:,0])**(1/3);mu=2*sample[:,1]-1
        r=R*np.sqrt(1-mu*mu);z=R*mu;red=f.reduced(r,z);entry={'shell_index':row['shell_index'],'samples':len(R),'equations':{}}
        for key in ['q','eta']:
            denominator=row['metrics']['equations'][key]['denominator'];values=red[key]
            eq={'registered_denominator':denominator,'fresh_rms':float(np.sqrt(np.mean(values**2))),
                'fresh_maximum':float(np.max(abs(values))),'registered_maximum':row['metrics']['equations'][key]['maximum'],'peaks':[]}
            if denominator<=0:
                eq['undefined_denominator']=True;entry['equations'][key]=eq;continue
            eq['fresh_m']=eq['fresh_maximum']/denominator
            # Optimize only five selected shells and the origin; all sets get fresh holdouts.
            if row['shell_index'] in ['origin',-2,0,2,5,11]:
                for at in np.argsort(-abs(values))[:a.starts]:
                    element=int(np.searchsorted(f.interfaces,R[at],side='left'))
                    left=max(lo,0. if element==0 else f.interfaces[element-1]);right=min(hi,np.inf if element==2 else f.interfaces[element])
                    def objective(x):
                        rr=left+(right-left)*x[0];m=x[1]
                        got=trace_residual(f,rr*np.sqrt(max(0.,1-m*m)),rr*m,element)[key]
                        return -(float(got)/denominator)**2
                    opt=minimize(objective,[(R[at]-left)/(right-left),mu[at]],method='L-BFGS-B',bounds=[(0.,1.),(-1.,1.)],
                                 options={'maxiter':60,'maxls':24,'ftol':2e-13,'gtol':1e-9})
                    radius=float(left+(right-left)*opt.x[0]);m=float(opt.x[1]);rr=radius*np.sqrt(max(0.,1-m*m));zz=radius*m
                    value=float(trace_residual(f,rr,zz,element)[key])
                    eq['peaks'].append(dict(r=rr,z=zz,R=radius,mu=m,element=element,residual=value,m_with_frozen_denominator=abs(value)/denominator,
                                            optimizer_success=bool(opt.success),message=str(opt.message),evaluations=int(opt.nfev),
                                            at_radial_boundary=bool(min(opt.x[0],1-opt.x[0])<1e-8),at_pole=bool(1-abs(m)<1e-8)))
            entry['equations'][key]=eq
        result['rows'].append(entry);save('shell_'+str(row['shell_index']))
    mu=np.r_[-1.,np.linspace(-1.,1.,257)[1:-1],1.]
    for i,R in enumerate(f.interfaces):
        r=R*np.sqrt(1-mu*mu);z=R*mu
        for element in [i,i+1]:
            values=trace_residual(f,r,z,element)
            result['interface_traces'].append(dict(radius=float(R),element=element,mu=mu.tolist(),residuals={key:v.tolist() for key,v in values.items()}))
        save('interface_'+str(i))
    result['interpretation']='A larger maximum can refute adequacy of the previous sampling. Failure to find a larger peak does not certify its absence.'
    save('complete')
if __name__=='__main__':main()

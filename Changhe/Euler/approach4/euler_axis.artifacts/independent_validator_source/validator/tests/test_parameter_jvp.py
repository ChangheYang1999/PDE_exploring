#!/usr/bin/env python3
"""Coefficient/exponent JVP: independent nested AD versus finite differences."""
import datetime,json,time,os
from pathlib import Path
import numpy as np
import torch
from independent_fields import ScalarExpansion,PotentialField

ROOT=Path(__file__).resolve().parents[1]

def numpy_field(p):
    a=(1-p[-1])/p[-1]
    return PotentialField(ScalarExpansion([(p[0],0,0,a/2),(p[1],0,1,(a+1)/2),(p[2],1,0,(a+2)/2)]),
                          ScalarExpansion([(p[3],0,0,(a+1)/2),(p[4],0,1,(a+2)/2),(p[5],1,0,(a+3)/2)]),p[-1])

def run():
    start=time.time()
    torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
    points=np.array([[0.,0.],[0.,.7],[.13,-.3],[.9,.4],[4.,-1.3]])
    p=np.array([.31,-.23,.11,.47,.19,-.13,.64])
    v=np.array([.13,-.2,.07,.21,.17,-.11,.03])
    checks=[]
    for device in ['cpu']+(['cuda:0'] if torch.cuda.is_available() else []):
        def residual(params):
            s=torch.tensor(points[:,0],device=device,requires_grad=True)
            z=torch.tensor(points[:,1],device=device,requires_grad=True)
            c=params[-1];a=(1-c)/c;rho=1+s+z*z
            phi=params[0]*rho**(-a/2)+params[1]*z*rho**(-(a+1)/2)+params[2]*s*rho**(-(a+2)/2)
            q=params[3]*rho**(-(a+1)/2)+params[4]*z*rho**(-(a+2)/2)+params[5]*s*rho**(-(a+3)/2)
            def derivative(f,x):
                return torch.autograd.grad(f.sum(),x,create_graph=True,retain_graph=True)[0]
            ps=derivative(phi,s);pz=derivative(phi,z)
            eta=-8*ps-4*s*derivative(ps,s)-derivative(pz,z)
            vz=c*z+2*phi+2*s*ps
            rq=q+2*s*(c-pz)*derivative(q,s)+vz*derivative(q,z)-2*pz*q
            re=(1+c)*eta+2*s*(c-pz)*derivative(eta,s)+vz*derivative(eta,z)-2*q*derivative(q,z)
            return torch.cat((rq,re))
        value,jvp=torch.autograd.functional.jvp(residual,torch.tensor(p,device=device),torch.tensor(v,device=device))
        value=value.cpu().numpy();jvp=jvp.cpu().numpy()
        def nres(p):
            r=numpy_field(p).reduced(np.sqrt(points[:,0]),points[:,1])
            return np.r_[r['q'],r['eta']]
        valerr=float(np.max(np.abs(value-nres(p))))
        errors=[]
        for h in [1e-3,1e-4,1e-5]:
            fd=(nres(p+h*v)-nres(p-h*v))/(2*h)
            errors.append(float(np.max(np.abs(fd-jvp))))
        row={'device':device,'reduced_residual_error':valerr,'jvp_steps':[1e-3,1e-4,1e-5],'jvp_errors':errors,
             'passed':valerr<1e-12 and errors[-1]<1e-8 and errors[1]<errors[0]}
        checks.append(row);print(json.dumps(row),flush=True)
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':checks,'all_passed':all(x['passed'] for x in checks),'visible_devices':os.environ.get('CUDA_VISIBLE_DEVICES')}
    (ROOT/'results/parameter_jvp_tests.json').write_text(json.dumps(record,indent=2)+'\n')
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':run()

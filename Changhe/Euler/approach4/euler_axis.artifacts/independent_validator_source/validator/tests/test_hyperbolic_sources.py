#!/usr/bin/env python3
"""Local exact examples only; no field here is a decaying global candidate."""
from pathlib import Path
import datetime,hashlib,json,time
import numpy as np
import sympy as sp
from independent_fields import ScalarExpansion,PotentialField
ROOT=Path(__file__).resolve().parents[1];checks=[]
def check(name,error,tolerance,detail=None):
    row={'name':name,'error':float(error),'tolerance':float(tolerance),'passed':bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)

def main():
    start=time.time();exception=None
    try:
        kappa=.37
        for c in [.51,.6,.74]:
            for j in range(5):
                A=-(1+2*j*c)/(2*(j+1))
                field=PotentialField(ScalarExpansion([(-A,0,1,0.)]),ScalarExpansion([(kappa,j,0,0.)]),c)
                r=np.array([0.,.03,.4,.8]);z=np.array([-.7,.2,.4,-.6])
                gp=np.stack((-A*(1+A)*r+kappa**2*r**(4*j+1),2*A*(1-2*A)*z),axis=-1)
                primitive=field.primitive_cylindrical(r,z,gp);red=field.reduced(r,z)
                error=max(np.max(np.abs(primitive)),np.max(np.abs(red['q'])),np.max(np.abs(red['eta'])))
                check(f'axis_polynomial_c{c}_j{j}',error,2e-14,{'A':A,'lambda_r':c+A,'lambda_z':c-2*A})
        r,z,r0,c,k=sp.symbols('r z r0 c k',positive=True)
        a=2*c-1
        for j in range(1,5):
            lam=a/(2*j);nu=3*c-2*lam
            wr=lam*(r-r0*r0/r);wz=nu*z
            ur=wr-c*r;uz=wz-c*z;gamma=k*(r*r-r0*r0)**j;ut=gamma/r
            divergence=sp.diff(ur,r)+ur/r+sp.diff(uz,z)
            rt=(1-c)*ut+wr*sp.diff(ut,r)+wz*sp.diff(ut,z)+ur*ut/r
            pr=-((1-c)*ur+wr*sp.diff(ur,r)+wz*sp.diff(ur,z)-ut*ut/r)
            pz=-((1-c)*uz+wr*sp.diff(uz,r)+wz*sp.diff(uz,z))
            source=sp.diff(ur,r)**2+(ur/r)**2+sp.diff(uz,z)**2-2*ut*sp.diff(ut,r)/r
            defects=[sp.simplify(divergence),sp.simplify(rt),sp.simplify(sp.diff(pr,z)-sp.diff(pz,r)),
                     sp.simplify(-sp.diff(pr,r)-pr/r-sp.diff(pz,z)-source),
                     sp.simplify(wr*sp.diff(gamma,r)-a*gamma)]
            check(f'annular_exact_j{j}',max(0 if d==0 else 1 for d in defects),0.,{'symbolic_defects':[str(d) for d in defects]})
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_fields.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':checks,'exception':exception,'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'all_passed':exception is None and all(c['passed'] for c in checks)}
    (ROOT/'results/hyperbolic_source_tests.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(checks),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()

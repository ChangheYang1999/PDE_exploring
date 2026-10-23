"""Result221 independently manufactured power-tail inverse gate."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math
import numpy as np
import mpmath as mp
from hydrostatic_power_tail import PowerVerticalInverse
R=Path('research/hydrostatic_power_tail_inverse');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    out=dict(status='RUNNING',utc_started=datetime.now(timezone.utc).isoformat(),checks=[],proof_sha256=sha(R/'PROOF.md'),code_sha256=sha(__file__),module_sha256=sha('independent_code/hydrostatic_power_tail.py'),parent_module_sha256=sha('independent_code/independent_hydrostatic.py'))
    def save():(V/'GATE.json').write_text(json.dumps(out,indent=2)+'\n')
    def check(name,ok,evidence=None):
        out['checks'].append(dict(name=name,passed=bool(ok),evidence=evidence))
        if not ok:out['status']='FAILED';save();raise AssertionError(name)
    pts=[(0.,0.),(.137,.219),(0.,3.),(3.,0.),(.5,.5),(3.,4.),(.01,1e4),(-.137,.219),(.137,-.219),(-.137,-.219)]
    for p in [.25,1/3,.5,.75]:
        b=(p-1)/2
        def jet(x,y):
            x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));S=1+x*x+y*y
            return np.stack([y*S**b,2*b*x*y*S**(b-1),S**b+2*b*y*y*S**(b-1),2*b*y*S**(b-1)+4*b*(b-1)*x*x*y*S**(b-2)],axis=-1)
        for order,tail,split in [(24,64,2.),(40,128,32.)]:
            inv=PowerVerticalInverse(jet,p,order,tail,split,.125)
            check('radial center '+str((p,order)),abs(inv.center()+1)<1e-10,inv.center()+1)
            for x,y in pts:
                val=inv.at(x,y)
                with mp.workdps(60):
                    X,Y=mp.mpf(x),mp.mpf(y);B=1+X*X;bb=mp.mpf(b)
                    # Scalar finite hypergeometric antiderivative, independent of tail integration.
                    I=lambda e:Y*B**e*mp.hyp2f1(mp.mpf('.5'),-e,mp.mpf('1.5'),-Y*Y/B)
                    ref=[X*(B+Y*Y)**bb,-I(bb)-2*bb*X*X*I(bb-1)]
                    errs=[float(abs(mp.mpf(a)-b))for a,b in zip(val['V'],ref)]
                check('radial velocity '+str((p,order,x,y)),max(errs)<1e-9,errs)
    for mode in [0,1]:
        def jet(x,y):
            x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));E=np.exp(-x*x-y*y)
            if mode==0:return np.stack([y*E,-2*x*y*E,(1-2*y*y)*E,(4*x*x-2)*y*E],axis=-1)
            return np.stack([x*x*y*E,2*x*(1-x*x)*y*E,x*x*(1-2*y*y)*E,(2-10*x*x+4*x**4)*y*E],axis=-1)
        inv=PowerVerticalInverse(jet,.5,32,96,4.,.125)
        for x,y in pts:
            val=inv.at(x,y);E=math.exp(-x*x-y*y);B=math.sqrt(math.pi)*math.exp(-x*x)*math.erf(y)
            ref=[x*E,(x*x-.5)*B]if mode==0 else[-x*(1-x*x)*E,(.5-2.5*x*x+x**4)*B]
            check('Gaussian angular velocity '+str((mode,x,y)),max(abs(a-b)for a,b in zip(val['V'],ref))<1e-11,[a-b for a,b in zip(val['V'],ref)])
    out.update(status='PASS',utc_finished=datetime.now(timezone.utc).isoformat(),count=len(out['checks']));save();print(out['status'],out['count'],flush=True)
if __name__=='__main__':main()

"""Independent exact energies for signed sums of explicit Poisson potentials."""
from pathlib import Path
from flint import fmpq,fmpq_poly,ctx
from math import factorial
from datetime import datetime,timezone
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import T
from negative import negative_norm

def beta_int(p,q):
    value=fmpq(factorial(p-1))
    for k in range(p):value/=q+k
    return value

if __name__=='__main__':
    ctx.prec=384
    c=fmpq('4076476460239181/2251799813685248');delta=1-1/c
    records=[]
    for n in [1,3,7,21,59]:
        m=(n-1)//2;A={};phi=[]
        for ell,w in zip([7,8,11],[fmpq(1),fmpq(-2),fmpq(1,3)]):
            b=ell*delta/2;a=b+m-1
            A[ell,'s',n]=4*w*a*T**m*((n+1)-(a+1)*T)
            phi.append((a,w))
        observed=fmpq(negative_norm({(0,0):A},delta,False)['squared_norm_div_pi'])
        expected=fmpq(0)
        for a,w in phi:
            for b,v in phi:
                expected+=2*a*w*v*((n+1)*beta_int(n+1,a+b+1-n)+(n-a)*beta_int(n+2,a+b-n))
        assert expected>0 and observed==expected
        records.append({'n':n,'signed_branches':3,'exact_match':True,'norm_squared_div_pi':str(expected)})
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'delta':str(delta),'checks':records}
    (ROOT/'research/exact_negative_norm/verification/cross_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print({k:v for k,v in out.items() if k!='checks'},'exact tests',len(records),flush=True)

"""Independent exact polynomial and enclosure checks of the field machinery."""
from collections import defaultdict
from hashlib import sha256
import json
import math
from pathlib import Path
import time
from flint import fmpq as Q,arb,ctx
from fields013 import Evaluator,derivative_series,SOURCE_HASHES
from asymptotics013 import Expansion

def addpoly(a,b):
    out=defaultdict(Q,a)
    for key,v in b.items():out[key]+=v
    return {k:v for k,v in out.items()if v}

def mulpoly(a,b):
    out=defaultdict(Q)
    for (i,j),v in a.items():
        for (k,l),w in b.items():out[i+k,j+l]+=v*w
    return {k:v for k,v in out.items()if v}

def harmonic_poly(kind,n,h):
    out={}
    for j in range(n+1):
        if (j%2==0)==(kind=='c'):
            out[n-j,j]=Q(math.comb(n,j)*(-1)**(j//2))
    radial={(0,0):Q(1)}
    for k in range(h):radial=mulpoly(radial,{(2,0):Q(1),(0,2):Q(1)})
    return mulpoly(out,radial)

def cartesian_poly_diff(poly,i,j):
    for axis in [0]*i+[1]*j:
        out={}
        for (x,y),a in poly.items():
            d=x if axis==0 else y
            if d:out[x-(axis==0),y-(axis==1)]=a*d
        poly=out
    return poly

def polynomial_check():
    checks=0;x,y=Q(3,5),Q(4,5)
    zz=[(Q(1),Q(0))]
    for n in range(24):
        a,b=zz[-1];zz.append((a*x-b*y,a*y+b*x))
    for kind in ['c','s']:
        for n in range(11):
            for h in range(4):
                p=harmonic_poly(kind,n,h);degree=n+2*h
                for total in range(6):
                    for i in range(total+1):
                        j=total-i;exact=sum((a*x**u*y**v for (u,v),a in cartesian_poly_diff(p,i,j).items()),Q(0))
                        actual=Q(0)
                        for (a,b,N,k),v in derivative_series(kind,n,i,j).items():
                            factor=Q(math.factorial(degree),math.factorial(degree-a))if degree>=a else Q(0)
                            actual+=v*factor*zz[N][0 if k=='c'else 1]
                        assert exact==actual,(kind,n,h,i,j,exact,actual)
                        checks+=1
    return checks

def main():
    tick=time.monotonic();pc=polynomial_check();e=Evaluator(384,max_density_order=2,max_velocity_order=1);checks=0
    # A complete local Taylor model must actually retain its announced degree.
    series=e.modes_taylor('1',40)
    assert all(p.prec>=41 for mm in series.values()for p in mm.values())
    for d in ['-.001','.001']:
        rr=arb(1)+arb(d);actual=e.modes_at(rr)
        majorants,R=e.mode_majorants(1);z=abs(arb(d))/R
        for key,mm in series.items():
            for mode,p in mm.items():
                val=arb(0)
                for a in reversed(p.coeffs()[:41]):val=val*arb(d)+a
                err=majorants[key].get(mode,arb(0))*z**41/(1-z)
                assert (actual[key].get(mode,arb(0))-val).abs_upper()<err.abs_upper()+arb('1e-75')
                checks+=1
    for side,r in [('origin','1e-3'),('far','1e4')]:
        expansion=Expansion(e,side,12);actual=e.modes_at(r)
        for key in [('rho',1,0),('rho',0,1),('rho',2,0),('rho',1,1),('rho',0,2)]:
            approximated=expansion.modes_at(*key,r)
            error=sum((a*arb(r)**arb(p) for a,p in expansion.remainder_terms(*key,r)),arb(0))
            for mode in set(actual[key])|set(approximated):
                assert (actual[key].get(mode,arb(0))-approximated.get(mode,arb(0))).abs_upper()<error.abs_upper()+arb('1e-75')
                checks+=1
    out={'status':'CHECKS_PASSED','source_hashes':SOURCE_HASHES,'exact_polynomial_checks':pc,'enclosure_crosschecks':checks,'elapsed_seconds':time.monotonic()-tick,'scope':'Independent finite polynomial derivatives and selected Taylor/asymptotic enclosures. Global bounds require the separate complete cover.'}
    dest=Path(__file__).with_suffix('.json');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()

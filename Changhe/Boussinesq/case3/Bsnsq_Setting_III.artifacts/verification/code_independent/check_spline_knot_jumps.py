"""Independent exact value-based checker of radial knot jumps.

No generator imports and no SciPy spline derivative calls. Exact de Boor
values at p+1 equally spaced points inside each polynomial interval give
its pth derivative via the pth finite difference, with no truncation error.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from math import comb
from bisect import bisect_right
import argparse,hashlib,json,time
import numpy as np


def readq(q):return F(int(q['numerator']),int(q['denominator']))
def binary(x):return F.from_float(float(x))


def value(t,c,p,x):
    k=bisect_right(t,x)-1
    assert p<=k<len(c)
    d=[c[k-p+j] for j in range(p+1)]
    for r in range(1,p+1):
        for j in range(p,r-1,-1):
            i=k-p+j;alpha=(x-t[i])/(t[i+p-r+1]-t[i])
            d[j]=(1-alpha)*d[j-1]+alpha*d[j]
    return d[p]


def derivative_by_values(knots,coeff,p,left,right):
    h=(right-left)/(p+2)
    values=[value(knots,coeff,p,left+(j+1)*h) for j in range(p+1)]
    return sum(((-1)**(p-j)*comb(p,j)*values[j] for j in range(p+1)),F(0))/h**p


def check(path):
    d=json.loads(Path(path).read_text());archive=Path(d['archive']);assert hashlib.sha256(archive.read_bytes()).hexdigest()==d['sha256']
    with np.load(archive,allow_pickle=False) as z:
        p=int(z['deg']);N=int(z['Nt']);K=int(z['K']);grade=float(z['grade']);assert str(z['rmap'])=='r2'
        assert p>=1 and N>=1 and K>=1 and grade>0 and float(z['beta_basis'])>0 and float(z['L'])>0
        assert float(z['beta_basis']).hex()==d['basis_beta_hex'] and float(z['L']).hex()==d['L_hex']
        assert (p,N,K,grade.hex())==(d['degree'],d['Nt'],d['K'],d['grade_hex'])
        raw=[0.]*p+list(np.linspace(0.,1.,N+1)**grade)+[1.]*p
        assert [float(v).hex() for v in raw]==d['knots_hex'];knots=[binary(v) for v in raw];edges=knots[p:-p] if p else knots
        result={}
        for name in ['cF','cG']:
            arr=z[name].reshape(K,len(knots)-p-1);c=[F(0) for _ in range(arr.shape[1])]
            for n in range(0,K,2):
                for j in range(n//2,len(c)):c[j]+=(-1 if (n//2)%2 else 1)*binary(arr[n,j])
            f=d['fields'][name];assert c==[readq(v) for v in f['axis_coefficients']]
            vals=[derivative_by_values(knots,c,p,a,b) for a,b in zip(edges[:-1],edges[1:])]
            assert vals==[readq(v) for v in f['interval_pth_derivatives']]
            jumps=[b-a for a,b in zip(vals[:-1],vals[1:])];assert jumps==[readq(v) for v in f['jumps']]
            count=sum(v!=0 for v in jumps);assert count==f['nonzero_count'];witness=next((i for i,v in enumerate(jumps,1) if v),None)
            result[name]={'nonzero_count':count,'first_nonzero_knot_index':witness,'first_jump_display':float(jumps[witness-1]) if witness else None,'verdict':'NOT_C'+str(p) if witness else 'AXIS_TEST_INCONCLUSIVE'}
    return {'certificate':str(path),'archive_sha256':d['sha256'],'degree':p,'intervals_per_field':N,'fields':result,'all_exact_equalities_passed':True}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('certificates',nargs='+');a=ap.parse_args();start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();rows=[check(p) for p in a.certificates]
    d={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'all_passed':True,'checks':rows};Path(a.output).write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))

if __name__=='__main__':main()

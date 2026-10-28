"""Independent numerical falsification tests for the geometric box bound.
The exhaustive interval certificate, not this diagnostic, supplies rigor.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import numpy as np,json,hashlib
from flint import arb,ctx
from certify_geometric_profile import bound
ctx.prec=192;ROOT=Path(__file__).resolve().parents[1]
def quotient(u,a,b,alpha):
    # Real-coordinate distance avoids the certifier's cosine-difference formula.
    distance=np.hypot(np.cos(a)-u*np.cos(b),np.sin(a)+u*np.sin(b))
    return (1-u**alpha+np.maximum(np.sin(2*a),0)**alpha+u**alpha*np.maximum(np.sin(2*b),0)**alpha)/(2*distance**alpha)
def main():
    rng=np.random.default_rng(4388834);records=[]
    for aa in ['3/10','1/2']:
        alpha=float(Fraction(aa));largest=-1e99;count=0
        for _ in range(12000):
            # Independent random exact rational boxes, including broad ones.
            den=2**int(rng.integers(3,17));bounds=[]
            for axis in range(3):
                last=den if axis==0 else den//2
                x,y=sorted(rng.integers(0,last+1,2))
                if axis==0:x=max(1,x);y=min(den-1,max(x,y))
                bounds.extend([Fraction(int(x),den),Fraction(int(y),den)])
            if bounds[0]>bounds[1]:continue
            upper=float(bound(tuple(bounds),arb(aa)).upper())
            points=rng.random((30,3))
            for axis in range(3):points[:,axis]=float(bounds[2*axis])+(float(bounds[2*axis+1]-bounds[2*axis]))*points[:,axis]
            points[:,1:]*=np.pi
            values=quotient(points[:,0],points[:,1],points[:,2],alpha)
            excess=float(values.max()-upper);largest=max(largest,excess);count+=len(values)
            assert excess<1e-10,(aa,bounds,upper,values.max())
        # Direct profile values for arbitrary quadrants independently test reduction.
        p=rng.normal(size=(250000,2));q=rng.normal(size=(250000,2))*np.exp(rng.uniform(-8,8,(250000,1)))
        def g(v):
            r=np.linalg.norm(v,axis=1);return .5*(r**alpha+np.sign(v[:,0]*v[:,1])*(2*abs(v[:,0]*v[:,1])/r)**alpha)
        ratios=abs(g(p)-g(q))/np.linalg.norm(p-q,axis=1)**alpha
        target=1.007 if aa=='3/10' else 1.021
        assert ratios.max()<target
        records.append(dict(alpha=aa,box_sample_checks=count,largest_box_excess=largest,arbitrary_pair_checks=len(p),largest_arbitrary_ratio=float(ratios.max()),certified_target=target))
    paths=['code/check_geometric_profile.py','code/certify_geometric_profile.py','data/geometric_profile_a30_tight.json','data/geometric_profile_a50_tight.json']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=records,status='Independent real-coordinate numerical diagnostics passed. Not a certificate.',sha256={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in paths})
    (ROOT/'data/geometric_profile_independent_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()

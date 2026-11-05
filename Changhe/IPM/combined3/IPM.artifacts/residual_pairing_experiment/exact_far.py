"""Exact homogeneous far-field residual coefficients using fmpq convolutions."""
import json,sys,time
from collections import defaultdict
from pathlib import Path
from flint import fmpq as Q,fmpq_poly
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator,C,SOURCE_HASHES
from asymptotics013 import Expansion
SHIFT=400

def polys(field):
    out={}
    for (kind,n,p),v in field.items():
        if (p,kind)not in out:out[p,kind]=[Q(0)]*(2*SHIFT+1)
        # sin(theta) represented by (z-z^-1)/2, with formal 1/i suppressed.
        out[p,kind][SHIFT+n]+=v/2
        out[p,kind][SHIFT-n]+=v/2 if kind=='c' else -v/2
    return {k:fmpq_poly(v)for k,v in out.items()}

def run():
    tick=time.monotonic();e=Evaluator();a=Expansion(e,'far',degree=2)
    rho=a.field('rho',0,0);rx=a.field('rho',1,0);ry=a.field('rho',0,1)
    u=a.field('u1',0,0);v=a.field('u2',0,0)
    floor=Q(-4)
    residual=defaultdict(Q)
    for (kind,n,p),c in rho.items():
        if p>=floor:residual[kind,n,p]+=(C*p-1)*c
    for velocity,gradient in [(u,rx),(v,ry)]:
        A=polys(velocity);B=polys(gradient)
        for (p,k),P in A.items():
            for (q,l),T in B.items():
                if p+q<floor:continue
                assert k!=l
                PT=P*T
                for n in range(1,2*SHIFT):
                    coeff=2*PT[2*SHIFT+n]
                    if coeff:residual['s',n,p+q]+=coeff
    residual={k:v for k,v in residual.items()if v}
    powers=sorted(set(k[2]for k in residual),reverse=True)
    result={'status':'EXACT_RATIONAL_ASYMPTOTIC_COEFFICIENTS','expansion_degree':2,'floor':str(floor),'source_hashes':SOURCE_HASHES,'powers':[],'elapsed_seconds':time.monotonic()-tick}
    for p in powers:
        coeffs=[{'kind':k,'n':n,'value':str(c),'float':float(c)}for (k,n,pp),c in sorted(residual.items())if pp==p]
        result['powers'].append({'power_exact':str(p),'power':float(p),'coefficients':coeffs,'angular_l2_coefficient':(3.141592653589793*sum(r['float']**2 for r in coeffs))**.5})
    (HERE/'exact_far_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({**result,'powers':[{k:v for k,v in p.items()if k!='coefficients'}for p in result['powers']]},indent=2),flush=True)
if __name__=='__main__':run()

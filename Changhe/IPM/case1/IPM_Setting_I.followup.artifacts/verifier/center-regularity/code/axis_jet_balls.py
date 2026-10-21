"""Ball enclosures for the exact ideal-node interpolant of binary checkpoint data.
Independent endpoint cardinal derivatives, cosine transform and Bessel moments.
No numerics-lane code imports. No claim about an unknown exact profile.
"""
import sys,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx
ctx.prec=256

def binary(v):
    p,q=float(v).as_integer_ratio()
    return arb(p)/q

def bessel(n,z):
    return z.bessel_j(n) if n>=0 else (-1)**(-n)*z.bessel_j(-n)

def evaluate(filename):
    data=np.load(filename)
    N=int(data['N']);M=int(data['M']); bv=data['b']
    assert bv.shape==(N+1,M) and np.all(bv[0]==1.)
    beta=binary(data['beta']);cl=binary(data['c_l']);L=binary(data['L'])
    k=1/cl;pi=arb.pi()
    dq=[arb(0)]+[-2*(-1)**j/((1-(pi*j/N).cos())/2) for j in range(1,N)]+[arb(-(-1)**N)]
    bq=[sum((dq[j]*(binary(bv[j,a])-1) for j in range(1,N+1)),arb(0)) for a in range(M)]
    co=[sum((bq[a]*(pi*m*(2*a+1)/(2*M)).cos() for a in range(M)),arb(0))*2/M for m in range(M)]
    co[0]/=2
    K=(1-k)/(2*L*L);d=1+beta
    ai=1/d;bi=2*beta/(3*d**4);ci=4*beta**2/(3*d**7)-2*beta/(15*d**6)
    F2=sum((-(2*m)**2*co[m] for m in range(1,M)),arb(0))
    F4=sum(((2*m)**4*co[m] for m in range(1,M)),arb(0))
    F6=sum((-(2*m)**6*co[m] for m in range(1,M)),arb(0))
    D2=K*ai**2*F2
    D4=K*(24*ai*bi*F2+ai**4*F4)
    D6=K*(360*(2*ai*ci+bi**2)*F2+120*ai**3*bi*F4+ai**6*F6)
    G5=(D4+4*D2)/24;G7=(D6-10*D4-56*D2)/720
    moments={}
    for ell in range(2,8):
        moments[ell]=pi/(4*ell)*sum((m*co[m]*(bessel(m-ell,ell*beta)-bessel(-ell-m,ell*beta)) for m in range(1,M)),arb(0))
    pn={n:K/(2*pi)*(moments[(n-1)//2]-moments[(n+1)//2]+moments[(n-3)//2]-moments[(n+3)//2]) for n in [7,9,11]}
    p7=pn[7];p9=pn[9];p11=pn[11]
    determinant=7*p9**2+p7**2-8*p7*p11
    values={'G5_axis_limit':G5,'x2_G7_axis_limit':G7,'rho5_sine7_coefficient':p7,
            'w_x5_logx_coefficient':3*p7,'D2':D2,'D4':D4,'D6':D6,
            'rho5_sine9_coefficient':p9,'rho5_sine11_coefficient':p11,
            'transport_balance_determinant':determinant,
            'Q9_if_Q7_zero_at_saved_cl':(5*cl-1)*determinant/(7*p9),
            'Q7_if_center_identity':(5*cl-1)*p7-7*(3*cl-1)*p9}
    return {'date':datetime.now(timezone.utc).isoformat(),'source':str(filename),
      'md5':hashlib.md5(Path(filename).read_bytes()).hexdigest(),'precision_bits':ctx.prec,
      'N':N,'M':M,'interpretation':'exact binary nodal values and parameters at ideal Chebyshev-Lobatto/Gauss nodes; k=1/exact(c_l)',
      'values':{n:v.str(45) for n,v in values.items()},
      'contains_zero':{n:bool(v.contains(0)) for n,v in values.items()},
      'angular_coefficients': [v.str(45) for v in co]}

if __name__=='__main__':
    result=evaluate(sys.argv[1]);text=json.dumps(result,indent=2)+'\n'
    if len(sys.argv)>2:Path(sys.argv[2]).write_text(text)
    print(json.dumps({k:v for k,v in result.items() if k!='angular_coefficients'},indent=2))

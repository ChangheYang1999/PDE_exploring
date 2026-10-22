"""Independent mpmath derivatives and difference-quotient Jacobian tests."""
import json
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
import mpmath as mp
from rational_basis import Term,matrix,make_terms
from rational_solver import Matrices,collocation


def main():
    mp.mp.dps=50
    pts=np.array([[0,0],[.17,-.42],[1.3,2.1]])
    terms=[Term(1,0,1,1),Term(1,2,4,2),Term(3,1,.5,1)]
    maxerr=0.
    for beta in (2.,2.9,4.):
        for term in terms:
            for dx,dy in ((0,0),(1,0),(0,1),(2,0),(0,2),(3,0),(1,2)):
                got=matrix([term],beta,'psi',pts,dx,dy)[:,0]
                q=(2-mp.mpf(term.tail_order)/beta-term.i-term.j)/2
                L=mp.mpf(term.scale)
                f=lambda x,y:L**(2-term.i-term.j)*x**term.i*y**term.j*(1+(x*x+y*y)/L**2)**q
                exact=np.array([float(mp.diff(f,(mp.mpf(str(x)),mp.mpf(str(y))),(dx,dy))) for x,y in pts])
                err=np.max(np.abs(got-exact)/(1+np.abs(exact)))
                maxerr=max(maxerr,float(err))
    assert maxerr<1e-12,maxerr
    ps=make_terms(4,(1,4),(1,2),'psi');ts=make_terms(4,(1,4),(1,2),'theta')
    M=Matrices(2.9,ps,ts,collocation(6,5,4,0))
    rng=np.random.default_rng(491)
    z=rng.normal(0,.02,M.np+M.nt)
    d=rng.normal(size=len(z));d/=np.linalg.norm(d)
    J=M.evaluate(z,True)
    errors=[]
    for h in (1e-3,1e-4,1e-5):
        fd=(M.evaluate(z+h*d)-M.evaluate(z-h*d))/(2*h)
        errors.append(float(np.max(np.abs(fd-J@d))/(1+np.max(np.abs(J@d)))))
    assert max(errors)<1e-8,errors
    p,t=M.unpack(z);a,c,b=M.center_rows
    center=[float(a@t),float(c@p),float(b@p)]
    assert np.max(np.abs(np.array(center)-[1,1+2.9/2,4/2.9]))<1e-13
    summary={'timestamp':datetime.now(timezone.utc).isoformat(),'mpmath_digits':50,
             'basis_derivative_max_scaled_error':maxerr,'jacobian_directional_errors':errors,
             'center':center,'verdict':'CONFIRMED for tested derivative and Jacobian formulas'}
    Path('verification/rational_math.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()

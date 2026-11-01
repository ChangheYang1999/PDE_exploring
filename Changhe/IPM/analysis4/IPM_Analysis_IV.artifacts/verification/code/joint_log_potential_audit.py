"""Exact Cartesian tests of the joint logarithmic potential reconstruction."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import math
import random
import time
from laurent_log_audit import Q, Poly, L, parse


def apply_scalar(p, c, d=Q(1)):
    return p*c+p.derivative()*d


def inverse_scalar(p, c, d=Q(1)):
    assert c
    out=Poly([])
    factor=1/c
    while p:
        out += p*factor
        p=p.derivative()
        factor *= -d/c
    return out


def euler(v, shift=0):
    return v.scale(v.q+shift)+v.dt()


def cosine_field(q, coeffs):
    M=2*(len(coeffs)-1)
    degree=max((len(p) for p in coeffs),default=0)
    rows=[[Q(0) for _ in range(2*M+1)] for _ in range(degree)]
    for m,p in enumerate(coeffs):
        for k,a in enumerate(p.coeffs()):
            if m==0: rows[k][M]+=a
            else:
                rows[k][M+2*m]+=a/2
                rows[k][M-2*m]+=a/2
    return L(q,M,[Poly(row) for row in rows])


def amplitude(v,m):
    return Poly([2*p[v.M+m] if v.M+m>=0 else Q(0) for p in v.a])


def inverse_y(v,q):
    top=max((len(p)-1-v.M for p in v.a if p),default=1)
    assert top%2==1
    J=(top-1)//2
    cc=[Poly([]) for _ in range(J+2)]
    for m in range(J,0,-1):
        target=amplitude(v,2*m+1)+apply_scalar(cc[m+1],q/2+m+1,Q(1,2))
        cc[m]=inverse_scalar(target,q/2-m,Q(1,2))
    target=amplitude(v,1)+apply_scalar(cc[1],q/2+1,Q(1,2))
    cc[0]=inverse_scalar(target,q)
    return cosine_field(q,cc[:-1])


def norm(v):
    return sum((abs(a) for p in v.a for a in p.coeffs()),Q(0))


def main():
    start=time.monotonic()
    rng=random.Random(9031742)
    xx=L(1,1,[Poly([Q(1,2),0,Q(1,2)])])
    iy=parse(1,{1:[1]})
    rows=[]
    for case in range(32):
        delta=[Q(2,3),Q(4,9),Q(1,2),Q(3,5),Q(7,10)][case%5]
        nr=2*int(delta.q)//math.gcd(int(delta.p),2)
        n=int(math.ceil(Q(20)/delta))+rng.randint(0,20)
        X=n*delta
        q=4-X
        K=rng.randint(0,n//nr)
        J=rng.randint(0,min(7,n-2))
        coeffs=[Poly([Q(rng.randint(-5,5),rng.randint(1,7)) for _ in range(K+1)]) for _ in range(J+1)]
        C=cosine_field(q,coeffs)
        Y=C.Y().scale(-1)
        G=C.X().Y().scale(-1)
        F=(C.X().X()-C.Y().Y()).Y()
        lhs=euler(euler(Y,-1))
        rhs=(xx*xx+iy*iy)*G.X()+(xx*iy*G.Y()).scale(2)+iy*iy*F
        assert (lhs-rhs).zero(),('Euler',case)
        V=L(rhs.q,rhs.M,[Poly([]) for _ in rhs.a])
        # Scalar polynomial inversion acts at each Laurent frequency.
        for angular in range(max((len(p) for p in rhs.a),default=0)):
            p=Poly([row[angular] for row in rhs.a])
            result=inverse_scalar(inverse_scalar(p,q-1),q-2)
            while len(V.a)<len(result):V.a.append(Poly([]))
            for k,a in enumerate(result.coeffs()):
                coefficients=V.a[k].coeffs()
                while len(coefficients)<=angular:coefficients.append(Q(0))
                coefficients[angular]+=a
                V.a[k]=Poly(coefficients)
        V=L(V.q,V.M,V.a)
        assert (V-Y).zero(),('first recovery',case)
        recovered=inverse_y(V,q)
        assert (recovered-C).zero(),('potential recovery',case)
        B=2
        bound=Q(432)/(X*X)*(norm(F)+n*(B+Q(3,2)*delta)*norm(G))
        assert norm(C)<=bound,('bound',case)
        rows.append(dict(case=case,delta=str(delta),n=n,q=str(q),log_degree=K,top_potential_frequency=2*J,
                         exact_euler_identity=True,exact_first_derivative_recovery=True,
                         exact_potential_recovery=True,potential_norm=str(norm(C)),bound=str(bound),bound_pass=True))
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),seed=9031742,
             code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
             cartesian_engine_sha256=sha256(Path('code/laurent_log_audit.py').read_bytes()).hexdigest(),
             cases=rows,actual_elapsed_s=time.monotonic()-start)
    Path('research/41_joint_log_potential/verification/cartesian_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(cases=len(rows),all_passed=True,actual_elapsed_s=out['actual_elapsed_s'])),flush=True)

if __name__=='__main__':main()

"""Exact Cartesian checks of the finite leading-velocity optimization."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from random import Random
from fractions import Fraction
import json
import time
from laurent_log_audit import Q, parse
from maximal_log_cartesian_check import poisson
from shear_approximant_audit import family, amplitudes

TARGET=Path('research/54_leading_velocity_optimum')


def one(gamma, a, t):
    K=len(a)-1
    A=family(gamma,K)
    f=parse(gamma,{2*k+1:[str(v)] for k,v in enumerate(a) if v})
    g=poisson(f)
    b=amplitudes(g)
    P=1+gamma
    objective=sum((m+P)*t**(m//2)*abs(v) for m,v in b.items())
    weights=[A[j-1]*t**j/2 for j in range(1,K+2)]
    bound=min(weights)
    assert objective>=bound
    constraint=sum(2*(2*j+P)*b.get(2*j,Q(0))/A[j-1] for j in range(1,K+2))
    assert constraint==-1
    if t==1:
        predicted=[K+1]
    else:
        J=P*(t+1)/(2*(t-1))
        p,q=int(J.p),int(J.q)
        ceil=(p+q-1)//q
        predicted=[min(K+1,max(1,ceil))]
        if q==1 and p>=1 and p+1<=K+1:
            predicted.append(p+1)
    actual=[j for j,v in enumerate(weights,1) if v==bound]
    assert predicted==actual,(str(gamma),str(t),K,predicted,actual)
    return dict(gamma=str(gamma),K=K,t_exp_2sigma=str(t),objective_exact=str(objective),
                minimum_exact=str(bound),minimum_indices=actual,equality=objective==bound,
                telescoping_constraint_exact=str(constraint))


def main():
    start=time.monotonic()
    raw=Path('research/02_candidate007/data/leading_exact.json').read_bytes()
    source=json.loads(raw)
    (TARGET/'sources/leading_exact.json').write_bytes(raw)
    gamma_stored=Q(source['gamma'])
    rng=Random(5402026)
    rows=[]
    for gamma in [Q(1,3),Q(1,2),Q(5,9),gamma_stored]:
        for K in [0,1,2,5,9]:
            for t in [Q(1),Q(9,8),Q(3,2),Q(11,5),Q(4)]:
                a=[Q(1)]+[Q(rng.randint(-7,7),rng.randint(1,11)) for _ in range(K)]
                control=one(gamma,a,t)
                rows.append(dict(kind='arbitrary_profile',**control))
                A=family(gamma,K)
                for j in control['minimum_indices']:
                    optimum=A[:j]+[Q(0)]*(K+1-j)
                    row=one(gamma,optimum,t)
                    assert row['equality']
                    rows.append(dict(kind='attaining_truncation',**row))
                if len(control['minimum_indices'])==2:
                    j,k=control['minimum_indices']
                    optimum=[A[l] if l<j else A[l]/3 if l<k else Q(0) for l in range(K+1)]
                    row=one(gamma,optimum,t)
                    assert row['equality']
                    rows.append(dict(kind='attaining_convex_combination',**row))
    gamma=gamma_stored
    first=Q(source['density']['1'])
    a={int(m):Q(v)/first for m,v in source['density'].items()}
    f=parse(gamma,{m:[str(v)] for m,v in a.items()})
    g=poisson(f); b=amplitudes(g)
    assert b=={int(m):Q(v)/first for m,v in source['stream'].items()}
    pure_b=-1/(2*(3+gamma))
    velocity=sum((m+1+gamma)*abs(v) for m,v in b.items())
    A=family(gamma,9)
    distance=sum(abs(a[2*k+1]-A[k]) for k in range(10))+(1+gamma)/(2*gamma)-sum(A)
    f2=(g.X()*f.Y()-g.Y()*f.X()).scale(1/(Q(source['c'])-1))
    second=sum(abs(v) for v in amplitudes(f2).values())
    cand={
        'normalized_first_stream':b[2], 'pure_first_stream':pure_b,
        'first_stream_ratio':abs(b[2]/pure_b),
        'combined_polar_velocity_norm':velocity,
        'combined_polar_velocity_ratio_to_pure':2*velocity,
        'wiener_distance_to_normalized_shear':distance,
        'normalized_shear_wiener_norm':(1+gamma)/(2*gamma),
        'second_density_wiener_norm':second,
        'degree19_minimum_velocity':A[9]/2,
        'velocity_over_degree19_minimum':2*velocity/A[9],
    }
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
             actual_elapsed_s=time.monotonic()-start,arithmetic='Exact rationals; independent Cartesian Poisson inverse',
             checks=rows,candidate007={k:dict(exact=str(v),approx=float(v)) for k,v in cand.items()},
             source_hashes={str(p):sha256(Path(p).read_bytes()).hexdigest() for p in [
                 'code/leading_velocity_optimum_audit.py','code/laurent_log_audit.py',
                 'code/maximal_log_cartesian_check.py','code/shear_approximant_audit.py',
                 'research/02_candidate007/data/leading_exact.json']})
    (TARGET/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(passed=len(rows),actual_elapsed_s=out['actual_elapsed_s'],
                         candidate007={k:float(v) for k,v in cand.items()}),indent=2))


if __name__=='__main__':main()

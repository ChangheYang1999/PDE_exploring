"""Independent explicit-mode checks. FLOAT diagnostics, not an interval certificate.
The proof precedes this script. One process, no networking, no servers.
"""
import json, math, time, datetime, hashlib
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import gammainc, gamma

root = Path(__file__).resolve().parents[1]
start = time.monotonic()
rows = []

def integrate(fn):
    v0, e0 = quad(fn, 0, 1, epsabs=2e-9, epsrel=2e-11, limit=300)
    v1, e1 = quad(fn, 1, np.inf, epsabs=2e-9, epsrel=2e-11, limit=300)
    return v0+v1, e0+e1

def values(r, M, sign):
    f = r**M * math.exp(-r*r) if r < 26 else 0.0
    df = (M-2*r*r)*f
    if sign == 1:
        g = f if M == 1 else math.exp(-r*r)*(r**M-(M-1)*r**(M-2)) if r < 26 else 0.0
        dg = (M-2)*g + (2*M-2*r*r)*f
    else:
        g = -gamma(M+2)*gammainc(M+2, r*r)*r**(-M-2)
        dg = -(M+2)*g-2*r*r*f
    return f, df, g, dg

for p in [-0.75, -0.25, 0, 0.5, 1, 1.5, 2, 2.5]:
    for M in [1, 3, 7]:
        ef = integrate(lambda r: (1+r*r)**p*sum(x*x for x in (values(r,M,1)[1],M*values(r,M,1)[0]))/r)
        energies=[]
        defects=[]
        for sign in [1,-1]:
            m = sign*M
            eg = integrate(lambda r: (1+r*r)**p*sum(x*x for x in (values(r,M,sign)[3],(m-2)*values(r,M,sign)[2]))/r)
            cross = integrate(lambda r: 2*p*r*r/(1+r*r)*(1+r*r)**p*(m*values(r,M,sign)[0]**2+(m-2)*values(r,M,sign)[2]**2)/r)
            defect=eg[0]-ef[0]+cross[0]
            error=eg[1]+ef[1]+cross[1]
            assert abs(defect) < max(100*error, 1e-8*ef[0]), (p,M,sign,defect,error)
            if p >= 0 and sign==1:
                assert eg[0] <= ef[0]+max(100*error,1e-8*ef[0])
            if p==0:
                assert abs(eg[0]/ef[0]-1)<1e-8
            energies.append(eg[0]); defects.append(defect)
        pair_ratio = sum(energies)/(2*ef[0])
        if p>=0:
            A=(9+p*p)/(3-p)**2
            B=(1+p)**2/(1+p*p) if p<=1 else 2
            bound=(1+A*B)/2
        else:
            bound=max(7,1+4/(1+p))**2
        assert pair_ratio <= bound+1e-7
        rows.append(dict(p=p,M=M,input_energy=ef[0],output_positive=energies[0],output_negative=energies[1],pair_squared_ratio=pair_ratio,proved_B_squared_bound=bound,identity_defects=defects))
# Pointwise comparison of the two potentials, including nonzero qdot.
checks=0
for p in [0,0.5,1,1.5,2,2.5,2.9]:
    A=(9+p*p)/(3-p)**2
    B=(1+p)**2/(1+p*p) if p<=1 else 2
    for M in [1,3,7,101]:
        for r in np.geomspace(1e-5,1e5,101):
            q=p*r*r/(1+r*r)
            qdot=2*p*r*r/(1+r*r)**2
            lhs=((M+2)**2+q*q+qdot)/((M+2-q)**2+qdot)
            rhs=((M+q)**2+qdot)/(M*M+q*q+qdot)
            assert lhs<=A*(1+1e-12)
            assert rhs<=B*(1+1e-12)
            checks+=1
result=dict(status='FLOAT diagnostic only; all explicit-mode and potential checks pass',timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,proof_sha256=hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=rows,potential_checks=checks)
out=root/'verification'/'gaussian_modes.json'
with out.open('x') as fp: json.dump(result,fp,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
print('p M pair_squared_ratio proved_B_squared_bound')
for row in rows:
    print(row['p'],row['M'],row['pair_squared_ratio'],row['proved_B_squared_bound'])

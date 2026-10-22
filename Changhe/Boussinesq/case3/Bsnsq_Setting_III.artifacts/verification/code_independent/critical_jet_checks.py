"""Exact independent B2 jet-transport and saddle-threshold checks.
No numerical-lane modules, servers, JavaScript, GPU or formal builds.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from math import comb
import json
import time
import sympy as s

start = time.perf_counter()
x, y = s.symbols('x y', real=True)
W = (2*x + 3*y + x*y + x**3 + 2*x*y**2,
     -x + 4*y + x*x*y - y**3 + x**4)
om = x**6 + 3*x**4*y**2 - 2*x**3*y**3 + y**6 + 2*x*y**2 + x + y
D = lambda f, a, b: s.diff(f, x, a, y, b)
jet_checks = []
for n in range(1, 6):
    for r in range(n + 1):
        t = n - r
        lhs = D(W[0]*D(om, 1, 0) + W[1]*D(om, 0, 1), r, t)
        rhs = W[0]*D(om, r+1, t) + W[1]*D(om, r, t+1)
        first = 0
        if r:
            first += r*(D(W[0], 1, 0)*D(om, r, t)
                       + D(W[1], 1, 0)*D(om, r-1, t+1))
        if t:
            first += t*(D(W[0], 0, 1)*D(om, r+1, t-1)
                       + D(W[1], 0, 1)*D(om, r, t))
        higher = 0
        for a in range(r+1):
            for b in range(t+1):
                if a+b < 2:
                    continue
                higher += comb(r, a)*comb(t, b)*(D(W[0], a, b)*D(om, r-a+1, t-b)
                                               + D(W[1], a, b)*D(om, r-a, t-b+1))
        defect = s.expand(lhs-rhs-first-higher)
        assert defect == 0, (n, r, defect)
        jet_checks.append({'order':n,'x_slots':r,'defect':str(defect)})

saddles = []
for m in (2, 4, 6):
    nu = s.Rational(1, m)
    w1, w2 = -nu*x, (4+nu)*y - x**(m+1)/(m+1)
    omega = x**m
    psi = (2+nu)*x*y - x**(m+2)/((m+1)*(m+2))
    equations = {
        'divergence_minus4':s.expand(D(w1,1,0)+D(w2,0,1)-4),
        'negative_curl_minus_omega':s.expand(-D(w2,1,0)+D(w1,0,1)-omega),
        'vorticity_transport':s.expand(w1*D(omega,1,0)+w2*D(omega,0,1)+omega),
        'poisson_defect':s.expand(-D(psi,2,0)-D(psi,0,2)-omega),
        'stream_velocity1_defect':s.expand(-D(psi,0,1)-(w1-2*x)),
        'stream_velocity2_defect':s.expand(D(psi,1,0)-(w2-2*y)),
    }
    assert all(v == 0 for v in equations.values())
    assert D(omega,m,0) == s.factorial(m)
    assert 1-m*nu == 0
    saddles.append({'m':m,'nu':str(nu),'N':m+2,'surviving_jet':str(s.factorial(m)),
                    'zero_eigenvalue':str(1-m*nu),'defects':{k:str(v) for k,v in equations.items()},
                    'scope':'local coupled PDE example only; fails global target and x parity'})

A = s.Matrix([[1, 20], [0, 2]])
p11,p12,p22=s.symbols('p11 p12 p22')
P=s.Matrix([[p11,p12],[p12,p22]])
sol=s.solve(list(A.T*P+P*A-s.eye(2)),(p11,p12,p22))
P=P.subs(sol)
assert P[0,0]>0 and P.det()>0
assert A.T*P+P*A==s.eye(2)
v=s.Matrix([1,-1]);euclid=(v.T*A*v)[0]
assert euclid<0

resonances=[]
for beta,nu,n,m in [(Q(4),Q(1),16,10),(Q(5,2),Q(1,2),21,13),(Q(8,3),Q(1,3),32,20)]:
    nn=2+(3*beta+2)/nu;mm=1+(2*beta+1)/nu
    ell=n-m;d=1/nu;r=d/beta.denominator
    assert nn==n and mm==m and n%2==m%2 and ell%2==0
    assert d==2*ell-m-1
    assert beta==Q(ell-1,d)-1
    assert d.denominator==1 and r.denominator==1 and r.numerator%2==1
    assert (beta.numerator+beta.denominator)%2==1
    resonances.append({'beta':str(beta),'nu':str(nu),'n':n,'m':m,'ell':ell,'d':str(d),'r':str(r),
                       'Theta_nonnegative_arithmetic_possible':n%2==0,
                       'scope':'necessary arithmetic only, no profile construction'})

out={'checked_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,
     'jet_product_formula':jet_checks,'local_equality_saddles':saddles,
     'non_normal_positive_stable_matrix':{'A':str(A),'P':str(P),'lyapunov_defect':'zero',
                                         'euclidean_quadratic_form_on_1_minus1':str(euclid)},
     'resonance_tuples':resonances,'all_checks_passed':True}
path=Path('research/59_beta2_critical_jets/verification/exact_checks.json')
path.write_text(json.dumps(out,indent=2)+'\n')
Path('research/57_additional_equilibria/verification/resonance_tuples.json').write_text(json.dumps({'checked_utc':out['checked_utc'],'source':'../../code_independent/critical_jet_checks.py','tuples':resonances,'scope':'necessary integer conditions only'},indent=2)+'\n')
print(json.dumps({'runtime_seconds':out['runtime_seconds'],'jet_checks':len(jet_checks),'saddle_examples':len(saddles),'resonance_tuples':resonances,'all_passed':True},indent=2))

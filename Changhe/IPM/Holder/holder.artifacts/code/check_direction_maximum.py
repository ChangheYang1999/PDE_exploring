"""Independent symbolic checks and Arb enclosures for the finite-part Fourier proof.
No numerical quadrature is used in the certificates.
"""
from fractions import Fraction
from math import comb
from datetime import datetime, timezone
from pathlib import Path
import json
import sympy as sy
from flint import arb, ctx

ctx.prec = 160
checks=[]
for n in range(1,51):
    moment = -4*sum((Fraction((-1)**j*comb(2*n-1,j)*comb(3*n-1-j,n-1-j),6*n-1-4*j) for j in range(n)),Fraction(0))
    prod=Fraction(1)
    for j in range(n): prod*=Fraction(2*n+1+4*j,2*n+3+4*j)
    expected=(Fraction((-1)**n)*prod-1)/(2*n)
    assert moment == expected
    checks.append({'n':n,'annular_moment':str(moment),'P_n':str(prod),'identity_exact':True})

u,v=sy.symbols('u v')
polychecks=[]
for n in range(1,13):
    cn=sum((-1)**j*sy.binomial(2*n-1,j)*sy.binomial(3*n-1-j,n-1-j)*u**(3*n-2-2*j) for j in range(n))
    p=sy.expand(u**n*sy.jacobi(n-1,1,n,2*u*u-1))
    der=sy.diff(sy.jacobi(n,0,n-1,2*v-1),v)-2*n*sy.jacobi(n-1,1,n,2*v-1)
    assert sy.expand(cn-p)==0 and sy.expand(der)==0
    polychecks.append({'n':n,'Jacobi_coefficient_identity':True,'derivative_identity':True})

N=50000
ps={1:arb(3)/5,2:arb(45)/77}
angles=[(0,1),(1,12),(1,8),(1,6),(1,4),(1,3),(5,12),(1,2)]
sums=[arb(0) for _ in angles]
for n in range(1,N+1):
    if n>2:
        k=n-2
        ps[n]=ps[n-2]*arb((6*k+1)*(6*k+5)*(2*k+3)**2)/((6*k+7)*(6*k+11)*(2*k+1)**2)
        del ps[n-2]
    pn=ps[n]
    for j,(a,b) in enumerate(angles):
        c=(2*arb.pi()*n*a/b).cos() if a else arb(1)
        sums[j]+=pn*(c-(-1)**n)/(n*(4*n*n-1)*arb.pi())
err=arb(1)/(5*arb.pi()*N*N)
rows=[]
for (a,b),s in zip(angles,sums):
    enclosure=arb(1)/2-s+arb(0,err)
    rows.append({'phase_over_pi':str(Fraction(a,b)),'W_enclosure':enclosure.str(30),'tail_bound':err.str(15)})

out={'created_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
     'description':__doc__,'precision_bits':ctx.prec,'fourier_terms':N,
     'exact_moment_checks':checks,'polynomial_checks':polychecks,'finite_parts':rows}
Path('data/direction_maximum_checks.json').write_text(json.dumps(out,indent=2)+'\n')
for row in rows: print(row)

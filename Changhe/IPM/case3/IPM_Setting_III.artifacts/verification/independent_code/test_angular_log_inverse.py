"""Manufactured, exact-quotient and cross-inverse checks of the new evaluator."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,math
import numpy as np
from angular_log_inverse import GaussianAngular,AngularLogInverse,endpoint_quotient,weighted_diagnostic,QAngular

rows=[]
for q,e in [(.3,.04),(-.2,.07)]:
    model=GaussianAngular(q,e)
    logr=np.log(np.array([.001,.01,.1,.3,1.,2.,3.]))
    exactp,exactd=model.exact_phi_coeff(logr)
    for order in [32,64,128]:
        cf=AngularLogInverse(model,order).coefficients(logr)
        error=max(float(np.max(abs(cf['p']-exactp))),float(np.max(abs(cf['d']-exactd))))
        rows.append(dict(q=q,e=e,order=order,max_coefficient_error=error))
        if order==128:assert error<2e-7,(q,e,error)
# The quotient is independently checked at rational t values without using
# its implementation recurrence to evaluate the original polynomials.
quotients=[]
for coeff in [[.125,-.25,.5,.0625],[-.25,.0625,.125,.25,-.0625]]:
    a,quotient,err=endpoint_quotient(coeff)
    for t in [Fraction(-1),Fraction(-2,3),Fraction(0),Fraction(3,4),Fraction(1)]:
        def cheb(c):
            T=[Fraction(1),t]
            for j in range(2,len(c)):T.append(2*t*T[-1]-T[-2])
            return sum((Fraction(float(v))*T[j] for j,v in enumerate(c)),Fraction(0))
        assert cheb(coeff)-Fraction(a)==(t+1)*cheb(quotient)
    quotients.append(dict(a=a,rounding_l1=err))
# Manufactured weighted identity has a finite-annulus flux, retained exactly
# in the comparison formula. Quadrature values are not interval evidence.
energies=[]
for m in [2.5,3.]:
    for order in [64,128]:
        row=weighted_diagnostic(GaussianAngular(),m,inverse_order=order,radial_order=20,z0=-6,z1=5,panel_width=.5,angles=32)
        energies.append(row)
        if order==128:assert abs(row['identity_defect'])<3e-7,row
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',manufactured_inverse=rows,exact_quotient=quotients,manufactured_energy=energies,
         scope='Manufactured tests of the independent log Green inverse and weighted evaluation. Finite quadrature only; no candidate claim.')
p=Path('research/angular_log_inverse/verification');p.mkdir(parents=True,exist_ok=True)
(p/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

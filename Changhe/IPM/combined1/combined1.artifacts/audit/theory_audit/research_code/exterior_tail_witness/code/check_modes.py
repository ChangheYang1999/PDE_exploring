"""Independent symbolic checks of Poisson signs and resonant/nonresonant energies."""
from pathlib import Path
import json
import sympy as s
r=s.symbols('r',positive=True)
rows=[]
for n,sigma in [(1,s.Rational(1)),(3,s.Rational(1,2)),(1,s.Rational(2))]:
    v=(r**(-sigma)-r**(-n))/(n*n-sigma*sigma) if sigma!=n else r**(-n)*s.log(r)/(2*n)
    eq=s.simplify(-s.diff(v,r,2)-s.diff(v,r)/r+n*n*v/r**2-r**(-2-sigma))
    energy=s.integrate((s.diff(v,r)**2+n*n*v*v/r**2)*r,(r,1,s.oo))
    expected=1/(2*sigma*(n+sigma)**2)
    assert eq==0 and s.simplify(energy-expected)==0
    assert v.subs(r,1)==0
    rows.append({'n':n,'sigma':str(sigma),'poisson_defect':str(eq),
                 'energy_divided_by_pi':str(energy),'expected':str(expected)})
Path(__file__).resolve().parents[1].joinpath('verification/modes.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))

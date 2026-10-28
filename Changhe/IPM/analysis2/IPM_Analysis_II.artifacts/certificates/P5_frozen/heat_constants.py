"""Certified explicit conversion from the heat norm to ordinary Holder seminorm."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import sympy as s
import json
ctx.prec=384
z,v=s.symbols('z v',positive=True)
# Delta(r^v exp(-r^2) sum_j a_j r^(2j)) is tracked exactly as a Laurent polynomial.
def laplace(poly):
    out={}
    for j,c in poly.items():
        power=v+2*j
        for k,term in [(j-1,power**2*c),(j,-4*(power+1)*c),(j+1,4*c)]:
            out[k]=s.expand(out.get(k,0)+term)
    return out
m={0:s.Integer(1)}
lm=laplace(m);llm=laplace(lm)
w=dict(m)
for j,c in lm.items():w[j]=s.expand(w.get(j,0)-2*c)
for j,c in llm.items():w[j]=s.expand(w.get(j,0)+c)
assert set(w)==set(range(-2,3))
# Independently check symbolic radial differentiation.
r=s.symbols('r',positive=True)
f=r**v*s.exp(-r*r)
d=lambda u:s.diff(u,r,2)+s.diff(u,r)/r
assert s.simplify((f-2*d(f)+d(d(f)))/(r**v*s.exp(-r*r))-sum(c*r**(2*j) for j,c in w.items()))==0

def aa(x):
    x=Q(str(x));return arb(x.numerator)/arb(x.denominator)
base=Path(__file__).resolve().parents[2]
records=[]
for state in [88,131]:
    params=json.loads((base/f'source_audit/state{state:03d}_exact.json').read_text())['exact_parameters']
    sigma=aa(params['sigma']);vs=s.Rational(params['sigma'])
    cs={j:aa(c.subs(v,vs)) for j,c in w.items()}
    # Radial integral I = integral_0^infty r |(1-Delta)^2 m(r)|^2 dr.
    # integral r^(2sigma+2j+2k+1) exp(-2r^2) dr
    #     = Gamma(sigma+j+k+1)/(2*2^(sigma+j+k+1)).
    I=arb(0)
    for j,c in cs.items():
        for k,dv in cs.items():
            t=sigma+j+k+1
            I+=c*dv*t.gamma()/(2*arb(2)**t)
    assert I>0
    # Plancherel: ||(1+|x|^2)^2 k||_2^2 = I/(2 pi).
    for alpha_q in [Q(1,4),Q(1,2),Q(3,4)]:
        alpha=aa(alpha_q);rr=sigma-alpha
        A=((alpha+1).gamma()*(3-alpha).gamma()*I/12).sqrt()
        Cr=(((rr+1)**(rr+1))/(arb.pi()*rr**rr)).sqrt()
        B=(4/alpha+2*Cr/(1-alpha))/(sigma/2).gamma()
        ordinary=A*B/(1-alpha)
        safe=int(float(ordinary))+1
        assert ordinary<arb(safe)
        rec={'state':state,'sigma_exact':params['sigma'],'alpha':str(alpha_q),'radial_integral_I':I.str(90),'A_upper':A.str(70),'B':B.str(70),'heat_inverse_constant':str(1/(1-alpha_q)),'ordinary_Holder_inverse_upper':ordinary.str(70),'safe_ordinary_integer':safe}
        records.append(rec)
        print(state,alpha_q,'A',A.str(12),'B',B.str(12),'ordinary',ordinary.str(12),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'formula':'N_heat inverse <=1/(1-alpha), ordinary seminorm inverse <= A_upper*B/(1-alpha)','radial_multiplier_coefficients':{str(j):str(c) for j,c in w.items()},'records':records,'scope':'Certified sufficient constants for principal frozen L0 on the stated little Holder completion. Not a full normalized profile inverse.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')

import sympy as S,json
from pathlib import Path
r,v,q,j=S.symbols('r v q j',positive=True)
A=(j-1)/q
F=r**(1-q)*v**j/(q-1)
Ds=lambda h:-S.diff(h,r)
J=1+Ds(S.diff(F,v));a=(A*(-r+S.diff(F,v))-v*S.diff(F,v,2))/J
b=J*v+Ds(Ds(F))*a;y=v+Ds(F)
checks={'all_j_inner_a':str(S.simplify(a+A*r)),'all_j_inner_b':str(S.simplify(b-y)),
 'fifth_axis_second_s':str(S.diff(-120*r**(-q),r,2))}
assert checks['all_j_inner_a']=='0' and checks['all_j_inner_b']=='0'
assert S.simplify(S.diff(-120*r**(-q),r,2)+120*q*(q+1)*r**(-q-2))==0
# The q=1 primitive is a separate prospective extension, not the v2 draft.
Fl=-S.log(r)*v**j
Jl=1+Ds(S.diff(Fl,v));Al=j-1
al=S.simplify((Al*(-r+S.diff(Fl,v))-v*S.diff(Fl,v,2))/Jl)
bl=S.simplify(Jl*v+Ds(Ds(Fl))*al);yl=v+Ds(Fl)
checks['logarithmic_a_minus_expected']=str(S.simplify(al+Al*r/Jl))
checks['logarithmic_b_minus_expected']=str(S.simplify(bl-yl-Al*j*r**(-2)*v**(2*j-1)/Jl))
assert checks['logarithmic_a_minus_expected']=='0' and checks['logarithmic_b_minus_expected']=='0'
Path(__file__).resolve().parents[1].joinpath('verification','higher_identities.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))

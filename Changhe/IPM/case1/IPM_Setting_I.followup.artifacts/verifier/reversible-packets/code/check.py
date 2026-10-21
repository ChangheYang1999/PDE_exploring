from pathlib import Path
import sympy as S,json
from datetime import datetime,timezone
s,v,A,g,d,sn=S.symbols('s v A g d sn', real=True)
F=S.Function('F')(s,v);J=1+S.diff(F,s,v);Fs2=S.diff(F,s,2);Fv2=S.diff(F,v,2)
Ds=lambda z:S.diff(z,s)-Fs2/J*S.diff(z,v)
Dy=lambda z:S.diff(z,v)/J
u=s+S.diff(F,v);a=(A*u-v*Fv2)/J;b=J*v+Fs2*a
expr={
 'area':Ds(u)*Dy(v)-Dy(u)*Ds(v)-1,
 'transport':a*Ds(g*v)+b*Dy(g*v)-g*v,
 'pullback_fast':a*Ds(u)+b*Dy(u)-A*u,
 'divergence':Ds(a)+Dy(b)-A-1,
}
checks={k:S.simplify(z)==0 for k,z in expr.items()}
Jc=1+5*d*v**4;Dc=lambda z:S.diff(z,v)/Jc
ac=A*s+A*sn*(1/Jc-1);bc=Jc*v;fc=g*v
fd=[fc]
for _ in range(5):fd.append(S.factor(Dc(fd[-1])))
checks['fifth_axis']=S.simplify(fd[5].subs(v,0)+120*g*d)==0
checks['curl_core']=S.simplify(-Dc(ac).subs(s,sn)-20*A*sn*d*v**3/Jc**3)==0
Y,de=S.symbols('Y de');test=Y-de*Y**5
checks['inverse_first_variation']=S.diff(test,Y,4)==-120*de*Y
out={'date':datetime.now(timezone.utc).isoformat(),'checks':checks,'fourth_derivative':str(fd[4]),'fifth_axis':str(fd[5].subs(v,0)),'scope':'Symbolic identities only; regularity, accumulation and superpolynomial growth proved in PROOF.md.'}
assert all(checks.values())
root=Path(__file__).resolve().parents[1];(root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

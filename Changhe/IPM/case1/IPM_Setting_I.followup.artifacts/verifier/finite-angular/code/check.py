"""Independent finite angular highest-mode and radial ODE checks."""
import sympy as S
import json
from pathlib import Path
r,t,z=S.symbols('r t z',positive=True)
a,b,c,H,Hp,T,Tp=S.symbols('a b c H Hp T Tp',nonzero=True,real=True)
rows=[]
for N in (1,3,5,7,9):
    left=S.cos(t)*Hp*S.sin(N*t)-S.sin(t)/r*N*H*S.cos(N*t)
    right=(Hp+N*H/r)*S.sin((N-1)*t)/2+(Hp-N*H/r)*S.sin((N+1)*t)/2
    assert S.expand((left-right).rewrite(S.exp))==0
    angular=-(N+1)*T*Hp*S.cos((N+1)*t)*S.sin(N*t)+Tp*N*H*S.sin((N+1)*t)*S.cos(N*t)
    expanded=S.expand(angular.rewrite(S.exp)).subs(S.exp(S.I*t),z)
    coefficient=S.simplify(2*S.I*S.expand(expanded).coeff(z,2*N+1))
    assert S.simplify(coefficient-(N*H*Tp-(N+1)*T*Hp)/2)==0
    v=a*r+b/r; hn=v**N; tn=-v**(N+1)/(4*(N+1)*a)
    assert S.simplify(S.diff(tn,r)+(N+1)*tn/r+hn/2)==0
    assert S.simplify(N*hn*S.diff(tn,r)-(N+1)*tn*S.diff(hn,r))==0
    source=(S.diff(hn,r)-N*hn/r)/2
    poisson=-(S.diff(tn,r,2)+S.diff(tn,r)/r-(N+1)**2*tn/r**2)-source
    assert S.simplify(poisson)==0
    b1=S.symbols('b1'); h0=r**N*(1+b1*r*r)
    t0=-r**(N+1)/S.Integer(4*(N+1))-b1*r**(N+3)/S.Integer(4*(N+2))
    high=S.expand((N*h0*S.diff(t0,r)-(N+1)*t0*S.diff(h0,r))/(2*r))
    leading=high.coeff(r,2*N+1)
    assert leading==b1/S.Integer(2*(N+2))
    rows.append({'N':N,'highest_coefficient':str(coefficient),'gaussian_jet_coefficient':str(leading.subs(b1,-1)),'all_defects':'exact zero'})
out={'rows':rows,'status':'all exact symbolic assertions passed'}
p=Path(__file__).resolve().parents[1]/'verification'/'identities.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

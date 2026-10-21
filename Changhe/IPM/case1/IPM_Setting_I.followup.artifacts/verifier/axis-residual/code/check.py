from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
x=s.symbols('x',positive=True);A=s.Integer(4);beta=s.Rational(1,2)
w=-A*x*(1-x*x)/(1+x*x);g=x*x/(1+x*x)
H=x**s.Rational(13,2)/(1+x*x)**3/s.sqrt(1-x*x)
Q=(s.diff(g,x)-s.diff(w,x,2))/(2*g**3);F=g**4*s.diff(Q,x)/3
G=s.Function('G')(x);r=w*s.diff(G,x)-(3*s.diff(w,x)-3*A-2)*G-F
chi=s.Function('chi')(x);B=s.symbols('B')
def zero(expr):
 z=s.simplify(expr);assert z==0,z;return str(z)
checks={
 'first_axis':zero(w*s.diff(g,x)-(s.diff(w,x)-A)*g),
 'H_homogeneous':zero(w*s.diff(H,x)-(3*s.diff(w,x)-3*A-2)*H),
 'residual_accounting':zero(s.diff(G/H,x)-(F+r)/(w*H)),
 'cutoff_residual':zero(w*s.diff(-B*H*chi,x)-(3*s.diff(w,x)-3*A-2)*(-B*H*chi)+B*w*H*s.diff(chi,x)),
 'explicit_F':zero(F+x*x*((6*A+3)*x*x+5-30*A)/(3*(1+x*x)**4)),
}
S=6*A*(4*A-3)/(8*A-1);assert S==s.Rational(312,31)
assert s.simplify(1-S)==-s.Rational(281,31)
obj={'date':datetime.now(timezone.utc).isoformat(),'checks':checks,'S4':str(S),'B3_over_C4':str(1-S),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'verdict':'CONFIRMED_EXACT_ALGEBRA'}
(ROOT/'verification/check.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))

"""Symbolic local test of a stream function with only angular mode sin(2phi)."""
from pathlib import Path
import sympy as S
b,h1,g1=S.symbols('beta h1 g1',real=True)
c=2*b+2; g0=-12*h1; a0=(2*b+1)*g0/2
J1=(4*b+1)*g1; K0=2*(h1*g0-c*g1)
as_=(J1+K0)/4; at_=(J1-K0)/2
rs=S.factor(-2*(b+2)*as_+h1*a0)
rt=S.factor(2*(3*b+2)*at_-5*h1*a0)
g1val=S.solve(rs,g1)[0]
print('s coefficient:',rs)
print('t coefficient:',rt)
print('g1 from s coefficient:',g1val)
print('remaining t coefficient:',S.factor(rt.subs(g1,g1val)))
print('nonzero h1 necessary roots:',S.solve(rt.subs(g1,g1val)/h1**2,b))

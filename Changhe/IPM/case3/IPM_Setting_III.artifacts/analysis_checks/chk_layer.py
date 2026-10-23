# Formal inner layer near the vertical axis for (H_c): symbolic reduction and 2F2 representation checks.
import sympy as sp
x,y,z,p,K,c=sp.symbols('x y z p K c',positive=True)
al=(p+1)/2; q=al*p+p-1; qq=al*p
b=sp.Function('b'); v=sp.Function('v')
Z=x/y**al
u=y**q*b(Z); w=y**qq*v(Z)
E1=sp.simplify(((c*x*sp.diff(u,x)+c*y*sp.diff(u,y)-u)+p*K*y**(p-1)*w)/y**q)
E2=sp.simplify((sp.diff(w,y,2)+sp.diff(u,x,2))/y**(q-2*al))
E1=sp.simplify(E1.subs(x,z*y**al)); E2=sp.simplify(E2.subs(x,z*y**al))
print('E1:',sp.simplify(E1.subs(c,1/p)))
print('E2:',sp.simplify(sp.expand(E2)))

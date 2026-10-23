import sympy as sp, numpy as np
exec(open('e2_integer.py').read().split("num,den")[0])
num,den=sp.fraction(sp.together(sp.simplify(pp)))
Pm=sp.Poly(sp.expand(num),mu); coef=[sp.lambdify((n,nu),c) for c in Pm.all_coeffs()]
for nn in (1,2,3,5):
  out=[]
  for vv in list(range(1,13))+[20,40,80,160]:
    rts=[z.real for z in np.roots([int(c(nn,vv)) for c in coef]) if abs(z.imag)<1e-9 and z.real>vv+nn]
    out.append((vv,[round(x,4) for x in rts]))
  print('n=',nn,out)
# top homogeneous form
tot=sp.Poly(sp.expand(num),n,nu,mu)
top=sum(c*n**e[0]*nu**e[1]*mu**e[2] for e,c in zip(tot.monoms(),tot.coeffs()) if sum(e)==6)
print('top form factor:',sp.factor(top))
print('num at mu=nu+n:',sp.factor(sp.expand(num.subs(mu,nu+n))))

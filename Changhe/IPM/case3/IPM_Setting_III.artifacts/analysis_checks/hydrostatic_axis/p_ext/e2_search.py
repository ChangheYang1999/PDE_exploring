# integer solutions of num(n,nu,mu)=0 with n>=1, nu>=1, mu>=nu+n+1 (e=2 survivors of the lemma)
import sympy as sp, numpy as np, sys, time
exec(open('e2_integer.py').read().split("num,den")[0])
num,den=sp.fraction(sp.together(sp.simplify(pp)))
N=int(sys.argv[1]); V=int(sys.argv[2])
Pm=sp.Poly(sp.expand(num),mu)
coef=[sp.lambdify((n,nu),c) for c in Pm.all_coeffs()]
f=sp.lambdify((n,nu,mu),sp.expand(num))
cnt=0; hits=[]; t0=time.time()
for nn in range(1,N+1):
  for vv in range(1,V+1):
    cs=[int(c(nn,vv)) for c in coef]
    rts=np.roots(cs)
    for z in rts:
      if abs(z.imag)<1e-6*max(1,abs(z)) and z.real>vv+nn+0.5:
        for k in (int(np.floor(z.real)),int(np.ceil(z.real))):
          if sum(c*k**(len(cs)-1-i) for i,c in enumerate(cs))==0: hits.append((nn,vv,k))
        cnt+=1
print('real roots mu>nu+n+1/2 found:',cnt,'integer solutions:',hits,'time %.1f'%(time.time()-t0))

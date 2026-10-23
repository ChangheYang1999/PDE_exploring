# Case II (exceptional P=(m+2)/2): g(u)=m(1+u)^e(u-us)/(u*prod(u-u_k)), k=1..e+1, us=-1/(m+2).
# residues A_0 (at 0), A_k must be positive (mu_0=A_0 odd int, mu_k=A_k/2 int); extra (X): sum_k (1+u_k)/(us-u_k)=0.
# Search all complex solutions of {A_k = given} ... here: numeric exploration with e=2: u = r (real), z, conj(z).
import numpy as np
from scipy.optimize import least_squares
rng=np.random.default_rng(1)
def res(us,m,e,uk):
    uk=np.asarray(uk,complex); A=[]
    allp=np.concatenate([[0],uk])
    for j,p in enumerate(allp):
        oth=np.delete(allp,j)
        A.append(m*(1+p)**e*(p-us)/np.prod(p-oth))
    return np.array(A)
def X(us,uk): return np.sum((1+uk)/(us-uk))
for m in [9,11,13,15,21,31,51]:
    e=2; us=-1/(m+2); best=[]
    for trial in range(4000):
        x0=[-abs(rng.normal())*3-0.01, rng.normal()*2, abs(rng.normal())*2+0.01]
        def F(p):
            r,a,b=p; uk=np.array([r,a+1j*b,a-1j*b])
            A=res(us,m,e,uk); x=X(us,uk)
            return [A[2].imag, x.real]
        try: s=least_squares(F,x0,xtol=1e-14,ftol=1e-14)
        except Exception: continue
        if np.max(np.abs(s.fun))<1e-10:
            r,a,b=s.x; uk=np.array([r,a+1j*b,a-1j*b]); A=res(us,m,e,uk)
            if abs(b)>1e-6 and np.all(A.real>0): best.append((A[0].real,A[1].real,A[2].real,r,a,b))
    if best:
        B=np.array(best); print(m,len(B),'A0 range',B[:,0].min(),B[:,0].max(),'A_r range',B[:,1].min(),B[:,1].max(),'A_z',B[:,2].min(),B[:,2].max())
    else: print(m,'no positive solutions found')

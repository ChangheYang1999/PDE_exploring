"""Independent direct real trigonometric and binomial identity tests."""
import math,json,time
from fractions import Fraction as F
import numpy as np
import kernels

def plus(a,b):
    z=a.copy()
    for key,v in b.items():z[key]=z.get(key,F(0))+v
    return {k:v for k,v in z.items() if v}
def scale(a,s):return {k:v*s for k,v in a.items() if v*s}
def dt(a,shift=0):
    z=scale(a,shift)
    for (q,l),v in a.items():
        if l:z[(q,l-1)]=z.get((q,l-1),F(0))+l*v
    return {k:v for k,v in z.items() if v}
def mul(a,b,order):
    # order: sincos or cossin; negative sine frequencies are folded exactly.
    z={}
    for (m,i),v in a.items():
        for (n,j),w in b.items():
            for q in (m+n,m-n if order=='sincos' else n-m):
                if q:
                    key=abs(q),i+j;z[key]=z.get(key,F(0))+(1 if q>0 else -1)*v*w/2
    return {k:v for k,v in z.items() if v}
def freq(a):return {(q,l):q*v for (q,l),v in a.items()}
def array(a,rows,cols):
    z=np.zeros((rows,cols),dtype=np.float64)
    for (q,l),v in a.items():z[q-1,l]=float(v)
    return z

def main():
    start=time.monotonic();counts={}
    for x,y in [([0],[3,-4]),([-7,3],[4,-9,2]),([1<<200,-(1<<180),1],[-3,7,-5]),([1,0,0,-1],[1,0,2])]:
        z,r=kernels.exact_product(x,y);direct=[sum(x[i]*y[k-i] for i in range(len(x)) if 0<=k-i<len(y)) for k in range(len(x)+len(y)-1)];assert z==direct
    counts['manufactured_CRT_products']=4
    T=np.zeros((8,260),dtype=np.float64)
    for l,m,v in [(0,0,7),(1,1,-3),(3,2,2),(2,259,-5)]:T[l,m]=v
    p={(1,0):F(3),(1,2):F(-2),(135,1):F(4),(261,3):F(-1)};r={(1,1):F(2),(135,2):F(-3),(261,0):F(5)}
    P=array(p,261,13);R=array(r,261,13)
    arrays={'P_mid':P,'R_mid':R,'T_mid':T,'P_rad':P*0,'R_rad':R*0,'T_rad':T*0,'P_rem':np.zeros(261),'R_rem':np.zeros(261)}
    model=kernels.build(arrays)
    # Independently form H by multiplying sin(theta)+sin(3theta) with cos(2mtheta).
    factor={(2*m,l):F(float(T[l,m])) for l,m in zip(*np.nonzero(T))}
    H=mul({(1,0):F(1,4),(3,0):F(1,4)},factor,'sincos');Hp=[H]
    for _ in range(3):Hp.append(dt(Hp[-1],3))
    P={(2*n,l):v for (n,l),v in p.items()};R={(2*n,l):v for (n,l),v in r.items()}
    Ap=[P,plus(scale(P,-2),freq(R))];Bp=[R,plus(freq(P),scale(R,-2))]
    Ap.append(plus(scale(Ap[1],-2),freq(Bp[1])));Bp.append(plus(freq(Ap[1]),scale(Bp[1],-2)))
    # partial_x(r^3 H)/r^2 = cos(theta)(D+3)H - sin(theta)partial_theta H.
    forcing=plus(mul({(1,0):F(1)},Hp[1],'cossin'),scale(mul({(1,0):F(1)},freq(H),'sincos'),-1))
    V=[]
    for degree in range(3):
        z=plus(scale(Hp[degree+1],F(kernels.N,kernels.D)),scale(Hp[degree],-1))
        for l in range(degree+1):
            term=plus(scale(mul(Ap[l],Hp[degree-l+1],'cossin'),-1),mul(Bp[l],freq(Hp[degree-l]),'sincos'))
            z=plus(z,scale(term,math.comb(degree,l)))
        V.append(z)
    W=[{},scale(mul(forcing,freq(Hp[0]),'sincos'),-1)]
    W.append(plus(plus(mul(freq(forcing),Hp[1],'cossin'),scale(mul(forcing,freq(Hp[1]),'sincos'),-2)),scale(mul(dt(forcing),freq(Hp[0]),'sincos'),-1)))
    count=0
    for name,direct,ex,den,degree in [('V',V,model['eV'],kernels.D,19),('W',W,model['eW'],1,14)]:
        for p in range(3):
            for j in range(522):
                for l in range(degree+1):
                    got=-2*F(model[name][p][j][l])*F(2)**ex/den;target=direct[p].get((2*j+1,l),F(0));assert got==target,(name,p,j,l,got,target);count+=1
    counts['all_manufactured_real_Fourier_binomial_coefficients']=count
    counts['actual_linear_identity_checks']=kernels.validate_actual_linear_maps(model)
    # Exhaustive algebraic support map checks, independent of actual coefficient values.
    mapping_checks=0
    for ra,rb,ja,jb,rs,jo in [(12,7,2,2,20,5),(7,7,0,0,15,1),(7,7,1,1,15,3)]:
        assert ra+rb<rs and ja+jb<jo
        for m in range(1044):
            for l in range(ra+rb+1):
                for p in range(ja+jb+1):
                    index=m*rs*jo+p*rs+l;mm,tail=divmod(index,rs*jo);pp,ll=divmod(tail,rs);assert (mm,pp,ll)==(m,p,l);mapping_checks+=1
        for p in range(min(2,ja+jb)+1):
            for l in range(p+1):assert F(math.factorial(p),math.factorial(l)*math.factorial(p-l))==math.comb(p,l)
    counts['injective_support_coordinates']=mapping_checks
    assert model['H'][-1]==[0]*8
    print(json.dumps({'status':'PASS_MANUFACTURED_EXACT_FOURIER_JETS_AND_CRT','counts':counts,'seconds':time.monotonic()-start}),flush=True)
if __name__=='__main__':main()

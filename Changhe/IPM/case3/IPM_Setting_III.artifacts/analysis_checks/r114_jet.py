# Independent check of result114 statement 1 (N = 0): c = 3, a = 24, prescribed T = M (1+z)^(-eps), g = -T-dot,
# unknown f, k (k = O(z^2)) and H; solve E1 = E3 = 0 order by order in z; report the order-4 compatibility.
import sympy as sp
z,eps,H=sp.symbols('z eps H')
c=sp.Integer(3); D=c-1; a=sp.Integer(24); M=a/4-D
N=6
dot=lambda F: sp.expand(2*z*sp.diff(F,z))
Tser=sp.series(M*(1+z)**(-eps),z,0,N).removeO()
g=sp.expand(-dot(Tser))
fs=sp.symbols('f1:%d'%N); ks=sp.symbols('k2:%d'%N)
f=a+sum(fs[j-1]*z**j for j in range(1,N))
k=sum(ks[j-2]*z**j for j in range(2,N))
def coef(F,j): return sp.expand(F).coeff(z,j)
J=a/4+sum(coef(f,j)/(2*j+4)*z**j for j in range(1,N))
K=sum(coef(g,j)/(2*j+6)*z**j for j in range(1,N))
L=sum(coef(k,j)/(2*j+8)*z**j for j in range(2,N))
S=H*z+sum(-coef(k,j)/(2*j-2)*z**j for j in range(2,N))
T=Tser
u=(T-J)/2; B=-u-K+S; C=K-sp.Rational(3,2)*L-S
F1=(D+T)*f-f**2/4+f*g/2+(-J+2*K+4*S-2*T)*g+(-4*K+6*L-6*S)*k+g*k/2
F3=(J+2*S)*f-f**2/4-f*g/2+(D+3*L)*g+(-2*J-3*T+f+g/2)*k
E1=sp.expand((c+u)*dot(f)+B*dot(g)+C*dot(k)+F1)
E3=sp.expand(B*dot(f)+(c-sp.Rational(3,2)*L)*dot(g)-u*dot(k)+F3)
def trunc(E,n): return sum(coef(E,j)*z**j for j in range(n+1))
E1=trunc(E1,5); E3=trunc(E3,5)
print('order0',sp.simplify(coef(E1,0)),sp.simplify(coef(E3,0)))
sol={}
# order 1: unknowns f1, H
s1=sp.solve([coef(E1,1),coef(E3,1)],[fs[0],H],dict=True)[0]; sol.update(s1)
print('H =',sp.factor(sol[H]),' f1 =',sp.factor(sol[fs[0]]))
for j in range(2,5):
    e1=sp.expand(coef(E1,j).subs(sol)); e3=sp.expand(coef(E3,j).subs(sol))
    unk=[fs[j-1],ks[j-2]]
    print('order',j,'coeffs k in E1:',sp.factor(sp.diff(e1,ks[j-2])),' k in E3:',sp.factor(sp.diff(e3,ks[j-2])),' f in E1:',sp.factor(sp.diff(e1,fs[j-1])))
    if j<4:
        s=sp.solve([e1,e3],unk,dict=True)[0]; sol.update(s)
        print('  k%d ='%j,sp.factor(sol[ks[j-2]]))
    else:
        sf=sp.solve(e1,fs[j-1])[0]; sol[fs[j-1]]=sf
        comp=sp.factor(sp.expand(e3.subs(sol)))
        print('  compat (E3 order 4, k4 coefficient %s):'%sp.factor(sp.diff(e3,ks[j-2]).subs(sol)),comp)
        cc=sp.Poly(sp.expand(comp*225/32/eps),eps); print('  225/(32 eps) * compat =',cc.as_expr())
        print('  value at eps=1/10:',sp.N(comp.subs(eps,sp.Rational(1,10))), ' roots:',[sp.N(r) for r in sp.Poly(sp.expand(comp/eps),eps).nroots()])

# Lead check of a referee answer, section 4 (R12 data, 1 < A < 2). In z = x/L, with kappa = A/L^2,
#   L^(4+beta) B_3 = -f.p. int_0^1 R_z dz,  R_z = z^(-7-beta) S(z),
#   S(z) = N(z) (1+z^2)^4 (1-z^2)^(beta-1)/(-2A),  N = -[(G'+k Wm'')G' - (G''+k Wm''')G/3],
# from B_3 = -f.p. int_0^L F_3/(w H_3) dx (axis hierarchy of 6.3.1 (a)), H_3 = A^beta g^(3+beta)|w|^(-beta), g = L^2 G, w = -A L Wm.
# Claim: this is linear in kappa and vanishes at L^2 = S_A = 6A(4A-3)/(8A-1).
import sympy as sp, mpmath as mp
mp.mp.dps=30
z,k=sp.symbols('z kappa')
G=z**2/(1+z**2); Wm=z*(1-z**2)/(1+z**2)
d=lambda f,n=1: sp.diff(f,z,n)
N=sp.together(-((d(G)+k*d(Wm,2))*d(G)-(d(G,2)+k*d(Wm,3))*G/3))
def J(A,kap,M=90):
    beta=sp.Rational(2)/A
    Sz=sp.simplify(N.subs(k,kap))*(1+z**2)**4/(-2*A)
    ser=sp.series(Sz*(1-z**2)**(beta-1),z,0,M).removeO()
    z0=mp.mpf(1)/3
    b=mp.mpf(beta.p)/beta.q
    fp=sum(mp.mpf(sp.Rational(ser.coeff(z,n)).p)/sp.Rational(ser.coeff(z,n)).q * z0**(n-6-b)/(n-6-b) for n in range(M))
    f=sp.lambdify(z,Sz,'mpmath')
    tail=mp.quad(lambda t: f(t)*(1-t**2)**(b-1)*t**(-7-b),[z0,0.7,1])
    return -(fp+tail)
for A in (sp.Rational(3,2),sp.Rational(5,4),sp.Rational(9,5)):
    SA=6*A*(4*A-3)/(8*A-1); k0=A/SA
    vals=[J(A,kap) for kap in (k0,k0*sp.Rational(1,2),k0*2,sp.Integer(0))]
    # linearity: J(k) = J(0)(1 - k/k0)
    print('A',A,'S_A',SA,' J(k0) =',mp.nstr(vals[0],6),' J(k0/2)/J(0) =',mp.nstr(vals[1]/vals[3],15),
          ' J(2k0)/J(0) =',mp.nstr(vals[2]/vals[3],15),' J(0) =',mp.nstr(vals[3],12))

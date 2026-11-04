# The global pressure gap with continuous pressure

## 1. Exact statement

Let 0<p<3/2, p!=1/2, c=1/(p+1), and omega be any finite real number. Put Jx=e3 cross x, F_s x=exp(cs)exp(-omega sJ)x. On G=R3 minus{0}, assume V is C1, P is continuous,

    div V=0, -Delta P=tr((DV)^2) in distributions,
    V(F_s x)=exp(-(1-c)s)exp(-omega sJ)V(x),
    P(F_s x)=exp(-2(1-c)s)P(x).

If P<=-|V|^2/(2p) throughout G, then V=P=0. The submitted LIT249 refinement has1<p<3/2, which is included. No helicity, rank, normalized curl, momentum, k=0, or singular-origin distributional equation is assumed. The condition is global on punctured space, including every direction. The earlier exact p=1/2 countermodel in A1607 also has continuous pressure and remains an exception.

## 2. Tangency and pressure equality require only continuity

Let T=V tensor V+P I. Local mollification of divergence-free V gives div div T=0. Put, with unit-sphere area integrals,

    A=integral |V|^2, B=integral(V.n)^2, C=integral P,
    N=B+C, M=A+3C.

Twisted homogeneity and rotational invariance give degree-2p angular means. Testing against a smooth compact radial function supported away from0 gives

    0=integral r^(2-2p)[N psi''+(M-N)psi'/r]dr
     =[M-(3-2p)N]integral r^(1-2p)psi'dr.

The final functional is not identically zero because p!=1/2. Therefore A+2pC=(3-2p)B. The pressure inequality makes its left side nonpositive; 3-2p>0 makes its right side nonnegative. Both vanish. Continuity, followed by homogeneity, yields

    V.x=0, P=-E/(2p), E=|V|^2, throughout G.             (1)

In particular E and P are C1. No C2 regularity is inferred. If V is nonzero, e=E restricted to the sphere attains a positive global maximum at n0.

## 3. The Jacobian calculation still is pointwise

Write v=V restricted to the sphere, D its intrinsic covariant derivative, and a=partial_r V at radius1. Tangency gives the full Cartesian Jacobian in the normal/tangent frame as

    DV=[0,-v^T; a,D], tr D=0,
    tr((DV)^2)=-2v.a+tr(D^2).                            (2)

Put tau=omega/c and Z(n)=Jn. Homogeneity gives E(rn)=r^(-2p)e(exp(tau log(r)J)n), so 2v.a=-2pe+tau Ze. At n0, grad e=2D^T v=0 and v!=0. Choosing the first tangent vector as v/|v|, D has first row zero, and its zero trace makes the remaining diagonal entry zero. Thus tr(D^2)=0. Also Ze=0. Consequently

    tr((DV)^2)(n0)=2p e(n0).                             (3)

All quantities here exist and are continuous under C1 regularity. No second velocity derivative or differentiated frame is used.

## 4. Angular distribution equation and a weak barrier

For smooth angular e the scalar Laplace formula is

    Delta E at r=1
       =[Delta_S+tau^2Z^2+tau(1-4p)Z+2p(2p-1)]e.

It remains valid distributionally for C1 e: approximate e smoothly on the sphere, extend by the exact homogeneous formula, and pass to distributions on compact annuli. From(1) and Poisson, Delta E=2p tr((DV)^2). This right side is continuous and has twisted degree-2p-2, by differentiating the homogeneity of V.

In annular coordinates x=r exp(-tau log(r)J)n, both sides have the same radial factor r^(-2p-2). Testing with a compact radial factor with nonzero integral therefore yields the angular distribution equation

    L0 e=f,
    L0=Delta_S+tau^2Z^2,
    f=2p tr((DV)^2)|S-2p(2p-1)e-tau(1-4p)Ze.           (4)

This is a distributional reduction, not a trace of a distribution at r=1. The function f is continuous. Since Z is a divergence-free Killing field,

    L0=div_S[(I+tau^2 Z tensor Z)grad_S].                (5)

Its coefficient matrix is smooth and positive definite, with smallest eigenvalue at least1. Equations(3)-(4) give f(n0)=2p e(n0)>0.

Choose coordinates z centered at n0 and a small disk B_r on which f>=delta>0. Let h=|z|^2. Its image under L0 is bounded on the closed disk. Choose epsilon>0 so that epsilon sup|L0h|<delta/2. Put w=e-epsilon h and M=e(n0)-epsilon r^2. On the disk boundary w<=M, whereas w(0)>M. Moreover L0w>=delta/2 distributionally. The nonnegative nonzero function phi=(w-M)_+ belongs to H1_0(B_r). By smooth approximation it is an admissible test. The weak equation gives

    -integral[|grad phi|^2+tau^2|Zphi|^2]
       =integral(f-epsilon L0h)phi>0,

a contradiction. Integrals use the sphere metric and area density. This proves V=0; (1) gives P=0. It avoids assuming that a continuous right side produces classical second derivatives.

## 5. Ratio scope, exponent extension and verification

For b=2p/(p+1), the global pressure premise is H=E/2-P>=E/b. Under the additional global sign S=P-E/2<=0 and strict S<0 wherever V!=0, any nonzero admissible pair must violate it at a nonzero point and hence have E/(-S)>b there. These sign and domain premises remain part of the ratio claim.

Every step above only needs p>0,3-2p>0 and p!=1/2. Thus A1606's optional exponent extension persists at continuous-pressure regularity. The exception A1607 is not a full Euler profile and lies outside the campaign interval.

All six sections of the revised LIT249 source and all five independent proof sections were read. The local weak test is complete and retains every rotation term. The pressure continuity revision is confirmed; it does not provide the global inequality for general tails or settle a local common-flat ratio gap. Comparison is through the existing configured model working files, with provider runtime unattested. No computation, external regularity theorem or formal build is used.

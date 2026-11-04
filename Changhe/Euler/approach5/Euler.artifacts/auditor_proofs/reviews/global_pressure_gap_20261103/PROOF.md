# A global pressure bound and the tangential speed maximum

## 1. Exact theorem

Let 1<p<3/2, c=1/(p+1), omega be any finite real number, Jx=e3 cross x, F_s x=exp(cs)exp(-omega sJ)x. On G=R3 minus{0}, suppose V in C1(G;R3), P in C2(G) satisfy

    div V=0, -Delta P=tr((DV)²),
    V(F_s x)=exp(-(1-c)s)exp(-omega sJ)V(x),
    P(F_s x)=exp(-2(1-c)s)P(x)

for every x and real s. The matrix trace is tr((DV)²), not |DV|². If P<=-|V|²/(2p) throughout G, then V=P=0. No helicity, vorticity rank, normalized curl relation, pressure-transport law or full momentum equation is assumed.

With E=|V|², S=P-E/2, H=-S and b=2p/(p+1), the pressure bound is exactly H>=E/b. Thus every nonzero pair in this class violates that global bound somewhere on the unit sphere. If additionally S<=0 everywhere and S<0 wherever V!=0, the violation occurs at a nonzero velocity point and reads E/(-S)>b. Without these sign assumptions a finite ratio conclusion is not asserted.

## 2. Spherical identity from compact annular tests

Put T=V tensor V+P I. Divergence freedom implies div div(V tensor V)=tr((DV)²) distributionally; locally mollify V and pass with its first derivatives to justify this at C1 regularity. Hence div div T=0 on G.

Write, on the unit sphere with its usual area measure,

    A=integral E, B=integral(V.n)², C=integral P,
    N=B+C, M=A+3C.

The angular means on a sphere of radius r scale by r^(-2p); rotations preserve surface area and scalar products. For a smooth radial test psi supported in an annulus, D²psi=psi'' n tensor n+(psi'/r)(I-n tensor n). Therefore

    0=integral_0^infinity r^(2-2p)[N psi''+(M-N)psi'/r]dr
      =[M-(3-2p)N]integral_0^infinity r^(1-2p)psi'dr.

The last functional is not identically zero, since 1-2p!=0. Thus

    A+2p C=(3-2p)B.                                     (1)

All integrations are compactly supported away from the singular origin. No stress-divergence equation, zero-origin flux or far-field boundary term is assumed. This independently reproduces A1508.

## 3. The inequality forces exact tangency and scalar regularity

The pointwise pressure bound gives A+2pC<=0. Since 3-2p>0 and B>=0, (1) forces B=0 and A+2pC=0. Continuity then gives V.n=0 everywhere on the unit sphere, and homogeneity gives V.x=0 throughout G. The continuous nonnegative function -P-E/(2p) has zero sphere integral, so

    P=-E/(2p) throughout G.                             (2)

In particular E is C2, even though V was assumed only C1. If V is nonzero, its spherical squared speed e attains a positive maximum at some n0.

## 4. The full velocity Jacobian at that maximum

Let v=V restricted to the sphere, and let D be its intrinsic covariant derivative. In an orthonormal frame with normal n followed by two tangent vectors, tangency gives the Cartesian block matrix

    DV=[0,-v^T; a,D], a=partial_r V at r=1.

The first entry is zero by radial differentiation of V.n=0. The top-right block follows from differentiating n.v=0 in tangent directions. Thus div V=0 gives tr D=0, and

    tr((DV)²)=-2v.a+tr(D²).                              (3)

Put Z(n)=Jn, tau=omega/c. Twisted homogeneity gives

    E(rn)=r^(-2p)e(exp(tau log(r)J)n),
    2v.a=partial_r E=-2p e+tau Z e at r=1.

At the positive maximum n0, 2D^T v=grad_S e=0. Choose the first tangent frame vector as v/|v|. The first row of D is then zero, and tr D=0 makes its second diagonal entry zero. Therefore D=[0,0;d,0], tr(D²)=0. Also Z e=0. Formula (3) consequently gives the exact value

    tr((DV)²)(n0)=2p e(n0).                              (4)

This calculation differentiates neither a chosen eigenframe nor V twice.

## 5. The pressure Laplacian contradicts the same maximum

Acting on the homogeneous scalar, r partial_r is -2p+tau Z. Hence at r=1,

    Delta E=[Delta_S+tau² Z²+tau(1-4p)Z+2p(2p-1)]e.       (5)

At n0, Z e=0 and both Delta_S e and Z² e are nonpositive. This follows from the negative semidefinite spherical Hessian and is also valid at the rotation poles. Thus Delta E(n0)<=2p(2p-1)e(n0). Combining the Poisson equation with (2) yields

    tr((DV)²)(n0)=Delta E(n0)/(2p)<=(2p-1)e(n0),

contrary to (4) and e(n0)>0. Hence V=0, and (2) then gives P=0. Every finite omega is covered because its quadratic contribution in (5) has the favorable sign at the maximum.

The ratio consequence in Section1 follows by the exact algebra H=E/2-P and 1/b=(p+1)/(2p). A violating point cannot have E=0 when S<=0 globally. The additional strict negative S on the nonzero set makes division legitimate there.

## 6. An optional extension and its real resonance

The same proof works for every 0<p<3/2 except p=1/2, with c=1/(p+1). Positivity of p is needed when dividing by2p, positivity of3-2p forces tangency, and p!=1/2 makes the compact radial functional nonzero. No step needs p>1. This extension lies partly outside the campaign interval and is not needed for LIT249.

The omitted p=1/2 is a genuine exception for this relaxed kinematic and Poisson class. For r=|x|, mu=x3/r, set

    p=1/2, c=2/3,
    V=r^(-3/2)Jx,
    P=-r^(-1)(1+mu²/2).

These fields are smooth on G, satisfy twisted homogeneity for every omega by axial equivariance, and are divergence free. With f=r^(-p-1), the matrix DV=fJ-(p+1)f(Jx tensor x)/r² has

    tr((DV)²)=2r^(-2p-2)[p-(p+1)mu²].

At p=1/2 this is r^(-3)(1-3mu²). Since Delta_S(mu²)=2-6mu² and the scalar radial degree -1 has zero radial Laplace coefficient, -Delta P has exactly that value. Also E=r^(-1)(1-mu²), so P+E=-(3/2)mu²/r<=0. This is a nonzero pair satisfying the pressure bound at the resonant exponent.

It is not a full similarity profile. Its linear similarity operator vanishes, but direct differentiation gives

    (V.grad)V+grad P=(3/2)x3² x/r^5,

which is nonzero off the equatorial plane. It is singular at the missing origin and has c=2/3, outside the task interval. This example tests precisely the attempted extension of the relaxed theorem to its missing exponent, not the main conjecture.

## 7. Verification and scope

All six sections of LIT249 were read and independently derived. The proof is entirely analytic: the annular distribution identity, tangency, C2 scalar recovery, pointwise two-dimensional nilpotent matrix, and rotating maximum calculation all pass. The optional extension and exact resonant model are sent back for comparison through existing configured model agents; provider runtime is unattested. No computation or formal build is used.

The pointwise pressure condition must hold on all punctured space. This result does not exclude a local common-flat neighborhood with bounded ratio, prove logarithmic ratio energy, or establish its pressure premise for an arbitrary Euler tail. Those questions and the main bare-decay arbitrary-helicity conjecture remain open. No optimality of the bound for the target class is claimed.

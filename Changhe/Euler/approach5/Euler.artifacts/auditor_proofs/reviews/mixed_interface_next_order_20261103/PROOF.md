# The specified mixed interface fails the next actual pressure equation

Status: A650 CONFIRMED after full source and independent proof postreads. The analytic incompatibility holds for every0<d<1/2; its actual-tail consequence retains c!=3/7. This is a one-germ exclusion, not a general interface theorem.

## 1. Exact statement and dependencies

Let0<d<1/2, p=1+d, sigma=1-d, c=1/(d+2), omega in R, A=cI-omega J, J(x1,x2,x3)=(-x2,x1,0), m=3p+1 and nu=cm=3-2c. On the invariant positive equatorial cone

    r=|x|>0, 0<z=x3/r<delta,

let V,P2 be exactly the analytic positive branch of A617/LIT158, recalled in Section2. Define k=(Ax).V and Z=DV V+grad P2. There is no C1 scalar p1 on this cone satisfying all three conditions

    p1(exp(sA)x)=exp(-nu s)p1(x),
    -Delta p1=2tr(DV DZ) in distributions,
    dk wedge d(p1-2V.grad P2)=0.                       (1)

This theorem assumes no symmetry of p1. Consequently A647-A648 exclude this particular pair V,P2 as the actual leading coefficients of any global C2/C1 helicity-free profile with the natural velocity and derivative bounds, for2/5<c<1/2,c!=3/7 and every omega. Uniform decay and DU=O(sqrt r) are the confirmed alternative starting bounds. A globally nonaxisymmetric tail is also excluded from containing this exact local pair.

The local assertion (1) holds at d=1/3 as well. Its application to actual tails at c=3/7 is not proved, because the actual first-pressure expansion is resonant there. This argument neither invalidates the five leading-equation countertest A617 nor excludes other local interfaces.

## 2. The actual analytic branch and its four jets

Put w=1-z^2, q=2p/d, and in the spherical orthonormal frame write

    V=r^-p(R er+f/sqrt(w) e_theta), R=f'/sigma,
    P2=r^-2p Q,
    Q=-R^q+(R^2+f^2/w)/2.                             (2)

Here f is the unique local analytic pressure-ODE solution with f(0)=0,f'(0)=sigma,f''(0)=0. Its ODE, already independently proved in A617, is

    (wQ')'+ell Q+T_f=0, ell=2p(2p-1),
    T_f=2(d^2+d+1)R^2+2zff'/w+2z^2f^2/w^2
                           +2pff''/sigma+2pf^2/w.     (3)

The coefficient of f''' at these data is (1-q)/sigma!=0. Analytic existence and uniqueness were checked in A617. The reflected function -f(-z) obeys the same equation and data, so uniqueness makes f odd. R and Q are even and analytic. The actual curl is nonzero on a sufficiently small positive side, R>0 there, and

    R=1+r2 z^2+r4 z^4+O(z^6),
    f=sigma[z+(r2/3)z^3+(r4/5)z^5]+O(z^7),
    Q=-1/2+Q2 z^2+Q4 z^4+O(z^6).                     (4)

Expansion of the definition of Q gives

    Q2=(1-q)r2+sigma^2/2,
    Q4=(1-q)r4+[1-q(q-1)]r2^2/2+sigma^2/2
                                             +sigma^2 r2/3. (5)

The constant equation in (3) and then its quadratic equation give

    r2=d sigma(2-d)/(2(d+2)), Q2=-sigma/2,
    [z^2]T_f=4(d+2)r2+2(d+2)sigma^2
             =2sigma(2+d-2d^2),
    Q4=sigma(6d^2+d-6)/12.                           (6)

For the source simplification, its four nonzero quadratic terms are 4(d^2+d+1)r2,2sigma^2,4p sigma r2,2p sigma^2. Their sum is the second line in (6). The equation 12Q4+(ell-6)Q2+[z^2]T_f=0 now proves the last line.

Solving (5) for the remaining coefficient yields the useful unsimplified recurrence

    r4=-d/(d+2)[Q4+(d^2+6d+4)r2^2/(2d^2)
                              -sigma^2/2-sigma^2 r2/3]. (7)

Equivalently r4=d(d-1)(d^5+d^4+104d^3+40d^2-80d-48)/[24(d+2)^3]. These are actual convergent jets of the analytic solution; no formal power series is used as an existence theorem.

## 3. Rank leaves one constant and forces local symmetry

Here k=c r^-d R>0. Its radial derivative is nonzero. Put tau=p1-2V.grad P2. It has degree -nu under the twisted scaling in (1). Rank makes grad tau proportional to grad k; contracting with Ax and using (Ax).grad k=-cd k shows

    grad tau=(nu tau/(cd k))grad k.

Therefore tau/k^(nu/(cd)) is constant on the connected cone. Write this constant with the positive factor c^(m/d) absorbed as C. The directional derivative in the spherical frame is V.grad P2=r^-m(-2pRQ-fQ'), so every possible p1 must have

    p1=r^-m J(z),
    J=C R^n-4pRQ-2fQ', n=m/d.                         (8)

This derives axisymmetry and parity of p1. There are no additional azimuthal harmonic terms or second free local harmonic constant. The formula is analytic up to z=0, even though p1 was initially only assumed C1 on the positive open side.

## 4. Independent derivation of the next source coefficient

Write the two components of Z as

    Z=r^(-2p-1)(B er+N/sqrt(w) e_theta),
    B=-pR^2-fR'-f^2/w-2pQ,
    N=-Rf-zf^2/w-wQ'.                                (9)

The first is the radial acceleration plus radial pressure derivative. The second follows from the polar acceleration using f'=sigma R and d+sigma=1. Inserting (4)-(6) gives

    B=B2 z^2+O(z^4), B2=-4r2+2d sigma
                              =4d^2 sigma/(d+2),
    N=N3 z^3+O(z^5), 3N3=-(2p-1)B2.                 (10)

The absence of a linear term in N follows from Q2=-sigma/2. The relation for N3 also follows independently from div Z=0, since in these coordinates div Z=r^(-2p-2)[(1-2p)B-N']. This uses the exact leading pressure equation, not an imposed new condition.

Let j=2p+1. The actual Cartesian gradients in their common moving orthonormal basis, with derivative directions as columns, have angular matrices

    M_V=[[-pR, -(wR'+f)/sqrt(w), 0],
         [-pf/sqrt(w), R-f'-zf/w, 0],
         [0,0,R+zf/w]],

    M_Z=[[-jB, -(wB'+N)/sqrt(w), 0],
         [-jN/sqrt(w), B-N'-zN/w, 0],
         [0,0,B+zN/w]].                              (11)

DV=r^(-p-1)M_V and DZ=r^(-2p-2)M_Z. These include the spherical basis derivatives. In the trace of their product, the quadratic contributions are, respectively,

    pj B2,
    d(B2-3N3),
    B2,
    2p sigma B2.

They come from the three diagonal products and M_V(theta,r)M_Z(r,theta). The other off-diagonal product starts at degree4. Thus

    [z^2]tr(M_V M_Z)
       =[pj+d+1+2p sigma]B2-3dN3
       =(2d+3)(d+2)B2.

There is no constant source term. It follows that

    2tr(M_V M_Z)=8d^2 sigma(2d+3)z^2+O(z^4).           (12)

This independently checks the source in LIT166 from four individual gradient products.

## 5. Two incompatible Poisson coefficients

Put ell1=m(m-1). The pressure equation (1), after substituting (8), reads

    -(wJ')'-ell1 J=2tr(M_V M_Z).                      (13)

Its sign is the negative of the residual convention used in LIT166. Expand J=J0+J2z^2+J4z^4+O(z^6). Directly from (8),

    J0=2p+C,
    J2=2p r2+4sigma+C n r2,
    J4=-4(3-d)Q4+4sigma(d+2)r2/3+2p r4
                         +C[n r4+n(n-1)r2^2/2].       (14)

Since the source has zero constant term, 2J2+ell1 J0=0. Its coefficient of C is 2n r2+ell1=2(3d+4)(2d^2+3d+4)/(d+2)>0. Therefore it fixes exactly

    C=-2(5d^4+23d^3+44d^2+38d+16)
                         /[(3d+4)(2d^2+3d+4)].       (15)

The quadratic coefficient of the left side of (13) minus the right side is

    E=-12J4-(ell1-6)J2-8d^2 sigma(2d+3)
      =4d(d-1)F(d)/[(d+2)^2(2d^2+3d+4)],
    F=15d^7+96d^6+303d^5+532d^4+384d^3
                                      -48d^2-376d-96. (16)

Equations(6),(7),(14),(15) make (16) a finite rational identity. The exact calculation retained in the team records verifies it symbolically, including the vanishing constant residual and the leading pressure and Q4 recurrence residuals. To make the sign independent of sampled arithmetic, for0<d<1/2 use

    15d^7+96d^6+303d^5+532d^4+384d^3
      <=(15/64+3+303/16+133/2+96)d=(11819/64)d.

Thus F<=-96-(12245/64)d-48d^2<0. The factor d(d-1) is negative and the denominator positive, so E>0. This contradicts (13). Since every quantity in its required formula is analytic up to z0, equality on the positive open interval would make every one-sided Taylor coefficient zero. The contradiction proves (1).

## 6. Verification and precise remaining scope

The full LIT166 source was read after the independent coefficient derivation and exact calculation. Its source coefficient, r4, C and eliminated polynomial agree exactly. Its final residual is -E because it puts all terms on the opposite side of Poisson; the sign difference is purely conventional. The all-parameter nonzero conclusion agrees. The original focused configured-model comparison supplied the sampled rank-failure suggestion; this proof replaces that observation by the exact coefficient obstruction. A focused follow-up through the existing model agents is requested, not falsely represented as already received.

The theoretical question and pass criterion precede the local one-worker computation in the team records. The exact arithmetic used CPU55 at low priority with one thread. Its measured core derivation interval was1.4313817732036114 seconds; total process wall time, including final output-expression simplifications, was not separately captured. No numerical approximation establishes the sign. Formal sources are explicitly absent because Lean and Lake builds are prohibited.

The actual-profile application is conditional on global zero helicity, natural bounds, and c!=3/7 through A647-A648. The analytic local incompatibility itself has no exception at d1/3. Other interfaces, other initial data, nonaxisymmetric local germs, arbitrary scalar nodes and the resonant actual expansion remain open. In particular A617 remains a correct countertest to the five leading equations and matched low-order traces. Those equations have been strengthened for actual tails; no general continuation principle has been proved.

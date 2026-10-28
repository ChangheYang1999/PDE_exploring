# What the low matrix condition forces on the vertical axis

Status: CONFIRMED V099 (analytical restrictions) and V100 (independent candidate certificates). A review by the lead was requested. No numerical scan is a continuum certificate.

## Exact assumptions and notation

Let c be real, and let rho be a smooth real density on the full plane, even in x and odd in y. Its smooth canonical IPM velocity is

    u=(-R1 R2 rho,R1^2 rho), div u=0.

The full-plane convention and the strain c[rho]=partial_y u2(0) are those of topic01 and topic04, including the contact term. Assume exact center normalization c+c[rho]=1 and a0=rho_y(0)>0. Set

    q(y)=rho(0,y), v(y)=u2(0,y), V(y)=c y+v(y),
    f(y)=F(rho;c)(0,y), F=(cX+u).D rho-rho,
    M=(2c+1)I+sym Du+[[rho_y,-rho_x/2],[-rho_x/2,0]].

For a specified matrix floor kappa define

    epsilon=c+2-kappa, a=1-epsilon=kappa-c-1.

The statements below concern the actual matrix M and actual unnormalized residual. A condition only on the density, with no relation to its velocity or residual, cannot replace this matrix condition.

## 1. Exact axial reduction and its integrated consequence

Parity gives rho_x(0,y)=u1(0,y)=u1_y(0,y)=u2_x(0,y)=0. Incompressibility gives u1_x(0,y)=-v'(y). Therefore at every point of the vertical axis

    M(0,y)=diag(2c+1-v'(y)+q'(y), 2c+1+v'(y)),           (1)
    f(y)=V(y)q'(y)-q(y).                                (2)

Consequently M(0,y)>=kappa I is exactly equivalent to the pair

    v'(y)>=kappa-2c-1,
    v'(y)<=2c+1-kappa+q'(y).                            (3)

The lower inequality can be written

    V'(y)>=a, or v'(y)>=v'(0)-epsilon.                  (4)

If (3) holds for0<=t<=y, integration, q(0)=v(0)=0, and y>0 give

    a y<=V(y)<= (3c+1-kappa)y+q(y).                     (5)

These are necessary conditions for a global matrix floor. They are not sufficient conditions away from the axis, nor do the integrated inequalities alone imply the pointwise inequalities.

At the origin the diagonal entries are3c+a0 and c+2. Hence every normalized reference, irrespective of its tail, has the universal ceiling

    inf_X lambda_min M(X)<=c+2.                         (6)

For the accepted c and kappa=19/5, epsilon=c-9/5 is a small positive rational number. Thus the imposed floor allows the axial velocity derivative to become more negative than its origin value by at most epsilon. This concerns local compression of the vertical velocity, rather than an assumption that a prescribed far-field angular function determines the interior.

If q'(y)>=0, (2),(5) also imply the residual condition

    f(y)>=a y q'(y)-q(y).                               (7)

It is only necessary; no residual upper bound follows from it alone.

## 2. Shape constraint for an exact profile

Assume now F=0, a>0 and M>=kappa I on the entire vertical axis. Equation(5) gives V(y)>=a y>0 for y>0. Since q(y)=a0 y+O(y^3) near zero with a0>0, the linear equation q'=q/V shows that q stays strictly positive for every y>0. For any fixed small y0>0 its exact representation is

    q(y)=q(y0) exp(int_(y0)^y 1/V(t) dt).

On compact subintervals of(0,infinity), V has a positive lower bound, so this formula propagates positivity without an assumption about the sign of q at infinity. In particular q'(y)>0 and V=q/q'. Differentiating gives

    V'=1-K, K=q q''/(q')^2.

Substitution into(1) gives the equivalent exact-profile matrix conditions

    kappa-3c-q'<=K<=epsilon.                            (8)

If additionally epsilon<1, then a=1-epsilon>0 and

    (q^a)''=a q^(a-2)(q q''-epsilon(q')^2)<=0.           (9)

Thus q^a is concave on the positive vertical axis. This is a necessary consequence of the low matrix condition for an exact profile. In the critical case kappa=c+2, it says that q itself is concave. For the current kappa=19/5 and c=4076476460239181/2251799813685248, the exponent is a=14/5-c, about0.98968.

Concavity is consistent with the sublinear asymptotic q(y)~Theta0(pi/2)y^(1/c) when the leading axial coefficient is positive, because0<a/c<1 for the present parameters. The argument proves neither an obstruction from the prescribed far-field profile nor the existence of an exact profile satisfying it. It does identify a local shape restriction absent from mere tail admissibility.

For an approximate reference with q' nonzero, the exact replacement for K is

    K_f=(q+f)q''/(q')^2-f'/q'.                          (10)

Indeed differentiation of V=(q+f)/q' gives V'=1-K_f. Equations(1),(8) hold with K_f in place of K. A curvature test on an approximate q that omits f or f' is invalid. If q>0 as well, the upper matrix inequality is equivalently

    (q^a)''<=a q^(a-2)(f'q'-f q'').                     (11)

No small-residual assumption is needed for this identity and inequality. It follows by multiplying K_f<=epsilon by(q')^2, rearranging, and using the exact derivative of q^a.

## 3. Exact center Taylor restriction

Write q=a0 y+b y^3+O(y^5) and v=(1-c)y+d y^3+O(y^5). Then V=y+d y^3+O(y^5), and direct multiplication in(2) gives

    f=(2b+a0 d)y^3+O(y^5).                              (12)

For an exact profile, d=-2b/a0. At the critical floor kappa=c+2, (4) gives v'(y)>=v'(0); expanding v' at zero shows d>=0. Thus b<=0. At a strictly smaller floor, the sign of b alone does not disprove the matrix inequality: the positive slack epsilon and the higher Taylor terms must be retained. Formula(12) explains why forcing only the center normalization is much weaker than controlling the cubic profile defect.

## 4. Quantitative distance from the sufficient matrix class

Fix c and use the precise compatible weighted space N=N_(s,R) of topic18, with0<s<=2^-12 andR>=1. Its reference-independent Fourier embedding gives

    ||Dh||_infinity<=4 N(h)/sqrt(s),
    ||DU[h]||_infinity<=4 N(h)/sqrt(s),                  (13)

where tensors have their Euclidean norm and the canonical velocity is used. These estimates extend to the completion, so both derivatives have continuous representatives.

Suppose a smooth reference rho has

    2c+1+partial_y u2(0,y0)<=kappa-delta0

for some y0 and delta0>0. If a correction h inN makes M_(rho+h)>=kappa I globally, then its lower axial diagonal entry must increase by at least delta0. That entry depends only on partial_y U2[h], not on the local density-gradient matrix. Consequently(13) implies the necessary distance bound

    N(h)>=delta0 sqrt(s)/4.                             (14)

This is stronger than the general off-axis estimate delta0 sqrt(s)/8 obtained from Weyl's inequality and ||sym DU[h]+A(Dh)||<=8N(h)/sqrt(s). The same conclusion holds if h is also required to have zero strain, positive corrected center slope or fixed leading tail, since these extra conditions only restrict the class of available corrections.

The assertion is about distance to this sufficient coercivity class. It does not exclude exact solutions that do not satisfy this particular matrix floor, and it is not a nonlinear nonexistence theorem. The nearby original reference or a later numerical iterate must be evaluated separately.

## Independent numerical method and scope

The adjacent program reconstructs the accepted state from the strictly read-only original checkpoint, using its exact rational elimination formula. It also reads the already independently reconstructed exact canonical A2 and A3 potentials, tied to their supplied files by hashes. It does not call the numerics producer's evaluation code. Cartesian Taylor jets and a separately differentiated polar polynomial representation check all previously certified fields, including the lower eigenvalue. The new axial derivative is calculated both by Cartesian jets and by differentiating an independently assembled one-dimensional axis series term by term.

Only a few rational points and the exact center jets are needed. This is a small independent computation, not a refit or a numerical global search. Numerical statements will be appended with rigorous intervals, exact inputs and actual times after this check succeeds.

## Dependencies

Topic01/PROOF.md proves parity, the origin normalization and operator conventions. Topic18/PROOF.md proves(13) with the Euclidean velocity multiplier. Every identity(1)-(12) and the distance consequence(14) is derived here. No Hölder-team result or unverified teammate claim is imported.


## Certified original and candidate consequences

The independent768-bit computation passes all axial/Cartesian comparisons at y=1/10,1,2 for state131, nb_stableA2_exact and nb_stableA3_exact. It reconstructs state131 from the read-only original and binds the exact N-B source and canonical hashes. The current slack and exponent satisfy

    0.01031921019999808<epsilon<0.01031921019999809,
    0.98968078980000191<a<0.98968078980000192.

At y=1, the lower axial diagonal entries satisfy

    state131: 4.12001312000831<M22<4.12001312000832,
    A2:       2.22252637111320<M22<2.22252637111321,
    A3:       3.13523976212836<M22<3.13523976212837.

The entire required matrix is diagonal there. These individual values do not certify the original matrix globally; that separate global certificate already exists in topic02. They do refute the required floor for both N-B references.

At s=3*2^-31, equation(14) and outward comparisons show that every correction bringing A2 into the matrix class satisfies N(h)>1.4740e-5, more than12000 times the theorem ball radius5*2^-32. For A3 the corresponding bound is N(h)>6.2115e-6, more than5000 times that radius. These lower bounds hold for anyR>=1 and for any additional trace or tail constraints on h. They are distances to the specified matrix class, not distances to every exact PDE solution.

The integrated necessary condition V(1)>=a also fails: A2 has-0.065468<V(1)<-0.065467, while A3 has0.424903<V(1)<0.424904. The original has1.135398<V(1)<1.135399. The A2 velocity changes the sign of the axial transport at this point, although its density and density derivative are both positive.

The exact cubic density coefficients have opposite signs: state131 has-0.994593<b<-0.994592, A2 has7.674956<b<7.674957, and A3 has17.382064<b<17.382065. Their exact velocity cubic coefficients and residual cubic coefficients are recorded separately in the certificate. Neither normalization nor a small cubic residual prevents the observed matrix failure.

Finally A3 at y=1 provides a concrete counterexample to omitting the residual terms in(10): its density-only ratio satisfies0.0000777<K<0.0000778<epsilon, while0.675079<K_f<0.675080 and M22<19/5. Thus the exact-profile curvature condition cannot be used as a matrix test for approximate profiles. All endpoints in this section are deliberately rounded outward from the saved balls.

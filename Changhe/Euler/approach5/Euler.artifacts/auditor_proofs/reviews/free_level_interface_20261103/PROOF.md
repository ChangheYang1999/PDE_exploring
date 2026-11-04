# Exact obstruction for all pressure levels in the normalized equatorial family

Status: independently CONFIRMED at A670-A672 after complete source and reconstruction postreads. This is the audit of LIT169. The proof uses exact finite algebra and its checked certificate; it is not a numerical residual or a formal Lean proof.

## 1. Exact statement

Fix 0<d<1/2, p=1+d, sigma=1-d, c=1/(d+2), any finite real omega and any real D. Let r=|x|, z=x3/r, w=1-z^2, q=2p/d, m=3p+1 and gamma=m/d. Let Jx=(-x2,x1,0), A=cI-omega J. In the usual spherical frame e_theta points in the direction of increasing polar angle, so the polar angular derivative on functions of z is -sqrt(w) times the z derivative.

For D different from d/[2(d+1)], define an analytic local function f by the initial data

    f(0)=0, f'(0)=sigma, f''(0)=0,

and the leading pressure equation below. Put

    R=f'/sigma,
    V=r^-p(R e_r+f/sqrt(w) e_theta),
    Q=-D R^q+(R^2+f^2/w)/2,
    P2=r^-2p Q,
    k=(Ax).V=c r^-d R,
    Z=DV V+grad P2.                                      (1)

On a sufficiently small positive band r>0, 0<z<delta, R is positive. There is no C1 function p1 there satisfying all three conditions

    p1(exp(tA)x)=exp(-(3-2c)t)p1(x),
    -Delta p1=2tr(DV DZ) in distributions,
    dk wedge d(p1-2V.grad P2)=0.                         (2)

No symmetry of p1 is assumed. At the omitted D there is no analytic leading solution with the stated initial data.

For a member with nonzero vorticity on a sufficiently small positive band, this excludes it as the leading pair of a global C2/C1 zero-helicity Euler profile with the established natural bounds |U|=O(r^-p), |DU|=O(r^-p-1). The actual next-scalar theorem A647-A648 and A653-A655 supplies(2), including c=3/7. The alternative starting assumptions U tending uniformly to zero and DU=O(sqrt r), together with global zero helicity, also supply those natural bounds by A498/A601. The derivative and helicity assumptions remain explicit.

The family is normalized at the equator, is reflection symmetric, axisymmetric and swirl free on its local band, and has zero polar velocity and zero vorticity at the interface. It does not cover arbitrary latitude, nonzero polar interface velocity, swirl or nonaxisymmetric local data. No global completion of V or P2 is assumed or constructed.

## 2. Leading existence and the recurrence

The full leading equation is

    (w Q')'+ell Q+T=0, ell=2p(2p-1),
    T=2(d^2+d+1)R^2+2zff'/w+2z^2f^2/w^2
                                  +2pff''/sigma+2pf^2/w. (3)

At the initial data the coefficient of f''' is (1-Dq)/sigma. It is nonzero at the permitted D. The analytic implicit-function theorem puts(3) in analytic ODE normal form near the data; local analytic existence and uniqueness then give the branch. The reflected function -f(-z) satisfies the same equation and data, so f is odd. It follows that R and Q are even and R remains positive in a sufficiently small band.

Write the actual convergent expansions

    R=1+sum r_(2n) z^(2n),
    f=sigma[z+sum r_(2n) z^(2n+1)/(2n+1)],
    Q=sum Q_(2n) z^(2n), Q0=1/2-D.

For n>=0, equation(3) gives

    (2n+2)(2n+1)Q_(2n+2)
      +[ell-2n(2n+1)]Q_(2n)+[z^(2n)]T=0.                (4)

The new r_(2n+2) has coefficient1-Dq in Q_(2n+2). Thus(4) recursively determines r2,r4,r6,r8 exactly over the rational function field Q(d,D).

This recurrence follows independently from the full moving-frame matrix in Section4, whose square trace is T. It does not import any of the source's computed rational jet coefficients. Nonintegral powers cause no difficulty: R is positive near zero, and its analytic powers have their usual convergent binomial expansions.

Define L=2D(d+1)-d. At L=0 the constant coefficient of(3) is 3d^2+2d+4, independently of r2. It is positive for the target d, excluding this exceptional leading parameter before any division.

## 3. The scalar is forced by rank and homogeneity

Let tau=p1-2V.grad P2. It has the same twisted homogeneity as p1. Since the radial derivative of k is -dk/r and is nonzero, rank in(2) yields d tau=h dk for a continuous scalar h. Dot with Ax, using the two homogeneities, to get h=gamma tau/k. Therefore d(tau/k^gamma)=0. The band is connected, so this ratio is one real constant. Absorb c^gamma into its name C. The result is

    p1=r^-m G(z),
    G=C R^gamma-4pRQ-2fQ'.                              (5)

Thus the equations force axisymmetry and evenness of p1. The formula is analytic across the equator even though p1 was initially assumed only C1 on the positive band. Consequently the Taylor equations at z=0 used below are necessary. There is no unassumed boundary trace or parity condition on p1.

## 4. Full matrix source and its independent reconstruction

For a general field r^-p(R e_r+f/sqrt(w)e_theta), the Cartesian derivative written in the orthonormal spherical frame is r^-p-1 times

    Mv = [ -pR, -(wR'+f)/sqrt(w), 0;
           -pf/sqrt(w), R-f'-zf/w, 0;
           0, 0, R+zf/w ].                              (6)

Its square trace gives(3). In particular the off-diagonal products and both angular connection terms are retained. The first correction is r^(-2p-1)(B e_r+N/sqrt(w)e_theta), with

    B=-pR^2-fR'-f^2/w-2pQ,
    N=-Rf-zf^2/w-wQ'.                                   (7)

The N formula uses f'=sigma R. With j=2p+1, its derivative is r^-2p-2 times

    Mz = [ -jB, -(wB'+N)/sqrt(w), 0;
           -jN/sqrt(w), B-N'-zN/w, 0;
           0, 0, B+zN/w ].                              (8)

The exact next equation is

    (wG')'+m(m-1)G+2tr(Mv Mz)=0.                        (9)

For n=0,1,2,3 its necessary coefficient is

    E_(2n)=(2n+2)(2n+1)G_(2n+2)
          +[m(m-1)-2n(2n+1)]G_(2n)
          +[z^(2n)]2tr(Mv Mz).                          (10)

The independent program uses the same pointwise similarity transformation diag(1,sqrt(w),1) on both matrices. This removes square roots without changing their product trace. It builds the correction by matrix-vector multiplication plus the pressure gradient, rather than importing B,N coefficients. In the transformed frame the velocity components are(R,f/w,0) and the pressure-gradient components are(-2pQ,-Q',0). Multiplying by Mv gives(7) exactly.

The generic power-series operations use coefficients in Q(d,D). If R0=1 and Y=R^alpha, they compute

    Y0=1,
    n Yn=sum_(j=1)^n[((alpha+1)j-n) Rj Y_(n-j)].          (11)

This is the coefficient identity RY'=alpha R'Y. It proves the power routine. Addition, multiplication, differentiation and integration use their defining finite convolution identities. For each new even coefficient j=2,4,6,8, the program temporarily sets Rj=0, computes the residual of(3) at j-2 and divides its negative by j(j-1)(1-Dq). Recomputing that leading coefficient gives zero. Thus each jet follows from(4), not from a stored table. Terms are retained through degree10; equations(10) use only coefficients through degree8.

## 5. Denominators and the three exact polynomial conditions

Put M=D(d+1)(d+2)+d^2+2. The coefficient of C in E0 is

    2(3d+4)M/L.                                         (12)

At M=0, substituting D=-(d^2+2)/[(d+1)(d+2)] in E0 BEFORE division gives

    -4(17d^4+46d^3+78d^2+70d+32)/(d+2),                 (13)

which is strictly negative. The program checks(12)-(13) separately. Hence both L=0 and M=0 are impossible.

For L M nonzero, solve E0=0 uniquely for C. The exact result is

    C=-2[22D^2d^4+82D^2d^3+122D^2d^2+86D^2d+24D^2
          -23Dd^4-73Dd^3-92Dd^2-50Dd-8D
          +6d^4+14d^3+14d^2+2d]/[(3d+4)M].              (14)

After substitution, define integer polynomials F,H4,H6 by

    E2=-4F/(L^2 M),
    E4=2H4/(3L^4 M),
    E6=H6/(90L^6 M).                                    (15)

These are the three primitive bivariate arrays named F,N4,N6 in the JSON certificate. Thus H4 is the source's N4 divided by2, a numerical constant only. The independent power-series reconstruction verifies all three identities(15) exactly against those arrays. Their degrees in D are4,6,8; their degrees in d are9,13,17. No parameter-dependent factor has been removed. The reconstruction also verifies div Z through all four required orders.

This closes the analytic-to-polynomial link. The next step is an independent finite check of what the three polynomials imply. The certificate alone would not prove their derivation from Euler or from(3)-(10).

## 6. Checked resultant certificate

If a pair d,D satisfies(9), then F=H4=H6=0 there. Therefore the two polynomial resultants

    R4(d)=Res_D(F,H4), R6(d)=Res_D(F,H6)

both vanish. This is only the necessary implication of the Sylvester determinant criterion; it remains valid if a specialized leading coefficient vanishes. The fixed symbolic D degrees are kept in every determinant.

The integer certificate retains the three bivariate arrays, both resultant coefficient arrays, a common factor G0, their cofactor arrays and a modular Bezout identity. A separate program using Python standard-library integers checks the following facts.

First, the degrees in d of the resultants are at most6*9+4*13=106 and8*9+4*17=140. Their proposed arrays obey these bounds. The program computes the exact integer Sylvester determinant at107 and141 distinct integer values of d respectively, using fraction-free elimination with every division checked for zero remainder. Each equals the proposed resultant evaluation. Since a nonzero polynomial of degree at most n cannot have more than n distinct roots, these checks prove the two polynomial identities. This is deterministic interpolation verification, not parameter sampling in the target interval.

Second, exact polynomial multiplication verifies that both resultants are a nonzero rational constant times G0 times their respective integer cofactors. The common factor, including its retained numerical normalization, is

    G0=4608 d^4(d-1)^2(d+1)^24(d+2)^3(2d+1)
          *(d^2+5d+12)*(3d^2+2d+4)^8
          *(17d^4+46d^3+78d^2+70d+32).                  (16)

The explicit factor product is checked against its stored coefficient array.

Third, modulo the prime101, the two cofactor leading coefficients are nonzero and the stored Bezout combination equals1. Hence the cofactors are coprime over Q. For completeness, a nonconstant common rational factor could be normalized to a primitive integer polynomial. Gauss's lemma would make it divide both integer cofactors. The nonvanishing product leading coefficients modulo101 force its leading coefficient and those of the quotients to remain nonzero, so its reduction would still be a nonconstant common divisor. This contradicts the checked Bezout identity.

It follows that the only common complex zeros of the two resultants are zeros of G0. Every factor in(16) is nonzero for0<d<1/2. The three nonconstant factors with exclusively positive coefficients are positive there, and all linear factors are visibly nonzero. Thus simultaneous resultant vanishing is impossible. Equations(2) cannot hold.

## 7. Why the first two equations did not suffice

The source also records a useful limitation of its earlier test. Substitution in the now independently reconstructed F gives

    F(d,d/[2(d+1)])=3d^2(d^2+5d+12)(3d^2+2d+4)^2/4>0,
    F(d,1/2)<0,
    F(d,1)=d(d-1)P7(d)>0,

where

    P7=15d^7+96d^6+303d^5+532d^4+384d^3-48d^2-376d-96,
    -4F(d,1/2)=60d^8+428d^7+961d^6+2139d^5+2537d^4
                  +3289d^3+2202d^2+1472d+304.

Bounding each positive term d^j by d/2^(j-1) gives P7<=-96-(12245/64)d-48d^2<0. The second displayed polynomial is positive. Thus two-coefficient solutions exist on both sides of1/2 by the intermediate value theorem. With Dh=2(d^2+d+1)/[(d+1)(d+2)], one has1/2<Dh<1 and F(d,Dh)<0; the exact identity is

    F(d,Dh)=-2d(d-1)(3d^2+2d+4)^2 H(d)/(d+2)^3,
    H=d^5-45d^4-89d^3-118d^2-114d-40<0.

The sign of H follows from d^5<1/32<40. The upper root can therefore be chosen above Dh. The first vorticity coefficient is

    2r2-d sigma=-2d[D(d+1)(d+2)-2(d^2+d+1)]/L.

It is nonzero at both selected roots. Hence these are genuine analytic vortical leading germs passing the first two necessary equations, while failing the four-equation system. This is a finite-test observation, not existence of a next pressure or a profile. The exact substitutions in this section are separately checked in the supplementary verification record.

## 8. Evidence, dependencies and scope

The independent coefficient reconstruction ran on CPU55 in13.067645865026861 measured seconds, from2026-11-03T09:55:53.374696+00:00 to09:56:06.442346+00:00. The separate integer certificate replay ran in0.09223342267796397 measured seconds, from09:56:33.079691+00:00 to09:56:33.171914+00:00. Both passed. The supplementary special-value check passed in0.6491202348843217seconds, from09:57:55.488501+00:00 to09:57:56.137627+00:00. The intervals cover their recorded calculation bodies; no longer full-process runtime is inferred. The complete scripts, exact JSON inputs and outputs, hashes and initial question are in the team records. No workers ran concurrently in this agent.

The actual-profile application depends on the full next-scalar and resonance arguments already confirmed at A647-A648,A653-A655 and on the stated natural bounds. The local algebra itself uses only(1)-(3) and the explicit finite recurrence. It does not use pressure uniqueness, tail density, an A2 assumption or any symmetry outside the local band. The reflected analytic branch, its geometry and the required vortical positive side must not be silently dropped from the conclusion.

The source proof, coefficient program, certificate producer and integer checker were read completely, and the derivation was reconstructed independently as described above. Existing configured-model comparisons through the coordinator and theory agents remain the collaboration channel. The configured identifier is the primary model; provider runtime is not independently attested. A new focused reply is not presumed. Arbitrary interfaces, uncontrolled nodes, the bare-decay derivative gap and both unrestricted nonexistence conjectures remain OPEN.

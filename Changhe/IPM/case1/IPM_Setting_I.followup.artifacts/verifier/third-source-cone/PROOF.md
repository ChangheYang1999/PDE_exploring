# A convergent third-order source solution on a left cone

Date: 2026-10-20. Status: complete informal proof, independently checked and reviewed by actual lead Claude Opus5.5 at17:13:34Z. Exact coefficient and independent Bessel checks passed. This is a cone theorem. It does not give a solution on a neighborhood of the source or a global canonical profile.

## Statement and notation

Let A>2, lambda=2/A, 3/2<b<2, g=2b(A-1), and d=3-lambda. Put C=1/(12 sin(pi lambda))>0. There are real fields v,V on

    C = {s=-r<0, |y|<r/4, 0<r<R},

for a positive R, which satisfy

    (A s partial_s+y partial_y-1)v+g V_2+V.grad v=0,
    div V=0, curl V=-v_s.                                  (1)

Here curl V=partial_s V_2-partial_y V_1. The fields v,V_2 are odd in y and V_1 is even. They are real analytic at every interior point, extend with two derivatives to the vertex, and their second derivatives are Holder continuous of exponent 1-lambda on every smaller closed cone and sufficiently small closed radial interval. With G_j(s)=partial_y^j v(s,0)/j!, they satisfy exactly

    v_y(s,0)=0,  V(s,0)=0,
    G_3(-r)=C r^(-lambda),
    G_5(-r)=-b lambda(lambda+1) C r^(-lambda-2)/20.          (2)

Consequently r^lambda G_3=C is nonzero, whereas r^(2lambda)G_5 tends to negative infinity. The physical pair f=g y+v, W=(A s,y)+V solves W.grad f=f, div W=A+1, curl W=-f_s on C and has the source jet D W(0)=diag(A,1), f_y(0)=g. No full-plane inverse or boundary condition outside C is asserted for the corrected V.

One sufficient radius is any R with

    R^(2-lambda) < 15(15-b)(A-1)/(28 C).                   (3)

The leading term is the left-cone restriction of the third-order frozen Fourier field. Every correction is a pure radial power with an analytic angular coefficient. No radial logarithm is necessary for this particular mode. The first correction has radial degree 5-2lambda, angular order seven, and seventh-axis coefficient

    -lambda(3-2lambda) C^2 r^(-2-2lambda)/[40(A-1)].         (4)

## 1. The frozen field and its left-axis coefficients

Use the Fourier convention hat f(zeta)=int exp(-i X.zeta)f(X)dX, with inverse factor (2pi)^(-2). Let a(t)=t_+^(-lambda) and define the homogeneous tempered field v_0 by

    hat v_0(xi,eta)=hat a(xi) i sign(eta) |eta|^(2b-4)
                     (xi^2+eta^2)^(-b).                  (5)

The angular singularities are integrable: their powers are lambda-1>-1 and 2b-4>-1. The total degree is lambda-5. Subtracting the Taylor polynomial of degree two from a test function near frequency zero makes the radial integral integrable; the resulting finite part has a unique homogeneous normalization because lambda-5 is not -2 minus an integer. Differences of extensions are derivatives of delta at zero, whose homogeneous degrees are integers. Formula (5) is thus unambiguous as a homogeneous distribution. Its inverse has degree d=3-lambda and odd y parity.

For the homogeneous canonical velocity, the second component multiplier is -xi^2/(xi^2+eta^2). Away from the coordinate axes, application of A xi partial_xi+eta partial_eta+A+2+g xi^2/(xi^2+eta^2) to (5) gives the factor

    A lambda-2+[g-2b(A-1)]xi^2/(xi^2+eta^2)=0.

The identity extends across the axes distributionally: a homogeneous locally integrable power has its usual Euler identity, and the derivatives eta partial_eta and xi partial_xi introduce no interface delta. Extension through zero cannot leave a distribution of the noninteger degree lambda-5 supported there. Fourier inversion proves the frozen transport equation, divergence and curl. This also fixes the Fourier sign of g U_2.

We rederive the physical constants. For eta>0, the one-dimensional inverse in xi of (xi^2+eta^2)^(-b) is

    K_b(x;eta)=1/[2 sqrt(pi) Gamma(b)]
       int_0^infinity tau^(b-3/2) exp(-tau eta^2-x^2/(4tau))dtau.

At s=-r<0, convolution with a samples x=r+t, t>0. For m>=0, taking 2m+3 derivatives in y removes the frequency-zero finite part. Integration first in eta and then in tau gives

    (-1)^m/pi int_0^infinity eta^(2b+2m-1) K_b(x;eta)deta
       =(-1)^m (b)_m (2m)!/[2pi m!] x^(-2m-1).            (6)

The Gaussian integral is positive before the explicit sign; both changes of order are justified by nonnegative integrands. The remaining t-integral is finite at both ends and equals

    int_0^infinity t^(-lambda)(r+t)^(-2m-1)dt
       =r^(-lambda-2m) Gamma(1-lambda)Gamma(2m+lambda)/(2m)!.

Euler's reflection identity therefore gives

    partial_y^(2m+3) v_0(-r,0)
       =(-1)^m (b)_m (lambda)_(2m)
          r^(-lambda-2m)/[2(m!) sin(pi lambda)].             (7)

Here (q)_m denotes q(q+1)...(q+m-1), with (q)_0=1.

The linear y coefficient is zero on the left. A direct calculation after the three derivatives partial_s^2 partial_y gives the well-defined axis trace

    partial_s^2 partial_y v_0(s,0)=a(s)/[2pi(b-1)].         (8)

Indeed the eta integral of |eta|^(2b-3)(xi^2+eta^2)^(-b) is 1/[(b-1)xi^2], which cancels the xi^2 factor. Its left-side kernel interpretation is legitimate: the integral of the absolute second x derivative of K_b with this eta weight is bounded by a constant times x^(-1), and convolution against t^(-lambda) is integrable for x=r+t. Thus (8) holds as an actual trace on s<0.

For completeness, subtract the linear term in the sine kernel defining v_0. The integral with sin(eta y)-eta y is absolutely convergent for |y|<r and defines an analytic odd function starting with y^3. Its third y derivative is that of v_0. The difference is y L(s) as a distribution, by odd parity. Equation (8), evaluated on the left, gives L''=0. Homogeneity requires L to have degree 2-lambda strictly between one and two, so the affine function L is zero. This justifies the left analytic germ without assuming its first trace in advance. Analyticity can also be seen from the exponential decay in eta of K_b(r+t;eta): on every smaller strip |Im y|<r the cubic-subtracted integral and all its y derivatives converge. Polynomial terms subtracted for convergence are analytic.

Set z=y/r. Formula (7) now gives

    v_0(-r,y)=r^d phi_0(z),
    phi_0(z)=C sum_(m>=0) (-1)^m
       6(b)_m(lambda)_(2m) z^(2m+3)/[m!(2m+3)!].          (9)

The ratio test gives radius one. The third and fifth coefficients are C and -b lambda(lambda+1)C/20. The frozen transport equation differentiated once in y and divergence give A s G_1'-g (V_0)_1'=0 on the axis. Since G_1=0 and V_0 is homogeneous of degree d, its first component is zero there. Its second component vanishes by odd parity.

## 2. A linear inverse with the angular order preserved

The general coefficient identities below can also be derived directly from (1); their independent derivation is in ../source-formal/PROOF.md, section 3. Seek a linear correction r^p(phi,alpha,beta) with odd phi,beta and even alpha. The linear transport, divergence and curl equations are

    (Ap-1)phi+(1-A)z phi'+g beta=h,
    beta'=p alpha-z alpha',
    -p beta+z beta'-alpha'=p phi-z phi'.                  (10)

Write phi_j,beta_j,h_j for odd Taylor coefficients and put c_j(p)=Ap-1-(A-1)j. With the lower coefficients zero, comparison gives

    c_j(p)phi_j+g beta_j=h_j,
    beta_(j+2)=-(p-j)(p-j-1)(beta_j+phi_j)/[(j+1)(j+2)],
    alpha_(j+1)=(j-p)(beta_j+phi_j)/(j+1).                (11)

Let n>=1, p=p_n=1+(n+1)(2-lambda) and m_n=4n+3. Then

    c_j(p_n)=(A-1)(2n+3-j).

The only odd-index resonance is j=2n+3. If h starts at degree m_n, choose all phi,beta coefficients below m_n, including the free resonant phi coefficient, to be zero. The compatibility condition there is 0=0. Equations (11) then give a unique triple with phi=O(z^m_n), alpha=O(z^(m_n+1)), beta=O(z^(m_n+2)). No later denominator vanishes.

We need a bound uniform in n, not just a formal recurrence. Fix kappa=1/4 and let ||u||=sum_j |u_j|kappa^j. Also put ||h||_-1=sum_j |h_j|kappa^j/j for odd h with zero constant. For j>=m_n we have 0<p_n<j and

    0< (j-p_n)(j+1-p_n)/[(j+1)(j+2)] <1.

The coefficient recurrences imply

    ||beta|| <= B ||phi||,  ||alpha|| <= kappa/(1-kappa^2)||phi||,
    B=kappa^2/(1-kappa^2)=1/15.                           (12)

These estimates hold first for every finite partial sum. Since j/(j-2n-3)<=7/2 and j-2n-3>=2, transport gives

    ||phi|| <= 7/[2(A-1)] ||h||_-1+b||beta||
            <= 7/[2(A-1)(1-b/15)] ||h||_-1.              (13)

The factor b/15<1 permits absorption. The finite partial-sum bounds and monotone convergence prove existence in this norm as well as the bound; they do not presuppose convergent series. Equations (10) hold on the open disk by differentiation on smaller disks. For n=0, p_0=d<3 and phi_0 starts at degree three, so the velocity estimates (12) also hold for its frozen velocity.

## 3. The nonlinear series converges

Construct (phi_n,alpha_n,beta_n) recursively from (11), with forcing

    h_n=sum_(i+j=n-1)
       [alpha_i(p_j phi_j-z phi_j')-beta_i phi_j'].        (14)

This is exactly the negative quadratic transport term, since partial_s[r^p phi(y/r)]=-r^(p-1)(p phi-z phi'). Induction gives the angular orders

    phi_n=O(z^(4n+3)), alpha_n=O(z^(4n+4)),
    beta_n=O(z^(4n+5)).                                  (15)

Thus each resonance is below the first forced coefficient and can be set to zero. These statements include all n and show that logarithms are unnecessary.

Let a_n=||phi_n||. Each density monomial has angular index l>=4j+3>p_j. In the first product in (14), the output index k is at least l, so |p_j-l|/k<=1. In the second, k is the beta index plus l-1, again at least l, so l/k<=1. Consequently the coefficient convolution, with the derivative compensated by the output weight, gives

    ||h_n||_-1 <= 2kappa/(1-kappa^2) sum_(i+j=n-1) a_i a_j.

Together with (13), this is

    a_n <= K sum_(i+j=n-1) a_i a_j,
    K=28/[(15-b)(A-1)].                                  (16)

There is no unbounded radial derivative hidden here: its coefficient p_j is controlled by the same angular index l, as used explicitly above. The Catalan recurrence proves

    a_n <= Catalan_n K^n a_0^(n+1) <= 4^n K^n a_0^(n+1).

From (9), successive absolute terms of ||phi_0|| have ratio at most kappa^2: after duplication the ratio without kappa^2 is

    (m+b)(m+lambda/2)(m+(lambda+1)/2)
       /[(m+1)(m+2)(m+5/2)] <1.

It follows that a_0<=C kappa^3/(1-kappa^2)=C/60. Now define

    v=sum_(n>=0) r^(p_n)phi_n(z),
    V=sum_(n>=0) r^(p_n)(alpha_n(z),beta_n(z)).             (17)

Since p_n=d+n(2-lambda), (16) proves normal convergence whenever 4 K a_0 r^(2-lambda)<1. Condition (3) is sufficient. On every smaller angular disk and compact radial subinterval all derivatives also converge: Cauchy estimates handle angular derivatives, while each radial derivative costs a polynomial in n and a fixed negative power of r. A geometric series with polynomial factors remains convergent strictly inside its radius. For analyticity, take complex r,z with Re r>0, |r|<R and |z|<kappa, and define r^p_n using the holomorphic logarithm on the right half-plane. Its modulus is |r|^p_n because p_n is real. The same majorant proves locally uniform convergence of holomorphic terms there. Composition with r=-s,z=y/r is therefore real analytic at every interior point of the real cone. We may therefore substitute (17) into the three equations and multiply the absolutely convergent series. The recurrences prove (1) exactly, not merely to finite order.

At the vertex, each derivative of order k<=3 is O(r^(d-k)), uniformly on a smaller closed cone. For k<=2 its limit is zero. The bound for k=3 and the bound O(r^(1-lambda)) for the second derivatives prove the stated Holder exponent: when two points are separated by at least half their smaller radius use the size bounds; otherwise integrate the third derivative along their segment, which stays at a comparable radius in this convex cone, and use |X-Y|r^(-lambda)<=constant |X-Y|^(1-lambda). The higher-order terms are smoother at the vertex and satisfy the same estimates after restricting the radius. This proves regularity on the closed cone; it does not supply values or equations outside it.

By (15), every n>=1 density correction has zero first, third and fifth y derivatives on the open axis, and every velocity correction vanishes there. Normal convergence at each axis point proves (2) for the summed field. Finally alpha_0 starts with lambda C z^4/4 and beta_0 with -lambda(lambda+1)C z^5/20. The coefficient of z^7 in (14) for n=1 is lambda(3-2lambda)C^2/20. Since c_7(p_1)=-2(A-1), formula (4) follows.

## Dependencies and scope

The proof uses elementary Gaussian and beta integrals, homogeneous distribution extension, power-series coefficient identities, and the Catalan majorant. Section 1 independently checks the normalization of the frozen third-order field in lead fred48 part 6; section 2 rederives the relevant special case of the previously independently audited source-formal recurrence. The new uniform bound (13) and angular-order gain (15) are what permit convergence for this mode. They do not establish convergence for the three fifth-order examples, whose lower angular terms and resonances are different.

The cone excludes every point (0,y) with y!=0. No extension across that line, full source neighborhood, global canonical inverse, matching to a smooth normalized center, or sublinear far field has been constructed. In particular, this theorem is not a coupled counterexample in P_inf, does not settle sharpness of a theorem stated on a full neighborhood of P, and is neither endpoint of TASK.md.


## Review precisions

Sections2-3 also construct a cone solution when the coefficient C is any nonzero real number: use |C| in the norm estimate and the sufficient radius (3). The Fourier calculation in section1 identifies one particular germ and fixes its positive normalization. The condition A>2 also ensures the stated C^(2,1-2/A) regularity; different A, b and odd initial orders, with their correct regularity, are treated in ../higher-source-cone/PROOF.md.

The div-curl equations alone allow addition of a local divergence-free, curl-free field. In the homogeneous angular recurrences we choose alpha_(n,0)=beta_(n,1)=0, which fixes the axis velocity of our solution. Such a harmonic addition need not preserve transport for the same density. Accordingly the corrected V is one local velocity solving the coupled equations; it is not specified by the global canonical inverse. The initial germ's agreement with the homogeneous Fourier inverse follows from section1. No canonical meaning is asserted for the higher corrections.

On a smaller cone, oddness and the angular order yield |v_yy|<=C'|y|r^(-lambda)<=C''|y|^(1-lambda), and |(V_1)_yy|<=C' r^(1-lambda). Also v_yyy(-r,0)=6C r^(-lambda). Thus the construction attains the critical exponent alpha=1-2/A in the source trace estimate. Its cone scope must be retained when discussing sharpness. These are source traces at P, not the B_j homogeneous coefficients at the separate normalized center.

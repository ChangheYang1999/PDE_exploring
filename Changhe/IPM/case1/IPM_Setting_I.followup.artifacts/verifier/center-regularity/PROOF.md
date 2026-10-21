# A necessary center-jet condition for the nodal density representation

Dated 2026-10-20. This result concerns the smoothness of a represented field, not the existence or nonexistence of profiles of the coupled equation.

## Exact statement

Let b(q,s) be smooth on a neighborhood of [0,epsilon] times the angular circle, even under the axis reflections, and let b(0,s)=1. Fix L>0, 0<k<1 and |beta|<1. Define

    theta = s + (beta/2) sin(2s),
    q = 1 - (1+r^2/L^2)^{-(1-k)/2},
    rho(x,y)=x^2 y (1+r^2/L^2)^{(k-3)/2} b(q,s(theta)).

The angular map is a smooth diffeomorphism because its derivative is at least 1-|beta|>0. Near the origin,

    a(r,theta) := rho/(x^2 y) = 1+r^2 A_2(theta)+O(r^4),
    A_2(theta) = [(1-k)b_q(0,s(theta))+(k-3)]/(2L^2).

The remainder and its angular derivatives are uniform. A necessary condition for a to be C^2, and for rho to be C^5 on a neighborhood of 0, is

    A_2(theta) = c_0+c_2 cos(2theta).

In particular A_2(pi/8)+A_2(3pi/8)-2A_2(pi/4) must vanish.

## Proof

The Taylor expansions of q and the radial weight give the formula for A_2 directly. If a is C^2, its parity and radial expansion show that its second-order Taylor polynomial is 1+alpha x^2+delta y^2. Restricting to a ray and dividing a-1 by r^2 therefore gives A_2=alpha cos^2(theta)+delta sin^2(theta).

For the claim about rho, subtract x^2 y. The result has degree-five leading term r^5 cos^2(theta)sin(theta)A_2(theta) and a uniform O(r^7) remainder. If rho is C^5, its fifth-order Taylor term must be a homogeneous polynomial. Parity restricts it to a linear combination of x^4 y, x^2 y^3 and y^5. The identity rho(0,y)=0 removes y^5. Dividing the ray identity by cos^2(theta)sin(theta) for 0<theta<pi/2 gives the same necessary form of A_2. Continuity extends it to the axes. The displayed three-angle contrast annihilates both 1 and cos(2theta), so it must vanish.

Conversely, this single condition is not sufficient for smoothness: higher radial coefficients must satisfy their own polynomial compatibility conditions. A nonzero measured contrast therefore detects a center obstruction that is logically separate from an axis finite-part B_3 diagnostic.

## Application and evidence

The checkpoint dnSA_n120m48.npz, md5 a1fb7c96388f3957f6b63312f82eb7bb, has been reconstructed with independent DCT coefficients in ../inverse/code/collocation.py. No solver module or evaluator from another lane is imported. The interpolation error at all published nodes is 8.2e-14 and the angular inversion error is below 1.9e-15.

The quadratic coefficient at pi/8, pi/4, 3pi/8 is respectively

    -0.05616879038927143, -0.05659356164281237, -0.04973218317577931.

Its contrast is +0.007286149720574009. Direct values of (a-1)/r^2 produce contrasts 0.00694239, 0.00724751, 0.00728267 and 0.00728576 at r=0.03, 0.01, 0.003 and 0.001. These calculations independently check the differentiation at q=0. Over 512 angles the remainder after fitting the two allowed angular modes has maximum 0.02580763 and RMS 0.00871419.

Thus, to the demonstrated numerical accuracy, this represented checkpoint has a nonzero center obstruction already at order five of rho. It cannot be offered as a smooth-center field. This conclusion concerns the actual finite interpolant and does not prove that a convergent sequence of interpolants has a nonsmooth limit. It also does not invalidate its use in the weaker C^(2,alpha) class. These are floating-point checks, not interval-certified bounds.

Evidence files are ../inverse/verification/dnSA_interpolation.json and dnSA_center_direct.json. No formal proof-assistant run is claimed.


## Current-state follow-up (2026-10-20T14:00:54.185375+00:00)

The same independent calculation gives a contrast +0.007295409450990276 for the published dnSB checkpoint (md5 0234b3634f747b0a50386d0359bea823), and +0.007245649575602378 for its dt/2 re-solve (md5 35f3672db73e30a89a460b1562e7ccda). Their direct r=0.001 contrasts are +0.007295022919073801 and +0.007245263500266219. Thus the smaller orbit step does not remove this center-jet defect. Both have b(0,s)=1 exactly in the saved nodal data.

The projected (96,40) seed gives -0.004950351060731419 and the incomplete (144,56) two-grid state gives +0.01144868539765985. These latter states are not converged solutions, so their values do not form a solution-convergence table. They illustrate sensitivity of the center jet to the representation. The numerical records, hashes, direct shrinking-radius checks and nonquadratic angular norms are in verification/current_states.json.

## Axis jets can miss a nonsmooth center

This section applies to the exact finite nodal interpolants, not to exact IPM profiles. The radial compactification and prefactor are analytic in r^2 near zero. The inverse angular map s(theta) is analytic near theta=0 since its derivative there is 1+beta>0. Thus the represented factor has a convergent expansion

    a(r,theta)=1+sum_(l>=1) r^(2l) A_(2l)(theta),

where each A_(2l) is even and analytic in theta near zero. For x>0 set t=y/x. Expanding the analytic even function (1+t^2)^l A_(2l)(arctan t) gives

    G_(2m+1)(x)=sum_(l>=1) a_(l,m) x^(2l+2-2m),  m>=1.

For fixed m this is a convergent Laurent series in x^2 near zero. The least possible exponent is 4-2m=5-j. In particular G_3 is analytic in x^2 and vanishes at least as x^2, G_5 can have a nonzero constant limit, and G_7 can have an x^(-2) pole. A fit to G_3 alone can therefore show no fractional power even when the represented field is not C^5 at the center. Such a fit is not the source-selected B_3 functional of an exact coupled profile; the trial field need not obey the axis ODE.

Write A(theta)=A_2(theta), and let D_i=A^(i)(0). Taylor expansion of arctan t gives

    lim_(x->0+) G_5(x) = (D_4+4D_2)/24,
    lim_(x->0+) x^2 G_7(x) = (D_6-10D_4-56D_2)/720.

These follow by taking the coefficients of t^4 and t^6 in (1+t^2)A(arctan t). Because the represented density vanishes identically on x=0, a nonzero first limit is another direct obstruction to C^5 regularity. The pole in G_7 gives an additional higher-order obstruction. These tests supplement the three-angle criterion, which does not require differentiation at the axis.

## The same fifth homogeneous term can generate a logarithmic velocity

Suppose the fifth homogeneous density term is r^5 P(theta), with P even in x and odd in y, and let p_7 be its seventh sine coefficient:

    P(theta)=cos(theta)^2 sin(theta) A(theta),
    p_7=(1/pi) integral_0^(2pi) P(theta) sin(7theta) dtheta.

The next density terms in the exact nodal representation have orders r^7, r^9, and so on. Then the canonical velocity on the positive x-axis has a term

    U_1(x,0)=3 p_7 x^5 log(x) + terms without this logarithm.

To verify the coefficient, differentiating r^5 sin(n theta) in x gives

    r^4 [(5+n)sin((n-1)theta)+(5-n)sin((n+1)theta)]/2.

Only n=7 contributes to the resonant sixth angular mode, with coefficient 6p_7; the potential contribution from n=5 has coefficient zero. Since

    Delta[r^6 log(r) sin(6theta)]=12 r^4 sin(6theta),

the equation -Delta psi=rho_x forces the term -(p_7/2)r^6 log(r)sin(6theta) in psi. Applying U_1=-psi_y at y=0 gives 3p_7 x^5 log(x). A smooth harmonic contribution from exterior data changes analytic powers only and cannot cancel this logarithm. Localizing the homogeneous term with a radial cutoff changes its potential by a harmonic function near zero, so the coefficient is a local statement. Higher homogeneous degrees cannot alter the r^6 logarithmic coefficient. This also follows by applying the elementary radial Green formula to the sixth angular component and splitting its integral near zero.

Consequently p_7!=0 implies that this axis velocity is not C^5 at the center. It prevents using a smooth odd Taylor model of w there without a model-error qualification. It does not change the independently valid origin-strain identity, which requires much less regularity.

## An interval formula for the tests on a nodal field

Let c_m be the cosine coefficients of b_q(0,s), with b_q(0,s)=sum_(m=0)^(M-1)c_m cos(2m s). The exact derivative row at the radial left endpoint is

    b_q(0,s_a)=sum_(j=1)^N d_j [b_(j,a)-b_(0,a)],
    d_j=-2(-1)^j/q_j for 1<=j<N,  d_N=-(-1)^N,
    q_j=[1-cos(j*pi/N)]/2.

This is the derivative of the cardinal interpolation formula: d_j=w_j/[w_0(q_0-q_j)], with endpoint barycentric weights halved. Taking a cosine transform on the ideal angular nodes gives the c_m. Thus the calculations can enclose the exact interpolant through the saved binary values using ball arithmetic, without differentiating a rounded DCT table.

Put K=(1-k)/(2L^2), d=1+beta and

    a=1/d, b=2beta/(3d^4), c=4beta^2/(3d^7)-2beta/(15d^6).

These are the first three odd coefficients of s(theta)=a theta+b theta^3+c theta^5+O(theta^7), obtained by inversion of theta=s+(beta/2)sin(2s). If F_2,F_4,F_6 are the second, fourth and sixth derivatives in s of sum c_m cos(2m s) at zero, then

    D_2=K a^2 F_2,
    D_4=K [24ab F_2+a^4 F_4],
    D_6=K [360(2ac+b^2)F_2+120a^3b F_4+a^6 F_6].

For p_7, elementary product-to-sum identities and reflection symmetry give

    p_7=K/(2pi) [I_2+I_3-I_4-I_5],
    I_l=integral_0^(pi/2) b_q(0,s(theta)) cos(2l theta) dtheta.

Substitute t=2s and integrate by parts using the derivative of sin(l t+l beta sin t). The endpoint sine terms vanish and one obtains

    I_l=pi/(4l) sum_(m>=1) m c_m [J_(m-l)(l beta)-J_(-l-m)(l beta)].

Here J_n is the Bessel function defined by its convergent power series. The identity for its integer Fourier coefficient follows by multiplying the two absolutely convergent exponential series in exp((z/2)(w-w^(-1))) on |w|=1. Thus no asymptotic approximation enters the moment formula. The implementation encloses these finite sums in Arb balls and separately compares them with ordinary angular quadrature. These are rigorous bounds for the stated exact nodal interpolant; they are not claims about an unknown limiting profile.


## Certified represented-field obstruction (2026-10-20T14:32:27.553827+00:00)

The 256-bit Arb evaluation through the exact saved binary nodal values excludes zero in all four quantities below. Balls in the evidence files carry over forty decimal digits; the following are rounded displays.

| Field | lim G5 | lim x^2 G7 | p7 | coefficient of x^5 log x in w |
|---|---:|---:|---:|---:|
| dnSB | 290.466388777705 | -14283.4528985618 | 0.000421593211532204 | 0.00126477963459661 |
| dnSB, dt/2 | 289.278168777589 | -14235.3681602425 | 0.000419271829018031 | 0.00125781548705409 |

These enclose the exact interpolant at ideal Chebyshev radial and angular nodes, with exact saved c_l, beta and L and k=1/c_l. Rounded DCT coefficients, binary approximations to ideal nodes, and any unknown limiting profile are different objects. The usual mathematical nodal representation is the former; the difference between rounded reconstruction and the exact representation is not hidden in the ball radius. Ordinary quadrature through this lane's independently reconstructed floating DCT coefficients at 128, 256, 512 and 1024 Legendre angles agrees with p7 to about 1e-15. Separate symbolic expansions verify both axis-jet formulas and the Poisson and velocity coefficients exactly.

Thus these represented densities are not C^5 at the origin, and their canonical axis velocities are not C^5 either. Analytic axis G3 data alone do not detect the full smooth-center obstruction. No claim about the B3 functional of an exact solution or about the existence of a smooth limiting profile follows from these tests.

Code: code/axis_jet_balls.py and code/check_axis_formulas.py. Evidence: verification/dnSB_axis_balls.json, dnSB_dt2_axis_balls.json and axis_formula_checks.json. A first attempt to write the code failed because the code subfolder did not exist; it was created before the successful runs. No results from the failed attempt are used.

## A center transport balance independent of the cubic velocity

Assume the represented density above has its angular expansion smooth on the full circle and the canonical inverse is defined with the stated sublinear growth. Write

    rho = x^2 y + r^5 P(theta) + O(r^7).

The remainder here has the corresponding differentiated angular expansion. The density is C^(4,alpha) near zero for every alpha<1, even when P is not polynomial. The localized order-zero velocity law and its smooth exterior part give at least a C^3 velocity expansion. Parity and zero divergence therefore imply

    U = (-c x, c y) + U_3(x,y) + o(r^3),

where U_3 is a homogeneous cubic vector polynomial. Let p_n be the sine coefficients of P. For any fixed c_l, the coefficient of r^5 sin(m theta) in R=(c_l X+U).grad rho-rho, at odd m>=7, is

    Q_m = (5c_l-1)p_m + (c/2)[(m-7)p_(m-2)-(m+7)p_(m+2)].

Indeed, U_3.grad(x^2 y) is a degree-five polynomial and has no sine modes above five. The linear transport field acts on r^5P as

    r^5 [(5c_l-1-5c cos(2theta))P+c sin(2theta)P'],

which gives the formula by the product-to-sum identities. The degree-three residual has only modes one and three and does not affect these coefficients. Thus the computation does not assume that the origin-strain identity already holds for the trial field.

In particular,

    Q_7 = (5c_l-1)p_7-7c p_9,
    Q_9 = (5c_l-1)p_9+c(p_7-8p_11).

If p_9!=0 and

    D = 7p_9^2+p_7^2-8p_7 p_11 != 0,

then Q_7 and Q_9 cannot both vanish for any c and any c_l>1. If Q_7 vanished, substituting c=(5c_l-1)p_7/(7p_9) in Q_9 would give Q_9=(5c_l-1)D/(7p_9), which is nonzero. Consequently that represented density cannot solve the transport equation with any parity-compatible divergence-free velocity having the local regularity of the canonical velocity. This is a necessary center balance, not a global nonexistence theorem or a lower bound on the residual of an unknown limiting profile.

For n>=7 odd, the same finite Bessel formula above computes p_n, using

    p_n = K/(2pi)[I_((n-1)/2)-I_((n+1)/2)+I_((n-3)/2)-I_((n+3)/2)].

The constant part of A_2 has no contribution to these modes. Thus p_7,p_9,p_11 and D can be enclosed using only the exact nodal data and parameters. A numerical application belongs in the evidence record only after these enclosures and the coefficient identity have been checked.


The enclosures completed at 2026-10-20T14:39:13.721163+00:00 give p9<0 for both fields, while p7>0. Their determinant D is -7.47694183197213e-7 and -7.38469659763744e-7 respectively, with rigorous ball radii much smaller than these values. The identity c=3c_l-1 gives Q7=0.0117840187900376 and0.0116440085759622. Thus either the sign test with the center identity or the two-mode determinant test proves the stated represented-field obstruction. The symbolic Fourier identities hold exactly after expansion in exponentials; ordinary angular quadrature agrees with all three moments and the determinant to about1e-15 and5e-18 respectively. Opus review of this added argument is pending; no statement about an unknown exact branch follows.

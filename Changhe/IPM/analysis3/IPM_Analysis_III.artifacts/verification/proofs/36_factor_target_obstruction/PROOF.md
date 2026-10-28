# The factor-to-density target mismatch in the S0 realization

This proves a corrected form of Prop IV.O in the theory author snapshot. The background is the exact modal trial of V005, with full normalized linearization

    Lh=(V.grad-1)h+(U[h]+c[h]X/3).grad rho0.

Write t=log r, C(theta)=cos^2(theta)sin(theta), D=X.grad=partial_t and Omega=partial_theta. The S0 remainder norm is equivalent, up to fixed Fourier normalization constants, to

    ||b||_X^2 = int W(t)(|b|^2+|Db|^2+|Omega b|^2+|D Omega b|^2) dt dtheta,
    h=r^3 C(theta)b.

The target has the same mixed norm on G=r^-3 f. Its radial weight W is comparable to r^-2 near0, equals1 on the central interval, and is comparable to r^(2(3-gamma)) at infinity, where gamma=(3k-1)/2. The domain also has the specified J, KP and TAU coordinates; all constructed packets have these coordinates zero.

Take the maximal domain of elements of X for which the canonical velocity is defined, belongs to H^1_loc, and the distribution Lh belongs to Y. The local regularity condition on U holds for the stated remainder and finite tail coordinates: localize h, use the order-zero Fourier multiplier on the local H^1 part, and differentiate the separated, sublinear far integral. The proposition is about this domain. L is not defined as a bounded X-to-Y map on all of X.

## 1. The range has a closed infinite-codimensional trace restriction

On any compact t interval, mixed H^1_t H^1_theta gives a continuous trace map at theta=pi/2 into H^1_t. In the sine expansion the trace is

    G(t,pi/2)=sum_(N>=0) (-1)^N G_N(t).

Cauchy-Schwarz bounds its squared H^1_t norm by

    [sum_(N>=0) (1+(2N+1)^2)^-1] ||G||_Y^2.

The trace map is onto the radial weighted H^1 space: use G(t,theta)=a(t)sin(theta). Its kernel Y0 is therefore closed and has infinite codimension.

For a smooth factor b, Lh has zero trace since h, grad h and grad rho0 vanish on x=0. The same conclusion holds on the maximal domain, without assuming a classical trace of grad h. Indeed, V is tangent to the axis and its angular coefficient v=V.grad(theta) is O(cos theta). The transport terms other than v C b_theta have zero H^1_theta trace, using b and b_t in H^1_theta and C=O(cos^2 theta). The coupling and strain terms have zero trace because U is locally H^1 and grad rho0 and X.grad rho0 vanish on the axis.

The remaining term v C b_theta has the form a^3 q(t,theta)b_theta, where a=cos theta and q is locally bounded. Since the whole image is in Y, this term has an H^1_theta representative for almost every t. Its trace must be zero: a nonzero continuous trace would force |b_theta|>=c|a|^-3 near the axis, contradicting b_theta in L^2_theta. Thus Lh lies in Y0. Surjectivity onto Y is impossible.

## 2. Exactly zero-strain axis packets

Choose a nonzero smooth eta compactly supported in a fixed open subinterval of (t_minus,t_plus), and put

    beta(t)=exp(-2t) eta'(t).

Then int exp(2t) beta(t)dt=0 exactly. Choose a nonconstant even smooth phi supported in(-1,1), and define globally

    b_epsilon(t,theta)=beta(t)phi(cos(theta)/epsilon),
    h_epsilon=r^3 C(theta)b_epsilon,

for0<epsilon<1/4. This has the required x-even, y-odd parity. It is smooth and compactly supported away from0; J=0. The strain integral separates into the zero radial moment above and an angular integral. Hence c[h_epsilon]=0 exactly, with no compensator and no KP term.

The support has angular width comparable to epsilon. Derivatives in t have bounded profiles, whereas a nonzero angular derivative of b_epsilon has size epsilon^-1. Consequently

    c epsilon^-1/2 <= ||h_epsilon||_X <= C epsilon^-1/2.             (1)

The physical density and its mixed D,Omega derivatives satisfy

    ||h_epsilon||_L1 <= C epsilon^3,
    sum_(i,j in{0,1}) ||D^i Omega^j h_epsilon||_L2 <= C epsilon^3/2. (2)

The first angular derivative costs epsilon^-1, but the factor cos^2 theta supplies epsilon^2. These estimates include the t-theta mixed derivative, which is required by the actual S0 norm.

## 3. Transport and complete nonlocal image

On the fixed annulus, all needed background derivatives are bounded and v=V.grad(theta)=cos(theta) v1 with v1 smooth. Therefore v partial_theta b_epsilon is a bounded scaled profile; its first theta derivative costs only epsilon^-1. The radial transport and zeroth-order terms have the same structure. Multiplication by C(theta) then gives

    ||(V.grad-1)h_epsilon||_Y <= C epsilon^3/2.                    (3)

For the coupling on a fixed larger annulus, use the full mixed norm, not merely the isotropic H^1 bound. Each component of U has a bounded homogeneous degree-zero Fourier multiplier m. D commutes with it. The commutator [Omega,U] has multiplier given, up to the Fourier convention's sign, by the angular derivative of m, again bounded and homogeneous of degree zero. D commutes with that multiplier as well. Thus

    sum_(i,j in{0,1}) ||D^i Omega^j U[h]||_2
      <= C sum_(i,j in{0,1}) ||D^i Omega^j h||_2.                  (4)

Multiplication by the smooth background gradient and the bounded radial weights on this annulus preserves the mixed norm. Equations(2) and(4) bound the local coupling by C epsilon^3/2.

The two nonlocal ends require separate estimates. In a disk separated from the packet support, the velocity kernel can be differentiated and Taylor expanded. Parity forces U(0)=0 and excludes quadratic terms. Its linear term is diag(-c,c), which vanishes here. Hence, with the same estimates after D and Omega,

    U[h_epsilon]=O(epsilon^3 r^3),
    U[h_epsilon].grad rho0=O(epsilon^3 r^5).

After division by r^3 the squared target integrand is O(epsilon^6 r^4 r^-2)dt, integrable at0. At infinity, the integral of h_epsilon is zero by y-odd parity. The degree-minus-two velocity kernel then has its leading monopole cancelled, giving

    U[h_epsilon]=O(epsilon^3 r^-3),
    U[h_epsilon].grad rho0=O(epsilon^3 r^(k-4)),

again with D and Omega derivatives. The squared target integrand has radial exponent2(k-4-gamma)<0 in dt. Both ends therefore contribute at most C epsilon^3 to the target norm. The full strain term is exactly zero.

Combining these estimates proves h_epsilon lies in the full operator domain and

    ||L h_epsilon||_Y <= C epsilon^3/2,
    ||L h_epsilon||_Y / ||h_epsilon||_X <= C epsilon^2.             (5)

There is no same-norm inverse estimate even with target Y0. The packets can also be approximated by finite cosine sums; the exact zero radial strain moment is preserved at every angular truncation. Thus the obstruction is compatible with the finite-mode approximation procedure.

## 4. Scope and repairs to the submitted argument

The conclusions of Prop IV.O are CONFIRMED for the explicit maximal realization above. The original proof needed the mixed multiplier estimate(4). An isotropic H^1 estimate does not control D Omega and therefore was insufficient. The original strain compensator argument also cannot bound the complete Y image of the compensator separately: a nonzero-strain compact function has a forbidden growing far contribution in L. The radial moment choice removes that problem exactly.

The finite S0 matrix remains a legitimate finite statement if its entries and norm comparisons are certified. Its positive smallest singular value cannot be uniform as the angular space resolves these packets. This says nothing by itself about a factor-to-factor target or a Hilbert realization using the same physical density weight on both sides.

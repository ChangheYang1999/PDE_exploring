# Rational scaled fields and full-plane weak tests

## Exact function class

Fix rational c>1 and gamma=1/c, delta=1-gamma. All potential coefficients
are exact rationals. Let S=1+r^2, t=r^2/S, v=1-t=1/S and
p_j=(3+gamma-j delta)/2. The finite generator family consists of

    chi=H_m(x,y) S^(p_j-m) t_R^w u_R^Q P_n(2t_R-1),
    H_m=Re(x+i y)^(2m),
    t_R=r^2/(R^2+r^2), u_R=R^2/(R^2+r^2),

with integers j,m,w,Q,n>=0 and rational R>=1. Here P_n is the Legendre
polynomial. The mono and leg generators are the corresponding R=1,
Q=0 special cases, and mono has n=0. Only R=1,10,100 are needed for
candidate010. Every generator is smooth on the Cartesian plane.

Put a=R^2-1 and L(t)=R^2-a t=1+a v. Since L>=1 on[0,1], no added
radial denominator has a zero on the integration interval. Direct
substitution gives

    chi=S^p_j cos(2m theta) A(t),
    A(t)=t^(m+w)(R^2 v)^Q P_n(2t/L-1)/L^(w+Q).         (1)

Thus A is a rational polynomial divided by nonnegative integer powers
of1+99v and1+9999v. Finite sums, products and derivatives preserve
this class. Their numerator coefficients and denominator powers are
kept exactly. Equality is checked after multiplying by the common
denominator, and any division by t^k requires its first k numerator
coefficients to vanish exactly. The denominator is nonzero at t=0.

## Cartesian differentiation

Represent a derivative of total order d in one branch as

    S^p r^(-d) A(t) trig_n(theta).                       (2)

Since r partial_r t=2t(1-t), its radial derivative numerator is
[2t(1-t)A'+(2pt-d)A]. Combining partial_x=cos theta partial_r
-sin theta r^(-1)partial_theta and partial_y=sin theta partial_r
+cos theta r^(-1)partial_theta with the elementary sum and difference
identities gives the same finite recurrence as the polynomial case.
For x differentiation, writing C=t A'+t(pA-t A'), the two shifted
numerators at n-1 and n+1 are C+(n-d)A/2 and C-(n+d)A/2.
For y differentiation of sine, these have signs plus and minus; for
y differentiation of cosine, signs minus and plus. Negative sine
frequencies reverse their sign, negative cosine frequencies do not,
and sine frequency0 vanishes. The target trigonometric kind changes
under y differentiation only. This derivation is valid for rational A
because its denominator is positive on the interval.

Apply this recurrence to rho=-chi_xxy-chi_yyy, u1=-chi_xyy,
u2=chi_xxy, rho_x and rho_y. Mixed derivative commutation and direct
Cartesian Taylor-jet evaluations give independent algebraic and point
checks. Source coefficients are never rounded during reconstruction.

## Weak-test statement and hypotheses

Let R denote this smooth reference density, F=c x dot grad R+u[R]
dot grad R-R, with the canonical divergence-free velocity
u[R]=(-chi_xyy,chi_xxy). Let h be an S1-symmetric L2 distributional
correction satisfying the stationary equation at this same c. Require
the canonical extension U[h] in L2, with divergence0 and
||U[h]||2<=||h||2. All products in the weak equation must be defined
by their locally integrable representatives.

Choose an odd positive integer n and rational polynomial P(t) divisible
by t^((n-1)/2), and put

    phi=r v^2 P(t) sin(n theta).

It is smooth at the origin, decays as O(r^-3), and has bounded gradient.
Set

    Mfield=(2c+1)phi+(c x+u[R]) dot grad phi,
    Cfield=phi grad R,
    I=integral_R2 F phi, M=||Mfield||2, C=||Cfield||2,
    H=||grad phi||infinity.

Assume the displayed integrals are finite and justified by the cutoff
limit. The finite rational backend checks their endpoint powers. At
infinity the reference and its velocity are O(r^gamma), gamma<1,
so the reference integration-by-parts boundary terms vanish. The L2
correction terms pass to the limit by Cauchy-Schwarz, with the bounded
probe gradient for the quadratic product.

Testing the correction equation gives

    |I| <= (M+C)||h||2+H||h||2^2.                       (3)

Indeed, the linear transport terms integrate to -integral h Mfield
because div(c x+u[R])=2c. The linear velocity correction is bounded
by C||U[h]||2. Divergence0 changes the quadratic transport term to
-integral h U[h] dot grad phi, whose magnitude is at most H||h||2^2.
This proves (3). If L<=|I|, M<=Mbar, C<=Cbar and H<=Hbar, with
L>0 and nonnegative finite upper bounds, then

    ||h||2 >= 2L/[Mbar+Cbar
           +sqrt((Mbar+Cbar)^2+4Hbar L)].               (4)

Containing intervals and strictly smaller rational floors make this a
certified necessary distance. This is not a sufficient existence test.
The extension to another c needs the separately audited tail-pinning
theorem and is not implied by this weak calculation alone.

## Finite fields and exact whole-plane radial moments

The same trigonometric product identities used above assemble every
component of Mfield and Cfield as

    r v^2 sum_(ell,kind,k) v^(ell delta/2) A_(ell,kind,k)(t)
                                  trig_k(theta),       (5)

where each A is a rational function of the class(1). All output
frequencies are odd positive integers. A complete norm includes every
angular frequency and every radial branch pair at the same frequency.
Orthogonality gives angular factor pi, and r dr=-dv/(2v^2) gives

    integral |field|^2
      =pi/2 sum_pairs integral_0^1
         v^(1+(ell+ell')delta/2)(1-v) A(1-v)B(1-v) dv,  (6)

where distinct branch pairs have multiplicity2. Vector components are
added in squared norm. The density itself has form
R=r sum_(ell>=1,k) v^(ell delta/2) A_(ell,k)(t) sin(k theta).
Consequently integration by parts yields an independent pairing

    I=-integral R Mfield
      =-pi/2 sum_pairs integral_0^1
        v^((ell+ell')delta/2-1)(1-v) A(1-v)B(1-v) dv.    (7)

A direct residual projection gives a second evaluation: construct
F/r from c x dot grad R-R and u[R] dot grad R using the complete
Cartesian derivatives, retain the output sine n coefficient, then
multiply by P. It has the same radial measure as(7). Requiring the
two containing pairings to overlap catches sign and normalization
errors without deriving one pairing from the other.

For(6) the exponent is at least1. For(7) the density index ell>=1
ensures exponent>-1. All terms are separately integrable here.
After multiplying by1-v and collecting positive rational poles, each
radial integral is exactly the scalar moment proved in
../rational_pole_moments/PROOF.md. Its exact partial-fraction replay
and outward moment evaluation preserve all cancellations within the
finite expression. Any low-accuracy result remains unaccepted.

For H, direct polar differentiation gives

    partial_r phi=v^2[(1-4t)P+2t(1-t)P'] sin(n theta),
    r^(-1)partial_theta phi=n v^2 P cos(n theta).

Hence the maximum of the absolute radial polynomial and angular
polynomial bounds the Euclidean gradient, since sin^2+cos^2=1.
Exact Bernstein subdivision on[0,1] certifies these two polynomial
bounds, as in ../angular_probe_audit/PROOF.md. No scaled background
quantity enters H.

## Verification and scope

First verify rational arithmetic and Cartesian derivatives on mixed-scale
manufactured potentials against the independent Cartesian Taylor-jet
engine. Check the R=1 specialization coefficientwise against the
previously audited polynomial Radial engine. Then calibrate the full
weak pairing, M, C and distance on the independently confirmed007
record before applying the same procedure to010. Bind exact candidate
and immutable snapshot hashes and retain field hashes, moment counts,
endpoint powers, containing intervals, Bernstein leaves, independent
comparisons and real execution times.

A test result is recorded separately from this proof. No candidate-level
certificate is available until its full computation and independent
review are complete. All large input coefficients remain in their exact
JSON source. This backend introduces no generated numeral-filled proof
source and uses no quadrature or finite-radius truncation.

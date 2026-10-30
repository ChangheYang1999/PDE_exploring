# Weighted membership of the rounded candidate 007

## Exact objects and statement

Keep the exact exponent

    c = 4076476460239181 / 2251799813685248.

Let chi_b be the exact mathematical potential obtained by replacing each
coefficient of C1-N1-007-d2w-j7-e2bal with its correctly rounded binary64
value, interpreted again as an exact rational number. The generators and
c remain exact and unchanged. This is the realization defined and
independently confirmed in ../rounding_realization/PROOF.md. It isolates
coefficient conversion; it does not model every floating arithmetic
operation in an evaluator.

Set rho_b=-partial_y Delta chi_b, u_b=(-chi_b,xyy,chi_b,xxy), and
F_b=(cX+u_b).grad rho_b-rho_b. For a>=0 define

    W_a(F_b) = ||(1+r^2)^(-a/2) F_b||_2,
    N_a(F_b) = ||(1+r^2)^((2-a)/2) Delta F_b||_2.

Then both quantities are finite if and only if

    a > a_crit = 2/c = 4503599627370496/4076476460239181.   (1)

In particular neither is finite at a=0, 1/4, 1/2, 3/4 or 1.
For a<=a_crit, F_b is not in the registered dyadic space Y, since its
weighted low component is infinite (any fixed positive radial scale
has the same membership threshold). This last assertion does not
claim the converse for Y, whose velocity and fractional components
must also be defined and controlled.

The exact rational published candidate has the leading sector in this
proof equal to zero. Equation (1) is not a statement about that candidate.
A finite-radius quadrature diagnostic of rounded coefficients can still
approximate the published candidate on its finite domain. Its limit as
the radius tends to infinity cannot supply a finite whole-plane norm in
the weights excluded by (1).

## Leading sector and differentiable remainder

The independently confirmed rounding record gives

    F_b(r,theta) = r^alpha A(theta) + O(r^(alpha-epsilon)),
    alpha = 2/c-1 = 427123167131315/4076476460239181,
    ||A||_(L2(0,2 pi)) > 0,                              (2)

for some epsilon>0. It is the residual sector (h,q)=(1,0).
The nominally preceding (0,0) sector vanishes exactly. The record
retains the nonzero norm of A, approximately 7.17546119049e-13,
with an outward enclosure. A is a finite sum of positive odd sine
harmonics, since the residual is S1 and the generator list is finite.

The single-scale rational generators have convergent expansions in
r^-2 for r>1, with only finitely many fractional prefactors. Their
products have the same property. The expansion can therefore be
differentiated twice, uniformly in theta on every exterior r>=R>1.
In particular the twice-differentiated remainder in (2) is
O(r^(alpha-epsilon-2)). These bounds also follow from the finite
analytic factors after extracting the first omitted radial power;
no asymptotic truncation is used as a numerical error certificate.

By the polar Laplacian,

    Delta F_b = r^(alpha-2) B(theta)
                   + O(r^(alpha-epsilon-2)),
    B = alpha^2 A + A''.

Write A=sum_(n odd, n>=1) A_n sin(n theta). Since 0<alpha<1,
every multiplier alpha^2-n^2 is nonzero, and orthogonality gives

    ||B||_2^2 = pi sum_n (n^2-alpha^2)^2 |A_n|^2
                 >= (1-alpha^2)^2 ||A||_2^2 > 0.          (3)

Thus differentiation cannot remove this leading sector. A harmonic
exception would require an integer radial exponent matching a
nonzero angular mode; it is excluded explicitly here.

## Radial integrability and divergence

Equations (2) and (3), including their uniform remainders, imply that
for sufficiently large r the angular L2 norms of F_b/r^alpha and
Delta F_b/r^(alpha-2) are bounded above and below by positive constants.
For either W_a squared or N_a squared, the radial integral is therefore
bounded above and below by positive multiples of

    integral_R^infinity r^(2 alpha+1-2a) dr.

It converges exactly when 2 alpha+1-2a<-1, equivalently
a>alpha+1=2/c. At equality the divergence is logarithmic. Below the
threshold it grows with a positive power of the truncation radius.
Every compact-region contribution is finite: the real denominators
of the generators are positive, so the fields are smooth at the origin
and throughout the plane. This proves both directions of (1).

For the dyadic low component replace 1+r^2 by 1+r^2/Rw^2 for any
fixed Rw>0. The quotient of the weights tends to a positive constant
at infinity, so this does not change the divergence threshold.

## Evidence and scope

The small checker reads the already confirmed exact rounding record,
checks its source identities and leading-sector exponent, and encloses
a_crit and the positive lower coefficient in (3). It performs no
quadrature and no coefficient refit. The existing sector certificate,
its independent peer record, this proof and the checker are hashed
in the output. The analytic implication above requires an independent
review before its new membership conclusion is marked confirmed.

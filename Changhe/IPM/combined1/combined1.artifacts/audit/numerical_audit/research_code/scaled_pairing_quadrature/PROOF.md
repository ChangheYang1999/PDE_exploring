# Exact radial pairing errors for scaled candidates

## Statement, hypotheses and notation

Fix c = 4076476460239181/2251799813685248 and delta = 1 - 1/c.
Use an immutable exact candidate whose potential is a finite rational sum
of the generators

 chi = sum a_(j,m,w,N,q,R) H_m (1+r^2)^(2-(j+1)delta/2-m)
                       t_R^w u_R^q P_N(2t_R-1),
 H_m = Re(x+iy)^(2m), t_R = r^2/(R^2+r^2), u_R = 1-t_R,
 R in {1,10,25,50,100}, j,m,w,N,q nonnegative integers.

P_N is the Legendre polynomial normalized by P_N(1)=1. Exact input
hashes, all coefficients and all generator shapes identify the function.
Define rho = -chi_xxy-chi_yyy, u = (-chi_xyy,chi_xxy) and
F = (cx+u1)rho_x + (cy+u2)rho_y - rho. All these fields are smooth
on the plane because H_m is polynomial and all denominators are positive.
They have the S1 parity, so F has only odd sine angular frequencies.
Set t = r^2/(1+r^2), v = 1/(1+r^2). For an odd positive n, let

 F_n(r) = (1/pi) integral_0^(2pi) F(r,theta) sin(n theta) dtheta
        = r sum_ell v^(ell delta/2) A_ell(t),
 A_ell(t) = P_ell(t)/product_a (1+a(1-t))^(p_(ell,a)),
 a in {99,624,2499,9999}, p_(ell,a) nonnegative integers.

The exact compact rational construction in joint_scaled_factored_weak
provides the complete finite sum. All linear terms and every compatible
velocity-gradient pair must be included. Assume, and check for every
nonzero group, b_ell = ell delta/2 - 1 > -1. The exact rational pole
functions then have no singularity on the closed integration interval.

For K >= (n-1)/2 define phi_(n,K) = r v^2 t^K sin(n theta). Its full
pairing is I_(n,K) = integral_(R^2) F phi_(n,K) dX. Given finitely many
positive exact rational radii r_i and weights w_i, define

 Q_(n,K) = pi sum_i w_i t_i^(K+2)
                             sum_ell v_i^(ell delta/2) A_ell(t_i),
 t_i = r_i^2/(1+r_i^2), v_i = 1/(1+r_i^2).

The assertion is that the exact formulas below compute I and Q. Outward
interval enclosures of the formulas give an enclosure of Q-I for this
particular exact candidate and these recorded nodes. No claim uniform
in coefficients or in optimizer iterations is made. Each actual result
requires its own source bindings and independent numerical reproduction.

The initial candidate application is C1-N1-021-heldin14-legqs25p50,
raw SHA256 c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8.
Its n=19 rows K=137,521 are objective rows, whereas K=1800 is outside
the recorded analytic objective span. Its n=21 rows K=138,522 are
objective rows. Mode1 exponents are classified against the complete
81-row metadata before comparison. Classification has no effect on the
integral identity. The earlier independent source history is retained
in candidate021_holdout/PROOF.md and its exact result record.

## Complete pairing and finite-sum identities

The sine orthogonality formula over the full circle is
integral sin(n theta)sin(m theta) dtheta = pi if n=m and zero otherwise.
It removes every residual mode except n. Since r dr = dt/(2v^2) and
r^2 = t/v, the integrand F_n r v^2 t^K r dr gives

 I_(n,K) = (pi/2) sum_ell integral_0^1
       v^(ell delta/2-1) (1-v)^(K+1) A_ell(1-v) dv.        (1)

The displayed integrals converge absolutely: at v=0 the only possibly
negative exponent is b_ell > -1; at v=1 the exponent K+1 is nonnegative;
the rational denominator has a positive minimum on [0,1]. The sum is
finite, so no exchange of infinite sums or integrals is required. At
r=0, phi is smooth because r^(2K+1)sin(n theta) is Im(x+iy)^n times
(r^2)^(K-(n-1)/2), divided by the positive smooth power (1+r^2)^(K+2).

Writing the same radial integral using ds=dr/r gives the summand
pi r^4 v^2 t^K sum_ell v^(ell delta/2) A_ell(t).
Since r^4 v^2=t^2, replacing its ds integral by the finite weighted sum
at (r_i,w_i) gives Q exactly as defined. This step defines the rule;
it assumes no Gaussian exactness and no bound on its error. Once I and
Q are both enclosed, interval subtraction encloses the actual total
error Q-I, including the effects of the omitted origin and exterior.
It does not separately attribute that total error to these domains.
Angular integration in both quantities is analytic, so this comparison
contains no floating angular summation.

## Exact full-interval evaluation

Compose P_ell(1-v) exactly. The integrand in (1) consists of a rational
function with positive linear factors, multiplied by v^b(1-v)^(K+1).
Exact polynomial division and partial fractions express the rational
factor as a polynomial plus finitely many constants/(1+a v)^j.
Multiplying back by the complete denominator must give the original
numerator exactly. Polynomial terms integrate by

 integral_0^1 v^(b+d)(1-v)^m dv = B(b+d+1,m+1).

Each pole term integrates by the Euler identity

 integral_0^1 v^b(1-v)^m/(1+a v)^j dv
   = B(b+1,m+1) 2F1(j,b+1;b+m+2;-a),
 b>-1, m>=0, a>0, j>=1.

This identity follows directly from the defining convergent Euler
integral for 2F1. The accepted factored_pole_moments proof and finite
calibration establish the outward evaluation and the pole-order
recurrence used here. The checker replays each exact decomposition and
compares recurrence and direct moment enclosures for every required
pole term. No radial cutoff or quadrature is used in (1).

At every finite node, evaluate P_ell(t) and the independently composed
P_ell(1-v) with outward coefficients, divide by the same positive pole
powers, and require overlap. These two evaluations are an arithmetic
consistency check of an exact polynomial identity. Sum the complete
branches before multiplying by t^(K+2). Require sufficient relative
accuracy in every nonzero radial amplitude and in each final pairing.
If cancellation defeats that check, the computation remains incomplete.

## Recorded rules and comparison with the optimizer

Use the exact binary64 radius and weight rationals already retained in
weak_radial_quadrature/verification/nodes_mid16.json, nodes_mid24.json
and nodes_mid32.json. They were constructed from equal log-radius
panels between log(0.02) and 16, with the stated Gauss-Legendre order,
then filtered to 0.02 <= r <= 10000. The last retained panel may be
partial. N4-159 independently checked these files and all earlier007
finite sums; this transfers the node identity, not an error bound for
any new candidate. Current copied N1 whole_axis_radial source and the
copied prior source have the same function body. The optimizer records
MID16 and 212 retained radial nodes for021. These facts do not certify
floating node construction as an ideal Gaussian rule.

The raw metadata I_k_final_mesh comes from the optimizer's floating
coefficient vector before finalize_exact. The immutable raw coefficients
have already undergone that exact projection. Therefore comparing that
metadata number with Q for the exact raw candidate is a diagnostic of
several effects together: coefficient projection, floating field and
angular evaluation, and implementation differences. It is not a bound
for any one effect. Comparing Q with I for the same exact raw candidate
is the certified finite-rule error calculation addressed by this proof.
Current publisher source has later per-row weighting changes. It is
read as supporting source text, never asserted to be historically
executed021 bytes. The completed021 log and immutable metadata supply
the actual row list and run settings.

## Dependencies, verification and scope

The exact generator calculus, Cartesian checks and moment calibration
are bound by joint_scaled_factored_weak/PROOF.md, its fields.json,
scalar_joint.json and candidate013.json records, and the positive-pole
moment certificate. N4-316 provides an independently constructed own
full-plane n=19,K=1800 value for actual021, still awaiting peer review.
The n=19 application must reproduce both its exact projection hash and
its full pairing enclosure. The recorded-node acceptance is N4-159.
Every input file and executed own implementation is hash bound.

This result concerns an exact field and finite sums. It supplies no
stationary solution, inverse, background bound, correction distance,
optimization minimum or explanation of an optimizer's behavior. In
particular a small contribution w I^2 alone is not a proof that a row
has no effect on a computed step. All new candidate results remain
OPEN until the independent audit has been completed.

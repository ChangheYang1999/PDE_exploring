# The retained radial shape in the profile-velocity closure test

Status: an independent T4 derivation, written before the numerical
checker. The scalar integration identity was already audited in
T4-381 and its review acceptance391. This application needs review.

## Exact statement and hypotheses

Retain the endpoint expansion and all stationary-reference hypotheses
of T4-335 and CI351. In particular -5<q<-3, delta>0,
D=1-c(q-delta)>0, H=H_q(h) is finite, and a reference gradient
coefficient satisfies G>=g0>0. The angular endpoint equation gives

 b=(A+tP)/(4c), B=dist_(L2(S1))(A,span(P))/(4c)>0,
 H>=H0>0.

The L2 circle measure is dtheta on [0,2pi]. H_q is the maximum of
sup(1+r)^(-q)|h| and sup(1+r)^(1-q)|grad h|. The velocity is the
canonical IPM velocity, with its local/contact term. Assume the
CI351 error majorant retains at least the nonnegative summand

 ehat(r) >= H(V+E G)r^(-delta)/D,  V>=v0>=0, E>0.       (1)

Here E is the coefficient being used in this sufficient error estimate.
This is a hypothesis on the chosen majorant, not a claim that E is a
lower bound for the true velocity of a stationary correction. The
square of the certified distance lower bound is

 I=integral_(R,infinity) [B-sqrt(2pi)ehat(r)]_+^2 r^(2q+1)dr,

with R>=0 and [x]_+=max(x,0). Set alpha=-2q-2>0 and

 S=2delta^2/[alpha(alpha+delta)(alpha+2delta)],
 r0=[sqrt(2pi)H0(v0+E g0)/(D B)]^(1/delta).

Then

 sqrt(I) <= B r0^(q+1) sqrt(S).                         (2)

Consequently reaching a target beta>0 with this certificate requires

 E <= [D B/(sqrt(2pi)H0)]
          [B sqrt(S)/beta]^(delta/(-q-1))/g0 - v0/g0.  (3)

If the right side is nonpositive, no E>0 reaches beta. A finite
starting radius, a positive remainder or any additional nonnegative
summand in ehat can only reduce the left side of (2).

## Proof

By (1) and the lower bounds on H, V and G,
sqrt(2pi)ehat(r)>=B(r0/r)^delta. Monotonicity of the positive part
bounds the integrand by B^2[1-(r0/r)^delta]_+^2 r^(2q+1).
Extend its lower endpoint to zero, substitute r=r0 u, and integrate
on u>=1. This gives

 I <= B^2 r0^(2q+2)
       [1/alpha-2/(alpha+delta)+1/(alpha+2delta)].

The bracket equals S by exact rational algebra. It is positive, so
taking square roots proves (2). Since q+1<0, (2) is strictly decreasing
in v0+E g0. Solving beta<=B r0^(q+1)sqrt(S) for E gives (3).
The weaker cutoff test replaces sqrt(S) by 1/sqrt(alpha), losing
the factor sqrt(alpha S). Thus passing that weaker test is not
sufficient to pass (2).

## Application to the three exact endpoint references

Use c=4076476460239181/2251799813685248, q=1/c-4,
delta=1-1/c and D=5c-1. Exact endpoint data for 007,013,014
are copied from the accepted T4-381 inputs and hash-bound below.
The pointwise argument380 gives H0>=999775,999745,999748,
respectively. To preserve conservative upper bounds in (2) and(3),
use precisely these integers, after checking them against the full
Arb pointwise formula. Set g0=Theta0'(0)=sum_n n Theta0,n.
The optional v0 is the absolute leading reference velocity at
angle zero, computed from its exact homogeneous Poisson solution.
These lower bounds are the same audited inputs as380/381.

The tested coefficient is E=583/1000. Although402 proves this only
asymptotically, assume it holds on the entire needed exterior with
zero remainder. This deliberately favorable hypothetical majorant
already lets (2) decide whether further remainder work could suffice
without improving the coefficient. The checker computes both v0=0
and the optional positive v0. It also computes thresholds(3) for the
fixed sharpw ball1351/1024000000, the rounded sharpw family ceiling
28496/10^10, the TB ceiling3793/10^9 and the original graded ceiling
25/54684. These are named targets, not interchangeable norm radii.

Only inequalities printed with enclosing rational bounds in the JSON
are asserted as numerical certificates. Pointwise-profile coefficients
around0.372 in the independent T2 review are FLOAT diagnostics and
are not proved here.

## Scope

Failure of(2) to reach beta means that this particular CI test using
the constant0.583 cannot certify that target. It is not a bound on
actual solution distance, is not nonexistence, and does not rule out
an improved coefficient, a profile-dependent majorant, or another
existence theorem. Replacing the coefficient by the actual angular
velocity profile may be useful and is a separate task.

## Independent review acceptance

The full independent T2 review is frozen as source/review.md. It
confirms the integral, monotonicity, threshold inversion and all
204 numerical checks. Its independent code was read in full and is
not executed here. The acceptance checker rechecks all directed
non-FLOAT tables, with both integer H0 and pointwise Phi, using
the existing certified endpoint intervals and exact g0,v0. It also
checks the peer's seven algebraic identities and source bindings.
The hypothetical0.583 ceiling and all four failures are now AUDITED.

The review's additional section4 discussion of a radius-dependent
coefficient is not accepted simply by substituting a pointwise
coefficient into a term obtained after radial integration. That
coefficient must first be averaged with the radial Green weight.
This is treated separately in the radius-dependent audit. The
original414 theorem and all its arithmetic are unaffected. No
claim here equates a sufficient coefficient with the actual
velocity, and the zero-remainder assumption remains explicit.

Collaboration used the theory lane configured for Claude Opus5.5;
actual provider identity is not observable here.

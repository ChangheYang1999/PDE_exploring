# Acceptance of the universal velocity lower bound and retained-integral cap

## Statement and hypotheses

Retain the exact canonical IPM velocity and weighted norm H_q of
../universal_velocity_lower/PROOF.md, with -5<q<-3. Suppose E is a
constant valid for every centrally odd C1 function of finite H_q,
or for every such S1 function, at all sufficiently large radii with a
fixed starting radius. Then E>=(-q-1)/(2(-q)(-q-3)). This is precisely
T4-381 Sections1 and2. The independent R1-040 review confirms this
full q interval; the earlier T2 review stated a narrower interval
containing the campaign exponent, so no extrapolation of that review
is needed.

For the cap statement assume all endpoint and canonical-velocity
hypotheses of T4-335, its three-cutoff application338/339, and CI351.
Use the notation of T4-380: c>1, gamma=1/c, delta=1-gamma,
q=gamma-4, D=1-c(q-delta)>0, alpha=-2q-2>0. Let B>0 be the
angular projection bound, H>=H0>0 its necessary pointwise gradient
budget, G>=g0>0, and V>=v0>=0 the optional velocity coefficient.
The nonnegative errors in CI include sqrt(2pi)H(V+EG)r^-delta/D.
Write E0=(-q-1)/(2(-q)(-q-3)) and

 r0=[sqrt(2pi)H0(v0+E0 g0)/(DB)]^(1/delta).

Then the square root of the full CI integral is at most

 B r0^(q+1) sqrt[2delta^2/(alpha(alpha+delta)(alpha+2delta))].

For the accepted exact007,013,014 endpoint data this is strictly below
1.421e-7 with v0=0. With their separate accepted positive velocity
lower bound it is below1.124e-7. The weaker cap obtained by dropping
the radial shape is below1.2485e-6 with v0=0. Each is below the
fixed sharpw radius1351/1024000000 and every registered family ceiling.
These are upper bounds on what this certificate can exclude, not
upper bounds on the actual solution distance.

## Complete argument

The admissible test h=y(1+r)^(q-1)/(-q) is C1 and S1. Its weighted
amplitude is at most1/(-q), and its weighted gradient is
sqrt([((1+qr)/(1+r))^2 sin(theta)^2+cos(theta)^2)/(-q), bounded by1
with limit1 on the y-axis. Thus H_q(h)=1. Its moment is
M=(0,6pi/[a^2(a-1)(a-2)(a-3)]), a=-q. The canonical first-sine
potential is -sin(theta)/2 times
[r^-1 integral_0^r s^2f(s)ds+r integral_r^infinity f(s)ds],
f=r(1+r)^(q-1)/a. Subtract the exact dipole from the first integral.
The remaining leading potential is r^(q+2)sin(theta)/[a(q+1)(q+3)],
with error whose derivatives through order2 are O(r^(q+1-j)).
Direct Hessian differentiation gives velocity divided by r^q equal to

 (cos(theta)[1+(q-1)sin(theta)^2],
  -sin(theta)[1+(q-1)cos(theta)^2])/[a(q+3)]+O(r^-1).

At theta=pi/4 its norm tends to E0. Applying the assumed universal
estimate and passing to infinity proves E>=E0 for every fixed
starting radius.

In CI the full positive part is no larger than
B[1-(r0/r)^delta]_+, since H>=H0, V>=v0 and EG>=E0g0, and
all omitted errors are nonnegative. Extending the integration from
its actual starting radius to0 only increases it. Substitution r=r0s
gives the displayed cap because

 integral_1^infinity (1-s^-delta)^2s^(2q+1)ds
 =1/alpha-2/(alpha+delta)+1/(alpha+2delta)
 =2delta^2/[alpha(alpha+delta)(alpha+2delta)].

All exponents are integrable and r0 is positive. Decreasing E,H,G,V
or increasing B enlarges the cap. Thus the independent interval
calculation uses the upper endpoint of B and lower endpoint of H0,
with exact rational g0,v0 and E0. The review's exact Fraction parser
preserves both endpoints of every printed Arb interval. Its mpmath
interval operations and extraction of binary endpoints are outward;
FLOAT checks A5 and C1 are diagnostics and are not used in this proof.
The already accepted T4 Arb calculation supplies a separate numerical
path. Both computations agree on all stated strict caps.

## Verdict and scope

R1-040 is CONFIRMED, including its Section3 cap review. T4-381 is
AUDITED in full, because T4-375 has now separately been accepted in
385. The review's conditional dependency is fulfilled. Its exclusion
of claims about normalization-restricted domains was its stated
scope, not a refutation of the separately proposed384. That extension
still needs its own acceptance. No stationary-only velocity estimate,
stationary H_q upper budget, inverse or existence statement is proved.
No foreign code was executed for this acceptance. Source files and
previous independent outputs are bound in verification/manifest.json.

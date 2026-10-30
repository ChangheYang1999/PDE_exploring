# Pointwise endpoint gradient budget and its conditional CI thresholds

Status: independent audit of the new pointwise estimate in the T2 theory worker's
`t4_375_review.py`, Parts D and E. Its hypotheses and its numerical
witnesses are audited separately from the proposed improved velocity
constant. The proof is written before the specialization checker.

## 1. Exact statement and pointwise minimization

Assume all hypotheses of T4-335 Section 2 and T4-375 Sections 1 to 3.
In particular c>1, gamma=1/c, delta=1-gamma, q=gamma-4, h is a real
S1 C1 stationary correction in the specified canonical chart, and
H=H_q(h)<infinity. The reference has the growth and differentiated
remainder bounds in T4-335 (5). Its endpoint functions A and P are
real C1 functions on the circle, and P is not identically zero. Put

    b=(A+tP)/(4c),  t=(integral y h)/pi,
    u(theta)=(q A(theta),A'(theta)),
    v(theta)=(q P(theta),P'(theta)).

For every theta with v(theta) nonzero,

    H >= Phi(theta)
      = |q| |A P'-A' P|/(4c sqrt(q^2 P^2+P'^2)).             (1)

At a point where v=0 the corresponding lower bound is |u|/(4c).
A single specified angle proves a lower bound. Locating the global
maximum or solving a minimax problem is unnecessary.

Proof. T4-375's uniform rescaling argument gives
4c H >= |u+t v| at every angle, without differentiating the original
remainder. For v nonzero complete the square:

    |u+t v|^2 = |v|^2(t+u.v/|v|^2)^2
                   +(u1 v2-u2 v1)^2/|v|^2.

Drop the first nonnegative term and use det(u,v)=q(AP'-A'P).
If v=0 the value is independent of t. These deductions do not choose
a moment separately at different angles: they give a necessary lower
bound valid for the single actual moment of any stationary correction.
Taking a supremum of these necessary bounds is therefore legitimate.

## 2. Consequence for the registered endpoint closure inequality

Let B=dist_L2(circle)(A,span{P})/(4c)>0, D=1-c(q-delta)>0.
Let H0 be any lower bound obtained in Section 1. Suppose E is a valid
velocity remainder constant in T4-335 (1), G bounds the leading
reference gradient as there, and V bounds its velocity. Choose
0<g0<=G and 0<=v0<=V. Set

    r0=[sqrt(2pi) H0 (v0+E g0)/(D B)]^(1/delta),
    C0=B r0^(q+1)/sqrt(-2q-2).                               (2)

The square root of the right-hand side of T4-351's CI is at most C0.
Consequently reaching a specified beta>0 by that CI requires

    E <= [D B/(sqrt(2pi)H0)
             (B/(beta sqrt(-2q-2)))^(delta/(-q-1))-v0]/g0.    (3)

Proof. One nonnegative error term in CI is
H(V+E G)r^(-delta)/D. Thus its positive part vanishes for r<=r0.
For larger r bound that part by B and integrate r^(2q+1).
The full radial domain starts at a finite positive radius; enlarging it
can only increase this upper bound. Since q+1<0, replacing H,V,G by
the lower bounds above makes the upper bound larger and conservative.
Algebraic inversion of (2) gives (3). A negative right-hand side in
(3) means the test cannot reach beta for any positive E.

These are upper bounds on what this one inequality can certify.
They are not upper bounds on the actual correction or distance.
They retain the finite-H hypothesis and supply no upper budget for H.
No PDE inverse or existence conclusion follows.

## 3. Campaign inputs, lower bounds and qualifications

Use the exact c=4076476460239181/2251799813685248 and the accepted
three-cutoff endpoint maps for007,013,014. Reconstruct B by the full
circle sine projection. Choose the three rational angles stored in
parameters.json, selected by the peer but evaluated independently in
Arb. Verify the denominators in (1) are strictly positive. All three
pointwise bounds exceed999745; this does not assert the optimal H0.
The full weighted projection of375 remains a separate valid bound.

The gradient lower bound g0=Theta0'(0)>0 follows directly by taking
r to infinity in the reference-gradient estimate at theta=0.
For these exact finite-generator references and their three finite
potential cutoffs, the leading potential is

    r^s Psi(theta), s=gamma+2,
    Psi=sum Theta0_n sin(n theta)/(s^2-n^2).

The cutoffs have smaller velocity order. Thus the canonical velocity
has leading value ((s-1)Psi'(0),0) at angle zero, and one may choose
v0=|(s-1)Psi'(0)|. This use of v0 requires that leading-velocity
asymptotic, in addition to the general endpoint theorem's stated
upper bound. Taking v0=0 needs no extra velocity asymptotic.

The checker evaluates both versions of (3), including the rounded
family ceilings used by the peer and the actual fixed sharpw ball's
L2 radius1351/(1000000*1024). It treats E=1.749109 as hypothetical
until the separate folded-kernel calculation has a complete audit.
A floating grid maximum is not used as a bound. Agreement of a grid
minimax value with one point does not prove a saddle or a global
maximum. Only the rigorously evaluated rational point enters (1).

Dependencies: the uniform endpoint expansion335, its three-cutoff
application338/339, the rescaling-gradient implication375, and the
registered CI351. All analytic hypotheses remain explicit. This audit
confirms the new pointwise consequence proposed in the peer script;
acceptance of the independent written review of375 is recorded
separately when it is published.

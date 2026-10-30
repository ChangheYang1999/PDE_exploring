# The outer tail term already obstructs the current remainder estimate

## Statement and exact hypotheses

This is an independent audit of T1 R1-044, including its hypothetical
kernel-threshold table. Use the complete canonical stationary S1
hypotheses of T4-335 and finite H=H_q(h)>0, with

 H_q(h)=max(sup(1+r)^(-q)|h|,sup(1+r)^(1-q)|grad h|),
 c=4076476460239181/2251799813685248,
 q=1/c-4, delta=1-1/c, kappa=1-q=4+delta,
 D=1-c(q-delta)=5c-1, alpha=-2q-2.

The operator is U=(partial_xy,-partial_xx)Delta^(-1), with its
canonical local/contact term. S1 means even in x and odd in y. The
reference is at the same c and leading angular profile as the correction
chart. Assume the reference gradient bound G r^(1/c-1), G>=g0>0,
and a velocity bound V r^(1/c), V>=0.

The exact endpoint data A,P,Theta0 for007,013,014 are in data/. Put
B=dist_L2(0,2pi)(A,span(P))/(4c), and at the stored rational angle set
Phi=|q(AP'-A'P)|/[4c sqrt(q^2P^2+(P')^2)]. The accepted pointwise
endpoint theorem gives H>=Phi>0; g0=Theta0'(0)>0. For each of the four
exact beta targets, write

 r_beta=[B/(beta sqrt(alpha))]^(1/(-q-1)),
 K=D B r_beta^delta/[sqrt(2pi) g0 Phi].

Let Ebase be a universal constant valid in the T4-335 compensated
velocity estimate. The audited universal lower theorem implies
Ebase>=0.7930365064..., so the relaxed bound u=793/1000<Ebase is valid.
It is not an admissible universal coefficient itself. The tail list
used in410 contains

 C_delta=H(V+Ebase G)/D>0.

Thus0<epsilon<=delta, a=q-epsilon. Keep only the outer-amplitude
term, discard the inner term, and even allow the outer factor2^(-a)
to be replaced by any F>=1. Define this optimistic majorant by

 Aout>=F C_delta L0^(epsilon-delta), L0=2R0>=4,
 J(s)=Aout s^(-epsilon) B_a(s), s>=L0,
 B_a(s)>=lambda=1/2+5*2^(1-q).

These inequalities hold for the displayed410 formula after the indicated
removals. They do not by themselves prove that discarding its inner term
gives a valid upper bound for the actual velocity. Showing failure even
for this optimistic error budget suffices to test that suggested repair.

For every s>=L0,

 J(s)/H>=lambda Ebase g0 s^(-delta)/D
        >=lambda u g0 s^(-delta)/D.                         (1)

For all twelve reference-target pairs, the constant use of this bound
fails the necessary CI condition, as does its radius-dependent use,
even with a universal fallback. A sharper bracket Lambda replacing
lambda must be below the exact thresholds derived below to have any
chance to pass the same CI. Passing these thresholds is not sufficient.

## Proof of the outer bound and radial consequence

Since epsilon-delta<=0 and s>=L0,
L0^(epsilon-delta)>=s^(epsilon-delta). Consequently
Aout s^(-epsilon)>=C_delta s^(-delta). Multiplication by the bracket
bound and V>=0,G>=g0 proves(1).

The radial Green integration of a coefficient E(s) is

 T[E](r)=kappa r^kappa integral_r^infinity E(s)s^(-kappa-1)ds.

Its contribution to the chosen bound on |h-r^q b|/r^q is
(HG/D)r^(-delta)T[E](r). This follows by integrating
c r partial_r h-h, with the far boundary condition supplied by H<infinity.
All other absolute error terms are nonnegative. Thus positivity of the
CI integrand at r<=r_beta requires

 T[E](r)<(r/r_beta)^delta K.                                (2)

If the integrand vanishes through r_beta, its remaining integral is
strictly less than beta^2, since its positive error makes it strictly
smaller than B^2 r^(2q+1) beyond r_beta. No R<=r_grad condition is needed.
Here r is at least the validity radius L0. A chosen starting radius
larger than r_beta cannot reach the target even with zero error.

Without fallback and with Eprof=p>=0, the optimistic coefficient is
p+lambda u g0 s^(-delta)/D. Integration multiplies its power term by
f=kappa/(kappa+delta). The checker proves its value at each r_beta
exceeds K by a factor greater than4.34. The value is larger at smaller
r, whereas the right side of(2) decreases, proving failure there too.

If a valid universal coefficient Eu is also available, Eu>=u, and
E(s)>=min(u,lambda u g0 s^(-delta)/D), even after dropping p. Let
su=(lambda g0/D)^(1/delta). Then, for r<=su,

 T[E](r)>=u[1-delta/(kappa+delta)(r/su)^kappa].               (3)

This is obtained by splitting the power integral at su. The checker
proves su>r_beta and the right side at r_beta exceeds K in all cases.
The common lower bound in R1-044 must be rounded below the true value:
with the relaxed u=0.793, expression(3) is strictly less than0.793,
not greater than or equal to0.7930 as printed. The strict comparison
against every K is unaffected.

## Necessary threshold for a sharper bracket

Replace lambda by any Lambda>=0 and set
Y=Lambda u g0 r_beta^(-delta)/D. In the no-fallback case,
T[E](r_beta)>=p+fY. A necessary condition is p<K and

 Lambda < (K-p) D r_beta^delta/(f u g0).                    (4)

For fallback, the optimistic averaged coefficient at r_beta is

 G_p(Y)=integral_1^infinity min(u,p+Y t^(-delta))
                           kappa t^(-kappa-1)dt.

It is nondecreasing in Y. At smaller r the argument is Y(r_beta/r)^delta,
so it is no smaller while the right side of(2) is no larger. Hence a
necessary condition remains G_p(Y)<K. For p>=K there is no room since
K<u for every checked target. When p<K<u, direct integration gives

 G_p(Y)=p+fY, Y<=u-p,
 G_p(Y)=u-(1-f)(u-p)[Y/(u-p)]^(-kappa/delta), Y>=u-p.

Both branches meet continuously. Thus define

 Ycrit=(K-p)/f, if K<=p+f(u-p),
 Ycrit=(u-p)[(1-f)(u-p)/(u-K)]^(delta/kappa), otherwise.

The necessary threshold with fallback is

 Lambda < Ycrit D r_beta^delta/(u g0).                     (5)

This also covers the exact boundary where both formulas coincide.
If p>=K the threshold is recorded as no room, not as an assertion that
a negative Lambda could help. Since the optimistic u is strictly below
the universal lower bound, these are deliberately generous necessary
thresholds. Neither u nor the optimistic error budget is asserted to
be an available velocity estimate.

## Scope repairs to R1-044

The outer-term result(1), both radius arguments, and thresholds(4)-(5)
are the claims audited here. The phrase 'smallest admissible value' for
0.793 should read 'relaxed lower bound'. The asserted fallback lower
bound0.7930 requires downward rounding as noted after(3).

A smaller positive velocity constant does not remove the delta exponent
from T4-335(7). Its coefficient is H(V+Ebase G)/D and includes the
reference transport term HV/D. Even if the Ebase term were removed,
positive V retains the exponent. Removing that power requires an actual
faster-decaying bound on the corresponding full forcing remainder or
an additional asymptotic term whose subtraction accounts for it.
These alternatives, the needed reference bounds and a stationary H
budget remain OPEN. Merely improving a constant can ease a numerical
inequality, but does not justify choosing epsilon>delta in410.

## Exact evidence

The checker rebuilds B,Phi,g0 from exact sine data, verifies every table
bound in R1-044 by768-bit Arb, and checks the integration and threshold
identities. Frozen review, checker, output and source-input hashes are
retained. The peer checker was read in full and is not executed here.
No quadrature, optimization or remote computation is used. This is an
independent audit of T1's theorem and arithmetic, with the stated repairs.

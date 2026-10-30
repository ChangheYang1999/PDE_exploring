# Reciprocal acceptance of the sharpw self-map maximum

## Exact statement and hypotheses

Fix s=1/5184 and w=(32768,1048576). On real S1 functions, even in x
and odd in y, put omega=(1+4|X|^2)^(2/5), J=(1-Delta)^(1/2), and
X(h)^2=||omega D2 J^s h||2^2+32768||D J^s h||2^2+1048576||J^s h||2^2.
Use the completion of compact smooth S1 functions. The velocity is
U[h]=(partial_xy,-partial_xx)Delta^(-1)h with the canonical local term
(0,-h/2). The normalized correction hyperplane is c[h]=partial_y U2[h](0)=0.

This is an optimization of already audited sufficient estimates. Assume
the background, inverse realization, common domains, origin identities
and coefficient hypotheses of T4-019 and T2-R3, as corrected and audited
in T4-042 and extended at g=0 in T4-065. Equivalently, the scalar step
used here needs the following precise consequences for the fixed norm:
for every 0<r<mu/A, the map T(k)=-A_k^(-1)F is defined on the
L2-closed normalized X-ball B_r, preserves the hyperplane, and satisfies

 X(T(k))<=X(F)/(mu-Ar),
 ||T(k)-T(l)||2<=(c_s r/2)||k-l||2,
 a0-||D T(k)||infty>7/10-c_s r,

where F belongs to X, a0>7/10,
mu=97/250-397s=201799/648000, A=(8/5)/sqrt(s)=576/5 and
c_s=(4 pi s(1+s))^(-1/2). These are assumptions inherited from the
audited framework; the numerical profile has not been shown to meet them.
No empirical bound substitutes for the inverse, normalization or
preservation of the operator domain.

Among pairs (r,eta) satisfying this particular self-map inequality
eta<=r(mu-Ar), with positive rate and its contraction and slope
conditions, the largest eta at these fixed s and weights is

 eta*=40722836401/193491763200000,
 attained at r*=201799/149299200.

Here eta*>2.1046e-4>2.1035e-4. At the old radius r0=1351/1000000,
r0(mu-Ar0)>2.1046e-4 also holds. The selected registered sufficient
test eta0=4207/20000000 remains valid. The frozen T2 review of T4-479
is correct. This does not establish optimality of an inverse estimate,
of every conditional theorem, of a different norm, or of an actual
solution radius. It supplies no existence result for a candidate.

## Complete argument

Complete the square exactly:

 r(mu-Ar)=mu^2/(4A)-A(r-mu/(2A))^2.

Since A>0, this quadratic has a unique global maximum at r*=mu/(2A).
The rate there is mu/2>0. Direct rational substitution gives eta* and
r* as stated. The remaining inequalities do not remove this maximum.
The verified lower bound pi>314159/100000 implies

 (c_s r*)^2 < 40722836401/54043470895104 < (0.02746)^2.

Consequently c_s r*/2<0.01373<1 and the slope margin is greater than
0.67254. Since eta*/(mu-Ar*)=r*, the closed ball is invariant even at
the endpoint eta=eta*. Completeness in the low metric and the assumed
Lipschitz estimate give the same contraction conclusion as the audited
framework. This is a conditional specialization of that theorem, with
all its hypotheses retained.

At r0, the exact rate is 63092119/405000000, greater than1557/10000.
Exact multiplication proves

 eta0<=(1557/10000)r0<=r0(mu-Ar0)<eta*,
 2.1046e-4<r0(mu-Ar0).

The already audited computed-defect extension gives the same expression
at g=0 because the correction size m and multiplier bound B both vanish.
The zero function belongs to each required generator domain. Its defect
is precisely F, so this specialization needs no computed nonzero g.
This does not waive any background or residual membership hypothesis.

For context only, if one varies s in the same rate formula while keeping
the weights, the quadratic maximum is
eta(s)=(5/32)(mu0-C s)^2 sqrt(s) on0<s<mu0/C, with mu0=97/250,C=397.
Differentiation gives

 eta'(s)=(5/64)(mu0-C s)(mu0-5C s)/sqrt(s).

Thus its unique maximum occurs at s0=97/496250, within the permitted
range0<s<=2^-10, and has square (25/4)C^4 s0^5. The larger numerical
value belongs to X_(s0,w), a different norm. It is not a tolerance
improvement at the fixed norm of the theorem above. Failure of a
sufficient Gram or self-map condition is not an upper bound on the
true operator rate or a necessary condition for the PDE.

The accepted007 sharpw forcing lower bound is756.5312630768, in the
same fixed norm. Dividing by eta* gives a factor greater than3594606.
This is a sufficient forcing-test failure factor. It is not an L2
correction-distance estimate. The family distance exclusions already
use independent suprema over s and r and remain unchanged.

## Verification and reporting scope

Freeze the T2 review, checker, exact result, completed log, complete
framework text with its corrections, and the current coordinator report.
The two input hashes pinned in the T2 checker are independently matched
to the previously frozen16:30 report and the frozen framework. Read the
peer program without executing it. Independently compare exact polynomial
coefficients, parameters, selected-radius bounds, contraction squares,
maximum differences and the007 factor. Certify the small pi lower bound
with Arb and check displayed square-root quantities by exact squaring.
All numerical inputs are registered in exact JSON before execution.

The current coordinator report's g=0 repair is accepted in this fixed
norm and for this scalar estimate. Its description of the largest
tolerance should keep that norm and estimate scope. Numbers from
incomparable norms are not a mathematical ranking. Neither the review
nor this acceptance adds a candidate with all closure hypotheses proved.

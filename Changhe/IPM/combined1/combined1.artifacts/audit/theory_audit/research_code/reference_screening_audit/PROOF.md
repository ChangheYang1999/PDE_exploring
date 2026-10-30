# Reference translation and endpoint-budget audit of R1-038

## Exact setting

This audits Parts 1 and 2 of the frozen T1_REVIEWS_v35.md. The exact
campaign constants are c=4076476460239181/2251799813685248, gamma=1/c,
delta=1-gamma, q=gamma-4, and D_delta=1-c(q-delta)=5c-1.

Let C be a real vector space of real S1 functions contained in L2(R2).
For each allowed reference R, fix its canonical background U_R. Assume
that the distributional expression

    F_R(h)=(cX+U_R+U[h]).grad(R+h)-(R+h)

is defined for h in C, and that the relevant background velocities are
divergence-free. Here U is the canonical linear L2 velocity multiplier.
For nonsmooth h its nonlinear part means div(h U[h]); this is a
well-defined distribution since both factors belong to L2 locally.
The other terms have their usual distributional meaning under the
background regularity used in the campaign weak-distance theorem.
Set S_R={h in C:F_R(h)=0} and d(R)=inf_(h in S_R)||h||2, with inf empty=+infinity.

Hypothesis (S) for R,R' is g=R'-R in C and U_(R')=U_R+U[g], with the
same c and compatible distributional domains. All conclusions about
translations below retain (S). Matching finitely many asymptotic
coefficients alone is not a replacement for (S).

## 1. Exact translation and the screening rule

By the linearity of U and the identity R'+h=R+(g+h), the two density
and velocity pairs are identical. Thus F_(R')(h)=F_R(g+h) distributionally.
Since C is a vector space, h belongs to C exactly when g+h does. It follows
that S_(R')=S_R-g. The two solution sets are simultaneously empty. If they
are not empty, the triangle inequality gives

    d(R)-||g||2 <= d(R') <= d(R)+||g||2.

The same inequalities are valid with +infinity on both sides under the
usual extended order and infinity plus or minus a finite number. The
notation |d(R)-d(R')| must be used only when these distances are finite;
infinity-infinity is not defined. This is a notation correction to (b1),
not a failure of the translation theorem.

Suppose a single certified bound d(R)>d0 is available and every correction
in the new framework has norm at most b. A certified upper bound
||g||2<=tau with tau<=d0-b gives d(R')>=d(R)-tau>d0-tau>=b.
Consequently the new ball contains no stationary solution. Conversely,
if it does contain one, then ||g||2>d0-b. This proves R-SCREEN, including
the non-strict comparison at tau=d0-b. A FLOAT estimate of tau has no
such consequence.

For the finite algebraic candidate class the density sector exponents are
1-l delta-2k, l>=1,k>=0. At the exact c, the nonintegrable exponents are
(l,k)=(1,0),...,(4,0), all strictly greater than -1; (5,0) and every
k>=1 exponent are strictly smaller than -1. Matching the first four
coefficients, with the already proved remainder bounds and local
smoothness for these finite generators, gives an L2 difference.
Membership in any smaller C and canonical velocity compatibility remain
separate requirements. Choosing C to be the S1 L2 class of the weak
necessary test is sufficient for the screening argument when the
background conditions hold.

For 005, the bound0.02436463 is derived from T4-175's weighted distance.
Its weight is at most1, so ||h||2>=||w h||2. Thus that certified weighted
floor is also a valid L2 floor. This conversion does not go in the
opposite direction.

## 2. Tail cutoffs and the value function

If g_L is the fourth cutoff and ||g_L||2 tends to zero while (S) holds,
the preceding inequalities imply d(R+g_L) tends to d(R) when finite.
If d(R)=infinity, every translated distance is infinity as well. This
proves the intended extended-real version of (b1). Removing the endpoint
coefficient does not force the distance to tend to zero.

For (b2), let K be a class of references, Phi its endpoint-coefficient map
and W a real vector subspace of the angular L2 space. Assume exactly
(H-cut): for each R in K, w in W and epsilon>0 there is g satisfying
(S), ||g||2<epsilon, R+g in K and Phi(R+g)=Phi(R)+w.
Define f*(A)=inf{d(R):R in K,Phi(R)=A}. Translation gives
f*(A+w)<=d(R)+epsilon for every R with Phi(R)=A. Taking infima gives
f*(A+w)<=f*(A); the reverse follows with -w. This also covers empty
fibres: existence of a finite-distance member in one fibre would transfer
to the other, while a nonempty infinite-distance fibre transfers as such.

If K contains an exact solution, its coefficient Phi is zero and its
distance is zero, so f*(0)=0 and f*(w)=0 on W. Any endpoint-only bound
beta(Phi(R))<=d(R) then satisfies beta(A)<=f*(A). A positive beta at one
w in W is incompatible with an exact solution in K. This is conditional
on H-cut at every reference, not just at one explicit pair. Compact
annular moment changes provide the claimed span-P direction only for
classes K that remain closed under those changes and keep the same
leading coefficient; that closure is not proved merely by constructing
one cutoff.

## 3. The a priori endpoint budget

Retain every growth, differentiability, remainder, canonical velocity and
finite-H_q hypothesis of T4-335 and T4-351 for a three-times repaired
reference R3. Write B=dist(A,span P)/(4c)>0, where A is its residual
coefficient at q. The accepted endpoint theorem gives
H_q(k)>=B/sqrt(2pi)>33917 for every such stationary correction.
Thus an a priori bound H_q(k)<=Hmax< B/sqrt(2pi) excludes these corrections.

When Hmax>=B/sqrt(2pi), let E be a valid velocity-remainder coefficient
and G a valid leading-gradient coefficient. In the CI error all terms
are nonnegative, and one of them is H E G r^(-delta)/D_delta.
Consequently the CI integrand

    (B-sqrt(2pi) ehat(r;H))_+^2 r^(2q+1)

vanishes for r<=r_H=(sqrt(2pi) H E G/(B D_delta))^(1/delta),
and is at most B^2 r^(2q+1) elsewhere. For every lower integration limit
R1>=R0, its integral is therefore at most

    B^2 r_H^(2q+2)/(-2q-2).

The same cap is valid if r_H<R0. Inserting H=Hmax is legitimate for a
uniform sufficient lower bound: ehat is increasing in the nonnegative
budget H, so replacing H_q(k) by Hmax only weakens that lower bound.
This does not say Hmax is attained by a stationary correction or that
this uniform CI choice is optimal among all possible methods.

To get a strict L2 lower bound above b by this uniform CI test, its cap
must exceed b^2. Hence

    E sqrt(2pi) Hmax/B
      < (D_delta/G) [B/(b sqrt(-2q-2))]^(delta/(-q-1)).

Using the certified B<85020 and G>285227/10000 enlarges the right side
to the R1-038 value Emax(b). Also B/sqrt(2pi)<33919 implies
E Hmax<33919 Emax(b). This proves (c)(ii) and its necessary-condition
interpretation. Lowering b in numerical verification enlarges the
threshold and is conservative for the displayed upper bounds.

The numerical checker independently verifies all42 screening margins,
the algebraic denominator identities and every displayed outward bound
in the R1-038 table at768-bit Arb precision. It never runs the peer code.

The moment-bound substitution described in (c)(iv) changes only its
second and fourth error terms, so it leaves this particular cap unchanged.
It can still increase a certified lower bound below the target b. Thus
the sentence saying it can sharpen the test only after (ii) holds should
say it can yield an exclusion at the ceiling b only after (ii) holds,
within this fixed uniform-CI construction. A different use of moment
information to restrict the angular projection is not analyzed here.

## 4. What the nonembedding does and does not prove

The sentence in (c)(iii), 'No budget of the first kind exists', is not
justified by T4-359 or the X-to-H_q nonembedding. Those results construct
arbitrary test functions with a small X or L2 norm and large H_q. They
do not construct stationary solutions with those properties. An a priori
estimate restricted to stationary solutions might use the PDE; no such
estimate is presently proved in this campaign. For logical clarity,
on the same function space the equation h=0 has the uniform H_q bound0
on its solution set even though the ambient embedding fails. This is a
counterexample to the inference from nonembedding to absence of all
solution-specific bounds, not a claim that the IPM a priori bound exists.
The correct status of such a PDE bound is OPEN.

Likewise (c)(iii)'s two requested new results concern the branch
Hmax>=B/sqrt(2pi) and the uniform CI route. A stronger PDE budget below
this threshold would exclude solutions directly by (c)(i), without an
improved E. The conditional alternatives should both be retained.

## 5. Norm-dominating frameworks

If a norm Y satisfies ||k||_Y>=H_q(k), every stationary correction of R3
in that norm has ||k||_Y>33917. Thus no Y ball of radius at most33917
can contain one. This is a statement about balls centered at R3, with
the endpoint hypotheses intact.

For any valid Newton-Kantorovich theorem that supplies a solution within
t*=2 eta/(1+sqrt(1-2K eta)), with K>=0, eta>=0 and 2K eta<=1,
we have t*<=2eta. For K>0, t*=(1-sqrt(1-2K eta))/K<=1/K.
Since the supplied solution requires t*>33917, eta>16958.5 and
K<1/33917 follow. For K=0 the continuous formula gives t*=eta and
the K bound is automatic. This is only a necessary implication of a
valid theorem with its domain, inverse and Lipschitz hypotheses; it does
not establish those hypotheses for R3.

T4-375 proposes replacing33917 by328627, which would strengthen these
numbers. Its analytic review remains separate, so this audit accepts
R1-038's original weaker bounds independently of375.

## 6. Erratum acceptance and verdict scope

Part1 correctly restores the nonzero drift contribution in R1-037(d):
for fixed m!=0 and nonzero compact f, the complete residual change is
asymptotic to |m| ||(cX.grad-1)f||2 R^-2, with the positive coefficient
at least(c+1)||f||2. Finite-radius lower bounds still require the other
constants. The old incorrect rate remains refuted.

The translation/screening theorem, conditional value-function theorem,
uniform-CI necessary threshold, and norm-dominating implications are
CONFIRMED under the explicit hypotheses above. The inference ruling out
all stationary a priori H_q budgets from an ambient nonembedding is
REFUTED; the existence of such a PDE estimate is OPEN. The extended-real
absolute-value notation and the target-specific moment sentence need
the stated repairs. No new snapshot exclusion is produced without a
certified difference norm and (S).

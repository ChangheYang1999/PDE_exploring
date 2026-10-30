# Acceptance of the endpoint audit's five logical repairs

## Exact statement and hypotheses

This result concerns revision 2 of T2's the T2 falsification review of the endpoint and the report summary,
SHA256 660b089b8e6435065918f020a45d971cce4d82e8210675944322f3d7c47dd7f5,
and its changes to the independently audited revision 1. The endpoint
CI certificate, its real C1 correction space with finite weighted H_q,
canonical velocity including the contact term, and all endpoint and
radial-error assumptions remain those of the standalone source/own_PROOF.md
(T4-443). This note changes none of those analytic hypotheses.

For clarity the underlying logical statement is independent of IPM.
Let A be the set of constants actually valid in a specified uniform
velocity estimate, with A contained in [Emin,infinity). Suppose passing
a given certificate at target beta requires E<=K(beta), for E in A.
Then K(beta)<Emin excludes every admissible E at that target. If
K(beta)>Emin, these premises alone neither produce an admissible E
that passes nor disprove exclusion by another argument. This remains
true if an auxiliary numerical-envelope class includes Emin itself.

The five revisions requested by T4-443 are logically correct: withdraw
the two-small-target universal conclusion as unproved; retain only the
necessary direction; distinguish loss of a derivation from refutation
of the historical bound; restrict the coefficient floor to the listed
estimates; and keep unproved exact-ceiling bracket assumptions explicit.
The 13-row numerical table and the arithmetic program are unchanged.

## Proof of the logical distinctions

If E belongs to A and K<Emin, then E>=Emin>K, contradicting the necessary
condition. For K>Emin, both A=[Emin,infinity) and A=[K+1,infinity) satisfy
the same lower-bound premise. In the first set some constants meet
E<=K; in the second none do. The premises therefore do not determine
whether any valid estimate passes. Even in the first example meeting
a necessary condition need not suffice for the certificate. These are
logical examples, not claims about which constants are valid in IPM.

Likewise J<=a and J<=b with b>a are compatible. Replacing a proof of
J<=a by a proof of J<=b supplies no counterexample to J<=a. Here the
historical cap a=9.28e-11 used older numerical inputs; the current
larger caps do not show that the actual certificate exceeds a.

For a listed collection e_i(r)>=f(r), positivity gives inf_i e_i(r)>=f(r).
Appending a previously absent estimate e_new can destroy that premise.
In particular a lower floor for the currently listed coefficients is
not a lower bound for all future valid stationary estimates.

Finally beta<=b, described as a rounded-up bound, does not imply
beta>=b-u for a prescribed positive printed unit u. Such a lower
bracket must come from an exact formula or a separate enclosure. For
the graded formula beta_g=50/(651 sqrt(28248)), both endpoints can be
checked directly; it lies strictly between 45697/10^8 and 25/54684.

## Accepted quantitative dependencies

T4-443's separate proof and 948-check result establish, at the 13
printed targets, all unchanged displays in sections 1 to 4. In its
notation q=1/c-4, delta=1-1/c, kappa=1-q, D=5c-1,
alpha=-2q-2, c=4076476460239181/2251799813685248, and
lambda=1/2+5*2^(1-q). For a nonnegative coefficient floor
f(r)=min(Ef,lambda*(5/r)^delta), its positive radial average
T[f](r)=kappa*r^kappa integral_r^infinity f(s)s^(-kappa-1)ds
bounds the chosen error majorant. Splitting the CI integral at any
M>0 gives the fully proved upper bound

 J^2 <= C(T[f](M))^2+B^2*M^(2q+2)/alpha,
 C(E)=B*[sqrt(2*pi)*Hmin*(vmin+g0*E)/(D*B)]^((q+1)/delta)
          *sqrt(2*delta^2/[alpha*(alpha+delta)*(alpha+2*delta)]).

The frozen exact candidate endpoint data and hypotheses of T4-443
supply B,Hmin,g0,vmin. Its current-list value is below 2.66323e-8,
less than 2^-25. For the universal lower floor and V>=v0 it is below
1.14141e-7, less than 2^-23. Without V it is below 1.43912e-7.
This bound limits that certificate, not the existence of a correction.
The two smallest Db targets remain OPEN for an improved valid constant.

## Additional exact-graded check

Revision 2's verdict and proposed wording say that R1-038 needs E below
0.2694533 at the graded ceiling. Its detailed section 4 distinguishes
the printed target b=25/54684 from beta_g. The necessary algebraic
cutoff at the exact graded value is

 K_g(Hmax)=D*B/(sqrt(2*pi)*Hmax*g0)
             *(B/(beta_g*sqrt(alpha)))^(delta/(-q-1)).

For each of the three endpoint records, using the common lower budget
Hmax>=999745 gives K_g<0.2694533. Although K_g is larger at beta_g
than at the printed target, the displayed decimal remains an upper
bound. It is also below Emin, so every admissible constant fails.
This does not furnish an existence implication under an impossible
stationary-correction hypothesis.

An initial draft of this audit conjectured that the bound failed at
beta_g. The first checker refuted that conjecture before acceptance.
The initial proof, manifest, code and failure log are preserved under
verification/initial_failed_*. The corrected argument above and the
final checker verify the common-budget bound directly. No accepted
result was overwritten.

## Verification and scope

The checker binds frozen revisions, proof and source graph, verifies
all 37 word-change blocks, the identical 13 numerical table rows,
unchanged source program, five repair markers and the prior result.
It independently encloses beta_g, the unchanged aggregate caps and
the exact graded cutoffs at 768 bits. No peer code, integration or
optimization is run. Acceptance concerns these repairs and explicit
consequences, not a new audit of every sentence in the T2 final summary.

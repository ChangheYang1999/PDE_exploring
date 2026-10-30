# A complete negative-norm upper certificate from a prefix of angular modes

Written UTC 2026-10-29T15:57:33.283407+00:00 before the checker. This is a finite-composition alternative for an unfinished mode-by-mode Hardy calculation. It supplies an upper bound with explicit omitted-mode coverage. It supplies no a posteriori existence theorem.

## Exact statement and domain

Let F be a real locally integrable S1 function on R2, even in x and odd in y, and suppose rF is in L2(R2), r=|X|. Define

 H(F)=sup{|integral F phi|: phi in C_c^infty(R2), ||grad phi||2<=1},
 S=||rF||2^2.

The angular expansion has only positive odd sine modes, F=sum_(n odd>=1) f_n(r) sin(n theta). Put

 S_n=pi integral_0^infty r^3 f_n(r)^2 dr.

All these quantities are nonnegative and sum_n S_n=S by angular Parseval in the weighted L2 space. A finite angular expansion is allowed but not required. Fix an odd positive integer N, and suppose every mode n<N has been included. Zero modes in this list may be established algebraically. Define

 B_N=S/N^2+sum_(n odd<N)(1/n^2-1/N^2)S_n.       (1)

Then the complete angular Hardy bound M2=sum_n S_n/n^2 and H satisfy

 H(F)^2<=M2<=B_N,                               (2)
 0<=B_N-M2<=S/N^2.                             (3)

For exact complete inputs, B_(N+2)<=B_N. In particular a partial calculation with only low modes gives a complete upper certificate once the full S is certified. No assertion that a truncated mode sum equals the full norm is needed.

For directed numerical use, take rigorous nonnegative upper bounds U>=S and U_n>=S_n for every odd n<N. The expression

 U/N^2+sum_(n odd<N)(1/n^2-1/N^2)U_n            (4)

is an upper bound for B_N. All coefficients are nonnegative. Thus no subtraction of nearly equal interval endpoints or lower bound for the omitted energy is needed. Each ingredient must belong to the same exact F, and all lower modes must be covered. Rigorous bounds obtained at several prefixes may be combined by taking their minimum. Rounded decimal displays without directed status are not admissible inputs.

## Proof, including the origin and infinitely many modes

Define the angular right inverse on annuli by

 A_F=-e_theta r sum_(n odd>=1) f_n(r) cos(n theta)/n.

Its series converges in L2(R2;R2), since its squared norm is M2<=S. The finite Fourier projections converge in that vector space. Angular integration gives div A_F=F on every annulus. The same identity on the entire plane follows by radial cutoffs: their gradients are radial and hence orthogonal to A_F, so there is no cutoff derivative term. The locally integrable F permits passage on the right, and the L2 vector field permits passage on the left against a fixed compact smooth gradient. Therefore |integral F phi|=|integral A_F dot grad phi|<=sqrt(M2)||grad phi||2. This proves the first inequality of (2) and the continuity of F on the gradient completion. It uses the distributional source itself, not a numerical Fourier section as an inverse.

For n>=N one has 1/n^2<=1/N^2. Hence

 M2<=sum_(n<N)S_n/n^2+(S-sum_(n<N)S_n)/N^2=B_N.

The identity

 B_N-M2=sum_(n>=N)(1/N^2-1/n^2)S_n

proves (3), with convergent nonnegative sums. Removing the next odd mode N from the tail gives

 B_(N+2)-B_N=(1/(N+2)^2-1/N^2)(S-sum_(n<=N)S_n)<=0.

In (1), every coefficient of an included S_n is nonnegative, proving (4). If a lower mode were omitted without an exact zero certificate, its correct reciprocal square could exceed 1/N^2; the bound would no longer follow. This is why both the angular support and complete prefix are part of the input certificate.

## Combining with the divergence-free improvement

Under the additional hypotheses of T4-469 and ERRATA_v01, let distinct angular tests psi_j define Z_j=A_(Delta psi_j)-grad psi_j, a_j=||Z_j||2^2>0 and b_j=<A_F,Z_j>. Then

 H(F)^2<=M2-sum_j b_j^2/a_j<=B_N-sum_j b_j^2/a_j.       (5)

If a_j<=A_j with A_j>0, and |b_j|>=L_j>=0, the upper in (4) minus sum L_j^2/A_j is valid. Each a upper and |b| lower must be directed and certified; a trial optimized in floating arithmetic is allowed only after its exact coefficients and all integrals are checked. The tests may use any distinct modes. Equation (5) does not discard the untested modes, and no lower-bound basis-completeness argument is involved. Its general divergence-free premise is separately under the existing Opus reviews. The prefix result (1)-(4) depends only on the elementary angular Hardy proof above.

This composition is useful even when a long run will eventually compute all modes. The low-mode certificates can be accepted as they finish, with the full S supplying the remaining positive mass. A process status or an incomplete log alone is not a certificate: the actual saved mode results, full field binding, integration proof, exact coefficients and interval groups still require review.

## Candidate016 scope and arithmetic to be checked

T4-467 already accepts the complete component upper

 ||rF016||2 < 7145701175364457183129953068731/10^30.

This is an accepted whole-plane component of the exact candidate, not a finite-box loss. For a complete prefix1,3,...,31, take N=33. By (3), the loss in squared upper bound relative to the full modewise Hardy value is less than this exact squared rational divided by1089. The checker will verify that it is below47/1000. This estimates the maximum loss of the prefix method; it does not certify the currently unfinished full Hardy value or any numerical B_33 without the sixteen mode certificates. Corresponding explicit loss bounds will also be recorded for N=3,5,9,17,65.

The separately accepted T4-472 two-mode cross improvement is strictly greater than

 59664789113139289718803/250000000000000000000000.

With the general T4-469 proof accepted and compatible mode-prefix inputs, this lower improvement can be subtracted from (4). Its numerical value is not a replacement for the missing B_N upper. No candidate016 H upper or new E2 upper is asserted here.

## Exact manufactured checks and scope limits

The checker uses finite rational energy lists, without spatial quadrature, to verify (1)-(4), monotonicity, directed upper data and the omission counterexample. Any finite nonnegative list S_n is realizable by mutually orthogonal smooth annular sine fields after rescaling their amplitudes, so the list identities test genuine mode decompositions. The tests include an all-zero list, a single nonzero high mode and a mixed1,3,5,7 list. A zero target field has H=0 and satisfies every inequality. A high-mode-only field shows why replacing all omitted terms by zero is invalid; a compact smooth test paired with that nonzero field gives H>0.

There is also a fixture with an exact negative-norm value. Let psi_1=r sin(theta)/(1+r^2)^(3/2), psi_3=r^3 sin(3theta)/(1+r^2)^3 and F=-Delta(psi_1+psi_3). The T4-469 manufactured polar identities give

 S_1/pi=3/4, S_3/pi=64/35,
 M2/pi=1201/1260, H(F)^2/pi=153/280,
 a_1/pi=3/8, a_3/pi=2/63, b_j=-a_j.

These positive rational identities and their sums are rechecked from the independently saved fixture outputs. B_3 equals the exact M2 because the only omitted nonzero frequency is3. Subtracting both a_j recovers the exact H(F)^2. This is a known-solution verification of the direction in (5), not an assertion that candidate016 has that solution.

The input manifests bind the accepted467 and472 arithmetic and the original469 proof, erratum and exact fixture result. No copied peer program, candidate field integration, background inverse, origin normalization or canonical contact functional is computed by this corollary. The existing T1/T2 lanes, configured for us.anthropic.claude-opus-5-5 with actual provider identity unobservable here, receive the proof for independent analytic review. No extra model call or compute worker is used.

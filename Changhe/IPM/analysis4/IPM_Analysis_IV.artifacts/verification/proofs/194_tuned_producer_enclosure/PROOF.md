# Enclosure induction for the tuned numerical producer

Status: PROVED as an interval-algorithm theorem; independent theory-part review accepted in V400 at 2026-10-31T14:38:27+00:00. Artifact-specific checks are separate.

## Exact statement and hypotheses

Fix Q=5 or Q=6, delta=2/Q and c=Q/(Q-2). Let b be a certified root of the first-obstruction polynomial130 or154, and suppose the exact affine responses sigma_k are nonzero for every required block, as proved in the corresponding all-index response theorem. Let the initial interval vector contain the exact profile sin(theta)+b sin(3theta), and let the stored parameter intervals contain the exact delta and c.

Consider the algorithm implemented by the retained versions of TunedQ for Q=5 and TunedGeneral with a=1,b_den=3 for Q=6, using the retained FarField step and product routines. Suppose every arithmetic operation is outward rounded; every nonresonant division uses a denominator interval excluding zero; every response division uses an interval excluding zero; and no coefficient interval is replaced by its midpoint. Then each completed block encloses the exact uniquely tuned density and stream coefficients through its last completed stream order. At a final resonant order n with H_n still unset, the density and the particular stream coefficients are enclosed, but the free stream coordinate is not yet an enclosure of the tuned H_n. A full tuned stream norm must therefore omit that order or fill its exact harmonic enclosure first.

## Definitions and exact block identity

Write T_(i,j)(g,f)=(2-i delta)g f'-(1-j delta)g' f, and lambda_m=(m-1)(c-1). At a resonant order n=kQ, k>=2, let e=sin((2k-2)theta). The density f_n is already fixed before H_n is chosen; write g_n=g_n^part+H_n e. All orders below n are independent of H_n.

Compute a provisional block f^0_(n+i), 1<=i<=Q, with H_n=0. Let phi_i be the coefficient of H_n in f_(n+i). Then

lambda_(n+i) phi_i = T_(n,i)(e,f_i)
  + sum_(m=1)^(i-1) [T_(n+m,i-m)(Pi_(n+m)phi_m,f_(i-m))
                     + T_(i-m,n+m)(g_(i-m),phi_m)],

where Pi is the nonresonant particular Poisson inverse. All n+m with 1<=m<Q are nonresonant. Put sigma_k=[sin((2k-1)theta)]phi_Q and R_k=[sin((2k-1)theta)]f^0_(n+Q).

## Complete proof

A change in H_n first changes the stream at n and the density at n+1. Below order n+Q, a nonlinear pair cannot contain two factors affected by H_n: their smallest possible total is n+(n+1)=2n+1, while n+Q<=2n because n>=2Q. Hence every coefficient through n+Q is affine in H_n. Collecting the pairs with exactly one affected factor gives the displayed response recurrence. The term with affected stream at n is T_(n,i)(e,f_i). The remaining affected stream and density terms give the two sums. The Poisson inverse between resonances is linear, so it introduces no higher power of H_n. This proves f_(n+i)=f^0_(n+i)+H_n phi_i.

At the next resonance the obstructed density coordinate is R_k+H_n sigma_k. Since sigma_k is nonzero, H_n=-R_k/sigma_k is the unique choice cancelling it exactly. The first obstruction at2Q vanishes because b is an exact root of the compatibility polynomial. Induction over blocks therefore proves every exact compatibility identity used by the algorithm; interval containment of zero is a consistency check, not the source of those identities.

Now induct on the numerical operations for this exact branch. The initial coefficient and parameter intervals contain their exact values by hypothesis. Ordinary finite sums, derivatives, polynomial convolutions and divisions by nonzero denominator intervals preserve containment under outward rounding. In a block, the provisional coefficients contain f^0, the response recurrence contains phi and sigma, and the next obstruction interval contains R. Thus the interval quotient -R/sigma contains the exact H. The affine correction f^0+H phi contains each exact corrected density coefficient, despite dependencies between the intervals, since using a larger rectangular product only enlarges the enclosure. Recomputing the particular Poisson inverses then encloses the corrected streams. At the exact kernel the compatibility just proved allows setting the free coordinate to its H enclosure. This completes the induction.

The retained convolution routine forms ordinary polynomial products of degrees J and K and keeps J+K+1 coefficients, so its truncation loses none of the product. The two sine-to-cosine product identities supply the required sum and difference frequencies and a factor1/2. The step routine trims only intervals that are exactly zero, not intervals merely containing zero. Its floating statistics are not used to update coefficient arrays. Neither tuned block routine replaces coefficient intervals by midpoint values.

At the last resonant order the loop may stop before the next lookahead block, leaving H_n absent from the harmonic table. The density is already determined, but the stored kernel value is the provisional choice0. That value need not contain the exact tuned H_n. Excluding the full stream norm at this order is therefore necessary. No extrapolation from the resulting finite norms to an infinite growth constant follows from this proof.

## Dependencies and artifact limits

The exact recurrence and Poisson inverse were independently derived at the start of the campaign. The affine block identity and compatibility mechanism are proved in131. The nonvanishing responses come from the Q5 and Q6 response certificates. Low-order Cartesian reconstruction in180 and185 independently checks the input root and block outputs, while191 checks high-order Cartesian residuals. The latter is a necessary consistency test and cannot replace this enclosure induction.

This theorem assumes output generated by the stated algorithm with its stated arithmetic. It is not a formal proof of the Python interpreter or the interval library, and a checksum alone does not establish that a checkpoint was generated by its claimed source. Saved source hashes, parameter and root containment, coefficient archives and independent equation checks provide the run-specific evidence. The proof makes no claim about midpoint-reset logarithmic continuations.

## Artifact checks, 2026-10-31T14:31:28+00:00, V388

Eight completed branches pass parameter and algebraic-root containment and match the independently audited source hashes: Q5roots3,4,5,6 and Q6roots1,2,5,6. For each branch, all90300 Poisson denominator intervals are nonzero except at the exact resonances, and all299 density divisors are positive. Source review finds no midpoint replacement in coefficient-update paths and no loss of polynomial-product coefficients. The automated artifact checks took4.910992220975459seconds. The final free stream harmonic at300 is excluded.

CONFIRMED for these artifact-specific hypotheses and the inspected source operations. Topic194 contains the complete enclosure-induction argument; its separate team review is pending. This entry does not certify an interpreter or library implementation.

## Independent review, V400

The theory part independently checked the affine index bound, both response sums, interval inclusion despite coefficient dependencies, exact compatibility before inserting the resonant free coordinate, and the final untuned-harmonic exclusion. All steps were accepted without a gap. The proof now applies to the retained Q5 and Q6 producers under its stated outward-arithmetic and execution hypotheses.

CONFIRMED. Topic194 is PROVED as an interval-algorithm enclosure theorem. This completes the pending analytic review underlying the finite continuum bounds in196; it adds no sharp infinite growth estimate.

## Complete artifact set, V404

All twelve branches Q5roots1..6 and Q6roots1..6 pass fresh exact-parameter containment, algebraic-root containment, independent-prefix checksum agreement, 90300 Poisson denominator checks per branch and299 positive density divisors per branch. All source checkpoints are complete through300. The final harmonic at300 remains excluded. Runtime 8.343786379788071 seconds. The earlier eight-branch check is retained under its dated filename.

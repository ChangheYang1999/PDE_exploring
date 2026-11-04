# Direct near moment bound and the revised scalar tuple

## Exact statement and hypotheses

Use all fixed parameters, source definitions, admitted norm endpoints, radial subtraction hypotheses, NR25 and NR32 Fourier hypotheses and HF1-NEAR localization premises of ../near_tuple_actual_audit/PROOF.md. The exact Source 013 and fixed c are unchanged. Write d4,d5,d6 for its actually adopted full-plane derivative norm upper endpoints and r_j=sqrt(d_j^2-K_j). Both the core-split bound and the direct NR25 bound are valid:

    M4(a_n) <= Bsplit = 1024c + sqrt((r4*r6+r5^2)/(2pi)),
    M4(a_n) <= Bdirect = sqrt((d4*d6+d5^2)/(2pi)).

Consequently M4(a_n) <= Bmin=min(Bsplit,Bdirect). Replacing only the second scalar loss by A*Bmin/mu^4 preserves the sufficient near bound. The four other losses, price expression, fixed parameters and case inputs stay those of the cited proof. All output comparisons use exact displayed rationals, including the sum of five upward losses and the resulting downward margins.

For the actual admitted d4,d5,d6, Bdirect is the smaller bound. The claimed new e_up is 152627111489/10^12 for b=11/20,mu=72 and 180101237602/10^12 for b=103/200,mu=68. Their exact rate rooms beta-b-e_up are 1164347009/(5*10^11) and 1970913581/(2*10^11), respectively. These rooms are prospective budgets for the still unproved complete H4 remainder; eps_rest=0 remains an OPEN stand-in. Fallback kernel constants and allowance remain UNAUDITED.

## Complete argument

A quantity bounded above by both Bsplit and Bdirect is bounded by their minimum. All factors in the second loss are positive, so replacing the split bound by that minimum preserves its direction and can only decrease this sufficient loss. The absolute-moment subadditivity used for the two tail terms is unchanged and does not require using the same decomposition to bound M4. Each bound is nondecreasing in every d_j. Bsplit is nonincreasing in each K_j, whereas Bdirect is independent of K_j. Therefore the minimum has the same monotonicity. This justifies checking adjacent grid points for the one-variable threshold interface, with every other input fixed. It does not establish a necessary analytic threshold.

The independent checker evaluates every actual expression at 768-bit Arb precision, with exact rational input. It selects the smaller moment expression only after verifying their balls are strictly ordered, rather than using the producer's interval minimum. It verifies the two moment displays, all five loss displays and their sum, the price and allowance, both margins, all side conditions and adjacent threshold transitions. It checks exact equality of the actual parameter file with the already audited v08 parameter file, and binds the program and output bytes. No producer arithmetic is imported or executed. This proves the claimed scalar enclosures subject to the cited analytic hypotheses.

## Dependencies and scope

The source and numerical-norm dependencies are the actually adopted whole-plane result in ../source013_near_norms/results/wholeplane_v02/ACTUAL_ADOPTION_PROOF_v01.md. The old near arithmetic and its exact-input check are in ../near_tuple_actual_audit/. This proof uses the admitted NR25 theorem and does not reopen it. Evidence for the new tuple is verification/check_v01.json; source snapshots are in source/. No Lean or Lake build is run. The scalar result supplies no full near localization theorem, actual H4 remainder, uniform inverse, invariant ball or stationary existence conclusion.

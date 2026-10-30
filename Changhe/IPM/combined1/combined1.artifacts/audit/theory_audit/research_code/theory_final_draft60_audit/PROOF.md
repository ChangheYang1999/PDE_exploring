# Theory draft 60: acceptance of the final literal repairs

Written UTC 2026-10-29T17:50:54.344563+00:00 before the checker. This is an incremental audit of all 18 changed blocks between accepted draft 58 (f76c41fb4e5f3733e5f0ac2749120c80a9771349b97ab83f61bcfe86c059f91f) and frozen draft 60 (8bac7dfc4a62c315297c0d54bc1f42812afbeb85dc2868af93c41e06c45ce137). It also checks review set 52 E13 and E14 and the two changed README hash entries. The older theorem proofs, hypotheses and accepted numerical source intervals remain premises. No peer code is executed.

## Exact statement and scope

The repairs of T4-491 and T4-493 are correct in the frozen draft and review set 52. The conditional existence theorems retain their exact S1 spaces, canonical velocity, origin trace, maximal operator domains, high and low inverse compatibility, positive rates, nonlinear bounds and slope condition. No candidate gains a closure certificate. The 83 candidate-row references and 78 directed distance-table factors are unchanged and remain correct against the frozen matrix v161. Candidates 011, 027 and 028 retain OPEN rows. Earlier source intervals are not recomputed in this audit.

Dependencies are the standalone proofs and exact results of T4-491 (the scalar caps), T4-492 (serialized FLOAT ratios), T4-493 (draft 58 and R1-052), T4-495 (partial 017 replay) and T4-496 (completed numerical wording repairs). The present draft predates the last two; its historical statements through T4-494 must not be read as a claim that the later events did not occur. In particular, the final report should cite the accepted 017 lower bound separately and keep the complete upper and E2 conditional.

## Complete argument

Let HL=308366750368225240013184170643/(5*10^29), the strict lower endpoint for H(016) accepted in T4-488. Exact subtraction gives

    HL - 0.6167335007 = 18225240013184170643/(5*10^29).

The last fraction lies strictly between 364/10^13 and 365/10^13. Thus E13's replacement by a difference below 3.65e-11 is directed correctly. The replacement does not change HL or any norm bound. The revised producer checker adds precisely this exact comparison to its previously accepted 88 checks; its new log records 89. Its stored code and output hashes are checked as data, not executed. The README differs in two hash entries, for that code and output, and in their descriptive prose. The other 184 hash entries equal the already accepted entries.

Let eta0=4207/(2*10^7), the selected sharpw threshold, and eta*=40722836401/193491763200000, the maximum of the fixed sharpw sufficient parabola proved in T4-485. These denominators are different and eta*>eta0. Therefore the former universal sentence about all sharpw factors was false, and the replacement "Unless expressly compared with eta*" covers the explicit comparison with eta*. Section 2.1, item 91 and E14 make this change. Item 87 now identifies the old wording as the historical text of drafts 56 to 59. There is no claim of optimality over different norms or all PDE solutions.

For the scalar cap, T4-491 supplies the exact TB-sharp example s=1/4096, r=3791/1953125 and r/512=3.791e-6. Its positive rate, contraction, slope and self-map checks are preserved in that accepted result. This budget exceeds 3.79e-6. The common upper 3.7930e-6, proved for the eight registered scalar families by maximizing their necessary scalar parabolas, remains valid. The stronger graded upper is 50/(651*sqrt(28248)); squaring shows it is below 4.5717e-4. The older, coarser 25/54684 is slightly above 4.5717e-4 and must not be identified with it exactly. The draft now states the valid common scalar and stronger graded uppers. For the accepted 007 distance lower 4769166867/10^12, division by the common scalar upper exceeds 1257; division by the stronger graded upper exceeds 10.43. These are necessary budget obstructions. Passing them would not prove existence or provide a sufficient refinement target.

The first-mode ratio at k=12 is the absolute ratio of two decimal numbers in the saved FLOAT register. Exact division of those serialized decimals lies between 9358.8588 and 9358.8589, hence rounds to 9359 to the nearest unit. At k=128 it lies between 26.8 and 26.9; the saved probes with 192<=k<=1024 remain below 2.1. T4-492 and T4-493 already check the complete relevant register. Repairing this descriptive rounding does not certify its underlying quadrature. The 600 other FLOAT displays and both later numerical literal repairs are accepted separately in T4-496.

For the remaining changed blocks, the additions are source history, accepted review status, positive-rate and slope reminders, and line reflow. The change list fixes every old and new line range. The 83 candidate-row references and the 78 distance factors are extracted again from the frozen document. A factor printed to a fixed number of decimals is the exact downward rounding of its displayed lower bound divided by the declared cap. The same 108-row matrix gives the candidate identities and OPEN statuses. These checks do not infer a candidate verdict from small loss or from a failed sufficient forcing bound. Existing exclusions retain their separately proved necessary-condition arguments.

## Verdict

CONFIRMED: all 18 changes under the previous audited premises; the E13 and E14 repairs; all 186 README hash entries by unchanged-entry inheritance and direct verification of the two replacements; the 83 row references and 78 directed factors. OPEN: existence, rankings of actual correction distances, unaccepted later 016 modes, and the complete 017 H upper and E2. The accepted 017 dual lower and two residual-mode enclosures of T4-495 are additional evidence outside this older draft, not a discharge of all its missing premises.

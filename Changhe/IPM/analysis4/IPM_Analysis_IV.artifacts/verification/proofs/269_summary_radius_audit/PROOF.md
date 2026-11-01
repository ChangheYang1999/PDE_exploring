# Exact comparison of the published radius table

Status: the first recorded audit is CONFIRMED in V546. The protocol was written before that run. This audit introduces no new convergence theorem.

## Statement and hypotheses

Assume a profile has an admitted nonnegative majorant at w=2^(-q), where delta=2h/Q is reduced, z=r^(-delta), and w=z^Q. Assume that the coefficient of order n is homogeneous of degree n in the leading amplitude epsilon. Then its certified exterior radius is

    R > 2^(q/(2h)) |epsilon|^(Q/(2h)).

For each row of the current aggregate certificate table, the audit checks the original certificate bytes against their retained hash, this exact change of variables, the relation c_l=1/(1-delta), root order and the exponent copied into the theory part's summary. Candidate-shaped amplitude-restoration bounds are compared to their already admitted aggregate values. This is a transcription and arithmetic check; each underlying convergence theorem retains its own hypotheses and proof.

## Proof

Because w=(r^(-delta))^Q=r^(-2h), the strict inequality w<2^(-q) is equivalent to r>2^(q/(2h)). Replacing every order-n coefficient by epsilon^n replaces the power-series argument z by epsilon*z. Absolute convergence therefore holds when |epsilon|*r^(-delta)<2^(-q/Q), which is equivalent to the displayed bound. The equation delta=(c_l-1)/c_l gives c_l=1/(1-delta). All comparisons are rational equalities. A digest check identifies the exact retained certificate bytes; it is not a substitute for their earlier mathematical verification.

The source summary is frozen once per run, so an edit made by the theory part during the audit cannot change the inspected table. Every grouped row must have exactly the same number and increasing root order as the aggregate table. The audit fails on an omitted, duplicated or extra group. Historical source bytes stored in a compression manifest are recovered and checked before their hash is compared.

## Scope and dependencies

The output certifies the radius table and amplitude arithmetic in the saved summary. It does not certify every theorem label elsewhere in that summary, asymptotic growth constants, sharp radii or newly proposed families. Dependencies are the admitted certificates referenced by current_certified_radii.json, their standalone proofs and the exact homogeneity and majorant results in topics01,131,132,169,172,175 and226. A later full report audit remains necessary.

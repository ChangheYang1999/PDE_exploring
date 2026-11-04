# Exact source013 compact table admitted

## Statement

Fix c=4076476460239181/2251799813685248 and authoritative Candidate007 with SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21. Add the frozen C2-N1-013 correction with raw SHA256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a and canonical SHA256 2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33. The accepted complete-source reconstruction has fields SHA256 3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb.

The compressed JSON table with SHA256 9ab660bd0b1117814ce2113a2bbff264a4484f180d02fdcc0e80d2b3801e94b6 represents exactly the five fields named linear, ux, uy, rx and ry in that accepted source reconstruction, at every positive radius and every angle. The statement uses the field definitions and Fourier convention of the accepted source evaluator. The table has7392distinct normalized radial factors and1041908nonzero rational coefficients.

This statement assumes the previously accepted reconstruction of the frozen source, exact rational arithmetic and the grouped-identity theorem in PROOF.md, independently accepted at AT867-872. It does not assume a numerical residual estimate.

## Complete verification argument

The source013 startup table producer completed under its independently accepted manifest and guard. Its source and complete-field hashes agree with those above. The independent admission reconstructed the same frozen source with the local accepted helper, retaining25940source polynomials. It parsed every table row, required positive scales, valid radial parities and integral denominator exponents, canonical scale normalization, integral modes, nonzero coefficients, and no repeated normalized factor key.

The independent procedure then grouped source and table terms by normalized scale, parity, denominator exponent, fractional radial exponent, named field and angular mode. As proved in PROOF.md, each group's equality is equivalent to an exact rational polynomial identity P(1-z)=Q(z). All22980grouped identities passed. This proves equality of each group for every positive radius; summing the finitely many groups and Fourier modes proves the stated equality of the five fields for every angle. No assertion of linear independence between different radial factors is needed.

The procedure checked the actual compressed archive hash before and after the algebraic comparison. Its retained evidence is verification/table_v01/receipt.json, SHA2565d08307d29f56b47bbe1654d8d6ddae10c72adf200538f7274c6e53ef5d898f6. The archive remains in the producing agent, linked relatively from verification/table_v01/source013_table_v01.json.zst. Small installation, producer-result and guard records are copied alongside the receipt.

The comparison ran from2026-11-03T11:56:38.805886Z to11:57:53.933412Z, taking75.12752256682143seconds. Its own accepted guard recorded successful exit0, no rejection reason and resumption of the previously held source009primary at11:57:54.269949Z. The guard's result hash matches the receipt. Thus the completed arithmetic evidence also satisfies its actual execution contract. The table is238724220bytes; it was not duplicated into this agent.

## Scope

CONFIRMED: exact equality of this table to the accepted frozen source013field representation, its counts and its successful guarded admission. The producer's independent per-polynomial reverse accumulation and this grouped identity are different checks of the same exact representation.

OPEN: the full source013planner union, coefficient enclosures in a primary calculation, annulus integration, origin and exterior bounds, whole-plane norms, background cover, continuum near/far bounds, L, invariant-ball closure and stationary existence. No energy or norm is inferred from this table identity. The statement is restricted to positive radii; origin regularity and disk integration use their separate accepted methods.

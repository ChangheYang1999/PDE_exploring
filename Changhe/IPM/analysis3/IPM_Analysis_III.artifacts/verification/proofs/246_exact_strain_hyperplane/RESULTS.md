# Exact input hyperplane result

Recorded 2026-10-28T17:05:41.618831+00:00. These are INPUT certificates only. No output matrix was read.

For each exact space W below, use its inherited LOW input norm. Let c be the exact source-defined strain and b the stored binary64 strain row, as exact rational data. The orthogonal projection P_W from ker b to ker c satisfies

    ||v-P_Wv|| < 6.244e-16 ||v||,    v in ker(b|W).

It is an isomorphism between these kernels and obeys the more precise norm comparison of PROOF.md(2). The exact c-zero dimensions are:

| W | Dimension of W | Dimension of W intersect ker c |
|---|---:|---:|
| Whole S1J1 input section |38|37|
| Its exact high input intersection |32|31|
| Its exact maximal high graph intersection |29|28|

The same kernel dimensions hold for b. The positive common reference direction is pure spline sp10, scaled column13.

The common directed bounds are ||(c-b)|W|| <3253/10^20, ||c|W|| >52024/10^6, and, using each space's own ratio, delta_W<6244/10^19. The last bound is checked separately for each W, not deduced from the ratio of the two coarser common bounds.

The primary calculation checks exact dyadic whiteners by640-bit interval congruences and exports them. Runtime 0.760252 seconds. An independent768-bit interval direct solve recomputes the three dual norms, without the whiteners, and confirms every displayed directed constant. Runtime 0.072061 seconds. An initial metadata-schema KeyError is preserved in evidence/initial_schema_failure.log; it produced no certificate.

PROOF.md SHA256 c90fc65d68d34e2656484279b1cb91469674a90b87b42ffe0c2c34af166f9970

Primary certificate SHA256 8714fd38312d89f348cbb5b700dc31e9300c48ccb98a8c9ba6515da8d97cd0d2

Direct replay SHA256 3a3cbe1fe5f0e7fe6dc2c60b447b46c48b69da4f9b64b7f2958c6fb4be500a0c

The exact input projection comparison does not certify an exact constrained singular value. That would require the missing image error bounds and, for a transfer argument, a quantitative bound on the operator acting on the correction. The low norm here is not a high norm. Analytic theorem adoption awaits actual independent review of the short proof and its established dependencies.

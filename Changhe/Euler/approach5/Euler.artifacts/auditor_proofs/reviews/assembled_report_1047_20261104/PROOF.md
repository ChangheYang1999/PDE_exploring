# Audit of report09f2ffd0 at cutoff A3170

## 1. Exact evidence and prior coverage

The candidate is coordinator pin09f2ffd09f963eaa3e8b573010e3b7a21a9f7ada337b29ed46f8b99814b31905, assembled10:35Z, with8076 newline-terminated lines and1283108 bytes. The base78e4ddbd was approved at cutoff A3165 in A3171. The retained42-line normal diff has five hunks and is byte-identical to a fresh normal diff of those two pins. All42 lines, the entire new LIT387 paragraph, its surrounding hypotheses and the new table row were read. This review concerns front matter, main Sections0-10 and AppendixA; historical appendices are not collectively certified.

## 2. A required distinction between the tail and the completed field

In Theorem8(o), U is explicitly assumed to equal the homogeneous formula only for |y|>=2. The new paragraph then defines

    M=(beta L)^(-1) integral_(S^2)|DU|^2

and identifies it with the large-radius gradient coefficient. This is not valid for the completed U as defined: S^2 lies inside the unspecified core. A compactly supported smooth divergence-free perturbation near S^2 can change that integral while leaving the homogeneous tail and the logarithmic coefficient unchanged. Explicitly let chi(r) be smooth, supported in(3/4,5/4) and equal to1 near1, and let W=curl[chi(|y|)|y|^2 e3/2]. Then W=(y2,-y1,0) near S^2, and the integral there of |DW|_F^2 is8pi. Replacing U by U+sW preserves solenoidality, the exterior formula and the energy ratio, while the displayed integral is a quadratic in s with positive leading coefficient8pi. The logarithmic coefficient is unchanged. No pressure condition repairs this kinematic mismatch.

The required repair is to define T(y)=|y|^t[k a-t(a.n)n+b cross n] for all y!=0 as the homogeneous extension of the tail and to use

    M=(beta L)^(-1) integral_(S^2)|DT(n)|_F^2,
    DU(rn)=r^(t-1)DT(n) for r>=2.

Alternatively define M solely as the limit of G_a/(beta L log R) and omit the incorrect sphere integral. A3176 already distinguishes these two fields explicitly. This is a notation error in the assembled statement, not a failure of A3166-A3167.

## 3. Checked mathematical transfers and two scope clarifications

With the repair in Section2, the normalization, necessary interval for rho, the two distinct parallel-axis extrema, strict-positive infima, absence of a common minimizer, amplitude ordering and nonzero core curl are the statements confirmed in A3166-A3167. The source version dd15d31d is status-only by A3177. The full gradient limit at each fixed center is justified by the homogeneous tail and the integrable translation error; the squared full spatial amplitude is the maximum of |DT(n)|_F^2. These do not require a homogeneous formula inside B2.

The phrase that the interval is sufficient for parallel axes but not for perpendicular ones should read “not sufficient in general for perpendicular axes.” A3167 gives perpendicular counterexamples near the upper endpoint; it does not assert that every perpendicular field in the interval fails. The phrase “These values bound the corresponding infima over larger classes from above” should explicitly say “larger kinematic classes containing these controls.” These controls give no upper bound for infima over actual Euler profiles, as A3178 records. All controls fail full momentum for every c,omega.

The final “No explicit gap above D_H is proved here” sentence is historically qualified by the stated cutoff; it should say “unconditional” even at that cutoff to distinguish8(p). More importantly the newly confirmed A3179 now supplies the unconditional explicit gap, so the next current assembly should replace it. This later theorem is not retroactively part of cutoff A3170.

## 4. Verdict and exact scope

The literal identification using DU on S^2 is refuted and requires repair before this candidate receives cumulative approval. The other LIT387 mathematical transfers checked in Section3 agree with their confirmed sources, subject to the specified scopes. No unrestricted profile nonexistence, larger-class optimum, numerical optimization or historical appendix is certified by this review. The prior approved report remains78e4ddbd at cutoff A3165 until a repaired candidate is checked.

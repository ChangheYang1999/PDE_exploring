# The universal assumption remark is too broad

Status: independently checked wording defect. The main theorem statements are not refuted. Recorded 2026-11-04T14:29:41.401611+00:00.

## 1. Exact claim and scope

In report 07ca41433a6f9b8a7858d4efd260a0e60e4779bda7d03d7559b2db653af97194, Section 3.1 says: "No theorem assumes a decay rate for U, finite energy, smallness of U or of omega, or a symmetry of U, except Corollary 2.1 (axisymmetry) and Theorem 7(a) (axisymmetry of the leading tail only)." The defect concerns the universal finite-energy clause. It is a statement about the report's hypotheses, not a claim that any Euler theorem is false.

Here finite kinetic energy means integral_R3 |U|^2 < infinity. Multiplication by the conventional factor one half does not affect finiteness. The report includes separate conditional variants, so the quantifier "No theorem" must include them or be explicitly restricted.

## 2. Complete contradiction to the literal wording

Theorem 8(i), lines 909-911, states a variant for every 0<c<1 and every finite omega: a C1 full Euler profile with work w of one sign is zero if U is in L^s and P-p0 is in L^(s/2), for some finite s>3/2 and some constant p0. Choose the permitted value s=2. Its assumptions then include U in L2 and P-p0 in L1. The first is exactly finite kinetic energy. The additional pressure assumption does not remove that hypothesis. Thus this stated variant assumes finite energy and is neither Corollary 2.1 nor Theorem 7(a).

The table itself correctly lists the separate L^s condition. The detailed work-sign theorem also explicitly says that its cases s<=2 in the bounded Hb class with 0<c<1/2 and c!=2/5 already follow from finite energy. No new Euler counterexample or mathematical theorem is needed to refute this universal description of the assumptions. The detailed conditional result and its older confirmations remain intact.

## 3. Narrow repair and regularity precision

One sufficient replacement is: "Theorems 1, 2, 4, 5 and 6 assume no prescribed velocity-decay rate or finite energy. Their other hypotheses remain as stated. The separate L^s variants in Theorem 8(i) retain their velocity and pressure integrability assumptions, including finite energy when s=2. The symmetry conditions in Corollary 2.1 and Theorem 7(a), and all other extra hypotheses in the table, remain explicit."

The finite-regularity sentence after Corollary 5.3 and the Theorem L row of the table should also say "integer r>=2". The complete Theorem L in Section 2D already requires an integer r. Its summary currently omits that qualification. This is a requested precision, not a refutation of a fractional-regularity theorem: no such theorem has been independently asserted or checked here.

## 4. Dependencies and verdict limits

The independently retained report and the exact excerpts identify the source. The complete Theorem 8(i) paragraph, the Theorem 5 finite-regularity paragraph, and the Section 3.1 table and remarks were read in bounded displays. The corresponding complete Theorem L statement was checked in the retained Section 2D source; it explicitly says integer. Source and excerpt hashes are in in the team records.

The claim "no theorem assumes finite energy" is REFUTED as worded. The current cumulative report approval must wait for a narrow repair or an explicit scope restriction. Older approved mathematical statements are not withdrawn. All growth, sign, integrability and smoothness conditions remain in force. The arbitrary-omega main conjecture is OPEN. This is a final-phase assumption audit, with no numerical experiment, formal build or new theorem direction.

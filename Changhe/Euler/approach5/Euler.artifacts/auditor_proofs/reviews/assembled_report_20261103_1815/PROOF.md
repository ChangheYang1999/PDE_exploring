# Repair audit of the coordinator's Note 103 report

Status: scoped repair check, CONFIRMED A2000-A2001; remaining summary precision A2002 OPEN; whole-assembly certification A2003 OPEN.

## 1. Object, hypotheses and read coverage

The object is the exact 6387-line report retained as this report, with SHA256 30b3e1f8649211bdc0c6be1434dc71603c80253b5d403a544414594acb5b2fcd. The snapshot manifest also fixes in the team records, THEOREM_ATTEMPTS.md and PROOF_OBSTRUCTIONS.md. The independent unified diff against the Note 102 snapshots has 218 lines for the report, 23 for README, 49 for attempts and 21 for obstructions. All these changes were read, including the appended revision-history paragraph, together with the complete 102-line README and the surrounding Theorem 7(g) statement and proof. This is not a fresh read of all 6387 lines.

The comparison is against the exact earlier mathematical verdicts A1939-A1999, not against the coordinator's summary of what changed. All assertions below retain the full-profile or abstract-tail distinction. Write E=|V|^2, S=P2-E/2, k=(cx-omega Jx).V and W=curl V as in the report. All occurrences of omega in the results checked here allow every finite real value unless explicitly stated otherwise.

## 2. Earlier requested repairs

The report summary now retains W.grad S=0 with k=0 in both affected rows. The standalone T41 now assumes the complete momentum equation and div U=0 on R3, defines p=(1-c)/c and gives finite uniform constants. These are substantive premises: with them the faithful-tail theorem applies, whereas a compactly supported divergence-free bump with P=0 refutes the statement without momentum. That example has zero tail and obeys the other bounds; it is not an Euler profile.

The C43 example now assigns the equatorial zero set to the scalar K, not to V. Indeed on the unit sphere V=(2-p)e3+p x3 x and X=cx at omega=0, so X.V=2c x3 while V=(2-p)e3 is nonzero on the equator in the target interval. The LIT268 row now restricts the vortical-density shortcut to actual helicity-free tails, or separately supplied vortical rank. The explicit LIT270 field shows why density and the reduced identities alone cannot supply that rank law.

The C57 row now states the uniformly sharp sufficient threshold over the reduced local class. It does not assert an individual-solution converse. The LIT273 formula now uses the velocity potential phi=-Re(B z^lambda)/a, U=grad phi and k=-a phi=Re(B z^lambda), with B nonzero and a chosen invariant domain on which the rank defect is nonzero. Differentiated twisted homogeneity gives precisely this contraction. The LIT274 row now excludes that specified germ; the zero-tail maximum principle is applied only in the separate no-exit, globally irrotational alternative.

The C60 margin statement now distinguishes exact positivity from three floating-point illustrations. Its exact formula gives epsilon(c)<=C T*(c)L^(-4), L>=1/(4-6c), so the margin tends to zero at 2/3. The report no longer states a uniform order 1e-15 over the full interval. The C61 integral estimate is the proved assertion and its fraction bound is a consequence, not an equivalent estimate with the same constant. L4 integrability is not converted to velocity vanishing. The F37 statement now retains its universal algebraic positivity test and the specific spatial-weight families analyzed. It does not purport to exclude all spatial weights or all Euler profiles. These ten repairs match their cited verdicts.

## 3. New upper-comparison paragraph

The added Theorem 7(g) paragraph accurately restricts CO67/LIT278 to smooth global tails. It states the global upper bound E<=r_+|S|, scalar transport W.grad S=0 and either k=0 or full rank on S!=0. For the rank alternative, the closed normalized one-form has a primitive with an additive linear-flow drift. Nonzero drift makes V and S nowhere zero and produces a compact regular level surface. Incompressibility and twisted homogeneity give zero sphere flux for c!=1/3, while that level has strictly signed velocity flux. Thus the drift vanishes.

The resulting invariant potential attains both extrema on the compact angular quotient. At the boundary of either extremal set, a nonzero tail has V=S=0 and a nonintegrable inverse-ratio weight. The elementary weighted Harnack proof therefore allows a positive lower comparison only near the entire common zero set. The Poisson equation is needed to conclude S=0 after V=0. These are precisely A1950-A1954 and A1974-A1978. The paragraph does not claim the natural-regularity improvement currently submitted in the auditor agent, nor an unconditional profile result. Its ledger and companion-file summaries retain these limits.

## 4. New matching paragraph and ledger rows

For 1/3<c<1/2 the added matching result assumes a nonzero irrotational germ with Q=P2+E/2=0. At omega=0, global C2 tail regularity supplies the one-sided third potential jet and a first-order supported rank zero, which the local harmonic lemma forbids. For arbitrary omega, global C3 tail regularity supplies the fourth potential jet and second-order rank zero. The two trace computations force c=1/3, outside the stated interval. No boundary smoothness or finite component count is used in obtaining the nonzero-velocity contact.

The counterexample to the first-order rotating lemma is kept local and analytic, with W=0 on its ball and therefore no supported vortical contact. Combining its F=DF=0 with the second-order obstruction gives D2F!=0, exactly as A1980. The new rows accurately distinguish the local lemma's wider c interval from the global matching interval, retain Q=0 and extra regularity, and do not erase the natural-regularity or general-Q problem. LIT279 and LIT280 were confirmed only after this report's last ledger update and are not required to be present in this pin.

## 5. Remaining precision in short summaries

Two short passages should be made self-contained at the next edit. The final README paragraph still says that global two-sided bounds "with k = 0 or the rank relation give U = 0". In the abstract k=0 alternative add W.grad S=0, as already correctly done in the main statement and earlier README paragraph. This is a scope clarification of the compressed recap, not a newly refuted theorem.

In section 7 (N3), the sentence "Without the rank relation a nonzero profile with these bounds has an open spiral sector" follows the newly weakened smooth upper-plus-local-lower comparison. The cited LIT271 sector theorem was established under the original global two-sided comparison and natural helicity-free profile hypotheses. Replace "these bounds" by that explicit original comparison. Likewise make "the comparison" explicit in the analogous section 10 sentence. No stronger sector theorem is certified just by inserting a new preceding paragraph. These are OPEN wording precision items; the exact Theorem 7(g) paragraph itself states its class correctly.

## 6. Scope and verification

A2000 confirms the ten earlier repairs, A2001 the scoped CO67/LIT275-LIT278 transfers. A2002 retains the two recap precisions above. A2003 does not certify the entire assembled report: unchanged sections were not all reread in this pass, and earlier unresolved mathematics remains unresolved. In particular this check supplies no derivative bound, no helicity premise, no scalar comparison and no general all-omega nonexistence from velocity decay alone.

Source snapshots and hashes are adjacent. This is file-based follow-up with the existing configured model coordinator; its actual provider runtime is not independently attested. All writes remain in the auditor agent.

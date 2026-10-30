# Component status and citation scope in the numerical final tables

This is a documentary audit. It proves no new integral identity or PDE theorem.

## Statement

For the exact frozen version of N3's `N3_FINAL_TABLES.md`, a whole-row
CONFIRMED label is supported by its cited N4 records only for the quantities
those records explicitly accept. In particular, N4-024 and N4-026 concern
d2, whereas N4-060 concerns Mpen2 G0 and G1. N4-028 confirms the first
immutable candidate's exact coefficients and leading sectors and excludes
its residual from the stated unweighted spaces. It assigns no finite
whole-plane norm. N4-166 explicitly confirms candidate007's complete Q3.

The conclusion concerns the supplied citations. It does not assert that
uncited Mpen2 or candidate001 finite norms are false, or that a possible
other independent computation could not establish them.

## Notation and dependencies

The labels G0, G1, P2 and Q3 have the definitions in the frozen table.
The candidate007 Q3 certificate uses
`Q3 = ||(1+4r^2)^(2/5) D^3 F||_2`, with the complete ordered tensor.
All dependencies are copied into `source` with byte hashes before checking.
The proof uses the exact accepted ledger passages, the retained007
comparison and full result, the retained Mpen2 G0/G1 comparison, and
the candidate001 sector certificate.

## Argument

Read each frozen cited ledger passage together with its claim, result and
verdict. An acceptance restricted to one named candidate and two named
quantities has no logical implication for a different candidate or further
quantities. Thus the citation pair024/026 cannot support the Mpen2 row,
and060 supports precisely that row's G0 and G1. The explicit final sentence
of028 excludes interpreting it as a finite-norm acceptance.

For007,166 supplies the full160-mode Q3 comparison and declares it
CONFIRMED. Check the saved result and comparison hashes, and interpret
their printed Arb balls as rational intervals: `[m +/- e]` means
`[m-e,m+e]`. The lower table endpoint must be below the lower bound ball,
and the upper table endpoint above the upper bound ball. The table's
claim that this quantity was not reproduced is therefore stale.

This audit can refute the scope of the blanket citations and the stale
status statement without refuting any numerical value. No membership,
existence, inverse estimate or candidate ranking is inferred.

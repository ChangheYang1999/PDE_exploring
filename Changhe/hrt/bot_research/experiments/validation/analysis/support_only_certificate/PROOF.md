# A certificate that does not need every matchup

Written 2026-10-31T21:18:14.803175+00:00, before its checker. This is a retrospective arithmetic deduction from completed protocols148,153 and154. There are no proposed new games or policy calls.

## Statement and hypotheses

Let the ordered policies be B,C,D,G,H,I,J,L,M,N,O,P, with exact definitions in the ten-policy declaration, wall-prefix-selector declaration and delayed-wall-counter declaration. Let A be any real12-by12 skew-symmetric payoff matrix that agrees with the measured rows G and O below. A win is1, a draw0 and a loss-1. The theorem concerns this fixed mathematical matrix. Actual source policies contain deadlines; measured matching assignments do not prove a load-invariant game law.

The measured G row is (1,1,0,0,-1,1,-1,1,1,1,0,1). The measured O row is (1,0,1,0,1,0,1,1,1,1,0,-1). Then the equal mixture p=(G+O)/2 has value0 against every such A. Within mixtures supported on G and O, p is the unique mixture with nonnegative payoff against every column. This statement does not need the unmeasured P pairs against C,D,H,I,J,M, nor any policy outside the stated twelve. The theorem also assumes diagonal entries zero through skew symmetry; no unplayed P self game is presented as measured.

## Complete argument

For a column j, p's payoff is (A[G,j]+A[O,j])/2. In the stated order this vector is (1,1/2,1/2,0,0,1/2,0,1,1,1,0,0), which is componentwise nonnegative. Thus p guarantees at least0 against any pure column, and by linearity against every column mixture. By skew symmetry A p is the negative transpose of p^T A, so every row has payoff at most0 against p. Hence both sides can secure value0, proving the claim directly without invoking an optimization solver or requiring the missing entries.

For uniqueness on this two-policy support, let t be the mass on G and1-t the mass on O, with0<=t<=1. Against H (also against J), its payoff is1-2t, so nonnegativity requires t<=1/2. Against P its payoff is2t-1, so nonnegativity requires t>=1/2. Both can hold only at t=1/2, and the previous calculation proves sufficiency. This is uniqueness on the specified support, not uniqueness among all twelve-policy mixtures.

## Evidence and proposed checks

Protocol148 provides the ten-policy table;153 supplies all O pairings and154 supplies P/G and P/O. The checker will revalidate parent receipt hashes, reconstruct all relevant outcomes from result records, enforce both assignments and full normalized history equality, and identify exactly23 unordered support pairs including G/G and O/O (46 existing games). It will explicitly check each retained terminal record stream and replay those46 histories with the unchanged engine; this is no new decision generation. All twelve support entries, including measured G/G, O/O and G/O, must match the two quoted rows.

For a finite executable cross-check, start from the complete measured eleven-policy block, add P's five measured old-policy pairs, and enumerate all729 choices in {-1,0,1} for the six missing unordered pairs. Each completion gets zero diagonal and reflected negative entries. Verify the certificate by exact fractions for every completion. Exhausting these729 finite completions corroborates the general real-matrix proof; it does not turn any completion into observed play.

The implementation must also reject the all-zero weight vector, negative weights, asymmetric matrices, and a changed G/P entry that destroys the certificate. Q is excluded because its games were ongoing when this proof was written. Final best.py and reserved D remain unchanged. Formal proof-assistant verification is not claimed.

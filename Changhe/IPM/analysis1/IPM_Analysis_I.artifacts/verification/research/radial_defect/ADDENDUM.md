# Signed forcing and completed scalar tests

In the generic defect-coefficient construction in PROOF.md, the symbols f_j mean the Taylor coefficients of the actual scalar right-hand forcing g. Thus q_+ uses -f_j from the density forcing, while q_- uses +f_j. Equivalently write g_j+lambda p_j-(j+1)p_{j+1}. The forcing remainder coefficient T_Q is unchanged by this sign. This makes the branch convention explicit; no bound changes.

The primary check passed 20 symbolic identities and 100 illustrative moment cases at 20 exact parameter rows, with 240 Arb512/iv180 enclosures and 400 inequalities. The fresh exact-rational series through K=300 passed 98 geometric remainder checks and 120 full-enclosure comparisons, including the20 initial-amplification factors. It does not use Arb, mpmath, numpy or the producer.

These tests validate the stated scalar formulas. They do not provide the actual forcing, initial Green anchors, candidate P/R models, interval coefficient radii or full cell/angular coverage needed for a finite-annulus certificate. The next application must retain the signed forcing and the exp(2t_a)exp((alpha+2)u) factor.

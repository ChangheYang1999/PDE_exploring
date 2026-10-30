# Rounded bounds in the producer's optional share note

This finite audit concerns paragraph (b) of N1's note dated18:51Z, copied to source/N1_note1851.md. It does not change NUMERICS_FINAL.md or the accepted N4-438/T4-509/N4-440 share conclusion.

Let g and x be positive real numbers satisfying the note's stated premises

    0.37668932470589 < g < 0.37668932470590,
    756.5312630768 <= x <= 757.8514372426.

Put y=1024g and r=y^2/x^2. Monotonicity in g and x gives

    1024*g_lo < y < 1024*g_hi,
    (1024*g_lo/x_hi)^2 < r < (1024*g_hi/x_lo)^2.

All displayed decimal inputs denote exact rationals in this argument. Exact cross multiplication verifies that y lies strictly between385.7298694988 and385.7298694989, and that r lies strictly between0.2590 and0.2600. Therefore r>1/4, as the note and the accepted certificates conclude. The exact lower monotonicity endpoint is below0.2591. More decisively, choose g=(g_lo+g_hi)/2 and x=x_hi: these satisfy the stated premises, but give r<0.2591. Thus the claimed enclosure[0.2591,0.2600] is not implied by the supplied premises. This counterexample is to that interval inference, not to a claim that the actual fractional norm share is less than0.2591.

The interval(385.7299,385.7299) is empty, so it cannot enclose y. The number385.7299 is a valid nearest-rounded summary of y at four decimal places. A valid replacement is either y approximately385.7299, explicitly an approximation, or385.7298694988<y<385.7298694989. A safe enclosure for the unregularized quotient r is0.2590<r<0.2600. No upper bound on the actual fractional G0 share is inferred from this unregularized quotient; N4-438 uses Plancherel only to obtain a lower bound for that actual share.

The checker reads the copied note as text, verifies the exact premises, computes rational endpoints and the explicit counterexample, and binds the existing N4-438/N4-440 roots without rerunning them. It preserves the above-one-quarter conclusion and every candidate classification. Code and results are in the named subfolders. No source integration, peer program, JavaScript, server, cluster, GPU or Lean/Lake execution is needed.

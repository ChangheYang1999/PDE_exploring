# Proof audit

Checked 2026-10-28T07:30Z. The radial contraction is one-Lipschitz by
its squared-distance identity. Cross-disk pairs obey the same exact
seminorm bound because the disk radii sum to the center separation.
The supporting disks meet only at a zero of both flowers.

At its own center the kernel mode +2 cancels the flower mode -2.
At the other center the uniformly convergent kernel expansion has
only modes -k, so multiplication by the flower gives nonzero modes
-k-2 and zero angular average. Thus both cross terms vanish exactly.
The two half-sized own contributions add to the stated integral.
The R=1/2 factor cancels 2^(-a) from the exact input seminorm.

The positive-series remainder follows by replacing each denominator
by a+N+1 and summing the geometric tail. The second-term lower bound
uses dominated parameter differentiation near a=0. Mollification needs
only convergence of one fixed output increment, not seminorm density.

Verdict: CONFIRMED. Formula evaluations are recorded in the neighboring
exact_angular_modes/verification/formula_checks.json. A matching second
term for M_a remains OPEN.

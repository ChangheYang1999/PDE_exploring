# Exact leading-tail separation of X3 and the normalized modal trial

This statement concerns the explicit original X3 density and the exact
normalized 260-mode trial rho0 from ../modal_repair/PROOF.md. Their stored
k and L agree as exact dyadics. The exact logarithmic outer knot, rather
than the separately rounded physical endpoint, defines the modal tail.

The leading-tail formulas in PROOF.md satisfy uniform angular limits
r^(-k) X3 -> ThetaX and r^(-k) rho0 -> ThetaM. The exact coefficient
T(1)=78259092636642149/9007199254740992 is positive and
6.19703<p<6.19704. ThetaX is not C7 at the y axis, whereas ThetaM is
analytic. In addition, two independent interval computations give at
exact theta=pi/4 the strict bounds

- 90.81020983980597 < ThetaX < 90.81020983980599;
- 90.81020983897880 < ThetaM < 90.81020983897882;
- 8.2716924477e-10 < ThetaX-ThetaM < 8.2716924478e-10;
- 80253 < D F(0) < 80254, the nonanalytic coefficient of PROOF.md (5).

Consequently, for every real gamma,

 X3-rho0 in L2(R2,(1+r^2)^(-gamma)dX) if and only if gamma>1+k.

In particular X3-rho0 is outside every whole-plane Hs for s>=0. No
finite unweighted Hs ball about rho0 contains X3. This clarifies the scope
of topic 102: its unweighted Sobolev exclusion ball cannot be a neighborhood
containing X3. The result gives neither an exclusion about X3 nor an
exclusion of exact solutions sharing the modal tail. It is compatible with
small weighted factor errors and high accuracy on finite domains. No
weighted Sobolev bound or quantitative finite-radius tail error is claimed.

Verification uses Arb at 512 bits with rational cyclic sums, and mpmath.iv
at 180 decimal digits with an independent interval complex recurrence.
They separately enclose the same exact real scalar normalization repair,
using its independently audited brackets. Each method must establish each
printed bound. The exact output/source audit and an authenticated actual
Claude Opus 5.5 closure review are required before a FINAL verdict.

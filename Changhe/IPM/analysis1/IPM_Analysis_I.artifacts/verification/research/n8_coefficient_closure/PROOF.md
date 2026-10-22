# Source coefficient closure from independent Hessian bounds

Status at proof writing: exact conditional implication proved; the completed velocity certificate and the scalar audit are pending. No global inverse or a posteriori endpoint follows.

Let the trial be the normalized modal_v2 density and its canonical velocity, with the audited archive and exact source bracket used in topics84 and85. Put delta=33/2000 and let P=(p,0) for any p in the stated bracket. Suppose the whole-disc bounds on B_(3delta)(P) are

 M_V=sup ||D^2 V||_F < 743/2500,
 M_rho=sup ||D^2 rho||_F < 5059/10000.

Then the coefficient constant in topic77, for a cutoff theta with delta||grad theta||_infinity<=2, satisfies

 C_V=(417/10) M_V+3 M_rho < 695547/50000=13.91094,
 E<=delta C_V < 22953051/100000000,
 kappa-E > 314446949/100000000,
 K_1=1/(kappa-E) < 100000000/314446949 < 3181/10000,

where kappa=1687/500. In particular E<kappa/2 and C_V<3374/33, the sufficient coefficient condition at this delta.

The proof is substitution of two strict positive upper bounds, multiplication by positive rationals, and reciprocal reversal on the positive interval kappa-E>0. The final reciprocal comparison is an integer cross multiplication. All scalar comparisons are checked independently as exact fractions and in Arb and mpmath.iv. Strictness is inherited from the squared ceilings in the two whole-disc certificates.

This closes the small-coefficient condition of the local source estimate. Applying that estimate still uses its other stated hypotheses, including V(P)=0, the exact derivative matrix, the source gradient bracket, the constant divergence, regularity, the cutoff definitions and the chosen function domain. The canonical strain sign is the one corrected in topic80. No numerical value for K_2, K_3, K_4, the rank-one denominator, a global inverse, or a residual norm is inferred from C_V. The original X3 numerical file is not silently identified with the repaired normalized trial.

The producer's N8v2 output is a separate reported enclosure. Freezing its code and metadata, or verifying its scalar C_V arithmetic, does not verify its modal Taylor models, Cartesian derivatives, distance mask or every rounding step. The present implication uses our two independent Hessian certificates instead. Any audit of N8v2 will state that distinction explicitly.

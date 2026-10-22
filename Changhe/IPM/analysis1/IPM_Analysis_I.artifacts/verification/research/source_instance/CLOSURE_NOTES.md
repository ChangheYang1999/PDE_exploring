# Completed-instance scope and explicit cutoff linkage

The v2 calculation completed at2026-10-21T02:02:38.402085Z with status PASS_FRESH_SOURCE_AND_LOCAL_INSTANCE. Each engine separately established both endpoint signs and all three whole-bracket inequalities. The original failed v1 run remains archived. The accepted exact input uses dyadic k and exact-real z, as spelled out in ADDENDUM; these are different parameters.

To make the last review's cutoff concern explicit, write zloc=X-P and R_V=V-D zloc. On B_(3delta), the segment formulas and the tensor Frobenius bound give

 |R_V| <= M_V |zloc|^2/2 <=(9/2)M_V delta^2,
 ||DV-D||_F <=3M_V delta.

For wvec=theta R_V and Ctheta=delta||grad theta||<=2,

 ||Dwvec||_F <=[(9/2)Ctheta+3]M_V delta <=12M_V delta.

The exact identity div V=trace D cancels the interior divergence term. Therefore

 |div wvec|=|grad theta.R_V| <=(9/2)Ctheta M_V delta <=9M_V delta.

Also ||qvec||<=3M_rho delta. Hence

 E<=delta[(9/2+(31/10)*12)M_V+3M_rho]
  =delta[(417/10)M_V+3M_rho].

These are precisely topic77 section4 equations(12)-(13), and precisely the scalar expression accepted in topic86. The cutoff derivative contribution is included, not omitted. This also explains why replacing Frobenius norms by individual component maxima would be insufficient; topics84 and85 bound the full Frobenius tensors.

The source rows are compatible with, and establish a bracket around, an exact zero of the trial velocity. They do not set mu=1. In fact the entire new mu enclosure lies below1 in both engines, which reinforces the distinction between this normalized trial and a stationary profile. No global normalized inverse or full residual closure follows.

The final local statement uses topic77's smooth zero-jet test class and its explicitly specified graph completion, with every annular, lower-order and remote term retained. The auxiliary inverse uses topic78's stated maximal transport domain and compact C4 coefficients. Its R and numerical operator norm remain unevaluated. Any stronger realization still requires a separate domain and matching argument.

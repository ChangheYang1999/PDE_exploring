# Exact structural checks for a campaign center plus an odd potential

Written 2026-11-03T00:27:49Z before the checker implementation or execution. The method applies to a named frozen trial; it does not register a new campaign candidate.

## Statement and input hypotheses

Fix c=4076476460239181/2251799813685248, lambda=1-1/c, mu=4/c-3, e=mu-2 and q=21/10. Let C be an exact campaign center whose normalization, origin slope a_C, first residual sector and full correction moments have already been certified. Bind its exact file, certified structure and exact origin record by SHA256. Let a frozen JSON specify a finite real potential

phi=sum a_m H_(n_m) s^(h_m)(1+s)^(b_m)(t_m+s)^(-d_m), s=x^2+y^2,

where H_n=Im((x+iy)^n), with rational a_m,b_m,t_m, positive t_m, positive odd integers n_m and nonnegative integers h_m,d_m. All JSON integer types must be integers without coercion; all exact rational values must be strings. Check tau_m=n_m+2h_m+2b_m-2d_m<=mu for every atom. Set h=-Delta phi, v=(-phi_xy,phi_xx), rho_star=rho_C+h and u_star=u_C+v.

The finite algorithm below exactly determines ell(h), the new slope a_star, the origin cap condition a_star>=q(2c-2), and the change in the leading residual sector r^e. Equality of these computed quantities to producer metadata is a separate exact check. A passed structural check does not certify any residual norm or new background.

## Origin calculation

Write the homogeneous cubic part as A s y+B Im(x+iy)^3. An atom with n=1,h=0 contributes a t^(-d)(b-d/t) to A; one with n=1,h=1 contributes a t^(-d). Atoms n=3,h=0 contribute a t^(-d) to B. Every other atom starts above degree3 and contributes neither. Taylor's formula at zero is valid since t>0. Summing exactly gives A and B.

The imported AT119 identities give ell(h)=2A+6B and partial_y h(0)=-8A. An independent Cartesian calculation verifies these particular finite identities: form Im(x+iy)^n by its binomial monomials, multiply by s^h and retain only degree<=3. Multiply by the exact first two radial Taylor coefficients t^(-d) and t^(-d)(b-d/t). If the resulting cubic monomial coefficients are p21 and p03, then ell(h)=2p21 and partial_y h(0)=-(2p21+6p03). Also A=(p21+3p03)/4 and B=(p21-p03)/4. These identities follow from s y=x^2y+y^3 and Im(x+iy)^3=3x^2y-y^3. The two constructions therefore agree exactly without a sample near zero.

Normalization is the rational equality A+3B=0. Given c+ell_C=1, it implies c+ell_star=1 and F_star,y(0)=0. The new slope is a_star=a_C-8A. Check a_star>0 and a_star-q(2c-2)>=0 separately after using the final exact coefficients. For positive slope, the imported AT167 origin formula gives beta_origin=c+1-q-max(q(2c-2)-a_star,0); its equality to the cap requires the second inequality. No global matrix assertion follows.

## Leading far sector

For a single atom, positive scales give phi_m=a_m r^(tau_m)sin(n_m theta)(1+O(r^(-2))) with termwise differentiable remainder on a sufficiently large exterior. The polar Laplacian yields

h_m=a_m(n_m^2-tau_m^2)r^(tau_m-2)sin(n_m theta)+O(r^(tau_m-4)).

Thus the correction's coefficient at r^e is the exact sum a_m(n_m^2-mu^2) over atoms with tau_m=mu. Atoms of smaller degree contribute no term at e. The campaign background fields are O(r^(1/c)) with their differentiated decay. Hence u_C.grad h and v.grad rho_C are O(r^(e-lambda)), while v.grad h is O(r^(2e-1)); both exponents are strictly below e. The linear transport contribution at e multiplies the density coefficient by ce-1. Consequently the full residual leading sine map is

f_e,star(n)=f_e,C(n)+(ce-1)sum_{m:n_m=n,tau_m=mu}a_m(n^2-mu^2).

Every contributing atom and every frequency in the union support must be included. Exact zero combined coefficients are removed only after summation. If the resulting map is nonzero, angular orthogonality gives its full-circle L2 norm sqrt(pi sum_n f_e,star(n)^2). Outward Arb arithmetic bounds this scalar. If it vanishes, this algorithm does not assert a next surviving exponent; it reports the cancellation. A leading asymptotic coefficient alone is not an exterior norm at a specified finite radius.

## Imported membership and verification

For C5, AN057 verifies the full moment premises, and AT174 supplies the composite application of AT119/AT162. Subject to the checks above, the correction (rho_C-rho_007)+h has all-order weighted Sobolev membership for sigma<4lambda and positive weight scale, and its velocity is the canonical sum. We import that established implication; this finite checker does not re-prove it. In particular sigma=7/5 satisfies the strict range by exact rational comparison.

Hash every input and mathematical method before accepting a record. Recompute the scalar origin identities through both formulas, compare all producer exact identities, compare every leading-sector metadata entry on the union support, and record all rational outputs. Round displayed endpoints outwards by exact fraction comparisons. A separate reducer can use Python Fraction and the Cartesian cubic construction to verify a saved primary output, without importing producer code. Finite rational identities are independent of numerical conditioning. Diagnostic ratios of sums of absolute origin contributions to their signed sums quantify cancellation only in those particular formulas, not a matrix condition number.

## Scope

An immutable draft may pass these checks and remain a trial. The certified function is identified by its actual input hashes, not an optimizer run name or a grid. Norms, high derivative bounds, gradient transfer, complete background cover, inverse constants and invariant-ball closure remain separate obligations. A structural failure is preserved and reported rather than silently repaired. No unverified decimal tolerance is used as a zero test.

# A necessary residual test for the conditional iteration

## Statement

Use the precise spaces, moving-tail chart, operators, domains and constants of proof 174. Thus X and Y are either its original low correction and target spaces, or its decoupled spaces with one fixed angular exponent in [18/5,4]. The high correction space is H, the high target is Y_H, f_0 is the exact normalized original residual, eta_H=||f_0||Y_H, and A_h is the exact operator defined there. Assume both base low injectivity (I) and the inequalities (S). Write R=K_H eta_H and q_0=K_L C R<1, and define h_0=0 and h_j=-A_(h_(j-1))^(-1)f_0 for j>=1.

For every j>=1, the full nonlinear residual belongs to Y and satisfies

 F_(ell(h_j))(rho_(ell(h_j))+h_j)
       =(A_(h_j)-A_(h_(j-1)))h_j,                     (1)
 ||F_(ell(h_j))(rho_(ell(h_j))+h_j)||Y
       <=q_0^j ||f_0||Y.                             (2)

If ||f_0||Y>0, every admissible choice of constants in (S) therefore satisfies

 q_0 >= ||F_(ell(h_1))(rho_(ell(h_1))+h_1)||Y/||f_0||Y. (3)

In particular, if the exact first iterate has residual norm at least ||f_0||Y, no admissible constants can satisfy (S). This last assertion is conditional on having the exact base inverse and an iterate in the family where the stated identities hold. A finite-section or collocation iterate alone does not test (3).

## Proof

Proof 173 puts every high correction in the low maximal domain of each operator in the prescribed family. Thus both A_(h_j)h_j and A_(h_(j-1))h_j are legitimate Y-valued expressions. Proof 174 proves the exact moving-tail identity

 F_(ell(h))(rho_(ell(h))+h)=f_0+A_h h.

Insert h=h_j and subtract its defining equation A_(h_(j-1))h_j=-f_0. This proves (1) as an identity in Y, including the exact exponent variation.

The high inverse estimate gives ||h_j||H<=R for all j. Subtraction of adjacent iteration equations and the all-domain embedding give

 ||h_j-h_(j-1)||X<=q_0^(j-1)||h_1||X.

For j=1 this reads an equality bound and uses no contraction step. Applying the base low inverse estimate to h_1 gives ||h_1||X<=K_L||f_0||Y. The low/high operator difference bound in proof 174 now yields

 ||(A_(h_j)-A_(h_(j-1)))h_j||Y
 <=C ||h_j-h_(j-1)||X ||h_j||H
 <=C q_0^(j-1)K_L ||f_0||Y R
 =q_0^j ||f_0||Y.

This proves (2), also when q_0=0 by the direct preceding product inequality. Division by the strictly positive residual norm at j=1 proves (3). The actual trial has positive low residual norm in both settings by V164 and V179, so this nonzero hypothesis is available there.

## Interpretation and scope

The result is a necessary consequence of the specific sufficient smallness conditions (S). Failure of its first-step test refutes those conditions for the exact trial and norm choices. It does not prove nonexistence of a nearby exact IPM profile, and it does not rule out a different iteration or a better trial. Conversely, a residual reduction at the first step does not prove injectivity, a uniform inverse, the bounds in (S), or convergence.

The norm ratio is unchanged by multiplying the low target norm by a positive scalar. If an approximate first iterate is used, a quantitative error bound for both its distance from h_1 and its nonlinear residual is required before drawing the asserted conclusion. No such first-iterate computation is certified here.

Dependencies: proof 173 for domains; proof 174 for the inverse family, difference inequality and exact nonlinear identity; V164 and V179 only for positivity of the actual low residual norms. This independently verifies the theory author's Claim NT of 2026-10-28 12:20Z, with the nonzero denominator and exact-iterate scope made explicit.

# Strict separation for every sufficiently small exponent

## Statement

On real homogeneous Holder functions on R^2 modulo constants, with seminorm

    [f]_alpha = sup_(x!=y) |f(x)-f(y)|/|x-y|^alpha,

let C_alpha be the norm of the circular principal-value operator with kernel
K_xx(z)=(z_1^2-z_2^2)/(2pi|z|^4), and let D_alpha be the norm of
R_1^2=T_xx-I/2. The operators are extended through absolutely convergent
increments, as in the accepted basic operator proof. The same constants
apply to complex scalar inputs.

There exists alpha_0>0 such that, for every 0<alpha<alpha_0,

    D_alpha-C_alpha > C_0/2 > 0,
    C_0=1/2+(log 2-1)/pi.

No explicit value of alpha_0 is asserted. This is an immediate corollary of
the accepted second-term asymptotics, not a new quantitative estimate.

## Dependencies and proof

Theorems 5.4 and 5.6 in the lead report, independently checked in the earlier
verification records, give

    C_alpha=2/(pi alpha)+C_0+o(1),
    D_alpha=2/(pi alpha)+2C_0+o(1).

Subtracting gives D_alpha-C_alpha=C_0+o(1). Since pi>2 and log 2>0,
C_0>1/2-1/pi>0. By the definition of the limit, there is alpha_0>0 such
that |D_alpha-C_alpha-C_0|<C_0/2 whenever 0<alpha<alpha_0. The stated
inequality follows. No continuity of the sharp operator norm is needed.

## Scope of the correction

The report's sentence that strict separation is unproved outside the ten
tabulated exponents is too strong. The exact second-term asymptotics prove
it for an entire punctured neighborhood of zero. The issue is only this
sentence. The assertion that separation for every 0<alpha<1 remains open
is consistent with the proved results. An appropriate replacement is:
"Strict separation holds at these ten exponents and for all sufficiently
small positive alpha, by the exact second-term limit. A proof for every
0<alpha<1 is still open."

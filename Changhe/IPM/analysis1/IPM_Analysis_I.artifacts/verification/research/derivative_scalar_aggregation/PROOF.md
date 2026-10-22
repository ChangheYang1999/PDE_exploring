# Scalar aggregation of saved derivative majorants

## Statement, input semantics and scope

This result concerns the three saved numerical-lane derivative JSON files named in evidence/manifest.json. Their completed row counts are7809 middle,2632 inner and8948 outer. Each JSON numerical token is interpreted as the exact IEEE754 binary64 number recovered by round-trip decoding, because the producer serializes binary64 values. The derivative sums and m_inf are consequently exact rational scalars for this finite audit. This interpretation does not certify how the producer obtained those values.

For every row let w_ij denote its nonnegative W_i_j and let m be its positive m_inf. Define

    A = (w_10+w_01)/m,
    B = (w_20+2w_11+w_02+w_10+2w_01)/m.

The finite assertion to be checked is that the maximum of A over all19389 saved rows is strictly less than4195/10000 and the maximum of B is strictly less than3566/5. The maxima and their row identifiers are certificate maxima. They are not points at which a physical residual reaches its maximum. Also aggregate the saved zeroth, eps-minus-Eeps, K and E K bounds by division by m, and their products with the saved nonnegative wf_sup. Their output is exact rational data rather than preassigned numerical conclusions.

This assertion gives conditional physical derivative bounds only if each row's w_ij bounds the indicated derivative of the same exact residual throughout its cell, m is a valid lower bound of the intended weight, and the cells cover the asserted region. None of those hypotheses is established by this finite scalar audit. In particular, this result does not certify the derivative Taylor models, midrad arithmetic, canonical Green input, true cell endpoints, far tails, derivative forcing norms, any inverse or any IPM endpoint. The producer's done flag is a file-status check, not proof of those hypotheses.

## Conditional Cartesian derivative implication

Let f be C2 on a polar annulus, t=log r, c=cos theta and s=sin theta. Write f_t and f_theta for derivatives in these coordinates. Since the polar frame is orthonormal,

    r |grad f| = sqrt(f_t^2+f_theta^2) <= |f_t|+|f_theta|.

Directly applying d_x=r^-1(c d_t-s d_theta) and d_y=r^-1(s d_t+c d_theta), including derivatives of r^-1,c,s, gives

    r^2 f_xx = c^2 f_tt -2cs f_ttheta +s^2 f_thetatheta
               +(s^2-c^2)f_t +2cs f_theta,
    r^2 f_yy = s^2 f_tt +2cs f_ttheta +c^2 f_thetatheta
               +(c^2-s^2)f_t -2cs f_theta,
    r^2 f_xy = cs f_tt +(c^2-s^2)f_ttheta -cs f_thetatheta
               -2cs f_t +(s^2-c^2)f_theta.

Every displayed coefficient has absolute value at most1. Thus the even smaller componentwise bound w_20+w_11+w_02+w_10+w_01 is valid if all w_ij are genuine derivative majorants. The reported numerator of B dominates it, since the w_ij are nonnegative. This proves the claimed implication for every second Cartesian partial derivative. It does not call B a Frobenius Hessian bound: for f=log r, the Frobenius norm of r^2 D2 f is sqrt2, while the reported expression with w_10=1 and all other derivative sums zero is1.

If m is a positive lower bound of the true weight, division by m and the maximum over a covering collection preserve these inequalities. A saved multiplier wf_sup similarly gives a weighted inequality only under its independent validity hypothesis.

## Independent finite verification

Freeze the original reports, derivative sources and JSON files by digest. Export the finite binary64 inputs used here to exact bit strings in a compressed JSON-lines file and register its digest. The first calculation converts decoded binary64 inputs to exact fractions and evaluates every scalar expression by rational arithmetic. It independently checks the Cartesian identities by a symbolic differential-operator calculation.

A second calculation reconstructs fractions directly from the sign, exponent and significand bits, checks that the original JSON decimal tokens lie in the round-to-nearest cells of the exported values, and compares every row expression with the first result. Arb and mpmath.iv independently enclose the ratios and weighted products. Exact rational output and strict rational comparisons decide the advertised ceilings; decimal displays are informational. Exact agreement validates the finite arithmetic only, with the physical hypotheses still OPEN.

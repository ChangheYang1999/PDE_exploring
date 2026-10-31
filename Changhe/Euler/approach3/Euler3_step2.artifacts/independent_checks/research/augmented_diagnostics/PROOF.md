# Finite augmented residual diagnostics

## Statement, spaces and hypotheses

Let c lie in (2/5, 1/2), let alpha=(1-c)/c, and let K be a nonempty finite collection of positive-volume domains. Each domain has a nonnegative reference radius r_k and a finite quadrature rule with nonnegative weights summing to one. The velocity and five momentum terms are vectors in R^3 at each node. Write R for their sum, T_1=(1-c)U, A_k for the quadrature RMS of R, and B_k for the quadrature RMS of T_1. Assume B_k>0. These are quadrature quantities, without an assumption that they equal exact volume integrals.

Define sigma_k=A_k/B_k, a_k=(1+r_k)^(2 alpha+1) A_k, sigma(K)=max_k sigma_k and a(K)=max_k a_k. For a ball B(y_*,b), the registered reference radius is |y_*|. Its separately reported upper-radius weight is (1+|y_*|+b)^(2 alpha+1) A_k. On ordinary domains the two weight conventions coincide.

Then:

1. Each maximum is attained. Adding domains cannot decrease either maximum.
2. The upper-radius maximum is at least the center-weight maximum.
3. For T_1 through T_5 with positive sum of RMS values, sigma_k=rho_k times (sum_i RMS(T_i))/B_k, where rho_k=A_k/(sum_i RMS(T_i)). Thus a reduction of rho alone need not reduce sigma.
4. A maximum over the union of two quadrature records is the larger of their separate maxima, even when they approximate the same physical domain. This identity does not bound the quadrature error.

The denominator screening rule is part of the diagnostic definition. Put D_k=(1+r_k)^alpha B_k. A domain is flagged when D_k<10^-14 max_j D_j. Within each radially ordered shell family, an interior domain is also flagged when D_k is below 10^-3 times each neighboring D. A flagged domain is retained in the output and cannot be used as a successful acceptance check. No small constant is added to B_k.

## Proof

There are finitely many real values in each maximum, so one attains it. A larger collection contains an old maximizer, proving monotonicity. Since alpha>1 and b>=0, the positive power 2 alpha+1 preserves the inequality 1+|y_*|+b>=1+|y_*|; multiplication by A_k>=0 and then maximization give item 2. Canceling the positive sum of term RMS values in the right side of item 3 gives A_k/B_k. Finally the union consists of the values from the two individual collections, so none exceeds the larger maximum and one attains it. This proves item 4.

The screening rule makes no mathematical inference from a small denominator. It marks a numerical evaluation that requires further resolution. The strict inequalities at the thresholds are retained exactly as stated.

## Dependencies and scope

The quadrature and pressure constructions are described in the adjacent holdout_quadrature, displaced_ball_quadrature and pressure_consistency proofs. No interpolation or continuum estimate is proved here. The implemented aggregation operates on previously audited floating-point RMS values. Its formula checks and finite maxima do not certify the underlying integrals, continuous maxima of U or vorticity, cross-degree core resolution, full-space norms, stationarity, or a solution of Euler.

For the current campaign the core-augmented set is both shell families, the registered core ball, one unit-ball quadrature and the two displaced balls. Both direct and composite unit-ball records are reported separately and as a union. A supplementary union also includes the physical comparison shells, origin neighborhood and far thin annuli. Reporting these distinct sets prevents an unmeasured or unfavorable domain from being silently substituted.

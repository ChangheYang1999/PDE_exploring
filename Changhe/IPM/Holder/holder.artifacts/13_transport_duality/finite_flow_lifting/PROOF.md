# Lifting a finite flow with signed divergence

## Statement

Let (X,d) be a metric space, let J be finite, and let A_j be nonempty measurable subsets of X. Fix real numbers m_j with sum zero. For m_j nonzero let sigma_j be a positive finite measure supported in A_j, of mass |m_j|. For m_j=0 choose any probability measure theta_j supported in A_j. For m_j nonzero put theta_j=sigma_j/|m_j|. Let pi_jk be nonnegative real numbers satisfying

    sum_k pi_jk - sum_k pi_kj = m_j

for every j. Suppose c_jk bounds d(x,y)^alpha on A_j times A_k whenever pi_jk>0, where 0<alpha<=1. Then every real or complex function f with Holder seminorm [f]_alpha obeys

    |sum_(j:m_j!=0) sign(m_j) integral f d sigma_j|
        <= [f]_alpha sum_jk pi_jk c_jk.

The same statement applies to a measurable parameterized family of these data and can be integrated against a positive parameter measure whenever the right side is integrable and the signed functional is defined. Separate positive-to-negative transport marginals are not required.

## Proof

For each ordered pair define the product measure pi_jk theta_j times theta_k. Their finite sum Pi is nonnegative. Its first marginal minus its second is

    sum_j (sum_k pi_jk - sum_k pi_kj) theta_j
      = sum_j m_j theta_j
      = sum_(j:m_j!=0) sign(m_j) sigma_j.

Vertices of zero divergence contribute zero regardless of the chosen theta_j. In particular, a flow may pass through a zero-mass cell; no division by its mass is used. Integrating f(x)-f(y) against Pi therefore gives the signed functional in the statement. Its modulus is at most [f]_alpha integral d(x,y)^alpha dPi, and the supportwise distance bound gives the claimed finite sum.

For parameterized data the same identity holds at each parameter. Measurable choices, for example normalized density restrictions for nonzero masses and a fixed angular center for zero masses, make the product kernels measurable. Integrate the pointwise bound. Absolute integrability of the bound permits the necessary changes of integration order. If a singular endpoint is present, first work on compact parameter intervals and then pass through the separately established endpoint bound.

## Application and scope

In Theorem 3.7 of the team report, A_j is an angular cell on either of the two local circles at the fixed radius. The sigma_j are the extracted signed-density magnitudes. A point mass at the center of a zero-mass angular cell supplies theta_j there. Every distance used in the theorem bounds all points of the cells, so it also bounds these choices. This completes the lifting argument for the theorem's general nonnegative flow formulation, including transshipment through zero-mass cells. No new numerical constant or singular-integral convention is introduced.

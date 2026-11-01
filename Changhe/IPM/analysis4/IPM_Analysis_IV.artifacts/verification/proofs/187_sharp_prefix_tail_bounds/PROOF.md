# Sharp derivative tails from the total majorant budget

Status: PROVED analytically by the argument below and the theory part's independently stated argument, checked as V360. Exact numerical evaluations are recorded separately.

## Statement and hypotheses

Use the exact notation and hypotheses of topic 184. In particular, 0<delta=2h/Q<1, N is a positive multiple of Q, and a certified prefix box at w0 has nonnegative components b_r and e satisfying

    sum_{k>=0} x_(N+r+kQ) w0^k <= b_r,
    sum_{k>=0} eta_(N+kQ) w0^k <= e,
    n ||f_n||_1 <= x_n,  n |H_n| <= eta_n,
    ||g_n||_1 <= L ||f_n||_1 + |H_n|.

The angular frequencies are at most Bn. Let J>=N be an integer, let z>0 with t=z^Q/w0<1, and use K_r, K_E and m_r=N+r as in 184. For integers d>=0 define

    S_d(m,K,t) = sup_{k integer, k>=K} (m+Qk)^(d-1) t^k.

In particular S_0=t^K/(m+QK), and S_1=t^K. Set

    Dsharp_d = sum_{r=1}^Q b_r z^(N+r) S_d(N+r,K_r,t),
    Esharp_d = e z^N S_d(N,K_E,t).

All tail inequalities in topic 184 hold with Dsharp_d and Esharp_d in place of D_d and E_d. These sharper quantities are no larger than the old quantities. They are rational and exactly computable when z, w0 and the box are rational. For each residue class they are the smallest possible upper bounds obtainable from that class's total nonnegative budget alone.

## Complete proof

Write c_k=x_(N+r+kQ) w0^k. Then c_k>=0 and sum c_k<=b_r. Consequently

    sum_{k>=K_r} (N+r+Qk)^(d-1) x_(N+r+kQ) z^(N+r+Qk)
      = z^(N+r) sum_{k>=K_r} c_k (N+r+Qk)^(d-1) t^k
      <= b_r z^(N+r) S_d(N+r,K_r,t).

Apply the same argument with c_k=eta_(N+kQ) w0^k. Summing over the residue classes proves the moment inequalities. The radial multipliers, angular bandwidth bound, Poisson norm estimate and uniform convergence argument are exactly those proved in 184. This completes the tail proof.

For d=0 the sequence decreases strictly because its successive ratio is t(m+Qk)/(m+Q(k+1))<1. For d=1 the ratio is t<1. For d>=2 the successive ratio is

    q_k=t(1+Q/(m+Qk))^(d-1).

This decreases strictly to t<1. Thus the least integer k>=K with q_k<=1 maximizes the sequence. If equality holds, k+1 gives the same value. Find this integer by doubling an upper endpoint until its ratio is at most one, then binary search. This uses comparisons and always terminates. When m, Q and t are rational, all comparisons are exact rational comparisons and the attained maximum is rational; no rationality is asserted for arbitrary real t. Concentrating the entire permitted budget at a maximizing k attains the class bound, proving its stated optimality. This optimality concerns abstract budgets and says nothing about the actual IPM coefficients or the best convergence radius.

The old moment bound is a sum of the same nonnegative terms for d>=1 and an upper bound for that sum for d=0. A maximum is no larger than a sum, proving the comparison.

## Primary radial normalization and amplitude

For unit leading amplitude, multiplying the 184 density inequality by r^delta=1/z gives

    ||r^(-gamma) (r d/dr)^a d_theta^b rho_tail||_infinity
       <= max(delta,1-delta)^a B^b Dsharp_(a+b)(z,J)/z,

with gamma=1-delta. For the stream replace r^(-gamma) by r^(-1-gamma), replace the radial factor by (2-delta)^a and use (L Dsharp_(a+b)+Esharp_(a+b))/z. The inequalities hold in the angular Wiener norm as well. Each right side is nondecreasing in z because it is a maximum or sum of nonnegative powers z^(n-1), n>J>=N>=1. Thus its value at z=R^(-delta) bounds the whole exterior r>=R.

For arbitrary nonzero real leading amplitude epsilon, homogeneity gives the same bounds with z replaced by z_e=|epsilon|r^(-delta) and the entire right side multiplied by |epsilon|. This statement uses the expressions divided by z_e. It does not identify amplitude reduction with a new convergence mechanism.

## Dependencies and scope

The only analytic dependencies are the certified total budgets of 172/175, the Poisson estimate of 169, and the tail argument of 184. The supremum argument was independently proposed by the theory part on 2026-10-31 at 13:48 UTC; its source excerpt is retained here. No external theorem, asymptotic fit or numerical cancellation assumption is used. Strict exteriors remain the scope of all-derivative convergence.

## Exact examples

At 2026-10-31T13:56:17+00:00, V362 confirms: Five certified prefixes give exact primary-normalized tail bounds at J=N,N+Q,N+2Q. All 516 integer maxima and 150 density/stream derivative pairs replay exactly; 648 additional maximum-search cases also pass. The two-mode root4 at N36, R=2^(135/4) has density angular orders0..3 bounded by2^(-448),2^(-440),2^(-433),2^(-426), and stream by2^(-446),2^(-439),2^(-432),2^(-425). Candidate-shaped root1 at N27, R=2^(171/4) has density bounds2^(-399),2^(-390),2^(-381),2^(-371), and stream2^(-396),2^(-386),2^(-377),2^(-368). All hold on the closed exterior with primary weights r^(-gamma),r^(-1-gamma) and unit leading amplitude. Exact inputs, further cases and amplitude scaling are in187/verification/BOUNDS.md. Computation 1.1234764410182834 seconds, replay 4.121704905293882 seconds.

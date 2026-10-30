# Independent arithmetic of the exterior-onset bounds

Let an S1 forcing have, for every r>T, the exact exterior sine coefficients

    F_n(r)=e_n r^(-2-sigma), sigma>0.

The audited exterior Dirichlet theorem gives

    ||F||Hdot^-1^2 >= pi T^(-2sigma) S/(2sigma),
    S=sum_n e_n^2/(n+sigma)^2.

Consequently the necessary condition ||F||Hdot^-1<=tau, tau>0, implies

    log10 T >= [log(pi)+log(S)-log(2sigma)-2log(tau)]
                    /(2sigma log(10)).                    (1)

This is exactly the onset in T2 Remark R3, evaluated through logarithms of the squared quantity. The code uses exact rational summation for S before making a single Arb conversion. It also computes the unweighted angular amplitude A=(pi sum e_n^2)^(1/2), the effective amplitude A_eff=(pi S)^(1/2), and the exact truncated-model amplitude through sum e_n^2/[n(n+sigma)]. These formulas follow from the independently audited exterior and truncated norm identities, not from quadrature.

The input JSON holds the complete rational sine vectors for branches6,7,8. The code verifies sigma=(j+1)(1-1/c)-3 against the exact residual exponent stored for each j, and compares every branch6 coefficient exactly with the separately sourced Analysis II vector. The input c and every tolerance are rational. Interval logarithms and square roots use Arb with384 bits. The independently produced intervals are compared with the printed interval values in T2's frozen arithmetic log; overlap is recorded separately from their mathematical interpretation.

The numbers certify only (1) under the displayed exterior hypothesis. With relative modewise error at most epsilon, the corresponding common-factor necessary onset is reduced by (1-epsilon)^(1/sigma), as in the audited remainder theorem. An asymptotic leading vector without a certified onset and remainder does not imply any of these numerical inequalities for a candidate. In particular, no branch count alone is ruled out by this table. The fixed-degree family obstructions elsewhere use additional hypotheses and are unaffected by that limitation.

Status before execution: the arithmetic certificate is pending. A successful output must report exact vector agreement and all requested interval comparisons. No optimization or candidate residual evaluation is part of this script.

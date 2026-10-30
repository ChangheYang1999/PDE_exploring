# Corrected Opus cross bound and exact candidate017 origin regularity

## Statement, hypotheses and scope

Use the real canonical residual of candidate017 with raw SHA2567dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114 and c=4076476460239181/2251799813685248. The accepted construction is rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy), F=(cX+U).D rho-rho, on the whole plane with Lebesgue measure. For a positive odd mode n, write F_n=f(r)sin(n theta), psi=u(r)sin(n theta), Q=||rF_n||2^2, d=||Dpsi||2^2 and a=||Z||2^2, where Z=-u' sin(n theta)e_r-(r u''+u')cos(n theta)e_theta/n. Let u be a finite real linear combination of r^3(1+r^2)^(-beta)(r^2/(1+r^2))^k with beta>3/2, integer k>=-1 and 3+2k-n a nonnegative even integer. Assume Q<infinity and d>0.

The corrected T2 revision1 gives the valid auxiliary bound

 |integral r^2 F_n Delta psi dx| <= n sqrt(Q(a+d)).

All main identities and inequalities accepted in T4-501 remain unchanged. Candidate017's exact2174 smooth generators imply that F_n is locally integrable and O(r) at the origin, discharging the separate local-integrability premise. N4-432 confirms the same statement, correction and finite examples. This result accepts its structural check and the T2 literal repair. It does not establish any new residual-mode value, full017 upper bound, E2, correction or existence theorem.

## Proof of the corrected estimate

The accepted integration-by-parts identity is ||r Delta psi||2^2=n^2(a+d); its boundary term vanishes by the stated trial conditions. Cauchy-Schwarz applied to rF_n and rDelta psi gives the estimate. Its right side is finite, so the absolute convergence argument is preserved. The other two pairings obey |p|<=sqrt(Qd)/n and |b|<=sqrt(Qa)/n with p=integral F_n psi and b=<A_Fn,Z>; these follow respectively from ||psi/r||2<=sqrt(d)/n and ||A_Fn||2=sqrt(Q)/n. None of these estimates alone infers unweighted local integrability of F_n from Q.

For the explicit admissible n=3 trial u=r^3(1+r^2)^(-3), choose F_n=Delta psi=-48r^3(1+r^2)^(-5)sin(3theta). Exact integrals, divided by pi, give d=6/35, a=2/63, p=-6/35, b=2/63 and Q=cross=64/35. Thus sqrt(Q(a+d))/pi=64/105 if the unscaled quantities are used consistently, and the corrected right side divided by pi is64/35. The old bound fails by exactly3. T4-501 independently calculated these values by rational beta recurrences. The present checker compares the new T2 erratum and N4-432 values against those frozen exact results, verifies the relevant squared inequalities for all three additional fixtures, and checks every changed T2 text block. It does not rerun a quadrature or a peer program.

## Candidate-specific origin condition

The exact potential is a finite sum of terms H_m(x,y)(1+r^2)^e t_R^w u_R^q P_j(2t_R-1), where H_m=Re(x+iy)^(2m), e is real, R>0, t_R=r^2/(R^2+r^2), u_R=R^2/(R^2+r^2), and m,w,q,j are nonnegative integers. The exact generator conventions and canonical field identity were accepted in T4-495 and its frozen projection proof. Each denominator is positive in a neighbourhood of zero; real powers of positive smooth functions, nonnegative integer powers and polynomials are smooth. Hence every generator, their finite sum, and all indicated derivatives defining F are smooth near zero.

Each generator is even in x and y. Therefore rho and F are even in x and odd in y, so F(0)=0. Bounded first derivatives on a small closed disk imply |F(X)|<=C|X|. Angular projection gives |f_n(r)|<=pi^(-1) integral_0^(2pi)|F(r,theta)|dtheta<=2Cr. Thus F_n is locally integrable at zero. This verifies the premise used when div A_Fn=F_n is passed from annuli to distributions on the whole plane. The argument also supplies that premise for F_n+Delta psi, since Delta psi is smooth.

The checker independently reads every exact raw generator, verifies its type, complete parameter arity, nonnegative integer indices, positive exact radius and rational coefficient. It compares counts and radii with N4-432, rehashes every declared producer source, and uses the already accepted generator-to-field convention. This is a finite structural inspection, not a reconstruction of the large residual polynomials or a new bound on F outside the origin.

## Dependencies and verdict

T4-495 provides the actual candidate construction and partial mode data; T4-501 provides the complete analytic argument and independent exact fixtures. Frozen T2 revision1, its erratum source/log/results, and N4-432 proof/source/results are copied as inert evidence. Every source is SHA256 bound; own accepted raw017 is reused. The proof is written before this checker. CONFIRMED applies to the corrected review, origin condition and listed finite checks. Full017 H upper, E2 and E2(017)<E2(007) remain OPEN. The existing T1/T2 peers are configured as us.anthropic.claude-opus-5-5; provider response identity is not independently observable.

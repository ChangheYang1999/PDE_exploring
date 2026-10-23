# What finite Gauss-Newton line-search failure does not prove

Result310. Written UTC: 2026-10-22T01:58:28.230424+00:00. Scope: a logical audit of the inference in numerics note163(a), not a recomputation of its Jacobian or singular-value data.

For a differentiable residual map F:R^n -> R^m and objective E(u)=||F(u)||^2/2, first-order stationarity means J(u)^T F(u)=0. If P is the orthogonal projector onto the exact range of J, this is equivalent to P F=0. Indeed ker(J^T)=(range J)^perp, by the definition of transpose and the Euclidean inner product. A small nonzero projected fraction ||PF||/||F|| indicates approximate stationarity in the residual-space metric; it does not imply exact first-order stationarity. With truncated singular values, the same statement applies to the retained subspace only and does not enclose omitted directions or differentiation error.

Failure of finitely many positive trial step lengths along a Gauss-Newton direction also does not prove stationarity. The following exact smooth counterexample even matches the reported order of the projected fraction. Let epsilon=77/10000, M=8192, and F(u)=(epsilon+u,1+M u^2) for real u. At u=0, F=(epsilon,1), J=(1,0)^T, J^T F=epsilon!=0, and ||PF||/||F||=epsilon/sqrt(1+epsilon^2), approximately0.77percent. The Gauss-Newton direction is d=-epsilon. For lambda>0,

||F(lambda d)||^2-||F(0)||^2
=epsilon^2 lambda[-2+(1+2M)lambda]+M^2 epsilon^4 lambda^4.

For every lambda=2^(-k), k=0,...,12, lambda>=1/4096 and (1+2M)lambda>=16385/4096>2. Both terms are then nonnegative and the first is strictly positive, so every listed step increases the objective. Nevertheless the directional derivative at lambda=0 is -2epsilon^2<0. For sufficiently small positive lambda the objective decreases; the checker also verifies one explicit smaller dyadic step exactly. All functions are polynomial and there are no regularity or numerical issues.

Consequently these two observations, a projected fraction near0.77percent and rejection of lambda=1,...,2^-12, do not establish the literal statement that the state is a first-order stationary point. Nor do they establish that an acceptance rule, smaller step schedule, inaccurate Jacobian or other search direction cannot affect a stall. The finite observations may be reported as small projected residual and failure of the tested truncated Gauss-Newton steps. Their interpretation as near stationarity must specify norms, scaling, truncation and numerical precision. The unexamined actual solver may have additional evidence, but that evidence is not supplied by this implication.

Verdict on the general inference: REFUTED by this exact counterexample, once the arithmetic check and independent review close. Verdict on the actual state's exact gradient/stationarity: OPEN; no Jacobian or original execution is authenticated here. This concerns an auxiliary hydrostatic trial and cannot decide the primary full-plane IPM problem.

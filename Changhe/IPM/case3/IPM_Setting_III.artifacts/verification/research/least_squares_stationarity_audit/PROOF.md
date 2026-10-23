# What a Gauss--Newton projection and segment barrier establish

Written 2026-10-21 UTC, before the supporting exact checker.

## Statement, notation, and scope

Let F:R^d -> R^m be C2, J=DF, Q=||F||_2^2, and P the orthogonal projector onto a selected left-singular subspace of J. Neither a small ||PF||^2/||F||^2 nor an unchanged full truncated Gauss--Newton step proves stationarity or local minimality of Q. Even exact stationarity, a zero full untruncated Gauss--Newton step, and arbitrarily high objective barriers on the straight segments between observed points do not imply that the points are local minima or that no curved flat valley connects them. The following polynomial examples prove each failure. They refute the inference used in NUM_REPORT 4L(c14), not the assertion that any particular IPM endpoint actually is a minimum. That classification remains open without further evidence.

Dependencies: differentiation of finite polynomials and orthogonal projection in Euclidean space. No IPM assumption is used or asserted for these examples.

## First-order distinction

For the full objective, grad Q=2 J^T F and Hess Q=2 J^T J+2 sum_i F_i Hess F_i. Thus J^T F=0 is a first-order condition, while the residual Hessian term is absent from the Gauss--Newton matrix and can have either sign.

For 0<epsilon<1, let F(x,y)=(x,1+epsilon y). At (0,0), J=diag(1,epsilon). Retaining only the first singular direction gives PF=0 and a zero truncated step, whereas grad Q=(0,2epsilon) is nonzero. In fact Q(0,-t)=(1-epsilon t)^2<1 for 0<t<2/epsilon. A truncated projection can miss descent entirely.

For a truncated singular-value inverse, d=-J_tau^+ F satisfies Jd=-PF in exact arithmetic. Thus DQ[d]=-2||PF||^2. A nonzero accurately computed projection identifies a strict descent direction, even when its relative decrease is too small for a chosen stopping rule.

The reported projection fractions 5.5e-6, 1.1e-6, 1.2e-5 are squared relative norms. Their square roots are about 0.00235, 0.00105, 0.00346. They are not orthogonality to 1e-6 in relative norm, and none equals zero. The projected gradient also weights these components by the singular values, so the projection alone does not report a gradient tolerance.

## Exact stationary saddles with segment barriers

Fix any K>0, set p(x)=x(x^2-1), and F(x,y)=(K p(x),1-y^2). At x in {-1,0,1}, y=0, the residual is (0,1), J has only the nonzero entry J_11=K p'(x), and p'(x) is 2,-1,2 respectively. The full, untruncated PF vanishes exactly and the minimum-norm Gauss--Newton step is zero. The objective Hessian has diagonal entries 2K^2 p'(x)^2 and -4 and zero off-diagonal entries. Every point is a saddle. Directly, Q(x,t)=(1-t^2)^2<1 for 0<|t|<sqrt(2), but Q(x+s,0)>1 for sufficiently small nonzero s.

Between any two of the three points, the straight segment has y=0 and contains points with p(x)!=0. At x=1/2 or -1/2, Q=1+9K^2/64. Its residual norm is sqrt(1+9K^2/64), arbitrarily large compared with the endpoint norm 1. Segment barriers do not cure the failure of the second-order condition.

The same phenomenon occurs with a quadratic residual map, as in the fixed-c_l IPM discretization: take F(x,y,z)=(K x(x-1),K y(y-1),1-z^2). At the three points (0,0,0),(1,0,0),(0,1,0), the residual is (0,0,1), J=diag(K(2x-1),K(2y-1),0), PF=0, and the Gauss--Newton step is zero. The objective Hessian is diag(2K^2,2K^2,-4), so all three are saddles. The midpoint squared norms on their three connecting segments are 1+K^2/16, 1+K^2/16, 1+K^2/8. All barriers are arbitrarily large with K.

## A connected flat valley with segment barriers

Let G(x,y)=(K(y-x^2),1). Every point on the parabola y=x^2 has Q=1, the global minimum, and these points form a connected flat valley. At each such point the residual is (0,1), the Jacobian has a zero second row, PF=0, and the full minimum-norm Gauss--Newton step is zero.

For two different points (a,a^2),(b,b^2), the chord at parameter t has x=(1-t)a+tb and y=(1-t)a^2+tb^2. Hence y-x^2=t(1-t)(a-b)^2 and Q=1+K^2 t^2(1-t)^2(a-b)^4. Every interior point of the chord has higher objective, and the barrier grows without bound with K. The endpoints are nevertheless connected by the constant-objective parabola. A straight-segment test cannot rule out a curved valley.

## Required correction and useful further checks

The saved experiments establish distinct attained states, small resolved Gauss--Newton projections, and barriers on the tested straight segments. They do not establish exact stationarity, distinct local minima, absence of a connected low-residual valley, or completion of optimization. Comparing scale-invariant observables can separately rule out pure spatial scaling as an explanation for their differences.

A common tighter optimization criterion, the full gradient with stated scaling and truncation, and second-order curvature checks on the relevant coefficient subspace would distinguish these possibilities more effectively. An observed positive Hessian on a tested subspace would still need an explicit scope and control of omitted directions. No new solver success or failure is claimed here.

# What a small spline repair does and does not imply for image rows

## Statement, notation and scope

This audit concerns two inferences in the captured NUM_REPORT section7.4b(v), not its computed singular values. Topic135 bounds first log-radial derivative jumps of precisely the topic132 C0-repaired individual radial columns. It does not bound the actual unmodified columns, retained combinations or a difference between two operator matrices. Topic136 bounds individual broken X norm errors for an exact C2,1 repair. It does not prove that the repaired operator spectrum agrees to printed digits with the stored one. Both inferences need further estimates.

Here X is the weighted weak H1 space with norm squared integral(h^2+r^2|grad h|^2)w(r)dX, with w positive and bounded above and below on each compact annulus. Let B_m(t) be C0 and piecewise C2, t=log r, and h=r^3 sum B_m(t)Phi_m(theta), Phi_m=cos^2(theta)sin(theta)cos(2m theta). Assume the background hypotheses of topic135: rho locally W2,infinity, canonical U[rho] locally W1,infinity and divergence free, and c_l!=0. Put V=c_l X+U[rho]. The full linearized operator is

    Lh=V.grad h-h+U[h].grad rho+(Sigma(h)/3)X.grad rho.

For one circular interface R, let d_m=[B_m'] and [f] be the outer minus inner trace. Then the jump of the image, understood as the jump of its piecewise transport part plus an H1 lower-order term, is

    J(theta)=[Lh]=V_r(R,theta) R^2 sum d_m Phi_m(theta).       (1)

For a sine coefficient J_N=(1/pi)int J(theta)sin((2N+1)theta)dtheta, a pair of log-radius nodes separated by Delta crossing exactly this jump has a jump contribution

    wbar J_N/Delta            for ROWS=H1,
    wbar J_N/sqrt(Delta)      for ROWS=H1q,                 (2)

where wbar=(w_row(t_i)+w_row(t_(i+1)))/2 and

    w_row(t)=sqrt(1+u)/[u^3(1+u^2)^((k-3)/2)], u=exp(t)/L.

The word contribution refers to the exact algebraic decomposition f_N=g_N+J_N1_(t>log R), with g_N continuous across that interface; it is not a bound for the whole row, since the smooth term can cancel it. Formula(2) assumes neither numerical nodes nor an actual singular vector. It identifies the factors a numerical bound must account for.

## Proof of the image and row identities

At a C0 interface, tangential derivatives agree and the physical normal derivative jump is R^2 sum d_m Phi_m. The lower-order terms in Lh belong to local H1 by the order-zero Fourier multiplier bound for U and the product rule with the stated background coefficients. Their weak derivatives have no circle measure. Thus the coefficient of the circle measure in the gradient of Lh is the right side of(1), as in topic135. If classical traces are available this is their difference. The sine coefficient is defined by its explicit finite angular integral and is not presumed equal to d_m.

For a node pair crossing the jump, subtract J_N from the outer branch. The finite difference splits exactly into (g_N(t_(i+1))-g_N(t_i))/Delta+J_N/Delta. The captured weighted_rows source multiplies this difference by wbar for H1 and by wbar sqrt(Delta) for H1q. This proves(2). Exact C1 joins suffice for local H1 membership under these hypotheses; the C2,1 repair is one sufficient stronger construction. Numerically enforcing exterior joins supplies no automatic exact internal join or global image theorem.

## An explicit amplification fixture

This is an independent model example, not the actual IPM trial, its grid, or its retained vectors. Take rho=0 and c_l=1/3, so U[rho]=0, Sigma(rho)=0 and the normalization-dependent speed is consistent with rho. Kinematic center normalization is not imposed on this model background. Let L and k have the positive exact values recorded in the fixture JSON; these are weight parameters only, with no relation c_l=1/k required for this local example. Choose R=100, d=10^-14 and Delta=1/50, with nodes log R plus or minus Delta/2. On the two sides of log R take B=0 and B=d(t-log R), then multiply by a smooth cutoff equal to1 near the two nodes. This defines a continuous compactly supported annular h=r^3 B Phi_0. Its sole nearby derivative jump is d. Other cutoff joins can be chosen smooth.

Since Phi_0=(sin theta+sin3theta)/4, both nonzero image jump sine coefficients are

    J_0=J_1=R^3 d/12.

Consequently the positive jump contributions in(2) are computed from this coefficient and the two exact node weights. They need not be below10^-11 merely because d<2.5e-14. Two interval engines will verify a strict lower bound. This refutes that inference from a scalar derivative jump alone, while leaving the actual finite rows and their total differences OPEN.

## Small X repair errors do not control collocation rows by themselves

There is no continuous extension of even the simple transport value row h -> (c_l E h-h)_N(t_*) to X on a compact annulus when c_l!=0. Fix R=exp(t_*) and let phi(z)=z(1-z^2)^3 on |z|<=1 and0 outside. It is C2, phi(0)=0, phi'(0)=1. Set

    e_epsilon=r^3 epsilon phi((log r-t_*)/epsilon)Phi_0(theta).

For epsilon small its support is an annulus of thickness O(epsilon). The function is O(epsilon), its first spatial derivatives are O(1), and its X norm squared is O(epsilon), because the weight and the polar Jacobian are bounded on this fixed annulus. Thus its X norm tends to0. At t=t_*, however, e_epsilon=0 and E e_epsilon=R^3 Phi_0. Both sine rows of (c_l E-1)e_epsilon equal c_l R^3/4, independently of epsilon. This remains an example of the full IPM linearization at rho=0, c_l=1/3. Its possibly nonzero Sigma(e_epsilon) multiplies E rho=0.

Thus a small single-column X norm perturbation alone supplies no modulus controlling even a value row. The very particular finite repair family may admit such control, but it must be proved using its explicit derivatives and the background, not inferred from the X norm ratio. This example is independent of jumps; all e_epsilon are C2 compact annular functions.

## A sufficient finite-section transfer bound

Let a finite real coefficient section have an original positive definite Gram G and an exact whitening Q, Q^T G Q=I. Let A and Ahat be the original and repaired row matrices of the same size, and let Ghat be the repaired Gram. Assume for some0<=epsilon<1 and a known eta>=0 that

    (1-epsilon)^2 I <= Q^T Ghat Q <= (1+epsilon)^2 I,
    ||(Ahat-A)Q||_2 <= eta.

Write sigma=inf_(||z||=1)||A Q z|| and sigmahat=inf_(z!=0)||Ahat Q z||/sqrt(z^T Q^T Ghat Q z). Then

    max(0,sigma-eta)/(1+epsilon) <= sigmahat
        <= (sigma+eta)/(1-epsilon).                       (3)

For every z the triangle inequality bounds the numerator below by (sigma-eta)||z||, and the repaired denominator above by (1+epsilon)||z||. If sigma-eta<0 use nonnegativity. For the upper bound choose a unit minimizer for the original finite matrix; its repaired numerator is at most sigma+eta and its denominator at least1-epsilon. This proves(3), also for rectangular row matrices. It concerns the chosen section range(Q) only. A changed selection or extra repaired vectors are not silently included.

Topic133 supplies a conditional route to the Gram hypothesis for a selected repaired subset. It does not supply eta or a conditioning bound for the actual retained Q. Per-column errors accumulate through coefficient synthesis; for columnwise row errors with norms at most eta_j, ||Ahat-A||<=sqrt(sum eta_j^2), and multiplication by Q costs at most ||Q||. These are sufficient estimates, not claims that these coarse bounds are necessary or sharp. Row discretization, floating rounding and continuum surjectivity require further arguments.

## Evidence and verdict plan

Capture the current source and report bytes without executing the numerical job. Check the AST formulas for weighted_rows and the exterior-only constraint locations independently of the report wording. Reconstruct the trigonometric and secant identities by direct polynomial/trigonometric algebra and a second rational Fourier method. Evaluate the explicit fixture with Arb and mpmath.iv, keeping exact rational endpoints. Verify the compact test polynomial's endpoint and central jets by Horner derivatives and independent monomial sums. Seek actual Opus5.5 review before finalization.

The final verdict may confirm these identities and refute the asserted logical implication. The actual10^-11 row bound, preservation of printed singular values, exact retained-vector conformity, global inverse and every IPM endpoint remain OPEN.

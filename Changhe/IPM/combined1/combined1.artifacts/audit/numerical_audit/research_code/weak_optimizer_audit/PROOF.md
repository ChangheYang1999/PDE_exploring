# Fixed-mesh weak-pairing rows and their Gauss-Newton derivatives

## Scope and finite objective

Fix c, a finite generator list, a fixed affine tail, a finite product mesh and its weights. For coefficient vector a, every density, stream and transport field at the mesh nodes is affine in a. Let the density residual be F=T-psi_y rho_x+psi_x rho_y. Its Cartesian derivative components are obtained by the finite Leibniz rule. Each component is therefore a polynomial of degree at most two in a.

For k>=0 the prescribed continuum test is phi_k=y t^k u^2, t=r^2/(1+r^2), u=1/(1+r^2). F and phi_k have S1 parity, so their product is even in both coordinates. For mesh weights W approximating ds dtheta on the first quadrant, with s=log r, define the discrete pairing

    I_k(a)=sum_nodes [4 W r^2 phi_k] F(a).

The factor r^2 is exactly the Jacobian r dr=r^2 ds. The factor4 follows from parity. A radial mask simply defines a restricted finite-mesh objective. Neither factor supplies a quadrature or omitted-domain error bound.

The new objective adds sum_k w_k I_k(a)^2, with fixed w_k>=0, to the previous least-squares objective. Its Gauss-Newton residual rows are sqrt(w_k) I_k. This note audits the implementation of that finite objective. It does not assert that a finite-mesh objective is a rigorous whole-plane norm or that reducing it must reduce every necessary correction bound.

## Exact derivatives

For any field label q, write A_q(a)=A_q,0+sum_j a_j A_q,j. A summand in a residual component is a fixed scalar times A_p(a) A_q(a). Its derivative with respect to a_j is

    A_p,j A_q(a)+A_p(a) A_q,j.

Consequently the residual Jacobian is the transport generator field plus these two product terms for every signed Leibniz contribution. The fixed affine tail enters A_p(a),A_q(a), but has zero coefficient derivative. At fixed mesh and fixed test function,

    J_(k,j)=d I_k/da_j=sum_nodes [4 W r^2 phi_k] dF/da_j.

With G=J_total^T J_total and g=J_total^T residual_total, the additional contributions are

    G_pair=sum_k w_k J_k^T J_k,
    g_pair=sum_k w_k I_k J_k,
    Phi_pair=sum_k w_k I_k^2.

The actual objective gradient is2g; the normal-equation convention uses g. Summing node chunks before forming J_k^T J_k is necessary. Forming a separate square per chunk would be a different objective. The frozen Problem3 code accumulates the complete J_k over chunks and forms the outer products afterwards.

For a quadratic I, centered differences with any exact nonzero step are exact directional derivatives: [I(a+epsilon v)-I(a-epsilon v)]/(2epsilon)=DI(a)v. This follows by cancelling the even powers in its degree-two expansion. In floating arithmetic there is still evaluation and subtractive cancellation error. A finite-difference discrepancy alone must not be identified with a Jacobian formula error.

## Independent finite fixtures

The checker copies the frozen library and dependencies into this topic before importing them. No foreign directory is executed and no candidate optimizer is launched. It constructs small affine field arrays with integer entries, arbitrary nonzero affine tails and the same finite derivative-index contract. Their residual values and Jacobians are computed independently using NumPy integer arithmetic and exact centered differences with unit coordinate steps. This is valid because every residual component is quadratic.

The checker forms reference objective, gradient and Gauss-Newton matrix directly over all mesh points, including pair terms. It compares them with the copied chunked implementation for several generator-block and radial-chunk sizes, with and without pair rows. Bounds on fixture magnitudes ensure the binary64 operations used in this comparison represent the integer operations exactly. Successful fixtures confirm this finite algebra and chunk assembly. They do not test conditioning of the2982-parameter candidate problem or certify its floating solution.

## Angular resolution and interpretation

At the N-point quarter-circle midpoint nodes theta_j=(j+1/2)pi/(2N),

    sin((4N-1)theta_j)=sin(theta_j),
    sin((4N+1)theta_j)=-sin(theta_j).

These identities follow by substituting4N theta_j=(2j+1)pi. Thus the first-sine pairing aliases frequencies4N-1 and4N+1. For a residual whose largest positive odd mode is319, N>=81 avoids this first-mode alias, whereas N=60 aliases239 and241. This requirement only concerns the first-mode pairing. Quadratic full derivative norms have their own stronger bandwidth condition, already audited in ../angular_resolution and ../angular_contract_audit.

A coarse angular rule is still legitimate for a discrete Jacobian fixture, provided no continuum accuracy claim is attached. Candidate optimization uses N=180 in the frozen launch plan, which passes this first-mode condition. Its reduced radial rule requires a separate matched accuracy check. A difference in pairing values between meshes can contain both angular and radial error; the identities above do not quantify their separate contributions.

Finally, raw I_k rows have different scales. The necessary correction test uses I_k divided by a candidate-dependent denominator, followed by its quadratic root. Uniform weights on raw pairings are a specified optimization choice, not minimization of that necessary distance. Every new candidate still needs independently evaluated complete tests, point exclusions and exact far-field constraints.

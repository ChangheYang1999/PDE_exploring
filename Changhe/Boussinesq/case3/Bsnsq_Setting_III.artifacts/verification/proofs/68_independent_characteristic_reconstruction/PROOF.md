# Independent characteristic reconstruction and its cutoff limit

Date:2026-10-20. Status: CONFIRMED conditional transport identities and cutoff-limit proof by independent reasoning; manufactured implementation checks passed. No profile or endpoint is asserted.

## 1. Statement and hypotheses

Let beta>2, lambda=(beta-2)/2, mu=(3beta+2)/2, and rho=beta-2=2lambda. Suppose a smooth B2 profile has W=beta X+V with W(0)=0, DW(0)=diag(lambda,mu), the prompt parity, and Theta=a0 x^2+O(|X|^3). Let B0 denote the backward basin of the origin. The vorticity equation gives b0=Omega_x(0)=4a0/beta. This proof uses only the transport equations and these local jets, except in Section4, which specifies the independently inverted velocity.

For a fixed nonzero Y in B0, let Z(t)=phi_{-t}(Y). For sufficiently small delta>0, let T_delta be the time when this backward orbit first reaches |Z|=delta after entering a fixed small backward-invariant disk. Put X_delta=Z(T_delta). On the stored reversed path P(s)=Z(T_delta-s), 0<=s<=T_delta, solve

    g'(s)=[rho I-DW(P(s))^T]g(s),
    o'(s)=g_1(s)-o(s),
    g(0)=(2a0 (X_delta)_1,0),
    o(0)=b0 (X_delta)_1.

Then

    Theta_delta(Y)=exp(rho T_delta)a0 (X_delta)_1^2 -> Theta(Y),
    g(T_delta)->grad Theta(Y),   o(T_delta)->Omega(Y).

The convergence is locally uniform in Y in B0 away from0. If the exact endpoint data Theta(X_delta), grad Theta(X_delta), Omega(X_delta) replace the leading jets, these formulas are exact at every cutoff.

These are conditional consistency statements for a true profile. A velocity with a slightly incorrect center strain does not meet the exact hypotheses. For it, values at several finite cutoffs are useful diagnostics, but a limit with the prescribed a0 is not inferred.

## 2. Exact transport formulas

Along the forward path P, scalar transport gives d_s Theta(P)=rho Theta(P). Differentiating W.grad Theta=rho Theta gives

    W.grad(grad Theta)=[rho I-DW^T]grad Theta.

The vorticity equation gives d_s Omega(P)=Theta_x(P)-Omega(P). Uniqueness of these finite-time scalar and linear systems proves the exact endpoint-data statement. This computation checks the transpose and signs independently of any fitting implementation. It avoids inverting a fundamental matrix with exponentially separated source eigenvalues.

## 3. Vanishing error from the leading center jets

Choose epsilon>0 so small that

    2-(lambda+epsilon)/(lambda-epsilon)>0,
    3-2lambda/(lambda-epsilon)>0.

For example epsilon<lambda/4 suffices. In a sufficiently small fixed disk, the smallest eigenvalue of the symmetric part of DW is at least lambda-epsilon. Thus along a backward orbit its radius decreases at least at logarithmic rate lambda-epsilon, and the time between radii r0 and delta is at most log(r0/delta)/(lambda-epsilon). Also the largest eigenvalue of the symmetric part of rho I-DW^T is at most lambda+epsilon there. Forward propagation of a gradient error therefore multiplies its norm by at most exp((lambda+epsilon)s) until exiting this disk. The remaining finite-time propagation to Y has a bounded multiplier, uniformly on each compact subset of B0: sufficiently late backward entry into the disk is uniform by continuous dependence and compactness.

Taylor's theorem gives center seed errors O(delta^3) in Theta and O(delta^2) in its gradient and Omega. Consequently the propagated temperature error is bounded by

    C delta^[3-2lambda/(lambda-epsilon)] ->0,

and the propagated gradient error is bounded by

    C delta^[2-(lambda+epsilon)/(lambda-epsilon)] ->0.

For vorticity, variation of constants gives the decaying initial O(delta^2) error plus the integral of the gradient error against exp(-(s-u)). Before the small-disk exit this integral is at most C delta^2 exp((lambda+epsilon)s)/(1+lambda+epsilon); after exit it remains controlled by the same vanishing bound times a fixed constant. This proves the claimed convergence. The source-basin and jet inputs were independently established in packets04 and48; the error proof here is independent.

## 3a. Exact finite-cutoff boundary gradient

There is also an exact finite-cutoff construction that does not require exact center strain. Let W be C1, let the circle Sigma={|X|=delta} satisfy W.n>0, and consider points whose backward orbit hits Sigma transversely once. Prescribe a C1 boundary value f and any boundary vorticity o0. Set

    Theta_delta(Y)=exp(rho T(Y)) f(X_delta(Y)).

Here a C1 extension of f near Sigma can be chosen arbitrarily. The hitting time and point are C1 by the implicit function theorem. Along the forward flow the hitting time increases by s while the hitting point is unchanged; therefore W.grad Theta_delta=rho Theta_delta. Its gradient on Sigma must have the same tangential derivative as f and must satisfy W.g=rho f. These conditions uniquely give

    g_seed = grad f + n [rho f-W.grad f]/(W.n).

The expression is independent of the chosen extension, because an extension change has zero tangential derivative and its normal derivative cancels in the correction. Solve the gradient ODE of Section2 with this g_seed, and solve o'=g_1-o with the prescribed o0. Differentiation of the exact transported scalar and uniqueness of the gradient ODE prove that g is its actual spatial gradient. The vorticity scalar obtained this way satisfies W.grad o+o=(Theta_delta)_x exactly on this flow tube. No curl relation is asserted. A differentiable flow and transverse circle suffice; the cutoff need not tend to zero.

For a true source profile and f=a0 x^2, the correction is O(delta^2): W=diag(lambda,mu)X+O(delta^2), rho=2lambda, and rho f-W.grad f=O(delta^3), while W.n>=lambda delta/2. Thus the earlier cutoff-limit proof also applies to the corrected construction. With an imperfect center strain this conclusion is not inferred, although the finite-cutoff transport identities remain exact. The implementation records the correction and distinguishes this boundary-compatible mode from the leading-gradient seed used in the first saved-state diagnostic.

## 4. Independent smooth interpolation of the full-plane inverse

Use phi with X=(r sin phi,-r cos phi). Let Omega=sum H_n(r)sin(n phi), and let p_n be the canonical relative stream coefficients. The inverse from packet63 supplies

    f_n(r)=p_n(r)/r,    d_n(r)=p_n'(r),
    p_n''=-d_n/r+n^2 f_n/r-H_n.

At s=log r, f_{n,s}=d_n-f_n and

    f_{n,ss}=(n^2-1)f_n-2 f_{n,s}-r H_n.

A piecewise quintic Hermite polynomial in s matching f,f_s,f_ss at every node is C2 in s. Its stream p=r f is C2, its velocity is C1, and its velocity derivative is continuous across all radial knots. Values and first and second derivatives are evaluated from this one polynomial, so the derivative matrix is the actual derivative of the interpolated velocity. This differs from differentiating independent velocity tables.

For the polar basis e_r=(sin phi,-cos phi), e_phi=(cos phi,sin phi), set

    Psi_r=sum (f+f_s) sin(n phi),
    Psi_phi/r=sum n f cos(n phi),
    H_rr=sum (f_s+f_ss)/r sin(n phi),
    H_rphi=sum n f_s/r cos(n phi),
    H_phiphi=sum ((1-n^2)f+f_s)/r sin(n phi).

These are respectively the radial gradient and Cartesian Hessian expressed in the orthonormal polar frame. Rotation to Cartesian coordinates, followed by J(a,b)=(-b,a), gives V=J grad Psi and DV=J Hess Psi. In particular div V=0 identically inside every cell and by continuity at its boundary. The interpolated curl need not equal the original source exactly between nodes; that discrepancy and the interpolation error must be measured separately against the original whole-plane inverse. No finite-radius boundary is imposed: every node value includes the entire plane. This is an approximation of the fixed inverse, not a new admissibility convention.

## 5. Verification and scope

Before applying the reconstruction, use (i) analytic stream functions for interpolation and Cartesian derivative checks, (ii) an explicit source flow with a known transported temperature and a separately integrated vorticity resolvent, and (iii) multiple interpolation resolutions, integration tolerances and center cutoffs. Error stability is not an interval certificate. The numerical reconstruction can explain residuals of a stored field but does not solve the coupled B2 equations, certify a global basin, or decide existence.

## 6. Separating stored-field and transported-gradient defects

Retain the transverse finite-cutoff setting of Section3a. Denote the exact transported fields by Theta_C, g_C=grad Theta_C and Omega_C. Let Theta_S,Omega_S be arbitrary C1 stored fields in the same flow tube, with the same W. Use the same vorticity seed o0 as for Omega_C, but define

    Omega_Ssrc(Y)=exp(-T)o0(Z(T))
                     +integral_0^T exp(-t) (Theta_S)_x(Z(t)) dt,

where Z(t)=phi_{-t}(Y). This scalar solves W.grad Omega_Ssrc+Omega_Ssrc=(Theta_S)_x with the prescribed boundary data. It generally differs from Omega_C, whose source is (Theta_C)_x. Their exact difference is

    Omega_Ssrc(Y)-Omega_C(Y)
       =integral_0^T exp(-t)[(Theta_S)_x-g_C,x](Z(t))dt.       (D1)

Here g_C,x denotes the first component, not another spatial derivative. The common seed cancels. Let

    Rv_S=W.grad Omega_S+Omega_S-(Theta_S)_x,
    Rt_S=W.grad Theta_S-rho Theta_S.

Differentiating exp(-t)Omega_S(Z(t)) and exp(rho t)Theta_S(Z(t)), respectively, and integrating gives

    Omega_S(Y)-Omega_Ssrc(Y)
       =exp(-T)[Omega_S(Z(T))-o0(Z(T))]
                   +integral_0^T exp(-t)Rv_S(Z(t))dt,       (D2)

    Theta_S(Y)-Theta_C(Y)
       =exp(rho T)[Theta_S(Z(T))-f(Z(T))]
                   +integral_0^T exp(rho t)Rt_S(Z(t))dt.    (D3)

Thus the total vorticity mismatch splits exactly into a source-gradient contribution D1 and a stored-vorticity transport contribution D2. The identities involve only finite-time integrals, so C1 regularity and a finite transverse hitting time suffice. With C1 W, the transported fields in Section3a are C1 on the flow tube. No smallness, inverse fixed point, or vanishing-cutoff limit is assumed.

In computation one can evaluate D2 and D3 with Cartesian differences and quadrature on the independently computed backward orbit. Agreement with direct field differences tests this error decomposition; it does not prove a PDE solution. Cancellation must be disclosed by recording both signed integrals and integrals of the absolute integrands. A small characteristic fit residual alone controls neither term in this decomposition without a separate error analysis.

# Negative scalar completion is impossible for every monotone flat Volterra factor

Status: CONFIRMED at the exact local scope in Sections 1-5, audit A2643-A2645. The broader extensions in A2646 remain OPEN. The existing coordinator comparison was read in full; its eleven items agree. No assertion about unrestricted rotating profiles is made.

## 1. Statement and notation

Fix 0<c<1/2 and any finite real omega. Write Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b0=2(1-c), eta=a/b0 and kappa=1-2eta=c/(1-c)>0. Let sigma be a smooth two-dimensional section through x0=sigma(0), transverse to X, with X(x0) nonzero. All assertions are local after shrinking its disc and a finite flowbox Phi(y,s)=exp(sA)sigma(y).

Set

    j=|det(sigma_1,sigma_2,X(sigma))|,
    beta_i=X(sigma).sigma_i/|X(sigma)|^2, b=(3c-1)beta,
    gQ_ij=sigma_i.sigma_j-|X(sigma)|^2 beta_i beta_j.

The matrix gQ is smooth positive definite and j is smooth positive. Let f:(0,R)->(0,infinity) be smooth and nondecreasing, with f^(k)(r)=O(r^N) for every pair of nonnegative integers k,N. No bound on r f'/f and no lower bound r f'>=f is required. Define

    q(r,theta)=r^-1 integral_0^r t b_theta(t,theta) f(t)
                         exp(integral_t^r b_r(u,theta)du)dt,
    w=f e_theta+q e_r, v=w/j, h=-beta.v,
    V(Phi(y,s))=exp(-s)D Phi(y,s)(v(y),h(y)).                 (1)

Here y=r e_r and e_theta is the positively oriented unit angular vector. This carrier is smooth, flat on its central orbit Gamma, nonzero off Gamma, and obeys

    div V=0, X.V=0, DV X=-LV.                              (2)

There is no smooth scalar S on any neighborhood of x0 satisfying

    X.grad S=-b0 S, W.grad S=0, W=curl V,
    S=0 on Gamma, S<0 off Gamma,
    -Delta(S+|V|^2/2)=tr((DV)^2).                           (3)

The sign and zero set in (3) concern that neighborhood. Flatness of S is not assumed. The conclusion concerns precisely the carrier (1), every finite omega, and this scalar sign and zero set. It does not exclude other completions, supply a pressure, or settle the global conjecture.

## 2. Carrier identities and normalized section form

The construction estimates can be checked without differentiating f. Smoothness of the fixed coefficients, f(t)<=f(r) for t<=r, and boundedness of the exponential kernel give

    |q|+|q_theta|<=C r f,
    q_r=b_r q+b_theta f-q/r,
    |D_y(q e_r)|<=C f.                                    (4)

Angular derivatives act only on bounded smooth coefficients and their integral kernels. Repeated radial differentiation of the second identity in (4) introduces derivatives of f and fixed powers of r^-1. Thus every fixed mixed derivative is flat. Cartesian derivatives are finite combinations of these derivatives and powers of r^-1, so (1) extends smoothly and flatly across the center. Positivity of the angular component f makes w nonzero elsewhere.

The flowbox volume density is exp(3cs)j. The formula for q gives div w=b.w. Together with h=-beta.v this proves div V=0. The coordinate form of (1) gives [X,V]=-V, hence DV X=(A-I)V=-LV. On the section X.V=0; the dilation and rotation in exp(sA) propagate it throughout the flowbox. These prove (2) and its stated zero set.

Pulling back the Euclidean one-form V.dx to the section gives

    sigma^*(V.dx)=gQ v=f zeta,
    zeta=M(y)[e_theta+(q/f)e_r], M=gQ/j.                   (5)

The fixed matrix M is smooth positive definite. Shrinking R, (4) implies constants d,c1,c2>0 with

    zeta.e_theta>=d, |zeta|<=C,
    c1 f<=|V(sigma(y))|<=c2 f.                            (6)

The normalized derivative may be large. Direct differentiation, retaining the f' term, gives

    |D zeta|<=C[1/r+1+r f'(r)/f(r)].                       (7)

Indeed |D e_theta|<=1/r, |D(q e_r)|/f<=C, and the derivative of 1/f contributes at most |q| f'/f^2<=C r f'/f. There is no logarithmic upper bound on this last term in the present hypotheses.

## 3. The accumulated derivative cost is negligible compared with log(1/f)

Let Y=(zeta2,-zeta1). Then Y_r=Y.e_r=zeta.e_theta>=d. Since |div Y|<=sqrt(2)|D zeta|, a nonnegative radial majorant for (-div Y)_+/Y_r is

    p(r)=C[1/r+1+r f'(r)/f(r)],
    Q(r)=integral_r^R p(s)ds.                             (8)

It is integrable on every compact subinterval of (0,R]. Shrink R so f<1, and put Hf(r)=log(1/f(r)). Value flatness gives

    Hf(r)/log(1/r) -> +infinity.                           (9)

For a fixed 0<delta<R and 0<r<delta, monotonicity gives

    0<=integral_r^delta s f'(s)/f(s) ds
        <=delta[log f(delta)-log f(r)]
        =delta[Hf(r)-Hf(delta)].                          (10)

The integral from delta to R is a fixed finite number. Dividing (10) and (8) by Hf(r), using (9), and then letting delta decrease to zero proves

    Q(r)/Hf(r) -> 0,
    kappa Hf(r)-Q(r) -> +infinity.                        (11)

This is the one-sided rate of A2611-A2612. It is stronger than needed and does not require r f'/f=O(log(1/r)). The same calculation works for every smaller outer radius, a point needed for the germ conclusion.

## 4. The scalar equations would make S negligible compared with the energy

For completeness, suppose (3) held, set H=-S>0 off Gamma, E=|V|^2, and restrict to a closed section disc inside its domain. Differentiating X.V=0 and using (2) gives

    X cross W=(DV)^T X-DV X=(L-A^T)V=aV.

The scalar identities give a grad H cross V=b0 H W, so curl(H^(-eta)V)=0. Its pullback to the section is closed. Thus with F=f(H composed sigma)^(-eta)>0,

    div(FY)=0.                                           (12)

Each forward Y-trajectory from a punctured-disc point reaches the outer circle in finite time: its radial speed is at least d, and the field is smooth and bounded on each intervening compact annulus. Parameterizing that trajectory by increasing radius and integrating (12) yields

    log F(y)=log F(y_R)+integral_r^R (div Y)/Y_r ds
             >=log m-Q(r),                              (13)

where m is the positive minimum of F on the outer circle. There is no requirement that the angular trajectory have a limit at the center. Solving (13) for H and using (6),

    H(sigma(y))/E(sigma(y))
      <=C exp(-[kappa Hf(r)-Q(r)]/eta) -> 0.               (14)

The convergence is uniform in angle. Both H and E have X-derivative -b0 times themselves; for E this follows from (2) and the skew part of L. Hence H/E is constant along the X-orbits. The smooth inverse flowbox has bounded derivatives near x0, and (14) gives 0<=H<=E/4 on a smaller Euclidean ball, including Gamma. Smoothness and flatness of E imply flatness of H there at x0. This flatness is a conclusion.

## 5. The pressure equation contradicts smooth flat positive stress

Set T=V tensor V+(E/2-H)I. The preceding bound implies

    (E/4)I<=T<=(3E/2)I.

Incompressibility gives div div(V tensor V)=tr((DV)^2), so (3) says div div T=0. The tensor is smooth and flat at x0. Translate x0 to zero. Write A0(r) for the normalized sphere average of n.T(rn)n, B0(r) for that of tr T(rn)-n.T(rn)n, and e(r) for that of E(rn).

The divergence theorem on the whole ball gives zero flux of div T. Resolving this flux into radial and angular components, the angular divergence averages to zero, and

    A0'(r)=[B0(r)-2A0(r)]/r.

Smoothness at the center rules out a point-source flux. The tensor bounds give A0>=e/4 and B0<=3e<=12A0, hence (r^(-10)A0)'<=0. For 0<r<r1, A0(r)>=(r/r1)^10 A0(r1). Flatness as r decreases to zero forces A0(r1)=0, then e(r1)=0. Every sufficiently small sphere therefore has V=0, which contradicts the nonzero carrier off Gamma. This proves (3) impossible.

## 6. Dependencies and the report scope question

The carrier formulas and estimates (4) agree with the full LIT305 audit, auditor_proofs/reviews/circulating_carrier_pressure_20261103/PROOF.md relative to the agent root. Sections 4 and 5 rederive the confirmed one-sided completion theorem, auditor_proofs/reviews/one_sided_circulating_completion_20261103/PROOF.md. The new point is (10)-(11): monotonicity makes the total normalized-derivative cost negligible even without a pointwise bound on r f'/f.

The earlier application auditor_proofs/reviews/radial_carrier_completion_transfer_20261104/PROOF.md used a logarithmic pointwise upper bound, so A2616 alone did not justify every monotone derivative-flat factor in the broad C69 row of the report. The present theorem covers that whole Volterra family and also drops the condition r f'>=f used for its pressure-source sign. It does not enlarge the parameter range of the separate integrating-factor construction. No computation, model client, formal build or external literature claim is used. The complete existing configured model file comparison is saved in the team records; actual provider execution is independently unattested. Numerical sanity logs were read, but the proof does not depend on them.

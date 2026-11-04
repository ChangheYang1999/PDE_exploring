# Independent audit of completion obstruction by exit-trajectory cost

Status: the conditional local theorem and radial corollary are CONFIRMED A2634-A2636 after complete independent and existing coordinator comparison. Unrestricted extensions remain OPEN A2637.

## 1. Exact statement and the neighborhood restriction

Let 0<c<1/2 and omega be any finite real number. Set Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c), eta=a/b, and kappa=1-2eta=c/(1-c)>0. Let sigma be a smooth two-dimensional section transverse to X, defined on a neighborhood of the closed disc |y|<=R with x0=sigma(0). Work in an X-flowbox Phi(y,s)=exp(sA)sigma(y); Gamma denotes its central orbit segment.

Suppose the smooth field V is flat on Gamma, nonzero elsewhere in this flowbox, and satisfies

    div V=0, X.V=0, DV X=-LV.                        (1)

Write W=curl V. Suppose positive smooth f and a smooth real one-form zeta on the punctured section satisfy

    sigma^*(V.dx)=f zeta,
    c1 f<=|V composed with sigma|<=c2 f              (2)

for constants c1,c2>0. They extend smoothly across the outer circle and f is positive there. Define Y=(zeta2,-zeta1). Every forward Y-trajectory starting in 0<|y|<R is assumed to meet |y|=R at a finite time tau(y), staying in the punctured open disc until this first exit. Let

    I(y)=integral_0^tau(y) div Y(Y_t(y))dt.          (3)

Assume, uniformly as y approaches zero,

    kappa log(1/f(y))+I(y) -> +infinity.             (4)

Then no smooth scalar S on this specified flowbox can obey

    X.grad S=-bS, W.grad S=0,
    S<0 off Gamma, S=0 on Gamma,
    -Delta(S+|V|^2/2)=tr((DV)^2).                    (5)

It is sufficient that the scalar be defined on a flowbox containing the entire closed section disc and all exit trajectories used in (3), together with a neighborhood of the center. With hypotheses only at this fixed R, the assertion excludes completions on that neighborhood. It does not automatically exclude a germ defined only near x0. If the exit and cost hypotheses hold at arbitrarily small radii within every germ neighborhood, then no germ exists.

No bound uniform in y is imposed on tau(y); no radiality of f or sign of the angular component of zeta is imposed in this theorem. Those freedoms do not remove either (3)'s exit hypothesis or (4)'s uniform cost hypothesis.

## 2. Exact first integral along each individual exit

Assume (5), set H=-S, E=|V|^2 and H0=H composed with sigma. Differentiating X.V=0 and using (1) gives

    X cross W=(DV)^T X-DV X=(L-A^T)V=aV.

Since X.grad H=-bH and W.grad H=0, the vector triple-product identity yields

    a grad H cross V=bH W.

Consequently curl(H^(-eta)V)=0 where H>0. Pullback to the section preserves closedness, so with F=fH0^(-eta),

    d(F zeta)=0, or div(FY)=0.                      (6)

The sign here follows directly from div(FY)=partial_1(F zeta2)-partial_2(F zeta1). Along a forward trajectory, (6) gives d(log F)/dt=-div Y. Integration to its own finite exit time yields

    log F(y)=log F(y_out)+I(y).                     (7)

The sign before I is positive. Each individual closed trajectory segment is compact and avoids zero; all its integrands are bounded, even when tau is arbitrarily large along a sequence of starting points. The positive smooth function F has a positive minimum m on the whole outer circle. Thus F(y)>=m exp(I(y)). No regularity of the function tau(y), no transversal crossing of the outer circle, and no uniform exit-time estimate is needed for this inequality.

## 3. Scalar-to-energy ratio and transfer to a Euclidean ball

Solving F=fH0^(-eta) for H0 and using (2),

    H0/E(sigma(y))
      <=c1^(-2)m^(-1/eta) f(y)^(1/eta-2) exp(-I(y)/eta)
      =c1^(-2)m^(-1/eta)
          exp(-[kappa log(1/f(y))+I(y)]/eta).        (8)

This uses kappa=1-2eta, which is positive throughout the stated range. The uniform hypothesis (4) gives a uniform ratio limit zero on the section. A merely pointwise limit along selected trajectories would not suffice.

The skew part of L drops out of X.grad E=2V.DV X=-bE. Hence both H and E have the same exponential scaling along an X-orbit, and H/E is constant there. The local inverse flowbox is smooth and Lipschitz after shrinking about x0, with |y|<=C|x-x0| and bounded s. Therefore (8) implies H/E tends to zero uniformly as x approaches x0 away from Gamma. On a smaller Euclidean ball,

    0<=H<=E/4.                                      (9)

The assertion includes Gamma, where both fields vanish. Flatness of V at x0 gives E=O(|x-x0|^N) for every N. By (9) the same bounds hold for H. Smoothness of H implies every Taylor coefficient at x0 is zero; thus S is flat there as a consequence, not an assumption.

## 4. Positive stress and the smooth center

Set P=E/2-H and T=V tensor V+P I. The tensor T is smooth and flat at x0. From (9), in the quadratic-form order,

    (E/4)I <= T <= (3E/2)I.                          (10)

The incompressibility identity div div(V tensor V)=tr((DV)^2) follows by expanding the derivatives and cancelling terms with div V. Equation (5) is therefore div div T=0 on the entire ball.

Translate x0 to zero. Let angle brackets denote normalized sphere averages, and define

    A0(r)=<n.T(rn)n>,
    B0(r)=<tr T(rn)-n.T(rn)n>, e(r)=<E(rn)>.

The divergence theorem applied to div T inside B(0,r) gives zero flux of div T across its boundary. Decompose that flux into radial and tangential components. The sphere integral of the tangential divergence vanishes, leaving

    A0'(r)+(2/r)A0(r)-(1/r)B0(r)=0.                 (11)

The coefficient 2 is the dimension of the sphere. One can verify the decomposition by choosing an orthonormal radial frame at a point: the normal component of div T is partial_r T_nn+(2T_nn-sum_t T_tt)/r plus a surface divergence. This also fixes the sign in (11). No point-source term occurs because both T and div T are smooth at the center.

From (10), A0>=e/4 and B0<=3e<=12A0. Thus A0'<=10A0/r, so r^(-10)A0(r) is nonincreasing. For 0<r<r1,

    A0(r)>=(r/r1)^10 A0(r1).                         (12)

Flatness gives A0(r)=O(r^N) for every N. Taking N>10 in (12) forces A0(r1)=0. Then e(r1)=0 and continuity yields V=0 on the sphere. For all sufficiently small r1, this contradicts the assumed nonzero field off Gamma. This proves the theorem.

## 5. Radial corollary with a degenerating but strictly positive angular component

Suppose f=f(r), zeta.e_theta>0 at every point 0<r<=R, and a nonnegative measurable q, integrable on each [r,R], satisfies

    (-div Y)_+/Y_r<=q(r), Y_r=Y.e_r=zeta.e_theta,
    Q(r)=integral_r^R q(s)ds,
    kappa log(1/f(r))-Q(r) -> +infinity.             (13)

A single positive lower bound for Y_r on the whole punctured disc is not assumed. Fix a starting radius r0>0. On the compact closed annulus r0<=r<=R, Y_r has a positive minimum d(r0), and Y is smooth and bounded. The radius is increasing and ODE continuation holds until outer exit, which occurs in time at most (R-r0)/d(r0). This establishes the individual finite-exit hypothesis even if this bound diverges as r0 approaches zero.

The radius is a valid increasing parameter on that segment. Changing variables in (3) gives

    I(y)=integral_r^R (div Y)/Y_r ds >=-Q(r).         (14)

The final limit in (13) therefore implies (4) uniformly in angle. If R is replaced by a smaller R', the new Q differs by the finite constant integral_R'^R q. All other premises persist. Hence this corollary rules out a completion germ, not only a completion on one fixed section disc.

A further sufficient condition for the general theorem is obtained by replacing I with minus the cost D(y)=integral_0^tau(y)(-div Y)_+(Y_t(y))dt. Since I>=-D, the limit kappa log(1/f)-D tending uniformly to infinity suffices. This loses any helpful cancellation of signed divergence and is not asserted to be sharp.

## 6. Scope, dependency comparison and unresolved cases

This proof independently reconstructs all six sections of LIT311, in the team records relative to the agent root. It uses the same carrier identity, section closedness and smooth positive-stress mechanism as the confirmed LIT309/LIT310, with the precise new exit-cost assumption. The positive-stress conclusion is local. Arbitrary finite omega is allowed through the flowbox geometry and the exact skew cancellations, without a uniform bound on geometry-dependent constants.

The radial corollary genuinely permits the angular component to tend to zero near the center while remaining strictly positive on the punctured disc. It does not automatically cover angular zeros at nonzero points, trapping, infinite exit time, or failure of the uniform cost limit. The general theorem may apply in further configurations only after its own assumptions are checked. Neither criterion constructs an Euler profile, establishes every carrier admits such a normalization, or excludes every scalar sign or zero-set geometry. The main arbitrary-helicity decay-only conjecture remains open.

No numerical computation, new model client or formal build was needed. Existing configured model coordinator comparison is requested through shared files; actual provider identity is independently unattested.

The complete eleven-item LIT311 coordinator comparison, all four joint wording remarks and the exact-check log were read. The finite-exit sign, uniform ratio limit, smooth center, arbitrary finite omega and fixed-domain versus germ distinctions agree with this proof. No gap was found. LIT312 in the same comparison file is a separate later submission and is not certified by these verdicts.

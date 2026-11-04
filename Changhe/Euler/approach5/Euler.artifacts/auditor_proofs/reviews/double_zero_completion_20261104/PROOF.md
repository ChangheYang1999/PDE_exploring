# Independent audit of completion obstructions at a double velocity zero

Status: LIT312 is CONFIRMED A2638-A2641 at the exact local scopes below. Broader conclusions remain OPEN A2642.

## 1. Finite-order stress theorem

Let V and H be C2 on B_R(x0) in R3, with V vector-valued and H scalar. Put E=|V|^2 and P=E/2-H. Suppose

    div V=0, -Delta P=tr((DV)^2),
    V(x0)=DV(x0)=0,
    0<=H<=delta E on B_R(x0), 0<=delta<1/4.             (1)

Then V=H=P=0 on the whole ball. No transport, homogeneity or infinite-flatness hypothesis is needed. Retaining the differential and center hypotheses, it is also sufficient locally that H>=0, H=0 wherever E=0, and H/E tend uniformly to zero as x approaches x0 through E>0: choose a smaller ball on which H<=E/8.

Translate x0 to zero. Set T=V tensor V+P I. Incompressibility gives div div(V tensor V)=tr((DV)^2), so div div T=0. For normalized sphere averages define

    e(r)=<E(rn)>, v(r)=<(V(rn).n)^2>, hbar(r)=<H(rn)>,
    A0(r)=<n.T(rn)n>=v+e/2-hbar,
    B0(r)=<tr T(rn)-n.T(rn)n>=2e-v-2hbar.

Thus B0-2A0=e-3v exactly. The flux of div T through each sphere is zero by the divergence theorem on the whole ball. The radial and tangential decomposition of this flux gives

    r A0'=B0-2A0=e-3v.                                (2)

The angular divergence integrates to zero; there is no center flux since T is C2. The scalar cancels in (2). From (1), A0>=v+(1/2-delta)e. Consequently

    A0'<=e/r<=p A0/r, p=1/(1/2-delta)<4.               (3)

This uses an upper bound on A0', not a claimed nonnegative derivative. Hence r^(-p)A0 is nonincreasing. For 0<r<r1<R,

    0<=A0(r1)<=(r1/r)^p A0(r).

The C2 Taylor estimate at a double zero gives e(r)=O(r^4), and A0<=3e/2 because H>=0. Letting r decrease to zero forces A0(r1)=0, then e(r1)=0. Continuity and all radii give V=0 on the whole ball. Equation (1) then gives H=P=0. For delta=1/8, p=8/3.

## 2. Exact finite-exit completion theorem

Fix 0<c<1/2 and any finite real omega. Write Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c), eta=a/b and kappa=1-2eta=c/(1-c)>0. Let sigma be a smooth section transverse to X through x0=sigma(0), defined across a closed disc |y|<=R. Use the finite flowbox Phi(y,s)=exp(sA)sigma(y) and its central orbit Gamma.

Suppose V is C2, zero on Gamma, nonzero off Gamma, V(x0)=DV(x0)=0, and

    div V=0, X.V=0, DV X=-LV, W=curl V.                (4)

Suppose positive C2 f and a C2 one-form zeta on the punctured section extend across the outer circle and satisfy

    sigma^*(V.dx)=f(y)zeta(y),
    c1 f(y)<=|V(sigma(y))|<=c2 f(y), c1,c2>0.          (5)

Let Y=(zeta2,-zeta1). Assume each forward trajectory from the punctured open disc has a finite first exit tau(y) at its outer circle, staying in the punctured disc until exit. Put

    I(y)=integral_0^tau(y) div Y(Y_t(y))dt,
    kappa log(1/f(y))+I(y) -> +infinity uniformly.     (6)

Then no C2 scalar S on that specified flowbox satisfies

    X.grad S=-bS, W.grad S=0,
    S=0 on Gamma, S<0 off Gamma,
    -Delta(S+|V|^2/2)=tr((DV)^2).                      (7)

The flowbox must contain the entire closed section and trajectories used in (6). At a fixed outer radius this excludes a completion on the specified neighborhood. To exclude a germ, the exit and cost assumptions must hold at arbitrarily small radii inside every possible germ domain. Infinite flatness is not a premise.

## 3. Proof by scalar-to-energy dominance

If S existed, put H=-S and E=|V|^2. Differentiating X.V=0 and using (4) gives

    X cross W=(DV)^T X-DV X=(L-A^T)V=aV.

Together with X.grad H=-bH and W.grad H=0, this implies a grad H cross V=bH W. Since eta=a/b,

    curl(H^(-eta)V)=0 off Gamma.

Pulling back to the section gives div(FY)=0 with F=f(H composed sigma)^(-eta). On each individual finite exit trajectory,

    log F(y)=log F(y_out)+I(y).                        (8)

Each closed trajectory segment is compact and avoids zero. A uniform exit time and regularity of tau as a function of y are unnecessary. The outer-circle minimum m=min F is positive, so (5), (6) and (8) give

    H(sigma(y))/E(sigma(y))
       <=c1^(-2)m^(-1/eta)
           exp(-[kappa log(1/f(y))+I(y)]/eta) -> 0.    (9)

The convergence is uniform. Both H and E scale by exp(-bs) along X, the latter because the skew part of L contributes zero to V.LV. Thus H/E is constant on each orbit. The smooth local inverse flowbox has bounded derivatives and |y|<=C|x-x0|. It transfers (9) to a full Euclidean neighborhood. On a smaller ball, 0<=H<=E/8, including Gamma. Section 1 gives V=0 there, contrary to its required nonzero values off Gamma. This proves the theorem.

## 4. Pointwise positive angular component with a one-sided rate

As a sufficient condition for (6), suppose f=f(r), zeta.e_theta>0 at every punctured point and a nonnegative radial function q, integrable on each [r,R], satisfies

    (-div Y)_+/(Y.e_r)<=q(r),
    kappa log(1/f(r))-integral_r^R q(s)ds -> +infinity. (10)

Here Y.e_r=zeta.e_theta. On each fixed compact annulus r0<=|y|<=R this positive function has a minimum d(r0)>0. The radius strictly increases, and continuation on that annulus gives exit in time at most (R-r0)/d(r0). Along the trajectory, change of variable from time to radius gives I(y)>=-integral_r^R q. Thus (6) holds uniformly in angle. On shrinking the outer radius, the integral changes by a finite constant. The hypotheses therefore exclude germs as well as completions on one specified domain. No lower angular bound uniform near zero is needed.

## 5. Radial coefficients of the normalized form

An alternative sufficient condition is

    zeta=g(r)e_r+h(r)e_theta, h(r)!=0 for 0<r<=R,      (11)

where g and h are C2 functions of r. In (5), f may depend on the angle. No derivative-rate hypothesis on g or h is imposed. This is a condition on a one-form in section coordinates, not axisymmetry of V in physical space.

The function h has constant sign. If h<0, replace V and zeta by their negatives; (4), (5), (7), E and tr((DV)^2) are preserved. Thus assume h>0. From the pullback estimate and the upper bound in (5),

    |zeta|<=C_sigma |V(sigma)|/f<=C_sigma c2.

In particular h is bounded above. The section field is Y=h e_r-g e_theta, so div Y=h'+h/r. Each compact annulus has positive minimum radial speed, giving a finite exit. Its signed cost is exactly

    I(y)=integral_r^R [h'(s)/h(s)+1/s]ds
         =log(Rh(R)/(r h(r))).                       (12)

There is no g term because it has no angular dependence. Boundedness of h gives I(y)>=log(C0/r). The Taylor estimate on V and the Lipschitz estimate |sigma(y)-x0|<=C|y| imply, from the lower bound in (5), f(y)<=C|y|^2 uniformly. Therefore the left side of (6) is at least (2kappa+1)log(1/r)-C and tends to infinity. Equivalently (9) is bounded by C f(y)^(kappa/eta)[r h(r)]^(1/eta). Conditions (11) and the center estimates persist on smaller discs, so the conclusion excludes a germ. This covers h tending to zero but never vanishing at a punctured point; it says nothing automatic about punctured zeros or trapped trajectories.

## 6. Dependencies, comparison and scope

All six source sections of LIT312 were read. The full existing coordinator LIT311/LIT312 comparison and its exact-check log were also read, including the four wording remarks. The independent proof above makes the smaller-ball use in Section 1, the Lipschitz transfer for f in Section 5, and the fixed-domain versus germ distinction explicit. Its stress identity, exponent, exit sign and radial cost agree with the comparison.

No computation was run and no new model client or agent was started. This proof does not classify every section form, construct a full scalar completion, or settle unrestricted Euler profile nonexistence. Section 1 treats delta<1/4; the endpoint is audited separately. Existing configured model collaboration is through files; actual provider execution is independently unattested.

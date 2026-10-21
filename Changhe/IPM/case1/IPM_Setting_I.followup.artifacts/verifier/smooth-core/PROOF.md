# Smooth center replacement at fixed canonical strain

Date: 2026-10-20. Status: proved approximation statement for trial fields, not an existence theorem for transport. This explains the scope of the exact finite-interpolant center obstructions in AV17/19/23.

## Statement and notation

Let rho be even in x, odd in y, smooth away from the origin and in the sublinear growth class of TASK.md. Write P(x,y)=x^2 y. Assume near the origin

    rho=P+r^5 A(theta)+r^7 B(r^2,theta),

where A and B are smooth angular functions with the stated parities, B and its needed derivatives are uniformly bounded, and rho=P a with a=1+O(r^2). More precisely, the factored angular expansion and all its derivatives on fixed annuli are uniform. These assumptions hold for the finite warped nodal representations under discussion. They imply rho is C^(2,alpha) locally for every alpha<1, but do not imply a smooth center.

There exist trial fields rho_epsilon, smooth at the center and equal to P on r<=epsilon, that retain parity, the exact normalization a(0)=1, the growth class and the canonical central strain of rho. For every fixed compact set K and 0<alpha<1,

    ||rho_epsilon-rho||_(C^(2,alpha)(K)) <= C_K epsilon^(3-alpha),
    ||U[rho_epsilon]-U[rho]||_(C^1(K)) <= C_K epsilon^4.

Their transport residuals at the same c_l converge locally uniformly to that of rho. In particular, if the original c_l obeys the canonical identity, so does every replacement. The replacements are not asserted to solve transport. A residual failure at a fixed point away from the origin persists for sufficiently small epsilon.

## Construction of the strain correction

Choose a smooth radial cutoff chi, one on [0,1], zero on [2,infinity), and between zero and one. Choose a nonnegative smooth radial function b supported in (1,2), normalized by

    (1/4) integral_1^2 r b(r) dr=1,
    phi(x,y)=x^2 y b(r).

The full-plane inverse proof in ../exterior-tail/PROOF.md gives c[phi]=1 and U[phi]=(-x,y) on r<1. Indeed phi has only density sine modes1 and3; the exterior sin1 mode contributes no interior velocity, and the sin3 mode contributes exactly the displayed strain. Alternatively these identities follow directly by expanding the nonsingular kernel on the inner disk. All quantities here use the canonical inverse, without a freely chosen harmonic field.

For epsilon<1/4 put

    delta_epsilon=chi(r/epsilon)(P-rho),
    d_epsilon=c[delta_epsilon],
    rho_epsilon=rho+delta_epsilon-d_epsilon phi.

The linearity of the canonical inverse and of its central strain gives c[rho_epsilon]=c[rho] exactly. On r<=epsilon, the shell is absent and rho_epsilon=P. Beyond r=2, the field is exactly rho. On the transition annulus both summands are smooth; parity and the x^2 y factor are preserved. The resulting density is globally smooth if rho was smooth everywhere away from zero; if rho has another allowed finite-regularity point, its existing regularity there is unchanged. This last precision suffices for local versions of the statement.

## Uniform estimates and proof

Scale X=epsilon Z. The assumed center expansion gives

    delta_epsilon(epsilon Z)=epsilon^5 F_epsilon(Z),
    F_epsilon=-chi(|Z|)[|Z|^5 A(arg Z)+epsilon^2 |Z|^7 B(epsilon^2|Z|^2,arg Z)].

The functions F_epsilon are supported in |Z|<=2 and uniformly bounded in C^(2,alpha), for each alpha<1. To check the assertion at zero, derivatives of |Z|^5 A have size O(|Z|^(5-j)) for j<=3. Their derivatives through order2 are Lipschitz, with bounded third derivatives, and the difference-quotient induction extends them at zero. The same bounds hold for the remainder uniformly in epsilon. Thus

    ||delta_epsilon||_(C^(2,alpha))<=C epsilon^(3-alpha).

For a compactly supported odd source F with uniformly bounded C^(1,alpha) norm, the canonical kernel has uniformly bounded U[F] and DU[F]. A direct proof subtracts F(X), respectively DF(X), on a unit disk: zero angular mean and the Holder increment give the integrable radial bound r^(alpha-1). Outside that disk the source is compact and bounded. Far from the support, oddness implies zero total mass and kernel pairing bounds the velocity by C|X|^-3 and its derivative by C|X|^-4. On intermediate bounded regions the same subtraction estimate is uniform. Applying this argument to F_epsilon gives uniform constants.

Since the operator is homogeneous of degree zero, including its contact term,

    U[delta_epsilon](epsilon Z)=epsilon^5 U[F_epsilon](Z).

Hence its global C1 norm is O(epsilon^4), and in particular |d_epsilon|<=C epsilon^4. The fixed shell and its velocity are smooth and bounded with their derivatives on compact sets. The two asserted estimates follow. For an observation point |X|>=4 epsilon the core alone satisfies the sharper bound

    |U[delta_epsilon](X)|<=C epsilon^8 |X|^-3,

because its zero mass cancels the zeroth kernel term and its absolute first moment is O(epsilon^8). The shell correction is generally the larger O(epsilon^4) change at fixed distance.

Write W=c_l X+U[rho] and R=W.grad rho-rho. With eta=rho_epsilon-rho and V=U[eta], direct algebra gives

    R_epsilon-R=W.grad eta+V.grad rho+V.grad eta-eta.

On every fixed compact set, W and grad rho are bounded, grad eta=O(epsilon^4), eta=O(epsilon^4) (including the shell), and V=O(epsilon^4). Therefore ||R_epsilon-R||_C0<=C_K epsilon^4. Where a chosen residual normalizer is positive and bounded away from zero, its normalized residual also converges uniformly. No uniform statement is made across zeros of that normalizer. In particular at the two selected radius10 points of dnSB, both density and density gradient are exactly unchanged by the construction and the residual change is V.grad rho.

At the center every higher transverse trace G_j, j>=3, is identically zero on the positive x-axis segment x<epsilon. This is an exact local property of the replacement. It does not establish the finite-part identities B_j=0: those identities use the coupled transport hierarchy, and the replaced fields do not satisfy it exactly. A fit restricted to the smooth core therefore cannot replace the independent axis compatibility test required by TASK.md.

## Scope and dependencies

The statement proves density of a set of smooth-center trial fields in these weak local norms while preserving canonical strain. It does not make an approximate profile into a solution, create a verified family, give the required three-resolution/three-domain sequence, or reach YES_inf. The pointwise residual defect of dnSB persists. Likewise it does not refute the exact finite-basis obstruction; the radial cutoff leaves that finite tensor space.

Dependencies are the explicit full-plane kernel, its homogeneity and cancellation, the exterior strain identity proved in the adjacent topic, and elementary scaling/Taylor estimates. The numerical file below checks the size of the changes for the saved candidate with an independently implemented compact-source quadrature. Floating checks are not enclosures.

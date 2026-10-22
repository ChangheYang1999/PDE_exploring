# Gradient of the finite-sphere characteristic extension

## Statement, hypotheses and scope

Let W be a C2 vector field, let kappa be real, and let S_epsilon be the circle of radius epsilon>0 centred at the origin. Let h be C2 in a neighbourhood of the circle. Work on any open set swept out by forward W characteristics from a transverse open part of that circle, with a unique C2 hitting time and boundary point. Transversality means W(Q).Q != 0. Define the temperature by Theta(P)=exp(kappa T(P))h(Q(P)), where Q is the backward intersection and T is elapsed time. Then the gradient on the circle is

    grad Theta(Q) = grad h(Q) + Q [kappa h(Q)-W(Q).grad h(Q)]/[W(Q).Q].        (1)

Along the forward characteristic this gradient satisfies

    g' = (kappa I-DW^T)g.                                                   (2)

Thus (1), followed by (2), computes the derivative of precisely the finite-sphere extension. Initializing (2) with grad h alone computes that derivative only if the boundary data already satisfy W.grad h=kappa h on the circle. This is a local transport statement; it asserts no global center solution, canonical velocity fixed point or B2 profile.

## Proof

The flow and the circle's defining function are C2. At a transverse intersection, the derivative in time of the defining function is nonzero. The implicit function theorem therefore gives a C2 local hitting time and boundary point. Their composition with h defines a C2 temperature. Following the forward flow by time s replaces T by T+s and preserves Q, so Theta evolves by exp(kappa s) and W.grad Theta=kappa Theta.

On the circle the trace is h. Every tangent derivative of Theta equals that of h, so their gradients differ by a scalar multiple of the normal Q. Taking the scalar product with W and using the transport equation determines that scalar uniquely, giving (1). This formula depends only on the trace: if the chosen extension changes grad h by mu Q, the scalar correction changes by -mu, so the sum is unchanged. Differentiating W.grad Theta=kappa Theta in Cartesian coordinates gives DW^T grad Theta + (W.grad)grad Theta=kappa grad Theta, which is (2). Uniqueness for the linear ordinary differential equation proves the stated reconstruction of the gradient. No integration by parts or assumption at infinity is used.

On an orbit segment that stays in x>0, write v=W1/x and p=grad Theta/x. The quotient rule gives

    p'=((kappa-v)I-DW^T)p,
    G'=-(1+v)G+p1,                                                        (3)

when Omega=xG solves Omega'+Omega=Theta_x. Prescribing the same G at the inner sphere, but replacing the gradient by the incompatible grad h, can alter the later G. Formula (3) avoids transporting a common factor proportional to the inner x coordinate, but divisions by x can be poorly conditioned near the axis. No uniform numerical-conditioning claim is made. It is exactly equivalent to (2) where defined. In the Gaussian application W1 is odd in x, hence the invariant axis and ordinary uniqueness preserve positive x over each finite orbit segment. The transported vorticity equation is imposed as an independent scalar equation along that orbit.

## Inner jet and size of the compatibility defect

For the literal signed Gaussian fields of P236, W is smooth (in particular C3) and the polynomial h below is smooth. These stronger local regularity hypotheses apply in this section; the abstract transport theorem above needs only C2. We have W(0)=0, W1 is odd and W2 is even in x, DW(0) is diagonal, and beta=3, kappa=1, W1=alpha x+a11 xy+O(r3), W2=mu y+O(r2), alpha=1/2 and mu=11/2. Set h=x2(1+f01 y), f01=-2 a11/mu. The degree2 term of W.grad h-kappa h is (2 alpha-kappa)x2=0. Its degree3 coefficient is [f01(2 alpha+mu-kappa)+2 a11]x2 y=(mu f01+2 a11)x2 y=0. Smoothness therefore gives a defect O(r4). The symmetric part of DW(0)=diag(alpha,mu) is positive definite, so W(Q).Q is bounded below by c epsilon2 on all sufficiently small circles. Formula (1) changes the gradient by O(epsilon3). The change in p also has a uniform local estimate, despite division by x: parity gives W1=x w with w smooth, and direct factorization gives kappa h-W.grad h=x2 D, where D=kappa(1+f01 y)-2w(1+f01 y)-f01 W2=O(r2) by the same two cancellations. If eta=(kappa h-W.grad h)/(W.Q), then |eta|<=C x2 on the circle. Hence |delta grad Theta|<=C x2 epsilon and |delta p|<=C |x| epsilon<=C epsilon2 for x!=0, extending continuously to zero on the axis. In angular coordinates eta=O(epsilon2 cos2(phi)), with the factor epsilon2 retained. These are local estimates only. No uniform estimate on amplification to remote points follows without a quantitative flow bound; the numerical experiment below must measure that amplification.

The field and jet use the independent exact full-plane Gaussian inverse in P236, with its own center subtraction. This experiment changes only the finite-sphere gradient treatment. All source and fitting differences remain separately identified.

## Manufactured noncompatible boundary data

Take W=a(x,y), a=1/2, kappa=1, h=x2(1+c y), epsilon>0. This affine field is a transport control, not B2. For r>epsilon, T=log(r/epsilon)/a and Q=epsilon P/r. The exact extension is

    Theta(P)=x2(1+c epsilon y/r).

Its derivatives are

    Theta_x=2x(1+c epsilon y/r)-c epsilon x3 y/r3,
    Theta_y=c epsilon x4/r3.

Both follow directly by differentiating r=(x2+y2)^(1/2). These derivatives satisfy (1) at r=epsilon and (2) along rays. They are homogeneous of degree1, hence p=grad Theta/x is constant on each ray. If G(Q)=G_e(Q), direct integration of (3) gives

    G(P)=exp(-(1+a)T)G_e(Q)+(1-exp(-(1+a)T))*[Theta_x(P)/x]/(1+a).

This supplies an exact noncompatible test of the boundary correction, gradient propagation and vorticity forcing. The case c=0 tests compatible boundary data. A deliberately tangent W must be rejected by the transversality guard.

## Additional non-diagonal transport control

The isotropic example alone cannot detect use of DW instead of DW^T. For a separate compatible test take

    W=(x/2+y/4, 3y/2), kappa=1, L=x-y/4,
    Theta=L^2, Omega=4L/3.

One has W.grad L=L/2, so W.grad Theta=Theta and W.grad Omega+Omega=2L=Theta_x. Also grad Theta=2L(1,-1/4). Prescribe exactly these traces on the inner circle. Formula (1) has zero correction and (2),(3) must reproduce the displayed fields at the target. DW has a nonzero off-diagonal entry, so this checks the transpose convention. This affine field does not satisfy the B2 divergence or symmetry hypotheses and is used only as a transport test. The chosen points have L>0 and positive x. Explicitly along a backward segment,

    y(t)=exp(-3t/2)y(0),
    x(t)=exp(-t/2)L(0)+exp(-3t/2)y(0)/4.

For the tested points (1,0.3),(3,-2),(0.2,0.4), x stays positive: this is immediate for positive y, and for y=-2 its minimum in the factored bracket L(0)+exp(-t)y(0)/4 is x(0)>0. This justifies the divided variables in this control.

## Numerical plan and evidentiary limits

The numerical construction uses the first backward intersection, with W(Q).Q>0; thus it extends data forward to the exterior. The abstract local formula above also holds for an inward transverse segment and does not need an exterior-domain claim.

At the three negative NUM witnesses studied in P240, use the same literal signed Gaussian W and the same finite-sphere temperature. Independently compare corrected gradient transport with fourth-order Cartesian differences of the scalar extension, at several difference steps and inner radii. Preserve the incompatible gradient result for comparison. Transport G with the same inner jet in each case. Check completion of every orbit and finite transversality denominators; report raw differences, PDE residuals and all signs. Direct finite differences are only numerical controls, not bounds on exact derivatives. Refinement agreement is not an interval certificate.

This argument was written before the experiment code. Numerical data, code hashes and actual execution times belong in verification/. The B2 existence question remains OPEN regardless of these outcomes.

# A geometric incoming zero arc with four sources and two saddle ancestors

Status: CONFIRMED by an independent full construction, exact controls and actual Opus5.5 reviews320/321, with the adjudication below. This is a smooth planar-field example, not a B2 profile.

## Exact statement

There is a smooth complete field W on R2 satisfying

    div W=4, W(-x,y)=(-W1(x,y),W2(x,y)),
    W(X)-2X bounded, DW(0)=diag(0,4),                (1)

whose zero set consists exactly of the segment gamma=[-1,1]x{0}, four nondegenerate sources and two nondegenerate saddles. The segment is normally repelling, with two nonaccumulating incoming endpoints flat in the tangential direction. At each endpoint the incoming exterior center orbit has a saddle as its backward limit; its two upstream stable connections come from the two nearby sources. Thus the immediate backward limit of that exterior orbit need not have an open backward basin for a field with this geometry.

The field equals(0,4y) near0. Consequently it cannot underlie a B2 solution with Theta=a0 x^2+O(|X|^3),a0!=0: Omega=-curl W would be zero there, and the B2 vorticity equation W.grad Omega+Omega=Theta_x would force Theta_x=0 there. The construction makes no claim about the coupled transport equations away from the center, or about a B2 candidate. Any extra parity enjoyed by this particular example is not an additional restriction on the B2 problem.

## A bounded-divergence perturbation of the radial field

Define the smooth nonnegative bump and its cumulative function

    eta(t)=exp(-1/[t(1-t)]) for0<t<1, and0 otherwise,
    H(t)=integral_(-infinity)^t eta(r)dr / integral_0^1 eta(r)dr.

H is smooth, equals0 for t<=0 and1 for t>=1, and has H'>0 throughout(0,1), since eta>0 there. In particular it is strictly increasing there. On[1/3,2/3] one has eta>=exp(-9/2), while eta<=exp(-4) everywhere. Therefore

    0<=H'<=3 exp(1/2)<6.                            (2)

For x>=0 define h(x)=0 on[0,1], and for x>1 set

    h(x)=2 H(log(x)/10)(x-2).                       (3)

Extend h oddly. Smooth flatness of H at0 makes h smooth and flat at x=1, and odd extension is smooth since h=0 near0. Its zeros are exactly[-1,1] and x=+/-2. It is negative on(1,2). For x>1,

    h'=2H + [(x-2)/(5x)] H'.                        (4)

When1<x<2, the second coefficient is in(-1/5,0), hence -6/5<h'<2. When x>=2, it is in[0,1/5), hence0<=h'<16/5. Reflection gives the same bounds on the negative side. For x>=exp(10), h=2x-4, and for x<=-exp(10), h=2x+4. In particular a(x)=2x-h(x) is bounded and a' has compact support.

At x=2, lambda=h'(2)=2H(log(2)/10) lies strictly between0 and2. We may modify h in an arbitrarily small neighborhood of2 so that it is exactly lambda(x-2) on a smaller neighborhood, while retaining the same zeros and h'<4. To justify this standard cutoff step, write h(2+u)=lambda u+r(u), with r(u)=O(u^2),r'(u)=O(u). Replace r by(1-rho(u/epsilon))r, where rho is a fixed smooth cutoff equal1 near0 and0 outside1. The change in derivative is O(epsilon); lambda and the positive gap between sup h' and4 are fixed. Choosing epsilon small preserves h'<4 and the sign of h(2+u)/u. Reflect this modification oddly near-2. The far field, central segment and endpoint flatness are untouched. Continue to denote the modified function by h.

Choose a smooth even cutoff chi0(y) in[0,1], equal1 for|y|<=1 and0 for|y|>=2. Put

    Psi0=a(x)y chi0(y),
    W0=2(x,y)+(-partial_y Psi0,partial_x Psi0).      (5)

Then div W0=4, the parity in(1) holds, and W0-2X is bounded. In particular the full flow is complete by the linear-growth bound. Its second component is

    (W0)2=y[2+(2-h'(x))chi0(y)].                    (6)

The bracket is the convex combination of2 and4-h'(x), both strictly positive. Hence a zero must have y=0, and there(W0)1=h(x). Thus Z(W0)=gamma union{(-2,0),(2,0)}. Near gamma, W0=(h(x),(4-h'(x))y), giving the stated normal and incoming geometry. In a rectangular neighborhood of q=(2,0) where h is linear and chi0=1,

    W0=(lambda u,kappa v), u=x-2,v=y,
    kappa=4-lambda in(2,4).                         (7)

At this stage q and its reflected partner are sources.

## An explicit smooth replacement of one source by three zeros

We construct the required odd b(v), rather than relying only on a phase portrait. Set A=kappa+1, so A>kappa, and choose M0=12A/lambda. Let chi(s)=1-H(s). Choose R>0 strictly smaller than the v half-height of the linear rectangle, and r0=R exp(-M0). For v!=0 put

    b(v)=v[kappa-A chi(log(|v|/r0)/M0)],             (8)

and define b(0)=0. For|v|<=r0, chi=1 and b(v)=-v, so there is no singularity at0 and b is smooth odd. For|v|>=R it equals kappa v. Flatness of the cutoff at its endpoints gives smooth matching at +/-r0,+/-R.

For v!=0 in the transition, let s=log(|v|/r0)/M0. Then

    b'=kappa-A chi(s)-(A/M0)chi'(s)
       <=kappa+6A/M0=kappa+lambda/2<4.              (9)

Outside the transition the derivative is either-1 or kappa, also below4. Since chi strictly decreases from1 to0, there is exactly one positive d in(r0,R) where chi= kappa/A. The equation chi(s_d)=kappa/A, with0<kappa/A<1, implies0<s_d<1. Therefore H'(s_d)>0 by the explicit positive bump. This strict interior conclusion follows from the zero equation, not from the support margin of the insertion. Thus the zeros of b are exactly0,+/-d. At them

    b'(0)=-1,
    0<b'(+/-d)=-(A/M0)chi'(s_d)<=lambda/2<4.       (10)

This remains a rigorous existence construction even if r0 is extremely small; no numerical resolution or computation of exp(-M0) is needed.

Set k(v)=kappa v-b(v), a compactly supported smooth odd function. Choose an even smooth cutoff rho(u) in[0,1], with compact support in the open u-interval of the linear rectangle and equal1 near0. Add to W0 the divergence-free field

    D=(partial_v psi,-partial_u psi),
    psi(u,v)=u rho(u)k(v).                          (11)

It is supported in that rectangle. There the new components are

    Wu=u[lambda+rho(u)k'(v)],
    Wv=kappa v-[rho(u)+u rho'(u)]k(v).              (12)

The bracket in Wu equals

    (1-rho)lambda+rho(4-b'(v))>0.                 (13)

Hence zeros in the rectangle must have u=0, and there Wv=b(v). There are exactly the three zeros(0,0),(0,d),(0,-d), with no additional transition-region zero. Their derivative matrices are diagonal with entries4-b'(v),b'(v). By(10), the middle zero is a nondegenerate saddle with eigenvalues5,-1, and the other two are nondegenerate sources. In particular the x eigenvalue changes from lambda to5; only the axis orbit set, not its parametrization in time, is preserved. The trace remains4 because div D=0.

Because k(0)=0, v=0 stays invariant. On its left branch Wu<0, and outside the insertion h<0 on(1,2), so the entire interval1<x<2,y=0 is the orbit from the new saddle q to the endpoint p+=(1,0). Smoothness and uniqueness prevent finite-time arrival at either zero. On u=0, v'=b(v); b is negative on0<v<d and positive on-d<v<0. Thus the saddle's two stable branches have backward limits at the two new sources. Ordinary hyperbolic saddle passage therefore puts its two adjacent outgoing sectors in the respective source basins. This last basin description is also a direct instance of the finite passage argument in178; it is not needed to establish the immediate saddle backward limit.

Make the x-reflected insertion in a disjoint rectangle near(-2,0), using Dminus(X)=S D(SX),S=diag(-1,1). Reflection preserves divergence and produces exactly the required vector parity. Each perturbation is compactly supported and smooth, so(1) and completeness persist. The only zeros are gamma, the two saddles and the four sources already identified. The exterior index sum is4-2=2, consistent with an incoming central arc of index-1 and index1 at infinity. No index argument is being used in place of the explicit zero count.

## Scope audit

This verifies the existence claim in the frozen lead4.7(xiv) scope paragraph: its listed geometric assumptions do not force the immediate ancestor of an incoming endpoint branch to be a source. The field is not a coupled counterexample, as the explicit center calculation shows. No profile PDE, inverse operator, far-field nonlinear balance or endpoint-exclusion theorem is refuted by it. The lead's qualitative derivative construction of b is replaced here by the explicit formula(8), with all derivative bounds proved. The h construction and localized divergence-free insertion were checked directly, without numerical-lane code.

Written UTC 2026-10-21T15:33:59.608439+00:00, before new controls.

Independent audit completed UTC 2026-10-21T15:49:45.588076+00:00.

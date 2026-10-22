# Smooth arc coordinates for the beta-two system

Status: proved local coordinate theorem and equivalent equations on the arc side. This does not construct a half-arc endpoint, an outgoing attachment, an incoming isothermal endpoint, or a global B2 profile. It independently checks the main new coordinate argument in the lead's endpoint2 consultation.

## Statement and notation

The plane has the fixed positively oriented orthonormal physical frame (e_x,e_y). Put J(v1,v2)=(-v2,v1), curl W=partial_x W2-partial_y W1. Let W be C-infinity near a smooth embedded zero half-arc gamma(a), -a0<=a<=0, parametrized by arclength toward p=gamma(0), and assume div W=4. Write tau=gamma'(a), n=J tau and lambda(a)=-curl W(gamma(a)). After shortening the terminal arc if necessary, there is a C-infinity chart X(a,r), smooth up to a=0 and extendible as a diffeomorphism across it, with

    X(a,0)=gamma(a), X_r(a,0)=e(a)=n+lambda tau/4,
    W(X(a,r))=4r X_r(a,r), det(X_a,X_r)=1,             (1)

for a<=0. The extension across a=0 is only a chart extension and need not satisfy the last two identities there. For a<0 the backward trajectory of X(a,r) converges to gamma(a). The fiber X(0,r) is the strong unstable curve of p.

Suppose also Theta is C-infinity, Omega=-curl W, and the fields obey

    W.grad Theta=0, (W.grad+1)Omega=partial_x Theta.    (2)

On the arc-side chart Theta(X(a,r))=G(a), G(a)=Theta(gamma(a)). Set

    Q=4 X_a.X_r+4r X_a.X_rr-4r X_r.X_ar.              (3)

Then the exact remaining equation is

    Q(a,r)=G'(a) int_0^1 y_r(a,r t^4) dt,
    det(X_a,X_r)=1.                                   (4)

Conversely any C-infinity local chart X and G satisfying (4) define all four local equations div W=4, Omega=-curl W and (2) by W(X)=4r X_r, Theta(X)=G and Omega(X)=Q. This includes r=0. It does not require arclength labels if det(X_a,X_r)=1 is imposed directly.

## Proof of the smooth chart

Differentiating W(gamma)=0 gives DW tau=0. In the oriented frame (tau,n), trace DW=4, so its matrix is [[0,lambda],[0,4]]: its curl is -lambda. Thus

    M_a=DW(gamma(a))=(4n+lambda tau) tensor n,
    M_a tau=0, M_a e=4e, det(tau,e)=1.

Extend gamma smoothly past a=0 as an arclength curve, and extend lambda smoothly. Choose tau=gamma' and n=J tau on this extension, preserving the orthonormal frame. Define the artificial matrix M_a by the same formula there. Its eigenvalues remain exactly0 and4, and its projections P0=I-M_a/4 and P4=M_a/4 are smooth. For all extended parameters set

    N_a(h)=W(gamma(a)+h)-W(gamma(a))-DW(gamma(a))h.

It is O(|h|^2), and so is every fixed a-derivative, uniformly on a small compact parameter interval. For a<=0 it is exactly W(gamma(a)+h)-M_a h.

Use the Banach space B of continuous h:(-infinity,0]->R2 with norm sup_(t<=0)e^(-4t)|h(t)|. For small real r solve

    h(t)=r e^(4t)e(a)
         +int_(-infinity)^t [P0(a)+e^(4(t-s))P4(a)]N_a(h(s)) ds.     (5)

On the ball ||h||<=rho, the integrand is bounded by a constant times rho^2 e^(8s) times the kernel. The P0 contribution is O(rho^2 e^(8t)); the P4 contribution is bounded by C rho^2 e^(4t)int_(-infinity)^t e^(4s)ds, again O(rho^2 e^(8t)). After multiplication by e^(-4t) this is uniformly O(rho^2). The derivative in h has norm O(rho). Taking rho small and |r| still smaller gives a uniform contraction into that ball.

The contraction map is C-infinity in (a,r,h). For its h derivative, DN_a(h)=O(rho e^(4s)), while a direction eta in B has size O(e^(4s)), so the product is O(rho e^(8s)). For m>=2 h derivatives, the product of m directions is O(e^(4ms)), with m>=2. These functions have the same integrable bounds for every fixed order. Parameter derivatives alter smooth coefficients but not the eigenvalues or exponential rates, and derivatives of N retain the quadratic zero. Differentiation under the integral, using these bounds on a small closed ball, proves the asserted Frechet smoothness. The implicit function theorem applies because I-D_h of the contraction is invertible by a norm-convergent Neumann series. Thus h_(a,r) depends smoothly on a,r.

For a<=0, differentiating (5) with respect to t gives h'=M_a h+N_a(h)=W(gamma(a)+h). The fixed point also satisfies

    h_(a,r)(t)=r e^(4t)e(a)+O(r^2 e^(8t)).              (6)

Here the O(r^2) bound follows first from ||h||<=C|r| by the contraction estimate and then by substitution in its integral. Define X(a,r)=gamma(a)+h_(a,r)(0). Uniqueness in (5) applied after a time shift gives phi_t X(a,r)=X(a,r e^(4t)) for t<=0. Therefore W(X)=4r X_r and the backward limit is gamma(a). At a=0 these are precisely the trajectories converging exponentially to p in its expanding eigendirection, giving the strong unstable germ. At r=0, X_a=tau and X_r=e, so det(X_a,X_r)=1. The smooth inverse function theorem gives the chart extension near(0,0). On a compact shortened terminal arc it gives local inverses uniformly. A sufficiently thin strip is globally injective: otherwise pairs of distinct points with radii tending to0 and equal images would have limits on the embedded arc; their labels would coincide, contradicting the local inverse there. The artificial extension can also be made at the left end of that shortened interval. Thus the asserted chart is valid on one thin tube, not merely pointwise.

Let D=det(X_a,X_r). In these coordinates W has components(0,4r). The divergence identity is

    4=D^(-1)partial_r(4rD)=4+4r D_r/D.

Thus D_r=0 for r!=0, and D(a,0)=1 plus continuity gives D=1 on the arc side. This proves(1). No C-infinity center-manifold theorem was used. The construction uses smooth parameters along an actual curve of equilibria, with constant nonzero transverse eigenvalue4.

## Proof of the equations and converse

Backward convergence and transport imply Theta(X(a,r))=Theta(gamma(a))=G(a). This follows along the actual bounded trajectories and by continuity, not from an infinite-time differentiation.

Pull back the physical velocity one-form W1 dx+W2 dy. It equals A da+B dr, with A=4r X_a.X_r and B=4r|X_r|^2. Its exterior derivative is (B_a-A_r)da wedge dr. In physical coordinates it is curl W dx wedge dy. Since the determinant is1,

    Omega=-curl W=A_r-B_a=Q,

which expands to(3). The inverse Jacobian is [[y_r,-x_r],[-y_a,x_a]], so a_x=y_r and Theta_x=G'(a)y_r. Consequently(2) is precisely

    (4r partial_r+1)Q=G'(a)y_r.                       (7)

Differentiating t y_r(a,r t^4) in t and integrating on[0,1] shows that(4) solves(7). Its integral is C-infinity in(a,r), including both signs of r and r=0, since the integrand is smooth on a compact interval. A homogeneous solution on either nonzero half-line is C(a)|r|^(-1/4); boundedness through0 kills it. Thus(4) is the unique bounded solution.

For the converse define W,Theta,Omega through the chart. The determinant gives div W=4 by the same coordinate formula. The one-form computation gives the exact curl. The coordinate a is a first integral, giving thermal transport. Formula(4) implies(7), including0 by continuity, proving vorticity transport. Every step is local and requires no inverse at infinity.

For the arclength normalization, at r=0, Q=lambda and y_r=e_y=tau_x+lambda tau_y/4. Hence the necessary interior-arc relation is

    lambda(1-G' tau_y/4)=G' tau_x.                    (8)

This identity is valid even when its prefactor vanishes; dividing by that prefactor requires an additional nonzero assumption. In particular tau=(0,1),G'=4 makes(8) compatible with every lambda.

## Exact examples, nonexamples and attachment scope

For any smooth function G, X(a,r)=(a,G(a)/4+r) has determinant1, Q=G' and y_r=1. It yields

    W=(0,4y-G(x)), Theta=G(x), Omega=G'(x).

This is an exact local solution but its zero curve continues through any proposed endpoint. It does not solve the half-arc problem.

More generally fix a constant unit tau, n=J tau, constants g,lambda satisfying(8), and e=n+lambda tau/4. The affine chart X=tau a+e r has determinant1 and Q=lambda, while Theta=ga. Equation(4) is exactly lambda=g e_y. This tests arbitrary fixed physical orientations. Rotating a solution while leaving its forcing derivative unchanged is not justified; the displayed constraint is essential.

For an arbitrary smooth area-preserving chart, the construction W(X)=4rX_r always gives divergence4 and thermal transport of G(a). Equation(4) is a further condition. It is not preserved by arbitrary area-preserving coordinate changes. For example, pushing the exact shear by(x,y)->(x,y+h(x)) gives W=(0,4y-G(x)-4h(x)), Theta=G(x), Omega=G'(x)+4h'(x), and vorticity residual4h'(x). These fields are not coupled solutions unless h is constant.

If the opposite side of the strong unstable curve is known by a separate outgoing-flow argument to have backward limit p, then Theta is constant L=Theta(p)=G(0) there. Smooth matching of Theta across the curve is equivalent to flatness of G-L at a=0, by extending G constantly across0 in the smooth chart. This is only a temperature matching statement. The opposite-side W must also satisfy the curl and vorticity equation, which force both components of W to be harmonic where Theta is constant and backward trajectories stay in a compact local neighborhood: boundedness of the smooth Omega and its homogeneous transport make Omega zero there. An arbitrary chart extension supplies none of these coupled conditions. Extending W(X)=4rX_r to a>0 would instead extend the equilibrium curve r=0, violating the desired half-arc geometry.

## Dependencies and audit scope

The proof uses elementary matrix algebra, the contraction theorem, the smooth Banach implicit function theorem, local ODE uniqueness, the inverse function theorem, and change of variables for divergence and differential forms. It supplies its own parameter estimates. There is no reliance on a C-infinity center manifold, formal power series, numerical residual as proof, or a theorem about a physical wall.

The lead's endpoint2 sections1-2 and4,6-11 also contain flat-jet, outgoing/incoming flow, harmonic Cauchy uniqueness, analytic-boundary and triangular-field arguments. These have been read and separately rederived in the verifier audit. They retain their stated extra hypotheses and do not establish the general endpoint. The present theorem isolates the new smooth chart and regular-coordinate converse; it does not use the lead's unproved general gluing or global scattering claims. Exact manufactured controls will check the coordinate identities and rejected unrestricted coordinate-change inference, with review findings recorded alongside this proof.

Written UTC 2026-10-21T13:59:58.097200+00:00, before the new controls.

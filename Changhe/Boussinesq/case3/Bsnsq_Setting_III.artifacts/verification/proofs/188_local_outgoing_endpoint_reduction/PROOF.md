# Exact local coordinates, gluing and formal jets at an outgoing endpoint

Status: CONFIRMED by independent informal proof, exact algebraic controls and actual Claude Opus5.5 reviews343/345/347, with scope objections resolved on follow-up. This is a conditional local equivalence, not a local existence theorem and not a B2 exclusion.

## Statement, notation and local premises

In physical Cartesian coordinates (x,y), let W,Theta,Omega be smooth on a neighborhood of p, satisfying

    div W=4, Omega=-curl W, curl W=partial_x W2-partial_y W1,
    W.grad Theta=0, W.grad Omega+Omega=Theta_x.                 (1)

Let the local zero set be a smooth embedded half-arc gamma(a), -delta0<=a<=0, parametrized by arclength, gamma(0)=p. Write tau=gamma', n=(-tau_y,tau_x), theta(a)=Theta(gamma(a)), lambda(a)=Omega(gamma(a)), L=theta(0). Assume the independently established B2 outgoing endpoint structure: DW(gamma(a))=(4n+lambda tau) tensor n, lambda(0)=0, and the endpoint is outgoing. We state exactly the local flow property used by that last term. A finite C4 chart puts the strong unstable curve C on u=0, the zero arc on v=0,u<=0, and the vector field in the form

    u'=g(u)+uv B(u,v), v'=v D(u,v),
    g(u)=0 for u<=0, g(u)>0 for u>0, D(u,v)>2, |B|<=M.             (2)

C is itself smooth; a smooth simultaneous center chart is not asserted. These local facts were proved in packets173,174 and177, with their outgoing consequences proved in179. Their derivations use local field equations and local endpoint isolation, not the canonical inverse or far-field decay. Below we also rederive the precise backward-basin consequence needed here. All subsequent construction uses only these stated local premises.

After shrinking delta, there is a smooth embedding X(a,r), defined on an open neighborhood of R=[-delta,0] times[-delta,delta], such that on R

    X(a,0)=gamma(a), X_r(a,0)=n(a)+lambda(a)tau(a)/4,
    det(X_a,X_r)=1, W(X(a,r))=4r X_r(a,r).                    (3)

Its a=0 curve parametrizes C near p. The scalar fields satisfy

    Theta(X(a,r))=theta(a),
    Omega(X(a,r))=(theta'(a)/4) int_0^1 u^(-3/4)y_r(a,ur)du.  (4)

Consequently the single equation for X and theta is

    4 partial_r(r X_a.X_r)-4r partial_a |X_r|^2
       =(theta'/4) int_0^1 u^(-3/4)y_r(a,ur)du.               (E)

For every sufficiently small disk D centered at p and contained in the chart domain of(2), the closure in D of the component D_- on the arc side of C equals X(R) intersect D. On the other component D_+, every point tends backward to p. In D_+, Theta=L and Omega=0, and W=grad H for a function smooth up to C, with

    Lap H=4, grad H(c(r))=4r c'(r), c(r)=X(0,r).              (5)

In particular the normal derivative of H on C is zero and

    H(c(r))=H(p)+int_0^r 4rho |c'(rho)|^2 drho.              (6)

Conversely, any smooth embedding X with determinant1 satisfying(E) defines smooth fields on the interior of X(R) by(3)-(4), and these solve(1). If X(R) intersect D is exactly the closure of one side of the embedded c, theta-L is flat at a=0, and H on the other side is smooth up to c and satisfies(5), these fields glue smoothly across c and solve(1) on D. The converse alone does not assert the prescribed zero set or outgoing type; those are additional requirements in an equivalence with an outgoing endpoint solution.

Finally, along the interior of gamma the formal Taylor coefficients in signed normal distance h are uniquely determined by gamma and theta whenever

    d_m=4m+1-tau_y theta'/(4(m+1)) !=0, m=0,1,2,... .          (7)

If |theta'|<4, all these numbers are positive. Conversely, any smooth arclength arc and smooth trace with |theta'|<4 determine formal series satisfying every coefficient of(1). Convergence, a smooth realization of these formal solutions, and compatibility with an outgoing endpoint are not asserted.

## Backward geometry and the one-sided zero fields

For backward time T in(2), |v(T)|<=|v0|exp(-2T). On u>0, choose k>M/2. Direct differentiation gives

    d/dT(log u+k|v|)=-g(u)/u-vB-kD|v|<=0.

A sufficiently small region u exp(k|v|)<epsilon, |v|<epsilon therefore stays in the chart for all backward times. With I(T)=int_0^T vB dt, |I(infinity)|<=M|v0|/2 and h(T)=u(T)exp(I(T)), one has h'=-g(u(T))exp(I(T))<0. Thus h has a nonnegative limit and, since exp(I) has a finite positive limit, u has a nonnegative limit. A positive limit would bound g(u) below by a positive number and force h to decrease at a fixed positive rate forever. Hence u tends to0 and every such point tends to p.

On u<0 the same estimates give u(T)=u0 exp(-I(T)), whose limit is strictly negative. By choosing the initial rectangle sufficiently small, these estimates also keep that orbit in a larger fixed chart. Its limit is an interior point of gamma. Points with u=0 lie on the strong curve and tend backward to p. These arguments give an entire smaller two-sided neighborhood with the asserted classification, including both signs of v. They do not need uniform convergence rates in the positive center direction.

Thermal transport and continuity now give Theta=L on the open side u>0. Hence Theta_x=0 there. Along its bounded backward trajectories, (1) gives Omega(Y)=exp(-T)Omega(phi_(-T)Y), and letting T tend to infinity yields Omega=0. All derivatives of Theta-L and Omega therefore vanish on C by smoothness. In particular theta-L is flat at a=0. This reasoning is local: the backward orbits stay in the fixed chart. No full-plane trajectory or global boundary is needed.

## Smooth endpoint-uniform construction of X

Extend gamma smoothly through a=0 and retain arclength on that extension; extend lambda smoothly as well. Put

    M=(4n+lambda tau) tensor n, P4=M/4, P0=I-P4,
    b=n+lambda tau/4.

Since n.tau=0 and |n|=1, M^2=4M, P0 and P4 are complementary projections, Mb=4b, and det(tau,b)=1. Direct expansion of the exponential series yields exp(tM)=P0+exp(4t)P4. For a<=0 the assumed derivative identity says M=DW(gamma(a)). Define for all nearby a

    N(a,h)=W(gamma(a)+h)-W(gamma(a))-DW(gamma(a))h.

Taylor's formula with integral remainder gives N=O(|h|^2), all pure a derivatives O(|h|^2), and all mixed derivatives with one h derivative O(|h|), uniformly on a small compact parameter interval. Derivatives with at least two h arguments are uniformly bounded. For a<=0, W(gamma(a))=0 and N=W(gamma(a)+h)-Mh.

Use the Banach space of continuous h(t), t<=0, with norm sup exp(-4t)|h(t)|. The integral map is

    F_(a,r)(h)(t)=r exp(4t)b(a)
       +int_(-infinity)^t [P0(a)+exp(4(t-v))P4(a)]N(a,h(v))dv. (8)

If ||h||<=R, the nonlinear source is bounded by C R^2 exp(8v). Integrating the two kernels gives respectively exp(8t)/8 and exp(8t)/4. After multiplication by exp(-4t), both are bounded uniformly for t<=0. The difference estimate has a factor C R||h1-h2||. Since lambda(0)=0, shrink the parameter interval so ||b||<3/2. For small |r|, the ball of radius2|r| is invariant and the Lipschitz constant is less than1/2. Equivalently work on a fixed small ball to include r=0. Iteration gives the unique fixed point there.

For completeness, let E_eta have norm sup exp(-eta t)|h(t)| on t<=0. The Nemytskii map h maps to N(a,h(.)) is smooth from a fixed small ball of E4 to E8, smoothly in a. The first Taylor remainder is bounded by C||k||^2 exp(8t); continuity of its first derivative follows from |(D_h N(h+k)-D_h N(h))k1|<=C||k||||k1||exp(8t). Derivatives with j>=2 h arguments contain a product bounded by exp(4jt), and pure a derivatives remain quadratic. The same Taylor estimates for every mixed derivative establish smoothness, not just bounded candidate derivatives. Each kernel in(8) is a bounded map E8 to E4, smoothly in a, by the displayed estimates. Thus F is a smooth map of parameters and h in a fixed small ball. The linearized operator in h has norm<1/2 and I-D_h F has inverse sum_(j>=0)(D_h F)^j. Differentiating the fixed-point equation determines each derivative uniquely with this bounded inverse. Taylor remainders in the smooth map give the inductive differentiability justification, not just formal differentiated equations. Hence the fixed point is C-infinity in(a,r).

Set X(a,r)=gamma(a)+h(a,r,0). At r=0 the fixed point is zero and its r derivative is exp(4t)b, giving X_r(a,0)=b. For a<=0, differentiating(8) in t gives h'=Mh+N=W(gamma+h); this differentiation is justified by the displayed exponential integrable bounds. Shifting time by t'<=0 in(8) gives the same integral equation with parameter exp(4t')r. Uniqueness implies

    h(a,r,t+t')=h(a,exp(4t')r,t),
    phi_t X(a,r)=X(a,exp(4t)r), t<=0.

Differentiating at t=0 gives W composed with X=4r X_r. The determinant of DX at (0,0) is1, so the inverse function theorem gives an injective smooth X on a small open parameter neighborhood; choose R inside it. On the arc side its Jacobian J satisfies

    div W composed with X=J^(-1)partial_r(4rJ)=4+4r J_r/J.

For r!=0, J_r=0, and by smoothness this also holds at0. Since J(a,0)=det(tau,b)=1, J=1 on all R. The a=0 curve is invariant, tangent to n at p, and has exponential backward convergence. Uniqueness of the local strong unstable manifold identifies its local germ with C. Throughout this statement C means that local germ; the disk is shrunk so no returning remote piece of a global strong curve is included.

## Exact scalar formulas and the curl equation

By the negative-time identity every X(a,r) tends to gamma(a) backward, so thermal transport and continuity imply the first formula(4). The inverse of the two by two derivative matrix has a_x=y_r/J=y_r. Thus Theta_x composed with X=theta' y_r. With omega=Omega composed with X, the vorticity equation becomes

    4r omega_r+omega=theta' y_r.                              (9)

Multiplying the equation along r exp(4t) by exp(t), integrating from minus infinity to0, and using boundedness gives (4) after u=exp(4t). The discarded homogeneous term is a multiple of |r|^(-1/4) on each side and cannot be bounded. At r=0, differentiating under the integral in(4) is valid to every order because u^(-3/4+j) is integrable for j>=0, so the formula is smooth through r=0 and solves(9) there too.

The pullback of the velocity one-form W1 dx+W2 dy is

    4r(X_a.X_r) da+4r|X_r|^2 dr.

Its exterior derivative is [4r partial_a|X_r|^2-4 partial_r(r X_a.X_r)] da wedge dr. Since dx wedge dy=da wedge dr, this coefficient is curl W composed with X. The convention Omega=-curl W proves(E), including its sign. Conversely a smooth determinant-one embedding and(E) imply div W=4 by the same Jacobian formula, thermal transport by independence of r, the vorticity transport equation by differentiating(4), and the curl relation by the one-form calculation. No extra equation remains in this converse.

The local side identification also follows topologically from X. Its extension is a diffeomorphism across a=0; its image of a=0 is C, and its negative-a image contains the negative zero arc. Choose an open parameter neighborhood V of(0,0) such that X is injective on a neighborhood of R union V, with V inside (-delta,delta)^2. Choose D contained in X(V) and in the smaller normal-form neighborhood. On X(V) let A be the first inverse coordinate. Then X(R) intersect D={A<=0} intersect D, because the other three boundaries of R have no preimages in V. The two components {A<0} and {A>0} in D are separated by the local curve C. The negative component contains the negative zero arc, so it agrees with the negative component of the normal-form chart. Thus X(R) intersect D is precisely the relative closure of that side of C in D. A sufficiently small disk meets a smooth embedded curve through its center transversely at two boundary points and in one arc: write the curve as a graph over its tangent and use the positive derivative of the squared distance away from the center. Its two sides are simply connected. The backward classification established above identifies the other side as D_+. This avoids extrapolating X's actual-flow identity to the artificial a>0 extension.

## Potential and smooth gluing

On D_+, curl W=0. Path integration on this simply connected domain produces H with grad H=W; its divergence gives Lap H=4. Locally up to each point of C, use a graph chart and integrate the smooth closed one-form from a boundary basepoint along tangential and then transverse paths. This constructs a smooth potential up to C with the same gradient on D_+, differing from H by a constant. The local extensions agree after adjusting that constant, so H is smooth up to the full relative boundary. Invariance of C gives its zero normal derivative. Equation(3) gives(5), and the ordinary chain rule integrated in r gives(6), including negative r with the oriented integral.

For the converse, flatness of theta-L at a=0 implies all mixed derivatives of theta(a)-L vanish there. The integral factor in(4) is smooth, so Omega is likewise flat on a=0. An invertible smooth coordinate change preserves ambient flat jets. Thus Theta and Omega match the constant and zero fields on the other side to every order. The vector values match by(5).

To show matching derivatives of W, fix an arclength chart on c and one choice of unit normal shared by both sides. Write W=P tau+Q n and J=1-kappa h. Direct differentiation gives

    div W=P_a/J+Q_h-kappa Q/J,
    -curl W=P_h-(Q_a+kappa P)/J.                             (10)

The first identity determines Q_h and the second determines P_h from the two tangential derivatives, values, divergence and curl. At h=0, these data agree on the two sides. Differentiating(10) m times in h expresses the next two normal derivatives through already matching derivatives and derivatives of divergence and curl. Divergence is identically4 and every curl jet is zero on c, so induction proves equality of all jets of W. Smooth functions on two sides of a smooth hypersurface with equal jets glue smoothly: in a flattened chart, induction with the fundamental theorem of calculus shows each one-sided derivative is the derivative of the glued lower derivative. All equations extend to c by continuity. This proves the claimed converse, without solving the overdetermined boundary problem(5).

## Formal normal recursion, with the physical x direction retained

Use Y(a,h)=gamma(a)+h n(a), tau'=kappa n. Then Y_a=J tau, Y_h=n. With W=P tau+Q n, formulas(10) hold and

    W.grad=(P/J)partial_a+Q partial_h,
    Theta_x=(tau_x/J)Theta_a+n_x Theta_h, n_x=-tau_y.          (11)

Let P_j,Q_j,T_j,O_j denote coefficients of h^j, not normal derivatives without factorials. Set P0=Q0=0 and T0=theta. The h^0 divergence equation yields Q1=4. Suppose P_j,Q_j,T_j for j<=m and O_j for j<m have been determined. The h^m divergence equation determines Q_(m+1) from known coefficients. The h^m curl relation gives

    P_(m+1)=O_m/(m+1)+known terms.

The h^(m+1) thermal equation gives

    4(m+1)T_(m+1)=-theta' P_(m+1)+known terms.

All other coefficients involved are known after the divergence step; for m=0 the two displayed unknown terms already include the complete leading equation, so no term is double counted. The h^m vorticity equation is

    (4m+1)O_m-n_x(m+1)T_(m+1)=known terms.

Here Q1 m O_m=4m O_m is the only new transport term, because P0=Q0=0. Substitution gives exactly d_m O_m=known terms, with d_m as in(7). Thus O_m, P_(m+1), T_(m+1) are determined. At m=0 this recovers

    lambda(1-tau_y theta'/4)=tau_x theta'.                    (12)

There is no additional arc constraint hidden in the recursion: (12) defines lambda when d0!=0. Each coefficient of divergence, curl and vorticity is used at step m; each positive-order thermal coefficient at step m uses h^(m+1), while its zeroth coefficient is identically zero. This accounts for all equations and proves formal solvability as well as uniqueness. If |theta'|<4 and |tau_y|<=1, then

    d_m>4m+1-1/(m+1)>=0.

The strict first inequality covers m=0. Smoothness of all coefficients follows inductively from differentiation and division by nonvanishing smooth d_m. This is a formal statement on the interior arc. Neither a convergent sum nor a smooth solution satisfying the equations follows from formal coefficients alone.

## Locality, nonanalyticity and scope of the equivalence

The outgoing side argument shows theta-L is flat at the endpoint. It cannot be identically zero on a terminal interval of gamma. Otherwise shrink the rectangle to a in[-epsilon,0] and shrink D so its negative-side relative closure is covered by that rectangle. Formula(4) then makes Theta=L and Omega=0 on the entire negative side of D; with the basin side this yields a whole neighborhood of p with curl W=0. Constant divergence then makes W harmonic and real analytic. Its normal component has a regular zero graph by its derivative4, and its tangential component restricted to that graph vanishes on the negative half-interval, hence also the positive half by the analytic identity theorem. This contradicts the zero arc ending at p. This is the local content of179 and the lead's4.7(xii); it uses no whole-plane inverse.

Nor can C agree with a regular real analytic curve germ (embedded, with nonzero tangent) at p. The local analytic-boundary argument of packet53, with its local harmonic consequences also re-audited in174 and179, applies to the irrotational outgoing side and its zero normal velocity. One can see the mechanism by an analytic conformal chart flattening the curve: Lap H=4 becomes a Poisson equation with analytic right side and zero normal derivative. An analytic local particular solution with zero normal derivative, constructed by the noncharacteristic power-series recursion, reduces it to a harmonic function with homogeneous Neumann data. Even reflection extends this harmonically, so W from the basin side has an analytic extension through C with the same full jet as the original W at p. The analytic implicit nullcline and the actual zero arc have the same formal jet at p. The analytic tangential restriction is therefore flat and vanishes identically. Its extended zero curve passes into the outgoing basin side, where the extension equals W, contradicting local absence of exterior zeros. This argument uses analytic-boundary reflection only conditionally; no smooth boundary is treated as analytic.

Equations(E),(5), determinant1, flat trace and side coverage, together with the extra outgoing endpoint requirement, are necessary and sufficient local data in exactly the stated sense. That extra requirement means the glued field has exactly the stated local negative zero half-arc and the finite regularity normal form(2), with the chart oriented so its u>0 side is exactly the glued H-side D_+, g(u)>0 for u>0 and D(u,v)>2. This is a local existential chart condition; every backward orbit starting in D_+ intersect U, for U a sufficiently small neighborhood of p, stays in that fixed chart and tends to p. The geometric zero set alone does not specify the outgoing sign. Neither this sign nor the zero set is implied by(E) and(5). They are still a coupled boundary problem. Formal solvability along the interior does not solve that problem or prescribe arbitrary endpoint data. No local example at a flat outgoing endpoint and no obstruction to all such examples has been obtained. A local obstruction would exclude the corresponding outgoing-endpoint subclass; a local example would not provide a canonical full-plane B2 profile, the required central x² jet, or admissible far-field behavior. The broad beta-two and beta-greater-than-two B2 questions remain OPEN.

Dependencies: the explicitly stated local endpoint normal form(2) and derivative identity from173/174/177; the elementary backward estimates rederived here; contraction and inverse function arguments with uniform estimates; elementary planar one-form integration; analytic uniqueness and analytic-boundary reflection for the final nonanalyticity corollary as audited in53/174. Formal sources and exact controls belong in the named neighboring subfolders. No Lean or Lake build is claimed or run.

Written UTC 2026-10-21T17:32:48.931208+00:00, before the new controls.

## Verification evidence

Published UTC 2026-10-21T17:55:22.934306+00:00. The complete initial proof was written2026-10-21T17:32:48.931208Z, before the controls. The original hash and subsequent revisions are retained. The verifier's own checker completed792 exact algebra controls and9 algebraic hypothesis counterchecks in1.842453607s at2026-10-21T17:35:28.651001+00:00. These test rank-one algebra, a curved physical area chart, the integral ODE coefficients for both signs of r, formal multipliers and their curvature recursion, and explicit convention failures. They are finite controls, not a proof of the Banach-space argument, smooth gluing or analytic uniqueness. The manufactured field X=(a,r+f(a)), theta=4f satisfies the displayed local equations but has an entire equilibrium arc. It is deliberately not an outgoing-endpoint example or a B2 profile. The nine counterchecks are algebraic comparisons, not nine executions of corrupted certificate inputs.

Review343 requested us.anthropic.claude-opus-5-5 and returned claude-opus-5-5; it supplied a substantive partial written audit before a max_tokens stop. Its mathematical comments led to explicit E4-to-E8 Taylor remainders, injective inverse-coordinate side coverage, the local strong-curve germ qualification, and the smaller terminal disk. The partial review is not presented as a completed audit. Complete written follow-ups345 and347 use the same actual model through Python Bedrock. They check the repaired proof and the exact outgoing hypothesis. We rejected345's proposed equivalence to unrestricted backward convergence because an orbit could leave and later return to the local chart. Review347 accepts this counterargument. The final definition is the oriented local normal-form condition; chart-staying backward convergence is its proved consequence. The coefficient vB can change the instantaneous sign of u', so neither347's incidental monotonicity sentence nor monotonicity of u alone is used. The proof instead uses u exp(I) and the invariant weighted region.

The final statement places D inside the chart, specifies D(u,v)>2, identifies u>0 with the H-side, and restricts the analytic exclusion to a regular embedded analytic curve germ. Lead draft xviii v2 is mathematically consistent with this reduction; its final presentation should retain the H-side orientation and analytic image-germ language. This is a draft comparison, not approval of an uninspected later report entry. All endpoint geometry dependencies retain their own earlier evidence. No formal build, local construction, full-plane inverse construction or decisive B2 endpoint is claimed.

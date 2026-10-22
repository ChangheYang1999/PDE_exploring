# Constant endpoint subarcs: independent restricted results

## Statement, hypotheses and scope

Work at beta=2 with smooth real fields on the plane satisfying

 div W=4, Omega=-curl W, W.grad Theta=0,
 W.grad Omega+Omega=partial_x Theta,
 W(X)=2X+U(X)-U(0), U(X)=o(|X|).

The little-o is uniform in direction. A local result below omits the last growth assumption and explicitly supplies its replacement. Let gamma be an embedded arc of zeros of W, let p be its endpoint, and suppose its local zero segment does not extend through p. Assume Theta=L on a terminal subarc. Coordinates (s,z) are positively oriented orthonormal coordinates at p, with the s direction tangent to gamma, pointing out of the arc. This rotation is used for the kinematic and harmonic calculations only. The triangular result separately requires s=x in the physical forcing derivative.

The following conclusions hold.

1. A terminal isothermal subarc produces an open isothermal region on its side of the strong unstable curve. Its invariant saturation is irrotational in a global profile. No full neighborhood of an endpoint can be isothermal.
2. At an incoming endpoint, a transverse section of the exterior center orbit carries a smooth trace b with b(0)=L. Nearby temperature values are exactly b evaluated at backward exit heights. If any point of that center orbit has an isothermal neighborhood, the terminal isothermal subarc is impossible.
3. At an accumulating endpoint, every neighborhood of p must contain an exterior zero-arc interval on which Theta is nonconstant. In particular, making Theta constant on each exterior zero-arc interval, even with different constants, excludes the terminal isothermal subarc.
4. A global profile has no open straight isothermal segment of zeros.
5. There is no smooth local solution of the displayed differential equations in the triangular form W=(f(s),(4-f'(s))z), with s=x, f=0 for s<=0, f<0 for s>0, and Theta=L for s<=0.

The reflection construction on the isothermal side does not extend its holomorphic identity to the other side. None of these statements excludes all smooth profiles of the prompt. The remaining general incoming and accumulating configurations stay OPEN.

The independently frozen source is verification/frozen_sources/subarc1_PROOF.md, sections 1-7. The proofs below are a separate derivation. They use the exact local chart and its construction spelled out next, rather than a global classification of backward limit sets.

## The endpoint chart

Along the zero arc, DW has a zero tangent eigenvector and trace 4. Initially diagonalize DW(p) with eigenvalues 0 and 4. If the first nonzero homogeneous term of Theta-L is P_m, transport gives 4b partial_b P_m=0, so P_m=c a^m. On the normal nullcline b=h(a)=O(a^2), partial_a Theta is mc a^(m-1)+o(|a|^(m-1)), nonzero for small nonzero a. The other component of W must then vanish on that nullcline by transport, extending the zero arc. This contradicts the endpoint assumption. Hence Theta-L is flat. The vorticity equation implies Omega(p)=0, and its first possible homogeneous term Q would satisfy (4b partial_b+1)Q=0. On every monomial its multiplier is 4j+1>0, so Omega is flat as well. In particular DW(p) is symmetric and is 4n tensor n in the orthonormal coordinates.

The normal nullcline is z=k(s), with k(0)=k'(0)=0. Smooth division gives

 W_s=f(s)+c_1(s,t)t, W_z=c_2(s,t)t, t=z-k(s), c_2(0)=4,

where f=0 on s<=0 and f is flat at zero. There is a local C^3 coordinate system satisfying

 u'=g(u)+uv c(u,v), v'=v d(u,v), d>2,

with c bounded, g=0 on u<=0, the center graph v=0 containing all nearby zeros, and the strong unstable curve C given by u=0. The sign and zeros of g agree with those of f. Here is sufficient construction detail to check this input.

Write W(h)=(0,4h_2)+F(h), F(0)=DF(0)=0, and cut F off in a small ball. Its global Lipschitz constant ell can be made small. For t>=0 solve

 h_1(t)=a+integral_0^t F_1(h(r))dr,
 h_2(t)=-integral_t^infty exp(4(t-r))F_2(h(r))dr.

In norm sup exp(-eta t)|h(t)| the difference operator has norm at most ell(1/eta+1/(4-eta)). Choose eta=1/8 and ell small enough for all five weights j eta. The contraction gives a graph h_2(0)=h_c(a). Differentiating up to order four solves the same contraction operator in progressively larger weights: at order j, products of lower derivatives grow at most exp(j eta t), and bounded cutoff derivatives suffice. Difference quotients on finite intervals followed by a larger weight on the tails justify continuity of these derivatives. Thus the graph is C^4 and h_c'(0)=0. Time translation makes it invariant, and every small equilibrium gives a constant solution and lies on it.

For t<=0 the strong curve is the solution of

 h_1(t)=integral_-infty^t F_1(h(r))dr,
 h_2(t)=b exp(4t)+integral_-infty^t exp(4(t-r))F_2(h(r))dr.

On the ball |h(t)|<=C|b|exp(4t), the quadratic bound on F gives integrands of size O(b^2 exp(8t)) and contraction constant O(|b|). Differentiation in b gives a smooth curve, tangent to the z axis, with backward limit p. Uniqueness gives its invariance.

Straighten the center graph by a=s,b=z-h_c(s). The strong curve is a=eta_0(b), eta_0(0)=eta_0'(0)=0; take u=a-eta_0(b),v=b. The vector field is at least C^2. Its second component vanishes on v=0, and the first component minus its restriction to v=0 vanishes on both axes. Single and double smooth division give the asserted form and bounded c. On the center graph the original invariance equation gives

 (c_2-h_c'c_1)(h_c-k)=h_c'f,
 g=c_2 f/(c_2-h_c'c_1).

The denominator is positive near p. On v=0 we have u=s, so the sign statement is literal. All zeros have v=0 because d>2. This construction needs only finite regularity for the arguments below.

## Isothermal saturation and the endpoint obstruction

In backward time tau, |v(tau)|<=|v(0)|exp(-2tau). On u<0, g=0, so

 |log(|u(tau)|/|u(0)|)|<=||c||_infty |v(0)|/2.

Starting in a smaller rectangle leaves a strict margin to all edges. The estimates therefore persist for all backward time. The integral of vc converges, hence u(tau) tends to a strictly negative value and v(tau) tends to zero. On C the limit is p. Continuity and transport give Theta=L on a smaller closed negative half-neighborhood, whose negative interior is open.

For the global profile, W has at most linear growth, so its smooth flow is complete. At sufficiently large radius W(X).X>=|X|^2. Therefore every backward orbit is bounded, and a sufficiently large closed disk is backward invariant. If D is open and Theta=L on D, its saturation V=union_t phi_t(D) is open and invariant, with Theta=L. The vorticity equation on V gives Omega(Y)=exp(-T)Omega(phi_-T(Y)). Continuity on the bounded backward orbit forces Omega(Y)=0. The divergence and curl identities then make both components of W harmonic.

If a full neighborhood of p were isothermal, W would be harmonic and real analytic there. Its analytic normal nullcline exists since partial_z W_z(p)=4. The restriction of W_s to that nullcline is analytic and zero on a segment ending at p, so the one-variable identity theorem extends its zeros through p. This contradicts the endpoint assumption. On a smaller negative half-neighborhood harmonicity also follows locally from the backward bounds already proved; the global assumption is needed for the full invariant saturation and the unrestricted endpoint-neighborhood obstruction.

## Incoming endpoints

Suppose g<0 on 0<u<=u_0. Choose delta>0 so that the backward field is strictly outward at u=u_0, |v|<=delta. In backward time put A(t)=integral_0^t vc and w=u exp(A). While 0<u<u_0,

 |A(t)|<=||c||_infty |v(0)|/2, w'=-g(u)exp(A)>0.

An orbit cannot remain in this strip forever: A converges; the positive increasing bounded w would have a positive limit; u would therefore tend to u_*>0, where -g is strictly positive, forcing w' to stay positive. Thus the orbit exits at u=u_0. If M bounds |g(u)/u|+delta||c||, then

 T_exit >= log(u_0/u(0))/M,
 |v_exit| <= |v(0)|(u(0)/u_0)^(2/M).

Transversality gives a smooth exit map for u>0. The exterior center orbit has forward limit p, so b(eta)=Theta(u_0,eta) satisfies b(0)=L. Transport gives exactly Theta(Y)=b(v_exit(Y)). If b equals L on a neighborhood of zero, this produces an isothermal positive half-neighborhood. The negative half-neighborhood proved above completes a full isothermal neighborhood, a contradiction in the global case. A neighborhood of any point on the same center orbit can be transported by a finite flow time to supply such a constant b.

For the stated sufficient condition involving an interior isothermal zero arc, choose local coordinates (a,b) with that arc b=0. Division gives a'=bA,b'=bD, with D>0. Backward time contracts b exponentially and changes a by at most ||A|| |b(0)|/inf D. A tube above a shorter subarc therefore converges backward to that subarc and is isothermal. If the exterior center orbit has a backward limit at an interior point there, it eventually enters that tube. This proves the restricted incoming exclusion without assuming continuity of backward limit sets for nearby initial points.

## Accumulating zeros

Let u_1>0 be a nearby zero of g, with |g'(u_1)|<1. At q_1=(u_1,0), the eigenvalues are lambda=g'(u_1) and mu=4-lambda>3. The physical trace is 4 at an equilibrium and is unchanged by a smooth change of coordinates. In physical coordinates, the same strong-curve contraction with spectral kernels exp(lambda(t-r)) and exp(mu(t-r)) converges since 2mu-lambda>0 and mu>0. It gives a strong unstable curve which in the (u,v) chart is u=sigma_1(v), sigma_1(0)=u_1. Its tangent has nonzero v component. Shrink its width until 0<sigma_1(v)<2u_1.

The region R={0<u<sigma_1(v), |v|<h} is backward invariant. Its two lateral boundaries are invariant curves and its top and bottom boundaries point inward. It contains a rectangle 0<u<m, |v|<h, with m>0. It can be placed in any prescribed neighborhood of p by taking u_1 and h small.

For a backward orbit in its compact closure,

 u'=-g(u)+r(t), |r(t)|<=C exp(-2t), v(t)->0.

Every limit value a of u is a zero of g. Otherwise choose an interval on which -g has a fixed sign bounded away from zero. For all large times the derivative has that sign whenever u is in the interval. A visit must leave in that direction, and a return would require an opposite crossing, which is impossible. The limit values of a bounded continuous real trajectory form [liminf u,limsup u]. If these endpoints differ, take a smaller [a,b] inside them. All of it consists of zeros of g. Arbitrarily late traversals between a and b have displacement at most integral_T^infty |r(t)|dt, which tends to zero. This contradicts b-a>0. Consequently every backward orbit in R converges to a single zero (u_*,0), even when the zero set contains intervals.

Set theta(u)=Theta(u,0). Then Theta(Y)=theta(u_*(Y)), and g theta'=0. If theta=L on a right neighborhood of zero, choose R with 2u_1 inside it. It and the negative half-neighborhood give a full isothermal neighborhood, impossible. Thus theta is nonconstant in every right neighborhood. The mean-value theorem gives arbitrarily small u>0 with theta'(u) nonzero. Continuity makes theta' nonzero on an interval there, so g vanishes on that interval. These are exterior zero arcs with nonconstant Theta.

Conversely, if Theta is constant on each zero-arc interval in some right neighborhood, a nonzero theta' anywhere would produce a forbidden nonconstant zero interval. Therefore theta'=0 everywhere in that neighborhood, and theta=L. This proves the exclusion even if the constants on different zero intervals were not initially identified. The local version follows if the displayed equations hold locally: the backward traps on the right and the estimates on the left keep the relevant backward orbits in the isothermal neighborhood, proving Omega=0 there without a global growth assumption. The same analytic continuation contradiction then applies.

## Straight zero segments

An interior portion of an isothermal zero segment has an open isothermal tube by the argument above. Its connected component V_0 in the interior of {Theta=L} is invariant: every finite flow time preserves the interior, and the continuous orbit cannot leave its connected component. On V_0, Omega=0 by global backward boundedness. In oriented orthonormal coordinates with the segment on z=0, define

 K=W_s-iW_z+4iz.

Direct differentiation gives partial_bar_w K=i Omega/2, so K is holomorphic on V_0. It is zero on the straight zero segment. The identity theorem gives K=0 on V_0, hence W=(0,4z) there. Choose a point with z_0 nonzero in this open set. Its entire orbit is (s_0,z_0 exp(4t)) and stays in V_0. In physical coordinates, W=2X+U-U(0) then implies |U|/|X|->2 along this orbit, contradicting sublinearity. This is a global restricted theorem.

## The triangular ansatz

Here require the physical forcing direction to be s=x. Suppose W=(f,(4-f')z), f=0 on s<=0, f<0 on s>0, and Theta=L on s<=0. Then Omega=f''z and the vorticity equation gives

 Theta_s=[f f'''+(5-f')f'']z.

Integrating from s=0 and using flatness of f gives Theta=L+A(s)z with A=f f''+5f'-(f')^2. Its derivative is exactly the preceding coefficient. Temperature transport gives fA'+(4-f')A=0.

A positive center orbit s'=f(s) stays positive for all forward time and tends to zero. Uniqueness prevents a finite-time hit, and f<0 excludes a positive limiting value. Along it put q=f'(s). Then

 q'=A-5q+q^2, A'=(q-4)A.

Both q and A tend to zero. Once |q|<=1/2, |A(t)|<=C exp(-7t/2), after shifting the initial time. Variation of constants in q'=(-5+q)q+A, with -5+q<=-9/2, gives |q(t)|<=C' exp(-7t/2). Thus q is integrable. But d f(s(t))/dt=q(t)f(s(t)), so f(s(t)) has a nonzero negative limit, contradicting f(0)=0. This excludes exactly the stated ansatz; rotating the forcing direction without changing Theta_x is not allowed.

## Reflection and a counterexample to extending its domain

In the orthonormal endpoint coordinates let w=s+iz, K=W_s-iW_z+4iz, S=w-K/2, R=conjugate(S). Then partial_bar_w K=i Omega/2 and W_s+iW_z=2(w-R(w)). On the negative harmonic side, R is antiholomorphic and R(w)=conjugate(w)+O(|w|^2). If C is s=sigma(z), choose constants m_1,m_2 so |R(w)-conjugate(w)|<=m_1|w|^2, |sigma(z)|<=m_2 z^2, |R(w)|<=2|w|. For sufficiently large M>m_1+4m_2, the disk D={Re w<-M|w|^2} and its R-image lie in that side. Thus E=R composed R-id is holomorphic on D. It vanishes on an interior negative zero-arc segment and therefore on D. This does not assert R(D) is contained in D; containment in the harmonic side is enough for composition.

On the positive normal nullcline kappa(s)=s+ik(s), R(kappa)=kappa-f/2. The real fundamental theorem of calculus yields

 E(kappa)=-f/2 [1+integral_0^1 partial_s R(kappa-t f/2)dt]=-f(1+O(s)).

These positive points are outside D and on the other side of C. No identity theorem is available there. Explicitly let f=-exp(-1/s^2) for s>0 and f=0 otherwise, and set W=(f,(4-f')z), Theta=L, Omega=f''z. These smooth local fields satisfy divergence, curl and temperature transport. On the negative side R=conjugation, E=0. On the positive real axis E(s)=-[f(s)+f(s-f(s)/2)]/2 is nonzero. Their vorticity residual is [f f'''+(5-f')f'']z, asymptotic to 5f''z, so they are not a full local solution. The triangular theorem proves that adjusting smooth Theta with the same left trace cannot repair them while retaining W.

There is no numerical existence claim or formal proof in this packet. Numerical and symbolic controls, if performed after this proof, test computations and transcription only.

## Supplemental scalar convergence lemma with integrable forcing

Let I be a compact real interval, g:I->R continuous, u:[0,infinity)->I locally absolutely continuous, and r in L1(0,infinity). Suppose u'=-g(u)+r almost everywhere. Then u(t) converges to a single zero of g. No uniqueness of the scalar equation, isolated-zero hypothesis or pointwise decay of r is needed.

Choose a C1 primitive H of g on I. The chain rule on every compact time interval gives

 integral_0^T g(u(t))^2 dt = H(u(0))-H(u(T))+integral_0^T g(u(t))r(t)dt.

The right side is bounded above uniformly in T by 2 max_I|H|+max_I|g| times ||r||_1. Thus g(u)^2 is integrable. For s<t,

 |u(t)-u(s)| <= max_I|g| |t-s|+integral_s^t |r|.

Absolute continuity of the Lebesgue integral of |r| makes the second term uniformly small on intervals of small length. Hence u is uniformly continuous. Since g^2 is uniformly continuous on I, g(u)^2 is uniformly continuous. If this nonnegative function did not tend to zero, there would be arbitrarily late values above a fixed epsilon. Uniform continuity would give intervals of one fixed positive length on which it is above epsilon/2. Choose an infinite disjoint subfamily; their integrals contradict integrability. Thus g(u(t)) tends to zero.

The cluster set of a bounded continuous real function is exactly [liminf u,limsup u]: every strict intermediate value is attained at arbitrarily late times, and the endpoints are cluster values by boundedness. Continuity of g shows that this interval consists entirely of zeros of g. If its length were positive, fix c<d in its interior. After any time T choose a time with u<c, then the first subsequent time s with u(s)=d, and the last time a before s with u(a)=c. Existence follows from the definitions of liminf and limsup and continuity. On [a,s] the function stays in [c,d]. Thus g(u)=0 there and

 d-c=integral_a^s r <= integral_T^infinity |r|.

Sending T to infinity gives a contradiction. The cluster interval is a singleton and its member is a zero of g. This proves the claim and contains the exponentially forced case used above. It corrects an auxiliary model remark: integrability alone does not imply pointwise decay of r.

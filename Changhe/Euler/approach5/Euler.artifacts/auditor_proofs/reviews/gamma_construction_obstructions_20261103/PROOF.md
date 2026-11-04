# Construction-specific obstructions for a transported field with zeros

## 1. Exact setting and review scope

Let 0<c<1/2, d=3c, kappa=1+c and delta=kappa-d=1-2c>0. On the domains specified below let X,W be smooth real vector fields, with

    div X=-d, div W=0, [X,W]=kappa W.

Write B=-X and Psi_t for the X-flow. Only times for which that flow exists are used; bounded orbits in an open domain are continued only if they stay in a compact subset of that domain. No equality W=curl U or Euler pressure equation is assumed. Consequently these are kinematic statements and cannot alone establish a profile theorem.

The claims checked are the expanding covector identity, the limitation of multiplying a nonvanishing model by a scalar, the global triangular obstruction, and the smooth-fiber return and monomial obstructions. The source answer also discusses convergence to equilibria and regular hyperbolic sets. Those topics have their separate previously audited proofs A058 and A267; this review does not replace those proofs or infer a new general exclusion from them.

The entire source answer and its complete symbolic checker/output were read. The checker confirms three algebraic identities but does not prove the dynamical conclusions. Those conclusions are reconstructed below. No computation is necessary. The exact source hashes are in the team records.

## 2. Covector expansion and the nonparallel condition

Let vol be Euclidean volume, alpha=i_W vol and beta=i_X alpha. With the usual orientation beta=(B cross W) dot dy. Cartan's identity and the divergence/bracket assumptions imply

    d alpha=0,
    Lie_X alpha=i_[X,W] vol+i_W Lie_X vol=delta alpha,
    d beta=delta alpha,
    Lie_X beta=delta beta.

Thus curl(B cross W)=delta W and

    Psi_t^* beta=e^(delta t) beta.

For a point a with beta(a)!=0, the covector identity and the operator norm inequality give

    |D Psi_t(a)| >= e^(delta t)|beta(a)|/|beta(Psi_t a)|.

The denominator cannot vanish at a finite flow time, by the same pullback identity.

Suppose the positive X-orbit of a is precompact, W(a)!=0, and its limit set contains no zero of B. Then B(a)!=0 and beta(a)!=0. Indeed, if B(a)=0 the orbit is a stationary zero of B, contrary to that limit-set assumption. If beta(a)=0, write W(a)=q B(a) with q!=0. The bracket transport equation is

    W(Psi_t a)=e^(kappa t)D Psi_t(a)W(a),

whereas the vector field B is preserved by its flow. Hence W(Psi_t a)=q e^(kappa t)B(Psi_t a). Precompactness bounds W, and the nonzero-limit-field condition bounds |B| below at all sufficiently late times. This is a contradiction.

If W tends to zero along a subsequence, the denominator in the norm lower bound may give an unbounded additional factor. No strictly larger Lyapunov exponent follows unless an exponential rate for that factor is supplied.

## 3. A scalar multiplier cannot create a zero on a nonvanishing limit set

Suppose W0 satisfies the same divergence and bracket equations and let W=fW0 for a smooth scalar f. The product identities give

    [X,fW0]-kappa fW0=(Xf)W0,
    div(fW0)=W0 dot grad f.

Where W0!=0, the same equations for W require Xf=0 and W0 dot grad f=0. A trajectory starting with W0!=0 never reaches a zero of W0 in finite time, by the invertible linear transport. Therefore f is constant along that entire trajectory.

Let its limit set be compact and suppose W0 has no zero there. If f(a)W0(a)!=0, then f(a)!=0 and every limit point p satisfies W(p)=f(a)W0(p)!=0 by continuity. Multiplying by f cannot convert this orbit into one whose limit set meets zeros of W. This conclusion uses nonvanishing of W0 on the limit set; it does not apply when W0 already degenerates there.

## 4. The global triangular obstruction and its measure quantifiers

Suppose now the fields are defined globally on R2 times R in the Euclidean product coordinates (q,z), with

    X(q,z)=(F(q),H(q,z)), W(q,z)=w(q) partial_z.

The divergence equation gives partial_z H=-d-div F. The vertical bracket equation then gives

    F dot grad w-w partial_z H=kappa w,
    div(wF)=delta w.

For the planar flow phi_t of F, its positive Jacobian J_t satisfies J_t'=div F(phi_t)J_t. The scalar equation along the same flow gives

    |w(phi_t q)| J_t(q)=e^(delta t)|w(q)|.

The sign of a nonzero w is preserved along every finite orbit segment. Let E be a measurable set of planar initial points with w!=0 whose positive trajectories stay in a fixed compact planar set K. If E has positive area, then integral_E |w|>0, while injectivity and change of variables give

    e^(delta t) integral_E |w|
       =integral_phi_t(E)|w| <= integral_K |w|<infinity.

This is impossible as t tends to infinity. For a set of bounded trajectories without a common compact K, take the countable union according to an integer radius bounding the whole positive trajectory. Each such set has zero area, so their union has zero area.

Every bounded three-dimensional trajectory projects to such a bounded planar trajectory. The full set of bounded trajectories with W!=0 is consequently contained in a planar null set times R and has zero three-dimensional volume, by Fubini and a countable union of finite z intervals. The global product representation is essential. Merely straightening W in local charts gives no global planar flow or weighted-area comparison.

## 5. A smooth-fiber return cannot approach its limiting cycle

Let Sigma be a smooth section transverse to X, with smooth coordinates (r,z) extending to r=0, and let

    W|Sigma=w(r,z) partial_z, w(r,z)!=0 for r>0.

Assume the positive-time return P(y)=Psi_tau(y)y is smooth on the side r>0, maps that side to itself and has return time tau(y)>0. The limiting return sends r towards0 as r decreases to0. The section and fields extend smoothly so that beta|Sigma is continuous at r=0. These extension and return assumptions are part of this claim.

Since W is tangent to Sigma, alpha|Sigma=0. Thus beta|Sigma is closed and annihilates partial_z, and so beta|Sigma=h(r)dr. On the connected side r>0, h is nonzero: W is nonzero and X is transverse, hence their cross product is a nonzero covector on the section. Its sign is constant there.

The variable-time term in DP is parallel to X, which beta annihilates. Consequently

    P^*(beta|Sigma)=e^(delta tau)beta|Sigma.

Also DP maps W to a positive scalar multiple of W: the fixed-time derivative does so by bracket transport, and the variable-time term must vanish because both W at the return and DPW are tangent to Sigma, whereas X is transverse. Thus P preserves the connected fiber leaves and has the form P(r,z)=(f(r),g(r,z)). It follows that

    h(f(r)) f'(r)=e^(delta tau(r,z))h(r).

The finite coordinate s=H(r)=integral_0^r |h(u)|du is strictly increasing, even if h is flat at0. The induced one-dimensional map F=H f H^(-1) extends with F(0)=0 and satisfies F'(s)=e^(delta tau)>1 for s>0. Hence F(s)>s for all s>0: the function F(s)-s is strictly increasing with limit0 at the origin. In particular no positive orbit remaining in the return domain can converge to0. If tau>=tau0>0, the stronger inequality F(s)>=e^(delta tau0)s follows.

The exclusion needs this smooth transverse fiber description through the limiting locus, as well as the stated return extension. Infinite-order vanishing of the magnitude of W does not defeat it. Degeneration of its direction, failure of a transverse section tangent to that direction, a return with no such one-dimensional quotient, or a general nonhyperbolic zero set remain outside the argument.

## 6. Monomial saddle chains

Suppose a finite cyclic sequence of local saddles has

    X=h_i x partial_x-b_i y partial_y-a_i z partial_z,
    W=x^(p_i)y^(q_i) partial_z,

where h_i,b_i,a_i>0 and p_i,q_i are nonnegative integers. The divergence equation says a_i=h_i-b_i+d. The bracket ratio is p_i h_i-q_i b_i+a_i, so its required value kappa is equivalent to

    (p_i+1)h_i-(q_i+1)b_i=delta>0.

Thus b_i/h_i<(p_i+1)/(q_i+1). If the smooth nondegenerate connecting maps preserve the fibers and match the vanishing orders q_i=p_(i+1) cyclically, multiplication gives product_i b_i/h_i<1. The order-matching condition is explicitly retained; no claim is made for arbitrary connecting maps.

For one saddle, travel from x=r,y=epsilon to x=epsilon takes time h_i^(-1)log(epsilon/r), and the outgoing y coordinate is epsilon(r/epsilon)^(b_i/h_i). Composing these exact local maps with smooth connecting maps of nonzero positive scalar derivative gives the scalar return r maps to C r^sigma(1+o(1)), where C>0 and sigma=product_i b_i/h_i. One has F(r)/r->infinity as r decreases to0 because sigma<1. It is repelling near0. This checks this specific monomial construction only, not every singular network.

## 7. Scope of the historical paragraph

The equations in the historical gamma paragraph are correct with the source assumptions retained, and the scalar-multiplier, global-triangular and smooth-fiber constructions have the stated obstructions. The smooth-fiber clause must retain that the return extends to the limiting cycle; a derivative bound F'>1 without F(0)=0 would not alone imply repulsion from0.

The source itself supplies neither a general gamma-model nor a proof excluding all such models. The identities above place no Euler curl coupling or pressure law into the kinematic hypotheses. They prove no derivative bound for a decaying profile, no general sign condition, no gamma-case exclusion and no unrestricted nonexistence theorem. The full source's conjectural inclination remains an opinion, not a proved conclusion.

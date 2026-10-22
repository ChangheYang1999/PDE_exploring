# A harmonic endpoint sign constraint and the critical vorticity flux at beta two

Status: CONFIRMED from the explicit hypotheses, after independent proof, exact controls and two actual Claude Opus5.5 reviews. These are necessary or conditional identities, not a nonexistence theorem.

## 1. A local endpoint theorem

Use a positively oriented orthonormal physical frame (tau,n), with coordinates (u,v) and origin p. Suppose W is smooth on a neighborhood of p, div W=4, W(p)=0, and its zero set contains a smooth half-arc ending at p with tangent tau. Let C be a smooth curve through p with tangent n. Suppose one side E of C, locally described by u>c(v), c(0)=c'(0)=0, has no zeros of W and curl W=0. The side chosen is the side beyond the endpoint; in particular (u,0) belongs to E for all sufficiently small u>0. The zero half-arc must lie outside E. If its direction away from p were +tau, its points would have u>0 of first order and v=O(u^2); since c(v)=O(v^2), these points would belong to E, contradicting zero-freeness.

Then the fixed tangential component q=tau dot W takes both positive and negative values in E arbitrarily close to p. The conclusion uses a fixed vector tau, not the tangent to a curved continuation away from p. It excludes a one-sign hypothesis on this velocity component alone. It does not impose a sign on temperature or vorticity, and it does not exclude B2.

### Proof

Differentiating W=0 along the half-arc and passing to p gives DW(p)tau=0. Continuity of curl W from E gives curl W(p)=0, so DW(p) is symmetric. Its trace is4. In the frame (tau,n), these three facts force DW(p)=diag(0,4). Consequently q(p)=0 and grad q(p)=0.

On E, writing W=(q,w), the two first-order relations are q_u+w_v=4 and w_u-q_v=0. Differentiating gives Delta q=0 and Delta w=0. If q vanished identically on a connected small neighborhood on this side, then w_v=4 and w_u=0, hence w=4v+C. Continuity at p gives C=0. Thus all (u,0), u>0 small, would be zeros of W in E, a contradiction. This argument applies in arbitrarily small side neighborhoods.

Suppose q>=0 on E intersected with a sufficiently small disk about p. A smaller graph strip {c(v)<u<c(v)+delta, |v|<delta} lies in that disk and is connected, so we work in this strip. The identically-zero contradiction above holds in it. It is not identically zero, so the strong minimum principle gives q>0 in its interior. Smoothness of C provides an interior disk B_R(a), tangent to C at p, whose closure except for p lies in that side neighborhood. On the inner circle |X-a|=R/2, q has a positive minimum m. In the annulus R/2<|X-a|<R, put

    h(X)=exp(-lambda |X-a|^2)-exp(-lambda R^2),

where lambda>=4/R^2. Direct differentiation gives

    Delta h=4 lambda (lambda |X-a|^2-1) exp(-lambda |X-a|^2)>=0.

Choose epsilon>0 so that epsilon h<=m on the inner circle. On the outer circle h=0 and q>=0. Since Delta(q-epsilon h)<=0, the minimum principle gives q>=epsilon h throughout the annulus. Along the inward radius from p, h has a strictly positive inward derivative at p. More explicitly, for the inward unit vector nu=(a-p)/R,

    q(p+t nu)/t >= epsilon h(p+t nu)/t
        -> 2 epsilon lambda R exp(-lambda R^2)>0.

The differentiability of q at p follows from the full-neighborhood smoothness of W. Thus its inward derivative is strictly positive, contradicting grad q(p)=0. The same argument for -q excludes q<=0. Both signs occur in every side neighborhood, as asserted.

The zero-free hypothesis is essential: W=(0,4v) has all the other local properties and q identically zero, but has zeros throughout the positive u-axis. No analytic extension across C is used. The sphere and annulus argument is included to specify the boundary regularity and derivative assumptions behind the Hopf step.

### Application and a sharpness example

At an outgoing beta-two B2 endpoint, the previously audited local basin theorem gives such an E, bounded by the strong unstable curve C, with Theta constant and Omega=-curl W=0. E has no equilibrium. Thus the theorem applies without assuming that the entire global zero set is the central arc. It also applies at an incoming endpoint whenever the separate local basin theorem supplies these same zero-free isothermal-side hypotheses. For an incoming endpoint these inputs are full-neighborhood smoothness, a smooth zero half-arc, a smooth transverse boundary with the specified side geometry, and a zero-free side on which Omega=0. The incoming theorem requiring isolated off-arc zeros supplies them; they must not be silently dropped.

Packet168 gives a smooth local field with precisely these endpoint data and a straight zero half-arc. On the right half-plane it is

    g(z)=exp(-z^(-1/2)), z=u+iv, principal branch,
    W=(Re g(z),4v-Im g(z)).

The sector cutoff construction in168 extends it smoothly across the endpoint while keeping div W=4, curl W=0 on this side, zero set {(u,0):u<=0}, and all jets of W-(0,4v) zero at p. For any fixed angle theta in(0,pi/2),

    q(r exp(i theta))
       =exp[-r^(-1/2) cos(theta/2)] cos[r^(-1/2) sin(theta/2)].

Take r_j=[sin(theta/2)/(j pi)]^2. These points lie in the right half-plane and tend to p, and q has sign (-1)^j there. Thus the sign changes are compatible with complete flatness of q at the endpoint. Taking locally constant temperature makes the equations true on the isothermal side, but packet168 does not solve the coupled equation on a full endpoint neighborhood. It is not a B2 counterexample. The example shows why finite Taylor information does not make the sign obstruction decisive.

## 2. The beta-two moment identity, including its critical flux

Let smooth real fields Theta,Omega,W on the full plane satisfy

    div W=4,  W dot grad Theta=0,
    W dot grad Omega+Omega=Theta_x.

Assume, uniformly in direction e(alpha)=(cos alpha,sin alpha), as r tends infinity,

    Theta(r e(alpha))=h(alpha)+o(1),
    Omega(r e(alpha))=r^(-1/2)a(alpha)+o(r^(-1/2)),
    |Theta_x(X)|<=C/(1+|X|),
    W(X)=2X+o(|X|),

and assume the displayed asymptotic traces h,a are continuous. These imply bounded Theta and |Omega(X)|<=C(1+|X|)^(-1/2), after increasing C on a compact disk. Let G be a C1 real function on an interval containing the range of Theta and h. Let D be either the full plane or the right half-plane. In the latter case assume W_1=0 on x=0, as supplied by B2 parity. Set J to the full angle circle or (-pi/2,pi/2), respectively.

For every integer k>3,

    integral_D G(Theta) Omega^k Theta_x
       = (k-3)/(k+1) integral_D G(Theta) Omega^(k+1).       (1)

Both integrals are absolutely convergent. At the critical integer k=3,

    integral_D G(Theta) Omega^3 Theta_x
       = (1/2) integral_J G(h(alpha)) a(alpha)^4 d alpha.   (2)

The left side of(2) is absolutely convergent. In general the integral of G(Theta)Omega^4 need not converge, and it is not used in the proof. Dropping the flux in(2) would be an error. If G(h)>=0 on J, its right side is nonnegative; it is strictly positive if G(h)a^4 is positive somewhere. These signs are consequences, not contradictions.

### Proof

The transport equation and chain rule give W dot grad G(Theta)=0. For every integer k>=0, the product rule gives the exact local identity

    div[G(Theta) Omega^(k+1) W]
       =(k+1) G(Theta) Omega^k Theta_x
        +(3-k) G(Theta) Omega^(k+1).                     (3)

No division by Omega occurs, so its zeros cause no singularity. The fields are smooth and G is C1, which suffices for the divergence theorem on D intersected with a disk B_R. In the half-plane case the straight boundary contributes zero since W_1=0. The remaining boundary flux is

    F_R=R integral_J G(Theta(R e)) Omega(R e)^(k+1)
                           [W(R e) dot e] d alpha.

The boundedness of G on the compact range gives |F_R|<=C R^((3-k)/2). For k>3 it therefore tends zero. The first volume integrand has size O(r^(-k/2-1)), with radial measure r dr; it is absolutely integrable for k>2. The second has size O(r^(-(k+1)/2)), hence is absolutely integrable for k>3. Passing to the limit in(3) proves(1).

When k=3, the second term of(3) is identically zero at every finite R. Uniform asymptotics and continuity of G give

    F_R -> 2 integral_J G(h) a^4.

The first volume integrand is absolutely integrable, as just shown. Divide its coefficient4 in(3) to obtain(2). In particular no product of a zero coefficient with an infinite integral was used.

If a beta-two B2 solution has the three-region decomposition of182, the integrands in(1) and(2) vanish off F because Omega=0 there. The formulas may then be written over F, or over its right half. This restriction is by equality of integrands, and does not discard any temperature term on a curved boundary. The full-plane or half-plane disk calculation is the defining argument. The right-half formula is the direct half-plane calculation, not one half of the full-plane identity. Under B2 parity its two volume integrands are even only for odd k; for even k they are odd and the full-plane integrals vanish without determining the right-half integrals. Continuity of h and a is redundant under the stated uniform convergence, and is retained explicitly for clarity. The asymptotic and derivative hypotheses must be checked separately before applying these identities to any proposed solution or representation.

## Dependencies and limits

Section1 is an independent local proof from its stated hypotheses. Its B2 application uses the already audited basin statements173-179. Its flat example is the fully proved local construction168. Section2 uses only its explicit transport, divergence, trace and derivative hypotheses and elementary integration. It independently checks the critical coefficient and the integrability thresholds in the lead's zgamma1 consultation. Neither section proves the smooth half-arc endpoint impossible, forces temperature positivity, guarantees the canonical inverse, or supplies a global profile. The remaining full B2 question stays open.

Written UTC 2026-10-21T16:31:14.021872+00:00, before controls and review.

## Verification and scope of the controls

Completed UTC 2026-10-21T16:39:51.224312+00:00. The complete mathematical argument above was written before the controls. The independent SymPy script test_endpoint_critical_flux.py passed65 exact algebraic or symbolic identities and five negative controls in1.155026774s, from2026-10-21T16:32:49.815130+00:00 to2026-10-21T16:32:50.970121+00:00. Exact formulas and counts are retained in verification/controls.json. No theorem-prover build was run.

The local harmonic polynomial control checks divergence, curl and the Laplacian calculation, but is not itself an endpoint construction. The flat-sector formula checks eight alternating phases and signs. The polynomial coupled control Theta=x^2,Omega=2x,W=(0,4y-x^2),Psi=2xy-x^3/3 satisfies the thermal, vorticity and elliptic equations algebraically. It violates the sublinear-velocity and far-field hypotheses, so it is not an admissible B2 profile. It checks18 weighted local identities for k=0,1,3,4,5,6 and G=1,Theta,Theta^2.

For the boundary flux, the independent exterior transport manufacture is

    W=2X, Theta=cos^2(alpha),
    Omega=r^(-1/2) cos(alpha)-2r^(-1)sin^2(alpha)cos(alpha), r>=1.

It satisfies the two transport equations and div W=4 on this exterior. It fails Omega=-curl W and is not smooth at the origin if extrapolated. Only the conditional transport identity is being tested. The annular calculation retains the inner boundary flux at r=1. For k=3,G=1 on the full exterior, the volume integral is13pi/64, the infinite outer flux divided by4 is3pi/8, and the inner flux divided by4 is11pi/64. Their difference gives13pi/64. The script also checks G=Theta andTheta^2, full and right half exteriors, and the supercritical radial identities through k=7. The half-plane values in this k=3 manufacture are exactly half because the integrands are even; that must not be generalized to even k.

Negative controls catch discarding the critical flux, claiming the exterior manufacture solves the curl equation, setting its nonzero infinite outer flux to zero, using the wrong critical factor, and reversing the inner-boundary sign. These finite controls do not replace the strong minimum principle, the explicitly proved barrier argument, the smooth flat extension168, or the stated B2 application hypotheses. No numerical evidence is presented as proof of a profile or of nonexistence.

The two written model reviews were substantive and sequential. Review331 identified boundary-regularity and dependency qualifications; the graph strip and inward derivative argument were made explicit. Review332 independently accepted the revised argument and corrected two erroneous suggestions in331: the parity assertion for even k and the claim that the weighted fourth moment must diverge whenever a is nonzero. Its own model-version introspection was unavailable, while the API returned claude-opus-5-5 in both calls. The actual returned model is recorded in the status metadata. The reviewers did not inspect dependent packets168,173-179,182, so their answers are not counted as external verification of those packets. Those dependencies have the verifier's separate written proofs and checks. The full B2 endpoint remains OPEN.

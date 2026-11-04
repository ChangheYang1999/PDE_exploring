# The angular pressure forcing must be positive near a flat zero

## 1. Exact local theorem

Let 1<p<3/2, equivalently 2/5<c=1/(p+1)<1/2, and eta=(p-1)/(2p) in (0,1/6). Let D be a sufficiently small geodesic disk about n0 on the unit round sphere with metric gamma. Suppose w is a smooth tangent vector field and h a smooth scalar on D, both vanishing to infinite order at n0, with h>0 on D minus {n0}. Assume

    div_gamma w=0,
    d(h^(-eta) w^flat)=0 on D minus {n0}.

Here w^flat is the metric-dual one-form. Define s=|w|^2, R=s/h on the punctured disk, u=s/2-h,

    lambda=2p(2p-1)>0,
    F=tr((nabla_gamma w)^2)+2p s,

and assume the exact angular pressure equation

    -(Delta_gamma+lambda)u=F.                       (1)

Suppose, additionally, that the period of the closed form h^(-eta)w^flat around n0 is zero. Then F>0 at points arbitrarily close to n0. If also u>=0 on a neighborhood of n0, then F has both positive and negative values arbitrarily close to n0, and liminf_(n->n0)R(n)=2.

The zero-period assumption follows, in particular, if there are radii rho_j tending to zero and finite constants C,N such that max_(dist(n,n0)=rho_j) R(n)<=C rho_j^(-N). The same C,N must work along this sequence. An upper bound for R throughout the punctured neighborhood is a special case.

This is the zero-rotation local k=0 reduction of CO65: V=r^(-p)w(n), S=-r^(-2p)h(n), P2=r^(-2p)u(n). It is a theorem about the explicitly displayed angular equations. It does not presume a global Euler profile and has not been extended to nonzero omega. The period is an additional hypothesis unless the stated sufficient condition is verified.

## 2. A smooth stream function and the Hessian inequality

The disk is simply connected and div w=0. Let J denote rotation by a right angle in its oriented tangent planes. There is a smooth real stream function psi with w=J grad psi; set psi(n0)=0. This follows from closedness of the rotated metric-dual form and integration along paths in the full disk. Since dpsi is a smooth rotation of w and w is infinitely flat at n0, psi is infinitely flat there as well.

On the punctured disk, closedness of h^(-eta)w^flat becomes

    div_gamma(h^(-eta)grad psi)=0,
    Delta_gamma psi=eta grad(log h).grad psi.        (2)

The sphere's area rotation J is parallel, so in an oriented orthonormal frame nabla w=J B, where B=Hess_gamma psi is a symmetric2 by2 matrix. Direct multiplication gives

    tr((J B)^2)=-2 det B.

Suppose for contradiction that F<=0 throughout some sufficiently small punctured disk. Then

    det B>=p|grad psi|^2>=0,
    |B|^2=(tr B)^2-2det B<=(Delta psi)^2.

Together with (2),

    |Hess psi|<=eta |grad log h| |grad psi|.          (3)

On any fixed compact path in the punctured disk, the coefficient in (3) is bounded. Parallel transport of grad psi along that path and Gronwall's inequality show that a zero gradient at one endpoint forces zero gradient throughout the path. The punctured disk is path connected. Therefore grad psi is either zero everywhere there or nowhere zero. This argument needs only finite compact paths, not a complete characteristic flow or a bound on grad log h near n0.

## 3. Both alternatives contradict the assumed nonpositive forcing

If grad psi=0 everywhere on the punctured disk, w=0 and F=0 there. Equation (1) becomes (Delta+lambda)h=0. By smoothness it extends across n0. Since h>=0 and h(n0)=0, Delta h=-lambda h<=0. The minimum principle forces h=0, contradicting h>0 away from n0. One can verify this directly: the spherical circle mean m(rho) satisfies (sin(rho)m')'=-lambda sin(rho)m<=0, m(0)=m'(0)=0, so m<=0.

If grad psi is nowhere zero, det B>=p|grad psi|^2>0. Hence B is definite at every punctured point and its sign is constant by connectedness. Choose sigma in {1,-1} so that f=sigma psi has positive definite Hessian there. Along each radial geodesic from n0, f(0)=f'(0)=0 and f''>0 for positive radius. Thus f is positive and strictly increasing along every such ray.

Choose a small fixed radius rho1. The minimum of f on its compact boundary circle is positive. For any positive level ell below that minimum, each ray meets {f=ell} once. The positive radial derivative and the implicit function theorem make this a smooth closed curve C, a radial graph enclosing n0 exactly once and contained in the punctured disk. The vector w is tangent to C and never zero. Orient C in its direction. Then

    integral_C h^(-eta)w^flat
       =integral_C h^(-eta)|w| ds>0.               (4)

However, C represents one of the two orientations of a generator around n0. A closed form with zero period has zero integral on C, by Stokes' theorem in the intervening compact annulus. This contradicts (4). Both alternatives are impossible, proving that F cannot be nonpositive on any punctured neighborhood. Thus positive values approach n0.

## 4. Verification of the sufficient zero-period condition

Closedness makes the oriented integral I of h^(-eta)w^flat on a centered geodesic circle independent of its radius. On the circle of radius rho,

    |I|<=2pi sin(rho) sup |w|^(1-2eta) R^eta.       (5)

The algebra h^(-eta)|w|=|w|^(1-2eta)R^eta is valid when w!=0 and extends as zero where w=0 because h>0 and 1-2eta>0. Flatness gives, for every integer m, sup_circle |w|<=C_m rho^m. Along the proposed sequence, (5) is at most

    C'_m rho_j^[1+m(1-2eta)-N eta].

Choose m large enough that the exponent is positive. The bound tends to zero, so the radius-independent period is zero. No derivative control on R is needed, and the condition is imposed only on the specified sequence of full circles. A pointwise bound along a single radial path would not justify this estimate.

## 5. Nonnegative pressure forces both signs and the endpoint ratio

Suppose u>=0 near n0. If F>=0 throughout some smaller punctured neighborhood, smoothness gives Delta u=-lambda u-F<=0 also at n0. Since u(n0)=0, the minimum principle gives u=0, hence F=0. This contradicts Section3. Therefore F<0 at points arbitrarily close to n0; Section3 also supplies positive points.

The inequality u=s/2-h>=0 gives R>=2 off n0. To prove liminf R<=2, suppose instead that R>=Rstar>2 throughout a punctured neighborhood. Put

    T=u gamma+w tensor w,
    mu=(p+1)(2p-1).

Incompressibility and the round-sphere Ricci tensor give

    div div T=Delta u+tr((nabla w)^2)+s
                =lambda h-mu s.

Here lambda/mu=2p/(p+1)<2. The two eigenvalues of T are s/2-h and3s/2-h. Thus T is positive definite away from n0, with uniformly bounded eigenvalue ratio, and div div T<=-(mu-lambda/Rstar)s<=0. It is infinitely flat at n0.

For completeness, let A(rho), B(rho) be the integrals over the unit angular parameter of T(e_rho,e_rho) and T(e_theta,e_theta). The integrated polar divergence formula gives

    A'+cot(rho)(A-B)<=0.

Uniform eigenvalue ratio gives B<=kappa A for a fixed kappa. Therefore A'<= (kappa-1)cot(rho) A. Integrating from rho to rho1 gives

    A(rho)>=[sin(rho)/sin(rho1)]^(kappa-1) A(rho1).

Strict positivity gives A(rho1)>0, contradicting infinite flatness. This is the already confirmed tensor-average argument A1609-A1613, specialized to the same angular equations. Hence liminf R<=2, and R>=2 proves equality. The endpoint R=2 itself is not excluded by this calculation.

## 6. Verdict and limits

CO65(a), (b), and the sequence-of-circles sufficient condition for its period hypothesis are confirmed. The source's phrase that w is flat on the whole disk should mean that w is smooth on the whole disk and flat at n0. The proof needs a stream function on the full disk and an additional zero period for the differently weighted form on the punctured disk; these are distinct facts.

The proof does not show that the required sign oscillation is impossible or that the period always vanishes. The zero-rotation hypothesis is essential to the displayed angular conductivity and pressure equations. The rotating reduction has an additional drift, as checked at A1578. No regular-point examples from the nested answer, no new numerical computation, and no formal build are used. The coordinator's actual source sections and the earlier tensor and rotating-reduction dependencies were fully reread. Existing configured model collaboration is through files; actual provider runtime is independently unattested.

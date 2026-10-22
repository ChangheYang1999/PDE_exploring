# Beta-two regular levels and the range on the equilibrium set

Status: independent proof of the range assertion in the lead's beta2t note. No Poincare-Bendixson theorem, finite-equilibrium hypothesis, or convergence assertion on critical levels is needed. This is a kinematic restriction, not a nonexistence theorem for the coupled B2 equations.

## Exact statement

Let W be a smooth planar vector field with div W=d>0, W(X)=beta X+o(|X|) as |X| tends to infinity, beta>0, and let T be a smooth nonconstant first integral, W.grad T=0. Put Z={W=0}. Then:

1. For each regular value c in the range of T, the level T=c is a finite disjoint union of proper embedded lines. Each line contains exactly one zero p of W. Every other point of that line converges to p in backward time and escapes in forward time.
2. T(R^2)=T(Z). In particular T is bounded, since Z is compact.
3. The forward nonescaping set K is compact, connected and of area zero. Its complement has no bounded connected component and is smoothly parametrized by an exterior transverse circle and flow time.

For B2 with beta=2, take T=Theta and d=4. The result requires no vorticity equation or Poisson inversion. It does not assert that every trajectory on a critical level converges to an equilibrium.

## 1. Complete flow and compact trapping in backward time

Sublinearity gives |W|<=C(1+|X|), so its flow phi_t is complete in both time directions. For sufficiently large R,

    X.W(X)>=beta |X|^2/2, |X|>=R.

Thus the closed disk Bbar_R is invariant under the reversed flow, every backward trajectory is bounded, and every trajectory reaching the exterior escapes exponentially in positive time. All equilibria lie in B_R, so Z is compact. A periodic orbit would have zero outward flux, contradicting div W=d>0 on its Jordan interior. The same argument excludes any invariant Jordan curve.

## 2. A regular level and its zeros

For a regular value c, L=T^(-1)(c) is a closed embedded one-manifold. Each component is open and closed in L, hence closed in the plane, and is either a circle or a proper embedded line. Properness here follows from closedness and regular-value local charts: a sequence on a component that converges to a finite point of L continues in the unique local level arc at that point. Equivalently, the inclusion of each closed embedded component is a proper map.

W is tangent to L. At a zero p in L, differentiating W.grad T=0 gives

    grad T(p)^T DW(p)=0.

The image of DW(p) is therefore contained in the tangent line. Its eigenvalue on that tangent line equals trace DW(p)=d. In a smooth oriented arclength coordinate, the scalar tangent speed has derivative d at the zero. Every zero is isolated on L and repelling in forward time.

A circular component with no zero is a periodic orbit. A circular component with zeros has finitely many, all with a positive derivative of its scalar tangent speed. This is impossible: the positive-to-negative crossing needed between two such zeros would supply a zero with the opposite crossing, and one zero on a circle would itself attract on one side. Hence all components are proper lines.

On a proper line, there is at most one zero. If two consecutive zeros existed, the tangent speed would be positive immediately to the right of the first and negative immediately to the left of the second, forcing an intervening zero not having derivative d>0. Zeros in a compact arclength interval are finite, so this argument does not omit an accumulation case.

There is at least one zero on every component. Choose a nonstationary point, which exists since the field cannot vanish on an open level arc when the tangent derivative at a zero is d. Its backward orbit is contained in a compact subset of the plane. Properness puts it in a compact arclength interval. The arclength coordinate is monotone until a zero is reached, and uniqueness precludes reaching a zero in finite time. It therefore has a finite backward limit, which must be a zero, since a nonzero scalar speed would preclude convergence. This proves existence and backward convergence to the unique zero. In positive time each nonstationary orbit moves away from that zero and has unbounded arclength; properness gives spatial escape.

Finally Z cap L is compact and has only isolated points in L. It is finite. Each component contains precisely one of these points, so the total number of components is finite.

## 3. Range equality by Sard and compactness

Every regular value in the range of T belongs to T(Z), by the preceding section. Since T is nonconstant and R^2 is connected, its range is a nondegenerate interval. Sard's theorem makes its critical values a set of one-dimensional measure zero. Thus every value c in its range is a limit of regular values c_j also in its range, including any attained endpoint of the interval. Choose p_j in Z with T(p_j)=c_j. Compactness of Z gives a convergent subsequence p_j->p in Z, and continuity gives T(p)=c. Consequently T(R^2) is contained in T(Z). The reverse inclusion is immediate. This also proves boundedness of T. The argument does not infer convergence of arbitrary critical-level trajectories from convergence on regular levels.

## 4. The full trapped set

With the transverse circle above, define

    K=intersection_(t>=0) phi_(-t)(Bbar_R).

The sets are nested topological closed disks. Their areas are e^(-dt) pi R^2. Thus K is nonempty, compact, connected and has area zero. It consists exactly of the bounded forward orbits. Membership means staying in Bbar_R for all positive time. Conversely a bounded forward orbit cannot leave that disk, because exterior radius is strictly increasing exponentially. K is invariant in both time directions by flow completeness and boundedness of the finite extra orbit segment.

If a bounded component of R^2 minus K existed, the flow would preserve that component: a continuous trajectory in the complement cannot cross K or move between its components. Its finite positive area would then grow by e^(dt), a contradiction. Thus no such component exists.

Each escaping trajectory crosses the chosen circle exactly once. Backward radial decrease gives existence, and strict outward crossing gives uniqueness. The hitting-time theorem applies because the crossing is transverse. Hence (angle,time) supplies a smooth diffeomorphism from S^1 times R to the escaping set. This allows T there to be expressed as a function of an exit angle; it gives no reason for that function to be constant.

## Audit of the lead beta2t closure attempt

The range identity and the source-basin argument are valid. If a backward basin of an equilibrium is open, temperature is constant there; the vorticity history equation forces Omega=0, and div/curl makes U harmonic there. This gives analyticity inside that open basin only. A function harmonic in a half-plane can be nonzero and flat at a boundary point, for example a real or imaginary part of exp(-z^(-a)), 0<a<1, with the branch in Re z>0. Therefore flatness at an endpoint is not a continuation argument across that endpoint.

For the lead's local endpoint construction W=(f(s),(4-f'(s))t) in translated Cartesian coordinates, its assigned temperature is constant and its assigned transported Omega is zero, whereas -curl W=t f''(s). A positive function flat at s=1 cannot have f'' identically zero on any interval immediately to the right. The coupled curl equation fails in every such neighborhood. This is an explicit defect of that construction, not a proof that all coupled extensions fail.

Our independent research/20 construction instead enforces the canonical velocity/vorticity law globally and drops the vorticity transport equation. The two constructions expose different parts of the same unresolved closure problem. Neither is a B2 profile.

Dependencies: complete smooth flows, the regular-value theorem, Sard's theorem, the one-dimensional scalar ODE, the divergence theorem and elementary compactness. Research/18 and actual Opus5.5 request10 independently checked the regular-level geometry used here. This packet adds the backward convergence, finiteness and Sard range argument. No numerical computation is used as proof.

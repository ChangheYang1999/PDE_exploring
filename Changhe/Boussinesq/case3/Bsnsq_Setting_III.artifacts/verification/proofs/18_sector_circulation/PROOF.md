# Slow-tail circulation in a fixed sector away from the axis

Status: new verifier extension of research/17. The beta=2 regular-level lemma has been independently confirmed by actual claude-opus-5-5; the complete sector transfer is recorded for lead review. It strengthens a restricted-class mass estimate, not the full B2 endpoint.

## Statement

Assume the smooth B2 equations and center data of research/17, beta>=2, and the power bound |U(X)-U(0)|<=C(1+|X|)^(1-delta), delta>0. Let s0=sign(a0). There are a compact sector-annulus K contained in {a<=|X|<=b, x>=epsilon |X|}, with a,b,epsilon>0, and c,R0>0 such that

    integral_(R K) (s0 Omega)_+ >= c R^(2-1/beta),  R>=R0.        (1)

Thus for every gamma<=2-1/beta,

    integral_{|X|>1} |x| |X|^(-gamma-1) (s0 Omega)_+ = infinity.  (2)

In particular the positive-part contribution to the absolute vertical center-kernel integral grows at least as R^(1-1/beta) on a fixed sequence of sector-annuli, and its full integral diverges. This proves a stronger component-weight conclusion than research/15, without a decay assumption on DU or a pointwise vorticity tail expansion.

## 1. A bounded domain with positive limiting circulation

Use the notation from research/17: Theta=a0 xi^2 in smooth local coordinates (xi,y), and

    H(X)=integral_0^infinity e^(-(beta+1)t)(phi_t X)_2 dt.

H is continuous. On the vertical axis it is strictly increasing: the scalar autonomous axis flow preserves strict order, so y2>y1 implies (phi_t(0,y2))_2>(phi_t(0,y1))_2 for every finite t, and integration preserves the strict inequality.

Choose 0<b1<b2 sufficiently small. Because W_2(0,y)=mu y+O(y^2), mu=1+3 beta/2>0, W_2>0 on the compact axis segment b1<=y<=b2. After shrinking h>0, throughout the coordinate rectangle 0<=xi<=h, b1<=y<=b2 we have W_2>0, Omega has the sign of a0 when xi>0, and

    Htilde(xi,b2)-Htilde(xi,b1)>0.                              (3)

For any 0<u<v<h let D_(u,v) be this coordinate rectangle u<xi<v, b1<y<b2. The same exact circulation calculation as in research/17 gives

    A_D=integral_D Omega
          +2a0 integral_u^v xi[Htilde(xi,b2)-Htilde(xi,b1)] dxi.

Therefore s0 A_D>0 for every such rectangle. We next choose u,v so that its closure lies entirely in the forward escape region E.

## 2. Putting the entire domain in the escape region

For beta>2, Theta is nonzero on every D_(u,v) and increases in absolute value exponentially along forward trajectories. A bounded trajectory would make smooth Theta bounded along it, a contradiction. Since W points strictly outward outside a sufficiently large ball, an unbounded trajectory eventually leaves that ball and escapes to infinity. Thus any compact closure with 0<u<v<h lies in E.

For beta=2, Theta is constant along the flow and that argument is unavailable. Choose xi0 in (0,h) such that c0=a0 xi0^2 is a regular value of the globally smooth function Theta. Such a choice exists by Sard's theorem: critical values have one-dimensional measure zero, whereas these c0 cover a nonempty interval. Every point of the compact coordinate segment xi=xi0, b1<=y<=b2 is nonstationary, because W_2>0 there. We use the following elementary lemma.

Lemma. If a smooth planar vector field W has constant divergence d>0 and a smooth first integral T, then every nonstationary orbit on a regular level T=c is unbounded, provided W has no periodic orbits.

Proof. The regular level is a closed embedded one-manifold. Each connected component is open and closed in that manifold, hence closed in the plane. Each of its connected components is closed in the plane and is either a circle or a proper embedded line. On a circle, a nowhere-zero tangent field gives a periodic orbit. At any zero p on a regular level, differentiating W.grad T=0 gives (grad T)DW=0. Thus the image of DW lies in the tangent line to the level; its eigenvalue on that tangent line equals trace DW=d. In a smooth arclength coordinate the scalar tangent speed therefore has derivative d>0 at every zero. All zeros are simple repellers for the one-dimensional forward flow. Such zeros cannot occur on a circle unless another zero crosses with the opposite sign. Hence there is no bounded circular component carrying a nonstationary orbit. On a proper line the arclength coordinate of a nonstationary orbit is strictly monotone. If it has a finite limit, the limit is a zero, and a simple repeller cannot be approached in forward time from either side. Otherwise the coordinate tends to plus or minus infinity. Properness then gives actual escape in spatial radius, not merely an unbounded trajectory. This proves the lemma. Properness follows directly from the regular-value local charts and closedness: a component accumulating at a finite point continues through the unique local level arc there. No arbitrary parametrization at infinity is being assumed.

For our W, div W=4 when beta=2. A periodic orbit would be a simple closed orbit by uniqueness; its outward flux is zero, contradicting div W=4 by the divergence theorem on its interior. The lemma therefore applies with T=Theta. Every point of the selected compact segment escapes. The power-sublinear bound is an assumption at infinity. It gives X.W>=beta |X|^2/2 beyond some radius rho. Thus E is exactly the set of points reaching |X|>rho at some finite positive time, and is open by continuity of the flow. Compactness supplies u<xi0<v with the whole closed rectangle contained in E. This completes the choice of D for beta=2 as well.

## 3. A fixed exterior sector for the transported domain

For completeness, the needed trajectory geometry does not require DU decay. Choose a large circle of radius rho with radial component w_r>=beta r/2 outside it. Let s(r,sigma) be the travel time from rho e(sigma) to radius r, and h_r(sigma) its arrival angle. The power bound gives, uniformly in sigma,

    s(r,sigma)-log(r/rho)/beta -> tau_infinity(sigma),
    h_r(sigma) -> h_infinity(sigma).

The derivatives with respect to r of the two differences are O(r^(-1-delta)) after decreasing delta if necessary. The exact flux Jacobian, using div W=2 beta, is

    h_r'(sigma)=rho w_r(rho,sigma)e^(2 beta s(r,sigma))
                  /[r w_r(r,h_r(sigma))].

It converges uniformly to the continuous strictly positive function

    [w_r(rho,sigma)/(beta rho)]e^(2 beta tau_infinity(sigma)).

Hence h_infinity is a C1 orientation-preserving circle diffeomorphism. Axis invariance fixes the two vertical angles, so it maps each open right semicircle to itself. The rescaled forward map Phi(X)=lim_(t->infinity)e^(-beta t)phi_t X exists continuously on E, with nonzero radius, and Phi_1(X)>0 for X in E and x>0. Existence and local uniform convergence follow either by integrating e^(-beta t)V(phi_t X), or from the time-angle coordinates just displayed; a compact subset of E has uniformly bounded exit times to the large circle.

Apply this to the compact closure of D. Its limiting radii are bounded above and away from zero, and its limiting x/r is bounded away from zero. Uniform convergence therefore supplies a,b,epsilon>0 such that, for all sufficiently large t,

    phi_t D subset e^(beta t) K,
    K={a<=|X|<=b, x>=epsilon |X|}.

The exact circulation asymptotic gives

    integral_(e^(beta t)K) (s0 Omega)_+
       >= s0 integral_(phi_t D)Omega
       >= |A_D|e^((2 beta-1)t)/2.

Put R=e^(beta t). Every sufficiently large R occurs, proving (1).

## 4. Weighted consequences and scope

On R K, |x|r^(-gamma-1)>=epsilon r^(-gamma)>=c_gamma R^(-gamma); use b for gamma>=0 and a for gamma<0 in the constant. Multiplying (1) gives a contribution at least c R^(2-1/beta-gamma). If the exponent is positive it is unbounded with R. At equality choose geometrically separated R_j with ratio>b/a; the sector-annuli are disjoint and each contributes a fixed positive amount. This proves (2). Take gamma=1 for the center kernel; since beta>=2, its lower exponent 1-1/beta is positive.

This result concerns the actual component weight and one sign of vorticity, not just the larger radial weight. It does not exclude cancellation in a signed truncation or choose a finite-part observer convention. The proof uses the power improvement of sublinearity to control limiting angles. The full class with only U=o(r), without that power improvement, remains outside this sector theorem.

Dependencies: research/17's exact integrated circulation formula, Sard's theorem for a smooth real-valued function on the plane, one-dimensional flow on a regular level, elementary ODE uniqueness and divergence theorem, and the independently derived angular flux Jacobian in research/14. No numerical evidence is used as proof.

Audit 2026-10-20T14:35:55.776456+00:00: opus_reviews/10_regular_level/answer.md, returned model claude-opus-5-5, confirms the regular-value topology, tangent eigenvalue, escape on a proper line, Sard with dense critical values, and the compact-rectangle argument. Its requested clarification that the velocity asymptotic is at infinity, and the direct properness argument for escape, are incorporated above.

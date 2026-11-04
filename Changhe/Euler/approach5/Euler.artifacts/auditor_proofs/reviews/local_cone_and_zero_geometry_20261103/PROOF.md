# Local cone equations and zero-set geometry

Status: A796-A804 CONFIRMED at the local and conditional scopes below. The unrestricted global exclusion remains OPEN, A805. This is an independent audit of CO44, including its analytic local models. No numerical integration is needed for their existence.

## 1. Exact setting and identities

Fix 2/5<c<1/2 and any real omega. Write Jx=(-x2,x1,0), A=cI-omega J, p=(1-c)/c in (1,3/2), lambda=p-1, mu=2-p, a=1-2c=c lambda, t=omega/c, q=2p/lambda>2 and eta=1/q. Work on the union C_U of all twisted rays exp(As)x over an open angular set U. Suppose V is C^(1,alpha), 0<alpha<1, and P2 is C1 there, with

    V(exp(As)x)=exp(-(1-c)s) exp(-omega sJ)V(x),
    P2(exp(As)x)=exp(-2(1-c)s)P2(x).

Set W=curl V, k=(Ax).V, S=P2-|V|^2/2. The five tail equations are

    div V=0; V.W=0; -Delta P2=partial_i partial_j(V_i V_j);
    W.grad S=0; grad k cross grad S=0 on {W!=0}.       (T1)-(T5)

The Poisson equation is distributional. It is equivalent to -Delta P2=tr((DV)^2). Where invoked, the additional nodal premise is

    {k=0} subset {W=0}.                               (N)

Differentiating homogeneity and using vector calculus gives

    grad k=Ax cross W-aV,
    Ax.grad k=-ak, Ax.grad S=-2(1-c)S,
    W.grad k=-a V.W=0.                                (1)

Away from the poles use rho=log r, z=cos theta, w=1-z^2 and chi=phi+t log r. Write

    V=r^(-p)(R e_r+H/sqrt(w) e_theta+F/sqrt(w) e_phi),
    P2=r^(-2p)u, S=r^(-2p)h,
    K=R-tF, gamma=-H dz/w+F dchi.

The Euclidean metric is r^2[d rho^2+dz^2/w+w(dchi-t d rho)^2]. Let M be the inverse angular round metric plus t^2 Z tensor Z, Z=partial_chi. Then

    V.dx=r^(-lambda)(K d rho+gamma), k=c r^(-lambda)K,
    Bq=M gamma+tKZ,
    div Bq=-mu R, dK wedge gamma=K d gamma.             (2)

The last two identities are precisely divergence and helicity. The exterior derivative of the velocity one-form is

    d(V.dx)=r^(-lambda)[d gamma-d rho wedge(lambda gamma+dK)].

Thus W=0 means d gamma=0 and dK=-lambda gamma. The same formulas hold in regular angular charts at the poles. M is positive definite.

These are local tail equations, not the full nonlinear profile momentum equation. On an open cone P2 is not required to be the globally normalized Newtonian pressure. Those distinctions are essential for the models below.

## 2. Nonflat zeros and their four nodal branches

Assume (N) near a zero x0 of V with DV(x0)!=0. Equation(1) gives dK(x0)=0, and (N) gives W(x0)=0. Hence DV(x0) is symmetric with trace zero and annihilates Ax0. In the quotient chart, G=D gamma(x0) is a nonzero symmetric matrix with tr(MG)=0. Positivity of M implies det G<0: M^(1/2) G M^(1/2) is a nonzero symmetric trace-zero matrix.

Choose a smooth positive area form Omega0 on the chart and define the C^(1,alpha) field C by i_C Omega0=gamma. Equation(2) gives

    C K=K div C.                                     (3)

The derivative DC(x0) has trace zero and determinant det G divided by the square of the area density. It therefore has two nonzero real eigenvalues sigma and -sigma. The local stable and unstable curves have two branches each, and x0 is the only zero of C in a sufficiently small disk. This is the ordinary C1 hyperbolic saddle theorem, used here only locally.

On a stable branch |x(s)-x0|<=C_delta exp(-(sigma-delta)s). Since K is C1 and K(x0)=0, K along it has the same upper bound. If K at one point were nonzero, equation(3), together with div C(x(s))->0, would imply |K(x(s))|>=C_epsilon exp(-epsilon s) for every epsilon>0. Choosing epsilon<sigma-delta is a contradiction. Thus K vanishes on both stable branches; reverse time for the unstable branches. At every noncentral point of these branches gamma!=0, and (N) now gives

    dK=-lambda gamma!=0.                              (4)

These are regular nodal curves, and K changes sign across each. Every zero of V near x0 must be a zero of gamma and hence equals x0. In particular a locally one-signed K can have only flat velocity zeros.

There are exactly these four nodal branches after shrinking the disk. Here is the local passage detail. Straighten the transverse stable and unstable curves by C1 coordinates. The two axes are invariant and the equations factor as xi'=xi A(xi,zeta), zeta'=zeta D(xi,zeta), with A bounded below by a positive number and D bounded above by a negative number in a small rectangle. Any off-axis orbit sufficiently close to the origin exits forward through a vertical side arbitrarily close to the unstable axis, or backward through a horizontal side arbitrarily close to the stable axis. For example, the bounds on A,D bound the exit zeta by its initial value and make it tend to zero when the initial point tends to the origin. At fixed nearby points of the four axes, equation(4) and the implicit function theorem say that the nodal set consists only of the axis. An additional nodal orbit, invariant by(3), would have to enter one of these forbidden local neighborhoods. This proves the assertion.

If dK is differentiable at x0, differentiation of(4) along the two separatrix directions e1,e2 gives

    D(dK)(x0)e_i=-lambda G e_i, i=1,2.

Since they span the tangent plane, Hess K(x0)=-lambda G is invertible. Differentiability of dK at this point is an additional hypothesis; C^(1,alpha) regularity of V does not supply it. With that hypothesis the already proved A734 estimate applies: the local vorticity-weighted mass of {|K|<tau} is O(tau^(1+alpha/2)). Thus this point is outside the critical concentration set for the k weight in an actual profile. Without that differentiability premise, the exclusion is not proved.

## 3. A locally one-signed boundary zero forces S=0

This assertion does not need (N), T3 or T4. Assume k>=0 near x0, k(x0)=0, and x0 lies in the closure of {k>0}. Suppose S(x0)!=0. Shrink the neighborhood so |S| is bounded below. On {W!=0}, contraction of T5 with Ax using(1) gives

    grad k=eta k grad S/S, hence |grad k|<=C k.        (5)

The inequality extends to the closure of that set. On the interior of {W=0}, equation(1) makes k harmonic.

Choose a positive point near x0 and an interior ball of its positive component touching a zero, with its closure contained in this neighborhood. In its outer half-annulus put b(x)=exp(-L|x-y|^2)-exp(-LR^2). For large L one has Delta b>0 and |grad b|>Cb. Choose delta>0 sufficiently small that k>=delta b on both boundary spheres. At a negative interior minimum of k-delta b, one has 0<k<delta b and grad k=delta grad b. This violates(5), so the point lies in the irrotational interior. There k-delta b has strictly negative Laplacian, which contradicts an interior minimum. Thus k>=delta b throughout. At the touching zero this forces a nonzero inward directional derivative, contrary to the C1 local minimum of k. Hence S(x0)=0. Apply the same argument to -k for the other sign.

Under (N), grad k(x0)=0 and W(x0)=0 imply V(x0)=0 by(1), then P2(x0)=0. Section2 implies DV(x0)=0. No assumption on the global pressure is used in this local result.

## 4. Irrotational isolation and local analytic models

If W=0 on a connected cone and V is not identically zero, equation(1) says grad k=-aV and Delta k=0. Thus k is real analytic and nonconstant. At a velocity zero x0, k=grad k=0. Let P_n be its first nonzero Taylor polynomial, of degree n>=2. The degree n-1 part of Ax.grad k=-ak gives Ax0.grad P_n=0. Since Delta P_n=0, its restriction to the plane Pi perpendicular to Ax0 is a nonzero harmonic homogeneous polynomial in two variables. It is Re(e zeta^n) for e!=0; its gradient has magnitude n|e||zeta|^(n-1). The Taylor remainder gives

    |V(x0+xi)| >= n|e||xi|^(n-1)/a-O(|xi|^n)>0

on Pi for sufficiently small nonzero xi. Pi is transverse to the twisted rays, so x0 is an isolated angular velocity zero. Therefore a nonisolated zero, near which V is not identically zero, has vortical points arbitrarily close.

Local analytic examples show why the value of S alone excludes neither isolated type. For a scalar of twisted degree -d write phi=r^(-d)f(z,chi). Its harmonic equation is

    (w f_z)_z+(1/w+t^2)f_chichi+t(1-2d)f_chi+d(d-1)f=0.  (6)

Near z=chi=0 this is an analytic equation solved for f_zz with nonzero coefficient w. The analytic Cauchy theorem, in the form already checked in A590, supplies a unique convergent solution from analytic f(0,chi) and f_z(0,chi). Take d=lambda, f(0,chi)=chi^n and f_z(0,chi)=0, n>=2. Taylor recursion in(6) gives no term below degree n and a nonzero degree-n homogeneous solution of its principal elliptic part. Equivalently the physical leading term is a transverse two-dimensional harmonic polynomial. Choose another local solution Q of degree -2p with arbitrary value Q(x0), using constant Cauchy value and zero normal Cauchy derivative.

Then

    V=grad phi, P2=Q-|grad phi|^2/2,
    k=-a phi, S=Q-|grad phi|^2                         (7)

satisfies the homogeneities and all T1-T5: T2,T4,T5 are immediate from W=0, and Delta(|grad phi|^2/2)=|D2phi|^2 proves T3. Premise(N) holds. At n=2 the velocity zero is nonflat; for n>2 it is flat, and in both cases it is isolated. Its S value is the arbitrary Q(x0). Choosing Q=0 gives S=-|V|^2, so the small-negative-part condition of A696 is not automatic. These are local analytic tails on a proper cone, not globally decaying profiles or global tail counterexamples.

## 5. A convergent local periodic quotient model

For t!=0 choose a0<0, b=(a0-1)/t and d<0 so small that |d|<(a0^2+b^2)/(2q). Seek functions of z alone on a full-azimuthal equatorial band:

    R=a0 K, F=bK, H'=mu a0K,
    h=dK^q,
    u=(a0^2 K^2+(H^2+b^2 K^2)/w)/2+dK^q.             (8)

The relation R-tF=K holds identically. Set

    a_r=-p a0^2 K^2-a0H K'-(H^2+b^2K^2)/w,
    a_z=lambda a0KH+HH'+z(H^2+b^2K^2)/w.

The exact pressure equation T3 reduces to

    (wu')'+2p(2p-1)u+(1-2p)a_r+a_z'=0.                (9)

Indeed a_r is the radial coefficient of (V.grad)V and a_z is its angular z coefficient; divergence gives the final two terms. The Laplacian of r^(-2p)u gives the first two. Substituting H'=mu a0K makes(9) an analytic second-order ODE for K whose K'' coefficient is

    w a0^2 K+b^2K+w d qK^(q-1).

At H=0,K=1,K'=0,z=0 this is a0^2+b^2+dq>0. The ordinary analytic ODE existence theorem therefore gives an exact analytic solution on some |z|<delta with these initial data and K>0. This is an existence proof, not an inference from a numerical trajectory.

Divergence is H'=mu R. The normalized one-form beta=gamma/K=-(H/(wK))dz+b dchi is closed, so helicity holds. Equation(9) proves pressure. Finally S=(d/c^q)k^q, hence T5; equation(1) and zero helicity imply W.grad k=0 and therefore T4. The dchi coefficient of d log K+lambda beta is lambda b!=0, so W never vanishes. Here k>0,S<0 and(N) is vacuous.

At z=0, Bq=(t a0+b)partial_chi, a nonzero field since a0(1+t^2)-1<0. Its circle is periodic with period T=2pi/|t a0+b|. Along it integral R ds=a0T<0. Since div Bq=-mu R, its transverse return multiplier is exp(-mu a0T)>1. Moreover b and t a0+b have the same sign, so integral_Gamma beta=2pi|b|>0. At the circle d(V.dx)=-r^(-lambda)lambda b d rho wedge dchi, so W is transverse to its cone. All these assertions hold for every nonzero omega and target c, on a sufficiently small band.

This verifies local compatibility of the periodic alternative with all five equations. The model is axisymmetric. A global axisymmetric extension satisfying the already audited global tail hypotheses is excluded by Theorem AX; no global extension, whether symmetric or not, is constructed here. At omega=0 this particular construction is undefined and makes no assertion.

## 6. A full vortical puncture cannot surround a velocity zero

Assume(N), V(x0)=0, and W!=0 at every point of a punctured angular neighborhood of x0. On that connected puncture k!=0, and contraction of rank with Ax gives

    grad S=q(S/k)grad k, hence S=D|k|^q                (10)

with one finite constant D. This derivation permits D=0 and does not divide by S. Since |k|<=C|V| locally, continuity gives S(x0)=0 and |S|<=C|V|^q=o(|V|^2). Also W(x0)=0 by(N). Choose any epsilon<alpha/(2+2alpha); sufficiently close to x0 the lower bound S-S(x0)>=-epsilon|V|^2 holds. The local pressure-zero theorem A696-A697 then forces V=0 nearby, a contradiction to the puncture hypothesis.

The same reasoning works when a full punctured neighborhood has the laws(10) with uniformly bounded constants. It does not apply to a single sector or to infinitely many components with unbounded constants. In particular, the proposed polar flat-attractor example with k>0 and W!=0 throughout a punctured cap cannot be completed to T3-T5, despite its valid kinematic transport identities.

## 7. Regular vortical nodes when(N) fails

Suppose k(x0)=0,W(x0)!=0. If S(x0)!=0, rank and homogeneity give(5) on a small ball. Gronwall along segments from x0 forces k=0 on that ball. Equation(1) gives V=(Ax cross W)/a there.

If instead grad k(x0)!=0, the previous conclusion forces S(x0)=0. The local nodal set is a C1 surface, and Ax and W are tangent by(1). Its normal contains both Ax cross W and grad k, hence V is normal. On each of its two connected sides equation(10) holds with possibly different finite constants D_+,D_-. On a small angular disk this implies |h|<=C|K|^q. Angular dK is nonzero: otherwise grad k would be radial, and Ax.grad k=0 with c>0 would force it to vanish.

Consequently the joint sublevel {|K|<tau, |h|<tau^q} contains {|K|<c0 tau} locally and is contained in {|K|<tau}. Since dK and |W| are bounded above and away from zero on a smaller transverse rectangle, its vorticity-weighted angular mass is bounded above and below by positive constants times tau. Thus CO43's sufficient small-mass criterion does not exclude this node. Recall that its degree-minus-one scalar uses max(|k|^(1/lambda),|S|^(1/(2p))); its small sublevel is this intersection, not a union.

The remaining vortical nodes have k=S=0, grad k=0 and Ax cross W=aV. None of these three alternatives is a global existence or exclusion theorem. In particular, three-dimensional almost-everywhere recurrence cannot automatically be restricted to this exceptional nodal surface.

## 8. Cone boundary terms and finite weights

For completeness the unsigned cone identity can be checked directly. Let D be a regular angular disk whose boundary is a Bq orbit. Put T0=(H^2+F^2)/w and let a_hat be the quotient angular part of (V.grad)V. The radial coefficient is a_r=-pR^2+Bq R-T0. Since Bq is tangent to the boundary and div Bq=-mu R,

    integral_D a_r=-2lambda integral_D R^2-integral_D T0.

In twisted coordinates the radial coefficient of grad P2 is -2pu+tZu and its quotient coefficient is Mdu-2ptuZ. Integrating div((V.grad)V+grad P2)=0 gives

    2p integral_D h+integral_D[(3p-2)R^2+(p+1)T0]
     =-1/(2p-1) integral_boundaryD
          [Mdu+(1-4p)t uZ+a_hat].n.                  (11)

The t coefficient is (1-2p)t-2pt, which explains its sign. The velocity is tangent to the physical cone, but its acceleration has normal component -V.(D_V N); this is a curvature term and need not vanish or have a fixed sign. Neither the normal pressure derivative nor the right-hand side of(11) is signed by tangency. The two complementary disks cancel the boundary term and recover the global mean identity.

At a quotient equilibrium where V=0, every finite C1 weight psi satisfies (mu psi R-Bq psi)=0. Its Dirac invariant probability therefore obstructs a strict positive invariant-measure certificate. For the explicit polar kinematic example v=1-z, Bq v=mu v^(m+1)/(m+1), R=-v^m. A power psi=v^(-sigma) gives

    mu psi R-Bq psi=mu(sigma/(m+1)-1)v^(m-sigma).

Strict positivity needs sigma>m+1, whereas local area integrability needs sigma<m+1. The inner flux is proportional to v^(m+1-sigma), so it vanishes only below the threshold. More generally its angular average equals -(mu/(m+1))d_v(v^(m+1) average psi). A nonnegative weight with vanishing inner flux has a nonpositive cap integral. These facts invalidate deletion of that inner boundary in this example, not all conceivable global estimates.

## 9. Dependencies and scope

The exact local results use C1 differential topology, the hyperbolic saddle theorem, harmonic analyticity, elementary analytic ODE existence and the analytic Cauchy theorem in the form already verified for A590. A734 supplies the conditional critical-mass estimate; A696-A697 supply the pressure-zero theorem. Each is used with its original regularity and nodal hypotheses. No derivative premise, pressure normalization or recurrence is inferred solely from velocity decay.

The coordinator's configured model check provides the continuing team comparison; this audit verifies its claims directly and supplies the previously unchecked analytic local existence. The nested request recorded with the answer of the external referee (a second model) failed before inference because its credential source returned no credentials. That failed request is not a successful model review, and the provider runtime of the existing configured agent is not independently attested.

The general rotating nonexistence theorem remains OPEN. Specifically unproved here are a global exclusion of the periodic alternative, automatic differentiability of dK at all saddle nodes, exclusion of accumulating irrotational or vortical components, the nodal premise itself, and surface-wise core return from an ambient almost-everywhere statement. The local analytic examples do not solve or refute the campaign conjecture.

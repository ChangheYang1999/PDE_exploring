# A bounded equilibrium vortex half-line cannot accumulate on a periodic orbit

Status: CONFIRMED as A541-A542 at the explicitly stated scopes after repeated full postreads and refreshed source comparison. A focused configured-model review of this synthesis has not been received; its reviewed premises and continuing file exchange are recorded separately. The old pointwise description of all alpha- and omega-limit sets inside K was unsupported; the source withdrew it in its revised Section4c. The finite-network conclusion below has an explicit additional hypothesis.

## 1. Exact setting and proposed conclusions

Suppose 0<c<1/2, omega is finite, U in C2(R3;R3), P in C1(R3), and

    div U=0, ((1-c)I+omega J)U+(DU)(Ay+U)+grad P=0,
    A=cI-omega J, J(x1,x2,x3)=(-x2,x1,0),
    U(y)=o(|y|) uniformly, U.curl U=0 everywhere.

Write B=Ay+U, W=curl U, a=1-2c, kappa=1+c, H=P+|U|^2/2+(Ay).U and g=U.B. Let p be a vortical equilibrium B(p)=0, W(p)!=0, and let

    DB(p)^T U(p)=rho U(p), rho<=-a<0.

These data follow from A468, A478 and A496. Let L+ be either half of the complete W-line through p, parametrized as a forward B-orbit. Suppose L+ is bounded, and let K be its omega-limit set.

The local conclusions are:

1. K contains no nonconstant periodic orbit of B.
2. If q in K is an equilibrium, rho is a simple eigenvalue of DB(q), and DB(q) is hyperbolic, then at least one of its other two eigenvalues has negative real part. Since their sum is 3c-rho>0, they must be real with opposite signs. Thus q has two stable directions and one unstable direction.
3. If also DW(q)!=0, A469's two possible spectral families reduce to

    spec DB(q)={rho,rho+kappa,-a-2rho}, rho<-(1+c).

The second family is incompatible with conclusion2.

Combined with the separately reconstructed B32 measure classification, conclusion1 implies that every ergodic invariant probability on K is an atom at a nonzero irrotational carrier equilibrium with the same covector rate rho. It does not, by itself, classify every point, alpha-limit set or omega-limit set in K.

## 2. The exact inherited identities

For completeness, the identities needed from B31/B32 have the following derivation, independent of their measure classification. The confirmed bracket and complete W-flow give

    B(Gamma_tau p)=kappa tau W(Gamma_tau p).

Thus each nonzero parameter half is a B-orbit, with tau(t)=tau(0)e^(kappa t). Helicity zero gives g=0 on the whole line; the Lamb identity gives grad H=-aU there and H=H(p). A413/A496 continue the constant multiplier relation

    dg=-(rho/a)dH

on the connected regular vortical H-level through p. Its covector ODE, obtained by differentiating the global identity BH=-ag, is

    (B.grad)grad H=rho grad H-DB^T grad H.                (1)

Initially U!=0 near p by A478. Along each line half this invertible linear ODE prevents a finite-time zero, so the entire line lies in that regular level. The relation dg=-(rho/a)dH extends continuously to its closure and hence to K. Since L+ is bounded, the formula for W on it gives W->0, so on K

    W=0, H=H(p), g=0, grad H=-aU,
    grad g=rho U,
    U(Phi_t x)=e^(rho t)DPhi_t(x)^(-T)U(x).             (2)

K is nonempty compact and fully invariant, and lies in closure{W!=0}. If 0 belonged to K, then g(0)=|U(0)|^2 would give U(0)=0. A478 would give an irrotational neighborhood of 0, contradicting that K lies in the vortical closure. Further, the zero set of U in K is invariant by (2). An orbit in that zero set equals exp(tA)x and has radius e^(ct)|x|. Compactness forces x=0, already excluded. Therefore

    min_K |U|>0, grad H!=0 on K.                       (3)

Only compactness, uniform sublinearity, the confirmed rank identities and complete flows are used here. No decay of U or DU is required.

## 3. Local no-entry lemma at a periodic orbit

Assume for contradiction that gamma is a nonconstant periodic orbit in K, with period T. At x in gamma, (2) implies that U(x) is a left eigenvector of D Phi_T(x), with multiplier e^(rho T). The flow direction has multiplier1, while div B=3c gives determinant e^(3cT). Hence the three distinct positive real multipliers are

    e^(rho T), 1, e^((3c-rho)T).

The orbit is hyperbolic, with one stable transverse direction and one unstable transverse direction. Let lambda=3c-rho>0. Since U is orthogonal to the flow and unstable directions, the tangent plane of the regular surface {H=H(p)} along gamma is exactly their span. This uses grad H=-aU from (2), not global invariance of the entire H-level.

Choose a sufficiently small tubular neighborhood of gamma with periodic Floquet coordinates (theta,s,u). The transverse s and u lines correspond to the two positive real multipliers, hence admit periodic nonvanishing frames. A periodic linear coordinate change puts the transverse variational system in the constant diagonal form. After shrinking the neighborhood, the C1 vector field has

    theta'=1+o(1),
    s'=rho s+o(|s|+|u|),
    u'=lambda u+o(|s|+|u|),                            (4)

uniformly in theta. The regular H-level in this tube is one graph

    s=phi(theta,u), phi(theta,0)=0,
    partial_u phi(theta,0)=0,
    |phi(theta,u)|<=epsilon(delta)|u| for |u|<=delta,
    epsilon(delta)->0.                                (5)

Compactness of gamma makes the graph and estimates uniform in phase. These are local implicit-function and Floquet statements for a C2 vector field and C2 H; no higher smoothness is assumed.

On the box Q_delta={|s|<=delta, |u|<=delta}, the field points strictly outward through either u-face for small delta, by (4). An orbit lying in this H-level never touches an s-face while in the box, because (5) gives |s|<delta. It therefore cannot enter Q_delta from outside: any first crossing would occur at an s-face, which its level excludes, or at an outward u-face, which the differential equation excludes. Corners are also excluded by (5).

If such an orbit begins inside Q_delta and is not gamma, then u!=0, since u=0 in (5) gives s=0. Along the segment inside the box, (4)-(5) give

    d|u|/dt >= (lambda/2)|u|.                          (6)

It exits in finite forward time through a u-face and can never reenter. In particular, a nonconstant orbit contained in this H-level cannot have gamma in its omega-limit set. Our L+ lies in the level and has W!=0, whereas W=0 on gamma, so it cannot coincide with gamma. This contradicts gamma subset K and proves conclusion1.

This corrects a direction error in the source wording: no-entry implies that the times in the box form an initial segment after a chosen starting time, not automatically a terminal segment. Accumulation would force perpetual residence, which (6) excludes unless the orbit is gamma. No unsupported inference from repeated visits to membership in a stable manifold is needed.

## 4. Local no-entry lemma at an equilibrium

Let q in K be an equilibrium with rho simple and DB(q) hyperbolic. Write F=DB(q). By (2), F^T U(q)=rho U(q), with U(q)!=0. The invariant real generalized eigenspace E' for the other two eigenvalues is contained in U(q)^perp: if v belongs to a generalized eigenspace for lambda!=rho, then applying U(q)^T to (F-lambda I)^m v=0 gives (rho-lambda)^m U(q).v=0. Dimension gives E'=U(q)^perp. The rho-eigenline is transverse to E' because rho is simple.

Suppose both other eigenvalues have positive real part. In the corresponding local linear coordinates (s,z) in R times E',

    s'=rho s+o(|s|+|z|), z'=F' z+o(|s|+|z|),           (7)

where F'=F restricted to E'. The regular H-level through q is a graph s=phi(z), with phi(0)=0 and Dphi(0)=0, because grad H(q)=-aU(q). Thus |s|<=epsilon(delta)|z| on this graph near0.

There is a positive definite quadratic norm on E' in which the F' flow expands strictly. Explicitly set

    M=integral_0^infinity exp(-t F'^T)exp(-t F') dt.

It converges because the real parts of the eigenvalues of F' are positive, and F'^T M+M F'=I. Therefore, in the norm |z|_M=(z^T M z)^(1/2), (7) on the level gives

    d|z|_M/dt >= eta |z|_M

for some eta>0 in a sufficiently small neighborhood. The same no-entry argument with a product box {|s|<=delta, |z|_M<=delta} shows that a nonconstant orbit contained in the level cannot accumulate at q. The H-level graph avoids the stable faces, and the z-boundary is outward. This contradicts q in K. Consequently at least one of the other eigenvalues has negative real part. Hyperbolicity excludes zero real parts. Their real sum is 3c-rho>0, so they are a real negative-positive pair. This proves conclusion2.

If DW(q)!=0, A469 gives the two alternatives displayed in B32:

    {rho,rho+kappa,-a-2rho},
    {rho,(-a-rho)/2,(1+4c-rho)/2}.                     (8)

Use rho<=-a, not merely rho<0. In the second family the middle entry is nonnegative and the last is positive; hyperbolicity excludes the zero case rho=-a. Thus both other eigenvalues would be positive, contradicting conclusion2. In the first family -a-2rho>=a>0, so the negative other entry must be rho+kappa<0. This gives conclusion3. The source's phrase that both entries in the second family are positive for every rho<0 needs this stronger inherited hypothesis and the hyperbolicity exclusion of rho=-a.

## 5. The pointwise limit-set claim still needs a proof

The earlier source version concluded that every orbit in K has alpha- and omega-limit sets contained in the equilibrium set, because its limit sets carry invariant probabilities and all such probabilities are mixtures of equilibrium atoms. This reasoning does not establish the stated containment. An invariant probability need not have full support on the limit set that carries it. In particular, a limit set can contain connecting trajectories whose points all have zero mass for every invariant probability.

LIT132 gives a fully explicit complete smooth constant-divergence example of precisely this measure-support gap. The example is not an Euler field and is not used to refute the stronger Euler conclusion. It shows why the displayed measure argument cannot prove that conclusion. To upgrade the conclusion for the actual K one would need an additional theorem using its geometry or recurrence, with all required hypotheses checked. Neither the local no-entry arguments above nor the B32 measure classification supplies such a theorem.

The exact safe conclusion is: K is compact connected and invariant, is irrotational and lies in the vortical closure, carries only equilibrium ergodic probabilities once B32 and conclusion1 are established, and has the local spectral restrictions of conclusions2-3. Its remaining nonstationary points and their limit sets are not classified here.


## 6. All equilibrium companions have a nonexpanding second direction

The restriction to simple rho and a hyperbolic F can be removed for the weaker index conclusion. Let q be any equilibrium in K and set ell=U(q)^T. The plane E'=ker ell is invariant under F=DB(q), and F induces multiplication by rho on the quotient. Thus

    trace(F restricted to E')=3c-rho>0.

If rho is an eigenvalue of F restricted to E', that plane already has a negative eigenvalue. Otherwise rho is a simple eigenvalue of F, so the invariant decomposition used in Section4 exists. If both eigenvalues on E' had positive real part, the same positive definite quadratic norm and no-entry proof would give a contradiction. Consequently at least one eigenvalue has nonpositive real part. The positive trace rules out a nonreal conjugate pair and gives

    eigenvalues(F restricted to E')={lambda_-,lambda_+},
    lambda_-<=0<lambda_+, lambda_-+lambda_+=3c-rho.

Under hyperbolicity lambda_-<0. This reasoning includes repeated eigenvalues and does not assume DW(q)!=0.

## 7. What the measure classification actually implies

Assume the B32 measure classification as a separate input. Together with Section3, it says that every ergodic invariant probability on K is a point mass at an equilibrium in E=K intersect{B=0}. Ergodic decomposition therefore puts every invariant probability on E. Such a probability need not be atomic if E is infinite.

Every nonempty compact fully invariant subset of K carries an invariant probability, obtained by weak limits of time averages. At least one ergodic component is an equilibrium atom, so every such subset meets E. Applying this to alpha(x) and omega(x) gives nonempty intersections with E for every x in K, not containment in E. Every compact minimal subset is one equilibrium, since it contains an equilibrium orbit.

There is also a uniform time-average statement. If f is continuous on K and f=0 on E, then

    sup_(x in K) |(1/T) integral_0^T f(Phi_t x)dt| ->0.

Otherwise take x_n in K and T_n tending to infinity with a fixed nonzero lower bound. A weakly convergent subsequence of the empirical probabilities exists by compactness. For every fixed s, their integrals against phi composed with Phi_s minus phi are bounded by 2|s| ||phi||infinity/T_n, so the limit is invariant. It is supported on E and hence has integral f=0, a contradiction. For any open neighborhood N of E in K, choose a nonnegative continuous f equal1 on K minus N and zero on E. The fraction of time spent outside N tends to zero uniformly on K. This permits infinitely many excursions and does not classify pointwise limit sets.

## 8. A finite hyperbolic network cannot be the whole limit set

Assume in addition that K is the union of finitely many hyperbolic equilibria and finitely many nonconstant connecting orbits, each having a single equilibrium as its alpha-limit and a single equilibrium as its omega-limit. Homoclinic connections are allowed. Then K consists of one equilibrium q and L+ tends to q. No finite-network structure is deduced from Section7.

By (3), choose an open neighborhood N of K on which grad H never vanishes. Let Sigma={H=H(p)} intersect N. It is a C2 surface. Define on it the C1 tangent vector field

    X=B-[(B.grad H)/|grad H|²]grad H.

On K and on the late part of L+, g=0, so X=B. At an equilibrium q, for z tangent to Sigma one has

    D(B.grad H)(q)z=grad H(q).Fz=0,

because F preserves E'=T_q Sigma. Consequently DX(q) restricted to T_q Sigma equals F restricted to E'. Section6 and hyperbolicity give the real eigenvalues -beta_q<0<lambda_q, with

    lambda_q-beta_q=3c-rho>0.                       (9)

Thus each q is an expanding saddle of this surface field.

Choose local C1 coordinates adapted to the two eigenlines. The C1 stable-manifold theorem gives stable and unstable curves with graph functions h_s(y),h_u(x), both with derivative0 at the origin. Use the simultaneous coordinate change

    xi=x-h_s(y), eta=y-h_u(x).

Its derivative at the origin is the identity, so it is a local C1 diffeomorphism. Its transformed xi equation is X_x-h_s'(y)X_y. This vanishes when x=h_s(y), by invariance of the stable curve. Holding y fixed and applying the mean-value theorem to the original C1 components therefore factors the equation as xi times a continuous coefficient tending to lambda_q. The eta equation is treated with x fixed and the unstable graph. No differentiability of the transformed field beyond these component factorizations is assumed. We obtain

    xi'=xi(lambda_q+r_1), eta'=eta(-beta_q+r_2),
    r_i ->0 at q.                                   (10)

Choose epsilon>0 so small that theta_q=(beta_q+epsilon)/(lambda_q-epsilon)<1, and a coordinate box |xi|,|eta|<=delta where |r_i|<=epsilon. A nonseparatrix orbit entering at |eta|=delta, |xi|=r>0 leaves at |xi|=delta. Its passage time obeys

    T<=[log(delta/r)]/(lambda_q-epsilon).

The eta equation gives the lower bound for the outgoing distance to the unstable separatrix:

    |eta(T)|>=delta exp(-(beta_q+epsilon)T)
               >=delta^(1-theta_q)r^theta_q.          (11)

All these are inequalities for the actual surface flow; no linearization or asymptotic equivalence is required.

Choose disjoint saddle boxes, small enough that each connecting arc has one outgoing section at its alpha endpoint and one incoming section at its omega endpoint. The part of each connection between these sections is compact and contains no zero of X. There are finitely many such arcs. Their thin flow tubes induce C1 maps between transverse sections with nonzero derivative at the connection point, so each map multiplies a sufficiently small transverse distance by a factor bounded below by a positive constant. The finitely many constants can be made uniform.

Since dist(L+(t),K) tends to zero, its late trajectory stays in the union of these boxes and tubes. If it makes infinitely many saddle passages, let r_n be the positive incoming transverse distances. The finite section choices and dist(L+(t),K)->0 imply r_n->0. Equation(11) and the transition bounds imply, for a fixed C>0 and theta=max_q theta_q<1,

    r_(n+1)>=C r_n^theta                              (12)

once r_n<1 and all passages are sufficiently late. Taking the maximum exponent weakens the lower bound correctly for r_n<1. For small r, C r^theta>=2r, so (12) would make r_n eventually increase by a factor at least2 at each passage, contradicting r_n->0. If an incoming distance is exactly0, uniqueness makes the orbit stay on that saddle's stable curve and converge to it, which already gives a singleton K.

If there are only finitely many saddle passages, the late trajectory remains in one box and converges to its saddle by (10), again giving a singleton K. Therefore K cannot contain a connecting orbit. It is connected, since it is the intersection of decreasing compact closures of connected forward tails of L+. A finite connected set of equilibria is one point. This proves the stated conditional conclusion, including hyperbolic equilibria with DW=0.

The source's revised Section4c reproduces this narrower finite-network argument and correctly withdraws the earlier general orbitwise claim. Infinite networks, nonhyperbolic equilibria and arbitrary compact equilibrium sets remain outside the conclusion. This section is independently reconstructed and confirmed only with its explicit finite-network hypothesis.

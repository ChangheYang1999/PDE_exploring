# Degenerate tails with controlled nodal surfaces

Status: CONFIRMED as the surface and zero-free cases of A547, including the separate pressure mean. Full own postreads and the exact imported weighted-Harnack hypotheses are checked. Its underlying FKS proof remains imported.

## 1. Statement and notation

Let 2/5<c<1/2, omega in R, a=1-2c, p=(1-c)/c in(1,3/2), beta=a/[2(1-c)]=(p-1)/(2p) in(0,1/6). Put A=cI-omega J, Q_t=exp(omega tJ), J(x1,x2,x3)=(-x2,x1,0), and D=R3 minus{0}. Let V in C1(D;R3) and S in C1(D;R) satisfy, with W=curl V,

    div V=0,
    V(exp(tA)x)=exp(-(1-c)t)Q_t^T V(x),
    S(exp(tA)x)=exp(-2(1-c)t)S(x),
    Ax cross W=aV, W.grad S=0.                       (1)

Assume that each zero x0 of S has a C1 coordinate chart x=Phi(z), from a cube centered at0 onto a neighborhood of x0, such that on a smaller cube both DPhi and its inverse are bounded and

    C0^(-1)|z3|^m <= |S(Phi(z))| <= C0|z3|^m,
    m>=1, eta=m beta<1.                              (2)

The constants, exponent and chart may vary with x0. The zero set may be empty. The conclusion is V=0.

In particular this applies when every zero is regular, since the inverse function theorem permits z3=S and m=1. It also applies when every zero has the full two-sided surface behavior (2) with m<=6. No condition (2) is inferred from C1 regularity, analyticity, a finite derivative at one point or the Euler equation. The hypothesis concerns a neighborhood of each entire local zero surface.

For an actual Euler tail the intended scalar is S=P2-|V|²/2. The extra assumption Ax cross W=aV means E=grad((Ax).V)=0 on all D. A local E=0 region around one limiting sheet does not suffice for this theorem. The actual pressure and velocity tail limits are separate inputs.

## 2. Closed integrating factor and global weak potential

Differentiating the homogeneity of S gives Ax.grad S=-2(1-c)S. Taking the scalar product of Ax cross W=aV with Ax gives Ax.V=0. The vector triple-product identity, using W.grad S=0, gives

    grad S cross V=(S/beta)W.                        (3)

For epsilon>0 set mu_epsilon=(S²+epsilon²)^(-beta/2). Product differentiation gives the exact identity

    curl(mu_epsilon V)
       =epsilon²(S²+epsilon²)^(-beta/2-1)W.           (4)

Off S=0, therefore, G=|S|^(-beta)V is curl-free.

Condition (2) makes the zero set locally one C1 surface, hence a null set in three dimensions. On a zero chart,

    |G|<=C|z3|^(-eta), |S|^(-beta)|W|<=C|z3|^(-eta).

These functions are locally integrable because eta<1. In fact G belongs to Lq on the chart for every 1<q<1/eta. Every compact set has a finite covering, so one q>1 works on that compact set. A global common q is not assumed.

The right side of (4) tends pointwise to zero off the null zero set and is bounded by |S|^(-beta)|W|. Also |mu_epsilon V|<=|S|^(-beta)|V| and mu_epsilon V tends almost everywhere to G. Dominated convergence on each compact set therefore gives curl G=0 distributionally on all D. This step explicitly rules out a curl measure concentrated on the nodal surface.

A closed Lq field on a ball has a W1q potential: mollify on a slightly larger ball, integrate the smooth closed fields, normalize their means, and use the ordinary Poincare inequality to obtain a convergent W1q sequence. Potentials on connected overlaps differ by constants. Since R3 minus{0} is simply connected, these constants can be matched to give a single global weak potential psi, with

    grad psi=G almost everywhere.                    (5)

Path independence can be checked on a homotopy of a loop by subdividing it into finitely many coordinate balls; the additive differences telescope around each small loop. Thus psi belongs to W1q locally for some q>1 on every compact set. At these exponents ordinary Sobolev embedding alone need not give continuity.

## 3. Continuity through a higher-order surface

In a smaller zero chart put u(z)=psi(Phi(z)). The weak chain rule and bounded DPhi give

    |Du(z)|<=C|z3|^(-eta) almost everywhere.           (6)

Away from z3=0 its weak gradient is continuous, so u has a C1 representative on each side. Integration along vertical segments shows that the limits u_+(z') and u_-(z') exist uniformly on smaller horizontal cubes, with

    |u(z',s)-u_+(z')|<=C s^(1-eta), s>0,
    |u(z',s)-u_-(z')|<=C |s|^(1-eta), s<0.            (7)

For two horizontal points a distance d apart, compare their values first at height d. The vertical errors are O(d^(1-eta)), and the horizontal segment contributes at most Cd*d^(-eta). This gives continuous, locally Holder traces of exponent 1-eta on both sides.

The traces agree. The W1q function u is absolutely continuous on almost every vertical line through the entire cube. On each such line its derivative is bounded by the integrable majorant in (6), so it cannot have a jump at0. Thus u_+=u_- almost everywhere; their continuity gives equality everywhere. Equations (7) give a continuous representative across the surface. The representatives agree on overlaps, and psi is continuous on D.

When zeros are regular, beta<1/6 already allows G in L4 and ordinary W1,4 embedding. The argument here covers the larger eta<1 range without that high exponent.

## 4. The exact weighted energy class

Set b=|S|^beta. Since b grad psi=V almost everywhere and div V=0,

    div(b grad psi)=0                                (8)

in distributions. On a zero chart b is comparable to |z3|^eta. The continuous psi is locally bounded, and

    b|grad psi|²=|S|^(-beta)|V|²<=C|z3|^(-eta),        (9)

so its weighted energy is finite. The Harnack source uses the completion of Lipschitz functions in that norm. Finite energy alone is not used as a substitute for membership in that completion.

Here is a concrete approximating sequence on a smaller cube. Leave u unchanged where |z3|>=epsilon; inside the band interpolate linearly between u(z',-epsilon) and u(z',epsilon). Denote the result by u_epsilon. The tangential derivatives at either boundary plane are O(epsilon^(-eta)) by (6). The normal derivative of the interpolant has the same bound by (7) and the common trace. The pieces agree at the two planes, so u_epsilon is Lipschitz on the smaller cube, with a constant allowed to depend on epsilon.

Its uniform error is O(epsilon^(1-eta)). The gradient difference is confined to the band and obeys

    integral |z3|^eta |Du_epsilon-Du|²
      <=C integral_0^epsilon s^eta
                       (epsilon^(-2eta)+s^(-2eta))ds
      <=C epsilon^(1-eta) ->0.                       (10)

The weighted function norm also converges. Composition with the bi-Lipschitz chart preserves these estimates up to constants. Restriction to a ball or multiplication by a fixed cutoff supplies local weighted-energy membership on the domains used below.

The weak equation is valid for compactly supported Lipschitz tests: ordinary mollification approximates any such test in unweighted W1,2, and the coefficient b is bounded on compact sets, so the approximation also converges in the weighted energy norm. It then extends by Cauchy-Schwarz to the completion of compactly supported Lipschitz tests. This verifies the exact weak-solution class of the primary source.

## 5. The imported Harnack theorem and its local hypotheses

The primary source is E. B. Fabes, D. S. Jerison and C. E. Kenig, The Wiener test for degenerate elliptic equations, Annales de l'Institut Fourier32(3)(1982),151-182, DOI10.5802/aif.883. Its actual retained PDF was read at printed pages151-156. Page152 assumes measurable real symmetric coefficients comparable above and below to wI, with w satisfying A2 or QC. Pages154-155 define H1,2 as the weighted completion of Lipschitz functions and define weak solutions. Page155 gives local Holder continuity, and equation(1.9) on page156 gives max on the inner ball <=C min there for a nonnegative solution on the doubled ball. The stated result is imported. FJK attributes it to Fabes-Kenig-Serapioni, Comm. PDE7(1)(1982),77-116, Section2.3.8; that underlying proof has not been independently reconstructed here.

For (8), the C1 coordinate map gives the symmetric coefficient

    b(Phi(z)) |det DPhi(z)| DPhi(z)^(-1)DPhi(z)^(-T).
                                                               (11)

By (2) and the bounded inverse Jacobian, (11) is comparable to |z3|^eta I. The reference weight w(z)=|z3|^eta is A2 when |eta|<1. Indeed, if the center of a ball has height at least twice its radius, w and its reciprocal are comparable to their center powers. Otherwise their integrals over the ball are bounded by its horizontal area times the one-dimensional integrals on(-3r,3r). Their averages are at most Cr^eta and Cr^(-eta), respectively; their product is bounded. Both integrals converge because |eta|<1.

The bounded positive matrix factor in (11) can be defined to be the identity outside the smaller coordinate neighborhood. This yields a measurable symmetric coefficient globally comparable to the same A2 weight and leaves the local doubled-ball equation unchanged. Section4 supplies the required completed weighted energy space and test identity after coordinate change. At points where S is nonzero, use a ball on which b is bounded above and below and take reference weight1. No assertion about an arbitrary critical-zero weight is used.

## 6. A global maximum exists and forces constancy

Equations Ax.V=0 and (5) give Ax.grad psi=0 almost everywhere. Acting on a local W1q function by the smooth linear flow and using smooth approximation gives

    psi(exp(tA)x)=psi(x)

for almost every x at each fixed t. Both sides have continuous representatives by Section3, so the equality holds for every x. The radius of exp(tA)x is exp(ct)|x|. Every point can therefore be moved to the unit sphere. Since psi is continuous on that compact sphere, it attains a finite global maximum M on D.

The function M-psi is nonnegative and satisfies the same weak equation. At a maximum point, Section5 gives Harnack on a small doubled ball, in zero coordinates when necessary. Its inner infimum is zero, so its inner supremum is zero. Hence the maximum set is open. It is nonempty and closed as well, and D is connected. Thus psi is constant, G=0 almost everywhere and V=0 everywhere by continuity.

For nonzero V, at least one zero must violate (2). A linear spiral map exp(tA) transports (2), or its failure, to the image point: it composes the chart and multiplies S by a positive constant, without changing m beta. A failed zero therefore exists on each centered sphere. This proves the stated scope and its regular-zero corollary.

## 7. The pressure equation forces a negative mean deficit

This is a separate conclusion requiring the pressure equation. Suppose (1) holds with S=P2-|V|²/2 and -Delta P2=partial_i partial_j(V_i V_j) on D. Denote angular integrals on the unit sphere by

    R0=integral V_r², T0=integral |V_T|², P0=integral P2.

Twisted homogeneity and invariance of angular measure under rotations make their radius dependence r^(-2p). Test the distributional pressure equation against a smooth radial chi supported in an annulus. Its radial Hessian gives

    -P0 integral r^(2-2p)(chi''+2chi'/r)dr
       =R0 integral r^(2-2p)chi''dr
          +T0 integral r^(1-2p)chi'dr.

Two integrations by parts, with no endpoint terms, imply

    P0=[(2-2p)R0-T0]/(2p),
    integral_(S²) S=[(2-3p)R0-(p+1)T0]/(2p).         (12)

The coefficient 2p-1 divided out in this calculation is nonzero. If V is nonzero, twisted homogeneity implies it is nonzero somewhere on the unit sphere, so R0+T0>0. Since p>1, the last expression is strictly negative. Thus S has a negative point on every sphere. Independently, the empty-zero case of the theorem says that a nonzero V must have a zero. No positivity, sign change or regularity of that zero follows from this mean identity.

The argument in Sections2-6 does not use (12) or any pressure equation. Section7 uses it explicitly. A nonzero field with an artificial first integral may evade the nodal hypothesis and still fail the pressure equation; the endpoint countertest is in the adjacent topic folder.

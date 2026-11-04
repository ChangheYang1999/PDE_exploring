# Vanishing vorticity at finite-order scalar nodes

Status: CONFIRMED A721-A722 after the full source, dependency and postwrite reads.

## 1. Exact theorem and dependencies

Let 2/5<c<1/2, omega be any finite real number, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, p=(1-c)/c and eta=(p-1)/(2p). Suppose U in C2(R3;R3), P in C1(R3) satisfy

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0 everywhere,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1).

Here C is finite, with no uniformity in omega required. Let V,W,P2 be the actual velocity, vorticity and canonical pressure tails from the confirmed scattering construction. On S2 set h=P2-|V|^2/2, G=W and Z={h=0}. Assume G=0 on all of Z.

Assume Z has a finite cover by smaller neighborhoods in smooth angular coordinate charts, with bounded first derivatives of charts and inverses and positive upper and lower bounds on area Jacobians. In each chart one of the following holds, with positive finite constants and exponents specific to that chart:

(C) Z={u=0}, |h(u,v)|>=b|u|^m, and m eta<2.
(P) Z={(0,0)}, |h(u,v)|>=b(u^2+v^2)^(m/2), and m eta<3.
(X) Z={uv=0}, |h(u,v)|>=b|u|^(m1)|v|^(m2), and

    max(m1 eta-1,0)+max(m2 eta-1,0)<1.

Then U=0. Empty Z is permitted. The separate h identically zero branch is covered by the pressure mean in A707 and needs none of these chart hypotheses. The natural bounds can be supplied by U->0 and DU=O(sqrt(|x|)) through A601, with global zero helicity still imposed.

The two substantive inputs are A533, which gives G in C^alpha(S2) for every 0<alpha<1, and A705-A706, which give actual-profile nonexistence if

    G=0 almost everywhere on {h=0},
    integral_{h!=0}|G||h|^(-eta)dA<infinity.          (1)

The complete independent proofs of A533 and A705-A708 were reread for this audit. The latter uses the actual volume-preserving partial W flow and finite-time core return, not a global flow through the origin or an abstract tail equation alone. The proof below verifies exactly(1).

## 2. General normal-coordinate estimate

In a two-dimensional chart, let the zero set be a smooth submanifold of codimension j=1 or2. Write z in R^j for its normal variables and y for the remaining variables. Suppose

    |h(z,y)|>=b|z|^m, |G(z,y)|<=B|z|^ell, ell>=0.

Off the zero set, the integrand in(1) is at most C|z|^(ell-m eta). The area density is bounded above. Polar integration in the j normal variables reduces convergence to

    integral_0^rho r^(j-1+ell-m eta)dr<infinity,

which holds if m eta<j+ell. This is a sufficient test. Equality is not covered, and an upper bound on G does not justify a converse, since G may vanish faster.

Similarly, if |h|>=b product_i|z_i|^(mi) and |G|<=B product_i|z_i|^(elli) for one or two independent scalar coordinates, Fubini gives integrability when mi eta<1+elli for each factor. We use this elementary product test at a crossing.

## 3. Curve and isolated-point charts

The compact sphere and A533 give a finite Holder constant for G for each fixed alpha<1. In a smaller curve chart, replace u by0 while keeping v fixed. This point is in Z and remains in the larger chart. Since the chart has bounded derivative and G vanishes on Z,

    |G(u,v)|<=C_alpha |u|^alpha.

In a point chart compare directly to its center to obtain |G(z)|<=C_alpha|z|^alpha. These comparisons require no smooth nearest-point projection of a general global zero set.

For a curve choose 0<alpha<1 with m eta<1+alpha, possible precisely under the stated strict bound m eta<2. For a point choose alpha with m eta<2+alpha, possible under m eta<3. Section2 proves local integrability. We do not take alpha=1 or infer a uniform Lipschitz estimate from the family of Holder estimates.

## 4. A transverse two-curve crossing

Put a1=m1 eta, a2=m2 eta and E=max(a1-1,0)+max(a2-1,0). Choose E<alpha<1. There exist nonnegative ell1,ell2 with

    ell1+ell2<alpha, ell1>a1-1, ell2>a2-1.

Indeed start with the two positive parts defining E and add sufficiently small positive increments. If an a_i<1, zero is also permitted for that ell_i, since its required inequality is already strict.

Comparing to either coordinate axis yields

    |G(u,v)|<=C_alpha min(|u|,|v|)^alpha.

Shrink so both absolute coordinates are below1. With rmin=min(|u|,|v|),

    rmin^alpha<=rmin^(ell1+ell2)<=|u|^ell1 |v|^ell2.

Consequently the weighted integrand is bounded by C|u|^(ell1-a1)|v|^(ell2-a2). Each exponent is strictly greater than-1, so the product test proves its local integrability. This includes a1=a2=1, with any chosen positive Holder exponent.

## 5. The finite cover and exact critical examples

The finite charts cover all of compact Z. On the compact complement of their union, continuous |h| has a positive minimum and G is bounded. The weighted integral is therefore finite everywhere off Z. The assumed G=0 on Z supplies the remaining clause of(1). A705-A706 prove U=0. In these charts Z also has area zero, but the proof does not need to replace the explicit pointwise vanishing by that measure fact: it is the pointwise vanishing that supplied the Holder gain.

The distinction from an unweighted reciprocal condition can be tested by exact local scalar examples. They are not asserted Euler tails. At a curve take h=|u|^(1/eta) and |G|=|u|^alpha, alpha>0. The reciprocal is1/|u| and diverges; its product with |G| has exponent alpha-1 and converges. At an isolated point take h=|z|^(2/eta), |G|=|z|^alpha. The unweighted radial integral is integral dr/r, while the weighted one is integral r^(alpha-1)dr.

At a crossing take h=|uv|^(1/eta), |G|=min(|u|,|v|)^alpha. The unweighted reciprocal1/|uv| diverges. On the sector0<u<v<rho the weighted integral is exactly

    integral_0^rho v^(-1) integral_0^v u^(alpha-1)du dv
       =rho^alpha/alpha^2.

All eight ordered sign sectors have the same finite value. No vector curl, pressure or profile realization is claimed for these scalar tests.

## 6. Scope and verification

This is a conditional theorem for actual globally helicity-free profiles with natural rates. It uses neither vorticity density nor A2. It retains the vanishing of G at every scalar node, the finite cover and explicit finite-order lower bounds. Flat nodes, tangent crossings, cusps and the endpoint upper bounds m eta=2 in(C) or3 in(P) are not decided by this argument. The strictness of the stated Holder choices is essential to this proof; no optimality theorem for actual profiles follows.

The kinematic sharpness example of A710-A711 has G nonzero at its critical isolated scalar nodes, so it violates the premise here. There is no conflict with its logarithmically divergent weighted critical moment. No computation or formal build is needed. The current LIT177 submission is pinned and hashed in verification. Existing configured-model comparison of the flux and node criteria is requested through working files; a pending request is not counted as a response.

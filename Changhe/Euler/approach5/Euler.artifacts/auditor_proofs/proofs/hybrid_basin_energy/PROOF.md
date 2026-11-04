# Bernoulli rewrites, basin flux, and weighted remainder energy

## Statement, notation and dependencies

This audits Theory Agent A C30, in the team records. Assume a C2 divergence-free profile U on R3, bounded and distributionally vanishing at infinity in the Theorem T sense, with the Dini gradient hypothesis of A209-A210, 2/5<c<1/2 and any real omega. Uniform decay implies the stated boundedness and vanishing condition. Write

    A=cI-omega J, b(y)=Ay, B=b+U,
    delta=1-2c, k=(1-c)/c, alpha=3-2k, gamma=(5c-2)/2,
    V=the scattering velocity tail, W=U-V,
    Omega=curl U, Omega_tilde=curl V, omega_W=curl W,
    e=|U|^2/2, q=P+e, H=q+b.U, tau=b.V,
    f=-V.(Omega cross U)=W.(Omega cross U)=W.(Omega cross V).

Use canonical pressure unless otherwise stated. A209-A210 give the scattering map S, compact null core K, continuous V and Omega_tilde off zero, their twisted homogeneities, div V=0, and

    delta U+Omega cross B+grad H=0,
    delta V+Omega_tilde cross b+grad tau=0.

The second identity gives tau in C1 even though the full gradient of V need not be continuous. A250 and A275 give

    W in L2, f in L1,
    J_E=b|W|^2/2+qW,
    div J_E=gamma|W|^2-f in distributions on R3,
    integral f=gamma||W||_2^2,
    integral_{B_R}V.W -> -||W||_2^2/2.

A355 supplies the normalized Weber identity. All new calculations below are conditional on these exact inputs. No basin energy sign or profile exclusion is concluded without the additional sign inequality stated in Section4.

## 1. Regularity needed for the algebra

On compact annuli, V and curl V are continuous and div V=0. The local div-curl estimate gives V in W1,p on smaller annuli for each finite p. For clarity this follows by cutting off V: the curl and divergence of the compactly supported cutoff field belong to Lp; the identity

    -Delta v=curl curl v-grad div v

and the Lp bounds for order-zero Riesz products control Dv. The harmonic localization remainder is smooth. This is the same local div-curl input used in the already confirmed A250 proof. Thus all products below can be derived by smooth approximation on annuli. Products involving grad tau are continuous there.

Near zero, |V|=O(r^-k), |Omega_tilde|=O(r^(-k-1)), |tau|=O(r^(1-k)), |grad tau|=O(r^-k), and U, Omega, P are bounded. Twisted homogeneity also gives the annular integral bound

    integral_{r<|y|<2r}|DV|dy <= C r^(2-k).

To see this, rescale by exp(sA) with exp(cs)=r. Its rotations preserve the annulus and the Jacobian is r3, while DV has degree -k-1. The bound at unit scale follows from W1,p. Summing dyadic annuli proves DV is integrable at zero since k<2. The surface flux of V is bounded by C r^(2-k), tending to zero, so its global weak derivative has no point defect. We never assume a pointwise bound for all components of DV.

The algebraic terms in the Bernoulli rewrite below are O(r^-2k), hence integrable at zero because 2k<3. The exceptional product U_i U_j partial_j V_i is also integrable globally: near zero use bounded U and the annular derivative estimate; at infinity combine that estimate with U=O(r^-k), giving summable annular bounds C R^(2-3k). These justifications also make the third divergence identity below meaningful on all of R3.

## 2. Exact identities and their boundary terms

Twisted homogeneity gives (b.grad)V=-(1-c)V-omega JV. Therefore

    curl(b cross V)=-3cV+AV-(b.grad)V=(1-3c)V.              (1)

Dot the profile Lamb identity with V and subtract the tail Lamb identity dotted with V. The result is

    f=delta V.W+V.grad(H-tau)+V.(omega_W cross b).          (2)

Using (1) and the vector product rule,

    V.(omega_W cross b)
       =div[W cross(b cross V)]+(1-3c)V.W,
    W cross(b cross V)=b(V.W)-V(b.W).

Since H-tau-b.W=q and div V=0, (2) reduces to

    f=(2-5c)V.W+div G, G=b(V.W)+qV.                       (3)

The absolute surface fluxes of G, J_E, (H-tau)V and W cross(b cross V) at radius r are at most

    C(r^(3-2k)+r^(2-k)),

which tends to zero. This and Section1 remove the origin from the distributional derivation without a point source. Integrating (3) over the radius-R ball gives

    cR integral_{|y|=R} V.W + integral_{|y|=R}q V_r
       =integral_{B_R}f+(5c-2)integral_{B_R}V.W ->0.       (4)

Only the sum is proved to tend to zero. The exact relation

    G+J_E=b(e-|V|^2/2)+qU,
    div(G+J_E)=gamma(|U|^2-|V|^2)

shows that the rewritten equation is the original energy identity minus the homogeneous tail-energy identity.

For later use, integrating the convective derivative by parts gives a third exact expression,

    f=U_i U_j partial_j V_i+div[eV-(U.V)U].                (5)

For example, (Omega cross U)=(U.grad)U-grad e; expand -V.(U.grad)U by the product rule and use both divergences zero. The current in (5) has absolute sphere flux O(r^(2-k)) at zero and O(R^(2-3k)) at infinity. Both vanish. These global sphere statements do not prove that its flux through an invariant basin boundary vanishes.

## 3. The three-term tail identity

Dot the tail Lamb equation with V and integrate. The small-sphere flux of tau V is O(r^(3-2k)), so

    delta integral_{B_R}|V|^2
      +integral_{|y|=R}tau V_r
      +integral_{B_R}V.(Omega_tilde cross b)=0.            (6)

The first two terms do not cancel in general. At omega=0, tau=cR V_r on the sphere, so both are nonnegative. An exact tail countertest is

    V(y)=|y|^(-k-1)(v0 cross y), v0!=0, omega=0.

It is solenoidal, homogeneous of degree -k, nonzero, and tau=0; its linear tail Lamb identity follows directly from the vector identity for grad(y.V). The last term of (6) is then necessary.

In fact,

    V.(Omega_tilde cross b)
      =(1-3c)|V|^2+div[b|V|^2-tau V].

Substitution in (6) cancels the explicit tau terms and leaves

    (2-5c)integral_{B_R}|V|^2+cR integral_{|y|=R}|V|^2=0.

This is exactly homogeneity, since integral_{B_R}|V|^2=L R^alpha and c alpha=5c-2. The cancellation does not say that the energy quantity is independent of V: V fixes both tau and W.

## 4. Basin flux and Weber decomposition

For any open D and chi in C_c^infinity(D), (2)-(3) give

    integral chi f
      =delta integral chi V.W+integral chi V.(omega_W cross b)
         -integral(H-tau)V.grad chi
      =-2gamma integral chi V.W-integral G.grad chi.

No separate limit of these terms follows from the centered-ball limit in A250. The convergent basin identity is

    N_D:=integral_D f=gamma integral_D|W|^2-b_D,
    b_D=-lim_j integral J_E.grad chi_j,

where 0<=chi_j<=1, chi_j in C_c^infinity(D), and chi_j->1_D pointwise. The limit exists and is independent of this exhaustion because div J_E is integrable and integration by parts reduces it to dominated convergence.

Off K union {0}, put kappa=tau composed with S, phi=(H-kappa)/delta and Z=DS^T(V composed with S)-V. A355 gives W=Z-grad phi. Expanding |Z|^2 and using div W=0 yields, for nonnegative compactly supported chi in this punctured part of D,

    integral chi|W|^2
      =integral chi|Z|^2-delta^-2 integral chi|grad(H-kappa)|^2
          +(2/delta)integral(H-kappa)W.grad chi.           (7)

Every term here is locally finite. Only W, not Z and grad phi separately, is known globally square integrable near K. The negative Dirichlet term is accompanied by a positive deformation term and a flux, so (7) gives no sign for N_D.

If D is invariant under the complete B flow and psi is C1 with compact support, change of variables gives

    integral_D psi(Phi_t y)exp(3ct)dy=integral_D psi,

hence integral_D div(B psi)=0. The analogous statement holds for Omega chi on a vortex-invariant D, using volume preservation. For noncompact or singular multipliers the cutoff errors must be checked separately.

Precisely, if A0=B psi+Omega chi is locally integrable, div A0 belongs to L1(D), and integral_D div A0=0, replacing J_E by J_E+A0 leaves b_D unchanged. Indeed the change in b_D is the integral of div A0, by the same cutoff argument. The zero-integral premise is essential; integrability of the divergence alone is not being substituted for it.

On a regular boundary patch tangent to B and Omega, b.n=-U.n, and direct expansion gives

    J_E.n=(P+U.V-|V|^2/2)U.n-qV.n,
    G.n=-(U.n)(V.W)+qV.n,
    (G+J_E).n=(P+|V|^2/2)U.n.

Adding the invariant currents changes none of these normal components. Invariance does not force either U.n or V.n to vanish. No estimate for these remaining terms has been proved.

For pairwise disjoint countably many invariant open essential basins covering almost every vortical point, the additional inequality

    b_D>=gamma integral_D|W|^2, equivalently N_D<=0,       (8)

on every basin would imply U=0. To verify the implication, absolute integrability of f and W2 allows summation and gives

    sum_D b_D=-gamma integral_{complement of union D}|W|^2<=0.

Under (8) every summand is nonnegative, so all energies, including that of the complement, vanish. Thus W=0 almost everywhere and, by continuity away from zero, U=V there. A bounded homogeneous field of negative degree is zero, hence U=0. Inequality (8) is an unproved extra premise, not a result of the rewrites.

## 5. The terminal coefficient as a multiplier

The scattering identities DS Omega=Omega_tilde composed with S and S(Phi_t y)=exp(tA)S(y), together with the tail Lamb identity, give off K

    B.grad kappa=-delta kappa,
    Omega.grad kappa=-delta eta,
    eta=(V.Omega_tilde) composed with S.

Together with B.grad H=-delta U.B and Omega.grad H=-delta U.Omega, these yield the submitted multiplier integrals for C1 F(H,kappa), provided the relevant divergences are integrable on D and cutoff errors vanish. They do not supply this admissibility automatically.

In particular, if D is carrier-invariant, C=S(D minus K) is invariant under exp(tA). In twisted polar coordinates z=exp((log r)A/c)theta it is given by r>0 and theta in a measurable angular set E, and volume is r2 dr dtheta. The scalar V.Omega_tilde has degree -2k-1. Volume preservation therefore gives

    integral_{D intersect {|S|<1}}|eta|
      =[integral_E |(V.Omega_tilde)(theta)|dtheta]
          integral_0^1 r^(1-2k)dr.

Since k>1, this is infinite whenever the ABSOLUTE angular integral is positive. A zero signed angular integral does not suffice to avoid this obstruction. The preimage of small balls approaches the compact core, since S is continuous and |S(y)-y|<=M/c. Thus the failure occurs in every neighborhood of K for such a cone. Equivalently successive exp(-nA) shells scale their absolute eta integral by exp(2delta n). If the absolute angular integral is zero, eta=0 almost everywhere on that cone and this specific obstruction is absent. No unconditional inadmissibility is asserted in that case.

## 6. Weighted identities and sufficient integrability

For rho_beta=|S|^-beta, B.grad rho_beta=-c beta rho_beta. Subtract the linear tail equation from the profile equation, take the W inner product, and use the local Sobolev product rule from Section1. Off K union {0},

    div(B rho_beta|W|^2/2)
      =rho_beta[(c/2)(alpha-beta)|W|^2
                  -W.grad P-W.(U.grad)V].               (9)

At beta=alpha, any admissible integration removes the energy term and leaves only a signed work identity. The energy's finiteness does not by itself justify this integration. The original current's absolute small-sphere bound is only O(r^(2-2k)), which need not vanish. The expression W.(U.grad)V contains a potentially nonintegrable degree -2k-1 term. These are bounds and possible obstructions, not assertions that every particular field attains them.

The unweighted repair is exact:

    W.(U.grad)V=U_i U_j partial_j V_i-div(U|V|^2/2),
    div[b|W|^2/2+U(e-U.V)+PW]
        =gamma|W|^2-U_i U_j partial_j V_i.               (10)

The current in (10) is J_E+eV-(U.V)U. Section2 proves its vanishing small-sphere flux. A nonconstant weight creates its dot product with grad rho, for which no sign has been shown.

There is a useful, but only sufficient, global weighted energy bound:

    integral_R3 |S|^-beta |W|^2 < infinity
            for every 0<=beta<alpha.                    (11)

Define the integrand arbitrarily on the null K. For beta>0 choose conjugate exponents p,q>1 satisfying beta p<3 and 2kq<3; such a pair exists exactly when beta+2k<3. Volume preservation and the bounded shift imply |S|^-beta in Lp on bounded sets. The bound W=O(1+r^-k) gives W in L2q there. Hoelder proves local integrability. Outside a large ball, |S(y)| is comparable to |y|, so the weight is bounded and W in L2 suffices. Beta=0 is A250. This proof establishes neither the endpoint nor optimality, and establishes no integrability of the work terms in (9).

For a C1 function F, rho=F(kappa) similarly replaces the energy coefficient by

    gamma F(kappa)-(delta/2)kappa F'(kappa).

For F=|kappa|^p with p>0, including p<1, the formula remains valid locally in the distributional transport sense. One may use F_epsilon=(kappa2+epsilon2)^(p/2): F_epsilon and kappa F'_epsilon converge uniformly on compact sets to |kappa|^p and p|kappa|^p, and the other local work terms are integrable. This avoids assuming that the nonsmooth transverse power is C1 at kappa=0. The critical exponent is

    p_E=(5c-2)/delta,
    |kappa|^p_E=|S|^-alpha |tau(pi(S))|^p_E.

It is the same critical radial weight times a nonnegative angular factor. This equality is not an endpoint integrability theorem.

## Verdict and limits

The stated exact identities, conditional multiplier obstruction, local Weber decomposition and strict-subcritical weighted energy bound are confirmed. The formerly proposed two-term tau cancellation is refuted by the explicit tail in Section3, as already corrected in the submitted source. No global sign of N_D follows from these manipulations. The invariant-current statement concerns exactly currents with verified zero integrated divergence; it is not a theorem excluding all possible Bernoulli, pressure or weighted methods.

# A critical scalar moment excludes finite-time tail core return

Status: CONFIRMED A705-A708 after full source and independent-proof postreads. Date: 2026-11-03T10:22:48.021216+00:00.

## 1. Exact conditional theorem

Let 2/5<c<1/2 and omega be any finite real number. Put

    p=(1-c)/c in (1,3/2), d=p-1, eta=d/(2p) in (0,1/6),
    J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J.

Let U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0 everywhere,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1).

The constant C is finite and may depend on the profile and omega. Let V,W and P2 be its actual velocity, vorticity and canonical pressure tails. Define on D=R3 minus{0}

    S=P2-|V|^2/2, h=S restricted to S2, G=W restricted to S2.

Suppose

    G=0 at area-almost every point of {h=0},
    integral_{h!=0} |G| |h|^(-eta) dA < infinity.       (1.1)

Then U=0. No vorticity-density hypothesis, rank identity, symmetry, finite angular spectrum or bound on omega is assumed.

Two sufficient alternatives are S=0 identically, handled separately in Section6, or |S|^(-eta) in L1loc(D) with its value defined to be infinity at zeros. In particular the local A2 condition on |S|^eta is sufficient without any density or exterior analyticity. The natural velocity and derivative bounds can be supplied instead by U->0 and |DU|=O(sqrt(|x|)), using A601 in this c interval. This is a conditional theorem, not the unrestricted bare-decay conjecture.

Sections2-5 prove the flux theorem; Section6 treats the scalar-only conditions; Section7 records a quantitative necessary condition for a possible nonzero profile and Section8 gives dependencies and scope. No computation is required.

## 2. The volume-preserving partial tail flow

Write Omega=curl U and let Gamma_t denote its flow on R3. Since U is C2, Omega is C1. The derivative estimate bounds Omega globally, so Gamma_t is complete. The identity div Omega=0 and the usual C1 flow Jacobian formula give det D Gamma_t=1. No bound on D Omega at infinity is required for completeness of this bounded field.

A209-A210 supply a compact null core C, a C1 diffeomorphism

    Xi:E=R3 minus C -> D, det D Xi=1,
    W(Xi y)=D Xi(y)Omega(y).                         (2.1)

The determinant assertion is pointwise: D Xi is the local uniform limit of exp(-sA)D Phi_s, each with determinant1, and is transported to E by equivariance. It is stronger than a bare measure-pushforward statement and was checked in the independent scattering proof.

For z in D, set y=Xi^(-1)z. On any interval for which Gamma_t(y) remains in E define

    F_t(z)=Xi(Gamma_t(y)).                           (2.2)

The chain rule makes this a W curve. Conversely every W curve pulls back by Xi^(-1) to an Omega curve, so uniqueness of the original C1 flow gives uniqueness of W curves in D. Let t_+(z) be its maximal positive lifetime and D_t={z:t_+(z)>t}, for t>=0. A point in D_t has a compact Gamma segment staying in E, hence staying a positive distance from the closed core C. Continuous dependence makes D_t open. Formula (2.2) is a C1 diffeomorphism from D_t onto its image; its inverse is the corresponding negative-time map. The chain rule yields det D F_t=1.

This is a partial flow. There is no map at a terminal point at the singular origin, and no global volume-preserving flow on D is claimed. The time-space domain { (t,z):0<=t<t_+(z)} is relatively open, its flow is continuous, and t_+ is measurable since {t_+>t}=D_t is open. These facts justify all product integrals and changes of variables below even though W is only known to be continuous.

## 3. Select a positive volume of uniformly bounded arrival times

The confirmed A360 theorem gives, for volume-almost every z in {W!=0}, a finite positive lifetime and

    F_t(z)->0 as t increases to t_+(z).              (3.1)

Only this forward finite-time statement is used. A360 also proves backward return and finite length, neither needed here. Its scattering realization, Hopf decomposition, angular recurrence and endpoint argument are retained hypotheses through that theorem; they are not properties of an arbitrary abstract homogeneous tail.

Suppose W is not identically zero. Its continuous twisted homogeneity makes {1<|z|<2,W!=0} a nonempty open set of positive, finite volume. The full-measure set where (3.1) holds is measurable; it can also be described by rational-time convergence tests on the continuous partial flow. Since it is the countable union of its subsets with t_+<=T, T a positive integer, one such subset B has positive volume. Thus

    0<|B|<infinity, B subset {1<|z|<2},
    0<t_+(z)<=T and (3.1) for every z in B.           (3.2)

A531 gives S continuous, locally Lipschitz and constant on every W curve. Let M=1+max_{1<=|z|<=2}|S(z)|. Then every surviving point of every curve from B has |S|<M. This uses the every-curve conclusion, not just an almost-everywhere formal transport identity.

Take a fixed smooth radial cutoff rescaled to chi_epsilon, equal to1 for |z|<=epsilon and0 for |z|>=2epsilon, with 0<=chi_epsilon<=1 and |grad chi_epsilon|<=C_chi/epsilon. For 0<epsilon<1/4, each curve from B starts where chi_epsilon=0 and eventually reaches chi_epsilon=1. The fundamental theorem on a compact segment of that curve gives

    1 <= integral_0^{t_+(z)}
             |W(F_t z)| |grad chi_epsilon(F_t z)| dt. (3.3)

The integral is allowed to be infinite at this stage. No differentiability at the terminal origin is used.

## 4. A stopped-flow flux inequality

Integrate (3.3) over B, extend the time integral to [0,T] with zero integrand for t>=t_+(z), and apply Tonelli to the nonnegative measurable function. At fixed t, the set B intersect D_t lies in the open C1 flow domain. The map F_t is injective there and has determinant1, so

    integral_{B intersect D_t} f(F_t z) dz
          = integral_{F_t(B intersect D_t)} f(y)dy
          <= integral_{|S(y)|<M} f(y)dy

for the nonnegative f=|W| |grad chi_epsilon|. Measurable sets cause no problem: a C1 diffeomorphism and its inverse are locally Lipschitz on their open domains, so preserve local null sets and the ordinary change-of-variables theorem applies. Therefore

    0<|B| <= (C_chi T/epsilon)
          integral_{epsilon<|y|<2epsilon, |S(y)|<M}|W(y)|dy.
                                                               (4.1)

Each change of variables occurs strictly before the terminal time. This avoids any invalid claim that all initial volume survives after hitting zero. There is no uncountable saturation of a null exceptional set: the selected set B is already good at every point, and the argument integrates on ordinary partial-flow domains.

## 5. Exact homogeneity and cancellation at the critical exponent

Write y=exp((log r)A/c)w. Ordinary polar measure followed by a rotation on each sphere gives

    dy=r^2 dr dA(w),
    |W(y)|=r^(-p-1)|G(w)|,
    |S(y)|=r^(-2p)|h(w)|.                            (5.1)

The radius-dependent angular rotation has no extra Jacobian: in polar variables the derivative matrix is triangular, with the sphere rotation as its angular block. On the shell in (4.1), |S|<M implies |h|<M(2epsilon)^(2p). Thus

    |B| <= C_0 T epsilon^(-d)
              integral_{|h|<M(2epsilon)^(2p)} |G|dA, (5.2)

where C_0=C_chi integral_1^2 u^(1-p)du is finite and positive. In particular the exponent is 1-p=-d, not 2-p; the radial shell integral has been divided by epsilon.

Define H=|G||h|^(-eta) on {h!=0}, and H=0 on {h=0}. By (1.1), H is integrable and the zero set contributes no |G| mass. On 0<|h|<M(2epsilon)^(2p),

    |G|=|h|^eta H <= M^eta 2^d epsilon^d H,

because 2p eta=d. Substituting in (5.2) gives

    0<|B| <= C_0 T M^eta 2^d
             integral_{0<|h|<M(2epsilon)^(2p)} H dA. (5.3)

The indicator of this punctured sublevel set tends pointwise to zero. Dominated convergence by H makes the right side tend to zero, a contradiction. Equality in the critical powers is sufficient; the strict limiting gain comes from absolute continuity of an L1 integral. No exponent greater than eta and no reverse-Holder theorem are needed.

It follows that W=0. By (2.1) and invertibility of D Xi, Omega=0 off the compact null core, hence everywhere by continuity. The identities div U=curl U=0 make U harmonic on R3. Boundedness and decay give U=0.

## 6. Scalar-only sufficient conditions and the separate S=0 branch

If |S|^(-eta) belongs to L1loc(D), compactness of the closed annulus and (5.1) give

    integral_{1<|y|<2}|S(y)|^(-eta)dy
      = (integral_1^2 r^(2+d)dr)
            integral_S2 |h|^(-eta)dA < infinity.

Here infinity is assigned on {h=0}. Consequently that zero set has area zero. The continuous angular vorticity G is bounded, so both clauses in (1.1) hold. This proves the scalar reciprocal condition. Local A2 of b=|S|^eta includes b>0 almost everywhere and local integrability of b^(-1), so it implies this condition directly. No density of {W!=0} is invoked anywhere.

The branch S=0 identically is separate: its reciprocal is not integrable. Use the actual Poisson identity

    -Delta P2=partial_i partial_j(V_i V_j)

on D, with smooth radial tests supported in an annulus. Define

    Pbar=integral_S2 P2,
    Rbar=integral_S2 |V.w|^2,
    Tbar=integral_S2 (|V|^2-|V.w|^2).

The radial Hessian formula and twisted homogeneity give

    (Pbar+Rbar) integral r^(2-2p)phi''(r)dr
       +(2Pbar+Tbar) integral r^(1-2p)phi'(r)dr=0.

Integration by parts changes the first radial integral to -(2-2p) times the second. The second can be nonzero because p>1, for example by a suitable nonnegative compactly supported test and one further integration by parts. Hence

    2p Pbar+(2p-2)Rbar+Tbar=0,
    integral_S2 S=-[(3p-2)Rbar+(p+1)Tbar]/(2p).

Both coefficients in the numerator are strictly positive in the stated range. If S=0, then Rbar=Tbar=0, V=0 by continuity, and again W=0 and U=0. No test reaches the origin or infinity, and no boundary term is discarded there.

## 7. A quantitative necessary nodal concentration

The stopped-flow argument gives more than divergence of the critical moment. For any nonzero actual profile under Section1, before imposing (1.1), the positive set B and finite constants M,T in Section3 yield

    integral_{|h|<s}|G|dA >= C_* s^eta               (7.1)

for every sufficiently small s>0. Indeed put s=M(2epsilon)^(2p) in (5.2), so epsilon^d=s^eta/(2^d M^eta), and take

    C_*=|B|/(C_0 T 2^d M^eta)>0.

Thus the vanishing condition integral_{|h|<s}|G|=o(s^eta) is itself sufficient for U=0. The weighted critical integrability in (1.1) implies this vanishing, as Section5 proves. Conversely a nonzero profile must either have positive |G| mass on {h=0}, or have a divergent weighted reciprocal integral; in the latter case (7.1) still describes the necessary concentration rate. This does not prove a universal order, dimension or shape for the nodal set. It also does not assert that the sufficient L1 condition is necessary for nonexistence.

## 8. Dependencies, verification and remaining hypotheses

The proof uses actual C1 scattering conjugacy and det D Xi=1 from A209-A210, finite positive W lifetime with terminal origin from A360, and canonical locally Lipschitz S constant on every W curve from A530-A531. These complete independent proofs have been reread in this audit session, including the determinant, endpoint, Hopf, sphere-flow and mollification steps. The scalar mean identity agrees with A591 and is rederived in Section6. A601 is used only for the alternative derivative-screen formulation.

The new reasoning is elementary measure and flow theory on the nonsingular partial domains: measurable selection of B, the fundamental theorem, Tonelli, ordinary change of variables, exact polar scaling and dominated convergence. No nonsmooth-flow theorem, absorbing-origin map, global rank extension, A2 regularity theorem, numerical test or formal build is used.

This confirms the improvement of the ACTUAL profile application of Theorem DA. The exterior-density or analyticity premise is removed, and A2 may be weakened to the critical reciprocal condition or (1.1). The abstract five-equation tail problem remains separate because finite-time core return is extra actual-profile information. Global zero helicity, natural rates or their derivative-screen substitute, and nodal integrability remain explicit sufficient assumptions. Both unrestricted C2 and C-infinity campaign conjectures remain open.

The source LIT175 has been read in full. Existing configured model agents are asked to compare the stopped-flow measurability, determinant, terminal-time restriction and endpoint exponent through working files. A requested review is not counted as a response; provider runtime is not independently attested. No new model client or agent is used.

# Repeated audit of the helicity-sign Liouville foundation

Status: independent reconstruction of current Section2D at the Note105 report pin. This is a conditional theorem, not a solution of the arbitrary-helicity conjecture. The current section and the earlier complete smooth, finite-regularity and recurrence proofs were read in full. The smooth coverage foundation was separately rechecked in A2040-A2043. All finite-regularity coverage results are used at their previously confirmed conditional scope; their entire projective construction is not rederived here.

## 1. Exact statement and coverage input

Let J(y1,y2,y3)=(-y2,y1,0), 2/5<=c<1/2, omega any finite real number, a=1-2c, kappa=1+c, A=cI-omega J and B=Ay+U. Suppose U in C2(R3;R3), P in C1(R3),

    div U=0,
    (1-c)U+B.grad U+omega JU+grad P=0,
    sup_(|y|>=R)|U(y)| -> 0.

Set Omega=curl U, O={Omega!=0}, h=U.Omega. Let Phi be the B flow and Psi_t=Phi_(-t). Assume a countable family F of compactly supported probabilities nu invariant and ergodic for the full Psi flow. Each gives full mass to {B!=0,Omega!=0}, has Lyapunov exponents a,0,-kappa and entropy a for Psi_1, and almost every point of O lies in one of its continuous-time basins. The basin consists of the points whose time averages under Psi converge to nu for every bounded continuous test function. Let

    D_nu = union {V open in O: Leb(V minus Bas(nu))=0}.

If h has one sign on each D_nu, with sign allowed to depend on nu, then U=0. Absolutely continuous unstable conditionals need not be added as a separate hypothesis: the stated exponents and entropy imply them with strictly positive densities by the precise Ledrappier-Young theorem used below.

For U in C-infinity the coverage hypotheses follow from A308, rechecked A2040-A2043. For U in C^r, integer r>=2, they follow under the additional componentwise condition Gamma_E<ra for every connected component E of O. Here Q is a strictly inward trapping ball for Psi, K=intersection_(t>=0)Psi_t Q, and Gamma_E is the maximum top Lyapunov exponent among full-flow-ergodic invariant probabilities on K intersect closure(E) intersect ({B=0} union {Omega=0}), with maximum -infinity for an empty class. Equivalently Lambda_E=lim_n n^-1 log max(1,max_(Q intersect closure(E))||D Psi_n||)<ra, by A430-A431. The global condition Lambda_core<ra suffices. These extra growth bounds are not inferred from decay. No conclusion here supplies unrestricted C2 coverage.

## 2. Complete flows and exact identities

Write M=||U||_infinity. The C1 field B has linear growth and is complete. Variation of constants, using that exp(-omega tJ) is orthogonal, gives for t>=0

    |Phi_t x|<=exp(ct)(|x|+M/c),
    |Psi_t x|<=exp(-ct)|x|+(1-exp(-ct))M/c.

Thus backward-carrier orbits from a compact set lie in one compact ball. Also det D Phi_t=exp(3ct), and B.y>=c|y|^2/2 for |y|>=2M/c. The equation improves P to C2. Define H=P+|U|^2/2+Ay.U. Direct expansion and curl give

    aU+grad H=B cross Omega,
    B.grad H=-a U.B,   Omega.grad H=-a h,
    [B,Omega]=-kappa Omega,
    D Phi_t(x)Omega(x)=exp(kappa t)Omega(Phi_t x).

All signs keep the rotation terms: A^T=cI+omega J cancels the explicit omega JU in momentum. Curl uses div B=3c and div Omega=0. The Cauchy identity follows by uniqueness of the variational equation, and holds at zeros as well.

For each compact starting set choose a ball containing all its Psi orbits, and a common local Omega-flow existence time delta>0 on a slightly larger ball. For arbitrary s and sufficiently large T define

    Gamma_s x=Phi_T Gamma^local_(s exp(-kappa T)) Psi_T x.

The local Cauchy conjugacy and uniqueness make this independent of T; it is the integral curve of Omega through x for every real s. Hence Omega is complete, and

    Phi_t Gamma_s=Gamma_(s exp(kappa t)) Phi_t

for every pair of real times. Taking T=kappa^-1 log(1+|s|/delta) gives

    sup_(x in compact C)|Gamma_s x|<=C_C(1+|s|/delta)^(c/kappa).

The C1 flow Gamma preserves volume because div Omega=0. No bound on Omega at infinity was assumed. Local conjugacy also gives |Psi_t Gamma_s x-Psi_t x|<=C_x|s|exp(-kappa t) for each fixed s and all sufficiently large t.

## 3. Recurrence and sign rigidity

Fix a nonzero integer N and a bounded rational ball V. The subset V' of points never returning to V under positive iterates of Gamma_N has pairwise disjoint images Gamma_(jN)V'. Their first n images fit in a ball of volume at most C(1+n)^(3c/kappa). Volume preservation yields

    (n+1)Leb(V')<=C(1+n)^(3c/kappa).

Since 3c/kappa<1, V' is null. Points returning only finitely often lie in a countable union of inverse images of V'. Taking all rational balls and all positive and negative integers N gives a Borel set of full volume with arbitrarily close returns in both time directions. This works on infinite-volume space without bounded vortex lines.

If an open Gamma-invariant set D has h>=0, H is nonincreasing on every vortex orbit in D. If h(x)>0 somewhere, a small positive-volume ball has a common strict H drop during a fixed positive time. Shrink it so the oscillation of H there is smaller than that drop. A recurrent point in the ball returns arbitrarily late and contradicts monotonicity. Thus h=0 on D; use -H for h<=0. These arguments only need c<1/2 and C2 regularity.

A recurrent point with h!=0 has both strict signs arbitrarily far in each time direction. To see the opposite sign, first return to a small region where h has its initial sign, wait through a strict H drop, then return again near the initial H value. The mean value theorem supplies a time with the opposite sign. This does not imply that almost every vortex line in a sign-changing basin has nonzero helicity anywhere.

## 4. One canonical pressure and transported mean decay

Use the independently checked energy and pressure results A031, A040 and A277, with beta=5-2/c in[0,1). Under the exact hypotheses of Section1,

    E(R)=integral_(B_R)|U|^2<=C_E R^beta,   R>=1.

At c=2/5 this is the finite-energy endpoint theorem; elsewhere finite energy is not assumed. The weighted far-field integral integral_(|z|>=rho)|U(z)|^2|z|^-3 is at most C rho^(beta-3) by dyadic summation.

For any R>0 split the canonical pressure into the whole-space Riesz transforms of U_iU_j supported in B_(4R), plus the absolutely convergent unsubtracted kernel integral outside that ball. The local pressure theorem identifies their sum with P minus a constant on B_(2R). Enlarging R moves a compact annulus between the two terms. Off its support the Riesz transform equals its ordinary kernel integral, so the constants agree on the overlapping balls. They define one fixed p_infinity, not a radius-dependent choice. With P0=P-p_infinity, Plancherel and |U|<=M bound the near term's squared L2 norm on B_R by C M^2 E(2R); the far term contributes at most C R^(2beta-3). Consequently

    integral_(B_R) P0^2<=C R^beta,
    integral_(B_R) H0^2<=C_H R^(beta+2),
    H0=P0+|U|^2/2+Ay.U.

The normalized quadratic mean of H0 tends to zero and selects this additive constant uniquely. For every bounded measurable Q', change variables by Phi_t, use its Jacobian and the radius bound in Section2, to obtain

    integral_(Q')H0(Phi_t y)^2dy<=C_Q' exp(c(beta-1)t)
                                  =C_Q' exp(-2at).

This calculation assumes no pointwise pressure decay. The current report's explicit constants, dyadic exponents and shell powers were checked; its rotation dependence in C_H is harmless for each finite omega.

## 5. Essential domains and full-volume product boxes

The basin is invariant under every carrier time. The local conjugacy estimate of Section2 and uniform continuity on the compact union of two backward orbits make it invariant under every finite Gamma time as well. Both the forward and reverse basins are Borel: use a countable dense collection of compactly supported continuous tests, and a compact cutoff of nu-integral1 to pass from convergence on C0 to every bounded continuous test. This argument works even when forward Phi orbits escape. Full-flow ergodicity, applied to the all-real-time-invariant limit of time averages, makes both basins full nu measure; time-one ergodicity is unnecessary.

At a two-sided Oseledets regular point, the Cauchy identity places Omega in the stable line and boundedness of B along the compact orbit places B in the zero line, using both time directions for the latter. They are independent. Thus the unstable tangent, -B and Omega span R3.

Extend -B by a cutoff outside a trapping ball to a C2 flow on S3. It agrees near K, and an unstable point of a regular x in K cannot leave the trapping ball under reverse time: the outward field preserves its exterior. Therefore the relevant unstable manifolds are contained in K. The entropy equality and Ledrappier-Young PartI TheoremA, Lemma3.1.1, Lemma6.1.1 and Corollaries6.1.4,6.2 give a subordinate partition with conditionals equivalent to arclength, with positive finite density on full local plaques. The nonergodic corollary applies to the time-one map. These primary statements were checked against the retained manuscript in the earlier section audit and reread in the current smooth-coverage recheck. The stronger density proportional to |(B cross Omega).e^u| is not needed here.

Take a local unstable arc gamma with full-arclength Borel subset T of two-sided generic regular support points. Since T is dense and supp nu closed, the whole arc lies in supp nu. The map

    Theta(s,r,tau)=Gamma_tau Psi_r gamma(s)

is a C1 coordinate map near the base point, with determinant bounded above and away from zero on a smaller box. The image E of T times the other two intervals has full volume in its open image V, and lies in Bas(nu). It follows that nu(D_nu)=1. Second countability gives Leb(D_nu minus Bas(nu))=0. The definition and preservation of null sets by C1 diffeomorphisms make D_nu invariant under all Phi and Gamma times. A compactly supported nonnegative observable in D_nu of positive nu integral forces every basin point to enter D_nu. Hence Bas(nu) subset D_nu. Distinct domains are disjoint because distinct basins are disjoint and any overlap is open. The domains cover O modulo a null set.

## 6. Zero helicity gives zero Bernoulli value

The sign premise and Section3 give h=0 on D_nu. Thus H0 is constant on each complete vortex orbit in this invariant domain. For y=Theta(s,r,tau), s in T, exact conjugacy gives for every real t

    H0(Phi_t y)=H0(Phi_(t-r)gamma(s)).

The right side stays in supp nu and is uniformly bounded, independently of t and the point y in the box. Its forward time average of the square tends to m=integral H0^2 dnu, because T was chosen generic in both time directions. A compact cutoff equal to1 on supp nu makes the test globally bounded. Dominated convergence over the full-volume subset E gives

    limit_(T0->infinity) integral_E (1/T0)integral_0^T0 H0(Phi_t y)^2dt dy
       =m Leb(E).

Section4 and Tonelli bound the left side by C/(2aT0), so m=0. Continuity gives H0=0 on supp nu. The same exact identity makes H0 zero on E and all its carrier translates, hence on V and all its translates by density. Their union is open and carrier invariant. It contains a support point, so a nonnegative continuous test supported in V has positive nu integral. Every basin point eventually enters V, hence lies in this union. The basin has full volume in D_nu, and H0=0 on D_nu by continuity. No integration by parts against a singular invariant measure is involved.

## 7. Zero-set localization and positive stress

Coverage gives H0=0 on O. By continuity grad H0=0 on closure(O). On boundary(O), Omega=0, so the Lamb identity gives U=0. If O is empty, U is entire harmonic and bounded, hence constant and zero by decay. Otherwise let D=int{Omega=0} and extend U from D by zero outside D. Boundary(D) is contained in boundary(O). On any fixed ball a bound for DU, applied to the first boundary points of segments, proves that the extension is Lipschitz. Its weak derivative is 1_D DU: on the complement it vanishes almost everywhere by the density-point argument for the zero set of a Lipschitz function, including any boundary of positive volume. Its divergence and curl are zero distributionally. Weyl's lemma and unique continuation from the nonempty open set O make the entire extension zero. Thus U=0 on all {Omega=0}.

The Lamb identity gives grad H0=0 there too. H0 is globally constant, and Section4 forces that constant to be0. Dotting Lamb with B gives U.B=0. Since H0=P0-|U|^2/2+U.B, we have P0=|U|^2/2.

Taking divergence of momentum gives

    partial_i partial_j(U_i U_j)+Delta P0=0.

The derivative of -omega Jy in the carrier and div(omega JU) cancel exactly; no restriction on omega occurs. Test with chi(y/R)psi(y), where chi is a nonnegative smooth cutoff equal to1 on B1 and zero outside B2, and psi=sqrt(1+|y|^2). Terms differentiating chi are at most C R^-1 E(2R)<=C R^(beta-1), tending to0. The remaining integrand is

    chi(y/R)[U^T D2psi U+(|U|^2/2)Delta psi],
    D2psi>=psi^-3 I,   Delta psi=(3+2|y|^2)/psi^3>0.

Its nonnegativity bounds the integral of |U|^2 psi^-3 on each fixed ball by the vanishing cutoff error. Thus U=0. This proof handles every boundary term with the previously established beta<1 energy bound, without a finite-energy assumption.

## 8. Corollaries and precise limits

For smooth U the coverage theorem supplies Section1's data. For finite C^r use the separately confirmed growth-conditioned package; all subsequent steps need only C2. If a nonzero profile exists in one of these classes, at least one essential basin contains both strict helicity signs, each on an open positive-volume subset. This says neither that every basin has both signs nor that the singular support has any prescribed helicity values.

The levelwise variant also follows. On a recurrent orbit starting where h>0, H first decreases through a nonempty interval and later returns above it. A first/last hitting-time argument and the mean value theorem produce an increasing segment through an interior value of that interval. The one-dimensional inverse function theorem gives a smaller interval of levels, each reached once with h>0 and once with h<0. Thus if on each level in each essential domain h has at most one strict sign, h must vanish there; Sections6-7 apply. This uses actual vortex recurrence, not carrier-measure ergodicity of vortex motion.

Current Section2D's CorollaryL.5 is explicitly quoted with proof omitted and is not used here. Its measurable band-integral identity is not freshly reproved by this audit. The extra alpha-density formula is likewise unnecessary for the checked Liouville chain. The complete finite-r projective proof remains under its earlier verdicts. No claim of unrestricted C2 coverage, exclusion of a sign-changing basin or resolution of arbitrary-helicity nonexistence is made.

## 9. Assembly precision and verification

All of current Section2D was read, including its external-theorem list and all41 provenance points, at the report pin named in the manifest. No new mathematical gap was found in the stated helicity-sign chain. Its updated CONDITIONAL labels are correct. The forward/reverse genericity, global vortex invariance, fixed pressure representative, zero-set extension and cutoff limit all retain their essential hypotheses.

The next table, Section3.1, contains a stale Theorem8 row: it still globally requires curl U bounded before listing both strain criteria, although the main theorem now removes that requirement. Split the vorticity alternatives from the two strain alternatives in this table. It also omits SF2/SF3 and should either include their exact premises or explicitly say it is a selected summary. This is a scope/assembly repair, not a refutation of the stronger theorem.

Dependencies and retained source pins are listed in the team records. The current review used no new numerical computation, formal build, model client, server or outside-agent write. Existing collaboration is through the configured model coordinator's reviewed report and earlier source reviews; the provider runtime is independently unattested. The proof does not rely on a model's approval as mathematical evidence.

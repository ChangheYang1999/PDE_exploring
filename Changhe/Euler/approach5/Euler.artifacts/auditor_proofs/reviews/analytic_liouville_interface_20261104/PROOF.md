# The analytic interface in the helicity-sign theorem

## 1. Exact statement and audit question

Let 0 < c < 1/2, let omega be any finite real number, and let J(x1,x2,x3) = (-x2,x1,0). Suppose U in C^2(R^3;R^3) is bounded and P in C^1(R^3) satisfies

    div U = 0,
    (1-c)U + (B.grad)U + omega JU + grad P = 0,
    B(y) = Ay + U(y),   A = cI - omega J.

Write Omega = curl U, O = {Omega != 0}, a = 1-2c > 0, kappa = 1+c, and E(R) = integral_(|y|<R) |U|^2. Assume E(R) = o(R) as R tends to infinity. Let Phi_t be the B flow and Psi_t = Phi_(-t).

Assume separately that there is an at most countable family (nu_i) of compactly supported Borel probabilities, invariant and ergodic for the entire Psi flow, with the following properties. Each gives full mass to {B != 0, Omega != 0}. For nu_i-almost every point the exponents of Psi_1 are the three simple exponents (a,0,-kappa), and the entropy h_(nu_i)(Psi_1) is a. The continuous-time basins

    Bas(nu) = {x: T^(-1) integral_0^T f(Psi_t x) dt -> integral f dnu
                  for every bounded continuous f on R^3}

cover O up to a Lebesgue null set. Define D_i to be the union of the open V contained in O for which Leb(V minus Bas(nu_i)) = 0. If on each D_i the continuous function h = U.Omega has one sign, with the sign allowed to depend on i, then U = 0.

This is a conditional theorem. The coverage and entropy assumptions are not inferred from C^2 regularity. Its purpose is to check the analytic interface of report Section 2D and to isolate the weaker sufficient energy input E(R)=o(R). No novelty is asserted. The positive-density theorem of Ledrappier and Young, in the precise form audited in A2948-A2949, is an explicit external input. Its intermediate entropy proof is not re-proved here.

## 2. Complete carrier flow and exact identities

Set M = sup |U|. The field B is locally Lipschitz and has at most linear growth, hence Phi and Psi exist for all real times. Variation of constants, using that exp(-omega tJ) is orthogonal, gives for t >= 0

    |Phi_t x| <= exp(ct)(|x|+M/c),
    |Phi_t x| >= exp(ct)(|x|-M/c)+M/c,
    |Psi_t x| <= exp(-ct)|x|+(1-exp(-ct))M/c.

Also div B = 3c, det D Phi_t = exp(3ct), and B(y).y >= c|y|^2-M|y|. Every compact invariant set therefore lies in the ball |y| <= M/c. To see this last assertion, apply the Psi bound to x = Psi_t(Phi_t x) and let t tend to infinity, using boundedness of the invariant orbit.

The profile equation implies P in C^2 by solving for its gradient. Put H = P+|U|^2/2+(Ay).U. Direct differentiation gives

    aU+grad H = B cross Omega,
    B.grad H = -a U.B,       Omega.grad H = -a h,
    [B,Omega] = -kappa Omega,
    D Phi_t(x) Omega(x) = exp(kappa t) Omega(Phi_t x).

For the first identity, (DU)B = grad(|U|^2/2+(Ay).U)-cU-omega JU+Omega cross B. Curling it gives the bracket identity because div Omega=0 and div B=3c. The last identity follows by uniqueness of the variational equation. Thus O and its complement are invariant under the carrier.

There is no estimate uniform in unbounded omega asserted here. Each finite omega is allowed; the rotations cancel exactly in the radial bounds and the pressure divergence identity.

## 3. The pressure representative is derived, not assumed

For a compactly supported smooth test function psi, let T_ij be the Fourier multiplier -xi_i xi_j/|xi|^2. The function T_ij partial_k psi is integrable: locally use its L^2 bound and away from the support differentiate the Newton kernel, obtaining decay O(|x|^-4). Thus, for F_ij=U_i U_j,

    <G_k,psi> = -sum_ij integral F_ij T_ij partial_k psi

defines the canonical pressure gradient. Taking the distributional divergence of the equation gives -Delta P = partial_i partial_j F_ij. The rotation contributions cancel, so partial_k P-G_k is a harmonic distribution, hence a smooth harmonic function.

The energy premise gives U(R.) -> 0 in L^2 on every bounded set: its squared norm on B_L equals R^-3 E(LR) = o(R^-2). Boundedness then extends this convergence against compactly supported tests to the moving tests used below. More generally the same conclusion would follow from boundedness and distributional dilation decay.

Pair the equation at y=Rz with psi. Integration by parts gives

    integral (partial_k P)(Rz) psi(z) dz
      = integral U(Rz).[(4c-1)psi e_k-omega psi J^T e_k+(Az.grad psi)e_k] dz
        +R^-1 sum_j integral U_k(Rz)U_j(Rz) partial_j psi(z) dz.

The corresponding pairing for G_k is -R^-1 sum_ij integral F_ij(Rz) T_ij partial_k psi(z) dz. Fix a point x and a radial smooth test phi of integral one. The harmonic mean-value identity expresses (partial_k P-G_k)(x) using psi_R(z)=phi(z-x/R). The first displayed right-hand term tends to zero, since its moving test tends in L^1 to a fixed compactly supported test and U is bounded with dilation decay. Both remaining terms are O(R^-1); translation preserves the L^1 norm of T_ij partial_k phi. Therefore partial_k P=G_k, for every k. No harmonic or affine pressure remainder is left except an additive scalar constant.

For R>0, put

    N_R = sum_ij T_ij(F_ij 1_(|z|<2R)),
    F_R(x) = integral_(|z|>=2R) sum_ij K_ij(x-z)F_ij(z) dz,   |x|<R,
    K_ij(w)=(3w_i w_j-delta_ij|w|^2)/(4 pi |w|^5).

These far integrals converge absolutely. Indeed, eta(R)=sup_(s>=R) E(s)/s is finite for R sufficiently large and tends to zero, and a dyadic shell sum gives

    S(R)=integral_(|z|>=R) |U(z)|^2 |z|^-3 dz
         <= (8/3) eta(R) R^-2.

For smaller positive R use boundedness on the intervening compact annulus. Testing the canonical gradient shows P=N_R+F_R+p_R on B_R. For two radii, the difference of the near terms is the classical kernel integral over the intervening annulus, exactly the negative difference of the far terms on the smaller ball. Hence all p_R equal one constant p_inf. Write P0=P-p_inf. This is one fixed representative for all radii and all basins.

## 4. Mean decay and transported decay under E(R)=o(R)

The multiplier bound and Cauchy-Schwarz in the matrix indices give

    ||N_R||_2^2 <= integral_(|z|<2R) |U|^4 <= M^2 E(2R)=o(R).

For |x|<R and |z|>=2R, |x-z|>=|z|/2, while |sum K_ij(w)U_i U_j|<=|U|^2/(2 pi |w|^3). Consequently |F_R(x)| <= (4/pi)S(2R)=o(R^-2), and

    integral_(B_R) P0^2 <= 2M^2 E(2R)+C R^3 S(2R)^2=o(R).

Let H0=H-p_inf. The expression H0=P0+|U|^2/2+(Ay).U gives

    integral_(B_R) H0^2
      <=3 integral_(B_R) P0^2+(3M^2/4)E(R)+3||A||^2 R^2 E(R)
      =o(R^3).

This also proves uniqueness of the constant p_inf for which the quadratic mean of H-p_inf tends to zero: the triangle inequality in normalized L^2 forces the difference of two such constants to vanish.

For every bounded measurable Q there is C_Q>0 with Phi_t(Q) contained in B_(C_Q exp(ct)) for t>=0. Change of variables gives

    integral_Q H0(Phi_t y)^2 dy
      <= exp(-3ct) integral_(B_(C_Q exp(ct))) H0^2 = o(1).

The integral is locally bounded in t and tends to zero, so its Cesaro mean tends to zero too. An exponential decay rate is not needed. In the report the stronger estimate E(R)<=CR^(5-2/c), with exponent below one, gives the stated exponential rate.

## 5. Complete vortex flow and recurrence

Let Gamma denote the local Omega flow. Omega is C^1 but need not be globally bounded. For each rho>0 there is delta>0 such that all starting points in B_rho have their local vortex trajectories for |s|<=delta in B_(rho+1). The bracket identity gives local conjugacy. For arbitrary x and s choose T>=0 large enough that |s|exp(-kappa T)<=delta, where rho bounds every Psi_t x. Define

    Gamma_s x = Phi_T Gamma_(s exp(-kappa T))^local Psi_T x.

Uniqueness of local integral curves shows independence of larger T. This defines a complete C^1 flow and proves the global conjugacy

    Phi_t Gamma_s = Gamma_(s exp(kappa t)) Phi_t.

For a compact set Q choose rho and delta uniformly. Taking T=kappa^-1 log(1+|s|/delta) and using the carrier bound gives

    sup_(x in Q) |Gamma_s x| <= C_Q (1+|s|/delta)^(c/kappa).

The flow preserves Lebesgue volume because div Omega=0. For any bounded rational ball W and nonzero integer N, let W' be the points of W that never return to W under positive iterates of Gamma_N. The sets Gamma_(jN)W' are disjoint and all have volume Leb(W'). For 0<=j<=n they lie in a ball of volume O((1+n)^(3c/kappa)). Since 3c/kappa<1, their total volume forces Leb(W')=0. Points with finitely many returns form a countable union of inverse images of W', hence are null. Intersecting over rational balls and nonzero integers proves that almost every point returns arbitrarily near itself at arbitrarily large positive and negative integer vortex times.

If D is open and Gamma-invariant and h has one sign on D, then h=0 on D. Otherwise continuity gives an open ball and a common positive vortex-time segment on which H0 drops by a fixed positive amount, or rises if the sign is negative. The one-sign identity Omega H0=-a h makes this change permanent along the orbit. A recurrent point of that ball contradicts continuity of H0 on returning near its starting point. The argument needs recurrence in ambient Lebesgue measure, not recurrence under nu_i and not bounded individual vortex lines.

## 6. The separately assumed measures produce the required boxes

This section uses precisely the external positive-density input A2948-A2949. Choose R0>2M/c and let Q0 be the closed ball of radius R0. The Psi_t(Q0) are nested compact sets; their intersection K is invariant under the entire carrier flow and contains every compact invariant set, by Section 2. In particular it contains every support under consideration. Choose a larger ball Q with the same center and cut off -B smoothly outside a still larger ball. The resulting C^2 time-one map on S^3 agrees with Psi_1 near the core, as does its inverse. The outward radial bound for B implies that an orbit backward asymptotic to a core orbit cannot leave Q. Thus the unstable manifolds agree with those of the original flow. The given invariant probability, spectrum and entropy transfer unchanged. The entropy equals the sum of its positive exponents. Ledrappier-Young gives a subordinate partition with conditional measures equivalent to arclength on its one-dimensional unstable pieces. Equivalence, rather than absolute continuity in only one direction, is the property needed below. Time-one ergodicity is not assumed.

At regular points Omega spans the exponent -kappa line and B spans the zero exponent line. Indeed their carrier derivative formulas, boundedness on the invariant support and the two-sided Oseledets limits exclude the other components. Therefore the unstable tangent, B and Omega are independent. Full-flow ergodicity and the ergodic theorem give a full-nu-measure Borel set G of support points generic for both time directions and regular for this splitting. For an observable f first apply the time-one ergodic theorem to integral_0^1 f(Psi_s x) ds. Its discrete averages equal the continuous-time averages at integer lengths. Their limit is invariant under every real time shift, since the two end intervals contribute at most 2|s| ||f||_infinity/T. Full-flow ergodicity therefore makes that limit constant, and integration identifies it with integral f dnu. Apply the same argument to the reversed flow and a countable dense family of observables on the compact support, then use uniform approximation. No ergodicity of Psi_1 follows or is used.

Disintegration and equivalent arclength null sets give, for almost every base point x, a local unstable arc gamma about x whose full-arclength subset lies in G. The whole arc lies in supp nu by density and closedness. The map

    Theta(s,r,tau)=Gamma_tau Psi_r gamma(s)

has invertible derivative at (0,0,0). Shrinking its domain gives a C^1 diffeomorphism of a bounded rectangular box onto an open V compactly contained in O, with Jacobian bounded above and below by positive constants.

Bas(nu) is Borel and carrier-invariant. Borel measurability follows using a countable dense family in C_0(R^3), convergence at integer averaging lengths, and continuous cutoffs equal to one on the compact support of nu to pass to bounded continuous functions. The same argument works for the opposite-time basin. It does not require bounded forward Phi orbits. For any fixed vortex time tau, conjugacy gives |Psi_t Gamma_tau y-Psi_t y|<=C_y |tau|exp(-kappa t) for sufficiently large t. Both backward carrier orbits are bounded. Uniform continuity of each test function on a containing compact ball then proves Gamma-invariance of Bas(nu).

The image under Theta of the full-arclength generic subset times the two full intervals therefore has full volume in V and lies in Bas(nu). These boxes exist at nu-almost every point. It follows that D_nu is open, has full basin volume, and nu(D_nu)=1. Its full-volume assertion follows from second countability, selecting a countable subcover of its defining open sets. Carrier and vortex diffeomorphisms preserve its definition, so D_nu is invariant under both complete flows. Every point of Bas(nu) lies in D_nu: a nonnegative continuous function supported compactly in D_nu with positive nu integral forces its backward carrier orbit to enter D_nu. Distinct domains are disjoint since their basins are disjoint and each domain has full basin volume. The separately assumed coverage therefore gives Leb(O minus union_i D_i)=0.

## 7. From zero helicity to zero Bernoulli value on a domain

By Section 5 the sign assumption gives h=0 on each D_i. Fix nu=nu_i. Then H0 is constant along every complete vortex orbit in D_i. Choose one box from Section 6, with generic arc subset T and full-volume image E_box in V. For y=Theta(s,r,tau), s in T, and every real t, conjugacy and invariance give

    H0(Phi_t y)=H0(Phi_(t-r) gamma(s)).

The expression on the right remains on the compact invariant support of nu, so is uniformly bounded. Multiplying H0^2 by a continuous compact cutoff equal to one on supp nu makes a bounded continuous test without changing its values on this orbit. Its positive-time square average therefore tends to m=integral H0^2 dnu by opposite-time genericity of gamma(s). Dominated convergence on E_box gives convergence of the spatial integral of those averages to m Leb(E_box). Section 4 gives convergence of the same integral to zero, since E_box is contained in V. Thus m=0. Continuity implies H0=0 everywhere on supp nu.

The same identity now gives H0=0 on E_box and all its carrier translates. Density and continuity give zero on V and all its translates. A nonnegative compactly supported test inside V with positive nu integral forces every point of Bas(nu) eventually into V under Psi. Carrier invariance therefore gives H0=0 on Bas(nu), and full basin volume and continuity give H0=0 on D_nu.

There is no integration by parts against a singular invariant probability in this argument. Opposite-time genericity is used only on the selected support arc, not on arbitrary physical-basin points.

## 8. Zero-set boundaries and positive stress

Since the D_i cover O modulo a null set, H0 and grad H0 vanish on O and then grad H0 vanishes on its closure. At a boundary point of O, Omega=0, so aU+grad H0=B cross Omega gives U=0 there. Put Z={Omega=0} and D=int Z. Every boundary point of D and every point of Z minus D is in the boundary of O.

Extend U|_D by zero outside D to obtain V. This V is locally Lipschitz. On a convex ball where ||DU||<=L, the segment between two points either stays in D or meets its boundary, where U=0. Using the first exit from each endpoint bounds |V(x)-V(y)| by L|x-y|. Its weak derivative is 1_D DU almost everywhere. On the remaining zero set the derivative vanishes almost everywhere by the density theorem and differentiability of Lipschitz maps. Hence div V=curl V=0 in distributions, so V is entire harmonic. If O is nonempty, V vanishes on that open set and thus vanishes everywhere. It follows that U=0 on Z. If O is empty, U itself is bounded entire harmonic, hence constant, and E(R)=o(R) forces that constant to be zero.

In the nonempty case, grad H0=0 on Z by the Lamb identity, so H0 is globally constant. Its zero quadratic mean forces H0=0. Dotting the Lamb identity with B gives U.B=0. Since H0=P0-|U|^2/2+U.B, we obtain P0=|U|^2/2.

The pressure equation becomes

    partial_i partial_j(U_i U_j)+Delta(|U|^2/2)=0.

Test it against chi(y/R) psi(y), where 0<=chi<=1 is smooth, equals one on B_1, is zero outside B_2, and psi(y)=sqrt(1+|y|^2). After two integrations by parts, all terms differentiating chi have absolute total at most C E(2R)/R=o(1): on the annulus the first cutoff derivative is O(R^-1), the second is O(R^-2), grad psi is bounded, and psi is O(R). The remaining integrand is

    chi(y/R)[U^T D^2 psi U+(|U|^2/2)Delta psi].

Here D^2 psi >= psi^-3 I and Delta psi=(3+2|y|^2)/psi^3>0. For each fixed ball, its integral of |U|^2 psi^-3 is at most the vanishing cutoff error for all large R. Therefore U=0 everywhere. No boundary regularity of Z, finite total energy, pressure limit or sign of the original pressure was assumed.

## 9. Application to the report and unresolved inputs

Report Section 2D assumes decaying U, hence boundedness, and derives E(R)<=CR^beta with beta=5-2/c in [0,1) for 2/5<=c<1/2. This implies every energy requirement above, with room to spare. Its fixed p_inf, vortex completeness, recurrence, product-box transfer, zero extension and positive-stress cutoff agree with the argument here. The exact exponent identity c(beta-1)=-2a explains its stronger transported decay. Arbitrary finite omega is retained throughout.

The smooth coverage theorem supplies the separately assumed measures only at its stated smooth scope; the finite-regularity theorem supplies them under its separate growth condition. This audit neither establishes automatic C^2 coverage nor derives the helicity-sign premise. It does not re-prove the energy law, the coverage theorem, the Ledrappier-Young entropy theorem, the unused density formula rho=C ell, or the levelwise corollaries of Section 2D. The unrestricted rotating Euler conjecture remains OPEN.

Status at initial reconstruction: all nine sections independently reconstructed and postread. The subsequently received comparisons are checked below. Actual provider execution is independently unattested.


## 10. Existing Theory Agent A  comparison and diagnostic scope

The complete 117-line Theory Agent A  comparison, all 62 lines of its script and its complete two-line log were read. The comparison independently covers all nine sections and the six specifically requested interfaces. It agrees with the proof, including the weaker energy premise and all separate measure and sign assumptions. Its reference to report Sections 2A and 2D is consistent with the retained extracts. No new report theorem or removal of an OPEN premise follows.

Two optional constant improvements are correct. Stieltjes integration by parts gives

    S(R)=-E(R)/R^3+3 integral_R^infinity E(r)r^-4 dr
         <=(3/2)eta(R)R^-2,

where the far endpoint vanishes because E(r)=o(r). The weaker factor 8/3 used above is therefore valid. Also, for R>=1 and R<=|y|<=2R, psi(y)<=3R. The cutoff errors in Section 8 are bounded by

    [3||grad chi||_infinity+3||D^2 chi||_infinity
       +(3/2)||Delta chi||_infinity] E(2R)/R.

The first coefficient combines the two velocity cross terms and one pressure cross term. The other two follow from the bound on psi. Replacing 3/2 by 2, as in the report, remains an upper bound.

The retained script log contains fourteen True entries and PASS. Thirteen are symbolic identities or exact symbolic scalar calculations: the Lamb identity, the bracket identity, three pressure-pairing identities, two tail constants, the report's beta=1 constant, the kernel extremum, the Hessian and Laplacian identities, the recurrence exponent interval and the exponent-rate identity. The remaining item computes eigenvalues only at y=(1,2,3). It is a finite exact sample, not a proof of positive semidefiniteness for every y. The required general fact follows directly from |y|^2|v|^2-(y.v)^2>=0 by Cauchy-Schwarz. The symbolic declaration omega>0 in the script does not certify the other signs by itself; the manually derived polynomial identities and orthogonality arguments above apply to every real omega.

The script prints FAIL if an assertion is false but does not itself set a nonzero exit status. Its displayed Boolean results, rather than a successful process status, are the evidence. None of these calculations is a proof premise, and this agent did not rerun the script.

## 11. Literature-agent reconstruction and final scope

The complete independent nine-section literature-agent reconstruction was read and retained. It agrees with Sections 1-9, including the exact positive-density input, the common pressure constant, complete vortex conjugacy, the distinction between full-flow and time-one ergodicity, the two-sided generic support arc, and zero extension across an arbitrary irrotational boundary. The version read has SHA256 5dad67f6e39099ebb78755b6af26aef41495c07b3a9ba937f4492b397130396c.

In particular its recurrence argument uses ambient Lebesgue measure, not the possibly singular invariant probabilities. Its transfer to a generic product box does not assume that all basin points are generic in the opposite time direction. The final positive test uses E(2R)/R tending to zero, not a missing finite-energy or pointwise pressure-decay premise. Its statement has the same explicit coverage, spectrum, entropy and one-sign assumptions as Section 1.

The conditional analytic theorem is CONFIRMED in A3015 and the qualified comparisons in A3016; the stronger conclusion remains OPEN in A3017. They neither derive the measure package for all C^2 profiles nor force one sign of helicity on its essential domains. The unrestricted rotating Euler conjecture remains OPEN. The external source audit A2948-A2949 remains an input; the entropy and Pesin theorems are not re-proved by this comparison. Existing configured model file collaboration is recorded, while actual provider execution is independently unattested.

## 12. Equivalent energy formulation under the profile equation

The additional observation in Theory Agent A A109 is correct. Let U and P be global C^1 solutions of the same profile equation, let U be bounded, and let 0<c<1/2. Write Hb for U(R.) tending to zero in distributions as R tends to infinity, together with boundedness. Then

    Hb if and only if E(R)=o(R).

The reverse implication is already proved in Section 3: on each fixed ball B_L, the squared L^2 norm of U(R.) is R^(-3)E(LR)=o(R^(-2)), which implies distributional convergence. For the forward implication use the separately audited energy law, not an assertion about arbitrary bounded functions. If 0<c<2/5 it gives U=0. If c=2/5 it gives finite total energy, so E(R)=O(1)=o(R). If 2/5<c<1/2 it gives E(R)=O(R^(5-2/c)), whose exponent is strictly smaller than one. These exhaust the interval.

Consequently the conditional theorem of Section 1 can equivalently be stated with Hb. The measure, spectrum, entropy and basinwise sign hypotheses remain. For 0<c<2/5 the energy theorem already gives zero without those extra hypotheses; the analytic-interface argument adds no new conclusion there.

For precision, the quantity estimated by o(R^3) in Section 4 is the unnormalized integral of H0^2 over B_R. Its volume-normalized square mean tends to zero. Occurrences of "o(R^3) square mean" in summaries should be written as "the integral of H0^2 over B_R is o(R^3)". This is a wording clarification of the existing estimate.

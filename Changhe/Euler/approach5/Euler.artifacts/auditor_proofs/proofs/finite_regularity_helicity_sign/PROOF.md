# One-sign helicity rigidity at finite regularity under intrinsic core growth

Status: CONFIRMED A422 after independent reconstruction and focused configured-model and literature reviews. The additional derivative-growth bound and one-sign basin premise remain theorem hypotheses.

## 1. Exact theorem

Let 2/5<=c<1/2, let omega be any finite real number, and let r>=2 be an integer. Let U in C^r(R3;R3) and P in C1(R3) solve

    div U=0,
    (1-c)U+[(cI-omega J)y+U].grad U+omega JU+grad P=0,
    U(y)->0 uniformly as |y|->infinity.

Set A=cI-omega J, B=Ay+U, Omega=curl U, O={Omega!=0}, a=1-2c>0, kappa=1+c, and h=U.Omega. Let Psi be the flow of -B. For a sufficiently large closed ball Q with B.y>0 on and outside its boundary define

    M_n=max(1,max_(y in Q)||D Psi_n(y)||),
    Lambda_core=lim_(n->infinity) n^-1 log M_n.

Assume

    r(1-2c)>Lambda_core.                              (C)

The limit exists and is independent of the admissible ball and norm by A398. For every compactly supported full-flow-ergodic vortical SRB probability supplied by A417, let D_nu be its invariant open essential basin from A223. If h has one sign on each such D_nu, with the sign allowed to depend on the basin, then U=0.

In particular U=0 if h>=0 everywhere or h<=0 everywhere. The hypothesis h=0 everywhere is included. No Dini strain decay, finite energy, axisymmetry, Fourier restriction, mixing or nonsingular uniformly hyperbolic support is assumed.

Equivalently, every nonzero C^r decaying profile in this range satisfying (C) has at least one essential vortical SRB basin on which h takes both positive and negative values. Each sign then occurs on a positive-volume open subset of that basin. The associated measure gives full mass to B!=0 and Omega!=0, has spectrum (1-2c,0,-1-c), and entropy 1-2c. Its topological support may still meet either zero set.

This is a conditional Liouville theorem and a necessary sign-changing-basin condition. It does not exclude the sign-changing case and does not prove the full conjecture.

## 2. The basin data follow from the stated growth hypothesis

The C^r field B is complete and radially outward at infinity. It obeys div B=3c and [B,Omega]=-kappa Omega, with kappa>3c. The fully proved finite-regularity coverage theorem A417 applies under (C), including r=2. It supplies countably many full-flow-ergodic vortical SRB measures whose continuous-time basins cover almost every point of O. This invocation retains the entire hypothesis (C); it does not infer it from boundedness or decay.

The C2 endpoint has been checked separately in A417: incoming arcs are C1,1, the carrier is C2 and Omega is C1. The zero-set capture, full unstable absolute continuity and original-target capture arguments require no additional velocity derivative. The topological supports may intersect B=0 or Omega=0, while each measure gives those sets zero mass. No uniform hyperbolicity or mixing is assumed.

For these actual Euler fields, the one-form alpha=(B cross Omega).dy has the exact expanding covariance with rate a and is invariant under the local Omega flow. A207 gives strictly positive local unstable conditional densities, proportional to positive alpha-length. A223 therefore gives pairwise disjoint invariant open sets D_nu with Bas(nu) subset D_nu, full basin volume in D_nu, and nu(D_nu)=1. Their union covers O modulo a null set. All support, density and coverage premises used below follow from the profile hypotheses and (C). A207 and A223 use only a C2 carrier, C1 transported vorticity and the stated measure data, so they apply at r=2.

## 3. The sign hypothesis gives zero helicity on each basin

The complete Omega flow Gamma is almost everywhere recurrent for every C2 uniformly sublinear profile in this parameter range, by A048-A049. Here is the argument needed below. The carrier flow Phi is complete and its negative semiorbits from compact sets remain in a compact ball. If Gamma is initially defined for short times near that ball, the local bracket identity extends it by

    Gamma_s x=Phi_T Gamma_(s exp(-kappa T)) Phi_-T x.

For sufficiently large T the inner time is in its uniform local interval. Uniqueness makes the extensions consistent and proves completeness and

    Phi_t Gamma_s=Gamma_(s exp(kappa t)) Phi_t.

Sublinearity and variation of constants bound Phi_T growth by C exp((c+epsilon)T). Taking T=kappa^-1 log(1+|s|/delta) gives, on each fixed compact K,

    sup_(x in K)|Gamma_s x|<=C_(K,epsilon)(1+|s|)^((c+epsilon)/kappa).

Choose epsilon>0 with 3(c+epsilon)<kappa. Since div Omega=0, Gamma preserves volume. The first N images under Gamma_1 of a bounded wandering set are disjoint but lie in a ball of volume O(N^(3(c+epsilon)/kappa)). Hence that set has zero volume. Apply the same argument to Gamma_N for every positive integer N, and to Gamma_-N. Each has the same sublinear-in-N confinement exponent with a constant depending on the fixed step. Applying it to no-return sets in a countable basis of bounded balls gives, on one full-measure set, returns in both directions at arbitrarily large times. This is the two-sided recurrence needed below. This uses neither bounded vortex lines nor finite total volume. The sets D_nu are invariant under this complete flow. By A223, D_nu is the union of open V in O for which Leb(V minus Bas(nu))=0. Exact conjugacy turns a fixed finite vortex shift into an exponentially small shift along a bounded backward carrier orbit, so it preserves continuous-time basin membership. Each Gamma_s is a C1 diffeomorphism preserving O and null sets, hence maps this defining union onto itself.

Let H0=P0+|U|^2/2+Ay.U, where P0 is the canonical pressure representative from A031. The exact Lamb and helicity identities are

    aU+grad H0=B cross Omega,
    Omega H0=-a h.

If h>=0 on D_nu, H0 is nonincreasing along each Gamma orbit there. If h were strictly positive anywhere, continuity would give a small open ball inside D_nu and a common positive vortex time on which H0 drops strictly. Almost every point of that ball is recurrent. Monotonicity prevents its H0 values from returning arbitrarily close to their initial values, contradicting recurrence and continuity. Hence h=0 on D_nu. Applying the same argument to -H0 treats h<=0. This is A283, with all invariance and completeness hypotheses checked here.

Thus the theorem's one-sign premise yields h=0 on every essential basin.

## 4. Bernoulli mean decay makes it constant on each basin

We recall the complete mechanism of A277-A278 to specify exactly which analytic information is used. Put beta=5-2/c, so 0<=beta<1. The canonical pressure and energy estimates give one fixed representative H0 with

    integral_(|y|<R)|H0|^2<=C R^(beta+2),    R>=1,
    integral_Q |H0(Phi_t y)|^2dy<=C_Q exp(-2a t)

for every bounded measurable Q, where Phi is the forward B flow. The second estimate uses det DPhi_t=exp(3ct) and |Phi_t y|<=exp(ct)(|y|+||U||_infinity/c). It assumes neither finite energy nor pointwise decay of P0.

Fix nu and its essential basin D_nu, now with h=0. Positive unstable conditional density gives a local unstable arc with a full-arclength set T of two-sided generic support points. The entire arc lies in supp(nu): almost every plaque point does by the conditional density, and the support is closed. At a regular point the unstable tangent, -B and Omega are independent. The map C(s,r,tau)=Gamma_tau Psi_r gamma(s) is a local C1 coordinate map in D_nu. The image E of T times a smaller rectangle has full volume in a small open box V.

Since Omega H0=0 on D_nu and the basin is invariant under the complete vortex flow, exact conjugacy gives, for all real t and y=C(s,r,tau) with s in T,

    H0(Phi_t y)=H0(Phi_(t-r) gamma(s)).

For the displayed equality, Phi_t y=Gamma_(tau exp(kappa t)) Phi_(t-r) gamma(s); the latter carrier point belongs to D_nu, and the complete Gamma orbit stays in D_nu where Omega H0=0. The right side stays on the compact invariant support. Its positive-time square average tends to integral H0^2 dnu, using the two-sided generic points. Dominated convergence over E, followed by the exponentially decaying spatial estimate above, gives

    Leb(E) integral H0^2 dnu=0.

Therefore H0 vanishes on supp(nu), by continuity. The same identity makes it vanish on every carrier translate of E and hence on every translate of V. Their invariant open union contains a support point and has positive nu measure. A nonnegative compactly supported observable inside that union has positive nu integral, so every basin point eventually enters it. Invariance places the whole basin in it. Since the basin has full volume in D_nu, continuity yields H0=0 on D_nu.

This step uses no integration by parts against a measure singular in the vortex direction. It does not presume backward genericity of arbitrary physical-basin points.

## 5. Localization and the global positive-stress argument

The essential basins cover O modulo a null set. Hence grad H0=0 everywhere on O by continuity. Let Z={Omega=0}. At every boundary point of O, the Lamb identity and continuity imply U=0.

Every boundary point of D=int(Z) lies in the boundary of O, since a point of Z outside its interior is approached by O. Hence U=0 on the boundary of D. On D, extend U by zero outside D. The extension is locally Lipschitz: near a boundary point, use U=0 there and the local bound on DU to estimate by distance to the boundary. Its weak derivative equals 1_D DU almost everywhere; on its zero set the weak derivative vanishes almost everywhere. Therefore its distributional divergence and curl both vanish. It is entire harmonic and vanishes on the nonempty open set O, so it vanishes everywhere by unique continuation. If O was empty, the original U was already entire harmonic and decaying, and hence zero. Thus U=0 on D and on all remaining points of Z as well.

The Lamb identity now gives grad H0=0 on Z, so H0 is globally constant. Its normalized quadratic mean tends to zero by beta<1, forcing that constant to be zero. Dotting the Lamb identity with B gives U.B=0. Since H0=P0-|U|^2/2+U.B, it follows that P0=q=|U|^2/2.

Taking the divergence of momentum cancels the two rotation terms exactly, while the linear c term vanishes by div U=0. The pressure equation is therefore

    partial_i partial_j(U_i U_j)+Delta q=0.

Test it against chi(y/R) sqrt(1+|y|^2), where chi is a nonnegative smooth cutoff equal to one on the unit ball. All terms differentiating chi are bounded in absolute value by C R^(-1) integral_(|y|<2R)|U|^2<=C R^(beta-1), which tends to zero. The remaining integrand is

    chi(y/R)[U^T D2 sqrt(1+|y|^2) U
                       +q Delta sqrt(1+|y|^2)].

Writing rho=sqrt(1+|y|^2), one has D2 rho>=rho^(-3)I and Delta rho=(2|y|^2+3)rho^(-3). The integrand is nonnegative and strictly positive wherever U!=0. On each fixed ball its integral is bounded by the vanishing cutoff error for sufficiently large R. Thus U=0 everywhere.

## 6. Contrapositive and scope

If a nonzero profile existed, some essential basin would violate the one-sign condition. Since h is a continuous real function, that means it takes both signs there. Its strict-sign sets are nonempty and open, hence have positive volume; removing the null nongeneric set leaves positive-volume sets of physical-basin points of both signs.

No claim is made that every essential basin must have both signs. No statement about the sign or values of h on the entire singular support is inferred from its Lebesgue basin. The conclusion at r=2 retains the strict condition Lambda_core<2(1-2c). Equivalently, if O is nonempty, let K=intersection_(t>=0) Psi_t Q and Z=K intersect ({B=0} union {Omega=0}). A399 gives Lambda_core=max(a,Gamma_Z), where Gamma_Z is the attained maximal top exponent of all full-flow-ergodic invariant probabilities on Z, with value negative infinity when Z is empty. Thus (C) is equivalent to Gamma_Z<r a. This includes entropy-zero measures and equilibria; controlling only physical measures is insufficient.

If r is arbitrarily large, the core growth is finite and some integer r satisfies (C), recovering the C-infinity theorem A309. For fixed r, no estimate establishing (C) from decay alone has been proved. A415 shows that local Euler identities alone cannot establish it. The displayed result therefore does not settle the unrestricted C2 helicity-free case, the sign-changing case or the main conjecture. The range 0<c<2/5 already has the stronger bounded-profile constancy theorem A407, which does not use (C) or a sign assumption.

## Dependencies and verification

The analytic proof above is the A309 proof with its only C-infinity input replaced by A417. The complete A277-A278 pressure and given-measure argument, A283 complete recurrent vortex-flow argument, and A417 finite-regularity coverage proof were reread. All analytic steps require at most U in C2 and P in C1. In particular Euler makes P in C2 locally, the Lamb identity is C1, both flows are C1, the local box is C1, and the arbitrary-boundary extension is locally Lipschitz. No Sard theorem, third derivative or density of the vortical set is used in this deduction.

Standalone dependencies: conditional coverage, fixed-pressure mean decay and localization, complete recurrence and sign rigidity, pressure normalization, energy growth, positive unstable densities, essential basin domains, and intrinsic zero-stratum growth. Snapshots are in verification with hashes.

The coordinator's first configured with the primary model review checked the predecessor partition proposal and its C2 interfaces. Its separate finite_regularity_liouville_review, written at 02:26Z on November3, directly checked this transfer and found no gap. The independent literature review likewise reconstructed the full transfer. All six coordinator precision items were checked and incorporated above; immutable copies of both reviews are in verification. The stated model is configuration, not independent provider attestation. No new model client, numerical computation, formal build or server is used.

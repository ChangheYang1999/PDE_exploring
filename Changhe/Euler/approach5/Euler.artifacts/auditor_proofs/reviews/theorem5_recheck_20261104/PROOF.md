# Repeated independent audit of the helicity-sign Liouville theorem

This audit rechecks all of report Section2D at the exact fc469b9c5442c992058a62b25366fa81f4fb398822b86714b3772d6d8d8ba561 assembly, lines3042-4131, and compares the complete existing Theory Agent A  recheck in the team records. It confirms the mathematical chain at its stated conditional scope. It finds one editorial chronology ambiguity, not a new mathematical gap. The source theorems listed below remain explicit dependencies; this is not a fresh reading of every external primary source.

## 1. Exact theorem and dependencies

Let 2/5<=c<1/2 and omega be any finite real number. Let J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J, and assume U in C-infinity(R3;R3), P in C1(R3), with

    (1-c)U+(Ay+U).grad U+omega JU+grad P=0,
    div U=0,
    sup_(|y|>=R)|U(y)| ->0 as R->infinity.

Put B=Ay+U, Omega=curl U, h=U.Omega, a=1-2c>0, kappa=1+c, d=3c and O={Omega!=0}. Let Phi be the B flow, Psi_t=Phi_(-t), and Gamma the Omega flow. The confirmed smooth coverage theorem A308 supplies an at most countable family F of compactly supported full-flow-ergodic Psi-invariant probabilities. Each nu gives full mass to {B!=0,Omega!=0}, has Psi_1 spectrum (a,0,-kappa), entropy a, and positive unstable conditional densities; their continuous-time basins cover O up to Lebesgue measure zero.

Define Bas(nu) by convergence of time averages along Psi to nu for every bounded continuous test function. Its essential domain D_nu is the union of open subsets V of O on which V minus Bas(nu) is Lebesgue null. Assume h>=0 on D_nu or h<=0 on D_nu for each nu separately. Then U=0.

This is Theorem5/Theorem L-infinity, CONDITIONAL on this sign assumption. The more general C2 proposition instead assumes the coverage package explicitly. Theorem A of Section2A supplies the energy growth and pressure decomposition. A308 supplies smooth coverage. The external qualitative inputs in the basin argument are Oseledets, Pesin unstable manifolds and Ledrappier-Young positive densities, with the previously verified nonergodic time-one formulation. Neither the sign nor unrestricted C2 coverage is derived here.

## 2. Identities, complete flows and recurrence

Decay gives M=sup|U|<infinity. The carrier B has linear growth, so its C1 flow is complete. Variation of constants and the orthogonality of exp(-omega Jt) give |Phi_t x|<=exp(ct)(|x|+M/c) for t>=0; backward trajectories enter and stay in any sufficiently large ball. Direct curl and vector identities give

    aU+grad H0=B cross Omega,
    Omega.grad H0=-a h,
    [B,Omega]=-kappa Omega,
    D Phi_t(x) Omega(x)=exp(kappa t) Omega(Phi_t x),

where H0 is the normalized function in Section3. Thus Phi_t Gamma_s=Gamma_(s exp(kappa t)) Phi_t whenever the local flows are defined.

For any finite s and x, take T large so Psi_T x lies in a fixed compact ball and |s|exp(-kappa T) lies within a uniform local Omega existence interval on that ball. The expression Phi_T Gamma_(s exp(-kappa T)) Psi_T x extends the local vortex flow. Uniqueness makes the extensions consistent and proves completeness for every s. Choosing T logarithmic in 1+|s| bounds Gamma_s x by a constant times (1+|s|)^(c/kappa), uniformly for x in any fixed bounded set. No global bound on Omega is required.

The Gamma flow preserves volume, because div Omega=0. A positive-volume wandering set in a bounded region would have n disjoint integer iterates with total volume proportional to n, all within a ball of volume O(n^(3c/kappa)). Since 3c/kappa<1, this is impossible. Taking a countable basis of bounded balls gives recurrence in both integer time directions for almost every point. This recurrence requires c<1/2 and contains no restriction on omega.

## 3. Energy, pressure and transported Bernoulli means

Set beta=5-2/c, so 0<=beta<1. Section2A gives E(R)=integral_(B_R)|U|^2<=C_E R^beta for R>=1. At c=2/5 one may take C_E=||U||2^2. Above that endpoint the printed constant is 2^beta(L+C_A/2), with L and C_A supplied by Section2A; monotonicity covers 1<=R<=2.

For rho>=1/2, the dyadic shell sum gives

    integral_(|z|>=rho)|U(z)|^2 |z|^(-3) dz
       <=C_S rho^(beta-3),
    C_S=2^beta C_E/(1-2^(beta-3)).

The lower radius condition makes every energy bound used in the sum valid. The near pressure term is the Riesz multiplier applied to U tensor U cut off at radius4R; its squared L2 norm is bounded by the integral of |U|^4, by the Hilbert-Schmidt contraction bound. The far kernel has absolute bound (4/pi)|U(z)|^2|z|^(-3) when |x|<2R and |z|>=4R. Consistency of the decompositions on overlapping balls, using Section2A fact(F1), makes p_R-c_R independent of R. Hence a single constant p_inf and P0=P-p_inf are obtained, without an unjustified pressure condition at infinity.

Using the decomposition at radius R/2 yields

    integral_(B_R)|P0|^2 <= C_P R^beta,
    C_P=2^(1+beta)M^2 C_E+2^(2beta+1)C_S^2/(3pi).

The far contribution before simplification is proportional to R^(2beta-3), bounded by R^beta for R>=1. Put H0=P0+|U|^2/2+(Ay).U. Since |Ay|^2=c^2|y|^2+omega^2(y1^2+y2^2),

    integral_(B_R)|H0|^2<=C_H R^(beta+2),
    C_H=3[C_P+M^2 C_E/4+(c^2+omega^2)C_E].

Its normalized ball mean tends to0, since beta<1. If two such representatives differ by a constant k, k^2 is bounded by twice the sum of their normalized means, so k=0. This also identifies the pressure route with the earlier A031/A278 representative.

For a fixed bounded measurable set V, the Jacobian of Phi_t is exp(3ct), and Phi_t V lies in B_(rho_t), with rho_t=(R'+M/c)exp(ct) for a suitable R'>=1. Thus

    integral_V |H0(Phi_t x)|^2 dx
       <=exp(-3ct) C_H rho_t^(beta+2) ->0,

because c(beta-1)=-2a<0. This is an unnormalized integral over a fixed set, sufficient for the basin argument.

## 4. Essential domains and the use of unstable densities

A countable family of compactly supported continuous tests, together with tightness, makes Bas(nu) Borel. Forward carrier trajectories need not be bounded; tightness is therefore retained for Bas^-(nu). Birkhoff applied to time one and the flow-invariance of the time-average limsup give two-sided genericity from full-flow ergodicity. Time-one ergodicity is not silently assumed.

For a regular point in the compact support, the identities for D Psi on B and Omega and two-sided recurrence place Omega in E^s and B in E^0. Their cross-product one-form is nonzero on E^u. The compact cutoff model agrees with Psi near the trapped core; every full unstable manifold stays there, because a backward orbit outside the enclosing sphere could not converge to the support. The metric may be chosen Euclidean near this core. The Ledrappier-Young density conclusion is used for the compact model without assuming time-one ergodicity. Its strictly positive densities give equivalence with arclength, which is stronger than mere absolute continuity and is the property needed here.

At almost every regular base point, choose a local unstable arc gamma. A full-arclength subset T consists of points generic in both directions and in the compact support. The arc itself is in that support by closedness and density of T. The map

    Theta(s,r,tau)=Gamma_tau Psi_r gamma(s)

is a C1 local diffeomorphism, because E^u, B and Omega are independent. The conjugacy contracts the vortex parameter under Psi, so Gamma preserves Bas(nu); finite carrier shifts also preserve it. Fubini and the local change of variables show that the corresponding box V has full-volume basin. Such boxes occur at nu-almost every base point, whence nu(D_nu)=1. Flow invariance, disjointness for distinct nu and almost-everywhere coverage follow from the definition, basin uniqueness and the assumed coverage package. A basin point lies in D_nu by averaging a positive compactly supported bump inside D_nu and using invariance. These arguments permit supports to meet the zero sets, even though nu gives those sets zero mass.

## 5. A sign forces zero Bernoulli value on every essential domain

On D_nu a fixed sign of h makes H0 along Gamma monotone, since d(H0(Gamma_s x))/ds=-a h(Gamma_s x). If h(x0)>0, continuity provides a box of positive volume on which H0 drops by a uniform positive amount during a fixed short time. Almost-everywhere recurrence supplies a point returning arbitrarily close to its start after that drop, contradicting continuity and monotonicity. The negative case reverses the signs. Thus h=0 throughout D_nu, and H0 is constant along each vortex curve there.

For the box of Section4, conjugacy and this constancy give

    H0(Phi_t Theta(s,r,tau))=H0(Phi_(t-r) gamma(s)).

For s in T, two-sided genericity on the compact support implies that the time average of the square of the right side tends to m=integral H0^2 dnu. It is uniformly bounded by the compact-support maximum. Dominated convergence and change of variables therefore make the time average of the integral over V tend to m times volume(V). Section3 makes that same quantity tend to0. Hence m=0. Continuity gives H0=0 on supp nu, then on each such box and all of its carrier saturations. Every basin point reaches a box saturation by the positive-bump argument. Thus H0=0 on Bas(nu), and continuity plus its full-volume property gives H0=0 on D_nu.

Coverage makes the union of D_nu dense in O: a missing open subset of O would have positive volume. Consequently H0 and grad H0 vanish on closure(O).

## 6. Zero extension and the positive-stress conclusion

On the boundary of O, Omega=0. The identity aU+grad H0=B cross Omega, with a>0, gives U=0 there. Let D_Z=int{Omega=0} and extend U restricted to D_Z by zero elsewhere, calling the result V. On a compact ball, U has a common Lipschitz constant. The first and last crossings of a line segment through the boundary of D_Z show that V has the same local Lipschitz bound, since U is zero on that boundary. Its weak derivative equals 1_(D_Z)DU almost everywhere: a Lipschitz function has derivative zero almost everywhere on its zero set. This handles a boundary of positive volume. Thus div V=curl V=0 distributionally. Weyl's lemma makes V harmonic and analytic; it vanishes on the nonempty open O, so V=0. Since Z minus D_Z is contained in the boundary of O, where U already vanishes, U=0 on all of Z. If O is empty from the start, U is an entire bounded harmonic vector and decay already gives U=0.

Now U.B=0 and grad H0=0 globally. The vanishing normalized means fix H0=0, so P0=|U|^2/2. Divergence of the Euler equation cancels the two rotation terms exactly, giving

    Delta P0+partial_i partial_j(U_i U_j)=0.

For psi=(1+|y|^2)^(1/2) and a smooth radial cutoff chi_R, testing this distributional identity gives the positive interior integral

    integral chi_R [U tensor U:D2 psi+(|U|^2/2) Delta psi]

bounded in absolute value by C_chi R^(-1) E(2R). The independently recomputed error coefficient is at most 3||grad chi||+3||D2 chi||+(3/2)||Delta chi||; the printed coefficient with2 in the last term is admissible. The bound tends to0, since beta<1. Meanwhile D2 psi>=psi^(-3)I and Delta psi=(2|y|^2+3)/psi^3>0. Restricting to any fixed ball forces the integral of |U|^2 psi^(-3) there to vanish. Therefore U=0 everywhere.

## 7. Other scope checks

For C^r profiles, r>=2, the report supplies coverage only under its explicit growth condition Gamma_E<r(1-2c) on every vortical component, or a stronger global sufficient condition. Decay does not establish this. For smooth U, the already confirmed A308 supplies coverage directly; equivalently a sufficiently large finite r meets the global growth bound on a compact core. Both routes retain the helicity-sign hypothesis.

Corollary5.3 uses smooth Omega: Delta U=-curl Omega and local elliptic regularity make U smooth. This step does not promote arbitrary C2 profiles. The same-level sign argument in Lemma18 correctly uses a first upper-level crossing and a last lower-level crossing, then the mean value theorem and local inverse branches. It yields an interval with opposite crossing signs under its recurrence hypothesis, not a statement about every vortex line. All omega dependence in the estimates is finite and permitted; no uniform-in-omega quantitative bound is asserted.

## 8. The chronology ambiguity in A100 H1

The paragraph headed Coordinator check(03:34Z) in Section2D.4 says the printed Ledrappier-Young statements had not been checked. The same section's points5 and9 correctly record A479's later visual source check. A479 is dated2026-11-03T05:02:03.420287Z and explicitly records that coverage. The old paragraph is also present in a retained November3 snapshot. These facts establish that this is a historical observation, not the current state of verification. Merely finding it in that snapshot does not by itself prove the exact date of the earlier03:34 event; the surrounding report provenance identifies that earlier campaign stage.

A safe repair is: Coordinator check(earlier03:34Z record): the printed statements had not been checked at that time; the later independent A479 check verified them, as points5 and9 record. The date2026-11-03 may be used if confirmed from the coordinator's own shift record. No mathematical statement or label changes. This agent has read the full A479 entry again, but has not newly reread the external paper for this recheck.

## 9. Verification and collaboration record

All of report Section2D and the entire A100 file were read, with overlapping ranges to fill the one truncated display. Constants, scaling, identities, completeness, recurrence, pressure consistency, positive-density use, zero-set extension and the final cutoff limit were independently checked as above. Section2A inputs and A308 remain explicitly imported from their earlier independent confirmations. The A-working file is the existing configured model comparison; actual provider execution is independently unattested. No new model client or agent was used. There was no mathematical computation, formalization or primary-source retrieval in this recheck.

## 10. Additional literature-agent scope review

The complete seven-section review in the literature agent, submitted as helicity-chain-final-scope, and all fifteen of its manual checks have now been read. Exact copies are retained in the team records. This is a separate reader's check of actual Section2D at the later97da5b93 pin. It explicitly imports Sections2A and2C instead of claiming to reprove them, and attributes the fresh Ledrappier-Young source reading to this auditor. Its statement keeps the smooth theorem, the finite-Cr growth condition and the stipulated C2 coverage package distinct.

Its flow completeness, polynomial vortex bound, recurrence exponent, pressure constants, full-arclength product box, dominated-convergence step, positive-volume zero-set extension and positive stress cutoff agree with Sections1-7 above. The normalized pressure constant is fixed once before the transported estimate. No uniform derivative bound at spatial infinity or time-one ergodicity is smuggled into the argument. The optional density formula in Lemma11(c) is not a dependency. Its reported omission of a fresh proof of CorollaryL.5 is not silently filled by this comparison.

The full existing configured model Theory Agent A  recheck, including the later Section2A addendum, was also read. The separate nine-section energy-law reconstruction now supplies a fresh direct check of the principal imported energy and pressure input. The general coverage theorem remains an explicit previously audited input. No new helicity sign condition, unrestricted finite-regularity coverage result or unconditional Euler theorem follows. Actual provider execution remains independently unattested. No computation was used.

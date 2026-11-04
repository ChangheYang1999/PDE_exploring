# Audit of report 8534ae9c at cutoff A3115

Status: mathematical transfers checked at the scopes below; cumulative approval waits for the two wording corrections in Section 5.

## 1. Object, reading scope and dependencies

The retained report has SHA256 8534ae9ca0ea5c5f135fe582195a9ab7e53efa70854272b1455bd6a2e79532ce, 7723 lines and 1219008 bytes. Its pin, the report and Euler.report copies were independently identical at the capture time in the team records. The complete 292-line normal difference from b2d9c61c was read, with the long table rows separately reread to avoid output truncation. Independent unified differences from b2d9c61c and the last approved 86286d44 are retained. This is a delta audit, not a fresh complete reading of all 7723 lines.

The b2d9c61c audit is in the team records. Its sole requested correction, concerning the constant profile and work sign, is now made exactly. Its other transfers retain their confirmed scopes. Approval of 86286d44 in A3083 covered the front matter, Sections 0-10 and Appendix A; historical Appendices B and C were not collectively approved. That boundary remains in force.

Dependencies for the new mathematics are the independent proofs of A3094-A3107 in the positive-source, critical-logarithmic, Holder and mean-work review folders, including the complete existing A and C comparisons. A3108-A3110 cover only the historical literature handoff and its file inventory. A3111 covers status-only source revisions. A3112-A3115 repeat the already established pressure-core, actual-pressure symmetry, energy and ordinary nonrotating theorems. Those last four introduce no change of theorem scope. No calculation or provider-execution claim of a different agent is certified merely by its appearance in the report.

Notation throughout: J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J, and the full profile equation is (1-c)U+((Ay+U).grad)U+omega JU+grad P=0 with div U=0. Hb means U(R.) tends to zero in distributions on R3 as R tends to infinity. C1 and C2 mean continuously differentiable and twice continuously differentiable, respectively; all norms of matrices below are Frobenius norms. Every constant in a field estimate may depend on the field and on the explicitly fixed parameters unless stated otherwise.

## 2. Mean work and the constant-profile correction

Let U and P be C1 on R3, div U = 0, and suppose the full momentum equation holds with 0 < c < 1 and arbitrary finite omega. Write e = |U|^2/2, w = U.grad(P+e), and put bars on spherical means about the origin. Dotting momentum with U gives

    w = -2(1-c)e - c y.grad e + omega d_phi e.

The angular derivative has zero spherical mean. With k = 2(1-c)/c > 0,

    wbar(r) = -c r^(1-k) (r^k ebar(r))'.

Continuity gives r^k ebar(r) -> 0 at the origin. If wbar is nonnegative at every radius, r^k ebar is nonincreasing from zero and is also nonnegative. It therefore vanishes, and so does U. No condition at infinity is used.

For bounded Hb profiles with 0 < c < 1/2, the opposite global sign is impossible for a nonzero profile. Below 2/5 this follows from the energy theorem. At 2/5, nondecreasing g = r E'(r), starting at zero, would make finite total energy impossible unless g = 0. Above 2/5 put beta = 5-2/c in (0,1). The same identity makes g = r^(1-beta) E' = 8 pi r^k ebar nondecreasing when wbar <= 0. The energy ratio forces g <= beta L: if g exceeds beta L at one radius, its monotonicity forces a strictly larger leading energy coefficient. Thus

    L R^beta - E(R) = integral_0^R (beta L-g(r)) r^(beta-1) dr.

The right side is nonnegative, nondecreasing and bounded below by a positive constant at large R, since g(0)=0 and L>0. The precise energy error makes the left side tend to zero. This is a contradiction. Hence both strict signs of wbar occur. They are asserted only at some radii about the origin; no translation or arbitrary-far recurrence is inferred.

The corrected constant example has U=a nonzero and P=-[(1-c)a+omega Ja].y. It has w=-(1-c)|a|^2, but fails Hb and every finite Ls condition. It proves that one-signed work and uniform sublinearity alone do not imply U=0. It does not refute any of the stated bounded-Hb or integrable criteria.

## 3. Critical source weight and derivative consequences

For C1 divergence-free U define q=tr((DU)^2). In distributions q=partial_i partial_j(U_i U_j). Let E(R)=integral_(B_R)|U|^2 and suppose E(R)/(L R^beta)->1 with L>0 and 0<beta<1. Put m=2-beta. The uncut weight phi=|y|^m is C1, locally W2,1, and convex, with

    D2 phi = m r^(-beta)(I-beta e_r tensor e_r)
              >= m(1-beta) r^(-beta) I.

A smooth radial cutoff equal to one on B_R and zero outside B_(2R) gives a separate annular Hessian error bounded by C R^(-beta) E(2R). The localized test is not itself convex. Integration by parts and positivity yield the critical positive-source lower bound. The radial energy identity is

    integral_(B_R) r^(-beta)|U|^2
      = R^(-beta) E(R) + beta integral_0^R t^(-beta-1) E(t) dt.

It equals beta L log R + o(log R) under the ratio hypothesis. Under the stronger error E(R)=L R^beta+O(R^(beta-1)), it equals beta L log R+O(1). Consequently the former premise yields only the asserted lower limit with coefficient k_beta=beta(2-beta)(1-beta); the latter yields the additive lower bound k_beta L log R-C. The signed localized pairing has lower and upper coefficients k_beta L and beta(2-beta)L, with additive bounded errors under that same stronger premise. With only a ratio limit its errors are o(log R).

The radial cutoff tests depend only on Q_a(r)=integral_(S2)q(a+r theta). When a C1 pressure P satisfying Delta P=-q is present, the distributional Poisson equation gives (r^2 Pbar_a')'=-r^2 Q_a/(4 pi). This verifies both the factor 4 pi and the exponents in the pressure form. Centered energy comparisons transfer the ratio and O(R^(beta-1)) remainder to each fixed center, with center-dependent constants.

For full bounded Hb profiles in 2/5<c<1/2, the energy theorem supplies beta=5-2/c and the stronger error. Then m=2/c-3, the radial Q weight is r^(2/c-1), and k_beta=(5-2/c)(2/c-3)(2/c-4)>0. Since q+ <= |DU|_F^2, a finite derivative integral with weight (1+r)^(2/c-3) is impossible for a nonzero profile. A global exterior bound |DU| <= C r^(-1/c)(log r)^(-1/2-epsilon) would make that integral finite, because its radial majorant is C/[r(log r)^(1+2epsilon)]. Thus every such bound fails at arbitrarily large radii. The natural bound O(r^(-1/c)) alone supplies only a nonintegrable upper majorant and decides no actual convergence question.

The exact swirl control and the coarser all-radius positive-source moment estimate remain at their previously confirmed scopes. The controls solve no full Euler profile equation for any c or omega. Optimal coefficients for actual profiles, automatic critical integrability and the two endpoints remain open.

## 4. Holder control and the additional full-profile premise

For a continuous vector field V, assume E(R)=L R^alpha+O(R^(alpha-1)), 0<alpha<1, and a local Holder seminorm of exponent nu in (0,1] bounded by K(1+|y|)^kappa, with 0<=kappa<nu(1-alpha)/3. A unit-width shell has energy O(R^(alpha-1)). The value delta=|V(y)| persists at magnitude at least delta/2 on a ball of radius comparable to (delta/R^kappa)^(1/nu), once the shell bound has ensured this radius is at most one. Therefore

    delta^(2+3/nu) <= C R^(alpha-1+3kappa/nu).

This gives the stated sigma=[nu(1-alpha)-3kappa]/(2nu+3)>0. The pointwise decay confines every small superlevel set to a ball of radius O(lambda^(-1/sigma)); Chebyshev and the energy growth give weak L^(2+alpha/sigma). Boundedness and layer cake give all larger finite strong norms. The previously checked smooth controls show failure of strong endpoint, smaller weak norms and every finite second Lorentz index at the endpoint, while retaining the precise energy law and a Poisson pressure. They are not full profiles.

For full C2/C1 bounded Hb profiles with 2/5<c<1/2, the separate hypothesis DU=o(sqrt(r)) invokes A498 to obtain DU->0. The preceding bounded-gradient case gives uniform decay of U. A476-A477 and A492 then give |DU|<=C(1+r)^(-1/c), and radial integration gives |U|<=C(1+r)^(-(1-c)/c). The weak endpoint is 3c/(1-c). A finite second Lorentz index at this endpoint contradicts the nonzero leading coefficient in the established energy theorem, so it forces U=0. The report's theorem paragraph and comparison table retain boundedness, Hb and the separate derivative premise; they do not infer that premise from decay. Its condensed section 5 discussion must be read in that stated profile class.

## 5. Exact wording corrections still required

The new proof outline calls the localized compact test r^(2-beta)chi(y/R) itself convex and assigns it the uncut Hessian. This is false literally: a nonzero compactly supported convex function on R3 does not exist. The correct statement is that the uncut weight is convex and the cutoff contributes the separately displayed annular error. The same correction is required in the LIT374 row of Appendix A.

The two-sided additive estimate for the signed compact pairing in Theorem 8(l) and that row must explicitly retain E(R)=L R^beta+O(R^(beta-1)). The preceding paragraph discusses both the ratio premise and the stronger remainder. Adding the qualification prevents the additive bound from being read under the ratio premise alone. This clarification does not alter the established theorem for full profiles, which already has the stronger remainder.

The stronger remainder is substantive. A smooth swirl U=f(r)Jy can have, for all sufficiently large r,

    E'(r) = L r^(beta-1)[beta(1+(log r)^(-1/2))-(1/2)(log r)^(-3/2)].

The bracket is positive there. Set f(r)^2=3E'(r)/(8 pi r^4) on this tail and extend f smoothly through a cutoff in a finite annulus. Then E(R)=L R^beta(1+(log R)^(-1/2))+O(1), so the ratio hypothesis holds. Since U is tangential, its signed localized pairing is

    beta(2-beta)L log R + 2 beta(2-beta)L sqrt(log R) + O(1).

Indeed, the uncut Hessian contributes (2-beta) integral r^(-beta)E'(r)dr and the cutoff contributes only O(R^(-beta)E(2R))=O(1). Thus the additive upper bound with coefficient beta(2-beta)L fails under the ratio premise alone. This control is used only for the kinematic implication; no Euler equation is claimed.

Both points were sent to the coordinator through this agent's notes. Neither is a failure of the independently proved critical-weight result. The first is a false assertion about the localized test; the second is an ambiguous omission of a hypothesis in an assembled statement.

## 6. Present audit conclusion

The new mean-work, critical-source and Holder transfers are mathematically correct with the precise qualifications in Sections 2-4. The constant-profile sentence previously blocking b2d9c61c is fixed. Cumulative approval of the new pin remains pending the two corrections in Section 5 and verification of the resulting exact bytes. No blanket approval of historical Appendices B and C is given. The unrestricted rotating-profile conjecture is still open.

The existing configured model comparisons in A, C and the coordinator are used as mathematical correspondence; actual provider execution is independently unattested. No new model client, mathematical computation, build or server was used. Retained source and file checks are described in the team records and use only relative paths.

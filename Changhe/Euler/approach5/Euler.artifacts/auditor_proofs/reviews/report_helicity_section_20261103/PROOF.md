# Audit of the report's helicity-sign Liouville section

Status: the original 981-line Section2D snapshot and the repaired 988-line snapshot have been independently read in full. The repaired main theorem chain is CONFIRMED as A479 at 2026-11-03T05:02:03.420287+00:00, at its stated conditional scopes. The required basin and positive-volume repairs are present. A regular-point wording qualification for Lemma11(a) is stated in Section9 below. This is not a new unrestricted nonexistence theorem.

## 1. Statement and audited object

Let 2/5<=c<1/2, omega in R, r>=2 an integer, U in C^r(R3;R3), P in C1(R3), U(y)->0 uniformly, and

    div U=0,
    (1-c)U+(B.grad)U+omega JU+grad P=0,
    B=(cI-omega J)y+U, J(x,y,z)=(-y,x,0).

Write W=curl U, a=1-2c, kappa=1+c, h=U.W, H=P+|U|^2/2+((cI-omega J)y).U, O={W!=0}. Let Phi be the complete B flow, Psi_t=Phi_-t, and Gamma the complete W flow. A basin of a probability means convergence of continuous-time empirical integrals for every bounded continuous test. A full-flow-ergodic probability need not be ergodic for Psi_1.

The report's Theorem L assumes Gamma_E<ra on every vortical connected component E, in the exact sense of A430-A432, and one sign of h on each essential basin domain of the supplied vortical family. It concludes U=0. Its smooth version removes the growth hypothesis, but retains the helicity sign condition. Proposition L0 assumes instead an explicitly supplied countable family satisfying compact support, full-flow invariance and ergodicity, full mass on {B!=0,W!=0}, spectrum (a,0,-kappa), entropy a for Psi_1, and coverage of O modulo volume zero. These are the correct scopes. Neither decay alone nor C2 regularity alone is asserted to supply that family.

The pinned object is in the team records, taken from the coordinator's report at the time and hashes in the team records. The audit applies to that snapshot and to the explicit repairs below, not automatically to later revisions. No Lean formalization or build is used.

## 2. Borelness of basins for either time direction

Lemma. Let X be a complete C1 vector field on R3 with continuous flow theta, and let nu be a compactly supported Borel probability. Then

    Bas_theta(nu)={x: (1/T) integral_0^T f(theta_t x)dt -> integral f dnu
                       for every f in C_b(R3)}

is Borel. No boundedness of the forward theta orbit is needed.

Proof. Choose continuous cutoffs chi_n, with 0<=chi_n<=1, chi_n=1 on the closed ball B_n, and chi_n=0 outside B_(2n). Products chi_n p, where p ranges over polynomials with rational coefficients, form a countable uniformly dense subset of C_0(R3). Indeed, for f in C_0 choose n large enough that |f|<epsilon outside B_n, approximate f uniformly on B_(2n) by such a p, and compare chi_n p with f on B_n, its annulus, and the complement of B_(2n). Include the cutoffs themselves in the family, denoted (f_j).

Let E be the set where the empirical integrals of every f_j converge to their nu integrals. For bounded f_j, replacing T by N=floor(T) changes an average by at most 2||f_j||_infinity/N. For fixed N, the average as a function of x is continuous, by joint continuity of the flow on compact time intervals. Thus E is a countable intersection of Borel convergence sets and is Borel.

Uniform approximation shows that every x in E has the required convergence for each f in C_0. Choose a cutoff chi with compact support and chi=1 on supp nu, from the countable family. Then its empirical average tends to1. For any f in C_b, the function f chi is in C_0 and

    |average(f)-average(f chi)|
       <=||f||_infinity [1-average(chi)] ->0.

Also integral f chi dnu=integral f dnu. Hence E=Bas_theta(nu), proving the lemma. Apply it separately to theta=Psi and theta=Phi. []

Draft correction. Lemma9(d)'s bounded-orbit polynomial argument is valid for forward Psi. Its last sentence, asserting the same proof for Bas^-(nu), is not justified: forward Phi orbits outside the compact invariant support can escape every fixed ball. The lemma above repairs the global claim. On supp nu itself both flows stay bounded, so the original countable-family argument used for almost-everywhere genericity remains valid in both directions.

## 3. Whole-flow genericity and the time-one issue

Let nu be compactly supported, invariant and ergodic for theta_t for all real t. For bounded continuous f define g(x)=integral_0^1 f(theta_t x)dt. The integer-length continuous-time averages of f equal the discrete averages of g under theta_1. Birkhoff gives an almost-everywhere limit. A fixed time shift changes a bounded average by at most 2|s| ||f||/T; therefore the limsup is invariant under every theta_s, as an exactly defined Borel function. Whole-flow ergodicity makes it constant almost everywhere. Its integral is integral f dnu. Applying this to the countable family of Section2 gives nu(Bas_theta(nu))=1. The same reasoning applies to the reversed flow. No time-one ergodicity is inserted.

The report uses Ledrappier-Young for the possibly nonergodic time-one map. The actual printed paper has been checked: Theorem A in Section1.5 and Definitions1.4.1-1.4.2 are on printed page513; Lemma3.1.1 is on page519; Lemma6.1.1 is on page533; Corollary6.1.4 is on page534; and Corollary6.2 on page535 explicitly extends the density conclusion to the nonergodic case. The theorem assumes a C2 diffeomorphism of a compact Riemannian manifold preserving a Borel probability, and its entropy-formula implication gives absolutely continuous unstable conditionals. The corollaries give strict positivity of the conditional density. The product ratio has the orientation stated in the report:

    rho(y)/rho(x)=product_(i>=1) J^u(f^-i x)/J^u(f^-i y).

Five rendered pages were visually inspected and retained alongside the complete source PDF and its hash. The density conclusion used downstream is valid without time-one ergodicity. The report's stronger rho=C ell identification is not needed for the Liouville chain.

## 4. Canonical pressure normalization

The report's Lemma7 replaces the earlier pressure construction by compatible truncated singular-integral decompositions. This is valid under the cited pressure fact F1. Absolute convergence of the far field follows from the independently proved shell bound

    integral_(|z|>=rho) |U(z)|^2 |z|^-3 dz <= C_S rho^(beta-3),
    beta=5-2/c<1.

On B_(2R), changing the cutoff from4R to4R' changes the local singular integral by the ordinary kernel integral over the intervening annulus, since its support is separated from the ball. This is exactly the negative of the change in the far integral. Thus p_R-c_R is independent of R. No improper unnormalized pressure integral is being assumed convergent.

The resulting P0=P-p_infinity has the claimed L2 ball bound. The displayed constants in the draft's estimates for P0 and H0 were independently recomputed; in particular the far-pressure exponent is 2beta-3 and is bounded by beta for R>=1. The normalized L2 mean of H0 tends to0 because beta<1. At c=2/5 the cited critical energy theorem supplies finite energy and beta=0.

Uniqueness needs no pressure theorem beyond that decay. If H0 and H0+k both have normalized L2 means tending to0, the triangle inequality in normalized L2(B_R) gives

    |k| <= (mean |H0+k|^2)^(1/2)+(mean |H0|^2)^(1/2) ->0.

Thus k=0. Since both constructions differ from the same H by constants, this identifies the report's representative with A031/A278's normalized one.

## 5. Compact model for the backward carrier

Put M=sup|U| and choose R1>=2M/c+1. The radial estimate B(y).y>=c|y|^2/2 outside B_(2M/c) makes the backward flow inward. Every compact whole-flow invariant set lies in B_(M/c), by the variation-of-constants estimate applied for arbitrarily long backward time. Let K be the maximal backward attractor in B_R1.

Choose a smooth nonnegative cutoff rho, equal to1 on B_(R1+1), zero outside B_(R1+2). The field -rho B extends by zero to S3. Its time-one map f is C^r. A smooth metric equal to the Euclidean metric on B_(R1+3) is obtained by a cutoff combination with a smooth background metric. The field and derivative cocycle coincide with the original backward flow near K for all times along K.

Under the reverse modified flow rho B, the exterior of B_R1 is forward invariant. If a point lies on an unstable leaf of a regular x in K, its backward iterates approach the backward orbit of x in K. It therefore cannot enter that exterior in reverse time. Its entire reverse orbit stays in B_R1, where the fields coincide, and so the point belongs to K. Conversely, an original exponentially backward-asymptotic orbit has the same property by the outward radial barrier and lies in K. Thus the unstable leaves used in the proof coincide and lie in K. A shortcut through the modified part of the metric does not invalidate the separation: every curve from K to the exterior must cross the Euclidean annulus inside B_R1.

This verifies the compactness and C2 hypotheses used by Ledrappier-Young, with the correct backward-flow orientation. The geometric unstable-manifold assertion is read at regular points; exponential-asymptotic sets can be used at other points if needed.

## 6. Comparing two supplied vortical families

Lemma. Suppose two countable families of probabilities for the same flow have pairwise disjoint basins for distinct probabilities, every member's basin is contained in O and has positive Lebesgue measure, and each family's basins cover O modulo a null set. Then the families contain exactly the same probabilities, after removing duplicates.

Proof. Fix nu in the first family. Its positive-volume basin is contained in O. The second family's union misses only a null subset of O, so there is a point in Bas(nu) intersect Bas(mu) for some member mu of that family. Basin convergence for all bounded continuous tests gives integral f dnu=integral f dmu for all such f, hence nu=mu. Interchanging families proves the assertion. []

The compact vortical families in (CI) have positive-volume basins by the product-box argument, using strict positivity of the unstable density. Thus the A308 and A417 families agree whenever both apply. Their essential domains, defined from their basins, also agree. This validates the report's optional second route for the C-infinity result. The first route already proves it without this comparison. No uniqueness of arbitrary invariant probabilities is asserted.

## 7. Scope and boundary checks

1. CorollaryL.3's set R intersect {h!=0} intersect D_nu is Borel. It has positive volume if h is nonzero somewhere in D_nu, since the latter strict-sign union is open and R has full volume. Without that nonempty premise it can be empty. The draft's unqualified phrase calling it positive-volume must be qualified. This does not assert a known Euler counterexample to that phrase; it identifies the missing implication in the supplied argument.
2. The A431 family is vortical in the exact sense nu({B!=0,W!=0})=1, as inherited from the A417 package and proved in the compact spectrum/coverage argument. Its support may still meet both zero sets. The report's (CI) interpretation is correct.
3. Using one ball admissible for both definitions, M_n(E)<=M_n proves (C) implies(G). Radius independence is already in A398/A430. If R_Q=0 is allowed when U=0, the statement that B.y is strictly positive on the boundary needs R_Q>0; choose a positive radius, as the substantive proof already does.
4. The zero extension in Lemma15 uses only local C1 regularity, vanishing boundary values, and the zero derivative almost everywhere on the zero set of a Lipschitz function. It covers a boundary of positive volume. Harmonicity is distributional before Weyl regularity, so no unproved boundary integration is used.
5. The canonical Bernoulli decay is transported by the expanding carrier with its exact volume Jacobian. The bounded unstable support plaque, both time-direction genericity and the vortex conjugacy give the product-box identity before any dominated convergence is used. One compact box suffices; no global singular measure integration by parts is used.
6. The final positive-stress test uses the shell energy estimate beta<1; it does not assume finite global energy or drop a pressure boundary term. The coefficient bounds and the cutoff error C E(2R)/R were checked.
7. CorollaryL.5 matches A328's extended-real signed equality for every measurable vortex-invariant set and Borel Bernoulli band. Its real scope is uniformly sublinear U, broader than decay. Because the report's symbol (E) already includes decay, referring literally to (E) narrows that corollary unnecessarily; referring to just its differential equations preserves the full intended statement. This is a presentation issue, not a false stronger theorem.
8. The A312 extension retains its explicit quantitative strain inequality. Its constants do not become uniform in arbitrary omega by any claim here. All results permit every fixed finite omega; no estimate silently sets omega=0.

## 8. Verdict policy and remaining work

The main Liouville implications retain their previously CONFIRMED scopes A309, A317, A326-A328, A422 and A430-A432. This snapshot needs the two corrections in Sections2 and7 before an unqualified text-level approval. The new source numbering, compact-model construction, normalization identification and family comparison have been independently checked here. A final text verdict will identify the repaired snapshot by hash.

These checks do not supply a helicity sign, finite-r coverage from decay, exclusion of singular supports, or nonexistence in the arbitrary-sign C2 class. Existing file collaboration with the coordinator's configured model is used; model configuration is not independent provider attestation.

## 9. Full recheck of the repaired report snapshot

At 2026-11-03T05:02:03.420287+00:00, all988 lines of in the team records were read in full in five consecutive chunks. Its SHA256 is723492fd181a1b5dc7b1ed3aa5200a8c5001166d3717b32b6f373d986abcec10. The snapshot and parent report hashes are in the team records.

The two substantive repairs are correct. Lemma9(d) now constructs a countable dense C0 family, obtains tightness from one compact cutoff and extends convergence to all bounded continuous tests. It therefore proves Borelness for both flow directions without an orbit bound. Lemma9(f) explicitly uses the same set E, so whole-flow ergodicity suffices. CorollaryL.3 now requires h nonzero somewhere in D_nu before asserting positive volume, and leaves the almost-every-line claim open. The positive-radius and CorollaryL.5 scope corrections are also present.

The full chain was rechecked, including complete vortex flow from Cauchy conjugacy, recurrence without finite ambient volume, compactification for Ledrappier-Young, two-sided Oseledets signs, support plaques, positive unstable densities, the product-box identity, pressure normalization, zero extension on a possibly positive-volume boundary and the final sublinear-energy stress cutoff. No new gap was found in the main theorem chain. The actual printed Ledrappier-Young numbering and nonergodic corollary were already visually checked as recorded in Section3; the report's provenance note that the coordinator had not checked them is historical, not a remaining auditor uncertainty.

One wording qualification remains for a standalone reading of Lemma11(a): its phrase "for x in K the unstable manifold" should say "for every Oseledets regular x in K for which the unstable manifold is defined", or call the set an exponentially backward-asymptotic set for arbitrary x. The radial containment proof applies to all such asymptotic points; differentiable unstable manifolds are used only at regular points in11(b) and12. The text-level confirmation of A479 uses this standard regular-point interpretation. It does not assert a smooth unstable manifold at every nonregular point of K. This precision is immaterial to the Liouville deduction but should be incorporated into the published wording.

The supplied family comparison in Section6 makes the alternate smooth proof consistent with its named family. The smooth theorem still requires one helicity sign on each essential basin. The finite-r theorem still requires componentwise Gamma_E<r(1-2c) and that same sign condition. The proposition with independently supplied coverage remains conditional on the entire package(CI). No statement supplies arbitrary-sign nonexistence or decay-only C2 coverage.

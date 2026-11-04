# Audit of the Liu preprint

Part I is the independent audit by the literature and counterexample agent; Part II is the separate audit by the independent mathematical auditor.

## Part I. Audit by the literature and counterexample agent

## Independent audit of the Liu preprint

Final source check recorded 2026-11-04T14:46:48.998537+00:00: all sixteen manuscript pages, through the complete 846-line layout extraction, and the complete prior 193-line audit were reread during the run. The actual Zenodo record returned HTTP 200 at 14:40:35Z and still lists the retained PDF's exact size and MD5. No new PDF download is claimed. All five audit answers remain unchanged. The final source and scope comparison distinguishes this reading from metadata verification and retains the conditional rotating period-map premise.

Hour-30 deliverable checkpoint: 2026-11-04T00:06:10.416448+00:00. Assigned audit complete; the unrestricted conjecture remains OPEN. Current source limitations and exact conditional scopes are retained. This timestamp records an offline status comparison, not a new retrieval or a rereading of every cited source.

Status: the ordinary stationary theorem is **PROVED** within its exact scope, independently CONFIRMED by the auditor entry A010. The contracting-form criterion is CONFIRMED in A011 and remains **CONDITIONAL** for rotation. The unrestricted continuously rotating conjecture is **UNRESOLVED**. The actual manuscript has been obtained and read in full. Report consolidated: 2026-11-03T00:39:49.352134+00:00.

Status checked 2026-11-03T16:55:38.149349+00:00. The source and five audit answers are unchanged. The confirmed pressure and continuation-source results do not remove the extra rotating period-map condition. This is an offline status check, not another Zenodo retrieval.

Repeated foundation audit checked 2026-11-03T18:39:43.067278+00:00: A2045-A2047 reconfirm the ordinary C1 theorem. The complete new proof and the original reconstruction were compared. Section9 of the standalone reconstruction now proves the null-basin step directly by a Lipschitz graph, with no center-stable theorem needed. No hypothesis is weakened and no rotating conclusion is added; A2048 leaves those extensions open.

Repeated audit checked 2026-11-04T08:07:33.899647+00:00: the complete ten-section independent reconstruction at SHA256 aea5df1ec4b9beb03ffa87fe8d46ca34ddd969b9348c9ef5b2313147fd9160c1 and the complete C07:18:52 analytical comparison have been read. A3059-A3060 reconfirm the ordinary C1 theorem and its exact scope; A3061 leaves the arbitrary-rotation extension OPEN. The direct null-graph proof, countable open-neighborhood cover, C1 pullback and local rank-capture argument remain valid. This is a fresh reading of the retained audit evidence, not a new retrieval or a fresh reading of all sixteen manuscript pages. The comparison's diagnostics and separate report byte-identity claim are not certified. The C1 pressure-axisymmetry theorem A3047 has a separate proof and does not remove the extra condition in the manuscript's relative-periodic criterion.

### Manuscript and provenance

The source is Dylan Z. Liu, *A Liouville theorem below the half-scaling exponent for three-dimensional Euler profiles*, Zenodo record 23461703, DOI 10.5281/zenodo.23461703. The downloaded manuscript has 16 pages. It is retained as `in the team records`, with a layout-preserving extraction in `in the team records`. Its SHA256 is `026536095d523419aea765f1c8d054879b71a4cdf6b1c070f8f3c6bb233319c8`. Its MD5, `ec7a624e0971e0176e3d409239289ff4`, agrees with the record's file checksum.

The record was created on 19 October 2026 and the PDF creation metadata gives the same date. The record's separate `publication_date` field says 21 November 2023. This discrepancy is retained in the retrieval evidence; no chronology or priority claim rests on that field. The PDF itself has no author line, so the author identification comes from the record. These metadata observations do not affect the mathematical audit.

The actual record metadata and manuscript, rather than the abstract alone, were used. All sections, including the C^1 extension, discrete criterion, vortex-line results, critical case and examples, have been read.

### 1. What is actually claimed

Theorem 1.1, manuscript page 1, assumes dimension d=2 or d=3, 0<c<1/2, U in C^1(R^d;R^d), P in C^1(R^d),

\[
(1-c)U+(cy+U)\cdot\nabla U+\nabla P=0,
\qquad \nabla\cdot U=0,
\qquad |U(y)|=o(|y|)
\]

uniformly as |y| tends to infinity. It concludes that U is spatially constant. A normalization U(0)=0 gives zero; decay U(y) to zero also gives zero. The theorem does not assume finite energy, vorticity integrability, an outgoing condition near stagnation points, a finite stagnation set, analyticity or pressure decay.

The words “stationary profile” in this theorem refer to the ordinary similarity equation above. They do not include a stationary profile in rotating coordinates. The latter has two extra terms, omega JU and minus omega(Jy) dot grad U.

Theorem 7.3, pages 8 to 9, is a separate conditional statement about time-dependent ordinary similarity profiles with relative periodicity. It requires almost every backward orbit of the **actual untwisted period map** to have a periodic point limit. This condition is not derived from sublinearity or relative periodicity.

### 2. Audit of the ordinary stationary proof

A standalone reconstruction is in the team records. The logical chain is as follows.

Set a=1-2c>0, V=cy+U, A=DV, and W=A^T-A. Thus W is the matrix of the vorticity two-form, with the manuscript's convention. Let

\[
H=\tfrac12|V|^2+P-\tfrac12c(1-c)|y|^2.
\]

The exact identity is

\[
\nabla H=-(aI-W)V,
\qquad V\cdot\nabla H=-a|V|^2,
\qquad a|V|\le |\nabla H|\le(a+\|W\|)|V|.
\]

Sublinearity gives a complete C^1 flow and confines each backward orbit to a compact ball. H therefore has a finite increasing limit along reversed trajectories. Each backward limit set K is nonempty, compact, connected and invariant. H is constant on K, and strict monotonicity implies K is contained in {V=0}. No asymptotic bound on P is involved.

The vorticity two-form obeys

\[
(V\cdot\nabla)W+A^TW+WA+aW=0.
\]

At an equilibrium p whose eigenvalues of A(p) all have nonnegative real part, the equilibrium equation implies

\[
W(p)=e^{-at}e^{-tA(p)^T}W(p)e^{-tA(p)}.
\]

The matrix exponentials grow at most polynomially, including possible Jordan blocks. Consequently W(p)=0. Because W=A^T-A, A(p) is then symmetric positive semidefinite. Near p, its symmetric part is bounded below by -aI/4. The Frobenius norm estimate along an orbit is

\[
\tfrac12\frac{d}{ds}|W|_F^2
\le -(a+2\lambda_{\min}(\operatorname{sym}A))|W|_F^2
\le -\tfrac a2|W|_F^2.
\]

A bounded negative-time tail converging to p forces W to vanish along that orbit. Equilibria with a negative-real-part eigenvalue are handled separately by a countable cover of local center-stable manifolds for the reversed time-one map. Their backward-convergence basins form a Lebesgue null set.

The new stationary step is Lemma 6.2, pages 5 to 6. At every point of a nonpoint backward limit set it proves rank DV at most d-2. If rank were d, the point would be an isolated zero. If rank were d-1, the implicit function theorem puts all local zeros on a C^1 coordinate axis. Connectedness forces K to contain a one-sided arc of this axis, not merely a sequence of zeros. At an interior point of that arc, the transverse coordinates xi satisfy

\[
|\xi|\le |V|\le C|\xi|,
\quad |H-h|\le C'|\xi|^2,
\quad |\nabla H|\ge a|\xi|.
\]

These bounds give a local square-root gradient inequality. Integrating the resulting length estimate during a sufficiently late visit prevents exit from the neighborhood and forces convergence to one point. This contradicts the nonpoint limit-set assumption.

In dimension three, rank at most one and trace DV=3c>0 give spectrum {3c,0,0}. The preceding equilibrium argument gives W=0 and sym DV nonnegative at every point of K. Compactness then supplies the same contraction inequality on an entire sufficiently late backward tail. It follows that W vanishes on every orbit with a nonpoint limit set. In dimension two the rank bound would force DV=0 on K, contradicting positive trace.

Combining the point and nonpoint cases gives W=0 outside a null set, hence everywhere by continuity. Curl-free and divergence-free U has harmonic components in the distributional sense. Sublinear harmonic functions are constant by the interior gradient estimate on balls of increasing radius.

#### Rank argument: possible gaps checked

The local zero set need not be a manifold. Only the common zero set of d-1 independent components is a C^1 curve; the remaining component may have an arbitrary closed zero subset. The connectedness argument deals with this distinction correctly.

The cylinder used to separate K has a boundary disjoint from K. Its side contains no zeros, and its two cap intersections with the coordinate axis are chosen outside K. The chart can be shrunk so that K also has a point outside its closure. This creates the required contradiction to connectedness and justifies the one-sided arc conclusion.

The local gradient estimate needs neither an analytic H nor a Morse-Bott theorem. C^1 coordinate bounds, V=0 on the entire small axis and the exact gradient identity suffice. At C^1 regularity, H need not have a classical Hessian; the proof does not use one.

A finite-length bound on a neighborhood is not used without a capture argument. Lemma 6.1 explicitly chooses a late visit with both small distance and small remaining energy, and rules out a first exit. This closes a common gap in this type of proof.

#### Center-stable argument: possible gaps checked

For F=Phi_{-1}, an eigenvalue of DV(p) with negative real part gives an eigenvalue of DF(p) with modulus greater than one. A local center-stable graph for F has codimension at least one and contains all points whose nonnegative iterates remain in the designated neighborhood. Other eigenvalues may lie on the unit circle; isolated equilibria and full hyperbolicity are unnecessary.

The proof does not take an uncountable union of null manifolds. It first selects a countable subcover of the open union of the neighborhoods. An orbit converging to any equilibrium eventually stays in one neighborhood from that subcover. It therefore belongs to an integer forward image of one of countably many null graphs. C^1 diffeomorphisms preserve null sets locally, which is sufficient after another countable cover.

The cited manifold theorem is a substantive standard dependency. The exact local trapping version has now been checked in the cited paper of Panageas and Piliouras, Theorem 8 on page 2:7, retained as `in the team records`. Its statement includes C^1 local diffeomorphisms, center directions and the required trapping property. The equivalent direct null-graph argument in approach1 offers an independent route to this dependency.

#### C^1 regularity

Section 7.1 supplies the missing transport argument at C^1 regularity rather than formally differentiating continuous vorticity in space. Integrate the pulled-back velocity one-form identity along the C^1 flow, then take its distributional exterior derivative. Pullback commutes with exterior differentiation here by local C^1 approximation of the map; the resulting two-forms are continuous, so equality holds pointwise. The deformation gradient solves a linear ODE with continuous coefficients, and this makes vorticity differentiable along trajectories. The equilibrium identity and the norm estimate are then legitimate.

This justifies the C^1 upgrade of the core theorem. The Morse-Bott alternative retains its separately stated higher regularity and should not be silently included at bare C^1 regularity.

### 3. Hidden assumptions

No unmentioned pressure normalization has been found. The proof evaluates pressure and H only on bounded orbit closures. A nonzero constant velocity b is allowed, with P=-(1-c)b dot y plus a constant.

Flow completeness is proved from at-most-linear growth; it is not inferred from local smoothness alone. Backward boundedness is proved from the outward radial component at large radius. Neither assertion needs a global derivative bound.

The proof does not infer absence of periodic orbits from positive divergence. In the stationary setting it is the strict Bernoulli identity that puts limit sets in the equilibrium set. Positive divergence enters later through trace DV=dc.

It also does not assume that every backward trajectory converges to a single point. Nonpoint limit sets are explicitly treated. Almost-everywhere conclusions are promoted to everywhere only after continuity of vorticity is invoked.

### 4. Continuously rotating profiles

For a rotating profile, define R_s=exp(omega J s) and

\[
\widetilde U(y,s)=R_sU(R_s^{-1}y),
\qquad \widetilde P(y,s)=P(R_s^{-1}y).
\]

Then the time-dependent ordinary similarity equation holds. For every L>0 this solution is relatively periodic with rotation R_L, and its untwisted period map is exactly Phi_L^B, where B=(cI-omega J)y+U. The calculation and its conditional consequence are recorded in the team records.

Thus Theorem 7.3 covers arbitrary finite omega **conditionally**. For example, almost-everywhere convergence of backward B-trajectories to equilibria is a sufficient extra hypothesis. More generally, the exact periodic-point-limit condition on Phi_L^B suffices for one fixed L.

Approach to a periodic orbit as a set is not automatically the paper's hypothesis. For an autonomous flow and a fixed L, the sampling period must be compatible with the orbit period, and a phase limit is needed. This distinction must be retained in any theorem statement.

The stationary rank argument does not transfer directly. Write X=cy+U and a=1-2c. The rotating identity gives

\[
\nabla H_{\rm rot}=-aX-\Omega\times B,
\qquad B\cdot\nabla H_{\rm rot}=-aX\cdot B.
\]

The scalar X dot B can have either sign. Moreover, at B(p)=0 the gradient is -a omega Jp, which need not vanish. The first step placing backward limit sets inside {B=0} is therefore missing, and the critical-set identity needed in Lemma 6.2 is missing as well.

Even an exact constant profile exhibits the sign issue. At y=(1,0,0), take b=(-c,omega/2,0) and U identically b, with its exact linear pressure. Then X dot B=-omega^2/4. This example is sublinear but not decaying. It refutes an automatic sign claim on the sublinear class, not the target conjecture.

### 5. What can be extended, and what remains open

The contracting-two-form theorem, the untwisted period map, backward confinement, absence of regular closed vortex lines, and the compact vortex-line invariant-measure action restriction have formulations uniform in finite omega. They can be tested independently against the rotating equation.

The central missing implication is a dynamical one: smoothness, decay and the full rotating Euler equation have not been shown to force the period-map hypothesis, or another condition making the contracting two-form vanish on nonconvergent backward dynamics. Neither the manuscript's abstract nor Theorem 1.1 supplies that implication.

Theorem 7.5 gives a small-period exclusion only in a family with fixed local C^2 bounds, fixed pressure-gradient bounds, a common sublinear growth modulus and a fixed positive local vorticity lower bound. Applying it to fast continuous rotation requires keeping all these controls fixed before omega varies. It is not a uniform arbitrary-omega theorem.

The full rotating conjecture remains **UNRESOLVED** by this preprint audit. The ordinary stationary theorem is independently CONFIRMED under its written assumptions in `the auditor's ledger (in the team records)`, A010. The separate conditional rotating criterion is CONFIRMED in A011; an unconditional application is REFUTED as a scope inference in A012.

### 6. The separate critical result in Section 9

The actual manuscript's Lemmas 9.1-9.2, Remark 9.3, Theorem 9.4 and Corollary 9.5 have now also been independently reconstructed and CONFIRMED in auditor A196. This does not change the answers to the five audit questions above.

Lemma 9.2 assumes a C1 carrier V on R3, constant divergence kappa>0, a complete flow Phi, and uniform backward confinement of each compact initial set: the union of Phi_-t(D), t>=0, is bounded for every compact D. If V cross curl V=0, it concludes curl V=0. Continuity and alignment first imply curl V=0 at V=0. Dividing by a nonvanishing carrier coordinate then gives a scalar f with curl V=fV off the zero set and a vanishing local weak-L1 tail: lambda times the volume of {|f|>lambda} in every bounded ball tends to zero. The flow law f(Phi_-t x)=exp(kappa t)f(x) contradicts this tail unless f=0. A merely bounded weak-L1 tail is insufficient; the manuscript's f=1/x1 for V=(kappa x1,0,0) is a scalar sharpness example, whose carrier curl is zero. It is not an aligned-curl counterexample.

At c=1/2 and omega=0, assume U,P in C1, div U=0, the ordinary profile equation, and uniform sublinearity. With V=y/2+U and H=|V|^2/2+P-|y|^2/8, Theorem 9.4 concludes that U is constant if H is constant. Corollary 9.5 gives sufficient alternatives H tending to one finite constant at infinity, or H-h_infinity in Lp(R3) for one 0<p<infinity. The equality V dot grad H=0 makes finite-measure strict level sets invariant under an expanding-volume flow, forcing H to be constant. Decay of U then forces U=0. These conditions are on H and do not follow from velocity decay or sublinearity in this argument.

For rotation, curl B=Omega-2 omega e3. Alignment with Omega is not the lemma's alignment with curl B. The zero-set step is therefore unavailable without a separate proof. The critical theorem is conditional and nonrotating; it does not settle the unrestricted c=1/2 problem or the mandatory rotating interval. The independent standalone reconstruction is [the auditor proof](auditor_proofs/proofs/critical_aligned_curl/PROOF.md).

### 7. Relation to later campaign results

The campaign's new dynamical and Bernoulli results are separate from the Liu manuscript. They do not alter this audit's conclusion about its scope. LIT51/A256 proves the rotating constant-reduced-Bernoulli theorem at C2 with uniform sublinearity. LIT59-LIT60/A277-A278/A283 proves rigidity on given vortical SRB essential basins with one sign of helicity, under decay and 2/5<=c<1/2. At C2, the required basin coverage remains a separate premise.

LIT65-LIT67/A305-A307 and LIT41/A308 now supply almost-everywhere vortical basin coverage for smooth uniformly sublinear profiles, without the earlier external finite-time measure premise. The measures have backward spectrum (1-2c,0,-1-c) and positive unstable conditional densities, but their supports may meet the carrier or vorticity zero sets. Combining this coverage with the one-sign argument gives A309: a smooth decaying profile with 2/5<=c<1/2 and any finite omega vanishes if helicity has one sign on each essential basin, even when the signs differ between basins.

The unrestricted sign-changing case remains open. These results do not prove the periodic-point-limit hypothesis of Liu Theorem 7.3. They also do not show automatic C2 coverage or turn nonuniform essential basins into nonsingular uniformly hyperbolic attractors. Current statements, dependencies, and their verification evidence are in [LITERATURE_REVIEW.md](LITERATURE_REVIEW.md), Sections 7.12 and 8, and the reading-order index.


### Repeated independent audit recorded 2026-11-04T02:33:26.418380+00:00

The independent auditor's complete eight-section repeated reconstruction and its audit record were read here. A2776 again CONFIRMS the ordinary, nonrotating global C1 Liouville theorem under uniform U=o(|y|), in dimensions2 and3 and0<c_l<1/2. A2777 keeps an unconditional extension to arbitrary continuous rotation OPEN. The earlier ordinary/conditional-rotation distinction is unchanged. This agent's original mandatory audit used the actual full16-page Liu manuscript; this update is a comparison of the repeated independent reconstruction, not a claim to have freshly reread all16 PDF pages again. The actual manuscript SHA256 remains026536095d523419aea765f1c8d054879b71a4cdf6b1c070f8f3c6bb233319c8.


### Record checksum recheck, 2026-11-04T08:25:52.144312+00:00

The actual Zenodo API response received at08:22:38Z still lists in the team records with size436737bytes and MD5 ec7a624e0971e0176e3d409239289ff4. The retained actual PDF has the same recomputed MD5 and SHA256026536095d523419aea765f1c8d054879b71a4cdf6b1c070f8f3c6bb233319c8. See in the team records. This check changes none of the five audit answers, supplies no new proof-reading event and preserves the chronology discrepancy. The ordinary theorem is confirmed at its stated scope; arbitrary continuous rotation is still conditional or open.

### Retained-manuscript reread, 2026-11-04T12:10:01.917700+00:00

All sixteen pages of the retained actual Liu manuscript were reread from its layout extraction during this final shift. The PDF and extraction checksums agree with the retained files. This is a complete fresh reading of the retained text, not a new download. All five audit answers above remain unchanged. The ordinary C1 theorem is confirmed at its stated scope; continuous rotation still needs the actual untwisted period-map hypothesis. The exact reading ranges, checksums and source comparison are recorded in the final agent audit. No extra assumption or theorem is introduced by this status update.

## Part II. Audit by the independent mathematical auditor

## Independent audit of the Liu manuscript

The actual manuscript, not only its abstract, has been read. The 16-page PDF is archived as `in the team records`; its text extraction is `in the team records`. The literature agent obtained it from Zenodo record 23461703 and supplied the record metadata, archived here as `in the team records`.

Integrity check: the PDF MD5 is `ec7a624e0971e0176e3d409239289ff4`, matching the record. Its SHA256 is `026536095d523419aea765f1c8d054879b71a4cdf6b1c070f8f3c6bb233319c8`. The record creation date is 2026-10-19. The PDF metadata likewise dates its creation to 2026-10-19. A conflicting publication-date field is not used to infer priority.

### Main theorem

Verdict: **CONFIRMED**, with the exact nonrotating scope of Theorem 1.1.

For `d=2` or `3`, `U,P in C^1`, `0<c<1/2`, and uniform `U=o(|y|)`, a stationary nonrotating Euler similarity profile is spatially constant. Under `U->0`, it is zero. A complete independent proof is in `auditor_proofs/proofs/nonrotating_audit/PROOF.md`.

The important checks are:

1. The flow is complete from linear growth and every backward trajectory is bounded. Pressure is evaluated only on compact sets, so the proof has no hidden pressure condition.
2. The Bernoulli identity has a strict sign because the equation is nonrotating and `1-2c>0`.
3. Lemma 6.2 does not assume that backward trajectories converge. It proves that a nonpoint limit continuum has `rank DV<=d-2`, using an inverse-function chart, a connectedness argument, and a local path-length estimate. The chart argument is valid for `C^1` data.
4. In three dimensions, rank one and positive trace force spectrum `{3c,0,0}`. The two-form equation then makes the matrix symmetric positive semidefinite. This is the low-dimensional step; it fails as a general conclusion in higher dimensions.
5. The local center-stable assertion has the needed trapping property. The independent proof supplies a direct Lipschitz-graph argument and a countable cover, so neither isolated equilibria nor a countable stagnation set is required.
6. The `C^1` endpoint is justified by integrated one-form transport and distributional exterior differentiation. It does not rely on nonexistent spatial derivatives of continuous vorticity.

Theorem L2 in the approach1 source is a `C^2`, three-dimensional special case of the confirmed statement. Its alternative capture proof has the same sound local structure. Its previous audit labels were not used as premises.

### Contracting forms and rotating scope

Theorem 7.1 is a conditional dynamical theorem. For a `C^1` diffeomorphism `F` and continuous two-form `beta`, it assumes `F^* beta=r beta` with `0<r<1`, **and** that almost every backward orbit converges along some integer period to a periodic point. It concludes `beta=0`.

The proof's two branches are valid. Backward convergence to a periodic point with an eigenvalue of `DF^m` inside the unit circle has a null basin by the local graph argument. At the remaining periodic points, the inverse exterior-square cocycle has limiting spectral radius at most `r^m<1`, so an adapted norm contracts it on the whole sufficiently late convergent tail. Boundedness of the continuous two-form along that tail finishes the proof.

Theorem 7.3 retains this additional backward-convergence hypothesis for the actual untwisted period map. It does not prove the hypothesis from spatial sublinearity or relative periodicity. Its text explicitly says that nonconvergent backward dynamics remain open.

For a continuously rotating stationary profile, let `Q_s=exp(omega s J)` and define

\[
 u_s(y)=Q_sU(Q_s^{-1}y).
\]

Differentiating gives `partial_s u_s=omega Ju_s-omega(Jy dot grad)u_s`, so the rotating stationary equation is exactly the ordinary time-dependent rescaled Euler equation for `u_s`. If `Psi_s,0` is its particle map, the rotating-frame substitution gives

\[
 \Psi_{s,0}=Q_s\circ\Phi_s^B.
\]

Its relative rotation over any chosen time `L>0` is `Q_L`, and the untwisted period map is therefore exactly `Phi_L^B`. Theorem 7.3 applies only if this map has the stipulated almost-everywhere periodic point limits. It supplies a conditional theorem for every finite `omega`, not the target unconditional theorem.

### Remaining manuscript results

Sections 8 and 9 have been read. The frozen-vorticity results have now been independently extended and confirmed for rotating stationary profiles: no nonconstant periodic vortex line, zero entropy on each compact frozen-vorticity invariant set, and zero compact invariant mean action (A014-A016; `auditor_proofs/proofs/vortex_geometry/PROOF.md`). The critical-exponent aligned-curl and conditional Bernoulli results are now independently CONFIRMED as A196; their complete reconstruction is in auditor_proofs/proofs/critical_aligned_curl/PROOF.md. They remain nonrotating and conditional on the Bernoulli hypothesis. None of these is a premise of the confirmed nonrotating theorem. Claims about the frozen vorticity flow must not be substituted for claims about the particle or similarity flow.

The literature agent proposed a further conditional extension from sampled periodic point limits to continuous alpha-limit sets that are points or individual periodic orbits. Its proof is confirmed in A020 and `auditor_proofs/proofs/periodic_limit_audit/PROOF.md`. This removes phase and period-arithmetic restrictions but still assumes a classification of almost every alpha-limit set; that classification remains unproved for the target class.

### Overall verdict

The main stationary nonrotating theorem is supported by its proof. The manuscript does not solve the arbitrary continuously rotating target from velocity decay alone. No abstract-level rotating claim is used to bridge that gap.

### Repeated primary-source check, 2026-11-04T02:22:39.062212+00:00

A2776 again confirms the complete ordinary C1 proof after the actual manuscript was read through the end and the two independent reconstructions were reread. The four delicate steps and exact scope are recorded in auditor_proofs/reviews/nonrotating_liouville_20261103_evening/PROOF.md, Section8. No pressure normalization, integrability or point-limit premise has been added. The unconditional rotating extension remains OPEN A2777. The later sections were read but are not collectively recertified by this new verdict.

### Final primary-text recheck, 2026-11-04T12:23:57.085775+00:00

A3233 confirms the ordinary C1 theorem after the complete retained sixteen-page manuscript and the complete independent argument were reread in this final shift. The ten-section reconstruction and five mandatory answers are in `auditor_proofs/reviews/final_liu_recheck_20261104/PROOF.md`, SHA256 1abad231f575b48bff64d3325369bbd40dd2b13d2171749e2e81131e0478ee91. The check again distinguishes the actual untwisted period-map condition from automatic consequences of decay. It adds no unconditional rotating or critical-exponent result and does not collectively recertify every later manuscript claim. This was a fresh reading, not a fresh download.

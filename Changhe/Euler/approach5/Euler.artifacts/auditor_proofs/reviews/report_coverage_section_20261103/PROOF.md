# Full text audit of the smooth vortical coverage section

Status: CONFIRMED as A490 for the repaired1041-line Section2C snapshot in Section8. Earlier snapshots and their repairs are retained as audit history. The complete configured-model review, full preceding text and final two-hunk repair diff were read and independently checked.

## 1. Exact object, hypotheses and conclusions

The object is in the team records, captured at2026-11-03T05:08:22.319865+00:00, SHA25689929d812a99156d94602bf0dce594bfac77e6d302330869b22697b0bd566375. Its parent hash and line count are in the team records. All1002 lines were read in order, including the proofs, finite-regularity outline, external dependencies and provenance questions. The audit does not automatically apply to later revisions.

For the Euler theorem, fix0<c<1/2 and any finite real omega. Let J(x,y,z)=(-y,x,0), A=cI-omega J, U smooth on R3, P C1, div U=0, and

    (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    |U(y)|/|y| ->0.

Write B=Ay+U, Omega=curl U, a=1-2c, kappa=1+c, Phi for the complete B flow and Psi_t=Phi_-t. Let Q be an admissible trapping ball and K its compact backward core. Theorem C asserts an at most countable collection of compactly supported, whole-flow-invariant and whole-flow-ergodic probabilities nu_i, with full mass on {B!=0,Omega!=0}, spectrum(a,0,-kappa), entropy a for Psi_1 and absolutely continuous one-dimensional unstable conditionals. Their positive-volume Borel basins lie in O={Omega!=0} and cover O modulo a null set. The density and essential-domain conclusions use alpha=(B cross Omega).dy. A whole-flow-ergodic measure is not assumed time-one ergodic.

The abstract theorem replaces these fields by smooth B,W satisfying completeness of B, div B=d>0, [B,W]=-kappa W with kappa>d and the stated radial lower bound. It asserts only conclusions1-4, with a=kappa-d. It does not assume a globally complete W flow; local W flows and the contracting conjugacy suffice.

The finite-Cr result, r>=2, remains conditional on Gamma_E<r(1-2c) for every vortical connected component E, with Gamma_E defined on the singular part of its own compact core. No common strict margin across components is needed. The smooth theorem supplies no helicity sign and no Euler Liouville conclusion by itself. Unconditional C2 coverage and the main arbitrary-sign decay-only conjecture remain OPEN.

## 2. Repairs required for a standalone reading

### 2.1 Lemma19: discrete transport does not state real-time invariance

The hypothesis in the snapshot is only

    Wt(Fp^n x)=exp(kp n) D Fp^n(x) Wt(x), n integer,

where Fp is the time-one map of the flow of -Bp. Its Lyapunov-norm and conorm argument correctly proves Wt=0 on the global strong stable curve through the stated regular point. The last sentence then asserts that the zero set is invariant under the entire flow and adds vanishing on its flow translates. The displayed discrete hypothesis justifies integer iterates, not arbitrary real times.

Repair the lemma by assuming the real-time transport law

    Wt(Theta_t x)=exp(kp t) D Theta_t(x) Wt(x), t real,

where Theta is the -Bp flow, or equivalently the bracket identity [Bp,Wt]=-kp Wt. Alternatively delete the extra assertion about flow translates. The real-time law immediately makes {Wt=0} invariant because D Theta_t is invertible. The Euler and abstract applications in Lemma23 already have this stronger bracket identity, with Bp=pB and kp=p kappa. Their conclusion is unchanged. This is a missing abstract hypothesis, not a claimed counterexample to Euler coverage.

The internal plaque proof was checked: choose eps with2eps<lambda and4eps<kp, compare DFp at the plaque point with DFp at its compact regular orbit in the tempered Lyapunov coordinates, and obtain the lower conorm exp(-lambda-2eps) after a finite initial segment. The C1 vanishing estimate gives the upper exp(-lambda+eps)n. Combining them gives |Wt(x)|<=C exp((-kp+4eps)n), hence zero. Every point of the global stable curve eventually enters the local one. No uniform hyperbolicity of the support is used.

### 2.2 Theorem C_r(A): attainment when the singular set is nonempty

The definition gives Gamma_E=-infinity if Z_E is empty. The statement should therefore say that Gamma_E is attained when Z_E is nonempty. There is no probability supported on an empty set. The max formula Lambda_E=max(a,Gamma_E) and the conditional coverage conclusion remain meaningful in either case. The projective-flow attainment proof is valid on a nonempty compact invariant Z_E.

### 2.3 Lemma25: a small two-sided flow box need not remain in an arbitrary closed Q

Its proof says Psi_t gamma(s) is in Q for small positive and negative t. This is immediate when the chosen central point is in int Q and the arc and box are shrunk. The stated arc lies only in the closed Q. Either require the central point and a small arc in int Q, as every application through K already has, or enlarge Q to another admissible ball before invoking the uniform local vortex-flow time. A compact small carrier-flow box is contained in such an enlarged admissible ball. The basin is flow invariant independently of Q. Thus the product-box argument is repaired without changing the theorem.

## 3. A complete conditional-measure step for Lemma20

Here is a proof of the measurable Lebesgue-decomposition implication that the snapshot cites without details. Work in a subordinate unstable partition, restricted to countably many measurable charts with finite normalized leaf arclength. Write s for the quotient variable, q for its probability, mu_s for the conditional probability and lambda_s for the normalized leaf-arclength probability. These are measurable kernels on a standard Borel fiber relation. Suppose every measurable set N with lambda_s(N_s)=0 for q-almost every s satisfies mu(N)=0.

Set rho_s=mu_s+lambda_s and let m,mu,l be the joint measures obtained by integration over q. Then mu<=m and l<=m. Let f=dmu/dm and g=dl/dm, chosen jointly measurable; f+g=1 almost everywhere. For every measurable base set and every member of a countable generating family of fiber sets, the Radon-Nikodym identities and integration over q give

    mu_s=f(s,.) rho_s,  lambda_s=g(s,.) rho_s

for q-almost every s. This is also the uniqueness of disintegration for finite kernels; countability gives one common full base set.

The joint measurable set N={g=0} has lambda_s(N_s)=0 for almost every s. By the hypothesis, mu(N)=0. Thus f=0 rho_s-almost everywhere on {g=0}, for almost every s. On {g>0} one has

    mu_s=(f/g)lambda_s.

Consequently mu_s is absolutely continuous with respect to lambda_s for almost every s, which is the desired statement. Conversely conditional absolute continuity plainly implies the null-set property by integration. Countably many chart restrictions yield the claim on the full subordinate partition. No selection of separate nonmeasurable singular supports is needed.

The snapshot's preceding proof of the null-set property checks: a compact incoming curve lies on a single immersed unstable leaf; the intrinsically open subordinate segments covering its full-measure good set have a countable subcover. Their leaf-null intersections are ambient H1-null in compact charts, hence arclength-null on the embedded incoming curve. Integrating its absolutely continuous curve conditional proves mu(N)=0. The whole argument uses measurable subordinate Pesin partitions and their measurable arclength kernels as explicit external measure-theoretic inputs.

## 4. Original Ledrappier-Young source and regular points

The actual PartI PDF retained in the team records was consulted. Printed page512, PDF page5, was rendered and visually read; the retained image is in the team records, with extracted first pages in the team records. Section1.2 defines the stable set by strictly negative upper exponential distance under forward integer iterates and defines the unstable set by applying the same criterion to f inverse. At regular points these are immersed C2 submanifolds tangent to the sums of the negative and positive Oseledets spaces, respectively. Zero Lyapunov exponents are explicitly permitted in the preceding Oseledets notation.

This supplies the report's unstable-graph characterization at regular base points: a nonconstant regular incoming curve whose backward distances contract at a uniform negative exponential rate belongs to that unstable set. There is no missing assumption of absence of a zero exponent. The report's provenance question2C.4 point17 can now cite Section1.2, printed page512, and state that the auditor checked the original page.

The separate full helicity-section audit already visually checked printed pages513,519,533,534 and535. The entropy-formula direction yielding absolutely continuous unstable conditionals, the converse credited there to Ledrappier-Strelcyn, and the nonergodic positive-density extension are used in the correct directions. The report should qualify geometric manifold assertions by Oseledets regularity, as the actual uses already do. No smooth unstable manifold at every nonregular point of K is asserted.

## 5. Full chain checks

The following checks are against the pinned text, in its displayed order, not a replacement of the cited complete source proofs.

1. The profile signs, alpha exterior derivative and transport, constant divergence3c, backward Jacobian exp(-3ct), and vorticity exponent kappa are correct. P C1 is enough because momentum upgrades its gradient to the required differentiability. Harmonicity of U when Omega=0 and div U=0 is distributional before regularity is used.
2. Uniform sublinearity gives two-sided completeness of B and the outward radial bound. Compact sets enter one admissible Q under Psi. The cutoff carrier agrees near K, extends smoothly to a compact manifold and has no relevant nonatomic ergodic measure in its transition annulus. Points where the cutoff vanishes are fixed, which are separately excluded by nonatomicity.
3. The Borel basin proof for the forward Psi flow can use a countable family on Q because every orbit eventually enters Q. This is different from the earlier backward-basin repair in Section2D. Local vortex saturation follows from conjugacy with a shrinking vortex parameter and bounded tests on the relevant compact orbit family.
4. The volume-to-curve step, affine curve tree, Vandermonde control and finite distortion are consistent with the earlier exact proofs. The small scale in Lemma11 can also be chosen below a quarter of the initial arc length before making the stated subarc cover. This is an available further smallness condition, not a new hypothesis.
5. The time-selection estimates charge only nonlarge hyperbolic returns. The order of choices is the exponent gap, the derivative order, the iterate and then the chart scale. The ability to choose arbitrarily high differentiability is essential in the smooth theorem. No fixed-r unconditional result is inferred.
6. Lemma12's entropy chain rule, bad-child estimate, residue-class telescoping and mass loss are correct. Restricting to positive-length curves makes normalized arclength weakly continuous. The countable Lipschitz-test argument and portmanteau give domination on that open class; taking K to infinity gives absolute continuity. Constant limit curves are explicitly retained outside that assertion.
7. In the increasing-window application all curve classes already live in one compact C1 ambient space. The marginal q^M is at most q and theta^M<<q^M lambda implies theta^M<<q lambda. Monotone convergence then gives theta<<q lambda. This direct argument avoids any need to interpret the snapshot's optional countable-disjoint-union wording for nested classes.
8. Incoming-curve tangency, the positive exponential backward-distance rate and the compactification put the curve on the full one-dimensional unstable manifold. The spectrum is then(chi,0,-d-chi). For the zero exponent, two-sided boundedness of the nonzero flow vector at a two-sided regular point rules out both positive and negative Oseledets components. No lower bound for its speed on the support is assumed.
9. Lemma19, with the Section2.1 clarification, eliminates the irrotational ergodic component. The remaining bracket law fixes the negative exponent at-kappa, and the determinant fixes the positive exponent at kappa-d. The supplied curve conditionals give the entropy formula. The measure's support may still contain zeros of either field.
10. Averaging a discrete g=Psi_p ergodic probability over one p-period produces a probability invariant and ergodic for the entire flow. Its entropy and spectrum are transferred using the stated entropy and flow theorems. Time-one ergodicity is not inserted. The positive unstable density assertion for the averaged measure uses the actual nonergodic extension.
11. The product-box columns are the unstable tangent, -B and W, with nonzero determinant. Its saturation and change of variables give positive volume. The capture argument only needs positive-length generic subsets and distortion bounds, and correctly returns positive length in the initial set. Distinct probability basins are disjoint, and sigma-finiteness of volume makes the positive-volume collection countable. The uncovered positive-volume contradiction proves coverage.
12. The alpha density formula has the correct backward-Jacobian product. Essential domains are open, contained in O, carrier-invariant and locally vortex-saturated. Their infinite volume follows from exact expanding Jacobian and invariance. The proof does not assert that an arbitrary invariant support has interior.
13. The componentwise finite-r statement preserves every extra hypothesis. Radius independence, the compact-core growth reduction, the projective-flow variational argument and the lower bound a retain their earlier A430 scopes, with Section2.2's empty-set qualification. Bounds are taken per component. The finite-r section is explicitly an outline referring to complete A416-A417 and A430-A432 proofs, not a claim that the displayed outline reproves every reparametrization estimate.

## 6. Verdict boundary and collaboration

The mathematical scopes already confirmed in A201,A207,A216,A223,A257,A299,A305-A308,A393-A394,A398-A399,A416-A418 and A430-A432 remain intact. The original Section2C draft is not yet unqualifiedly confirmed as a standalone text because of Section2's repairs. No flaw has been found in the main Euler implication after those local repairs. A final text verdict should pin the repaired source and check the coordinator's focused response.

This work uses existing file exchange with the coordinator and theory agents configured for model. The configuration is evidence of the requested model selection, not independent provider attestation. No new remote client or external contact is used. No numerical computation was needed for this audit.

## 7. Repaired text and the independent review

The revised1039-line snapshot in the team records, captured2026-11-03T05:19:45.837996+00:00 with SHA25645da959b073d089614bce11b37c692374cce827de9bceb2a3453b3fcce87786f, was read in full, in four consecutive chunks. The210-line repair diff was also read completely. The three Section2 repairs are present: real-time transport in Lemma19, attainment only for nonempty Z_E, and an interior point in Lemma25. The original Ledrappier-Young unstable-set definition and the measurable-kernel argument are now identified precisely.

The separate configured-model response in the team records was read completely. It agrees with the29-lemma chain and detects one further missing hypothesis in the original global formula: Lambda_core=max(a,Gamma_Z) requires W not identically zero. This is an exact counterexample to the unqualified version. Take U=0, P constant and B=Ay. Then Psi_t=exp(-At), ||D Psi_t||=exp(-ct), M_n=1 and Lambda_core=0. The core is the origin, the sole invariant probability has largest exponent-c, so max(a,Gamma_Z)=a>0. The revised Theorem C_r(C) includes the nonzero-vorticity qualification and records the vacuous irrotational coverage case. The componentwise formula is unchanged because a vortical component is nonempty by definition.

The full read found two remaining wording points. Lemma5(b) must state that Gamma_tau x and Psi_s x belong to Basin(nu); an arbitrary negative Psi translate need not belong to Q. The remark after Lemma20 must use strict radial decrease on all points outside Q with rho>0, including the collar where rho=1. A forward orbit in that set decreases its radius strictly until it enters Q, after which it cannot leave, so such a point is nonrecurrent. At rho=0 the nonnegative smooth cutoff has zero gradient, hence D(-rho B)=0 and all exponents at the fixed point are zero. These are local text clarifications, not new Euler hypotheses. They were sent to the coordinator in the05:20:10 note; confirmation of the final standalone text awaits their incorporation.

The review's warning about the target bin in A417 is correctly scoped: the actual geometric-time bin target has allowance-1, whereas a greedy-label preliminary target needs allowance-3, as in A431. It does not invalidate the corrected finite-regularity theorem. The review also confirms that the trapping ball Q may be convex; only its intersection with a component closure need not be convex. None of these checks certifies unconditional finite regularity.

Some global summary and ledger occurrences outside Section2C still lacked the nonzero-vorticity qualification at the subsequent full-source check. They need editorial synchronization even after this section is repaired. A text verdict for Section2C will not automatically certify the rest of the report.

## 8. Final repaired section

The final1041-line source snapshot and complete two-hunk repair diff are retained as in the team records and in the team records. The preceding entire1039-line source was already read in full. The new changes were read in full: Lemma5(b) states basin membership, and the compactification paragraph treats every positive-cutoff point outside int Q. Since the radial cutoff is nonincreasing in radius, its value along a decreasing-radius trajectory is bounded below by its positive initial value. The exterior radial derivative is strictly negative with a uniform bound on that compact radial shell. The trajectory therefore enters int Q in finite time and cannot return. Poincare recurrence excludes mass there. At a zero of the smooth nonnegative cutoff its derivative vanishes, so the compactified vector field has zero linearization and zero exponents. These complete the two remaining repairs.

Verdict A490 confirms this repaired standalone section at its exact smooth and conditional finite-regularity scopes. It does not certify every summary elsewhere in the report, unrestricted C2 coverage or arbitrary-sign nonexistence. No new computation was needed.

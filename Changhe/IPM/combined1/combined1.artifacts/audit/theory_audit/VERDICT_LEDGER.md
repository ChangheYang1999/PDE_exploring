# Independent theoretical verification report

Entries are appended in time order. Each entry records the exact claim, method, result, verdict and actual date. CONFIRMED applies only to the stated scope and dependencies; conditional theorems do not certify a numerical profile.

No completed audit entries yet.

## T4-001. Canonical strain and origin/scaling identities

- Date: 2026-10-28T20:34:45Z.
- Claim: the baseline contact coefficient is -1/4; fixed-exponent normalized forcing satisfies f_y(0)=a_0 c[h] when c[k]=0; center slope alone does not remove scaling.
- Method: independent distributional integration by parts, Gaussian angular check, first-order Taylor expansion, and dilation covariance. Full argument: audit record operator_audit, proof. Source hashes are retained alongside it.
- Result: all three identities hold under the stated regularity and canonical-inverse hypotheses. The variable-exponent operator has a different range and cannot be silently substituted. No numerical normalization or global inverse was independently certified here.
- Verdict: CONFIRMED.

## T4-002. Finite-rank approximation of the entire nonlocal coupling

- Date: 2026-10-28T20:36:20Z.
- Claim tested: Qh=U[h].grad(rho_bar) can be treated in L2 or integer Hm as a compact remainder approximable by finite matrices to arbitrary norm accuracy.
- Method: explicit high-frequency S1 wave packets in a small annulus around the origin, with exact strain correction. Read the primary Hou source Sections 1.3 and 2.4 to distinguish its actual smoother remainder from Q.
- Result: for every compact K, ||Q-K|| >= a0 when a0=rho_bar_y(0)>0. The statement remains true on the smooth zero-strain, zero-origin-jet test family. This does not obstruct signed coercivity or a graph-relative decomposition.
- Verdict: REFUTED for the full-Q compact-remainder claim. The lower-bound theorem and exact scope are in audit record finite_rank_limit, proof.

## T4-003. Passing the nonlinearity from low-energy compactness

- Date: 2026-10-28T20:39:35Z.
- Claim tested: an L2-bounded S1 sequence converging strongly in Hdot^-1, with zero strain and all center jets fixed, necessarily has a convergent IPM nonlinearity equal to the nonlinearity of its limit.
- Method: annular amplitude A times cos(nx), explicit multiplier limit U[h_n] approximately (0,-h_n), and an exact vanishing-strain correction. Proof: audit record weak_limit_obstruction, proof.
- Result: h_n tends weakly to zero in L2 and strongly to zero in Hdot^-1, while U[h_n].grad(h_n) tends to -(1/2) partial_y(A^2), a nonzero distribution. A low-energy Galerkin argument needs additional compactness.
- Verdict: REFUTED.

## Audit-version receipt, 2026-10-28T20:46:57Z

The initial header line saying no completed entries is superseded by T4-001 and later entries. The exact proof versions checked by the first three verdicts have these SHA-256 hashes:

- T4-001: `audit record operator_audit, proof`, SHA-256 `23126a68b002c9782b63655e857c08567fcf9ed35ad78671e96eac515fa169d1`.
- T4-002: `audit record finite_rank_limit, proof`, SHA-256 `52d3e55bc65310099ab788e74a993d3ab2e20f7dd9bd3b17fd4a343966b162a8`.
- T4-003: `audit record weak_limit_obstruction, proof`, SHA-256 `c1ef288063b1d1723eb48c2a05363bb4859a01498d080c4a3847d00efab450c2`.

## T4-004. Conditional closure from a computed linear correction

- Date: 2026-10-28T20:46:57Z.
- Target: `audit record alternative_route, proof`, SHA-256 `d347071a02ea22eef12b4d209886deb0118738338d27bd8c531bcc559dbc61fa`; Sections 2-4.
- Claim: under the stated baseline background and common-inverse assumptions, a smooth zero-strain g with m>=N_s(g), epsilon>=N_s(F+Lg) and multiplication bound B closes the high ball if (r-m)(1/10-4800s-5r/sqrt(s))>=epsilon+Br and the inverse gap is positive.
- Method: checked all four energy components, the fractional commutator moments, tensor coefficient sums, cutoff density, origin hyperplane, maximal distributional domain, common low inverse, and the exact scalar certificate. This is an author self-audit; an independent T1/T2 response is requested in team note 03 and remains pending.
- Result: the written conditional theorem is valid within those hypotheses. Eight bounds on the fixed correction through order four are required. B11 is required only for a specified leading-tail conclusion. No high-to-high bound for the full quadratic transport map is used.
- Verdict: CONFIRMED for the conditional analytic theorem and exact scalar parameter boxes. Numerical candidate hypotheses and independent Opus follow-up remain OPEN.

## T4-005. Signed principal part, compact energy remainder and L2 inverse

- Date: 2026-10-28T20:58:56Z.
- Target: `audit record signed_coupling, proof`, SHA-256 `058da78775cdfe71294ad6de011876fcf55b0c4c9fc523a4e4029328376b193f`.
- Claim: The exact symmetric coupling decomposition retains the principal matrix and has a compact commutator remainder. Its explicit finite-rank error and positive-gap criterion yield a maximal-domain L2 inverse.
- Method: Checked the operator adjoints, pointwise eigenvalue, two-sided Schur estimate, exterior Hilbert-Schmidt estimate, cell error, parity compression, zero eigenvalue on the infinite complement, semigroup domain and inverse integral. Independently matched Section 5 to the baseline N matrix.
- Result: The stated analytic theorem and constants hold. Baseline B2 already retains the same principal sign; no new numerical improvement is certified. The local scan is only a diagnostic.
- Verdict: CONFIRMED for the conditional analytic theorem; profile-specific matrix certification and high/nonlinear extension remain OPEN.
- Review status: author self-audit; existing Opus theory lanes have been asked for independent follow-up through team note 03-v05.

## T4-006. High derivative loss and the common low-domain argument

- Date: 2026-10-28T20:58:56Z.
- Target: `audit record nonlinear_audit, proof`, SHA-256 `be3a60d4861c50437c75fe2d504cf94d9ed1c1ce4f552bf0ec32acb63708be40`.
- Claim: The full transport nonlinearity is not bounded high-to-high, while the stated common-semigroup assumptions suffice for the low contraction domain and complete-ball steps.
- Method: Checked modulated Fourier asymptotics with weighted derivatives, exact strain correction, polarization, simultaneous Hdot^-1/L2 density, distributional semigroup consistency, generator orbit identity, stream-function product bound and weak compactness of the high ball.
- Result: A quadratic high-space bound is refuted by smooth zero-strain inputs. The baseline two-norm construction avoids that invalid bound and has a valid common-domain implication under the listed semigroup assumptions. Background constants are not re-certified.
- Verdict: CONFIRMED for the obstruction theorem and conditional common-domain lemma; REFUTED for any claimed uniform quadratic N_s-to-N_s estimate.
- Review status: author self-audit; existing Opus theory lanes have been asked for independent follow-up through team note 03-v05.

## T4-007. Necessary pointwise correction radius and uniform baseline-gap obstruction

- Date: 2026-10-28T20:58:56Z.
- Target: `audit record residual_witness, proof`, SHA-256 `7079170e843d64759e93a25cc17ce34742afdc2f29fd38473904cb88d78c661f`.
- Claim: Every exact stationary correction satisfies the explicit pointwise quadratic radius bound. Every ball with positive gap 1/10-4800s-5r/sqrt(s) satisfies the uniform rational point bound (6).
- Method: Computed the exact two-dimensional Fourier embedding integrals, used directional gradient duality, expanded the stationary equation, solved the quadratic inequality, and checked all rational relaxations using pi>3.
- Result: The bound is necessary and applies even when F is not in the sufficient forcing norm. It does not exclude larger balls, a different inverse estimate, a different norm or reference. Numerical exclusions require separately audited point enclosures.
- Verdict: CONFIRMED for the analytic necessary inequalities. Numerical applications remain PENDING-N4.
- Review status: author self-audit; existing Opus theory lanes have been asked for independent follow-up through team note 03-v05.

## T4-008. Numerical point exclusions for d2, Mpen2 and b6

- Date: 2026-10-28T20:58:56Z.
- Targets: `audit/theory_audit/research_code/residual_witness/verification/point_witnesses.json`, SHA-256 `d7bfd982f515fe941bb55adc4b940a7866c7422f5736bbd4d94cafb89111322c`; `uniform_gap_witnesses.json`, SHA-256 `344c0b3b716ddc6aacbe69d7cde466083d3fe20e5b90ea8b5209358985b5fdc0`. Input hashes are in the adjacent `input_hashes.txt`.
- Claim: the three exact refits violate the necessary uniform point bound from T4-007.
- Method: copied N4 exact canonical JSON inputs and evaluator, computed Arb768 point enclosures, then applied the rational bound to the saved interval outputs with Arb256.
- Result: positive gaps were found for d2 at (0,1), Mpen2 at (0,2), and b6 at (0,1), among others. This is a derived calculation using N4 code, not an independent numerical reproduction.
- Verdict: OPEN pending N4 confirmation of the conversions and point triples. The analytic implication is CONFIRMED by T4-007.

## T4-009. Hilbert-Schmidt double-commutator remainder

- Date: 2026-10-28T21:04:06Z.
- Target: `audit record double_commutator, proof`, SHA-256 `9d9b21f5fb83a716f680cee97f90908382605f0976dd865e9fe35c9972135a58`.
- Claim: the signed energy remainder is a double Riesz commutator with HS norm at most sqrt((4log2-1)/(8pi)) ||D²rho||_2; the explicit frequency and cell error estimates give a finite-rank approximation.
- Method: checked operator expansion, Fourier normalization, exact elliptic-coordinate integral, extension from compact coefficients, both frequency tails and the matrix-cell Lipschitz constants. A separate floating quadrature cross-check agrees with the exact integral.
- Result: the analytic bounds hold under the stated C_0 and derivative hypotheses. No candidate matrix or positive inverse gap is certified. The single-commutator analogue is not asserted.
- Verdict: CONFIRMED for the written analytic theorem, by author self-audit. Independent Opus review requested in team note 06; numerical application OPEN.

## T4-010. N4 exact Hdot^-1 radial formula

- Date: 2026-10-28T21:04:06Z.
- Target: N4 `audit record exact_negative_norm, proof`, frozen copy `audit/theory_audit/research_code/negative_norm_audit/source/n4_proof.md`, SHA-256 `f9eb62e30d03cf3192500d8d06e9a25331b5f43b4a80b371cc14007a12dc07cd`. Independent proof: `audit record negative_norm_audit, proof`, SHA-256 `ad805b628cdf8561dcc3945af5995c314670168df6c586a539ae1452531632d2`.
- Claim: the finite odd radial Fourier sum with every extracted exponent b>3/2 has the stated exact rational squared negative norm divided by pi.
- Method: independently derived the outer Green antiderivative, avoiding the source's intermediate logarithmic case, proved membership and energy identification, checked full-circle factors and inspected the frozen implementation.
- Result: the formula, all denominators and the factor1/(4n) are correct. Candidate calculations are not independently executed here. Generic INFINITE classification requires exact resonance grouping or the separately checked case4 nonresonance assumption; failure of b>3/2 alone is not a universal classification of ungrouped sums.
- Verdict: CONFIRMED for the analytic formula within its stated sufficient hypotheses. Generic unchecked infinity classification is OPEN.

## T4-011. Critical power/log weights and external tail coordinates

- Date: 2026-10-28T21:06:41Z.
- Targets: frozen A2 P61, P64 and P68 excerpts in `audit/theory_audit/research_code/critical_space_audit/source/`, individual hashes in `verification/source_hashes.txt`. Independent proof: `audit record critical_space_audit, proof`, SHA-256 `111e3d10996f50723c147409d9bf9b98fa12ce144d7e04e0b3823c188983d4ef`.
- Claim: exact finite constraints and compact observations of a critical power/log remainder do not remove its weakly null annular approximate kernel.
- Method: rechecked both weighted kernel block exponents, local strain regularity, every packet derivative, inner and outer coupling estimates, exact finite constraints, graph-space weak convergence and Banach quotient argument.
- Result: the stated obstruction is valid, including arbitrary Banach external coordinates when their observation of the compact core is compact. It does not cover noncompact bulk observations, a changed remainder topology, or a radiation domain omitting the test core.
- Verdict: CONFIRMED within these exact domain and compactness hypotheses. No universal obstruction to all asymptotic-coordinate methods is asserted.

## T4-012. T2 rebalanced scalar rate and nonlinear threshold

- Date: 2026-10-28T21:11:55Z.
- Target: T2-R1 and FW-T-TB-rebal-v1, frozen `audit/theory_audit/research_code/rebalanced_rate_audit/source/T2_routes_v01.md`, SHA-256 `5a9922992cde96267204307f08613b3cf95817379aa696ca912abc2288844bba`.
- Independent argument: `audit record rebalanced_rate_audit, proof`, SHA-256 `ef8ee8852ad5d5e9f9c1675bf9f3f210ecce8c56ca35f1b7c0aa56c14ca32bae`.
- Claim: the unchanged E2 weights give base decay 297/1000; with s=2^-16 and r=3*2^-15 the sufficient threshold is 3/327680.
- Method: reconstructed the quadratic form from the three P7.5 inequalities; independently checked its exact leading principal minors, rough/background losses, semigroup-domain argument, origin constraint, common low domain, complete ball and changed local moment parameters. Recomputed scalar constants in Fraction and Arb256.
- Result: rate on the ball is 13641/128000>1/10; gradient bound is below0.00662 and contraction below0.0018. No other proof step requires the old d<1/400 or s=2^-18. The threshold is in the new Ns16 norm.
- Verdict: CONFIRMED, conditional on the stated reference hypotheses and new residual upper bound. This is an independent audit of T2's claim, not a self-audit. No candidate closure follows yet.

## T4-013. T1 four-component closure and missing explicit feedback condition

- Date: 2026-10-28T21:11:55Z.
- Target: Section4 of frozen `audit/theory_audit/research_code/graded_closure_audit/source/T1_model_v01.md`, SHA-256 `5ce5eedb5b830f234fb2f618d41ab697b4906b1fd4c93b8a8f0efb45bac2abe7`.
- Independent argument: `audit record graded_closure_audit, proof`, SHA-256 `9f5928835f1a5ba04c0ceb5118d7c41d8d830100138e363acec9a53ed99d1bb1`.
- Claim: the four component inequalities yield a uniform inverse and normalized nonlinear closure on a component box.
- Method: independently checked every P8.4 row, all occurrences of the rough k norm, the H product estimate, the improved top product, an explicit auxiliary energy, approximation and maximal domains, component-bound limits and low contraction.
- Result: H1, H2 and H4 hold. H3 holds with the additional explicit condition q0<mH*sqrt(m0), already tested in T1's code. Positive diagonal margins alone are insufficient. The theorem and proof state this condition and give explicit auxiliary weights. An independent Arb256 rational box is in verification/rational_box.json; no optimized maximum or candidate data is certified.
- Verdict: CONFIRMED for the conditional theorem with the feedback condition. The bare claim that positive diagonal margins alone suffice is not confirmed. This independently audits T1's proposal; the new illustrative rational box still awaits another lane's arithmetic reproduction.

## T4-014. Exterior negative-norm tail witness and the role of onset

- Date: 2026-10-28T21:18:31Z.
- Target: `audit record exterior_tail_witness, proof`, SHA-256 `8f3d5dff89092fac93c17fba4eb7922642ec03c8bd2db07c0aae85df6e6730e5`.
- Claim: an exact exterior sector r^(-2-sigma) sum a_n sin(n theta) gives the interior-independent lower bound pi*T^(-2sigma)/(2sigma) sum a_n^2/(n+sigma)^2 for the squared homogeneous negative norm. The exactly truncated sector has n(n+sigma) in the denominator. A fixed asymptotic coefficient alone gives no positive uniform norm floor.
- Method: solved the exterior Dirichlet problem mode by mode, including resonance n=sigma; checked density, duality and full-circle factors; independently computed the truncated Green energy; checked the quantified remainder and scaling construction. Symbolic examples are in verification/modes.json.
- Result: the lower bounds and counterexample hold with the exact stated onset and remainder hypotheses. The construction concerns forcing functions, not a claim that all such functions are realizable as residuals in the finite IPM family. The existing degree-limited six-branch lower bound is unaffected.
- Verdict: CONFIRMED by author self-audit; team status CLAIMED pending independent review. A Hardy upper proxy alone is insufficient to infer a necessary onset radius.

## T4-015. Independent reviews complete the baseline point exclusions

- Date: 2026-10-28T21:18:31Z.
- Targets: T1 independent review R1-001, frozen `audit/theory_audit/research_code/residual_witness/source/T1_reviews_v01.md`, SHA-256 `bacf115b323c57103495bc650dd1c0aa4d3de40f362f7dd5a754906ce40c66ed`; N4 independent Cartesian evaluation, frozen `audit/theory_audit/research_code/residual_witness/verification/N4_cartesian_witnesses.json`, SHA-256 `4596e2d6a18041d2bad3a01f14cca26611ba508070be63ec77786b2984407a7e`.
- Claim: the exact d2, Mpen2 and b6 references violate the necessary point inequality for every positive baseline-gap ball.
- Method: T1 independently rederived the embedding constants and all rational relaxations in T4-007. N4 independently evaluated the selected points through a Cartesian Taylor representation at Arb1024 precision, separate from the radial recurrence used in T4-008. Checked the frozen reviews and matching input and output hashes.
- Result: positive gaps are approximately 0.00673833 for d2 at (0,1), 0.06355669 for Mpen2 at (0,2), and 2.95346980 for b6 at (0,1). T4-008's pending numerical condition is resolved. T4-007 is independently reviewed, so the analytic implication is AUDITED under coordinator amendment v03.
- Verdict: CONFIRMED for these three exact references and every ball with positive gap 1/10-4800s-5r/sqrt(s). This does not yet exclude every ball with the improved base rate297/1000, a different component norm, a different reference or a different inverse estimate.


## T4-016. Exact gradient-structured Hilbert-Schmidt identity

- Date: 2026-10-28T21:20:11Z.
- Target: N4 `audit record gradient_commutator, proof`, frozen source SHA-256 `e5f6483e981baff0ba8edc00abc4bb661dcd5edba06e68a243d699acba7c6994`. Independent proof: `audit record gradient_commutator_audit, proof`, SHA-256 `63e9f4875e5ddfeeb3c0486063a4ef692d7122176f657dee898af22bf3b1c6af`.
- Claim: the squared Hilbert-Schmidt norm of the exact compact symmetric remainder is (log2-1/2)/(16pi) times ||D rho_x||² plus (3log2-2)/(16pi) times ||D rho_y||².
- Method: independently reconstructed the Fourier kernel, rotated and scaled the inner frequency integral, evaluated both elliptic-coordinate constants, checked every Plancherel factor and the orientation of the Hessian columns, and proved the cutoff extension to sublinear profiles.
- Result: the identity and its universal coefficient sqrt((log2-1/2)/(16pi)) are correct. The analytic identity needs no floating quadrature. Profile seminorms and a positive inverse gap are separate claims.
- Verdict: CONFIRMED by independent cross-lane proof audit; eligible for AUDITED under coordinator amendment v03. Numerical background values remain N4-ORIGIN pending their separate review.


## T4-017. S1 symmetry strengthens point exclusions to base rates up to0.3

- Date: 2026-10-28T21:20:45Z.
- Target: `audit record symmetry_point_witness, proof`, SHA-256 `f9344e9033930ce6c50895ba42a939c39e4e47f7624e90e17f4e53e942ea393b`. Interval evidence: `audit/theory_audit/research_code/symmetry_point_witness/verification/witnesses.json`, SHA-256 `583931eecc3aaa210aa807d50d8d9053a61a34fbff0ef2280130bcee64cb83a7`.
- Claim: for0<s<=1/2 and |y|>=1/2, the S1 gradient point constant at(0,y) improves by sqrt(2). Every scalar-gap ball mu-4800s-5r/sqrt(s)>0 with0<mu<=3/10 obeys the rational necessary bound(4).
- Method: computed the norm of the parity-projected derivative representer; derived the reflected covariance from the heat kernel; proved its sign by the integral definition of K_nu. Optimized the radius bound and checked all rational relaxations exactly. Applied the resulting inequality with Arb256 to the independently confirmed N4 Cartesian point intervals.
- Result: strict violation gaps are0.00138045382623607 for d2,0.0518750863119540 for Mpen2, and2.94836588663451 for b6. This includes all positive-gap balls with T2's base rate297/1000, but does not address arbitrary component boxes or different inverse costs.
- Verdict: CONFIRMED by author self-audit; team theorem remains CLAIMED pending T1/T2 independent review. Numerical inputs are independently CONFIRMED; the new rational postprocessing is provided for independent reproduction.


## T4-018. Independent exact reproduction of background seminorms

- Date: 2026-10-28T21:24:20Z.
- Target: N4 `audit/numerical_audit/research_code/background_sobolev/verification/state131.json`, frozen SHA-256 `c5bd82c83142b9673c2053e4f923d758055fefc0c8be68ae287820ee38554027`. Independent proof: `audit record background_norm_reproduction, proof`, SHA-256 `52355ab5d054e3390ec6b322cf89054e1e5c2b53b8a9c2824461cb0825f28161`; independent output SHA-256 `515b7df592818cdc78a1805115a1a2fda4cf7f527970db74376b1019522c7315`.
- Claim: the four state131 background seminorms and the resulting anisotropic Hilbert-Schmidt norm have the values reported by N4-018.
- Method: reconstructed rho from a direct radial Laplacian of the canonical potential, used Hessian integration-by-parts identities, and integrated the resulting products by an exact rational beta recurrence. No N4 derivative or norm code is called. Compared all four exact rational energies, not just displayed decimal intervals. The canonical potential input itself is shared and already independently audited by N4.
- Result: all four rational energies agree exactly. Norms are ||D²rho||=16.9864259963711, ||D³rho||=10.4642093189440, ||D rho_x||=4.66141632497324 and ||D rho_y||=16.3343155955634. The separately audited identity gives ||K||_HS=0.7107535441929825338137948. Actual numerical runtime4.18seconds; output includes the measured value.
- Verdict: CONFIRMED as an independent reproduction of N4's background calculation and an audit of the underlying formulas. No full-plane new matrix bound or nonlinear closure is claimed.

## T4-019: Three-component high norm with a low L2 inverse

Date: 2026-10-28T21:29:35Z.
Claim: Under the explicit structural, signed-margin, derivative-energy and component-commutator hypotheses in audit record l2_closure, proof, the no-H high norm X_s has rate 1/4-4800s-5X_s(k)/sqrt(s). With s=2^-17 and radius2^-14, an actual residual norm at most1/163840 gives a unique normalized stationary correction, with L2 contraction ratio below0.00312. The pure-power residual threshold is q<-1.
Method: Decompose Sym Q into the signed Riesz principal form plus the independently audited gradient-structured HS remainder; obtain L2 decay2. Retain the first three rows of the A2 energy and commutator identities, verify their independence from H, and prove the rough realization and maximal domain through low-L2 convergence. Check the full Gram minors and parameter box with exact rational arithmetic and Arb256.
Result: Gram minors 1/4,144831/100,1077858728/25 are positive. Beta>0.10289347; the L2 contraction ratio<0.003116725. The independently reproduced state131 background gives low margin>2.04956566. State131 itself fails residual L2 membership; no new candidate existence is claimed.
Verdict: CONFIRMED by the author; CLAIMED under coordinatorv03 until an independent Opus theory lane reviews this new theorem.
Target proof SHA256: e15173a459fd59e89c1c4746b0fb6f32d35891cc948930c0ded553ac5aeb6e0f.
Arithmetic evidence SHA256: e306deb98fda27c3c273899a3237367b96b4e4e7a4603c448957bef5c36b5946.
Dependencies: P7.5/P8.1/P8.4 source excerpts are frozen in audit/theory_audit/research_code/l2_closure/source; the manifest audit/theory_audit/research_code/l2_closure/SHA256SUMS records their hashes. T4-016 audits the HS identity and T4-018 independently reproduces the exact background seminorm integrals.

## T4-020: Angular bandwidth, midpoint exactness and the scope of a Gauss-rule witness

Date: 2026-10-28T21:31:57Z.
Claim: See the exact statement and scope in audit record angular_rule_audit, proof.
Method: Independent polar-frequency count; explicit geometric-series orthogonality for both odd sine density modes and even cosine quotient modes; Gram-matrix comparison.
Result and verdict: CONFIRMED. N>=2M+2 quadrant midpoints integrate both squared fields exactly at each fixed radius. N4's analytic claims are correct. This does not certify its floating eigenvalues, a radial integral, or realizability of an arbitrary test polynomial by a nonlinear IPM residual.
Audited target SHA256: 16ad586b4a31050b95fd59aa3911f139e01a3b935dbe14d70faebeeae1d6c402.
Independent proof SHA256: 51e732394db6a3b0bff5dbf9e83bd7866979b42dd747230d341a69248ece594f.

## T4-021: Independent application of the point inequality to the rebalanced and specified graded boxes

Date: 2026-10-28T21:31:57Z.
Claim: See the exact statement and scope in audit record new_ball_point_audit, proof.
Method: Independent Arb512 postprocessing of exact radii and the already confirmed Cartesian field enclosures. No N4 scalar code imported.
Result and verdict: CONFIRMED. All six strict gaps overlap N4; d2 has gaps0.00620093765682 and0.00109819662480. The analytic point inequality is already independently confirmed by T1/T2. This excludes these specific balls, not every graded box.
Audited target SHA256: 9c0784f6e3b4699a421ea7af5e9a64b05b02c510e5fbfca547d2393b91b21fa2.
Independent proof SHA256: 82c4c52b5b9473349a8b513eee9664ab2fea87d90b64d3b5b74f8ef12b7c8569.
Arithmetic evidence for T4-021: audit/theory_audit/research_code/new_ball_point_audit/verification/reproduction.json, SHA256 7c2a487c9e417b7ed8061adeab4281407218db10e159816a46aecbb577f5945e.

## T4-022: Explicit radial weighted L2 commutator and low inverse

Date: 2026-10-28T21:37:01Z.
Claim: For real centrally odd inputs,0<a<2 and0<d<2-a, the weighted velocity commutator has norm at most C(a,d)R^(-d) from L2 to r^d L2, with C(a,d)=a M_d sqrt(((2-a-d)^(-2)+(2+d)^(-2))/2). If beta0 is an unweighted L2 rate, the weighted rate is at least beta0-ca-[C_rho C(a,d)+a C_u M_d]R^(-d).
Method: Derive canonical Beurling angular Volterra kernels, bound the two weight-ratio differences, integrate their positive kernels exactly, and use equal positive/negative angular energy for real inputs. Conjugate the transport and retain the identity/contact term, whose commutator vanishes. Check state131 low-space parameters with Arb256.
Result: The low-space example a221/200,d4/9,R2^29 has rate>0.02181481 and admits the original residual at infinity. No compatible high inverse, full residual smallness or nonlinear existence is established.
Verdict: CONFIRMED self-audit; CLAIMED pending independent Opus review.
Proof SHA256: e9e72abe2aa0f5274c461ff9f9c34b50a7269416e32cc264020b1209949c2aed. Arithmetic evidence SHA256: 4b9ea4494d056d0046fb39d0baa5198b8b593c17f100a6a70a80368fca1d9f9f. Frozen P7.2 and P21.1 source excerpts are included alongside the proof.

## T4-023: Independent Opus review closes the S1 point-theorem audit

Date: 2026-10-28T21:40:16Z.
Claim: T4-017's S1-axis derivative constant and its uniform scalar-ball exclusions are independently confirmed.
Method: Read the T2 theory worker's complete independent review, verify the reviewed proof hash, and freeze the review. T2 redid the parity projection, Fourier constants, heat-kernel/Bessel identity, sign argument, exact rational relaxations and all three interval gap calculations.
Result: CONFIRMED, independently reviewed by the T2 theory worker (configured model us.anthropic.claude-opus-5-5). T4-017 is eligible for AUDITED. Its scope remains the same fixed-exponent chart and scalar gap mu-4800s-5r/sqrt(s)>0 with mu<=3/10; arbitrary component boxes and changed rough costs are outside this statement.
Reviewed proof SHA256: f9344e9033930ce6c50895ba42a939c39e4e47f7624e90e17f4e53e942ea393b.
Frozen independent review SHA256: 887d4996d933a2a3d0cae58f1a78fe194eb8ed71820515b166c4768550262ef8.
Numerical fields retain their separately confirmed status. T2's additional proposed general-mu exclusions are not incorporated by this entry.

## T4-024: Independent reproduction of frozen angular quadrature witnesses

Date: 2026-10-28T21:40:16Z.
Claim: The three frozen positive-weight angular rules can underestimate squared norms in the full allowed odd-sine space by factors below one millionth.
Method: Read exact rational frozen nodes and weights and integer sine coefficients; use 512-bit Arb with an odd-sine recurrence from sin(theta) and cos(2theta), independently of N4's separately evaluated sine sums. Compare with the analytic integral pi/4 times the squared coefficient sum.
Result: CONFIRMED. Ratios are 3.70877085961885e-14 (M59,N160), 1.50395584330845e-18 (M69,N160), and 3.17442906914603e-12 (M69,N192). Each overlaps N4's interval and is rigorously below 1e-6. Actual runtime 0.141037701 seconds. These are witnesses in the full angular polynomial space; no assertion that a witness is realized by an IPM residual or that a particular candidate's loss has this error.
Frozen N4 witness SHA256: 0e798c2a3182f75f3a7f3e4b0821fc42359dff873ed3c4db7aa0cee14ccfc767.
Independent code SHA256: 65c7c0f7b2c92c28a8a5589b2afa6f4af80c215c555788f3ae0610d5709d83df.
Independent output SHA256: 2304596631e2086edacfac176ac05952fcba71bc658e9308e88918f4b55c0472.
Analytic context: T4-020, audit record angular_rule_audit, proof.

## T4-025: Finite-family L2 floor, independent analytic audit

Date: 2026-10-28T21:42:09Z.
Claim: The finite-family L2 lower bound in N4 audit record l2_family_floor, proof is correct under its exact family, stationary-profile and power-distinctness hypotheses.
Method: Independently count radial polynomial degrees, identify the fixed coefficient after the (1-u) transformation, verify all integrability thresholds, derive the Cauchy power-space distance via a Mellin rational function, and check full-circle normalization.
Result and verdict: CONFIRMED for the analytic theorem. The lower bound is E_B D/sqrt(2). Its high-norm implication is conditional on X_s>=(1-34s)E and E>=512G0. Arithmetic values and resulting exclusions remain pending separate reproduction.
Frozen audited target SHA256: f99802da933cca5f69360c62303d69591a59fad6affd44839a160a294c2875fb.
Independent proof SHA256: 6a9716feadefc98ae61acc387339df531f7438fc7aefbdd8f08b8c0627ed3064.

## T4-026: Independent numerical audit of T4-019's scalar box

Date: 2026-10-28T21:45:45Z.
Claim: The matrix minors, commutator row sums, rough-cost scalar inequality and numerical parameter box in T4-019 are independently confirmed.
Method: Read N4's separate Fraction interval implementation and frozen output; verify outward square roots via integer square roots and the alternating-series Machin enclosure for pi. Check the reviewed proof and arithmetic-target hashes match T4-019.
Result and verdict: CONFIRMED for finite algebra and scalar arithmetic. All three positive minors, the bound A_s+B_s<5, beta>0.1, the self-map inequality and L2 contraction<0.00312 pass. The output overlaps the original Arb calculation. This is not an independent review of the analytic generator, trace or nonlinear theorem, which remains CLAIMED pending Opus review.
Frozen N4 review SHA256: e685836e5226a6ea956ee6a0de277e06de59844a586908bfea63149c09a798ad.
Frozen independent output SHA256: 292ae944ae3cdb233d648c7a0a4629c4f0bbb5c43bdbb32c491caaa6f96ec801.
Frozen independent code SHA256: a6162f13bde83e13f5008946f1856d97611bbbc186dd56e7ce549e3b6474f704; helper SHA256: 56da80e573ede867ca7eea55479ebaa70804dee4a36a932d4dfb0d36421ca68f.


## T4-027: Independent product evaluation of finite-family L2 floors

Date: 2026-10-28T21:48:26Z.
Claim: N4's selected finite-family L2 floor values are reproduced independently, and the four-branch floor has a sharp integer crossing for the T4-019 threshold.
Method: Use the same exact stationary angular coefficients, sum their rational squares, and evaluate every Cauchy-distance factor directly as a positive integer ratio with 512-bit Arb. No gamma-function code or N4 floor implementation is used. Compare all selected output intervals.
Result and verdict: CONFIRMED for N4's eight four-branch rows (K=75,150,300,750,1500,3675,10000,100000) and its B=5,6,7,8 rows at K=150. All interval pairs overlap. Actual runtime 13.282575502 seconds. In particular the B=4,K=150 lower bound is 0.1083720980773968, and at K=10000 it is 3.745607591802169e-5, both greater than eta=1/163840. The B=5,K=150 bound is only 4.33863017283021e-16 and cannot exclude that family.
New numerical extension, T4-ORIGIN pending independent reproduction: the B=4 floor is greater than eta for K=25929 (6.103834828383889e-6) and less than eta at K=25930 (6.103386574210375e-6). Increasing K only appends factors strictly between zero and one, since every exponent exceeds -1/2. Thus this floor excludes every nonempty four-branch family of radial degree at most25929, conditional on the norm comparison and eta of T4-019. It says nothing about attainability beyond that degree.
Scope: the analytic floor is independently AUDITED in T4-025. The stationary-profile coefficient file is shared input; this calculation independently evaluates the product, not the upstream stationary recursion. No unrestricted-profile exclusion is asserted.
audit/theory_audit/research_code/finite_family_l2_audit/code/reproduce.py SHA256: 3914eb48dcf09bd0f380c0613eea04a2d3bc260cf12da8e69b1f386ae8e56ba7.
audit/theory_audit/research_code/finite_family_l2_audit/verification/reproduction.json SHA256: e783c121406679da6b085e5d84fa403535aca4096a525434fb5bdba4031e8609.
audit/theory_audit/research_code/finite_family_l2_audit/source/N4_floors.json SHA256: 29ddfd1cc6aa4e8f824cb1e5558befdd1b81d88bdff4815a58fa59f616de29a5.
audit/theory_audit/research_code/finite_family_l2_audit/source/stationary_principal.json SHA256: b80ec60e098b2752543d52548139ef264c1cca0dc4c273d789e5feb4274ae363.

## T4-028: Independent audit of T2-R2 sharp fractional constants

Date: 2026-10-28T22:00:03Z.
Claim: T2-R2's smooth constant402, rough constant8/5, and conditional Ns13 closure box are valid under the stated A2 background and realization hypotheses.
Method: Independently derive the positive Bessel moments, weighted multiplication estimate, divergence-free transport Taylor cancellation, principal-kernel first moments, weighted rough commutator and product estimate. Reconstruct every matrix entry. Bound all constants by exact rational arithmetic using Machin's identity, the gamma logarithmic derivative and elementary power comparisons. No numerical special-function implementation is used in the independent certificate.
Result and verdict: CONFIRMED for the central analytic theorem and specified box. The rational upper bounds give maximum symmetric row sum401.077615465183<402 and rough cost1.590957279309<8/5. For s=2^-13 and r=43/50000, beta>0.12338643054652>123/1000; eta=5289/50000000 maps the ball to itself; the low contraction is below0.005811947725. The output-weight transport remainder uses the weight on D²u and an unweighted input; the stronger form follows explicitly from Lemma6(ii), even though its headline gives a weaker bound. No derivative of the rough coefficient beyond H^(2+s) is used. Local delta terms commute with the weight.
Scope: No candidate residual, new background cap, floating sensitivity study or optimum is certified by this entry. Numerical component requirements in the target need minor correction: P2 projects J^s F, not raw F without a norm comparison; G1's necessary limit is exactlyeta/128=8.2640625e-7, so8.26e-7 is not an outward necessary bound. The displayed k1u<=1.5723 also rounds down; use the exact formula or1.572304. These presentational issues do not enter the exact constants402 and8/5 or the certified box.
Audited target SHA256: 1d2d65b523562d5a6d71fb5e53598047b0604882c97d084f481f1fecdc042fc1.
Independent proof SHA256: b6584a83bbadbc2bea8459164eaef7b7f37db4b972b7901eaf9870ecf68ebaa0.
Rational enclosure argument SHA256: 6d951e2a46b4210e3931e232fb34f662bdcc54c868d6ec401baefc17d9bb3758.
Independent code SHA256: 4d321a28a6d340d63b0bdfd428a747d22e0768174d6ab07ada40f699c3bb84dd.
Independent output SHA256: be2af017e9c0b290070caa06ea0c4eccc026f6f7ff00855f711016475224f77b.

## T4-029: Reconciliation of the finite-family integer cutoff

Date: 2026-10-28T22:00:03Z.
Claim: The B4 cutoffK25929/25930 of T4-027 has an independent N4 evaluation and is no longer T4-ORIGIN.
Method: Freeze N4's previously published boundary output and compare its gamma-formula intervals with T4's independent direct-product intervals, after exact normalization by eta=1/163840.
Result and verdict: CONFIRMED. Both interval pairs overlap. K<=25929 is excluded by this finite-family lower bound under the analytic and norm hypotheses stated in T4-025/027; K25930 is inconclusive, not feasible. N4 had independently obtained these values before T4-027, so the pending label in that entry and team note 17 is superseded here.
Frozen N4 target SHA256: c5f86e3cc15e16cc8b26dc8c3955799100fbc3a569c6276f8cc5bfffc2dd721e.
Comparison output SHA256: 700365073e23c4b991ead78854fb1be2628e01b38d86eb98a2c8ce38a2ab9a02.

## T4-030: Independent point exclusion for the T4-019 box

Date: 2026-10-28T22:00:03Z.
Claim: None of d2, Mpen2 or b6 admits an exact stationary correction in the specified X_(2^-17) ball of radius2^-14 in the fixed-exponent chart.
Method: Apply the already independently audited point inequality to the confirmed Cartesian field intervals, using a new Arb512 calculation and comparing to N4's separate Fraction-interval output. Only the H^(2+s) control by X_s is needed; the T4-019 existence theorem is not needed for this necessary condition.
Result and verdict: CONFIRMED. Strict residual-minus-correction gaps are0.00658506512141,0.06304303755267 and2.95332455714483 respectively, at the frozen axis points. All six output intervals overlap N4's. This excludes the specified ball, not all possible L2-based frameworks or larger corrections.
Frozen N4 target SHA256: 30e585ae065643db5b765a290b39d83ed0be91d59a9417a476f06f60e6b2f63b.
Independent code SHA256: a19ce3b94d1ce871bb4404b8e7ee913ab186f1cdc28edba0eabe5a8ff873abf5.
Independent output SHA256: 3b209d98d01f280f5f68d5ef165ac2fc4ce5328bd35cfd235ba304f312b60539.

## T4-031: Exact background seminorms for the three admissible refits

Date: 2026-10-28T22:01:35Z.
Claim: N4's four background seminorms and structured Hilbert-Schmidt values for d2, Mpen2 and b6 are independently reproduced.
Method: Construct rho from the radial Laplacian of the exact potential, compute the Laplacian and Hessian diagonal difference, apply the integration-by-parts identities in audit record background_norm_reproduction, proof, and integrate signed cross terms with an exact rational beta recurrence. Compare all four rational energies exactly, then use Arb512 for square roots and log2. This differs from N4's derivative and integration path.
Result and verdict: CONFIRMED. All twelve rational energies agree exactly. The structured kappa values are0.71041113747990759(d2),0.71262892806326245(Mpen2),1.76061564341649873(b6). Since b6 has kappa>c-1, the sufficient condition c+1-theta-kappa>=2 is impossible for theta>=0. This does not disprove actual coercivity. d2 and Mpen2 still require their own principal-sign and remaining background certificates.
Evidence correction: the original loop shadowed the candidate-name variable. d2 and Mpen2 were rerun after the fix, taking86.810451190 and87.043990453 seconds. The b6 raw record is preserved with a documented metadata correction and original hash; its numerical runtime was175.303070653 seconds. Canonical input and target hashes identify every calculation. Numerical values were unchanged by relabelling.
Method proof SHA256: 52355ab5d054e3390ec6b322cf89054e1e5c2b53b8a9c2824461cb0825f28161.
Corrected code SHA256: c995ac1068dd08559c1759291aadb7c0bc1acb5e18e16d33d9cb290ec9ec8de9.
Comparison manifest SHA256: 14027d897f0c50f952957f431abba2033d45f556ad669eece2cd7e9fe617c341.
d2: input ff1cb263a566ccf9cbe9321ae42d521ab8672dbb669d191da99d49756d43ef8f; N4 target c6b09fffec79c2c594fc3157e4fb4b8ea50bece832fa5ae2eeacda692976e668; independent output 38a4aa3c8b9e3add7db55b941019722d182f43b359bd907045bc36d3214ae523.
Mpen2: input af6554eecfe9ad81f53c8e439b58467208bbaa3b1787716a5fd8ffbbac8bb553; N4 target 74ba66d2c53128bed86b99c552d475571b404c47bae1383495c30e399a2989c0; independent output 3eeea137376192eca946a26d348e90ce6caecd3bbdf23a66bb4325b747a91aad.
b6: input fb182c8e0cf19052ffc2b20424551aa2e3d41b958c04ebd499dff848f926d4e0; N4 target 63b4118000766c22a0296a5caea67b4f4ee5e286344d25eac1093c29676672bf; independent output 0ca483dbceed01534837b1755839a820151b1424ac6f5bc8a1dcea02a5b72d5e.

## T4-032: Weighted forcing lower bound, independently reconstructed

Date: 2026-10-28T22:06:04Z.
Claim and method: The exact statement, hypotheses and independent argument are in audit record weighted_forcing_audit, proof.
Result and verdict: CONFIRMED. A separate polar density/stream construction, exact rational square expansion and Arb1024 power integration reproduce all seven annular values and the exterior lower bound 25963336062.244749522984813786059 for state131 at a=221/200 and R=2^29. The exact computation took1.569512389 seconds. This quantifies a severe cost of this particular weighted norm; it is not an inverse-correction lower bound or a nonexistence theorem.
Audited target SHA256: 015149b03dfa38315b85716ef8b616403956065eed0d212b3b195d638cfffac8.
Independent proof SHA256: fb9eb6e4cda87374d009396e20e45fa0c91c4c802bf43dca11c6a8bcd3730f9c.

## T4-033: Finite-generator membership contracts

Date: 2026-10-28T22:06:04Z.
Claim and method: The exact statement, hypotheses and independent argument are in audit record membership_audit, proof.
Result and verdict: CONFIRMED for the analytic equivalences under the exact fixed exponent and the convergent differentiable finite-generator expansion. The no-H energy and weighted third derivative require exactly E_(1,0)=E_(2,0)=E_(3,0)=0. Adding Hdot^-1 requires E_(h,0)=0 for h=1,...,5 and E_(0,1)=E_(1,1)=0. Exact sector cancellation is required; small numerical coefficients do not suffice.
Audited target SHA256: 1ead27cf206ddc077032a49603dacf6ace06c127bb4fa5c909f8dfb2ec758b53.
Independent proof SHA256: 1de2059a9c5306ee28dad6a82af9b802c71aec3a94530147ee4bdd0ab8bb04fb.

## T4-034: Global matrix-cover identities and acceptance method

Date: 2026-10-28T22:06:04Z.
Claim and method: The exact statement, hypotheses and independent argument are in audit record global_matrix_audit, proof.
Result and verdict: CONFIRMED for the algebra and analytic soundness of the cover test. I independently derived all matrix entries, checked the polar scalar, Bernstein/Taylor range method, eigenvalue lower bounds and finite-tree coverage argument. This entry does not independently reproduce every d2 leaf. In particular the weighted M1 in this test is not the unweighted first-derivative matrix I-sym Du+A in T4-019.
Audited target SHA256: 0ec6dd18926b32268d54d12f008d5b4203f7c8567eac70d61372678966268594.
Independent proof SHA256: c6f48ad0a2ab5b8363e9e13e59f180442dcc0b2e7dd648b3aa8be1079ca863b4.
Weighted numerical target SHA256: 9e18d9c0ef4008303227b59fdbaea65e3416ef5195e8926a0965436c01e8b2ee.
Independent weighted code SHA256: 8404e08095e51b9362420e0f63f8b10937d9925048ca00589175655be7aac467.
Independent weighted output SHA256: be77f8866868c767bfb48baf23d43ab299ff71b0426318e1cce0b37eef97339e.

## T4-035: Independent Opus review of the L2 closure theorem

Date: 2026-10-28T22:09:42Z.
Claim: The full conditional T4-019 theorem, including deletion of Hdot^-1, maximal domains, normalization and nonlinear contraction, is independently reviewed.
Method: Freeze the T2 theory worker's complete fourteen-step review, its independent script and output. Compare the reviewed hash with the unchanged local proof. Supply the explicit L2 consistency argument requested in the nonblocking remark R2.
Result and verdict: CONFIRMED. T4-019 is now AUDITED as a conditional theorem under (A)-(D), F in X_s and X_s(F)<=1/163840. The inverse bound1/2, high rate1/4-4800s-5X_s(k)/sqrt(s), specified box and contraction all survived independent review. No candidate satisfies the complete hypothesis set in the present record. The review's floating quadrature of the Hilbert-Schmidt coefficient is a check only; the exact identity remains the separately audited T4-016 input.
Reviewed proof SHA256: e15173a459fd59e89c1c4746b0fb6f32d35891cc948930c0ded553ac5aeb6e0f.
Independent review SHA256: d3914c4a2cb64928fcc5cb18ed4f396f9a91adca16e624c6ada45a74e510fa76.
Independent review code SHA256: 8bb53776ae010bd7cb2ef8423380efc7f9bd4e147c1591294a1dc2acd2401660.
Independent review output SHA256: 1a447f9bdb4b05b553131d1afc4a8791e3238335f336b65230b194521c20072e.
Clarification SHA256: d828bdc758d4beb975d8abbd5a2d6e79c4789b9b6bf5e2eccbf643fc3a896b48.
Record clarification: the three final hashes printed under T4-034 (weighted numerical target, independent weighted code and output) belong to T4-032. They do not describe the matrix-cover audit.

## T4-036: Scope and arithmetic of the numerical tail claims

Date: 2026-10-28T22:14:52Z.
Claim: The pure leading-power formulas in numerics_v01 provide universal fixed-radius lower bounds and a finite coefficient root screen establishes the convergence threshold of the stationary series.
Method: Independently check N4's cutoff counterexample, derive the exact pure-power integrals, and recompute ten pure-model rows from exact rational angular coefficients using Arb512. Check the bilinear index range of a truncated stationary profile.
Result and verdict: REFUTED for the general lower-bound and convergence inferences. CONFIRMED for N4's scope correction and its ten corrected pure-model rows. These rows are equalities for a pure exterior power, not lower bounds for a complete candidate residual without a remainder estimate. The finite-family theorem T4-025/027 is unaffected. In addition, eliminating descendants q=1,2,3 does not by itself remove the higher principal interactions h=N+2,...,2N+1 of a profile truncated at j=N; an O(r^(gamma-8)) remainder requires checking those sectors too. No unpublished candidate is declared invalid here.
Numerics target SHA256: 975aa84c943a0ab52dfd2d22baf1eb54f4c384f1f9d57a4ce0738551210cfa52.
N4 analytic target SHA256: 09eb56c9dba07160e4c4f276bbce38a47e6f04a1367453a9ef93abfa6dd39bb2.
Independent proof SHA256: 45f25901245d614b0cd1bea5b3d9c8565845e0b22e54d1e4545f076ff2d077ee.
N4 arithmetic target SHA256: 90863d0bef7fd1a42217d98709ce711e72fa8bed5a7afe97f3a0016cc3e8e277.
Independent code SHA256: 11730e9e2e546dddc9886efebe2ed982877d2d778db3da2293c25ec9763b5cc0.
Independent output SHA256: d90464c61f46adcc76cf467a9aa6f7b9c419c0371766113ec3bad11badc4a662.

## T4-037: Independent exact-generator point witnesses for candidates002 and003

Date: 2026-10-28T22:14:52Z.
Claim: The new seven- and eight-branch candidates violate the necessary pointwise correction inequality for each listed small correction ball.
Method: Start from the immutable original generator JSON, convert the shifted Legendre polynomials by the closed Rodrigues coefficient formula, and check every canonical coefficient against N4's separate recurrence conversion. Construct rho through the polar Laplacian, the stream through two polar derivatives, and all point fields by exact polynomial evaluation and Arb1024 powers. No candidate-producing or N4 evaluator code is imported. Apply the independently audited point inequality.
Result and verdict: CONFIRMED for both sets of eight field intervals and all prior listed point-ball gaps. Candidate002 has F(3/7,3/16)=-465.8797175915476163031; candidate003 has F(3/7,15/32)=95.72476096329597434711. Each is excluded from A2-Db, the rebalanced, sharp, original T4-019 and specified graded balls. The candidate002 sharp-ball combination is newly computed here from the independently reproduced fields and audited formula; its arithmetic output is separately identified. These exclusions need no sufficient inverse hypotheses and are restricted to the listed chart and balls.
Independent proof SHA256: c6cfee446c85c0e0091fdc16f6127b6c96ae4b5536d56a6b57279044a20b991d.
Independent code SHA256: c1e875277a06209250adf5c838a20112a241bce43528f6b6fd14daee48f9cb38.
C1-N1-002-7branch-frf: source 74f3b4cbcb3cb83289f518ce25e27a54273959dc78f637b6b9e12efb41c8669b; N4 point target e5954d123b88bba44aee62956199845966b00125a3f00c2154b7495c48a31d3f; independent output 2aad2373b859749d5a16901b42e257f58097c5953d1fd1ad882b3fdfb438f644; actual elapsed seconds 2.8170012240298092.
C1-N1-003-8branch-frf: source a4814f4b93aa4904a67fa773ca11ef84bf050971b1f5ea2ca62eeab5b9952ee3; N4 point target 2173fc8b100e11df9134eff78a9d8c2a49108d1a31d36491a85571e0aceba13d; independent output 81b5b938c6b05a3bd2a0043ca12aadb23997c710b1458008eac746700d0c81f4; actual elapsed seconds 5.773061383049935.

## T4-038: Candidate004 independent point exclusion

Date: 2026-10-28T22:22:06Z.
Claim: Candidate C1-N1-004-4branch-l2fw violates the five listed necessary correction-ball bounds.
Method: The same independent exact Rodrigues conversion and polar field construction as T4-037, starting from the original immutable generator JSON. All canonical coefficients agree exactly with N4's separate conversion.
Result and verdict: CONFIRMED. F(3/7,3/16)=-4.3600728164101006668231823. All eight field intervals and five point-gap intervals overlap the N4 targets. The baseline, rebalanced, sharp, original T4-019 and specified T4 graded balls are excluded, without assuming any sufficient inverse hypotheses. Actual computation 0.3981466367840767 seconds.
Source SHA256: 898981d8e2e86fd31a0373cd102afcef8295e2c90e62ebe5bc3a3de34031b528.
N4 canonical SHA256: 5390e3f78b03c12b04773d37a3067ef89ef9a2b9c9d52ae10325d36da71f6154.
N4 point target SHA256: 0b083bad5e555c62dbf89c5c757862b4c367bcd693cbfad758d372241ff3a7d6.
Independent code SHA256: c1e875277a06209250adf5c838a20112a241bce43528f6b6fd14daee48f9cb38.
Independent output SHA256: afe2f10018f62acc768986b6af2255bf72d73fdbf7d70f27f01ee82ff071a8b5.

## T4-039: Graded L2 transfer, printed boxes and elementary lemmas in theory_v01

Date: 2026-10-28T22:22:06Z.
Claim: FW-T-TB-gradedL2-v1 is a valid conditional closure theorem; its printed box and the printed four-component graded instance(i) are sufficient; comparisons(G-a)-(G-c) and finite-rank lemma L4 are correct.
Method: Independently derive the three component inequalities and an auxiliary positive energy, verify maximal-domain consistency and the L2 contraction, and check exact printed decimal boxes with Arb512. Derive the norm inequalities from scalar concavity and prove L4 by an explicit right inverse and the finite-rank alternative.
Result and verdict: CONFIRMED under the complete background hypotheses of T4-019 and the explicit domain and boundedness hypotheses on L4 in audit record theory_v01_audit, proof. Both printed boxes pass. The gradedL2 contraction is below0.006533456. This does not claim the scalar T4-019 high decay at the larger graded box; the separate auxiliary energy is necessary. No candidate closure follows.
Theory target SHA256: 47ba2ee70a6bfc7f939ca6fd661462d9b2a6988f47e7e545a6e433fd6e5eacb5.
Independent proof SHA256: f911e94471c46c2547ea837d45ab775a6f8b57cc152adecc7ac6986fc4d2c6de.
Independent box code SHA256: 15f394ce8cca1859cee6f103f73f4c2bce0dfa60b2a0a6be902830fb46ecf6ff.
Independent box output SHA256: 736f3c44ac67a37d5aac136f5ab15c5ae2a2f3787df2a58a94fd045025148d6e.

## T4-040: Six-branch cutoffs and scope of theory_v01

Date: 2026-10-28T22:22:06Z.
Claim: The A2 P33 finite-family H lower bound excludes the listed sufficient thresholds through K=3675,1315,1021,1063,511 respectively.
Method: Freeze the exact A2 family statement. Independently multiply positive integer distance ratios in Arb512, assemble the angular factor from exact stationary coefficients and check both adjacent K values. This differs from T1's logarithmic-sum arithmetic. Strict monotonicity extends each cutoff to all smaller admissible K.
Result and verdict: CONFIRMED for precisely the A2 six-branch family stated in Section6 of the independent proof, with the exact printed graded phi_H. The next K is only inconclusive. The broad claim that H always binds away from the origin is REFUTED as a norm statement by annular oscillations. Claims that decaying residuals never benefit from weights, or that no inverse improvement can provide the missing factor, remain OPEN as universal claims and should be phrased as planning judgments about current candidates and estimates.
Theory target SHA256: 47ba2ee70a6bfc7f939ca6fd661462d9b2a6988f47e7e545a6e433fd6e5eacb5.
A2 theorem excerpt SHA256: 4f9c719cdde2149273d446ca2909574958d306a6af3353aa4c7d89e1bc04a007.
Independent code SHA256: 6d069f7c283a6e7319331c4a1e1bdd4981961cf9f6c5caf65059129c0b2be0bd.
Independent output SHA256: 8b564699ee93dc8fe44abb0ff511dbb72aabeefd098b7ee96f4bbdc9f67f124e.

## T4-041: Weighted signed compact remainder on the odd subspace

Date: 2026-10-28T22:29:28Z.
Claim: For 0<a<2 and a C1 even coefficient A with |A(RX)|<=C0<X>^-delta and |R DA(RX)|<=C1<X>^(-1-delta), delta>0, the symmetric difference of the weighted and unweighted canonical coupling is Hilbert-Schmidt on odd L2, with the exact kernel and finite bound in audit record weighted_signed_compact, proof. Combining it with a scalar Riesz double commutator gives the local principal bound b_R+(|D rho|-rho_y)/2 and a conditional finite-rank low inverse test.
Method: Derive the angular Beurling blocks, retain the contact term, prove second-order near-diagonal cancellation and odd far cancellation, integrate the kernel majorants, and derive the principal matrix and generator realization. A separate floating grid explores the local principal bound for state131.
Result and verdict: CONFIRMED as a T4 self-audit; campaign status CLAIMED pending independent Opus review. The exact proof gives a conditional low-space theorem only. No certified finite-rank approximation, positive global energy gap or weighted high-space closure is claimed. The grid is FLOAT and took3.156791909 seconds.
Proof SHA256: 1eeb2c06da28a942c19dea488e10bb4e06bbcb1ef458a5bb7c2b0dcaf87be4d1.
Screen code SHA256: 64e21159b1ba2da5620c201e1e1106696569fcb7ee83635eb7817bc7b84ef9ef.
Screen output SHA256: 3727f84e722a66807cbe557ad464336a07542cdcd516c670bbcb9762a584460a.

## T4-042: Sharpened L2 frameworks, raw conversion and weak necessary test

Date: 2026-10-28T22:34:31Z.
Claim: T2-R3 and its two parameter boxes give valid conditional closure theorems; the raw-norm conversion and weak necessary test in the same note are valid.
Method: Independently derive the weight scaling, remove the H energy cross-term, check maximal-domain consistency and normalized contraction, and certify the constants by rational LDU and a separate rational Gamma enclosure. Derive the raw conversion by Hilbert-valued interpolation and the weak test by integration by parts. Independently recompute the printed point gaps with Arb512.
Result and verdict: CONFIRMED under the full hypotheses in audit record sharp_l2_audit, proof. The two smooth constants401 and397 and thresholds76219/10^9 and4207/(2*10^7) pass. The exact rational smooth maxima are below400.997003 and396.663266. The weak inequality needs no inverse hypothesis. Corrections to the target: the Gram relation is a lower inequality, not equality; the velocity symbol has both signs reversed but its modulus is unchanged; component projections must use exact fractions or safe roundings; a finite FLOAT weight scan does not prove a universal3e-7 limit.
Target SHA256: 46f927a1c12188a7b0b234572ad5ff89e068848ec1f996676f3e6473a0419e3e.
Independent proof SHA256: 8ca3bb460727294595087e114935f564bff5605b00b5432c59cfc1bb0ecd6734.
Independent rational code SHA256: 5db45f65ad42450c507dbd7ac05cb9be09e74cf6a02b54a59b6bf7681ab08b64.
Independent rational output SHA256: 17bc104ef592f272662a48c88abf7cac6e859342922665142d097b3fd5404281.
Point and floor code SHA256: 4fa78ae0b2e819b3ce417798a522b874350fc67b3cf13f040f40d8516305c1fb.
Point and floor output SHA256: 3783ed1b135a7e8dee98a5314d9739d1f7d3615e4ef48b4e04e9fad77e8ae215.

## T4-043: B4 finite-family cutoffs for the new L2 boxes

Date: 2026-10-28T22:34:31Z.
Claim: Under the exact T4-025 four-branch finite-family hypotheses, the full-residual L2 floor exceeds the sharp and sharpw thresholds through K=6886 and K=5814 respectively.
Method: Use X_(s,w)(F)>=sqrt(w2)||F||_2 without a fractional comparison loss. Form the fixed coefficient energy from exact rational data and multiply positive integer distance ratios directly in Arb512. Check both adjacent degrees and strict monotonicity.
Result and verdict: CONFIRMED as a local validated calculation from the audited family theorem; independent cross-lane reproduction of these new numerical cutoffs is pending. The last ratios are1.0001635497952092 and1.0003077288791668; the next ratios are0.9998870850571503 and0.9999802741479729. The following degree is inconclusive, not feasible. This computation and the point checks took0.887288483 seconds. Exact scope and proof: audit/theory_audit/research_code/sharp_l2_audit/verification/FAMILY_SCOPE.md, SHA256 f5fe6153feb8d73ce1aaa7f52137e1aa5ecad41810f85647e4876d3e67d0b237.

## T4-044: Global weak residual test and sharp-ball exclusion of d2

Date: 2026-10-28T22:40:06Z.
Claim: N4's phi_p=y/(1+r^2)^p weak test is valid; its d2 integrals exclude both new sharp L2 balls and the three other printed balls.
Method: Independently prove cutoff removal and the necessary inequality, then reconstruct the canonical density and stream function over the rationals. Compute the signed pairing directly from the weak background equation rather than the cached residual; compute the norms from polar vector components. Compare Arb1024 intervals.
Result and verdict: CONFIRMED. All 63 interval comparisons agree; all15 gaps are positive. The p=2 pairing is -0.028802081112908754894682696. Sharp and sharpw gaps exceed0.028786869139892300 and0.028788094379832049. This is an actual exclusion of the specified fixed-c correction balls, independent of any sufficient inverse hypotheses. Actual reproduction 27.250916950 seconds.
Independent proof SHA256: fe4bacf4d0b6c9e3c710b19757a7d6044b2ffd7e4870710a29943cc072d3288d.
Frozen N4 proof SHA256: ff7cf55786fb213c4c2f978b87136668b58733919c80ad7f443bca6df3419b85.
Frozen N4 output SHA256: 80a7e6d9a398296a32d5cf96b4fe66a4092316293c73ef7544c4269f5a8c2971.
Independent code SHA256: ef1e4885c3e2c35a6957219a2c1ed7bba1b8dac34df2a19ec689cfa977121ecb.
Independent output SHA256: b7af4f692a326bc803325e7cff99d8f79eb2233052608a170e4b6ec31eb3c2ff.

## T4-045: Independent Opus review of the regularized weighted low inverse

Date: 2026-10-28T22:40:06Z.
Claim: T4-022's weighted velocity commutator and conditional low-space inverse theorem have passed complete independent review.
Method: Read and freeze T2's full review, which separately checks the Beurling identity, Volterra blocks, real-pair constants, weighted energy, canonical generator and membership. Its independent Sympy/Arb script reproduces the exact parameter box. Check the reviewed proof hash against the original.
Result and verdict: CONFIRMED; T4-022 is now AUDITED as a conditional low-space theorem. The original proof remains unchanged, SHA256 e9e72abe2aa0f5274c461ff9f9c34b50a7269416e32cc264020b1209949c2aed. The checked rate is beta_R>0.02181481 for a=221/200,R=2^29; the perturbed rate at the printed cap is >0.01739481. No weighted high-space estimate, invariant ball or existence claim is supplied by this review. T2's optional sharper constants and planning remarks are separate from this promotion.
Independent review SHA256: d7856b22ed676d6bfc3e1fe80ff18ff013a9550b8af72deadba3d31b758c2deb.
Independent script SHA256: 66dd6c4b5833e0ec27d4daaf7579ef1a8c0a7a488b208cdb9655344637637103.
Independent log SHA256: 4b2a173dda4554b917500da4a74f6aa5db0093caed0c954fb224e270502bb25a.

## 2026-10-28T22:40:06Z: T4-043 cutoff values independently reproduced

N4's separate gamma-ratio evaluation and direct-product cross-check reproduce the last and next ratios for both sharp boxes:6886/6887 and5814/5815. The frozen output is audit/theory_audit/research_code/sharp_l2_audit/source/N4_T2_R3.json, SHA256 c668131558966a6f03cca074bb52753450fd4f793ca13ae57b1eeaea1e162733; its code is source/N4_sharp.py, SHA256 3ba9f4b266f799f69cf592fd4ffe87bced69dd2e4731c6f96a7ad6e24acfd515. I read the full implementation; it uses the direct G0 bound and the same exact family. Together with T4's prior independent product calculation, the four numerical ratios and cutoff values are now CONFIRMED cross-lane. The next degree remains inconclusive.

## T4-046: Independent signed-condition witnesses for candidates002,003,004

Date: 2026-10-28T22:41:16Z.
Claim: At the three selected rational points, each exact candidate has theta_X>c-1 and therefore fails c+1-theta-kappa>=2 for every kappa>=0.
Method: Use the exact canonical coefficients already verified against original generator JSON in T4-037/038, independently construct the polar density, differentiate its rational radial polynomials and evaluate in Arb1024. Compare the selected point and failure-gap intervals with N4.
Result and verdict: CONFIRMED for the three selected witnesses. This disproves the stated sufficient signed condition; it is not a nonexistence result or an obstruction to every possible inverse estimate. No global supremum upper bound is inferred from the scan.
Proof SHA256: 3772c4f931385151d82f88e87ffd04fb5f367c4fd3de014f3d47a069380cbdb8.
Code SHA256: b46dc4c8f04aef5070b6d638362d48252984481733328919de0eb18aea5434b6.
C1-N1-002-7branch-frf, point ['1/2', '1/2']: theta [47.59321873748298720018734808825370510686059931999999480180410542543730827093546983002418084209172251 +/- 1.99e-99], failure gap [46.78289952728298911454541109258257439005990962273436980180410542543730827093546983002418084209172251 +/- 1.99e-99]. Target SHA256 5cce3a8dfffa1535b6c6a4cdde46a44db6c405943fa37af1b756df6759534dbd; output SHA256 fca03b7f158ea93523a77695d3b840983bf82b9b03ee2027c31c5b859a6eda1f; actual runtime 1.856925391s.

C1-N1-003-8branch-frf, point ['1/2', '1/8']: theta [30.90569043774492956016668543288042976546622605515207477739018309746749535979595157240535466058121471 +/- 6.36e-100], failure gap [30.09537122754493147452474843720929904866553635788644977739018309746749535979595157240535466058121471 +/- 6.36e-100]. Target SHA256 5ad400f30b3b9b715237f3c244d5c8b8ed56d318f7c2cae460dce26c9455ad77; output SHA256 b9e9588e94e4c55c937aefcb9bd2b0f75db17c73b9a8e0465af66ecc8c7a32de; actual runtime 2.887799415s.

C1-N1-004-4branch-l2fw, point ['1/4', '4']: theta [0.8799401611337266987113532657664103259416101872206049525528115368395000993686424777626753018990414494 +/- 4.70e-101], failure gap [0.06962095093372861306941627009527960914092048995497995255281153683950009936864247776267530189904144945 +/- 3.02e-102]. Target SHA256 574a2f879b1138e85be3b00b6c0fb8d1a114cbb0e7bc171e0a3ed5b309aff68a; output SHA256 d6dccc5be32589df02ade4b6efdb58bea734c8c8e0388eca25e866f8d65bb8be; actual runtime 0.195980114s.

## T4-047: Principal energy obstruction survives compact repairs

Date: 2026-10-28T22:44:25Z.
Claim: Under the signed compact decomposition, any contractive L2(w^2) energy estimate after a compact additive correction has decay rate beta<=c+1-ess sup[b+(|D rho|-rho_y)/2]. This remains necessary in the exact zero-strain subspace.
Method: Construct localized real high-frequency S1 packets, use Fourier translation for the Riesz multipliers, remove finitely many normalization constraints by small fixed smooth corrections, and use compactness on weakly null packets. Independently evaluate seven rational state131 points with exact polar coefficients and Arb1024.
Result and verdict: CONFIRMED as a T4 self-audit; campaign status CLAIMED pending independent Opus review and numerical reproduction. The theorem rules out a positive contraction rate for the seven listed (a,R) pairs, for example a=13/10,R=1 at(5,0) has excess>0.07236305588, and a=7/5,R=4 at(23,0) has excess>0.01767413630. It does not rule out invertibility or a semigroup bound with prefactor greater than one. Applied to the already confirmed unweighted witnesses, rate2 cannot be rescued by a compact remainder calculation for candidates002,003,004. For002/003 every positive unweighted contractive rate is obstructed by these points.
Proof SHA256: e603f56231021a78d5f89751f316c9fa5afb34f9ff0cc21a1d3051630e64a3e7.
Code SHA256: 39d864b1abff9de5d6035ec9d8c6ad8f9ece471d03c73ede2461d266752cb800.
Point output SHA256: a7e63cc67d1f1b1903e23e21afa79ed5e9d46400abd0e893597ca10792e4fc70.
Actual numerical elapsed seconds: 0.031956136.

## T4-048: Gradient-free necessary L2 distance from d2

Date: 2026-10-28T22:48:01+00:00.
Claim: N4's pure-L2 weak test applies to all distributional divergence-form corrections, without a gradient cap; its d2 values exclude radius27/10000.
Method: Independently check the weak divergence equation, L1 nonlinear product, cutoff removal and the exact gradient bound. Evaluate the positive quadratic root from the separately confirmed T4-044 weak integrals in Arb512, without using N4's postprocessor.
Result and verdict: CONFIRMED for the analytic N4 theorem and input integrals. The independently computed necessary radius is >0.00271973702015789175, with strict gap >0.00020906881288969583 at radius0.0027. New numerical root arithmetic remains pending independent reproduction. A T4 improvement |grad phi|<=3u^2 lowers D to9.62347033613611 and raises the radius to0.00299196944823650895; this added improvement is CLAIMED pending review. Both are fixed-c distance bounds, not general nonexistence.
Proof SHA256: 5d24bd24c49e8c97b2311d00b57e12117d71e2ca82c1fc49293296fd103d8367.
Frozen N4 proof SHA256: 2069cd76cf72aba7b5d127a9746935e4462163f8f7c593cb842cc7d51fa80afb.
Code SHA256: df87c656febfc4d8753dd14c445723bfa39d0c0881ff22274a97f2c6f6c16c39.
Output SHA256: 3e9bb0c908568b3b1042f0625a7d9ae7cca9b72f60896385de419fb01c78f5ed.
Actual arithmetic elapsed seconds: 0.001890811137855053.

## T4-049: Annular L2 affine-class obstruction and exponent rigidity

Date: 2026-10-28T22:48:01+00:00.
Claim: N4-055 excludes every bounded-gradient L2 correction when a nonzero uniform leading residual has exponent q>=-1, and fixes c in the stated affine class.
Method: Independently test the divergence-form equation against R^-1 psi(X/R), retain annular L2 tails, and compare with the nonzero leading moment. Check the endpoint q=-1 and the changed-c leading term.
Result and verdict: CONFIRMED for the exact N4 hypotheses. No additional numerical inference is needed. The same proof with the nonlinear term integrated by parts removes the bounded-gradient hypothesis and applies to all L2 divergence-form corrections; this strengthened T4 version is CLAIMED pending independent review. It does not exclude non-L2 tail repairs or weighted affine spaces.
Proof SHA256: ebf243859dc4e104c71f7414a95e9e38001be51ca65efe3e9abcb5e21f0ffcd4.
Frozen N4 proof SHA256: 6623683d3283a5ff72895130740601b1ffdb9464b7a95579c7eac3286a329192.

## T4-050: Audit of the TM-17b high-low transfer

Date: 2026-10-28T22:51:28+00:00.
Claim: A stationary L2 Woodbury inverse bound can directly replace condition(B) in the existing T4-019 high-norm theorem.
Method: Read the frozen T1 transfer matrix, TM-17b and Section3.2, and trace every use of T4-019 equation(7) through its proof.
Result and verdict: REFUTED as a direct substitution in that proof. The signed low term supplies 2w2 b^2 in the high Gram matrix in Section3, so the proof needs more than ||A_k^-1||<=1/2. This does not refute the stationary Woodbury lemma, which is independently confirmed in T4-039, and does not establish that all resolvent-based replacements fail. The T1 text correctly leaves this transfer open. A separate route is T4-051.
Frozen transfer matrix SHA256: 0033dd5e1514ddd27ac84a8cf0e55f2e1ef69fa6040b7d10d46c16101a3c8c6e.
Audit and replacement proof SHA256: 85a6f3eecbf3388e9f793da5af1c536f9f0f2df39a28a1e6c0419ff89e88617a.

## T4-051: Conditional closure allowing transient low growth

Date: 2026-10-28T22:51:28+00:00.
Claim: Under(A),(C),(D) of the standalone proof and the uniform low semigroup bound ||exp(tA_k)||<=2exp(-t) on the normalized X_s ball, s=2^-17,R=2^-14, the sufficient residual threshold is X_s(F)<=1/196608.
Method: Prove ||J^s h||2<=||h||2+s||DJ^s h||2; use it to derive triangular gradient and Hessian decay from the low semigroup, then establish maximal high domains and a stationary component inverse. Check the scalar parameters with Arb512 and close the normalized L2 contraction.
Result and verdict: CONFIRMED as a T4 self-audit; campaign status CLAIMED pending independent Opus review. The high inverse constant is <11.490384<12 and the contraction is <0.012467. The low semigroup bound is a new explicit uniform hypothesis, not supplied by a stationary Woodbury certificate, and has not been verified for a candidate. This is a conditional framework, not an existence certificate.
Proof SHA256: 85a6f3eecbf3388e9f793da5af1c536f9f0f2df39a28a1e6c0419ff89e88617a.
Code SHA256: 13dba1bacb14babb7967c7224b738e66f01868bf3616c741cebf2cf15d8782e0.
Output SHA256: f6ae625bd86178dbcb880144ba9641f15dafb1a6091964fa52f57a2939bfccba.
Actual parameter arithmetic elapsed seconds: 0.0007806820794939995.

## T4-052: Independent confirmations of the weighted theorem and L2 obstructions

Date: 2026-10-28T22:58:00.631698+00:00.
Claim: T4-041 is an audited conditional low-space theorem; the sharper analytic inequality of T4-048 and weaker-regularity theorem of T4-049 are independently confirmed.
Method: Read the complete independent reviews, verify exact target hashes, freeze them beside their proofs, and retain the unchanged reviewed proof versions.
Result and verdict: CONFIRMED. T1 R1-008 confirms all six sections of T4-041 and its precise low-space scope. N4 confirms the A+3B+C bound in T4-048 and the full distributional L2 annular theorem in T4-049. The improved scalar root comparison is separate and pending. No candidate existence theorem is closed.
T4-041: proof SHA256 1eeb2c06da28a942c19dea488e10bb4e06bbcb1ef458a5bb7c2b0dcaf87be4d1; review SHA256 12d94d0e00e165d3296aa7b524af4afdf4249fdb3851f28f13870c4589a033d3; audit/theory_audit/research_code/weighted_signed_compact/REVIEW_STATUS.md.
T4-048: proof SHA256 5d24bd24c49e8c97b2311d00b57e12117d71e2ca82c1fc49293296fd103d8367; review SHA256 5bdb3fa6e3855762f138729b9d50033452c34c36c7a12af531e27bf1ccf9df5b; audit/theory_audit/research_code/pure_l2_probe_audit/REVIEW_STATUS.md.
T4-049: proof SHA256 ebf243859dc4e104c71f7414a95e9e38001be51ca65efe3e9abcb5e21f0ffcd4; review SHA256 8edb3e3562299df5c7acc28666c798763015d276968d36382bef5d99568a2bff; audit/theory_audit/research_code/affine_l2_audit/REVIEW_STATUS.md.

## T4-053: Independent global d2 signed L2 certificate

Date: 2026-10-28T23:00:42.082854+00:00.
Claim: N4's full-plane bound theta=(|grad rho|-rho_y)/2<=2/25 for exact d2 and the resulting signed low rate above2.0199.
Method: Independently reconstruct the gradient from the polar density, compare all rational coefficients with N4's fourth-derivative representation, then cover the compactified (t,z) rectangle using a different degree8 correlated Bernstein enclosure and a scalar Schur determinant test. Independently check the complete binary partition.
Result and verdict: CONFIRMED. All120 final closed cells pass;38 refinements were needed from N4's82-leaf partition. Minimum computed Schur lower margin is [0.0003115684680141801600500795266950160196626422239507244159923249620930099 +/- 1.15e-74]. Combining with the independently confirmed Hilbert-Schmidt norm gives c+1-2/25-kappa=[2.01990807272009049211943247773102799156820182670436841441899576431 +/- 3.21e-66]>2.0199. This confirms only condition(B-L2), not residual smallness, the other matrix conditions, or existence. Actual cover runtime 291.7316093631089 seconds; postprocessing 0.0041972273029387 seconds.
N4 target cover SHA256: d38216945b06233cbb4ea26cb2e409a23e04004797dd1f3241859727ef4bbfd8.
N4 target proof SHA256: 608a9cd7fd61b99795d1050b49c709b37040dcc21aa0735f407cf6b79c6dc686.
Independent proof SHA256: d06d43d491c800c808ed1296996c9393b98dcd50ba55cdc459279cbae02e171c.
Independent cover code SHA256: 78f6a526cd69e84a155125c01572e527084fbb12c66430bc23a7aa89308dbbae.
Independent cover output SHA256: c05b0867a8ec7f8a38f100a96e7c42bbae81d09a4dd964739352d79c26db9ec3.
Summary SHA256: 39b1781f7677e62f7bf7264fec7dd4e6d43493e13473729ed37752858564d5fd.

## T4-054: Sharp weighted odd Beurling bound

Date: 2026-10-28T23:00:42.082854+00:00.
Claim: For w_R=(1+r^2/R^2)^(-a/2),0<a<2, the complex odd weighted Beurling norm is exactly(2+a)/(2-a), and the real odd IPM velocity norm is at most2/(2-a).
Method: On the future angular block, write F=-H'+(n-p)H, G=-H'-(n+p)H, where0<=p<=a, and complete the positive square in equation(9). On every past block, ||F||^2-||G||^2=4k integral p|H|^2. Prove sharpness by annular packets escaping to infinity; verify the algebra independently with symbolic coefficient identities.
Result and verdict: CONFIRMED as a T4 self-audit; campaign status CLAIMED pending independent Opus review. The new velocity constant is5/2 at a=6/5 and10/3 at a=7/5. The same upper bound holds for locally absolutely continuous radial weights with logarithmic slope in[0,a]. The exact norm claim concerns the complex odd Beurling operator; no optimal real S1 velocity norm is asserted. This improves only an operator constant in T4-041, with no new high-space or existence conclusion.
Proof SHA256: 5c3bdfe1c4b7c203f3cf9b361f16cd938589b38487bd197a59b40af2c6473f32.
Symbolic code SHA256: 8402b2e8f62d600aeff3a4e5aa53e98f5b7a1f6daa1e704d8d0ec24565c71927.
Output SHA256: 9621da11975ff70fb680e6fce3b9425c57501b4a7266d4c1f97a8daa261f29dd.
Actual symbolic runtime: 0.05958682904019952 seconds.

## T4-055: New sharp-ball point gaps and d2 assembled residual norms

Date: 2026-10-28T23:04:13.372116+00:00.
Claim: Candidates002,003,004 are outside both new T2-R3 correction balls; N4's two assembled d2 X intervals and threshold ratios agree with independent interval postprocessing.
Method: Use T4's independently reconstructed, cross-confirmed Cartesian point fields in the general necessary Sobolev point test. Separately apply the audited fractional comparison to the four independently confirmed raw d2 components, evaluating its upper bound in the equivalent factored form E[2Q^2/E^2+Cw]^(s/2)+(48s/25)E.
Result and verdict: CONFIRMED. All six point gaps are strictly positive. The sharp d2 lower bound is2557.7512812172563 and its threshold ratio exceeds3.3557922e7. The sharpw lower bound is5111.9855285715822 and its ratio exceeds2.4302284e7. Full intervals overlap N4. No candidate existence is inferred from a sufficient-test failure or a point exclusion.
Proof SHA256: 17fc8ba16a276216ccd4f573870d3625d9621d4992a88bdbda7aad325e729229.
Code SHA256: 95ee467e994e2fbf3d70213b184d7b9dd55e98b9bbd5299c8cff8c2820b4845d.
Output SHA256: 2d6c9c2f20d6a0b675afe6d6c8f42ffab2f3d0fb51d93e4f8cb9d3bb672b2098.
N4 comparison target SHA256: c668131558966a6f03cca074bb52753450fd4f793ca13ae57b1eeaea1e162733.
Actual postprocessing elapsed seconds: 0.02392629161477089.

## T4-056: Exterior-tail review and optimal extension audit

Date: 2026-10-28T23:05:51.246061+00:00.
Claim: T4-014 is independently audited; T2's new Remark R1 gives the exact minimum over all Hdot^-1 extensions and Remark R4 gives the weighted per-mode remainder bound.
Method: Freeze the complete T2 review and verify its target hash. Independently construct the exterior Dirichlet potential, compute its boundary measure with the correct polar normalization, and use Hilbert-space orthogonality. Check the per-mode dual test and prove an explicit L2 shell approximation.
Result and verdict: CONFIRMED for T4-014 and T2 Remarks R1 and R4. The minimum K is attained uniquely by the exterior density plus the negative boundary layer. Mere L2 membership does not increase the infimum: the shell approximation converges at rate at most sqrt(2T epsilon)||mu||L2(theta) in Hdot^-1. This last quantitative estimate is a new T4 addition, CLAIMED pending independent review. T2 Remark R3 numerical tables remain separately unreviewed here. The result supplies no onset or remainder certificate for a candidate.
Original T4 proof SHA256: 8f3d5dff89092fac93c17fba4eb7922642ec03c8bd2db07c0aae85df6e6730e5.
T2 review SHA256: d1bb584cd61ef6fad0234755a53f0788e93b1835c0c5e0ee9e4e7030d3f54bd7.
Independent extension proof SHA256: 69ceadd607c169170ce64227383f7f74250cc5ae2d175fbe71ea67940135cba8.

## T4-057: Independent review and repaired rough passage for T4-051

Date: 2026-10-28T23:14:18.925097+00:00.
Claim: The transient low-semigroup framework is an audited conditional theorem at its original constants.
Method: Read T1 R1-009 in full, match its exact target, freeze its independent arithmetic, and implement its two proof repairs in a separate addendum. Use an equivalent finite-time energy with raw b, and pass only final inverse norm bounds through normalized smooth approximants.
Result and verdict: CONFIRMED, with the addendum included. Campaign status AUDITED conditional. The original K_X<11.490384<12 and contraction<0.012467 agree with T1's independent calculations. The unrelaxed component products need not be weakly upper semicontinuous; the repaired proof avoids passing them. No candidate satisfies all hypotheses yet.
Original proof SHA256: 85a6f3eecbf3388e9f793da5af1c536f9f0f2df39a28a1e6c0419ff89e88617a.
Addendum SHA256: 932645e00e52f479b0d8c1779a12f54f7fa68c2dfc5cda70c6037539b118b946.
T1 review SHA256: db32450dc0311a104f445483cf5b17dde35e6b3d68ec793f7ba2a57b58911f4e.
T1 code SHA256: 256175f0b57999800e9afaacdb439e8918e4aea561d43bed1907e11ee922c0d6.
T1 output SHA256: 24f9c7fde5fcda178cf8d5b2cbd6d1c4fd4d5c89a3cf8d948c5e801f5a680335.

## T4-058: Scale-adapted weighted high space

Date: 2026-10-28T23:14:18.925097+00:00.
Claim: The explicitly defined dyadic density-velocity graph norm supplies a globally bounded gradient, a continuous strain trace, a complete normalized ball in weighted L2, and a conditional nonlinear closure under the uniform high resolvent hypothesis(H). An ordinary fixed-scale decreasing-weight Sobolev norm cannot supply the required gradient embedding.
Method: Local Fourier embedding on rescaled annuli, a closed Hilbert graph argument, the weighted low inverse, and a translated four-packet counterexample with exact strain removal.
Result and verdict: CONFIRMED as a T4 self-audit; campaign status CLAIMED pending Opus review. The proposed space is compatible with growing subleading corrections and preserves a leading r^gamma profile when a-1<gamma. The high resolvent estimate(H), its numerical constant and the forcing bound are explicitly OPEN. This is a functional setting and conditional theorem, not a verified new candidate.
Proof SHA256: 906111ef2e54596ca432cf6513b13318dbdba9cb8f766cb784cb8e08d660d365.
No numerical computation was used.

## T4-059: Audit of T1's positive-real resolvent continuation

Date: 2026-10-28T23:14:18.925097+00:00.
Claim: T1 TP-1 transfers the low positive-real resolvent hypothesis(L0) to a high inverse; TP-1b reduces(L0) to finite-rank certificates.
Method: Reprove a priori high estimates on the generator domain, continue high invertibility using the resolvent identity and local low resolvent boundedness, pass rough inverses by normalized smooth approximation, and derive the finite-rank perturbation formula with all norm factors.
Result and verdict: CONFIRMED for TP-1, its Woodbury formula and the matrix perturbation bound. OPEN for TP-1b's claimed automatic high control unless the additional condition alpha'=m1-s(q+d1)>0 is supplied, or the columns receive another high regularity certificate. Finite rank and psi_j in X_s alone do not imply this positivity. The explicit low inverse bound must also be evaluated from the finite-matrix margin. No numerical matrix certificate is provided.
T1 source SHA256: db32450dc0311a104f445483cf5b17dde35e6b3d68ec793f7ba2a57b58911f4e.
Independent audit proof SHA256: daa55c5868d689186fbe67b7afc5bea1f85b7bb27d82b97ef0830c8695e89d02.

## T4-060: Origin restriction on contractive high energies

Date: 2026-10-28T23:18:34.907636+00:00.
Claim: A normalized S1 reference with partial_y V_y(0)=1 can satisfy Re<Lh,h>Hq<=-beta||h||Hq^2 on normalized tests only if beta<=c+1-q. The same condition holds for the specified dyadic graph norm under the stated background decay.
Method: Use vertical high-frequency packets supported away from, and then tending to, the origin. Expand the Sobolev multiplier through its first subleading term, retain q partial_y V_y in the transport energy, show the velocity multiplier vanishes in the vertical direction, and remove the strain by a rapidly vanishing fixed correction.
Result and verdict: CONFIRMED as a T4 self-audit; campaign status CLAIMED pending Opus review. The ordinary H^3 energy has limiting positive growth 2-c>3/20 for the case4 range. A positive H^(2+s) contractive gap requires s<c-1. This does not rule out a transient semigroup bound, a stationary inverse or an adapted equivalent norm.
Proof SHA256: 1e59a48b5d024a73ab47042cad5e6104dbc45b007874111a3ab571c37a0baa57.
No numerical computation was used.

## T4-061: Independent complete first-derivative matrix cover

Date: 2026-10-28T23:24:46.318352+00:00.
Claim: The exact d2 reference satisfies M1>=9/10 I everywhere on the plane, as in N4-056.
Method: Reconstruct velocity derivatives from the polar stream function, compare every coefficient with N4's fourth-potential derivative arrays, and bound the two diagonals and determinant by independent correlated Bernstein enclosures. Independently check exact rectangle area and all 52975 pairwise interior disjointness relations after completion.
Result and verdict: CONFIRMED. There are 326 accepted cells, 99 refinements and zero pending cells. The smallest stored determinant lower bound is greater than0.0003688578; both diagonal lower bounds are positive. This removes N4-ORIGIN from the d2 unweighted M1 condition. It does not certify other high-space hypotheses or closure.
Cover SHA256: df2a75fbd8016bb0b30852dc6d2c05173f8cd31fd9ddc885f33501c3ce5487cd.
Proof SHA256: a6ca977139a831c42dd0ea6165b0aa78dc3d21b72299fb908cb542f0aa6bc409.
Final-check SHA256: 408aa329988b64d6d32213c64861f0855016a7fc65880ad3ea84def4e711ce9d.
Actual cover time across three stages: 996.5068538472988 seconds. Final partition check: 0.4972865148447454 seconds.

## T4-062: Full independent review of the computed-defect theorem

Date: 2026-10-28T23:24:46.318352+00:00.
Claim: T4-004 sections2,3,4 have a complete independent review, including the multiplication estimate and domain argument missing from the earlier T1 review.
Method: Read T2's full review, match the unchanged original proof hash, and freeze its independent code and results. Track the reviewed scope explicitly.
Result and verdict: CONFIRMED. FW-T-T4ALT-defect-v1 is AUDITED as a conditional theorem for sections2,3,4, except the leading-tail sentence under B11, which T2 explicitly did not review. No numerical g or defect certificate has been supplied. Its total correction radius retains all baseline-gap exclusions, so the computed g does not rescue d2, Mpen2 or b6. New T2 remarks R3/R4 are being audited separately and are not covered by this promotion.
Original proof SHA256: d347071a02ea22eef12b4d209886deb0118738338d27bd8c531bcc559dbc61fa.
T2 review SHA256: f265065bf723bfb33f6bce71e32eea15a26681f89fd3b7efc01f0beb2aca43c2.
T2 independent code SHA256: ab4a028282cf100a6ebc2d5f5f2752689ab63da730d9b2bf7ebdafd8b01b20a0.
T2 independent output SHA256: eacfd6035bc8203ea720b581b23987eee3f05c1358d51b8c286e0aa4739a3f68.

## T4-063: Independent exact exterior-onset table

Date: 2026-10-28T23:24:46.318352+00:00.
Claim: T2's six-, seven- and eight-branch necessary onset values follow from the audited exterior negative-norm bound.
Method: Independently sum the exact rational sine vectors, compare all branch6 coefficients with Analysis II's separate JSON, and evaluate log10 onset directly from the squared amplitude with384-bit Arb. Compare three amplitude/sigma quantities and five onset values for each branch.
Result and verdict: CONFIRMED. Exact branch6 vector equality holds and all24 interval comparisons overlap. These onsets require an exact exterior model or a certified remainder; they do not alone rule out an asymptotic branch count.
Proof SHA256: 41cdc6c0cc0c733849f02917a983eff396629cd81bc6365bf1197e688d82fe27.
Code SHA256: 43d03296278b96ac8a28f59445847c65296cc65382da00ddefb66e6b8a95ee84.
Results SHA256: 574513d8688f55983cea218e31827fa302d9817198b448924eab8643f9620f21.
Actual arithmetic time: 1.2597747459076345 seconds.

## T4-064: Independent localized weak-probe distances

Date: 2026-10-28T23:26:03.661258+00:00.
Claim: The N4 localized weak tests imply substantial fixed-c L2 distance from d2 and Mpen2 to every exact distributional solution, without a correction-gradient bound.
Method: Reprove the weak inequality and cutoff removal. Reconstruct the polar density and stream polynomials directly from the rational potential. Compute the signed residual pairing by the background weak equation, without reading a residual cache. Evaluate every radial moment with gamma-free positive beta products and exact polynomial coefficients, using2048-bit Arb.
Result and verdict: CONFIRMED. All35 constituent interval comparisons agree with N4: d2 k=0,128,1024 and Mpen2 k=0,512. The strongest reproduced radii are d2 >=0.2955267500250031224546050894 and Mpen2 >=0.5500667532470527071305191294. Both decimal bounds are rounded down. The hypotheses are fixed c, smooth sublinear reference and an L2 distributional correction, with the divergence-form nonlinearity. No claim concerns a change of c or arbitrary distant profiles.
Proof SHA256: 4f744234c6594613748764a995282abe6f1069518d2e21bde36158c7e875f508.
Code SHA256: 155d39ddeedd9e28a6071e1dfdde8b34ef10c953da251194a4940eb581780f23.
d2 results SHA256: 81e1b306776000a281182e2ef1d2a1ca40a3dcdc921c8772a8e464cbc4bc1041.
Mpen2 results SHA256: f5a1fb0b8a2d9765a40695b00cf9133e49647a74179b467dbcf333f76b272b99.
Actual arithmetic times: d2 22.854139923118055 seconds; Mpen2 16.686446784995496 seconds.

## T4-065: T2 H-free defect extension and commutator improvement

Date: 2026-10-28T23:26:03.661258+00:00.
Claim: T2's R3 H-free defect theorem, R4 commutator replacement17 by24/5, exact scalar feasibility and universal correction-distance budgets hold with the audited T2-R3 inverses.
Method: Reconstruct the weighted three-row multiplication estimate, maximal-domain fixed-point proof and low L2 contraction; maximize the scalar quadratic and cubic exactly. Bound the gamma ratio by convexity and Jensen, and independently enclose the endpoint by Arb.
Result and verdict: CONFIRMED with notation and endpoint qualifications in audit record defect_review_audit, proof. The moment bound is4.77230396774536358<24/5 at s<=2^-10. The H-free defect extension is an AUDITED conditional theorem, not a candidate closure. T2's sentence B<beta needs m+epsilon>0; generally B<=beta. Its statement that (B-L2) fails for every current candidate is too broad, since d2 now passes that signed condition. Neither correction affects the theorem. Printed rounded tolerances and q bounds must be directed outward as appropriate; the exact rational values and interval bounds are in the certificate.
Audited T2 source SHA256: f265065bf723bfb33f6bce71e32eea15a26681f89fd3b7efc01f0beb2aca43c2.
Independent proof SHA256: 5846b59cf0dd5f216fe2d780ed584a70ac3a583fbfd3ef76c5d7d41667166e5e.
Independent results SHA256: 5c76f8b270fd9365047d06745a3ad85e161f52e710f5107669b11dac33dc6cae.
Actual scalar computation: 0.001395953819155693 seconds.

## T4-066: Independent confirmation of the exterior Green-factor error

Date: 2026-10-28T23:26:03.661258+00:00.
Claim: N4-067 identifies a missing factor two in the frozen N1 outer-outer negative-Sobolev computation.
Method: Reconstruct the radial Green function and both triangular halves, then verify the explicit potential for F=1_(r>=1)r^-4 sin(theta) by the differential equation, interface matching and exact integration.
Result and verdict: CONFIRMED for N4's diagnosis; REFUTED for the frozen N1 exterior factor. The exact synthetic norm squared is pi/12, while pi/(2n) times its ordered triangular sum gives pi/24. The correct exterior factor is pi/n. This audit neither certifies remaining quadratures nor states that the owning lane has repaired its current code.
Frozen N1 SHA256: 1c227353f2a5316154a17157f8854fad36b39aee5accd755482ee02c6ec009ee.
Independent proof SHA256: 1a23a2d47643e77a3c9d258af8276a8288b0759beadd4533ed385987b4811e68.
Independent results SHA256: 9cbe36fd8f4cc208b253f0c5cdf5ea6f93b1f9544a7cf732c8f1af1899218fd6.
Actual exact-check time: 0.41301547177135944 seconds.

## T4-067: Certified stationary matrix constants and directed tolerances

Date: 2026-10-28T23:35:43.981151+00:00.
Claim: T1's optimized stationary inverse constants give the stated sufficient residual thresholds.
Method: Reconstruct the three by three nonnegative matrix in the norm-weighted component coordinates. Certify rational operator-norm upper bounds by all three positive leading minors of K^2 I-N^T N at512-bit Arb precision; check contraction and slope inequalities separately.
Result and verdict: CONFIRMED for the matrix argument and the directed thresholds in the certificate. Two printed tolerances are rounded upward and are not certified by that argument: baseline7.9595e-6 and the K_L=1 value2.41869e-5. Safe replacements are7.959492e-6 and2.4186857e-5. The negative minor tests refute the displayed matrix certificates at those exact decimals, not the actual inverse bound or possible sharper closure. All low and high operator hypotheses remain conditional.
Proof SHA256: c10496fe17c9593f571ec5fa7ff7707a54accfe07d90bc1e1757245d51d869b5.
Code SHA256: 462f2afd6c34d7912db835a07be7e45a5551ff7e9b878f41f03ea59c7eba585d.
Results SHA256: 92afe838e5c3c40ea7430350fdd5718e814a2b05d95be1c2f7b880ad17b4f262.
Actual computation: 0.022316422313451767 seconds.

## T4-068: Independent localized distances for candidates002,003,004

Date: 2026-10-28T23:35:43.981151+00:00.
Claim: N4 localized weak probes give positive fixed-c L2 distance bounds for the three immutable candidates.
Method: Apply the independently proved T4-064 weak inequality. Reconstruct polar fields, pair through the weak background equation, and integrate by exact polynomial coefficients and gamma-free beta products at2048-bit precision. Compare all seven quantities for k=0,128,512,1024.
Result and verdict: CONFIRMED. All84 constituent comparisons overlap. Safe lower bounds are1.56361352 for002 at k=0,0.22988134 for003 at k=0, and1.40009623 for004 at k=1024. These apply to every L2 distributional correction at fixed c under the smooth sublinear reference hypotheses. No correction-gradient cap is required. They do not exclude a changed exponent or unrelated distant solutions.
C1-N1-002-7branch-frf: results SHA256 6b9e8c608729e092746ce6c9bc682333028907fef7fea22da580f14aae90c5fb; actual computation 54.066371999215335 seconds.
C1-N1-003-8branch-frf: results SHA256 c95a61be92a8dabbfd70fcaa37cf396ac3b730146ebbf5c0bf5ab58665400186; actual computation 114.09016111586243 seconds.
C1-N1-004-4branch-l2fw: results SHA256 2183dca3ac8164da8ce57bb4359c7145022bcbecebcbd57e59ae3184e5a5547d; actual computation 3.0740689379163086 seconds.

## T4-069: Remaining sharp-ball point comparisons

Date: 2026-10-28T23:35:43.981151+00:00.
Claim: N4's pointwise witnesses for the s=1/8192,r=43/50000 ball are correct, including the remaining b6 entry.
Method: Use the T4-015 independently confirmed point fields and recompute the exact pointwise upper bound with512-bit Arb. Compare upper bounds and signed gaps independently.
Result and verdict: CONFIRMED. All six comparisons overlap. The d2 gap is negative (about-0.00814480226) and this point test is inconclusive; Mpen2 has gap greater than0.0330957077 and b6 greater than2.9392836795, so both are excluded from this fixed-c ball. This completes the requested b6 comparison.
Proof SHA256: 5412dc85768719f509e33ba54f60804417d5627b9ea859c331c9320332312bb4.
Code SHA256: 2b648318e826d2a8eb6e91b92f7715e3489455444f1b057b508db676e399b7f9.
Results SHA256: 5c0ded4d2946825c9866e42e4334da9135a86b16e624efcce6f25056f1c2af66.
Actual computation: 0.0015097670257091522 seconds.

## T4-070: Uniform graded correction budget and point exclusions

Date: 2026-10-28T23:35:43.981151+00:00.
Claim: T2 Proposition G and T1's uniform graded point exclusions hold for every positive top-row budget.
Method: Maximize the exact cubic in s and use n^2=r2^2+2r1^2+r0^2. Independently recompute the three point gaps and combine the resulting L2 radius cap with T4-064.
Result and verdict: CONFIRMED. Every positive top-row budget has ||h||H^(2+s)<=n<50/(651 sqrt(28248))<25/54684<1/2000. Consequently d2 and Mpen2 are excluded from every such graded or gradedL2 box at fixed c by the localized weak distances. The separate uniform point test excludes Mpen2 and b6, while its d2 gap is negative. The older decimal0.0029920 for the d2 weak radius should be marked approximate or rounded down; the stronger T4-064 bound makes that rounding immaterial to this exclusion.
Proof SHA256: 1542ed5df48fcbdf9ae956f6c1474c827a154f817659f3d9de6429ee8ff03c00.
Code SHA256: 79c270a0bcfd33182abb3d2bd454cafc8176e3f99c0b6038b9fe674123f215e6.
Results SHA256: 142d41dd586ee2b127005eec41bf785f5900239a7d45c18eb0e9c3bfcbd93a66.
Actual computation: 0.0014343787916004658 seconds.

## T4-071: Independent Opus review of sharp odd weighted velocity

Date: 2026-10-28T23:35:43.981151+00:00.
Claim: T4-054 has a complete independent review by T1 R1-010.
Method: Freeze the full T1 review, its independent code and output; verify the unchanged original proof hash. Track the ODE and boundary integration justifications supplied by the review.
Result and verdict: CONFIRMED. T4-054 is now AUDITED: the sharp complex odd Beurling norm (2+a)/(2-a) and the real odd IPM velocity upper bound2/(2-a) hold for the exact radial-weight hypotheses in that proof. This does not itself imply a high inverse or a nonlinear closure.
Original proof SHA256: 5c3bdfe1c4b7c203f3cf9b361f16cd938589b38487bd197a59b40af2c6473f32.
T1 review SHA256: 1ddc82863a3e7b0491f0898ec0a1d8d9b2791394cf05d1cef43a712dba504352.

## T4-072: S1 weighted velocity improvement and exact infinite-matrix certificates

Date: 2026-10-28T23:35:43.981151+00:00.
Claim: T1 TP-2 and its five printed rational velocity constants hold.
Method: Rederive all angular shifts, the exact output-mode cancellation and the pi/8 normalization. Prove the infinite Schur test. Independently construct rational positive vectors with constant tails, verify every finite row and a monotone bound on every remaining row by exact fractions. Floating power iteration only proposes the rational certificate.
Result and verdict: CONFIRMED. For a=6/5,13/10,7/5,3/2,19/10 the respective valid constants are1.616466,1.836267,2.142307,2.585263,13.806975. The true optimal S1 norm is not asserted. The complete rational vectors and positive margins are stored in the certificate. No high-space inverse or candidate existence follows.
Proof SHA256: 0eb58c0e8582da5784be99a9f6de17ae32b4b9d63a3e32fd2bc2589c2ee3fa35.
Code SHA256: 22590a9f06ec866c49c35a5708877780cce03f7ee4bf5f196cf7109bdb8bbeac.
Results SHA256: e729d49201154824c4795bf974b190ac3907403e841732406a6390535d5405f8.
Actual computation: 0.03802215401083231 seconds.

## T4-073: Finite-rank high-regularity repair using raw L2

Date: 2026-10-28T23:35:43.981151+00:00.
Claim: T1's revised TP-1b avoids the extra positivity condition identified for its original coarser argument.
Method: Rederive the forced high rows with ||K h||derivative<=d_j ||h||L2 before using b_s<=b+s a. Use the existing high generator, bounded perturbation, the low resolvent and positive-real continuation.
Result and verdict: CONFIRMED under the precise generator and low-resolvent hypotheses in the standalone proof. The first row has(alpha+lambda)a<=f1+(q+d1)b, so alpha-s d1>0 is not required. T4-059 remains correct for the original coarse b_s argument. TP-1b's high-column regularity gap is repaired; a quantitative Woodbury matrix margin and K_L certificate remain OPEN.
Proof SHA256: 675d02f8f7325c6888b780e425ff32692aea6c9025f3483512d49d0d13083b38.
Frozen T1 review SHA256: 1ddc82863a3e7b0491f0898ec0a1d8d9b2791394cf05d1cef43a712dba504352.
No numerical computation was used.

## T4-074: Independent N4 confirmation of six sharp point gaps

Date: 2026-10-28T23:35:43.981151+00:00.
Claim: T4-055's six sharp-ball point exclusions have a second independent numerical path.
Method: Archive N4's exact rational interval computation using its independent Cartesian fields, Machin pi bounds and integer-square-root enclosures. Match the exact T4 result hash.
Result and verdict: CONFIRMED. N4 reports all12 component overlaps and six positive gaps. This removes the remaining independent-reproduction condition on these fixed-c point exclusions. It does not validate sufficient background hypotheses.
N4 result SHA256: 7888e414b799ab14227f81d0aec080a7b21907b0fa45a2fe5a0701581120eed9.
T4 matched result SHA256: 2d6c9c2f20d6a0b675afe6d6c8f42ffab2f3d0fb51d93e4f8cb9d3bb672b2098.
N4 reported actual computation: 0.07274176692590117 seconds.

## T4-075: Exact independent first-sine residual projection

Date: 2026-10-28T23:40:07.771142+00:00.
Claim: N4's first-mode residual certificates retain every contributing angular interaction and are exact for d2, Mpen2 and snapshots002 through005.
Method: Independently derive and implement the projection using the polar stream function and density. Reconstruct both from the rational potential, then compare the entire branch-polynomial dictionary with the frozen Cartesian-product projection. No N4 field arrays or residual cache enters the independent construction.
Result and verdict: CONFIRMED. All 7206 polynomial coefficients across 78 branches match exactly. This includes the newly published candidate005. The projection is exact, not a truncation of background angular modes. This validates only the first residual mode; no global residual norm or candidate closure is inferred.
Proof SHA256: 575bfc525672bbc76d52e5b44b501f8ccb99da67baeb75d56932ba2a54c7c95d.
Code SHA256: 58dab5f52b712edd9b0254311a4b92f6b724a85d2ada2c7047622a87a9e27374.
N4 target proof SHA256: 38c8ec4a9c40997247fc18a65c5405fd6af5d120c0a4dec10239a1dcc830533f.
Actual total computation: 118.34361603436992 seconds.
C1-N1-002-7branch-frf: 1171 coefficients; result SHA256 c33452b90062b6f2d50b20206e40f37bdcb6fd520936f5d0960f3ab5f4d8d76e; 17.105765948072076 seconds.
C1-N1-003-8branch-frf: 1487 coefficients; result SHA256 5d602b20f4c7908c41b0da0034179d0e8cdc15c625203ffcde86658a03e494bf; 37.63705771882087 seconds.
C1-N1-004-4branch-l2fw: 463 coefficients; result SHA256 522f4b2de0fb857818aed0746711ccba4f6723e7008dfb11328b74a835072bcf; 1.0570367882028222 seconds.
C1-N1-005-d2w-j7-x3: 1765 coefficients; result SHA256 27e039a33d6b64a8a659e0305c46863c933acdc0cf073bf5b0b8477e0e853297; 42.6910724719055 seconds.
Mpen2: 1160 coefficients; result SHA256 83507c5feac70e5683b9cc6ef750f150dd814557c709b5ae6fad5586f9bf09ff; 10.002259875182062 seconds.
d2: 1160 coefficients; result SHA256 0ad5ddfa759155f4845a955c87871c358cc23d3b35b1981a61807475d305fc47; 9.850423232186586 seconds.

## T4-076: General scaled-generator algebra and finite-prefix remainder

Date: 2026-10-28T23:40:07.771142+00:00.
Claim: The general theorem accompanying N4-073/074 gives the correct origin degree, far-field coefficients, convergence region and finite-prefix remainder for the scaled legqs generators.
Method: Re-derive the radial function directly from the Legendre monomial formula. Prove the origin degree, the first two nonzero moments, the pole at negative inverse scale, and Cauchy's remainder estimate. Audit the Cartesian composition argument without assuming a finite test grid proves the theorem.
Result and verdict: CONFIRMED with R rational for rational-coefficient claims. The theorem holds as stated in audit record multiscale_generator_audit, proof. At m+w>=5 all potential derivatives through order9 vanish, preserving the fourth-order origin slope and strain quantities exactly. For R>1 and w+Q+n>0 the far-field series has radius R^-2 in z=r^-2. A finite prefix is not a certified residual tail without the differentiated remainder. The result supplies no whole-plane integration rule for the additional denominator, and canonical inversion outside the campaign's admissible growth class is not asserted.
Independent proof SHA256: b65e605f0c053e4c6bd77734da59ae6e6b5b32c1f5ed48e5ddcddb3caded617c.
Frozen N4 proof SHA256: ca42cff2b5dfd2688263b5177f7e8033e4c8f5d5bb2f1970d53bd9ed4a7a4bb9.
No computation is needed for this general analytic verdict.

## T4-077: Independent exact moments and interval scaled jets

Date: 2026-10-28T23:40:07.771142+00:00.
Claim: N4's scaled-generator moment and Cartesian-jet implementations agree with independent exact constructions.
Method: Use direct Legendre monomial coefficients and separate binomial products for moments. For jets, collect all derivative coefficients as exact rationals before evaluating a single common positive real power; compare with N4's recurrence and interval composition. This replaces decimal symbolic checks by a second outward interval path.
Result and verdict: CONFIRMED on the stated finite fixtures. All 5400 exact moment coefficients match over360 cases. All 388 interval jet comparisons overlap over10 fixtures, including four exact zero-jet cases through order9. The general correctness argument is T4-076; these finite checks do not validate arbitrary future inputs or whole-plane norms.
Independent code SHA256: 6da08d7c20d9956e153c75abcaccdf8f98d6adbae0da3e5ba28900ac300676ca.
N4 moment code SHA256: 7e5d3d449e44d30187dd9b7fb7b7be0a14a09aae0089898c02a395facde18c69.
N4 jet code SHA256: 776281b9383dd38f94cafb12888339378bff8877ee30bfefd85e1b6ff20c7915.
Results SHA256: 5d584af4f35772999b4eddb08aae26b91f52ab2c1c8c904592dc37f12c7cde98.
Actual computation: 1.0392896058037877 seconds.

## T4-078: Independent compact-annulus weak probes

Date: 2026-10-28T23:43:52.672532+00:00.
Claim: N4-066's compact C1 probes give the stated fixed-c L2 distance lower bounds, with only local background smoothness.
Method: Reprove admissibility by C1 mollification, check the Bernstein derivative bound, reconstruct polar fields, and evaluate the signed pairing through the weak background equation. Integrate homogeneous polynomial weights against exact rational powers on the compact radial interval, independently of the N4 residual representation.
Result and verdict: CONFIRMED. All56 component comparisons agree at R=8,16,32,16384 for d2 and Mpen2. Safe lower bounds at R=16 are0.08512606 and0.17820407 respectively. No correction-gradient bound or global F membership is required. These local probes are weaker than the already confirmed global localized probes, but independently locate a necessary correction cost.
Proof SHA256: a997944363305b78a7573c1b6a15dcb039433a5cc09337d04731b2370e8cfb35.
Code SHA256: b3c210f6bcfd31ccc06d1797304c2e70377b9c00599dacb9eb6bbd202b173c39.
Frozen N4 proof SHA256: de11ec6555f99df55fd16239aac26d8e4fcf8565feccff209855d02e05102791.
d2 results SHA256: b86c0630c9cc7f2a148af31d25f64ee49f19bf096ef5efc1d3708a70ab214477; actual computation 20.44350614072755 seconds.
Mpen2 results SHA256: 4449c264c5e9f8c8a14dad39a4a207fc2628f60bf54d6ca7e0f7b0e5d160b773; actual computation 20.296416472177953 seconds.

## T4-079: Geometric-partition integration for scaled radial factors

Date: 2026-10-28T23:49:48.434771+00:00.
Claim: Finite products of rational powers at finitely many positive rational squared radii admit a convergent exact-polynomial enclosure method.
Method: Prove a geometric partition keeps every analytic linear-factor ratio at most one half; use exact Taylor coefficients, a Cauchy remainder at radius3/2 and rational endpoint beta moments. Test eight independent closed-form integrals at degree192 and768 bits.
Result: All eight enclosures contain the independently evaluated closed forms, including scales100, two scales and fractional positive/negative exponents. Relative interval radii are below2e-31.
Verdict: OPEN pending independent theory review. This is an original T4 claim, not a candidate norm certificate. Endpoint cancellations and integrability must be established separately.
Proof SHA256: 2cc3b9421932ed60921e90bd9f266c3c8b5de7e654b81b00422a0f0d6955f72f.
Code SHA256: f1ff8f8e85e3911fbf05786dacd423b5c949c61eec3ba80ea0bbb9219c8f0a72.
Result SHA256: 22f1dd992786f31dcb9a4a2817610bf0244563bc7580115d3bc28870fd43cab7.
Actual computation: 1.3499343348667026 seconds.

## T4-080: Independent review of the principal energy obstruction

Date: 2026-10-28T23:49:48.434771+00:00.
Claim: T4-047 is independently reviewed, including S1 reflection, compact repairs, normalization constraints and the seven weighted point values.
Method: Read and archive the complete T1 R1-011 review. Check the exact reviewed proof hash and the distinction between a necessary energy condition and invertibility.
Result and verdict: CONFIRMED. T4-047 is now AUDITED conditional on its stated signed-decomposition, bounded-coefficient and canonical-velocity hypotheses. The reviewer independently reproduced every original point value. The separate TP-3 extension remains pending our review.
Reviewed proof SHA256: e603f56231021a78d5f89751f316c9fa5afb34f9ff0cc21a1d3051630e64a3e7.
Frozen review SHA256: 2beb01edd9e09fc79324481c1f86c6d4f8bd2be5512cff3d53827aeff374fb31.
No new numerical execution was used for this review-status change.

## T4-081: Weighted weak-distance test

Date: 2026-10-28T23:54:53.303471+00:00.
Claim: For H_a=L2((1+r^2)^(-a)dX), 0<a<2, a weighted canonical velocity bound yields a derivative-free necessary correction radius from localized weak probes.
Method: Test the divergence-form correction equation and use weighted Cauchy-Schwarz. Prove cutoff removal using sublinear background growth, then derive exact one-scale beta formulas and an explicit nonlinear gradient coefficient.
Result: The proposed inequality is I<=D m+C_U H m^2, with every coefficient and hypothesis defined in audit record weighted_weak_probe, proof. For k=0 and a<=3/2, H=1 exactly.
Verdict: OPEN pending independent review. This original extension is CLAIMED and has not been used to certify a candidate. No high weighted inverse estimate is supplied.
Proof SHA256: 575679aa179a0aa426a4ddef45a850ef1c55a9ffffc8c631aa3058d103f985ed.
No numerical computation was used.

## T4-082: Candidate005 point and localized weak-distance reproduction

Date: 2026-10-28T23:54:53.303471+00:00.
Claim: N4-076's point and localized weak probes give fixed-c exclusions for candidate005.
Method: Reconstruct the canonical potential from the exact immutable generator input by Rodrigues polynomials; form independent polar fields. Evaluate the weak background equation and complete polar squared norms without a residual cache.
Result and verdict: CONFIRMED. All8 point fields agree, all5 point-box gaps are positive, and all28 weak-probe component comparisons agree at k=0,128,512,1024. The k=0 L2 distance is strictly above0.01625064, exceeding the uniform graded budget from T4-070 and all current unweighted framework budgets. This is a fixed-c necessary exclusion and does not address weighted correction balls.
Canonical SHA256: 62e97be17e7068fe05012866126ef22b5c16fcfd29a6857fed30cd550588c7e5.
Point result SHA256: 87a1d5495c0aeaab5def1b18c6f7a489ef1b092f41c189737ce732d693a5a101; actual computation 3.931354397907853 seconds.
Weak result SHA256: ab7806f6660b39b08dfd5e78c1611272b792a4cef0ae728ede2b3211f1013eaa; actual computation 128.82286229124293 seconds.
Point code SHA256: c1e875277a06209250adf5c838a20112a241bce43528f6b6fd14daee48f9cb38.
Weak code SHA256: 155d39ddeedd9e28a6071e1dfdde8b34ef10c953da251194a4940eb581780f23.
Background Sobolev reproduction is still running and is not included in this verdict.

## T4-083: Candidate005 exact background seminorms

Date: 2026-10-28T23:59:36.593105+00:00.
Claim: N4's candidate005 background derivative seminorms and gradient-structured Hilbert-Schmidt quantity have the stated exact normalization.
Method: Independently reconstruct the density from the canonical potential, form radial Laplacians and anisotropic Hessian columns, and use integration-by-parts identities with exact rational beta sums. Compare four complete rational energies with N4 before evaluating pi and square roots.
Result and verdict: CONFIRMED. All four exact energies agree, and all five interval quantities overlap. D2rho=30.82479103338..., D3rho=796.0924146745..., the two derivative-column norms are12.30836391162... and28.26078413758..., and kappa_HS=1.35808003187097... . The specified sufficient criterion theta+kappa_HS<c-1 fails for every theta>=0. This does not lower-bound the true operator norm and does not exclude a sharper compact-operator or stationary-inverse estimate.
Canonical SHA256: 62e97be17e7068fe05012866126ef22b5c16fcfd29a6857fed30cd550588c7e5.
N4 target SHA256: 3685f9dad1c8ff50cb1ecb0ba0935d5c86108c48830cf6379820b8e66165fefb.
Proof SHA256: 52355ab5d054e3390ec6b322cf89054e1e5c2b53b8a9c2824461cb0825f28161.
Code SHA256: d695076df0f84e0b218a1b200aa20b61a079da68eca97c35fcb5f7b7a5663be4.
Result SHA256: 874628c265a403b20e9dfc12c543eb80cbbfedc5f335815b116e30d4297a751f.
Actual computation: 232.2109465529211 seconds.

## T4-084: Independent weighted obstruction map

Date: 2026-10-28T23:59:36.593105+00:00.
Claim: T1 TP-3's far-field ceiling and58 obstructed weight parameter entries hold for state131.
Method: Reprove the derivative homogeneity count and Lambda>=ac; use the independently reviewed principal-energy obstruction. Construct six independent rational-axis witnesses from the polar potential representation at1024 bits, then prove monotonicity in R when V.X>0.
Result and verdict: CONFIRMED. All six strict endpoint witnesses succeed, covering all58 entries and every positive radius below their respective endpoints. The endpoints (a,R,x) are(6/5,1/4,3/2), (13/10,1,5), (7/5,4,23), (3/2,16,135), (31/20,4096,102400), (8/5,4096,16777216). The corresponding excess over c+1 is positive, including2.48786169614e-5 in the narrow31/20 case. The analytic rate ceiling is beta<=c+1-ac. Nonpositive sampled maxima are not upper certificates, and this result does not obstruct general inverse estimates.
Target review SHA256: 2beb01edd9e09fc79324481c1f86c6d4f8bd2be5512cff3d53827aeff374fb31.
Proof SHA256: a26e9a415322000431f98ffd0534dd5332a9346a1411b3ae51f2d610c736863a.
Code SHA256: 24d2aada48905dc49782093eedd09445dc6158aced5db68cd3c171840ea591ab.
Result SHA256: ebbad4a66380dd5546994b3118b4502576d23c7a30ca5c31ad4f0ca9ad23b8df.
Actual computation: 0.03739089798182249 seconds.

## T4-085: Provisional weighted weak-distance calculations

Date: 2026-10-29T00:01:33.202835+00:00.
Claim: The corrected T4-081 necessary test gives positive weighted correction distances for three refits at a=1.
Method: Reuse the independently confirmed weight-independent pairings after exact canonical-hash checks. Compute the weighted dual coefficients from complete polar square polynomials using outward2048-bit beta recurrences. Use the audited constant C_U=2. The C coefficient is an upper bound, as corrected before these runs.
Result: Among the tested scales, the strongest lower endpoints are d2>0.0071933655 at k128, Mpen2>0.0156668300 at k512 and candidate005>0.0061687217 at k0. These concern ||(1+r^2)^(-1/2)h||_2 at fixed c, not an unweighted norm.
Verdict: OPEN. Both the new weighted theorem and its implementation await independent review; no candidate is certified from this original result. The calculations do not verify a weighted inverse or a high-space contraction radius.
Corrected proof SHA256: 91dd4069dc6fc143dfd142cbfa744891d18d96d6ed12395d214a7e62bffc0156.
Executed code SHA256: 93ecfb8d9a3a3bb77e6d987e9f43324aa3263fb83fbe6f17d677b7b7cf00c79f.
d2: k128, radius [0.007193365585655433980298843553302765640460396758572532893519536669765046597759602013902 +/- 3.93e-88]; result SHA256 233039faba43ed03ec790c4d8c6a5c8f1d30e8324d2810777ff1002bfe9e50cc; actual computation 7.7438910831697285 seconds.
Mpen2: k512, radius [0.01566683002256225458695957757638801151774010012563091089526494643737823658865022392541 +/- 7.43e-88]; result SHA256 0977ab949fd3c1732369345d94181403841f38d4e03801b08c0ea431e5a2d35d; actual computation 6.763160051777959 seconds.
C1-N1-005-d2w-j7-x3: k0, radius [0.006168721705245819722798104149318281872035206475015760680219591523922990472697078191122 +/- 4.60e-88]; result SHA256 868d23182c6be81c2a7ba7ff2b15b0659229ba52b6b98cb4822b11d2d20b8e32; actual computation 33.155915850773454 seconds.

## T4-086: Candidate006 independent point, projection and weak-distance checks

Date: 2026-10-29T00:04:57.265772+00:00.
Claim: N4-081 gives correct fixed-c necessary exclusions for candidate006.
Method: Independently convert all exact generators by Rodrigues polynomials, reconstruct polar density and stream fields, and compare the complete first residual mode. Evaluate the weak background equation and its full polar dual coefficients at four scales.
Result and verdict: CONFIRMED. The canonical reconstruction agrees exactly. All8 point fields and5 original point-box gaps agree. The entire first-mode projection agrees in1487 coefficients over16 radial branches. All28 weak components agree at k0,128,512,1024. The k0 necessary L2 correction distance exceeds0.52622436, excluding every current fixed and uniform graded unweighted correction budget. These are fixed-exponent necessary statements, not existence or optimal-distance claims.
Canonical SHA256: 669e5a4e3412700d867c6ec9a19e19863ecf53c6fe81fa3bc4438d48edac5a00.
N4 point target SHA256: edad1c588e35e34da499d395ec76e29c7c40f1026fef83427d795027cb8a762c.
N4 projection target SHA256: 9a0dca3a7ab2bd7904062ecbd5675db643fb4d4f1f302bf4284f748e3a1149df.
N4 weak target SHA256: 250ca455a442797202914e9c3fcda56bb7f9e12c901b33ad8f2dd07e8fbcf947.
Point result SHA256: f7950f2c2b8df4ba9f0f11f92851388f5ec166196baab68b464569cc44c47214; actual computation 3.926767851226032 seconds.
Projection result SHA256: efad2574813503500a85bb138395ea10de98a5e149c98ac470ada0961b562ea0; actual computation 34.77474850928411 seconds.
Weak result SHA256: e38c9fd6395896fbbe168a048617759618d555e55151d1681fcc008dd023a173; actual computation 111.06814764393494 seconds.

## T4-087: Candidate005/006 sharper point boxes and signed witness

Date: 2026-10-29T00:04:57.265772+00:00.
Claim: N4's additional point combinations give four further positive sharp-box gaps, and candidate006 fails the prescribed signed rate-two condition at the selected point.
Method: Apply the previously audited point and signed inequalities to the independently reconstructed polar fields. Compare every resulting quantity with the frozen N4 rational endpoint records.
Result and verdict: CONFIRMED. Candidate005 sharp/sharpw gaps are1.40549367629919... and1.40271057157701... . Candidate006 gaps are6.34361791007551... and6.33729325277716... . At(3/7,1/4), candidate006 has theta=6.432313124164565... and theta-(c-1)=5.621993913964567...>0. Thus the specified sufficient signed rate-two condition fails even with kappa=0. The candidate005 point has theta=0 and supplies no signed obstruction by itself.
Code SHA256: 8f251461b88604b381b7ac4334038527b3d1ecf69658342a1f3bdc35e11ec3c5.
Scope proof SHA256: 485b4f5a38705a69c11a1f51a4862af9dd121242f9b4b171e3bcb3d6f93b309a.
C1-N1-005-d2w-j7-x3: target SHA256 489f5decf9378484b99beafd830ba5b3148683dc273a02fd48345a19ab0770ed; result SHA256 f451720875f53a0d2c43ebb7f418e47653bf075b674601f5d77647a0a327dc3c; actual computation 0.001358918845653534 seconds.
C1-N1-006-8branch-e2: target SHA256 02493cd19a78dc5e0dfa1ed6a80082beacf516d0217378335fbe9bc3ee210b5d; result SHA256 65e50ec17cab851007278662e528a7b24b606f89402ace21d4e5dad32a6873d8; actual computation 0.000746504869312048 seconds.

## T4-088: Provisional weighted weak distances at a=6/5

Date: 2026-10-29T00:09:20.495623+00:00.
Claim: The corrected weighted weak test yields the stated necessary radii for state131 and three refits.
Method: Use C_U=808233/500000 from the independently audited S1 Schur certificate. Evaluate complete dual square polynomials with outward2048-bit beta recurrences. For the three refits reuse independently confirmed pairings after canonical-hash checks. For state131 reconstruct the pairing directly from the polar weak background equation.
Result: The largest tested bounds are state131>0.000029157438, d2>0.0048295932, Mpen2>0.0091651753 and candidate005>0.0064650914. These are weighted fixed-c distances, not residual norms.
Verdict: OPEN pending independent review of T4-081 and reproduction of these new weighted coefficients. The original state131 pairings also require a second path. No weighted closure is claimed.
Corrected proof SHA256: 91dd4069dc6fc143dfd142cbfa744891d18d96d6ed12395d214a7e62bffc0156.
Executed code SHA256: ced4ed418bb86c19854b546f7c54799bf64713b4a9c33833169fa2cf8e7a8d6e.
State131 pairing SHA256: a2a9fd01dcfdad01a15b510c7509078a786a581230500cef7bf82dc92f18f24d.
state131, k=1024: {'weighted_L2_radius_lower': '[2.915743832610422103684252833605287459728999207033236472127946736182627499689594274300e-5 +/- 4.56e-91]'}; result SHA256 4ca5d192623971f2d64d06e62c5ecb1fd55a8b31decc39fdbcab25e1663517dc; actual computation 0.15727032674476504 seconds.
d2, k=128: {'weighted_L2_radius_lower': '[0.004829593203158804471512315644607033432459075263289565598366059134984550469136862588828 +/- 1.71e-88]'}; result SHA256 5055e9e86ae6e460b981d6a32520b038a5dc1287b09f70a597fb409af1b76dd9; actual computation 7.814749974291772 seconds.
Mpen2, k=512: {'weighted_L2_radius_lower': '[0.009165175350157292107289737060481514538888088203068360281011972867486343223312127633669 +/- 4.47e-88]'}; result SHA256 adc642c2a9087a6b9eeb906c13f76a6ce271141408a4452cf3e8f1f0cc391255; actual computation 6.802986595313996 seconds.
C1-N1-005-d2w-j7-x3, k=0: {'weighted_L2_radius_lower': '[0.006465091471948015327121217792630522811139121883499141743870604925801193698451339054546 +/- 1.98e-89]'}; result SHA256 50e74451da8bd88b5ec589b408ac332647102e03b744939d2ec72ace183c069a; actual computation 33.28986005438492 seconds.

## T4-089: Full weighted state131 residual norm

Date: 2026-10-29T00:09:20.495623+00:00.
Claim: Exact finite polar algebra gives the full-plane norm ||(1+r^2)^(-a/2) F||_2 for state131 and its sharp membership threshold.
Method: Reconstruct all150 residual components in20 sine modes from rho and psi, group the full square into15 rational power families, and integrate each signed polynomial exactly. All beta denominators are checked positive; pi and the square root are enclosed at1024 bits. The exact leading angular vector is nonzero.
Result: Membership is exactly a>4503599627370496/4076476460239181=2/c. In particular a=1 and11/10 diverge. The norm is8.6128211244 at a=221/200,0.16931885885 at6/5,0.04997773856 at13/10,0.01821818172 at7/5, and0.00738180087 at3/2. Exact rational squared energies and outward intervals are saved.
Verdict: OPEN pending independent reproduction. The complete polar residual identities were previously audited in T4-032; this new full weighted calculation remains original. No omitted tail or spatial quadrature is present, but no inverse or nonlinear closure is certified.
Source SHA256: 25874f2b636a2c34b8b2c207d3e5c8b34aa2ac594cdd5c321c79285499f0af2c.
Proof SHA256: 0a14edcf32c893ee526b674ccd20735e6367959b30522da85145fbd43638b848.
Code SHA256: b94520d86c1e311c49902e979262ee9d4eefc8d79c0af91774b6630e3354940e.
Result SHA256: 7048d8e511199bedb558dfd2425ddd54465d34a8c40f7141017d7b1ab9a0fcf6.
Actual complete computation: 0.9398953458294272 seconds.

## T4-090: b6 exclusion in the seven stationary-inverse boxes

Date: 2026-10-29T00:11:25.208933+00:00.
Claim: N4-083 correctly transfers the confirmed b6 point gap to all seven T4-067 parameter pairs.
Method: Independently form the differences of the squared Sobolev point coefficients using our original exact parameter file, check all14 differences strictly positive, then compare the peer's rational ratios. Check the old b6 gap against our independently reproduced point certificate.
Result and verdict: CONFIRMED. Every new necessary upper bound is smaller than the old one, so each gap is greater than2.9392836795 at the same point and fixed c. This is a correction-ball exclusion, not failure of a general inverse.
Proof SHA256: 0cc5bd264d6e9559aa7ef649668f166cce6986afb88656486b21fa42dbd64856.
Code SHA256: f504a8cb3159ebb7089b1eee38091189f525190028a88b333f389ac4bbfc0057.
Result SHA256: 8c63f6a04aeb91ddd9ba54b90344d597e00faa7b405515ec8d60bafcc316a93b.
Actual computation: 0.0013210810720920563 seconds.

## T4-091: Independent review of the origin high-regularity obstruction

Date: 2026-10-29T00:11:25.208933+00:00.
Claim: T4-060 has an independent complete analytic review.
Method: Read and archive T1 R1-012, check the exact target proof hash, and distinguish its analytic review from the supplementary FLOAT packet experiments.
Result and verdict: CONFIRMED. T4-060 is AUDITED conditional on its coefficient hypotheses; the graph variant retains the separate T4-058 definition dependency. The necessary rate is beta<=c+1-q, so q=3 gives beta<=c-2<0. No stationary-inverse obstruction follows. Minor cone and wording clarifications are in REVIEW_STATUS.md without changing the audited proof.
Reviewed proof SHA256: 1e59a48b5d024a73ab47042cad5e6104dbc45b007874111a3ab571c37a0baa57.
Frozen review SHA256: fe75f3c8120f808991f81be6bb18a7a1f87e37fd20890a5ec7b23d9ae9c88a89.
No new numerical execution was needed.

## T4-092: Scoped weighted principal-packet theorem

Date: 2026-10-29T00:18:15.453088+00:00.
Claim: T1 TP-4 gives the necessary principal matrix for the campaign's weighted Sobolev energies.
Method: Independently expand the Bessel multiplier, calculate the transport weight term, retain the signed velocity symbol, control the global coupling tail, impose S1 symmetry and remove the canonical strain with the exact contact corrector. Check the homogeneous negative norm separately.
Result and verdict: CONFIRMED in the explicit scope of audit record weighted_packet_audit, proof: smooth sublinear backgrounds with differentiated power bounds, polynomially comparable weights of exponent p<3-gamma, every real Bessel order, and the unweighted homogeneous order-1 case. The five A2 matrix identifications, origin cap beta<=c+1-q and power-weight far-field limit are confirmed. The unrestricted arbitrary-weight/arbitrary-homogeneous-order extension is OPEN without adequate packet-domain hypotheses. An energy cap does not lower-bound an arbitrary inverse norm; the K_H sentence must be scoped to reciprocal energy certificates.
Proof SHA256: 351dcccc4ca64f4016b0f918bbf1f901786992613ca6da6ed5e743257a2ead94.
Frozen T1 review SHA256: fe75f3c8120f808991f81be6bb18a7a1f87e37fd20890a5ec7b23d9ae9c88a89.

## T4-093: Independent rational-point energy caps

Date: 2026-10-29T00:18:15.453088+00:00.
Claim: T1's stated coarse state131 matrix caps and negative examples have independent point witnesses.
Method: Reconstruct the polar stream Hessian and rotate to Cartesian derivatives, independently of T1's Cartesian potential evaluator. At1024 bits evaluate twelve rational points and the exact principal matrices.
Result and verdict: CONFIRMED. Safe strict upper caps are0.99116 for B4,0.63089 for W2 k1,0.61151 for B5, and-1.20662 for B6. Unweighted order2, omega order5/2, and every tested R16 exponent p=1/2,4/5,1,3/2 have strictly negative witnesses. The omega order(2+1/1024) cap is below0.60974. These point certificates upper-bound available rates; they are not global positive lower bounds. The new rational points intentionally need not equal the peer's grid coordinates.
Code SHA256: 585aab8fa6c036d9714d3b2fb1aeefc690af404ee86626d64c13a9b3d07a83e2.
Result SHA256: 5c56a54df6ad97632b5e6ad5f12d8ac164dbe5c696fab4cb8ea8902c3a97d7fc.
Actual computation: 0.12830240093171597 seconds.

## T4-094: Growing-weight background obstruction

Date: 2026-10-29T00:18:15.453088+00:00.
Claim: A nonzero differentiated leading density r^gamma G with0<gamma<1 has infinite ||w D2rho||_infinity whenever w is comparable to r^p and p>2-gamma.
Method: Take the radial second derivative gamma(gamma-1)r^(gamma-2)G and use the Frobenius Hessian bound. Check the nonzero exact leading angular vector of state131.
Result: The trial p=3/2 violates the existing weighted second-derivative background condition for state131, since gamma>1/2. This does not exclude a hierarchy with different coefficient weights.
Verdict: OPEN pending independent review of this original extension. The exact nonzero leading-energy and exponent checks are in the T4-093 result JSON.
Proof SHA256: 351dcccc4ca64f4016b0f918bbf1f901786992613ca6da6ed5e743257a2ead94.

## T4-095: Independent review of the dyadic high-space closure

Date: 2026-10-29T00:18:15.453088+00:00.
Claim: T4-058 has a complete independent analytic review by T2.
Method: Read and freeze the review, match the original proof hash, and check that every high and low hypothesis remains explicit.
Result and verdict: CONFIRMED. T4-058 is AUDITED conditional on (1), (8), (9), (H), (12) and F in Y. Its high-space completeness, closed low-metric ball, normalized inverse map and contraction are confirmed. No concrete high resolvent estimate or successful candidate closure is thereby proved.
Original proof SHA256: 906111ef2e54596ca432cf6513b13318dbdba9cb8f766cb784cb8e08d660d365.
Frozen T2 review SHA256: 6b4164c59a82bd968b4be01e86d1c43905892298bf8a8c9ecb3fe4b953105422.

## T4-096: Audit of T2's additional dyadic-radius consequences

Date: 2026-10-29T00:18:15.453088+00:00.
Claim: T2 R2-R7 and C1-C4 give further consequences for the dyadic framework.
Method: Independently prove the plateau lower bounds and universal radius ceiling, check the transport-model inverse, reconstruct all20 leading residual coefficients from the potential, and evaluate the two rate-dependent ceilings with outward1024-bit arithmetic.
Result and verdict: CONFIRMED for Lemma Y1, C_U>=1, R<R_univ(a)=sqrt(8pi)(1+c-ca)/(1+a), the scoped transport-model counterexample, and the leading angular norms0.18207889107112578 and15.20937674970366. At a=221/200 and the prescribed certificate beta=0.02181481, the scheme needs M<1.2613e-12; with any possible rate at that weight, M<7.4294e-11. The first number is not necessary for every sharper possible rate, since T4-022 gave a lower bound on beta. REFUTED as a logical implication: an origin energy packet alone does not require s<c-1 for the actual high inverse (H), nor does a lower rate certificate upper-bound the best rate. OPEN: the all-a state131 exclusion from the truncated31-sector series and an assumed correction asymptotic. Neither an infinite-series remainder nor a finite onset for arbitrary corrections in Y was proved.
Proof SHA256: d2a6acbddd65b7f8b4e7e0d1fbd211c04a7124341192a8f866b9c9abd53d4f3d.
Code SHA256: 77623c14cb3208ff27b1ba9611245123a86bef77775c4a7dc4fd0f460547288f.
Result SHA256: d8759baae2a501b8919d3cdb991257c01a3954eaccaf822198fd1d043d3bb595.
Actual successful computation: 0.39274758799001575 seconds. The first run stopped on an unsupported decimal-rational input string; its log is retained and the inputs were replaced by exact integer fractions.

## T4-097: Genuine far-field lower bound on the dyadic inverse

Date: 2026-10-29T00:22:43.992215+00:00.
Claim: Under the finite-angular differentiated-decay hypotheses in audit record farfield_resolvent_floor, proof, every actual high inverse bound(H) of T4-058 has M>=1/(1+c-ca).
Method: Construct compact mode1 logarithmic plateaux h_N=r^(a-1) chi((log r-T_N)/N) sin(theta). Exact canonical angular formulas make h_N and its velocity zero near the origin, preserving both normalization and the input hyperplane. Prove uniform Y estimates directly with logarithmic Volterra kernels. Show (L+beta_infinity)h_N is o(Y(h_N)) in Y, then apply the actual consistent inverse.
Result: A true approximate-eigenvector argument replaces the heuristic inverse comparison. Combining it with the audited radius ceiling requires Y(F)<sqrt(8pi)(1+c-ca)^2/(1+a). It is independent of energy numerical-range arguments.
Verdict: OPEN pending independent Opus review. No numerical packet or large-radius computation is used. The profile-specific finite-angular/decay hypotheses are explicit.
Proof SHA256: 1d195ca686dd2deae3df192344ebe5aeb01c5c92529999816242cc028da93bee.

## T4-098: Complete Laplacian tail bound for state131

Date: 2026-10-29T00:22:43.992215+00:00.
Claim: The complete state131 residual has an angular Laplacian lower bound from radius8192, with a half-leading-sector margin.
Method: Reconstruct every residual component and differentiate the finite polar formula exactly. Combine all414 rational-power coefficient vectors of r^(2-b) Delta F. Bound every positive-power vector by its angular norm at z0=1/(1+8192^2), including the exact t^delta factor.
Result: The full relative remainder is below0.466203338674<1/2 at and beyond8192. The leading Laplacian angular norm is15.20937674970366. This is a full finite-algebra bound, with no omitted asymptotic series. It implies the geometric-series lower bound(5) in audit record dyadic_laplacian_certificate, proof.
Verdict: OPEN pending independent numerical reproduction. The proof and algorithm were written before the calculation.
Proof SHA256: 37e1521d7a56dcd8629f1307c0df061a982545a87ecf1e816bac1f2637bafb20.
Tail code SHA256: 50ef1feb352c6120f0cd48621b52399ea688875bb0084ec501f96161a5bf227d.
Tail result SHA256: 50691e61b353005df1c869b0e6cde6bb54b6fdfcd07c6bcd9eee17f3b1fb86ad.
Actual computation: 0.5672816382721066 seconds. The tail result records the proof hash before its subsequent interval-cover section was appended; the original tail statement and proof are unchanged.

## T4-099: Uniform dyadic-scheme obstruction for state131, pending review

Date: 2026-10-29T00:22:43.992215+00:00.
Claim: If T4-097/098 are independently accepted, state131 cannot satisfy T4-058's closure inequalities for any a,s or finite low weight radius Rw.
Method: Parametrize the entire remaining exponent window by a=2/c+(1-1/c)x,0<x<1. Square the necessary comparison so pi cancels. On256 exact consecutive rational cells covering[0,1], bound the increasing and decreasing factors at their appropriate endpoints, using1024-bit outward arithmetic. Check positive lower endpoints for every cell.
Result: Every cell passes. The minimum certified squared ratio of the full-tail lower bound to the necessary residual ceiling exceeds11.2378037794, and the minimum unsimplified positive difference exceeds32.37186956. Outside this exponent window, F fails Y membership or the low positive energy rate is impossible. This would rule out this specific dyadic closure scheme at the original reference, not the existence of the profile or all weighted approaches.
Verdict: OPEN pending independent review of T4-097 and independent reproduction of T4-098/099. Do not mark a closure-matrix row RULED OUT solely from this original result yet.
Cover code SHA256: 380537b01f46231dd7666a3001006f8d88eb9c5e1621d7ac99bd15ccd50d218c.
Cover result SHA256: da631e50fc07fdab7dd0d813ca27ef0a23c8cd7466a3713aa8672d9f9fda4f97.
Actual cover computation: 0.022208441980183125 seconds.

## T4-100: Independent confirmation of weighted weak computations

Date: 2026-10-29T00:27:54.915645+00:00.
Claim: N4-085 and N4-089 independently reproduce T4-085 and T4-088.
Method: Read the complete independent cutoff proof, Cartesian gamma-beta implementation and reviews; freeze the seven result files and source identities.
Result and verdict: CONFIRMED for all63 a=1 and91 a=6/5 numerical comparisons. Safe lower bounds at a=1 are0.0071933655(d2),0.0156668300(Mpen2),0.0061687217(005); at a=6/5 they are0.0000291574383(state131),0.0048295932(d2),0.0091651753(Mpen2),0.0064650914(005). The corrected original theorem still awaits the required T1/T2 review. Historical a=1 evaluator identity is explicitly not asserted after its later update.
Archived PROOF.md SHA256: 1ee1c77bc68afe7e0f5ef828b66a2a54558bff61643fa704c9ae11305aef3caa.
Archived d2_a1_2048.json SHA256: 74e81d1692070f4f7a4da62e0350a8d9886ae741db038e40c8d71dd62ca409c1.
Archived Mpen2_a1_2048.json SHA256: ba3332db7fe3836c6d86e141abc2488f200c9c27f6cede647a415bb97320ee85.
Archived C1-N1-005-d2w-j7-x3_a1_2048.json SHA256: 6e2c8fde876bf6d431d04654487e1cb5bf4dcc795cb5838fb825021f217bb682.
Archived state131_a6_5_2048.json SHA256: 9d3252dee4be115ed699dd77970d2d90e59f49aa5aa9e6525f2ab6e55038d23a.
Archived d2_a6_5_2048.json SHA256: 6f821f9b0a41ba49cb96d169e37dc811c8f22f2bcf9b3f481f0a9dca86fae9be.
Archived Mpen2_a6_5_2048.json SHA256: e86722b71fdf5a9cb127c738d3cd1e41bc1e496001e4a9ff4e2179d74ec66680.
Archived C1-N1-005-d2w-j7-x3_a6_5_2048.json SHA256: f2747cd234b3132b517ff8eaa72f77cd09a72269efa37fc45699c0bc53feac59.
No new numerical execution was required to archive and assess this completed independent review.

## T4-101: Independent scaled-moment review

Date: 2026-10-29T00:27:54.915645+00:00.
Claim: N4-086 independently reviews T4-079's finite-scale integration method.
Method: Read the full analytic partition and Cauchy-remainder argument, implementation and13 closed-form fixtures; freeze the evidence.
Result and verdict: CONFIRMED for the independent review and all13 enclosure tests, including8 overlaps with the original computation. No full candidate norm is thereby certified. Any additional T1/T2 policy review remains separate.
Archived PROOF.md SHA256: b8d9f1b58b4021863d373e9362a367249c59bf27724a29950d10093b43740c75.
Archived results.json SHA256: 01c25c66fc3adb7a28edd81fd57fbb6fc10524fc18c145f54f613dcd3d4dae40.
No new numerical execution was required to archive and assess this completed independent review.

## T4-102: Independent full weighted residual confirmation

Date: 2026-10-29T00:27:54.915645+00:00.
Claim: N4-087 reproduces T4-089's complete state131 forcing norm.
Method: Read the independent Cartesian assembly and exact moment proof; check the review and freeze the complete rational comparison record.
Result and verdict: CONFIRMED: all5 exact rational energies, membership threshold a>2/c and leading angular energy agree. At a=6/5 the full R=1 norm is0.169318858858787; at3/2 it is0.00738180087000192. These are forcing norms, not correction bounds or existence results.
Archived PROOF.md SHA256: 7b258cf21b7ae0d79c1b744f8ed0dde5d82a7a04dfd32d7fe48b6333afc8b503.
Archived state131.json SHA256: 0786a0ac953d1cba48143cf7385dd8d471d859e1b1e8e8af7874702a0cd3a980.
No new numerical execution was required to archive and assess this completed independent review.

## T4-103: Independent S1 velocity confirmation

Date: 2026-10-29T00:27:54.915645+00:00.
Claim: N4-088 confirms the five weighted S1 velocity upper bounds of T1 TP-2/T4-072.
Method: Independently reread the positive-square block identity, S1 angular cancellation and pi/8 normalization; inspect the rational row and Gram checks.
Result and verdict: CONFIRMED: all335 finite-row or tail comparisons and405 Gram entries pass. Constants at a=6/5,13/10,7/5,3/2,19/10 are1.616466,1.836267,2.142307,2.585263,13.806975. No optimality or inverse conclusion follows.
Archived PROOF.md SHA256: ce95ffc80e03dd94476211d70375cf59088fd17518ebfcd7773c5502dd49dfa4.
Archived results.json SHA256: 57166436f17a5d329ea51dd26ca0c64fb246e776bdc2ee3a84659810e6f8a313.
No new numerical execution was required to archive and assess this completed independent review.

## T4-104: Direct scaled-generator sector assembly audit

Date: 2026-10-29T00:27:54.915645+00:00.
Claim: The analytic generalization behind N4-084 correctly computes origin jets and complete finite forbidden-sector tables for positive rational scales.
Method: Re-derive the origin parity transform, exterior scalar series, all derivative signs, product exponent convolution and omitted-exponent bound. Inspect the direct implementation. Complete standalone argument in audit record direct_generator_audit, proof.
Result and verdict: CONFIRMED under the stated finite rational-family hypotheses. Equal exponents must be aggregated and a leading-sector claim requires a strict omitted-exponent comparison. N4's3240 coefficient comparisons are archived, not newly rerun by T4. The earlier T4-076/077 covers the independent moment/jet ingredient. No multiscale full-plane norm or infinite-branch convergence is claimed.
Archived PROOF.md SHA256: 192106f0eb187f3930505f9f3bae51895d8776a118488171704926be8d25a823.
Archived direct_comparisons.json SHA256: 12f276363acdd7bad0152f171498660a2f495169aa98d246be74c76b7845caa2.
No new numerical execution was required to archive and assess this completed independent review.

## T4-105: Independent complete-tail and interval-cover confirmation

Date: 2026-10-29T00:32:03.920992+00:00.
Claim: N4-093/094 independently reproduces T4-098 and the numerical part of T4-099.
Method: Read the full independent proof, Cartesian derivative implementation and complete review. Freeze their source and result. Check the dyadic plateau scaling and the historical proof-hash distinction.
Result and verdict: CONFIRMED for150 exact Laplacian identities,414 rational angular-energy comparisons,11 full-tail ratios and1024 interval-cover quantities. The radius8192 remainder is below0.466203338674; the256 cells have minimum positive difference above32.3718695601 and minimum squared ratio above11.2378037794. The all-parameter scheme exclusion is still OPEN pending independent analytic review of T4-097.
Independent result SHA256: 4711cc368c9cdb64dc0c0a216536770504242857bd22c855b23c2c7b0f7b580e.
Independent runtime:1.066286 seconds. No numerical rerun was necessary for this record.

## T4-106: Large-scale weighted weak probes independently reproduced

Date: 2026-10-29T00:39:25.397326+00:00.
Claim: N4-095's finite large-scale search gives stronger necessary weighted correction distances for state131.
Method: Reconstruct the density and stream function independently in polar coordinates, integrate the weak equation directly, and use outward log-gamma beta moments instead of the peer's projected residual and direct gamma quotient. Compare all seven quantities in each of 104 rows.
Result and verdict: CONFIRMED for all 728 component comparisons. The best tested lower bounds are 0.00126243167054647 at a=6/5,k=2^32; 0.000436835013298882 at a=13/10,k=2^28; 0.000163823854295507 at a=7/5,k=2^26; and 0.0000633313418036115 at a=3/2,k=2^24. These are finite-test necessary distances, not optimal scales or existence claims. The original weighted weak theorem still retains its separate T1/T2 review requirement.
Proof SHA256: 44abe7179a6fea60afba55e9e86dafcff3bb61d0d47412cb6a53ec6593b80a3e.
Code SHA256: 11b06b4c2d1f2533f2af22212d12da092631aa954a373f9acbb9c23a24ffb681.
Result SHA256: d7d2b104a3ee6cf18afb843f33af588db925245a76fc849ae4da740d98171a1e.
Actual computation: 1.9284291872754693 seconds.

## T4-107: Complete weighted Laplacian norms for d2

Date: 2026-10-29T00:39:25.397326+00:00.
Claim: The dyadic norm satisfies Y(F)>=5^((a-2)/2)||(1+r^2)^((2-a)/2) Delta F||_2, and the full d2 Laplacian norms have the stated values at seven exponents.
Method: Use the cutoff plateaux to prove the continuous comparison. Independently assemble all 780 residual components from the canonical potential, differentiate exactly, group the complete square in 23 rational-power groups, and integrate all 4704 nonzero monomials with outward 2048-bit arithmetic. Check every component's integrability and each denominator.
Result: The norms at a=0,1/4,1/2,3/4,1,5/4,3/2 are respectively 1161.65961265051,392.468789957815,142.246591604973,54.9396454319633,22.6836992643494,10.2218155242159,5.25474052266155. Each corresponding lower bound exceeds the necessary residual ceiling from T4-097 at that exponent. A finite list alone is not an all-parameter exclusion.
Verdict: OPEN pending independent review of the continuous estimate and numerical reproduction. The subsequent uniform comparison is proved in UNIFORM_COVER.md and awaits its own arithmetic execution.
Proof SHA256: 516e3d20063b96b21e073638fa532ff861e40c2231b6a7a1fff11e64983fa422.
Code SHA256: 70a19589a4de20aa5d59a1ede980815210c995c82f8fc2072a73ec5df1cf75b7.
Result SHA256: 7f8f2780172609a1580c723fe764e224ffbae419af988a98daaf8e0bda1385a6.
Actual computation: 565.4028132059611 seconds. The bounded job completed before its 590-second timeout; it did not fail or time out.

## T4-108: Candidate007 canonical, point and first-mode checks

Date: 2026-10-29T00:39:25.397326+00:00.
Claim: The exact candidate C1-N1-007-d2w-j7-e2bal has the independently reported point fields and first residual mode.
Method: Convert its exact Legendre generators by the Rodrigues coefficients, match the canonical coefficients exactly, and evaluate independent polar derivatives at (1/10,73/100). Independently assemble the first residual mode directly from the polar density and stream function.
Result and verdict: CONFIRMED. All eight point quantities agree, including F=0.091143284501653733606, and the five listed point-ball gaps are positive. All 1765 coefficients of the 16 first-mode components agree exactly, using 4044 nonlinear angular pairs. This verifies neither a global signed margin nor a full-plane small residual. The weak and background queue is still running.
Snapshot SHA256: ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21.
Point result SHA256: 9ee1f44b692f6e3c3bd8cec103ae061d961f657d90c656ecf9a01abacf7b9db1.
Projection result SHA256: 6b8b45731debc59a5628d647d2f756b4cca10c4e633d52dbb11f92cd85f6f7f7.
Actual computations: point 4.546552492305636 seconds; projection 41.57245876407251 seconds.

## T4-109: Required theory review of the weighted weak-distance theorem

Date: 2026-10-29T00:42:37.764053+00:00.
Claim: The corrected T4-081 statement and proof, including cutoff admissibility and all explicit constants, pass an independent theory review.
Method: Read T2's complete proof reconstruction, generator construction and numerical log; verify the reviewed proof hash. Inspect the independent polar-in-t implementation.
Result and verdict: CONFIRMED. T4-081 is now AUDITED under Amendment v03. T2 additionally reproduces all 154 previously stored comparisons. T4-106's 104 larger-scale rows therefore use an audited theorem and independently confirmed arithmetic. T2's refined new k values remain separate claims until independently reproduced. The weight transfer to Rw>=1 and the dyadic Y norm is valid.
Reviewed proof SHA256: 91dd4069dc6fc143dfd142cbfa744891d18d96d6ed12395d214a7e62bffc0156.
Independent review SHA256: 1a972a3389f799adf4b16c2f8ef9e84742128ad7f4bbe0c5a7848d1bbe8b0b89.
Independent script SHA256: 37959994eaaede8776b2d8705c425a191be58de9d9dccb4d675a4683cf912e31.
Independent log SHA256: 01d26d63d47a8ed258a804c866ac79f1274eb677c2e876cbafea1f0330ca1e83.
No new numerical execution was needed for the analytic review.

## T4-110: Candidate007 localized weak distances and source identity

Date: 2026-10-29T00:42:37.764053+00:00.
Claim: The four localized weak probes for C1-N1-007-d2w-j7-e2bal independently agree with N4-091.
Method: Assemble and integrate the polar weak background equation directly, using outward 2048-bit arithmetic. Match all seven quantities at each k; verify the exact generator-file hash against its manifest and the exact c against its canonical representation.
Result and verdict: CONFIRMED for all 28 numerical comparisons and the source identities. The best tested fixed-c L2 correction lower bound is strictly greater than 0.00004398700347 at k=128. The other lower bounds are greater than 0.00001618643917,0.00002912721217,0.00002392482094 at k=0,512,1024. Together with T4-108 this excludes the listed scalar balls and graded box1. It does not yet exclude the other graded boxes. No global signed margin follows from these tests.
Weak result SHA256: a766199200a2c1a202f65f5eb6d2ca4ba772582a6c8cc49cc5bfe46969f83e00.
Identity record SHA256: f496aba1e653516713edb15e247e5f8e1048b636a5731fcad8d294d56155ec1d.
Background norms remain under computation.

## T4-111: Candidate007 complete background norms

Date: 2026-10-29T00:43:51.030121+00:00.
Claim: N4-092's full-plane Hessian, third derivative and Hilbert-Schmidt bounds for candidate007 are correct.
Method: Differentiate the exact canonical potential independently in polar form. Use Hessian integration-by-parts identities and exact rational beta integrals. Compare all four rational energies before enclosing square roots.
Result and verdict: CONFIRMED. The full-plane norms are ||D2rho||2=17.28647575490666, ||D3rho||2=127.4975902563294, ||D rho_x||2=5.061548159966704 and ||D rho_y||2=16.52885278079859. The complete Hilbert-Schmidt bound is kappa=0.72816468018232542728. Every rational energy agrees exactly with N4. These are enclosures in the result file; displayed decimals are approximations. A global theta certificate remains necessary for the signed rate.
Result SHA256: f37fb673cb613b1c4953204ab0ad7448271c1fc4f102d137337eb73d4a210011.
Executed code SHA256: 1b5c95566b0b4e705bc9a800a0008c74032ef47f059bd2bd4af43b00d2a7d010.
Proof SHA256: 52355ab5d054e3390ec6b322cf89054e1e5c2b53b8a9c2824461cb0825f28161.
Actual background computation: 237.10244074370712 seconds. The sequential queue completed at00:42:25Z. Earlier status notes reporting it still running were stale polling information.

## T4-112: Seven-cell d2 dyadic comparison

Date: 2026-10-29T00:43:51.030121+00:00.
Claim: Subject to T4-097 and T4-107, d2 cannot meet the specified dyadic closure inequalities for any possible exponent, regularity or finite low-weight radius.
Method: Monotonicity bounds six quarter-length cells from0 to3/2. For the last cell up to7/4, Cauchy-Schwarz gives N(7/4)>=N(3/2)^2/N(5/4). The positive-rate exponent endpoint is strictly below7/4. Compare outward bounds on every cell.
Result: All seven cells pass, with ratio greater than1.35446238584264 everywhere. No asymptotic truncation is used.
Verdict: OPEN pending independent review of T4-107 and its numbers, and acceptance of T4-097. This is an obstruction to this sufficient scheme, not nonexistence of a profile.
Cover proof SHA256: c7253f73c992f0d87e1d90feb770f6d08ccf0c075935972ca6ef5db5cf9eaab4.
Cover code SHA256: 61010c72c5cc0331fe86108f4ed03f5f6dee467577d7c796deb943321703b280.
Cover result SHA256: 12c8e3cfbbdace363d6653e49c7c5ca04167f4c42574bf57bc2cc784fdde6bba.
Actual computation: 0.004410802852362394 seconds.

## T4-113: Signed L2 rate trade and exact Gram thresholds

Date: 2026-10-29T00:43:51.030121+00:00.
Claim: T1's new FW-T-T4L2-bL-v1 corollary allows a positive signed L2 rate beta_L in place of2, with the displayed Gram and nonlinear conditions.
Method: Reconstruct the low and high inverse, contact-normalization and contraction arguments in audit record low_rate_trade_audit, proof. Independently check exact LDL pivots,22 rate-bracket rows, both rational parameter instances and the Schur-complement critical rates.
Result and verdict: CONFIRMED conditional on all stated background, residual membership and smallness hypotheses. Critical rates of this fixed Gram certificate are exactly3829321675/5037023232 for sharp weights and15208393675/44307283968 for sharpw. Safe sufficient decimal endpoints are0.76024 and0.34325. The statements that0.7602 or0.3432 themselves suffice are REFUTED by negative Gram tests. Neither threshold is an optimal operator rate.
The two sharpw instances are certified: beta_L=7/5,mu=359/1000,s=1/5476,r=1213/1000000,eta=423/2500000; and beta_L=1,mu=151/500,s=1/6561,r=459/500000,eta=533/5000000. Their contraction ratios are at most0.0196 and0.0229. Six floor-sensitivity brackets are arithmetic only; packet caps are upper limits, not sufficient global lower bounds.
Audited peer code SHA256: 96c09fbef4a781a66100bb268881bc89e1e56ff53cbcf139d6365ded4d068ac5.
Audited peer output SHA256: 57503e9f71c728c19508ebbb36c365778339e4eda7b71e9b4bfb3cddd0debe97.
Independent proof SHA256: 87e9dab70a60d1b603297657ddc53c799dcaf56f1dfdba059eecfa3c2abc228f.
Independent code SHA256: 2a9b09126361bf397a6009adcacff786e793b955e62a283a7d0bcb298a62442d.
Independent result SHA256: ab8d60034be3a4e4fb8f098f62aa94388c84bc229fffac097bb6b2c9d811922a.
Actual computation: 0.1076977108605206 seconds.

## T4-114: Independent acceptance of the inverse floor and state131 exclusion

Date: 2026-10-29T00:45:50.313610+00:00.
Claim: T4-097's actual inverse lower bound is independently valid, and the completed T4-097/098/099 chain excludes the original state131 reference from the T4-058 dyadic closure scheme for every a,s and finite low-weight radius.
Method: Read T1 R1-013 in full, including its independent canonical mode formulas, core-tail bounds, exact symbolic scaling and inverse-domain argument. Check the application hypotheses directly from the finite canonical generators, as written in reviews/APPLICATION_CHECK.md. Combine the audited inverse floor with independently reproduced complete-tail and interval-cover certificates.
Result and verdict: CONFIRMED. T4-097 is AUDITED under its exact stated hypotheses. The complete state131 scheme exclusion is now independently checked: outside2/c<a<1+1/c, membership or the positive low rate fails; inside it, all256 cells contradict the necessary residual ceiling. The closure-matrix entry for this reference and this scheme may be marked RULED OUT. This does not prove nonexistence of a stationary profile or exclude other high spaces.
Reviewed original proof SHA256: 1d195ca686dd2deae3df192344ebe5aeb01c5c92529999816242cc028da93bee.
Independent review SHA256: 3050ed5ebe1bbd8c0ba8b56315c5ab0678e79918380794877b87c2f0aa87d188.
Independent script SHA256: 3cb784332d8757d65414e657c604009f8fcc10c67fd24392dd7ae44b3a2a81a9.
Independent log SHA256: 53f5ad8dacdd4b02367b06d508299d446f5e7d27c9378992f29e181d5cd459d7.
Exact applicability note SHA256: 833a23ff5129c112f8d835782f7d641541439b453f67eb7b9073b80cda16a3c3.
The reviewer includes illustrative floating computations; none replaces the exact finite-structure proof or the directed N4/T4 tail certificate. Printed rounded ceilings in the review are not imported as rigorous decimal upper bounds.


## T4-115: Refined weighted weak probes

Date: 2026-10-29T00:49:00.736977+00:00.
Claim: The eight safe lower bounds in T2's refined weak-probe table are valid.
Method: Independently reconstruct the polar weak equation and exact quadratic forms, evaluate outward log-gamma moments, and compare with exact decimal rationals. This uses the now-audited T4-081 theorem.
Result and verdict: CONFIRMED for all eight rows. For state131 the lower bounds are0.000517550 at a=1,k=32768 and0.0001980444 at a=6/5,k=32768. For d2 they are0.007810675 at a=1,k=288 and0.004928906 at a=6/5,k=192. For Mpen2 they are0.02242667 at a=1,k=96 and0.01587303 at a=6/5,k=64. The005 k=0 checks give0.0061687217 and0.0064650914. All are strict necessary weighted correction distances, with no maximizing-scale or existence claim. Some numbers printed as lower endpoints in the peer log round upward; the safe main-table bounds listed here pass.
Proof SHA256: 4e0bef842d3bbdaec91b689cecef7630deabef09ceb39bdecfee6596188fa2b0.
Code SHA256: f63dcc7ed4dace338adb7a5bba19ccc0f528a79c1f88071222e35e8f44ebd600.
Result SHA256: 63ce176c7ebb937524c58ec0714731bb6b90cdc7335d702bdb38eb1616b6d6bf.
Actual successful computation: 106.67970874672756 seconds. An initial exact-decimal parser failure is preserved in verification/first_attempt_decimal_parse.log; it produced no numerical result.

## T4-116: Independent reproduction of d2 Laplacian norms and uniform comparison

Date: 2026-10-29T00:49:00.736977+00:00.
Claim: N4's Cartesian derivative computation independently reproduces T4-107 and confirms the uniform d2 numerical obstruction.
Method: Read the full independent proof and result. Freeze both and compare all21 point quantities and24 shared-cell quantities. N4 checks780 exact Cartesian-versus-polar Laplacians and23 complete squared groups with4704 nonzero moments.
Result and verdict: CONFIRMED for the numerical values and the independently positive seven-cell cover. All45 local comparisons pass. N4 evaluates the last endpoint at A=1+1/c directly, while T4-112 uses a Cauchy-Schwarz bound at7/4; both covers have minimum ratio greater than1.35446238584264. The original continuous inequality in T4-107 still needs T1/T2 theory review under Amendment v03, so the full d2 scheme exclusion remains OPEN pending that review. T4-097 is now independently audited.
Independent proof SHA256: 3cd51afe982f58ec20ea1399a86e0c6bec74430cf179c5ee2631adb642cb49cf.
Independent result SHA256: 85758c4e35b4f3d1e32c11b3bc63bded1b34eb4f7710afdbe7a4eb94d913744f.
Comparison record SHA256: 75177deac926ca559bde6dc25ebe3949fc44911eadf17a6bce823066ed7019f2.
Independent N4 computation: 323.57764422893524 seconds. This record does not claim an independent recomputation of N4's new endpoint value.


## T4-117: Independent coefficient-rounding audit of candidate007

Date: 2026-10-29T00:51:56.294862+00:00.
Claim: N4-096 correctly distinguishes the exact candidate from its binary64 coefficient realization and identifies the latter's nonintegrable residual tail.
Method: Convert the exact and rounded generator vectors independently by Rodrigues polynomials. Reconstruct density and stream function in polar form, check origin jets and the leading homogeneous residual coefficient exactly, and independently evaluate both point comparisons.
Result and verdict: CONFIRMED for all2982 coefficient realizations,421 changes, both canonical polynomial maps, exact origin normalization differences, the leading(1,0) sector, and all16 point-field differences. Its full-circle angular norm is approximately7.17546119048963e-13 and its exponent is427123167131315/4076476460239181>0. Therefore the rounded mathematical residual is not in full-plane L2. The strain changes by approximately-3.84680149284508e-15. The point residual differences are approximately-7.32482862878545e-15 at(0,1/4) and-1.41752196945947e-13 at(100,200).
The exact rational snapshot remains unchanged. This audit isolates coefficient conversion at exact c and exact generators. It neither attributes that realization to an unchecked executable nor bounds all floating evaluation errors. Higher forbidden-sector values from N4's table were not needed or independently reproduced here.
Proof SHA256: 3c80a2ff98e8fb8894c6eea0bddbbc2cd87827831ef2f6cfe1c33d69e6a10e72.
Code SHA256: 7d83ccb5943bdfca959bdd86a25b2f57fe1cb208bb1672c052083e7639c4a84a.
Result SHA256: 0b55e723b0ab59cec53c05207152e7e2eb6fd4236dac91fcdacb8f9d08aa5b8c.
Audited N4 result SHA256: 3f037063c124a28b318852b7c7919015b2b711fc176d7ac6807f09d721f1413a.
Actual computation: 6.630972252693027 seconds.

## T4-118: Independent radial Hessian mass audit of candidate007

Date: 2026-10-29T00:56:57.724829+00:00.
Claim: N4-097 correctly accounts for the full-plane and omitted regional contributions to the structured Hilbert-Schmidt bound for exact candidate007.
Method: Differentiate the exact canonical density independently in polar form through two Cartesian derivatives. Square the resulting pointwise modes, integrate each finite radial monomial exactly or with outward powers, and compare with N4's Cartesian method. No restricted-domain integration by parts is used.
Result and verdict: CONFIRMED. All17 interval comparisons overlap, the mixed derivatives agree exactly, and the complete rational energies match T4-111. The full bound is approximately0.72816468018232542728; the exact middle-region bound is0.72693924797277978454. The outer radius is2297010315299855/274877906944 and the inner radius1/50. The exterior contributes approximately0.336292393400837 percent of the squared bound; the origin contributes approximately0.00000545231465074 percent. The reported floating middle value differs by approximately-6.27e-13. This explains the discrepancy without certifying all floating evaluations or a global signed margin.
Proof SHA256: ca13cd9a621a4d815626770c4fa0bcbc4a2ce16fb0342f1c05db79fea19f5448.
Code SHA256: 55239885dadfad0d0195301bf213333c631bc58392529e99b240727c0d5d7e8f.
Result SHA256: 4b27411fd07396e00ed0529ce2402b8ec9e01d6f7e23538590add17739fcb70b.
Actual computation: 47.34187803696841 seconds.

## T4-119: State131 matrix-floor pinning and threshold-ceiling scope

Date: 2026-10-29T00:56:57.724829+00:00.
Claim: The P96 global floors and independently checked packet caps tightly bracket three state131 matrix infima, and quantify the maximum benefit within the fixed TP-5 Gram scheme.
Method: Check the three inherited P96 certificate identities, positive recorded bounds and exact rectangular covers, all9431 stored independent audit checks, and the independently reproduced point and Gram data. Optimize the radius and s algebraically, then evaluate the upper ceiling by outward arithmetic.
Result and verdict: CONFIRMED with inherited P96 global theorem. The intervals are[0.972875,0.99116),[0.587238,0.61151),[-1.230876,-1.20662), with widths0.018285,0.024272,0.024256. The possible E2-floor increase over0.5 is at most0.11151, whereas0.024272 is the increase over the improved P96 floor0.587238. The latter distinction is required in T2 Q2.
At beta_L=2 with all other constants fixed, the threshold ceilings are approximately0.000165554533577083 (sharp) and0.000380259638882139 (sharpw). Their ratios to the published thresholds are2.17209007697664 and1.80774727303132, giving safe bounds2.2 and1.81. Relative to optimized baseline Gram values the corresponding upper comparisons are2.16379931278502 and1.79918681507570. Thus TP-5's factor1.8 needs the optimized-baseline denominator; it is not established relative to the published2.1035e-4. The ceiling itself need not be attainable, so this does not refute a sharper1.8 estimate based on additional information. State131 caps do not bound d2's matrix floors.
Proof SHA256: 501331ef8a3fca857115a1c9ac2fe126121552dbc8c00f0bb1b25fda264c522d.
Code SHA256: b8b423ff440764ced1ca61de21ec738a511bdda7f07ac5c3fa621d3f612b6030.
Result SHA256: ad57279436fda4661b715e1bc324e8296a7e862ea1e20b8a0a00e06ab1843a0e.
Actual computation: 0.09869538713246584 seconds. The original P96 polynomial construction was not rerun; its existing global theorem is an explicit dependency.

## T4-120: Independent acceptance of the continuous plateau estimate and d2 exclusion

Date: 2026-10-29T00:56:57.724829+00:00.
Claim: T4-107 and the T4-112 seven-cell d2 comparison pass the required independent theory review.
Method: Read T1 R1-014 in full, inspect its independent analytic reconstruction and symbolic checker, freeze review/code/output, and match the exact reviewed proof hashes. Its toy quadratures are supporting checks; the independently directed T4/N4 full norms and cover remain the numerical certificate.
Result and verdict: CONFIRMED. T4-107 is AUDITED for Y exactly as defined in T4-058, with chi0=1 on r<=2 and chi=1 on1<=r<=2. It gives Y(h)>=5^((a-2)/2)||<r>^(2-a) Delta h||2 for0<a<2. The T4-097 inverse floor applies to d2 by its finite canonical decay structure; TP-3 supplies the required low-rate ceiling. Thus the completed chain rules out FW-T-DYADIC-Y-v1 at d2 for every0<a<2,0<s<1 and finite positive Rw. The certified seven-cell ratio is greater than1.35446238584264. This excludes one sufficient scheme, not a stationary profile or another high-space construction.
Independent review SHA256: 33513ce7d3ea000c58df52f1f37a92bec927b2154c1470df70bf749da45abf21.
Independent script SHA256: 5722485a34cd67d5ecc8dbddfc67de347df34270c542988462ae3c29b1e8c4b7.
Independent output SHA256: 3208fb4cddfeb8f51a268ec775beb77af5252410bc591c5dd88ea5a4da86256a.
The reviewed proof and cover hashes remain516e3d20063b96b21e073638fa532ff861e40c2231b6a7a1fff11e64983fa422 andc7253f73c992f0d87e1d90feb770f6d08ccf0c075935972ca6ef5db5cf9eaab4. Reviewer reported10.2 seconds for supporting checks. No new full norm computation was performed here.

## T4-121: Directed-decimal corrections

Date: 2026-10-29T00:56:57.724829+00:00.
Claim: Displayed decimals used as strict bounds must be directed correctly.
Method: Compare exact decimal rationals against the stored outward balls using512-bit Arb arithmetic.
Result and verdict: CONFIRMED correction to T4-106: the safe state131 a=7/5,k=2^26 lower bound is0.000163823854295506. The previously printed0.000163823854295507 lies above the computed bound and must not be used as a certified lower bound. The a=13/10 value0.000436835013298882 is valid as printed. T1 R1-014's sqrt(10 pi) is approximately5.60499121639793, so5.604991 is not a rounded-up ceiling;5.604992 is safe. Its test N1>=5.6050 remains valid. None of the scheme exclusions depends on the incorrect last decimal.
Evidence SHA256: 11294e8b3c3c3a57e19663b9c5760861a6eeee13b2eaf9f0c3f2663779a92396.
The first audit checker incorrectly expected the a=13/10 printed value to round upward and stopped at that assertion before writing results. Inspecting its full ball showed it was already safe; the corrected checker preserves that value and completes both checks.

## T4-122: Candidate007 exclusion from every original graded box

Date: 2026-10-29T00:57:49.283983+00:00.
Claim: N4-102 excludes exact candidate007 from every graded and gradedL2 box with the original positive top margin, as well as both sharper scalar balls.
Method: Independently eliminate s and all component radii from the margin by exact cubic maximization, reconstruct V and D rho from T4-108's point components, and evaluate the universal and five finite point bounds with1024-bit outward arithmetic.
Result and verdict: CONFIRMED. All21 comparisons agree. The uniform upper point bound is approximately0.02040423000582999 against residual0.09114328450165373, giving gap greater than0.0707390544958237 at(1/10,73/100). This excludes every original graded or gradedL2 box, including all allowed s and radii. Both sharper scalar balls and three specified finite graded instances separately have positive gaps. The result fixes c and the exact candidate; it does not exclude a scheme with a changed top margin.
Proof SHA256: 45f122037e7c559e8598e84dd7231b1cbd84aacc02f1cbbd525aa33c09c1fe5d.
Code SHA256: bcedbadc62db91601cde4c65d8973df813c646ec3158d16e6f182183ace26385.
Result SHA256: 0d3a627c1e14e75c0284ad8ddfc63838f4b2898c49df51a76e747484f5d8435f.
Audited peer result SHA256: 9c93792a0d2522fcc103cbaa2b18b717a445d9c091d86d1889af7374f7462ab9.
Actual computation: 0.0018943450413644314 seconds.

## T4-123: Finite stationary angular recursion through order sixteen

Date: 2026-10-29T01:03:54.033412+00:00.
Claim: N4-098's finite homogeneous stationary recursion has an invertible angular step at every order through16.
Method: Specify the exact potential and density spaces, prove closure under the polar Poisson bracket, derive the triangular density map, and check all1530 diagonal pivots with exact rationals. Inspect the complete N4 proof/code and freeze its independent N1 comparison summary.
Result and verdict: CONFIRMED for the finite analytic recursion and the scope of N4's existing independent numerical confirmation. At order j the potential space is span of cos(2m theta),0<=m<=10(j+1)-1, and the density space uses sin((2m+1)theta) over the same indices. The highest bracket frequency is20(j+1)-1. All pivots are nonzero, so each finite step is uniquely determined after the leading potential is fixed. N4 reports3060 exact coefficient equalities and13 exact forcing-energy comparisons; this audit does not claim a fresh third recomputation of all those coefficients.
The near-resonant order-eight diagnostic is OPEN pending independent review: s8=-116183978028673/4076476460239181, and the pure first-density-mode homogeneous velocity amplification is approximately49.9744537988431. The actual order-eight stream-mode2 contributions are approximately-12846.7990674824 and-91.83651971326. Its exact first-density coefficient identity passes. These are homogeneous exterior algebra diagnostics, not a whole-plane inverse estimate or an infinite-series convergence claim.
Proof SHA256: 3c24f87cef10cc0a758133174c87803c3022daebc1aa15982f9f7be4075c36e8.
Code SHA256: 863811aa1a6521c9c46762a2719fa5f58ffb062810f3138dcdd231750d8319c8.
Result SHA256: 8380a1c8aa0ef147e900fd0a81427372bdd2e44c7ff80faf97c3f361bd680a4e.
N4 summary SHA256: fd3e653204b4525964f904242989b91d1212899b507378422a22a312529e3ba6.
Actual local check:0.014537232927978039 seconds. N4's separate recorded recurrence computation took185.01869655400515 seconds.

## T4-124: Far-field spectrum and the limit of a transient prefactor

Date: 2026-10-29T01:07:07.863843+00:00.
Claim: T1 R1-013 remark3 correctly extends the far-field inverse-floor tests to a vertical approximate spectral line and a semigroup decay-rate ceiling.
Method: Independently construct complex logarithmic plateaux, retain all canonical velocity tails, prove their normalization and graph-domain properties, and derive the semigroup conclusion directly by an integrated domain identity.
Result and verdict: CONFIRMED for every explicitly stated closed Y realization containing these tests. The line Re lambda=-(1+c-ca) is in its approximate point spectrum. Any strongly continuous semigroup has norm at least exp(-(1+c-ca)t), so a finite transient prefactor cannot permit a faster asymptotic exponential decay rate. This is a statement about the specified Y, not an invariant normalized hyperplane or another space.
An extension, OPEN pending independent review, proves the normalized tests are weakly null in Y. Consequently every compact bounded perturbation has the same spectral obstruction and, wherever its resolvent exists, the norm is at least1/abs(Re z+1+c-ca). This includes finite-rank repairs and the stationary inverse floor at z=0.
Proof SHA256: 476187a50ed997bd1011c9375892b15f04ba6b382ba520bbafe7f74518e5078f.
Reviewed source SHA256: 3050ed5ebe1bbd8c0ba8b56315c5ab0678e79918380794877b87c2f0aa87d188.
No numerical spectrum computation was run.

## T4-125: Candidate008 point and uniform graded exclusions

Date: 2026-10-29T01:19:18.311529+00:00.
Claim: N4-106's exact candidate008 point fields and point exclusions are correct.
Method: Independently convert all exact generators by Rodrigues polynomials, match the canonical coefficient map exactly, reconstruct density and stream derivatives in polar coordinates, and compare eight Cartesian point fields and the five original finite-ball tests. Eliminate all original graded radii and s analytically and independently evaluate the universal bound and both sharper scalar balls.
Result and verdict: CONFIRMED. At(1/10,73/100), F is approximately-0.10616057879642431100. The uniform original graded/gradedL2 positive gap exceeds0.0858095924457140. The sharp and sharpw gaps are approximately0.09339781203515318 and0.08627754289146951. The five original finite-ball tests also have positive gaps. This fixes c and the exact snapshot, and does not cover altered top-margin constants. Eight further available peer comparisons agree after updating the reader for N4's changed result schema. The first reader attempt failed at a missing key and produced no certificate.
Exact point result SHA256: 095725184df8dd16bfb70f3c891f2283267ccc910d9822f82b58b9a19d23a15c.
Uniform proof SHA256: b7e59cc713b503ed626d377b7929008ed6828a3e2c53350a2c5df35d842ec6c7.
Uniform checker SHA256: 36e2e1c8e2f879d3078dfc2a925b5afd408a505370f691d3e819cfdfddf4dc7a.
Uniform result SHA256: 12df68f12415acdaaf8f19c5e35a3dff2bed05dbbece17468c38e841ea67e36a.
Audited point result SHA256: 3df50bd418a7822e1c841cba704fd8d55068b16d16aaf6acf9c8b45522257155.
Audited uniform result SHA256: 0bf1258ddfde9a6ea2f1864e995b629d2de815a9982e07ac9a86fd4f77bb9f4c.
Actual successful calculations: 3.920611510053277 seconds for point fields and 0.001953416969627142 seconds for the uniform comparisons.

## T4-126: Candidate008 exact background seminorms

Date: 2026-10-29T01:19:18.311529+00:00.
Claim: N4-107's complete-plane background norms and structured Hilbert-Schmidt value are correct.
Method: Independently construct the polar Laplacian and Cartesian Hessian difference, evaluate exact rational beta integrals and compare all four rational energies with N4's Cartesian derivative calculation.
Result and verdict: CONFIRMED. All four exact rational energies agree. The norms are approximately ||D2 rho||2=19.64773757943722202, ||D3 rho||2=349.86204752506547725, ||D rho_x||2=6.835140192840438773 and ||D rho_y||2=18.42048996456518791. The full-space structured Hilbert-Schmidt value is0.84604142762615305206, greater than c-1 by more than0.0357221. Hence the sufficient criterion using this full-space bound cannot give beta_L=2, even with theta=0. This value is not a lower bound on the actual S1 operator norm and does not exclude a sharper signed certificate.
Proof SHA256: 52355ab5d054e3390ec6b322cf89054e1e5c2b53b8a9c2824461cb0825f28161.
Checker SHA256: 1b5c95566b0b4e705bc9a800a0008c74032ef47f059bd2bd4af43b00d2a7d010.
Result SHA256: 934e35fafbc1d312163b4353fc56e419e011eefc1dce2979fb8059aa3065ff62.
Audited N4 result SHA256: 77881459abceec3f0c8be5a34c3f1a509969fe11761ecb0d4d1ce51ded2fe216.
Actual computation: 245.06043270090595 seconds.

## T4-127: Selected angular Laplacian modes for candidate007

Date: 2026-10-29T01:19:18.311529+00:00.
Claim: The first and third angular modes alone exclude the dyadic sufficient scheme for candidate007 at every a>=4/5 in its admissible range.
Method: Construct the exact residual angular projection from the canonical potential, retain all radial-branch cross terms, apply the radial Laplacian and integrate the weighted square by exact finite moments with2048-bit outward arithmetic. Use the audited continuous plateau inequality and four monotonic cells.
Result and verdict: OPEN pending independent reproduction of the new moments. The four cell ratios exceed1.01380000134458,2.23154592959989,9.40192511453420 and393.749117877902, respectively. The cells are[4/5,1],[1,5/4],[5/4,3/2],[3/2,1+1/c], with the last norm conservatively evaluated at7/4. The first two mode norms at a=1 are approximately5.45984845624946 and12.6289833138820. Modes5 through15 are also retained but are not needed for this cover. If independently confirmed, only0<a<4/5 remains open within this one scheme; no whole-parameter or existence claim is made.
Proof SHA256: e5b3dbd420cea877227be70f3e6042035058de7d976624e4ab44ea07bb100969.
Cover proof SHA256: 8e2ad1911d19729a6aee4614ce01347756bd761356efe3ba3ee4bd975ced77c4.
Mode checker SHA256: 4908f506a52f42792902641952a5d9e6bf84ac23ac9ee5f0b0acc08cb4c9eb27.
Combined result SHA256: bd5a33163064e077c0b145f27837c853762651dfe0f3ab85dedf35dfa6a6e0f1.
The result records each mode input hash and actual per-mode runtime. The combination itself took 0.004055156372487545 seconds.

## T4-128: Symmetry-resolved commutator energy budget

Date: 2026-10-29T01:19:18.311529+00:00.
Claim: A certified even-even compression can improve the full-space Hilbert-Schmidt bound on the S1 commutator, without a kernel truncation or a finite-section inverse inference.
Method: Prove that the double commutator preserves each parity block. Subtract the finite even-even block's exact squared Hilbert-Schmidt norm from the known full-space budget. Derive an exact radial Poisson basis and its rational beta-integral compression formula.
Result and verdict: OPEN pending independent theory review. For positive Gram G and Hermitian compression B on any finite even-even family, the S1 operator norm is at most sqrt(kappa^2-tr(G^-1 B G^-1 B)). The new radial family h_n=-Delta(partial_z^n(z^2+r^2)^(-1/2)|z=1) has exact rational G/pi and B/pi for the canonical profiles. This is a possible sharper low-space certificate, not a high inverse or closure theorem. Candidate arithmetic is in progress.
Proof SHA256: 4780ff82c8b361ffbc7e0e7de97126aad09fdb758aa6fb0cd430b632c959a479.

## T4-129: Exact radial parity-compression calculations

Date: 2026-10-29T01:22:54.477779+00:00.
Claim: The radial Poisson compression in T4-128 gives a smaller S1 Hilbert-Schmidt upper bound for the exact profiles.
Method: Form Gram and commutator matrices as exact rational beta sums, check every Gram pivot by rational LDL and every constant-gradient cancellation, and compute tr(G^-1 B G^-1 B) exactly before outward conversion.
Result and verdict: OPEN pending independent theorem and numerical review. For008, dimension32 captures approximately0.05135858380804771 and reduces the S1 upper bound from0.84604142762615305 to0.81512423191293452. It remains above c-1 by about0.0048050. At dimension12 the improved upper bounds are0.70463578768349055 for007,1.33241631458180091 for005 and0.68630823487828082 for d2. These are only improved sufficient low-space estimates, not actual operator norms or closure certificates.
Proof SHA256: 4780ff82c8b361ffbc7e0e7de97126aad09fdb758aa6fb0cd430b632c959a479.
Code SHA256: 09e1ea9a63d0b0b1656b24aa5190804fb2d8adc2842ad478cdf51f6a02cd9743.
Candidate008 dimension32 result SHA256: d13abf740386450aace79aa085b758033d51f759ecfdf3cfa280d4b143128929.
Actual008 dimension32 computation: 22.143807793967426 seconds. Each other result records its own runtime and exact inputs.

## T4-130: Angular parity budget and exact complementary blocks

Date: 2026-10-29T01:22:54.477779+00:00.
Claim: Several even-even, odd-even and odd-odd Poisson derivative compressions can be subtracted simultaneously from the full commutator Hilbert-Schmidt energy to bound the S1 block.
Method: Extend the parity proof to three orthogonal reducing spaces. Compute rational Cartesian test fields, integrate the exact signed bilinear form by parts against rho, and evaluate every full-plane angular and beta moment exactly. Compare the radial subblock with the separately derived radial formula.
Result and verdict: OPEN pending independent review. The first008 run has four radial derivatives for each angular mode through4, using28 tests in three blocks. It captures approximately0.03375417565102946 and leaves the S1 upper bound0.82585223957356301. All150 constant-gradient cancellations and20 radial comparisons pass; all Gram LDL pivots are positive. The method improves monotonically under nested spans, but no quantitative rate of convergence is asserted. A larger run is in progress.
Proof SHA256: ba67a0a6eec32724ac12fffca0f43c54489b3f975bde29566fecd2f01114ffa6.
Code SHA256: 5c5504588df39ca4512886e0ea476ddfc156b9424aca9fdb2d030ec6bba472ab.
Result SHA256: 93f8a66e865f748715d0c9455289642f8ec528e2440593d8e087a655995acbc9.
Actual computation: 12.709764454048127 seconds.

## T4-131: Graph-compact perturbations and approximate inverse scope

Date: 2026-10-29T01:25:38.088932+00:00.
Claim: T2's R1 to R3 extend the far-field singular sequence to graph-compact perturbations and bound approximate left inverses. T2 independently confirms the compact extension in T4-124.
Method: Prove graph-compact perturbations have relative bound zero and preserve closedness; use graph-weak convergence of the singular sequence; derive the approximate inverse inequality directly. Check the closure interpretation with two elementary operator examples.
Result and verdict: CONFIRMED for R1, R2 and R3 with the domain and graph conventions stated in the standalone proof. T4-124's weakly-null, compact-perturbation and resolvent extensions are now AUDITED through T2's independent review. A raw approximate inverse bound ||B|| is not an effective inverse bound: compact defects still require a finite-dimensional check, and a small-norm defect costs the factor1/(1-||D||). The review's section5 is only a weaker necessary comparison under independently established closure hypotheses; it proves no threshold improvement. The a=1/2 row belongs to the already proved0<a<2 range; a=0 remains outside.
Source SHA256: fb3ef35192feaf306af8544a4a26f32ff4ede2c4cad652dd5f3f6865932e1578.
Audit proof SHA256: cb72b6a25e4b97ad55606a8c72fe88f94b81beb8bae2caf81058d39696e4a48c.
No computational result is asserted.

## T4-132: Eighty-test complementary parity calculation

Date: 2026-10-29T01:28:22.774258+00:00.
Claim: The80-test compression improves the sufficient S1 commutator bound for candidate008 below c-1.
Method: Exact rational full-plane beta moments in the three complementary parity blocks, rational Gram LDL checks, then1024-bit outward conversion.
Result and verdict: OPEN pending independent theory and numerical review. The captured squared norm is enclosed about0.06378177122889545591, leaving an S1 absolute operator bound0.80746784829540037660. This leaves only0.00285136190459770904 for theta if beta_L=2 is wanted. All1128 constant-gradient identities and72 radial comparisons pass. This is a sufficient low-space bound; it does not undo candidate008's residual exclusion.
Result SHA256: b031e806d6cd64016fab3b8ce4d5594ccd2f8ab0403ecf6c5a9996e57b81249a.
Code SHA256: 5c5504588df39ca4512886e0ea476ddfc156b9424aca9fdb2d030ec6bba472ab.
Actual computation:110.95017575006932 seconds.

## T4-133: Signed S1 compression budget

Date: 2026-10-29T01:28:22.774258+00:00.
Claim: A finite S1 compression can improve the quadratic-form upper bound by accounting for all its squared eigenvalues except the largest positive one.
Method: Apply the compact self-adjoint min-max principle separately to positive and negative eigenvalues. Prove a rational generalized eigenvalue upper bound by qG-B positive semidefinite.
Result and verdict: OPEN pending independent theory review. If T_other is the captured complementary-parity energy, T_H=tr(G^-1 B G^-1 B) for an S1 compression, and q>=0 satisfies qG-B>=0, then <Kh,h> <= sqrt(kappa2-T_other-T_H+q^2)||h||2^2. This is a signed upper bound, not an absolute operator-norm bound. It improves the low generator rate under the previously stated complete-transport assumptions, but provides no high inverse or nonlinear closure alone.
Proof SHA256: 8f12e7acb992aa8942e4168aa093309b5f711023f1160fa075caafb6e721b88b.
The proof precedes its new numerical application.

## T4-134: Independent order-eight small-divisor confirmation

Date: 2026-10-29T01:30:21.027770+00:00.
Claim: N4-109 independently confirms the1530 finite-angular pivots and all six new order-eight diagnostic quantities from T4-123.
Method: Inspect the independent polar differential algebra path, its exact potential data comparison and its768-bit outward comparisons; freeze the proof, code and result and verify their recorded hashes.
Result and verdict: CONFIRMED. N4 uses its own stationary recurrence coefficients and angular differential operations, not the T4 diagnostic implementation. All1530 pivots,17 minima and six outward intervals agree. The pure first-mode velocity amplification49.9744537988431 and the actual second-stream-mode coefficient about-12938.6355871957 are now independently confirmed. This establishes finite homogeneous algebra only, not an infinite expansion or a full-plane norm lower bound.
Independent result SHA256: 1ac0db861aa817b92ba12aecddc3ed2f944f8c2efebb2316df54a038037d0383.
Independent code SHA256: 57f9ba0a46e919ca1c9a821d06afa915ee321e434ec390532bdbfc0a35906c8d.
Independent proof SHA256: 18bbc3e470c3c66cbc446e656e908d23bd851441cfa52ee3d966d469f24a8b18.
N4's recorded actual computation: 0.2942722961306572 seconds. T4 did not rerun that code during this acceptance check.

## T4-135: Sharp order of the shell approximation

Date: 2026-10-29T01:30:21.027770+00:00.
Claim: T2's improved shell upper bound and its matching fixed-mode lower bound are valid. Its independent review confirms T4-056 estimate(4).
Method: Redo the radial fundamental-theorem estimate and compute the core and shell energies of T2's explicit dual test.
Result and verdict: CONFIRMED. The upper constant is sqrt(T epsilon)*sqrt(T/(T-epsilon))*m_(1/2)||mu||2; for a fixed odd mode n the lower constant is m_1 sqrt(T epsilon)||mu||2 divided by sqrt(1+n epsilon/T+2n^2 epsilon^2/T^2). Thus the epsilon^(1/2) order is sharp. The T4-056 shell approximation is now AUDITED. These claims do not prove a new constrained joint(H,L2) minimum or an IPM candidate bound.
Source SHA256: c1b96ddad1ea21c4d55f418d16ec19b4bce18d55203f7ea099a5dc1d968b5352.
Audit proof SHA256: dcfeb0264f8b659f9e6452d9fb2416ee1e0c391129317bdb16fd8774f482adb0.
No numerical experiment was needed.

## T4-136: Independent candidate007 selected-mode confirmation

Date: 2026-10-29T01:35:30.380156+00:00.
Claim: N4-113 independently confirms T4-127's first- and third-mode weighted Laplacian values and the continuous four-cell exclusion.
Method: Inspect the independent Cartesian projection and differentiation, its exact check against the polar Laplacian, all branch cross terms and finite weighted moments. Freeze the review and verify the proof, code and matching original input hashes.
Result and verdict: CONFIRMED. The sixteen selected-mode norms and all four strict cell ratios agree. The registered dyadic sufficient scheme is excluded for every4/5<=a<1+1/c for candidate007; at larger admissible a its required positive rate already fails. The range0<a<4/5 remains open in this scheme. This does not prove nonexistence or exclude another high space.
Independent result SHA256: abb29b532d5b43043b8b26a22851928281f3835f45af164792305b59c4ae3501.
Independent proof SHA256: d25cb90a24b9977b0280adea1342c7d28c709b57d86f8f1378598f18b7b68437.
Independent code SHA256: 553a29c3932105381f6cf1558be382bd6120f6c30339974508a6f0825f59d833.
N4's actual computation: 241.1777310599573 seconds. T4 did not rerun it during acceptance.

## T4-137: Independent radial compression confirmation

Date: 2026-10-29T01:35:30.380156+00:00.
Claim: N4-116 independently confirms candidate008's radial compression through dimension12.
Method: Inspect the independent Fourier Gram formula, Legendre-Rodrigues construction and direct density-gradient pairing, which does not use T4's density integration-by-parts formula. Freeze and hash-check the review, matrices and original dimension12 input.
Result and verdict: CONFIRMED for this finite compression and its arithmetic. All Gram and commutator entries and all five captured energies at dimensions1,2,4,8,12 agree; the Gram pivots are positive. The dimension12 remaining bound is0.8258163504343835904. This review does not certify the dimension32 matrix, angular matrices, signed extension, theta cover or low-generator domain hypotheses. T1/T2 theory review remains requested for the new route.
Independent result SHA256: da744765a77bb43da2e65ecc96f51451cdc44ab43ba7ab930e32ce791049f34f.
Independent proof SHA256: a9c0928bf70535e43df0b6e4462ac9d0b6f1d293011f782b15ddb0d79cab61ae.
Independent code SHA256: bb8c892a16072b2ef026edfd25b6ca9c0b90939fd87d86e40974b2a55c9f0717.
N4's actual computation: 16.6001715073362 seconds. T4 did not rerun it during acceptance.

## T4-138: Union of overlapping compression spaces

Date: 2026-10-29T01:35:30.380156+00:00.
Claim: Completed angular and radial compressions can be combined without double counting their common radial block.
Method: Decompose two commuting orthogonal projections into their common and disjoint parts, and count each squared Hilbert-Schmidt matrix entry once. Different Poisson angular harmonics are orthogonal, so the completed spans satisfy the commuting hypothesis.
Result and verdict: OPEN pending independent theory review. For commuting finite-rank P,Q and R=PQ, the quantity ||PKP||HS^2+||QKQ||HS^2-||RKR||HS^2 is bounded above by ||K||HS^2. Thus T_union=T_angular(N,M)+T_radial(d)-T_radial(N), d>=N, can replace the old complementary energy. The omitted off-diagonal blocks have nonnegative energy. No calculation or low-rate success is asserted in this entry.
Proof SHA256: 866f80f6cfdd68f3e1b1b4ca072c315319c5cba73d61fe5b23b4e06431e7bd14.

## T4-139: Independent signed-compression review and origin semigroup extension

Date: 2026-10-29T01:39:17.514139+00:00.
Claim: N4-118 independently confirms the abstract signed-compression theorem T4-133. T1 R1-015 confirms the analytic part of T4-127.
Method: Read and freeze both independent proofs, verify the N4 source and review hashes, and check that the scope excludes an absolute-norm interpretation and a new generator theorem.
Result and verdict: CONFIRMED. The signed spectral-budget argument is independently audited conditional on its exact HS, matrix and PSD hypotheses; the larger candidate-specific calculation is still incomplete. The selected-mode007 dyadic exclusion is also AUDITED through Opus T1 R1-015 as well as the N4 arithmetic check accepted in136. No stationary inverse or existence follows from either.
N4 review proof SHA256: fd16bb0021f3b8c85efaa791a2ab2d1245e04fcb6b2b655a16234c04e18798ca.
N4 review record SHA256: 45ccd25ba87ea90d1834e33754fe89161d8d44d7516a55271601833777b43021.
T1 R1-015 SHA256: a36dc30e7131847789a8eecd76f968bdaf01edc9da94f34686410273c87c5c30.

## T4-140: Origin lower bound for Sobolev semigroup growth

Date: 2026-10-29T01:39:17.514139+00:00.
Claim: In an H^q Sobolev realization satisfying the stated smooth-domain and generator hypotheses, the origin condition gives ||S(t)||>=exp((q-c-1)t) even with bounded finite-dimensional pinning and compact perturbations.
Method: Solve the frozen origin operator exactly in Fourier variables, choose a narrow vertical cone, scale it into the origin, normalize with a bounded finite-rank projection, and estimate the exact model residual by dominated convergence and Duhamel.
Result and verdict: OPEN pending independent theory review. A bound ||S(t)||<=C exp(-beta t) with finite C would require beta<=c+1-q, also under equivalent norms. Unlike the earlier numerical-range test, this proposed result addresses a finite transient prefactor. It does not assert a stationary inverse obstruction, a spectral eigenvalue, or a result for the dyadic graph norm Y. All generator, smooth-test and domain hypotheses must be matched before applying it.
Proof SHA256: d7fa58cbcce2cdd452b293c25cf251285aa3b661d1bbae7bda37aeaa0e59765a.
No numerical computation is used.

## T4-141: Combined angular and radial compression

Date: 2026-10-29T01:40:50.326320+00:00.
Claim: Adding the completed dimension32 radial space to the completed80-test angular spaces improves the candidate008 S1 bound.
Method: Verify the same canonical hashes and all128 common radial Gram/coupling entries, then add the exact captured energies and subtract the exact common dimension8 energy using T4-138. Convert outward at1024 bits.
Result and verdict: OPEN pending independent dimension32 arithmetic and combination review. The union captures0.08823916327399040282 and yields the sufficient absolute S1 bound0.79217859980291614159. The remaining theta budget for rate two is0.01814061039708194406. This is neither a theta certificate nor a closure claim.
Result SHA256: 21269de39eebfde69baf761bafe14c06495b5a2eef1b3126b7616d8abc6415cb.
Checker SHA256: 90ec77f3e155615d746cd9649c7a26101d963eccc5905a2bde21c9aea2585d71.
Actual computation:0.6386117548681796 seconds.

## T4-142: Independent angular and overlap confirmations

Date: 2026-10-29T01:40:50.326320+00:00.
Claim: N4-119 confirms the28- and80-test angular matrices; N4-120 confirms the overlap-compression theorem.
Method: Read the independent Fourier Gram and direct Cartesian-gradient derivation and implementation, freeze both results, verify their code/proof and original matrix-input hashes. Independently check N4's proof using commuting projections on the Hilbert space of Hilbert-Schmidt operators.
Result and verdict: CONFIRMED. All300 and2256 lower-triangle Gram/coupling checks agree for the28- and80-test runs; all exact traces, positive Gram pivots and outward bounds agree. T4-130 and132 finite arithmetic and parity subtraction are independently confirmed. The union lemma T4-138 is independently confirmed, including its Poisson nesting. The new dimension32 radial value and signed matrix PSD are separate obligations. The overlap lemma in fact needs neither finite rank nor self-adjointness of K, though the numerical application uses both.
Angular80-test result SHA256: f8cc1d4511a08965c070092a37a0a28b826559e1ff4c67d300088a88ac160257.
Angular review proof SHA256: 1bac5bf63249fb1773badcfd9a47dcf1f35e01f80fd479dacf9e1e35cb6d9b39.
Angular checker SHA256: 96d656d7436239773d4c81c9baa1de7abbbd4c95662a044d08b2fdd7eb68f232.
Overlap review proof SHA256: f10a79845345f6f38c52d102f55bb42517dfab58f2bffed86f8838faf53c7860.
Overlap review record SHA256: 0299a22265deeb424063ceeae9a8969e87459a9b4ea3d87b10f1d7c930193015.
N4 actual runtimes:50.37226061988622 seconds for28tests and293.8337672846392 seconds for80tests. T4 did not rerun them during acceptance.

## T4-143: Outward signed-compression certificate

Date: 2026-10-29T01:41:28.392818+00:00.
Claim: The32-test S1 compression improves the signed bound for candidate008.
Method: Reassemble the exact rational matrices, freeze them before the spectral stage, use exact Gram LDL congruence, and verify all32 positive pivots of qI-C by1024-bit outward LDL. The floating eigenvalue only proposes q. Combine with the complementary blocks and, separately, the radial union.
Result and verdict: OPEN pending independent matrix and PSD review. Exact q=4615759/200000000 bounds the largest positive compressed eigenvalue; target energy is0.01000643890021374070. The angular-only signed bound is0.80158001341677800167. With the dimension32 radial union it is0.78617626895254670632, leaving theta<=0.02414294124745137932 as the sufficient condition for low rate two. No theta cover or high inverse is supplied. The signed theorem and union lemma have independent abstract reviews, but the new numerical inputs remain separate.
Signed result SHA256: 1a9760f75c476c2ddb4843ac706d0347d782e1877baf098df352032a6d6d2444.
Signed checker SHA256: d831552e02a20e075cf49fedc776b13e9a82bc24bbf0ea523f67c2c14b3f8678.
Outward-LDL proof SHA256: 23b54db4046237779d10b36efeb315d55aceac1d361ac1a903a5dc256e5d8ee7.
Combined result SHA256: da52d2c938fe0e7162df61c77b2de2f8f087445d16b5c2b848a4e94eea410926.
Actual signed calculation: 80.28893486596644 seconds. The final combination took0.7126292218454182 seconds.

## T4-144: Independent candidate009 point and graded exclusions

Date: 2026-10-29T01:45:11.433211+00:00.
Claim: Candidate C1-N1-009-d2w-j7-x3balk fails the listed scalar balls and all original graded boxes covered by the uniform one-point theorem.
Method: Reconstruct the exact Rodrigues coefficient map and polar density, velocity and gradient independently; compare all eight point fields and five original ball tests. Apply the previously audited universal graded-budget theorem at1024 bits, with two additional sharp scalar tests and three explicit graded boxes.
Result and verdict: CONFIRMED. At (1/10,73/100), F=0.0607853489257176873687951125716. All coefficient and field comparisons agree. The uniform original-graded positive gap exceeds0.04041970196032596. The two sharp and three explicit graded tests also have strictly positive gaps. These exclude nearby fixed-c solutions only in the precise balls or boxes tested; they do not exclude the profile problem or all possible correction spaces.
Point result SHA256: 31a9731c5bd17ce900d6721480c15e951ba59d920b4e970f9d84121c8a5e5a6b.
Graded result SHA256: 64dd84839945d7a402526e0669d72d238629b131201720b48ebe6a102242f03b.
Exact generator SHA256: 0d6bddf6a80fcab5afa00efa6989b28b98bf8f43d54493874b8d0d3d4bf98a6c.
Actual computation:4.231185887008905 seconds for the point reconstruction and0.00219983933493495 seconds for the graded comparisons.

## T4-145: Origin singular spectrum and a possible H3 inverse obstruction

Date: 2026-10-29T01:47:38.807833+00:00.
Claim: On the explicitly stated H^q Sobolev realization, the frozen origin gives singular sequences on the lines Re lambda=q-c-1 and Re lambda=q(2c-1)-c-1-a0. When the second line lies to the left of the first, the entire intervening strip has such sequences. Bounded finite-dimensional pinning and compact H-to-H corrections preserve them.
Method: Conjugate the frozen Fourier operator by logarithmic frequency coordinates and the exact homogeneous Sobolev weight. Build compactly supported approximants to constant-coefficient packets at either end, and to an explicit L2 eigenfunction in the interior strip. Rescale each fixed test into the physical origin, then apply bounded pinning and compactness.
Result and verdict: OPEN pending independent Opus theory review and separate realization checks. The proof gives inverse lower bounds and, conditionally on a generator, a finite-prefactor semigroup obstruction. It predicts no bounded stationary inverse on a pure H3 realization when1<c<=2 and a0>=5c-4. It does not yet apply to weighted high energies or the Y graph norm, and does not rule out the profile problem.
Proof SHA256: 61be7efac561247a90520522fbbf1a67883ac600ee37062571f5c6c5b018558a.
No numerical computation is used.

## T4-146: Origin transfer to the actual dyadic inverse hypothesis

Date: 2026-10-29T01:51:38.178470+00:00.
Claim: Under the explicit smooth normalized background hypotheses and1<c<2, a0>=5c-4, the actual dyadic high inverse estimate(H) forces s<c-1 and M>=1/(c-1-s).
Method: Prove a shrinking-packet limit for the full Y norm, including the canonical velocity and all exterior shells. Control the velocity tail using mean-zero kernel cancellation with the local/contact term retained. Pin the strain exactly and use (Lh)_y(0)=a0 c[h], so the test forcings lie in the actual hyperplane f_y(0)=0. Use the frozen singular strip of T4-145 and low maximal-domain injectivity.
Result and verdict: OPEN pending independent Opus review. The resulting necessary residual ceiling is Y(F)<H(c-1)(1+c-ca)/(1+a), where H(d)=max_(0<s<d)(d-s)sqrt(4 pi s(1+s)) and its exact maximizer is stated. This may strengthen the remaining small-a007test substantially. No numerical exclusion is yet claimed.
Proof SHA256: ad3ce419d8c06eab03bacde165e4a1f90cb2e0b559587feda4444bfe4d537d4c.
No numerical computation is used.

## T4-147: Candidate007 complete parameter cover using the origin inverse floor

Date: 2026-10-29T01:54:57.535096+00:00.
Claim: The proposed origin inverse theorem excludes candidate007 from FW-T-DYADIC-Y-v1 for every0<a<2,0<s<1 and every fixed positive low-weight radius.
Method: Independently reconstruct the exact origin slope and strain from the rational polar density and stream function; check smooth monomial orders, normalization,1<c<2 and a0>=5c-4. Use the previously independently certified mode1 and mode3 Laplacian norms, with seven monotone cells and an outward proof that H(c-1)<57/50.
Result and verdict: OPEN pending Opus acceptance of T4-145/146 and independent reproduction of this arithmetic. All seven cells pass; the minimum ratio is1.23427738878510651005 on[0,1/4]. The exact reconstructed a0 is10.31199902106439505; H(c-1)=1.13023563884066332482. Thus the previously open small-a range would close if the analytic transfer survives review. No unconditional exclusion is asserted yet.
Application proof SHA256: 05c74ce4976dfa510af9d585c792ca166da8448afa60df8d87970ce277d4e9bf.
Result SHA256: ce0e842c6322813b335bfa69df262f5edbf56c585d6edcb26032a117ba01f4b7.
Checker SHA256: 005d221e862d699f0d78ca198f7c49be756717fa60bc99d19fc307462f5a9d51.
Actual computation: 2.9210587460547686 seconds.

## T4-148: Scope correction for the dyadic transient-rate cap

Date: 2026-10-29T01:57:34.479986+00:00.
Claim: theory_v02 lines347-349 infer that rate-one transient routes must be posed outsideY from the far-field cap beta<=1+c-ca.
Method: Substitute0<a<=1 into the exact cap and compare with the stated rate1 in(L).
Result and verdict: REFUTED as an inference from that cap. The cap permits rate1 when0<a<=1, with equality at a=1. It excludes that rate only for a>1. This does not prove an actualY semigroup estimate or change the registeredL2 theorem. The proposed origin cap is a separate necessary condition.
Target theory_v02 SHA256: 45b735907cf4c9c487c611c30b8c23e7aee7f1efde191f84ff42a7449e986758.
Standalone audit SHA256: 406f59e3e7a74818e5e9c89bb4ee877f716f7359e5490c674792b2afeddd38e1.
No numerical calculation is required.

## T4-149: Independent multiscale background-decay audit

Date: 2026-10-29T01:57:34.479986+00:00.
Claim: theory_v02 section8's new candidate010 legqs terms preserve the finite-angular T4-097 decay assumptions.
Method: Independently express each multiscale term as r^(2p_j-8) times a bounded logarithmic-radial symbol and a trigonometric polynomial. Prove all Cartesian and logarithmic derivative estimates by induction. Check the exact snapshot metadata and generator definition.
Result and verdict: CONFIRMED. The exact snapshot has1322 mono,1660 leg and960 legqs terms. Every new term has Q=4,R=10or100, j=0..3,m=0..9,w=0..5,n=0..11. Its contributions to u/r and D rho decay like r^(-delta-jdelta-8), with all finite logarithmic derivatives. The complete background therefore satisfies the T4-097 decay hypothesis at the original delta. Positive-order background derivatives are also bounded. Center normalization, mandatory sectors, matrix bounds and residual norms remain separate obligations.
Proof SHA256: 59170efcff708fafef89f46e808867d7292f5685b39075b2ff5d0867e0d42d80.
Metadata record SHA256: 1073b4c0bb19fe3f35932b09c25afbaa4242c86278f67203c03ba405ddd7ef41.
Coefficient source SHA256: 2341ac50f06d89f6a0dbdf0f27a0e40449edcb62ca772ac66a155e0b7c3fb615.
Actual metadata check: 0.08425009809434414 seconds; no quadrature or background computation.

## T4-150: Independent confirmation of the complete007 scalar cover

Date: 2026-10-29T02:01:10.690791+00:00.
Claim: N4-128 and N4-129 independently reproduce the origin coefficients, optimized ceiling and all seven cells of T4-147.
Method: Read the complete independent quartic-potential origin calculation, exact derivative identity for the ceiling, monotone cover proof and peer comparison. Freeze both outputs, proofs and all named inputs; verify every input hash. Check the nine-point analytic review separately from the required Opus review.
Result and verdict: CONFIRMED for the arithmetic and conditional scalar cover. The exact origin slope and strain agree. All32 scalar comparisons agree, and every cell has positive margin. The minimum ratio is1.23427738878510651005 with the rational upper ceiling57/50, or1.24494059013952763517 with the directly enclosed maximum. The whole007 dyadic-scheme exclusion remains conditional on independent acceptance of T4-145/146. N4's positive analytic review does not replace that required Opus review.
N4-128 output SHA256: e6aa97a5cfdea1ccef7fdd55d76df3ea3997c601112c311bbde7c8a3e6886961.
N4-129 output SHA256: 386c2be63f3ef9fc2ae4df412b87d2e4c4b3162a22d16679302c6c25d8f1b16e.
Frozen bundle: audit/theory_audit/research_code/origin_dyadic_inverse/reviews/N4_0128_0129/MANIFEST.json.
N4 actual arithmetic runtimes:0.048937 and0.030445 seconds. This acceptance did not repeat the arithmetic.

## T4-151: Independent confirmation of the008 extended compression certificates

Date: 2026-10-29T02:01:10.690791+00:00.
Claim: N4-124 to N4-127 confirm the dimension32 radial matrix, overlapping angular-radial union, signed target matrix and combined signed bound.
Method: Read the independent Fourier Gram and Cartesian-gradient pairing constructions, exact trace calculations, direct outward LDL proof and combination code. Verify all named input hashes and freeze the34-file bundle. The independent signed check operates directly on qG-B at2048 bits, distinct from the original orthonormalized matrix test.
Result and verdict: CONFIRMED for the finite arithmetic. All radial and target matrix entries and exact traces agree; all32 direct signed LDL pivots are positive for q=4615759/200000000. The union absolute S1 bound is below0.792178600 and the combined upper quadratic-form bound is below0.786176269. Its low-rate-two theta allowance exceeds0.02414294. This is a one-sided quadratic-form bound, not the same absolute operator-norm bound. Full-plane theta, generator hypotheses and high inverse remain separate obligations.
N4 outputs SHA256: radial26ebdecd3bbce36b196b7abf5271d9ba0d38b0db43b0251a27c4fc9a71b16acf; union8035e3f39d3bb57a1a2f785ece7acfb1e1c2673b815951368f68705b94bb85d7; signed631270a399a4674f9955f679b57aa74b343f92678f2f2b44b16e6aa085e64b09; combinede3bf5929268303ff13c1cdd7d0b388259adf03adee0adb2af67c69cd23afdae9.
Frozen bundle: audit/theory_audit/research_code/nested_compression_union/reviews/N4_0124_0127/MANIFEST.json.
N4 completed runtimes:56.044829,1.203599,145.375522 and1.096335 seconds. T4 did not rerun these calculations during acceptance.

## T4-152: Opus acceptance of the compression theorems

Date: 2026-10-29T02:01:10.690791+00:00.
Claim: Opus R1-016 independently confirms the abstract and exact-formula parts of T4-128,130,133 and138, including BALL_LDL.
Method: Read the full ten-step review and its exact symbolic checks. Verify all five reviewed proof hashes and freeze the review, script and output. Check its self-adjointness and reflection argument, nonorthogonal compression formula, min-max signed subtraction, congruence proof and commuting-projection overlap count against the original claims. The randomized illustrations are not used as proof.
Result and verdict: CONFIRMED. The listed abstract results and formulas are AUDITED under their explicit hypotheses. Together with T4-151 and the independently confirmed008 Hilbert-Schmidt input, the stated008 signed bound is AUDITED. The maximal low-generator conclusion remains conditional on the required full-plane theta and smooth complete Lipschitz transport inputs. No high inverse or nonlinear closure follows.
Opus review SHA256: ad3a51e78c8f63cdd0b39047c64de7af8840215f2da73c2c1f287d3a29c6dc1c.
Frozen bundle: audit/theory_audit/research_code/nested_compression_union/reviews/Opus_R1_016/MANIFEST.json.
Collaboration identity: the existing the T1/T3 theory worker lane is configured for us.anthropic.claude-opus-5-5; no API-observed model identity was available to this lane. No extra inference client or worker was started.

## T4-153: Weighted third-order endpoint obstruction

Date: 2026-10-29T02:03:17.846224+00:00.
Claim: The weighted third-order endpoint with any fixed positive lower-level coefficients has no normalized stationary inverse bound when1<c<=2 and a0>=5c-4, under the stated smooth coefficient and domain assumptions.
Method: Prove an exact shrinking-packet limit for the integer-order weighted norm, including an optional homogeneous negative term. Transfer the zero singular strip of T4-145, pin the canonical strain exactly, and verify the actual forcing trace.
Result and verdict: OPEN pending Opus review. This extends the proposed H3 obstruction to the growing weight omega=(1+4r²)^(2/5) of the Analysis II E3 endpoint. Increasing its fixed lower-level weights cannot remove the obstruction. Analysis II only claims growth at E3 and obtains decay in weaker fractional or interpolated spaces, so this is not a contradiction to its high inverse theorem.
Proof SHA256: ada3ee6523cb54a0fc4518a174655f49aa5ab51ac72b21b00b07284e3604a03e.
No numerical computation is used.

## T4-154: Opus acceptance of the origin obstruction and full007 scheme exclusion

Date: 2026-10-29T02:08:17.281589+00:00.
Claim: R1-017 independently confirms T4-145, T4-146 and the complete parameter exclusion of T4-147.
Method: Read the full review, its exact symbolic checker and 21-check output; verify all original proof and arithmetic-input hashes; freeze the review bundle. Check the boundary-packet scaling, canonical velocity, forcing hyperplane, inverse floor, monotone cell rule and scope against the original arguments. Record two abbreviated explanations precisely in ACCEPTANCE.md.
Result and verdict: CONFIRMED under the original explicit hypotheses. T4-145/146 are AUDITED. For exact candidate007 the registered FW-T-DYADIC-Y-v1 closure conditions are ruled out for every0<a<2, every0<s<1 and every fixed Rw>0. In particular the previously open small-a range is closed. The result uses the registered embedding and nonlinear margin; it is not a nonexistence theorem for nearby profiles or a statement about other norms.
Opus review SHA256: 5cb1c275a1df18fb14c6545125046da653fa4e4795c780aa0bfbce030d2d42d0.
Frozen bundle: audit/theory_audit/research_code/origin_dyadic_inverse/reviews/Opus_R1_017/MANIFEST.json.
The review's N_a monotonicity follows from its weighted-Laplacian integral, not from its quoted dyadic weights. Its boundary packets require the wide cutoff explicitly present in the original proof. Semigroup conclusions still require a generator. These are explanatory corrections, not failures of the reviewed proof.
Collaboration identity: The T1/T3 theory worker is configured as us.anthropic.claude-opus-5-5; API-observed identity unavailable. Its checker ran about3 seconds; this acceptance did not rerun it.

## T4-155: Independent multiscale010 point and graded exclusions

Date: 2026-10-29T02:08:17.281589+00:00.
Claim: N4-123's candidate010 point residual and its six scalar-ball and uniform graded exclusions are correct.
Method: Reconstruct each mono, shifted-Legendre and legqs radial Taylor jet exactly through degree4, then apply Euler differentiation and independent polar formulas for density, gradient and canonical velocity. Use1024-bit outward Arb at(1/10,73/100) and compare all eight fields and all necessary bounds.
Result and verdict: CONFIRMED. F=-0.1176966383056904124212613610117078638082 with an outward enclosure. Every field agrees with the independent Cartesian calculation. All six scalar-ball gaps are strictly positive; the uniform original-graded gap exceeds0.09730668451907358. These exclude fixed-c corrections only in the precise tested balls or original graded family. No profile nonexistence is asserted.
Point output SHA256: 10c338cd8be5868f3aa96fbfe01d7f00598436d2615d70a665b7399b9495f104.
Proof SHA256: 4699c5f8acaf9c4f13c0c50dad024bc9e5c125d93d06af0637610ef5d675d559.
Checker SHA256: cd542a621a9298a9f28e8130679332e1fc80865471833ce33a8f9d5e68758884.
Exact input SHA256: 2341ac50f06d89f6a0dbdf0f27a0e40449edcb62ca772ac66a155e0b7c3fb615.
Actual calculation: 1.9419537708163261 seconds.

## T4-156: Rounded007 weighted membership threshold

Date: 2026-10-29T02:10:33.977457+00:00.
Claim: N4-131 gives the exact threshold a>2/c for both weighted residual norms of the binary64 coefficient realization.
Method: Verify all source hashes against the independently confirmed T4-117 rounding record. Differentiate the finite convergent radial expansion twice, check that every odd angular multiplier alpha^2-n^2 is nonzero, and compare both radial integrals to the same power.
Result and verdict: CONFIRMED. Both W_a and N_a are finite exactly for a>4503599627370496/4076476460239181. At equality their squared integrals diverge logarithmically. The rounded realization is outside the registered Y whenever a is at or below this value, for every fixed positive low-weight radius. This does not concern the published exact rational candidate, and no sufficiency for membership in Y is claimed.
Proof SHA256: c554d302b927ee55be62d5d3dd38968600dc99e7943dad22e5b5c2c2c6f2d531.
N4 result SHA256: 0c052e2115daef7a778be3a03200d4e9a20881a50a2b0dec21d9b6061c3e5afa.
Frozen inputs: audit/theory_audit/research_code/rounded_membership_audit/source/MANIFEST.json. No new numerical computation was required.

## T4-157: Localized low-energy main estimate and double commutator

Date: 2026-10-29T02:11:59.971908+00:00.
Claim: T2_localized_BL2 L1, Lemma C and L2 give the stated unweighted numerical-range bounds, exact double-commutator constant and weighted rate.
Method: Independently reconstruct the reflected packets, evaluate the angular defect integral in bipolar coordinates, supply the bounded homogeneous-H1 approximation, and check every conjugated transport and velocity term.
Result and verdict: CONFIRMED with the explicit generator/core conditions retained for semigroup conclusions. The exact constant is C_T=sqrt((4log2-1)/(8pi)). The weighted rate is essinf(1+c+g-theta_1)-theta_c-kappa-C_T||grad theta_1||_2-omega, with omega bounded by||grad rho||_infinity(exp(osc psi)-1). No current candidate or nonlinear closure is certified.
Standalone proof SHA256: 6a1885eb9354a114bcaf0fe8509e1bf50d0d7afed67f7c99585b8831ae50582e.
Frozen T2 source SHA256: fd4c6f2e47a50e82983cbb3ffbc82d1c591ebac1c0fb29ba9502d71c39c616b6. No numerical rerun was needed; the integral is evaluated analytically.

## T4-158: First velocity commutator is not Hilbert-Schmidt

Date: 2026-10-29T02:11:59.971908+00:00.
Claim: Section8 of T2_localized_BL2 suggests ||[U,w^-1]||_HS<=C_U'||grad psi||_2.
Method: For a nonconstant compact smooth multiplier, compute the exact high-frequency angular expansion of the vector IPM symbol. Its angular derivative has norm1. The squared Fourier kernel has a positive r^-2 angular average, whose r dr integral diverges.
Result and verdict: REFUTED. Even smooth bounded even weights with compactly supported psi give a non-Hilbert-Schmidt first commutator. No finite C_U' exists in that suggested generality. This does not affect L2's valid oscillation operator-norm bound or Lemma C's double commutator. Proof is Section4 of audit record localized_low_audit, proof.

## T4-159: Orbit-weight regularity and support qualifications

Date: 2026-10-29T02:11:59.971908+00:00.
Claim: The orbit discussion extends the chain-rule equality to every starting point by continuity, and L4 asserts its derivative formula everywhere and compact support under its finiteness hypotheses.
Method: Separate the continuous-integrand inequality from the equality involving measurable g. Check a workload draining to zero, and a smooth radial tail theta_1=lambda-(log r)^(-2) with finite total future negative drift.
Result and verdict: REFUTED for the literal everywhere derivative and unjustified extension of the equality with g. The required orbit inequality is CONFIRMED by extending its continuous theta-lambda integrand. Compact support is OPEN until theta_1's uniform negative exterior drift is explicit: merely theta_1<lambda outside an annulus is insufficient, while theta_1 tending to0 at both ends supplies the missing condition. The counterexample has finite orbit budget and grad theta_1 in L2 but noncompact workload support. With the stronger condition and an almost-everywhere derivative statement, the construction is valid. Proof is Section5 of audit record localized_low_audit, proof.

## T4-160: Opus acceptance of the weighted third-order obstruction

Date: 2026-10-29T02:15:07.220698+00:00.
Claim: R1-018 independently confirms the exact weighted endpoint result T4-153.
Method: Read the complete six-step review, symbolic checker and ten-check output; verify their hashes and the original T4-145/153 proof hashes. Check the weighted scaling, real S1 construction, canonical strain pinning, forcing trace and low-domain qualification against the original argument.
Result and verdict: CONFIRMED. T4-153 is AUDITED under its explicit hypotheses. No bounded stationary inverse can hold in the specified Z3 endpoint when1<c<=2 and a0>=5c-4 if the realization contains the constructed tests. Analysis II's fractional/interpolated spaces and third-order growth estimate are outside this exclusion. R1-018 also accepts all three explanatory corrections to R1-017 recorded in T4-154.
Review SHA256: 57e406a5e82edf80be67407d2295d4267c7727bd87da1c262b083fde83cd9186.
Frozen evidence: audit/theory_audit/research_code/weighted_third_origin/reviews/Opus_R1_018/MANIFEST.json. Opus configured model us.anthropic.claude-opus-5-5; API-observed identity unavailable. No duplicate numerical computation was needed.

## T4-161: Independent radial dimension-12 bounds for d2,005 and007

Date: 2026-10-29T02:15:49.366040+00:00.
Claim: N4-133 to135 independently confirm all T4-129 radial compression values.
Method: Read the complete independent proof, direct Cartesian-gradient integration code and radial differentiation helper. Freeze and hash-check all output dependencies. Inspect the exact matrix, LDL and nested-dimension comparisons. The peer uses the Fourier Gram formula and direct gradient integral while T4 uses density integration by parts.
Result and verdict: CONFIRMED. With the R1-016 theorem review, these arithmetic applications are AUDITED under the named background energy inputs. Dimension12 gives commutator bounds0.6863082348782808154547 for d2,1.332416314581800909 for005 and0.7046357876834905475325 for007. The007 theta allowance at low rate2 increases to0.105683422516507538. This improves only the low estimate; neither high invertibility nor nonlinear closure follows.
Output SHA256s, in that order: a2c2ed60548d39d20b805685586ccc53b3361ecc96077cf3055ca23696935e31, e1411c95eb0406d89a21442bd54306924bd2c7333bb9e83cbd2c97aee10d0f2f, 5d8f92acdf6e67108843282ae3b38523e38ec3d6190cc56e4ebc132e40314b88.
Frozen complete dependency manifest: audit/theory_audit/research_code/parity_hs_budget/reviews/N4_133_135/MANIFEST.json. The peer computations took3.962728,11.500254,11.188960 real seconds. This acceptance did not rerun them.

## T4-162: Completed independent full-plane signed L2 certificate for007

Date: 2026-10-29T02:18:02.380282+00:00.
Claim: N4-111's theta<=2/25 target holds everywhere for the exact candidate007.
Method: Exact polar density-gradient reconstruction, coefficientwise comparison with the independent Cartesian polynomials, 1024-bit outward Bernstein and correlated Taylor bounds, scalar Schur tests and an exact binary partition check. The final validator checks all source, code, proof, seed and reconstruction hashes and preserves the original69 accepted seed rows.
Result and verdict: CONFIRMED. All232 closed cells pass; none remain pending. The smallest stored Schur margin exceeds0.00245606399. The independently reproduced full Hilbert-Schmidt constant gives a signed low rate greater than2.00215453, hence (B-L2) with rate2. With T4-161's reviewed radial compression the available rate exceeds2.02568. High inverses, residual smallness and nonlinear closure remain separate and are not certified by this result.
Final validation SHA256: 88577f3e87892fd675254fbde25e06eee7b2e78a56a97a46ea09481609fe4c35.
Complete cover SHA256: db3e7596759d9f4f7cfbc074d71255721fdd963d6d4b5b9324a0e017e2117c78.
Canonical input SHA256: 153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316.
Completed-stage wall time: 1512.116776265204 seconds; final validation: 2.028176608029753 seconds. Evidence: audit/theory_audit/research_code/candidate007_signed_cover/ACCEPTANCE.md and verification/FINAL_VALIDATION.json.

## T4-163: Symmetric weighted coupling repairs the Hilbert-Schmidt route

Date: 2026-10-29T02:19:34.158585+00:00.
Claim: Although the full first velocity commutator is not Hilbert-Schmidt, the symmetric conjugation error Sym(e^psi Q e^-psi)-Sym Q is Hilbert-Schmidt under bounded Lipschitz grad rho, bounded Lipschitz psi, and psi-constant in H1.
Method: Derive its exact physical kernel, retaining and then cancelling the unchanged local term. Symmetrization produces a squared weight increment and a product of weight and background increments. Bound their full-plane kernel norms by an explicitly integrated three-region increment estimate.
Result and verdict: OPEN pending independent Opus review. The proposed bound is cosh(Psi)/(4pi) times [G J(A,B;L,Psi)+J(A,B;H,2G)], with the exact function J and every parameter defined in the proof. This replaces the conjugation cost in the localized low-energy inequality by the minimum of the new bound and G(exp(Psi)-1). No current candidate improvement or closure is asserted.
Standalone proof SHA256: c37e645d8eba418394ad8a876ccdea5b6c5fa6e2ee1ef0d84a67454abcc19617.
Proof path: audit record weighted_symmetric_coupling, proof. No numerical computation is needed for the displayed integral.

## T4-164: Second Opus confirmation of the origin results

Date: 2026-10-29T02:21:11.733094+00:00.
Claim: The independent the T2 theory worker reviews confirm T4-145/146 and reproduce T4-147 directly from the exact generator list.
Method: Read both full reviews, exact symbolic and generator-based scripts, and complete logs. Freeze all named inputs and verify the original generator and mode1/mode3 hashes. Check the shrinking argument, canonical contact term, input hyperplane, origin constants and seven-cell comparison against the original proof.
Result and verdict: CONFIRMED. The already AUDITED origin theorem and007 scheme exclusion receive a second Opus theory review and a third arithmetic path. The Hq rescaling integral decreases, rather than increases, to its homogeneous limit; that review typo does not affect its dominated-convergence proof. The unneeded modes5 to15 table and new B>0 adjoint-spectrum remark are outside this acceptance.
Evidence: audit/theory_audit/research_code/origin_dyadic_inverse/reviews/Opus_T2_second/MANIFEST.json. The independent007 checker reported15.6 real seconds; no duplicate calculation was run. Model configured us.anthropic.claude-opus-5-5, API-observed identity unavailable.

## T4-165: Joint origin and far-field inverse ceiling

Date: 2026-10-29T02:21:11.733094+00:00.
Claim: the review of T4-146 Remark R1 correctly optimizes the two inverse floors simultaneously.
Method: Start from the precise scalar closure inequalities, take the minimum of the reciprocal floors, and maximize the resulting piecewise function. Prove monotonicity on both sides of s=d-b and locate the unique stationary point s_star.
Result and verdict: CONFIRMED. With d=c-1 and b=1+c-ca>0, the necessary ceiling is eta<b J(d,b)/(1+a), where J=H(d) if b>=d-s_star and J=b sqrt(4pi(d-b)(1+d-b)) otherwise. It improves or equals both separate ceilings. Its ratio to the far-field-only ceiling tends to sqrt(c(c-1)/2) at the admissible far-field endpoint. Both inverse floors must apply to the same realization and norm. No current row changes, and the peer's numerical table remains FLOAT.
Standalone proof SHA256: 0563378cc80819dc448847ed71b556562274e9ab4c7e02dfd8f82be56a53cc34.
Proof: audit record combined_inverse_ceiling, proof. No numerical computation was required.

## T4-166: Independent candidate009 background energies

Date: 2026-10-29T02:24:24.047387+00:00.
Claim: N4-121's whole-plane background energies and coupling constant for C1-N1-009-d2w-j7-x3balk are correct.
Method: Reconstruct density harmonics by applying the radial Laplacian directly to the canonical potential, compute Hessian energies by integration by parts, and evaluate exact rational beta sums. Compare all four rational energies before outward square roots; this differs from N4's Cartesian gradient route.
Result and verdict: CONFIRMED. All four exact rational energies agree. D2rho=17.01404387016401345, D3rho=90.95552575790029156, D(rho_x)=4.75625015244757044 and D(rho_y)=16.33572077697241078. The coupling constant is enclosed by [0.71321453930810894998957083517630926946245853309981594090861613326 +/- 4.90e-66]. This is a background bound, not nonlinear closure.
Canonical SHA256: 5ae619bc7f775c7997c4c5936a7463d56d1ec6a09ae70c1a47ec200776bda0ad.
Reproduction SHA256: 6ab0b3ef821efefb07d5d0f25144bbd892ed6fa9ab6b2b9478adec6076d974ad.
Independent elapsed time: 250.47993807774037 real seconds. Evidence: audit/theory_audit/research_code/background_norm_reproduction/verification/C1-N1-009-d2w-j7-x3balk_reproduction.json.

## T4-167: Multiscale finite-panel integrator independently audited

Date: 2026-10-29T02:24:24.047387+00:00.
Claim: N4-137's finite-panel integration theorem and implementation enclose the stated rational-weight integrals.
Method: Check the partition, binomial tail ratios, telescoping product error, signed numerator bound and outward power moments. Freeze all five source files. Replay all eight source cases identically. Independently integrate four additional signed rational functions by exact partial fractions, including repeated factors, an improper fraction, zero scale and three scales.
Result and verdict: CONFIRMED within the stated rational parameters and integer multiplicities. All eight replays and four independent comparisons pass. The theorem promises abstract arbitrary accuracy, while the implementation has a finite work cap; its tolerance is per factor and does not promise a final width. The raw API int(m) conversion requires caller-side integer validation. No candidate norm or missing cross term is certified by this primitive alone.
Standalone proof SHA256: b20df6f469096a6fb383bd43f839ca0ff5f95196609111067c349547cc0b132f.
Independent arithmetic SHA256: c85f4645a7fe1b2aceff14b6bf361ae86c7c09bdf2f624b8a7d547964906eeec.
Replay arithmetic SHA256: 873c07d03fdf8ee7107377153a5a64f4bb001ff826d2903cf6440ec3fef6527b.
Real elapsed times: independent checks 0.6955345482565463 seconds; replay 0.17068261513486505 seconds. Complete frozen manifest: audit/theory_audit/research_code/multiscale_moment_audit/MANIFEST.json.

## T4-168: Bounded multiplier weights obey the actual principal orbit budget

Date: 2026-10-29T02:26:39.459811+00:00.
Claim: T2 Proposition L3 remains valid for bounded locally Lipschitz psi with V.grad psi in L infinity.
Method: Apply even degree-zero multiplier asymptotics to packets with amplitudes phi and w phi; use smooth rescaled bumps at Lebesgue points of g. Extend the integrated inequality, whose right side contains continuous theta, across exceptional flow lines.
Result and verdict: CONFIRMED. Any weighted rate beta forces V.grad psi>=theta-(1+c-beta) almost everywhere and osc psi at least the corresponding actual-theta orbit budget. The indicator in the peer's sketch should be replaced by smooth shrinking bumps. No Hilbert-Schmidt first commutator estimate is used. An identity involving arbitrary measurable representatives of g does not extend by continuity.
Standalone proof: audit record bounded_orbit_weight, proof Section A, SHA256 149da4904aa3000997ef415d8e289a56c3c607576a5c59457c8035017bb8d408.

## T4-169: Auxiliary theta_1 budget is not necessary for every multiplier weight

Date: 2026-10-29T02:26:39.459811+00:00.
Claim: The T2 paragraph after Lemma L4 says its theta_1 orbit-budget cost cannot be avoided by any multiplier weight by applying L3 with theta_1 in place of theta.
Method: Distinguish the actual principal eigenvalue theta from an arbitrarily enlarged majorant. Take rho=0,V=cX,theta=0 and a nonnegative compact radial theta_1 bump higher than lambda.
Result and verdict: REFUTED as a universal necessity claim. The bump has positive theta_1-lambda orbit budget, but the zero weight gives the exact rate1+c with zero oscillation. More generally one can enlarge an auxiliary majorant without changing the operator. The corrected optimality applies only to weights satisfying the chosen stronger barrier g>=theta_1-lambda. The sufficient weighted bound is unaffected.
Frozen peer note SHA256: d15a678f4354354b43324e754644ff449a5e7ba5f1b26a97a7427bb20a3b637a. Standalone counterexample: audit record bounded_orbit_weight, proof Section B.

## T4-170: Explicit compact Lipschitz orbit-weight repair

Date: 2026-10-29T02:26:39.459811+00:00.
Claim: The orbit-workload construction is compactly supported and globally Lipschitz under global Lipschitz outward flow and a uniform negative exterior drift.
Method: Bound the positive annulus occupation by C=H log(r2/r1)/m. Exterior drift at most-delta drains it within C/delta, giving support radius R=r2 exp(L C/delta). Reduce the past supremum to a common finite time window and bound the Lipschitz constant by flow growth.
Result and verdict: OPEN pending independent Opus review. The proof gives a.e. transport inequality, exact oscillation budget, compact support and explicit H1 inputs for T4-163. Every extra hypothesis is stated, including the uniform margin absent from the original assertion. No candidate application or low-rate improvement is claimed.
Standalone proof: audit record bounded_orbit_weight, proof Section C, SHA256 149da4904aa3000997ef415d8e289a56c3c607576a5c59457c8035017bb8d408. No numerical computation.

## T4-171: Increasing frozen strip is residual rather than approximate spectrum

Date: 2026-10-29T02:27:36.132110+00:00.
Claim: T2 the review of T4-145 Remark R1 correctly places the B>0 interior strip in the frozen spectrum through the adjoint, not through primal approximate eigenvalues.
Method: Straighten the logarithmic transport by r=u-v/d. Construct the entire adjoint kernel explicitly as an arbitrary L2(r) function times the decaying one-dimensional profile. Prove the primal lower bound by the exact identity ||Th||^2=d^2||h'||^2+integral[(W-sigma)^2+dW']|h|^2.
Result and verdict: CONFIRMED for the natural frozen realization. The positive potential (Bp-delta)^2+2dB p(1-p) has a strictly positive minimum on[0,1] for0<delta<B. Thus the primal operator is bounded below with closed nondense range, while its adjoint kernel is infinite-dimensional. No variable-coefficient, pinned, or dyadic transfer is inferred without an adjoint-domain argument.
Standalone proof SHA256: 3e7dda44123efb1957c6d0bbe90e2acd60cd50f8aa56b06256078b2eef122ef2. Topic: audit record frozen_adjoint_strip, proof. No numerical computation.

## T4-172: Sharpened weighted weak proposition and polar forms

Date: 2026-10-29T02:29:13.515525+00:00.
Claim: T2-W4 sharpens T4-081 by retaining the joint transport norm and exact angular factors.
Method: Derive the three-term weak identity, weighted Cauchy-Schwarz estimates, exact radial and angular gradient, trigonometric product tables and the radial Jacobian. Read all617lines of the implementation.
Result and verdict: CONFIRMED for the analytic proposition and polar formulas, under T4-081's full admissibility and velocity hypotheses. Use the trivial zero bound for a zero probe. Exact rational freezing makes the floating search acceptable, but all candidate-specific values remain OPEN until an independent field path checks them.
Standalone proof SHA256: eb39e4618da430d33e2d8804aa8d1c183e35f5f13ca85826e1740794b7a90194. Topic: research/sharp_weak_form_audit.

## T4-173: Decimal lower-bound output is not directed downward

Date: 2026-10-29T02:29:13.515525+00:00.
Claim: The T2 sharp-weak JSON m_lower fields and table entries are rounded-down versions of their certified quadratic formula.
Method: Independently reconstruct that formula at512bits from each stored component ball, and compare the claimed decimal with both endpoints. This is a component-level audit, not a new field computation.
Result and verdict: REFUTED for the claimed rounding convention. Twenty of34JSON scalars exceed the upper endpoint of their own formula enclosure. Example d2,a=1,k=288: formula near0.01423120590745775518, JSON0.0142312059075, Markdown0.014231206. SpanMpen2,a=1: formula near0.04395530670478615, Markdown0.043955307. The true correction-distance bound might still be larger, but these decimals are not justified by the reported certificate. Preserve a ball or explicitly floor below its lower endpoint. No current row changes.
Evidence SHA256: 4732c65604f2a1d86dfc19f120e6f83a5b531338c7115afafc46380f3296e38b. Reproduction code: audit/theory_audit/research_code/sharp_weak_form_audit/code/check_decimal_rounding.py.

## T4-174: Symmetric weighted coupling independently reviewed

Date: 2026-10-29T02:36:49.127840+00:00.
Claim: T4-163 is a valid Hilbert-Schmidt bound and may enter the localized low-energy estimate under its full hypotheses.
Method: Read and freeze the complete Opus T2 review, then check its kernel, increment and energy arguments against the original proof.
Result and verdict: CONFIRMED. T4-163 is AUDITED under its stated hypotheses. The review's numerical placeholders and heuristic cost model are not accepted as executed computations. No candidate rate follows.
Frozen review SHA256: 286640b8b683ce0387f01d6947145155a5525ab5aeb50954810f4f5ce30fbdee. Evidence: audit/theory_audit/research_code/weighted_symmetric_coupling/reviews/Opus_T2_163/ACCEPTANCE.md.

## T4-175: Independent sharp weak span for candidate005

Date: 2026-10-29T02:36:49.127840+00:00.
Claim: The candidate005,a=6/5 rational span probe gives a weighted correction-distance bound above0.02436463.
Method: Rebuild fields from canonical potential coefficients through the separate T4 polar loader; combine the general polynomial transport modes before squaring; use exact angular gradient cross terms and rational W-moments, with2048-bit Arb arithmetic. Bound the gradient supremum by a separate dyadic mean-value subdivision.
Result and verdict: CONFIRMED. Pairing, M and C overlap all peer enclosures. Independent H bound 1999843/100000000, 34 cells, yields strict necessary lower bound 6091157959/250000000000, hence0.02436463. This does not adopt the faulty rounded scalar fields identified in T4-173 and does not certify the other33 rows.
Output SHA256: 3704c54dae47583889ae23f95454805b1ccd96138e81cccf5f5098ff81890924. Real elapsed time 99.978011s. Reproduction: audit/theory_audit/research_code/sharp_weak_form_audit/code/reconstruct.py --candidate C1-N1-005 --a 6/5.

## T4-176: Annular localized symmetric coupling bound

Date: 2026-10-29T02:36:49.127840+00:00.
Claim: For |v|<=G<X>^-delta and |Dv|<=H<X>^(-delta-1),0<delta<1, a multiplier supported at radiusR has the explicit bound R^-delta sqrt(N^2+T^2) in audit record annular_symmetric_coupling, proof.
Method: Split the exact symmetric kernel at separationR/2. Use local gradient bounds only when the weight increment is nonzero; integrate the far part over the whole plane, explicitly retaining its coupling to the origin.
Result and verdict: OPEN pending independent Opus review. The proof predicts an O(R^-2delta) cost for a fixed-shape annular weight of amplitudeR^-delta. This addresses T2's request for a local version; no weight construction, candidate constants, or high inverse is asserted.
Standalone proof SHA256: f1ad59b6a9e2f5f53580f06eec6192d097fb5b6fa1ff64b12d63d1fd61e580e5. No numerical computation.

## T4-177: Growing-weight S1 velocity and the exact admissible interval

Date: 2026-10-29T02:41:01.750534+00:00.
Claim: For w_p=(1+r^2/R^2)^(p/2), the complex odd Beurling norm is (2+|p|)/(2-|p|), and the real S1 velocity has a finite bound precisely for |p|<2.
Method: Apply weighted duality and physical conjugation to audited T4-054. Use an explicit odd compact source and its r^-3 dipole tail to exclude |p|>=2. The full-space comparison uses the n=1 block and r^-2 monopole tail.
Result and verdict: OPEN pending independent Opus review. The explicit S1 velocity upper bound is2/(2-|p|); its sharpness on S1 is not claimed. Derivative parity must be checked separately in a hierarchy.
Evidence: audit record growing_weight_velocity, proof, SHA256 57498412d681621363d935541575b88050855e6c9264dd4293447febbd470c76.

## T4-178: Bessel multipliers retain differentiated power tails

Date: 2026-10-29T02:41:01.750534+00:00.
Claim: If all derivatives of smooth f have symbol-type bounds of order e, J^s f-f has order e-2 for every s>=0. A nonzero differentiated homogeneous leading tail has the same weighted L2 threshold after J^s.
Method: Use the exact heat representation, an explicit polynomially weighted Gaussian estimate, and a finite differential expansion for general s. Integrate the nonzero angular leading term to obtain the endpoint.
Result and verdict: OPEN pending independent Opus review. This fills the unproved assertion in T2 the review of T4-094 A4 under explicit global derivative hypotheses. It does not deduce asymptotics from the multiplier Taylor expansion alone.
Evidence: audit record bessel_tail_preservation, proof, SHA256 bb3f77dc59f21a4ebc1b27c2d972a706d9fe013c436bb54fb8df610f8d9360af.

## T4-179: Growing-weight coefficient obstruction and graded bookkeeping reviewed

Date: 2026-10-29T02:41:01.750534+00:00.
Claim: The T2 review confirms T4-094 and adds sharp coefficient thresholds, graded weight differences, residual derivative membership and the comparable-weight packet cap.
Method: Read the entire analytic review. Reconstruct the radial derivative lower bound, polar integrability test, Leibniz coefficient weights and the bounded logarithmic-weight argument.
Result and verdict: CONFIRMED with the stated scope. T4-094 is now AUDITED. A1,A2,A3,integer-derivative A4,A7 are confirmed. The Bessel extension is separately OPEN as T4-178. Numerical sections still contain placeholders, so no new numerical execution is accepted.
Evidence: audit/theory_audit/research_code/weighted_packet_audit/reviews/Opus_T2_094/REVIEW.md, SHA256 f95780a04ebbf58cd66eadd2c09ff897dd56711d80252b72205f975d94fedbc1.

## T4-180: Compact orbit weight independently reviewed and support sharpened

Date: 2026-10-29T02:41:01.750534+00:00.
Claim: R1-020 confirms T4-170 and proposes support radius r2 exp(L_r Theta_1/delta), using the actual orbit budget and maximal radial logarithmic speed.
Method: Check all ten analytic review steps against the original proof and inspect the toy script/output. Bound exterior drainage time by Theta_1/delta and radial growth by L_r.
Result and verdict: CONFIRMED. T4-170 is now AUDITED. The C-S1 smaller support radius and corresponding finite-window Lipschitz bound are also confirmed when Theta_1 is a rigorous upper bound. The FLOAT toy values are not candidate certificates and were not rerun here.
Evidence: audit/theory_audit/research_code/bounded_orbit_weight/reviews/Opus_R1_020/REVIEW.md, SHA256 60d47c903668aef562bdafe396931ac9b7d4e2ca1d86671752ca37275971e046.

## T4-181: Sign in the full-space Riesz decomposition

Date: 2026-10-29T02:41:01.750534+00:00.
Claim: T2 the review of T4-094 A5 prints R1^2=-I/2-(R1^2-R2^2)/2.
Method: Use R1^2+R2^2=-I, or test the Fourier multiplier at xi=(1,0).
Result and verdict: REFUTED as printed. The difference has a plus sign. The full-space power-weight interval conclusion is unaffected and receives a direct proof in T4-177.
Evidence: audit/theory_audit/research_code/weighted_packet_audit/reviews/Opus_T2_094/REVIEW.md, SHA256 f95780a04ebbf58cd66eadd2c09ff897dd56711d80252b72205f975d94fedbc1.

## T4-182: Rational span probe strengthens the candidate007 weak-distance screen

Date: 2026-10-29T02:46:22.451519+00:00.
Claim: A rational polynomial probe with powers0,1,2,3,4,6,8,12,16,24,32,48,64,96,128 gives unweighted L2 correction distance above0.00031474108 for exact candidate007.
Method: Build exact canonical fields independently of T2's loader, form joint transport and exact angular gradient Gram matrices at2048bits, use floating linear algebra only to propose the rational vector, then enclose its quadratic forms and the full radial gradient supremum. Floor the final root below its lower endpoint.
Result and verdict: OPEN pending independent numerical review. The local interval computation yields strict floor7868527/25000000000, about7.15times the earlier registered4.3987e-5 lower bound. A separate direct-polynomial reconstruction is running; it does not replace a second lane's review. The analytic weak-test theorem is already audited.
Evidence: audit/theory_audit/research_code/optimized_probe_007/verification/a0.json, SHA256 b5b510bbabe556d2e07008473d9d92eb7098bac38cc36955cac0799bd0de425e. Real search-and-verification time61.139554s. No candidate closure.

## T4-183: One-sided expansion sharpens orbit-weight regularity

Date: 2026-10-29T02:46:22.451519+00:00.
Claim: T2 the review of T4-170 R1 replaces exp(Ls) by exp(-mu s) in the backward-flow estimate when Sym DV>=mu I.
Method: Differentiate squared backward-flow distances; integrate the common Lipschitz bound and pass it through the supremum. Use mollification to justify the all-pairs condition from an almost-everywhere matrix bound.
Result and verdict: CONFIRMED. For mu>0, Lip(psi)<=Lip(theta_1)/mu independently of the time horizon; the finite-window sharper expression is also valid for any real mu. The actual candidate value of mu remains unmeasured here.
Standalone proof: audit record monotone_orbit_lipschitz, proof, SHA256 4a2f5b7093efdba19ab6f6f019a52c4072b5c15b52021b2ba4eeadbb9bb90333. Frozen Opus review SHA256 739f28526656330824257664a7ca6bd28b6aff4c222ee216a1d97dbdfab4b3c2.

## T4-184: Candidate007 first-harmonic span independently reproduced

Date: 2026-10-29T03:00:58.516033+00:00.
Claim: R1-021 confirms T4-182 and its exact strict distance floor7868527/25000000000.
Method: Read the complete Opus T1 review and script. Check its source-generator reconstruction, exact angular Gram forms, adaptive second-derivative H certificate and final scalar calculation against our canonical calculation. Inspect the independent output and the separate local direct-polynomial check.
Result and verdict: CONFIRMED. T4-182 is now AUDITED. The independent1024-bit M,C,pairing balls overlap ours; H is certified on61cells. Our direct-polynomial check independently agrees within this lane in100.503573s. No optimality, inverse or existence claim.
Evidence: audit/theory_audit/research_code/optimized_probe_007/reviews/Opus_R1_021/REVIEW.md, SHA256 3171f549fdbb70a22bd01559c997918f69160901cb147fd1752edc12b17a5cee.

## T4-185: Higher angular probes detect a substantially larger candidate007 correction distance

Date: 2026-10-29T03:00:58.516033+00:00.
Claim: For odd n, smooth phi_n=r W^2 P(t)sin(n theta), with t^((n-1)/2) dividing P, obeys the same audited weak necessary inequality. The proposed n=7 probe gives ||h||2>4769166867/1000000000000.
Method: Derive the signed sum-and-difference angular products and the exact sin(n theta)^2 gradient form. Build all Gram forms from canonical fields at2048bits. Independently recombine full polynomials and compute int F phi by differentiating rho directly, instead of using -int rho M. Certify H by full interval subdivision.
Result and verdict: OPEN pending an independent lane review of the new angular formulas and candidate arithmetic. Both local paths agree on M,C,pairing and the strict floor0.004769166867. Gram run19.086108s; direct check35.093916s after correcting an unsupported arb_poly division in a failed first attempt. This is a necessary correction distance only.
Evidence: audit/theory_audit/research_code/optimized_probe_007/verification/n7_a0.json, SHA256 2a268c62e9e45096d2b745679a49adeee0cb9a3da532a06e4b89faaffdb3ef1f.

## T4-186: Annular symmetric-coupling theorem and variable cutoff reviewed

Date: 2026-10-29T03:00:58.516033+00:00.
Claim: T2 the review of T4-176 confirms the complete annular Hilbert-Schmidt bound. Its R1 variable cutoff and R3 inner vanishing assertion sharpen the application.
Method: Read every analytic review step and the numerical source. Recheck near/far separation, the origin contribution, signed multiplier factor, arbitrary cutoff k and monotonicity of backward radii.
Result and verdict: CONFIRMED. T4-176 is AUDITED. R1 and R3 are proved in CUTOFF_PROOF.md. The peer FLOAT quadrature table remains exploratory: its displayed HS upper column is not a certificate because quadrature and omitted small-separation errors are unbounded. No candidate weight, high inverse or nonlinear closure follows.
Evidence: audit/theory_audit/research_code/annular_symmetric_coupling/reviews/Opus_T2_176/REVIEW.md, SHA256 15d08c01b0e82defd788495d81a91873348400158c023000d74e92e21d74e194.

## T4-187: Directed scalar floors repaired in all34 sharp weak-test rows

Date: 2026-10-29T03:00:58.516033+00:00.
Claim: T2 wws_directed_floor.json supplies two decimal floors below each row's full quadratic-root ball, repairing T4-173.
Method: Freeze the correction, verify the source hash and unique row matching, independently reconstruct each quadratic root from its M,C,H,pairing balls at768bits, and compare both decimals and ball overlap.
Result and verdict: CONFIRMED as a component-level rounding correction. All34 rows pass both strict-floor comparisons. This does not certify the PDE-field arithmetic of the33 rows not independently reconstructed here. The standalone implementation initially failed while hashing a string path after all comparisons; the corrected path conversion completed successfully.
Evidence: audit/theory_audit/research_code/sharp_weak_form_audit/verification/directed_floor_fix.json, SHA256 060bf54815cfc028512deef2f73ac0f82f5e3d3e78cd2f9554de3ca1b13f06c9.

## T4-188: Gradient subtraction in the weak coupling functional

Date: 2026-10-29T03:07:11.030383+00:00.
Claim: Incompressibility permits replacement of phi grad rho by (1-lambda)phi grad rho-lambda rho grad phi, with an exact optimal scalar formula and unchanged weak pairing.
Method: Prove the cutoff identity for grad(rho phi), derive the complete polar cross forms, and compute the candidate007 mode7 form at2048bits. A second local path assembles the vector Fourier coefficients before squaring.
Result and verdict: OPEN pending independent review. Both local forms agree. The provisional distance improves only from0.004769166867 to0.004789655401, about0.43percent. This scalar subtraction is not a priority for further numerical tuning; it does not address the closure gap. Real computation18.490738s.
Evidence: audit record solenoidal_weak_probe, proof, SHA256 bd0e46fce74c46ecf6c552b1bbb529b2e6db7e95677e338ef7ec3f1b469f6bf8; verification/n7_a0.json in that topic, SHA256 3c42d03791982084cebfcfd03fa77203e8cb3257c3f5a07feb3bde65fc17c8ee.

## T4-189: Weak correction spaces pin the similarity exponent

Date: 2026-10-29T03:07:11.030383+00:00.
Claim: If rho has a nonzero leading r^gamma angular profile with0<gamma<1 and the explicit growth bounds, every stationary correction h with h,U[h] in L2((1+r^2)^(-a)dX), 0<=a<=1+gamma, must have exponent c'=1/gamma. No derivative or pointwise asymptotics of h is required.
Method: Test the full distributional equation against a compact annular test escaping to infinity. Bound all five error terms using weighted tails and exact scaling powers, including the quadratic term. The surviving linear background term forces c'gamma=1.
Result and verdict: OPEN pending Opus review. The endpoint is included. The condition is sharp for the stated affine class since a>1+gamma admits h=-rho. If a C1 nonzero-slope solution is also assumed, the canonical strain is pinned by the origin identity. No existence or cross-chart distance claim.
Evidence: audit record weak_tail_exponent_pinning, proof, SHA256 b516639410c86d01c393cd9c10b7c5de9079f2150912f7a3af684f40bb814577.

## T4-190: Candidate007 angular probe independently confirmed

Date: 2026-10-29T03:17:28.289762+00:00.
Claim: R1-022 confirms the n=7 weak-distance certificate T4-185.
Method: Read the full Opus review, independent field/Parseval implementation, both pairing paths, H subdivision and all output; validate frozen input hashes.
Result and verdict: CONFIRMED. T4-185 is AUDITED, giving strict fixed-c L2 distance >4769166867/10^12. The symbol sign and old-probe index slips in the review are recorded in ACCEPTANCE.md and do not affect any calculation. Finite differences are diagnostics only.
Evidence: audit/theory_audit/research_code/optimized_probe_007/reviews/Opus_R1_022/REVIEW.md, SHA256 c6bcf54172ef330453695ca10ade3430cad28677714f48831a9d576482cd8671.

## T4-191: Bessel-tail preservation independently reviewed

Date: 2026-10-29T03:17:28.289762+00:00.
Claim: T2 confirms all of T4-178 under its stated differentiated polynomial bounds.
Method: Read the complete review and its numerical source; recheck the heat representation, absolute convergence, Peetre estimate and differentiated tail argument.
Result and verdict: CONFIRMED. T4-178 is AUDITED. Its canonical application remains conditional on a global differentiated expansion of the actual full-plane fields, as Q1 requires. FLOAT checks are not certificates.
Evidence: audit/theory_audit/research_code/bessel_tail_preservation/reviews/Opus_T2_178/REVIEW.md, SHA256 c0587374b5f5579a1fa32a7f3382ee5ec1aa1e6786d551529619e87f51a67a8d.

## T4-192: Growing-weight velocity interval independently reviewed

Date: 2026-10-29T03:17:28.289762+00:00.
Claim: T2 confirms T4-177, including exact admissible interval |p|<2 on S1.
Method: Read every duality, parity, multipole and full-space step and the complete check source.
Result and verdict: CONFIRMED. T4-177 is AUDITED. Its first-derivative-row question is separate and remains unproved by this argument.
Evidence: audit/theory_audit/research_code/growing_weight_velocity/reviews/Opus_T2_177/REVIEW.md, SHA256 db170e2acb396bb6b9a43e5fc4f4d4bcbc7646a2f28b7ef26956ff6187fff543.

## T4-193: Independent radial quadrature error reproduction

Date: 2026-10-29T03:17:28.289762+00:00.
Claim: N4-150 gives exact finite-sum errors for MID8,12,16,24,32 on candidate007.
Method: Reconstruct the canonical first mode independently, check all1765 rational coefficients, integrate all14 pairings exactly and evaluate all70 recorded radial rules directly in t, with independent rational-coefficient tail antiderivatives.
Result and verdict: CONFIRMED, for the exact candidate and recorded rational nodes. All comparisons pass at2048bits in148.377164seconds. MID8 low-k signs are wrong; the MID24/32 error enclosures are confirmed. No uniform-in-candidate quadrature guarantee or optimization certificate.
Evidence: audit/theory_audit/research_code/radial_quadrature_audit/verification/candidate007.json, SHA256 6ca52a4e947ba6dc5b8293bfd71bd665d7a41d2fead5ccd0805e6caeb4869e2c.

## T4-194: Gradient compatibility enlarges the admissible power-weight interval

Date: 2026-10-29T03:17:28.289762+00:00.
Claim: For S1 h, ||w_p grad U[h]||2 <= C_p ||w_p grad h||2 holds precisely for -1<p<3, with explicit constants in the new proof.
Method: Keep both gradient components, use the exact radial Beurling ODE, and compare its weighted energy identities. Construct compact multipole and escaping-annulus counterexamples at the two endpoints.
Result and verdict: OPEN pending independent Opus review. For0<=p<3 the proposed C_p is [1+sqrt((1+A(p)B(p))/2)]/2. In particular p=3/2 admits C=(1+sqrt(11/2))/2. No inverse or nonlinear closure follows.
Evidence: audit record weighted_gradient_velocity, proof, SHA256 831cb25f0216615457c13166a4cf3b80737f244c35e3dcc0a5d837c1b5372fad.


## T4-195: Independent exact rank of the candidate007 potential parameterization

Date: 2026-10-29T03:23:08.575329+00:00.
Claim: N4-158 gives potential rank1922 and kernel dimension1060 for2982 variable generators.
Method: Read the complete proof and frozen optimizer setup. Rebuild shifted Legendre columns by exact Fraction recurrence, certify each block rank by nonzero minors modulo the trial-division-certified prime2147483647 and a matching support upper bound, verify all1060 rational kernel identities and28 nonresonance pairs, and reconstruct all1922 canonical coefficients.
Result and verdict: CONFIRMED. All360 blocks and all identities agree. These are zero-potential directions, not nonzero PDE perturbations. The first local attempt stopped at Python's integer-string digit limit after its rank checks; the corrected explicit digit setting completed in1.028101seconds. No optimizer was run. Opus discussion requested through v88.
Evidence: audit/theory_audit/research_code/basis_rank_audit/verification/result.json, SHA256 cce9b0190fc8d592863a536096cde20e0eb914744ae8747227d97244d38109ce; N4 proof SHA256 b425c544fe0505bd3806d8b5445ad21dc198e689340a66b51713b5dadc51ef60.

## T4-196: Numerical-lane confirmation of the mode7 distance accepted

Date: 2026-10-29T03:23:08.575329+00:00.
Claim: N4-157 independently confirms T4-185's distance >0.004769166867.
Method: Read its full proof and independent Cartesian field/Parseval code, compare all retained intervals with our exact probe, and validate the complete four-cell Bernstein cover and strict root floor.
Result and verdict: CONFIRMED. Together with Opus R1-022 and T4-190, the result meets both theory and numerical independence rules. This is a necessary fixed-c L2 correction distance, with no inverse or existence conclusion.
Evidence: audit/theory_audit/research_code/optimized_probe_007/reviews/N4_157/result.json, SHA256 5ce7fecef218b0a537b6d02a97dd0eb03b88535a75ab5f7aa82d1fd9d2683e4c.

## T4-197: Candidate007 sharpw residual gap strengthened

Date: 2026-10-29T03:23:08.575329+00:00.
Claim: Coordinator matrixv37 gives X_(s,w)(F)>732.35 and a sharpw threshold gap>3.48million.
Method: Use Plancherel monotonicity only on the unweighted low components. Substitute strict rational floors from the CONFIRMED G0 and G1 enclosures, and compare squares over the rationals.
Result and verdict: CONFIRMED. The resulting norm lower bound exceeds732.35846197 and its ratio to0.00021035 exceeds3481618.5499. The weighted Hessian is discarded, so no unjustified weighted Bessel monotonicity is assumed. This is a failed sufficient smallness condition, distinct from the distance exclusion.
Evidence: audit record candidate007_smallness_gap, proof, SHA256 5444288501914bb4ebfad885e169cf8363f48840b097dbe036f93bf45b8c99b3; verification/result.json in that topic, SHA256 61ff7240a7c7f7fdb6bf7fe0ccd5b7c164ee2a09bd627f5a11350b4e0192c08d.

## T4-198: Explicit-mode diagnostic for the weighted gradient theorem

Date: 2026-10-29T03:23:08.575329+00:00.
Claim: The radial identities and constants in T4-194 are consistent with independently explicit Gaussian-mode Beurling outputs.
Method: Integrate both gradient energies and the signed identity for24 real mode pairs, and check2828 potential ratios. The explicit incomplete-gamma output is differentiated algebraically, not by finite differences.
Result and verdict: CONFIRMED for these FLOAT diagnostic comparisons only. All p=0 ratios are1 to quadrature precision. T4-194 itself remains OPEN independent Opus review. Runtime0.121207251seconds.
Evidence: audit/theory_audit/research_code/weighted_gradient_velocity/verification/gaussian_modes.json, SHA256 da6f24ea6169f8137dba85ddb06777bf7759e924288b3d2a915fb127ca73703f.

## T4-199: The exact potential quotient has no additional density gauge

Date: 2026-10-29T03:26:22.196824+00:00.
Claim: For the finite canonical branch family j=0,...,7, the map chi -> -partial_y Delta chi is injective on the function span. Thus the independently confirmed potential rank1922 is also the density rank, with precisely1060 redundant coefficient dimensions.
Method: Four-derivative decay and even parity reduce a zero-density potential to a quadratic polynomial. Exact branch nonresonance then excludes every nonzero such polynomial from the span. Rational arithmetic checks all eight exponents and28 branch differences.
Result and verdict: OPEN pending independent Opus review. This excludes an additional representation gauge only; it does not establish the rank of the PDE linearization, a sampled Jacobian, or an inverse estimate.
Evidence: audit record potential_density_injectivity, proof, SHA256 b57d0a801a9c504c446a5559f3ee44c875f11eb9ac39f47611842e8177bdaffb; verification/parameters.json in that topic.

## T4-200: Both Opus reviews confirm weighted tail exponent pinning

Date: 2026-10-29T03:28:33.376433+00:00.
Claim: R1-023 and T2 the review of T4-189 independently confirm T4-189.
Method: Read both complete analytic reviews, their source and numerical illustrations; recheck the sign convention, endpoint powers, local products and origin trace conditions. Freeze hashes of every retained review file.
Result and verdict: CONFIRMED. T4-189 is AUDITED. The result includes the endpoint a=1+gamma and does not need derivatives of the correction. FLOAT illustrations are not certificates.
Evidence: audit/theory_audit/research_code/weak_tail_exponent_pinning/reviews/Opus_R1_023/REVIEW.md, SHA256 a6d89d826486de5f43db6161de62e696ba138e9c6fa977e2a870862bb4bebc61; Opus_T2_189/REVIEW.md, SHA256 d077386abb2c9993d7e28e96c9312275e3cd3923a267e10f19bc7c6234ec5b63.

## T4-201: Automatic canonical velocity and derivative-free background

Date: 2026-10-29T03:28:33.376433+00:00.
Claim: The two Opus reviews' R1/R2 reductions remove the separate weighted velocity assumption and the background gradient bound from T4-189.
Method: Use the already audited S1 weighted velocity extension, density of compact S1 tests and local convergence; keep the two background-density terms in divergence form and rederive their exact powers.
Result and verdict: CONFIRMED, for the explicitly specified canonical continuous extension. The density correction alone suffices for0<=a<=1+gamma; the reference needs its uniform undifferentiated nonzero leading profile and velocity growth. No plain Fourier definition for an arbitrary growing correction is silently assumed.
Evidence: audit record weak_tail_canonical_application, proof, SHA256 812fc9ae866b9b7d9cf2f9af4d9f290f1323dadd1e47857b2f045c9e38852d18.

## T4-202: Weighted residual-tail obstruction

Date: 2026-10-29T03:28:33.376433+00:00.
Claim: T2 the review of T4-189 Remark R3 excludes every weighted L2 correction when a<=2 and the residual has a uniform nonzero leading power q>=a-1.
Method: Test against R^-1 psi(X/R), bound all four correction terms by their weighted annular tails and divide by R^(q+1). Recheck negative weights and the quadratic endpoint a=2 explicitly.
Result and verdict: CONFIRMED under all displayed hypotheses. This is an entire affine-class obstruction, not a contraction failure. Individual candidate applications remain conditional on exact nonzero leading coefficients and a uniform expansion. The proof also identifies the stronger condition q>=max(a-1,2a-3) if a>2.
Evidence: audit record weighted_residual_obstruction, proof, SHA256 b0ec2901ffd9c6e51e23d3c788dd56fabc7507c01942c026a500d0c3d91571c3.

## T4-203: Exact nonzero leading profile of candidate007

Date: 2026-10-29T03:28:33.376433+00:00.
Claim: Candidate007 has a nonzero leading r^(1/c) density profile; its first sine coefficient lies strictly between18 and19.
Method: Sum exact j=0 potential coefficients, apply the homogeneous Laplacian and y derivative algebraically, and compare the resulting rational with18 and19. The finite canonical family also gives the needed differentiated uniform expansions termwise.
Result and verdict: OPEN numerical-lane reproduction of this new exact scalar. Local rational comparisons pass in0.034475915seconds and agree with Opus's18.56782229754644 FLOAT diagnostic. Once confirmed, the now-audited weak tail theorem fixes c for every solution in candidate007's original affine class, including all registered unweighted L2 balls.
Evidence: audit/theory_audit/research_code/weak_tail_canonical_application/verification/candidate007.json, SHA256 df8a4665cd430b72844fc82590d71289ae59f1a68d5d6ee53b6fc6eec02ce20f.

## T4-204: Candidate012 point exclusions independently reproduced

Date: 2026-10-29T03:34:50.550548+00:00.
Claim: N4-155's new point fields and scalar/graded exclusions hold for exact candidate012.
Method: Load the immutable generator coefficients, form exact local radial Taylor data through fourth order, compute the density and velocity by independent polar differential formulas at(1/10,73/100), and compare every field and necessary-inequality interval at1024bits.
Result and verdict: CONFIRMED. All eight fields, the uniform original-graded bound and gap, and all six scalar-box bounds/gaps overlap. F=0.03929516148112317736 and the graded gap is0.01901378313389195457. Runtime1.699851176seconds. This excludes only the stated balls/family and does not evaluate full-plane residual norms.
Evidence: audit/theory_audit/research_code/candidate012_point/verification/results.json, SHA256 9e0e874cb72675d126538f9610b61f3cdf4485c451a6b745b6c83ea21073bfbf; source coefficient SHA2563a578c95a394f84fdad2edfdcb52dfa43c284404ce441e68b749ca55ff6ab6fc.

## T4-205: Finite logarithmic tangent spaces do not cover exponent changes

Date: 2026-10-29T03:34:50.550548+00:00.
Claim: Tails chi r^gamma Theta with distinct gamma>=a-1 are independent modulo E_a=L2((1+r^2)^(-a)dX). No finite linear augmentation, including finitely many logarithmic tangent terms, represents an interval of exponent changes modulo E_a.
Method: Compare the largest radial power in any finite relation and integrate its weighted square. Separately construct the smooth nonlinear chart in a weaker ambient E_b with explicit logarithmic derivative bounds.
Result and verdict: OPEN independent Opus review. This refines the tail-coordinate design condition without excluding nonlinear parameterized tails. It supplies no inverse or closure.
Evidence: audit record nonlinear_tail_chart, proof, SHA256 a8769187d8b381e55c743fdd94ca0cb0e28a11b85a87b8a09a51aa368c817b88.

## T4-206: Direct first-moment bound for compatible derivative tensors

Date: 2026-10-29T03:38:50.980849+00:00.
Claim: For compact real centrally odd h, w=(1+r^2/R^2)^(1/2), and the full ordered derivative tensor, ||w D^k U[h]||2 <= sqrt(1+2/(k+1)) ||w D^k h||2 for every integer k>=0. In particular the Hessian constant is sqrt(5/3).
Method: Derive the exact Fourier first-moment identity for the signed two-component velocity symbol. Use the tensor orientation energy k and odd angular Poincare to control the singular symbol derivative. Check the origin of Fourier space and define the completion at the derivative-tensor level.
Result and verdict: OPEN independent Opus review. This is a concrete alternative hierarchy input, with no inverse, origin trace or nonlinear closure assertion. No computation was needed.
Evidence: audit record weighted_derivative_moment, proof, SHA256 ce3b59a2cc98ba38fce2f9004c48dc526e13f197751d95ec8d6d0b15e5bb8f82.

## T4-207: Complete polar third-tensor method and candidate007 record

Date: 2026-10-29T03:43:40.689994+00:00.
Claim: N4's polar third-derivative method gives the full ordered tensor norm and valid whole-plane Q3 bounds.
Method: Derive the independent complex-derivative identity |D^3F|^2=(|Dplus^3F|^2+3|Dplus Delta F|^2)/4, compare the four general radial amplitudes symbolically, check the exact weight remainder, and verify every manifest, mode hash, endpoint exponent and outward total in the completed007 record.
Result and verdict: CONFIRMED. All160 modes,2720 tensor identities and5440 stored endpoint exponents pass. The full interval near5599.096813043943 agrees with the independent N3 Cartesian enclosure. The local audit took1.462421394seconds. This audits the theorem/code and complete retained arithmetic; the two full field regeneration paths remain N3 and N4. No inverse or closure assertion.
Evidence: audit record polar_third_tensor_audit, proof, SHA256 09a5338d6020fc5236e9886770b6c3323bedd4253ef35441b655fd6017e05822; verification/result.json, SHA256 2a70bf77ce27aae82b719fa440c31efb24a40cb0d00823f07026dd8787c496cc.

## T4-208: Independent leading-harmonic confirmation accepted

Date: 2026-10-29T03:44:52.576271+00:00.
Claim: N4-165 independently confirms T4-203's nonzero leading density profile for exact007.
Method: Read its complete raw-generator/complex-Fourier proof and code, freeze hashes, and compare every exact potential amplitude and the resulting first sine coefficient with our independent canonical calculation.
Result and verdict: CONFIRMED. The strict rational18<b1<19 and finite uniform expansion satisfy the numerical independence rule. The audited tail theorem therefore pins c for every exact solution in007's specified weighted affine class, including all registered unweightedL2 balls. The ball exclusions persist at any trialc under those same hypotheses; no cross-chart nonexistence claim.
Evidence: audit/theory_audit/research_code/weak_tail_canonical_application/reviews/N4_165/result.json, SHA256 bc06d154c0e20e0ba1c38d0dd2ca3331f1f2aef7424f57570917025ef9ce8f1d; ACCEPTANCE.md in the same folder.

## T4-209: Exact constraint rank and Taylor feasibility independently checked

Date: 2026-10-29T03:47:47.845517+00:00.
Claim: N4-164 gives tail rank420, linear rank421 and full constraint differential rank426 for exact007, hence a1496-dimensional physical potential tangent kernel.
Method: Rebuild all360 block endpoint minors by explicit shifted-Legendre binomial coefficients. Verify six exact tail-kernel directions and their block membership. Compute the complete6x6 differential with independent squared-coordinate polynomial jets, including the full local velocity, then compare all exact entries and candidate Taylor coefficients.
Result and verdict: CONFIRMED. The two determinant factors are about5.0707221803 and-0.1705546605, both nonzero. The2982 coefficient coordinates retain1060 zero-potential directions; their constraint kernel has dimension2556. The five nonconstant Taylor residual coefficients are small but nonzero, so the exact candidate is not on the zero-Taylor constraint manifold. Rank gives a smooth level set at its actual values; a zero-target manifold needs a feasible point. No PDE Jacobian rank or inverse follows. Runtime0.552485310seconds.
Evidence: audit record constraint_rank_audit, proof, SHA256 8f2eea22ca85127270e2cf2243bb5140a44c385a89d96ed9179f79459d68b58a; verification/result.json in that topic, SHA256 ad5af92ae4212c34f9260e1f3bb57894f08437f0caec83a2a0f9dd0715b1534b.

## T4-210: Exact common leading profile for state131,d2,and005 through012

Date: 2026-10-29T03:49:58.291027+00:00.
Claim: The ten named functions share the entire leading density profile, not only its first harmonic.
Method: Freeze each exact snapshot and manifest, sum all j=0 polynomial endpoints, and compare the full angular amplitude maps over the rationals. Check every multiscale legqs term has a positive scale and the exact fourth-order vanishing factor.
Result and verdict: OPEN numerical-lane reproduction of the new family table. All ten local checks pass in0.512671597seconds. Every leading potential amplitude equals state131's, and every first leading density sine coefficient equals the already CONFIRMED007 value, strictly between18 and19. Once the finite table is confirmed, audited T4-201 pins c in every listed weighted affine class. Existing fixed-c ball exclusions then extend to every trialc in the same chart, row by row. No new exclusion for unchecked balls or changed tail charts follows.
Evidence: audit record family_leading_tail, proof, SHA256 0933c13b979b43bfbcb2273405a9e9800532e287119265899c18e89c9f5dbf36; verification/result.json, SHA256 18a18ba0262e6f7b593b5858601f76668eafa0e4a47ada0b7c775ce42ad9acfc.

## T4-211: Exact triangular Taylor projection with a small L2 correction

Date: 2026-10-29T03:51:48.536225+00:00.
Claim: Five tail-kernel directions give an explicit rational, idempotent projection onto the five nonconstant Taylor equations, preserving a0,strain and all tail rows.
Method: Solve the two cubic residual coefficients exactly, recompute all quadratic correction interactions, then solve the three quintic coefficients by a lower triangular system. Reconstruct independently in canonical coordinates. Derive each direction's full-plane density L2 norm from exact Cartesian polynomial differentiation and beta moments.
Result and verdict: OPEN independent Opus theorem review and numerical-lane reproduction. All local exact checks pass, including six zero residual coefficients, every preserved tail moment and exact idempotence. The summed L2 perturbation bound is3.423716897e-12, below3.424e-12. Runtime1.701530591seconds. This tiny normalization repair cannot evade the existing007 distance obstruction. It is an unregistered algebraic artifact, not an accepted candidate or existence proof.
Evidence: audit record taylor_projection, proof, SHA256 640eaa21127a2b58e406abfae7aeb32a8b27bfcc37a6a500d68e64cc1e40a613; verification/result.json SHA256 95f704bf55f880c159eac5c3604535a19a7c2978cacc025241ffbf4a8f52198d; exact parameters.json SHA256 1af0b1ab66ef41bff38d0f58add1bcb72e36463c81a0919ea32a50cf510058a9.

## T4-212: Independent potential-to-density injectivity review accepted

Date: 2026-10-29T03:55:25.916207+00:00.
Claim: R1-024 independently confirms T4-199 and hence the exact density rank1922 for007.
Method: Read and freeze the full Opus proof review, arithmetic helper and output; check the decay, harmonic reduction and exponent-class separation step by step.
Result and verdict: CONFIRMED; T4-199 is AUDITED. No extra density gauge remains after the1060 zero-potential relations. Two harmless review errata are recorded: den(c) was used for the denominator of gamma, and ordinary integral legq factors actually remain polynomial in t and are covered. No PDE Jacobian rank or inverse follows.
Evidence: audit/theory_audit/research_code/potential_density_injectivity/reviews/R1_024/ACCEPTANCE.md; reviewed R1-024 SHA256 fa9e8301bb2e777005a208789a6bd9d1324fa63340ee3c7fd4615b18e37e41a1.

## T4-213: Independent common leading-profile family table accepted

Date: 2026-10-29T03:55:25.916207+00:00.
Claim: N4-172 independently confirms the entire leading density equality forstate131,d2,005 through012.
Method: Read its complete canonical/raw endpoint and complex Fourier proof and code, freeze the records, verify allten exact matches and source identities. Its endpoint recurrence differs from our binomial evaluation.
Result and verdict: CONFIRMED. T4-210 now satisfies numerical independence. The common18<b1<19 gives nonzero leading density, so audited T4-189/200/201 pins c throughout the stated canonical weighted affine correction classes. All already confirmed fixed-c ball exclusions transfer to every trial c in those classes. No unchecked011 ball or different tail chart is excluded here.
Evidence: audit/theory_audit/research_code/family_leading_tail/reviews/N4_172/ACCEPTANCE.md; N4 result SHA256 30a92741e59f1e53035435128050762e02600e45d8db5eea936df957e19ae8ea.

## T4-214: Theory_v03 Newton-step and held-out residual bounds

Date: 2026-10-29T04:00:48.631092+00:00.
Claim: R6(a), the corrected-domain interpretation of R6(b), and R9(e) follow from the weak adjoint identity.
Method: Redo integration by parts and the Hilbert adjoint argument; check the two endpoints of the affine held-out bound with512-bit Arb using independently certified mode7 inputs.
Result and verdict: CONFIRMED with the domain and probe-density hypotheses in the standalone proof. Every exact L2 Newton step from007 has norm>0.0047694; I/D=0.00476940290877443236. The held-out linear residual bound passes. Scalar runtime0.000896536seconds. No inverse or Newton convergence is established.
Evidence: audit record theory_v03_audit, proof, SHA256 8fe7d3cf2546f9f709ba7f33c3516f253b078e72bab06e973877c72751ef3dc3; frozen publication SHA256 e541f3ba19c8a67d51c5792600a461c971cc8575eab18ffeb07cc9a29c2e0b19. Scalar result SHA256 ffa1a7d0fb6fba2bd9a9787b9d8e9ff0b084f6b15339f9bdc4aca1002b09910e.

## T4-215: Theory_v03 full-span L2 Gram matrix is undefined

Date: 2026-10-29T04:00:48.631092+00:00.
Claim: R9(c) defines an L2 Gram matrix on the whole1922-dimensional density span after removing coefficient redundancy.
Method: Use the independently confirmed nonzero growing leading tail of007 and the exact generator reconstruction; derive the decay of the420-row tail-preserving kernel.
Result and verdict: REFUTED as stated: the full span contains007 itself, which is not in L2, so every basis has an infinite diagonal Gram entry. Restrict first to admissible correction directions. The1502-dimensional tail kernel lies in L2; strain gives1501, the five Taylor differentials give1496. A chosen L realization and row domain still need verification. The finite-span inverse obstruction in R9(d) is CONFIRMED only on such an admissible W with proved row domination. Zero modes should be expressed as nullity>=1060, or zero eigenvalues of J*J.
Evidence: audit record theory_v03_audit, proof, SHA256 8fe7d3cf2546f9f709ba7f33c3516f253b078e72bab06e973877c72751ef3dc3; frozen publication SHA256 e541f3ba19c8a67d51c5792600a461c971cc8575eab18ffeb07cc9a29c2e0b19. Scalar result SHA256 ffa1a7d0fb6fba2bd9a9787b9d8e9ff0b084f6b15339f9bdc4aca1002b09910e.

## T4-216: Theory_v03 defect feasibility omits its second condition

Date: 2026-10-29T04:00:48.631092+00:00.
Claim: Section3 says feasibility is equivalent to mu-Am-B>0 after printing epsilon_max.
Method: Redo the one-variable quadratic maximization and the exact counterexample A=m=B=1,mu=3.
Result and verdict: REFUTED as a sufficient or equivalent condition. Feasibility requires both mu-Am-B>0 and epsilon<=((mu-Am-B)^2-4ABm)/(4A). Even existence of some epsilon>=0 needs epsilon_max>=0. The example has epsilon_max=-3/4. This restores the already audited T4-065 statement; the underlying defect theorem and verified boxes are unchanged.
Evidence: audit record theory_v03_audit, proof, SHA256 8fe7d3cf2546f9f709ba7f33c3516f253b078e72bab06e973877c72751ef3dc3; frozen publication SHA256 e541f3ba19c8a67d51c5792600a461c971cc8575eab18ffeb07cc9a29c2e0b19. Scalar result SHA256 ffa1a7d0fb6fba2bd9a9787b9d8e9ff0b084f6b15339f9bdc4aca1002b09910e.

## T4-217: Theory_v03 closed-ball exclusion needs strictness

Date: 2026-10-29T04:00:48.631092+00:00.
Claim: R6(d) deduces exclusion of a radius-b ball from |I|>=Db+Hb^2.
Method: Compare the nonlinear necessary inequality at the boundary m=b; give the exact scalar equality example D=1,H=0,I=b=m>0.
Result and verdict: REFUTED as an inference for a closed ball. Require |I|>Db+Hb^2, or specify an open ball and a strictly increasing right side. No IPM boundary solution is asserted. Existing certified exclusions use positive strict gaps and remain valid.
Evidence: audit record theory_v03_audit, proof, SHA256 8fe7d3cf2546f9f709ba7f33c3516f253b078e72bab06e973877c72751ef3dc3; frozen publication SHA256 e541f3ba19c8a67d51c5792600a461c971cc8575eab18ffeb07cc9a29c2e0b19. Scalar result SHA256 ffa1a7d0fb6fba2bd9a9787b9d8e9ff0b084f6b15339f9bdc4aca1002b09910e.

## T4-218: Theory_v03 scaling identities and operator scope

Date: 2026-10-29T04:00:48.631092+00:00.
Claim: R7(a) gives the covariance, norm and probe scaling laws, and uses the infinitesimal dilation direction.
Method: Apply the degree-zero velocity multiplier, chain rule and change of variables; distinguish a formal linearized identity from membership in an operator domain.
Result and verdict: CONFIRMED for the canonical velocity and stated finite norms. The asymptotic for Lambda rho requires a differentiated remainder bound; the registered algebraic references have it, while a generic undifferentiated little-o statement alone is insufficient. The identities supply no inverse and do not put the dilation mode in the fixed L2 correction class.
Evidence: audit record theory_v03_audit, proof, SHA256 8fe7d3cf2546f9f709ba7f33c3516f253b078e72bab06e973877c72751ef3dc3; frozen publication SHA256 e541f3ba19c8a67d51c5792600a461c971cc8575eab18ffeb07cc9a29c2e0b19. Scalar result SHA256 ffa1a7d0fb6fba2bd9a9787b9d8e9ff0b084f6b15339f9bdc4aca1002b09910e.

## T4-219: Theory_v03 summary and localized-route scope

Date: 2026-10-29T04:00:48.631092+00:00.
Claim: The summary describes007 as closest, every001..007/refit as excluded from every registered ball, and normalized localization as incapable of enlarging the ball.
Method: Compare the actual per-framework coverage and use only norm domination under inf psi=0.
Result and verdict: REFUTED as deductions from the cited evidence. Lower distance bounds do not order actual distances; dyadic exclusions coverstate131,d2,007 rather than every listed candidate; norm domination forces a larger radius but does not forbid proving one. Objective rows remain valid evidence when rigorously violated. The remaining inverse and alternative-closure questions stay OPEN.
Evidence: audit record theory_v03_audit, proof, SHA256 8fe7d3cf2546f9f709ba7f33c3516f253b078e72bab06e973877c72751ef3dc3; frozen publication SHA256 e541f3ba19c8a67d51c5792600a461c971cc8575eab18ffeb07cc9a29c2e0b19. Scalar result SHA256 ffa1a7d0fb6fba2bd9a9787b9d8e9ff0b084f6b15339f9bdc4aca1002b09910e.

## T4-220: Nonlinear exponent-chart review accepted

Date: 2026-10-29T04:03:04.178632+00:00.
Claim: R1-025 independently confirms the three assertions of T4-205.
Method: Read all analytic steps, both diagnostic helpers and outputs, and verify the frozen source hashes.
Result and verdict: CONFIRMED; T4-205 is AUDITED. Distinct growing exponent tails are independent modulo E_a, finite log tangents do not contain finite exponent changes, and the parameterized tail is smooth into the stated weaker E_b. The diagnostic quadrature is not part of the proof.
Evidence: audit/theory_audit/research_code/nonlinear_tail_chart/reviews/R1_025/ACCEPTANCE.md; R1-025 SHA256 97f36cadf16e07bcfb08bb839761c97e4c5bfcb99405988b88eaabdf89cb2920.

## T4-221: Opus normalization and one-tangent dilation remarks

Date: 2026-10-29T04:03:04.178632+00:00.
Claim: R1-025 R1 makes exponent extraction unique but discontinuous in E_b; R3 excludes finite dilation from rho+span(Lambda rho)+E_a for0<=a<=2/c when the first two branch profiles are nonzero.
Method: Use smooth compact cutoffs for the discontinuity sequence and differentiate (exp(sx)-1)/x to get a strictly positive derivative for s!=0.
Result and verdict: CONFIRMED as analytic statements under the exact nonzero-profile hypotheses. The product norm is one sufficient topology, not uniquely required. The complete007 profile calculation agrees in two independent theory paths; numerical-lane confirmation of branches1..3 is requested separately.
Evidence: audit record dilation_chart_audit, proof, SHA256 e536a1b3e2046836cb18831e5d0e58a53810a27bc001537dbb43f57df8bed287.

## T4-222: Finite tail amplitudes contain the fixed-c dilation orbit

Date: 2026-10-29T04:03:04.178632+00:00.
Claim: For exact007 and a>=0, the quotient span of all dilation differences has dimension equal to the number of nonintegrable leading branches, at most4; at a=0 it is exactly4.
Method: Subtract cutoff leading tails in the finite asymptotic expansion. Prove independence by distinct powers and the dimension lower bound by the polynomial matrix z_i^k-1; recompute all branch first harmonics from canonical potential endpoints.
Result and verdict: OPEN independent Opus review of the new finite-augmentation theorem and numerical-lane confirmation of the new branch values. All eight first harmonics are locally exact nonzero; the4x4 determinant is288. The one-tangent obstruction stands, but the broad claim that only nonlinear coordinates can contain the dilation orbit is too strong. Unlike exponent variation, fixed-c dilation fits in a finite linear tail augmentation. No inverse or existence claim.
Evidence: audit record dilation_chart_audit, proof SHA256 e536a1b3e2046836cb18831e5d0e58a53810a27bc001537dbb43f57df8bed287; verification/result.json SHA256 1c0246c8793ab4fccb8069d3bbe8a0c304854f4926b4768b36eff38dd13b3cd1.

## T4-223: Opus review of the growing-weight derivative estimate accepted

Date: 2026-10-29T04:07:09.401367+00:00.
Claim: R1-026 confirms T4-206 on the centrally odd compact test class and its completion.
Method: Check every Fourier, tensor and completion step and inspect both independent diagnostic scripts and outputs.
Result and verdict: CONFIRMED; T4-206 is AUDITED. The weighted Hessian constant is sqrt(5/3), and the general tensor constant is sqrt(1+2/(k+1)), independent of R. This is an operator input, not a transport inverse. No new numerical assertion is made.
Evidence: audit/theory_audit/research_code/weighted_derivative_moment/reviews/R1_026/ACCEPTANCE.md; review SHA256 da81a3d1aee6f657ea00750f504394e72452aea8cd53bdf24332aac92da18979.

## T4-224: Sharp variational formula for the derivative first-moment constant

Date: 2026-10-29T04:07:09.401367+00:00.
Claim: R1-026 R2 identifies the sharp squared constant as max(1,Lambda_k), for all fixed R>0.
Method: Verify the Fourier annulus extremizing sequence, prove compact approximation explicitly, and supply a localized angular bump proof that Lambda_k>=1. Separate the S1 sine block from the full centrally odd space.
Result and verdict: CONFIRMED analytically; max(1,Lambda_k)=Lambda_k. The finite-matrix eigenvalues in R1-026 remain FLOAT and do not certify infinite-dimensional upper bounds. Sharpness for the full odd class must not be attributed automatically to S1.
Evidence: audit record sharp_derivative_moment, proof, SHA256 793f180058f9b3713be90136c47bfb1e8e8bfa1f77d76b4195a3f1d29d433e38.

## T4-225: Candidate008 frozen mode7 and mode1 distances independently reproduced

Date: 2026-10-29T04:08:25.576378+00:00.
Claim: N4-176 gives necessary L2 correction distances from the exact008 reference using the frozen007 probe vectors.
Method: Reconstruct polar density and stream polynomials from008's own canonical input, assemble the signed transport field and exact angular norm forms, differentiate the residual directly for its pairing, and sum all beta moments with2048-bit outward arithmetic. Independently certify H by interval mean-value subdivision. This differs from N4's Cartesian fields and its direct/parts pairing paths.
Result and verdict: CONFIRMED. The mode7 radius is0.001938714195960253317113... and its strict rational lower bound is387742839/200000000000; the mode1 radius is0.0002640568956462053109601... and its strict rational floor is52811379/200000000000. All six M,C,I interval comparisons agree. Real runtimes35.250957404s and38.645628918s. The theorem gives a necessary distance only. The audited common-leading-tail pinning extends it to any c within the same canonical affine correction class. These bounds do not order actual distances or prove a solution.
Evidence: audit record frozen_successor_probes, proof SHA256f252f4a09f1cab8f56668dd85635cf5d7ee578d82f861bb9a99b351e1119604f;008 n7 output SHA2563c4447299fcdba4ed6fbbd09a56db75a81ecb7f3950eee8b6396e9fd730f227c;008 n1 output SHA2563be4cb12ef3ee2574e1e60fecff17280e86c5047263002013c63c087158e7124. Canonical input SHA25613fe3fb1d9204b61e08599da7c4f5d6584034666040305bd01e4dde1783677f1.

## T4-226: Numerical branch-tail confirmation accepted

Date: 2026-10-29T04:09:34.338781+00:00.
Claim: N4-177 independently reproduces every exact branch first harmonic in T4-222.
Method: Inspect the raw-generator endpoint recurrence and full complex Fourier differentiation, then compare all eight exact scalar records and the threshold/determinant checks.
Result and verdict: CONFIRMED all eight branch amplitudes, nonzero signs and nonintegrability thresholds. The numerical hypotheses for the four-dimensional unweighted dilation quotient are now independently confirmed. The general finite-amplitude theorem still awaits Opus review.
Evidence: audit/theory_audit/research_code/dilation_chart_audit/reviews/N4_177/MANIFEST.json; peer result SHA25613668179a0e47fd76e1a5a16aba57f82d33cfe29fc4efee817e0f1cc9861aa8f.

## T4-227: Taylor repair arithmetic and distance transfer accepted

Date: 2026-10-29T04:09:34.338781+00:00.
Claim: N4-173 reproduces the five parameters, six vanishing equations and complete-plane triangle bound of T4-211.
Method: Inspect its independent Cartesian jet computation, direct Leibniz density derivatives and exact beta moments, including all twelve checks and original input hashes.
Result and verdict: CONFIRMED T4-211 arithmetic. The density perturbation has norm below3.423716897e-12, so the confirmed007 distance bound transfers to distance>0.004769166863 from this repaired reference in the same solution class. The sharper combined norm in N4-174 is not needed for this transfer and remains OPEN here. The general projection theorem still awaits Opus review; this algebraic artifact is not a registered candidate.
Evidence: audit/theory_audit/research_code/taylor_projection/reviews/N4_173/MANIFEST.json; peer result SHA256bc0b416c3db93b582bb6c96105997fe16ab3b0b4b20d8043ad5dc6a2f2b88939.

## T4-228: Physical constraints cannot remove redundant potentials

Date: 2026-10-29T04:09:34.338781+00:00.
Claim: N4-178 refutes absorption of38 out of1060 exact zero potentials by the426 physical constraints, and rejects invariance of physical damped steps under duplication.
Method: Factor every physical derivative through the potential map, prove the exact kernel sequence, and solve the one-coordinate and duplicated-coordinate scalar damped equations.
Result and verdict: CONFIRMED N4-178's mathematical counterarguments. The coefficient tangent is2556=1496+1060; all1060 redundant directions survive. At lambda=1 the physical damped steps are1/2 and2/3. The cause of a specific failed numerical step remains OPEN. This is a parameterization audit, not a PDE near-kernel.
Evidence: audit record quotient_parameterization, proof, sections1 and2, SHA2562f7493b79afd24f165c2d9e95c0fc672423be384c828fa7edea2b845be33e982.

## T4-229: Coordinate-invariant damping on a physical tangent

Date: 2026-10-29T04:09:34.338781+00:00.
Claim: A positive-definite physical tangent norm gives a unique damped physical step independent of any onto redundant parameterization.
Method: Complete the square for ||f+Jw||^2+lambda||w||_G^2 and pull it back through an onto map K. The pullback normal matrix has exactly ker K as its kernel; solutions form one affine coset.
Result and verdict: OPEN independent Opus review of this proposed optimizer design lemma. A density L2 metric must first restrict to the L2 tail tangent, then strain and Taylor differentials; the unrestricted1922-dimensional Gram is undefined. No improved conditioning or convergence is claimed.
Evidence: audit record quotient_parameterization, proof, section3, SHA2562f7493b79afd24f165c2d9e95c0fc672423be384c828fa7edea2b845be33e982.

## T4-230: Exact quotient map independently reproduced

Date: 2026-10-29T04:16:52.633791+00:00.
Claim: N4-175 gives an exact reduction of all 2982 potential coefficients to 1922 selected original generators.
Method: Expand the supplied relations by the closed-form shifted-Legendre formula, check all selected shapes and transformed coefficients, and reconstruct the whole canonical map without repeating pivot elimination.
Result and verdict: CONFIRMED all 1060 unit-nonpivot identities, all transformed coefficients and equality of the full canonical potential. Real runtime 0.837273971 seconds. Rounded convenience coefficients and optimizer conditioning are not certified.
Evidence: audit/theory_audit/research_code/quotient_parameterization/verification/map_result.json, SHA256 707235eed3154afca3d37843907eb266b5931ecf773442b098cade754c649345; code SHA256 a74d04363fd31c643f396ee3efd204fa6882dcb949afe4edc87b518245db2c31.

## T4-231: Candidate009 frozen weak distances independently reproduced

Date: 2026-10-29T04:16:52.633791+00:00.
Claim: N4-179 gives necessary correction distances for exact candidate009 using the frozen mode7 and mode1 probes.
Method: Use the independently reconstructed polar fields, direct residual derivatives, complete angular norm forms and 2048-bit outward beta moments, with an independent interval cover for the probe gradient.
Result and verdict: CONFIRMED. Mode7 distance exceeds 4241900989/250000000000 = 0.016967603956; mode1 exceeds 1882466903/1000000000000 = 0.001882466903. All six I,M,C comparisons agree. Real runtimes 44.781002133 and 33.553882781 seconds. These are necessary distances, not measured actual distances. Common-leading-tail pinning extends the exclusion to every c in the same audited affine class.
Evidence: audit/theory_audit/research_code/frozen_successor_probes/verification/009_n7_direct.json SHA256 7925d217d3bb3e82482efd2c4e5a1ec9b8a8b28c2fccd670a224594cf312e1fb; mode1 output SHA256 53cd1b2a1924249f5f61635c13625cf35e81f53b31f513717e4da917b3b12e04.

## T4-232: Opus finite-amplitude dilation review accepted

Date: 2026-10-29T04:16:52.633791+00:00.
Claim: R1-027 confirms T4-222 and retracts the overly broad claim that only nonlinear coordinates can contain finite fixed-c dilations.
Method: Inspect the complete proof, exact independent raw-generator endpoint check, thresholds and polynomial determinant argument.
Result and verdict: CONFIRMED; T4-222 is AUDITED, with all numerical branch hypotheses separately CONFIRMED by N4-177/T4-226. At unweighted L2 the dilation differences span four tail directions. One tangent remains insufficient. R1-027 B2 about PDE-forced lower tails remains HEURISTIC here.
Evidence: audit/theory_audit/research_code/dilation_chart_audit/reviews/R1_027/ACCEPTANCE.md; frozen review SHA256 5ea47305fee6f8f93fd0a3ff18f9be7b9e41e5f45af25b357273e99d3124f237.

## T4-233: Opus triangular Taylor projection review accepted with scope

Date: 2026-10-29T04:16:52.633791+00:00.
Claim: R1-028 confirms the local five-parameter projection, its exact candidate arithmetic and L2 perturbation estimate.
Method: Inspect all six analytic steps, independent symbolic leading matrices, exact beta moments and output; separate arbitrary-c algebra from membership in the frozen 007 generator span.
Result and verdict: CONFIRMED; T4-211 is AUDITED with the explicit restriction c=c_007 for membership in that frozen span. The local projection works for general nonzero c under its stated nonvanishing divisors, with the analogous c-dependent generators. The norm proof extends to c>1/3. N4-173 already confirms the candidate arithmetic. No registered candidate or existence theorem results.
Evidence: audit/theory_audit/research_code/taylor_projection/reviews/R1_028/ACCEPTANCE.md; frozen review SHA256 5ea47305fee6f8f93fd0a3ff18f9be7b9e41e5f45af25b357273e99d3124f237.

## T4-234: Canonical tail velocity and forced nonintegrable profiles

Date: 2026-10-29T04:20:55.391911+00:00.
Claim: For 0<gamma<1, c=1/gamma and N=floor(2/(1-gamma)), an S1 solution with expansion sum_(j=0)^(N-1) chi r^(1-(j+1)(1-gamma)) Theta_j plus an L2 remainder must obey the explicit triangular angular recurrence in the proof.
Method: Solve each nonresonant sine-even angular Poisson equation, construct the canonical cutoff velocity with a compact zero-mean curl correction, prove its O(r^-2) remainder and uniqueness, then apply the annular weak obstruction to each nonintegrable residual sector. No derivative of the L2 correction is needed.
Result and verdict: OPEN independent Opus review. The proposed theorem forces all lower nonintegrable profiles from the full leading angular profile; compatible tails have an L2 reference residual. For007 there are four such profiles. This resolves R1-027 B2's formal issue if confirmed, but gives no inverse or solution.
Evidence: audit record triangular_tail_equations, proof SHA256 b69f785ae141620bcf255c631a0075df63daea9d83538dfdf8e416fb28c60b6a.

## T4-235: Exact007 satisfies all three forced tail equations

Date: 2026-10-29T04:20:55.391911+00:00.
Claim: The exact007 density and stream endpoints satisfy the angular Poisson relations and the nonintegrable-sector recurrence of T4-234.
Method: Differentiate the homogeneous endpoint potential directly, expand each trigonometric product over Q and compare the first harmonics with the previously confirmed branch record.
Result and verdict: OPEN independent numerical-lane review. All four Poisson equations and all90 residual coefficients (20,30,40 by sector) vanish exactly. The lower profiles have20,30,40 nonzero odd harmonics through39,59,79. Runtime 0.256863607 seconds. The candidate-specific conclusion depends also on confirmation of T4-234's theorem.
Evidence: audit/theory_audit/research_code/triangular_tail_equations/verification/result.json SHA256 8907ede4fcf79d24434b56a6150256269705c43764b95b8561d63733014b728c; full exact profiles SHA256 f29d73ec42c0d98f9ea985a0461b43ab4a09664eba40a1b20853dbbcc2fa885e; canonical source153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316.

## T4-236: Candidate012 frozen weak distances independently reproduced

Date: 2026-10-29T04:29:39.046989+00:00.
Claim: N4-182 gives necessary correction distances for exact012 using the frozen mode7 and mode1 probes.
Method: Independent polar reconstruction, direct residual pairing and exact beta moments with2048-bit outward arithmetic, plus an independent gradient interval cover.
Result and verdict: CONFIRMED. Mode7 distance exceeds18641021007/1000000000000=0.018641021007; mode1 exceeds1427242229/200000000000=0.007136211145. All six I,M,C comparisons agree. Real runtimes35.038256342 and50.773956705 seconds. These are necessary bounds, not actual distance measurements. The audited common-leading-tail theorem extends them to every c in the same affine class.
Evidence: audit/theory_audit/research_code/frozen_successor_probes/verification/012_n7_direct.json and012_n1_direct.json.

## T4-237: Opus weighted-gradient review accepted

Date: 2026-10-29T04:29:39.046989+00:00.
Claim: T2 confirms T4-194 with the exact interval -1<p<3 on S1 and the centrally odd compact class and its completion.
Method: Inspect the complete analytic proof, symbolic helper and FLOAT diagnostics; separate new remarks from the reviewed theorem.
Result and verdict: CONFIRMED; T4-194 is AUDITED. R1 also gives the valid improved constant1/(1+p) for -1<p<0 using the full-space weighted L2 estimate. Additional claims in R2-R5 are not accepted merely by this entry.
Evidence: audit/theory_audit/research_code/weighted_gradient_velocity/reviews/T2_194/ACCEPTANCE.md.

## T4-238: Registered norm assembly and rounding audit accepted

Date: 2026-10-29T04:29:39.046989+00:00.
Claim: N4-180/181 reproduce the five registered forcing comparisons and identify non-directed endpoint displays.
Method: Check the monotone comparison from already confirmed G0,G1,P2,Q3, every exact threshold and all outward scalar enclosures.
Result and verdict: CONFIRMED. For007 sharpw, X lower bound>756.5312630768 and forcing/threshold ratio>3596535.57. All five sufficient tests fail. Nearest decimal rendering is not directed, but the wide published enclosures remain valid. No new ball exclusion follows solely from a sufficient-test failure.
Evidence: audit/theory_audit/research_code/registered_norm_assembly/reviews/N4_180_181/ACCEPTANCE.md.

## T4-239: Opus physical-metric damping review accepted

Date: 2026-10-29T04:29:39.046989+00:00.
Claim: R1-029 confirms T4-229, including the full1060-dimensional redundant kernel.
Method: Check all finite-dimensional arguments, the exact helper/output and remarksR1/R2.
Result and verdict: CONFIRMED; T4-229 is AUDITED. The affine version is valid when w0 actually solves the linearized affine constraints. No conditioning or convergence theorem follows.
Evidence: audit/theory_audit/research_code/quotient_parameterization/reviews/R1_029/ACCEPTANCE.md.

## T4-240: Unregistered Taylor repair is inside the generator span

Date: 2026-10-29T04:29:39.046989+00:00.
Claim: R1-029 R3 says the T4-211 repair is outside the generator span because it is unregistered.
Method: Compare the exact block expansion b_m t^(l-m)(1-t)^2 and the independent N4-173 membership checks.
Result and verdict: REFUTED. At c=c007 the five repair directions lie inside the exact frozen007 generator span. Unregistered only means no candidate ID. The further identification of the nonlinear repair with an affine linearized step remains OPEN pending a separate check.
Evidence: audit record taylor_projection, proof; audit/theory_audit/research_code/quotient_parameterization/reviews/R1_029/ACCEPTANCE.md.

## T4-241: Exact Taylor repair does not solve the linearized affine equation

Date: 2026-10-29T04:32:04.403232+00:00.
Claim: R1-029 R3 identifies the exact T4-211 repair eta with an affine step satisfying DC(ref)eta=-C(ref).
Method: Expand the quadratic residual exactly. The degree-six potential alpha x^4y^2+beta y^6 gives nonlinear contribution -192alpha^2 x^4-8640alpha beta x^2y^2 in F/y. Reconstruct the exact007 original and repaired jets and their differential.
Result and verdict: REFUTED. The affine defect is(0,0,192alpha^2,8640alpha beta,0); exact007 has alpha=2.4364087057814e-14... !=0. Its nonzero degree-four defects are1.1397287772686e-25 and-3.7451886634569e-24. The displayed formula is exact and the candidate scalar check agrees in0.603906780 seconds. The abstract affine minimization lemma and the nonlinear Taylor projection remain valid.
Evidence: audit record affine_taylor_audit, proof SHA256 acefdf5abddb4e8a6332bfb3c3a771eaf8f39ea07e129f671421cc5c3d122169; verification/result.json SHA256 c3feb9a3ba040cb948464fcfb42235b964e19ff595a01f511a4ec93f12770c06.

## T4-242: Weighted Hessian bound at p=2

Date: 2026-10-29T04:32:04.403232+00:00.
Claim: On the real centrally odd compact test class, ||(1+r^2/R^2)D2U[h]||2 <=(1+sqrt6)/2 ||(1+r^2/R^2)D2h||2, uniformly inR>0, with its canonical derivative completion.
Method: Mellin-transform the exact Beurling mode equation, compute the full Hessian quartic Q_m, prove the negative-mode factor11 by an explicit nonnegative polynomial identity, and pair conjugate real modes for factor6. Combine this homogeneous second moment with the audited first moment and unweighted estimate.
Result and verdict: OPEN independent Opus review. The new proof is complete locally; exact quartic, ordered-tensor and factorization checks pass in0.203688843 seconds. The Beurling squared factor6 is sharp on S1 by slowly varying annular mode1 tests. No sharpness of the velocity constant, transport inverse or existence conclusion is asserted.
Evidence: audit record weighted_hessian_second_moment, proof SHA256 82e9f46b3447202dc62f8bfcfe59d5ed13de90e4af8276bf0e82cc07dc4ade6e; verification/result.json SHA256 c0f14b8d967acb01b1d23d471371d1d9d9660d13f33143dcb68bfe0bdffb8361.

## T4-243: Weighted gradient sharpness remarks in their positive-weight range

Date: 2026-10-29T04:34:44.940933+00:00.
Claim: T2 the review of T4-194 R2 gives C*_p>=1, the exact sine-one ratio and a frozen-mode lower bound.
Method: Prove the lower bound by high-frequency S1 inputs and shrinking dilation; derive the exact angular cancellation and the Mellin ratio.
Result and verdict: CONFIRMED with0<=p<3 for the claimed decreasing frozen ratio and its zero-frequency supremum. The1.506199 scan remains FLOAT; no uniform1.51theorem is certified.
Evidence: audit record weighted_hierarchy_audit, proof SHA256 d1c70dc08da01a4fb3abdfc5bb548608b31f31499153ae8a4d55094482294270; verification/exact_scalars.json.

## T4-244: Negative-weight and residual-range scope corrections

Date: 2026-10-29T04:34:44.940933+00:00.
Claim: T2 the review of T4-194 R2 states the frozen ratio is decreasing without restrictingp, andR5 makes the whole007residual range available for the velocity.
Method: Atp=-1/2,M=1computeS(0)=37/245<1=lim S(infinity). Apply the already sharp gradient lower endpoint to p=-2.
Result and verdict: REFUTED as unqualified statements. Use0<=p<3 for the monotonicity argument, and intersect the007residual range withp>-1. These repairs change no closure verdict.
Evidence: audit record weighted_hierarchy_audit, proof SHA256 d1c70dc08da01a4fb3abdfc5bb548608b31f31499153ae8a4d55094482294270; verification/exact_scalars.json.

## T4-245: Higher derivative-row necessary intervals and the graded pair

Date: 2026-10-29T04:34:44.940933+00:00.
Claim: T2 the review of T4-194 R3/R4 give the exact scalar-gradient overlap and parity-dependent necessary endpoints for every derivative row.
Method: Construct compact S1 annular modes whose interior canonical velocity is a holomorphic polynomial; rescale and sum disjoint shells to exclude both lower endpoints. Use the nonzero exterior z^-3tail to exclude p>=j+2. Apply the audited scalar/gradient bounds componentwise for existing sufficiency.
Result and verdict: CONFIRMED. Oddj needs-1<p<j+2; evenj needs-2<p<j+2. Known sufficiency is-1<p<3foroddj and-2<p<2forevenj. The scalar weightp andgradientweightp+1rows overlap exactlyat|p|<2, withconstants5/3and2atp=4/5. No full higher-row sufficiency claim is inferred.
Evidence: audit record weighted_hierarchy_audit, proof SHA256 d1c70dc08da01a4fb3abdfc5bb548608b31f31499153ae8a4d55094482294270; verification/exact_scalars.json.

## T4-246: Forced-tail theorem independently reviewed by Opus

Date: 2026-10-29T04:40:16.884203+00:00.
Claim: R1-030 confirms T4-234, including the canonical velocity and annular weak necessity.
Method: Read the full analytic review, two helper scripts and both outputs; compare each sign, exponent, domain and normalization with the proof.
Result and verdict: CONFIRMED; T4-234 is AUDITED. Harmonic uniqueness also holds for a difference in O(r^gamma)+L2. The raw-generator 90-coefficient check supports T4-235, which still awaits the required numerical-lane confirmation. R3's positive-amplitude dilation classification is valid in the stated chart; a different angular shape lies outside that chart, not outside the general theorem.
Evidence: audit/theory_audit/research_code/triangular_tail_equations/reviews/R1_030/ACCEPTANCE.md and MANIFEST.json.

## T4-247: Affine Taylor defect independently accepted

Date: 2026-10-29T04:40:16.884203+00:00.
Claim: R1-029's two disputed Taylor-step assertions should be withdrawn.
Method: Inspect the author's erratum file review set 27, which recalculates the degree-six quadratic contribution by hand.
Result and verdict: CONFIRMED. The Opus author accepts T4-240 and T4-241: the nonlinear repair lies inside the frozen007span at c=c007, and its affine defect is (0,0,192alpha^2,8640alpha beta,0), nonzero for007. The erratum has no new numbered R1 theorem.
Evidence: audit/theory_audit/research_code/triangular_tail_equations/reviews/R1_030/ERRATUM_R1_029.md.

## T4-248: Candidate008 seven-cell dyadic obstruction independently reproduced

Date: 2026-10-29T04:43:00.808814+00:00.
Claim: N4-186 excludes008 from FW-T-DYADIC-Y-v1 over its full parameter interval by the audited origin-inverse ceiling.
Method: Own polar density and stream construction from the exact original potential; all contributing pairs for modes1,3,7; exact rational Laplacian polynomial squares, whole-plane monomial moments and2048-bit outward arithmetic. Check origin identities exactly and bound every parameter cell by monotonicity.
Result and verdict: CONFIRMED. All24mode energies and24norms agree with N4, as do all35cell quantities. Every cell has a strict positive margin; the smallest ratio exceeds58108067/12500000=4.64864536. Real runtime197.065616110seconds. The original sufficient dyadic scheme is excluded for0<a<2,0<s<1 and every fixed finite weight radius, under all its audited domain and normalization hypotheses. This does not prove nonexistence in other spaces.
Evidence: audit record successor_dyadic_reproduction, proof SHA256 b05433278e5cc74261107630c804f33d9d22604f3427bed8a6f2440803120216; code/check.py SHA256 dd28b8fc0333c7e4f29dc1627adb41910bfac752b778843424968dba1e492457; verification/008_result.json SHA256 11b7169abbd61e871a7f33a173eb7db149b183ce23dd64c189f38b59c1cb71e2; data/008_MANIFEST.json.

## T4-249: Weighted forced-tail classification including arbitrary finite powers

Date: 2026-10-29T04:43:00.808814+00:00.
Claim: For-2<a<=1+gamma,0<gamma<1 and E_a=L2((1+r2)^(-a)dX), an exact S1 profile with a finite homogeneous-power expansion in[a-1,gamma] modulo E_a has only the ladder e_j=1-(j+1)(1-gamma), with N_a=floor((2-a)/(1-gamma)) retained profiles and the triangular equations of234.
Method: Extend the sharp odd multiplier by reciprocal-weight duality; cancel the zeroth and first moments of the compact oddxy curl defect to obtain velocity error O(r^-3); prove uniqueness in O(r^gamma)+E_a; apply the audited annular weak obstruction. Close a finite power set under e+f-1 and inductively eliminate every non-ladder coefficient.
Result and verdict: OPEN independent Opus review. The standalone informal proof is complete, with exact threshold inclusion and no derivative of the correction. Compatibility is equivalent to reference residual membership. No negative-a candidate application, inverse or existence claim is made; subleading integer-shift powers of a regularized candidate must be checked separately.
Evidence: audit record weighted_forced_tails, proof SHA256 fbd41043a4eee5af83f8c1655f44da5724151ade7f078fa01eacb10d7376d1c9; verification/STATUS.md. No computation was required for this analytic extension.

## T4-250: Candidate 009 seven-cell dyadic obstruction independently reproduced

Date: 2026-10-29T04:49:27.158418+00:00.
Claim: N4-187 excludes C1-N1-009-d2w-j7-x3balk from the registered dyadic sufficient scheme.
Method: Independent exact polar fields, all contributing background pairs, rational Laplacian polynomial products, whole-plane moments and 2048-bit outward arithmetic. Check exact origin identities and all seven parameter cells.
Result and verdict: CONFIRMED. All 48 mode and 35 cell comparisons overlap. The minimum ratio exceeds 51016411/50000000 = 1.02032822. Real runtime 257.701175391 seconds. This excludes FW-T-DYADIC-Y-v1 over 0<a<2, 0<s<1 and every fixed finite weight radius under the audited origin-inverse hypotheses. It is a sufficient-scheme obstruction, not a general nonexistence theorem.
Evidence: audit/theory_audit/research_code/successor_dyadic_reproduction/verification/009_result.json SHA256 1f0b8d85423aa012909215c674f9a6165c7aecd7c0aa324963b91f75cd8622e7; data/009_MANIFEST.json; shared proof SHA256 b05433278e5cc74261107630c804f33d9d22604f3427bed8a6f2440803120216.

## T4-251: Constructive affine lift of the origin constraints

Date: 2026-10-29T04:49:27.158418+00:00.
Claim: A degree-eight adjustment tau converts the audited nonlinear five-parameter Taylor repair eta into the unique affine feasible step z in that five-dimensional space.
Method: Solve the exact triangular derivative block against (0,0,192 alpha^2,8640 alpha beta,0). Verify the standalone proof before reconstructing local and canonical jets; use exact rational whole-plane direction norms for a perturbation bound.
Result and verdict: OPEN independent Opus theorem review and numerical reproduction. All five affine constraints vanish exactly in the local 007 calculation. Its nonlinear constraints are the opposite quadratic defect, as predicted. Origin slope, strain and tail rows are preserved in the frozen 007 span. The extra density norm is below 1e-24 (computed triangle bound 1.3465347243e-26); total affine-step norm below 3.424e-12. Runtime 5.116371900 seconds. This supplies a valid particular step for T4-229, not an exact PDE solution.
Evidence: audit record affine_taylor_lift, proof SHA256 b7cabefd300571db84da827dc83acb7a56ff74abac9fc89fb32342587884cb4c; verification/result.json SHA256 75338792fb90fd2ce329fe2644d59a784d744cc6cae414c9921b193d7b9488fd; exact parameters in verification/parameters.json.

## T4-252: All 007 nonintegrable tail recurrences independently confirmed

Date: 2026-10-29T04:49:27.158418+00:00.
Claim: N4-189 confirms all full profiles and all 90 lower-tail coefficients in T4-235.
Method: Inspect the independent Cartesian endpoint and complex Laurent proof and code; bind source and dependency hashes and compare the complete density and stream coefficient dictionaries exactly.
Result and verdict: CONFIRMED. T4-235 now has the required numerical-lane confirmation. Every Poisson, polar velocity, gradient and recurrence check passes. Together with the already audited T4-234 this verifies that 007 satisfies the four-profile L2 compatibility equations. It does not establish an inverse or an exact solution.
Evidence: audit/theory_audit/research_code/triangular_tail_equations/reviews/N4_189/ACCEPTANCE.md and MANIFEST.json; frozen result SHA256 da144163de510fe2b91aa45884ac1e170b15c38df218feca1ac76497021d1949.

## T4-253: Candidate013 exact raw conversion and frozen weak tests

Date: 2026-10-29T04:58:36.222366+00:00.
Claim: The exact published013 preserves the four full007 tails and admits the two frozen weak-distance evaluations.
Method: Independent exact shifted-Legendre expansion of all2982 raw generators into1922 canonical terms; exact polar origin and endpoint checks; whole-plane2048-bit polynomial moments with every contributing angular mode and separate direct/by-parts pairings. The frozen gradient bounds are independently rechecked by interval subdivision.
Result and verdict: OPEN numerical peer. All local tests pass. The first four full density and stream profiles equal007 exactly, the strain is1-c, and a0 is positive. Frozen mode7 gives distance>7094343/125000000000=0.000056754744; mode1 gives>6590501/1000000000000=0.000006590501. Both are below the universal graded-ball ceiling; these tests alone do not exclude that whole family. Actual build/runtime seconds: 8.213035255, 86.718340167, 69.358009200. No claim orders the true distances of007 and013.
Evidence: audit record new_successor_weak, proof SHA256 10bde5e173b07f189d8245da5164fae162eb1b4256b06f0a0063420d11f52715; verification/013_build.json,013_n7_direct.json,013_n1_direct.json. Raw source SHA256 c07f87ddfe35e1fd82cfb86e01949749381aac7209a752c713dd01b48a478940; canonical SHA256 25842fdc120de25565f7f5881d24f35fdee73d7ad9309718455587fc4f1dab22.

## T4-254: Second independent Opus review of the canonical tail theorem

Date: 2026-10-29T04:58:36.222366+00:00.
Claim: T2's the review of T4-234 confirms the full analytic proof and proposes canonical-velocity and finite-power extensions.
Method: Read the complete review and compare the polar equations, cutoff moments, harmonic uniqueness and weak annular exponents with the frozen theorem and T4-249.
Result and verdict: CONFIRMED for the analytic review and its R1,R2,R4 conclusions with the minor compact-core and empty-set qualifications recorded in ACCEPTANCE.md. T4-234 remains AUDITED. R3's new multi-candidate arithmetic is not independently reexecuted here;007 already has separate numerical confirmation. The finite-log expectation in R2 remains OPEN until a separate proof is reviewed.
Evidence: audit/theory_audit/research_code/triangular_tail_equations/reviews/T2_234/REVIEW.md SHA256 1c47f92e8f31651569ae8ee2a281d9df0d11dbfebc7247836bdf2bb995b46473; MANIFEST.json and ACCEPTANCE.md.

## T4-255: Candidate013 held-out high-angular probe

Date: 2026-10-29T05:02:20.532357+00:00.
Claim: The exact013 fails the registered graded L2 budget by a held-out n=21,K=522 probe.
Method: Full exact polar fields and angular cross terms; keep t^522 factored and integrate by a positive beta recurrence at2048bits. Compute the signed pairing directly and by parts. Prove the global probe-gradient maximum through the two exact quadratic critical roots and the angular critical point.
Result and verdict: OPEN numerical peer and review of the new supremum implementation. Both pairing enclosures agree at I=-1.8366244908740e-5, M=0.00519519768712, C=0.00402313285653. The strict necessary distance is>199234339/100000000000=0.00199234339, exceeding25/54684 by a factor4.35797224. This would exclude the registered graded budget upon independent confirmation. All2387radial terms have exponent>-1; minimum is-gamma. Actual runtime32.106214681s. The sharper result than the N1 FLOAT estimate uses combined M, the exact angular C weight and a sharper H; it is not an independent discrepancy claim.
Evidence: audit record high_power_weak_probe, proof SHA256 c0d5bee2edf8d971dd20d7a169918adcbb81347418821e74fa8e158c40f063a3; code/check.py SHA256 ceca468bc444a28f031967dd84f47bccc31d6ea97679349bd4171d9f8e935d19; verification/013_n21_k522.json SHA256 28e34ca4f18c5aff627facb2f205ebc371233b9ec99b55737e652412e7d8871a. Exact probe in data/probe_21_522.json. Source conversion is T4-253, itself OPEN numerical peer.

## T4-256: Finite logarithmic corrections give no extra tail parameters

Date: 2026-10-29T05:02:20.532357+00:00.
Claim: For-2<a<=1+gamma, every finite expansion sum chi r^e P_e(log r,theta), e in[a-1,1), compatible with an exact S1 weak solution modulo E_a has only the pure-power ladder e_j=1-(j+1)(1-gamma), with all logarithmic degrees zero and the forced triangular profiles.
Method: Solve the nonresonant angular stream equation polynomially in log r; use oddxy moment cancellation for the O(r^-3) curl correction; extend the annular necessity test to the largest exponent and logarithmic degree; close a finite exponent set and induct downward. The leading transport equation kills positive log degrees even at its root e=gamma.
Result and verdict: OPEN independent Opus review. Complete standalone informal proof, including the weighted endpoint and arbitrary finite input exponents below1. No numerical computation. This rules out extra polynomial-log tail coordinates in the specified class if confirmed; it gives no inverse or existence theorem and does not treat inverse-log or infinite expansions.
Evidence: audit record finite_log_tails, proof SHA256 fa36215d9c78b69e85e1829d12b29b5d84c4ac21c4818b4991eeb1db2cf0d261; verification/STATUS.md.

## T4-257: N4 rational-pole integration independently verified

Date: 2026-10-29T05:02:20.532357+00:00.
Claim: N4-190's rational-pole scalar primitive is correct under its endpoint and multiplicity hypotheses.
Method: Audit the full proof and frozen code. Independently obtain partial fractions by exact coefficient-system Gaussian elimination, not local pole expansions. Evaluate each k-th pole moment directly by2F1(k,b+1;b+2;-a), not the peer's k-recurrence. Retain the documented exact-integer parameter flags. Compare with rerun peer values and all stored elementary or rigorous panel checks.
Result and verdict: CONFIRMED. All31peer fixtures and8new cases pass, including7resonance values and b=-999/1000; every exact reconstruction and interval comparison passes at2048bits. Runtime0.165827849s. The proof requires b>-1 after exact cancellations and positive integral pole orders; it supplies no candidate norm by itself.
Evidence: audit record rational_pole_audit, proof SHA256 a64e600e651b67d9f4aa6ec8e29085d23cc9e72894d26d6a37d0fa3deb10adfb; code/check.py SHA256 32e831f745a246ab6196784fea4d30cff5f3e244ce0e09f2b1ee96c8979eb5d4; verification/result.json SHA256 5be4cfc564286627fd424cf0f5b9a0d0ef5ba639f6ed74bf144510e5f1917988; frozen sources and installed2F1doc under source/ and verification/.

## T4-258: Zero-parameter Woodbury margin does not certify the positive-real axis

Date: 2026-10-29T05:07:16.246476+00:00.
Claim: The finite-rank sentence in THEORY_FINAL draft3 section2.4 would verify (L0) from its displayed zero-parameter hypotheses.
Method: Compare the full audited continuation proof and give the exact rank-one fixture D=-I, A=-I+2P.
Result and verdict: REFUTED as a standalone sufficient implication. M(0)=-1 and A inverse norm1, but A has eigenvalue+1. The full source theorem remains valid; a uniform-in-k positive-real-axis certificate and consistent maximal generators are required.
Evidence: audit record theory_final_draft_audit, proof SHA256 0378fab17bbaff0fbb07ed2ba2e50a8f56731815dc0ae5ca84e23082b7cbaf54; frozen draft SHA256 73aa2b484bff6e15c1cd762f918cf4192d1ec6b9ae1cc56ca5c3cb39ec85e7f2; verification/manifest.json.

## T4-259: Selected forcing spaces are incomparable

Date: 2026-10-29T05:07:16.246476+00:00.
Claim: THEORY_FINAL draft3 says sharpw at t=1/5184 has a larger forcing space than A2 at s=2^-18.
Method: Construct disjoint translated high-frequency S1 bumps and shrinking low-frequency S1 annuli; prove weighted Hessian bounds by Fourier first moments and verify completion membership.
Result and verdict: REFUTED as a set inclusion. Neither space contains the other at the selected exponents. At a common exponent dropping Hdot^-1 is a strict enlargement. Fewer far-field sectors is correct, but330.8 compares tolerances in different norms, not a common residual ball. New Fourier proof awaits Opus review.
Evidence: audit record theory_final_draft_audit, proof SHA256 0378fab17bbaff0fbb07ed2ba2e50a8f56731815dc0ae5ca84e23082b7cbaf54; frozen draft SHA256 73aa2b484bff6e15c1cd762f918cf4192d1ec6b9ae1cc56ca5c3cb39ec85e7f2; verification/manifest.json.

## T4-260: Localized weights retain the necessary distance radius

Date: 2026-10-29T05:07:16.246476+00:00.
Claim: THEORY_FINAL draft3 section6 excludes the localized route from NC-T-DIST because its domination factor is not large.
Method: Use the exact embedding inequality ||h||2<=C||h||Y, with C=1 after inf psi=0.
Result and verdict: REFUTED for that exception. Every007 localized exact correction has weighted norm>0.004769166867. No universal upper radius has been proved for this route, so this alone does not exclude it. Section2.7 already states the correct distinction.
Evidence: audit record theory_final_draft_audit, proof SHA256 0378fab17bbaff0fbb07ed2ba2e50a8f56731815dc0ae5ca84e23082b7cbaf54; frozen draft SHA256 73aa2b484bff6e15c1cd762f918cf4192d1ec6b9ae1cc56ca5c3cb39ec85e7f2; verification/manifest.json.

## T4-261: Compression parity and graded norm scope rechecked

Date: 2026-10-29T05:07:16.246476+00:00.
Claim: The complementary-parity compression and H^(2+s) graded ceiling in THEORY_FINAL are supported by their source proofs.
Method: Read the unsigned and signed Hilbert-Schmidt budget proofs and the Fourier identity underlying the top-margin bound.
Result and verdict: CONFIRMED with explicit complementary-parity qualification. S1 compressions instead require the q^2 signed repair and yield a quadratic-form upper bound. The graded ceiling controls the full H^(2+s) norm, not only L2.
Evidence: audit record theory_final_draft_audit, proof SHA256 0378fab17bbaff0fbb07ed2ba2e50a8f56731815dc0ae5ca84e23082b7cbaf54; frozen draft SHA256 73aa2b484bff6e15c1cd762f918cf4192d1ec6b9ae1cc56ca5c3cb39ec85e7f2; verification/manifest.json.

## T4-262: Fixed-ball budgets distinguished from parameter-family ceilings

Date: 2026-10-29T05:07:16.246476+00:00.
Claim: The fixed-ball L2 radius in section2.1 is the table value3.0927e-6 or2.8496e-6.
Method: Divide each exact listed r by sqrt(w2), and compare with the separately optimized family bound.
Result and verdict: REFUTED if read as the radius implied by that fixed ball; CONFIRMED as a conservative universal family ceiling. Fixed values are1.435546875e-6 and1.3193359375e-6. Relabel the existing row; all uniform exclusions remain valid.
Evidence: audit record theory_final_draft_audit, proof SHA256 0378fab17bbaff0fbb07ed2ba2e50a8f56731815dc0ae5ca84e23082b7cbaf54; frozen draft SHA256 73aa2b484bff6e15c1cd762f918cf4192d1ec6b9ae1cc56ca5c3cb39ec85e7f2; verification/manifest.json.

## T4-263: Independent polar confirmation of N4-200

Date: 2026-10-29T05:12:45.568952+00:00.
Claim: The weaker high-angular013 probe gives a necessary L2 distance above0.001123713803.
Method: Independently assemble exact polar angular energies, integrate all radial cross terms by positive beta recurrences, and compare I,A,B,C,D,H and the root with frozen Cartesian N4-200.
Result and verdict: CONFIRMED. All six scalar intervals overlap, the exact H agrees, and the strict rational floor1123713803/10^12 is verified. Runtime47.998138199seconds. This alone excludes the registered graded ceiling.
Evidence: audit record high_power_peer_audit, proof; code/check.py; verification/result.json.

## T4-264: Sharper candidate013 weak distance independently confirmed

Date: 2026-10-29T05:12:45.568952+00:00.
Claim: T4-255 gives necessary L2 distance>0.00199234339.
Method: Read and freeze N4-204 full proof, code, manifest and result; recheck source binding, all calibration flags, eight scalar interval comparisons and strict floor. Independent Cartesian assembly and v-endpoint integration reproduce the original polar calculation.
Result and verdict: CONFIRMED. T4-255 and its013 canonical source now have independent numerical confirmation. The bound exceeds25/54684 by a factor>4.35797. The all-c exclusion uses the separately audited pinning and common leading tail. Frozen mode7/mode1 values of253 remain separate OPEN numerical tasks.
Evidence: audit/theory_audit/research_code/high_power_weak_probe/reviews/N4_204/ACCEPTANCE.md and MANIFEST.json; peer result SHA256 8617acf19e20d4afad3d44c52f623cde32fd87f0fb586ed9196e9ced35994038.

## T4-265: Affine Taylor lift candidate arithmetic confirmed

Date: 2026-10-29T05:12:45.568952+00:00.
Claim: T4-251 exact affine correction and perturbation-size bounds hold at007.
Method: Read N4-198 ordinary Cartesian jet proof and implementation; compare exact tau parameters,15and19canonical coordinate counts, all stored equation/invariance flags, and both norm intervals against the original squared-coordinate computation.
Result and verdict: CONFIRMED for candidate arithmetic. Tau density norm<1e-24 and affine z density norm<3.424e-12. The affine equation is solved exactly; the nonlinear residual remains the explicitly stated quadratic defect. General real-c theorem OPEN Opus.
Evidence: audit/theory_audit/research_code/affine_taylor_lift/reviews/N4_198/ACCEPTANCE.md and MANIFEST.json; peer result SHA256 53e6495c0d7b48d7298c0d98d943b2b1d68990927dbb98a05963b7cdd78faa60.

## T4-266: Candidate013 point exclusions independently confirmed

Date: 2026-10-29T05:19:15.980360+00:00.
Claim: N4-201 point values and all recorded necessary gaps at(1/10,73/100).
Method: Reconstruct all raw generators by exact local radial Taylor coefficients and polar differentiation through order4. Check all8field/norm values,7fixed-ball upper bounds and roots, the uniform graded gap, and rational endpoint extensions. The fifth graded radius is reconstructed from its exact squared formula.
Result and verdict: CONFIRMED. F=0.0908758992838998273876392094091; uniform graded gap=0.0704737547511889926070490947614; sharp and sharpw gaps=0.0780504248242110473052479900576 and0.0708811112476429782324950117573. The signed principal criterion is inconclusive at this point. Actual runtime1.710063548seconds.
Evidence: audit record candidate013_point, proof; code/check.py; verification/manifest.json and results.json SHA256 e6dec5f8067f5eeb220255c5aca30faccb60691335dd5cf34ad0405f6a364514.

## T4-267: Scaled rational field engine independently audited

Date: 2026-10-29T05:19:15.980360+00:00.
Claim: N4-191 correctly reconstructs the stated scaled potential class and its first4Cartesian derivative orders.
Method: Prove the rational constructor, quotient rule and full angular derivative recurrence. Independently expand ordinary bivariate Cartesian Taylor series with exact coefficients and one outward noninteger power per generator. Compare15potential derivatives and6physical fields at6points for each of2mixed-scale fixtures, including signed and axis points. Check12rational arithmetic evaluations, exact mixed derivative identities, quotient rule and rejection of invalid origin division/float input.
Result and verdict: CONFIRMED for the algebraic engine and listed252independent scalar comparisons. Runtime0.204170222seconds. The peer007specialization is not recomputed in this task; its previously calibrated values remain separate evidence. This does not by itself certify010moments or its weak radius.
Evidence: audit record scaled_field_audit, proof; code/check.py; verification/source_manifest.json and result.json SHA256 29d35bdd9979e4df34b91f2967630d860d1a0aee5ec72fa70440c73445f69c0e.

## T4-268: Weighted forced-tail classification accepted after independent Opus review

Date: 2026-10-29T05:30:14.185453+00:00.
Claim: T4-249 in the exact range -2<a<=1+gamma, including threshold equality.
Method: Read and freeze the complete independent T2 review and code; recheck odd-space duality, vanishing moments, weighted Liouville uniqueness, annular estimates and descending induction. Verify exact first-sector exponents and all stored Poisson flags for five candidate checks.
Result and verdict: CONFIRMED. T4-249 is AUDITED. The review's finite-power extension to exponents below1 is also confirmed by the explicit descending argument. Numerical matrix and angular-norm illustrations remain FLOAT. The separate finite-log theorem256 still awaits its independent review.
Evidence: audit/theory_audit/research_code/weighted_forced_tails/reviews/T2_249/ACCEPTANCE.md and MANIFEST.json; original proof SHA256 fbd41043a4eee5af83f8c1655f44da5724151ade7f078fa01eacb10d7376d1c9; independent review SHA256 5a82df2ae2d2f82bc993b7bc513e88191ad6056400f18ffa4fa96dbcac8c63f3.

## T4-269: General affine Taylor lift accepted after Opus review

Date: 2026-10-29T05:36:59.670659+00:00.
Claim: T4-251 for every nonzero real c satisfying (a-4c+2)(a-8c+4) != 0.
Method: Read and freeze R1-031 and its full symbolic Cartesian checker. Recheck the block triangular derivative, exact quadratic vector and explicit correction. The review supplies the general-c existence argument for eta by the same triangular nonlinear system; numerical values already have N4-198 confirmation.
Result and verdict: CONFIRMED. T4-251 is AUDITED. The affine solution is unique in the stated five-dimensional span, preserves origin slope and strain, and has exactly the stated quadratic nonlinear defect. Frozen-basis membership and the two tail rows refer to c007. Smallness of a jet correction makes no whole-plane existence claim.
Evidence: audit/theory_audit/research_code/affine_taylor_lift/reviews/T1_R1031/ACCEPTANCE.md and MANIFEST.json; review SHA256 b9476a4ccfac8e6464247701710e69b73bba8f6946443a3544e5298d3cf6a89b.

## T4-270: Independent scaled-polar confirmation of candidate010 mode7

Date: 2026-10-29T05:36:59.670659+00:00.
Claim: N4-205 necessary L2 correction distance exceeds 0.022479506978.
Method: Reconstruct raw scaled generators with independent Legendre coefficients and polar differentiation. Calibrate all007 fields exactly and compare six010 point quantities. Assemble all angular cross terms. Integrate each rational radial moment by exact polynomial CRT and direct Arb2F1, independently of N4's reciprocal series and pole-order recurrence. Compare direct and integrated-by-parts pairings, M, C and radius.
Result and verdict: CONFIRMED. I=-8.32059152046976982796507533575e-5, M=0.00159290252304286532691947582668, C=0.00210764618291847067745617417089; the root is 0.022479506979890299528531989367. All five peer intervals overlap; strict floor 11239753489/500000000000 is verified. All 64 radial moments pass exact reconstruction and more than150 relative bits. Actual runtime 670.7652528584003 seconds. This necessary-distance test closes the remaining010 statL and bL scalar balls and exceeds the registered graded ceiling25/54684. The all-c interpretation still uses the separate common-leading-tail and pinning hypotheses. Mode1 remains pending.
Evidence: audit record scaled_polar_weak, proof; code/check.py; verification/010_n7.json SHA256 2548752c2002d17536fb9485a75e6494f266cbc745c34e8efd8562ff10273d68.

## T4-271: Finite polynomial-logarithmic tails accepted after Opus review

Date: 2026-10-29T05:39:46.019973+00:00.
Claim: T4-256 for c>1, -2<a<=1+1/c, finite smooth S1 polynomial-log tails with exponents in[a-1,1), and an assumed canonical weak solution modulo E_a.
Method: Read and freeze the complete Opus review and both scripts/logs. Check the positive even angular inverse, triangular log recursion, compact-curl moment cancellation, weighted annular endpoint and finite descending closure. The proof uses no pointwise decay or derivatives of the correction.
Result and verdict: CONFIRMED. T4-256 is AUDITED. All logarithmic coefficients vanish; the pure-power profiles are forced by c and the leading profile. Interpret the largest exponent as the largest with nonzero profile, and cutoff independence as independence for a fixed total density. No inverse or existence is supplied. The review's separate global resonance wording is corrected in272.
Evidence: audit/theory_audit/research_code/finite_log_tails/reviews/T2_256/ACCEPTANCE.md and MANIFEST.json; frozen review SHA256 98a64a7bbec8cfb7949909404a6f70999d0a948ab2bb7bf3507749d74b0c7645.

## T4-272: Exact scope of the homogeneous-stream resonance interval

Date: 2026-10-29T05:39:46.019973+00:00.
Claim: T2 review of256, R3, calls -3<e<1 exactly the log-free range.
Method: Diagonalize the angular operator on positive even sine modes. Give the explicit e=-4 stream(1/2)r^-3 sin(2theta), and check the two resonant endpoint examples.
Result and verdict: REFUTED if read as the set of all nonresonant real exponents. CONFIRMED as the maximal connected interval containing gamma in(0,1), for arbitrary S1 profiles. Nonresonance fails precisely at e=2k-1 or e=-2k-1 for positive integers k; some profiles at those exponents can still be solvable. The endpoint examples are correct and the theorem256 is unchanged. No conclusion about every possible formulation at a<=-2 follows.
Evidence: audit record stream_resonance_scope, proof; frozen T2_256 review and supplement.

## T4-273: Damped numerical plateaus do not establish a span-wide floor

Date: 2026-10-29T05:39:46.019973+00:00.
Claim: numerics_v07 section2 and summary infer the whole-span residual floor0.338, identify the span as the obstruction, and use two damping values as a bracket for the undamped answer.
Method: Solve the one-dimensional damped quadratic exactly. Both positive damping steps lie on the same side of the undamped solution; near-zero Jacobians give an arbitrarily flat plateau with exact minimum0. Prove the correct upper-bound direction and continuous dual lower-bound certificates.
Result and verdict: REFUTED for these inferences from the displayed experiments. The experiments remain FLOAT. The report's section4 already acknowledges unresolved conditioning. The independently proved lower bound for an exact Newton correction remains valid and continues to exclude its small balls; it does not turn a damped least-squares step into an exact solution or certify0.338 as the minimum residual.
Evidence: audit record damped_diagnostic_scope, proof and verification/MANIFEST.json; frozen numerics_v07 SHA256 8fb65706ecd07ff52be92b0604483c0b02a19ac8de483bc755c3b967d8661c33.

## T4-274: Candidate010 mode1 independently reproduced

Date: 2026-10-29T05:44:01.142700+00:00.
Claim: N4-207 gives a necessary fixed-c L2 correction distance above0.00062746942.
Method: Independent scaled-polar generator reconstruction and angular assembly, exact polynomial CRT and direct Arb2F1 radial integration, and separate direct and weak pairings. The v2 C assembly uses the exact symmetry recorded in code/C_SYMMETRY.md.
Result and verdict: CONFIRMED. I=-1.09634391636405729721580867167e-7, M=0.000110678673331925860779204428503, C=0.0000640132943262035655381203326992, root=0.000627469421213087299084707928. All five peer intervals overlap, all64radial moments pass exact reconstruction and150relative bits, and the strict rational floor31373471/50000000000 is verified. Runtime341.02062100404873seconds. This is weaker than mode7, already confirmed270, but independently exceeds the registered graded ceiling.
Evidence: audit record scaled_polar_weak, proof; code/check_v2.py; verification/010_n1.json SHA256 186a2d27c0001264680bc57f2e627de3eb57a960dfa5b813f8d46db2d22fde7a. Completion timestamp 2026-10-29T05:42:05.827129+00:00.

## T4-275: Omitted q4 far-field coefficient confirmed independently

Date: 2026-10-29T05:44:01.142700+00:00.
Claim: N4-195 identifies a nonzero first-sine term at exponent gamma-8 in the exact007residual, omitted by the q<=3model.
Method: Reconstruct the first density harmonic from the branch-zero canonical potential, expand its exact radial polynomial in z=r^-2, and multiply its q-th coefficient by -2cq. Compare all q=0,...,6rational coefficients with the independent homogeneous-potential calculation. Check exact nonresonance against every other branch and quadratic exponent.
Result and verdict: CONFIRMED. All seven density and residual coefficients agree exactly. The q4coefficient is about8.549703308646135e10 and cannot be cancelled by another branch. Runtime0.029653115663677454seconds. This certifies the omitted term; its size alone gives neither a global pairing-error bound nor a spatial remainder bound.
Evidence: audit record omitted_far_sector, proof SHA256 aab6fefa60c2e22b05a0b7c0a89ad4988ed31e1c9804a1970015066f50ea426b; code/check.py SHA256 7fb4715b2e20e56fbae5dcfbb0f0c5adce05c900362e5a1d1dbc53910a85cd91; verification/result.json SHA256 1c1d57752d6422ffb7fc93fcf586bdf0a919f4a0514379a0c335dcc426319706.

## T4-276: Full far-field pairings and finite-model errors reproduced

Date: 2026-10-29T05:48:21.161405+00:00.
Claim: N4-209's nineteen full-plane first-sine pairings and fifteen finite-model errors for007 are correct.
Method: Reconstruct all exact polar background fields independently; assemble4044stream-density interactions by weak integration by parts. Recover the complete first-sine residual by an exact radial adjoint identity. Integrate directly and by parts with positive Beta recurrences. Compare all30retained asymptotic coefficients exactly, plus the nonzero q4coefficient. Compare both peer endpoint formulas and every recorded model-error scalar.
Result and verdict: CONFIRMED. All19pairings agree; minimum relative accuracy1805bits. All30model coefficients and q4agree exactly. All15actual model errors are strictly larger than the last retained term. At K3162 the relative error is6060.86479429; at K10000 the signs differ and the relative error is42.57690739. At K1e10 the relative error is1.36539939610e-13. Runtime116.49343770183623seconds. This is a finite list of whole-plane scalar identities, not a uniform asymptotic remainder bound or a norm upper certificate.
Evidence: audit record full_far_pairing, proof SHA256 85f06fb71c9e971ff549539b5bf0733e854fd053e47e058321dc054b78f4080b; code/check.py SHA256 f21bd9c9c725f7aa06b34d6f0579886a9f19ca0d4eec005cd09c2a256e554c8b; verification/result.json SHA256 2a2bf86bfe9a2b5589c9ba808c9dfca0c04b1577021767ed94f324f1072ccf0b; verification/strict_last_term_check.json confirms the strict comparisons.

## T4-277: Localizing only the low-energy row retains the graded ceiling

Date: 2026-10-29T05:48:21.161405+00:00.
Claim: Replacing the low component by ||w J^s h||2 with w>=1 can allow an annular correction above0.002 while retaining the original graded high-row margin.
Method: Use Plancherel with the exact ordered-Hessian identity, then maximize the unchanged scalar high-row margin in sqrt(s). No computation is needed.
Result and verdict: REFUTED under the exact retained-margin hypotheses; the conditional bound is CONFIRMED. Every such box has ||h||2<=||h||H^(2+s)<25/54684<0.0005. Hence it cannot contain corrections required for007 or013, or a correction whose annular L2 norm is at least0.002. This does not exclude a new high-row estimate, a decaying low weight, or another norm that no longer satisfies the stated comparison. The complete proof was sent for Opus follow-up.
Evidence: audit record localized_high_margin, proof SHA256 f9528c66fdf94468c76340b53e009fc6438fd743d08989a3fce454d4dbb55524; frozen graded proof and T2 proposal under source/.

## T4-278: Annular lemma confirmed; family-radius conversion repaired

Date: 2026-10-29T05:48:21.161405+00:00.
Claim: T1 theory_v04 draft R2 item6 gives a justified annular lemma and a sharpw parameter-family ceiling2.834998772e-6.
Method: Prove angular Parseval and the H2 integration-by-parts estimate for globally H2 corrections supported in20<=r<=32 with frequencies>=19. Audit the scalar optimization and norm-equivalence parameter. Enclose the exact expressions with512-bit Arb.
Result and verdict: CONFIRMED the supported-correction lemma and fixed-ball upper1.312585971071236e-6. REFUTED the displayed parameter-family deduction: it divides the optimized X radius by the equivalence factor at a different fixed s. A conservative uniform repair is2.839272408273125e-6, or strictly2.84e-6. These changes do not affect the stated candidate exclusions. The annular lemma requires properties of h, which do not follow from localization of the reference residual. Changed-weight extrapolations remain HEURISTIC; the conclusion that every weaker geometry fails is unsupported.
Evidence: audit record annulus_radius_audit, proof SHA256 27d6f7e3dd8b6ee12bf21e09c590c40ca463d4354ef1317402b8a5eb833ee57d; code/check.py SHA256 4f80dec9ffc6c58c382867edae68dff82c0a2a37f00dd55c9d1aa4463bf24cb9; verification/result.json SHA256 4268394edb55a0870beba861843820f8eff587ea105c6bc39aae21e984a4dd07. Frozen source draft SHA256 2c4cb05fb8a3e3d0de419dfa404e4d6c60a06a078ed55b940cb3ef64046787e5.

## T4-279: Candidate014 point obstructions independently confirmed

Date: 2026-10-29T05:48:21.161405+00:00.
Claim: N4-213's014point values, uniform original graded gap and seven fixed-ball point exclusions hold.
Method: Independently convert all raw generators to an exact1922coordinate canonical map and compare it with N4's map. At(1/10,73/100), reconstruct fourth-order radial Taylor coefficients, then polar density, velocity and gradient. Recompute all fixed and uniform point inequalities, including the exact square-root graded radius and independent rational endpoint records.
Result and verdict: CONFIRMED. F=0.09077331018636077963794026869588, uniform graded gap0.07036934977759504275936806542774, sharp gap0.07794694687386802856168926460814 and sharpw gap0.07077725247628580378671436198833. All eight fields and all seven ball comparisons agree. Point computation1.687084768seconds; canonical conversion5.524160345seconds. The signed-principal test is inconclusive at this point. The all-c interpretation retains the separate common-tail pinning hypothesis.
Evidence: audit record candidate014_point, proof SHA256 f45a1ef3f42f58b0456f2f55d5de1c50895bccc1a358832c43db9edb035e6f2b; code/check.py SHA256 e66955d9a0b19df83229693c5b4f6a4996ee17683f17f4af14c1100a7c6325cd; verification/results.json SHA256 bd20846f250edad0400e47ad4e570fe3e689b089e34c5ec8f6616dff682d8345; preparation.json binds all raw/canonical inputs. A pre-evaluation schema mismatch and the fixed integer-string limit are documented and yielded no numerical result.

## T4-280: Candidate014 whole-plane weak distance independently confirmed

Date: 2026-10-29T05:50:52.676966+00:00.
Claim: N4-214 gives every canonical fixed-c S1 L2 correction of014 a necessary norm strictly above0.00198301351067.
Method: Read the entire frozen standalone proof and candidate checker. Independently assemble complete polar fields from the raw-to-canonical map, retain every angular cross term, and integrate with positive t-endpoint Beta recurrences. Check the pairing directly and by parts, M2,C2,M,C,D,radius, the exact gradient cap and both raw/canonical source maps.
Result and verdict: CONFIRMED. All eight scalar comparisons agree. I=-1.82802370577619844923467327711e-5, M=0.005195197731800707923446065979, C=0.004023132615791693817618327622, root=0.001983013510671948149422954371. The peer's strict floor198301351067/10^14 is independently verified. Runtime32.454022567seconds. The probe was in014's objective; this does not affect its necessary inequality. It excludes all registered balls with smaller L2 ceilings, including the original graded family. All-c use requires the separately audited common-leading-tail chart. No uniform generator-family floor is inferred.
Evidence: audit record candidate014_weak, proof SHA256 c98f70e493c0c401536e52ea88c0ff8dade69945e6c58e33307cac8130ce330f; verification/014_n21_k522.json SHA256 45131bd715ce89ddeb13302f635183aec226dd866f38a247c1f651a37af13f3e; verification/ACCEPTANCE.json SHA256 df67fb0a18acce97a756bd067715e53f98c4e31a4dc566d4163540dcf227a1cd.

## T4-281: Exact compact corrections are obstructed by the first surviving descendant

Date: 2026-10-29T05:54:51.042505+00:00.
Claim: In the canonical fixed-c S1 chart, candidates007,013and014 admit no compactly supported L2 correction to an exact stationary solution.
Method: Prove an exterior kernel estimate using the zero mass of an S1 compact correction. Its velocity is bounded by(8/pi)r^-3 times its first absolute moment. Hence a correction of support radius A requires |F|<=4sqrt(2/pi)GA^2||h||2 r^(gamma-4). Independently extract the exact first radial descendant of each canonical density and stream polynomial; verify lower-branch cancellations and exponent nonresonance.
Result: Exact arithmetic CONFIRMS that all three candidates have a nonzero branch4,q1 residual coefficient at e=-11375183046454913/4076476460239181, exceeding gamma-4 by2678922980816563/4076476460239181. Forty sine coefficients are nonzero for each candidate. Runtime8.495449714seconds, completed2026-10-29T05:52:17.974567+00:00.
Verdict: OPEN for the new general theorem and resulting candidate exclusion pending independent Opus review. The proof retains the global velocity contact term; it vanishes only in the exterior where h=0. This does not exclude predominantly annular corrections with nonzero tails and gives no outside-mass fraction.
Evidence: audit record compact_correction_tail, proof SHA256 0f256ccdfaf919efb7f9a2665818c612baf2f6cc392072d31b349be9adc89f8c; code/check.py SHA256 d471ddf1cb1dc0f667c4b65c226c238df29428606c130530fe9e009dc06cb444; verification/result.json SHA256 e77b13367f9e10cd0e1040205e7ec0eeabba7176e9dffc1fa23a18d773fb223c.

## T4-282: Six complete large-index weak records and matched envelopes confirmed

Date: 2026-10-29T05:58:51.330157+00:00.
Claim: N4-216's full007 weak-distance and matched-envelope records hold for K=1024,10^5,10^6,3*10^6,10^7,10^10.
Method: Read the entire peer proof and checker. Reconstruct exact polar fields independently, assemble all angular cross terms, and integrate finite polynomial products against positive Beta recurrences with scalar K. Compute the velocity and gradient envelopes directly from polar components, independently of the peer's Cartesian conversion. Recompute I by parts and compare with this lane's already independently confirmed full-residual pairing. Verify complete gradient maxima and strict rational floors.
Result and verdict: CONFIRMED. All17scalar comparisons and both own pairing checks agree at every K. Minimum positive-energy accuracy 1810bits. All six gradient caps2/K^2 and peer strict floors pass. At all four matching model indices10^5,10^6,10^7,10^10, the stored Cenv estimate is strictly below the complete norm and the Benv estimate strictly above it, with all eight ratios independently reproduced. The largest distance in this finite list is about0.000209622651609 at K10^5, below the already stronger007mode7 certificate. Runtime19.942436347seconds, completed2026-10-29T05:57:53.339146+00:00. These are finite-list identities and comparisons, not a uniform remainder, a maximum over K, an inverse or existence proof.
Evidence: audit record large_index_weak_audit, proof SHA256 5dd3a2e98542d68a73c7d976c0ea08ff215014e0e611291dd8d6a8cb54276200; code/check.py SHA256 303dd98a1e061a70b5d90160e49eead87279d6a99b84685d9b51bdc21538b4f0; verification/result.json SHA256 e23fa3d8cd4926bb9ef6f5cc3ca142211da8676a10071748ba2d3878dbe43984; frozen source SHA256 list in source/SHA256.json.

## T4-283: Opus confirms forcing-space incomparability and report-scope repairs

Date: 2026-10-29T05:58:51.330157+00:00.
Claim: T2's completed the review of T4-259 independently confirms T4-259 and the accompanying258,260,261,262repairs.
Method: Read the complete review and recheck its Fourier support, S1 reality/parity, weighted-Hessian estimates, completion arguments and low-frequency divergence against the frozen standalone proof. Check its finite-rank and norm-comparison reasoning. Freeze the review, arithmetic and run evidence.
Result and verdict: CONFIRMED. T4-259 is AUDITED: the selected A2 and sharpw forcing spaces are incomparable, while at equal fractional exponent X_u<=2N_u and inclusion is strict. The zero-resolvent, localization, compression and fixed-ball repairs258,260,261,262are also independently confirmed. T2's new R2 quantitative E3 comparison and R3/R4 extensions are not automatically accepted by this entry; they receive separate scope and arithmetic checks. Existing Opus5.5 lane collaboration is used; actual API model identity is not observable from this lane.
Evidence: audit record theory_final_draft_audit, proof SHA256 0378fab17bbaff0fbb07ed2ba2e50a8f56731815dc0ae5ca84e23082b7cbaf54; reviews/T2_259/the review of T4-259 SHA256 b355bcaf243df0cdf726928893ba8a7f63b7c3511f4302fe94061e86ea93cd20; reviews/T2_259/MANIFEST.json binds all frozen evidence.

## T4-284: Quantitative forcing comparison under an E3 derivative-ratio bound

Date: 2026-10-29T06:01:31.890273+00:00.
Claim: T2 the review of T4-259 R2 repairs the threshold comparison by assuming E3 membership and a bound Q3<=K E2.
Method: Check both imported A2 theorems and their parameter ranges in the frozen source; combine the common-exponent X_u<=2N_u inequality with residual conversion and reverse comparison. Independently enclose kappa(K) at six exact K values. Prove the failure of a reverse norm bound using a single shrinking band-limited S1 Fourier packet, which remains in E3 and satisfies Q3/E2->0.
Result and verdict: CONFIRMED as a conditional forcing-test comparison. At K=10^6, kappa=2.01885036527399881954 and eta_w/(kappa eta_A)=163.881359456324392305. Hence N_s(F)<=163.88 eta_A implies X_t(F)<eta_w on the stated derivative-ratio class. At K=10^11500 the enlargement remains>1.0003152804. Runtime0.002899121seconds. These do not compare all background hypotheses or prove existence, and the unrestricted selected forcing spaces remain incomparable.
Evidence: audit record forcing_conversion, proof SHA256 38738decb5a56f1030b36bd5476808c3cb63ac48d9af3c4e6d2cd2b878209438; code/check.py SHA256 5c0d0a83349d20a0d791138df085540aad9bc52a920c8a7b4432ece6293fe2db; verification/result.json SHA256 b303b3caaf62ade1e8d63e26997335aa61945de6f02c1d01a1c7ea5e89c6510b; source/A2_S1_CLOSURE.md and frozen T2review bind the imported statements.

## T4-285: Uniform full-velocity weak-test ceiling confirmed

Date: 2026-10-29T06:08:28.235566+00:00.
Claim: N4-222 and N4-225 give a uniform large-index upper bound for the complete first-sine weak-test values of007.
Method: Prove the full-velocity energy identity <phi,M>=(c+1)||phi||2^2 using the canonical divergence-free velocity and vanishing boundary flux. Independently reconstruct the complete16-branch first-sine projection from4044polar interaction pairs, compare every rational polynomial coefficient with N4's independent Cartesian projection, and check all nonzero endpoint exponents exceed4/3. Prove exact monotonicity of the positive Beta envelope. Evaluate with Arb and compare both peer formulas and the previous full signed pairings.
Result and verdict: CONFIRMED. The minimum beta is7725829753347047/4076476460239181. All six peer envelope values and all three strict rational upper bounds agree. In addition U(3000000)=0.0036327175496113885645...<0.004769166867. Thus for every integer K>=3000000, this first-mode test cannot improve the already certified007mode7 distance lower bound. Runtime70.47972021112218seconds; completed2026-10-29T06:06:29.816972+00:00. This is an upper bound on test values, not on solution distances; it neither maximizes smaller K nor covers other angular modes.
Evidence: audit record uniform_weak_tail_audit, proof SHA256 132f795c0777be5a5953fdf92e2e0ae2c0accdcf651b0fd7de9f5f6754ed6d7d; code/check.py SHA256 c5a467e5978ce0a7403837186a7c4fcd62e40d7bcea844eeba90f3aea6be6af0; verification/result.json SHA256 b7b9f5c4fba7ee41cb58d983daec50e7febe71437f39d7e548651a2b120343e7; exact coefficient JSON SHA256 017b962640aace07eae81d8aaad95842090266567a5ffbaefd33b955fa929e1f. An initial input-schema failure yielded no numerical result and is retained separately.

## T4-286: Downward decimal substitutions in theory_v04

Date: 2026-10-29T06:12:17.747866+00:00.
Claim: The annular bounds and forcing conversion retain their proved constants after decimal substitution.
Method: Compare the exact formulas with512-bit Arb; check both directions of every proposed rounding and the163.88threshold using exact rational arithmetic.
Result and verdict: The printed annular endpoints are below the right sides of their cited estimates, and2.01885 is below the proved kappa. CONFIRMED the rounding defects; REFUTED the displayed equalities/inferences, without claiming the smaller inequalities cannot be proved by stronger arguments. Safe upper values are1.312585972e-6,2.839272409e-6 and2.018851. The163.88forcing comparison still passes. No exclusion changes.
Evidence: audit record theory_v04_audit, proof SHA256 045d627f4cab0610691f591aa2461cec9a4dc2f4c23d91364160b64c5d429597; frozen source/theory_v04.md SHA2567638b0dae2e1cd03bd307fec28143ce84ae37b5a42a0d882d64e879094fcca93; verification/result.json SHA256 5fc62c64c4040902cb45f18871c2c3d7914a9d6f697fdc29a0b774b94c817681.

## T4-287: Positive leading-amplitude ray is the dilation orbit

Date: 2026-10-29T06:12:17.747866+00:00.
Claim: theory_v04 section5.2 identifies positive multiples of the leading profile with dilation.
Method: Induct in the exact triangular recurrence to obtain degree j+1. Compare dilated cutoffs modulo compact support, use canonical velocity covariance, and change variables in the L2 norm.
Result and verdict: CONFIRMED: muTheta0 gives forced profiles mu^(j+1)Thetaj and the affine class of D_lambda R, lambda=mu^(1/delta). The solution sets are in bijection and distance from the specifically dilated reference scales by lambda^2. This makes the T1 claim AUDITED with the stated scope. An arbitrary refit within the class does not inherit that distance identity.
Evidence: audit record theory_v04_audit, proof SHA256 045d627f4cab0610691f591aa2461cec9a4dc2f4c23d91364160b64c5d429597; frozen source/theory_v04.md SHA2567638b0dae2e1cd03bd307fec28143ce84ae37b5a42a0d882d64e879094fcca93; verification/result.json SHA256 5fc62c64c4040902cb45f18871c2c3d7914a9d6f697fdc29a0b774b94c817681.

## T4-288: Homogeneous norm does not alone imply invariant budget ratio

Date: 2026-10-29T06:12:17.747866+00:00.
Claim: theory_v04 section5.2 infers an invariant distance-to-budget ratio from a homogeneous framework norm.
Method: Separate the homogeneity of the distance from covariance of the admissible radius. Use L2, solution set{0}, nonzero S1 reference R and fixed radius1 as a counterexample to the general implication.
Result and verdict: REFUTED as an implication from norm homogeneity alone. The ratio is invariant if the radius and all hypotheses transform covariantly with the same homogeneity. Those properties have not been verified for the registered frameworks. The positive-ray solution-class result T4-287 is unaffected.
Evidence: audit record theory_v04_audit, proof SHA256 045d627f4cab0610691f591aa2461cec9a4dc2f4c23d91364160b64c5d429597; frozen source/theory_v04.md SHA2567638b0dae2e1cd03bd307fec28143ce84ae37b5a42a0d882d64e879094fcca93; verification/result.json SHA256 5fc62c64c4040902cb45f18871c2c3d7914a9d6f697fdc29a0b774b94c817681.

## T4-289: Complete theory_v04 text and distance-table audit

Date: 2026-10-29T06:12:17.747866+00:00.
Claim: The published summary and design recommendations preserve the logical scope of their supporting results.
Method: Read all852lines. Check the33printed candidate ratios by exact fractions against the larger true graded ceiling25/54684. Compare design-row and route statements with the audited weak inequality and damped least-squares counterexample.
Result and verdict: CONFIRMED all33table ratios and the previously corrected weak, domain, normalization, tail and ball statements within their cited hypotheses. REFUTED as unsupported deductions the statements that optimized probes no longer measure distance, that stalled optimization proves no basis leverage, and that no R-TE chart exists. Any certified probe remains a necessary distance bound; neither type measures the actual distance. No such chart or new high-row estimate has been constructed in this program. No existence closure or unrestricted nonexistence result follows.
Evidence: audit record theory_v04_audit, proof SHA256 045d627f4cab0610691f591aa2461cec9a4dc2f4c23d91364160b64c5d429597; frozen source/theory_v04.md SHA2567638b0dae2e1cd03bd307fec28143ce84ae37b5a42a0d882d64e879094fcca93; verification/result.json SHA256 5fc62c64c4040902cb45f18871c2c3d7914a9d6f697fdc29a0b774b94c817681.

## T4-290: Both Opus reviews of the localized high-row ceiling accepted

Date: 2026-10-29T06:12:17.747866+00:00.
Claim: T1 R1-032 and T2 the review of T4-277 confirm T4-277 and its scope.
Method: Read both complete reviews and compare their Plancherel identity, cubic maximum and integer bounds with the frozen proof. Check T2's additional T4L2 remark by maximizing the conditional scalar high-row cap.
Result and verdict: CONFIRMED; T4-277 is AUDITED. T2's extension is also CONFIRMED under the explicitly unchanged high-row margin and norm-domination hypotheses. It does not establish those hypotheses for a new localized PDE framework. T1's annular decimal truncations are handled in T4-286; the underlying formulas are accepted.
Evidence: audit/theory_audit/research_code/localized_high_margin/reviews/ACCEPTANCE.md and MANIFEST.json; T1 review SHA256 423d9f062f9fcfb1b802088a552b4b376d53df3a43a17d0cb7d1c3d01e858055; T2 review SHA256 b0b915ab06b17e558ef0ba0d6b2095b9202a5dc7ba452a17300bfa8b28d278b8. Existing Opus5.5 file collaboration; actual API model identity is unobservable.

## T4-291: Independent exact weighted-tail audit of the five Opus candidates

Date: 2026-10-29T06:20:18.926708+00:00.
Claim: T2 the review of T4-249 R3 identifies the first nonzero residual sector and the sharp range excluded by T4-249 for state131, d2, Mpen2,005 and007; the review of T4-234 R3 identifies their affine L2 classes.
Method: Expand the potential directly at infinity, using P(1) and pP(1)-P'(1), then differentiate each homogeneous term. This bypasses the peer's full density-polynomial endpoint construction. Check all18 angular Poisson identities, all exact residual coefficients, the complete nonzero-sector set above every admissible threshold, all printed norms, and the first four density profiles.
Result and verdict: CONFIRMED. The first sectors are(2,0) for state131,(7,0) for d2/Mpen2 and(4,1) for005/007. For -2<a<=1+gamma the necessary weighted-tail condition excludes a<=4503599627370496/4076476460239181 for state131, a<=-4619783605399169/4076476460239181 for d2/Mpen2, and a<=-7298706586215732/4076476460239181 for005/007. Equality is included. The latter obstruction is a radial-regularization descendant, not a failed leading ladder relation. The four nonbaseline candidates have identical first four profiles and hence the same affine L2 class, though their distances to a solution set need not agree. No obstruction from this particular test above those thresholds means no existence conclusion. The11-candidate computation ran277.2765652718954seconds and completed2026-10-29T06:19:25.178349+00:00.
Evidence: audit record weighted_tail_candidate_audit, proof SHA256 bf5cf9d5af30a0c8df947c09cf5ee4423850e618baeb6abc45662f8713ab2aa1; code/check.py SHA256 3da782aec224eb1b86bd54ac1e64730e14166a2d7e35a967474cc6ab34a0390f; verification/result.json SHA256 5d31a674da22c80b87735ebbd5a055e937b872623412bf54e0decf397752599d; frozen peer sources and all exact sector tables are beside the proof.

## T4-292: Weighted-tail extension to six further exact canonical candidates

Date: 2026-10-29T06:20:18.926708+00:00.
Claim:006,008,009,012,013 and014 have the same first nonzero sector(4,1), and first four density profiles, as007.
Method: Use the independent exact potential expansion of T4-291 on the six hashed canonical inputs; check all angular Poisson equations and retain every residual sector relevant to -2<a<=1+gamma.
Result: All six exact computations give q_*=-11375183046454913/4076476460239181, hence threshold a_*=-7298706586215732/4076476460239181. Their first four profiles agree exactly with007. The residual angular norms differ and are retained in result.json.
Verdict: OPEN pending an independent numerical peer check of these extensions. The underlying weighted-tail theorem is already AUDITED. This entry does not cover010,011 or a scaled rational-pole candidate.
Evidence: audit record weighted_tail_candidate_audit, proof SHA256 bf5cf9d5af30a0c8df947c09cf5ee4423850e618baeb6abc45662f8713ab2aa1; code/check.py SHA256 3da782aec224eb1b86bd54ac1e64730e14166a2d7e35a967474cc6ab34a0390f; verification/result.json SHA256 5d31a674da22c80b87735ebbd5a055e937b872623412bf54e0decf397752599d.

## T4-293: Negative-weight endpoint rounding in published theory_v04

Date: 2026-10-29T06:20:18.926708+00:00.
Claim: The printed decimals -1.133278617 and -1.790444924 may replace the exact upper endpoints in the proved correction-space exclusions.
Method: Compare each finite decimal with the exact rational threshold from T4-291.
Result and verdict: REFUTED as a deduction from these exact tail tests. Both printed endpoints are strictly larger than their exact values, so each expands the stated exclusion interval. Use the exact expressions 7gamma-5 and4gamma-4, or the safe downward decimals -1.133278618 and -1.790444925. This does not prove the tiny extra intervals admit solutions; it shows they are not excluded by the cited calculation.
Evidence: audit/theory_audit/research_code/weighted_tail_candidate_audit/verification/rounding.json SHA256 6650ed883b79dfd2846467a9c52a68d4f919aee6cf1d356bf55cab2cd4a407b5; theory_v04 section5.1 and current THEORY_FINAL section8.1 carry the decimals.

## T4-294: A weighted C1 correction has a forced integrable tail

Date: 2026-10-29T06:26:57.527945+00:00.
Claim: For -3<q<0, a centrally odd C1 correction with H_q=max(sup(1+r)^(-q)|h|,sup(1+r)^(1-q)|grad h|)<infinity has a canonical velocity bounded by C_q H_q r^q for r>=2. If F(R)=r^q A+O(r^(q-epsilon)), the background velocity and gradient have the stated sublinear bounds, and R+h is stationary at the fixed c>1, then h=r^q A/(1-cq) with the explicit remainder in PROOF.md(5).
Method: Four-region kernel estimate retaining the -h/2 contact term, zero mass on centered balls by oddness, and integration of the radial transport equation from infinity. No derivative of U[h] is taken.
Result: Complete standalone argument and explicit constants. At the campaign q=-11375183046454913/4076476460239181, C_q is about129.002791900423387. For the first descendant of007,013,014, A=(cq-1)Theta, so the necessary correction is -r^q Theta to leading order.
Verdict: OPEN pending independent Opus review. Weighted C1 decay is an explicit hypothesis; no such pointwise asymptotic is inferred for an arbitrary L2 correction.
Evidence: audit record forced_integrable_tail, proof SHA256 1c490b83e9c3e7fa7d7a3445f9b37c0edc2ce0e184cc2e2231335ca122dc0e1a; code/check.py SHA256 da15e147157dad41a4f5968b467a7e652fdf0bcc097df6ec139846392d736067; verification/result.json SHA256 15ec5879fa3593baccd02f5d3ee99348fc64013cb6c64878ade676e9b3ef01be.

## T4-295: Exact smooth cancellation of the first integrable reference descendant

Date: 2026-10-29T06:26:57.527945+00:00.
Claim: A potential correction in branch j=3 cancels the (4,1) density and stream sectors without changing the leading ladder or origin normalizations.
Method: Put A1_m=pP_m(1)-P'_m(1), p=2gamma, and add -(1+r^2)^p sum A1_m t^(m+4)(1-t)cos(2m theta). Verify its two endpoint moments, origin order and all relevant residual coefficients in exact arithmetic for007,013,014.
Result: All three checks pass. Every residual sector of exponent>=-3 vanishes after the operation. The first remaining sector is(9,0), exponent -12345613358746216/4076476460239181, or -3-epsilon1 with epsilon1=116183978028673/4076476460239181>0. The correction has40 potential modes, vanishes to potential order8 at the origin and preserves density and velocity jets through order4. It lies in L2, preserving that affine class, but lies in E_a only for a>4gamma-4. Runtime72.74951060628518seconds, completed2026-10-29T06:24:46.728369+00:00.
Verdict: OPEN pending independent Opus review. This is an exact reference-design direction, not an accepted candidate, small-residual claim or existence proof. In the tighter weighted spaces it changes the affine class and therefore does not evade T4-291.
Evidence: audit record forced_integrable_tail, proof SHA256 1c490b83e9c3e7fa7d7a3445f9b37c0edc2ce0e184cc2e2231335ca122dc0e1a; code/check.py SHA256 da15e147157dad41a4f5968b467a7e652fdf0bcc097df6ec139846392d736067; verification/result.json SHA256 15ec5879fa3593baccd02f5d3ee99348fc64013cb6c64878ade676e9b3ef01be; exact potential directions are in data/007_tail_repair.json, data/013_tail_repair.json and data/014_tail_repair.json.

## T4-296: Compact-correction theorem independently confirmed by Opus

Date: 2026-10-29T06:26:57.527945+00:00.
Claim: T1 R1-033 confirms T4-281 analytically and independently reconstructs its three candidate applications from raw generator snapshots.
Method: Read the complete review, checker and output. Recheck the zero-mass kernel estimate and exterior distributional identity. Compare the independently obtained exponents,40 nonzero modes and first coefficients with this lane's exact tables.
Result and verdict: CONFIRMED; T4-281 is AUDITED. No S1 compactly supported L2 correction at the fixed campaign c makes007,013 or014 stationary in the canonical chart. No tail-mass fraction or exclusion of noncompact corrections follows. The endpoint exponent gamma-4 is correctly not excluded by this argument.
Evidence: audit/theory_audit/research_code/compact_correction_tail/reviews/T1_033/ACCEPTANCE.md and MANIFEST.json; review SHA256 a6856ca19d9d537d6c76f6add367b09255be73e820d11bea34f637d889bd5dc9; independent checker SHA256 c05bf08f1b78b0b5eef598577929d867ded763ead2c8fde0c2b4f16d0f8a70dc; output SHA256 c59bbff085bf75d87566e74a4b17fdd9149d6a67eed0f26e95b1d59feefccfc3.

## T4-297: Exact structure of candidate015 independently reconstructed

Date: 2026-10-29T06:26:57.527945+00:00.
Claim: C1-N1-015-pairQ-quot013 belongs to the primary fixed-c chart and has the same first four density and stream profiles as007.
Method: Freeze the snapshot manifest, checksums and raw rational generator file, expand each generator independently, combine exact monomials, and apply this lane's audited polar differentiator.
Result:1922 raw generators and1922 nonzero canonical monomials; c=4076476460239181/2251799813685248; strain=1-c exactly; a0>0; all four leading density and stream profiles agree exactly with007. Build runtime5.720880195964128seconds, completed2026-10-29T06:25:18.390986+00:00.
Verdict: OPEN pending independent numerical acceptance. This certifies neither the full residual norm nor any closure inequality.
Evidence: audit/theory_audit/research_code/new_successor_weak/verification/015_build.json; raw coefficient SHA256 d7759bbaa98fb5d686c8f88af4ec6b9ddd96e457acc2d9166924c5c729ee8eae; canonical SHA256 fe9bc91d9448c68fc7821af5ea02df5c0bdb82add39e9eab96519d6c9240e8ba.

## T4-298: Candidate015 held-out whole-plane weak distance independently confirmed

Date: 2026-10-29T06:33:07.296143+00:00.
Claim: The n=19,K=600 monomial probe gives a strict necessary L2 distance greater than351804115950603/10^18 for015 in the fixed canonical chart.
Method: Independent exact raw-to-polar fields, all360 density and360 stream components, full M and C norms, direct and integrated-by-parts pairing, and complete derivative-root classification of the Euclidean probe gradient. Compare all seven common scalars with N4's independent Cartesian rational-field path. Both rational gradient caps are valid; recomputing the root with N4's finer cap reproduces its interval.
Result and verdict: CONFIRMED. I=2.74445007804097864818e-6, M=0.00439417039528328133, C=0.00340689397340463572, distance>0.000351804115950603. The independent calculation took34.472132951021194seconds, completing2026-10-29T06:28:22.502614+00:00. This is one held-out probe relative to the documented objectives, not the maximum of the25-probe set. It lies below the universal graded ceiling, so that comparison alone does not exclude every registered framework. Every smaller named L2 ball is excluded under the weak-equation hypotheses.
Evidence: audit record candidate015_heldout, proof SHA256 60f2197202db1816f78823fe69e3b06150e25090e85b1655fc321481fba4ad9b; own result SHA256 eec613c67b4ad56f80cd52e8be679a48348b9292d9ae693f6b589704be944aec; independent N4 result SHA256 3fb7191954ff162fecb4911138d1aac37c178ee9ea94d0ff3f8c5348bd7fbf9a; acceptance SHA256 e8c728579981e4ba5dcb8c1b593f67ef7a1297f4cf73b4f4d7e676a45be54c11.

## T4-299: Candidate015 point exclusions independently reproduced

Date: 2026-10-29T06:33:07.296143+00:00.
Claim: N4-234's six scalar point exclusions and universal original-graded point exclusion hold at X=(1/10,73/100).
Method: Exact rational radial Taylor jets through fourth order, polar density/velocity differentiation and1024-bit Arb, independent of N4's Cartesian Taylor code. Compare all eight fields, every scalar bound and gap, and the universal graded bound and gap. Use exact rational radii.
Result and verdict: CONFIRMED. F(X)=0.09024908594883730806..., universal graded gap=0.06984581440341596867...; all six scalar gaps are strictly positive. Runtime1.7583893714472651seconds, completed2026-10-29T06:31:44.774638+00:00. This excludes only the stated fixed-c balls and original graded family. Together with T4-298 the necessary tests exclude015 in all currently registered scalar and graded balls, with no global nonexistence conclusion.
Evidence: audit record candidate015_point, proof SHA256 55038cef9d4efba30a00346287579480c295a14e30c3dfdc4dbdac54f39e0c39; code/check.py SHA256 f112b1966265b7a3f349e02d420e2531ccb3146d4a1504f2947d747bce7678a6; verification/results.json SHA256 673526f1631173833e732f1b43350f5cc4572d579f42d7170daa816120dc865f; raw coefficient SHA256 d7759bbaa98fb5d686c8f88af4ec6b9ddd96e457acc2d9166924c5c729ee8eae; frozen N4 direct record SHA256 3053046c231c815aee839fbf6f6f25d8ceb1eed2e7fc6e1fa5f3196073ab5763.

## T4-300: Weighted second-moment Hessian theorem independently accepted

Date: 2026-10-29T06:40:19.432859+00:00.
Claim: Opus the review of T4-242 confirms the centrally odd Hessian estimate and its derivative-tensor completion.
Method: Read the full frozen review,267-line independent checker and output; reread the original proof. Recheck the canonical multiplier, Mellin line, real-mode pairing, endpoint behavior and weighted completion. The numerical illustrations are not proof inputs.
Result and verdict: CONFIRMED; T4-242 is AUDITED. For real smooth compactly supported centrally odd h, the bound is ||(1+r^2/R^2)D2U[h]||2 <= (1+sqrt6)/2 ||(1+r^2/R^2)D2h||2 for every R>0. The Beurling squared constant6 is sharp on S1, while sharpness of the velocity constant is not asserted. The extension concerns the limiting derivative tensor, not an independently normalized scalar representative.
Evidence: original proof SHA256 82e9f46b3447202dc62f8bfcfe59d5ed13de90e4af8276bf0e82cc07dc4ade6e; frozen Opus review SHA256 4d3b3884be2b03611a20c03b291b8b43201b7121fc09310b3955a16ef4fa30b2; independent checker SHA256 48edffa20830766016d4c5fdb38043e10a329a0b071871da27fa69454c8f213c. Acceptance: audit/theory_audit/research_code/s1_hessian_refinement/ACCEPTANCE.md.

## T4-301: The Opus S1 refinement and parity counterexamples

Date: 2026-10-29T06:40:19.432859+00:00.
Claim: the review of T4-242 R2 gives squared constant63/32 on real S1 inputs; R3 shows why the parity assumptions cannot be dropped.
Method: Independently derive the positive/negative odd-mode output split, including the outgoing final mode. Check the exact Q_m polynomial comparisons and the Young parameters1 and4. Use the annular Mellin concentration families analytically, without relying on a frequency grid.
Result and verdict: CONFIRMED. The squared S1 constant63/32 follows for the homogeneous second moment and the full w2 weight. The centrally odd cosine family has velocity squared limit2; the radial family has limit33/10. The latter exceeds the centrally odd constant((1+sqrt6)/2)^2. These are counterexamples to dropping the corresponding parity restrictions, not claims that either upper constant is optimal.
Evidence: complete standalone derivation in audit record s1_hessian_refinement, proof SHA256 ce2565f331bf77187169bd83102e8f6f1f6cefbff8172b7feea56836ed26e4cf; source/FROZEN.json and ACCEPTANCE.md in that topic.

## T4-302: Balanced S1 Hessian constant

Date: 2026-10-29T06:40:19.432859+00:00.
Claim: The same real S1 Hessian estimate holds with squared constant185/96.
Method: In the independently confirmed mode split, use Young parameters lambda=2/3 and kappa=4. Both coefficients become185/12, then division by the input factor2 and velocity factor4 gives185/96. Sum the zeroth, first and second moments, using1<5/3<185/96.
Result: Complete proof, with the canonical multiplier and completion hypotheses explicit. This is a small operator-constant improvement, not a transport, inverse or nonlinear closure result. The exact symbolic checker is prepared but not yet executed because the lane's one allowed busy worker is reproducing candidate010's dyadic cells.
Verdict: OPEN pending independent Opus review. The already confirmed63/32 bound does not depend on this refinement.
Evidence: audit record s1_hessian_refinement, proof SHA256 ce2565f331bf77187169bd83102e8f6f1f6cefbff8172b7feea56836ed26e4cf; code/check.py SHA256 86b25cff240462a1ca9ee55f961b48894f0a1ef660960105d10f79921d88364e.

## T4-303: Candidate010 dyadic obstruction independently reproduced

Date: 2026-10-29T06:50:29.742896+00:00.
Claim: N4-231's two complete angular projections and seven cell exclusions are correct for the immutable candidate010.
Method: Independent exact raw-to-polar field construction, all interacting angular pairs, exact radial Laplacians, endpoint orders, polynomial CRT identities and direct Arb hypergeometric moments at2048 bits. Verify the exact origin identities and six accepted physical point values. Compare all32 energy/norm scalars and35 cell quantities with the frozen N4 result.
Result and verdict: CONFIRMED. J1(0)=92.689749884415749712..., J3(0)=59.818918678553417238.... Every cell gap is strictly positive; the smallest ratio exceeds5.78998557. The computation took851.1710245758295seconds, completing2026-10-29T06:49:37.753360+00:00. The seven cells cover0<a<1+1/c. Only after invoking the audited nonpositive far-field rate for1+1/c<=a<2, together with the origin inverse, canonical velocity, forcing hyperplane, domain and absorption hypotheses, does this exclude the registered dyadic sufficient scheme for0<a<2,0<s<1 and each fixed finite weight radius. It is not a nonexistence result for stationary profiles.
Evidence: audit record scaled_dyadic_reproduction, proof SHA256 d9d4733d2c2d7bf8d6c84eab6d18e98f9378a215b3e7be7851071ed2e0b6c684; code/check.py SHA256 45d63f213c2f8f1dfb0d4d7afc9ab0ee027708a5b3e16e9dab3287cfc6031ebc; verification/result.json SHA256 83fa422d51358207a7a027befd9ac0e23e3c3e728b7e0996fc10d1df41e20c58; mode001 SHA256 8348ae8c9357f9f8d3ad792fee1ad50417558a98a0018387ae13a9c6a1931064; mode003 SHA256 238bfde717a399bd433e0179813bf82b42a329c7aa82c2a212072adf015d0661.

### T4-302 computational supplement

Date: 2026-10-29T06:50:29.742896+00:00. The exact symbolic checker completed2026-10-29T06:49:44.970604+00:00 in0.048097935039550066seconds. All three polynomial identities, both Young coefficient choices and the two parity limits pass. Its result SHA256 is 01f6e8399a533f11a3dbe9834ecc21ae209fbc293340309f9aaa394bad909268. The185/96 theorem remains OPEN independent Opus review; executing its own algebra checker does not replace that review.

## T4-304: Stronger held-out candidate015 distance independently confirmed

Date: 2026-10-29T06:52:52.060232+00:00.
Claim: N4-237's n=23,K=600 probe gives a strict necessary L2 correction radius greater than1232449584356253/10^18.
Method: Reconstruct all360 density and360 stream components through the independent polar path; integrate every angular interaction by exact polynomial beta moments with2048-bit Arb. Compare direct and integration-by-parts pairings, M,C,D and their squared norms with N4. Independently certify its finer rational Euclidean-gradient cap by the complete critical-point classification, then recompute its quadratic root. The probe is outside the documented013 and015 objective lists and spans.
Result and verdict: CONFIRMED. I=9.84284617558176635657e-6, D=0.00798636629184973136, and radius>0.001232449584356253. This alone exceeds the universal original-graded ceiling25/54684 and all smaller registered scalar budgets. The calculation completed2026-10-29T06:50:24.683602+00:00 in33.54576864792034seconds. This is one certified held-out witness, not a maximum over the registered set or an estimate of the actual distance.
Evidence: audit record candidate015_heldout23, proof SHA256 9a69554cfc5a7ebfbb6ebc6d869abd99c36b8ea990430ba3b03a78d6b2deb85e; own result SHA256 3db6a95cbab95a5b8392376c17d28e2d1786a14419d4c5afe82170fe92dbd023; acceptance SHA256 9ffa6db44f6c80570fb72cf921945d322a88d0dda8d74b1eece17ff880b8c5db; frozen independent N4 result SHA256 fdbab56c46b48091df7f34cd9c76220f4ef58d0ce0c87c814d9b20c019d959de.

## T4-305: The Opus compact-support endpoint constraint independently confirmed

Date: 2026-10-29T06:52:52.060232+00:00.
Claim: T2 the review of T4-281 R2 forces the residual coefficient at gamma-4 into the single dipole profile -(My/pi)[gamma cos(2theta)Theta0+sin(2theta)Theta0'];007,013,014 fail this proportionality exactly.
Method: Recheck the exterior canonical kernel, mass and x-moment cancellation from S1 parity, first-moment Taylor expansion and its sign. Derive the endpoint from exterior stationarity. Independently extract the branch0 potential coefficients at q=0,2 by rational binomial coefficients, apply homogeneous density differentiation, and exhibit a nonzero rational determinant in sine modes1 and3 for all three candidates. Compare all four numerical summaries with T2's output.
Result and verdict: CONFIRMED. The three relative projection residuals are0.6293860220545,0.6293963295090,0.6293853189807, with the exact determinant supplying the proof. Runtime0.07388961501419544seconds, completed2026-10-29T06:50:40.512194+00:00. If proportionality held with Fstar=lambda P, Cauchy-Schwarz would also force||h||2>=2sqrt(pi)|lambda|/A^2 for support radiusA. Altering branch3 alone leaves this endpoint unchanged. This is a necessary condition for exactly compact S1 L2 corrections at fixed c; it does not exclude the noncompact integrable-tail direction of295.
Evidence: audit record compact_endpoint_audit, proof SHA256 bae67380f5e529973a9e65bc31ededa044cd48bd82016de0878f655d678aa86f; code/check.py SHA256 26bd49f4fd290771d2e0c6996c51ed642051837c460897c495f8d5e1a82bb85b; verification/result.json SHA256 07e941a3b7a713a17b6e9b8b29bd6cfd232a1cf3c26e62317c423e3d23d318f7; exact coefficient and determinant JSON files are in data; frozen T2 review and output hashes are in source/FROZEN.json.

## T4-306: Independent exact canonical and origin acceptance for015

Date: 2026-10-29T06:52:52.060232+00:00.
Claim: The numerical structure claims in T4-297 agree with the independent N4-233 computation.
Method: Compare all1922 rational canonical coefficients by index, despite differing JSON metadata and hashes. Verify common raw hash,c,exact strain and positive slope. N4's independent zero sectorsE1,E2,E3 and common leading density imply the remaining three profiles by the already audited unique triangular recurrence, independently of the own direct four-profile comparison.
Result and verdict: CONFIRMED; T4-297 is numerically accepted in full. This confirms the fixed-c affine chart, all four density/stream profiles and origin normalizations only. It does not confirm untested global background inequalities or closure. Canonical comparison took0.6670413538813591seconds, completed2026-10-29T06:51:18.128934+00:00.
Evidence: audit/theory_audit/research_code/new_successor_weak/reviews/015/PROOF.md SHA256 00c99d4e44d485721b16e68a4158853cb963c9da1419359bce7a29589ae12b01; verification/result.json SHA256 e9917c0e8d56e5802eb2e6166aeb0b17f98b7f9d60c4308da8254bcfb8ce8ab1; verification/deduction.json SHA256 6356d6c996fcb7f93163980013ee99679c58bd4387a54a6cadad04010968d214; N4 canonical SHA256 2ab9b2e877caf825d148131ae9b22568f3ab735e61a3570aaa28d86ee42127c1; N4 result SHA256 18bb2e6abe3d79b970eb09dc26fab12f46e928cca088b433feca24018a107b61.

## T4-307: Candidate016 point exclusions independently confirmed

Date: 2026-10-29T06:58:51.616082+00:00.
Claim: N4-242's eight local fields, six scalar necessary inequalities and universal original-graded inequality are correct for immutable C1-N1-016-legqs25-quot013.
Method: Exact raw-generator radial Taylor jets through fourth order, polar density and velocity differentiation, and1024-bit Arb. The radius25 factors use the exact positive denominator625(1-t)+t. Compare all eight fields and every exact-radius bound, root and gap with the independent Cartesian result.
Result and verdict: CONFIRMED. F(1/10,73/100)=0.09021756899686665397..., uniform graded gap=0.06982061854573119564..., and all six scalar gaps are strictly positive. Runtime1.6972422245889902seconds, completed2026-10-29T06:57:06.296880+00:00. This independently excludes016 from the named fixed-c balls and original graded family. It does not validate the new global R25 moment backend or establish global profile nonexistence.
Evidence: audit record candidate016_point, proof SHA256 e71794a44df1aad9d73571a1f9915451e9e319e5a6a54f3966c75638f491988c; code SHA256 34de654349d36f1f9f1c52a90e20a0d44178cefa27560b1fffa9130e2194a04d; result SHA256 44058daf8ae54a8c3e3d90e96e8bbab117fcde65ccdde84654a619ecb6ae8153; raw SHA256 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42; frozen N4 result SHA256502ed0004bdf6d35a4e42ec16ea21daf8efc3fe7adcbe52695a70093acfb60f3.

## T4-308: Six weighted-tail extensions independently accepted

Date: 2026-10-29T06:58:51.616082+00:00.
Claim: N4-240 independently reproduces all numerical and exact candidate claims of T4-292.
Method: Read the complete frozen proof, checker and source-binding procedures. Verify all six own exact-data hashes against the peer manifest, all108 sector-map and Poisson flags, exact first sectors and weighted endpoints, and all six angular-norm overlaps. The peer computed10800 coefficients directly from raw generators in Cartesian angular frequencies, independently of the own polar path.
Result and verdict: CONFIRMED; T4-292 is numerically accepted. Candidates006,008,009,012,013,014 have first sector(4,1), exponent4gamma-5, and no exact S1 correction in E_a for-2<a<=4gamma-4 under the audited canonical weighted-velocity and weak-equation hypotheses. The first four density and stream profiles equal007. The peer runtime was72.8134695426561seconds. No claim of existence or of equality of actual distances follows.
Evidence: audit/theory_audit/research_code/weighted_tail_candidate_audit/reviews/N4_240/ACCEPTANCE.md SHA256 7b42c61c04719c4a013cac0808e2d217e16f97509fe533569f216baf89b0737e; acceptance result SHA256 a23dc090cd2b2b1b8209e174054ff612ef44062b1051440d658f114d8fb273d7; peer result SHA2567990493835e7dddb3ae04e9cd228969e26220736b74fc8cc045a7bc8a323d47b.

## T4-309: Balanced S1 Hessian bound accepted after Opus review

Date: 2026-10-29T06:58:51.616082+00:00.
Claim: Opus the review of T4-302 independently confirms squared constant185/96.
Method: Read the full review, independent exact checker and log; reread the complete standalone proof. Recheck the angular grouping, polynomial inequalities, Young coefficients, normalization factors and completion. Independently square the directed decimal1.388195.
Result and verdict: CONFIRMED; T4-302 is AUDITED. The estimate holds for real S1 inputs and the stated weighted Hessian completion, for everyR>0; sqrt(185/96)<1.388195. Optional optimized constants in the peer remark remain FLOAT and are not proof inputs. This improves an operator constant only.
Evidence: audit record s1_hessian_refinement, proof SHA256ce2565f331bf77187169bd83102e8f6f1f6cefbff8172b7feea56836ed26e4cf; frozen Opus review SHA256 a37af42f97266235e3077636a2913c063386418807c1ca437efea18ab42005ce; independent checker SHA256 2d9370cca7a976e418c4ca6d06898d16848f76a614fdbcf6d1ddcfa731756b5d; acceptance SHA256 1352eca00f9ffc7b729ec9fc169e738acaadae64815e61bc759bda3e9381c8fd.

## T4-310: Candidate016 whole-plane registered weak witness independently confirmed

Date: 2026-10-29T07:09:03.717557+00:00.
Claim: N4-246's n=23,K=2400 probe gives a necessary L2 correction radius greater than273158289826571/250000000000000000 for C1-N1-016-legqs25-quot013.
Method: Reconstruct all360 density and360 stream components by the independent polar path. Keep the localization t^K factored and integrate all1616 M pairs and5672 ordered C pairs by exact rational CRT and direct Arb hypergeometric moments at2048 bits. Four scalar fixtures agree with the earlier expanded-localization path; all007 calibration fields agree exactly and all six016 point fields agree with T4-307. Independently certify the complete gradient critical-point bound. Compare all eight scalar values with N4, including direct and integration-by-parts residual pairings.
Result and verdict: CONFIRMED. Radius>0.001092633159306284, hence larger than25/54684 and all registered smaller scalar budgets. The calculation completed2026-10-29T07:06:01.124424+00:00 in125.26011940930039seconds. This is one registered held-out necessary witness, not an estimate of the actual correction distance or a maximum over the probe register. It excludes the remaining statL and bL balls in coordinator row80. It does not supply the separately requested full016 sector audit.
Evidence: audit record candidate016_weak, proof SHA256 4fbabec09346c990f7fe6e6cea0e707e39d57c797d34381d086742521a05688f; code/check.py SHA256 cdf794d7ad86339fb7296a9f25cf4c1d2ab34edcaf6b0d79f4b39f27d78208a9; verification/n23_K2400.json SHA256 2c3cd616e372ecbe0497eb66b43f9a47c7ba2d70e76a0baf79e38caba0d5dac5; raw SHA256 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42; frozen N4 result SHA256 4e9fd6e4ea778c0726d1dfe235ca59aa0598c0097d576bdc0d74cc17b2b51bfe.

## T4-311: Stronger registered016 weak witness independently confirmed

Date: 2026-10-29T07:12:11.241503+00:00.
Claim: N4-246's second registered probe, n=19,K=1800, gives radius>367590231030927/250000000000000000.
Method: The independent exact polar and direct factored-hypergeometric path of T4-310, with fresh complete angular products and independent gradient critical-point certification. All eight scalar values agree with N4 and the direct/parts pairings overlap.
Result and verdict: CONFIRMED. Radius>0.001470360924123708. Completed2026-10-29T07:11:09.629695+00:00 in125.82851266488433seconds. This stronger necessary witness exceeds25/54684 by a factor above3.21. Both this and the n23,K2400 probe are in the25-probe register; no maximum over that register is claimed.
Evidence: audit/theory_audit/research_code/candidate016_weak/verification/n19_K1800.json SHA256 788f1b6086db74da012cf984cd5b0691bf27367da00056b9516a5dba8e95dc0e; same proof/code hashes as T4-310; frozen N4 result SHA256 8f650bf10daac0c90d3da6cf32d137e0522a8ea298b259017f51f57cdf2bbc28.

## T4-312: Theory v05 arithmetic and publication-scope audit, with own-summary erratum

Date: 2026-10-29T07:12:11.241503+00:00.
Claim: The new candidate table is conservative; held-out improvements establish an actual-distance improvement; expanded-basis trials establish a span floor; finite Beta sums are only FLOAT; no alternative decaying-weight framework exists. Also audit the T4 working-summary inequality25/54684<0.00045717.
Method: Read the full v04-to-v05 diff and new text against previously audited unchanged statements. Check all36 ratios by exact rational arithmetic. Supply exact Hilbert-space and damped-step counterexamples, an exact complete Beta-sum example64/315, and cross-multiply the displayed decimal.
Result and verdict: CONFIRMED all36 conservative table ratios. REFUTED the unsupported general deductions and the own-summary decimal inequality. Neither held-out nor design-probe reductions alone prove a reduction of actual distance; finite trials do not certify a span floor; complete finite Beta formulas can be certified, whereas truncated asymptotic models need remainder bounds; status should say no such framework has been verified in this program. The corrected own-summary bound is25/54684<0.000457173. The sharper separate expression50/(651 sqrt28248)<0.00045717 is true, but does not justify the larger rational comparison. These are wording/arithmetic repairs, not changes to any candidate exclusion. Arithmetic completed2026-10-29T07:11:37.185667+00:00 in0.0022992538288235664seconds.
Evidence: audit record theory_v05_audit, proof SHA256 1f45effc422ae46066199fb376d8559e2b8fe7ee96a65bd8f9915f495ab5bda0; code/check.py SHA256 499de57bab12f0b0863b2b5c01c9659a0b46a6cd9a3a1f469ee979c20a77e2bb; verification/result.json SHA256 2e58fcba425c99c4b2cb917b0d9e976aecee86a302ef4bc5f3ffe18931515383; frozen v05 SHA256 b003dd48930032569529ad4962bcb64cb531bb8dab3b616d82f2e56aa47a6cc5; pre-correction working summary is frozen in source/AUDIT_SUMMARY_before_310.md.

## T4-313: Complete016 far-field prefix independently confirmed

Date: 2026-10-29T07:16:29.011342+00:00.
Claim: N4-242's exact016 sector flags and the additional N1 sectors (9,0),(1,2),(10,0) follow from the immutable raw generators.
Method: Independent homogeneous potential expansion of every raw generator in z=r^-2, followed by exact polar differentiation and every nonlinear sector product. The252 legqs generators carry z^4, so contribute zero through descendant L=2. Enumerate the complete exponent>=-7/2 prefix exactly. Compare thirteen common maps with N4 in rational arithmetic and all sixteen rows with N1 status/norms; check all sixteen Poisson identities and all four leading density/stream profiles against007.
Result and verdict: CONFIRMED the thirteen common N4 maps, all sixteen sector statuses and the four common profiles. Nonzero sectors are exactly(4,1),(9,0),(5,1),(1,2),(10,0), with first exponent4gamma-5. Three further exact nonzero coefficient maps have N1 FLOAT norm comparisons and await any desired independent exact-map reproduction. This supplies the coordinator's requested016 far-field audit, not a residual upper norm or existence theorem. Completed2026-10-29T07:14:36.723997+00:00 in22.943267052061856seconds. An earlier run incorrectly assumed identical peer prefix lists and stopped before output; the scope correction is in DEVELOPMENT.md.
Evidence: audit record candidate016_sectors, proof SHA256 67781aaea56929aea91dca6d199708d2405ffdb55c15c64147e72c92e9249c22; code/check.py SHA256 575ae0a66e52ee1002f04fa79cce4fbb41f8b1b7981110eebe3d78f0a7ece30e; verification/result.json SHA256 2806407565030c159e22b74016447aa762915d0343bf3454a896cf9629003a6e; exact sector JSON SHA256 fdf5ccdb39abda83725ed0c64e01263dabf385c67cfe51c1871529b9fc93899d.

## T4-314: Far-out potential repair has arbitrarily small L2 cost

Date: 2026-10-29T07:16:29.011342+00:00.
Claim: For-3<q<-1, a fixed smooth radial cutoff of a prescribed homogeneous potential tail, dilated to radiusL, has canonical density/velocity scalingL^q and exact weighted derivative norms scalingL^(q+1+beta-k). It can cancel the campaign(4,1) tail while its L2, graded Hessian and sharp Hessian costs tend to zero.
Method: Complete standalone proof precedes code. Identify canonical velocity by the L2 divergence/curl equations, retaining the full multiplier; derive exact scaling and the quantitative residual perturbation bound. Verify exact campaign exponents and all120 nonzero A1 coefficients.
Result and verdict: OPEN independent Opus review. The analytic argument and exact specialization pass own review. The new reference preserves the full interior disk and every origin jet, cancels the prescribed exterior tail, and retains first residual sector(9,0). It does not produce a stationary solution. The triangle inequality preserves any existing distance exclusion when the correction norm is smaller than its margin. No lower bound on all tail-repair costs follows from the large norm of the particular global polynomial repair.
Evidence: audit record far_out_tail_repair, proof SHA256 d0160e7250906bfbc432a9ec8399b54601129b4364d9a96ebb4664450f73b83b; code/check.py SHA256 85563aa0766859141d94c424ac75999ee794e3cd7dfdef2d14bcb74f28ad5667; verification/result.json SHA256 c034258e6b324c17262e198d2e2cf1ce650ace0e779198ab246af1cc52a3422a; exact specialization runtime0.028549750801175833seconds, completed2026-10-29T07:16:28.968005+00:00.

## T4-315: Forced integrable tail and global repair accepted after Opus reviews

Date: 2026-10-29T07:21:25.250272+00:00.
Claim: T2 the review of T4-294 and T1 R1-034 independently confirm T4-294 and T4-295.
Method: Read both complete reviews and independent checkers; recheck the kernel partition, contact term, radial signs, domain at q>=-1, origin orders and canonical velocity. Compare all exact repair, zero-sector, ladder and first-sector flags, and directed C_q intervals.
Result and verdict: CONFIRMED; T4-294 and T4-295 are AUDITED. The physical-kernel/Lp definition covers -1<=q<0; the candidate application is in L2. The phrase only(4,1),(4,2)change refers to density/stream prefixes, not residuals. The peer's dipole extension and faster-decay corollary remain separate pending claims. No inverse or residual smallness follows.
Evidence: audit/theory_audit/research_code/forced_integrable_tail/reviews/ACCEPTANCE.md SHA256 e10a28b17194c4f3c6652c97fedab8aad7cdfdf35c33b2f5cf72f02b22e19416; acceptance JSON SHA256 b1bccd51308d73c1b5023d90f188dec69ef7a53bfdc30e0ec6b1538bf9c60aa4; T2 review SHA256 4c23eaedc7183b727740c7a2bfe4db55765beeae86ac406a1294bfef515abd5e; T1 review SHA256 e038dc73410689e38f59eaae7b53665dc61e55aefea78790778ad75fc9c2abc1.

## T4-316: Particular global polynomial repair norms independently confirmed

Date: 2026-10-29T07:21:25.250272+00:00.
Claim: The three T4-295 repairs have L2 norm greater than4373.34.
Method: Independent exact polar differentiation, polynomial division by1-t, exact squares and complete finite rational-Beta moments at2048-bit Arb precision. All three intervals overlap the independent Opus calculation.
Result and verdict: CONFIRMED. Norms are4373.36938664759278...(007),4373.36854273639287...(013),4373.34268004322653...(014). Runtime0.5611942219547927seconds, completed2026-10-29T07:17:27.859805+00:00. The lower bound concerns this particular global formula only; T4-314 investigates another family with arbitrarily small cost.
Evidence: audit record tail_repair_norm, proof SHA256 17df46943ef09e0c655d5bac9abaa287a6d0fb2298de05c4114f1aba35b17f27; code SHA256 60bd36349d48a5e145463a95c02bd10c677c93f71b01214c8572afeb79037058; result SHA256 3d90434eb9342b6ec8b1c440539ae42f584f418c72a86ab1ef8d5d7cf428e89d.

## T4-317: Opus dipole forced-tail extension independently confirmed

Date: 2026-10-29T07:24:24.762971+00:00.
Claim: the review of T4-294 R2 extends the forced-tail theorem to gamma-4<q<-3 using the canonical dipole velocity estimate.
Method: Independent standalone proof retains the contact term, integrates the full first moment in the inner kernel region, and solves the radial difference equation with the r^(gamma-4) coupling term included. Exact rational exponents and512-bit Arb verify the three campaign applications and compare the Opus constant.
Result and verdict: CONFIRMED. For the precise C1 weighted-decay and stationary hypotheses in PROOF.md, |U[h]|<=D_q H_q(h)r^-3 and the stated four-term error bound hold. At q2=1-9delta, D_q2 is between610.805532899 and610.805532900. The forced(9,0)density circle norm is5428.790031389922696... for all007,013,014. No coefficient is forced by this argument at q=gamma-4. Runtime1.0042095272801816seconds, completed2026-10-29T07:23:17.280887+00:00.
Evidence: audit record dipole_forced_tail, proof SHA256 c9f36de80ca53c0d97f742e99bad6cf0c0e34ff4a826d60a0d9650046ee16c21; code SHA256 a942666b0ba7c9096ad79aae1d2edf5e175a27f6c470e62b19d5a35ab4cd8ed0; result SHA256 3e07179d6d82d71086d695bf01034531682dea277604a9ce6dfcc258b4c3f20b.

## T4-318: Faster weighted C1 correction decay independently excluded

Date: 2026-10-29T07:24:24.762971+00:00.
Claim: the review of T4-294 R3 excludes H_q'-finite exact corrections with q'<q1 before the repair and q'<q2 after it.
Method: H_q(h)<=H_q'(h) for q'<q; divide the independently accepted forced-tail identity by r^q and use its nonzero limiting coefficient.
Result and verdict: CONFIRMED under the exact fixed-c, canonical-velocity and weighted C1 hypotheses of the two theorems. For007,013,014, q1=-1-4delta before the repair and q2=1-9delta after it. This does not exclude arbitrary L2 corrections or assert existence at the threshold.
Evidence: audit record dipole_forced_tail, proof, sections3and4, and T4-315/T4-317.

## T4-319: Candidate017 point exclusions independently confirmed

Date: 2026-10-29T07:30:48.163016+00:00.
Claim: N4-254's local fields and six scalar plus original-graded necessary point gaps hold for immutable C1-N1-017-legqs50-quot013.
Method: Independent exact radial Taylor data through fourth order, polar density/velocity formulas and1024-bit Arb. Every raw generator is included; the radius50 denominator is2500(1-t)+t>0. Compare all eight fields and all six gaps with N4's Cartesian calculation.
Result and verdict: CONFIRMED. F(1/10,73/100)=0.08993927431084596634..., original-graded gap=0.06953622573013016376..., all six scalar gaps positive. Runtime2.1300859772600234seconds, completed2026-10-29T07:26:09.735711+00:00. Local tests do not provide a full-plane residual norm or the remaining statL/bL distance tests.
Evidence: audit record candidate017_point, proof SHA256 03e61249f325e3062b316ab8c7e6d0903c270d425953641fb2a779cc3e2dc04f; code SHA256 318ad769a06a692ca6dc30521923d949e431bf4524493186c461b18083f89535; result SHA256 e755eab031ea4524bdc392468165704e2bc5ea0c6980fbf5937e6e9544acf2b0; rawSHA7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114.

## T4-320: Candidate017 registered full-plane weak distance independently confirmed

Date: 2026-10-29T07:30:48.163016+00:00.
Claim: The registered n23,K2400 probe for017 gives necessary L2 radius>1068502321536437/1000000000000000000.
Method: Independent full polar reconstruction and direct factored hypergeometric moments at2048bits; four scalar fixtures, exact007 field calibration, all six actual017 point checks, all angular M/C products, exact CRT replay, direct/parts identity and complete gradient critical points. Compare all eight scalar intervals with the independent N4 radius50 calculation.
Result and verdict: CONFIRMED. Radius>0.001068502321536437>25/54684, excluding every named smaller scalar/graded budget including statL andbL. Runtime134.3564906278625seconds, completed2026-10-29T07:29:19.741405+00:00. This is a necessary correction bound, not an actual-distance estimate, probe-register maximum, inverse or existence proof.
Evidence: audit record candidate017_weak, proof SHA256 0794ac3ae7c2caf51ed22a46f9c16ea9be54c21fc62e1d5bca20585631ef2714; code SHA256 29b3b3b182d950b98b2ac07f0aae97b8646f7f4272431a2cc42485979cdaf1db; result SHA256 e8be5f47c0ca86681e4697b378f1336daec1107790e055570abe64f8ff3aace5; peer result SHA256 61fe31cd9cbf747b1be985df4620b05796583989e4b4fe998b2fb25e6921e8d6.

## T4-321: Radius25 extension has exact potential rank2174

Date: 2026-10-29T07:30:48.163016+00:00.
Claim: N4-248's252 new potential directions are independent modulo the audited1922-dimensional old space, and mode17 occurs among their densities.
Method: Read complete N4 proof/checker. Independently use Rodrigues polynomials to verify all84 nonzero Laurent coefficients at-1/624, all28 branch differences and8 nonintegrality conditions, and exact old/new generator shape sets. Orthogonal angular modes, distinct branch powers and largest pole orders prove independence. The same calculation also checks radius50 at-1/2499.
Result and verdict: CONFIRMED N4-248, including exact mode17 coefficient-25980116626525539798432/2547797787649488125. Radius50 has the identical proof with a different positive scale and passes all finite checks; its extension is submitted with the density lemma for Opus review. The first checker required identical ordering of the old basis; it was corrected to compare the same1922distinct shapes as sets, as documented. Runtime0.07788248127326369seconds, completed2026-10-29T07:29:55.962524+00:00. No conditioning, objective floor or inverse follows.
Evidence: audit record scaled_rank_audit, proof SHA256 8386bfca0b18b70248698cc3b386132cc8182bdadfad59ed13efedb45fedac96; code SHA256 10dc1dfc460334d47abe1bddff01f25311739eda3566c29c87a7c42dad8d3b7e; result SHA256 b95295c053ae1d976874cac9c2e4e695e9240aa0c552ee0d98a1ec9476945402; N4resultSHA084418d3f47bca67dc97fd995ee2ab8e68e88422e07432bfce48873d69fd0bfd.

## T4-322: No additional density gauge in the radius-scaled spaces

Date: 2026-10-29T07:30:48.163016+00:00.
Claim: The radius25andradius50 augmented potential spaces also have density rank2174.
Method: Extend audited T4-199: fourth derivatives decay, zero density forces a quadratic potential, and noninteger branch powers exclude every such nonzero polynomial. The rational radial factors are smooth at physical radii and analytic at infinity, so the same least-exponent proof applies.
Result and verdict: OPEN independent Opus review. The full own proof is section4 of the standalone rank note; all exact exponent checks pass. This concerns representation injectivity only, not the linearized PDE.
Evidence: audit record scaled_rank_audit, proof, section4, and the exact verification result cited in321.

## T4-323: Complete candidate017 far-field prefix independently confirmed

Date: 2026-10-29T07:35:21.208989+00:00.
Claim: The immutable radius50 candidate has the complete exponent >= -7/2 sector prefix reported by N1, with N4's thirteen common exact maps and the four leading profiles of007.
Method: Expand all2174 raw potential generators homogeneously in z=r^-2, differentiate in polar coordinates and include every nonlinear sector product in exact rational arithmetic. The252 new generators start at descendant L=4. Compare all thirteen common coefficient maps and Arb norms with N4, sixteen statuses with N1, and all four density/stream profiles with007.
Result and verdict: CONFIRMED. Sixteen sectors, eleven zero, and nonzero sectors exactly(4,1),(9,0),(5,1),(1,2),(10,0). The first is4gamma-5. Together with319and320 this supplies all independent017 checks requested by the coordinator. No residual upper norm, inverse or existence theorem follows. Runtime23.008442484773695seconds, completed2026-10-29T07:30:19.016254+00:00.
Evidence: audit record candidate017_sectors, proof SHA256 205d52c903059623e5fa1239658242de7cd77ebd64ed5ab72b72cb75e07faac1; code SHA256 d5a64e83887d278bdd47fbc89ce420ca3294788de60ebe1fb1f97b859fa0b56f; result SHA256 14fa4de257a83189617673fae0e71d325485e91b2b4edd12a4bbde2e995e3793; exact sector data SHA256 c84fb9082f634a325db6c350c5b182f57ff5c30037284ac3003df5e21cd777cd.

## T4-324: Two homogeneous tails can be removed at arbitrarily small L2 cost

Date: 2026-10-29T07:35:21.208989+00:00.
Claim: For q<-1 and nonresonant a=q+3, any finite odd-sine density tail has a unique finite even-cosine potential at homogeneity a. A smooth potential cutoff dilated to a large radius realizes that tail with arbitrarily small density and residual changes in L2. Applied successively to007,013,014, it removes(4,1)and(9,0), leaving residual O(r^(-1-5delta)).
Method: Write the complete triangular inverse after the radial exponent shift caused by the Laplacian, identify the canonical velocity by the L2 harmonic uniqueness argument, and prove exact dilation norms and residual bounds. For q<-3 prove vanishing first moments, including the cutoff annulus. Independently solve the exact angular systems, differentiate them directly, and compare all120 first-tail coefficients with the accepted A1 repair.
Result and verdict: OPEN independent Opus review. Own analytic and exact checks pass. Ninety exact potential coefficients per candidate solve the second tail. The construction preserves the interior and origin jets and any distance exclusion with a larger margin. It neither produces a stationary solution nor makes a fixed nonzero full residual tend to zero. The preliminary draft's radial shift was corrected before computation or registration and is documented in DEVELOPMENT.md. Runtime0.9190054549835622seconds, completed2026-10-29T07:32:53.891957+00:00.
Evidence: audit record homogeneous_tail_surgery, proof SHA256 966279c233b843e49d321764be482ccaf4ddd01436f23b421d1ea49aaae8aa27; code SHA256 bfbeb237710f8d9f821744debfbc50c342fdf38757cdf7a42af2ec4b38b2c822; result SHA256 547e9ea4ec0d5c701f48277a8c5286c44ba799a05cc5970e20da04ac3f3cce8d; exact JSON outputs and all frozen input hashes are in that result.

## T4-325: Far-out tail repair accepted after Opus review

Date: 2026-10-29T07:38:02.543183+00:00.
Claim: R1-035 confirms the exact T4-314 proof, including the canonical velocity, norm scaling, residual bound and first-tail application.
Method: Read the complete review and independent symbolic/numerical checker; verify the bound proof, Fourier signs, derivative exponents, sector ordering and weighted membership against the frozen T4 proof.
Result and verdict: CONFIRMED; T4-314 is AUDITED. The mpmath values C00 approximately215936.94 and the proposed cutoff radii remain FLOAT and are not used as certificates. The analytic existence of a sufficiently large radius uses only the defined finite constants. No inverse or stationary solution is implied.
Evidence: audit/theory_audit/research_code/far_out_tail_repair/reviews/R1_035/ACCEPTANCE.md SHA256 4fbfa07ca7f5d75af059beb2f683214ea1340b2a4687f05d41d7d53d7802843f; frozen R1-035 review SHA256 e5afb52af154817583df4c56dfcf108f1c4c36c0f91de9e5def23ef86a213d7e; complete source manifest alongside it.

## T4-326: Opus weighted-residual cost of the cutoff independently confirmed

Date: 2026-10-29T07:38:02.543183+00:00.
Claim: R1-035 remark(b): for a<=q+1 the residual of the far-out cutoff family grows as its L2 correction tends to zero.
Method: Prove a finite-annulus bound with explicit remainder radius R=max(R0,(E/(epsilon M))^(1/eta)). Integrate the angular reverse-triangle bound over R<=r<=L. For kappa=q+1-a>0 obtain(1-epsilon)M sqrt((L^(2kappa)-R^(2kappa))/(2kappa)); at equality obtain(1-epsilon)M sqrt(log(L/R)). Substitute the exact correction norm C L^(q+1).
Result and verdict: CONFIRMED under the stated uniform remainder and interior-agreement assumptions. The power-law lower bound has coefficient M/sqrt(2kappa); the endpoint is logarithmic. In the campaign's range-2<a<=4gamma-4 the repaired residual norm is finite but diverges along this family. This is a tradeoff for this construction, not a lower bound for every tail repair or every framework. Exact exponent check completed2026-10-29T07:36:27.906066+00:00 in0.0004562009125947952seconds.
Evidence: audit record tail_cutoff_weighted_cost, proof SHA256 dd76d51d2b82db0de39703d5a8a621ed5d8431ceef2c5e51bb138f445e2497b5; verification/result.json SHA256 34696536ff4410dafcaae41bfb0529ad1a8deb4753f72bc66590ba7d685bac3b.

## T4-327: Mode-wise Mellin identity and sharpness, with origin-domain clarification

Date: 2026-10-29T07:38:02.543183+00:00.
Claim: T2 REVIEW_N3_MODE_HARDY R2 gives the exact Mellin identity, strict Hardy inequality, optimal constant1/n, and the Gaussian ratio n/(n+1).
Method: Independent complete proof using the one-dimensional resolvent and Dirichlet approximation; check the origin by cutting off angular test projections. Derive the Gaussian example independently by the two-dimensional Fourier transform and verify all63 exact factorial ratios. Enclose three logarithmic-Gaussian ratios with1024-bit Arb. Examine the proposed domain with only r g in L2.
Result and verdict: CONFIRMED under the reviewed lemma's original assumptions g and r g in L2. The extension with only r g in L2 requires defining the angular-cancellation distribution explicitly: that assumption does not imply local integrability. The example f=r^-2/log(1/r) near0 proves this limitation. With the stated cancellation convention the extension is valid as well. The007 application is smooth and unaffected. Runtime0.001779946032911539seconds, completed2026-10-29T07:37:28.388686+00:00. No new inverse or candidate norm certificate is claimed.
Evidence: audit record mode_hardy_mellin, proof SHA256 5e1d8e3a35f0e49ad111b61db5c9d1dd5e453377b74ffcef945af25b60a9f395; verification/result.json SHA256 e3a14c056f6917855309ba86677c29ffa936bac774096141f10dd60c7d662b71; frozen Opus review SHA256 47fa8da5294dccf97de5cc9035c2ea89544d19c9237cdb02b792fc369da6bd89.

## T4-328: H12 sector specification corrected

Date: 2026-10-29T07:42:48.987342+00:00.
Claim: THEORY_FINAL draft12 uses global indices e=1-l delta-2q but requires the three nonautomatic cancellations(1,0),(2,0),(3,0).
Method: Exact exhaustive enumeration at exponents>=-1 and>=-2, plus the radial L2 integrability test. Compare the new definition with the old h-index by l=h+1.
Result and verdict: REFUTED as an indexed specification. The correct nonautomatic L2 list is(2,0),(3,0),(4,0). The three-versus-seven counts are CONFIRMED. Repair lines77,104,134,189,583,841 of the frozen draft. Existing eleven-sector candidate certificates include all required cancellations, so no exclusion changes.
Evidence: audit record theory_final_h12_audit, proof SHA256 56730ae0043f5d0b5a00147a8963f0673254bd93d74c11c7319b65f45555a536; exact result SHA256 7e0d7290abec09ac54041c332a3e0d1e7e47f3481cadec77b0c37c23f9034815; source SHA256 5e4f4b003ed15fbed67ba4e6e32bafe2c4dd23b8b48bf4a3b42cddcb8d23daa6.

## T4-329: H12 forced-tail domains and numerical cutoff threshold

Date: 2026-10-29T07:42:48.987342+00:00.
Claim: The H12 G6 summary gives the second forced correction tail, and a cutoff norm below1e-3 requires a radius above approximately45174.
Method: Trace every hypothesis to the audited T4-294/317 statements and distinguish the original reference R, repaired reference R+eta, total correction h and new correction k. Use the exact dilation identity for the cutoff norm.
Result and verdict: OPEN as an unqualified standalone theorem until the omitted reference-growth bounds and H_q2(k) hypothesis are stated. CONFIRMED with those hypotheses and h_total=eta+k, k=r^q2 F_(9,0)/(1-cq2)+o(r^q2). The radius criterion for the particular family is exactly L>(C00/epsilon)^(1/(-q1-1)); the numerical45174.312 estimate remains FLOAT. Underlying audited proofs are unchanged.
Evidence: same standalone audit, sections2and3; audit record forced_integrable_tail, proof; audit record dipole_forced_tail, proof; T4-325and326.

## T4-330: H12 arithmetic and interpretation audit

Date: 2026-10-29T07:42:48.987342+00:00.
Claim: The fourteen numerical rows of THEORY_FINAL draft12 have conservative ratios; numerics_v09's finite probe reductions decide a previous span floor and localize residual mass to a finite mode band.
Method: Exact rational checks of all42 displayed factors, retaining OPEN status for the stronger017 input; apply the explicit finite-probe kernel and damped-step counterexamples of T4-312 to numerics_v09. Check current candidate and dyadic statuses.
Result and verdict: CONFIRMED all42 ratios, REFUTED the stated probe/optimization deductions. The017 status is superseded by319/320/323, and010's dyadic test by303. Correct T4's own overbroad H12 shorthand to all registered scalar and graded pairs through017, excluding the FLOAT comparison011; this does not claim every dyadic pair or the incomplete localized route is excluded. Runtime0.001841497141867876seconds, completed2026-10-29T07:42:03.764047+00:00.
Evidence: same standalone audit, sections4and5, result SHA256 7e0d7290abec09ac54041c332a3e0d1e7e47f3481cadec77b0c37c23f9034815; numerics_v09 SHA256 e77839d57014df0345334a0de15a32b3419292a775647823f2ce1db1fd564862.

## T4-331: Stronger registered candidate017 weak witness independently confirmed

Date: 2026-10-29T07:52:28.899414+00:00.
Claim: N4-257's registered n19,K1800 test gives necessary L2 correction greater than20897883728991/12500000000000000 for immutable candidate017.
Method: Reuse the reviewed full polar reconstruction with fresh complete angular products, exact CRT identities,2048-bit direct hypergeometric integration, independent gradient critical-point certificate, raw007 calibration and all actual017 point checks. Compare all eight scalar enclosures with the independent N4 calculation.
Result and verdict: CONFIRMED. Radius>0.00167183069831928>25/54684. The run completed2026-10-29T07:46:54.898025+00:00 in132.32147747883573seconds. The stronger floor reinforces the already registered scalar/graded exclusions; it is not a maximum over probes or an estimate of actual distance. No active computation remains. The candidate017 sector proof's name is corrected from legqs25 to legqs50 by the separate ERRATA.md; raw data, radius50 code and all sector conclusions were already correct.
Evidence: audit/theory_audit/research_code/candidate017_weak/verification/n19_K1800.json SHA256 21d3480547f0b80b04ccb7a15e9ceb3ac6f8b4fa71381e66f3c2070b0ee847fd; proof/code hashes asT4-320; frozen N4 n19 input SHA256 80db2ef50716df589d2d2b751fc8feb5884005a8782ea122ee486a429fc4d356; sector ERRATA SHA256 14083fc7e3ecd7ed0300195b610e2b1e9ac4f91e3763f95d7901d41a02b93695.

## T4-332: Scaled density injectivity accepted after Opus review

Date: 2026-10-29T07:52:28.899414+00:00.
Claim: T1 R1-036 confirms T4-322 and its radius50 specialization.
Method: Read the complete independent review, exact checker and output; recheck growth, reduction to quadratics, branch separation and the final use of potential independence. Freeze the review and evidence in the local topic folder.
Result and verdict: CONFIRMED; T4-322 is AUDITED. Both radius25 andradius50 spaces have potential and density rank2174. The general analytic-factor observation preserves injectivity when its hypotheses hold, but a separate independence argument is needed for any new dimension count. No inverse or objective floor is implied.
Evidence: audit/theory_audit/research_code/scaled_rank_audit/reviews/R1_036/ACCEPTANCE.md SHA256 dea2de7fe4d98f24133b0ccab255ef7e816150cb1f355bd6a8d5108c646df5b0; frozen review SHA256 16f477438241e0531cf4d0e5142bdb5aff1055e249e43e034fa2261edea5b1a1; peer checker SHA256 d3e7e6cf6ca0ec2956b4a3f7caa1894abf3ac579ce7a410ed0f3013c4099a9d9; peer output SHA256 f3cd671f36eb06a3b3c5a3f7b0cad1c0566ffa329577d415592c6f85f1780ea8; original proof SHA256 8386bfca0b18b70248698cc3b386132cc8182bdadfad59ed13efedb45fedac96.

## T4-333: Second Opus review of the far-out cutoff accepted

Date: 2026-10-29T07:55:41.086505+00:00.
Claim: T2 the review of T4-314 confirms the original potential cutoff theorem and residual perturbation bound.
Method: Read the complete review and its independent symbolic/numerical checker; compare its canonical divergence/curl argument, full Fourier multiplier, support and derivative scaling with the registered proof. Freeze the review, checker and results locally.
Result and verdict: CONFIRMED. This is a second review of314, already AUDITED through325. The finite constants in the residual perturbation bound remain unevaluated for the actual references; the review's quadrature constants and numerical cutoff radii remain FLOAT.
Evidence: audit/theory_audit/research_code/cutoff_norm_extensions/source/the review of T4-314 SHA256 2e04bc199c60ba57cb8d46a3f1931940c16288d72097d7f4dfae0c136898deb0; source checker SHA256 9e6f7b8cf51d07b2e99c3e4a33eb9bab4fc020bb49b2be503b227c928bc79bd4; original proof SHA256 d0160e7250906bfbc432a9ec8399b54601129b4364d9a96ebb4664450f73b83b.

## T4-334: Negative Sobolev cutoff costs and endpoint sector agreement confirmed

Date: 2026-10-29T07:55:41.086505+00:00.
Claim: T2 the review of T4-314 R2 andR3 extend the cutoff scaling to dot H^-sigma, identify a nonvanishing weighted C1 cost, and preserve the global repair's residual sectors through gamma-4.
Method: Independent complete proof using Fourier dilation, the audited mode Hardy bound, the Laplacian primitive, exact exterior powers and the full residual difference. Check every campaign exponent by rational arithmetic.
Result and verdict: CONFIRMED under the precise hypotheses in PROOF.md. For q<-2 and0<sigma<=1 the cutoff's dot H^-sigma cost tends to zero. For the nonzero campaign tail the H_q cost has a positive lower bound independent of cutoff radius. The residual coefficients agree at or above gamma-4, including endpoint(1,2); replacing this by strictly above would omit that endpoint. The forced(9,0) tail applies only to a newly named correction k with H_q2(k)<infinity. No candidate verdict changes. Exact check completed2026-10-29T07:54:31.819648+00:00 in0.0009037721902132034seconds.
Evidence: audit record cutoff_norm_extensions, proof SHA256 4eaadc7e7d870a1d231e2139cb69026cad1379900002c9386bca536c6cbac810; checker SHA256 c15fe80f58cbefd91dec2543dd4e9a762a8b036f568e8e60bd96962be87bbf3f; result SHA256 7dbbd7855b0e93c4311fac01aca8338cde795aa828aaecd1eae8d9ff387c0083.

## T4-335: Moment-resolved velocity and a noncompact endpoint theorem

Date: 2026-10-29T07:59:07.135842+00:00.
Claim: For centrally odd C1 h with H_q(h)<infinity and-5<q<-3, the canonical velocity satisfies |U[h]+DK M|<=E_q H_q(h)r^q, with the explicit six-term constant in PROOF.md; at qstar=gamma-4 the stationary correction has leading coefficient[A+(My/pi)P]/(4c).
Method: Complete new proof: split the physical kernel into four regions, retain the local/contact term, use parity to cancel the constant and quadratic Taylor terms, bound the cubic remainder and the missing moment tail, then integrate the exact stationary radial equation. Verify the kernel Jacobian norm, third derivative and dipole sign symbolically, and all campaign angular projection identities in exact rational arithmetic with768-bit Arb norms.
Result and verdict: OPEN independent Opus review. Own analytic review and all exact checks pass. E_qstar=133.004254783715271... . The theorem excludes faster weighted C1 corrections when A is not in span(P), under the full endpoint reference hypotheses. The three previously verified angular pairs have exact nonproportionality and prospective angular tail coefficient bounds above85017,85018,85016 respectively. These are angular coefficients, not whole-plane distance bounds. The original, single- and double-repaired references still have larger residual sectors and do not yet meet the new endpoint theorem's reference hypothesis. No new candidate verdict is asserted. Exact computation completed2026-10-29T07:58:21.447214+00:00 in0.1184678147546947seconds.
Evidence: audit record moment_resolved_tail, proof SHA256 99aa80a9b5ce0474e26c8a53e53218b2b1bb628f0283eab5eb62b4aeefead6df; code SHA256 c18f2c4794cfe75fa0943a5b29b44915603293f1546961e1a7e0439549f36b10; result SHA256 65c496ab2f0220ed38175d01339ca3796627f2223469aa6c42b019e50801e03b; exact coefficient input hashes match T4-305.

## T4-336: THEORY_FINAL draft15 repairs and one remaining cutoff error

Date: 2026-10-29T08:02:27.826538+00:00.
Claim: Draft15 repairs the earlier sector labels and forced-tail domains, and says that both cutoffs change the (5,1) residual coefficient.
Method: Read the complete diff from audited draft12, check all42 table ratios by exact arithmetic, and compare each new theorem statement with its standalone proof. Order the second cutoff's linear, mixed and quadratic exponents against q3=-1-5delta.
Result and verdict: CONFIRMED the328and329 repairs, all42 conservative ratios, the corrected010 dyadic status and the finite-probe caveats. REFUTED the sentence that both cutoffs change(5,1): the first changes it; the second preserves it since q2-delta<q3 and2q2-1<q3. The source proof324 already has the correct inequalities. No candidate exclusion changes. Draft16's subsequent status updates are not covered by this entry. Arithmetic completed2026-10-29T08:00:21.992541+00:00 in0.0018808459863066673seconds.
Evidence: audit record theory_final_draft15_audit, proof SHA256 bdfd20d7fcfb8901bb04d4d01ca34caa308967535789d6ccb0631dc1c0d6e710; source SHA256 345b9a31b1b72a2a8a61526df000114a703eb947ae4eb81ba238b371e14097d5; result SHA256 2f11fc462d436b82968470c6dfa47f4379ce3990e64e11eda6512d4158eb2e5c.

## T4-337: Independent Opus review of the two homogeneous cutoffs accepted

Date: 2026-10-29T08:06:00.492813+00:00.
Claim: T2 the review of T4-324 confirms the finite angular inverse, canonical potential cutoff and two successive tail removals in T4-324.
Method: Read the complete review, its revised R3, code and log; independently recheck the density/stream signs, nonresonance roots, scaling, first-moment boundary terms, residual exponents and sequential radius choices.
Result and verdict: CONFIRMED; T4-324 is AUDITED. The independent exact 007 coefficient reconstruction agrees with both stored repairs. The second radius and its background constants depend on the first repair. The review's numerical cutoff constants and radii remain FLOAT. Additional R2/R3 assertions are being audited separately; this acceptance does not extend automatically to them. No existence or candidate verdict changes.
Evidence: audit/theory_audit/research_code/homogeneous_tail_surgery/reviews/T2_324/ACCEPTANCE.md SHA256 82621312d3855ca4d5927f49bbe4d565460ca411439c18800b9cd3c19d98e5b6; frozen review SHA256 81741e5c8ba5c19dc294e108aee6d341f3658938845bc0550dfff33d4d03ccde; checker SHA256 fd806d3d4a335e1cd79c38cd7f3d2cf3d85e73648a7bbacda46b779c7fe68bea; log SHA256 6d4cd8f3e2c5c33657bab18944f2782baca5f210059385457ed1f757d056967d; result SHA256 cd7eb83434be20e48a84a02554009b8105c77fdf88c9376d39f4e7e8fa6b555e.

## T4-338: Finite-order tail removal and the third campaign cutoff

Date: 2026-10-29T08:09:20.655281+00:00.
Claim: Opus the review of T4-324 R2/R3 allow finite removal of every residual sector above a fixed nonresonant threshold; a third cutoff removes (5,1) for007,013,014 and preserves the endpoint (1,2).
Method: Independent standalone proof with explicit finite angular expansion, differentiated remainder, growth and positive-first-index hypotheses. Prove arithmetic nonresonance for T>=-3649353293107865, strict descent of the sector algebra, and successively small L2 density and residual costs. Reconstruct all18 original sector maps in each of three exact references, then directly differentiate the second and third potentials and recompute the entire relevant residual prefix.
Result and verdict: CONFIRMED under the stated hypotheses. The first cutoff changes (5,1); the second preserves it. The third eliminates it and preserves (1,2), which is then the sole leading sector. The common third angular density coefficient has circle norm in(27840,27842). The construction is finite reference design, preserves the interior disk and leading profile, and supplies no inverse or stationary solution. Runtime157.50640100613236seconds, completed2026-10-29T08:07:21.814223+00:00.
Evidence: audit record finite_tail_surgery, proof SHA256 11a6a2eb04c60a33e2bae2e8692c839556762a7b47e9485e2dc72cd4d8b7c990; code/check.py SHA256 8a669b9c3534c99b017a0c373387fc48d500b1afa25f5961e3d01fce2afc535e; verification/result.json SHA256 97be3636ee5fe5c097d4af80365b9f9d3472868b8c0c4afb99c4b6b40f511361; exact JSON inputs and outputs in source/ and data/, all bound by verification/MANIFEST.json.

## T4-339: Conditional endpoint obstruction after three cutoffs

Date: 2026-10-29T08:09:20.655281+00:00.
Claim: A third-cutoff reference has the asymptotic hypotheses for the moment-resolved endpoint theorem and admits no stationary weighted C1 correction decaying strictly faster than r^(gamma-4).
Method: Apply the explicit endpoint expansion of T4-335 to the exact unchanged (1,2) residual and leading profile verified in338. The first-moment term spans the single angular direction P; its distance from the residual coefficient was computed exactly and with directed arithmetic in335.
Result and verdict: OPEN, conditional on independent review of T4-335. The reference construction and preservation of the endpoint coefficient are CONFIRMED in338. Conditional on335, the asymptotic coefficient has circle-norm lower bounds85017,85018,85016 for007,013,014, respectively. These are not whole-plane distance estimates. A fourth reference cutoff can remove the endpoint, so no obstruction to all finite reference design is claimed.
Evidence: audit record finite_tail_surgery, proof section3, SHA256 11a6a2eb04c60a33e2bae2e8692c839556762a7b47e9485e2dc72cd4d8b7c990; audit record moment_resolved_tail, proof SHA256 99aa80a9b5ce0474e26c8a53e53218b2b1bb628f0283eab5eb62b4aeefead6df.

## T4-340: H12 numerical report inference and status audit

Date: 2026-10-29T08:11:36.460256+00:00.
Claim: The 08:02 NUMERICS_FINAL establishes an old-basis span floor, redistribution of residual mass into modes33-47, stationary GN plateaus, a universal smooth-integrand quadrature accuracy, and all-snapshot/all-ball exclusion.
Method: Full report reading; standalone exact counterexamples using a common probe kernel, scalar damped least squares, identical Jacobians with different gradients, and smooth bumps between quadrature nodes. Trace every relevant exclusion to its actual framework and certificate. Retain the exact Newton bound via T4-214.
Result and verdict: REFUTED as inferences. Small finite probes do not certify an infimum or angular-band mass, and their optimization does not invalidate rigorous necessary bounds. Two damping values do not bracket the undamped solution. GN stationarity and an irremovable point-test obstruction remain OPEN. Correct density support is17-31. Current scope is scalar/original graded pairs through017 except011, with separately specified dyadic coverage and incomplete localization;018 remains OPEN. The existing candidate exclusions stand. The report's007,016,017 entries need the current certificates listed in the standalone proof.
Evidence: audit record numerics_final_h12_audit, proof SHA256 ea36fca4f37b439484598b6a921760ce57f31ef5fcb4c0bf8c2b64cfb1fc4a43; frozen source SHA256 cc80028931ebc98b8e8d313eca840d88b17b3886ecdf3683bde20789b8d8402b; claim-by-claim verification/audit_manifest.json SHA256 ac2ce30a863a7cd7b2d6fae33fda2146bb91dbfb84d0a120e397389a4ba95274. No optimizer or FLOAT quadrature was re-executed for this analytic audit.

## T4-341: Draft17 cutoff repair and updated numerical table

Date: 2026-10-29T08:11:36.460256+00:00.
Claim: THEORY_FINAL draft17 correctly repairs the second-cutoff sentence and incorporates the stronger017 floor with conservative table ratios.
Method: Read every change from drafts15 through17; exact exponent comparison and rational check of all42 ratios against the upward scalar budgets and25/54684.
Result and verdict: CONFIRMED. Only the first cutoff changes(5,1); the second preserves it. All42 ratios are conservative, including017's440.7,586.6,3.656. The322 acceptance and335 OPEN status are correct.324's OPEN label is now stale, superseded by337, and its finite third-cutoff extension338 may be added with339 still conditional. Runtime0.0018746298737823963seconds, completed2026-10-29T08:10:51.026548+00:00.
Evidence: audit/theory_audit/research_code/theory_final_draft15_audit/DRAFT17_ADDENDUM.md SHA256 7ac53e8d24092d2a5a480aa018147f4df1927de7e162a3cfa18c6e99fed54506; source SHA256 b824beaf47936a5dd34bcce79ccc09c26b4bc2b154bc9f685b95b66f6f97f0a2; verification/draft17_result.json SHA256 76e99f479c8214a3b05462a92452a2e41cf076c1de95a466307b078bd12272d7.

## T4-342: Candidate018 independent point exclusions

Date: 2026-10-29T08:16:38.280255+00:00.
Claim: Candidate C1-N1-018-legqs25-cont12 fails the six registered scalar balls and the original uniformly graded ball at the rational point (1/10,73/100).
Method: Independent exact polar field construction and 1024-bit Arb evaluation of all eight fields and the necessary perturbation inequalities. Compare intervals with the frozen N4 certificate.
Result and verdict: CONFIRMED. Residual is in(0.09587881446813860,0.09587881446813861); the uniform graded gap exceeds0.07547297250468689. All six scalar gaps are strictly positive. This point audit does not independently verify origin normalization or exclude the larger L2 distance budgets. Runtime2.4835393419489264seconds; completed2026-10-29T08:13:10.811142+00:00.
Evidence: audit record candidate018_point, proof SHA256 f3952c1cd8798ec9b4993c8337a0063574c4f8cf0da457d31b34c6da3b55f47f; result SHA256 210d1ac7782c60565ddda33c8affc11e5992ba5241bb4710c9f5ee48b0588997; raw SHA256 1c99bf4d77865f7c576a9ba6c08bc08cf008416a737d4a8626b5799ceb4a85e2.

## T4-343: Candidate018 complete far-field sector prefix

Date: 2026-10-29T08:16:38.280255+00:00.
Claim: The 018 generator has the published exact cancellations and retained leading four profiles.
Method: Independently expand every monomial, Legendre and scaled Legendre generator in the homogeneous sector algebra; recompute all16 sectors with exponents at least-7/2, and compare all13 common N4 maps exactly.
Result and verdict: CONFIRMED. The raw262 monomial,1660 Legendre and252 scaled terms give11 zero sectors and five nonzero sectors(4,1),(9,0),(5,1),(1,2),(10,0). All16 N1 statuses,13 exact N4 maps and13 norm intervals agree. The leading four density and stream profiles equal007 exactly. Runtime33.79593834700063seconds; completed2026-10-29T08:13:44.696237+00:00.
Evidence: audit record candidate018_sectors, proof SHA256 2fc7b996075f3a91aa55e1d1d28a4be25f8cc3c6793bcee57d1a657d85b35c4b; result SHA256 60088e37dc3acc2108f0b4361bfbf130914106d9b1dd8f91aeb6ba329294755d; exact sector JSON SHA256 b459f76df8d2a0ce68d565b023617398ab55f8cabd1d500a249b45986cff29ac.

## T4-344: Review scope and endpoint radius clarification

Date: 2026-10-29T08:18:02.751024+00:00.
Claim: The third-cutoff application in338 and the endpoint application339 are fully AUDITED, and equations(6),(7) of335 hold below the reference radius.
Method: Trace independent authorship and the integration interval in the standalone proofs; compare the preliminary T2 notes with the frozen complete-review record.
Result and verdict: REFUTED as those broader statements. The independent audit of Opus R2/R3 is CONFIRMED, as is the exact third coefficient algebra, but the new third-cutoff analytic application is OPEN independent review.339 is conditional on that application and335. Equations(6),(7) hold for r>=R0; no below-radius claim is made. S1 supplies central oddness. The next residual gap is exactly116183978028673/4076476460239181; constants remain uncomputed. The published angular floors each use one unnecessary unit of slack, not an analytic loss.
Evidence: audit/theory_audit/research_code/finite_tail_surgery/REVIEW_STATUS.md SHA256 6cd218ad6c621cedb2e0ca02b44442cc2d859f2fc2d05ea0a3fa2019f94469ed; audit/theory_audit/research_code/moment_resolved_tail/DOMAIN_ADDENDUM.md SHA256 ae54aec0c3bc9dcaca2995e0534126df3af4bbc0150a4231b75f388168a3afd2; frozen preliminary review SHA256 0f4636c5492a58b79c38dee281ff300c271d75eefa5fd66be976eb6c8a728b9d.

## T4-345: Candidate 018 whole-plane necessary L2 distance

Date: 2026-10-29T08:20:33.308045+00:00.
Claim: Every real S1 L2 stationary correction of the fixed-c exact rational reference C1-N1-018-legqs25-cont12 has norm greater than 82791289602803/50000000000000000.
Method: Reconstruct all 360 density and 360 stream polar terms independently from the raw generators; check them against the independently accepted point values. Integrate all 63 complete moment groups by exact rational CRT and direct Arb hypergeometric evaluation at 2048 bits, independently of the peer's recurrence. Reproduce both pairings, both norms, the complete gradient critical-point certificate and the exact quadratic root.
Result and verdict: CONFIRMED under the explicit canonical-velocity and stationary weak-equation hypotheses of PROOF.md. The radius is in (0.0016558257920560614,0.0016558257920560616), strictly above the frozen rational floor and 25/54684. Thus 018 is excluded from every registered scalar and original graded L2-distance budget. This is a whole-plane necessary condition; no origin normalization, dyadic exclusion or existence claim is inferred. All eight peer scalar comparisons overlap. Runtime 130.30133342789486 seconds, completed 2026-10-29T08:19:13.757242+00:00.
Evidence: audit record candidate018_weak, proof SHA256 24ca0f96efd2739947ffd7e96ab0fee6e8842945b7a668ac3eabd53ff122b97f; checker SHA256 d4ff89d8c50667e3c7f8e6fe5c27df8225e62d3bd264cc6f4417f5948736b8a5; result SHA256 a11275021dc52bd5721c48bb3916cbba021435aa4f228792feb58dba36d102bc; all raw and dependency hashes are recorded in that result.

## T4-346: Candidate 018 exact origin normalization

Date: 2026-10-29T08:22:45.622952+00:00.
Claim: The candidate 018 canonical potential has c + partial_y u2(0) = 1 and a positive density slope, with the exact origin fields stated by N4.
Method: Independent quartic Taylor expansion of every raw generator that can contribute at the origin. Generalized rational binomial identities give the three quartic coefficients without using either candidate field implementation. Differentiate these finite polynomials exactly.
Result and verdict: CONFIRMED. Exactly 24 generators and 24 summands contribute. All four N4 rational fields agree, c + strain = 1 exactly, and the density slope lies in (10.3106636255510647,10.3106636255510648). All remaining generators vanish to order at least six. Runtime 0.05404203059151769 seconds, completed 2026-10-29T08:21:53.559343+00:00. The global canonical-potential identification remains the existing audited dependency; no stationary solution is claimed.
Evidence: audit record candidate018_origin, proof SHA256 be525cd326284b48e6ad11dade0ae09bf0ab7c3f7339f0d4917b41f2fde4db66; code SHA256 8a105ab01d0c272d74d64709feb67aee8802252f8fac19c9ac39f39faa2580c4; result SHA256 290f8b03a4f0d84c8a28e13d6ad26970097807b5eba27944fa15ad5d28f13845.

## T4-347: Theory draft 21 update and all 48 ratios

Date: 2026-10-29T08:24:20.054502+00:00.
Claim: The new 018 statuses, finite-tail review labels and displayed ratios of draft 21 agree with the audit record, and its point gaps cover every registered budget.
Method: Read the entire diff from audited draft 17, trace all changed theorem/status claims, and recompute the 42 table ratios plus six new prose ratios by exact arithmetic.
Result and verdict: CONFIRMED the theorem/status updates and all 48 conservative ratios. The n23 arithmetic does not accept its still-open certificate. REFUTED only the overbroad phrase that 018 has point gaps for every registered budget: point audit 342 covers six named scalar balls and the original graded bound; the wider exclusion follows instead from full-plane distance 345. Matrix-v79 OPEN labels are explicitly historical. The exact origin conditions are now independently confirmed in346. Runtime 0.002031404059380293 seconds, completed 2026-10-29T08:23:31.811110+00:00.
Evidence: audit/theory_audit/research_code/theory_final_draft15_audit/DRAFT21_ADDENDUM.md SHA256 0524caf679e21a010261f4e07c229eaea27ee827ba33b157fc8e2cc74da9bb19; frozen draft21 SHA256 5021587e70c4095e0598bbd0c71d2cd9e98c963022b2378bba9f4c415ef36bec; result SHA256 43a17fcf9017e40e1a6900fef31ed56f31b906082df3f4333af012849b1fd883.

## T4-348: Simultaneous-scale potential and density dimension

Date: 2026-10-29T08:27:42.325750+00:00.
Claim: The abstract old 1922-dimensional potential basis plus both 252-generator radius-25 and radius-50 extensions has potential and density dimensions exactly 2426 (N4-274).
Method: Read the complete proof and checker. Independently prove angular and fractional-branch separation, cancellation at the two distinct auxiliary poles, and density injectivity from the fourth-derivative decay. Reconstruct the abstract shape list and all 168 rational Laurent coefficients, comparing them with the independently accepted single-scale records and N4's new record. Check both cross-pole values and all inherited input hashes.
Result and verdict: CONFIRMED. All 2426 shapes are distinct and agree with the abstract list; the 168 nonzero Laurent coefficients agree exactly. No term from the other scale can cancel the highest pole. The old rank and the audited density-injectivity argument supply the stated dependencies. Actual mixed-candidate shape matching remains OPEN until a snapshot exists. No conditioning, optimizer floor, inverse or existence claim follows. Runtime 0.04942703014239669 seconds, completed 2026-10-29T08:26:42.333019+00:00.
Evidence: audit record joint_scaled_rank_audit, proof SHA256 6ce362e830f86f488829060d820478a2bd7232d65da61eb5decd08181ee22433; checker SHA256 86ec63b08f67dd3b889e3b649426d28d5c4f6585b1d443efbabef51b7aedde8a; result SHA256 0d167869fb0d49e68a7cc2bcbc2a29420629eccf43f3c5c57651d73129755aa9; frozen N4 proof SHA256 2bed77f97d0333c6fd0e9241657522db9d31ad6e78603f34395407bd154d2c0a; dependency checks in verification/dependency_binding.json.

## T4-349: Candidate 018 companion n23 whole-plane distance

Date: 2026-10-29T08:35:06.731785+00:00.
Claim: The complete N4-272 n23 K2400 certificate gives a necessary fixed-c S1 L2 stationary-correction norm greater than 41500501394941/31250000000000000.
Method: Reconstruct all 360 density and stream polar terms, compare the actual point fields, retain every angular interaction, and integrate all 61 complete moment groups with exact CRT replay and direct Arb hypergeometric evaluation. Recheck all gradient critical amplitudes and eight peer scalars. The unchanged backend uses the previously passed fixtures.
Result and verdict: CONFIRMED under the explicit stationary weak-equation and canonical-velocity hypotheses of PROOF.md. Both pairings and all comparisons overlap, minimum moment accuracy1926 bits. Radius in(0.0013280160446381137,0.0013280160446381139). This is weaker than345 and changes no exclusion. Runtime128.82126134028658seconds, completed2026-10-29T08:34:03.873008+00:00.
Evidence: audit/theory_audit/research_code/candidate018_weak/N23_ADDENDUM.md SHA256 9de330044816bc79668d59fa3d2c386c0074ab118b0ad90c170df655adf8837d; result SHA256 f7b5b8f6d541f98310e51233ae74d1d0e6660f7c919f2f43207469e9c9bd4e9f; peer SHA256 d4f6f2f5d8f63805c4098e1a1a0c4949cc413605ef642878bf1c9b84994dbc41; raw SHA256 1c99bf4d77865f7c576a9ba6c08bc08cf008416a737d4a8626b5799ceb4a85e2.

## T4-350: Independent Opus review of the moment-resolved endpoint theorem accepted

Date: 2026-10-29T08:36:42.799908+00:00.
Claim: T2 the review of T4-335 confirms the complete first-moment velocity estimate, endpoint expansion, faster-decay obstruction and exact angular data of335.
Method: Read the full independent review, code and log; recheck the canonical kernel including its contact term, the region constants, dipole signs by both kernel and Green-function routes, integration domains and exact projected angular data.
Result and verdict: CONFIRMED; T4-335 is AUDITED. The stated r>=R0 endpoint domain remains necessary. The review's R2/R3 additions are audited separately; its FLOAT examples are not certificates. The third-cutoff application and339 remain OPEN independent review. No candidate or existence verdict changes.
Evidence: audit/theory_audit/research_code/moment_resolved_tail/reviews/T2_335/ACCEPTANCE.md SHA256 3dbf0397cc5e5275e8d08ebd22b464605dda4f66b2e7f05ba34c5adf10bf40d8; frozen review SHA256 090b6e0f14decffd5e0b7e98d56db3ce009b559a1eab8f2f47eb0a045c853001; code SHA256 24eb86ccce6812d2d48c3971bffdfd94041922230cee8a30edbf55542cc51846; output SHA256 d27e40d756e80a79605b2d28edd5accf89b32a704d973073d25d750ec677535f; log SHA256 ba6bb95af51619bac1dd65392c4d5d0a43470335a9579dac86d15b4232ca2b07.

## T4-351: Endpoint moment bound, two-budget inequality and its certified reach

Date: 2026-10-29T08:38:14.450128+00:00.
Claim: T2 the review of T4-335 R2/R3 give an explicit first-moment bound, a weighted-C1 necessary budget and a two-parameter L2 closure inequality; their current constants cannot yield a useful L2 exclusion at the registered budgets.
Method: Independently integrate the moment majorant, apply the angular triangle inequality to the audited endpoint expansion, and bound the support and size of the positive-part integral. Reconstruct the exact angular projection from JSON and replace the peer's FLOAT gradient maximum by the exact point value Theta'(0).
Result and verdict: CONFIRMED under all endpoint hypotheses. |m|<=mu H with mu<5.04423, H>33917 for each angular pair, and CI as stated in PROOF.md. With E>133, G>Theta'(0)>28.5227 and B<85020, the square root of CI's right side is strictly below928/10^13=9.28e-11, uniformly in admissible H and R1. The computed conservative upper expression is9.27594793267544e-11. This bounds the reach of this test, not the true distance or norm of a correction. No actual reference is asserted to satisfy the endpoint hypotheses here. Runtime0.0033998130820691586seconds, completed2026-10-29T08:37:23.693201+00:00.
Evidence: audit record endpoint_closure_inequality, proof SHA256 85e01f1bfab61b078138120f3ec6011b76ace5cd45d7436d7cdd5ca35251fc34; result SHA256 37310c7df2390e1a749d70dbe4b0edafe05be19aff63c7b1e5985abba9ccb439; source review SHA256 090b6e0f14decffd5e0b7e98d56db3ce009b559a1eab8f2f47eb0a045c853001.

T4-351 notation correction: the chained relation in its result is G >= Theta'(0) > 28.5227. Equality in the first comparison is allowed. The standalone proof and numeric certificate use exactly this non-strict first comparison; the strict final cap is unchanged.

## T4-352: Theory v06 dryrun and long-report draft23

Date: 2026-10-29T08:41:54.150962+00:00.
Claim: The unpublished v06 exchange draft and long-report draft23 correctly state the new cutoffs, sectors, candidate exclusions and budget ratios.
Method: Read all625 lines of v06 and every321-line change from draft21 to draft23; trace each new claim to the independent ledger. Check48 v06 and51 draft23 displayed/prose ratios by exact rational arithmetic.
Result and verdict: CONFIRMED the mathematical changes under their stated hypotheses and the narrow declared-analytic-objective meaning of held-out. Every ratio is conservative. Draft23 has repaired the point-test scope and lists both339 dependencies. REFUTED the completeness of v06's339 dependency list in section2.1 and5.5(f): it must include the third-cutoff application in338 as well as335.335 is now AUDITED350; the new third-cutoff application remains OPEN. These checks do not publish v06 or accept later unseen edits.
Evidence: audit record theory_v06_draft_audit, proof SHA256 a6829cafb35c25e8317d87e83afd55cebfef96520bcbef5d37d2be37a30f680d; v06 source f7e06f9933ba02db50f9856c72b4e54deb499431251645012a4caf8d25202c97; draft23 source 031bbfd75061053247a1d959353cfea55f956f66eb5a39a8fe82a020b60794ae; v06 result 6c6862bcbd5973b8244f972bf3ddf1b43a275ac34e1906ec19a61abb684ad79d; draft23 result 8cc5c1f6faffef8d13c77d3a773f9db03a337c9e6568c628b4b7b56cf10e23ef. Exact checks completed 2026-10-29T08:39:18.611326+00:00 and 2026-10-29T08:41:23.640422+00:00.

## T4-353: Candidate019 independent local point exclusions

Date: 2026-10-29T08:43:01.521227+00:00.
Claim: Every named scalar point-test gap and the original uniform graded gap are positive.
Method: Exact polar Taylor differentiation through order4 and outward1024-bit Arb evaluation, independently of Cartesian jets.
Result and verdict: CONFIRMED. Residual in(0.08974395121409148,0.08974395121409150), uniform graded gap>0.06934033757930145; all eight fields and six scalar rows agree. This is the six tested scalar balls and original graded family, not every registered L2 budget. Runtime1.83501454629004seconds; completed2026-10-29T08:42:01.985150+00:00.
Evidence: audit record candidate019_point, proof SHA256 317cf331af042374f291699530e8806c2ed7f23b8a640eeeec1c656b13851a81; result SHA256 f7d5dcaa384e4bd3a4aa89662e70da945777b41cb9c64b69a1e2d08052d59229; raw SHA256 ca0fffafe2aa7ea3c6049e0b5a83651113451087027b0783800c046ae170d419.

## T4-354: Candidate019 exact origin normalization

Date: 2026-10-29T08:43:01.521227+00:00.
Claim: The canonical potential satisfies c+partial_y u2(0)=1 and positive density slope.
Method: Independent exact quartic Taylor expansion of every raw generator capable of contributing to the origin jet.
Result and verdict: CONFIRMED. All four rational origin fields agree;24 contributing generators and24 summands. Density slope in(10.3114890201060617,10.3114890201060618). This does not assert stationarity away from the origin. Runtime0.045879343058913946seconds; completed2026-10-29T08:42:02.123266+00:00.
Evidence: audit record candidate019_origin, proof SHA256 619e176a880f3e10f06c7acaae1468dea0798742dee42611db632f6e70f723ec; result SHA256 4e8740e93e809b716c15d83a6194049b6a9b80901d53aabfcbc86fad408acd82; raw SHA256 ca0fffafe2aa7ea3c6049e0b5a83651113451087027b0783800c046ae170d419.

## T4-355: Candidate019 complete far-field sector prefix

Date: 2026-10-29T08:43:01.521227+00:00.
Claim: The sixteen retained sectors above-7/2, eleven zeros and first four leading profiles are as published.
Method: Independent homogeneous expansion of all2174 generators, exact Poisson identities and complete nonlinear coefficient convolution.
Result and verdict: CONFIRMED. All13 common N4 coefficient maps and norms agree, all16 N1 statuses agree, and the first four profiles equal007. Nonzero sectors are(4,1),(9,0),(5,1),(1,2),(10,0);252 radius50 Q4 generators enter only at L>=4. No residual upper bound or inverse follows. Runtime22.206904522143304seconds; completed2026-10-29T08:42:24.363314+00:00.
Evidence: audit record candidate019_sectors, proof SHA256 76586cc3543314bb8e68442c6bf576f4bcae18d42216a7af45ba9f3482815eec; result SHA256 82d832328420ef2e134f7d4908cff2ae285751786b5a4c5bfc802fb6f30bdd29; raw SHA256 ca0fffafe2aa7ea3c6049e0b5a83651113451087027b0783800c046ae170d419.

## T4-356: H12 numerical report repairs partially accepted

Date: 2026-10-29T08:45:16.532720+00:00.
Claim: The223-line revision repairs all T4-340 inferences and scope issues.
Method: Read the complete revision and every marked repair against the standalone counterexamples. Independently prove the angular-projection Cauchy-Schwarz bound to test a new sentence.
Result and verdict: CONFIRMED calibration, index, summary-scope, design-probe, exact-Newton, no-bracket and plateau-OPEN repairs. REFUTED completeness: point-test/all-ball scope survives at lines80-81,96-97, density19to31 at169, and all-MID32 at122. Old-span unreachability remains unsupported at17-18,208-210. REFUTED the new line172 denial of any angular-mass lower bound: a certified pairing in that band gives ||Pi_B F||2>=|<F,phi>|/||phi||2. It still gives no upper bound or proof of an increase between references. Exact feasible objective trials give upper, not lower, bounds on the infimum; FLOAT values need enclosure. No exclusion reverses.
Evidence: audit/theory_audit/research_code/numerics_final_h12_audit/REPAIRS_REVIEW.md SHA256 b98c0cd778863f73f9bf4c967bf7075f3f5975fbab30aa1ffa1082ffaae939cd; source c6df1c17eb254a7d173cbefbcbe235cf96569ee13802e792a28e69a46b95705b; verification/repairs_manifest.json 65262dc08cd25ef6b5a67086b16ffc7f3df5b8fa801d0632778cfefdf869c447. No computation was needed for these analytic checks.

## T4-357: Candidate019 independent whole-plane distance

Date: 2026-10-29T08:51:27.691125+00:00.
Claim: N4-282's complete n19 K1800 certificate gives a necessary fixed-c S1 L2 stationary-correction norm greater than1661806967193251/10^18.
Method: Independently reconstruct all360 density and360 stream polar terms, compare six physical point fields, retain every angular interaction and integrate all63 moment groups by exact CRT replay and direct Arb hypergeometric evaluation. Recheck all gradient critical points and all eight peer scalars.
Result and verdict: CONFIRMED under PROOF.md's stationary weak-equation and canonical-velocity hypotheses. Both pairings and all comparisons agree, minimum moment accuracy1973 bits. Radius in(0.0016618069671932526,0.0016618069671932527), strictly above the declared rational floor. This excludes all registered scalar and original graded balls, including the larger registered L2 budgets not covered by the six point tests. It supplies neither a dyadic exclusion nor existence. Runtime128.98341427603737seconds, completed2026-10-29T08:48:14.463092+00:00.
Evidence: audit record candidate019_weak, proof SHA256 ad703a8e8cd2bd0ffdaf0d32359836049f1754a8af4c0fe00b64a1f81aec2f7a; result SHA256 897c46d49b6d79ebb3a597052a5414af5e4d57f58c52409b10fdbca68a7c3428; peer SHA256 9803dd5455429ebeb624b60688bd38bc92840b2514935dda4ebd64bc2867f9b2; raw SHA256 ca0fffafe2aa7ea3c6049e0b5a83651113451087027b0783800c046ae170d419. The first run completed its numerical assertions but failed hashing a missing inherited documentation file; its log is retained. This acceptance uses the complete successful rerun only.

## T4-358: Draft24, v06 second preview and the one-reference closure record

Date: 2026-10-29T08:53:25.428900+00:00.
Claim: The new endpoint statement, CI limitation, one-reference record, inverse-constant calculation and019 ratios are valid.
Method: Read every change from the previously audited sources; compare the full endpoint hypotheses with335 and351 and the closure hypotheses with the audited sharpw proof. Independently check54 table/prose ratios in each source, all ball inequalities and the required commutator constant.
Result and verdict: CONFIRMED the endpoint statements, repaired third-cutoff dependency, conditional closure constants, and all108 ratio comparisons. Within the same family formula and fixed cU=8/5,w2=2^20, overcoming007 requires C'<775390625/2554506927217<3.04e-4. The exact rate is63092119/405000000, self-map slack7/1557000000, contraction<0.0137200. The inherited6.4226 inverse bound is valid using the full exact rate. REFUTED the verification-status claim in v06 section3 that007 has all checks except H6 and NC-T-DIST: its own correct table leaves(A),(B0n),H3,H4 unchecked. The unqualified prohibition on any mode-band inference should be narrowed: certified finite pairings give band-mass lower bounds, not upper bounds or ordering between candidates.019 OPEN labels are stale after353-355,357, not an error at the cited historical cutoff. No exclusion reverses.
Evidence: audit/theory_audit/research_code/theory_v06_draft_audit/DRAFT24_ADDENDUM.md SHA256 0fa13589f9fe858b82c22c81a93f6c98c754836c0e052c770b095d4fefb5e7e5; result SHA256 76d02ddff177a43e4139eca158d70ddb8868656931062f9b678c89c813fbed9c; draft24 source SHA256 5a6419c1671826ff8486e27dbb7721a4a1b1819d8b836d6db3579875b1589e84; v06 preview2 SHA256 e873cb3ab5558243b83ea507ec45c61ae46ffe012b31ff567a755f7ac6eb57d1. Exact and Arb checks completed2026-10-29T08:52:56.298238+00:00, elapsed0.005802589934319258seconds.

## T4-359: Annular moment adjustment with exact interior screening

Date: 2026-10-29T08:57:49.439752+00:00.
Claim: A prescribed first moment m can be realized by a compact smooth S1 annular correction h_R with X(h_R)=O(|m|R^-2), zero density and velocity on r<R, and exterior velocity m(cos3theta,sin3theta)/(pi r^3). Its H_q cost diverges for q<-3, and it changes an endpoint residual only by(m/pi)P.
Method: Solve the mode1 radial Poisson equation exactly, differentiate its exterior dipole, use the audited raw-to-fractional inequality, and scale all four residual terms. The standalone proof gives explicit bump-dependent constants and exact reference-growth hypotheses. Independently check the Cartesian derivatives, radial Green equation, divergence, polar components and rational scaling exponents.
Result and verdict: CONFIRMED the finite symbolic identities; OPEN the new analytic construction pending independent Opus review. The proposed result would prove that the first moment and H_q are not controlled by the present high norm, and would realize the endpoint moment direction at arbitrarily small cost while preserving the interior. It would not remove the orthogonal endpoint component or prove existence. Symbolic check completed2026-10-29T08:57:24.420222+00:00 in0.2943878239020705seconds.
Evidence: audit record annular_moment_adjustment, proof SHA256 0b3944af5bcc7c176ecf5036b822894dfc0a06d49da1306de904ced2938f6e35; result SHA256 c38c7a44b24833b59cba53371523d04fc78f74be8c82bf9b12ca92a3f0ae9915; imported audited inequality SHA256 8ca3bb460727294595087e114935f564bff5605b00b5432c59cfc1bb0ecd6734.

## T4-360: Candidate020 independent polar point test

Date: 2026-10-29T09:01:17.277939+00:00.
Claim: The stated candidate-specific necessary conditions and algebraic identities hold for raw SHAbddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf.
Method: Independent fourth-order radial Taylor reconstruction of all2426 raw generators at(1/10,73/100), separate from N4 Cartesian differentiation.
Result and verdict: CONFIRMED. All eight point fields and six named scalar-ball gaps agree; the uniform original-graded gap is strictly positive. These six point tests do not cover every larger registered L2 budget. Runtime2.0774783953092992seconds, completed2026-10-29T09:00:18.943228+00:00.
Evidence: audit record candidate020_point, proof SHA256 2a58cd13b9360da79759f84f0f33e30bfa44df460e97fd8704b0771f4a822163; result SHA256 3ac63d5428117f75a56ac2325bdb872c9ed6de88ed7341d0edd99263c3b91f1d.

## T4-361: Candidate020 exact origin normalization

Date: 2026-10-29T09:01:17.277939+00:00.
Claim: The stated candidate-specific necessary conditions and algebraic identities hold for raw SHAbddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf.
Method: Exact quartic Taylor expansion, retaining every raw generator that can contribute.
Result and verdict: CONFIRMED. All four rational fields agree, c+partial_y u2(0)=1 and partial_y rho(0)>0. No stationarity away from zero follows. Runtime0.04656153963878751seconds, completed2026-10-29T09:00:19.081745+00:00.
Evidence: audit record candidate020_origin, proof SHA256 594c589cbc39a23ab7d24d0a15296b7403b45af9d79ab5d4be5897b2c30dde11; result SHA256 ff8a3abe79a03cd8733c941c5bf0e26601fe68a25fb28f8c11a8397028292b9d.

## T4-362: Candidate020 complete far-field prefix

Date: 2026-10-29T09:01:17.277939+00:00.
Claim: The stated candidate-specific necessary conditions and algebraic identities hold for raw SHAbddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf.
Method: Independent exact homogeneous expansion, Poisson identity and every nonlinear interaction at exponents at least-7/2.
Result and verdict: CONFIRMED. All13 common N4 coefficient maps and norms agree; all16 N1 statuses agree. Eleven zeros and five nonzero sectors(4,1),(9,0),(5,1),(1,2),(10,0); first four leading profiles equal007. Both252-function scaled blocks have Q4 and enter only at L>=4. No residual upper bound or inverse follows. Runtime22.241688318084925seconds, completed2026-10-29T09:00:41.356635+00:00.
Evidence: audit record candidate020_sectors, proof SHA256 a2ed16f6b0c92291f9d91ef92a71f0e5d4066019a738ea4b56216fcd37333f7c; result SHA256 61ea2602fbc83881c04ad26662b7dbe18e756b2c7f7c424ca39b585cf2bcfc76.

## T4-363: Candidate020 independent complete mixed-scale weak distance

Date: 2026-10-29T09:04:16.915703+00:00.
Claim: For the fixed-c S1 stationary-correction hypotheses in PROOF.md, the complete n19 K1800 probe forces ||h||2>231921834680339/125000000000000000.
Method: Independently reconstruct every polar density/stream field, calibrate the R1 coefficients, exercise six scalar fixtures at poles624 and2499, retain every angular interaction and integrate every moment by exact CRT replay and direct hypergeometric evaluation. Recheck the three gradient critical values and all eight independent peer scalars.
Result and verdict: CONFIRMED. Both actual scales occur jointly. Six physical point fields and all peer quantities agree. 63 complete moment groups, minimum1937 bits, density/stream counts360/360, M pairs1560, C ordered pairs5778. Radius in(0.0018553746774427130,0.0018553746774427131), strict floor0.00185537467744271208, above every registered scalar and original-graded budget. No dyadic exclusion, maximum over probes, ordering of actual distances, inverse or existence follows. Runtime149.09255622606725seconds, completed2026-10-29T09:03:46.466132+00:00.
Evidence: PROOF.md SHA256 5c1c8cb5ec816d3f70bd803a90ee8b87e64c1e6057c879b9f1a97dfdf4e94612; result SHA256 5e10d30772f536111793bf56d29a5c8247e1bc0456c9deb4dd1cb512261a9899; peer SHA256 7add6b088e45d002f7e14f9632c4a0f5574cd7395467a55bc3a51c210af1f981; raw SHAbddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf. Six mixed-scale fixtures were actually run, with no skip-fixtures option.

## T4-364: Candidate020 actual dimension and current objective-span binding

Date: 2026-10-29T09:04:16.915703+00:00.
Claim: The actual candidate020 generator space has potential and density dimensions2426, and all26 listed probes lie outside its recorded current67-row analytic objective span.
Method: Compare all2426 raw shapes, in order and as a set, to the accepted abstract T4-348 list, verify the2174-shape parent016 prefix and252 appended R50 tuples, and rehash the accepted theorem inputs. Independently parse the complete launch, metadata and completed log; use sine Fourier orthogonality to prove span separation.
Result and verdict: CONFIRMED at the stated scope. All exact shape, parameter and current objective checks pass. Earlier historical stages are not independently replayed here; the stronger N4 recorded-history claim is retained as a separate source. No rank conditioning, optimizer floor or statistical independence follows. Runtime0.07035068469122052seconds, completed2026-10-29T09:04:16.870272+00:00.
Evidence: audit record candidate020_shapes, proof SHA256 95625beb9d770c93963f0897b3880f72fd7763ae36002122a0d964100ad27820; result SHA256 8fe23ef3b6d21c313efc456130e8819695c035c04b946f049c479b3ebb0f1c4a. No publisher code was executed.

## T4-365: Independent Opus third-cutoff review accepted

Date: 2026-10-29T09:08:15.526816+00:00.
Claim: Sections2 and3 of the third-cutoff proof, including the endpoint application, have complete independent verification.
Method: Read the entire Opus review, match each argument and exact source hash to the retained proof and computations, inspect every main candidate check in its independent result, and separate the review's extra R2-R4 claims.
Result and verdict: CONFIRMED. T4-338's third-cutoff application and T4-339 are now AUDITED. For007,013,014 the third potential, density, stream and remaining endpoint maps agree, and all earlier residual sectors vanish. The application of already audited335 has no remaining proof dependency. This is a weighted asymptotic consequence for the repaired reference, not an L2 exclusion. Extra remainder claims are not accepted here.
Evidence: review SHA256 7a6e46ba809d8285beed063057e7efcf45caf4f57919a6026782485cd9cef03f; result fe640db6b636638d6db3a41136b05668dbe0f1c800b91dada50c24919f1e35fc; acceptance PROOF 4aaadde5158bb7a6243bbbf69b70560bbaaa09c4d8e1965247bc4d9d3b2eab4a; manifest f59cc794673b6b2ea831af4e35b0cc604c64f0f30785081651cb442772b3225b. The independent review's reported computation took499.19844613876194seconds. No computation was rerun for this acceptance.

Erratum to T4-363 decimal prose, recorded 2026-10-29T09:08:15.526816+00:00: the exact fraction231921834680339/125000000000000000 equals0.001855374677442712. The trailing08 in that entry's decimal is a transcription error. The exact fraction, the certificate, handoff165 and all exclusion comparisons are unchanged.

## T4-366: Independent complete-plane Hessian and commutator norms

Date: 2026-10-29T09:10:41.262537+00:00.
Claim: N4-268's complete Hessian energies and structured Hilbert-Schmidt norms for007,016,017 are correct.
Method: Reconstruct raw density through the independent polar field path, differentiate it twice by radial and angular product identities, compare mixed partials exactly, and integrate all135 branch groups by exact CRT and direct hypergeometric evaluation. Compare every group,27 physical derivative values, all component energies and all norm scalars. Calibrate007 against its accepted exact rational energy sums.
Result and verdict: CONFIRMED. Each candidate's45 complete groups agree; minimum accuracy1888bits at2048-bit precision. Ordered mixed derivatives are counted twice. The full-plane kappa values are enclosed near0.7281646801823254273,0.7350536729937207651,0.7290805386289553487 for007,016,017 respectively. Thus016 has kappa<0.735053672993720766 and017 has kappa<0.729080538628955349. These are upper bounds for the structured operator norm by the audited identity, not lower bounds on it. They do not certify global theta or an inverse. The007 Y endpoint-ball regression fails as expected while the exact energy and containing norm ball agree, confirming N4's calibration correction.
Evidence: PROOF SHA256 3553df6f02c23903791ce89a0d94dc0d454713798e98787df2e2839110038263; code d55cdaa8a81f0a0f4feeb3642512fb566044d3dfdab6d10baa564134a17f1fab. Results: [{"candidate": 7, "result_sha256": "51c3ee19294695865dda7e315ac5c1ccc96839b998891b44ce10e0b084c44e3a", "utc": "2026-10-29T09:08:12.899594+00:00", "seconds": 40.27517622895539, "minimum_bits": 1894}, {"candidate": 16, "result_sha256": "579091063afcff541bde0afc90ccecaac3298f2d58af6c7fe3aab4b0f3e14d7c", "utc": "2026-10-29T09:09:00.403984+00:00", "seconds": 47.48149544978514, "minimum_bits": 1888}, {"candidate": 17, "result_sha256": "f93a2d47ad5e30cf604cea46b29be0ba551d33667ae8b79fd91ce3febad831ab", "utc": "2026-10-29T09:09:49.321985+00:00", "seconds": 48.890554558020085, "minimum_bits": 1892}]. No foreign code was executed.

## T4-367: Full radial Hessian partition reproduced independently

Date: 2026-10-29T09:12:49.412041+00:00.
Claim: N4-273's origin, annulus and far-field Hessian energy partition is correct for016 and017.
Method: Reconstruct polar Hessians again, form all45 angular/radial groups per candidate, integrate each primitive at three exact cuts using CRT replay and direct hypergeometric evaluation, and compare all270 primitives with the peer recurrence. Compare the whole-plane primitives with366 and every domain metric and omission ratio. Independently reconstruct the saved Gaussian node selection from frozen publisher source text.
Result and verdict: CONFIRMED. Exact cuts are r0=1/50 and R=4178237423365963/500000000000. All primitive, energy, norm and ratio comparisons pass, minimum1882bits. The full-minus-annulus kappa is0.0012139280127493846... for016 and0.0012238902090590967... for017. The far field supplies more than99.998% of the omitted squared kappa contribution. Exact annulus minus saved FLOAT kappa is approximately-1.62962e-12 and-1.68355e-12 respectively. The FLOAT rule selects416 nodes in13 complete panels; no selected final panel is partial. The nominal rational annulus remains distinct from the FLOAT panel endpoints. No general FLOAT quadrature-error bound, localized Hilbert-Schmidt operator identity, global theta bound or inverse is claimed.
Evidence: PROOF SHA256 2842d293b53500571dabd5e5c7509ebfe146f926ef38e8238b3e3939dead828b; code f410921f8ab20090759a24d9cfe988a4b6289f4e6174fee3ff312ca622c08635; result records [{"candidate": 16, "result_sha256": "37128f86a663b0f5b30b787355b43944d440ad17d2f243ee1631107e3b7e6bb4", "utc": "2026-10-29T09:10:50.181208+00:00", "seconds": 49.90072045521811, "minimum_bits": 1882}, {"candidate": 17, "result_sha256": "78dece4ef64504480e08ff9a7ba46c08e2e8f87a8b1b7459f0b09351e72eb5ea", "utc": "2026-10-29T09:11:39.762756+00:00", "seconds": 49.573810308706015, "minimum_bits": 1886}]. Frozen diagnostic hashes are rechecked. Publisher code was read only as text.

## T4-368: Endpoint reference changes and the next forcing term

Date: 2026-10-29T09:14:38.724769+00:00.
Claim: Opus the review of T4-338 R2-R4 correctly describe dipole shifts, the next retained forcing term, and a fourth cutoff.
Method: Check the entire analytic argument with exact canonical-velocity and weighted-class hypotheses. Independently reconstruct the repaired(10,0) coefficient, project it and the endpoint coefficient away from P, check their rational inner product, and solve/replay the fourth angular potential inverse for007,013,014. Prove its zero first moment by two boundary integrations.
Result and verdict: CONFIRMED the exterior dipole bookkeeping, two-term asymptotic expansion, strictly positive projected inner products, and fourth-cutoff endpoint removal with zero first moment and arbitrarily small L2 cost. The projected cosines agree with Opus, about0.93994. Exterior dipole bookkeeping does not authorize a singular change to a global fixed canonical velocity. The two-term norm is never below its limiting norm, but the actual correction retains a remainder. OPEN a finite-radius bound on the complete remainder or a claim that it is quantitatively dominated by the velocity error; the short sector table does not establish that. The prior9.28e-11 ceiling on what the current CI can prove remains valid and is not contradicted.
Evidence: PROOF SHA256 1e4199089cefe888803b3678b191779b0e242b874c63f348d24136aa53cf45c9; result 59446cc842af664f4b64556a12132a3c2216963160810a14cc4a70380db3265d; code 235fd01ee076a6d33be399c94b48e3240996bbc89b11732e9aa821b63194eb9d. Exact coefficient maps are in data/007_fourth.json,013_fourth.json,014_fourth.json. Completed2026-10-29T09:13:10.465178+00:00, elapsed51.81605864316225seconds. No existence or new whole-plane distance exclusion follows.

## T4-369: Proposed higher angular extension has exact dimension2414

Date: 2026-10-29T09:21:47.817872+00:00.
Claim: N4-294's abstract radius25 extension has independent potentials and densities of dimension2414; its240 additions beyond016 have support in odd modes31 to47 and an actual nonzero mode31 term.
Method: Independently check the complete proof by fractional branch separation, rational poles and harmonic density injectivity. Reconstruct the exact proposed shape list and all180 normalized Legendre numerators by a three-term recurrence; compare every Laurent coefficient,84 old witnesses,36 nonintegrality conditions and the exact origin coefficient.
Result and verdict: CONFIRMED. All exact checks pass. The initial ordered old-prefix assertion stopped before any certificate: the accepted old list and016 list differ by a permutation. The repaired checker verifies the exact1922-element set and the ordered252 new prefix, then the complete proposed list in order. This is documented in DEVELOPMENT.md and the original checker is retained. Actual future candidate identity, conditioning, an inverse and existence remain unproved.
Evidence: PROOF SHA256 dc75e8947550fc116ba767e63554c37267d67e093633c2427fcee444d2fcb305; result b67778e11607769ac6ff5fb90417cd4c90f42b1487e309b7c9e777f137d11c94; peer result fba74577bff755e86fd5d473add67f8a9b91473fb99b48808069b2c48a9bd768. Completed2026-10-29T09:20:55.297102+00:00, elapsed0.12238233583047986seconds. No publisher code was executed.

## T4-370: Independent Opus review of the annular moment theorem accepted

Date: 2026-10-29T09:22:32.450387+00:00.
Claim: T4-359's exact screening, prescribed moment, high-norm and residual estimates have complete independent verification.
Method: Read the entire Opus review, compare every analytic step with the retained original proof, verify all23 A-checks and exact source hashes, and separate FLOAT bump diagnostics and new remarks from the main theorem.
Result and verdict: CONFIRMED. T4-359 is AUDITED. The residual endpoint expansion holds past max(2R,R_e), with its remainder constant independent of R. Weighted-moment unboundedness and vanishing X cost hold as stated. The imported fractional comparison remains an explicit accepted dependency. No FLOAT quadrature or bump constant is needed for this verdict. New R2-R4 claims are separate.
Evidence: review SHA256 805342c1fea11d5e833c1902bc7100ea960f85e36a9cf57a3cf452c4a0a99de0; reviewer result 9afafd031495b5cc84777b1a0cf476a678253a418380a53d7a49092593b52635; acceptance PROOF 12c7b456550a44e4394d465e3047a9c3ff00f68f18b6a06af55d4275b97997ae; manifest dc3fa568f84718abc4c25df244ad4d6e120efe1cc788bb350e5fb6397ac53892. Reviewer computation30.352751058992seconds; no new numerical calculation for this acceptance.

## T4-371: Weighted-budget moment interpolation and endpoint projection

Date: 2026-10-29T09:25:09.365845+00:00.
Claim: the review of T4-359 R2 gives a valid Holder estimate for the first moment, with optimal exponent on bounded Hq sets; its R3 minimizing endpoint moment and R4 interior harmonic description are correct.
Method: Independently split the absolute moment integral on a disk and its exterior, optimize the exact bound, and test exponent optimality with the audited screened annular family normalized to bounded Hq. Recompute all three rational endpoint projections and Arb moment values; derive the complete mode-n Green formula.
Result and verdict: CONFIRMED the interpolation bound and exponent optimality at the peer's stated range -5<q<-3 (the same proof needs only q<-3), the endpoint minimizing moment and the interior harmonic formulas. At qstar, theta=0.1828767679031661323... and Csplit=9.4238258909662014.... This controls a moment only when both L2 and a weighted amplitude budget are supplied. The derivative-weighted space remains stronger than the amplitude hypothesis. R3's numerical bump costs remain FLOAT. OPEN the implication from its drift-term comparison to the complete annular residual change for every R: the other terms can cancel and need estimates. No existing candidate/ball exclusion changes.
Evidence: PROOF SHA256 c6651df9d9f45984faa0e7bbe7eb8e1111cab9f183ca84ead312bf86fbd75ba9; result a6877651a22621e45850d14fee78ea49723ed647e46e0db6cd12530a6cba02a5; runtime0.011196671985089779seconds, completed2026-10-29T09:24:09.374347+00:00. Conditional H bounds in that file refer only to the exact beta values printed there; the rounded scalar beta is not asserted to cover an entire framework family.

## T4-372: Sharp homogeneous-amplitude moment inequality proposed

Date: 2026-10-29T09:26:32.746352+00:00.
Claim: For d>0, theta=d/(d+2), nu=2(d+2)/(d+4), C0=(d+4)integral|sin phi|^nu/[4(d+2)], every real L2 density with ||h||2<=beta and |h|<=H r^(-d-3) obeys |integral y h|<=((d+2)/d)C0^(1-theta/2) beta^theta H^(1-theta), with optimal constant in this amplitude class.
Method: Write the complete proof before code. Compute the exact L2 norm and first moment of sign(y)min(lambda|y|,H r^(-d-3)); use pointwise concavity of y t-t^2/(2lambda) to prove optimality. Verify all rational radial exponents and factors, the gamma-function angular integral and four extremizer norm/equality calibrations in Arb.
Result and verdict: OPEN independent Opus review of the new sharp theorem. All arithmetic checks pass. At the campaign d, Csharp=9.15513474115363927..., ratio0.97148810335406... to T4-371's split constant. The weighted C1 class inherits the inequality through its amplitude bound, but sharpness of the constant is not claimed there: the extremizer has an uncontrolled weighted gradient. No absent weighted budget, inverse or solution is supplied.
Evidence: PROOF SHA256 6283be5d859389d7da9efa3e3d46a20ec31d8d6687bb0ec06e77919d88c26174; result cd50a52f7cc97a3ac28d46ed7d8ec6dcd38fc28e9a63ebdbcdc71463b0a61ba9; completed2026-10-29T09:26:07.089952+00:00, elapsed0.0019504749216139317seconds. Independent review requested through handoff172.

## T4-373: Published theory_v06 and R1-037 review audit

Date: 2026-10-29T09:31:18.884140+00:00.
Claim: The published theory contract incorporates the accepted closure constants, candidate exclusions and tail results without changing their scope; R1-037's additional claims follow from359.
Method: Read all988 published lines, compare the new status records and hypotheses with the accepted proofs, check all51 table ratios and closure constants, and derive an exact scaled-generator counterexample. Review all of R1-037, including its new remarks. Use reverse triangle inequality and compact-support integration by parts for the complete annular residual change.
Result and verdict: CONFIRMED the closure inequalities, corrected unchecked007 hypotheses, endpoint dependencies and exclusion scope through020, and all51 ratios. CONFIRMED R1-037's main359 review and remarks(a)-(c), including no bounded embedding from the current X norm into Hq for any q<-1. REFUTED the publication's scaled-block index l>=4: the correct descendant index is q>=4, with a nonzero density example at(l,q)=(2,4). REFUTED R1-037(d)'s O(R^(gamma-3)) for the complete residual change: for fixed nonzero moment and gamma<1, its norm is asymptotic to |m|Ac R^-2, Ac>= (c+1)||f||2>0, with the explicit smaller error of PROOF equation(1). This does not validate a lower bound at every finite radius without background estimates. The specialized2.839272409e-6 annular bound remains valid only for globally H2 corrections supported20<=r<=32 with sine frequencies>=19; the general family ceiling is2.84957773827575...e-6. The post-launch021/022 declaration needs the coordinator's provenance qualification. No candidate exclusion changes.
Evidence: PROOF SHA256 8974cb567d6246f737cff5240b63db3553e341b397f6159b463b4d4f97fe44b7; result c8feeb98cf62aff8404bf8e21187d1f8dd22db418a5db1f27044960e9ae73570; frozen publication493549a9b49ac3eb0fd2c115c90c4ac8e5e9513305c38eb3f41598c31801b6bb; R1-037 d25fa09bf5783e9a55b10a2a6057e70747cf61750be3f576d3eed0d7ba70eea4. Arithmetic completed2026-10-29T09:30:47.223132+00:00, elapsed0.010572116356343031seconds. THEORY_FINAL and NUMERICS_FINAL copies are separate snapshots, not certified by this entry.

## T4-374: Numerical report revision after theory_v06

Date: 2026-10-29T09:37:20.188202+00:00.
Claim: The complete197-line NUMERICS_FINAL revision consistently states the accepted certificates, scalar budgets and conclusions of its trials.
Method: Freeze the complete source2aba9267..., read every line, compare accepted certificates and previous counterexamples, derive full-tensor angular exactness in polar coordinates, and verify all relevant interval ratios and rounding with hash-bound accepted inputs.
Result and verdict: CONFIRMED repaired scalar/original-graded exclusions through020 except011, restricted dyadic scope and the correct distinctions about finite probes, calibration and Newton diagnostics. REFUTED unrestricted use of the specialized annular2.839272409e-6 ceiling; use2.8496e-6, giving016 ratio>515.9, about516. REFUTED upward rounding of the specified017 n23 certificate to0.001068502322; safe floor0.001068502321536437. REFUTED blanket point-gap/radius descriptions: accepted sharpw point ratios007/009 are4.558 and3.048; radii are not all2^-14 to2^-16. REFUTED the retained causal deductions from finite trials and inconsistent020 summaries (small-radius reported ratio725/19; mid-field example relative increase71/272). No exclusion changes. The complete tensor angular rule N>=2M+2 follows by polar invariance; individual derivative squares need N>=2M+3 by the componentwise bandwidth argument. Actual180 is sufficient for both. This full-tensor sharpening is offered for independent review. Missing background hypotheses, true optima and existence closure remain OPEN.
Evidence: PROOF SHA256 23fd6bf89d68be46c1635d01205a7b620afd797a6029b353ebbf1f78778b59e4; result 0e15f5158f506c1e647daa13133eefea5044fd63ff3e7fd9c1d197f9e55a971b; completed2026-10-29T09:36:42.956985+00:00, elapsed0.06026590662077069seconds,768-bit interval checks and exact symbolic identities. Eleven frozen dependencies verified. The initial draft's>516 ratio was rejected and corrected before publication, as logged in verification/development.md.

## T4-375: The endpoint tail forces a stronger weighted gradient budget

Date: 2026-10-29T09:43:22.056166+00:00.
Claim: Uniform convergence of r^(-q)h to a C1 angular profile, together with a weighted C1 bound, forces H_q >= sup sqrt(q^2 b^2+b'^2); eliminating the unknown first moment in this gradient norm strengthens the upper bound on what the existing endpoint CI can certify.
Method: Write a full proof before code. Use uniform convergence of rescalings and their local Lipschitz bounds, without differentiating the asymptotic remainder. Reconstruct the exact weighted angular projection independently, verify orthogonality and its Poincare comparison, and evaluate all constants in768-bit Arb against hash-bound accepted angular inputs.
Result and verdict: OPEN independent Opus review of the new analytic theorem. All exact and directed checks pass. For the three-cutoff007/013/014 endpoint data, H_q>328627 and the current CI can reach at most3.752e-16; its separation radius exceeds149800000. Hypothetical E=1 gives a cap below.00015411. To reach the original graded ceiling, an effective E below.81966 would be necessary; it is not sufficient. The formula keeps all endpoint hypotheses, including finite H_q, and does not supply its missing upper budget, a PDE inverse or an existence result.
Evidence: PROOF SHA256 ce8e8db2dc4ce001136d4e9324ce07fd4beb77732744cad351ee7e17675a2aa8; result 5e29af4997b8de34fe53366cc3e86d0f529915bc2e2daaa66f755f28ad6e45fb; summary comparison 4f63b11585a409d203eac81bac0a661d7fbe5f4a086af733a0879577c8fe86e2. Computation completed2026-10-29T09:42:25.375282+00:00, elapsed0.009400682989507914seconds. Independent review requested from the T2 theory worker in handoff175.

## T4-376: Full-tensor angular theorem independently reviewed

Date: 2026-10-29T09:45:16.001280+00:00.
Claim: N4-307 independently verifies the complete angular sharpening of T4-374 Section5.
Method: Read its complete proof and code, check every retained source hash and all12 grouped checks, and inspect the exact168 cyclotomic moments including the first alias. Verify C6 regularity suffices for the specified derivatives and retain exact-arithmetic scope.
Result and verdict: CONFIRMED. T4-374 Section5 is independently reviewed; M79 requires sufficient160 nodes for invariant tensor squares,161 for arbitrary separate Cartesian derivative squares through order2; actual180 passes. N4's QQ-versus-ZZ comparison repair was a type mismatch, not a failed identity. No other374 section, floating evaluation, radial error, future candidate binding or existence statement is certified here.
Evidence: acceptance PROOF SHA256 8ee67f56385a374e97b214fcfa93ea4954cfee2b36476c33386e3854dd168423; manifest 727255c1b4cf7ca4ee1d08d96ec061fbdf9703b2b081f111650098726a03e6b3; N4 result325a5ab177722a9fda89c3f0b26c3bbf3ca6500b0950d1857492d1437350754d. Reviewer elapsed0.5248389118351042seconds. No new numerical calculation or foreign code execution for this acceptance.

## T4-377: Rational Bernstein theorem and partial-cover audit

Date: 2026-10-29T09:47:27.674640+00:00.
Claim: N4-285's positive rational Bernstein weights, independent-w and correlated degree-six Taylor enclosures, and signed-gradient matrix test are valid under a hash-bound exact reconstruction and complete finite cover.
Method: Read the full proof,95-line driver and shared transform, Taylor, eigenvalue and tree routines. Independently derive the rational convex weights and both enclosures. Use direct exact polynomial substitution to reconstruct20 fixtures, check80 point overlaps, and compare all denominator coefficients at degrees103/109 in12 cells with an independent positive degree-elevation formula. Check24 Taylor values and the frozen247-leaf cover geometrically by exact area and30381 pairwise disjointness tests.
Result and verdict: CONFIRMED the range theorem, inspected implementation and positive denominator method. The frozen09:46:03 cover has196 accepted and51 pending leaves; its accepted signs and complete accepted-plus-pending partition pass. This does not certify its actual accepted-cell arithmetic or the candidate reconstruction, and the pending leaves prevent a whole-plane bound. OPEN the complete candidate017 signed-gradient bound and separate N4-284 reconstruction review. No inverse or existence follows.
Evidence: PROOF SHA256 f5add5925dc0435d57a3d87b116fae7e03af445a30789c1007862f8ba6b6db06; result 41af39a8be9adbc104f312e899557593438dca86aa59224e76d3899d80dcf73d; frozen N4 theorem hashe02319b2d6e7b4236aea7f880ef2b00e3b1957cd5c7f46537743e270adfa5932. Checker completed2026-10-29T09:47:08.664260+00:00, elapsed0.2920729788020253seconds. No foreign code was executed.

## T4-378: Complete independent candidate017 gradient reconstruction

Date: 2026-10-29T09:55:17.653857+00:00.
Claim: N4-284's compressed rational polynomials represent rho_x and rho_y of the exact candidate017 on the whole plane.
Method: Derive rho by the accepted polar Laplacian, then its two gradient components by polar first derivatives. Clear denominators exactly and use closed Chebyshev coefficient formulas. Compare every coefficient with the frozen N4 Cartesian reconstruction. Independently expand the raw quartic jet at the origin and check six Arb gradient values at three points.
Result and verdict: CONFIRMED. All40082 nonzero coefficients,728 clearing identities and158 Chebyshev recurrence checks pass. The exact common denominator is (1+2499(1-t))^19, with degrees103 in t and80 in z, branches1 through8. The origin slope is positive, c+strain=1 exactly, and both origin polynomial limits agree with the raw quartic jet. All six point intervals overlap with more than150 accurate bits. This accepts N4-284 as an exact global representation, not a complete Bernstein cover, theta bound, inverse or existence result.
Evidence: PROOF SHA256 e44fb3f0f1da913e0abe1097249eaebea24c0d5e0f6551db5b8187f7fbb78ddb; result 7c72008a0f4a67b9afd4764262055cfedb116b5e98bb818af5f60fc825e9ac03; raw017 7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114; compressed peer polynomial 6887cdc6cdcc02fd0a7733d0343188df67c42c653e1a82ec033b2a207a08e872. Completed2026-10-29T09:54:26.768631+00:00, elapsed72.95496338699013seconds,2048-bit diagnostics and exact-rational equality. No foreign code executed. The harmless preparation-path failure and its pre-execution correction are retained in verification/DEVELOPMENT.md.

## T4-379: Reference screening and endpoint budget audit of R1-038

Date: 2026-10-29T09:59:29.800048+00:00.
Claim: R1-038 translates stationary solution sets between compatible references, transfers L2 distance exclusions, and identifies necessary endpoint budgets.
Method: Read the complete frozen35 review and its arithmetic script. Prove the distributional affine identity with a common correction space and canonical velocity, derive the distance and value-function statements including empty solution sets, and check the uniform-CI monotonicity and norm-dominating implications. Independently verify42 exact screening margins, sector thresholds and all twelve table bounds in768-bit Arb.
Result and verdict: CONFIRMED R-SCREEN under(S), conditional(b2) under(H-cut), the endpoint necessary cap(c)(ii), and(d) under a valid Newton theorem and the endpoint hypotheses. Part1 correctly repairs R1-037(d). REFUTED the inference in(c)(iii) from failure of an ambient X-to-H_q embedding to nonexistence of every stationary-solution a priori H_q bound: the latter remains OPEN. Clarify the absolute-difference notation when both distances are infinity; keep(S), including canonical velocity and domain compatibility, rather than replacing it by a finite sector check. Restrict(c)(iv)'s last sentence to exclusion at the specified ceiling by this fixed CI cap; moment bounds can sharpen a subthreshold numerical bound before that condition holds. No actual successor exclusion follows without a certified difference norm. T4-375's stronger constants retain their separate OPEN review status.
Evidence: source7fd26ed09b58f2d18ecad860f358cec5eabb73d0dfbfbb2cd8a19fbd26fc256d; PROOF 25d028a9798bf0f69d87293da8182d4e7111e4a51687831bbcfc1ba1d0df1d55; result 6254eb19fe4df594759708539d0fe38269c941130d85444785f93d50d7ec5344; completed2026-10-29T09:59:01.703232+00:00, elapsed0.0038895681500434875seconds. All42 margins are strict downward bounds; smallest graded margin is015. Original interval self-ordering assertion and its repair are preserved in verification/DEVELOPMENT.md. No foreign code executed.

## T4-380: Pointwise endpoint budget independently confirmed

Date: 2026-10-29T10:05:04.098717+00:00.
Claim: The pointwise minimization in the T2 theory worker's375 review script gives a valid necessary H_q bound and sharper thresholds for the existing CI.
Method: Complete the two-dimensional square for(qA,A')+t(qP,P'); independently evaluate the three exact rational angles and all circle projections in768-bit Arb. Retain the separate leading-velocity assumption when using V>=0.991488..., and evaluate both V=0 and that stronger input.
Result and verdict: CONFIRMED the pointwise consequence and conditional cap formulas. H_q exceeds999775 for007,999745 for013 and999748 for014. No minimax or optimal-angle claim is needed. Without any extra velocity asymptotic, reaching the fixed sharpw L2 radius1351/1024000000 requires E<0.785064, stricter than the hypothetical single-mode lower constant under investigation. The family ceiling thresholds are below0.682 sharpw,0.648 TB and0.27 graded. Hypothetical E=1.749109 gives a common cap below2e-8; below1.65e-8 additionally uses the stated positive leading-velocity bound. The folded-kernel proof of that E remains a separate OPEN audit. The original375 written review has not yet been published, so its acceptance is separate.
Evidence: PROOF 4fcfd14192b17ea5816132716b3ded2fbbdb3cbe0ae81ca217cd3f3d67a7a92c; result b081ef430ad054bb3255d191ec23b0bdad713b98f0d30f3407fe1540c456f4d5; computation completed2026-10-29T10:04:28.887187+00:00, elapsed0.008689210750162601seconds. The initial cap assertion omitted the velocity qualification and was repaired before publication; original code/log retained in verification/DEVELOPMENT.md. No foreign code executed.

## T4-381: Universal velocity lower bound and intrinsic CI limit proposed

Date: 2026-10-29T10:07:12.802521+00:00.
Claim: Every universal T4-335 velocity constant on the centrally odd weighted C1 class is at least(-q-1)/(2(-q)(-q-3)); this prevents the existing endpoint CI from reaching the fixed sharpw radius for007/013/014 even with an optimal universal E.
Method: Write a standalone proof for h=y(1+r)^(q-1)/(-q), show H_q=1 exactly, compute its canonical mode1 Green potential and first moment, retain the exact dipole and derive the remainder at theta=pi/4. Independently check the Cartesian derivatives and tail coefficient symbolically; recompute all rational-angle endpoint budgets in768-bit Arb. Integrate the retained delta-error shape exactly.
Result and verdict: OPEN independent Opus review of the new theorem. Exact and interval checks pass. Etest=0.793036506422514088..., while380 requires E<0.785064 for the fixed sharpw ball. With V=0 already, every universal E gives crude CI cap<1.2485e-6 and the sharper retained-error integral cap<1.421e-7, below the fixed sharpw L2 radius1351/1024000000. No stationary h is supplied: the lower bound concerns the universal C1 estimate, not a PDE-specific estimate on stationary solutions or a normalization-restricted subspace. It does not exclude all smaller radii or supply a missing upper H_q budget.
Evidence: PROOF ca0e008a1bfb7868fb1242af0a0eeb1897552a574dc27f7b1a9ad36e1a0b30b9; result 0b3e6350ea9f4183c4020b1ad5af3e43ac2c45408e86b831e9d92a05f95ca03d; completed2026-10-29T10:06:44.077498+00:00, elapsed0.4091672566719353seconds. Independent peer review requested in handoff180.

## T4-382: Sharp amplitude moment theorem independently reviewed

Date: 2026-10-29T10:08:22.233866+00:00.
Claim: R1-039 independently confirms T4-372 in its exact amplitude class.
Method: Read all151 review lines and the full checker/output, compare the complete variational proof and all26 reported checks with the frozen original argument, and verify source hashes. Distinguish the analytic maximum proof from finite tests and interval constants from FLOAT diagnostics.
Result and verdict: CONFIRMED. T4-372 is AUDITED. The scalar/vector inequality, absolute moment integrability, exact constant and S1 extremizer pass. Sharpness remains restricted to the homogeneous amplitude class, not weighted C1. The constant is9.155134741153639269902... and the ratio to the split bound0.971488103354059961363.... No absent H_q budget is supplied. The moment-independent CI cap is unchanged; the broader phrase that all endpoint reach is unchanged needs the existing379 qualification about subthreshold bounds.
Evidence: reviewb4f54ce979c7c88afec87f00d404de674f44e3e26a400c40a76d2d49b551cc2b; acceptance PROOF9cfa7b9dae64a330ebcffd75ebeb7c01e5b3d4494721435ca4c3d86def6ba337; manifest8e27ff37364e287b833539176062abf00bc416d51919f009980a25eb468ea949; no new numerical calculation and no foreign code executed.

## T4-383: R1-038 repair text accepted

Date: 2026-10-29T10:08:22.236225+00:00.
Claim: review set 37 fully carries the five analytic scope repairs of T4-379.
Method: Read all71 lines and compare each replacement with the complete379 proof, including extended-real distances, chart compatibility, stationary-only budgets, moment-cap scope and the K-stability hypothesis.
Result and verdict: CONFIRMED. All five repairs are correct. R-SCREEN remains conditional on(S), the value-function statement on(H-cut), and the Newton discussion on a valid theorem with all hypotheses. No actual successor difference norm is supplied; no candidate verdict changes. This does not certify all of THEORY_FINAL draft31.
Evidence: repaired sourced292f292f8d5948fe4872c856b57ca61cfc91ab723a18c20eec1893728bd208c; addendum54040937f2b2ec18d1e7cba2f750fe403d635662ea53ec35f69fa40b2b338cfe. No new calculation.

## T4-384: Normalization and an arbitrarily small L2 budget do not lower the universal velocity obstruction

Date: 2026-10-29T10:12:34.210368+00:00.
Claim: The universal lower E>=(-q-1)/(2(-q)(-q-3)) persists on smooth S1 functions with c[h]=0 and ||h||2<=beta, for every beta>0.
Method: Write a standalone proof using f_R=y(R^2+r^2)^((q-1)/2)/(-q) and subtract an explicit compact first-sine bump to cancel the exact contact trace. Bound H_q(k_R) by a quantity tending to1, prove its L2 norm tends to0, and retain the exact mode-one exterior dipole. Check16 symbolic and interval identities independently.
Result and verdict: OPEN independent Opus review. All checks pass. The construction retains the contact term and is smooth at the origin. At R=10000 its necessary E exceeds0.79303648 with L2 norm below2.028e-11. This strengthens381's domain statement; it still does not impose stationarity or claim membership in a specified fractional X ball. A stationary-only estimate remains OPEN.
Evidence: PROOF a18ad405134e554e0613f6764ce566b8a3b458295b1445067fa3ad415c41083c; result eedbfd683b7ebca07031071ed25376375acd2e7c4098014a6dfc0760aeb70345; completed2026-10-29T10:12:11.771995+00:00, elapsed0.6121267797425389seconds. No foreign code executed.

## T4-385: Accept the independent endpoint-gradient review

Date: 2026-10-29T10:20:49.316585+00:00.
Claim: T2 the review of T4-375 confirms all of375's gradient-limit, projection and cap theorem.
Method: Read the complete frozen review and compare every analytic step with375. Reuse the already independent exact projections and interval computations; distinguish the new review remarks from its verdict.
Result and verdict: CONFIRMED. T4-375 is AUDITED. Uniform convergence and local Lipschitz bounds pass to the limit without differentiating the remainder. All cap inequality directions and source specializations agree. R2's unsupported FLOAT-to-saddle inference is REFUTED as an inference, not as a counterexample to the proposed saddle. Quotient domain, common cap rounding and a future writing endpoint require the attached repairs.
Evidence: review 2fae48f9c409ca9b970e1bcd726d86ba78ba33290b2e88badd82475fe45bea79; acceptance PROOF 36f92c10eeac0fc7eae173bed420019345c45c33cafc1bf8b3dcee31612d49f4; manifest 9e502e601dbef5fb013d231a5a23998503c6691c973c41d860a32641eda61831. No new computation or foreign code execution.

## T4-386: Independent universal velocity lower bound accepted

Date: 2026-10-29T10:20:49.316585+00:00.
Claim: T2 R4 independently derives the same lower E as381 Sections1-2.
Method: Compare both controlled mode-one Green expansions, exact moments, C1 admissibility and homogeneous velocity formulas; match the independent symbolic and interval outputs.
Result and verdict: CONFIRMED the universal lower constant0.793036506422514088... on the full weighted C1 class, including S1.381 Sections1-2 are AUDITED through this independent derivation. The sharper delta integral in381 Section3 and normalized extension384 retain separate peer-review status. The review's common crude cap1.2484e-6 is REFUTED numerically by013; use1.2485e-6. No radius comparison changes. No stationary-only estimate is excluded.
Evidence: same frozen review and acceptance PROOF; independent T2 output 5efe22d4d40746913631517335d09beb57735f07f125ebfa1f51f098759e46d3; own381 result 0b3e6350ea9f4183c4020b1ad5af3e43ac2c45408e86b831e9d92a05f95ca03d. No new computation.

## T4-387: Candidate021 independent polar point obstruction

Date: 2026-10-29T10:26:46.324460+00:00.
Claim: The exact2426-generator021 violates the six named scalar and original graded necessary point inequalities at(1/10,73/100).
Method: Independent polar Euler derivatives through order4 from exact raw rational generators,1024-bit outward evaluation, and the already audited point embeddings. No Cartesian publisher code is executed.
Result and verdict: CONFIRMED. All8 point-field enclosures agree with N4-314, all six scalar gaps are positive, and the graded gap is0.08009735417307405636... with F=0.10049880549013846295.... The exclusions apply only under the stated fixed-c stationary-difference and canonical-velocity hypotheses. No global norm or inverse follows.
Evidence: audit record candidate021_point, proof SHA256 8335d44f08ea881a90720931f08cc388537539d0b5e09133890475854db207bb; result 42b8ef6ea959e7f90803d0d211cce54d9060fa21a55c300550f9733fb015a9c1; completed2026-10-29T10:24:03.673330+00:00, elapsed1.998979528900236seconds. Raw021 SHA256 c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8.

## T4-388: Candidate021 exact center normalization

Date: 2026-10-29T10:26:46.324460+00:00.
Claim: Candidate021 has c+partial_y U2(0)=1 exactly and positive density slope.
Method: Independent exact local quartic series, including every generator able to contribute. Compare all rational coefficients to N4-314; use512-bit Arb only for the decimal slope.
Result and verdict: CONFIRMED. The center relation is exactly1 and the density slope is10.31287390743806604080022948.... This local identity does not claim stationarity elsewhere.
Evidence: audit record candidate021_origin, proof SHA256 f049aafb6bdce09942ab7ee62753626c1a8b7d4dcb3625c6c206c7f9b18fc880; result 213afe3297fde85769998ac5ae113e86c916ae808be41b4169048427025fed16; completed2026-10-29T10:24:03.861654+00:00, elapsed0.04657799005508423seconds. Raw021 SHA256 c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8.

## T4-389: Candidate021 complete far-field prefix

Date: 2026-10-29T10:26:46.324460+00:00.
Claim: Candidate021 has the full accepted leading profile and exact cancellation of the forbidden residual prefix.
Method: Independent raw-generator homogeneous expansion through the exact exponent cutoff-7/2, complete convolution of density and stream modes, and differentiated analytic remainder control. Compare13 common exact N4 rows and all16 N1 rows.
Result and verdict: CONFIRMED. All11 zero sectors and5 nonzero sectors match; the first nonzero sector is(4,1), exponent-11375183046454913/4076476460239181. The first four leading density/stream profiles equal007 exactly. All504 scaled generators have q=4, hence cannot directly change this prefix. The output certifies asymptotics, not a residual upper norm.
Evidence: audit record candidate021_sectors, proof SHA256 0d94a8adc64c16a0c3bf8ff0e7fdd4cf90886e8d58735436fd7c21a48e1724ab; result fe7c0a0bf7f2fa84f204872b37708206282d6bb89bcbd5d64765292db05e7c7b; completed2026-10-29T10:24:26.884744+00:00, elapsed22.97646242612973seconds. Raw021 SHA256 c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8.

## T4-390: Numerical report repairs accepted with two remaining qualifications

Date: 2026-10-29T10:26:46.324460+00:00.
Claim: The numerical report applies all eight T4-374 requests.
Method: Read the repaired passages against every original request and its accepted proof. Audit the new021 penalty explanation with an exact scalar quadratic counterexample.
Result and verdict: CONFIRMED requests1-7 and the mathematical portion of8. REFUTED full completion of8: the frozen header still says09:08Z. REFUTED the inference that a small objective-value fraction makes the14 new021 rows inert; their actual causal impact remains OPEN. The observed unchanged pairings remain valid FLOAT trial observations. No mathematical repair changes an exclusion.
Evidence: frozen report6648ebd2190e41fe951e9fab2c90dbc6c73c0b7d993279d04919fa75a5aa1540; audit record numerics_final_repair_acceptance, proof 2245004992790dd1815c020935b0b606fc478b32e0298858f89de4d781fb2231; manifest1e4446b79f1a814affe501a6932f3627463aba84764402b858e50221ad4e5d68. No new computation.

## T4-391: Full independent review of381 accepted

Date: 2026-10-29T10:31:18.506542+00:00.
Claim: R1-040 independently confirms the universal velocity lower bound and the retained-delta cap of T4-381.
Method: Read the complete review, all checker code and25-check output; verify the exact Green argument, cap monotonicity, integration identity, endpoint parser and outward interval path against the existing independent Arb calculations.
Result and verdict: CONFIRMED. T4-381 is now AUDITED in full, including Section3. With the accepted375 gradient theorem and380 pointwise budget, the universal-constant CI is incapable of reaching the fixed sharpw radius or any registered family ceiling for007/013/014. Its retained-delta cap is below1.421e-7 already with v0=0. The full range-5<q<-3 is checked by R1-040; the earlier T2 derivation used a narrower interval containing the campaign exponent. No conclusion about a stationary-only estimate or an upper H_q budget follows.
Evidence: review 0e1c20eba41a5e07c73945ccfe3a180f59e8fa78ed91bac88104a0ee32b4cf2d; acceptance PROOF 4ecd82290091fd3b0c8356da3bc9084786c12a0fa4b16faaaa2c52f3fb1ca877; manifest 83675a6a4d9c30d3ff48680d718c0e1e91715136201badfce6baad12e3b6649f. No new computation or foreign code execution.

## T4-392: Candidate021 whole-plane weak distance independently reproduced

Date: 2026-10-29T10:36:11.920052+00:00.
Claim: N4-316 excludes every stationary L2 correction to021 below its registered weak-distance floor.
Method: Reconstruct all fields independently by polar Euler derivatives, evaluate the exact rational angular products, and integrate63 complete exponent groups with exact CRT and direct hypergeometric Arb values at2048 bits. Six scalar fixtures, the full007 coefficient calibration, actual021 point values, both pairing formulas and the complete gradient critical-point bound are checked.
Result and verdict: CONFIRMED. The registered(19,1800) probe gives I=-4.3215653806821456993e-6, M=0.0014045807906480636670, C=0.00091298323787915261542 and distance strictly above466174213699793/250000000000000000=0.001864696854799172. The complete bound exceeds every registered scalar family and original graded ceiling. All9 peer comparisons pass. The usual fixed-c canonical weak-stationary hypotheses apply; no inverse or existence claim follows.
Evidence: PROOF a93de1e58f060bc03bb6d7729efe4215c2a06b066230683363206897a3dc40f6; result a2524cf4b8c80e94b835278a45a73123879496efa897b3085a07bfe617aafdc0; peer cf4855e5966575dd744c68806635ce6f2e4b8b1a489e8eaf0f12ab3bd23010c5; completed2026-10-29T10:32:43.100363+00:00, elapsed149.12764535285532seconds. Foreign code was not executed. The017 cover was paused149.31495098024607seconds and resumed10:32:43Z.

## T4-393: Complete potential-prefix matching implies reference compatibility

Date: 2026-10-29T10:36:11.920052+00:00.
Claim: The general compatibility lemma in N4-313 satisfies the full R-SCREEN hypothesis for all real S1 L2 corrections.
Method: Check the finite-generator analytic expansion, differentiated decay, all Sobolev and drift integrability claims, canonical velocity by L2 harmonic uniqueness, locally integrable stationary products, translation of zero sets and both extended-real distance inequalities. A standalone independent proof precedes the actual-pair computation.
Result and verdict: CONFIRMED. Equality of the leading potential coefficient in each angular mode of branches1 through4 implies g and V=O(r^(1-5delta)), g in every integer Sobolev space, X.grad g in L2, and V=U[g]. For the stated weak class the stationary sets translate exactly. Stronger classes require their own stability or can be excluded as subsets of the weak class. Prefix failure is not asserted to imply nonintegrability. No numerical finite-sector list alone is substituted for the complete representation.
Evidence: peer PROOF 6f2d3685d0b914c92f8b7caedc0571bb6f95d8092cf53a60eb8616985b2bd2a3; independent PROOF f233bbad3faf8660f035ca681b70a751728225091e9df2e748c06723f9e149cc; prepared input graph a309ef4f11b6f73f844fcaf0fa513aaf8480c8347366802490fd2641ddb2e729. General analytic audit; the actual-pair result follows separately.

## T4-394: Candidate021-minus020 whole-plane density norm

Date: 2026-10-29T10:36:11.920052+00:00.
Claim: The actual N4-313 density difference norm is0.007349253249719724... and all three sufficient R-SCREEN comparisons fail.
Method: Subtract the exact raw generator lists, check all potential-prefix sums, reconstruct the polar fields independently, check nine raw Cartesian values, retain all834 ordered angular products in14 groups, strip exact endpoint zeros, and integrate by direct hypergeometric CRT at2048 bits. The parent floor is taken from the independent020 weak certificate.
Result and verdict: CONFIRMED. There are2286 nonzero generator differences. The complete norm agrees with N4-313 and is strictly below3674626624859862044982741129/500000000000000000000000000000. Every group and the squared norm agree. The norm is strictly above each sharpw, TB and graded transfer allowance. This refutes only the proposed sufficient transfer comparison, not existence or other exclusions;392 already excludes021 directly.
Evidence: PROOF f233bbad3faf8660f035ca681b70a751728225091e9df2e748c06723f9e149cc; result 5ec953335a564483d210e86b9165478f3bf33fa80d10c07df4c3f779139baba7; peer 51a129103f1d11116da041e5e06ce23026641630c3ea3336d11df2c9caaf8a4a; completed2026-10-29T10:34:52.707085+00:00, elapsed2.4440349680371583seconds. No foreign code executed.

## T4-395: Candidate021 dimension and current objective span

Date: 2026-10-29T10:36:11.920052+00:00.
Claim: N4-315's actual2426-dimensional space and81 current analytic rows have the stated probe-span properties.
Method: Compare every exact shape and c to the accepted020 application and rank theorem. Parse the raw metadata, completed launch and log, compare the current and earlier PAIRK ASTs, reproduce their source diff and apply sine orthogonality followed by polynomial independence.
Result and verdict: CONFIRMED for the current recorded021 objective. All25 registered probes and21 smaller-radius diagnostic probes lie outside its analytic span; (21,522) is explicitly inside it. The two dimensions are2426. Historical claims before the accepted020 application are outside this independent replay. The current source includes later weighting options and is not claimed to be the historical executed bytes. Analytic span separation is not statistical independence or blinded optimization.
Evidence: PROOF 0dd675f53c96f4c1a6a9fbf00316bc9ea44e792ee8797b344eed21991e1f2c61; result e7da2ceadc102d14013f59776f22f0eeef428edb89659fff6573374188cae652; peer db86063a45b941cdd72e955611886e1f6e4fd6a7a2e96758ded2b053fa3a6005; completed2026-10-29T10:34:52.894846+00:00, elapsed0.10007074335590005seconds. Publisher sources were inspected only.

## T4-396: Normalized smooth small-L2 velocity obstruction independently accepted

Date: 2026-10-29T10:42:29.942445+00:00.
Claim: T2 the review of T4-381 and T4-384 confirms the complete normalized extension384 and supplies a second independent check of381.
Method: Read both proofs, the full review, all346 lines of its independent checker and the complete output. Recheck the mode-one contact identity, normalized sequence, weighted gradient and L2 scaling, controlled Green remainder and order of limits. Compare the precise stored intervals to the review tables.
Result and verdict: CONFIRMED. T4-384 is AUDITED: every universal velocity constant on smooth normalized S1 functions of arbitrarily small positive L2 norm is at least0.793036506422514088... at the campaign exponent. The review's first-moment condition a>2 is corrected to a>3, already assumed. Its statement that all displayed caps are rounded upward is REFUTED; several table entries need approximate labels or outward rounding. The stored intervals and conservative caps remain valid. No statement about stationary-only or full fractional-ball estimates follows from384.
Evidence: review964eb741a7d42f522582285241a3359514ca2e12677366d71238abdf05a6bb56; acceptance PROOF f14b779d2df23bea30015c52062eb5871820153ddf49757b2f4a44c0e683dd98; manifest 6902d15c14d916ed7f0d9afb520079336df5c4a10248c28d66ab663c8aec82d7. No new computation or foreign code execution.

## T4-397: The universal velocity obstruction persists in the full fractional ball

Date: 2026-10-29T10:45:33.368179+00:00.
Claim: For every0<s<2, positive component weights, positive fractional-ball radius and L2 radius, the universal lower E of381 persists on smooth normalized S1 functions in both balls; one may also prescribe any exact H_q=Hstar>0.
Method: Derive the positive Bessel convolution kernel and an explicit weighted Young constant. Control the exact fractional norm by weighted integer derivatives through order4. Apply the exact scaling of384's normalized sequence, prove membership in the compact-smooth completion, and use its unchanged homogeneous velocity limit. Twelve finite identities and512-bit constant checks are performed after writing the complete proof.
Result and verdict: OPEN independent Opus review. All finite checks pass. The Bessel estimate gives C_s=4.468299565794177... at selected s, and X_(s,w)(k_R)<=D R^(1-a)+X_(s,w)(b)R^(-a-1)/a tends to zero with explicitly defined finite D. Thus adding only the full fractional norm ball cannot lower the universal E. Stationarity or a specific tail profile remains a separate possible input. No finite-R fractional norm or existence claim is made.
Evidence: PROOF 9afe571d5720f1bc304c712c8fb4331ca148f83bcc55f842f06abc4943ae2330; result 64b1442c9cbdc9062c5bce2a90ea447f79f376c2befe80314d345abb659a6243; completed2026-10-29T10:45:05.178484+00:00, elapsed0.22400161484256387seconds. Cover paused0.7198287071660161seconds and resumed.

## T4-398: Repaired endpoint review accepted

Date: 2026-10-29T10:49:48.736443+00:00.
Claim: The revised T2 the review of T4-375 satisfies all five requests from T4-385.
Method: Read the complete revised text and frozen diff, recheck pointwise projection and cap directions, and compare all nine published code/result/log hashes to the frozen files.
Result and verdict: CONFIRMED. T4-375 remains AUDITED. The FLOAT minimax inference is removed, zero denominators handled, the common cap rounded safely, actual times recorded, and R3 explicitly left awaiting separate audit. Its revised conversion mechanism is documented, without accepting its numerical integral here.
Evidence: review 1ea7ed2521f15750600f466d2b659e85ed402285a5a93b8312102b2fe6bd35fb; PROOF 3e3e235999753b71c7c7ebcf51bb0d5421469618e47275b6d794ecffd1bdcae3; manifest 81c3eae7f1e2a3267afea8ab9ca6715b783adcff2dc9dd3b19a916dede8e5650. No new computation or foreign execution.

## T4-399: Complete theory_v07 preview audit

Date: 2026-10-29T10:51:34.575895+00:00.
Claim: The new screening, endpoint and Y-norm statements, the candidate021 row and the T4-373 repairs in theory_v07 preview1 are valid.
Method: Read all542 lines, compare the exact domains to the accepted proofs, rederive the extended-distance and Newton implications, and run44 exact/768-bit checks using the printed integer H0 values.
Result and verdict: CONFIRMED for NC-T-SCREEN under(S), NC-T-UNIV-E as a bound on this certificate, NC-T-ENDPT-Y with K=0 handled separately, the021 row and all four prior repairs. Maximum fixed-radius Ecrit with the rounded-down H0 is0.785063779293793..., still below0.785064. Maximum shape cap is1.4208033127739053e-7, below1.421e-7. REFUTED literally: every stationary-only velocity estimate must fail on the universal test; only an estimate sharp enough to evade the obstruction needs that additional restriction. T4-384 and the repaired T2 review now have the later acceptance statuses396/398.
Evidence: preview393b6640fff20907d2a96184072b0f355e862c0f797c876acfbf45ffff277f5f; PROOF 66e9343e8a13675b6bb64aaab47e3d00eb5143e48506001bbd0c6a27bd685e41; result 650c0d0e5b11fc70b6bac7e539a84c607e12f1d5d6bbd47fe688c785a083d04a; completed2026-10-29T10:51:12.517282+00:00, elapsed0.003470050171017647seconds.

## T4-400: Complete candidate017 signed-gradient cover independently confirmed

Date: 2026-10-29T10:55:08.852637+00:00.
Claim: The N4-309 complete cover gives theta<=2/25 and signed background rate>2.00123867 for exact candidate017.
Method: Reconstruct all global Bernstein coefficients from the accepted40082 rational gradient coefficients, subdivide through an independent de Casteljau implementation, and recompute each of247 leaves with positive-denominator rational ranges, independent-w and correlated Taylor enclosures. Check exact full partition area2,30381 disjoint pairs, all leaf hashes and8 exact fixtures.
Result and verdict: CONFIRMED. Every leaf passes at2048 bits. The whole-plane theta is at most2/25; the accepted commutator bound gives c+1-theta-kappa>2.00123867. Origin and far-field boundaries are included. No inverse or existence claim follows;017 remains excluded in registered balls.
Evidence: PROOF 9e6a4f7d15ef1d306a0623e924ff43f7b9c385e0321a2094dbbea1a85402e79d; checker 3d1af6186f595b0848b2aa9502a56d510b7abb9a974eb82519587ad4a74e2044; result 373804eea41dd375f29edcaac94a5b4107fbf8f52641db0c4398dbdef95bdcb8; completed2026-10-29T10:53:48.840942+00:00, elapsed2209.560071857646seconds including recorded pauses. All foreign code was inspected only.

## T4-401: Repaired normalized velocity review accepted

Date: 2026-10-29T11:00:44.611245+00:00.
Claim: The revised T2 the review of T4-381 and T4-384 satisfies the integrability, outward-rounding and provenance repairs from396.
Method: Read the complete final review and checker diff, prove the exact dyadic-to-decimal direction, compare the three published hashes and retain intermediate files separately.
Result and verdict: CONFIRMED. The finite first absolute moment uses a>3; all stated bound tables now round outward and conservative caps are asserted in Arb. The consumed theta-star values are asserted exactly and the whole-file hash is explicitly only printed. T4-381 and384 remain AUDITED. No foreign code executed or new integral repeated.
Evidence: review 5fa23303d3c4328313ff05958eced1de6059e857858377e38f3e01279d0ed112; PROOF ac911ee902f1ff33ce3338697200efdd4c4fe2d2008f6b702c5b197377d32deb; manifest 926ad260e70214f4b2d470c7e78e718101e9da22797e283f8990023d82a0c680.

## T4-402: The angular tail determines the compensated velocity coefficient

Date: 2026-10-29T11:06:09.226123+00:00.
Claim: For -5<q<-3, a C1 S1 correction with finite H_q and uniform finite odd-sine tail b satisfies r^(-q)(U[h]+DK M) -> V_q[b] uniformly in angle. For the endpoint subspaces span(A,P) of007,013,014, its limiting magnitude is at most (583/1000)H_q.
Method: Symmetrize and compensate the kernel before passing to the scaling limit. Use cubic origin cancellation, first-moment integrability, local Lipschitz subtraction at both PV singularities, and an exact cutoff Green calculation to identify the limit. Derive a two-dimensional Gram trace bound and certify its full-angle upper bound by rational cosine coefficient sums.
Result and verdict: OPEN independent Opus review. All twelve exact and symbolic checks pass; the common rational bound0.583 is proved for the finite angular calculation. It is below the universal0.7930365 because the tail subspace is an extra hypothesis. No finite-radius error or successful CI certificate follows.
Evidence: PROOF a98e64b04a4ab8f8e46f311c028d55138e9483f761d84e140ed550066e5ab3d9; result b8d33a7e9aeb8e2d81ab23b9c73e34b0b6f6dfb7c137e004f5330600a86ebdce; completed 2026-10-29T11:05:03.354478+00:00, elapsed 0.5469149169512093seconds. The first attempt had a rational-simplification false negative, retained in DEVELOPMENT.md.

## T4-403: Candidate022 dimension and recorded objective independently bound

Date: 2026-10-29T11:08:40.270964+00:00.
Claim: N4-321's actual2414-dimensional basis and67-row objective-span conclusions hold for immutable022.
Method: Bind both raw stages to every accepted abstract369 shape, rehash that proof's dependencies, compare the exact c and parent016, inspect both completed launches and logs and compare current row-parser ASTs to the accepted020 source. Apply full-circle sine orthogonality and reproduce the mode31 origin witness.
Result and verdict: CONFIRMED for parent016 and both022 stages. All25 registered and35 diagnostic probes lie outside the67-row analytic objective span. There are12 then28 logged iterations, not necessarily40 accepted updates. REFUTED: the added density support is disjoint from a sweep through31; mode31 actually occurs. The longer007-through013 history and statistical blindness are outside this replay. No candidate norm, exclusion or inverse follows.
Evidence: PROOF 475e61a8acefc640270b4c3e092af9ba446f418b1ab5bcd922fce4cf293c881e; result 9dea5cb71c53e4f6f41a06f35cdf339f2d48bac39ec43ce90ea4019eeba3c896; peer44ee4cd4bbf00b2bf667313db5cbb9da358ad9e14d2c467828d25f5fedf97b05. Completed 2026-10-29T11:08:40.211802+00:00, elapsed 0.13961172569543123seconds.

## T4-404: Second endpoint display revision accepted

Date: 2026-10-29T11:11:34.684569+00:00.
Claim: The later T2 the review of T4-375 revision repairs all displayed bound directions and preserves the accepted result.
Method: Read the complete source and review diffs, verify all ten frozen input hashes and all nine printed artifact hashes, and compare both directed-conversion ASTs to the accepted401 function.
Result and verdict: CONFIRMED. T4-375 remains AUDITED; the correct common displayed Ecrit cap is0.6819391. E_new stays CLAIMED pending its separate audit. The lower script also consumes Phi data; this acceptance binds the particular hashed result rather than treating the theta-only assertion as validation of arbitrary replacement Phi. No foreign code executed or integral repeated.
Evidence: review ca3aa4a013c36e6727258d99d6e63283b58d95f078a87ebd0c17719c86bc4fc6; PROOF b3d4f09f604b4ac0aeb4af258fa7ea6b5dbeadac8a1a43ecbf35de272b528739; result 9d9e068d1d7740d0de0396a661d2c85237c4b9a33aef066ae6a8a90e4ad7d754.

## T4-405: Candidate022 point exclusions independently reproduced

Date: 2026-10-29T11:13:35.915950+00:00.
Claim: N4-326 correctly excludes all six tested scalar balls and the original graded family by the fixed point (1/10,73/100).
Method: Use exact radial Taylor jets through order4 and independent polar differentiation; evaluate non-rational powers at1024 bits and recompute all necessary inequalities.
Result and verdict: CONFIRMED. All eight physical field enclosures overlap, residual0.08875964289635570284 and graded gap0.06836100482471213789 are positive. All six scalar gaps and necessary-radius checks pass. The single-point signed quantity is only diagnostic, not a global theta certificate.
Evidence: PROOF 5c0a5750b8d5c352748c2b72b2b7d27dbeaac39eb084ba9b4922864e43fb6bc3; result 25ef41a63f668a16b5b77a69e9c9fcb1fc9867330cb334a6ececd7c1109144ba; completed2026-10-29T11:12:31.575570+00:00, elapsed1.8105027452111244seconds. Frozen N4 direct record0a97a30195bdc687113e9f65857331f85d653651cb103e470b19cc597e44cbbe. Foreign code was not executed.

## T4-406: Candidate022 exact origin normalization reproduced

Date: 2026-10-29T11:13:35.915950+00:00.
Claim: N4-326 has the exact center strain and positive density slope.
Method: Compute the quartic raw-generator Taylor jet with independent rational binomial series, then differentiate its three quartic coefficients.
Result and verdict: CONFIRMED. c+partial_y u2(0)=1 exactly, all four N4 rational comparisons pass, and partial_y rho(0)=10.31182777938345267919... is positive. No stationarity away from the origin follows.
Evidence: PROOF a409689a05fa32804beb0b35489d4ff4737f27501963b1c16acf1509a3de2e48; result 1f043e3909bc9a82befca89ac77da378104ebce1349c5d30994c7b558233df56; completed2026-10-29T11:12:31.736586+00:00, elapsed0.04561237897723913seconds. Frozen N4 direct record0a97a30195bdc687113e9f65857331f85d653651cb103e470b19cc597e44cbbe. Foreign code was not executed.

## T4-407: Candidate022 complete asymptotic prefix independently reproduced

Date: 2026-10-29T11:13:35.915950+00:00.
Claim: N4-326 and the published022 sector table have the stated complete leading prefix.
Method: Expand raw generators in inverse radius, apply exact homogeneous polar differentiation, enumerate all exponents at least-7/2 and compare every angular coefficient in the13 common peer rows.
Result and verdict: CONFIRMED. The16-sector prefix has11 exact zeros and five nonzero labels (4,1),(9,0),(5,1),(1,2),(10,0). All492 radius25 generators have q=4 and contribute zero through L=2. The leading four density and stream profiles equal the accepted007 coefficients. All16 published table rows agree. These are asymptotic statements, not global residual upper bounds.
Evidence: PROOF f6f0ad00caff8420987d8790a2e908a210776cb4daae1f939542fff4a1d56515; result f7bd59c9d0dcddd1da235f6b3c5b4cbe5b20706f0ad7ecfb1e8f82ba76fe3cfd; completed2026-10-29T11:12:53.887251+00:00, elapsed22.084429278969765seconds. Frozen N4 direct record0a97a30195bdc687113e9f65857331f85d653651cb103e470b19cc597e44cbbe. Foreign code was not executed.

## T4-408: Candidate022 whole-plane weak distance independently reproduced

Date: 2026-10-29T11:15:57.616364+00:00.
Claim: N4-327 excludes every fixed-c stationary L2 correction to022 below its strict weak-distance floor.
Method: Reconstruct every field by independent polar Euler derivatives, evaluate all angular products and integrate63 complete exponent groups by exact CRT and direct hypergeometric Arb arithmetic at2048 bits. Check six scalar fixtures, full007 coefficient calibration, actual022 point values, both pairing formulas and the complete probe-gradient critical set.
Result and verdict: CONFIRMED. All nine peer comparisons pass. The registered(19,1800) probe gives distance strictly above135251075726327/100000000000000000=0.00135251075726327. This exceeds every registered scalar-family and original graded-family ceiling. The minimum retained moment accuracy is1936bits. The canonical fixed-c weak-stationary hypotheses remain mandatory; no inverse or existence claim follows.
Evidence: PROOF 80a91ccad7c863f94d703311ac8fe7273fafcbf544bbd4ef899c4baa81d2abd6; result 0fcd89adc9f57616f6ba2d8fdafb9b777dc2a55e049b6287997cea108851f835; peer fb9f8033b9c2cd199aad6e1f549501e07a8b2a386d612e4925dfcfad73edaac4; completed2026-10-29T11:14:56.370993+00:00, elapsed122.30854803370312seconds. Foreign code was inspected only.

## T4-409: Full fractional-ball universal obstruction independently accepted

Date: 2026-10-29T11:20:49.511474+00:00.
Claim: T1 R1-042 independently confirms T4-397 in its complete fractional space and prescribed-Hstar version.
Method: Read the complete proposal, review, independent checker and output. Recheck weighted Young and distributional extension, cutoff membership, the first-sine contact term, exact scaling and order of limits.
Result and verdict: CONFIRMED. T4-397 is AUDITED. The constant cannot fall below(a-1)/(2a(a-3)) merely by imposing the selected fractional and L2 balls, normalization and any fixed H_q. General S1 c[h] is not local; the test functions are first sine. The independent R=512 and derivative-norm numbers remain FLOAT diagnostics with no finite-R certification.
Evidence: PROOF e6f9f4e3cd51e7c434bb337489901a40be6dbd7782df3a14f859ca4e7415621d; manifest 9b137a55f177aacfcfeba4a7fdeb31165f6bdb72aae2a72ed75a94c6bbc71f55; review3c0c801e1c3568c2e4b6a02549278992684b1aa6c8a113191f2a93b98992a5f4. Nineteen exact and three Arb checks are independently reported; two FLOAT checks are diagnostic only. No foreign code executed.

## T4-410: Explicit finite-radius two-weight velocity remainder

Date: 2026-10-29T11:23:38.408479+00:00.
Claim: A centrally odd C1 remainder with amplitude weight a and weaker gradient weight q, -5<a<-3 and a<q<0, has compensated velocity bounded by A r^a times an explicit logarithmic factor. An explicit cutoff model then gives a finite-radius error for the profile-specific coefficient.
Method: Separate the kernel singularity, origin and exterior; use min(Ls,2B) at the local singularity, odd Taylor cancellation and exact harmonic Green tails. Bound the model difference using only amplitude asymptotics and the original gradient weight. Check20 exact identities and512-bit arithmetic fixtures.
Result and verdict: OPEN independent Opus review. All finite checks pass. The normalized error J(R)=A R^(-epsilon)[C_a+2^(1-a)(1+log_+(k R^epsilon))] decreases to zero. The cutoff harmonic error is at most B_b(2R0/R)^(q+5). The result requires explicit H and remainder inputs and supplies no a priori stationary H budget, successful CI certificate or existence theorem.
Evidence: PROOF cd2e6f18fb4b9255503e988e220709cb258338a8b4829080910ca8a11797bde6; result 4763413e14e845a23a298d8e5ab8b712438cbac5cbdef00423f2fd5b2531276f; completed 2026-10-29T11:22:39.617872+00:00, elapsed4.442687056958675seconds. No differentiated amplitude remainder is assumed.

## T4-411: Complete independent folded-kernel upper bound

Date: 2026-10-29T11:32:12.032879+00:00.
Claim: T2's improved universal compensated-velocity constant E=1.749109 is valid for the campaign q, with central oddness, C1 regularity and finite H_q.
Method: Independently derive the scaled folded kernel, retain its contact term, enclose origin and infinity analytically, and evaluate every polar cell and every output direction at128bits with exact dyadic validation. Use a complete8-by8 subdivision on the cutoff circle and a Taylor remainder with factor1/2.
Result and verdict: CONFIRMED. All1000000 cells,15616 crossing subcells and121 direction intervals are covered. The resulting upper bound is below1.747261, hence below the claimed1.749109. The estimate holds for every nonzero X under PROOF.md's exact hypotheses. No stationary H budget, inverse or existence follows; unrelated T2 diagnostics are outside scope.
Evidence: PROOF e72bc63bf849a60c5d7df86317d012c78c57a5f2f984f79c65809fb0fa874426; result 46a023a7cd6f2c6b5820a3ab6ae3cffba08430b4b11a0266a8e1f2af290191df; checker 85d35a0a2dc5f6dbb9c4be30a8863031a977dd1694dff3e54321ed8ca22d3213; completed 2026-10-29T11:30:43.254698+00:00, elapsed159.66070708399639seconds. Final validation is exact rational, not nearest-rounded float.

## T4-412: Published theory_v07 audited by exact file

Date: 2026-10-29T11:34:23.066158+00:00.
Claim: The published710-line theory_v07 incorporates the accepted preview repairs and states its new022 exclusions and endpoint results on the correct domains.
Method: Read the full publication and591-line diff; recheck theorem domains against399, all later cited T4 results and nine exact rational distance ratios. Parse all65 full AppendixH hashes, recovering historical record prefixes and note suffixes where available.
Result and verdict: CONFIRMED mathematical statements with three explicit repairs. REFUTED stale status:2.1 actual022 binding unchecked and5.6(e)022(P)/tau uncomputed. Both were computed in the publication's own cited records. Qualify5.6(d)'s every registered snapshot to the enumerated references with certified distance floors;011 is FLOAT and023 was untested. The statement keeps the correct fixed-c canonical and finite-H hypotheses, K=0 case and certificate-only scope. Historical matrix and draft32 bytes were not recovered from their mutable current paths;63 of65 source hashes bind, and this limitation does not affect the underlying accepted proof artifacts.
Evidence: publication42eb222a38caadac911cffc261287892a9f18f60888f211f3e028f560508b320; PROOF 5720a3c058165143cbc622f7de0806c95a44860979da73bc3a611d7af4b37304; result 0ca4af8a7b9e8ddac2cc96a7e77e172d9f441ddff235ff8e0d510d73a5eea15c. No integral or foreign code executed. Later397 acceptance409 and universal upper audit411 are separate post-publication updates.

## T4-413: Independent profile-specific velocity review accepted

Date: 2026-10-29T11:38:49.718309+00:00.
Claim: T4-402's uniform compensated-velocity limit and the exact common coefficient583/1000 for the three endpoint spans are valid under its stated weighted C1 and uniform-tail hypotheses.
Method: Read the complete independent T2 review and all354 lines of its checker. Reconcile the folded-kernel proof, Green mode solution, Cartesian identity and Gram trace argument. Bind all eight frozen review/original inputs; check15 review algebra identities,21 exact span checks, the three exact l1 equalities and rational thresholds, positive Gram determinants and the375 dependency hash.
Result and verdict: CONFIRMED. T4-402 is now AUDITED, including its analytic hypotheses and exact certificate.46 acceptance checks pass. The independent review's finer angular bounds and FLOAT pointwise-profile diagnostics are not needed. The finite-radius discussion uses the weaker cutoff test; its positive error room is not sufficient for the complete radial integral. A retained-shape check follows separately. No finite-radius remainder, H upper bound, inverse or existence assertion follows.
Evidence: reviewffb49200aa1277900c8db4e7749a7a79a193d59ff4c3b0f514c190f22421c9af; PROOF 3f5da5310fccb4feb8dd117dcd4b9f1789e3eccda089a9bdc5d79dc8ba14d32e; result c2d87d383649d56477d7b8415b00777c3a3b557dc2b8ebe9086462fcdf58406c. No foreign code executed.

## T4-414: Retained-shape CI cap for the profile coefficient0.583

Date: 2026-10-29T11:39:53.171754+00:00.
Claim: Assuming the profile coefficient E=583/1000 is valid at every required radius with zero remainder, the full CI351 radial integral still cannot reach any of the four named targets for007/013/014.
Method: Use the audited scalar integral identity of381 with the exact endpoint projection B, independently recomputed pointwise H lower bounds, and exact g0. Integrate the positive part rather than retaining only its support cutoff.94 Arb768-bit and exact rational checks pass, including optional positive reference velocity.
Result: With V=0, cap007=7.6399937715...e-7,013=7.6421438838...e-7,014=7.6407721072...e-7, all strictly below7.643e-7. Necessary common upper bounds on E are0.527596 for the fixed sharpw ball,0.458292 for the sharpw family ceiling,0.434940 for TB and0.181070 for the graded ceiling. Positive V or remainder only reduces the cap. The weaker cutoff test's positive remainder room therefore does not establish a viable0.583 full-integral route.
Verdict: CONFIRMED arithmetic and the previously audited integral identity; OPEN independent review of this application. This is a limitation of the stated sufficient certificate using0.583, not a velocity lower bound or nonexistence claim. A sharper pointwise coefficient may pass these necessary thresholds.
Evidence: PROOF 0e0f608d167b2c3453568d06ccc4ba8319e67e5c2d066e4c4ee6854c8fb3a66b; result e94368caabeca952aa08be744c4df75e840d4d6e73ef9b9f990dfc3b950ffe10; manifest aeac422340c535091f216bd24915ddd88f07b3393723bf4cb3f3cc768b21038e.

## T4-415: Pointwise profile coefficient93/250

Date: 2026-10-29T11:46:04.025214+00:00.
Claim: On each of the three exact endpoint spans007/013/014, sup|V_q[f]| <= (93/250) sup sqrt(q^2 f^2+(f')^2). Consequently the uniform compensated-velocity limsup for an admissible correction with that tail is at most0.372 H_q.
Method: Write a complete informal reduction to quadratic forms, projective direction alpha and physical angle theta. Reuse the audited exact Hessian-mode algebra402. Cover the full projective interval by20 certified dyadic cells per reference, and all theta by1024 intervals per cell. A selected gradient witness gives a lower norm; second-order Taylor bounds in both variables control all values between centers. All 61440 accepted rectangles pass with strictly positive Arb192-bit lower gaps; failed parent cells are bisected. FLOAT is used only to select an arbitrary witness, not for acceptance.
Result and verdict: CONFIRMED finite certificate; OPEN independent analytic/numerical review. E=93/250=0.372, sharper than the mean-gradient coefficient0.583. Three candidates finish in 1.274502 measured seconds at 2026-10-29T11:45:02.539059+00:00. The projection scaling f2=100000P is only a coordinate choice. Neither a finite-radius remainder nor an upper H_q budget is supplied. The universal lower-E theorem remains valid on its larger domain.
Evidence: PROOF 57110fd5b3c62f0fa06b6e6194c53e6d9cf1fac091e89a8a3cd514f38ac9fab6; result bd9d38cb021f4009288a1444e55c5d2ca31dbe9477218a0b30695b531d796520; checker af67e89181b470eebdcd1eb8487e5cbc1e0a8da8ff91a23b676f9d1de43787ba; geometry 4a241764133e76d8d78b56398ebc0d531d80c822c90d9da56444ea4701ef03e6; manifest 699627f6b83a9fe10d6faeac7ee2778606d2f5c2ec15e69e842afd53bb969327.

## T4-416: Actual023 dimension and recorded analytic objective

Date: 2026-10-29T11:58:25.467017+00:00.
Claim: The exact radius25/100 candidate has potential and density dimension2426, with67 analytic objective rows in both recorded stages; all25 public and35 diagnostic probes lie outside that span.
Method: Apply the standalone branch and harmonic-kernel proof; bind every raw shape, exact c and two-stage metadata; independently expand the homogenized Legendre recurrence and check all168 Laurent coefficients at the two distinct poles. Inspect launch, logs and row propagation as text only.
Result and verdict: CONFIRMED. The old basis is a permutation of the first1922 parent016 shapes; the first ordering assumption failed and its proof/code/log are retained. The corrected check confirms the exact set and parent order. All168 fresh25/100 witnesses and7 grouped checks pass. Only parent016 and the two023 stages are independently replayed; earlier history and statistical independence are outside scope.
Measured computation: 0.159437 seconds, completed 2026-10-29T11:55:28.508822+00:00.
Evidence: PROOF b7848590e905055458f72616a9d27f55a30c68c9b3c47203f0bdfccfb5457b44; result f5c30d517cd31c5c6e4f3e33829298e3f8d59f5572a37e6c9b140b4d1e5d2443; checker c1c30d2f1c5c11a973dbe1f4a2d51922fd21ea2b796f08aa04773f3f031d4321.

## T4-417: Actual023 independent local fields and necessary point gaps

Date: 2026-10-29T11:58:25.467017+00:00.
Claim: The exact candidate023 violates all six named scalar point budgets and the original graded family point budget at(1/10,73/100).
Method: Rebuild exact fourth-order radial Taylor data directly from all2426 raw generators and evaluate the polar density, velocity and gradient in1024-bit Arb; compare with the independent Cartesian calculation and recompute every necessary inequality.
Result and verdict: CONFIRMED. F=0.083280868582953659827...; original graded gap=0.062882815459541270946...; every scalar gap is strictly positive. All eight local field comparisons pass. This is a fixed-c necessary-condition exclusion, not global nonexistence or an inverse certificate.
Measured computation: 1.786920 seconds, completed 2026-10-29T11:56:01.471435+00:00.
Evidence: PROOF 1ad317d8290220cb417ea3e5ecbdb82760e31ae0a0cb8e85f1690a26aa82cbdb; result 1fd68e5223cfd8627efbd984831eede62082ad8a9211d6fb8854df89a8d5db7e; checker 8518611bfbe9ced8dc153e0bdacf8843f4313c9061c7b611c694938d45de3def.

## T4-418: Actual023 exact origin normalization

Date: 2026-10-29T11:58:25.467017+00:00.
Claim: Candidate023 has c+partial_y U2(0)=1 exactly and positive density slope.
Method: Compute the quartic origin jet by an independent finite generalized-binomial expansion of the raw generators. Only24 generators can contribute by their exact vanishing orders. Compare every relevant exact coefficient with N4.
Result and verdict: CONFIRMED. All four exact comparisons pass, normalization equals1, and the positive slope is10.30469840811666042438... . The local/contact convention is unchanged. No stationarity away from the origin is inferred.
Measured computation: 0.045548 seconds, completed 2026-10-29T11:56:01.614327+00:00.
Evidence: PROOF ec364dc7a9be28ef0c9b3795c1ca367cbbccd96c0ff0b1ca7643fd95b5b55609; result aeab4fac09314a65fcd75d86abaf508a80fee9e9064fcb0ba6b03bf9cab78427; checker e37d1210433d73ea2ac5588725a45ee7c50f145628ad0e3dfe77afaec72e8481.

## T4-419: Actual023 complete far-field prefix

Date: 2026-10-29T11:58:25.467017+00:00.
Claim: All16 residual sectors at exponent at least-7/2 have the stated coefficients:11 exact zeros and5 nonzeros; the first four leading density and stream profiles equal007.
Method: Expand every raw generator directly in z=r^-2, apply homogeneous differential identities, and assemble all angular products by exact rational arithmetic. Enumerate the exponent cutoff exactly; check Delta psi=-partial_x rho, compare13 common exact coefficient maps with N4 and all16 rows with the published table.
Result and verdict: CONFIRMED. The nonzero labels are(4,1),(9,0),(5,1),(1,2),(10,0), first exponent4gamma-5. All504 scaled generators have Q=4 at radii25/100 and contribute zero to the retained L<=2 prefix. This does not supply a full-plane norm upper bound.
Measured computation: 22.552984 seconds, completed 2026-10-29T11:56:24.231664+00:00.
Evidence: PROOF 025500c420e787e4f8c072f54dbc15e04215559065998fa1c53348d6f9a43ba6; result e63fd9f791dbb54ed4ae54cd148ae4f83aa6f815bb4c7280861d89ead05a60fa; checker aa85c573f75fc183ec9aa8afa0fcac7a7a96b4faeac9626365c135db6d503e66.

## T4-420: Candidate023 independent whole-plane weak distance

Date: 2026-10-29T12:01:55.234369+00:00.
Claim: Under the exact canonical weak-stationary correction hypotheses in the standalone proof, candidate023 has correction L2 distance strictly greater than2634958245163687/10^18.
Method: Independent polar reconstruction from all2426 raw generators, exact complete angular assembly, CRT numerator identities at the distinct positive factors1+624v and1+9999v, and direct2048-bit Arb hypergeometric evaluation. The probe is(n,K)=(19,1800). No radial or angular truncation is used.
Result and verdict: CONFIRMED. Radius enclosure [0.002634958245163688142000861001805447642760571275449231977977329443880991628099259072358160066873062301 +/- 2.31e-103]. All63 scalar moment groups pass, minimum nonzero accuracy1935bits. All six physical field comparisons, both residual pairings, eight final comparisons, full R1 calibration, six scalar fixtures and the complete gradient critical-point certificate pass. The strict floor exceeds the original graded ceiling as well as every registered scalar ceiling. This is a necessary-condition exclusion, not global nonexistence, an inverse, or existence closure.
Measured computation: 146.989488 seconds; completed 2026-10-29T11:58:51.408037+00:00.
Evidence: PROOF 5b8f6a0736b5b28bd51753fd617b68314df9f39a350b97124fa38e521ed09cfa; result bf3bcece42f9148d6100c032be16f732acc53368f813f7c98173082e157d2af2; checker ca4a222bf1f1937e6fd7cf1cd0c5b6157c92591cc40c7a86407544be77043e93; raw d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df.

## T4-421: Independent audit of the current remainder at campaign radii

Date: 2026-10-29T12:04:41.281633+00:00.
Claim: T2 the review of T4-410 claims the T4-410 uniform velocity majorant with the present positive delta-term cannot pass the registered endpoint CI at any of four targets for007,013,014.
Method: Re-derive the lower bound from A>=H(1+L0)^epsilon, epsilon<=delta, and C_a+L_a>=Sigma. Reconstruct the exact endpoint projection and rational-angle H lower bounds, then check all non-FLOAT table bounds independently in768-bit Arb.
Result and verdict: CONFIRMED main obstruction and all180 finite checks. At sharpw J/H>=3.974970,3.974957,3.974975, exceeding the allowed absolute constants by factors>5.829224,5.828903,5.829124. REFUTED the assertion that a general CI starting radius must satisfy R<=r_grad: only max(R,r_grad)<=r_beta is necessary. The main obstruction uses only R<=r_beta and survives. The stronger structural variant is CONFIRMED only under its same-coefficient and R<=r_grad hypotheses. FLOAT threshold searches and heuristic improvements remain OPEN.
Measured computation: 0.011134 seconds, completed 2026-10-29T12:03:51.245113+00:00.
Evidence: PROOF 93f001802c42ef67be3f4ddfdd599b299dec0c57d8637a86d6c6e7f289e317a9; result 54e4b223db4f2891ec83fcb093a6fa56f0194f128c9a9685e30dbdd0222f6ad2; checker bb69666623d6303c48c5aaaa97ebfdc45189085bb5fecd6f45677dc6ef6c3567.

## T4-422: Complete radial-integral ceiling with profile coefficient93/250

Date: 2026-10-29T12:04:41.281633+00:00.
Claim: Evaluate the retained-shape CI ceiling for007,013,014 with E=93/250, V=0, zero finite-radius remainder and no other error terms.
Method: Integrate all three radial powers exactly, use conservative integer H lower bounds verified against the exact endpoint pointwise formula, and evaluate outward768-bit Arb caps and all four target ratios.
Result and verdict: CONFIRMED conditional arithmetic and59 checks. Caps are8.913980874769618785e-6,8.916489523349172026e-6,8.914888999746365613e-6. Ratios are about6.756/6.758/6.757 fixed sharpw,3.128/3.129/3.128 sharpw family,2.350/2.351/2.350 TB, and0.01950 graded. Thus this hypothetical ceiling passes the three scalar necessary thresholds but not graded. It supplies neither an achieved distance certificate nor existence. The actual finite-radius input is blocked by421; independent review of415 remains pending.
Measured computation: 0.009047 seconds, completed 2026-10-29T12:03:51.345001+00:00.
Evidence: PROOF fb03764b22fd8ab33a6da10b2422d0678a36bc3951fc2fac643204a3f2b45302; result 2d23b763e2bf9aa1a9caaafd427f61f19a87c8405a54a3216a7c59e3ee301d21; checker b8c8154955dd5ad8bc5f1ce3efe65648c7468998660623ffe53bb7170242a82c.

## T4-423: Acceptance of the full retained-shape radial integral

Date: 2026-10-29T12:12:12.350604+00:00.
Claim: The complete T4-414 theorem and all directed numerical comparisons in T2 the review of T4-414 are valid.
Method: Read the independent proof and full checker, verify its seven algebraic identities, and recheck all204 numerical bounds using exact endpoint data and768-bit Arb.
Result and verdict: CONFIRMED full414 theorem and arithmetic, now AUDITED. All212 own checks pass. The0.583 ceiling misses allfour targets. The finite-radius discussion is audited separately with radial averaging.
Measured computation: 0.015673383 seconds, completed 2026-10-29T12:08:20.584268+00:00.
Evidence: PROOF 865eb8423aeae53ee84452d8fcb06348d2829c295f913578ec1eba009e7d5232; result f99be88192b260f9b20c2f4ecb5b0ee86ddc20c06a1922e05a161886d79ac932; checker 9d88dfc907d7cf654a5b8d6beb6eebad55e3b0069995be30cdf37f4857f67df7.

## T4-424: Acceptance of the complete two-weight velocity theorem

Date: 2026-10-29T12:12:12.350604+00:00.
Claim: T1 R1-043 confirms every analytic claim of T4-410.
Method: Read the full review and checker, verify the complete canonical kernel proof, and independently check the finite display inequalities in768-bit Arb.
Result and verdict: CONFIRMED full410 theorem, now AUDITED. All25 own checks and22 peer groups pass. Peer C1,C2 and finite-point A12 are FLOAT. Repair printed upper bound0.785063 to0.785064, lower radii to3.16e7,1.15e7,4.29e7,8.69e7, and lam2 lower bound to1195.78. No finite-radius closure follows.
Measured computation: 0.002713508 seconds, completed 2026-10-29T12:08:20.709071+00:00.
Evidence: PROOF 0c2d360a304f04f5b022144f7d9c42b3b681fa4dab3a00de68a5de4d27f04ceb; result dec925fba2ed41f3a0ea5b2e50c5d08b4af29784a00ef720ac6ea0f28abd7af7; checker 219c2c5290eab7d0be1125a47581659bca5ce348dd062cceaed9e91921eb7344.

## T4-425: Radius averaging does not rescue the current remainder

Date: 2026-10-29T12:14:44.774722+00:00.
Claim: T1 R1-043's radius-dependent obstruction persists even when410 is combined with any valid norm-class universal velocity coefficient, using the current positive delta-term input.
Method: Derive the exact radial Green averaging operator. Construct a common pointwise lower envelope for the chosen majorants, handling s<5 and all varying R0,epsilon. Integrate the envelope explicitly and reconstruct all12 endpoint-target cutoff constants in768-bit Arb.
Result: All109 checks pass. The universal floor is0.7930365064225140883557111110; its switching radius is302748.4007664045; the averaged floor at18860 is0.7930361911778637328405552269, strictly above0.79303. Every cutoff requirement is below0.785064. The original current-universal case is also confirmed, with exact-envelope average1.745480614 and the T1 coarse bound1.727790118. No assumption R<=r_grad is used.
Verdict: CONFIRMED finite arithmetic and the corrected R1-043 radius argument; the stronger new analytic statement is OPEN independent review. The obstruction concerns the specified majorants and current tail list only. It is not a lower bound on actual velocity, a nonexistence proof or an unconditional candidate exclusion.
Measured computation: 0.010357245 seconds, completed 2026-10-29T12:14:01.688614+00:00.
Evidence: PROOF 4d13c623b32b738f78fe7963b67fe4548b5617f24b839be5dc2fe35383155bf3; result 69f36c4a52298dc8f8b85c30548ab845eebb3d56e0f5a542c51babe05bbc5171; checker a90f3228affe199004449ddde10da105896244952f801b5281df84df74a14fd2.

## T4-426: Outer amplitude alone blocks the current remainder route

Date: 2026-10-29T12:24:07.048992+00:00.
Claim: T1 R1-044's outer-only obstruction and necessary kernel thresholds for all twelve endpoint-target pairs.
Method: Independently derive the radial averaging and fallback inversion, reconstruct B,Phi,g0 from exact angular data, compare421's intervals, and check all36 hypothetical kernel thresholds in768-bit Arb. The standalone proof predates the checker; no peer code is executed.
Result: All316 checks pass. The optimistic outer remainder has J/H>3.756 for fixed sharpw, >4.324 sharpw, >4.556 TB, >10.94 graded. Its radius average exceeds each K by more than4.34. A fallback based on the relaxed0.793 has averaged coefficient>0.7929999, still larger than every K<0.785064. The printed lower bound>=0.7930 is false: the smallest value is about0.79299998591205438445. All table entries are verified, including the93/250 fallback thresholds<8.647 sharpw,<7.287 TB,<14.41 fixed sharpw, and no room for graded.
Verdict: CONFIRMED R44.1 and the necessary-threshold table, with these repairs. REFUTED the literal>=0.7930 bound and describing0.793 as an admissible universal coefficient; it is a relaxed lower bound. A smaller positive velocity constant alone does not remove the delta exponent because the coefficient includes HV/D. No assertion is made that dropping the inner amplitude yields an actual velocity upper bound. No sufficient closure condition or nonexistence result follows.
Measured computation: 0.015611086 seconds, completed 2026-10-29T12:23:37.925045+00:00.
Evidence: PROOF 935e166fdaaf4d79fbb421117803cc780845bb30d9ab02bbcbf43b6da3234aa4; result fd5cc1d1d2f3e30be095cc131ccc20e74b8f9566bf8a0303a9b49b71e3d7a913; checker 280c45172a8bb2a5358b0aadf870284421bb0a75d7ee0f66f6797f1d8e10e93f. Frozen T1 review54f06c10339f98795fac85b338f63d855baa209883540bf2172f506cd6bbaf1e; later published review may contain wording repairs.

## T4-427: Actual024 dimensions, objective and historical hash reconstruction

Date: 2026-10-29T12:30:25.051048+00:00.
Claim: The actual024 potential and density spaces have dimension2174; all60 listed diagnostic probes lie outside its67-row analytic objective span.
Method: Rebind the independently proved two-scale2426-dimensional space and restrict the radius100 coefficients to zero. Compare every actual shape with parent016 and the exact013 quotient. Inspect launch, objective propagation, metadata and all iterations as text; reverse the single heading edit in the held-out record and hash every byte.
Result and verdict: CONFIRMED, all87 checks pass. The recorded trial makes12 attempts,5 accepted and7 rejected. Both the radial order16 to32 and CPU to CUDA backend changed, so a one-variable comparison is REFUTED. The held-out hash explanation is CONFIRMED exactly; save times09:13 remain independently unobserved. Two immutable MID16 index labels are REFUTED. Only parent016, quotient013 and the024 launch are checked here; statistical independence and earlier optimizer history are outside scope.
Measured computation: 0.535539029 seconds, completed 2026-10-29T12:28:56.762012+00:00.
Evidence: PROOF 7e76ce5e6951dd47249c17687d5d664f1da3b09dca8c05cf902465c58ea4c7fc; result d9dbfdf586ca696f09c287b890c41d9636257ac092b8301a2878bb01ada29ef1; checker a7e6fa87a905b4112a456b133c3e92f994a8ab6593f76bb6c19ddd317d335e3b; raw3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d.

## T4-428: Actual024 independent local fields and necessary point gaps

Date: 2026-10-29T12:30:25.051048+00:00.
Claim: The exact024 candidate violates all six specified scalar point budgets and the original graded-family point budget at(1/10,73/100).
Method: Rebuild fourth-order radial Taylor data from all2174 exact raw generators. Evaluate the polar density, velocity and gradient with1024-bit Arb and compare the independent Cartesian record. Recompute each necessary inequality.
Result and verdict: CONFIRMED. F=0.095280877528863606879... and original graded gap=0.074870039634554045471... . All eight physical-field overlaps and all six positive scalar gaps pass. This is a fixed-c necessary-condition exclusion, not global nonexistence or a background inverse.
Measured computation: 1.688126483 seconds, completed 2026-10-29T12:25:25.452510+00:00.
Evidence: PROOF 9801f71f1a470e080a325204c1c84cfbaab479e030d51288fe43d1d9243c29ac; result e252fb1a7cc031e9a5a039d03085bd8ae60c296e7a327bb1f552ac81dac22449; checker cc6c598b95fdae98d5d4a7039b937cae1fa662ed0255e0a72bed3b03f109d99d; raw3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d.

## T4-429: Actual024 exact origin normalization

Date: 2026-10-29T12:30:25.051048+00:00.
Claim: The actual024 reference has c+partial_y U2(0)=1 exactly and positive density slope.
Method: Evaluate the quartic origin jet by a finite generalized-binomial expansion of the raw generators. Exact vanishing orders leave24 contributing generators. Compare the strain, slope and two quartic coefficients independently.
Result and verdict: CONFIRMED. All four exact comparisons pass and a0=10.312002863308989066273...>0. The normalization includes the unchanged canonical local/contact convention. This does not imply stationarity elsewhere.
Measured computation: 0.045805287 seconds, completed 2026-10-29T12:25:25.624605+00:00.
Evidence: PROOF b151176fffd242583f9fee5ece5d5acd8e948788774575f8e180b01fb8c2d357; result d0e99fd9ad2afb15ecfd8b5b01a3344c0b68c6dd382e6a657517b0387a119102; checker a14f3c73ad9a2dcf291e36cbae375346ca4428122a313230c171d904f778de24; raw3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d.

## T4-430: Actual024 complete far-field prefix

Date: 2026-10-29T12:30:25.051048+00:00.
Claim: The entire024 residual prefix at exponents at least-7/2 consists of16 rows,11 zero and5 nonzero, with its first four density and stream profiles equal007.
Method: Expand every generator in z=r^-2 with exact rational arithmetic, differentiate by homogeneous identities, and assemble all angular products. Enumerate the exponent cutoff exactly and compare13 common coefficient maps and all16 published rows.
Result and verdict: CONFIRMED. Nonzero labels are(4,1),(9,0),(5,1),(1,2),(10,0), with first exponent4gamma-5. All252 scaled generators have Q=4,R=25 and vanish from the retained L<=2 expansion. No whole-plane norm upper bound follows.
Measured computation: 22.245663654 seconds, completed 2026-10-29T12:25:47.934232+00:00.
Evidence: PROOF 5cb2e5fe0e0a36186bb6e8d892f7720e5d27ce6a6bd1710d5ac0289a541e42dd; result c42057b9eabe3bfa4ff4de8d7469e21949c501814007ef613fa551886c8c806b; checker 2789797a5f0e452a9518c14f12e63143945b4a9892a6f7b4180d94c4cd8a7003; raw3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d.

## T4-431: Actual024 independent whole-plane weak correction distance

Date: 2026-10-29T12:30:25.051048+00:00.
Claim: Under the canonical weak-stationary fixed-c correction hypotheses in the standalone proof, the actual024 reference has correction L2 distance strictly greater than1556067368832641/10^18.
Method: Reconstruct every polar field from the2174 raw generators, retain the complete angular products, and integrate every scalar moment by exact CRT identities and direct2048-bit Arb hypergeometric evaluation. The complete probe is(n,K)=(19,1800), with no radial/angular truncation.
Result and verdict: CONFIRMED. The radius enclosure starts0.0015560673688326428286727171. All63 moments pass with minimum nonzero accuracy1937bits, together with both residual pairings, eight final overlaps, six physical fields, complete R1 calibration, six scalar fixtures and every gradient critical point. This floor exceeds the original graded ceiling and all registered scalar ceilings. The actual denominator uses1+624v; the unused second factor1+2499v is independently exercised in fixtures. The conclusion excludes these balls, not the profile problem or other correction spaces.
Measured computation: 125.564778706 seconds, completed 2026-10-29T12:27:53.700736+00:00.
Evidence: PROOF d0b409da2c491469be4e3d4333251bf2af614691395d95804c52ce9ac18f8cc3; result ee1d08b9e3effc10598ca3b18c74587d9ce428f06e29e5e0f8555f26dc14f47d; checker 98e988012926223486209dd2e0dc8b91d4956baf0f95caee7da1c96d9c8c12d9; raw3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d.

## T4-432: Radial-averaging theorem accepted through R1-045, with outer-only extension

Date: 2026-10-29T12:34:32.024092+00:00.
Claim: The full425 theorem is independently confirmed, and its conclusion persists for any valid majorant retaining the current outer amplitude alone, with universal list coefficient Ebase>=Emin.
Method: Read the full T1 R1-045 review and its independent exact/Arb checker as text. Reconstruct the angular data and all12 target inequalities in768-bit Arb, rederive the outer envelope and its Green average, and check every source binding. Freeze the intact T2 review and compare the historical incident bytes exactly.
Result: All190 own checks and16 frozen peer groups pass. The outer-only averaged floor is strictly greater than0.79303648 at each r_beta, while every critical ratio is below0.785064. The full425 analytic theorem, small-radius case, radial integration and target comparison are accepted. R1-045's four errata to R1-044 are accepted;0.793 is a relaxed lower value and the VH contribution retains the delta exponent. T1's locked R1-044 changes no underlying claim.
Verdict: CONFIRMED. T4-425 is AUDITED. The outer-only extension is independently confirmed under the explicit noncircular list hypothesis. These results obstruct the stated majorants, not the actual velocity or existence in another framework. Historical425 contained the incident copy c0e299a4...; this acceptance binds intact20ee1bb3... and verifies that only metadata and one display's extra digits differ. The first provenance normalizer was too broad; its failed code/log are preserved, and the corrected line-specific comparison passes.
Measured computation: 0.014927897 seconds, completed 2026-10-29T12:33:55.755856+00:00.
Evidence: PROOF c2035403ef932424d6fc797376675919702bae7f86ef3c46ce0874af29fc4e8c; result 9c46cc69fc4e8340b3cb383092fcedea1d05dfce36f49484250ea17c8da3841c; checker ca309686d1b32d35f85e27c6f0c0014f13273c1bf3b2b4615bde29a36874e475; peer review dcd62d661e4bb18b72277843a819d3574bf1a70332d546de09a0013f2bac66f1; peer checker a70a1512db660f802c41f981974f7873763e3229eb50fef00ba620097927f8dc; peer log 8d83f7e8f1a509cc79c52806629a89d77ff0239f9b4b594ba6d5efbcf43ec40d.

## T4-433: Independent audit of THEORY_FINAL draft34

Date: 2026-10-29T12:45:32.371901+00:00.
Claim: The changed theory and closure arithmetic of the frozen1655-line draft34 are valid under their explicit hypotheses.
Method: Read all989 difference lines against accepted draft24 and follow the new theorem dependencies, retaining their domain, normalization, finite-radius and stationary-versus-universal distinctions. Recompute the19 table rows, six new023/024 ratios, exact sharpw rate, self-map slack, contraction and family ceilings. Check18 frozen inputs.
Result: All79 checks pass. Exact high rate63092119/405000000 gives the stated inverse bound; the lower-rate self-map has positive slack7/1557000000. The family ceiling is below2.8496e-6. The necessary new commutator constant is below775390625/2554506927217<3.04e-4. No closure is established. PROOF.md lists eight status/wording repairs, including023/024 exclusions,414/410/425 acceptance,382 acceptance of R1-039,016's smaller confirmed G0, the upper-bound existential quantifier and the fixed-fallback scope of the1.72 illustration. A full CI may start beyond r_grad; the cited draft comparison correctly states its extra condition.
Verdict: CONFIRMED changed mathematics under its hypotheses. The unrestricted1.72 interpretation is OPEN; its fixed-fallback calculation does not prove it. Current-status repairs are required before the next consolidated version. The review does not certify unseen later edits. The first checker failed only on a line-wrapped literal text match; its code/log are preserved and the whitespace-normalized check passes.
Measured computation: 0.008670877seconds, finished2026-10-29T12:41:51.586921+00:00,256bits.
Evidence: PROOF 8f6f8232bc5660c56ec7765349794eb5e66a9f8c386e5a68bbc38b67442cf502; result e6de0e68fa9ef9d7bea76f15a7e771081c4e3aee79b955b4911f4c66538dd8ed; checker a12055c99689cb39a238fe0bb5c1eaaa6c1a8db9cb4f6715dc787801319edfb6; frozen draft febf6c09e19a2e6b585c5263348250017d4af86fca9aa731db89fbc6d6106b40.

## T4-434: Pointwise-profile theorem and radial cap independently accepted

Date: 2026-10-29T12:50:01.351528+00:00.
Claim: the review of T4-415 confirms the exact angular inequality N(z)<=(93/250)G(z), its asymptotic consequence and the T4-422 conditional radial caps for007,013,014.
Method: Read the full review and all578 lines of its checker. Reconstruct its independent17-cell projective certificate with the accepted exact angular algebra, verify all78336 rectangles at384bits, and bound each denominator globally on8192 cells for the three rational coefficient witnesses. Independently compute the cap, optimistic V=v0 version, thresholds, rooms and remainder ratios. Verify23 source bindings and the restored414 hash.
Result: All341 checks,78336 angular rectangles and24576 denominator cells pass. The coefficient lower bounds are0.3714757,0.3714938,0.3715026. The V=0 caps remain8.913980874...e-6,8.916489523...e-6,8.914888999...e-6. The current remainder exceeds the sharpw room by at least46.06, TB by66.54 and the fixed-ball room by22.19. For larger radii use the already audited radial-average obstruction. The lower coefficient bounds concern the angular inequality, not every stronger stationary estimate. Peer 'equal' gap wording is relative-tolerance agreement; acceptance of each certificate uses strict interval positivity.
Verdict: CONFIRMED with the explicit scope clarification. T4-415 and T4-422 are AUDITED. No finite-radius or existence conclusion follows.
Provenance: The old launch/log at11:44:12/13 belong to the E=3/8 trial. The final E=93/250 result at11:45:02 includes source hashes and actual UTC but no separate historical launch/log is asserted. Old files are retained. The restored the review of T4-414 equals221b113543dc815315d771563c9c0b9618919663db794720f55887169221ab51. The review's correction of its earlier pointwise radial substitution is accepted.
Measured computation: 7.566933458seconds, completed2026-10-29T12:48:49.893037+00:00.
Evidence: PROOF 8848da16d556cb0089a56a3fb41d09f9b98dc3a2e0d4985843f59300e0075674; result 1b36315ea49aa19d5c5f37c7ab5ddd9241192a028946731c4d30f323d1bc23c1; checker 006d79dd303764d842c215dc449edf2fe61808f34a6981b55d408431c15dc484; review ee7b1b1b7d9bc92c2fba61324c25b39aa4178c75a42296bbe7b444c8959671e8; peer result 59034a6c3f429a5c68e0809b7ad2e8ff1b1c5822bb031af90ff98c070c06765a.

## T4-435: Numerical publication v12 contains incorrect universal FLOAT comparisons

Date: 2026-10-29T12:56:54.374878+00:00.
Claim: The GPU-phase summary of numerics_v12 accurately describes its printed probe tables; the frozen NUMERICS_FINAL does the same for026.
Method: Read the full v12 and affected final sections. Parse50 registered rows, compare positive decimals as exact rationals, verify9 source bindings, and check accepted023/024witness factors and graded-gap balls. No candidate diagnostic rerun.
Result: All67 checks confirm the counterexamples.025 K600 mode19 increases24.94-fold while four other modes fall. AtK1200mode25 rises3.49-fold, modes29and31 fall. AtK1800mode31,024 rises1.57-fold and023 rises3.37-fold.026 K600mode19 rises2.508-fold, contradicting a uniform5to50-fold decrease. The expected factors for023/024must be rounded down as already requested by coordinator.024status is stale and MID16loss labels are wrong for024.
Verdict: REFUTED for the universal FLOAT ranges and all-MID16label. CONFIRMED for the corrected internal comparisons and witness factors. These are reporting repairs; underlying FLOAT values are not interval-certified here and no existing exclusion changes.
Provenance: Initial bound1.408for1.27e-3/9.02e-4 failed and was corrected to1.4079before publication; a numeric parser consumed trailing punctuation and was repaired. Both failed attempts are retained. Final checker completed2026-10-29T12:56:09.783837+00:00 in0.006246885seconds.
Evidence: audit record numerics_v12_audit, proof 026501ef13ee36ddf79f98725e55c32d204d2c0639d41afdbef9a36e0346dc26; result c4333b5b6163939dd9f0b3ca86f9bb4300ff3dce8771215ea4221051bf3ea0a1; checker a09ddbbb7f9b2f5771e97e2de0c36056ed4be4e23c8b1cd6a14e41e469997f05; publication20763c86645a954697bb617b57efc7d81f7afbbcd3aa173d5ee4d00d352bae9c; frozenNUMERICS_FINAL 7e6e685209510dc5d6518047e0686aabc00e63ce5872d35cea2844bd4543f25e.

## T4-436: Actual025 exact dimension and analytic objective audit

Date: 2026-10-29T13:03:03.562917+00:00.
Claim: C1-N1-025-combined-heldin1e16 has2918 independent potential generators and density images; its46 diagnostic probes lie outside the81-row analytic objective span.
Method: Rebind the old1922-rank result, compare every actual ordered shape and exact rational parameter, independently expand348 homogenized Legendre numerators at all three poles, check six cross-pole values and36 noninteger conditions. Inspect the recorded launch, parser, split weights and all60 iterations as text. Prove radial monomial independence after angular projection.
Result: All554 checks pass. The new count is996 over the old space,744 over016. Objective weights are10^12 on67 rows and10^16 on14 added rows. There are39 accepted and21 rejected attempts; accepted displayed mesh steps sum0.08387595, a FLOAT diagnostic only. The dimensions precede421 recorded constraints and do not assert the tangent rank. Both immutable manifest descriptions terminate at 'at weight ' and omit10^16.
Verdict: CONFIRMED within the exact stated spaces and recorded-history scope. REFUTED for completeness of the two manifest descriptions. OPEN independent comparison with N4's eventual025 result. No norm or existence claim.
Measured computation: 0.416744326seconds, completed2026-10-29T13:02:29.175753+00:00.
Evidence: PROOFb4257d03f59aeee241404a618c7d16b6c07716fc5e521bbb42804dbb53069f20; result36d1857d6b96b8addb380b03ed85b295604c2a33d5f251e5d550f45f63239611; checker2e1e0d4a0362af163423bf64646147ed474c3b3a529c5c39196a2bdf1f5b7ff6; raw3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17.

## T4-437: theory_v08 factor table, corrected sharp norm and separate scopes

Date: 2026-10-29T13:11:29.119435+00:00.
Claim: T1 notev47's24 factors use correctly matched lower quantities and upper thresholds for007 and are necessary closure failures.
Method: Read the full proposed table and arithmetic program as text; parse its literal rows without executing it; bind23 source/acceptance files; independently divide exact rationals and compare every numeric direction against accepted containing balls at512bits. Read the relevant domain, tail and coefficient proofs.
Result:114checks pass after correcting S2. Sharp at(s,w1,w2)=(1/7744,2^14,2^18) has516.9717852723<X<517.5527701453. Its proposed756.5312630768 numerator is above its upper bound and belongs to sharpw. Replace S2's factor9925756.87 by6782715.40. Every other printed factor is conservative within its stated scope. Chosen0.372/0.583 coefficients, sufficient norm tests, ball exclusions, universal-class obstructions and current majorant failures have different quantifiers. Decimal down-rounding is10^(-k)floor(10^k p/t), not literally floor(p/t).
Verdict: REFUTED original S2 lower bound and global claim that all24 are necessary for every closure proof. CONFIRMED corrected24 arithmetic comparisons and the separate scopes in PROOF. OPEN high inverse/localization/stationary-H/alternative-tail framework. No existence conclusion.
Measured computation:0.006298556seconds, completed2026-10-29T13:10:49.511713+00:00. The earlier109-check run is retained before adding five acceptance/proof bindings.
Evidence: PROOFb7c3e467fdc2a8cf664453730a84c2dd49122063bc5459ef9fcd2b8abc92e48d; result043acbe315823e762c8723ffbb5c89b9716fc267a316082c386752426b7f1b82; checker35e830ba61381448eb2369b52d36e3586c23013a8c33c49dc01279aefd563cc9; frozen T1 table programc458e24e1f070f6880aeb6f3074ac81390ad7cd9065e26415d25ef9e1cf6dc53.

## T4-438: Actual 025 independent point exclusions

Date: 2026-10-29T13:18:02.363202+00:00.
Claim: The exact 025 reference fails all six specified scalar point budgets and the original graded-family point budget at (1/10,73/100).
Method: Rebuild fourth-order radial Taylor data from all 2918 raw generators, evaluate polar fields at 1024 bits, and compare the independent Cartesian record. Recalculate each necessary inequality.
Result and verdict: CONFIRMED. Residual F=0.090271148155392282742...; original graded gap=0.069881270806748353645... . All eight field overlaps and six positive scalar gaps pass. This is a necessary fixed-c correction-budget exclusion, not a background inverse or a global nonexistence result.
Measured computation: 2.029328342 seconds, completed 2026-10-29T13:12:03.835650+00:00.
Evidence: PROOF 6d795defef60a41d14b32c2ff77ce03bb3a8666e894e7e7be38802148b3ab04f; result 54a7ab5cac657fbc463d9635361efe1f5fe64f27fd6d72af2d10571e99bfc2a6; checker 84a3859bb34b9b369c7938a10195a385b2443deb0b20ff377819a12a1eef2a78; raw 3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17.

## T4-439: Actual 025 exact origin normalization

Date: 2026-10-29T13:18:02.363202+00:00.
Claim: The exact 025 reference satisfies c+partial_y U2(0)=1 and has positive density slope.
Method: Evaluate the finite generalized-binomial quartic jet directly from the raw list and compare the four rational origin quantities independently.
Result and verdict: CONFIRMED. Exactly 24 generators contribute; a0=10.308511991999799401177... and c+strain=1 exactly. The canonical local/contact convention is preserved. No stationarity away from the origin follows.
Measured computation: 0.051559538 seconds, completed 2026-10-29T13:12:04.032176+00:00.
Evidence: PROOF 88b01d4f5e77b8abb91eabf30ca6d8b8161346f5fd988589b25580ec35c7f821; result bd943389d9786eec1aa6f470f2ae747b771785933558d44d306744e488b31a7c; checker 69263a10547edfc7df69e4bf48b77adbd35ca49af02c1b9998dc8f6a017170c2; raw 3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17.

## T4-440: Actual 025 complete far-field prefix

Date: 2026-10-29T13:18:02.363202+00:00.
Claim: The entire 025 residual prefix at exponents at least -7/2 has 16 rows, 11 zero and 5 nonzero, and its first four density and stream profiles equal 007.
Method: Expand every generator exactly in r^-2, differentiate by homogeneous identities and assemble all angular products. Enumerate the exact exponent cutoff and compare all common coefficient maps.
Result and verdict: CONFIRMED. The nonzero labels are (4,1),(9,0),(5,1),(1,2),(10,0), with first exponent 4gamma-5. All 996 added scaled generators have Q=4 and radii in {25,50,100}; none changes the retained L<=2 profiles. This gives no whole-plane upper norm.
Measured computation: 22.387691186 seconds, completed 2026-10-29T13:12:26.477680+00:00.
Evidence: PROOF 88b9c219728bb13448468ca5d064a0262f6b0cc55d8a73cbeee187e28b2213bf; result a017e4cd49f2a94b0debf7b71f3c226c162a896f49768f4d8b2d81e857e25d56; checker 846b64054238ae92111ab399a481c816ca46287aeb570b5b35576892db2d5ae6; raw 3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17.

## T4-441: Actual 025 independent whole-plane correction-distance floor

Date: 2026-10-29T13:18:02.363202+00:00.
Claim: Every correction satisfying the canonical weak-stationary fixed-c hypotheses of the standalone proof has L2 norm strictly greater than 516450316394513/250000000000000000.
Method: Reconstruct all 2918 polar generators, retain every angular product, and integrate all scalar moments by exact CRT identities and direct 2048-bit Arb hypergeometric evaluation. Use the complete probe (n,K)=(19,1800), with three distinct denominator factors and no spatial truncation.
Result and verdict: CONFIRMED. The radius starts 0.0020658012655780539356552873; the strict rational floor is 0.002065801265578052. All 63 moments pass with minimum nonzero accuracy 1933 bits. Both residual pairings, eight final comparisons, six physical fields, the full R1 calibration, eight fixtures including repeated triple poles, and every gradient critical point pass. This excludes every registered scalar ball and the original graded family under their hypotheses. It does not exclude the decaying-weight dyadic family or another correction chart.
Measured computation: 194.455858890 seconds, completed 2026-10-29T13:15:41.145536+00:00.
Evidence: PROOF d7689362724aa9ac9c3de761a54e75173bef191ae9d76c583e8a9a643ebaef46; result acba0e2a9c96f10989f8337babe2887a662fd15a89bacb3027ccae863e374416; checker 60724f9391f3b59195dff35d7edd57ac196e198e4a2d210787f0e9f01f46238a; raw 3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17.

## T4-442: Independent audit of theory draft 38 and the two-endpoint dyadic implication

Date: 2026-10-29T13:20:27.112679+00:00.
Claim: The changed conditional mathematics of frozen draft 38 and its new 016 seven-cell implication are valid in their stated spaces.
Method: Read all 124 word-change blocks (743 lines), rederive the projection monotonicity, exact maximizer of H, two-endpoint cover and polar Laplacian identity. Recalculate all 21 table rows, conditional closure arithmetic, seven cell inequalities and current radial-average consequences at 512 bits. Bind 22 frozen inputs and the two complete independent N4 mode records. No third candidate integration is claimed.
Result: All 548 checks pass. The minimum 016 ratio is above 1.253908386497. The 93/250 coefficient and caps remain AUDITED through 434. Exact lambda is greater than 109.6024, so the printed equality is false. The two-projection J(1)=13.758675979450936... is below 13.758676, so the printed lower inference is invalid; use >13.75867597. Section 9 omits the piecewise r<5 qualification already present in section 3.4. The factor >4.34 belongs to the outer comparison without the fallback. Other scope repairs are in PROOF.md.
Verdict: CONFIRMED changed conditional mathematics and the source-bound seven-cell consequence. REFUTED the exact decimal equality and the upward-rounded projection inference. OPEN the unqualified small-radius intermediate formula and missing inverse or stationary-only hypotheses. The actual full N_1 is not proved below the rounded number. No existence conclusion follows.
Measured computation: 1.781524884 seconds, completed 2026-10-29T13:19:47.053421+00:00. The first finite checker used the full-envelope field instead of the outer-envelope field in the final comparison; its code/log are preserved. The corrected named field passes.
Evidence: PROOF 6d890545d3384c2e8c0d407d693dda837b4cad7b25d5498fa393c0ec10285399; result 3f9e5256179ea88daad4424fb811155eba8a5fb5a48ebec92f8526b1e05b41dc; checker 690ad6b1e61aeabd160cbebb90751df50ded8aa6cbc16e3cc4884a091b3d4e6c; frozen draft ccaa8623477ffdffbb977e866e669cffc9546a657eade246d053941ea0162a02.

## T4-443: Independent audit of T2 endpoint falsification and its new whole-integral bound

Date: 2026-10-29T13:26:31.808867+00:00.
Claim: T2's finite-radius upper bound for the whole CI integral, in the T2 falsification review of the endpoint and the report summary revision 1, is valid and supports the current-list obstruction at all thirteen printed target radii.
Method: Read all 204 lines of the review and all 579 lines of its checker. Write a separate proof of the split-integral inequality including M<R. Independently reconstruct B, Phi, g0, v0 from exact endpoint JSON, evaluate nine chosen-M bounds at 768 bits, and check all 39 target classifications, their directed displays, the old and current constant-coefficient caps and the exact graded R1-038 threshold. No peer code was run.
Result: All 948 checks pass in 0.040476816 seconds at 2026-10-29T13:25:57.875694+00:00. For the current list with floor min(1.747261,lambda*(5/s)^delta), the whole CI value is below 2.66323e-8<2^-25. With the universal lower floor Emin and H>=Phi,V>=v0 the upper bound is below 1.14141e-7<2^-23. Without V it is below 1.43912e-7. T2's numerical displays in sections 1 to 4 are independently confirmed. The exact graded ceiling has R1-038 threshold greater than 7.942167, while the printed rational target has threshold below 7.9417.
Verdict: CONFIRMED the new integral theorem and scoped finite consequences. REFUTED the inference that passing a necessary condition disproves a universal obstruction, the claimed equivalence 'exactly when', and membership of Emin in the class of actual admissible universal constants. OPEN whether an improved valid universal coefficient can reach either small Db target. The stale 9.28e-11 current claim lacks its previous derivation; a larger upper bound does not refute the smaller upper bound for the actual full CI value. One-unit brackets are verified as mathematical brackets, not inferred from the bare phrase 'rounded up'. No inverse or existence closure.
Evidence: PROOF 972ac08e7af8600550f83cbc03e8e6bf327fc166ebcb2eea91f881506ae56c6a; result ee10abf8872809ccf6b891d7962d66ec381a586fb358a2534ab3addee8754c2c; checker 568c99a0db2d12e9cc17fae1fcad92c16b4becebdc25c1796900400abf93ac79; T2 revision1 6eede4644e0f5c82859909135e7ed0c6031b871a5e069228107ab93a06e2c1cc, peer result 182605610a32ed0f7030f0282cc14a2a9f75639da99fcbaad51c3ad261eb03d2.

## T4-444: Reciprocal acceptance of N4-365 actual025 structural comparison

Date: 2026-10-29T13:28:05.887869+00:00.
Claim: N4's independent expanded generator records agree with T4-436 and support the same pre-constraint rank and analytic probe span.
Method: Read both structural proofs and the complete N4 comparison code. Bind 202 current peer-source hashes read-only. Independently recalculate all 348 binomial highest-pole coefficients and six cross-poles, compare all 81 ordered rows and weights, 46 probes, 36 noninteger conditions and 60 complete iteration records.
Result: 392 checks pass, 0.023510708 seconds at 2026-10-29T13:27:43.926938+00:00. The two independent expansion records agree exactly and all 2918 pre-constraint dimensions are CONFIRMED. The original T4-436 JSON phrase 'projection ... excluded' is too broad: only the initial projection is excluded; each trial's Taylor projection precedes its logged step norm. No certified whole-plane distance follows from the sum 0.08387595.
Verdict: CONFIRMED the reciprocal comparison and N4's projection qualification. REFUTED the unqualified exclusion of all projections in T4-436 JSON's step_scope. Accepted proof bytes remain unchanged; this entry is the correction. Historical source timing remains limited to recorded provenance. No inverse or existence result.
Evidence: PROOF 630ccc8cbbd1e1128dc75cb8778b0755dfd63ee3284d475f70bfb930ef84689f; result 9c8c940d17b72a41d0a0f949f9470dcfd24ae5e16400d6b8136c753a6ab07e73; checker b2360e712cd27a69a278a7a47d9d7ce7cd6c8c878f53ca71a798ae0fa950bd66; N4-365 proof b26e24fdcb627135aca6dbe52c6178fd9cbb266a83d47014014b9b3f40e49a91; peer result a7f4dcbdb6e64b5e919c423542b0f207f0c750bbed56f983b0e0245e25066548.

## T4-445: Exact-file audit of theory_v08 preview 1

Date: 2026-10-29T13:35:27.496082+00:00.
Claim: The frozen 769-line preview d8c8e8ba4d36e281381c0f7c55447c9636fc39977e6350a00d805c765725cf06 states the corrected factors and endpoint obstructions without changing their scope.
Method: Read the complete preview, parse revision-2 factor source as data, independently divide all 24 exact rows, check every Markdown numerator/threshold/factor, bind six accepted proof/result pairs, check three-candidate kernel and integral bounds, and observe all 75 Appendix H hashes read-only.
Result: 333 checks pass in 0.013113444s at 2026-10-29T13:34:59.037931+00:00. Corrected S2 and all 24 factors pass; the small-target OPEN qualification and current-list bound are sound. The closure matrix alone changed after preview generation. Remaining repairs: unrestricted 'every registered ball' statements, the 025 opening OPEN label, the claim that two-mode tests necessarily complete dyadic rows or cannot affect their closure question, the universal reading of scalar ceilings and rows S/N1, stale T2 review status, the 'no number changed' erratum sentence, and DK notation.
Verdict: CONFIRMED the corrected factor table within its separate scopes and the four-target conditional majorant obstruction. REFUTED the stale 025 OPEN label, the literal no-number-changed sentence and the inference from scalar/original-graded exclusions to untested dyadic exclusions. OPEN the untested dyadic results and improved universal coefficients at the two smallest targets. The preview needs the listed repairs; no existence closure.
Evidence: PROOF 0eb9308dea16756f9896dff4c1ea5b438c9075517adf35b1d9742778372f1ca0; result a48fe7d12f4bab5a2e3e766a6fbb5ef88e0c4aa34f0aa1285a2f53dc8e87877d; checker af5005593b7c60c57cbbe8ce5c5402b864bff4cd1671de784a4abffa1e0fa3f2. No foreign code executed and no candidate integrations repeated.

## T4-446: Actual 026 independent structure and peer comparison

Date: 2026-10-29T13:45:16.862902+00:00.
Claim: The exact 026 potential and canonical density spaces each have dimension2414 before the421 recorded constraints, equal to the ordered022 basis. Its81 analytic objective rows leave the46 stated probes outside their linear span.
Method: Check every ordered shape, the36 exact noninteger conditions,180 highest-pole coefficients, all objective rows and weights, all60 iteration records, and all six immutable snapshot files. Use the standalone pole and density-injectivity proofs and independently compare the frozen N4 structural record.
Result and verdict: CONFIRMED:397 structural checks and641 comparison checks pass. There are492 radius25,Q4 additions to the1922-dimensional quotient space, with no new basis directions relative to022. The final14 objective rows have weight10^16. The 40 accepted rounded mesh steps sum to0.05665324, a FLOAT diagnostic including per-step projection but excluding initial projection, final exact conversion and integration error. Finer historical ordering of the private holdout declaration remains OPEN. No constrained tangent rank, statistical independence, inverse or full-plane norm follows.
Measured computation: 0.420901983 seconds, completed 2026-10-29T13:39:12.119349+00:00.
Evidence: PROOF 97d9a73864ad89d86602c7c1f56cf844b9e8e38d96c0b285316bb224e77575dc; result e83ae148109d1b04a33ccfb08de6f24d39296f9fde7bbbcb1eefa162fa8733e8; checker 1e52346c8947bc3601d99be524273ef14267739ead3a440ffe260f7bcd098091; raw 2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3. Peer comparison SHA256 d8c081fe4a83c426a0764b1bb39cee479e9fa6c28de915376f43c20f99162d52.

## T4-447: Actual 026 independent point exclusions

Date: 2026-10-29T13:45:16.862902+00:00.
Claim: The exact026 reference fails all six specified scalar point budgets and the original graded-family point budget at(1/10,73/100).
Method: Rebuild fourth-order radial Taylor data from all2414 raw generators, evaluate polar fields at1024bits, and compare the independent Cartesian record. Recalculate every necessary inequality.
Result and verdict: CONFIRMED. Residual F=0.079901987643040288729...; original graded gap=0.059485034360572262525... . All eight field overlaps and six positive scalar gaps pass. This is a necessary fixed-c correction-budget exclusion, not a background inverse or a global nonexistence result.
Measured computation: 1.773794276 seconds, completed 2026-10-29T13:39:14.028088+00:00.
Evidence: PROOF 41e5dff47ecf8fb11dc075b6a0a6a7e29cbc306e5aeb67be19dbd9d702978934; result 399e3d2b655d08bc6f697730ba54539aaf05515ac78bede7c4aa927cec9197a8; checker b2e59c7181975a96e133f9412075a4bd4aef144233494242c0c72f52c3a26bc6; raw 2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3.

## T4-448: Actual 026 exact origin normalization

Date: 2026-10-29T13:45:16.862902+00:00.
Claim: The exact026 reference satisfies c+partial_y U2(0)=1 and has positive density slope.
Method: Evaluate the finite generalized-binomial quartic jet directly from the raw list and compare the four rational origin quantities independently.
Result and verdict: CONFIRMED. Exactly24 generators contribute; a0=10.309480124562667227756... and c+strain=1 exactly. The canonical local/contact convention is preserved. No stationarity away from the origin follows.
Measured computation: 0.046079587 seconds, completed 2026-10-29T13:39:14.184974+00:00.
Evidence: PROOF 3d1d4bad28cebe297fa3207a936764faa7147732062a0c4f730c3809fbf8049c; result 0eed768440646318984ceb8431f094295885abfb317bbf1f51279907a0cb55ff; checker 6c183f33e05043950e74db33b3ecbb419a9880ba597e59161475271ab6b13cdb; raw 2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3.

## T4-449: Actual 026 complete far-field prefix

Date: 2026-10-29T13:45:16.862902+00:00.
Claim: The entire026 residual prefix at exponents at least-7/2 has16 rows,11 zero and5 nonzero, and its first four density and stream profiles equal007.
Method: Expand all generators exactly in r^-2, differentiate by homogeneous identities and assemble all angular products. Enumerate the exact exponent cutoff. Compare the earlier13-row rectangle and all16 rows of the full N4 prefix.
Result and verdict: CONFIRMED. The nonzero labels are(4,1),(9,0),(5,1),(1,2),(10,0), with first exponent4gamma-5. All492 added scaled generators have Q=4 and R=25; none changes the retained L<=2 profiles. The full-prefix comparison has287 passing checks, including exact density, stream and residual coefficient maps and every norm enclosure. This gives no whole-plane upper norm.
Measured computation: 22.127992637 seconds, completed 2026-10-29T13:39:36.370405+00:00.
Evidence: PROOF 78f0caa4275f993e35dd94b409df00600ee4123bfb81d6c6378d4ec6f871db69; result 489f2f4c3d02a80360aa7ffdd697dd20817994619fa4cdd23dd41c85bcf25755; checker 9d4fcd22adde787dea0bb40c8b2be6a719ad0b8d3c11f0749db43d3094e66ee7; raw 2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3. Full-prefix comparison SHA256 194d013b9fedd7395ff4312a94aa1ffd92f6666cec8cac8a165677b43d9f64f4.

## T4-450: Actual 026 independent whole-plane correction-distance floor

Date: 2026-10-29T13:45:16.862902+00:00.
Claim: Every correction satisfying the canonical weak-stationary fixed-c hypotheses of the standalone proof has L2 norm strictly greater than 1355907204057457/1000000000000000000.
Method: Reconstruct all2414 polar generators, retain every angular product, and integrate all scalar moments by exact CRT identities and direct2048-bit Arb hypergeometric evaluation. Use the complete probe(n,K)=(19,1800), with no spatial truncation.
Result and verdict: CONFIRMED. The radius starts0.0013559072040574580429812871; the strict rational floor is0.001355907204057457. All63 moments pass with minimum nonzero accuracy 1935bits. Both pairings, eight final comparisons, six physical fields, the full R1 calibration, six fixtures, and every gradient critical point pass. The actual candidate uses radius25; the general two-factor primitive also exercises the unused radius50 in fixtures. This excludes every registered scalar ball and the original graded family under their hypotheses. It does not exclude the decaying-weight dyadic family or another correction chart.
Measured computation: 122.720949993 seconds, completed 2026-10-29T13:41:39.300564+00:00.
Evidence: PROOF 042beeb993874daf236c7423c1a1546b7c57c307555c9fe252c189a93932bfd8; result 9f30e9cf9a9ef585ba9a4ed15ca70dbc35f53c7397a85b9c0b302aeec8917773; checker c1c3662e3993da6d5384d90c0b801e7b9604dacc30ed915fd6eaed98e1ac8122; raw 2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3. Supplemental import binding SHA256 7272ec5729b0ba1fb581cde8b3567afd8eee0475114f83f4470abcc6f4406b9b. The loaded but unused Sup module and its transitive local import were omitted from the main input map; the sidecar records their unchanged pre-run bytes. Accepted code and results were not edited.

## T4-451: Independent audit of N4-374 candidate016 sufficient forcing failures

Date: 2026-10-29T13:53:53.268830+00:00.
Claim: For F in H1(R2), s>=0 and positive weights, X_(s,w)(F)>sqrt(w1 ell1^2+w2 ell0^2) whenever ||F||2>ell0>0 and ||DF||2>ell1>0. The ten registered scalar sufficient forcing tests fail for actual016.
Method: Prove the unweighted Bessel lower comparisons by unitary Plancherel, allowing infinite norms. Freeze and read the complete N4 proof and checker, attest all59 input hashes, bind the accepted N3/N4 H1 component records, reassemble both saved31-group sums, and independently evaluate every exact threshold ratio in1024-bit Arb. No foreign code or new integration.
Result:318 checks pass. Base forcing comparison>502.575806591370 and sharpw comparison>745.109145778602. Ratios exceed790483392 (A2-Db),1349091658168 (A2-Da),54894679 (rebal),4751141 (TB-sharp),82342019 (legacy),6593837 (sharp),3542234 (sharpw),4403717 (bL7/5),6989765 (bL1),63141692 (trans). Exact divisors3/327680 and1/163840 are used. The two norm endpoints, moment sums and wider N3 balls are consistent.
Verdict: CONFIRMED the theorem and these failed sufficient tests on the accepted H1 component evidence. This is not a distance exclusion or nonexistence theorem. P2, actual H, Q3 and fractional upper norms are unused and remain separate. Full1024-bit peer endpoint agreement remains OPEN because the stored N4 balls retain100decimal digits. No dyadic implication, inverse or closure.
Measured computation:0.060085314seconds, completed2026-10-29T13:53:21.672388+00:00.
Evidence:PROOF 05028d893c13ae9a813a63a8d720ec8cba770aa52bbe96b096a54f4b77180941; result d89ab420afebb15493fc88ff8286868238136b371878328913e2d4ae0eb07c98; checker 99fbdfbf3052e593980af5155e457f1fcd6e68c7facde087e07b39a1e7755a33; N4-374 result1b402adaa66ee89e620efdd8ec79b40ee953c90c9389a48b502c99fc97313f2c.

## T4-452: Acceptance of T2 endpoint revision2 logical repairs

Date: 2026-10-29T13:56:18.214160+00:00.
Claim: Revision2 repairs the five logical defects identified in T4-443 while retaining the same13 numerical table rows and arithmetic program.
Method: Read all224lines and37word-change blocks. Prove the admissible-set distinction, necessity-only implication, monotonic upper-bound logic, list-specific floor and rounded-ceiling bracket scope. Bind the prior948-check result, compare all table entries and independently evaluate the exact graded cutoff at768bits.
Result:107checks pass in0.022993384seconds at2026-10-29T13:55:51.294244+00:00. All five requested repairs are present. The exact graded ceiling lies strictly between45697/10^8and25/54684. With the common budgetH>=999745 the three R1-038 cutoffs are below0.2694533, including the largest0.26945243670784104023856... for013. The current-list CI cap remains below2.66323e-8<2^-25.
Verdict: CONFIRMED the five repairs and unchanged finite consequences. OPEN whether an improved admissible universal coefficient reaches2^-25or6.8626e-8. The unprinted exact sharpw/TB one-unit brackets remain conditional. This audit does not accept all unrelated the T2 final summary claims. An initial T4 suspicion that the0.2694533bound failed at the exact graded ceiling was REFUTED by the first checker; its draftproof, code, manifest and failurelog are retained, and the final proof corrects it before acceptance. No candidate exclusion changes.
Evidence:PROOF 88b0ac35e46072242a94e57b198470d16b100a8bd77b744bf626e18f8d35c4f6; result 9ab5d4327cce63876910a9e0d30b6758865606e99190858db6536cf21bf943b1; checker 19329a2387c0a9b9084859ea15124ad5d81dd33ad952a281f9d94b6ad9a7597d; revision2 660b089b8e6435065918f020a45d971cce4d82e8210675944322f3d7c47dd7f5.

## T4-453: Independent audit of THEORY_FINAL draft 39

Date: 2026-10-29T14:02:04.615837+00:00.
Claim: The frozen 1897-line draft39, saved13:47Z, retains valid conditional arithmetic, endpoint quantifiers and candidate-distance comparisons, subject to its exact chart hypotheses.
Method: Read all88word-change blocks in the352-line comparison with accepted draft38. Bind the preceding proofs and results, recompute the sharpw rate and closure slack, all22 numeric table rows, six small-Db ratios, nine split-integral bounds, the normalized R1-038 cutoff, lambda and projected norm. Incorporate the independently accepted016 forcing result451, endpoint repairs452 and026 results446-450. No peer program or large moment integration is executed.
Result:237checks pass at768bits in1.808552526seconds, completed2026-10-29T13:58:51.574573+00:00. The exact sharpw rate is63092119/405000000 and the self-map slack is7/1557000000. All table bounds pass. The026 full-plane floor gives downward-rounded family factors357.4,475.8,2.965; the current draft still says026OPEN. The normalized endpoint threshold, repaired lambda and downward-rounded projection lower bound pass. The two small Db targets remain OPEN for an improved admissible coefficient; their three named candidates remain independently excluded in the scalar/original graded charts.
Verdict: CONFIRMED the changed conditional mathematics and22 table rows. REFUTED as current status the026 reproduction OPEN/no certified bound entries. Update026, cite451 for016 forcing, distinguish acceptedG0/rF/G1 from remainingP2/actualH, display the normalized R1-038 expression in section0, and attach target scope to the radius-dependent obstruction. These are publication updates and scope clarifications. No inverse or existence closure is established. Unseen later edits are outside scope.
Evidence:PROOF a2319328ba7b3fdb59d460237483c016accc38eaf6ec27127e4b7a6d51033d6d; result 4fce0c45248649a19963bb1ce5bc2d92917e75b2d7b3a32b5371cde370a18654; checker 2972c5be0d31776c76ff59733c3f02e2dac28b39b4266b6bc21c6244f59d16da; frozen draft39 28f5f6ce4bd47463335e8b76b07bdfb53a1c6445bd9e1f0552a81dbb1ae5b97b. The earlier1909-line draft39 is a distinct mutable precursor and is not the audited object.

## T4-454: Exact scalar-family brackets and TB-rebal rounding repair

Date: 2026-10-29T14:06:46.694406+00:00.
Claim: T2 handoff BE correctly locates seven scalar-family suprema and the original graded ceiling, with an upward-rounding correction for TB-rebal.
Method: Reprove the cubic maximum, compare squares using exact rational arithmetic, bind all four peer source inputs, and compare independent 512-bit roots with the peer enclosures. Check the endpoint monotonicity and the four-significant-digit factor repair. Retain all positive-rate and norm-control hypotheses.
Result: 166 checks pass in 0.012317326 seconds at 2026-10-29T14:06:02.247373+00:00. TB-rebal has supremum 3.51254748112091806496...e-7, strictly above 3.5125e-7 and below 3.5126e-7. Its ratio to the old printed value is 1.000013517756845... < 1.0000136. The six other scalar suprema lie strictly in the one-unit brackets below their printed ceilings. The original graded ceiling lies strictly between 45697/10^8 and 25/54684. All seven scalar suprema are below 3.7930e-6.
Verdict: CONFIRMED the eight brackets and scoped persistence conclusions. REFUTED the historical statement that 3.5125e-7 is rounded upward for TB-rebal. The common scalar and original graded distance exclusions are unchanged. A decreasing endpoint cutoff preserves its upper bound at the larger exact radius, but its old lower bound need not persist. R2/R3 factor formulas and historical O3/C4 ratio entries are outside this audit. No attainment, inverse or existence result is added.
Evidence: PROOF bba858593cf8d4c98d2e8a430dbf6751bd151767ecc5452e14e64e0eebf1c53a; result 43a549a41c10848f67f73d54bb6dcf11ed0b5d05e95078859a30de6872f71de2; checker 528a828f4f4c3b427a0a472f8d8866f49ca77a7a78039c54cd6d97d18004652c; T2 result b1fea0a74af0a7729b38a27f1796deea0b3597b4ca9549ba235e9131af3b98a7. No peer program or spatial integral was executed.

## T4-455: theory_v08 preview2 and its exact-ceiling factors

Date: 2026-10-29T14:12:17.860775+00:00.
Claim: The frozen 868-line preview2 (5940b948...70158) incorporates the seven T4-445 repairs, and its new exact-ceiling and H0-only factors are valid in their stated certificate scopes.
Method: Read all127 changed word blocks, bind106 local inputs, reparse and recompute all24 exact printed-target divisions, reconstruct B, Phi and critical coefficients from exact endpoint JSON for007,013,014, and use the independently proved T4-454 radius brackets with the beta^e scaling of the selected remainder. Compare the nine new factors and three H0-only factors independently. Check immutable appendix bindings and preserve five changed live hashes as historical references. No peer code or spatial integral executed.
Result: All415 checks pass at768bits in 0.032970979seconds, completed 2026-10-29T14:11:47.714097+00:00. Exact-ceiling U4/P1/P2 factors at007 are at least2.9432/2.0544/2.0515. R2/R3 are at least46.0752/66.5677 under H>=Phi; H0-only R1/R2/R3 are at least22.1948/46.0750/66.5674. U2/U3/P4/P5 retain their printed factors; K2/K3 stay at printed targets. All77 appendix references are accounted for,72 matching frozen files and five later-mutated reports. The 026 distance and016 forcing additions agree with accepted T4-446 to451.
Verdict: CONFIRMED the changed mathematics and scoped factors. The seven445 repairs are made. Before publication update the now-complete reciprocal026 status, cite independent451/454 acceptance, and use3.5126e-7 for the TB-rebal upper ceiling. Those successor updates change no common-ceiling exclusion. This audit neither repeats the full matrix falsification nor establishes an inverse, existence or unrestricted nonexistence theorem.
Evidence: PROOF 8c1b6532cf66d1c05fe5a919c92dfe8b3233e1ba37697816c0b2222c6ab8ea07; result 88262498ad6701bd7ba6d630e2da22ea0a487412e04816d30b48c1e24cb69c64; checker c16927a9682259c2e9b7937cc6ac621723c3bc94510b4db8ef86d7f5f1036aa4; preview 5940b948c623aab0e744375d26100c99356f6bdc6acb46d915822e8b86d70158.

## T4-456: theory final draft 43, repaired normalization and status

Date: 2026-10-29T14:19:23.233664+00:00.
Claim: The changed mathematics of the frozen 1933-line draft43, generated14:09Z, and its23 distance-table rows are valid with the stated analytic and integral dependencies; the T4-453/454 repairs are made.
Method: Read all48 changed word blocks against the accepted1897-line draft39. Bind22 frozen copies and their result/proof pairs, recompute all23 exact table divisions, seven scalar supremum squares and the graded square, the normalized endpoint conditions for007/013/014, ten016 forcing lower factors and the unchanged sharpw conditional arithmetic. Check the fixed-c/L2, original graded, dyadic and necessary-certificate scopes. No peer code or spatial integral was executed.
Result: All263 checks pass at768bits in 1.395492123seconds, completed 2026-10-29T14:18:39.139038+00:00. The026 truncated floor0.001355907204 gives strict factors above357.4/475.8/2.965. Its reciprocal status is correctly closed through N4-379. The full R1-038 condition E sqrt(2pi) Hmax/B < Emax(b) is now printed; its unnormalized consequence is below0.2694533 once Hmax>=999745. TB-rebal uses3.5126e-7. T4-425 has its four-target scope; improved valid coefficients at the two small Db radii remain OPEN. The016 statement correctly reports ten sufficient-test failures without norm ordering or distance exclusion. The first checker stopped at a schema-only KeyError for026's proof hash; the failed code/log are retained, and the corrected reader uses the accepted inputs map.
Verdict: CONFIRMED the changed mathematics, numerical rows and requested repairs of this frozen draft. No changed mathematical assertion examined here is refuted. This is not the full H18 closure-matrix falsification and supplies no high inverse, existence or unrestricted nonexistence theorem. Later draft edits and the new N4-382 conditional015 dyadic result are outside this frozen delta.
Evidence: PROOF 644e6d03ba403ff966c50b1b8c72b51f71e6fde41af63c9a47de672cc3c1cc85; result 60eb4f367092e06f94975a634e7b4b4cad633cf3042f48082b634754c74be9ed; checker fcf235d6d379c0e2aec30330e9d6a86ee5aa3951b0df3ce3688f7cc4b62433b9; draft a3b59ce9cedb7c9c3307c4bff1fac47af57bfa076717c1d426dfc487c2218c21.

## T4-457: exact historical ratio floors and a prose consequence

Date: 2026-10-29T14:22:35.592896+00:00.
Claim: T2's ratio report correctly identifies13 of18 historical O3 factors and8 of12 C4 factors as exceeding the exact quotient, while the15 current summary factors are valid directed floors; all corrected factors still exceed one.
Method: Freeze the three tables and peer report. Use the T4-454 exact rational squares of six family suprema. For positive d,b,u, compute k=isqrt(floor(d^2/(b^2 u^2))) and verify k^2<=d^2/(b^2u^2)<(k+1)^2 with exact fractions. This gives the exact floor at display unit u without floating arithmetic. Independently parse every table row and compare all45 floors with the peer report. Record the two changed historical summary/handoff hashes instead of claiming identity. No peer code or integral is run.
Result: All233 checks pass in 0.007950929seconds, completed 2026-10-29T14:21:43.484329+00:00. The15 current summary factors are exact floors; d2/sharpw is1.03e5, not the former1.04e5. Exactly13 O3 and8 C4 values exceed their valid floor by one displayed unit. Every corrected factor exceeds one. The graded d2 quotient lies strictly between646 and647 and the Mpen2 display1204 has floor1203. The O5 prose's at-least647 wording is unsupported by this certified quotient, even though the unknown actual PDE distance may be larger.
Verdict: CONFIRMED T2's counts, exact replacement floors and preservation of exclusions. REFUTED the lower-factor interpretation of the21 identified historical values. OPEN the stronger actual-distance assertion that O5 might be read to make; this finite computation provides no PDE counterexample. Use646 for the directed O5 factor or label647 approximate. No candidate ordering, inverse or existence claim follows.
Evidence: PROOF 4daf08a6a8b3e769fee56cc450d5a5490693ce2c12c829033b4cf1ca82e29d6f; result 5ab0c3bec3817a391cd9f7c129854ff910123c6b6a3e1660cd41392404235724; checker 23360454c312de9f0f496285743f924f0a0209cedb098901ff9d7539489e215b; prose corollary dc5828d7527f5fceb6dff7c321897510c1a68863311db3edba7621d4fe9426dc.

## T4-458: Candidate001 leading obstruction and affine-class application

Date: 2026-10-29T14:34:25.599981+00:00.
Claim: the immutable candidate001 has a nonzero leading residual at q=2gamma-1>0 and a nonzero leading density, so the AUDITED annular obstruction excludes every real L2 distributional correction at every real exponent.
Method: independently sum all860 exact raw generator coefficients at radial t=1, derive density and stream profiles by homogeneous polar differentiation, check four exact Laplacian identities and compare the complete E_(1,0) polynomial with N4-028. Apply the previously independently accepted T4-049 theorem, retaining its distributional products, sublinear growth, uniform analytic remainder and changed-exponent hypotheses.
Result and verdict: CONFIRMED for the896 finite exact checks and all10 nonzero residual modes. The actual check ended2026-10-29T14:33:46.266125+00:00 in0.039926711935549974seconds. The new standalone application is OPEN for independent Opus review; the original matrix row35 nonmembership exclusion remains valid. This application would strengthen it to no stationary correction anywhere in the affine L2 class, without a strain trace, correction-gradient bound or radius assumption. No weighted or non-L2 conclusion follows.
Proof SHA256: 771ad6b4af564e1b3a0acf1284184fd8f36c15d2dd090212370122d433789a3e.
Result SHA256: f367ac93db809c7d9c74c27d7b788bd198e4448c62afa1db894ae5251d324f61.
Checker SHA256: 8f95265bf10dcc0ad08679cc4e0912c299d392007e912ccce1fd581624a9d96d.
Raw SHA256: 8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7.

## T4-459: H18 finite registry and whole-family coverage audit

Date: 2026-10-29T14:41:03.476169+00:00.
Claim: the scalar and original graded exclusion applies uniformly to every frozen snapshot through026except011, with fixed-c, norm and candidate identities preserved.
Method: froze matrixv135, THEORY_FINAL draft44, T2 summary and27exact snapshot manifests; checked raw coefficient hashes directly. Bound24accepted weak results to raw inputs or accepted canonical conversions, exact proof hashes and review excerpts. Recomputed I_lower-D_upper/1000-H_upper/1000000 with rational decimal intervals. Derived the eight scalar-family supremum squares and the original graded/trans/statL top-margin bounds. Reparsed every frozen matrix row and tracked all73candidate occurrences.
Result: CONFIRMED finite arithmetic and the stated necessary-condition composition:806checks in0.233623seconds; every002-026except011has fixed-c L2 distance>1/1000, exceeding all eight scalar ceilings, the original graded/gradedL2 ceiling and every trans/statL parameter choice retaining its positive top margin. The two bL instances are fixed; arbitrary weight changes are outside scope. Computed-defect radii are total correction radii. No L2 trace or hidden derivative of h is used.
Scope correction:001requires a separate reason. Its forcing nonmembership confirms scheme inapplicability, but does not itself prove no solution in a ball. The stronger T4-458 annular application remainsOPENpending independent Opus review.011and027areOPEN; decaying-weight dyadic schemes and generic improved frameworks are not covered by this L2 argument. The exact all-snapshot nonexistence sentence isOPENuntil001's independent review, although all-snapshot scheme inapplicability through026except011is supported. Requested Opus review of the composition and trans/statL uniform extension in team note 235.
Evidence: audit record h18_coverage_audit, proof SHA256 353fc1575bccca1927be976d646b9ff886ee5fb87c99a090c8fce0c0b3d9f650; verification/result.json SHA256 3b433eb41a607839e3e4a9140fae9acaace1ed6ea46a50149d840d112c84d8c5; COVERAGE.md; data/manifest.json binds130inputs. Initial preparation had a Python format-brace KeyError before proof generation, repaired before the checker was written; no mathematical check failed.

## T4-460: Six supplemental weak roots and global probe caps

Date: 2026-10-29T14:48:10.047350+00:00.
Claim: N4-383 and N4-384 give valid conditional necessary fixed-c L2 correction bounds for three complete probes each at candidates 015 and 017, including the stronger 015 (23,2400) bound.
Method: Wrote the standalone weak proof before the checker. Froze 24 local inputs and rehashed all 69 distinct original direct inputs, 74 occurrences. Independently differentiated the radial gradient, enclosed all three possible positive maxima for each probe, checked both coarse and sharp caps, compared all 18 I/M/C intervals with N3, checked the reference integration-by-parts identity, and recomputed both roots and their strict quadratic margins at 2048 bits. The accepted field integrations were not repeated.
Result: 257 checks passed in 0.034212478 seconds at 2026-10-29T14:47:21.727848+00:00. The 015 sharp strict floors are 0.000351804115950603, 0.001232449584356253 and 0.003033479200692324. The 017 floors are 0.000596123050327423, 0.001068502321536437 and 0.00167183069831928. Every global gradient cap is confirmed independently of candidate transfer. The strongest accepted 015 floor exceeds every specified scalar and original graded ceiling.
Verdict: CONFIRMED the finite arithmetic, global gradient caps and conditional fixed-c canonical L2 implications. REFUTED the generic relative-change less than 1e-5 statement for all six rows. The coarse method is a closed monomial bound, and the distance is from rho, not F. Candidate 017's (21,522) row remains outside the public 25-probe family. Other probes, a maximum over them, dyadic consequences and full-norm ranking are outside scope. No new field integration, inverse or existence assertion is made. Historical N3 cache and import-version limitations are retained.
Evidence: audit record late_weak_supplement_audit, proof SHA256 3a1dd3017e44b9cfd57bca4a6ac19f08f4603622715e64dfc30d54b696149474; verification/result.json SHA256 c2d3cbc84925f5b3aee7c320e72e37d14fd6c008bed9b1d533e716b6a7b9027e; code/check.py SHA256 71eafb738a06d3a4f934b8dae5b26176bb8eb4ac8e3e56371617b7780e96bbbf. Dependencies N4-383 result c9350681334bee416f3fa085203b3ebd3c4e383654d61e3c9a477f95288a5375 and N4-384 result 4f49a7b95ec6fdbbb274161149037c0b77d449db3e4daf3d02b08d46a110d996.

## T4-461: Candidate 015 complete conditional dyadic deduction

Date: 2026-10-29T14:52:08.889973+00:00.
Claim: N4-382 supplies the exact origin and projected energies needed to exclude all parameter cells of FW-T-DYADIC-Y-v1 for candidate015, under that specified scheme's full hypotheses.
Method: Wrote the standalone proof before finite arithmetic, retained the actual weighted norm, canonical velocity, normalized origin, maximal low realization, high inverse input hyperplane, partition and absorption hypotheses. Rehashed 33 original direct inputs and froze19 local inputs. Independently reconstructed the complete canonical serialization and origin derivatives, checked every diagonal and radial cross endpoint condition, exact positive N3 energy sums and all14 independent mode comparisons, then recomputed the continuous maximizer and all seven strict cell ratios. No field integration or L2-distance inference was used.
Result: 739 checks passed at1024bits in 1.533902380 seconds, completed 2026-10-29T14:51:05.578631+00:00. All1922 canonical coefficients and24 quartic origin terms are accounted for. The exact strain is1-c and slope exceeds5c-4. Every cell is strictly excluded; minimum ratio exceeds621461129537/500000000000=1.242922259074. The seven cells cover[0,1+1/c]; the complementary a range fails positive low rate under the same assumptions. All0<s<1 and each fixed finite weight radius are covered by the conditional implication.
Verdict: CONFIRMED the source-bound finite checks and specified conditional scheme exclusion. No high inverse is constructed, no full upper Laplacian norm is inferred from two modes, and no exact-profile nonexistence follows. The N3 historical cache and import-version limitations remain explicit. The first T4 checker failed at origin_strain_exact because it treated canonical k as the raw monomial power; canonical k already includes m. The corrected standalone proof preceded the corrected code. Failed proof, checker, manifest and explanation remain in verification/failed_attempt_v01. This error was in the new audit, not N4's accepted energies.
Evidence: audit record candidate015_dyadic_audit, proof SHA256 27cd1dc8f365f769542257c309a0fb5a602da580985487c8cb269e09abb0c163; verification/result.json SHA256 158a939abc32cd8e04e5b39b484e03b3b74dfebdbc51ed9e4fb90c90f6aabf6f; code/check.py SHA256 a75e5861e0f96e7e7412ade2734bd14751bcb8f23dd965845f2637c76ab85ce8. Accepted N4-382 result24bdc65df109a3002e4bdd6ac8676e955a606466c3fb046a4d04bcd91e741266; independent T4/N4 termwise canonical agreement and Opus T2 origin review are frozen dependencies.


## T4-462: exact weight elimination, WU3 ceilings and every unweighted bL margin

Date: 2026-10-29T15:00:35.854050+00:00.
Claim: all five WU3 ceilings and two bL supplements are necessary upper budgets, uniformly over the weight pairs of the two stated Gram schemes; T2's independent review accepts the T4-459 finite coverage and trans/statL implication.
Method: derive the determinant identity symbolically and eliminate w1 exactly by AM-GM. With p=m2-mu, a=m1-mu, c=beta-mu and O=347/10, positivity forces w2 >= [1440p+(6O+5a)^2]/(c*p*a^2). Maximize over s, then prove the resulting degree-seven rational polynomial positive by exact Bernstein subdivision. Independently reconstruct every leaf from the original power polynomial. Check kernel constants with1024-bit Arb, seven exact gain and distance comparisons, and all24 accepted weak inequalities. Read the full T2-459 review; bind its two main targets and189 passing checks. No peer program or field integral is executed.
Result: 320 checks pass at 2026-10-29T14:59:26.691578+00:00 in 0.1739647500216961 seconds. The seven strict L2 upper budgets are3.3469e-6,4.0249e-6,5.0757e-6,6.1373e-6,7.5854e-6,4.0746e-6,4.1069e-6. Every polynomial needs only4or6 intervals, depth at most5. The three modified-floor rows are hypothetical. The unweighted margin beta_L<=1+c-theta-kappa<=1+c<57/20 makes the last bound cover every positive certifiable beta_L and every allowed pair of weights. All24 fixed-c snapshots002--026 except011 are outside those bL balls, by a common factor greater than243. The007 factor is at least1161.2. T4-459 is now independently CONFIRMED by T2, including the uniform trans/statL L2 ceiling25/(54684*512).
Verdict: CONFIRMED all seven scoped upper bounds, the bL extension and the acceptance of T2's T4-459 review. OPEN actual full-scheme sharpness: the FLOAT weight samples use relaxed uniform constant lower approximations, and do not certify feasible full commutator constants at those weights. The weighted(B-L2-w) alternative, different floors/constants, independently weighted E0 summands, variable-c weak exclusions and decaying-weight dyadic spaces are outside scope. The new exact AM-GM simplification is submitted for reciprocal Opus review; it agrees independently with T2's separate cell calculation. No inverse or existence conclusion is added.
Evidence: PROOF 3c871d7f9ef82ba6b6fb925cf73a31cda678805cadc2c8a91f9659b2e2f3030c; result 61803920bea366913555ebb213ac40b466d370b1c92dd5cfe9cc9b67b9895450; checker 45e04c8f649fb8389c8c16600b55bfe3cb7100deac6db0f9e4583a12efd584b7. T2 review459 e140e6c03aa2ec4487ac18da011853e9819c387787aa48b5e4ecb4485052d87f; T2 review result 2e861406303c8ce65f030c7d486cc98d5986dfb260872ecd4c9c138d631c6b59. A pre-code correction restored the TB coefficient20/21 in E0; the first draft is preserved and no numerical claim depended on the omission.

## T4-463: Candidate017 exact origin and two-endpoint conditional dyadic exclusion

Date: 2026-10-29T15:05:10.563088+00:00.
Claim: N4-389 supplies the complete two projected norms needed to exclude all seven parameter cells of FW-T-DYADIC-Y-v1 for017 under its complete analytic hypotheses.
Method: Wrote the standalone proof before checker code. Rehashed47 original production inputs and froze27 local inputs. Independently reconstructed the quartic jet from exact raw generators, rederived all16 diagonal and136 cross endpoint conditions for each of four calibration/candidate modes, reconstructed51 group exponents, re-summed all408 saved integral balls, compared prior007 energies and two containing N3 squared displays, and recomputed the continuous H maximum and all seven bounds. No field integration or peer code executed.
Result: 1070checks pass at1024bits in0.09962146496400237seconds, completed2026-10-29T15:04:41.569847+00:00. The24 raw quartic contributions give exact strain1-c and a0=10.311598215877167151...>=5c-4. The017 projected norms are19.772210980628416609... at1/4 and10.650574295793333524... at7/4. Monotonicity excludes every cell; the minimum ratio exceeds1.221854480167 on[1/4,1/2]. The first-cell ratio1.244974... is larger and is not this audit's minimum.
Verdict: CONFIRMED the finite source/energy/origin/cell replay and the conditional seven-cell implication. The actual inverse, normalized origin, low realization, input hyperplane, canonical velocity, fixed partition, plateau and absorption hypotheses remain explicit. Five unused N3 endpoint energies and unprinted internal interval endpoints were not reproduced. Source-bound differentiation and exact partial-fraction reconstruction remain accepted numerical premises; their large numerators were not reconstructed from hashes in this finite replay. No L2-distance argument, full upper norm, profile nonexistence or existence closure follows.
Evidence: audit record candidate017_dyadic_audit, proof SHA256 0e32cdb67612d8d6ca21188aaae63c5f9fda2e096f920633ff319bd9457e399d; verification/result.json SHA256 96c4b875268111d8e96a2a7be9b38e04a4e624fba22046168d9852ff20a7f3b7; code/check.py SHA256 2379a52f964355c2e6ec9ed55a4a605a0671012e2d97c5d88a318014b003d92e. N4 production3478699c05de85ae62fb7be1b90b6f8e5b54e11138efbae88aeb1960cc710b5e; acceptance618460b3ee525af964d31340466ee789786463cadeda003f3862f63939453e93. Every external source matched at the recorded observation time. No historical-execution inference is added.

## T4-464: TB-rebal endpoint row at the exact family radius

Date: 2026-10-29T15:07:14.270738+00:00.
Claim: T2 FALSIFY revision3 correctly repairs the TB-rebal endpoint bounds at its exact radius and preserves the retained-shape obstruction.
Method: Wrote the complete endpoint CI argument and radius maximization before code. Froze15 inputs, rehashed12 original peer dependencies, independently reconstructed B,Phi,g0,v0 from exact endpoint JSON and b from323433/2621440000000000000. Checked all63 directed per-candidate bounds across old/new brackets and exact radius, plus common bounds and monotonicity.
Result: 199checks pass at768bits in0.012813719920814037seconds, completed2026-10-29T15:06:50.471769+00:00. On[3.5125e-7,3.5126e-7], K(Phi,0)<=0.6720590 and K(Phi,v0) is in[0.6372593,0.6372977]; at exact b these become0.6720573 and[0.6372611,0.6372960]. All retained-shape upper cutoffs are below0.7930365<Emin. Every crude cutoff remains greater thanEmin and is inconclusive. Candidate007 at b has K(Phi,v0)<0.6372612<0.6372628.
Verdict: CONFIRMED the revision3 row and unchanged conditional certificate obstruction. REFUTED the old007 lower endpoint as an exact-radius bound. The old upper endpoints remain conservative. This is a necessary-condition argument for the specified endpoint certificate; it proves no correction nonexistence, attained family radius or existence. The two small Db targets retain their separate OPEN status. No peer code or spatial integral executed.
Evidence: audit record tb_rebal_endpoint_audit, proof SHA256 3e9793dfb4e539a225a70d554d6cd3814aae068d654754b306d340140a8edecf; verification/result.json SHA256 75657839be3bf34c1c321b05f50b3ea4d9844d86ef5414381ec66978a9fc8f81; code/check.py SHA256 4cc1f1c51f3679a5b7656c9a030a2038b7d9fe84c3d70cad804b4834ed7e2050; T2 revision3de58845366cdfa397f0fb47e496db574aed2fa1a584c42c09962f6372d21dfc8, peer result65e00fcc4678944772c21e68a3bd55ccdefa820a3f8d84d39fe99c9cb95e4240.


## T4-465: independent Opus reviews accept candidate001's whole affine L2 exclusion

Date: 2026-10-29T15:11:34.635602+00:00.
Claim: T1 R1-046 and T2 the review of T4-458 independently confirm the canonical candidate001 annular application at every real c. The changed-c test needs its angular factor written explicitly. T1's constant-velocity extension is valid.
Method: Read both complete reviews and their distinct exact derivative calculi. Wrote the standalone acceptance argument before code. Froze19 inputs and verified10 original source identities. Reconstructed all860 raw branch sums, exact exponents, complete angular supports, positive squared norms and the zero E/G0 pairing. Bound both original review targets, logs and coefficients. Reproved all distributional annular bounds, including the constant transport, without differentiating h. No peer program or finite-point diagnostic was executed.
Result: 957 checks pass in 0.027909382712095976 seconds at 2026-10-29T15:10:41.624130+00:00. T1's912 exact checks and T2's30 checks agree with the original896-check table. E has modes21--39 and G0 modes1--19, both odd; their inner product is exactly zero. For c!=c0 the test is phi_R=R^-1 eta(r/R)G0, with a nonzero leading pairing of orderR^(gamma+1). The canonical theorem excludes every real L2 correction, without symmetry, normalization, trace, smallness or derivative conditions, at every real c. A constant background velocity adds only lower-order forcing and transport and is covered too.
Verdict: CONFIRMED both reviews, the whole affine L2 exclusion and constant-background extension. REFUTED the interpretation that changing q alone while retaining E gives the required changed-c leading pairing. The wording correction is saved as candidate001_affine_exclusion/ERRATA_v01.md; the reviewed PROOF hash remains unchanged. No non-L2 class, changed far field, linear background or profile-existence conclusion is covered. An initial consumer schema error treated the original check list as a mapping; preserved development_v01 explains the fix, and no original result changed.
Evidence: audit record candidate001_affine_review, proof SHA256 a3dbba66ab10ccb3be109e9c9afd3dfbfb545397ed10e18bd96c58562fdc3083; verification/result.json SHA256 96c9365d3ecae7f96c8c71068dca5b093cb9d8ac2c41be1f606735c10caede8e; code/check.py SHA256 9e18963c7336bc831038acf551aef0513435a6f6be073fc1ffe960ef61273cad. T1 review 1b7c425c77edfaade35aa73b5316a9fd3c4e1b052b56f6c8acfb446dbbb9a11d; T2 review ca936460537bea92ba0b2e0ddd1add8af2614341b20f9e5613cd898d4660229a; erratum 00f281c080c5ee4af1b3d12f30bb2681b97789e16ff2c4544357124ca226bea0. Original application771ad6b4af564e1b3a0acf1284184fd8f36c15d2dd090212370122d433789a3e, resultf367ac93db809c7d9c74c27d7b788bd198e4448c62afa1db894ae5251d324f61. Actual provider model identity is unobservable; these are the existing Opus5.5-configured theory lanes.


## T4-466: domain and exact test formulas for the proposed negative-norm dual certificate

Date: 2026-10-29T15:13:48.221128+00:00.
Claim: N4's prospective candidate016 dual certificate supplies a valid homogeneous negative-norm lower bound for any admissible exact rational test vector, and can support an actual same-energy comparison after numerical reproduction.
Method: Read the complete dual and mode-Hardy proofs. Independently rederive the distributional angular vector field, gradient-completion domain, origin polynomial, cutoff convergence, orthogonality and finite-dimensional dual inequality. Recompute the polar derivative and both Jacobians by hand, including all pi factors, ordered cross pairs and complete endpoint integrability. Record10 individual claim verdicts in analytic_review.json. No code, solver, peer program or integral executed.
Result: H^2>=sum p_n^2/d_n holds for distinct modes and strictly positive complete test energies. beta>3/2 and3+2k>=n give admissible smooth tests. The exact formulas for d_n/pi and p_n agree with N4. The cutoff orderR^(6-4beta) is a squared-norm bound; its norm order isR^(3-2beta). An arbitrary rational vector needs no solver optimality or conditioning premise. A positive016 lower energy exceeding a same-definition007 upper energy would order those actual energies.
Verdict: CONFIRMED the analytic dual proof and scoped prospective comparison, with the squared-cutoff wording clarification. REFUTED the inference that a lower H witness below an upper H display confirms that upper bound; it establishes consistency only. The angular-divergence construction and complete norm enclosure supply the actual upper proof. OPEN all new016 numerical dual pairings, H floors and E2 ordering until independent numerical calculation passes. No correction-distance ranking or existence conclusion follows.
Evidence: audit record negative_norm_dual_audit, proof SHA256 488b4a7207c8cb917cce25b674bfac8dcdcbb40326318551ec115ebc14858668; verification/analytic_review.json SHA256 b7d5f6404a0be5fd6365f5a67f78843e2ae6cfceb149826c7969e04e05236417. Both prospective N4 proofs and the dated N3 wording are frozen with hashes. This is an analytic audit, not numerical reproduction.


## T4-467: complete016 component assembly and five actual weighted norm comparisons

Date: 2026-10-29T15:18:52.905547+00:00.
Claim: N4-392/393 correctly composes all four complete016 norms, fails all ten registered forcing tests and orders the five actual same-parameter XSW norms007<016.
Method: Wrote a standalone direct-sum/domain, angular multiplicity, radial exponent and binomial-remainder proof before code. Froze18 compact inputs and rehashed139 source-graph records, including all62 N4-393 dependencies. Independently reconstructed six representation metadata hashes and all ordered pair counts, checked31 complete groups per norm and every integrable exponent, re-summed124 unweighted and31 weighted moment balls, recomputed the exact binomial error and all outward component endpoints, ten forcing rows and five rational gaps. No peer code, field differentiation or spatial integral was executed; accepted exact coefficients and moment certificates are explicit premises.
Result: 8874checks pass at2048bits in0.15313391387462616seconds, completed2026-10-29T15:18:16.671440+00:00. Full ordered Hessian multiplicities1,2,1 give45648 ordered pairs; P2 minimum recorded accuracy1690bits. P2 strict bounds218.104089397824118537999059607229 and218.104089397824131729926375547616 pass. E_star is in(547.861145896494,547.861145896497). All ten sufficient forcing tests fail. Same-parameter actual007<016 XSW gaps exceed sharp30.172542254537,sharpw18.235303194523,bL[7/5]18.306105182355,bL[1]18.513960661750,trans30.726383186740.
Verdict: CONFIRMED finite component composition and all five actual weighted forcing orderings, under accepted moment and commutator premises. The H<=rF proxy gives only an upper proxy for E2. OPEN actual016 H, new dual values, actual E2 ordering, Q3 and fractional upper bounds. No correction-distance ranking, other-candidate ordering, dyadic exclusion, inverse or existence conclusion. N4-347 imported-fixture qualification and saved40-digit peer containment scope retained. Conditional target only: independently proved mode1 and3 absolute quotient floors0.376 and0.371 would giveH^2>=0.279017 andE2(016)>608.121275>606.820219>E2(007). Exact squared margin is8298711468010498138547833189/5250000000000000000000000; the two new quotient premises remainOPEN.
Evidence: audit record candidate016_complete_forcing_audit, proof SHA256 dae8594bf2eee8cd5b9bf6d9356b1be9b34a3fe51c5c95440202dffb813fd39b; verification/result.json SHA256 5883ec4dbb7c53e2bd4343c0a04afdfcc6ec813e62a84d479575141bcfe4cf74; code/check.py SHA256 a5a014176b746e53be021573ab1190485775daf909eeceaf2b47936de6974384. Complete N4 productionf7e0202b858f0f49eb2e32b0345468829d0df35f6efe00ca71715e6c814c3c62, component acceptancea2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc, forcingcb7906f600202359c4d33a5cfc9afd1e9b338aaf903407253ebf57f0ca8b70f1. This is finite independent arithmetic, not an independent repeat of moment integration.

## T4-468: Both Opus weight reviews and exact relaxed supremum brackets

Date: 2026-10-29T15:24:46.137525+00:00.
Claim: T4-462's exact all-weight elimination is confirmed by both Opus reviews, and the seven tighter six-digit suprema in T2's new review belong to rigorously enclosed relaxed budgets.
Method: full manual T1 R1-047 review/script reading and source hashes; T2 review/result/code bindings without execution; own exact rational test points, degree7 Bernstein certificates with independent affine recomposition and exhaustive leaf coverage, directed Arb square roots and exact decimal rounding cells. Proved that the equality weights satisfy w1>2,w2>1 throughout each whole mu interval.
Result and verdict: CONFIRMED, 364 finite checks at768bits in0.068488seconds at2026-10-29T15:21:05.272426+00:00; eleven manual T1 claims. The displays are3.34629e-6,4.02421e-6,5.07475e-6,6.13623e-6,7.58412e-6,4.07386e-6,4.10620e-6. They approximate the exact supremum of the scalar formula using k=390.68,u=1.5871. They are neither exact suprema nor directed bounds. The original strict ceilings remain unchanged. Global sharpness of the prescribed weight-dependent PDE scheme and a new inverse or existence result remain OPEN. REFUTED if read without the positive-margin domain: sup over all s>0 of s(mu-C*s)^2 is finite. T1's proof uses the correct unsquared concave function and the correct domain, so its theorem is unaffected.
Proof SHA256: 5dd594c0b033ce0a2b7d6bcb9343d5aa1b18ab2357f615c86e6ae719b49bb487.
Result SHA256: cea6f1b33b29f713aac0d95bbafcad4a494b50a724fa0d365069925be4e717fd.
Checker SHA256: 9b03697d2a555011bc117f0dbc2d2321c56d4169270f6b92d0ac1e613ad4f2a4.
T1 acceptance SHA256: 59be5bb22fde58d4beaa5dc937807b4c356f37c640e23339f027bf172c290b7c.

## T4-469: A divergence-free correction of the Hardy negative-norm upper bound

Date: 2026-10-29T15:28:38.611858+00:00.
Claim: for finite sine-mode F withrF inL2, the angular right inverse A_F can be corrected by Z=A_(Delta psi)-grad psi, divZ=0, givingH(F)^2<=M2+2tb+t^2a and, whena>0,H(F)^2<=M2-b^2/a. Distinct trial modes add while retaining every omitted mode inM2.
Method: standalone distributional and homogeneous-space proof before code. Proved exact positive log-radius formulaa=(pi/n^2)integral v''^2+pi integral v'^2 and cross formulab=(pi/n^2)integral r f_n u_yy dr. Derived exact rational moment representation compatible with the current test vectors. Exact two-mode manufactured F=-Delta psi tests use independent symbolic polar differentiation and exact antiderivatives versus beta moments.
Result and verdict: CONFIRMED for75 exact fixture checks, sign, pi/n^2 normalization and explicitly nonzero omitted-mode gap;0.656805seconds at2026-10-29T15:27:20.045448+00:00. The new general analytic statement is OPEN pending independent Opus review. The proof is supplied in full; no numerical candidate claim follows. Two exact test corrections recoverH2/pi=153/280; one-test upper1457/2520 retains the omitted gap2/63. This provides a possible alternative to assuming finite dual basis completeness.
Proof SHA256: efabe956aa103859e42f8240f270217a1738a732d590d0dd1f01be11377c2cbf.
Result SHA256: 144fd3c25a57d48302e5aa4f94012ae64204752d402c6dfdf6adddc7dafe595c.
Checker SHA256: 869ddaf2340145223d5ad0030308f5feba571ffc3f6b03268c981b7d5fc9c95c.

## T4-470: Candidate016 exact dual denominators and actual E2 ordering

Date: 2026-10-29T15:34:48.353220+00:00.
Claim: N4-396's complete exact-vector dual certificate impliesH016>0.529469576110512066428681 andE2(016)>608.392385921614>606.820219>E2(007).
Method:2099checks at2048bits, all100external source bindings and12frozen inputs, every663exact coefficient admissibility condition,338ordered beta pairs and82complete gradient groups integrated independently by rational beta moments in t. Exact denominators match both producers. Checked all131pairing-group endpoint/reconstruction records and full projection hashes, reassembled quotients from the full-precision production's final containing pairing balls, and recomputed every strict scalar square and energy comparison. No peer program or new candidate integral ran.
Result and verdict: CONFIRMED, with N4's source-bound full4096bit positive-pole pairing execution retained as the numerical premise. ActualE2 separation is>1.572166921614. Source execution253.482020seconds; own finite audit0.552784seconds at2026-10-29T15:34:10.802186+00:00. The first consumer schema failure is archived: basis_labels is descriptive text; exact labels come from x_rational. No input changed.
Serialization finding: CONFIRMED limitation, not a failed full-precision result. Re-summing the200digit per-group displays gives only[+/-6.92e40] for mode1 and[+/-3.63e31] for mode3. These saved intermediate displays cannot themselves certify the final pairing. The final200digit total balls and exact denominator give the stated directed quotients; the131coarse group sum is not called an independent pairing replay. A high-precision group sidecar or moment rerun is needed for that stronger archival claim. No H-only ordering, Hardy upper, optimizer completeness, correction-distance or existence claim follows.
Proof SHA256: 6122ca86e256550c6675daa71078932120c94f09d4ae7c04fba0afd1050583da.
Result SHA256: 5be9214bc6af162200802c7518eb64c5f1fe5382db3374c565b8a103eff726d2.
Checker SHA256: 2747d5c4be0a08b7b20e3559e56ef7a0fcd4132c50a5e3362f407f550c8bb8bc.

## T4-471: Published theory_v08 and THEORY_FINAL draft52 audit

Date: 2026-10-29T15:44:07.036919+00:00.
Claim: the published theory_v08 a35184b7 and draft52 82b4d9db preserve the accepted quantitative exclusions and correctly report their scope and current inputs.
Method: all156 and72 changed word blocks read; exact24 factor divisions,26distance rows and78factors, seven family-square checks,24 common-floor weak inequalities and accepted thirteen proof/result pairs. Recovered every139 Appendix hash:134 contemporaneous full matches and5 exact historical byte prefixes or frozen files. Frozen registry and numerics_v15 establish the028 chronology.
Result and verdict: CONFIRMED finite mathematics with695checks in2.722438seconds at2026-10-29T15:43:17.767410+00:00. The old2.7e-6 scalar cap is REFUTED as an implication of the registered high-margin algebra: TB-sharp s=1/4096,r=1536/1000000 has positive margin6651051/160000000 and L2 radius3e-6. This is not a claim that all other inverse hypotheses hold. Replace by3.7930e-6 for the fixed weights, or the separately scoped4.1069e-6 WU3 unweightedbL bound; no exclusion changes. REFUTED literal status/scope:001 matrixrow35 only membership (v140 already records its all-real-c affine theorem); every exclusion fixed-c and small-ball;028 unregistered (INDEX and numerics_v15 were published before v08); draft52's017(21,522) OPEN status (T4-460 already accepted it, still outside25probes). The unchanged conditional inverse hypotheses and endpoint certificate boundaries remain necessary. No existence closure, unrestricted nonexistence, candidate optimality or actualH ordering follows.
The first checker failure is retained: it used H/2 where the coverage certificate stores the conservative fullH coefficient. Both the proof and checker were corrected to fullH before acceptance; inputs unchanged. The strictE2 endpoints give an actual gap strictly above their exact displayed floor difference.
Proof SHA256: 2a1de0d23da9560e1464ea2915fdb7a7cb9a581772024ed91435219feca72ee6.
Result SHA256: c4c005dcd8f349ccdbc42c68fe87a9250d7d218f7b1c3dd0cb8ccb6ad3e0631d.
Checker SHA256: 80ad961eab2eab022e19ed149af3ba46500bc824ce43cb2c2e7db93798a78034.

## T4-472: Candidate016 cross energies and complete650digit group replay

Date: 2026-10-29T15:49:36.229646+00:00.
Claim: N4-398/399's two cross improvements and the complete four-pairing archive independently reproduce the dual floors and actual E2 ordering of T4-470.
Method: all663 exact coefficient admissibility conditions; independent rational beta moments in t for338 ordered pairs,82 cross energy and82 gradient groups;125 external bindings,25 frozen inputs and eight decompressed hashes; all262 saved650digit group intervals independently summed at4096bits. Every source exponent, endpoint order, numerator hash, positive-pole factor, complete projection hash, original containing ball and strict scalar floor checked. No foreign program or candidate moment integration ran.
Result and verdict: CONFIRMED finite coefficient, interval and scalar composition,3113checks in1.768388seconds at2026-10-29T15:48:59.658430+00:00; fresh staging passed15:49:16Z. The four pairing replays have1356,1351,1387,1384 relative bits and absolute input radii below1e-250. Retains the source-bound complete projection and positive-pole integral soundness/execution premises. Strict cross improvement sum is59664789113139289718803/250000000000000000000000. ReproducesH016>0.529469576110512066428681 andE2(016)>608.392385921614>606.820219>E2(007), gap>1.572166921614. The new650digit sidecar discharges the intermediate-log replay limitation; original200digit logs remain insufficient and unchanged. OPEN numerical H upper until fullM2 is accepted, and general469 theorem until Opus review. No basis completeness, exactH, correction-distance or existence claim.
The first consumer failed before numerical assertions because the external receipt is a dated dictionary with rows, not a list. Its code/manifest are archived; only the schema read was corrected, no proof or frozen input changed.
Proof SHA256: 023ee6d44fa3fa4b5ea231569266c1e245c27160326f4334262fd3b7da937274.
Result SHA256: 111d25b9726e54d92184c7fadbca89487e68a6a5882099c65ea40023b64748e5.
Checker SHA256: 25c6e953c7e64146f76c5570577e22405456d97b1753a445af41371bb598af56.
N4 archive result SHA256: c3e148aaab94ed6b50920f114c80260cb7f0061756398a90f6f444fa6b0367c6.

## T4-473: Exact-constant relaxed budgets and directed display successors

Date: 2026-10-29T15:52:46.555768+00:00.
Claim: T2 handoffBN's exactK/v relaxed budget displays, the review of T4-459 revision2's directed bounds, and the reported correction to the theory_v08 delta displays.
Method: complete informal scalar proof before code; independently reevaluated exact Gamma/elementary K,v at1024bits and rescaled T4-468's accepted exact polynomial brackets. Compared whole intervals against exact six-digit rounding cells. Independently verified24 rational weak-root floors by integer-square inequalities,48 displayed lower endpoints by exact decimal cells and8 family upper displays by rational squared inequalities. Exactdelta and its50-place enclosing fractions computed fromc0.
Result and verdict: CONFIRMED,290checks in0.029006seconds at2026-10-29T15:52:09.047084+00:00; fresh staging passed15:52:18Z. Factor sqrt(k/K)u/v lies near0.999983125683069758510778304103. Seven rounded values:3.34624e-6,4.02414e-6,5.07467e-6,6.13613e-6,7.58399e-6,4.07379e-6,4.10613e-6. These concern the exactK/v relaxation only, not the full weight-dependent prescription. All56 revised lower/upper displays are directed as labelled. REFUTED the0.44764... delta displays at theory_v08 lines189,413; exactdelta=1824676646553933/4076476460239181=0.44761123101073246431935044179100532374519968543159... . No exclusion or inverse hypothesis changes. T2's approximate12digit interval endpoints were not imported as directed bounds.
The first run passed all290checks and wrote its result, then failed only in final console formatting because the stream variable shadowed the numerical factor. Original code/manifest/result are archived; only stream naming changed. No proof or numerical input changed.
Proof SHA256: c56267463623768c89587602459ff6a917a76f3088929fda60146c0ff69f87e9.
Result SHA256: 1f61d931fdb49e1d62dcc6480b9e13cd22aadbe19dc8e74f47fe4a895b469d07.
Checker SHA256: 6b91d2189e4647b8d4c3f259310d0a59d2480f26ee63d4d24b471beac19cfca6.

## T4-474: complete angular Hardy certificate from a partial low-mode calculation

Date: 2026-10-29T15:59:00.192903+00:00.

Claim. For real locally integrable S1 F with rF in L2, a complete odd prefix below N gives H(F)^2<=M2<=S/N^2+sum_(n<N)(1/n^2-1/N^2)S_n. Exact prefixes decrease monotonically, retain all omitted mass, and lose at most S/N^2 relative to full M2. With469's separate hypotheses, subtract its divergence-free improvements.

Method. Wrote a standalone distributional polar proof including the origin cutoff and infinite angular expansion before code. Bound10frozen inputs and checked720exact rational identities, directed inputs, complete tail sums, monotonicity and known-solution153pi/280. Used467's accepted rF upper solely for a maximum prefix-loss estimate and472's accepted cross floor solely as a conditional composition. Executed no candidate moment integral or copied peer program.

Result. All720checks passed in0.12285890523344278seconds. For016, the N=33 loss is<0.046888012202<0.047. Fresh stage passed15:58:34Z. No new numerical candidate H upper follows without its actual compatible prefix inputs. Proofafd349a713799271446eb9f3ae4676af93227eebc18bc2fef2af9fc189aa9414; result5eef39af9c96f1d14dc39b95c8e5eca9ff394af701ee7c46f87ca07224cb3524.

Verdict. CONFIRMED finite arithmetic, known-solution fixture and directed gap bound. OPEN independent Opus analytic acceptance of the new corollary and any new candidate upper. Refuted omission schemes are recorded by exact fixtures. See audit record partial_mode_hardy_certificate, proof and team note 253.

## T4-475: Opus acceptance of the divergence-free upper theorem, exact added examples and a necessity-wording counterexample

Date: 2026-10-29T16:06:11.776580+00:00.

Claim. T2 the review of T4-469 confirms the complete finite-mode theorem469, its positive-pole supplement and residual-energy identity, with remarks R1 to R5; its Section1.5 also says the ungrouped condition beta_min>3/2 is necessary.

Method. Read the complete frozen review, Python source,59-check log and output. Rechecked the distributional polar identity, origin, gradient completion, absolute pairings, Gram orthogonality, sign, endpoint cancellations and complete-source requirement. An independent exact polynomial-beta implementation reproduces every rational example, all seven trial/source Gram identities, the half-test triangle, directed rounding and full2x2 Gram correction. A separate exact rational antiderivative confirms the pole3 closed form; its scalar enclosure uses512bit Arb. Copied peer code was not executed; no candidate integral was evaluated.

Result. 193 checks passed in0.06279615778476seconds; fresh stage2026-10-29T16:05:29.884762+00:00,16bindings. The cancelled n3 test u=r^3(1+r^2)^(-3/2)(1-t)=r^3(1+r^2)^(-5/2) has ungrouped beta_min=3/2 but admissible energies d/pi=5/12,a/pi=25/432,M2/pi=205/432. The positive-pole closed form is -28442/9009+(34256/59049)sqrt3*pi.

Verdict. CONFIRMED T2 analytic review acceptance, with469 now AUDITED under its exact hypotheses. REFUTED necessity for ungrouped beta_min; the original sufficient subfamily and every candidate input are unchanged. R1's direct derivation, R2's sufficient grouping qualification, R3's general finite-mode identity, R4's explicitly conditional infinite-series extension and R5's full-M2 requirement are accepted. T1 R1-049 remains a separate pending reciprocal review. Any numerical upper for016 stays OPEN until a complete compatible Hardy input or an accepted474 prefix bound is supplied. No inverse, existence or completeness-of-trial-basis claim.

Proof SHA256: 5f3dbd5fd86235ef97212a2ed460c927d82f435ccdc8c2f54a212f52269fe63c.
Result SHA256: b38a40ce5a1fc2147cf5c43a178b986b1f96c8932527be00f36c5a40ffac85fb.
Checker SHA256: c9364628cc1d81211f338cad1e9ce907fdfe36d7756e69b35490c0c28a13f1d5.

## T4-476: complete candidate016 upper from a four-mode prefix

Date: 2026-10-29T16:13:02.435385+00:00.

Claim. N4-403's complete mode1,3,5,7 prefix, combined with the independently accepted total rF norm, gives an upper for the full160-mode Hardy quantity. Through the reviewed469 theorem and472's strict two-mode cross floor it gives a whole-field upper for H(F016) and the identical registered E2.

Method. Read the full N4 Hardy and angular-tail proofs and programs, including REPLAY_SCOPE_v02. Bound12frozen source files and rehashed140external source-graph files. Rechecked1360 canonical branch records and160-mode support, every included ordered pair and124complete group metadata records. Independently summed exact dyadic endpoints of every650digit integral ball, multiplied by a containing8192bit pi/2, and proved all N4 prefix endpoints contain the new enclosures. Recomputed positive-coefficient and split-tail formulas as exact rationals, with their difference exactly sum(U_n-L_n)/81. Inserted467's accepted full component endpoints,472's dual and cross floors, and475's accepted Opus review.

Result. 2297 checks passed in0.22318091010674834seconds; fresh stage2026-10-29T16:12:28.143317+00:00,23bindings. H016 is strictly between0.529469576110512066428681 and0.944107; the uncorrected complete upper is1.063013. E2(016) is strictly between608.392385921614 and722.969. The existing actualE2 ordering007<016 is preserved. Full omitted energy is retained even though only4 of160mode integrals are replayed. The bound should tighten with a longer certified prefix.

Verdict. CONFIRMED finite complete-field upper and improved composition under the accepted source-specific construction, positive-pole moment and outward-serialization premises. This checker does not reconstruct the full residual numerators or reintegrate candidate moments; it independently composes their source-certified group intervals. This is a numerical whole-field upper, not exactH, a correction-distance bound, inverse, contraction or existence theorem. T1's reciprocal469review and the general infinite-mode474review remain separate; the finite candidate needs neither an infinite-series limit nor all160 individual integrals.

Two consumer failures are archived. The initial check tested overlap of one lower endpoint instead of the complete replay interval and unnecessarily demanded containment in the old rounded source mode. The second retained the analogous unnecessary containment on its square-root displays. Both were replaced by interval consistency, exactly as the frozen source REPLAY_SCOPE_v02 already required. Containment of every N4 prefix endpoint and every directed H/E2 bound remains checked. The exact group sum is the enclosure premise, never mere overlap. A separate diagnostic formatting failure hit Python's default4300digit limit; the checker already removed that limit. No proof or numerical source changed.

Proof SHA256: 5c1350cf713e5ef5367b54e4a2fa528a2799ef514bd74536c4f66fe78c4e1635.
Result SHA256: 1c91f2e3507891bf04ec694147022c0c837fee06b0ab489f4dffab7833b08a37.
Checker SHA256: f69798d3caf74093ea560ddc00693a41f84fb12dbdb5dcea236aa8264f2806af.

## T4-477 | 2026-10-29T16:17:52.205690+00:00 | R1-048 and R1-049 reciprocal review acceptance

Claim: T1 review set 46 confirms the N4-396 dual lower bound and ordering, and independently confirms T4-469 and its positive-pole/residual-energy supplement.

Method: Read the complete review, both complete peer scripts and logs. Reproved distributional angular divergence, domain/trace, gradient cutoffs, dual optimization, polar cross energies and residual identities. Parsed peer source maps without executing their scripts and matched all nine data inputs to existing own accepted originals. Reconstructed rational manufactured energies and27 differential shift fixtures. Independently checked the exact dual/archive/prefix composition. 209 checks in 0.0498503758572042 seconds; one fresh staged replay also passes. No candidate integrals or peer code ran.

Result: CONFIRMED reciprocal R1-048 and R1-049 under their explicit source-pairing premises. The650-digit archive premise is already independently accepted in472. T4-469 is now independently reviewed by both Opus theory lanes. The exact pairwise gap E2(016)-E2(007)>1.572166921614 remains valid. T4-476 separately supplies H016<.944107 and E2(016)<722.969 from a complete-source prefix bound. R1-049 V9 N3 Hardy display observations remain CONDITIONAL. REFUTED R1-049 V6 exponent7/10 attribution of its FLOAT example: the code and comparisons use7/5. This transcription error does not affect the theorem, exact fixtures or candidate values.

Verdict: CONFIRMED with stated scope; REFUTED the single FLOAT example attribution; OPEN narrower N3 upper values, inverse and existence.

Evidence: `audit record reciprocal_hardy_review_acceptance, proof` sha256 `0ed6f993a43094ca6b647eada80bebe453404519cd6e1e0693621fc0bd431ba3`; result `3595001545461938d6f5819ba772a528932137a4d69cb9bfba6a9a667fc58687`; checker `74ba845ce1f0b3322ebae1989c8fe007d202e10ebdcaad364e5f705b3b3c0207`; frozen review `349cb718f4242514e9c714e0a10430f3f96192df111e66819e7a13868530e205`. Existing model collaboration is configured us.anthropic.claude-opus-5-5; actual provider identity is unobservable.

## T4-478 | 2026-10-29T16:23:59.906457+00:00 | Prefix endpoint ordering in the work-in-progress T2 review

Claim: the split upper Q and positive-coefficient upper P satisfy Q-P=sum widths/N^2>=0; the inspected draft's reversed comparison is false.

Method: standalone exact proof, then44checks using exact accepted016 endpoints,18 manufactured interval lists and a rational nonzero counterexample. Read the original476 output definition and freeze the actual peer draft/result. No candidate integrals or copied program execution.

Result: strict Q>P for016; the stored476 upper is P. Both formulas retain H<.944107 and E2<722.969. The frozen peer draft has34checks and two recorded failures. The general474 review is pending. Two own reader failures and their original proof/code/log objects are preserved and explained in the topic.

Verdict: CONFIRMED the exact ordering and persistence of both accepted upper displays. REFUTED the reversed work-in-progress partG comparison and split-field attribution. This refutes no completed review, candidate certificate, or general theorem.

Evidence: proof `fab210682563e93e3d40e286f9ba8a74edf731c4d4fdd75afc29bd6fd49dbb31`; result `ad1a1cf07d089ef3b0957b755ec649990ed23fa91db98a3ccceb7ec62ecdf1fd`; checker `d5321ef01f758dc642711adefc98a887ffab449a2437f3fa6114a2f84b8f9d4e`; frozen peer draft `c36e1af53cd09db48d3cc39e053e13ef4b6ba0f0439d1bbca718c0ca9a4b938a`.

## T4-479 | 2026-10-29T16:34:47.489134+00:00 | Frozen16:30 report audit

Claim. The coordinator's frozen Answers in brief, Short answers and comparison table correctly compose the accepted theory and numerical records. Frozen report SHA256 244c9c223dad0925c570d594cb4afdfcbbcb8196d5981a6c8cf024827813f838; matrix v149 SHA256 6a6c2bc0fac0460b0add7b2e6d139bd49eb30d6973e96180a8d8543c668c0982.

Method. Read all three requested sections in full, and the exact earlier defect theorem and its accepted result. Independently parse the106 physical table rows into108 distinct matrix entries and compare every status and primary candidate association. Check296 cited audit IDs,24 weak inequalities, seven scalar ceilings, both graded displays and nine directed factors. Recompute the g=0 defect specialization as exact fractions and check its contraction estimate. Recheck the accepted frozen016 bounds without promoting later data. 823 checks passed in 0.14760918077081442 seconds. Fresh stage at 2026-10-29T16:32:28.523099+00:00 passes17bindings and one full replay.

Result. CONFIRMED all108 status and candidate comparisons, existing conditional theorems and their stated limitations,24weak exclusions, correction budgets, and the frozen H016/E2 pairwise enclosures. No candidate verdict changes. REFUTED the absolute maximum claim at frozen lines22-23 and110-111: the already audited T4-065 with g=0, m=B=0, s=1/5184 and weights(32768,1048576) admits epsilon=40722836401/193491763200000>2.1046e-4 at r=201799/149299200. Even the old r=1351/1000000 permits2.1046e-4. The selected sharpw2.1035e-4 remains valid; restrict its maximality to the selected matrix tests or include this existing specialization. No new candidate certificate or inverse is supplied.

Clarification. Lines1035-1036 should say that factors use exact registered thresholds before rounding the table displays. Row25, line1062:4321.48/1.0578e-4>4.08e7, while division by the printed1.06e-4 does not give that strict factor. The exact registered factor is CONFIRMED.

Verdict. CONFIRMED the stated finite composition with those qualifications; REFUTED the unrestricted strongest-threshold wording; OPEN existence closure and numerical records not accepted at the freeze.

Three own parsing failures are archived. They concern106physical versus105ordinary-numbered rows, matrix status prefixes, and a parenthetical state131 reference in row51. These were consumer assumptions, not report errors. The frozen sources and original proof remain unchanged.

Evidence: PROOF.md 4da91e5f325d05308a735c473034eeb277e23dd5e38e7296ce64068dbf1f23a1; verification/result.json db307cd256cf766c0f3ec53cfea77c124b5be258ea0664e64280786bb1e1b569; code/check.py 35f0d59443e42b73b133944f4035d663a63d2e01a0eac32c127809b5f22bef25. No foreign code, candidate integral or model client ran. Existing theory collaboration is through configured Opus5.5 lanes; actual provider identity is unobservable.

## T4-480 | 2026-10-29T16:36:20.712517+00:00 | Candidate016 prefix31 complete upper

Claim. N4-409's sixteen odd-mode certificates through31, with the accepted full rF norm, enclose the complete160-mode Hardy upper. The accepted two-mode divergence-free correction improves it to H016<0.619652 and E2(016)<629.296113.

Method. Standalone proof before checker. Read and bind N4's complete angular-tail proof and replay clarification. Freeze24inputs, rehash152original source-graph bindings read-only, and independently sum exact dyadic endpoints of all484650-digit group balls at8192bits. Recheck1360unique ordered branches,160odd frequencies,33Cartesian construction checks, every endpoint exponent, positive pole, exact-decomposition metadata and complete group count. Every published prefix endpoint contains the independent enclosure. Recompute both complete upper forms with exact difference sum widths/1089. Insert472's exact dual/cross certificates and467's component endpoints. Both Opus reviews of469 are already accepted475/477.

Result. 4463 checks passed in 0.682767297141254 seconds, fresh stage 2026-10-29T16:35:54.660699+00:00 passes37bindings and the full checker. Plain H016<0.789068, improved H016<0.619652, and 608.392385921614<E2(016)<629.296113. Retained lower H016>0.529469576110512066428681. All144 omitted modes are covered by the accepted complete rF energy; they were not integrated here. The pairwise actual energy gap E2(016)-E2(007)>1.572166921614 remains valid. Candidate016 remains excluded by its independent correction distance.

Verdict. CONFIRMED the complete finite source-bound upper and the improved H/E2 composition. This discharges the requested T4 reproduction of N4-409. Retains the accepted full residual construction, source-specific positive-pole moment enclosures and outward serialization; no hash is a substitute for those proofs. No copied peer code, candidate integral, inverse, contraction, exact H or existence claim. The general infinite-series474 review is a separate theorem and is unnecessary for this finite candidate.

Evidence. PROOF.md eca40cc89d04f89e78ba7f314e64144fda81c4b41d4e5cbb8583d390c40c7815; result.json ab005a62f3e3c27385ac50a1d1148879b5f9e8eccd0bcab0ec0b6f390b746cd1; checker 1365398ac5ce1bfc2da4cb97594e1c2df73924ad313ba008ffb597686d0415a5; frozen N4 result01019cd56639661ace672791a4fbe7f938d90bf02237b93b38f061238bb15b41. No failed run. Existing Opus5.5 collaboration is file-based; actual provider identity remains unobservable.

## T4-481 | 2026-10-29T16:42:29.297234+00:00 | Both reviews of the general partial Hardy theorem

Claim. T1 R1-050 (review set 47) and T2 the review of T4-474 establish the infinite-mode theorem474, including the origin, complete-prefix tail, directed upper and finite divergence-free improvement. Their candidate arithmetic and exact manufactured fixtures agree.

Method. Read both full reviews and programs, without executing peer code. Standalone proof before checker. Independently justify angular Parseval, whole-plane distributional divergence, local integrability, positive coefficient comparison, monotone convergence and distinct-frequency correction. Recompute polynomial beta moments, eight planar parity pairings, the infinite-mode sgn(y) source, its exact cross -256/1155, all seven prefixes and four exact fixture lists. Parse T1's source map and bind T2's nine declared inputs and474's ten manifest rows. Recompose both N4v01 and T4-476 candidate endpoints and all seven omitted-energy bounds. Retain accepted candidate construction, moment and outward-serialization premises.

Result. 263 checks passed in 0.0685273902490735 seconds; fresh stage2026-10-29T16:41:40.081731+00:00 passes30bindings and the checker. The two independent Opus reviews are accepted. The complete general theorem474 is now CONFIRMED with F real, locally integrable, even in x, odd in y, rF in L2 and every odd n<N included. Correction tests have distinct frequencies and satisfy469's domain hypotheses. Candidate prefix7 gives H<.944107, E2<722.968760. The stronger accepted prefix31 H<.619652, E2<629.296113 is480, separately.

Verdict. CONFIRMED both analytic reviews and exact fixture/candidate composition. REFUTED R1-050 V7's attribution of the intermediate decimals1.129995949,1.063012676,.944106346 as directed uppers by exact squaring: each lies inward of the bound it displays. Safe displays1.129995950,1.063012677,.944106347. The repeated R2 display51.061045287604983 is below both exact endpoints; use outward[51.06104528760498,51.06104528760499] or label approximate. This does not refute the coarse theorem or those H inequalities as consequences of a different stronger certificate. Clarify V4: the formulas coincide iff the included interval widths vanish, allowing loose total U. Local integrability is a separate hypothesis, and tests at the same frequency require the Gram form. FLOAT quadratures stay observations. No new inverse or existence result.

Evidence. PROOF.md 8759fa7e82ba42a70a623f5de89b6f3d669f6a71c2e3fe12ee3e7339a00730bc; result.json a5b3659c90eaf13bbe068e64a72c056a21f2307446d7ea9c2639e598a9d8ca78; checkerdc4d95b42d74d994ec3a24147d4b8c1014d6a15c3e03c0c79f4effe26e56a4be; frozen T1review4d26ce8f7a8199acb97359236125a962ec24561727c07ad847ec7c7c8a217fe9 and T2review620c2928ffb457eb9ae04fd95f4fdadd93fb9213909197919e7a7d89f5875289. Peer logs4783checks7.1s and35checks26.99s retained as peer reports. No failure or candidate integration. Existing Opus5.5 collaboration, actual provider identity unobservable.

## T4-482 | 2026-10-29T16:47:45.608305+00:00 | THEORY_FINAL draft53 and its exact optimizer

Claim. Draft53 incorporates471's scope repairs, states the new Hardy/dual implications and identifies t=1 as the optimal divergence-free correction.

Method. All24 changed line blocks read against accepted draft52. Standalone proof before checker with its immutable margin erratum. Bind25originalinputs plus erratum, eleven accepted audit results, complete component endpoints and472's independently resummed650digit b intervals. Combine b with pi times the exact rational a at2048bits. Complete the square, check strict signs, sufficient H threshold, displayed energy ordering,017diagnostic factor and frozen report's outward007/017 decimal renderings.

Result.77checks passed in0.027471505105495453seconds; fresh stage2026-10-29T16:47:21.828175+00:00 passes26bindings. CONFIRMED changed theorem scopes, 3.7930e-6 common cap, fixed-floor weight hypotheses,001 every-real-c affine exclusion,028FLOAT registration,017diagnostic acceptance, finite Hardy gains and strict E2(007)<E2(016). BOTH general474reviews are now accepted481; prefix31upper480 supersedes the historical prefix7status. H>.522193054 suffices for E2 comparison. Actual certified margin exceeds1.39percent and rounds to1.4percent.

Verdict. REFUTED literal exact optimizer t=1: mode1 has a+b in[4.1421104592540737411244715984629817906232044989062849338931075e-39 +/- 6.66e-101]; mode3 in[5.7927634026693551384457408394674131081828144944377208478492887061e-38 +/- 3.85e-103]. Both are strictly positive. Thus exact tstar=-b/a<1, with0<1-tstar<1e-34 and0<(a+b)^2/a<1e-68. Choosing1 remains a valid upper bound and changes no directed improvement floor. Correct text to approximately1. REFUTED inward007/017 displayed endpoints as renderings of the claimed source enclosures; use007[606.8181534,606.8202172],017[605.4068697,605.9589546],H017lower.6144195987. The017 certificate remains OPEN/CLAIMED, and its comparison gap>.8591 is conditional. No inverse, correction distance or existence conclusion.

Evidence. PROOF8694cd5b77fe069ae4f38d7300183c4ea21c7a31cce1f631ddc1a1f871e0418f; ERRATA_v01eea54680fd74946fd4a88f30f6bd5cec0a06bc5f90d79e9e5bfa27ecff03b667; result3a9ea1efd41c1ce882b950b4e41b81953ee31d4f9eb527d0da1c14343feab48b; checker9a3c21937e84e7db5a7dc031edf545134562d809535c2ed696b802618cd67be2; target51647b68b4833b370cc47b3efe5777befa24e1810f593f549180eaceb1326397. Two own preparation failures retained: directed1.4percent margin corrected to1.39percent, and staging helper omitted named erratum, now copied. No peerprogram or candidate integral executed.

## T4-483 | 2026-10-29T16:50:38.865889+00:00 | R1-051 acceptance and opposite actual norm orderings

Claim. T1 R1-051 recomposes the N4-409 prefix31 upper and N4-410 complete H/E2 enclosure correctly; N4-412 proves opposite actual H and E2 orderings for007 and016. R1-051 E4 to E7 repair the prior directed displays.

Method. Read complete T1 review,54-check program/log, repaired4783-check program/log, N4-410 and412 proofs. Standalone proof before checker. Parse peer source map against nine immutable accepted inputs. Verify revised program has identical assertions. Recompute16mode positive/split formulas, complete144mode tail, all interval widths and prefix sums, both H and E2 squares, strict endpoint subtraction, and repaired displays. Decode007 H lower ball into exact finite decimal endpoints. Bind accepted480484groups and472deep source energies/pairings without repeating integrals. All domains, normalization, source regularity and canonical local term are retained.

Result.131checks pass in0.09008776908740401seconds. Freshstage2026-10-29T16:50:07.590620+00:00 passes27bindings and its replay. Main R1-051 and N4-410 finite implications are CONFIRMED: .529469576110<H016<.619651337324093367770781451079 and608.392385921614<E2016<629.296112162914. N4-412 CONFIRMED: H007-H016>.015873038675998, whereas E2016-E2007>1.572166921614. All E4 to E7 repaired uppers, lower/upper total R2 endpoints, prefix7 no-improvement E2<=763.064677 and seven tail ceilings are accepted. These results have the accepted complete source and both Opus469/474 reviews as premises, and do not depend on N3's narrower claimed bracket.

Verdict. CONFIRMED main exact review and opposite actual residual norm comparisons. REFUTED the literal R1-051 V7 FLOAT phrase at most0.9888 ofR2: exact accepted prefix fraction is strictly between.988805 and.988806. Use about.9888 or rigorous upper.988806. The main theorem and endpoints are unchanged. FLOAT consistency remains conditional, with no integral certified by overlap. No correction-distance, inverse, existence or overall-quality ordering.

Evidence. PROOF3786f045c8641d78ee673f229ee7b2e0793406bfc89f3f0c2a7531f91fa252c0; resultc32b0e1d700dade06f581551f1c1f21c4a6e2044dd019f01ae14dd6230da1a31; checker6a062efa4fcbd0310767e69cc76d85d1a68aecbf1200f44fdebbab393a4a48e5; frozen publishedT1review f7a43c40237c554e26a0412e36436a0ff325aee007a135c115d739a3a5b8dcd8, peercheck79f98f5f2446ec705844e35186f2caa08c3d9af6cb4eddd17687ccd3821a4415. No failure, peer execution or new moment integral. Existing configured Opus5.5 collaboration; actual provider identity unobservable.

## T4-484 | 2026-10-29T16:56:09.784340+00:00 | Candidate017 conditional total and residual identity

Claim. N4-413 proves the coarse candidate017 H/E2 displays under its explicitly OPEN source premises C1-C3. The queued017 replay's dual and weighted residual formulas have correct signs, domains, normalization and endpoint conditions.

Method. Read both413proof versions, its checker, both frozen N3 producer programs and the queued replay proof. Freeze13files, losslessly compress4datarecords and independently rehash all29peer input bindings. Write standalone proof before checker. Recompute all160mode energies, sixteen alternative residual uppers, sixteen dual lower squares, complete144mode tail and all positive E2 terms with exact rational endpoints. Check2312saved nonzero trial labels for beta>3/2, origin harmonic regularity and exact rational coefficients. Derive the logarithmic-radius formulas, cutoff convergence and residual square independently. Check exact manufactured psi=y/(1+r^2)^2, d/pi=4/15,a/pi=12/35,QDelta/pi=64/105, including six signed multiples F=lambda Delta psi.

Result.2982checks pass in0.18458967888727784seconds. Freshstage2026-10-29T16:55:36.455166+00:00 passes19bindings and a fresh replay. Conditional .6144195987<H017<.6165956396 and605.4068697<E2017<605.9589546 are CONFIRMED. Conditional E2007-E2017>.8591964>.8591 follows from accepted007. Residual identity Rn^2=Qn+2n^2(b-p)+n^2(a+d), the corresponding forward/reverse triangle bounds, sixteen-frequency dual lower formula and radial formulas are CONFIRMED under the stated integrability hypotheses. Source trial labels satisfy the sufficient admissibility conditions. N4's repaired directed comparison of stored upper versus primitive upper is correct; a conservative upper need not lie in the primitive interval.

Verdict. CONFIRMED conditional finite consequences and analytic identities. OPEN actual017 full Hardy integrals, residual trials beyond the pending selected replay, complete G0/G1/P2, actual H/E2 bounds and actual017<007 ordering. Replaying16duals and2residual trials cannot discharge C1-C3. The historical residual code hash1944bedc... differs from current615478fe... and remains unobserved. Four incomplete diagnostic strings are rejected as balls. No inverse, correction distance, normalization control, existence or closure.

Evidence. PROOFf3b2e7ded4f09359119175d975b45344fa0a5f04d4eb491ac0072df816cf5475; result581543f29421e571e68801c311e9721fa58e7bb422616226017c12ee92edb0e5; checker2b51e8ce9641b0f6c4937eecd14f16595a05c3d2a43ef20b452bbd6f192c0e56. Frozen N4-413 result309a3946afa3d503e0b3559b787ca92d910cf043e11a85c6ff3228770cac0e52. Own firstchecker incorrectly assumed extra integer beta2 at every mode; source labels show(n+3)/2. Failure, original checker and original manifest preserved; theorem unchanged. No foreign execution or candidate moment run. Existing Opus5.5lane collaboration, actual provider identity unobservable.

## T4-485 | 2026-10-29T16:59:10.529710+00:00 | T2 reciprocal sharpw maximum review and report repair

Claim. T2 the T2 check of T4-479 (sharpw max) correctly confirms the fixed-norm self-map maximum and the old-radius improvement identified in T4-479. The current coordinator g=0 repair and007failure factor are valid in that scope.

Method. Read complete review,17-check program/result/log and corrected framework text; freeze six files, including current report raw2248f2c58de2d8b7b635de1ffa649223e72c1665afff5946cd922c4b4c8e3b75. Standalone proof and residual-budget clarification before checker. Bind peer input hashes to frozen16:30report and T2framework. Compare exact polynomial coefficients, optimum and old-radius rates, directed pi bound and contraction square, slope, other-s derivative and complete accepted007forcing factor. No foreign program or candidate integration runs.

Result.57checks pass in0.012183052022010088seconds. Freshstage2026-10-29T16:58:30.601603+00:00 passes14bindings. At fixed s=1/5184,w=(32768,1048576), eta*=40722836401/193491763200000 and r*=201799/149299200 are the unique maximum/radius of r(mu-Ar), subject to the stated nonbinding contraction and slope conditions. Exact c_s r*<.02746 gives contraction<.01373 and slope>.67254. Oldradius1351/1000000 already admits2.1046e-4. The accepted007same-norm forcing lower bound misseseta*by morethan3594606. Currentreportg=0repair accepted.

Verdict. CONFIRMED T2 reciprocal review and finite report repair. The maximum is of this sufficient estimate at fixed weights and s. It is not a largest theorem tolerance across incomparable norms, an optimum true inverse constant, a necessary PDEcondition or a candidate closure. The zero-defect correction g=0 waives no background, origin, hyperplane, range/domain or residual membership hypothesis. The s0=97/496250 arithmetic is correct but belongs to a different norm. Distance exclusions unchanged.

Evidence. PROOFcbf0d53a80d0b33cf833eddafc2bb388792e4cb02f7c88ee4a122d2d04ba2e9a; ERRATA_v01a3f11c869a829e58e2d376a7ffc834d8e3d047f6abeaa4ba9d03d1b89524bf97; result46eeefeaa1fdb35a0e6698c5573decc0550f8ae9de509a4e740a9b0a830cdc05; checker737d53d93179672108e1fb89772c9dc60d0b37ce3b37e17b8626a00a5777c513. Frozen T2reviewdae1f3895fc984cfe32ff0418087eeb988bc0b363b5f088ea346c6d65385b057. Ownpreparationusedincorrectfrozenfilenameandwasarchivedbeforechecker; no numericalfailure. The clarification applies the radius-dependent Lipschitz and slope estimates after the residual self-map budget. Existing Opus5.5collaboration, actualprovideridentityunobservable.

## T4-486 | 2026-10-29T17:04:42.692870+00:00 | Complete sixteen-mode016 dual/cross replay and whole-field composition

Claim. N4's completed sixteen-mode exact dual and solenoidal source certifies stronger actual H and E2 bounds for candidate016; one may select the better deep trial in frequencies1and3, separately for lower and upper bounds. Source proof88a0c8df..., producer resultc89c1735aa4dc582c4d32fd1d729613cf5a6ead38c9e1ed349869ef13a5381cf completed17:02:58Z after2448.7240375480615real seconds and6925checks.

Method. Read the full producer proof and code. Freeze56files and rehash all137producer dependencies. Independently reconstruct all1224rational coefficients,81ordered beta pairs per mode, and every exact d/pi and a/pi by t-monomial beta moments instead of the producer's powers-of-v integration. Match complete projected branch sets against accepted1360branch residual. Reparse all2130signed650digit group enclosures and reprove strict floors against their sums. Select max within modes1and3, never add same-frequency tests. Compose the alreadyaccepted T4-480 complete prefix31 upper with all144omitted modes. No foreign code or candidate integral executes.

Result.13380checks pass in1.8559805760160089seconds. Freshstage2026-10-29T17:04:05.090157+00:00 repeats successfully,70bindings. Directed actual enclosures: .616733500735 < H016 < .617952953855 and628.580088525 < E2016 <628.879024750. Accepted007gives H007-H016>.017571422145091 and E2016-E2007>21.759869525. Exact squares, all individual floors and the complete upper are in result.json. This upper improves the earlier two-mode .619652 bound and the unaccepted N3 .6189603636 display, without using N3 residual-trial upper data.

Verdict. CONFIRMED finite full-field norm enclosures, retaining the accepted exact residual construction and source-specific positive-pole moment soundness/execution premises. The general divergence-free theorem is already accepted from BOTH Opus reviewers (T4-477); complete-prefix theorem T4-474 is accepted through T4-481. Actual upper assembly is therefore discharged in this audit, although the standalone producer correctly leaves its external premise OPEN. Candidate016 remains RULED OUT by the separate correction-distance certificate. No exact H, optimal trial/basis, inverse, contraction or existence claim follows. Candidate017 C1-C3remainOPEN.

Evidence. PROOFe285200450294afaf50b3604b647c735456da8878e8b760907e65c7d06c6178a; resulta478c6015c40a9a737cab7afbea99fae6062abc464ac938b002b2c266156ad4f; checker0f1da68ceff7de21a7139176fbc8ae7fbc91484ba359fb2080b0303038f2ac38; source rawresultc89c1735aa4dc582c4d32fd1d729613cf5a6ead38c9e1ed349869ef13a5381cf. Two ownreader schema failures are preserved with original code/manifests/logs: compressedfilename and list-of-two projectioncounts. Both precede completed aggregate arithmetic; no candidate datum, moment or theorem changed. Earlier maintenance inspection hit Python's integer-string limit and was left as an inspection error; the actual checker explicitly removes that parsing limit. Code/source are the certificate-source subfolders, not a Lean formalization. Existing Opus5.5collaboration through sharedteamfiles; actualprovideridentityunobservable.

## T4-487 | 2026-10-29T17:09:36.906596+00:00 | Theory draft55 and E8 to E11

Claim. The16changes since draft53 and review set 49/v50 repair the reviewed claims, preserve the conditional017 status and correctly describe the verification record. Frozen draft55 aa2d306329e3a653d089824eebf9ee741c3383af60c17e0bf61f7deee4325169,2269lines.

Method. Read every changed block and both errata files in full. Recheck the exact sufficient H threshold, positive nonunit optimizer displacements, split-minus-positive coefficient identity including its equality case, allfour prefix endpoint ratios, selected sharpw rate/radius product and quadratic optimum. Independently parse83candidate-row references and78exactfloor factors. Freeze all180README file bodies losslessly, verify hashes and parse Python source without execution. Check source counter semantics and saved output.

Result.492checks pass in0.42141477297991514seconds. Freshstage2026-10-29T17:09:36.860015+00:00 passes34bindings. E8-E11 and allmathematical changes retain their stated scopes. The 017C1-C3 premises remainOPEN. REFUTED two literal textual assertions: every failure factor uses2.1035e-4, and check_v50.py ran33checks. Correct the first to the quoted selected sharpw forcing factors. The second has13after PartA and20cumulative after PartB, hence20total, with no reset. Correct review set 50, THEORY_FINALsection12 and the README row. READMErow_refs/h18_verdicts input columns stillnamev151 although scripts/provenance usev153.

Verdict. CONFIRMED mathematical repairs, selected-radius arithmetic,180hashbindings,83references,78exactfloors and conditional statuses. REFUTED the universalfactor scope and33count claims; provenance input-column correction above. No theorem or candidate verdict changes. T4-486 subsequently strengthens016 bounds beyond this valid draft55 enclosure and should be incorporated at the next freeze. No candidate integral or foreign code executes.

Evidence. PROOFf35e8fad6a11b243ac53efc1fa81b7ae90c95d1e7c717ba34ddc26986d9be52c; resulte2a54857aff1b7e03e41c2edffe2e162591111f05fb15bcbe0b4a1fef86dd720; checker7c5b49275ba768965438e1ad5b1f11684c9050855312d2f10c70adc1af5d6406. No failed ownchecker run. Archive source/README_graph.tar.gz contains17,789,067original bytes losslessly in6,785,824bytes. Existing Opus5.5file collaboration, actualprovideridentityunobservable.

## T4-488 | 2026-10-29T17:15:12.787481+00:00 | Complete016 reciprocal bounds

Claim. N4-417/418 use the selected tests, complete whole-field Hardy upper and norm definitions already accepted independently in T4-486, and their narrower printed bounds are valid.

Method. Read the complete producer proof and checker. Compare every selected floor in16frequencies and all16Hardy modal source endpoints with the independently resummed intervals from480. Recompute complete positive coefficients, both H squares and all E2 component substitutions exactly. Check every narrow endpoint by exact squaring and both007gaps by exact subtraction. Use the accepted477/480/481/486 analytic and finite chain; no imported status flag substitutes for this chain.

Result.121checks pass in0.08857820089906454seconds; freshstage2026-10-29T17:14:45.981343+00:00passes20bindings. N4's exact lower squares equal486. Its upper Hardy square is slightly larger than486, with difference exactly sum(1/n^2-1/33^2)(source_upper-independent_upper), strictly between0and10^(-500). Its E2 upper square differs by (20/21)2^18 times this quantity. All narrow displayed endpoints pass. In particular actualE2(016)-E2(007)>21.759869526341; actualH(007)-H(016)>.017571422145091. All144omitted modes are retained.

Verdict. CONFIRMED complete N4-417/418 bounds and opposite same-norm orders. REFUTED the initial own exact-upper-equality wording; the corrected standalone proof and exact enclosure relation replace it. Both own failed comparisons are preserved: first exact-upper equality, then equality of the007exactball endpoint with a coarser old rational display. No field integral or producer program executes; no existence or correction-distance verdict changes.

Evidence. PROOF79fd54cabc81935c4996942b9e20e44d60a94db2cd6b3e7c060304afba4ad25e; result2392099d178c6f0a1de27c11e26eec69c33694faeca54266096a8dd3ab384dd7; checker56f79428debc659f1a5ec670b02a78ef4b64e1fd95b26818c60a8810aa12c95f. Source N4-418 result8eec600612f7719a1c0cbcb408d1665659b8d2c06d861f032a102651953c3728, N4-417 result285dac39d93e32574c214d00cef9764087c0718c19b4042398c7ec728b530840. PROOF revision precedes corrected checker; originals and both failures retained.

## T4-489 | 2026-10-29T17:17:54.361392+00:00 | T2 review469revision2 and report479repair

Claim. the review of T4-469 revision2 repairs the erroneous necessity claim without changing the sufficient theorem. The T2 check of T4-479 (report repair) correctly validates the specified historical report excerpt and exact scalar-budget arithmetic.

Method. Read both reviews, both complete producer scripts and saved results. Diff all three changes from the original49583d59 frozen review accepted475. Independently reconstruct the cancellation example by exact polynomial beta integrals, including both divergent single-term coefficients. Check the source excerpt's exact hash and32numbered lines, three optimum/radius blocks, completing-square identity, registered-radius budget and strict007factor floors. Bind the accepted475/485results. Peer programs remain text.

Result.86checks pass in0.0066772401332855225seconds, freshstage2026-10-29T17:17:16.267435+00:00passes19bindings. d/pi=5/12,a/pi=25/432,M2/pi=205/432. The two uncancelled terms have source-square coefficient81/r and gradient-energy coefficient9/r, but their sum is admissible. The fixednorm optimum and radius agree with485; factor floors3594606and3596535.57pass. All three review changes are accounted for. The excerpt is verified as a frozen artifact; its whole historical report provenance is producer-recorded, not independently recovered here.

Verdict. CONFIRMED both remaining T2 review repairs in their stated scopes. The earlier necessity claim remains REFUTED and is now explicitly repaired. No new candidate, inverse or existence assertion. One own schema failure, M2 versus the older key M, is preserved; no mathematical value changed.

Evidence. PROOF7e015a3c8f365d7c784031967825203f0e864aa6f439d73368ffe2d05f13d3f0; result2b9e7bdd801f9b854bec8625cc15a88e3a6a542edb4f657f9c02d466e98bbcc6; checkerda2f38c623a02c2a9debf75b3cceeda3475f6fd4bf30c1ac3cefa4c5ddfd6511. T2review4693eb37f0fe791a01cbd849d135e6467edfb031922e831c84214b378c94bd7a1f9. No field integral, foreign code or remote model runs.

## T4-490 | 2026-10-29T17:22:34.875137+00:00 | Exact full origin Taylor jet of candidate007

Claim. The saved exact candidate007 satisfies all five nonconstant degree-two and degree-four Taylor equations for R_f=F/y to2e-13, as universally claimed in NUMERICS_FINAL lines53to54. N4-419 instead exhibits a y4 counterexample.

Method. Read the complete N4 and N1 proofs, scripts and output as text. Independently expand the2982 exact generators through potential degree8; all60 relevant generators and140radial terms are included. Use Delta(H_m z^s)=4s(2m+s)H_m z^(s-1), verified against Cartesian differentiation term by term, to construct the density; use Cartesian derivatives for the velocity. Exact convolution gives F through degree5. Parity and derivative order prove discarded terms cannot affect this jet. Compare every saved N4 potential, density, velocity and residual axis coefficient by exact rational equality. Check five strict rational intervals and the center relation.

Result.3181checks pass in0.1260867021046579seconds. Freshstage2026-10-29T17:20:18.019816+00:00passes14bindings. In the order x2,y2,x4,x2y2,y4, the directed intervals are(-2.96505e-12,-2.96504e-12),(-4.26994e-12,-4.26993e-12),(1.45669e-11,1.45670e-11),(-2.32866e-12,-2.32865e-12),(2.0899e-11,2.0900e-11). Each absolute value exceeds2e-13. The constant is exactlyzero and c+u2_y(0)=1, with rho_y(0)>0.

Verdict. REFUTED the universal saved-candidate tolerance claim, for every one of these five coefficients of candidate007. CONFIRMED N4-419's axis counterexample and the already disclosed N1 referee finding. This concerns the saved exact rational potential, not an earlier optimizer stage. Exact center normalization, far-field and all inverse/existence/distance verdicts are unchanged. No failure or new candidate.

Evidence. PROOFecd049c2ecfd177cbdcd8107e02182d223a9bda24a7d29aa018b2936123d0f14; resultf0d5d2427bb66c4f0f80183ff2b6d129611ad5a63c406f11974342b9a0e955c7; checker8a48dc1cdae52eaf72b899740445c112bf741447a7789d1a248a4e6e9634a52d; rawed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21. Full polynomial jets, source manifest, proof-first receipt and directed intervals are in research/candidate007_taylor_tolerance. No foreign program or field integral was executed.

## T4-491 | 2026-10-29T17:28:26.288085+00:00 | T2 final-summary scope and draft55 corrections

Claim. The T2 final summary (17:25,7986a0886a628726369236b5bf8fb714a0692118cb435d26e68c5434d9ea8eb9) calls007 the closest candidate, states a necessary scalar distance below3.79e-6, and calls0.99998313 the exact relaxation factor. T2's BS checker gives draft55 scope and display corrections.

Method. Standalone informal proof before checker. Freeze10sources; compare all47draft55excerpt lines to the complete frozen draft, all32own ledger lines and6original theory_v01 lines. Independently check a rational scalar parameter counterexample, allseven family-square upper comparisons, exact Gamma/elementary factor in512bitArb, both defect boxes, rate reciprocals,005floor and index conversion. Peer code is parsed and read, never executed.

Result.278checks pass in0.01291451882570982seconds; freshstage2026-10-29T17:28:26.244393+00:00passes19bindings. Scalar example s=1/4096,r=3791/1953125 admitsL2budget3.791e-6 with beta=1957759/20000000000 and positive forcing1e-7. Rate, contraction and slope all pass. The common upper3.7930e-6 is valid. Exactfactor lies in(0.99998312568,0.99998312569). Actual inverse upper displays9.6432,6.4226 are valid although the displayed intermediate quotient equalities are false. Both defect maxima require their own m,B,s. Draft55 AJ2status, norm-family attribution and registered-floor corrections are supported; add beta/slope hypotheses to any complete closure checklist. Original graded bound4.5717e-4 remains valid by the stronger exact estimate.

Verdict. REFUTED3.79e-6 as a uniform scalar-budget deduction, not as an independent theorem about actual PDE solutions. REFUTED0.99998313 as the exact factor; correct nearest rounding. OPEN the actual closest-candidate ordering, since weak lower bounds do not rank unknown distances. CONFIRMED T2BS source/arithmetic corrections in the stated scope, including conditional AJ2only. No candidate or existence verdict changes. One preparation failure from a live summary update17:15to17:25 is preserved before any checker ran.

Evidence. PROOF30c6f770367cbc2bcf8fd98c8d4c060bd859a5026687a2b54497d5c5f3c2f283; resultb27deb5f9e5b18ad8a1244909cee39548bb47ba303741b87e6ef062d090fcf8b; checkere25111f855b78dc3eae4400d122bd02909e8bc84a5c75b8cd2f428179aea9887; research/t2_final_summary_audit contains exactJSON, complete argument, source binding and fresh-stage evidence. Actual Opus5.5provider identity remains unobservable; collaboration is via existing theory lanes.

## T4-492 | 2026-10-29T17:33:07.708360+00:00 | Final numerical-report literal and source-scope audit

Claim. N4-420 reports600 rounded displays and six finite-source scope corrections in NUMERICS_FINAL frozen17:02, hash3c10441009b5d7932df153d145673148264de2f20c32e2ec601c6ed28077eedf.

Method. Write the complete informal proof before checking. Freeze18small peer sources and reuse three explicitly hashed own accepted dependencies. Independently enumerate all200 old/new/ratio rows, reconstruct decimal place sizes and rational comparisons, recover complete extrema, bind twelve-step versus final candidate hashes, and inspect the exact far-correction source label. Parse and read peer code without execution.

Result.1340checks pass in0.13002271810546517seconds. All600displays round correctly as serialized FLOAT data. Complete first-mode007/013 range runs from26.8456... at k128 to9358.8588... at k12. At(19,600),023/016 is44.4183... after12steps and26.1665... in the final40step file. Over all25probes, final023/12step ranges0.5815766... to10.2622079... . The two024hash descriptions conflict, as already distinguished427; no unobserved write time is inferred. The far contribution is a finite asymptotic correction without a certified remainder. Freshstage2026-10-29T17:32:40.424496+00:00passes26bindings and all24files. Initial syntax failure is preserved before correction.

Verdict. CONFIRMED N4-420's finite arithmetic and source findings. REFUTED the five universal or conflicting literal descriptions, restricted to the saved FLOAT/text records. OPEN the asserted exact complete far part. Field names do not certify pairing accuracy. No candidate norm, correction-distance ranking, optimization cause or existence claim follows. All candidate-framework verdicts are unchanged.

Evidence. PROOF9b76ff6809931a6ba48610dd80d2cbe59460c588004604c9055ba8102a9e257c; result6a6eb78df150f120041b6f4091a44b9eafc420bf9303dce08d8589adfcf6b905; checker51786f97d0b6a78acc12d55360f050565fbcb60119c92ca2f9eb3d27d3a3f4f0; research/numerical_literal_review_acceptance contains proof, exactJSON, source manifest and verification. Collaboration with Opus continues through the existing T1/T2/coordinator files; actual model provider identity remains unobservable.

## T4-493 | 2026-10-29T17:38:43.439068+00:00 | Theory draft58 and reciprocal review R1-052

Claim. THEORY_FINAL draft58 f76c41fb4e5f3733e5f0ac2749120c80a9771349b97ab83f61bcfe86c059f91f incorporates the late016 bounds and BS repairs. R1-052 in review set 51 recomposes the sixteen-mode certificate and describes its width.

Method. Read all31 changed blocks, the complete review and its checker without execution. Write the standalone proof before own checking, reuse accepted486/488 inputs and own487 source archive, freeze9 changed archive members, and independently check exact rational bounds, width identity, endpoint rounding, closure margins,83row references and78directed distance factors. Verify all186READMEhashes. AK2 is specifically the parity-sensitive63/32 squared Hessian bound, not a blanket handoff acceptance.

Result.535checks pass in0.46210148371756077seconds. All norm endpoints and opposite007/016 orderings pass. Width U-L=sum(qU_n/n^2-J_n-L_n^2)+(RU-sum qU_n)/33^2; mode17to31 share rounds0.651, tail0.349. Every term is a difference of bounds. R1-052 V8's difference below3.6e-11 is false: the exact lower endpoint differs from0.6167335007 by a number in(3.64e-11,3.65e-11). The selected-threshold universal sentence remains false because the same paragraph explicitly quotes the eta* comparison. Freshstage2026-10-29T17:38:22.616140+00:00passes30bindings,21files,4Python and6JSON parsed, one inexpensive replay. Failed draft-version expectation, failed proximity claim and corrected handwritten timestamp are preserved.

Verdict. CONFIRMED R1-052 under its already accepted numerical and analytic premises, and the31draft changes with the scopes in PROOF. REFUTED R1-052 V8's3.6e-11 proximity and the literal universal selected-threshold sentence. OPEN017whole-fieldC1-C3, unreplayed016modes33to63, correction-distance rankings and existence. No candidate-framework verdict changes.

Evidence. PROOF645cde457ea62fab51ae6d9a636e59ae5126b4db562d800cdbccd051b945c15d; result744c9208a35206d4aad5093bc48f28e34f8807a6f58218e807a959d66b2c7a53; checker4392f0887c3e26c72cf7f58258e106688cc7e5ff6c42b54b1cd2411341d65c68; research/theory_final_draft58_audit. Existing Opus5.5 collaboration continues throughT1/T2/coordinator files; actual provider model identity remains unobservable.

## T4-494 | 2026-10-29T17:40:28.344511+00:00 | Numerical report successor and N4-422

Claim. N4-422 accepts600 unchanged displays and several requested repairs in NUMERICS_FINAL6ffe5ea8fc6f971650b0037f70c89c6b866a08f672b573a15ad4d6a91abfa6b3, while identifying two remaining literal defects.

Method. Full proof and supplement read before own code. Freeze7small sources. Transfer every200 exact five-field display tuple from492, sort all25saved023values, recompute the four selected ratios, inspect the actual09:13and11:00note sections, and compare016endpoints with488. No peer code or field integration.

Result.294checks pass in0.02243858575820923seconds. All600displays unchanged. Actual global largest four are(19,1800),(19,1200),(19,2400),(23,2400). The listed subset's ratios are exactly40388338190095206/43015474594738885 through16169779966494155/15994649763252204; nearest displays0.94and1.01, while1.04is a loose upper display. The09:13note and the work log printcurrente171c051, and11:00refers to reconstructed58586004. Freshstage2026-10-29T17:40:08.784601+00:00passes17bindings13files. No failures.

Verdict. CONFIRMED N4-422's finite repairs and600display transfer. REFUTED the largest-four and09:13hash-attribution descriptions. OPEN independently unobserved chronology, full017norms and existence. These are text/FLOAT-source findings, not new PDE values. No candidate-framework verdict changes.

Evidence. PROOF642bfea2e77bfbb6878b9a548624c9d330301f64525401a87abdd0dd81097544; result25adcb3437686a8d92e9da4ca7c1e43f5d96fa0d85a7330c7ef1346efd9189f4; checker1ddc1468a16446b92b52aa804708b1b9228de03ade97a3fd88f154683face8fc; research/numerical_repair_successor_acceptance.

## T4-495 | 2026-10-29T17:45:53.199324+00:00 | Candidate017 partial replay, N4-425

Claim. The complete sixteen saved dual trials and residual trials at modes1 and3 imply a whole-field H lower bound and two individual modal enclosures. They do not establish the full017 upper norm or E2.

Method. Read the complete producer proof, schema supplement, projection and moment proofs and checker before own verification. Freeze52 direct sources and194 producer bindings. Independently reconstruct1472 rational coefficients and1424 ordered energy pairs with Beta-moment recurrence, then sum all1339 signed650digit interval groups at4096bits. Recompute the cancellation-sensitive residual identity and compare strict rational endpoints directly. No peer program or field integral ran.

Result.10450 checks pass in1.9664848512038589seconds. H017>307209799380023711068567013529/(5*10^29)>0.614419598760. The actual H1 and H3 lie strictly between the exact endpoints in the result. Source hres historical program hash mismatch remains explicitly unobserved; proposed exact vectors are checked independently. Fresh stage2026-10-29T17:45:24.927611+00:00 passes59 bindings58 files. A supplementary proof-history file was omitted from the first staging list; failure metadata are retained, the byte-identical failed staging copy was pruned, and the repaired fresh stage passes. Mathematical calculation had no failures.

Verdict. CONFIRMED the complete sixteen-mode dual lower sum and two residual-mode enclosures under the stated exact source and moment soundness premises. OPEN full017 H upper, E2 and actual017<007. Of T4-484's premises, the sixteen duals, two residual trials and two Hardy squares are discharged; fourteen residual trials,158 other Hardy squares and G0/G1/P2 remain. No inverse, distance ordering or existence claim. All registered candidate-framework exclusions remain.

Evidence. PROOF8b77ec10b524bedf1bb1ef5492515c3d444cba7699f5ad85bc2cd9f4aea91d7f; result0247900877c34e23227b8d181a5788893d727d9399a16a9b369a9c9d92bf7755; checker8f6ed90cb7994119ad8715743686b93203753763256c42919f51f4cae4b3c667; research/candidate017_partial_replay_audit. Producer result7e093982e733237262819ca3ad0486f85bdc4d31c69d73a99e382dbad5c3ab06.

## T4-496 | 2026-10-29T17:47:07.763513+00:00 | Numerical report literal completion, N4-424

Claim. Report0b0b1e898c54648b792471298b6f6c50d90a30783a7e76fd4c1c80fc57eb9422 repairs the two T4-494/N4-422 findings while preserving600 accepted displays.

Method. Full N4 proof and code read, four direct sources frozen. Compare every line against494, all200 five-field records, all25 exact reconstructed twelve-step values, within-mode maxima, complete final ranking and selected ratios. Inspect the two hash-attribution sentences against494's accepted evidence. No peer code or field integral.

Result.310 checks pass in0.01528506027534604seconds. Exactly two lines changed. Four selected probes are unique twelve-step maxima in modes19,23,25,31; the different global final four and nearest0.9389/1.0109 displays pass.024 current and reconstructed hashes are correctly attributed, and save times remain publisher testimony. All600 displays unchanged. Fresh stage2026-10-29T17:46:42.609712+00:00 passes12 bindings9 files. No failures.

Verdict. CONFIRMED both specified literal repairs and display transfer. No further finding from494 remains. OPEN entire-report acceptance, unobserved save events and017 whole-field norm claims. T4-495's partial017 update remains separate. No candidate-framework verdict changes.

Evidence. PROOFee18ea7288ec323aeed9d22bac25f0b6b9a0f75599a71a918ea6fe5ba794d568; result5b6fb6fdab942c4f55cb36e0740c5c1a5995b306eaf38a95dd03fd801e29b3ed; checkerce5be5b2908b126ef0f13195ccd7b61cf36e469fca9f10c57c7eb86e043800b9; research/numerical_literal_completion. N4-424 result857cdac52d9e3598787d36dc8b7976566be5580233f091b6f6ffde1c6779e303.

## T4-497 | 2026-10-29T17:51:52.439646+00:00 | Theory draft 60 and review set 52 repair acceptance

Claim. Draft 60, 8bac7dfc4a62c315297c0d54bc1f42812afbeb85dc2868af93c41e06c45ce137, repairs the scalar cap, first-mode rounding, positive-rate reminders and both T4-493 literal errors. review set 52 E13/E14 makes the corresponding review repairs.

Method. Read all 18 changed blocks against the accepted draft 58, the whole errata review and the changed producer code without execution. Write a standalone proof first; independently check exact subtraction, budget example, eight cap squares, graded upper, ratio roundings, source inheritance and the complete table references and directed factors. Check all 186 README entries, with 184 inherited unchanged and two directly replaced.

Result. 452 checks pass in 0.07897149911150336 seconds. The exact H proximity is in (3.64e-11,3.65e-11). The selected-threshold sentence now exempts eta*. Scalar cap 3.7930e-6 and stronger graded cap 4.5717e-4 are valid in their stated families. The one added producer comparison explains its 89-check log. All 83 row references and 78 factors match matrix v161. Fresh stage 2026-10-29T17:51:32.640641+00:00 passes 22 bindings, 13 files, 2 Python and 4 JSON files, one inexpensive replay. No failure and no repeated candidate integration.

Verdict. CONFIRMED all 18 changes and review set 52 literal repairs under the accepted theorem and numerical premises. The draft predates accepted T4-495 partial017 lower/two residual-mode evidence and T4-496 numerical completion; those are additional evidence, not a discharge of complete017 upper/E2. Existence and correction-distance rankings remain OPEN. No snapshot-framework verdict changes.

Evidence. PROOF 83cc3b41b2b678752ad7e6e81305245c259ae5e4e272341ec1506680f6133637; result b3b824edf34c308457b7d7f06ed232f5810a2f32a7b944c32f6b831e4ad060ff; checker eceec2d6bdb678eaa2b16fc13cd6b006ae960734601ad98f7852f642866b1c7d; research/theory_final_draft60_audit. Opus collaboration uses the existing T1/T2/coordinator files; actual provider model identity is unobservable.

## T4-498 | 2026-10-29T18:00:01.979352+00:00 | Complete prefix47 replay and tighter candidate016 upper bounds

Claim. N4-427/428's 24-mode prefix, with all 136 omitted modes retained, improves the complete H and E2 upper bounds for the same canonical candidate016 residual.

Method. Read the general prefix and complete assembly proofs and their code as text. Write the standalone argument before the independent checker. Rehash all 353 producer source bindings, inherit the first sixteen frozen mode files from T4-480 and freeze eight new mode files. Independently add exact dyadic endpoints of all 708 source-certified groups at 8192 bits; check complete pair/group coverage, every integrability and positive-pole condition, source field identity, all directed prefix endpoints, complete positive-coefficient tail formula and sixteen previously accepted dual/cross selections. Use T4-467/477/480/481/486/488 as explicit accepted premises.

Result. 6234 checks pass in 0.9680761550553143 seconds. Every 160-mode contribution remains covered. H016 is strictly between 308366750368225240013184170643/(5*10^29) and 617899375474255800449928932337/10^30; E2016 is strictly between 628580088526341/10^12 and 125773176230483/(2*10^11). The actual H007-H016 gap exceeds0.017625000525836 and E2016-E2007 exceeds21.759869526341. The independent interval upper is at least as sharp as the producer's; their nonnegative difference is retained. Fresh stage 2026-10-29T17:59:33.230844+00:00 passes47 bindings,17 files,1 Python,15 JSON, one inexpensive replay. No failure or repeated integration.

Verdict. CONFIRMED complete prefix47 and N4-427/428 two-sided bounds, conditional only on the explicitly retained and already accepted source-integration soundness premises. No new analytic premise remains for this finite assembly. Old488 upper bounds stay valid. OPEN complete017 upper/E2, actual correction-distance rankings and existence. No candidate-framework verdict changes.

Evidence. PROOF 81d9aa0ca377e92a4f808195cdaabec4ba8a0edd5730b5985fc37d03a4f8cb20; result 14b32ac0db315e492e47099f47feb59546bd6321743a1bdbd9fb1cdb8cd2f2dc; checker 86d88c54574fc53be11d92ffe1b82933f0716d9e1a5dfec2909790d8e89dbc17; research/candidate016_prefix47_replay_audit. Both general Opus reviews are already accepted; actual provider model identity is unobservable.

## T4-499 | 2026-10-29T18:04:40.006394+00:00 | Acceptance of repaired T2 summary and BT decimal sweep

Claim. The T2 final summary at5398df04b9433573fe796b788180db8f230ba44076da2a8b578e7ea66e70f62c repairs all four T4-491 findings; BT also corrects the moment coefficient and approximate decimal displays.

Method. Read all17 changed blocks against491, the full BT handoff, producer checker as text and its11-check result. Write the standalone argument first. Independently reconstruct the scalar counterexample, exact scalar and graded optima, moment coefficient and all21 decimal expressions in Fraction/512-bit Arb arithmetic. Bind the previously accepted exact factor and source hypotheses. No peer code executes.

Result. 80 checks pass in0.011537808924913406seconds. Scalar cap3.7930e-6 and graded chain through50/(651 sqrt28248) are correct; 0.99998313 is approximate; actual distance ordering staysOPEN. The exact moment coefficient lies in(5.04422709906931,5.04422709906932), so5.0442 is too small and5.04423 is safe. All21 sweep classifications match independently:5exact,16rounded. Threshold rounding gap9.1553e-6 minus3/327680 equals17/640000000000>0. Fresh stage2026-10-29T18:04:08.828964+00:00 passes14 bindings,11 files,2Python,6JSON and one inexpensive replay. No failures.

Verdict. CONFIRMED all requested491repairs and BT's moment/decimal corrections. Historical review-row shorthand0.99998313 is controlled by the explicit exact-formula erratum in current sections0,2.4,7. No candidate verdict or theorem scope changes. The producer's older failed classification expectations are documented by BT, not treated as successful runs.

Evidence. PROOFba47fa739e090ef7de1256b784ab8141c5298de3e304b99f188bbde555e31f96; resultb6ea3d21449ce57dfa6fc6bc5d1265200154da9b58cc05b6f43b5df33c0f20fb; checker2431563931c95ca8b7575059dc6ec26ccebbf910a26513ace472545862b67163; research/t2_summary_repair_acceptance. Opus collaboration uses existing T2/T1/coordinator files; actual provider identity remains unobservable.

## T4-500 | 2026-10-29T18:08:21.131468+00:00 | Exact final threshold divisions

Claim. N4-429's final exact-threshold correction uses 1/163840 for the X3 comparison and 3/327680 for the Ns comparison, without changing the candidate, component bounds or admissible theorem.

Method. Read producer proof, checker as text, result and frozen report/table sources. Write the standalone argument first. Independently divide the exact registered lower comparisons using Fraction arithmetic, compare old rounded denominators, verify source ball lower endpoints, and rehash all16 producer bindings. No peer code or integral executes.

Result. 83 checks pass in 0.012774489354342222 seconds. The X3 comparison quotient lies strictly between84699685 and84699686; the Ns quotient lies strictly between66246337 and66246338. The old X3 rounded threshold inflates its quotient; the old Ns rounded threshold is conservative. All candidate components and bounds are unchanged. The three named old X3 spellings are absent from the three frozen final sources. Fresh stage 2026-10-29T18:06:46.780552+00:00 passes17 bindings,18 files,2 Python,10 JSON and one inexpensive replay.

Verdict. CONFIRMED N4-429's exact divisions and bounded spelling check. REFUTED84699902 as the lower-comparison quotient obtained from these same data with the exact threshold. This does not refute84699902 as some separately supported lower bound on the actual norm ratio, nor supply such support. No theorem or candidate verdict changes.

Evidence. PROOF afd7ebf18448be81babe1ad765803fe864b495c00aebea7c0210b26477228e71; result 281dac96de569f847116c6e864a8f297d60c9be9a24c8ff441ee2dba64b799a5; checker 4ff2fd682f725ff367d787c0aad9cf01d3643efe0d7540b2aa64d9d7947559e7; research/final_threshold_division_acceptance. Opus collaboration continues through existing theory/coordinator files; actual provider identity remains unobservable.

## T4-501 | 2026-10-29T18:11:38.536650+00:00 | Both Opus residual-identity reviews and missing-n correction

Claim. T1 R1-053 and T2 the T2 check of N4-017 (residual identity) confirm the017 residual identity, admissibility and gradient completion; T1 also recomposes the accepted partial017 data. T2 R2 prints a cross-term bound without the required n.

Method. Read both reviews in full, all producer checker source as text and79/18-check logs. Write a standalone argument before the own finite checker. Independently differentiate finite radial monomials and use exact Fraction beta recurrences for T2's three examples, the known Riesz example and a counterexample. Compare T1's entire extract to own495 frozen source results/modes. Recheck endpoint powers, exact squares, widths, displays and source hashes. No peer code, candidate moment engine or integration runs.

Result. 398 checks pass in 0.026819384656846523 seconds. The residual identity and radial formulas agree. For n3,u=r^3(1+r^2)^(-3),F=Delta psi, dividing by pi gives d6/35,a2/63,Q=cross64/35. The printed sqrt(Q(a+d)) equals64/105 and fails by exactly3; the correct bound n sqrt(Q(a+d)) gives equality. Local integrability is necessary in the general distributional argument and follows for017 from its accepted finite smooth Cartesian potential. T1's sixteen floors and two mode endpoints match the own495 frozen records. Fresh stage 2026-10-29T18:11:16.371633+00:00 passes21 bindings,14 files,3 Python,6 JSON and one inexpensive replay.

Verdict. CONFIRMED both analytic reviews after correcting T2 R2, and T1's exact finite recomposition. REFUTED only the missing-n display. The corrected estimate still proves absolute convergence. No candidate number or exclusion changes. Full017 H upper,E2 and comparison017<007 remain OPEN. Source group soundness and actual017 structural identity are retained495 premises, not newly reconstructed in this acceptance.

Evidence. PROOF 153425f5922d69220cd62bec4dd8692040929fb50f23abb4cae3c8d21d0aa6c3; result e9efed4a188b06f7ea223b0f6fe0c7d692a2d50c16069d65a059b21a6c4f11c9; checker 7468adfc16a038c2f9efca4e53940c49f5cb20c1f671e1f4634cbecabe2f7db0; research/candidate017_residual_review_acceptance. Existing Opus T1/T2 collaboration is explicit; actual provider identity remains unobservable. Their FLOAT fixtures remain observations, not certificates.

## T4-502 | 2026-10-29T18:16:04.741790+00:00 | Final candidate016 prefix63 replay and complete upper bounds

Claim. N4-430/431's32 individually integrated modes through63, together with the complete tail of128 omitted modes, improve the actual complete H/E2 upper bounds of the same canonical016 residual.

Method. Write the standalone proof before the checker; retain PROOF with ERRATA_v01 for one stale136 prose count. Rehash all361 producer input files read-only, reuse24 accepted own frozen mode records and freeze8 new records. Independently sum all920 saved signed group endpoints as exact rational dyadics at8192bits; recheck every positive pole, endpoint exponent, complete ordered pair/group list,160-mode1360-branch representation, containing intervals and full tail formula. Compose the accepted16 distinct dual/solenoidal floors and all2130 trial-group premises of486, and accepted467/477/480/481/488/498 evidence. No peer program or candidate integral runs.

Result. 7564 checks in 1.1550934459082782 seconds. Strict H endpoints are308366750368225240013184170643/(5*10^29) and308948684181969723952067879861/(5*10^29); strictE2 endpoints628580088526341/10^12 and39304086799647/62500000000. Thus H016<.617897369,E2016<628.865389,H007-H016>.017627007636152781 andE2016-E2007>21.759869526341. All previous lower bounds are unchanged and upper bounds remain valid. Fresh stage 2026-10-29T18:15:39.602950+00:00 passes57 bindings17 files1 Python15 JSON and one inexpensive replay. The producer upper exceeds the independently resummed upper by a nonnegative amount below10^-500, retained exactly.

Verdict. CONFIRMED N4-430/431 complete bounds and every omitted-mode contribution under the retained accepted source-specific integration premises. REFUTED only the stale136 prose count, corrected by ERRATA_v01; first preparation replacement failure retained. No candidate or exclusion changes. Full017 upper/E2, correction-distance rankings and existence remain OPEN.

Evidence. PROOF 8db3d74da38b58139914a5620db918bc1b9e0ca1bfb2636c73c5a513080c3c5a; result e3ca43736903ef7d6437159a61f0282cc427fc432a58dc516ad8b87c0fccd6ba; checker 226140916cbaa660f4b33af6a5cdc99001d655cc4e9c24807ca2b5dc1760cf28; research/candidate016_prefix63_replay_audit. Both general Opus reviews already accepted477/481. No new analytic premise or field integral.

## T4-503 | 2026-10-29T18:17:38.511556+00:00 | T2 corrected R2 and N4-432 source-origin review

Claim. T2's18:14 revision1 repairs the missing n in R2 without changing its analytic conclusions; N4-432 independently confirms the same analytic identities and supplies local integrability for the actual017 residual from its2174 exact potential generators.

Method. Read the revised review, all three changed blocks, N4 proof and both new peer programs as inert text. Write a standalone argument before the checker. Rehash all257 N4 producer inputs; freeze7 small source files. Compare every T2 erratum fixture and N4 fixture to the independent exact501 results, recheck Cauchy-Schwarz squares and factor3 counterexample, and inspect every exact raw017 generator with its complete type, arity, indices, rational coefficient and positive radius. Reuse own accepted raw/projection convention and495/501 proof premises. No peer code, quadrature or candidate integration.

Result. 4710 checks pass in 0.2851671683602035 seconds. All three review edits are precisely the bound and provenance repairs. All2174 generators are smooth:262mono,1660leg,252legqs, with radii1 and50. Even potential implies F odd in y and smooth, hence F_n=O(r) at zero. Correct cross bound n sqrt(Q(a+d)) and all exact fixtures agree both ways. Fresh stage 2026-10-29T18:17:18.831742+00:00 passes19bindings14files3Python7JSON and one inexpensive replay. No failures.

Verdict. CONFIRMED T2 revision1 literal repair, N4-432 main review and candidate-specific origin condition. T2 R3 is discharged for the actual017 source, without using Q alone to infer local integrability. The old missing-n display remains REFUTED and preserved in501. Full017 H upper,E2 and017<007 remain OPEN; no candidate or closure verdict changes.

Evidence. PROOF 519d6e2857d52747138051fd54dd95969664c2c22f5db12a1829c992941b64bf; result 8962b227b2b561864010d4ed57a6330ebd1a961c273e09f74b024d3588514f5c; checker 092b160f2cd57f03aa2f7e633730bb41e74fffbdb9e1d15da63af74fe3bfc245; research/candidate017_review_repair_acceptance. Reviewed T2 2ce074267abc712072958a29be0d6a61a9171d4f95eb87d9562627d5427ae915; N4 result ec2d4e90b3666a0b5d2c5b605a650a4cad0ef358b1881d2dc64ffc02570e8bdb. Configured Opus collaboration continues through existing peer files; actual provider response identity is not observable.

## T4-504 | 2026-10-29T18:23:51.073668+00:00 | R1-054 prefix recomposition and width-allocation scope

Claim. R1-054 recomposes the accepted47/63prefix bounds and splits the H-squared enclosure width. Its V5 attributes the majority of the width to the dual lower bound.

Method. Read the complete review, producer checker, extractor and output as inert files. Freeze their hashes and write the standalone argument before the independent checker. Compare the extracted exact fields and long-field hashes against own frozen N4 records, independently sum the positive-coefficient formula, trial floors, full tail, all32modal endpoint pairs, two width identities and rational share brackets. Reuse accepted498/502integration premises. No peer execution or integration.

Result. 473checks pass in 0.11596820503473282 seconds. The retained16mode gaps comprise(.681,.682) of prefix47width and(.682,.6835) of prefix63width, respectively; both exceed2/3. The stored split fields do equal the split expression and exceed the positive form by the exact positive endpoint-width term. Main H/E2 values and actual norm ordering agree with498/502. Fresh stage 2026-10-29T18:23:19.367067+00:00 passes19bindings10files1Python4JSON and one inexpensive check. No failures.

Verdict. CONFIRMED finite recomposition, complete tail, norm endpoints and width identity. REFUTED the inference that this identity locates the majority specifically in the dual lower slack: every retained gap is upper slack plus lower slack, and the identity does not separate them. Actual allocation remains OPEN. Correct V5 to say most width lies in the modes1to31 enclosures; additional Hardy modes alone cannot remove it with the existing low-mode intervals/trials. No candidate, bound or closure changes.

Evidence. PROOF 3d53245ceaf62beaaef59ae517c99603643e463031a63785ab2038e79533a5d4; result c926b67282d73f4270c612fe80d77aac20179d69e4f8e3c47fe0bf10c090a083; checker 3f0e49ceca5dd1cb0103b3715404047980d16c0720126ef898039c2f4f304360; research/prefix63_opus_review_acceptance. Frozen Opus review b1c92ba7680293fe854b6da08054f2f0a9340427281a3c2b36689fe0802ff9ce. Both exact interval allocations g/4 and3g/4 demonstrate the logical ambiguity, without making a claim about actual modal energies.

## T4-505 | 2026-10-29T18:26:05.584373+00:00 | R1-054 E15 mathematical repair

Claim. review set 55 E15 repairs the unsupported lower-slack inference in R1-054 and adds the fixed-input qualifier; its open share brackets contain the printed FLOAT shares.

Method. Freeze and read all E15. Apply the already proved504 width identity; compare both exact shares against their accepted rational brackets and nearest-three-decimal rounding intervals. Source-bound standalone addendum written before these finite checks. No peer code or integrations.

Result. 9 checks. The mathematical repair and fixed-input qualifier are correct. The prefix47 open bracket(.681,.682) does not contain the rounded display.681, although it contains the true exact share and is consistent with that rounding. Prefix63 display.683 is inside its bracket. No exact bound changes.

Verdict. CONFIRMED E15's main mathematical repair. REFUTED only the literal phrase that both open brackets contain their rounded displays; use "consistent with the rounded FLOAT shares". Actual allocation between upper and lower slack remains OPEN.

Evidence. audit/theory_audit/research_code/prefix63_opus_review_acceptance/REVIEW_REPAIR_ADDENDUM_v01.md 1cab997cfe870be7cb109b3f8c85d607a52a8558f6dbece184f20c4144ef46c3; verification/e15_acceptance.json 0aa1f1773fa7b30b810ae638e9281eb58a0bc26ae09f6e944009cad866ecb77a; frozen E15 bc15f3409c15d7e9de8574cfba8d07787dcd57d437511d5484636a08392c1d5e. No new theorem or candidate verdict.

## T4-506 | 2026-10-29T18:34:04.779884+00:00 | Final THEORY_FINAL draft65 and E16

Claim. The final batch T text (2459lines, target55406b637f5e6c23c0abe0335ec6eab183af73967842a5591c2644663ab61a62) correctly incorporates the accepted prefix63 and partial017 results, exact threshold repairs and retained-mode width interpretation. review set 56 E16 repairs505.

Method. Read all19 changed blocks from accepted497draft60 and E16. Freeze final text, matrixv170, README and every20neworchanged artifact. Write standalone proof before checker. Recheck195READMEhashes,83matrixreferences,78directed floors, finite exact016/017endpoints, factor-n fixture and both H18ASTs. Eight compressed historical matrices retain their accepted decompressed hashes. Peer programs remain inert. All numerical source moment/projection premises stay inherited from accepted495/498/500/502/503/504; no candidate integration.

Result. 828checks in 0.2665066127665341 seconds. Fresh stage2026-10-29T18:33:39.473010+00:00passes53bindings34files7Python8JSON. All mathematical additions and table mappings agree. One raw line-wrap reader failure was archived and repaired by whitespace normalization. No bound or matrix verdict changes.

Verdict. CONFIRMED mathematics, source bindings, all19changed blocks subject to the literal correction below, and E16. REFUTED only 'This document quotes neither ratio.' in section2.5: the preceding sentence prints84699685and66246337, as does item94. Delete that sentence or replace it by 'These corrected ratios do not alter any earlier norm bound.' Full017Hupper,E2and017<007remainOPEN; no existence or correction-distance ranking follows.

Evidence. audit record theory_final_frozen_audit, proof 6fb31f4d39ccee51f3103bcbe811bd72a3747e446879100c80849867afba9d64; result 99dc9d25b95b3f2cddaf8848e328747638a3b86ea497b76bc30899fca6eb389a; checker aa19961f36dd8faba444b603fcfe5c786f2fa32258d5f338023dbc6c0253a782; manifest 79787abf4c8ba908168c80d3ff2aff60104a18f66a1dbfc548990b532b0dcbe4. Final main T4 synthesis stays frozen through505; this is a dated addendum.

## T4-507 | 2026-10-29T18:38:05.017031+00:00 | Final T2 summary

Claim. The final T2 summary692lines,13cd15cdadfcc1ac07e94dd08157d5740f66e8ee98ab54ecc658fdcfb6722a0f, correctly adds the017 residual review, exact fixtures, factor-n correction and source-origin qualification to the accepted499 version.

Method. Read all4changedblocks and full linked review. Write standalone analytic proof before checker. Recompose four exact rational residual examples from accepted501 inputs; check the Riesz triangle and dual inequalities and missing-n fixture. Bind current review to503, historical text to501, and all2174 origin generators to503's accepted result. No peer execution or source integration.

Result. 73checks in0.020175504963845015seconds; freshstage2026-10-29T18:37:45.434281+00:00passes19bindings11files. R^2/pi=63/110,667/945,349/210 and1959/20020. All four additions are supported. No checker failure. Two initial shell reads used the wrong diff pathname and were corrected to source/changes.diff before the audit; no mathematical data changed.

Verdict. CONFIRMED final T2 additions under the accepted hypotheses. The beta=3/2 divergence example refers to its specified single trial n=1,k=0; beta_min>3/2 is sufficient, not necessary for every finite sum with possible leading cancellation. Complete017 H upper,E2andactual correction-distance ranking remainOPEN. No theorem or candidate verdict changes.

Evidence. audit record t2_final_frozen_audit, proof 5747c0382f746471d03a493ea2426cb3eb009787ef00326c263604854eb0765c; result8f234ff62e3832f8d030a623976b64a3c37e13719eab25092a4218eb88548ad7; checkere7cc34336c6b165b5e353a9a0dab6734409305aff6aaa0e98c6638afeb4ab3f2; manifest3688f3fa3ea8819483358c808e81c8967baf700019c9581d4f89e01bf61906f6. Main audit/map remain frozen through505.

## T4-508 | 2026-10-29T18:44:43.829025+00:00 | Coordinator's frozen final report

Claim. the frozen copy of this report of 1837Z, 7fd963af5ac20ddc4cf2a2c253f1e1f76e7d719af431642108714311307b4743, states the accepted conditional theory, framework exclusions and unresolved inequalities consistently with matrix v175 d16aedf93023679b47cc3dd144db361b36ad926e1513829e88b71e77f930da72.

Method. Read all first answers, comparison rows, theory-track section and section6, plus the named historical passages. Write the standalone scope and arithmetic proof before checker. Independently compare all108 matrix rows, recompose exact sufficient maxima, scalar/graded ceilings,24 weak-probe gaps and accepted016/017 consequences. Bind both final theory audits506/507 and the frozen ledgers. No peer program or candidate integral runs.

Result. 1083 checks in 0.19550572708249092 seconds;106 physical rows represent108 logical rows,474 cited audit IDs have ledger provenance. Fresh stage 2026-10-29T18:44:11.731217+00:00 passes38 bindings17 files. Exact OPEN set4,19,27,33,34,50,69,70,103,104,107,108. T1 note67 EF1 andEF2 are accepted. Own first check used a stale affine-class expected literal; original checker/log retained and corrected. First staging stopped before checker execution because its supplement list omitted the bound checker erratum; failed stage retained, second stage passes. No mathematical comparison failed.

Verdict. CONFIRMED conditional framework statements, fixed-norm maximum, all108 candidate associations/statuses and their stated scopes, accepted016 opposite H/E2 orderings and017 partial status. REFUTED stale pending-review labels at frozen lines1290 (T4-324 accepted337) and1688 (endpoint review accepted443/452 with454/464 refinements). OPEN unrestricted largest-residual comparisons, and actual016 upper/lower slack allocation. The introductory maximum at42/106 requires fixeds/weights/estimate qualification;1683-1684 must scope the improvement factor to the selected sufficient test. Full printed016 precision at62/141/1129/2344-2348 should cite488 or502;486's original directed display is slightly weaker, though its squared input supports the later value. No bound, theorem hypothesis or candidate verdict changes. Existence,017 fullupper/E2,unregistered routes and actual distance ordering remainOPEN.

Evidence. audit record frozen_report_1837_audit, proof 86887d8f18c22aadaf00879a8616f3d4abf28633dc6e324b79d9f5df9c2a669d; result 350c1846f5510a3b83773a582ec764047dc16c0dc8b83e4c63aa8de823a28498; checker f1f9497cb158415b17ee3e9f1385ae82e70cc43f88c05d6ebd1b73eeb022b4f4; manifest 041b6c64f3ef84ac48d43350d5ac5f587f633e1c34edf19154e77c57cd708668. Exact line findings in data/findings.json. Main FINAL_AUDIT and evidence map remain frozen through505; this record is a dated addendum.

## T4-509 | 2026-10-29T18:48:38.092111+00:00 | Frozen energy-share attribution, independent N4-438 acceptance

Claim. Frozen coordinator report7fd963af..., lines226-227 and993-994, attributes the72/14/14 percentages to squared fractional sharpw. N4-438 says they belong to unregularized E_star with weights2^14,2^18.

Method. Read peer proof and inactive checker; bind all10 peer input hashes and the exact root180 previously accepted by T4-238. Write complete standalone proof first. Reconstruct every decimal-ball endpoint using exact rationals. Derive tighter share intervals by monotonicity of x/(x+y); independently compare all12 peer exact endpoints and the old180 containing intervals. Use Plancherel and the accepted fractional total upper bound to bound the actual zeroth share. No peer execution or new integral.

Result.95 checks in0.013160176109522581seconds. Fresh stage2026-10-29T18:48:12.097325+00:00 passes17 bindings16 files. The E_star P2,G1,G0 shares round to14,72,14percent. Unregularized E_w with sharpw weights has about6.36,67.67,25.98percent; these are not fractionalX shares. Actual fractional sharpw G0 share is at least0.2590588189602427 (FLOAT rendering of exact rational in result), rigorously greater than1/4. The Plancherel argument uses only the unweighted G0 term and makes no false commutation with omega.

Verdict. CONFIRMED N4-438 corrected E_star attribution, all exact saved share endpoints and actual sharpw G0 share>1/4. REFUTED both frozen squared-sharpw72/14/14 assignments. OPEN actual fractional P2/G1 shares here. Accepted total norms, thresholds and candidate verdicts do not change. Prior configured Opus5.5 analytic reviews of norm assembly remain the premises; attribution erratum is circulated through lane files for continued theory collaboration, without a remote client.

Evidence. audit record energy_share_attribution_acceptance, proof 8a80f990298155789e93ccac28e2f0390871e35226f808e781347d056c12c4f6; result323735b9140289d9eb07508a4f07be2feb0f735466e0d6f207adf1ab966d8aae; checker30bfd97c8012334151cc922f0b2da5856f9b5e284ba225b2f93ad4383a0c969c; manifesta31a216d5e93dc1cbc09f6587e19856cf4d0312f1a7cf6d17b8fe84a3522e277. Prefreeze root180 and report frozen hashes are exact inputs. Main final synthesis is immutable through505; this is a dated report erratum.

## T4-510 | 2026-10-29T18:50:31.697660+00:00 | Rounded table displays and lower-bound heading

Claim. Frozen coordinator report 7fd963af..., line 1050, calls its residual column “residual LB”. The displayed values in rows 20, 37 and 80 are lower bounds.

Method. Read N4-439's proof and both inactive checker versions. Bind its result and selected exact inputs. Write the independent proof before code. Parse d2 G0 balls and complete 016 rF rational endpoints; compare the latter byte for byte with T4-467's accepted source and its independently assembled endpoints. Check frozen row identities and exact rounding cells by integer arithmetic. No candidate integral or peer program is executed.

Result. 59 checks pass in 0.011401693802326918 seconds, followed by a fresh 13-binding, 10-file staged reproduction at 2026-10-29T18:49:54.862316+00:00. In rows 20 and 37, 4.985 < G0 < 4.99 < 4.995. In row 80, 7.14570115 < ||rF||_2 < 7.1457012 < 7.14570125. All three printed values are valid nearest summaries and strictly exceed the respective accepted upper endpoint. All twelve exact defect endpoints saved by N4-439 agree.

Verdict. CONFIRMED N4-439's heading correction and three rounded-display counterexamples. REFUTED the blanket literal lower-bound interpretation. No acceptance here of N4-439's other supplemental checks. No numerical certificate, ratio or candidate verdict changes. Explicit inequalities must remain directed; the proposed convention applies only to finite displays without an inequality or enclosing interval. Complete 017 upper bounds and unsupplied inverse conditions remain OPEN.

Evidence. audit record rounded_table_display_audit, proof 62b60bb2025cf30aac16770ddd6a7f2dd63fac4fd338b36aa22ab34e1951ebaa; result 6ba3bab79e2994191220acc1dab98952fd9ce5a618b837c0b316ce63f8cb4c63; checker 16765ffd34c835a87c9e256123223059f2729244ea2df84e7f56beefb6b32c0d; manifest 887fe7943cdd2d198a3250a549d989a59065a278a7e41d6c12ca586aa4730642. The source-integral soundness is a previously accepted premise, not inferred from hashes. The main synthesis remains frozen through T4-505.

## T4-511 | 2026-10-29T18:57:16.109846+00:00 | T1's final rerun output comparison

Claim. T1 note69 reports 69 successful rerun jobs: 51 outputs identical, 15 differing only in elapsed times or named timestamps, and three differing only in a terminal rc=0 line. No printed mathematical number, check count or verdict changes.

Method. Copy 149 files: job script, note, log, inactive peer helper/result, all 69 old/new output pairs and three side-JSON pairs. Read every changed line. Write the standalone finite proof before code. Independently parse all job and log records, compare bytes, remove only the three exact terminal lines, and mask only the inspected seconds/timestamp tokens while preserving the rest of each line. Reconstruct every changed block. Parse side decimals exactly and compare all non-seconds fields. No peer program or mathematical computation reruns.

Result. 532 checks in 0.03139854269102216 seconds; fresh stage at 2026-10-29T18:56:42.670341+00:00 passes 157 input bindings and 156 files. The bound log lists all 69 unique jobs in order with recorded rc=0. The output partition is exactly 51+3+15. One side JSON is byte-identical; the other two differ only in the top-level seconds field. Every coefficient, interval, check count, cell count and verdict in the inspected differences is unchanged.

Verdict. CONFIRMED the finite output comparison and recorded zero exits in T1 note69. OPEN independent attestation of process execution, actual wall time or affinity by this comparison; those are T1's run reports. No promotion of a diagnostic or conditional mathematical result. The 195 artifact hashes are outside this acceptance and were separately checked in506. No new quantity, candidate or existence conclusion is obtained.

Evidence. audit record theory_final_replay_comparison, proof 42b707cf27945c42eeac5b31ba911e21b5f02212b52caf96768c279370ff1206; result afa0ee0d3116a99ce56dfe1ca786663337d9c2a0c60c038e31db2810263b1f6e; checker f9caccd7f893f082490004802bfef0f966c054dc25ffd01e481bd31c8a925608; manifest c22e64917a8422b6191034bdc77f9cf543871ece9e50b33d0692dbeb3a062cf6. T1's Opus-configured final rerun is independently compared through files. The frozen main evidence through505 and immutable addenda evidence through510 remain unchanged; this later acceptance is separate.

## T4-512 | 2026-10-29T19:04:52.428396+00:00 | Frozen 19:00 joint report: changed text and section 8

Claim. The nominated report ff680b749d855f1c28dfdea1eff56455ca3ded98643838a8c26e3e8dfd57af21 applies the eight substantive repairs in T4-508 to T4-510 without changing a candidate verdict. Its new verification section must distinguish file integrity, saved-output comparison and mathematical proof.

Method. Copy the frozen report, official diff, immutable matrix180 and nomination; bind accepted proofs/results and static evidence. Read every changed block and section8. Write the standalone argument first. Independently apply all18 unified-diff hunks, reconstruct all29 sequence-comparison blocks, compare all108 rows against predecessor and matrix, recompute the fixed-estimate maximum and finite display witnesses, and compare the new labels with accepted511 and staticv06.

Result. 1433 checks in 0.06537215039134026 seconds; fresh stage at 2026-10-29T19:04:22.697456+00:00 passes39 source bindings. All108status/candidate rows agree, with the same12OPENrows. All eight repairs are applied. The selected exact optimum is unchanged. Two literal rerun errors remain: lines2521-2522 say no number changes although runtime numbers do; lines2947-2948 omit the three terminal rc=0 differences. Two label clarifications concern selected-evidence coverage and the undefined phrase approximate solution in a ball. One own checker preparation failure wrongly treated a parenthetical state131 reference in matrix row51 as a primary candidate; original code/manifest and transcribed failure are retained, and the repaired test passes.

Verdict. CONFIRMED all eight substantive repairs, candidate/status consistency, fixed-estimate maximum and static count4608. REFUTED only the two literal rerun descriptions, with exact replacement text in the proof and note297. The two label clarifications assert no mathematical counterexample. OPEN existence closure, unregistered routes, full017upper/E2 and actual016width allocation. No unchanged historical paragraph receives a new mathematical audit; no peer program or candidate integral is run.

Evidence. audit record frozen_report_1900_diff_audit, proof f325d196bdc1649694fadb48473a2ff307e34416dfeb26a7c906fa573fbf80a2; result b88ab673145b513ad0ef65fbc15cf5b3c86436e79fccbc89c31d78d852975bf0; checker 409b676cadcfdc4159f3e1c57ee8957468b40bae487978f1171d0f1ba2647a95; manifest 6c96774831ac08512e952736cdcd30ff80166c4bef3dccff4eef6f8b1077f294. The coordinator's Opus-configured report has a limited independent diff audit. Main frozen evidence remains unchanged.

## T4-513 | 2026-10-29T19:16:24.144589+00:00 | Acceptance of all four final report wording repairs

Claim. Report 12638987379f94b545751c9f96008696718861a3057b5ca02e1165a980b9502a applies T4-512 F1,F2,C1,C2 without changing a candidate classification. The new static references have the stated counts and selection.

Method. Copy the revised report and matrix182, T1 note72, N4 findings and frozen numerical audit, the static receipt v07 and map through512. Read all13 changed blocks against the previously audited frozen1900report. Write the standalone proof before the checker. Compare all108 rows and the exact output partition, receipt counts, map scope and quoted source hashes.

Result. 717 checks,23source bindings, 0.0535802161321044 seconds. Fresh stage 2026-10-29T19:16:00.986332+00:00 passes. All four repairs are applied and all106physical/108logical report rows are byte-identical to the prior report, with the same12OPEN classifications. T1 note72 accepts both literal findings and corrects its own notes69-71 by a dated interpretation. Latest static count5302 and through512 selection are exact. The N4 numerical audit identity15dec905 is repaired. One own checker line-window failure and one staging-helper missing-retained-file failure are preserved with their repairs; neither changes source content or the mathematical conclusion.

Verdict. CONFIRMED all four repairs, row preservation and the selected static references. No new claim is REFUTED. OPEN existence closure, unregistered correction routes, full017upper/E2 and actual016Hardy width allocation. No independent process-execution attestation and no acceptance of future coordinator edits.

Evidence. audit record final_report_repairs_acceptance, proof b0909989389fb8f3da9251932da2bbb1237133096e72f687d9cebf729fd0fc5c; result 5761a208b612f43061a6970fe79aeef655707a7d63cab19db5074d0ec0868aa3; checker db28b5e83738e525c46b9746975137b28bc6c9fa48fea1dc06cdf5005d8af192; manifest 3eecc874ee4679a462ed323ab0d4223cf6d0dd901111168456d9c4c7c41d70b7. Reproduction receipt maintenance/staging_513.json; retained errors in the topic CHECKER_ERRATUM_v01.md and maintenance/STAGING513_ERRATUM.md. Main frozen evidence remains unchanged.

## T4-514 | 2026-10-29T19:23:09.427970+00:00 | Final prefix-check scope and repaired report wording

Claim. T1 note75 narrows the final hash-prefix check to its selected54 tokens. The copied report v184 applies that repair at lines2543-2544. A240-character selection window does not itself establish universal citation coverage.

Method. Copy the report, T1 notes73-75, the inert selector and its saved output. Write the standalone argument before the checker. Count the54 output rows and their29/10/15 tags. Construct two texts with the same filename and token, one inside and one outside the240-character window. Check the exact source rule and repaired wording.

Result. 88 checks and12 source bindings in 0.009074001107364893 seconds. Fresh stage 2026-10-29T19:22:41.934521+00:00 passes. The repaired target is 1ee8d6afe69fd431b347d3d11a54b1b40e0c841d9ca55166296aa72d14c78bca. An initial source lookup expected the older universal phrase, but the coordinator had repaired it before the copy; that preparation transition is retained in PREPARATION_NOTE.md. No checker fails.

Verdict. CONFIRMED T1's scope clarification, the54-row partition and application of the two-line repair. REFUTED universal completeness of the window rule on arbitrary documents. OPEN actual exhaustive coverage; no omitted citation in the actual report is asserted. No mathematical theorem, candidate verdict or existence status changes. The adjacent T2 clause and other new report passages are outside this audit.

Evidence. audit record final_prefix_scope_review, proof e1f6f9b17f84457f777fd1ea9189092d157923267f4b72bfa8f726e3377171e1; result d5403481bed0b50f3d6e453fe7cce3ef71c4da396cd9130bcbf72597f4c23957; checker cd9fe9b1e198157905df4507dbae26252fed90e472d0ff399600326f8ae3767b; manifest 3714b8eb524f2b0976f819fb90598e60ff01a0240f1594a60f16f83849bedd35. No peer program executes. The Opus-configured T1 author's objection is supported by independent inspection and a finite rule counterexample.

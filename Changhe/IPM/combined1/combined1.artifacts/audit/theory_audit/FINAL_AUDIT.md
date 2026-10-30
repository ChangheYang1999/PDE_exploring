# Independent theoretical audit of the S1 / IPM case 4 program

Frozen final through T4-505, at 2026-10-29T18:30:22.821687+00:00. The report and evidence map are immutable after this time. Later final-report audits and corrections are recorded in the [dated addenda](FINAL_ADDENDA.md) and append-only [verification ledger](VERDICT_LEDGER.md). All times in the evidence files are actual recorded times.

**No candidate-framework pair has an a posteriori existence proof.** The principal positive result is a stronger conditional existence theorem. The principal negative result is an independent necessary-distance obstruction, which rules out the registered correction balls for the tested candidates. Complete residual certificates for 016 improve one norm and worsen another. They do not close the existence argument or order the unknown correction distances.

This audit distinguishes a conditional theorem from a candidate satisfying it. A failed sufficient smallness test supplies no nonexistence theorem. The exclusions below come from separately proved necessary conditions. The append-only [verification ledger](VERDICT_LEDGER.md) gives the claim, method, result, verdict and date for each audit. The [reading-order index](research/INDEX.md) links standalone proofs and their verification evidence. Earlier proposal-time OPEN headings are preserved where changing them would invalidate reviewed hashes; later acceptance entries determine their status.

## 1. What theorem is available?

The selected scalar theorem used for the quantitative comparison is FW-T-T4L2-sharpw-v1. Its full argument is in the [sharp L2 audit](audit record sharp_l2_audit, proof), with the maximal-domain construction in the [L2 closure proof](audit record l2_closure, proof). The following states its hypotheses so that the threshold can be read in context.

All functions are real on the whole plane and have S1 symmetry, even in x and odd in y. Use the canonical velocity

\[
U[h]=(-R_1R_2h,R_1^2h),\qquad
\widehat{U[h]}(\xi)=\frac{(\xi_1\xi_2,-\xi_1^2)}{|\xi|^2}\widehat h(\xi),
\]

where the Riesz transform has symbol \(i\xi_j/|\xi|\). Set

\[
J=(1-\Delta)^{1/2},\quad \omega=(1+4|X|^2)^{2/5},\quad s=1/5184,
\]
\[
\|f\|_X^2=\|\omega D^2J^sf\|_2^2
 +2^{15}\|DJ^sf\|_2^2+2^{20}\|J^sf\|_2^2.
\]

The space is the completion of compact smooth S1 functions. Derivative tensors contain all ordered Cartesian components, with Euclidean tensor norms. The contraction metric is the unweighted L2 metric.

Let \(\rho\) be a smooth S1 reference, \(u=U[\rho]\), \(V=cX+u\), and \(F=V\cdot D\rho-\rho\). Require all four groups of background hypotheses:

1. \(9/5<c<37/20\), \(a_0=\rho_y(0)>0\), and \(c+\partial_yu_2(0)=1\). The fields \(D\rho,\langle r\rangle D^2\rho,\langle r\rangle^2D^3\rho,\langle r\rangle^2D^4\rho,Du,\langle r\rangle D^2u,\langle r\rangle D^3u\) are bounded. The canonical velocity is smooth, divergence free and sublinear. For some \(\gamma<1\), \(|D^j\rho|=O(r^{\gamma-j})\), \(j=0,1,2\).
2. With
   \[
   \theta=\mathop{\rm ess\,sup}\frac{|D\rho|-\rho_y}{2},\qquad
   \kappa^2=\frac{(\log2-1/2)\|D\rho_x\|_2^2+(3\log2-2)\|D\rho_y\|_2^2}{16\pi},
   \]
   one has \(c+1-\theta-\kappa\ge2\).
3. Put
   \[
   A=\begin{pmatrix}\rho_y&-\rho_x/2\\-\rho_x/2&0\end{pmatrix},\quad
   v=\omega^2,\quad
   M_1=I-\operatorname{sym}Du+A,
   \]
   \[
   M_2=(1+c+V\cdot D\log\omega)I-2\operatorname{sym}DV+A,
   \quad S=\tfrac12(v_{xy}\rho_x-v_{xx}\rho_y-v_x\rho_{xy}+v_y\rho_{xx}).
   \]
   Require \(M_1\ge(9/10)I\), \(M_2\ge(1/2)I\), and the six supremum norms of
   \[
   (D^2\rho,\omega D^2\rho,\omega D^3\rho,\omega D^2u,
   D(vD\rho)/\omega,S)
   \]
   bounded componentwise by \((3,8,10,3,28,40)\).
4. The separate component-supremum sums for
   \[
   (|c|,Du,\omega D^2u,\omega D^3u,D\rho,
   \omega D^2\rho,\omega D^3\rho,\omega D^4\rho)
   \]
   are bounded componentwise by \((2,6,24,160,22,32,80,2048)\). These are the component sums specified in the proof, not replacements by a smaller pointwise tensor norm.

Under these hypotheses, \(F\in X\) and

\[
\|F\|_X\le \frac{4207}{20000000}=0.00021035
\]

imply exactly one stationary correction in

\[
\|h\|_X\le \frac{1351}{1000000},\qquad
c[h]:=\partial_yU_2[h](0)=0.
\]

Here stationarity means \((cX+U[\rho+h])\cdot D(\rho+h)-(\rho+h)=0\) on the whole plane, with the same c and canonical velocity as the reference.

The matrix bound at the origin implies \(a_0\ge c-11/10>7/10\); the correction preserves a positive origin slope. A prescribed leading profile in the campaign's affine chart is preserved. Uniqueness is within this normalized ball.

The high rate is at least \(1557/10000\), the low inverse bound is \(1/2\), and the contraction factor is below \(0.01372\). In particular, the proof checks a positive rate, self-mapping, contraction, and a positive origin-slope margin. It constructs compatible maximal realizations on the high space and L2. For \(A_k=L+U[k]\cdot D\), where \(L=V\cdot D-1+U[\,\cdot\,]\cdot D\rho\), the inverse is the convergent integral \(-\int_0^\infty e^{tA_k}\,dt\). The high energy estimate and the low difference estimate perform different tasks. Their combination avoids assuming a derivative-preserving nonlinear contraction in the high norm.

For these fixed sharpw parameters, optimizing the sufficient scalar parabola gives the slightly larger threshold

\[
\eta_* =\frac{40722836401}{193491763200000},\qquad
r_* =\frac{201799}{149299200}.
\]

The [independent maximum audit](audit record sharpw_maximum_review_acceptance, proof) verifies its additional rate, contraction and slope checks. This is an optimum of the specified sufficient estimate at fixed norm parameters. It is not an optimal PDE threshold or an optimum over other norms.

## 2. What improved over Analysis II?

The selected threshold divided by the Analysis II threshold \(1/1572864\) exceeds 330.8. That quotient is not a ball-enlargement factor. Analysis II uses \(s=2^{-18}\) and an additional homogeneous negative norm; sharpw uses \(s=1/5184\) without that component. The unrestricted forcing spaces are incomparable.

Removing the negative component reduces the required far-field cancellations in the exact finite sector family. Write

\[
c=\frac{4076476460239181}{2251799813685248},\quad
\gamma=1/c,\quad\delta=1-\gamma,\quad
\lambda_{\ell,q}=1-\ell\delta-2q.
\]

The leading sector \((1,0)\) cancels automatically. The L2-bottom test requires the three further sectors \((2,0),(3,0),(4,0)\) to vanish. The Analysis II negative component requires seven nonautomatic cancellations. These statements include the finite generator representation, differentiated remainder bounds and the correct index conversion. A formal sector list alone would not prove membership.

There is a same-input comparison on the [forcing-conversion domain](audit record forcing_conversion, proof): if \(Q_3=\|\omega D^3F\|_2\le10^6E_2(F)\), the conversion factor is below 2.018851, so 163.88 times the Analysis II threshold suffices for the new forcing test. This compares smallness; each theorem still needs all its own background hypotheses.

## 3. Which candidate has the strongest evidence?

Candidate 007 remains the most completely certified reference for the existing scalar theory. The audit does not establish which reference is closest to an exact solution. Comparing lower bounds for unknown distances cannot establish that ranking.

For the complete norm comparison below, use

\[
H=\|F\|_{\dot H^{-1}},\quad G_0=\|F\|_2,\quad
G_1=\|DF\|_2,\quad P_2=\|\omega D^2F\|_2,
\]
\[
E_2^2=P_2^2+2^{14}G_1^2+2^{18}G_0^2+(20/21)2^{18}H^2.
\]

| Reference | Accepted whole-plane information | Consequence |
|---|---|---|
| 007 | \(H>0.6355243760\), \(E_2<606.820219\); sharpw forcing exceeds 756.531263 | Complete forcing and necessary-distance tests fail |
| 016 | \(0.6167335007<H<0.617897369\); \(628.580088526341<E_2<628.865389\) | Smaller H than 007, but larger E2 |
| 017 | \(H>0.614419598760\); sixteen dual trials and residual enclosures for modes 1 and 3 accepted | Complete H upper, E2, and E2 ordering remain OPEN |

For 016, the actual gaps satisfy

\[
H(007)-H(016)>0.017627007636152781,\qquad
E_2(016)-E_2(007)>21.759869526341.
\]

The final [prefix63 replay](audit record candidate016_prefix63_replay_audit, proof), with its [prose-count erratum](audit/theory_audit/research_code/candidate016_prefix63_replay_audit/ERRATA_v01.md), checks all 920 groups in 32 individually integrated modes and retains a complete bound for the other 128. The earlier [reciprocal bound audit](audit record candidate016_complete_bounds_reciprocal, proof) remains valid. The [independent multimode replay](audit record candidate016_multimode_replay_audit, proof) verifies 2130 source pairing groups and the exact trial energies. Five further comparisons of the same \(X_{s,w}\) norm at identical parameter choices favor 007. The smaller \(G_0(016)\), approximately 0.3088864451425247368, therefore does not demonstrate a smaller forcing norm for these schemes.

The [Opus recomposition audit](audit record prefix63_opus_review_acceptance, proof) confirms that more than two thirds of the prefix63 squared enclosure width lies in the sixteen retained-mode enclosures. Adding Hardy modes with those inputs fixed cannot remove that portion. The identity does not determine how much comes from dual lower slack or divergence-field upper slack.

For 017, the [partial replay audit](audit record candidate017_partial_replay_audit, proof) verifies 1339 groups and 1472 exact trial coefficients. It discharges all sixteen dual lower tests and only two residual-mode tests. The other fourteen residual modes, the remaining Hardy components, and the complete \(G_0,G_1,P_2\) package remain separate premises. The earlier conditional estimate \(E_2(017)<605.9589546\) must remain conditional. A partial replay cannot establish \(E_2(017)<E_2(007)\). The [acceptance of both Opus residual reviews](audit record candidate017_residual_review_acceptance, proof) confirms the identity, cutoff argument and two modal enclosures. It corrects a missing factor of n in T2's ancillary cross-term estimate; no candidate value changes. The [revision and origin audit](audit record candidate017_review_repair_acceptance, proof) accepts T2's repaired statement and independently inspects all 2174 exact potential generators. Their smoothness and parity imply that F and each angular projection are O(r) at zero, supplying the local-integrability premise. Qn finite alone would not supply it.

## 4. Were normalization, scaling, the origin and the far field handled?

The canonical trace includes a local term:

\[
c[h]=-\frac14h_y(0)+\frac1\pi\operatorname{PV}
\int_{\mathbb R^2}\frac{\sin(3\theta)}{r^3}h(X)\,dX.
\]

Dropping the contact term changes the functional. Positive fractional regularity makes the trace continuous in the high space. The origin identity \((A_kh)_y(0)=a_0c[h]\), for normalized k, and \(F_y(0)=0\) preserve the normalization during iteration. The high ball is complete in its L2 contraction metric by weak high compactness and continuity of this trace. The [operator audit](audit record operator_audit, proof) gives the underlying distributional calculation.

The condition \(c[h]=0\) alone does not remove dilation. Under \(\rho_\lambda(X)=\lambda^{-1}\rho(\lambda X)\), the origin velocity derivative is unchanged. The nonzero scaling tangent changes the prescribed leading \(r^\gamma\) profile and lies outside the high correction space. Excluding that direction depends on the fixed far-field chart, not just the origin functional.

The exact saved 007 has the correct linear origin normalization. All five nonconstant degree-two and degree-four coefficients of \(F/y\) exceed \(2\times10^{-13}\) in magnitude, so the universal saved-Taylor tolerance was refuted. The [Taylor audit](audit record candidate007_taylor_tolerance, proof) preserves the distinction between exact normalization, these small nonzero coefficients, and a separate exact projection that removes them.

Changing c or finitely many lower tail amplitudes is also constrained by the chart. A nonzero leading profile fixes c for stationary solutions differing by L2. At fixed c and leading profile, stationarity forces the lower nonintegrable amplitudes back to the recurrence. A different leading angular profile or exponent requires a new space, normalization, realization, inverse and nonlinear estimates.

## 5. Which candidate tests fail quantitatively?

The necessary weak identity is independent of the sufficient inverse theorem. For a real \(\phi\in C_c^\infty(\mathbb R^2)\) and a distributional stationary correction \(h\in L^2\) at fixed c,

\[
|\langle F,\phi\rangle|\le D_\phi\|h\|_2+H_\phi\|h\|_2^2,
\]
\[
D_\phi=\|V\cdot D\phi+(2c+1)\phi\|_2+
\|\phi D\rho\|_2,\qquad H_\phi=\|D\phi\|_\infty.
\]

The [whole-plane weak proof](audit record pure_l2_probe_audit, proof) justifies integration by parts and the canonical vector multiplier bound. Noncompact probes require its separately checked cutoff convergence conditions. The positive quadratic root supplies a necessary correction distance. Subsequent audits use exact rational coefficients and directed ball arithmetic for the complete integrals.

For 007 the certified distance is strictly greater than 0.004769166867. Compare it with:

| Correction family | Necessary upper budget in L2 | Mismatch for 007 |
|---|---:|---:|
| Eight registered fixed-weight scalar families | 0.0000037930 | greater than 1257 |
| Original graded family, including the audited low-row extensions | \(50/(651\sqrt{28248})<0.00045717\) | greater than 10.43 |
| Audited unweighted bL scheme over all permitted component weights and certifiable positive low margins | 0.0000041069 | greater than 1161.2 |

These are upper bounds for the specified families, not sufficient targets. The coarser fraction \(25/54684\) is slightly larger than 0.00045717 and must not be equated with that decimal. The [summary-constant audit](audit record t2_final_summary_audit, proof), its [accepted summary repairs](audit record t2_summary_repair_acceptance, proof), and [weight-uniform audit](audit record weight_uniform_gram_audit, proof) give the exact scopes.

The 24 snapshots 002 through 026, excluding 011, fail the registered scalar and original graded correction tests. Candidate 001 has a stronger obstruction: its entire canonical affine L2 class contains no stationary solution for any real c, under the hypotheses of the [annular exclusion proof](audit record candidate001_affine_exclusion, proof), accepted through [both independent Opus reviews](audit record candidate001_affine_review, proof). The changed-c argument uses the leading density coefficient G0, as its erratum specifies. Candidates 011, 027 and 028 remain OPEN. This is not a nonexistence claim for all profiles with different far fields or correction spaces.

The sharpw forcing lower bound for 007 exceeds the selected sufficient threshold by more than 3,596,535.57. Even the optimized fixed-norm threshold \(\eta_*\) fails by more than 3,594,606. The failed forcing tests and the necessary-distance obstructions are logically distinct.

## 6. Is an alternative proof route available?

Several pieces are proved, but no alternative has a complete candidate closure.

The independent divergence construction gives a practical whole-field negative-norm certificate. For real S1 \(F\in L^1_{\rm loc}\) with \(rF\in L^2\), write \(F=\sum_{n\text{ odd}}f_n(r)\sin(n\theta)\), and let \(S_n\) be the contribution of mode n to \(\|rF\|_2^2\). The tangential field

\[
A_F=-e_\theta r\sum_{n\text{ odd}}\frac{f_n(r)}n\cos(n\theta)
\]

has distributional divergence F and no radial flux at the origin. Therefore

\[
H^2\le\sum_n\frac{S_n}{n^2}
\le\frac{S}{N^2}+\sum_{n<N}\left(\frac1{n^2}-\frac1{N^2}\right)S_n,
\qquad S=\|rF\|_2^2.
\]

Every coefficient of an included mode is positive. A finite prefix and a bound for the full S therefore cover every omitted frequency. Distinct solenoidal trial modes yield further reductions by orthogonal projection. Trials at one frequency require a Gram calculation or selection of one trial; their individual improvements cannot simply be added. The [general prefix theorem](audit record partial_mode_hardy_certificate, proof) and both Opus reviews are accepted in T4-481. This route enabled the complete 016 upper bound. It bounds a residual norm and supplies no inverse for the nonlinear PDE.

The registered dyadic density-velocity framework is a different weakening. Its audited inverse costs require \(s<c-1\) at the origin and a far-field rate no larger than \(1+c-ca\). Under the framework's realization, forcing-hyperplane, partition and absorption hypotheses, seven cells cover \(0<a<1+1/c\); the complementary range uses the nonpositive far-field rate. For 017 the minimum cell ratio exceeds 1.221854480167. This excludes the specified dyadic test, not every decaying-weight space. An L2 distance alone cannot exclude a space that does not dominate L2.

The tail-design route removes any prescribed finite list of nonresonant residual sectors by far-out potential cutoffs at arbitrarily small L2 cost, while preserving the interior and leading profile. Its full [finite construction](audit record finite_tail_surgery, proof) is audited. The change in residual tends to zero; the original residual does not. These constructions neither sum an infinite correction nor establish an inverse.

For the endpoint velocity route, the audited optimal universal coefficient lies between 0.7930365 and 1.747261 on its stated weighted C1 domain. The profile-specific asymptotic coefficient 0.583 still fails the retained-shape necessary test even with zero remainder. The improved coefficient 0.372 passes some necessary scalar comparisons, but the accepted finite-radius remainder is too large for the current tail list. Its radius-dependent use and universal fallback are also obstructed within the audited majorant class. The [pointwise-profile review](audit record pointwise_profile_review_acceptance, proof) and [radial review](audit record radial_average_review_acceptance, proof) record these limits. No ambient embedding argument rules out a future a priori budget derived specifically from stationarity; such a budget remains OPEN.

## 7. What is the smallest unresolved step?

For the current scalar and graded estimates, the first gate is a reference for which the certified necessary-distance tests permit the intended ball. That gate currently fails by orders of magnitude. A reference that passes it would still need complete forcing bounds, every background inequality and a compatible inverse.

The most plausible unexcluded theory changes alter the correction geometry or the leading profile. A localized signed low estimate without a new high estimate retains the existing graded ceiling. An orbit weight has its own transport and commutator costs and no certified successful high inverse. A new exponent or leading angular profile requires a new affine chart. These are substantive missing constructions, not normalization choices that can be appended to the present proof.

For 017 the missing full norm certificate is a smaller, concrete certification task, but completing it cannot remove the already certified distance obstruction. The same distinction applies to tightening 016's remaining Hardy tail.

## 8. What should the next campaign prioritize?

First, refine a reference against the full stationary equation and test it early with exact weak witnesses and origin point tests. Use both design probes and probes outside the declared objective, naming them accurately. A design probe remains a valid necessary test. Lower loss or smaller sampled pairings do not measure the true correction distance, establish a whole-plane norm, or prove that an earlier optimization span was exhausted.

Second, develop a new correction geometry only with an explicit target suggested by an actual correction: its far field, localization, angular content and derivative costs. The new proof must state the operator domain, normalization, complete tail conditions and nonlinear estimates before its numerical inverse can be used. The independent tail and weighted-velocity results above provide components for that work.

Third, refine inverse constants when the resulting budget could bridge the measured gap. The fixed-matrix floor improvements studied here have limited scope; their modest gains are not an upper bound on all possible future analytical improvements. They are insufficient for the present candidate-distance mismatch.

The latest accepted theory text is covered by [the frozen draft60 audit](audit record theory_final_draft60_audit, proof): 452 checks, all 18 changed blocks, 186 README entries, 83 candidate-row references and 78 directed factors. Both numerical wording repairs are accepted in [T4-496](audit record numerical_literal_completion, proof). These document repairs change no candidate verdict.

Collaboration used the existing T1, T2 and coordinator lanes, configured for Claude Opus 5.5, with proofs, counterexamples, corrections and reciprocal checks exchanged in files throughout the run. The provider's actual model identity is not observable from this lane. No substitute model or new remote client was used. All computation for this audit stayed local under the assigned affinity and one-worker limit; no JavaScript/TypeScript, server, cluster, GPU or Lean build was used.

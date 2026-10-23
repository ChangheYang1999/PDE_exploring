REPORT NEEDS REPAIRS

This review concerns the revised report with SHA256
`b252ead9aa8f2c3ebdc0b048a0103f8bf5e1e244f12f2c0f022725e802f9f3fe`.
The report changed during this review; findings repaired in that revision are not repeated as outstanding defects. Quotations below retain the report's wording, with line wrapping normalized. Each replacement is proposed text, not an edit to the report.

The primary nonexistence result survives this review. The main numerical table and activity-enclosure arithmetic agree with the frozen evidence. The verdict concerns remaining mathematical qualifications, incomplete numerical reporting, unsupported resource and lifecycle claims, and self-containment.

1. **Describe credited elapsed intervals consistently; do not call their ratio to 96 hours a measured compute fraction.**

   Report:

   > **Measured active numerical time: 96 hours were NOT completed.** At the snapshot the union of credited elapsed
   > training intervals lies between 0.73 and 0.91 hours. Including the independent numerical validation intervals, the
   > union over all workers lies between 0.78 and 0.96 hours. This is about 1 % of the required minimum.

   Replacement:

   **The required 96 eligible active numerical hours were not completed.** The frozen records enclose the union of credited training elapsed intervals between 0.731 and 0.911 hours, and the union including recorded validation intervals between 0.775 and 0.956 hours. These intervals include some ineligible time and omit some eligible work. They neither measure nor enclose eligible active numerical time, so their ratio to 96 hours is not a measured fraction of the required activity.

   Report:

   > About 1 % of the planned compute was used, and no refinement, free-exponent,
   >    alternative-seed, alternative-optimizer or whole-space certification step was carried out.

   Replacement:

   Eligible active numerical time was not measured exactly. The credited training-and-validation elapsed-time union is enclosed between 0.775 and 0.956 hours. No refinement, free-exponent, alternative-seed, alternative-optimizer or whole-space certification step was carried out.

   Report:

   > Active-time accounting. The task asks for the non-overlapping union of active intervals across workers. The trainer
   > did not record exact boundaries of numerical work, so the active time can only be bounded.

   Replacement:

   Activity accounting. The task asks for the non-overlapping union of eligible numerical activity across workers. The trainer did not record its exact boundaries. The following enclosures concern credited elapsed intervals, not eligible activity.

   Report:

   > | Snapshot (UTC) | Training ledger records | Training union, hours | Training and validation union, hours |

   Replacement:

   | Snapshot (UTC) | Training ledger records | Credited training elapsed-time union, hours | Credited training and recorded validation elapsed-time union, hours |

   Evidence and reason: The enclosure script reproduces 0.730806090861894 to 0.9113480567269855 hours for training and 0.7754191168450686 to 0.9559610827101601 hours after adding 78 closed validation intervals. These numbers round correctly in the report. Their interpretation is the defect. The script expressly disclaims eligible-activity certification. The approximately 1% statements divide the wrong quantity by the requested budget. The report does explicitly deny completing 96 hours; I found no literal assertion that the minimum was reached.

2. **Correct the pilot step count, or explicitly label it as a training-ledger boundary.**

   Report:

   > | pilot | first, width 64 | 0.45 | 3813 (second Adam stage) | running |

   Replacement:

   | pilot | first, width 64 | 0.45 | at least 4000 (second Adam stage; latest training-ledger boundary 3813) | running |

   Evidence and reason: The frozen training ledger ends this run at step 3813, but the same frozen checkpoint table includes the independently evaluated step-4000 checkpoint 26fd45eaf50211dd, saved at 07:25:47 UTC. Thus 3813 is not the greatest documented step under the heading “Steps reached” at the 07:32 snapshot. This does not change the selected best checkpoint at step 3000. The other execution-table step ranges agree with their ledger entries.

3. **Remove the unsupported count of physical GPUs.**

   Report:

   > Hardware: two NVIDIA A100 80 GB GPUs for training, in FP64.

   Replacement:

   Training records identify NVIDIA A100-SXM4-80GB hardware and FP64 arithmetic. The frozen records do not establish the number of physical GPUs used.

   Evidence and reason: The frozen records contain the GPU model, float64 dtype and process-local device cuda:0, but no physical GPU index, UUID or device-visibility mapping establishing two physical devices. Multiple masked processes can all report cuda:0, so the records also do not prove that only one physical GPU was used. The count “two” is unverified from the specified numerical evidence, not demonstrably false.

4. **Separate the frozen numerical snapshot from the later batch audit, and withdraw unverified final-stop wording.**

   Report:

   > Report version: final draft, 2026-10-23 07:35 UTC. Numerical snapshot: 2026-10-23 07:32 UTC (training ledger of 51
   > records, SHA256 prefix 1ed5a4c6404ab225; independent checkpoint table of 49 evaluated checkpoints, SHA256 prefix
   > e8b703c47768517460fd).

   Replacement:

   Report version: revised draft. Main numerical evidence: the frozen 2026-10-23 07:32 UTC snapshot, containing 51 training-ledger records (SHA256 prefix 1ed5a4c6404ab225) and 49 independently evaluated checkpoints (SHA256 prefix e8b703c47768517460fd). The separately identified last-batch comparison was evaluated after this snapshot and audited at 07:39:54 UTC. Its validation time is outside the frozen activity accounting.

   Report:

   > **Training versus holdout.** For one checkpoint (second representation, c_l = 0.45, saved step 4476) the final
   > training batch was reconstructed exactly by replaying the sampler; the replayed generator state matched the saved one
   > byte for byte.

   Replacement:

   **Supplementary training versus holdout comparison, after the main snapshot.** For checkpoint 2ed27e207ff9c68e (second representation, c_l = 0.45, saved step 4476), the final training batch was reconstructed by replaying the sampler; the replayed generator state matched the saved one byte for byte. This comparison was evaluated after the frozen snapshot and independently audited at 07:39:54 UTC.

   Report:

   > Training continued after the snapshot until the queue was stopped, and the ledger in the accompanying artifacts
   > records those intervals.

   Replacement:

   The frozen evidence does not establish the subsequent stop time or final activity total. This report's numerical accounting ends at the stated snapshot.

   Report:

   > The stopped fixed-exponent runs, and the two requeued second-representation runs at
   > c_l = 0.47 and 0.49, continue from their last atomic checkpoints.

   Replacement:

   On continuation, previously started fixed-exponent runs, including the two requeued second-representation runs at c_l = 0.47 and 0.49, load their saved checkpoints. Resume fidelity remains subject to the stage-transition limitation stated above.

   Evidence and reason: The supplementary evaluation was created at 07:36:59.709965 UTC, after both the stated 07:32 numerical snapshot and the stated 07:35 report version. Its numbers are supported by independent evidence and need not be discarded, but their later provenance must be explicit. The older report audit left campaign-stop confirmation open; the frozen inputs do not close it. Later live checkpoints must not silently replace the frozen 49 or be charged to the frozen hours. If the report is to certify final campaign closure, a separately identified, independently checked stop-inclusive snapshot is still needed.

5. **Say that a soft amplitude penalty discourages zero; it does not forbid it.**

   Report:

   > 3. *Does the candidate survive removal of artificial nondegeneracy constraints and refinement?* Not applicable,
   >    because no acceptable candidate was found. No additional anti-axisymmetry or nondegeneracy penalty was used. A soft
   >    sampled amplitude constraint was retained (a smooth-maximum surrogate of |U| on fixed core points, pushed toward 1),
   >    which prevents collapse to zero. The other constraints were the exact m = 2 symmetry, exact incompressibility, the
   >    envelope structure of the representation and the pressure gauge P -> 0 at infinity. No refinement series was run
   >    (section 8).

   Replacement:

   3. *Does the candidate survive removal of artificial nondegeneracy constraints and refinement?* This was not tested, and no acceptable candidate was found. No additional anti-axisymmetry penalty was used. A soft sampled amplitude penalty was retained: the 16-norm of |U| on 2048 fixed core points was pushed toward 1 with weight 1. This penalizes collapse to zero but does not exclude zero or fix the global amplitude. The representation imposes exact m = 2 symmetry, incompressibility, algebraic envelopes and the pressure gauge P -> 0 at infinity. No refinement series was run (section 8).

   Evidence and reason: The saved configuration has lambda_amp = 1, amp_p = 8, n_gauge = 2048 and lambda_nonaxi = 0. The loss uses (smooth_max_norm(U) - 1)^2. At U = 0 this is a finite penalty, not an infeasibility constraint. The revised section 4 correctly identifies the 16-norm surrogate; retain that repair. The answer should directly say “not tested,” rather than suggesting that nondegeneracy or survival under removing the penalty was established.

6. **Disambiguate the sample counts and the underlying measures.**

   Report:

   > It samples uniform physical-volume shells (256 points each), a core
   > grid, the axis and far-field spheres (96 points each).

   Replacement:

   For the selected checkpoint it samples 256 points in each uniform physical-volume shell, 1331 points on the core Cartesian grid, 129 points on the axis and 96 points on each far-field sphere. Grid and axis statistics use their diagnostic sample measures and are not three-dimensional volume norms.

   Evidence and reason: The original placement of “96 points each” can include the core grid and axis. Their recorded counts are 1331 and 129, not 96. The sphere count of 96 and shell count of 256 are correct. This is an ambiguity in the sentence, not evidence that the evaluator used the wrong counts.

7. **Supply the absolute residuals, high quantiles and sampled maxima required by section 11.**

   Report:

   > - Momentum, by physical region: relative RMS 0.0096 for R < 0.25, 0.144 for 0.25 < R < 1, 0.176 for 1 < R < 2 and
   >   0.016 to 0.031 for 2 < R < 64.
   > - Vorticity equation: worst relative RMS 0.385, on 1 < R < 2.
   > - Pressure-Poisson consistency: worst relative RMS 0.94, on 32 < R < 64.
   > - Divergence: relative RMS below 1.5 x 10^-12 in every sampled region (the curl construction makes it vanish
   >   analytically; the sampled value is roundoff).

   Replacement:

   The selected checkpoint has the following residual statistics. Here R = |y|, c = c_l, V = cy + U and Omega = curl U; C = 0 in this checkpoint. The residuals are

       R_m = (1-c)U + V·grad U + grad P,
       R_div = div U,
       R_omega = Omega + V·grad Omega - (Omega·grad)U,
       R_P = -Delta P - sum_{i,j}(partial_i U_j)(partial_j U_i).

   Relative momentum RMS divides the absolute RMS by the sum of the RMS norms of (1-c)U, cy·grad U, (U·grad)U and grad P. The vorticity denominator is the corresponding sum for Omega, V·grad Omega and (Omega·grad)U. The pressure denominator sums the RMS norms of Delta P and the displayed quadratic velocity-gradient term. Divergence is divided by the RMS Frobenius norm of grad U. No denominator is flagged as zero.

   Shell RMS values estimate averages with respect to uniform physical volume; the corresponding L2 norm is RMS times the square root of shell volume. Grid and axis rows are diagnostic sample statistics. The quantiles and maxima concern the absolute magnitude of each residual on the stated samples. They are not whole-space bounds.

   | Region or diagnostic set | Residual | Relative RMS | Absolute RMS | Absolute q99 | Absolute q99.9 | Sampled absolute maximum |
   |---|---|---:|---:|---:|---:|---:|
   | R < 0.25 | m | 0.00961815 | 0.00589663 | 0.012582 | 0.0145224 | 0.0150397 |
   | R < 0.25 | div | 1.46635e-12 | 2.61179e-12 | 5.75416e-12 | 6.77867e-12 | 6.96498e-12 |
   | R < 0.25 | omega | 0.0763155 | 0.12246 | 0.236534 | 0.265272 | 0.266078 |
   | R < 0.25 | P | 0.0134172 | 0.0702122 | 0.186937 | 0.248383 | 0.260688 |
   | 0.25 < R < 1 | m | 0.143542 | 0.0774933 | 0.449469 | 0.594119 | 0.598358 |
   | 0.25 < R < 1 | div | 5.22402e-13 | 4.92593e-13 | 1.91247e-12 | 3.1083e-12 | 3.43447e-12 |
   | 0.25 < R < 1 | omega | 0.380079 | 0.756166 | 4.63088 | 5.49896 | 5.76973 |
   | 0.25 < R < 1 | P | 0.279961 | 0.268973 | 1.4019 | 1.57665 | 1.58006 |
   | 1 < R < 2 | m | 0.176295 | 0.0367808 | 0.0395949 | 0.430838 | 0.560236 |
   | 1 < R < 2 | div | 6.05904e-13 | 1.75364e-13 | 1.04278e-12 | 1.2231e-12 | 1.23207e-12 |
   | 1 < R < 2 | omega | 0.384787 | 0.23793 | 0.31927 | 2.86997 | 3.28298 |
   | 1 < R < 2 | P | 0.699525 | 0.0919149 | 0.17014 | 1.10433 | 1.32551 |
   | 2 < R < 4 | m | 0.0273597 | 0.00168553 | 0.00525111 | 0.00653974 | 0.00689922 |
   | 2 < R < 4 | div | 7.73231e-13 | 4.23812e-14 | 1.71293e-13 | 3.37077e-13 | 3.83991e-13 |
   | 2 < R < 4 | omega | 0.0468158 | 0.00482079 | 0.0170587 | 0.0299855 | 0.0319549 |
   | 2 < R < 4 | P | 0.483733 | 0.00242527 | 0.00900502 | 0.011521 | 0.01204 |
   | 4 < R < 8 | m | 0.0306655 | 0.000736817 | 0.00180096 | 0.0019714 | 0.00200269 |
   | 4 < R < 8 | div | 4.14758e-13 | 4.48272e-15 | 1.87905e-14 | 2.84441e-14 | 2.9806e-14 |
   | 4 < R < 8 | omega | 0.0344326 | 0.000713152 | 0.00215896 | 0.00377942 | 0.00430163 |
   | 4 < R < 8 | P | 0.765288 | 0.000258362 | 0.00116491 | 0.00156867 | 0.00163503 |
   | 8 < R < 16 | m | 0.0247614 | 0.000252543 | 0.000605399 | 0.000884078 | 0.000909227 |
   | 8 < R < 16 | div | 3.29095e-13 | 7.42583e-16 | 3.15397e-15 | 5.24248e-15 | 5.46243e-15 |
   | 8 < R < 16 | omega | 0.0318724 | 0.000136912 | 0.000534714 | 0.000905287 | 0.000987437 |
   | 8 < R < 16 | P | 0.857833 | 1.75083e-05 | 6.55131e-05 | 9.84531e-05 | 0.000102305 |
   | 16 < R < 32 | m | 0.017554 | 7.52463e-05 | 0.000172319 | 0.000184454 | 0.000184794 |
   | 16 < R < 32 | div | 2.70478e-13 | 1.35782e-16 | 4.63511e-16 | 8.24099e-16 | 9.20325e-16 |
   | 16 < R < 32 | omega | 0.019877 | 1.93952e-05 | 6.30476e-05 | 8.50138e-05 | 8.51987e-05 |
   | 16 < R < 32 | P | 0.915838 | 1.11626e-06 | 4.25737e-06 | 5.9556e-06 | 6.48508e-06 |
   | 32 < R < 64 | m | 0.0159053 | 2.87395e-05 | 7.28903e-05 | 8.23994e-05 | 8.29213e-05 |
   | 32 < R < 64 | div | 2.33965e-13 | 2.2322e-17 | 7.88657e-17 | 1.15728e-16 | 1.2017e-16 |
   | 32 < R < 64 | omega | 0.0171096 | 3.11805e-06 | 1.12006e-05 | 1.37917e-05 | 1.43083e-05 |
   | 32 < R < 64 | P | 0.942304 | 5.95056e-08 | 2.71003e-07 | 3.01711e-07 | 3.05782e-07 |
   | Core Cartesian grid | m | 0.132986 | 0.050735 | 0.270405 | 0.562276 | 0.601756 |
   | Core Cartesian grid | div | 4.46661e-13 | 2.9626e-13 | 1.52827e-12 | 2.46217e-12 | 2.82729e-12 |
   | Core Cartesian grid | omega | 0.371033 | 0.517266 | 3.36996 | 5.2182 | 5.311 |
   | Core Cartesian grid | P | 0.227262 | 0.171692 | 0.821624 | 1.63974 | 1.66559 |
   | Axis sample | m | 0.010015 | 0.0018037 | 0.00710306 | 0.00742917 | 0.00744224 |
   | Axis sample | div | 8.09763e-13 | 4.61045e-13 | 2.12352e-12 | 3.51998e-12 | 3.71481e-12 |
   | Axis sample | omega | 0.0729202 | 0.0393009 | 0.136431 | 0.205458 | 0.214672 |
   | Axis sample | P | 0.0226403 | 0.0359042 | 0.176453 | 0.235882 | 0.240078 |

   The largest sampled relative momentum RMS is 0.176295 on 1 < R < 2. The largest vorticity and pressure ratios are 0.384787 on 1 < R < 2 and 0.942304 on 32 < R < 64. Relative divergence RMS is below 1.5 x 10^-12 in every sampled region. Analytically, the curl representation is divergence-free; its numerical evaluation has differentiation and floating-point error.

   Evidence and reason: The displayed relative values are correct. The omission is substantive: the task requires both absolute and relative residuals, regional RMS, high quantiles and sampled maxima. All 40 rows above come directly from the selected immutable evaluation, with six significant digits. They expose localized errors that a short list of RMS ratios conceals. For example, on 1 < R < 2 the absolute momentum RMS is 0.0367807521 but the sampled maximum is 0.5602359903. The revised attribution of the divergence defect solely to roundoff is also unjustified: the independent evaluator uses finite differences, which introduce truncation error as well.

8. **Limit the inference from coordinate agreement to the tests actually performed.**

   Report:

   > - Coordinate cross-check: Cartesian and cylindrical momentum residuals differ by RMS 2.7 x 10^-13. The failures above
   >   are therefore properties of the field, not derivative errors.

   Replacement:

   - Coordinate cross-check: Cartesian and cylindrical momentum residuals differ by RMS 2.7 x 10^-13 on the tested points. Together with the derivative-step checks, this supports the reported sampled momentum defects. It is not a certified error bound for every derivative, residual or point.

   Evidence and reason: The RMS difference is 2.709682858237202e-13 and rounds correctly. Agreement of two implementations on finitely many points does not rigorously eliminate all shared, truncation or unsampled errors, and a momentum comparison cannot by itself certify the pressure-Poisson or all other diagnostics. Numerical rejection by these large sampled defects remains well supported.

9. **Use the scalar symmetry projection for pressure.**

   Report:

   > A and P are FP64 tanh
   > networks symmetrized by F -> [F(y) + Q F(Qy)]/2, so the m = 2 symmetry is exact; no other parity is imposed.

   Replacement:

   The learned vector-potential and pressure corrections are FP64 tanh networks. Their symmetry projections are F(y) -> [F(y) + QF(Qy)]/2 for a vector output and p(y) -> [p(y) + p(Qy)]/2 for a scalar output. These enforce the stated m = 2 symmetry; no additional parity is imposed.

   Evidence and reason: Q is a 3 by 3 matrix. Multiplying the scalar pressure by Q is not a well-typed formula. The implementation and task distinguish vector equivariance from scalar invariance; the report must do so too. This is an expository error, not a finding that the saved model applies the wrong projection.

10. **Define the executed seed instead of relying on an unavailable task specification or internal seed labels.**

   Report:

   > The
   > learned corrections are added to the smooth, divergence-free, non-axisymmetric seed of the task specification. Two
   > representations were run.

   Replacement:

   The learned corrections are added to a smooth seed defined by

       M = [[a,b,0],[g,-1-a,0],[0,0,1]],
       chi(y) = (1+|y|^2)^(-1/(2c_l)),
       A_seed(y) = -(chi(y)/3) [y cross (M y)],
       U_seed = curl A_seed,
       P_seed(y) = -(chi(y)^2/2) y·[(M+M^2)y].

   The executed seed starts at (a,b,g) = (0.2,-0.4,0.7); these matrix parameters are trainable. This is an initialization, not an exact profile. Two representations were run.

   Report:

   > Executed: only seed family M1, at all six exponents (table in section 5).

   Replacement:

   Executed: only the seed family defined above, at all six exponents (table in section 5).

   Report:

   > Experiments executed up to the snapshot (seed family M1 for every run; steps are Adam steps):

   Replacement:

   Experiments executed up to the snapshot (the seed family defined in section 4 for every run; steps are Adam steps):

   Report:

   > - the seed families other than M1, and the off-axis paired-blob representation;

   Replacement:

   - the other configured seed families and the off-axis paired-blob representation;

   Report:

   > The never-started entries (a first-representation
   > run at c_l = 0.45, the second-representation seed families M3 and Z0 and the paired-blob family, all at fixed c_l
   > between 0.41 and 0.50) start from their configurations.

   Replacement:

   The never-started entries comprise a first-representation run at c_l = 0.45, two additional seed families in the second representation and the paired-blob family, all at fixed c_l between 0.41 and 0.50. They start from their saved configurations.

   Evidence and reason: The task supplies the seed formula, and the selected checkpoint metadata supplies these initial parameters and their trainability. The report did not define its seed label. The replacement uses g for the matrix entry so that it is not confused with c = c_l. No execution or successful evaluation of the other seed families is implied.

11. **Add the missing divergence-free hypothesis to the homogeneous-tail assertion.**

   Report:

   > A nonzero homogeneous leading tail of degree d in (-3/2, -1) that is smooth away from the origin cannot be
   >   irrotational.

   Replacement:

   A nonzero divergence-free homogeneous leading velocity tail of degree d in (-3/2, -1), smooth away from the origin, cannot be irrotational.

   Evidence and reason: As written, the assertion is false: grad(|y|^(d+1)) is nonzero, homogeneous of degree d, smooth away from zero and irrotational. Its divergence is (d+1)(d+2)|y|^(d-1), which is nonzero in this interval. With both divergence and curl zero, every velocity component is harmonic. A degree-d harmonic component requires the spherical eigenvalue d(d+1), which here lies strictly between 0 and 3/4, whereas the spherical eigenvalues are l(l+1) for nonnegative integers l. Thus the corrected assertion follows. Incompressibility is available in the Euler setting; it must be retained in this standalone claim.

12. **Make the physical tail limit explicitly conditional and include its angular dependence.**

   Report:

   > Such a tail gives a blowup-time
   > limit |x - x_*|^d that is locally square-integrable if and only if c_l > 2/5.

   Replacement:

   If an exact similarity solution has a nonzero leading tail U(R theta) = R^d A_infty(theta) + o(R^d), formal outer matching gives |x-x_*|^d A_infty((x-x_*)/|x-x_*|) as its blowup-time limit away from x_*. For a nonzero smooth angular coefficient, this expression is locally square-integrable near x_* if and only if c_l > 2/5. This scaling calculation does not construct a blowup solution.

   Evidence and reason: The radial power count is correct: the local energy integral is proportional to integral_0^epsilon r^(2d+2) dr and is finite exactly when d > -3/2. Also c_l - 1 - c_l d = 0, so the similarity time powers cancel. The report's scalar expression suppresses the vector angular coefficient and can sound like a constructed physical limit. In the primary interval the hypothesized nonzero exact profile is excluded by the theorem itself.

13. **Distinguish a growth hypothesis that is unverified from one that fails.**

   Report:

   > - fields that decay only along each ray, without uniformity in the direction;

   Replacement:

   - fields for which only decay along individual rays is known and uniform sublinearity U = o(|y|) has not been established; raywise decay alone does not verify the theorem's growth hypothesis;

   Evidence and reason: L2 assumes uniform sublinearity, not uniform decay. A field can fail uniform decay while still satisfying uniform sublinearity; it is then covered if it also solves the exact equations with the stated regularity. Thus nonuniform raywise decay is not itself an exclusion from L2. What fails is the implication from raywise decay alone to its growth hypothesis. The supplied scope audit correctly distinguishes these statements.

14. **Remove internal role names and the local path while preserving reproducibility in the accompanying instructions.**

   Report:

   > Its 33 symbolic checks are recorded in the lead's check log, and the independent verifier audited the
   > equations claim by claim.

   Replacement:

   The symbolic check log records 33 checks, and an independent audit examined the equations claim by claim.

   Report:

   > The lead reviewed both proofs and the reconciled written proof line by line.

   Replacement:

   Both proofs and the reconciled written proof underwent a further line-by-line review.

   Report:

   > Section 9 gives the command that resumes the numerical queue.

   Replacement:

   Section 9 describes continuation; the accompanying reproduction instructions give the literal resume command.

   Report:

   > Continuation. The numerics project's resume script (`bin/resume.sh` in the project root) restarts the supervised
   > runner on the existing queue.

   Replacement:

   Continuation. The accompanying reproduction instructions give the literal command that restarts the supervised runner on the existing queue.

   Evidence and reason: The report contains no absolute local path and no em dash, but it does contain the relative path quoted above, the internal role “lead” and undefined seed identifiers. The previous repair removes the seed identifiers. The defined theorem labels L1 and L2 are legitimate mathematical notation and need not be removed. The task still requires a literal continuation command among the deliverables; retain it in the reproduction instructions rather than in this path-free report. The revised explanation that the queue does not create larger-exponent or free-exponent experiments is correct and should be retained.

15. **State the decision to leave secondary work unfinished, rather than letting the primary obstruction stand in for it.**

   Report:

   > The campaign ends because the primary objective (a nonzero exact smooth decaying m = 2 profile with 0.4 < c_l < 0.5) is
   > excluded by an independently checked proof. Further blind search in that range cannot produce such a profile. The
   > following planned work was not performed:

   Replacement:

   The primary objective, a nonzero exact smooth globally decaying m = 2 profile with 0.4 < c_l < 0.5, is excluded by an independently checked proof. Section 13 therefore supersedes further blind search in this primary class. We choose to end this campaign at that obstruction, leaving extended calibration at c_l = 1/2 and searches above 1/2 unfinished. This decision does not resolve those secondary questions, complete the numerical deliverables or satisfy the 96-hour minimum. The following planned work was not performed:

   Evidence and reason: The primary stopping exception is justified. It is not a theorem about the secondary exponents or a substitute for recording what was left undone. The current report already lists the open work honestly; this replacement makes the scope of the stopping decision direct. No exhaustive new campaign over all c_l >= 1/2 is demanded by the task.

**Answers to the five audit questions.**

1. **Numerical agreement.** The 49 frozen checkpoint-table rows agree with their independent evaluation records at the displayed precision. All 12 best-by-representation-and-exponent selections, their saved steps, worst regions and tail values agree. The pilot's “steps reached” entry is misleading because step 4000 is already documented; the hardware count is unsupported; sample-count wording is ambiguous; and the approximately 1% activity statements interpret credited time as eligible activity. These are identified individually above. I found no additional rounded numerical discrepancy in the revised report. In particular, the former upward-rounded affine lower bound has been repaired: 0.328 is conservative for the actual minimum 0.3286623468665186. The angular comparison now correctly says absolute energy units: the difference is 3.029241746610456e-5, about 1.0418349152076463e-4 relative.

2. **Overclaiming and status.** Both status labels are justified for the scopes explicitly attached to them: a rigorous obstruction for the primary exact class, and no acceptable numerical candidate among the evaluated states. There is no strong-candidate claim and no literal assertion of 96-hour completion. Remaining overclaims concern soft penalties, the scope of finite numerical comparisons, a missing divergence-free hypothesis in one tail statement, the conditional physical limit, unverified final-stop wording and the interpretation of activity accounting. The repaired report no longer asserts unqualified nonexistence of every exact profile: zero remains exact, and constants remain possible under sublinearity without decay. Its training objective is explicitly distinguished from physical-volume validation. The newly added batch comparison uses independently recomputed residuals at fixed saved parameters, not a logged optimizer loss or amplitude-penalty value. It is appropriately limited to one training batch and a reused holdout set, but must be dated as supplementary evidence.

3. **Early stopping.** Yes for further blind numerical search in the primary exact class; no as a claim to have finished the numerical milestones or ruled out all secondary exponents. Smoothness, global decay, stationarity and the isotropic single-scale ansatz are actual target hypotheses, not assumptions inserted to exclude inconvenient candidates. The allowed constant axial recentering is a translation and creates no missing branch. The report clearly lists c_l = 1/2, larger exponents, refinement, exponent fitting, other seeds, whole-space certification, stability and finite-energy blowup construction as unresolved or unperformed. The proposed stopping sentence makes the decision about secondary work explicit. The frozen accounting establishes neither exact eligible hours nor final campaign closure.

4. **Required section 14 answers.** All six questions appear and receive direct answers. The following qualifications are necessary:

   | Required question | Assessment |
   |---|---|
   | Genuinely non-axisymmetric m = 2 candidate? | Honest “No”: substantial sampled n = 2 content does not overcome the momentum defects. |
   | Exponent resolved below 1/2? | Honest “No”: the exponents were fixed inputs, and no free refit or sensitivity/refinement study resolved an exponent. |
   | Survival after constraint removal and refinement? | Not tested. The revised answer discloses the amplitude penalty, but must say that a soft penalty only discourages zero. |
   | Worst validated region? | Correct: 47 of 49 have worst momentum RMS on 1 < R < 2; two step-75 states on 0.25 < R < 1. The selected pressure maximum is separately identified on 32 < R < 64. |
   | Credible tail? | Honest “No”; the revised report correctly identifies the 10^-2 screen as a chosen diagnostic, not a sufficient theorem or task-prescribed threshold. |
   | What prevents a stronger conclusion? | The primary theorem and its limits are stated honestly. Secondary work is incomplete. The “1% of planned compute” clause must be replaced by the credited-interval statement. |

5. **Self-containment and prose.** Not fully self-contained yet: a seed is defined only by reference to the task, residual normalizations and required statistics are missing, and the report contains internal role/seed identifiers and a relative local path. These are addressed above. The prose is generally plain, contains no em dashes and does not need a stylistic rewrite. I found no material hype. Technical notation, hashes and the locally defined theorem labels are useful provenance or mathematics, not internal review tags.

**Independent mathematical assessment.**

The theorem being used is: if 0 < c < 1/2, U and P solve

    (1-c)U + (cy+U)·grad U + grad P = 0,   div U = 0

on all of R^3 with the stated C^2 regularity and uniform U(y) = o(|y|), then U is constant and curl U = 0. Global decay forces U = 0 and P constant. This is precisely sufficient to exclude the primary nonzero target. It does not exclude the zero solution, nonzero constant sublinear solutions with linear pressure, approximate states, or the endpoint c = 1/2.

The essential proof steps check out in the supplied complete proof, including the repaired steps that are abbreviated in the report. For V = cy + U, sublinearity gives a complete flow and compact backward trapping. With kappa = 1-2c > 0,

    H = |V|^2/2 + P + c(c-1)|y|^2/2,
    grad H = -(kappa I + Omega cross)V,
    dH/ds = -kappa|V|^2.

Thus backward limit sets are compact connected equilibrium sets. Vorticity transport is Omega' = (grad U-I)Omega. If a backward limit set avoids the equilibrium set E where the largest strain eigenvalue is at least one, compactness supplies a uniform gap below one. Bounded backward vorticity then forces zero vorticity at the starting point.

At an equilibrium in E, DV has rank at least two and has expanding and contracting spectral directions. In the vortical case, DV has eigenvalue 1+c and its remaining eigenvalues have sum 2c-1 < 0; in the irrotational case the symmetric trace-free strain gives the required signs. The nontrivial issue is an uncountable equilibrium set. The repaired local-chart argument forces a nontrivial equilibrium arc if a connected backward limit set meeting E is not a singleton. At an interior arc point the transverse derivative is invertible. Taylor expansion gives sqrt(|H-h|) <= C|V|. Together with the exact dissipation identity this bounds the remaining backward path length and traps a sufficiently late return, contradicting a nonsingleton limit set. This does not require analyticity or isolated equilibria.

The adapted-norm variation-of-constants estimate puts locally backward-trapped points on a Lipschitz graph of dimension at most two, including when center directions are present. A finite cover of compact E and countably many integer-time flow images then cover the nonzero-vorticity set by null sets. That set is open, so it is empty. Harmonicity and sublinear growth force each velocity component to be constant. Constant drift C is removed by Y = y + (C/c)e_3, preserving decay and the twofold symmetry. I found no missing symmetry, stagnation-countability, finite-energy, axis-vorticity or tail-rate hypothesis in this argument.

The section 8 residual floor is also correct in its stated, restricted form: c and K must be fixed, the weighted bounds through second derivatives and a uniform continuity control on D^2U must hold, and the nonzero normalization ||D^2U||_infinity = 1 must be retained. A bound on D^3U supplies that continuity control. Local C^2 compactness plus the tail bound retains the normalization; a residual tending to zero reconstructs a limiting pressure and contradicts the exact theorem. The result is a positive but uncomputed absolute whole-space momentum-residual floor. It gives neither a 10^-3 relative screen nor a lower bound for the finite neural-network sample losses. Without amplitude normalization, epsilon W tends to the zero solution. Without uniform second-derivative continuity, ell^2 W(y/ell) preserves curvature scale while its residual is O(ell^2) and its third derivatives diverge. These limitations are material and are substantially stated correctly in the report.

This is an informal proof review, not formal verification, a novelty finding, or a general conclusion about Euler or Navier-Stokes blowup. No new defect in the central obstruction was found.

**Numerical cross-check record.**

The principal independently recomputed quantities are:

| Quantity | Evidence value |
|---|---:|
| Frozen evaluated checkpoints | 49 |
| Worst-region relative momentum RMS range | 0.14625103764046682 to 0.3331640990216087 |
| Worst momentum region counts | 47 on 1 < R < 2; 2 on 0.25 < R < 1 |
| Core ring n = 2 fraction range | 0.35433728422776156 to 0.6868158225007958 |
| Minimum core affine remainder | 0.3286623468665186 |
| Sampled core vector non-axisymmetric fraction range | 0.3731690945227845 to 0.7420810000120643 |
| Minimum n = 2 fraction of non-axisymmetric ring energy | 0.8862564994819712 |
| Minimum normalized derivative-variation fraction | 0.09846550174804382 |
| First-representation primary tail ratio range at R = 4096 | 43930.572999135264 to 2455906.2917153127 |
| First-representation control tail ratio range | 39239.31866726132 to 63779.2688913807 |
| Second-representation primary tail ratio range | 1.5417617906621848 to 83.67945514705123 |
| Second-representation control tail ratio range | 0.8048848708322304 to 0.9838866022645778 |
| Training-ledger records | 51: 38 legacy and 13 explicit-chunk records |
| Credited training elapsed-time union enclosure, hours | 0.730806090861894 to 0.9113480567269855 |
| Closed validation intervals | 78 |
| Combined elapsed-time union enclosure, hours | 0.7754191168450686 to 0.9559610827101601 |
| Sum of per-training-process credited hours, with overlap counted repeatedly | 5.654809166666666 |

For the selected checkpoint, the stated momentum, divergence, vorticity, pressure, symmetry, affine, angular, derivative-Gram, axis, coordinate, local-extremum, located-root and tail figures agree with the individual evaluation record. The selected primary minimum is step 3000 at c_l = 0.45, checkpoint f47c4600fc4e6356. Its smallest normalized derivative-Gram eigenvalue is 0.15650196139716938; its located stretching ratios round to -0.135 and 0.039; and the finite root search reports three zeros from 31 starts. None of these finite observations is a global root-count or supremum certificate.

The two early whole-space checks also agree: the finest first-representation pressure mismatch is 0.0212201188; the second-representation pressure mismatches are 0.0214861796 and 0.0197057045. Biot-Savart mismatches decrease from 0.0007276738 to 0.0000556660 and from 0.0053030889 to 0.0002786045. These are finite quadratures at three targets through radius 256, without certified exterior or quadrature errors. The report properly leaves whole-space certification open.

The supplementary batch comparison agrees to rounding: on R < 1, 0.1033323508 versus 0.2160253524, ratio 2.0905878; on 1 < R < 3, 0.07253264509 versus 0.1153139745, ratio 1.5898217. The four outer-shell holdout-to-batch ratios range from 0.94488449 to 1.04278912, consistent with “within about 6%.” Counts of 100 and 61 in the first region and saved step 4476 are correct. Its independent recomputation and explicitly limited interpretation are acceptable; its provenance postdates the main snapshot.

The reported 32 calibration tests, nine decoder tests, 17 repaired trainer tests, 33 attributed symbolic checks, tested derivative-agreement scales and approximately 0.004 stage-transition resume discrepancy are supported by the supplied audit records. I did not rerun training, model evaluation, symbolic checks or unit tests. The enclosure script was rerun read-only on the frozen inputs and reproduced both saved hours results. Historical 45-record and 22-record enclosures agree with the rounded report values. The invalid 16-record estimate is explicitly withdrawn, not asserted as valid.

The decisive frozen inputs were identified by these SHA256 values:

| Input | SHA256 |
|---|---|
| Checkpoint table | e8b703c47768517460fd15ac5c572a55b6b9ffa3970e028156cc3dd0d74a9f80 |
| Training ledger | 1ed5a4c6404ab22594f8754fc671023edda2718e8ea8f997a9e9719028d1fb65 |
| Validation ledger | 8754b4e5a109340f999cc635c44b897219f44efb58aff1b5f9ba1fae4fb098c3 |
| Theory notes | 828ff9f3df4557e605f3bbcefa5fc121a1d20bfd02443768938e755c2f64d4cd |

The newer live verifier report includes results beyond the frozen 49. I did not substitute its current best checkpoint or current totals for the specified snapshot. The theorem audits and their explicit scope restrictions were checked separately from numerical acceptance.

**Model-collaboration limitation.** A new consultation of Claude Opus 5.5 was attempted using the configured Bedrock model identifier `us.anthropic.claude-opus-5-5`. Credential retrieval failed, so no model response was received and no substitute model was used. The supplied historical audits document actual Opus 5.5 participation in the underlying proof review; that is existing evidence, not a new consultation for this review.

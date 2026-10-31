## 2026-10-29T23:42:57Z lead: V499 to V516 accepted; refit v2.3 control failed both conditions, so the refit line closes; F3 start usable and pilot (vi) running; P1 s5 excluded under 6.3 (a) (g), so P1 s4 is the candidate; four proof reviews; Phase IV priority order; no degree 8

Read before this note: numerics 23:07:29Z, 23:10:34Z, 23:25:16Z and 23:32:06Z; the P1 s5 end record; verifier 22:54:41Z to 23:39:18Z (V499 to V516); the
refit control log and record (starts/F6_control_S01_smallmove_refit.pt.json); the F3 record
(starts/F3_S01_1e-3_s1.pt.json); research/initialization/perturbation/PROOF.md; research/first_nonlinear_coefficient/PROOF.md;
research/tail_coordinates/refit/fixed_asymptotics/PROOF.md; research/initialization/perturbation/objective_recovery/PROOF.md.

1. Verdicts accepted.
   - V499 (133 admission guards), V500 (730 Cartesian checks; the legacy replay stays queued and final values OPEN),
     V501 (the F3 fault reproduced on a CPU grid, with 0 * NaN reaching the parameter slots), V502 (energy and helicity
     adapter registered, qualification pending), V503 and V505 (perturb_start_free.py repairs; v1.1 9f4c52d5... confirmed
     for the first generation).
   - V504: the four corrections are applied in the draft: 466 to 648 accepted iterations; the F2 actual start is the
     S01 coefficients after the fresh-entry projection, separate from the F-normalized start-reference record; P3 44
     and 108 iterations under nominal 3600 s allowances (3648 s and 3618 s of history; 43 and 107 within 3600 s); the
     single J_c smoke iteration (4 trials, optional save) gives an upper bound, not a typical step cost.
   - V499 asked for finite shell ratios in the actual small-move record. All 13 shell ratios in the control record are
     finite.
   - V506 and V507 (first-nonlinear and far full-pressure adapters registered; qualification pending), V508 and V509
     (items 2 and 3), V511 and V513 (corrections, items 2 and 3), V512 (lossless archive of closed shifts), V514 and V516
     (draft labels and widths) and V515 (partial claim ledger, 63 of 291 units; no clearance claimed).
   - Applied to the draft: the P1 s3 values 6.66 and 6.31 are "vorticity residual RMS", and the ball-rule changes are
     relative; F2 m1 predicted decrease 0.1355; "four latest ends" names P1 s4, P2 s4, F1 m1 and F2 m1 (two places);
     history windows are "the 50 transitions from iteration 537 to 587"; the stiff log-omega ratio is "approximately
     five to eight".

2. Refit v2.3 control (S01 refit at (0.451, 1.01)). It completed in 418 s and failed both conditions of 22:41:03Z
   item 3 (d), so "unusable" applies in the sense of 22:55:42Z item 1 (a completed check that failed).
   - Fit: rank 1397 of 1463 live columns at rcond 1e-8 (4 null columns removed), relative fit residual 7.4e-3.
   - Velocity: the per-shell relU against the source is 9.1e-4 to 2.0e-2, against 3.8e-5 to 6.0e-2 for the kept
     coefficients. The refit is closer for j >= -1 and farther on j = -4, -3, -2 (9.1e-4, 1.2e-3, 1.1e-3 against 3.8e-5,
     1.6e-4, 6.6e-4).
   - Entry objective (raw and replayed agree): refit 5.648, of which 5.617 is the gauge row and 0.0306 the rest; kept
     0.2075, of which 0.2075 is the gauge row and 3.0e-7 the rest. The fit's far-field norm is 0.9665 (kept 1.0064, not
     rescaled). At rcond 1e-6 the rest is 0.0162, still about 5e4 times the kept value.
   - Block energies relative to the source: A 2.0e7, C 4.5e9, E 8.6e6 at rcond 1e-8 (1.7e4, 2.1e5, 6.8e3 at 1e-6). The
     caps fail on A, C, D and E.
   Decision, under 22:41:03Z item 3 (f):
   - No target fit runs for F6 points 0 and 1. The control is the most favourable case (a move of 0.001 in c_l and
     0.01 in omega), and its residual at entry, without the gauge row, is about 1e5 times the kept one.
   - Pilots (iii) and (v) are dropped. Their slots go to the next breadth items. The record reads "refit initialization
     unusable with the plain least-squares refit; one regularized refit (truncated SVD at rcond 1e-8, null columns
     removed) also unusable at the small-move control". The raw refit files, the failed pilot (iii) and this control
     stay as records.
   - V508 confirms the failure independently (fresh grids; inner shells worse than KEEP; gauge costs agree), and
     V509 and V511 correct my reading, posted at 23:19Z in the report draft. Corrections accepted:
     - the condition estimate 5.0e11 is that of the untruncated live scaled matrix;
     - the claim is that this regularization, at two cutoffs, failed. It does not show that every refit fails or that
       KEEP is the right initialization in general;
     - my sentence that the refit "keeps the source decay and twist" was wrong. A finite coefficient vector in the
       target basis has the target exponent and twist by construction, and matches the source only on the sampled
       radii. The sign of the fitted far-field amplitude is not forced by the exponent difference, since it depends
       on the radii and weights. The report now uses V511's wording.
3. F3 start file (starts/F3_S01_1e-3_s1.pt, sha256 e1bc6dd2..., tool 9f4c52d5...): usable.
   - V509 checks the file independently (147 checks; the seeded vector is reconstructed bitwise). Accepted with its
     correction: 1e-3 is the size of the raw generated perturbation. The worker's entry adds the phase rotation and the
     tail projection. The entry state is 3.2e-3 from the unaligned S01 in the unweighted training norm, a distance that
     includes the phase change and is not quotiented by rotation. The entry's far-field norm squared is 1.000352 (raw
     1.000518), and the gauge-cost reduction comes from the tail projection, not from the phase.
   - 1464 coefficients touched (m != 0, E l = 1 excluded, no projection). Achieved raw relU 1.000e-3; per-shell 5.6e-5
     (j = -4) to 2.9e-3 (j = 1). m = 0, E l = 1 and parameter slots unchanged. Raw far-field norm 1.000259.
   - Entry O1, replayed: 1.551e-4, of which 1.547e-4 is the gauge row and 3.2e-7 the rest (source 2.72e-7, gauge 0). Raw
     1.677 times that, 3.356e-4 (rest 6.9e-7). The gauge row dominates, as expected for a perturbation without kernel
     projection (item 6 (a)).
   - Pilot (vi) started from it at 23:20:46Z as an ordinary FREE start (keep_coefficients, 60 iterations, 1800 s),
     labelled "F3 (offline perturbed start)". This is accepted under V505. The worker's initial cost,
     1.55058744818160969e-4, equals the record's replayed entry O1 to every printed digit. So for this file the
     replay is the worker entry, which V505 had left OPEN. After two accepted
     iterations O1 is 2.82e-7 (S01: 2.72e-7). This is objective recovery. Whether the field perturbation was removed
     is OPEN (V513) until the saved field is compared with S01 on common shells, at each state's own parameters and
     with the rotation stated. The lead will make that comparison on core 30 at the pilot end
     (tools/branch_field_rot.py, same mode set) and post it as information.
   - Then one F6 point of (viii), then (vii) F3 S01 1e-1 seed 2. At 1e-1 the gauge part of the entry O1 will be of
     order 1 (it scales with the square of the size). That is acceptable for a start and is reported with the record.

4. P1 s5. The --full end record (validation/records_63a/cont1_s5_S01_end.json) raises the 6.3 (a) exclusion (g) against
   P1_start_v10. rho_u^max is 0.034626 (start 0.045472), and the core a_max ratios are 2.2212 (centre weight, 1.23842
   against 0.55755) and 2.1196 (outer weight, 1.69152 against 0.79804). The admitted producer's recomputed decision
   agrees, and nothing is open. The wrapper answered no at 23:38:47Z, so no segment 6 is queued.
   - Under the rule registered in the report draft and restated at 22:55:42Z item 4, P1 s5 is diagnostic only: it is
     not ranked, not a candidate and not continued. P1's candidate is P1 s4 (cont1_s4_S01_end), labelled "later
     continuation excluded under 6.3 (a)". The ranking table lists P1 s5 as an excluded entry with its values: 745
     cumulative accepted iterations, O1 1.3265e-7 at (0.447703, 1.462425).
   - Open 6.3 (b) flags on the s5 record (information): radial-tail flags on blocks B, D and E, and the block C N6
     radial part at 2.33 times its start value.
   - The lineage, in segment order: core a_max ratios 0.99, 1.29, 1.50, 1.93, 2.22, while O1 fell from 2.72e-7 to
     1.33e-7 and omega rose from 1.0 to 1.46. This is the pattern the prompt warns about: the shell-relative residual
     falls while the absolute weighted core residual grows. V438 and V448 measured it independently. FIXED-CONTROL grew
     the same way (1.37), so the parameter change is not required for it.
   - Selection consequence, to be weighed at 08:30Z: a Phase III continuation of P1 s4 under the same objective is
     likely to cross (g) again within one segment. If P1 is selected, its Phase III use must say what the
     continuation tests, given this.

5. Numerics 23:25:16Z and 23:32:06Z.
   - Host-slot overrun. Five busy computations ran from 23:20:44Z to 23:27:14Z (6.5 min); the second overrun after
     22:08:46Z to 22:12:29Z. The cause and the fix are accepted: scripts/wait_slot.sh (af4606dd...) is called before
     every scripted enqueue, and manual enqueues are checked by hand. Both overruns go into the report's resource
     section with their times.
   - Pilot (vi) was paused by SIGSTOP from 23:27:14Z to 23:31:05Z, while its 1800 s wall allowance kept running. Its
     row must carry the pause (3 min 51 s), and its iteration count is not compared with the other pilots without it.
     To end an overrun, pause the computation that started last, as here. Never pause a depth segment.
   - Pilot (viii) f4_rand_k2 is accepted as a breadth record. After 34 accepted iterations O1 is 2.54e-5, rho_u^max
     0.41 and core a_max 7.7e4, with the parameters nearly unmoved. It is not a promotion candidate under the O1
     ordering, and it enters the ranking table as a breadth sample. F6 point k = 3 next, then (vii), as numerics
     proposes.
   - P2 s5 ended at its 7200 s limit: 807 cumulative accepted iterations, O1 1.0863e-7 at (0.459253, 0.323198). Its
     chain runs as registered.

6. Proof reviews, as requested.
   (a) research/initialization/perturbation/PROOF.md. I checked:
       - the scaling identity: t > 0 and the achieved size equals epsilon exactly, by linearity at the fixed pair p;
       - the invariance of the leading tail when T_p d = 0, and the closure of S under scaling;
       - the affine reduced-coordinate case (use L_p a = E_p(a) - E_p(0)) and the reading of the F3 fault as an
         evaluation at (0, 0);
       - the counterexample: the projection of (1, 0) onto ker(x + y) is (1/2, -1/2), which is not in S.
       I agree with every statement. Remark: the tool uses no projection, so T_p C changes. The gauge row depends only
       on the leading tail, and it dominates the entry objective (item 3: 1.547e-4 of 1.551e-4 at 1e-3). Each record
       should state this, which the tool already does. The recorded size 0.9999999999999979e-3 agrees with the
       identity to rounding, in the unweighted training-grid norm (w_i = 1) that was ordered.
   (b) research/first_nonlinear_coefficient/PROOF.md. I checked:
       - L against the momentum residual. With W = (c_l I - omega J) y + U, the linear part is
         (1 - c)U + c(DU)y - omega(DU)Jy + omega JU = LU. It is divergence free, so -Delta P = tr((DU)^2).
       - Identity 2 from H_lm(Q_theta' lambda Q_[-kappa log lambda] y) = lambda^l H_lm(Q_theta y), for both potentials.
         Its lambda-derivative at one gives the eigenvalue 1 - c - c gamma_j: 0 for alpha, -1 for 2 alpha + 1.
       - The pressure. The source at (r, n) is r^(-2 alpha - 2) s(Q_[kappa log r] n). The exponent is
         q_m = -2 alpha + i m kappa, with the sign of -Delta(r^q Y) as stated. The m = 0 value 2 alpha(2 alpha - 1) lies
         in (2, 6). Im q_m(q_m + 1) = m kappa(1 - 4 alpha) is nonzero.
       - The rate separation: alpha + j = beta needs j = alpha + 1 in (2, 5/2).
       - Identity 4: curl curl(Sy) = 2 grad S + (D^2 S)y - y Delta S. The radial part -Delta_S sigma and the
         tangential part grad_S[(2 - beta)sigma + kappa partial_phi sigma] at r = 1, and the vanishing cross terms.
       - Identity 5: integral of div V over the sphere = (d + 2) integral of V . n for rotating degree d =
         -(3 alpha + 1), giving 1 - 3 alpha. Also n . (F x G) = G . (n x F).
       - The auxiliary substitution: (1 - c/2) / (c/2) = 2 alpha + 1 = beta and (omega/2) / (c/2) = kappa.
       I agree with every statement. Remarks:
       - One sentence would help: the E channels start at l = 2 because the E l = 1 columns are null (they produce no
         field), so the rate statement holds whatever values those entries store.
       - The twist in the representation is (omega / (2 c)) ln(1 + r^2 / R0^2) = kappa ln(r / R0) + O(r^-2). Saying so
         would tie theta to bases/radial.py explicitly.
       - In identity 4, m is the absolute azimuthal index of the real pair.
       - The conditional full-pressure remainder, which the verifier asked me to look at. I think the hypothesis
         grad(P - P0) = O(r^-4) is the generic sharp rate. A sketch follows; it is not a proof, and the conditional
         statement stays as written until one is supplied.
         - Since div U = 0, the source is a double divergence: tr((DU)^2) = d_i d_j (U_i U_j). The decaying full-space
           pressure is P = R_i R_j (U_i U_j), with Riesz transforms.
         - Split U_i U_j = T0 + (T - T0), with T0 = U0 (x) U0 homogeneous of degree -2 alpha in (-3, -2). R_i R_j T0 is
           rotating-homogeneous of the same degree. On R^3 minus {0} it differs from P0 by a harmonic function of
           complex degree -2 alpha + i m kappa. There is none: m = 0 would need an integer degree, and m != 0 a real
           degree. So R_i R_j T0 = P0.
         - The rest, T - T0, is O(r^-2 alpha) near 0 and O(r^-(2 alpha + 1)) at infinity. At infinity the slowest
           terms are U0 times the first regular A,C correction (rate alpha + 1); U0 x U1 is O(r^-(3 alpha + 1)). Its
           zeroth moment M_ij converges: 2 alpha < 3 at 0, and 2 alpha + 1 > 3 at infinity.
         - P - P0 = d_i d_j Gamma * (T - T0). The leading exterior term is d_i d_j (M_ij / (4 pi r)) = O(r^-3), with
           gradient O(r^-4). There is no monopole or dipole term, because of the double divergence.
         - The first moment of T - T0 can diverge (it needs alpha > 3/2). Its place is taken by the
           rotating-homogeneous particular pressure of the tail, of degree -(2 alpha + 1) plus the twist. That degree
           is non-resonant, as for P0, and its gradient is O(r^-(beta + 1)).
         - The margin needed is beta < 4, which the hypotheses give. The worker's setting exterior_monopole = false
           is consistent with the vanishing monopole.
   (c) research/tail_coordinates/refit/fixed_asymptotics/PROOF.md. I checked the norm limit and exponent, the ratio
       and difference divergence, the weighted scalar minimizer a_* as a positive weighted average of
       rho_j^-(alpha_s - alpha_t), and the exponents 11/9, 549/451, 20/4059 and 1010/451. I agree with every statement,
       and with the correction of my reading (item 2). Remark: over the sampled shells, rho runs from 1/16 to 512. The
       exponent difference changes the target-to-source amplitude ratio by a factor of only 512^(20/4059) = 1.031 at the
       outer edge and 0.986 at the inner edge. The twist difference 70/4059 per unit log rho rotates by at most 0.11
       rad. So the target law does not show in the sampled domain, which supports V511's limited wording.
   (d) research/initialization/perturbation/objective_recovery/PROOF.md. Agree. The example is exact, and the
       sufficient condition with the triangle bound sqrt(2L(z)) + sqrt(2L(z0)) is right. Remark: the campaign has an
       exact instance of its own. A rotation about the z axis leaves every objective unchanged and moves the field by
       an O(1) unquotiented distance. So any field comparison must state its rotation, as item 3 does.

7. Phase IV priority order (answer to V504's capacity request). Planning counts: 50 min per all-m member (measured
   49.5 min) and 35 min per even-m member (the upper end of the earlier estimate, until the verifier measures an
   even-m primary member and replaces it). Usable window 14:30:31Z to 19:00:31Z, 270 min, of which 240 min is planned
   and 30 min kept as margin.
   Order of final sampling:
   (1) The rank-1 branch: its FREE end, then its B0 start, then its FIXED control if one exists. Reason: the
       comparison of joint against fixed optimization is a main deliverable, and it is worth more on the leading branch
       than a lower branch's B0.
   (2) The other selected branches in rank order: FREE end, then B0. A B0 shared by two branches (the S01 start of P1
       and F2) is evaluated once if the files are checkpoint-identical by sha256. Otherwise it is evaluated twice.
   (3) The remaining FIXED controls, in rank order.
   (4) Complementary diagnostics.
   - A member whose cumulative planned time passes 240 min is reported as "exact-input and origin checks only; final
     evaluation OPEN". No quadrature is lowered to fit (V504).
   - The exact list, with each member's mode class and planned minutes, goes with the 08:30Z selection. It is restated
     at the 14:30:31Z freeze with the frozen file hashes.
   - Implication for the selection (information). With four even-m candidates and P3 (all-m), the FREE ends alone
     take 4 x 35 + 50 = 190 min. Their B0s add 35 (shared S01) + 35 + 35 + 50 = 155 min. So at most three or four
     branches get a complete final evaluation with their B0, and fewer if FIXED controls are included. The selection
     will weigh this.

8. Degree 8 or higher is never run.


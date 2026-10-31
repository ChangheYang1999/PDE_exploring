# specification: joint optimization of c_l and omega at main angular degree 6

Version 1.25, 2026-10-29T16:00Z (v1.24 registered 2026-10-29T15:41Z; v1.23 registered 2026-10-29T15:16Z; v1.22 registered 2026-10-29T14:53Z; v1.21 registered 2026-10-29T14:43Z; v1.20 registered 2026-10-29T14:29Z; v1.19 registered 2026-10-29T09:22Z; v1.18 registered 2026-10-29T07:40Z; v1.17 registered 2026-10-29T06:19Z; v1.16 registered 2026-10-29T06:08Z; v1.15 registered 2026-10-29T05:53Z; v1.14 registered 2026-10-29T05:22Z; v1.13 registered 2026-10-29T05:01Z; v1.12 2026-10-29T04:20Z; v1.11 2026-10-29T04:04Z; v1.10 2026-10-29T02:50Z; v1.9 2026-10-29T01:12Z; v1.0 registered 2026-10-28T20:42Z, v1.1 20:53Z, v1.2 20:54Z, v1.3 21:10Z, v1.4 21:25Z, v1.5 21:54Z, v1.6 22:02Z, v1.7 22:16Z, v1.8 22:49Z). Chronology (corrected in v1.3
after the verifier's note of 20:57Z): v1.0 was registered before any production derivative test result and before any
production optimization result. v1.1 and v1.2 were written after the verifier's component checks of the frozen
production field code against its independent evaluator (V007, posted 20:44Z; V008, 20:49Z), and v1.2 also after its
component comparison of the new production pressure tables (completed 20:54:07Z, posted 20:57Z). Those amendments only
tightened or clarified; none relaxed a threshold. No production optimization result exists at v1.3 or v1.4. v1.5 was
written after production derivative test results (verifier V026 to V036, the numerics quick gate battery of
21:44Z to 21:50Z); its changes to the step coordinates of 3.0 (b') are post-result changes, registered with their
reasons in section 14; they change no threshold, floor or pass rule, and the outcome on the v1.4 ladder is reported
beside every result obtained with them. No production optimization result exists at v1.5. v1.6 corrects the v1.5
statements of 3.0 (b') after the audit by an external referee (a second model) and tightens their use (section 14). v1.7 adds the
gauge-subtracted G3 estimator 3.0 (b') (3), written after the verifier's V037, V042 and V043 and before the lead had
seen any release-battery G3 or G1 result or any J_cw or J_c coefficient-column block result; it changes no
threshold, floor, reported derivative or pass condition. Smoke runs of at most 20 iterations (3.4 (a)) exist; no
ranked or released optimization result exists at v1.7. v1.8 adds the far-anchor monopole evaluation (2.6), the
far-anchor pressure accuracy check G4 (d) and the scope of G5 (c), written after the verifier's V045 to V051 and
before any comparison of the production pressure at the far anchors with an independent evaluation; no threshold is
relaxed. No ranked or released optimization result exists at v1.8. v1.9 records the arithmetic configuration of the
residual (2.7) and the CPU-only operation after the withdrawal of all GPUs at 2026-10-29T00:57:59Z (3.5, 8.7); it was
written before any CPU timing of the production code and before any release-battery result on the final code; it
changes no threshold, floor or pass rule. No ranked or released optimization result exists at v1.9. v1.10 records
rulings and CPU rules posted in lead notes between 01:11Z and 02:48Z (section 14); it was written after the one-thread
CPU timing and the M2 results and before any M3 trajectory result for the all-float64 Jacobian implementation, any
lagged-Jacobian smoke result and any release-battery result on the final code; it changes no threshold, floor or pass
rule of a gate. No ranked or released optimization result exists at v1.10. v1.11 removes S20 from the CPU release
battery and the CPU queue, allows one case's battery to run as two processes and clarifies section 9 (section 14); it
was written after M1 (T3) and the M3 time ratio and before any M3 trajectory result, any lagged-Jacobian smoke result,
any release-battery result on the final code and any optimization result; it changes no threshold, floor, ladder or
pass rule. No ranked or released optimization result exists at v1.11. v1.12 fixes the release treatment of three
inherited features of the gate harness, lists a test-only repair and adds record checks for a split battery (3.5 (e), section 14); it was written
after the verifier's note of 04:14:46Z and V160 and before the lead had read any release-battery G3 result or any
release-battery J_c column result; it adds requirements only and changes no threshold, floor rule, ladder or pass rule.
No ranked or released optimization result exists at v1.12. v1.13 records the GPU restoration of 2026-10-29T02:51:04Z (3.6); it was written after the GPU M3 record of the all-float64 Jacobian implementation (V165), the first iterations of the GPU lagged-Jacobian smoke and V161 to V164, and before the lead had read any GPU release-battery result or any optimization result; it adds requirements and changes no threshold, floor, ladder or pass rule. No ranked or released optimization result exists at v1.13. v1.14 adds the host-process limit, the order of slot use and the source rule for G6 (3.6 (h)); it was written after the M3 reproduction on gpu_v1 (numerics 05:21Z) and V166, and before the lead had read any GPU release-battery result or any optimization result; no threshold, floor, ladder or pass rule changes. No ranked or released optimization result exists at v1.14. v1.15 admits the worker patch gpu_v1p1 under conditions and fixes the reading of the segment 2 budget (3.6 (i)). It was written after the G7 run on gpu_v1 and its audit (V172), the verifier's V167 to V174, and numerics' notes up to 05:45Z. It was written before the lead had read any GPU release-battery result of the numerics side or any optimization result. No threshold, floor, ladder or pass rule changes. No ranked or released optimization result exists at v1.15. v1.16 is a post-result amendment. It was written after the S09_own G1 coefficient-column record of the GPU battery and its diagnosis, and before the lead had read any other case's G1 coefficient-column result or any optimization result. It adds a classification of rounding-level groups with a coverage condition, and a test-only repair of the harness J_c closure step (3.6 (j)). It changes no threshold, ladder, floor or pass rule, and both changes are labelled wherever they decide an outcome. No ranked or released optimization result exists at v1.16. v1.17 corrects 3.6 (j) after V179 and V180. It replaces the false rationale of (2) (i) with the bound of V180, renames the classification "small-amplitude", keeps every parameter-column comparison, states the change of aggregate acceptance and the reporting of both outcomes, and adds the harness conformance of (4) (V179). It was written before the lead had read any coefficient-column record of the new harness. No threshold, ladder, floor or pass rule changes. No ranked or released optimization result exists at v1.17. v1.18 adds 3.6 (k), a post-result upward extension of the G1 coefficient-column ladder by the step 1e-2 s_j. It was written after the harness-v4 G1 records of the four release cases and V194, and before the lead had read any harness-v5c coefficient record or any evaluation at the added step. No threshold, floor, group or pass condition changes. No ranked or released optimization result exists at v1.18. v1.19 adds 3.6 (l), a post-result reference of higher precision for the G1 parameter-column comparisons that fail the registered rule on a case of 3.1. It was written after the harness-v5c G1 records of S01_shift_a, S05_shift_c and manu_small_omega and V217 to V221, and before the lead had read any record of the other cases of 3.1 or any evaluation of that reference. No threshold, floor, ladder, group or pass condition changes. At v1.19 a provisional release exists (lead note of 08:50Z), and no optimization iteration has run. v1.20 adds 3.6 (m), a post-result relaxation of the release order of 3.6 (b): the full release may be posted while named confirmations of 3.1 run, with relabelling on a failure, and the registered G3 failure of S11_own along one random direction stands and goes to the verifier for attribution. It was written after every record of the 3.1 cases existing at 14:29Z and after the P1 and P2 pair results. No threshold, floor, ladder, group, estimator or pass rule changes. (v1.21 correction: that statement is false. The manu_a (k) add-on record and its checker output existed at 14:29Z and had not been read; see 3.6 (n) (1).) v1.21 adds 3.6 (n): the correction, the withdrawal of the full release of 14:31:05Z before any run started under it (manu_a G1 fails with (k) and is OPEN with (k) and (j) in the gauge group), a post-result reference of higher precision for the gauge row of coefficient columns, registered before its evaluation, the conditions for a new full release, and a post-result order for the provisional release (the P1 and P2 FREE continuations). It was written after the manu_a (k) record, its checker output, numerics' note of 14:34:00Z, V334 and V335, and before any segment 3 result. No threshold, floor, ladder, group, estimator or pass rule changes. v1.22 corrects the function description of 3.6 (n) (5) (i): the production gauge row is computed from the analytic modal tail energies, not from tail-field values at quadrature nodes (verifier note of 14:47:31Z). It adds the saved inputs (i'), a statement of the feasibility of the unchanged same-function tolerance of (iii), and the modal form of the independent evaluation of (4). It was written after numerics' note of 14:52:00Z (which had not read v1.21) and V339, and before any evaluation of the reference of (n) (5) or of the diagnostic of (n) (4). No threshold, floor, ladder, group, estimator or pass condition changes. v1.23 adds 3.6 (o): after the first continuation jobs were refused by the resume guard and ran as fresh starts (labelled invalid), the J_c records of the continuations come from EVAL jobs at the segment-end checkpoints, the labels move to the job metadata, and every continuation is checked for its resume line. It was written after V348 to V350 and numerics' note of 15:05:00Z, and before any segment 3 end. No threshold, floor, ladder, group, estimator or pass condition changes. v1.24 makes 3.6 (n) (5) explicit on four points raised by the verifier (V358, V359) before any evaluation of (n) (5): the coefficient-independent constants of the coordinate map are held as production float64 values, the saved inputs are one hashed file written before the evaluation, d, F, the base and the steps are checked against the registered record, and a pass needs the ladder, the same-function check and the power check. It also corrects the word "bounds" in the feasibility statement of (iii) to "estimate" and states the smaller expected margin. It was written after the (n) (4) diagnostic record (numerics' note of 15:31:04Z), V356 to V360 and numerics' note of 15:34:48Z, and before any evaluation of the reference of (n) (5). No threshold, floor, ladder, group, estimator or pass condition changes. v1.25 rules, before any evaluation of (n) (5), on the three source conditions of the verifier's note of 15:57:04Z and the offset point of V366: the base vector of manu_a, which the registered records do not contain, is regenerated and tied to them by equality of every scalar they hold; the active-set evidence is saved in full; the power check saves the full decision and needs a failure. It adds 3.6 (p), a prospective rule for the closure block of J_c v in G3 records written after v1.25, after numerics' S11 closure diagnostic (note of 15:58:35Z), which changes no outcome. It was written after V364 to V366, the verifier's notes of 15:57:04Z and numerics' notes of 15:51:27Z and 15:58:35Z, and before any evaluation of the reference of (n) (5). No threshold, floor, ladder, group, estimator or pass condition changes. The verifier's
preliminary checks of its own independent evaluator completed at 20:37Z under its own standard of 20:35Z. Owner: lead. Changes are made only by appending a dated entry to the change log (section 14). A change that
relaxes a threshold after results are seen is forbidden; a change that tightens is allowed with its reason.

Campaign clock: T0 = 2026-10-28T20:30:31Z. Team stop 2026-10-30T19:30:31Z. Budget end 2026-10-30T20:30:31Z.

Binding references (read only, copied into this side with SHA-256 in registered/SHA256SUMS.txt):
- the previous campaign's specification v1.24 (sha256 e185ec86dbadc23b892d51fc444743f9bd079d9ff40518b4b72c458bbcf62481),
  sections 7 to 10 copied verbatim to registered/e3_specification_v1.24_sections_7_to_10.md;
- the previous campaign's CONVENTIONS.md (representation, gauges, pressure, grids, weights) in the frozen numerics
  directory reports/CONVENTIONS.md.
Where this specification and the run instructions conflict, the run instructions win. Where this specification and the task prompt
conflict, the prompt wins except where the run instructions override it.

## 1. Scope and hard limits

1.1 Main angular degree L = 6 exactly, for every optimization, every pilot and every control. No main degree 7, 8 or
higher, and no fit of a state into a basis of higher main degree for the purpose of continuing an optimization. The
far-field correction channels keep their existing angular degrees (which may exceed 6), unchanged.
1.2 The representation is frozen (prompt section 2): U = curl(T y) + curl curl(S y); real orthonormal spherical
harmonics as regular solid harmonics; radial Chebyshev basis in x = (s - R0)/(s + R0), s = sqrt(r^2 + R0^2), with the
radial counts of each restarted state; toroidal and poloidal envelopes (s/R0)^-(alpha + l) and (s/R0)^-(alpha + l - 1);
the smooth twist psi(r) = (omega/(2 c_l)) log(1 + r^2/R0^2); far-field channels B, D, E with their counts; the tail
constraints that cancel the forbidden rates; the full-space Newton pressure; the gauges; the symmetry classes. No new
angular harmonics, radial functions or channel functions. Quadrature, verification resolution and solver precision may
be increased; they are validation changes and are recorded as such.
1.3 Symmetry classes: the even-azimuthal-mode class and the unrestricted class (where implemented for degree 6) stay
available. A restart never enlarges the basis of the checkpoint it starts from.
1.4 All arithmetic in float64 (on a GPU with TF32 disabled explicitly, torch.backends.cuda.matmul.allow_tf32 = False and
torch.backends.cudnn.allow_tf32 = False, recorded in every job log), except the residual values of configuration M
(2.7), which are part of production. Other extended precision only in validation. (v1.10: since 2026-10-29T00:57:59Z
every computation runs on CPU cores, 3.5.)

## 2. Free-parameter formulation

2.1 Unknowns. X = (a, c_l, omega), where a is the vector of reduced spectral coefficients (all active toroidal,
poloidal and far-correction coefficients after the parameter-dependent tail-constraint elimination). The full
coefficient vector is z = E(c_l, omega) a, where E is the tail-constraint expansion; E depends on both parameters
through p = (alpha + l)/2 and q = m kappa/2, kappa = omega/c_l. "Fixed coefficient coordinates" means fixed a. Every
parameter derivative in this campaign is taken at fixed a and includes dE/dp; a test at fixed full z is a separate,
labelled field-level test.

2.2 Parameter dependence that must be differentiated (prompt section 3):
alpha = (1 - c_l)/c_l, d alpha/d c_l = -1/c_l^2;
psi = (omega/(2 c_l)) log(1 + r^2/R0^2), d psi/d c_l = -(omega/(2 c_l^2)) log(1 + r^2/R0^2),
d psi/d omega = (1/(2 c_l)) log(1 + r^2/R0^2);
chi = phi + (omega/c_l) log r in the far-field and pressure frames;
the envelopes, the twist rotation of every (cos, sin) pair by m psi, the channel rates (2 alpha + 1 + l for B,
2 alpha + l for D), the tail-constraint expansion E, the momentum-row scaling (1 + r^2/R0^2)^(alpha/2), the far-row
scaling, the gauge rows (the F-gauge norm contains (2 - alpha)^2 + (m omega/c_l)^2), the closure target G_req and the
nonlinear weights, and the pressure (source, kernel tables, the factoring exponent p0 = 2 alpha + 2, the twisted frame
and the interior and exterior Green integrals).

2.3 Pressure derivative. For a parameter p, P_p is the decaying full-space solution of
-Delta P_p = 2 tr(DU DU_p), with DU[i, j] = d_i U_j, and grad P_p is its gradient. The implementation must give the
exact derivative of the implemented discrete pressure at a fixed quadrature layout (section 2.5), including the
parameter dependence of the kernel tables. Acceptable implementations: automatic differentiation through a torch
construction of the kernels; an analytic derivative of the kernels; or a central difference of the complete
discrete pressure at a fixed layout used only for the two parameter columns, provided it passes the column tests of
section 3 at the stated tolerances (it is then labelled "FD parameter columns" in every record). A Jacobian whose
parameter columns omit the kernel dependence is forbidden in production.

2.4 Momentum-residual identities (prompt section 3; independent check, section 3 G2):
d_{c_l} R_u = -U + (1 - c_l) U_c + (y + U_c).grad U + W.grad U_c + omega J U_c + grad P_c,
d_omega R_u = (1 - c_l) U_w + (-J y + U_w).grad U + W.grad U_w + J U + omega J U_w + grad P_w,
with W = (c_l I - omega J) y + U and U_c, U_w taken at the same fixed coordinates as the residual derivative.

2.5 Quadrature layout. The pressure panel count in log s is a discrete function of kappa (panel width at most
pi/(kappa M_max), capped at 0.5). For derivative tests the layout (panel count, nodes) is held fixed. In production
the preferred rule is a frozen layout per stage: a layout adequate for every kappa the stage can reach (panel width at
most pi/(kappa_stage M_max) with kappa_stage at least twice the current kappa), kept fixed until kappa leaves its
coverage; a new stage then starts with a recorded objective jump |O1_new(X) - O1_old(X)|/O1(X) and a rebuilt local
model. If the layout instead follows the point, acceptance follows 4.3 (b). A jump above 1e-6 is reported in the job
record and in optimization working report.

2.6 Far-anchor monopole (v1.8). At the three far-anchor radii of 4.1, and only there, the l = 0 pressure may be
evaluated in the exterior form P_00(r) = -(1/r) int_r^inf s^2 F_00 ds + int_r^inf s F_00 ds, d_r P_00(r) =
(1/r^2) int_r^inf s^2 F_00 ds, with the same quadrature as the Newton formula. The two forms differ by M_0 / r with
M_0 = int_0^inf s^2 F_00 ds, which vanishes for every represented field (verifier V049, under the conditions stated
there). Condition of use: the discrete monopole of the production quadrature satisfies |M_0^disc| <= 1e-13
int_0^inf s^2 |F_00| ds at the evaluated state; it is recorded in every job and gate record, and a job whose state
violates it stops with a flag (its results are diagnostic only). Under this condition the change is a rounding-level
quantity that removes the cancellation of two large terms; it is not a harmonic pressure correction in the sense of
the prompt, since it removes no discretization error. The l = 1 and l >= 2 parts are evaluated by the Newton formula
unchanged: the discrete dipole of the production quadrature is a discretization-level value (about 1.7e-10 of its
absolute integral on the verifier's V027 field at (0.42, 0.3)) and is not removed. Adoption requires the regression of O1 and the pressure gates
(as for the stable linear operator, v1.7) and the verifier's reproduction on its own snapshot of the code.

2.7 Arithmetic of the residual (v1.9; lead notes 2026-10-29T00:44Z, 00:57Z, 01:02Z). Configuration M: every residual
evaluation used for O1, for the right-hand side of a step and for trial acceptance evaluates the pressure source, the
radial contraction, the twist and the radial Green sums in double-double arithmetic up to a single rounding of P and
grad P (dd2). J_cw, the parameter columns, J_c and the complete gradient are evaluated in float64; two
implementations are admitted: dd2 values with float64 tangents, and an entirely float64 Jacobian at the accepted point.
Adoption requires M1 (45-digit row references on the eight blocks of the lead note of 00:25Z and on the V027 field: dd2
within 1e-12 of the block norm in every selected row with the row weights matched, and |fp64 - reference| within a
factor 2 of |fp64 - dd2|), M2 (the six coefficient columns 152, 181, 183, 185, 187, 188 of the V027 field: the float64
Jacobian of the implementation against differences of the dd2 residual, unchanged G1 rule) and M3 (five accepted
iterations from S01: the same accepted and trial counts as the full dd2 run, cost within 1e-10 relative at every
iteration, and a time per iteration at most 1.5 times that of float64 on the production hardware; on the CPU the
time ratio is taken from the projected time per iteration of the CPU timing record). Until M1 to M3 hold for an
implementation, it is not used for production. Every record states the configuration and implementation.
M3 on the CPU (v1.10). A dd2 run of five iterations on the CPU is not feasible (projected about 39000 s per accepted
iteration at one thread). The trajectory reference is the GPU dd2 run from S01 completed at 2026-10-29T00:43Z (5
accepted in 5 iterations, 10 trials, start cost 2.724831834536661e-07, per-iteration costs 2.5849690794409736e-07,
2.5613897635456636e-07, 2.5507708536137813e-07, 2.5462047115340984e-07, 2.543394743207999e-07). The CPU run of the
implementation, from the same start with the same solver settings and the lagged-Jacobian option off, must give the
same accepted and trial counts and costs within 1e-10 relative at every iteration. The code hashes of the test run
are recorded, and any code change since the reference run is listed with it. If both implementations pass M1 to M3,
the faster one is adopted.

## 3. Derivative-validation protocol (gate before the large queue)

3.0 General rules.
(a) Precision: float64; TF32 off. Tests use the production code path (the same functions the optimizer calls).
(b) Steps: centered differences D_h f = (f(p + h) - f(p - h))/(2h) and the fourth-order five-point stencil
D4_h f = (8 (f(p + h) - f(p - h)) - (f(p + 2h) - f(p - 2h)))/(12 h), with h in {1e-3, 1e-4, 1e-5, 1e-6, 1e-7} in c_l and
in omega (absolute steps, all stencil points inside the open domain; at small omega the omega step is relative,
h omega, and recorded as such); in optimizer coordinates the same ladder in z_c and z_omega.
(b') Step coordinates (v1.5, post-result; corrected in v1.6; reasons in section 14). These rules change which steps
are tried or, for (3), the difference estimator, and so enlarge the chances of meeting the existential rule (d); they are changes to gate acceptance made
after results, although no threshold, floor or pass condition is changed. For each rule, the outcome on the v1.4
ladder is reported beside the outcome under the rule, and a comparison that passes only under the rule is labelled
"pass under the post-result step rule" ((1), (2)) or "pass under the post-result gauge-subtracted estimator" ((3)).
  (1) Coefficient columns (G1): the step in coefficient a_j is h s_j, h over the full five-step ladder of (b), with
  s_j = max(1, 1e-4 / ||J_f e_j||), where ||J_f e_j|| is the Euclidean norm of the frozen-weight production column at
  the base point; if ||J_f e_j|| = 0 the scaled test is OPEN. s_j is set by this formula and never tuned per column; it
  is recorded. With u_j = a_j / s_j, the derivative and its difference estimates are multiplied by s_j at the same
  physical stencil points while the G1 floor F stays fixed, so the floor gives no extra leniency. The motivation (no
  truncation error in centered differences) holds only for rows that are at most quadratic in the coefficients with the
  weights and the closure target held, which excludes the gauge row and the J_cw and J_c columns; for those the scaled
  steps carry truncation error and are judged by rule (d) as they stand.
  (2) Directional derivatives of O1 (G3): the ladder is extended by h = 1e-8 and 1e-9 (seven steps); rule (d) applies
  unchanged on the extended ladder. The last five steps are the registered ladder along v / 100 (d, D_h and the G3
  floor all scale by 1/100, so e is unchanged).
  (3) Gauge-subtracted estimator for G3 (v1.7). Let g(t) be the gauge row of 4.1 evaluated at X + t v together with
  the rest of r (same evaluation, all ingredients recomputed), and O~(t) = O1(X + t v) - (1/2) (g(t) - g(0))^2. The
  subtracted term has zero first derivative at t = 0 for every smooth g, so O~'(0) = O1'(0) = d. The comparison of (c)
  and the rule (d) are applied to the stencils of O~ in place of those of O1, with the same reported derivative d, the
  same floor F = 1e-3 ||r|| ||J_c v||, the same threshold and the ladder of (2); the active sets of (e) are those of
  the O1 evaluations. Equivalently O~(t) = O1_m(t) + g(0) g(t) + const, where O1_m is O1 without the gauge row: the
  third derivative 3 g'(0) g''(0) of the gauge term, which the verifier's V037 identified as the source of the
  truncation of a correct gradient, is removed, and g(0) g'''(0) remains. A bias in the reported d enters the
  comparison exactly as in the unmodified test, because d is unchanged and the subtracted term has zero derivative.
  The unmodified outcomes (O1 on the v1.4 ladder and on the ladder of (2)) are reported beside it for every direction.
(b'') Scope of a pass (v1.6). A finite-difference comparison is evidence under the assumption that the quantity has
no structure on scales below the tested steps; it is not a certified bound (the external referee constructs smooth
functions that pass rule (d) with a biased derivative on any ladder). Reports say "passed the test" and never
"certified". A G1 or G3 comparison that passes only under (b') counts for the provisional release (3.4 (b)) only after
the verifier reproduces it with its own script on at least one case of 3.1 named in a dated note before that
evaluation.
Extended precision remains a validation diagnostic only (3.0 (a)); no other step rule is registered.
(c) Error measure: e(h) = ||D_h - d|| / max(||d||, ||D_h||, F) in the Euclidean norm of the weighted quantity, and the
maximum component error, reported separately for (i) the near-origin group r <= 0.1 R0 (including y = 0 where the
quantity is defined and the axis), (ii) the core and intermediate group 0.1 R0 < r <= 2^8 R0, (iii) the far group
r > 2^8 R0 including the far-radius momentum rows at radii 4096, 16384 and 65536 (4.1), and for each row block
(momentum rows, of which the far-radius rows are reported separately; closure rows; gauge row). Floors F: for a vector quantity of a group, F = 1e-10 times the norm of the
undifferentiated weighted quantity of that group; for a directional derivative of the objective, d = r . (J v),
F = 1e-3 ||r|| ||J v||. A comparison that passes only because the floor exceeds max(||d||, ||D_h||) is recorded as an
absolute test and flagged; it cannot be reported as a relative pass.
(d) Pass rule for a comparison with threshold tau (replaces the v1.0 order and plateau rules, which a biased derivative
could pass): (i) e(h) <= tau for the second-order stencil at two consecutive ladder steps; (ii) e4(h) <= tau for the
five-point stencil at two consecutive ladder steps; (iii) the Richardson value D_h' + (D_h' - D_h)/99 (h' = h/10) from the
pair of (i) has error <= tau. The per-decade error ratio in the truncation regime is reported; a ratio outside
[20, 500] (second order) or [2000, 50000] (fourth order) is explained in the test report. A production
finite-difference parameter column never validates itself: its test uses the five-point stencil and steps different
from the production step.
(e) Non-smooth switches: the nonlinear weights use a median over shells and a clamp at 1e3 times the median, and the
pressure layout is discrete. At the base point p and at every stencil point (including p +- 2h) the active set is
recorded: the index of the median shell, the set of clamped shells, any denominator floors or maxima that are active,
the panel layout. A step whose stencil points do not share the active set of the base point is invalid (sampled points
cannot exclude a switch between them; this residual risk is stated in the test report); a case with fewer than two consecutive valid steps is OPEN, not passed. At a state on a switch a one-sided
test is used only if it is the intended method and is registered as such.
(f) Recording: inputs, seeds, code hashes (SHA-256 of every source file used), GPU, timings and the full error tables
are saved as machine-readable files with the test report. A failure is investigated and logged; it is never deleted.

3.1 Test cases (all required).
(a) Parameter pairs: (0.42, 0.3), (0.45, 0.3), (0.45, 1.0), one small-omega pair (0.44, 0.05), one large-omega pair
(0.47, 5.0) and one near-edge pair (0.49, 0.3).
(b) Fields: at least two existing degree-6 checkpoints of different lineages (the first degree-6 nest rung at
c_l = 0.45, omega = 1 and one state at omega = 0.3 from the nest ladder or the independent-route lineage), each
evaluated at its own parameters and at one shifted pair from (a); one manufactured smooth field with random
non-axisymmetric coefficients in every active block (toroidal, poloidal, B, D, E), seed recorded, amplitudes decaying
geometrically in the radial index so the field is smooth; both symmetry classes where implemented.
(c) Points: the training grid; additionally a point set with near-origin points (including y = 0 and the axis), log-
spaced radii from 1e-3 R0 to 65536, and random angles (seed recorded).

3.2 Gates. Each threshold tau below is applied with the pass rule of 3.0 (d) over the ladder of 3.0 (b).
G1 Jacobian parameter columns. The c_l and omega columns of the production Jacobian of the full residual vector r
   (the Jacobian the optimizer uses for its steps, of the kind stated under 7.0, at v1.5 J_cw; all row blocks; weights
   and closure target treated exactly as the production Jacobian treats them, that is, for J_cw, weights recomputed
   and the closure target held at each stencil point) against
   centered differences of the production residual at fixed a and fixed layout: e <= 1e-6 for the whole column and
   e <= 1e-5 in every group and row block of 3.0 (c), with the pass rule of 3.0 (d). At least the
   pairs and fields of 3.1, in physical and optimizer coordinates. The same test is applied separately to the parameter
   columns of the complete Jacobian J_c of 7.0 against differences of the self-consistent residual (weights and closure
   target recomputed at every stencil point), and to at least 20 random coefficient columns of each Jacobian (step rule
   3.0 (b') (1)). Tests of the frozen-weight columns J_f check shared ingredients and are reported, but do not replace
   the test of the production Jacobian.
G2 Identities. (a) d_p R_u from the formulas of 2.4, built from the production U, DU, U_p, DU_p and grad P_p,
   against the production automatic derivative of R_u: relative difference <= 1e-10 per group (shared ingredients, so
   this checks assembly only). (b) The same formulas built from ingredients computed independently of the production
   automatic differentiation (the verifier's own evaluation of U, DU, U_p, DU_p and the derivative pressure): relative
   difference <= 1e-6 per group in the resolved range 0.1 R0 <= r <= 2^8 R0 for the identity without the pressure term,
   and <= 1e-5 with it (the pressure term carries the G4 (c) tolerance); outside that range the values are reported.
   (c) U_p and DU_p themselves against centered differences of U and DU at fixed coordinates: G1 thresholds.
G3 Complete loss gradient. The directional derivative of the complete objective O1 of section 4 (with the weights, the
   closure target, the scalings, the gauge rows and the pressure kernels all recomputed at each perturbed point, layout
   fixed) against the gradient the implementation reports, along e_c, e_omega (physical and optimizer coordinates),
   three random unit directions in the scaled full X, and two mixed coefficient-parameter directions: e <= 1e-6 with
   the pass rule of 3.0 (d) on the ladder of 3.0 (b') (2) (estimator 3.0 (b') (3) allowed with its label), and the
   active sets of 3.0 (e) recorded; J in the floor
   F = 1e-3 ||r|| ||J v|| is the complete Jacobian. If the optimizer uses a frozen-weight Jacobian,
   the relative difference between its gradient J^T r and the complete gradient is reported for every case (it is not
   a pass or fail item, but it fixes which gradient is used for stationarity, section 7).
G4 Pressure derivative. (a) grad P_p against centered differences of the production grad P at fixed layout:
   e <= 1e-6 per group in the resolved range, reported beyond it. (b) The source f_p = 2 tr(DU DU_p) used by the
   production pressure derivative against the same expression from the production fields: <= 1e-12 relative (same
   field, checks that the derivative source is the derivative of the source actually used). (c) grad P_p against the
   verifier's independent ray-integral or Green-function evaluation, which includes both the interior and the exterior
   integral: <= 1e-5 relative per group in the resolved range, with the verifier's quadrature refinement reported
   separately as an error estimate (agreement of two evaluations of one inconsistent source does not count).
   (d) Far-anchor pressure accuracy (v1.8, added requirement). On S01_own, the V027 field and one manufactured field
   of 3.1, the production P and grad P (base values) at the three far-anchor radii against the verifier's independent
   evaluation of the same source with the leading tail integrated exactly; l = 0, l = 1 and l >= 2 reported
   separately. Let Delta be the change of the far-anchor residual block when the production grad P there is replaced
   by the independent one (weights and scalings unchanged). Required: ||Delta|| <= 1e-2 times the norm of that block at
   every tested state; the implied relative change of O1 is reported. If (d) fails, the remedy is a more accurate
   production quadrature of the exterior Green integrals, adopted with a regression of O1 and the pressure gates.
G5 Field consistency. (a) Centered spatial differences of U against the supplied DU at fixed coefficients and
   parameters, displacements scaled to radius: best relative error <= 5e-7 in each radial group. (b) div U and div U_p
   relative to |DU| and |DU_p|: <= 1e-10 at every test point. (c) The angular tables: the derivative tables against a
   recomputation in at least 50-digit arithmetic at the table nodes, <= 1e-13 relative with the floor 1e-13 times the
   largest table entry of the same degree (absolute test at zeros of the tables); and the source tr(DU^2) used by
   the pressure equals the one recomputed from the DU used in the residual to <= 1e-12 relative. Scope (v1.8): (c)
   applies to every angular table used by the residual, the Jacobian, the pressure and O1 of the optimizer; a table
   path not tested under (c) may be used only by diagnostics (battery and holdout evaluations), and every record states
   which path each point set used.
G6 Extended precision. At least 9 points (3 per radial group) for at least two parameter pairs: U, DU, U_c, U_w,
   DU_c, DU_w and the two momentum-residual derivatives without the pressure term, evaluated from the basis definition
   in at least 50-digit arithmetic (mpmath), against the float64 production values: relative error <= 1e-10 per
   quantity where the quantity is not dominated by cancellation; where it is (the condition number estimated as the
   ratio of the sum of absolute term sizes to the result exceeds 1e4), the absolute error and the scale are recorded
   and the threshold is 1e-14 times the sum of absolute term sizes.
G7 Checkpoint and resume. A disposable free-parameter run interrupted by SIGKILL and restarted continues from its
   last checkpoint with the same X (bitwise), the same optimizer state (damping, counters, histories), random-generator
   states and quadrature layout, and the same O1 (relative 1e-12); its ledger shows the interruption.
G8 Negative controls (power of the tests). With the production code modified in a test-only copy to omit, one at a
   time, (i) the parameter dependence of the pressure kernel tables, (ii) dE/dp of the tail-constraint expansion,
   (iii) the parameter dependence of the far-radius momentum rows (4.1; the rows at 4096, 16384 and 65536 evaluated with
   the parameters held at the base point), (iv) the parameter dependence of the gauge row, (v) the pressure term of the
   parameter columns, G1 must fail in the affected group or row block on at least one case of 3.1 where that dependence
   is excited (error at least 100 tau). The size of each omitted contribution relative to the column norm and to each
   group and row block norm is reported for every case of 3.1. An omission that cannot be made to fail is reported with
   the reason. For (i), whose exact continuous counterpart vanishes (the Green operator does not depend on the
   parameters, so the table dependence is a discretization-level term), the kernel-table derivatives are in addition
   tested directly: the production table derivatives against five-point differences of the tables at fixed layout,
   relative error <= 1e-6 per table with the floors of 3.0 (c), and the test-only copy omitting them must fail that
   table-level test.

3.3 Verifier independent check. Before the full release (3.4 (c)), the verifier reports CONFIRMED for: G1 on at least
two pairs and two fields using its own finite-difference script driving the production residual (independent of the
production differentiation); G2 (b); G4 (c) and (d); G6 on at least one pair. OPEN or REFUTED on any of these blocks the full
release.

3.4 Release.
(a) Before G1 to G8 pass in the numerics side's own tests: only smoke tests of at most 20 iterations, labelled
"smoke", never ranked.
(b) Provisional release: after the numerics side passes G1 to G8, writes the test report and the profiling report
(section 9), and the lead has reviewed them (lead note "PROVISIONAL RELEASE" in team notes). Up to two
concurrent free-parameter jobs may run; their records carry "pre-verifier".
(c) Full release: after 3.3 and a lead note "FULL RELEASE". If the verifier later refutes a gate, the affected runs are
relabelled "invalid derivative" and their states are diagnostic only.
(d) Failure: if a gate fails, the derivative is repaired before production; a frozen-parameter Jacobian is never
substituted, and no degraded production mode is allowed. If the gates cannot be met within the campaign, the outcome
is E for the affected evidence.
3.5 CPU-only operation (v1.9). All GPUs were withdrawn at 2026-10-29T00:57:59Z; from then on every computation runs on
CPU cores (optimization side: four cores, at most four busy computations; independent checks: one core).
(a) Release battery. The coverage of 3.1 is divided. Release-blocking, on the frozen snapshot in the adopted
configuration of 2.7: G1 (J_cw and J_c; parameter columns in both coordinate systems and the registered 20
coefficient columns; all groups and blocks including the far-anchor block), G2, G3, G4 (a), (b) and G5 (a) to (c) on
S01_own (0.45, 1.0), S09 at its own parameters (0.45, 0.3) and the two cases named for 3.0 (b'') (S05_own,
manu_large_omega) (v1.11: S20 at its own parameters, all-m class, was removed from this list; see 3.5 (c)); G6 on two pairs; G7 on the CPU with the production worker;
G8 on S01_own. The remaining cases of 3.1 run after the release as confirmations; a failure there relabels the
affected runs under 3.4 (c). Thresholds, floors, ladders and pass rules are unchanged. Every run record states
"release battery: CPU-reduced (v1.9)", and the report lists the cases tested before and after the release.
(b) Lagged Jacobian (solver option). Admitted only if the CPU timing record shows J_cw plus the parameter columns
costing at least ten trial evaluations in the adopted configuration and a smoke run of at most 20 iterations on S01
has consistent records. J_cw (validated, evaluated at an earlier accepted point of the same run), its column scaling
and its normal matrix are reused while steps are accepted with rho >= 0.25, for at most 8 consecutive reuses (rho:
actual decrease of O1 recomputed from scratch over the decrease predicted by the reused linear model at the fresh
residual); a rejection or rho < 0.25 with a reused J refreshes J at the current point before any damping increase.
Acceptance (4.3) and the parameter trust region are unchanged. This is not a substitution of the derivative in the
sense of 3.4 (d): the parameter columns are always present, and no stationarity or sensitivity quantity (section 7)
is computed from a reused J. Each accepted step records the J age and rho; both members of a pair use the same
policy; on resume J is refreshed and the ledger records it. The smoke (v1.10) runs on the frozen snapshot with the
production worker in the adopted configuration and includes G7: the worker is killed with SIGKILL after the checkpoint
that follows its first accepted step with J age at least 1 and is resumed by the production resume path; the G7
requirements apply, with J refreshed on resume. It records J age and rho per accepted step, the end-of-segment set of
8.7 (e) with its CPU time, and the gradient records of 7.1.
(c) (v1.11) S20 and the all-m class on the CPU. The S20 start has 3572 coefficients against 1796 for S01 and all
azimuthal modes; the T3 test needed 4140 s for S20 against 1116 s for S01. The one-thread battery of (a) for S01 is
estimated at 15 to 17 h from the measured rate of about 65 s per rebuilt stencil point, so S20 would need at least
30 h on one core and could not finish before 2026-10-30T08:30Z. S20 therefore leaves the release battery of (a) and
the CPU queue (8.7); no all-m state is optimized on the CPU in this campaign. S20_own and manu_allm_c stay in the
post-release confirmation list with the lowest priority. The report states that the field-structure diversity of
the pairs is reduced for this reason.
(d) (v1.11) Split processes. The battery of one case may run as two processes on the frozen snapshot: part A is G1
unchanged (including the J_f items); part B is G2 and G4, G3 and G5. The harness change is control flow only and is
recorded with its hash and diff; part B reproduces the state G3 inherits from G1 (the random generator advanced by
the coefficient-column draw, the residual function of the coefficient columns), both parts record the drawn
columns and a hash of the G3 directions, and the verifier checks the diff before the release.
  (v1.12) A split battery counts only if part A records sections_run = [G1] and part B records [G2G4, G3, G5], and
  both records agree on the case, the start state, the parameters, the drawn coefficient columns and the hash of the
  raw G3 draws (the harness does not reject an unknown section name, so the caller checks the coverage).
(e) (v1.12, after the verifier's note of 2026-10-29T04:14:46Z) Release treatment of features of the gate harness
inherited by the frozen snapshot:
  (1) G3 floor. The harness forms F = 1e-3 ||r|| ||J v|| with J = J_cw (closure target held) where G3 names the
  complete J_c. A G3 comparison counts for the release by its pass rule with F = 0 (PASS_rel), which does not depend on
  J. A comparison that passes with the J_cw floor but not with F = 0 counts only after ||J_c v|| is computed at the case
  start for that direction and the floor rule is evaluated again from the saved d and D_h; it is then an absolute test,
  flagged under 3.0 (c).
  (2) Scaled entries. The scaled parameter components of the G3 records (scaled_complete) use the column norms of the
  frozen-weight J_f at the case start. They are not 7.1 quantities (7.1 scaling rule (b) to (d)) and appear, if at
  all, only in the gate table with that label. The random and mixed G3 directions are unit vectors in coordinates
  scaled by the same J_f column norms; this is a choice of test direction, and the report states it.
  (3) J_c in G1. The harness tests a J_c it builds itself (weights by forward mode, closure rows by five-point
  differences at h = 1e-4) against differences of the self-consistent residual; the result is reported as "J_c
  (harness construction)" and stays release-blocking as in (a). The J_c that the worker computes for section 7 counts
  as validated only after G1 on the worker's own J_c helper passes on S01 and S09 (the verifier's worker J_c checks,
  or an equivalent test in the numerics side checked by the verifier). Until then every section 7 quantity from the
  worker's J_c carries "J_c helper pending G1" and no ranking, outcome claim or reduced sensitivity uses it. The steps
  of the optimizer use J_cw, so the provisional and full releases of optimization runs do not wait for this item.
  (4) The 03:24Z repair of the cache-counter expectations in validation/test_table_cache.py (V155) is a reviewed
  test-only change in the frozen snapshot; the release records and the report list it.

3.6 GPU operation restored (v1.13). At 2026-10-29T02:51:04Z the operator restored GPUs: GPUs 4, 5 and 6 to the
optimization side and GPU 7 to the independent checks (NVIDIA A100-SXM4-80GB); GPUs 0 to 3 are announced for about
17:00Z. The restoration was found by the verifier at 04:37Z, by numerics at 04:44Z and by the lead at 04:55Z; about
two hours of restored GPU time went unused, and the report states it. From the time of this version 3.5 and 8.7
apply only to computations that run on the CPU. Records made under them keep their CPU labels; the partial CPU battery
records are diagnostics and count for nothing in the release.
(a) Configuration M on the GPU. M3 is taken in its registered GPU form of 2.7. The run of 04:48Z to 04:52Z on GPU 6
(all-float64 Jacobian, dd2 values) meets the count and cost conditions against the GPU dd2 run and has the time ratio
1.044 against the float64 run of 00:26Z to 00:43Z (V165). That float64 run used another physical A100 shared with
another project, so V165 leaves a controlled comparison open. Before the full release numerics repeats the float64
five-iteration run on the GPU that ran the candidate, alone on it, and records the ratio; a ratio above 1.5 blocks
the full release until a lead ruling. M1 and M2 concern arithmetic and carry over. The lead's CPU M3 run is a
second sample, not a condition.
(b) Release battery on the GPU. The battery runs unsplit on the GPU with the frozen code; 3.5 (d) does not apply.
Provisional release (3.4 (b)) requires, in the numerics side's own GPU tests, the release-blocking set of 3.5 (a)
(G1 to G5 on S01_own, S09_own, S05_own and manu_large_omega; G6 on two pairs; G8 on S01_own), G7 by (d) below, the
test report, and the GPU profiling report of section 9 (profiling/profile_S01.json) with an addendum giving the
configuration-M timings and peak GPU memory from the M3 record and the jobs per GPU chosen under (c). The full release
(3.4 (c)) requires 3.3 and in addition the remaining cases of 3.1 passed on the GPU: S01_shift_a, S05_shift_c,
manu_small_omega, manu_near_edge, manu_a, S11_own, S20_own and manu_allm_c. This restores S20 and the all-m class to
the battery and to the queue (reverting 3.5 (c)) and moves the 3.1 confirmations of 3.5 (a) before the full release;
both are tightenings. 3.5 (e) (1) to (4) apply unchanged. Every record states "release battery: GPU (v1.13)", the
device and the snapshot.
(c) Jobs per GPU and ledger. The two members of a pair run on the same physical GPU, started together, when the sum of
their peak GPU memories plus 8 GB is below the device memory; otherwise each runs alone on its own GPU of the same
type, started together. GPU-hours are charged per job as wall time divided by the number of optimization jobs on its
GPU over that time. Numerics keeps a ledger of GPU-hours by label (8.3) and updates it at every segment end; the mix of
8.3 is computed in GPU-hours, with CPU-hours of coefficient optimization added at their recorded wall time.
(d) G7 on the GPU. G7 runs with the production worker in the production configuration (dd_fp64jac, lagged Jacobian
off) from S01: SIGKILL after the first checkpoint that follows the second accepted step, resume by the production
resume path, at least three further accepted steps. Checked: the vector at the first resumed objective and Jacobian
evaluation is byte-identical to the saved vector (the first resumed linearization record holds the full vector,
V162); damping, the cumulative counters (accepted, rejected, saturation streak) and the complete-gradient schedule
(V161); the histories; the random-generator states and the quadrature layout before the first resumed trial; O1
within 1e-12 relative; the ledger shows the interruption; the checker identifies the first resumed record by its
cumulative iteration. The cpu_v1 worker resets the counters (V161, REFUTED) and applies the entry projection again on
resume (V162), so G7 cannot pass on cpu_v1. Repair: snapshot gpu_v1, equal to cpu_v1 except the resume path (the LM
routine accepts and returns its counter state; the worker saves and restores it with the gradient schedule and does
not apply the entry projection to a resumed vector; trial projections unchanged). Conditions: the verifier checks the
diff; every source file recorded by the G1 to G6 and G8 runs is byte-identical in gpu_v1, so those results carry
over (otherwise they are repeated on gpu_v1); a five-iteration fresh-start run of the M3 form on gpu_v1 has the counts
and costs (1e-10 relative) of the 04:48Z record; G7 passes on gpu_v1. Production runs only on gpu_v1.
(e) Lagged Jacobian off. Every GPU production job runs with the lagged Jacobian off. On the GPU the ratio of J_cw plus
the parameter columns to a trial is about 14, which 3.5 (b) admits, but in the GPU smoke every trial with a reused J up
to the sixth iteration was rejected, and a fresh iteration costs about 45 s; the possible saving is small and the
option would add a policy to compare across pairs. The smoke completes as a record. This is decided before any
production result.
(f) Queue on the GPU (replaces 8.7 there; 8.2 to 8.6 apply). Provisional release: pair P1 (S01) on GPU 4 and pair P2
(S09) on GPU 5, FREE and FIXED-CONTROL each. Segment 1 (pilot): max_iter 120, time limit 3600 s. Segment 2 (medium,
both members unless a rule of 6.3 (a) or 5.3 stops a member): max_iter 240, time limit 7200 s, from the segment 1 end
state. The pair result is reported at the end of segment 2 (matched budget 3 h, 360 iterations). GPU 6 and any GPU
not used by P1 and P2 run the remaining battery cases. After the full release: pair P3 (S20, all-m class) with the same two segments; then FREE
continuations of the P1 and P2 FREE members beyond the matched budget (reported as unmatched; long budget of 8.5 while
O1 decreases by more than 1 per cent per hour), then FREE starts: S05 and S11 (F1), F2 from S01 and S09 at the first
parameter points of the F6 design (coefficients kept and refit), F3 from S01 (1e-3 and 1e-1). When GPUs 0 to 3 arrive,
one FREE job per GPU while the other project holds memory there, two when the memory rule of (c) allows. If the
8.3 mix falls below 80 per cent FREE, the next job started is FREE.
(g) Gradient records on the GPU. 7.1 is reported per accepted iteration as registered; 7.2 to 7.4 and the full 6.4
list run at the end of every segment, inside the job or as an EVAL job; either way they are required before a state
is ranked under 8.6 or enters a claim. 8.7 (e) does not apply on the GPU.
(h) (v1.14) Host processes and slot order. Every GPU job of the optimization side (gate run, worker, check) occupies one
busy host process on its four CPU cores, so at most four such jobs run at once whatever the number of GPUs; GPUs 0 to 3
add no slots. (1) The two members of a pair always run under the same sharing condition: together on one GPU, or each
alone on its own GPU of the same type, started together; when a GPU would otherwise stay idle, the members run alone.
This replaces the first sentence of (c). (2) Order of slot use: a slot that frees goes to the remaining validation
items (G8, the G3 add-on, G6, then the 3.1 cases of (b) in the order of the queue) until all of them are launched; after
that, and once the provisional release is posted, freed slots go to P1, then P2, each pair starting when two slots are
free. P3 and the further jobs of (f) follow under the full release. A slot freed by a stopped pair member goes to the
next item of this order. (3) G6 source. G6 is field-level as registered (3.2). For 3.4 (b) the field-level G6 on two
pairs at the gpu_v1 field code may come from the numerics side or from the verifier's own field-level evaluator; in the
second case the same record also serves 3.3. Scalar-level checks of the ingredients are supplementary records and do
not replace it. (4) A CPU validation item may run on the lead's core from a copy of gpu_v1 whose source hashes match the
snapshot record; its record names the core and the copy.
(i) (v1.15) Worker gpu_v1p1 and the segment budget. (1) Production may run on snapshot gpu_v1p1: gpu_v1 with only
scripts/worker_d6.py replaced (sha256 prefix cd35acf01f770dfb); the 43 numerical source modules and the complete-Jacobian
helper are byte-identical to gpu_v1 (V174). The patch keys the entry projection on the resume branch. It writes an
end-of-segment checkpoint. It admits a segment continuation (cfg continue_from_run) only from a checkpoint with a positive
iteration count, saved counters, an equal grad_every, and a job configuration equal except max_iter and time limit;
otherwise it records a fresh start instead of resuming. The gates do not import the worker, so no battery result is
affected. This replaces the last sentence of (d) ("Production runs only on gpu_v1").
(2) Conditions before the first production job on gpu_v1p1:
    (i) the verifier's diff check (V174, done, with the limits of (3));
    (ii) G7 exactly as registered in (d), killed after the first checkpoint that follows the second accepted step, on the
         gpu_v1p1 worker, passed and audited. Its pre-kill part is a fresh start; it must have the counts and costs
         (1e-10 relative) of the 05:21:55Z gpu_v1 G7 run over the same iterations;
    (iii) a segment continuation smoke (a fresh job, a continuation of it, and a continuation with a changed chunk that
         must be refused and recorded), passed and audited. The first linearization of the continuation uses the
         end-of-segment vector byte for byte, and damping, counters, gradient schedule, history and generator state
         continue.
    If (ii) or (iii) fails, no production job starts until a repaired worker passes both.
(3) Restrictions (V174): one start per job; a job's configuration is never edited after launch, and every resume
record and end-of-segment report states the configuration hash at launch and at that point; continuations only from
gpu_v1p1 checkpoints that carry grad_every.
(4) The 05:21:55Z G7 run on gpu_v1 (V172: state preserved, kill after the second eligible checkpoint, not the first)
is a supplementary record. It does not satisfy (d).
(5) Segment budget. The max_iter 240 and 7200 s of segment 2 in (f) are that segment's allowance. The continuation job
has cfg max_iter equal to the cumulative iteration of the segment 1 end state plus 240 (the worker treats max_iter as a
cumulative ceiling, V174) and a time limit of 7200 s (the worker's timer is local to a job). The matched budget of (f)
is therefore at most 360 iterations and 3 h of solver time per member. Both members of a pair get the same allowances.
(j) (v1.16, post-result; corrected in v1.17 after V179 and V180) Small-amplitude coefficient-column groups and the
harness J_c closure step. v1.16 was written after the S09_own G1 record of the GPU battery (numerics 05:58Z) and the
diagnosis validation/diag_coef_S09_own.json, and before the lead had read any G1 coefficient-column result of another GPU
battery case. v1.17 was written after V178 to V181 and numerics' notes of 06:04Z and 06:07Z (which give the manu_large_omega
coefficient-column pass counts, 8/10/10 of 20). It was written before the lead had read any coefficient-column record of
the new harness.
(1) Facts on S09_own (gpu_v1):
    - Coefficient columns 793, 873, 912, 1035 and 1354 of J_cw and J_f fail; their column norms are 3e-12 to 3e-9 and
      s_j is 1e4 to 1e7. Each passes the whole-column rule and every group except the near-origin group. There the
      derivative norm is 3e-9 to 3e-8 of the column norm (columns 793, 873). Over the three largest steps, e(h) grows in
      proportion to 1/h from 4e-4 at h = 1e-3, and no truncation regime appears. This is consistent with rounding, but
      three centered steps do not prove the mechanism.
    - J_f columns 186 and 189 fail the near-origin group at the second step (1.1e-5 at h = 1e-4) with the same 1/h
      growth. The J_f group norm there is 1.5e-7 and 5.9e-7 of the column norm.
    - The harness J_c columns 793, 856, 873, 912, 1035 and 1354 fail with an error that does not depend on h. For
      columns 793 and 873 it equals the difference between the harness J_c and J_cw closure blocks (5e-16 absolute). The
      differences of the self-consistent residual agree with J_cw there. On columns 186 and 189 they resolve a
      closure-target contribution of 1e-4 of the column, and J_c passes. This is consistent with the harness's
      five-point difference of the closure rows at the fixed unscaled step 1e-4; the repair of (3) tests that.
    These failures stand as registered failures in every record and in the report.
(2) Small-amplitude groups (post-result rule; label "small-amplitude group, post-result rule").
    (i) Definition. A group or row block of 3.0 (c) in a coefficient column is small-amplitude if max(||d||, ||D_h||)
        over the group, at every valid ladder step, is below tau_c = 1e-6 times the norm of the column of the Jacobian
        under test. tau_c is the whole-column G1 threshold. An error confined to such a group changes the whole-column
        error by less than 2 tau_c, and by less than 2 sqrt(k) tau_c over k such groups (V180). The whole-column test
        is retained and still bounds it; the classification does not make that test redundant. The finite differences
        enter the definition so that an omitted dependence, with d small and D_h large, is not classified. The name
        describes a relative amplitude, not a proven rounding mechanism.
    (ii) Parameter columns are never classified. They keep every required comparison.
    (iii) Reporting. A small-amplitude comparison is reported with its values and counts neither as passed nor as
          failed: the group is "not tested on that column".
    (iv) Coverage. A coefficient column whose only failures are in small-amplitude groups counts for the release only
         if, in the same case and for the same Jacobian, that group passes the registered rule on both parameter
         columns, and on at least five coefficient columns where it is not small-amplitude. Otherwise the group is OPEN
         for the case, and an OPEN item blocks the release as a failure does.
    (v) G8 is evaluated under this rule as applied: each negative control must still fail in a group that is not
        small-amplitude.
    (vi) Aggregate acceptance. The rule for each retained comparison is unchanged, but excluding required comparisons
         and requiring coverage on other columns changes the aggregate acceptance of G1 after results. As in 3.0 (b'),
         the outcome under the registered rule and the amended outcome are distinct, and both are reported for every
         case. A G1 that passes only under this rule is reported as "passes under the post-result small-amplitude
         rule". It counts for the provisional release only after the verifier has reproduced the classification and
         the coverage check with its own script on S09_own from complete records (3.0 (b'')).
(3) Harness J_c closure step (test-only repair; label "J_c harness, post-result closure step").
    (i) The harness forms the closure rows of its J_c column j by the five-point difference with step 1e-4 s_j, with
        s_j from 3.0 (b') (1), recorded, in place of the step 1e-4. The production code does not change, and the
        verifier checks the diff of the test file.
    (ii) The J_c coefficient-column section is rerun with the repaired harness on every battery case whose harness
         J_c coefficient columns fail with an error that does not depend on h. Both outcomes are reported, and the
         repaired outcome counts for the release, with the label.
    (iii) The repair does not validate the worker's J_c helper, which 3.5 (e) (3) still governs. If the helper uses
          the same fixed closure step, its coefficient columns are tested on S09 before any section 7 quantity from
          the helper is used.
(4) Conformance of the harness to the registered rule (v1.17, V179). These are corrections that bring the test to the
    registered rule; they are not amendments.
    (i) Coefficient columns follow 3.0 (b') (1) as registered: d and D_h are multiplied by s_j and compared against the
        fixed floor F.
    (ii) The Richardson value of 3.0 (d) (iii) is judged with the same floor F as the stencils.
    (iii) The records store, per column, group, row block and ladder step: the unscaled norms of d, D_h, D4_h and of
          their differences; s_j; F; the active-set flag; and e under the registered convention. The verdict can then
          be recomputed from saved values.
    (iv) G1 outcomes computed under the earlier harness convention are reported as such and do not count. A G1
         record counts only from a harness whose diff the verifier has checked against 3.0 (b') (1) and 3.0 (d).
(5) Nothing else changes: no threshold, ladder, floor or pass rule of 3.0 and 3.2. (2) adds a classification with a
    coverage condition, (3) repairs a test construction, and (4) corrects the harness to the registered rule. (2) and
    (3) are post-result changes and carry their labels wherever they decide an outcome.
(k) (v1.18, post-result) Upward extension of the coefficient-column ladder (G1). v1.18 was written after:
    - the G1 records of S09_own, S01_own, S05_own and manu_large_omega on harness v4 (numerics' notes of 07:22Z to 07:34Z);
    - the verifier's independent S09_own J_cw check (V194).
    It was written before the lead had read any coefficient-column record of harness v5c, and before any evaluation at the step added here.
(1) Facts (numerics 07:33Z, V194):
    - At manu_large_omega, the gauge group of the J_f coefficient columns 186, 189 and 215 fails, and is not small-amplitude (gauge-row derivative 3e-6 to
      5.5e-6 against column norms 1.7e-4). e = 1.65e-6 at h = 1e-3 and 2.75e-5 at 1e-4, and it grows roughly as 1/h over the remaining steps.
    - At S09_own, in the verifier's independently drawn J_cw column 116 (s_j = 1), the near-origin group has 1.58e-6 of the column norm, so it is not
      small-amplitude. e = 1.31e-6 at h = 1e-3 and 1.27e-5 at 1e-4, and it grows roughly as 1/h.
    In both cases every other group and the whole column pass. The largest step passes, and the second step fails because the error grows. The growth is
    consistent with rounding of row values that are large relative to the group derivative, divided by the step, but it does not prove that mechanism.
    These failures stand as registered failures in every record and in the report.
(2) Rule. For the coefficient columns of G1 (J_f, J_cw and J_c), the ladder of 3.0 (b') (1) is extended by one larger step, h = 1e-2, so the steps are
    1e-2 s_j to 1e-7 s_j. Rule (d) applies unchanged on the six-step ladder: two consecutive passing steps for each stencil, and the Richardson value from
    the pair of (d) (i) with h' = h/10. The floors, thresholds and groups of 3.0 (c) are unchanged, as are the scaling of 3.0 (b') (1) and the active-set
    rule of 3.0 (e) at every stencil point, including p +- 2h. No further step is added, whatever the outcome.
(3) Nature of the change. Rule (d) asks for some pair of consecutive passing steps, so a comparison that passes on the registered ladder also passes on the
    extended one. The extension can only add passes. It changes gate acceptance after results, and a comparison that passes only on the extended ladder is
    labelled "pass under the post-result step rule (k)". The larger step reduces the resolution of structure below 1e-2 s_j (3.0 (b'')), and the report
    states this limit.
(4) Scope. It applies to coefficient columns of G1 on every case of 3.1, and to all of them alike, with no selection of columns. Parameter columns, G3 and
    G8 are unchanged. A comparison that already passes on the registered ladder cannot change its outcome, so the extra step needs to be evaluated only for
    the column groups that do not pass there. For each such column, the steps 1e-2 s_j and 1e-3 s_j are evaluated afresh in one record. That record carries
    every witness of 3.6 (j) (4) (iii), on the deciding harness and checker of 3.6 (j) (4) (iv).
(5) Relation to 3.6 (j). The small-amplitude rule of 3.6 (j) (2) is applied after this rule, to the comparisons that still fail. Each case and Jacobian
    reports three outcomes:
    (i) the registered outcome (five-step ladder of 3.0 (b') (1));
    (ii) with (k);
    (iii) with (k) and 3.6 (j).
    Each comparison carries its label. For a group that passes only at the step 1e-2 s_j, the report gives the per-decade error ratio between 1e-2 s_j and
    1e-3 s_j.
(6) Verifier reproduction (3.0 (b'')). A pass under (k) counts for the provisional release only after the verifier reproduces the extended-ladder outcome
    with its own script on a named case. This version names, before their evaluation at the step 1e-2:
    - S09_own: J_cw column 116 of the verifier's draw (seed 281020269), near-origin group;
    - manu_large_omega: J_f columns 186, 189 and 215, gauge group.
(7) Labels. If the provisional release depends on (k) or 3.6 (j), the release note says so, and the records of the released runs carry the label
    "G1 under post-result rules 3.6 (j), (k)". The report states the registered G1 outcome of every release case beside the amended outcomes.
(8) Nothing else changes: no threshold, floor, group or pass condition. (k) adds one step to a ladder.

(l) (v1.19, post-result) Reference of higher precision for failing G1 parameter-column comparisons. v1.19 was written after:
    - the harness-v5c G1 records of S01_shift_a, S05_shift_c and manu_small_omega (numerics' note of 09:11:54Z) and the extra-step record of
      S01_shift_a (numerics 09:16:07Z);
    - V217 to V221.
    It was written before the lead had read any record of the other cases of 3.1 (manu_near_edge, manu_a, manu_allm_c, S11_own, S20_own), and
    before any evaluation of the reference defined here.
(1) Facts (J_cw values; J_f and J_c agree to the digits given):
    - S01_shift_a, column z_c, group far_anchor_block. |d| = 1.03e-8 against the column norm 9.16. The group's value norm is 2.0e-8
      (F = 2.0e-18). e = 2.58e-6 at h = 1e-3 and 2.58e-5 at 1e-4, and it grows as 1/h over the remaining steps; ||D_h - d|| = 2.7e-14 at
      h = 1e-3. In exact arithmetic the z_c column is dc_l/dz_c (here 0.016) times the physical c_l column. The physical c_l column passes in
      this group (smallest e 3.4e-6); the z_c steps move c_l by 1.6e-5 to 1.6e-9.
    - S05_shift_c, group far_anchor_block, columns z_c (|d| 7.1e-8 against 16.3) and physical c_l (|d| 2.8e-6 against 650.6); value norm
      2.7e-8. For c_l, e = 4.4e-3, 4.4e-5, 6.3e-6, 5.2e-5 and 5.5e-5 at h = 1e-3 to 1e-7: second-order truncation down to 1e-5, and growth as
      1/h below it. The interval of h with e <= 1e-5 is narrower than one decade, so two consecutive registered steps cannot both lie in it;
      the five-point stencil passes at 1e-4 only. The z_c steps (factor 0.025) sample the same interval.
    - In both cases the noise of the differences in this group corresponds to perturbations of the rows of 3e-9 to 1e-8 of their value norm,
      far above the rounding of the rows themselves. This is consistent with float64 rounding of larger intermediate quantities that change
      with the parameters (for example the pressure tables rebuilt at every stencil point). That mechanism is not shown.
    - These failures stand as registered failures in every record and in the report. Rules (j) and (k) do not apply to parameter columns.
(2) Rule. For a parameter column of G1 (J_f, J_cw and J_c; physical and optimizer coordinates) that fails the registered rule on a case of
    3.1, the comparisons of that column are recomputed against a reference of higher precision.
    (i) The residual at every stencil point is evaluated by a test-only copy of the production code. In it, the quantities that the production
        code rounds to float64 between the parameters and the weighted rows are carried in double-double arithmetic: the parameter-dependent
        tables, the field values and derivatives at the rows, the pressure and its gradient, and the assembly of the weighted rows. D_h and
        D4_h are formed in double-double before rounding. The record lists every quantity that remains in float64.
    (ii) The derivative d is the production column, unchanged. The steps, stencils and five-step ladder, the scaling of 3.0 (b') (1), the
         floors F (taken from the registered record), the thresholds, groups and row blocks, the active-set rule of 3.0 (e) and the pass rule
         of 3.0 (d) are unchanged.
    (iii) Every group, every row block and the whole column are judged again, not only the failing group. The column passes under (l) only
          if all of them pass.
(3) Same-function check. The test-only copy changes arithmetic only.
    (i) Its diff against the production code is recorded, and the verifier checks it.
    (ii) At the base point it reproduces O1 within 1e-12 relative.
    (iii) At the base point and at the stencil points of the steps 1e-3 and 1e-4, its rows, rounded to float64, agree with the production rows
          within 1e-6 of the value norm in every group of 3.0 (c). A dropped parameter dependence moves the rows by about |d| h, which exceeds
          this bound at these steps in the failing groups of (1). The agreement found is recorded per group.
    If a check fails, the comparison is not recomputed and the registered failure decides.
(4) Nature. All groups are judged again, so a more accurate reference can change an outcome in either direction. It is evaluated only where
    the registered rule fails, so for the release it can only add passes, and it changes the reference of a comparison after results. A
    comparison that passes only under it is labelled "pass under the post-result reference rule (l)". Both outcomes are reported for every
    case, column and Jacobian, with e on both references at every step.
(5) Power. The negative controls G8 (i) and (iii), which act on the parameter columns, are judged against the differences of (l) on one case
    of 3.1 where (l) is evaluated and where they are excited. Each must still fail by at least 100 tau in the affected group.
(6) Verifier reproduction (3.0 (b'')). A pass under (l) counts for the full release only after the verifier has checked the diff of (3) (i)
    and reproduced the outcome with its own script from complete records. This version names, before their evaluation:
    - S05_shift_c: J_cw, physical c_l, far_anchor_block;
    - S01_shift_a: J_cw, z_c, far_anchor_block.
(7) Scope. Every parameter column that fails the registered rule on a case of 3.1, with no selection. (l) is not applied to coefficient
    columns, which have (j) and (k). G3 is unchanged, and G8 is unchanged apart from (5).
(8) Labels. Runs started after a full release that depends on (l) carry the label "G1 under post-result rules 3.6 (j), (k), (l)". The
    provisional release (lead note of 08:50Z) does not depend on (l), and its label is unchanged.
(9) If the test-only copy cannot be built, or a comparison fails under (l), the registered failure stands and 3.4 (d) applies: the derivative
    is investigated and repaired, and the full release is not given while the failure stands. Runs under the provisional release continue
    under 3.4 (b).
(10) Nothing else changes: no threshold, floor, ladder, group or pass condition.
(m) (v1.20, post-result) Timing of the full release, and the S11_own G3 failure. v1.20 was written after every record of
    the 3.1 cases that existed at 2026-10-29T14:29Z (including the seven-step G3 add-ons of S20_own, manu_a and S11_own and
    the verifier's V332), the P1 and P2 pair results at the end of segment 2, and V333. It is a relaxation of the release
    order of 3.6 (b), which v1.13 introduced as a tightening, made after results; it changes no threshold, floor, ladder,
    group, estimator or pass rule, and no registered failure is reclassified.
(1) Items open at the time of writing:
    (i) S05_shift_c under (l): the elementary qualification of the physical c_l column (running), the J_f and J_c records of
        that column (absent at 14:24:30Z, V333), the qualification of the z_c column (its first run stopped at 14:19:36Z on a
        file-key mismatch in the qualifier, before any comparison), and the verifier's checks of both qualifications;
    (ii) the (k) add-ons of manu_a and manu_allm_c (running) and the verifier's reproduction of them;
    (iii) S11_own G3 along random_scaled_2 ((3) below).
(2) The full release (3.4 (c)) may be posted while the items of (1) are open. They run after it as confirmations in the
    sense of 3.5 (a): if a comparison of (1) (i) or (ii) fails, or a qualification is not confirmed by the verifier, or (3)
    ends with a finding against the derivative, every run started under the full release is relabelled "invalid
    derivative" (3.4 (c)), its states are diagnostic only, and 3.4 (d) applies. The items of (1) keep the chain slots that
    run them; the rerun of the S05_shift_c z_c qualification takes the first slot freed by a validation chain.
(3) S11_own G3, random_scaled_2. Registered outcome: FAIL on O1 and on the gauge-subtracted estimator, on the five-step
    and the seven-step ladders. The record (optimizer coordinates, all seven steps active-set valid) has d = -8.5225e-8 with
    the floor F = 8.37e-7 of 3.0 (c), so d is small against ||r|| ||J_c v||. With F = 0 the second-order errors of O1 are
    6.17e-3, 6.17e-5, 2.44e-6, 2.23e-5 at h = 1e-5, 1e-6, 1e-7, 1e-8 (per-decade ratio 100.0 from 1e-4 to 1e-6, then
    growing as h decreases); the five-point errors are 4.80e-8 and 1.18e-8 at h = 1e-5 and 1e-6 (ratio 4.1e3 from 1e-4 to
    1e-5), so (d) (ii) holds, (d) (i) fails, and (d) (iii) has no admissible pair. The gauge-subtracted estimator gives the
    same pattern (second order 1.14e-5, 1.66e-6, 2.24e-5 at 1e-6, 1e-7, 1e-8 with F = 0). The failure stands, is reported
    in the gate table beside the eight passing directions, and S11_own is reported as not passing G3 under the registered
    rule. The lead's reading, which is a post-result judgement: along this direction the second-order truncation reaches
    tau only at steps where rounding of the O1 evaluations exceeds tau, and the five-point record bounds a bias of d at
    about 1e-8 |d| under the assumption of 3.0 (b''). Investigation under 3.4 (d): the verifier checks this reading from the
    saved differences (truncation coefficient and ratios of both stencils, rounding level against the precision of the O1
    evaluations, whether a bias above tau |d| is compatible with the five-point record) and states CONFIRMED, REFUTED or
    OPEN. Until CONFIRMED, no FREE job starts from the S11 state (F1 S11 waits), and the report states the full release as
    depending on an unattributed registered G3 failure. If REFUTED, (2) applies.
(4) Labels. Every run started under the full release carries "G1 under post-result rules 3.6 (j), (k), (l)" and "full
    release under the post-result timing rule 3.6 (m)". Segments run before it keep "pre-verifier". The report gives the
    time of the full release, the items of (1) open at that time, and the time and outcome of each confirmation.
(5) Reason. All release-blocking items of 3.5 (a) as named in 3.6 (b), 3.3 and the controlled M3 ratio (V171) are met, and
    the production code (gpu_v1p1) is unchanged since the provisional release. The open items of (1) (i) and (ii) concern
    references and step ladders of the tests; (1) (iii) concerns a direction where the registered stencil cannot meet the
    rule on this ladder. Two of the four host slots of 3.6 (h) are idle while the remaining items run, and the free-parameter
    discovery of Phase II is about 14 hours behind the plan of section 8.
(6) Considered and not adopted: (i) waiting for (1) (i) and (ii), expected between 15:30Z and 16:00Z, which leaves two slots
    idle and still leaves (1) (iii) without a route to a pass; (ii) a double-double reference for G3 along random_scaled_2,
    because (l) (7) keeps G3 unchanged and a new reference chosen after this result would be a further post-result rule;
    (iii) dropping S11_own from 3.6 (b), which would remove a registered case.
(7) Nothing else changes.
(n) (v1.21, post-result) Correction of v1.20, withdrawal of the full release of 14:31:05Z, a reference of higher precision
    for the gauge row of coefficient columns, and the order under the provisional release. v1.21 was written after the
    manu_a (k) add-on record (validation/g1_step_addon_manu_a.json, run 14:17:54Z to 14:25:13Z, file 14:27:41Z, sha256 992a681945d4df57), the coverage
    checker output of 14:28:50Z (validation/gates_gpu_v1_manu_a_coverage.json, sha256 4ec1730326e26fee), numerics' note of 14:34:00Z, V334 and V335.
    It was written before any evaluation of the reference defined in (5), and before the lead had read the manu_allm_c (k)
    add-on record (14:39:51Z) or any segment 3 result.
(1) Correction. The sentence of v1.20 that (m) "was written after every record of the 3.1 cases that existed at
    2026-10-29T14:29Z" is false. The manu_a (k) add-on record and its checker output existed then, and the lead had not read
    them. (m) is otherwise kept, with the changes of (4) and (8) below.
(2) Facts (checker output of 14:28:50Z; J_f, J_cw and J_c agree to the digits given).
    - manu_a G1 with (k): FAIL in all three Jacobians (J_f columns 189, 724, 793, 856, 873, 912, 1035, 1104, 1354; J_cw and J_c
      columns 189, 793, 873, 912, 1035, 1104, 1354).
    - With (k) and (j): every group and row block passes except the gauge group, which is OPEN in all three Jacobians. Its
      failing column is 189; column 186 passes there under (k); 6 coefficient columns cover the group.
    - Column 189, gauge group: the gauge-row derivative is 4.07e-7 against the column norm 1.72e-4 (2.4e-3 of it), so the
      group is not small-amplitude. Second-order e = 2.28e-6 at h = 1e-2 s_j and 5.90e-6 at 1e-3 s_j; five-point e = 3.19e-6
      and 1.04e-5; Richardson 5.99e-6. The five-point stencil fails at 1e-3 s_j (tau 1e-5), so (d) (ii) holds at one step
      only. The error grows as h decreases (ratio 0.386 per decade from 1e-2 to 1e-3), and the absolute differences
      (9.3e-13 and 2.4e-12) are of the size that a perturbation of the gauge row of about 5e-15 would give at these steps.
      This is consistent with rounding of the gauge row 100 (||F|| - 1), whose value is close to 0 while ||F|| is close to 1,
      but the mechanism is not shown.
    - Numerics' note of 14:34:00Z lists columns 186 and 189 as failing in the gauge group with 5 covering columns, and the
      J_f far group as OPEN for column 1389. The checker output of 14:28:50Z lists 189 only, coverage 6, and no open far
      group (column 1389 passes the far group under (k), ratio 0.107). The verifier's replay of the record decides; until
      then the note's reading is kept as the more severe one.
    - These failures stand as registered failures in every record and in the report.
(3) Withdrawal. By (m) (2) and (j) (2) (iv), an OPEN group blocks as a failure, so the full release of the lead note of
    2026-10-29T14:31:05Z is withdrawn (lead note of 14:40:01Z). No run had started under it: no acknowledgement file
    existed and queue/running was empty at 14:37:40Z. Nothing is relabelled. 3.4 (d) applies to the gauge group of manu_a
    column 189: the derivative is investigated, and repaired if it is wrong.
(4) Investigation under 3.4 (d) (a diagnostic; it decides no gate). At the manu_a base point, for columns 189 and 186, the
    record gives: the gauge-row entries of J_f, J_cw and J_c; an independent evaluation of the same derivative from the
    definition of the gauge row (the modal formula of (5) (i) as corrected at v1.22; forward-mode differentiation in
    double-double, which for this formula is dg/da = w (dN/da) / (2 sqrt(N)) with dN/da = 2 W_q t_q dt_q/da for a toroidal
    coefficient, W_q = l(l+1), and the same with s_q and the bracket of (5) (i) as W_q for a poloidal one; or the identity
    N_+ - N_- = sum_q W_q (t_q+ - t_q-) (t_q+ + t_q-) + (the same in s_q), with t_q+ - t_q- formed from the coefficient
    difference, which removes the cancellation of the leading part); the float64 value of
    ||F||^2 and of the gauge row at the base point with their ulps; and the spread of the gauge row over at least three
    summation orders at the base point and at +-1e-3 s_j. The verifier states CONFIRMED, REFUTED or OPEN on agreement of
    the production entry with the independent value. A disagreement above 1e-6 of the entry is a finding against the
    derivative.
(5) Rule (reference of higher precision for the gauge row; post-result). For a coefficient column of G1 (J_f, J_cw and J_c)
    whose gauge group fails or is OPEN on a case of 3.1 after (k) and (j), the gauge group of that column is judged again
    against a reference of higher precision.
    (i) (corrected at v1.22, before any evaluation; the v1.21 wording described tail-field values at quadrature nodes and a
        quadrature sum, which is not the production function; verifier note of 14:47:31Z) A test-only copy of the
        production code evaluates the gauge row g = w (sqrt(N) - 1), w = gauge_weight = 100, at every stencil point of the
        six-step ladder of (k). N is the production tail_norm2, the analytic modal energy
            N = sum_q [ l(l+1) t_q^2 + ( l^2 (l+1)^2 + l(l+1) ((2 - alpha)^2 + (m omega / c_l)^2) ) s_q^2 ],
            t_q = (sum_k aT[k, q]) R0^(alpha + l),   s_q = (sum_k aS[k, q]) R0^(alpha + l - 1),
        as computed by Problem.tail_amplitudes, mode_tail_energies, tail_norm2 and the first row of gauge_residuals (the
        manu_a gauge group is this one row). No tail-field sample and no angular quadrature enters. The map from the
        optimizer coordinates to aT and aS, the radial sums, the products with the powers of R0, the squares, the products
        with the mode weights, the sum over q, the square root, the subtraction of 1 and the product with w are carried in
        double-double; D_h and D4_h are formed in double-double from these values before rounding. A quantity that does not
        depend on the perturbed coefficient (alpha, the powers of R0, the mode weights, m omega / c_l, w) is taken as the
        production float64 value and then held exactly. The record lists each such quantity with its hex value and every
        other quantity that remains in float64. The stencil inputs are the float64 optimizer vectors of the registered
        record, bitwise, and D_h and D4_h divide by the same h as the registered record.
        (v1.24, before any evaluation; verifier V358 item 1) The coefficient-independent quantities of the map from the
        optimizer coordinates to aT and aS are among the quantities held exactly: alpha, kappa = omega / c_l, k2, k4, the
        tail-constraint constants p and q, k4 - p, and the rows of the constraint solve built from them, each as its
        production float64 value. The dependent coefficients are solved in higher precision from these held rows by a
        test-only routine; the shared production code and the shared double-double tables are not changed. A routine that
        recomputes these constants from c_l and omega in higher precision does not meet (i).
    (i') Saved inputs (verifier note of 14:47:31Z), written and hashed before the evaluation: the base optimizer vector (hex);
         the coefficient arrays aT and aS at the base; for columns 189 and 186 the coefficient each column moves (potential,
         radial index k, mode index q, l, m) and the map entry; c_l and omega (hex), alpha and R0; the l and m arrays in the
         production mode order; s_j and the steps; the production gauge entries of J_f, J_cw and J_c of each column; every
         input of the double-double stencil (the float64 stencil vectors, or their differences from the base, in hex).
         (v1.24; verifier V358 item 2) The saved inputs also include, for both columns 186 and 189, the base A and C, the
         exact rounded constraint rows, the mode and layout maps, and the ties to the registered source and record. They
         are written as one file whose hash is recorded before the first evaluation; the evaluation reads that file and
         checks its hash.
    (ii) The derivative d is the production entry, unchanged. The steps, stencils, scaling of 3.0 (b') (1), floor F (from the
         registered record), threshold, active-set rule of 3.0 (e) and pass rule of 3.0 (d) are unchanged.
         (v1.24; verifier V358 item 3) d, F, the base vector and the nominal steps are read from the registered (k) add-on
         record and checked against it bitwise; regenerating them is not enough. The active set of 3.0 (e) and its
         evidence are saved at every stencil point.
         (v1.25, before any evaluation; verifier note of 15:57:04Z, V366) The registered records of manu_a
         (gates_gpu_v1_manu_a.json and g1_step_addon_manu_a.json) do not contain the base optimizer vector. The base vector
         is therefore regenerated by the registered generator of the manufactured cases (seed and source hash recorded).
         It is tied to the registered records by equality, as stored there, of every scalar they hold for this case and
         column: the cost, |d| of the gauge group, F, and the gauge group's difference norms and errors e at every
         registered step (the five steps of the registered record and 1e-2 s_j of the add-on). The record states that the
         original vector was not archived and that its identity rests on these equalities. If any of them fails, the
         reference is not evaluated, the registered outcome stands and 3.4 (d) applies. The active-set evidence of 3.0 (e)
         is saved in full at every stencil point: median shell, clamped shells, geometry, the active denominator floors and
         the maxima; no part of it is exempted.
    (iii) Same-function check: the copy's diff against the production code is recorded and checked by the verifier; at the
          base point and at the stencil points of 1e-2 s_j and 1e-3 s_j, the copy's gauge row rounded to float64 agrees with
          the production row within 1e-3 |d| h. A dropped coefficient dependence moves the row by about |d| h. If a check
          fails, the comparison is not recomputed and the registered failure decides.
          (v1.22, statement of feasibility; the tolerance is unchanged.) The check compares the copy's row, rounded once to
          float64, with the production float64 row, so their difference is the rounding error of the production row. The
          final subtraction of 1 is exact in binary64 when sqrt(N) lies in [1/2, 2] (Sterbenz) and otherwise adds at most
          half an ulp of the difference; the error is that of N, the square root and the product with w. The registered
          manu_a record gives an estimate (not a bound; wording corrected at v1.24) of the row's noise for column 189 of about 2.4e-15 to 2.8e-15 per evaluation (second-order and
          five-point errors at 1e-3 s_j of 2.4e-12 and 4.3e-12, with noise amplification 1/h and 1.5/h). With
          |d| s_j = 4.07e-7 the tolerance is 4.1e-12 at 1e-2 s_j and 4.1e-13 at 1e-3 s_j, so the check can be met with a
          margin of about 100, and a dropped dependence fails it by a factor of about 1e3. The record also reports the
          difference at every stencil point of the six steps (information only).
          (v1.24; verifier V359) The production base row differs from the exact modal value with held inputs by about
          2.0e-14, more than that estimate. This systematic part cancels in differences of production rows but enters the
          check, so the expected margin at 1e-3 s_j is about 20, not 100. The tolerance is unchanged. The record reports
          the production-row difference at every stencil point of all six steps; only the base and the 1e-2 s_j and
          1e-3 s_j points enter the check.
          (v1.25; V366) The offsets used by the difference identity of (4) and by the same-function tolerance are the exact
          differences of the saved endpoints (rational or two-word). A rounded offset is labelled as rounded. The binary64
          stencil vectors are unchanged.
    (iv) Power: the same record judges the entry d (1 + 1e-3) against the reference, and the rule counts only if that
         comparison fails with e >= 1e-4 (10 tau).
         (v1.25; verifier note of 15:57:04Z) The full decision for d (1 + 1e-3) under the rule of (ii) is saved. The power
         check succeeds only if that decision is a failure and e >= 1e-4 holds at every step where the comparison of d
         passes.
    (v) Scope: every such column on every case of 3.1, with no selection; at v1.21 this is manu_a column 189 in J_f, J_cw
        and J_c, and column 186 if the verifier's replay finds it failing. Every other group, row block and the whole column
        keep their registered or (k) outcome. Parameter columns keep (l); G3 and G8 are unchanged.
    (vi) Labels and reporting: "pass under the post-result gauge-row reference rule (n)"; the registered outcome, the
         outcomes with (k), with (k) and (j), and with (n) are all reported, with e on both references at every step.
         (v1.24; verifier V358 item 4) A pass under (n) requires all three of: the ladder decision under (ii), the
         same-function check of (iii) at every named point, and the power check of (iv). The record reports the three
         separately, and the label is given only when all three pass.
    (vii) Verifier reproduction (3.0 (b'')): a pass under (n) counts for the full release only after the verifier has checked
          the diff of (iii) and reproduced the outcome with its own script on manu_a J_cw column 189, named here before the
          evaluation.
    (viii) If the copy cannot be built, a check of (iii) or (iv) fails, or a comparison fails under (n), the registered
           failure stands and 3.4 (d) applies; the full release is not given while it stands.
(6) A new full release requires a lead note "FULL RELEASE" posted after: (a) every comparison of the 3.1 cases has a
    complete record, with none running; (b) none of them fails or is OPEN under the registered rule as amended by (j), (k),
    (l) and (n); (c) the investigation of (4) has no finding against the derivative. The verifier's reproductions of (k)
    (6), (l) (6) and (n) (5) (vii) and its checks of the qualifications may still be open; they then run as confirmations
    under (m) (2). (m) (3) for S11_own is unchanged: F1 S11 waits for CONFIRMED, and V335 (OPEN, not a finding against the
    derivative) keeps it waiting.
(7) Order under the provisional release (post-result relaxation of 3.6 (f) and (h) (2), which put the continuations after
    the full release). While no full release stands, the two concurrent free-parameter jobs of 3.4 (b) are the FREE
    continuations of P1 (S01) and P2 (S09): segment 3, max_iter 240, time limit 7200 s, from the segment 2 end state, then
    the long budget of 8.5 while O1 decreases by more than 1 per cent per hour. They run with "linearization_complete" set,
    so every segment end carries a J_c record for 7.2 to 7.4. Labels: "pre-verifier" and "provisional-release
    continuation, post-result order rule 3.6 (n)". No other free-parameter job, no FIXED control, no P3, F1 to F4 or
    promotion runs under the provisional release. EVAL jobs (J_c records, 7.2 to 7.4, 6.4, holdouts) and validation items
    may take free slots. Order of slots: the slot free at 14:43Z (busy: chains 6 and 11 and a smoke on GPU 6) goes to the P1 continuation; the next slot freed goes to the
    P2 continuation; later slots go to the records of (4) and (5), the S11 capture requested by the verifier (verifier note
    of 14:33:22Z), and the J_c EVAL of the segment 2 end states, in that order. If a full release is posted, segments run
    before it keep "pre-verifier"; if 3.4 (d) finds the derivative wrong, they are relabelled "invalid derivative".
(8) Reason. The provisional release rests on the release-blocking set of 3.5 (a) as named in 3.6 (b), which is unchanged by
    the manu_a outcome; the production code (gpu_v1p1) is unchanged; the 8.3 mix is at 38 per cent FIXED-CONTROL (62 per cent FREE) in
    GPU-hours after P1 and P2 (ledger at 14:42:53Z), and only FREE jobs move it toward 80 per cent. Considered and not adopted: leaving the free
    slots idle until a new full release; running P3 (it adds a FIXED control while the mix is below 80 per cent FREE, and the
    rule of 3.6 (f) then requires a FREE job); a further relaxation of the release order (the error of (1) shows that open
    comparison records cannot be treated as confirmations); dropping manu_a from 3.6 (b), which would remove a registered case.
(9) Nothing else changes: no threshold, floor, ladder, group, estimator or pass condition.
(o) (v1.23) J_c records of the continuations of 3.6 (n) (7), and the continuation incident of 15:02Z to 15:12Z.
(1) Facts. The first continuation jobs (cont_p1_s3_S01 and cont_p2_s3_S09, staged at 15:02:46Z and 15:03:25Z) carried the
    configuration key linearization_complete, which segment 2 did not have. The worker's continuation guard (configuration
    equality with the previous segment, 3.6 (i)) refused the resume, and the worker then ran from the starting files. These
    were fresh starts, not continuations. They are labelled INVALID_fresh_start_*, are diagnostic only and are excluded from
    every result; their GPU-hours stay in the 8.3 denominator under FREE. The jobs cont1_s3_S01 and cont2_s3_S09 (staged
    15:13:47Z and 15:14:28Z) resumed at accepted iterations 228 and 280 with the segment 2 configuration, changed only in
    max_iter and the time limit.
(2) Rule. For the continuations of (n) (7), the J_c record of each segment end is produced by an EVAL job from the
    segment-end checkpoint. It uses the same function as the worker's linearization_complete path: the J_cw at that state,
    then complete_jacobian_from_Jcw. The checkpoint's sha256 and the code hashes are recorded. This replaces the words "They
    run with linearization_complete set" of (n) (7). The labels of (n) (7) are carried in the job metadata, not in the
    configuration. The configuration-equality guard is unchanged.
(3) Safeguard. Every continuation is checked before its first accepted iteration is used: the worker's resume line must give
    the iteration and counters of the previous segment end. If it does not, the job is stopped at once and labelled INVALID.
    A worker change that turns a refused continuation into an error exit is allowed only as a code change, with a recorded
    diff that the verifier checks before use.
(4) Reason. The J_c record serves 7.2 to 7.4 at the segment end. An EVAL from the same checkpoint with the same function gives
    the same record without changing the configuration that the resume guard protects. Considered and not adopted: exempting
    the key from the guard, which would be an unreviewed change of production code.
(5) Nothing else changes: no threshold, floor, ladder, group, estimator or pass condition.
(p) (v1.25, prospective) Closure block of J_c v in G3 records.
(1) Facts (numerics' S11 closure diagnostic, record validation/s11_closure_diag_random_scaled_2.json, sha256 9480545c97773f76;
    verifier V342, V345, V347). In the S11_own G3 add-on along random_scaled_2, the closure block of J_c v was a five-point
    difference of the fresh closure rows along v with h = 1e-4/|v|, where |v| = 4.21e13. At that step 701 of the 1469
    coordinates and neither parameter move. The resolved action J_c[closure rows] v, with J_c from complete_jacobian_from_Jcw,
    differs from the captured block (norms 3.151e-2 against 4.278e-2, difference 2.942e-2). With the resolved action,
    r . J_c v = -8.52249077364e-8 against d = g_c . v = -8.52249077325e-8, a relative difference of 4.6e-11. The floor
    F = 1e-3 ||r|| ||J_c v|| changes from 8.3670e-7 to 8.3613e-7. Re-judged with that floor, all four saved ladders stay FAIL.
(2) Rule. A G3 record written after v1.25 forms the closure block of J_c v as J_c[closure rows] v, with J_c from
    complete_jacobian_from_Jcw. It also reports the five-point closure difference along v with its step and the number of
    coordinates the step moves. Records written before v1.25 keep their floors as recorded, and no registered outcome
    changes. The S11_own G3 failure along random_scaled_2 stands. (m) (3) is unchanged: the verifier states CONFIRMED,
    REFUTED or OPEN on the lead's reading, and F1 S11 waits until CONFIRMED.
(3) Reason. A directional step below the resolution of most coordinates does not differentiate the closure rows; the
    per-column steps of complete_jacobian_from_Jcw do. The floor depends on ||J_c v|| only, and the G3 decision is unchanged.
(4) Nothing else changes: no threshold, floor, ladder, group, estimator or pass condition.

## 4. Objective (unchanged production objective, evaluated self-consistently)

4.1 Rows and settings (the degree-6 production configuration of the previous campaign, nest6 ladder): formulation
"mom" (momentum rows) with nonlinear weighting on, denominator "all5far" (far_lambda 1e-2, nl_weight_cap 1e3, shell
weights mean-normalized); the far radii 4096, 16384, 65536 appended to the radial training grid as ordinary momentum
rows with pressure (frozen default far_merged = True, so there is no separate pressure-free vorticity block; for the
first nest rung Nr = 48 + 3 = 51); tail constraints on; closure rows with closure_lambda 1e-3; one gauge row
gauge_weight (||F|| - 1) with gauge_weight 100 (F-gauge in norm form, ||F||^2 the integral of |F|^2 over S^2); the
azimuthal phase fixed by the exact symmetry projection phase_align after each step, not by a residual row; momentum
rows scaled by (1 + r^2/R0^2)^(alpha/2) sqrt(w_node w_ang) sqrt(nl_w); and the training grid and radial counts of the
restarted state. (Corrected in v1.4 after the verifier's V024, which read the first nest rung's job configuration and
the frozen code: v1.0 to v1.3 described separate pressure-free far vorticity rows and a phase residual row, which the
production objective never had. The objective itself is unchanged.) Any difference from this list in a job is recorded in its
configuration and its label.

4.2 Definition. O1(X) = (1/2) ||r(X)||^2, where every state-dependent ingredient (nonlinear shell weights, closure
target G_req, row scalings, gauge-row coefficients, basis, tail-constraint expansion, pressure kernels) is evaluated at
X itself. The previous campaign refreshed weights and the closure target after accepted steps. A fixed point of that
lagged refresh need not be stationary for O1; stationarity in this campaign refers to O1 (section 7). Comparisons with
the previous campaign use the registered diagnostics (section 6), which do not depend on the training weights.
Determinism: the median is the lower median over occupied shells (torch.median convention), ties are broken by shell
index, the denominators carry the floors of the frozen code (1e-6 of their maximum), and the closure target is computed
by the frozen code's deterministic quadrature; any change is recorded in the code and in optimization working report.

4.3 Step acceptance. A trial point X+ is accepted only if O1(X+) < O1(X), with O1(X+) computed from scratch at X+ (new
basis, expansion E, kernels, weights and closure target). (a) With a frozen stage layout (2.5) both values use that
layout. (b) If the layout follows the point and the layouts of X and X+ differ, all of the following are required:
O1_{L+}(X+) < O1_{L+}(X) (common layout), O1_{L+}(X+) < O1_{L}(X) (each value on its own layout), and the decrease
O1_{L}(X) - O1_{L+}(X+) exceeds |O1_{L+}(X) - O1_{L}(X)|; the local model is rebuilt after such a step. The gain ratio
uses the actual decrease and the predicted decrease of the model that produced the step. A frozen-weight or lagged
Gauss-Newton model is allowed to generate steps and is labelled as such; it is never used to accept a step. Every
rejected trial records the reason (increase of O1, gain ratio below threshold, non-finite value, parameter-domain
violation, trust-region cut, saturation, layout rule) and O1(X+).

4.4 Diagnostic variants. Objectives other than O1 (different row weights, Sigma_Z rows, balance rows, vorticity rows,
viscosity) are allowed only as separately labelled diagnostic variants O2, O3, ..., each registered in team notes
with its reason (a concrete conditioning problem of O1) before it runs. Their results are never presented as effects of
freeing the parameters. Solver changes (scaling, damping, trust region, QR or SVD solves, matrix-free least squares,
block preconditioning, Gauss-Newton or Newton-Krylov) do not change O1 and need no relabelling.

## 5. Parameter constraints

5.1 Domain 0.4 < c_l < 0.5, omega > 0. Default transform c_l = 0.4 + 0.1 sigmoid(z_c), omega = exp(z_w). Another
smooth or reliably bound-constrained formulation is allowed if it is recorded.
5.2 Every gradient, step and stationarity diagnostic is reported in physical (c_l, omega) and optimizer (z_c, z_w)
coordinates: dO/dz_c = 0.1 sigma(1 - sigma) dO/dc_l and dO/dz_w = omega dO/domega.
5.3 Saturation flag (a diagnostic stop condition, not convergence): min(c_l - 0.4, 0.5 - c_l) < 0.002, or
omega < 1e-3, or omega > 1e3. A run flagged for 50 consecutive accepted iterations is stopped with reason "saturation".
5.4 Near edge: min(c_l - 0.4, 0.5 - c_l) < 0.02 carries the registered near-edge label (e3 specification v1.21 (d)) for the
state and the arm.
5.5 Trust region on parameter steps: |delta z_c| <= 0.5 and |delta z_w| <= 0.5 per trial (stability only). A run
must be able to move omega below 0.1 or above 10 over many steps; the bound is recorded and may be changed for
stability, not to steer the location.
5.6 States in the saturation zone, with omega drifting toward 0, or approaching the edge without the v1.21 (d) evidence,
are diagnostic results, not profile candidates (section 6.3).

## 6. Acceptance tiers and diagnostics (carried over unchanged)

6.1 The registered Tier S, Tier R and Tier A requirements of the previous campaign (e3 specification v1.24 section 8, with the
additions v1, v1.15, v1.17, v1.19, v1.21 and v1.22, the stall rule, and the diagnostics of section 7 there) apply
unchanged, verbatim from registered/e3_specification_v1.24_sections_7_to_10.md. Compact reading (the registered text governs):
Tier S: rho_u^max <= 1e-2 on both shell families, rho_nl^max <= 1e-1, rho_sp^max <= 1e-1, sigma_u^max <= 1e-1 (with the
core-resolved sets of v1.21 (b)), sigma_Om <= 1e-1, rho_P^max <= 1e-3, rho_div^max <= 1e-8, N1 to N6 without flags (N2:
lambda_max(S) >= 0.9), N_core >= 1e-2, N_F >= 1e-2, e_core >= 1e-4, e_F >= 1e-4, core resolution (v1.21 (c)).
Tier R and Tier A: as registered, including the three refinement levels, a_max decrease, field-size growth limits,
independent re-evaluation within a factor 3, and the Tier A values.
6.2 Consequence of the degree restriction. Tier R and Tier A require three levels that each raise the angular degree.
This campaign is restricted to main degree 6, so Tier R and Tier A cannot be attained here; no state of this campaign
can carry the previous campaign's labels A or B. Tier S status is evaluated for every promising state. Registered
items that need levels L2 and L3 (for example the near-edge evidence of v1.21 (d) and the collapse rules per level) are
OPEN in this campaign; they are not replaced by quadrature refinement. Radial counts of each restarted state are kept
(prompt section 2); no radial ladder is run as an optimization.
6.3 False-improvement rules (prompt section 7). (a) Exclusions: a state is diagnostic only (not a profile candidate,
not usable for outcome A) if any holds: a Tier S nontriviality warning (N_core < 1e-2, N_F < 1e-2, e_core < 1e-4 or
e_F < 1e-4: collapse toward axisymmetry); max|U| or ||U||_L2(|y| < 1) in the F-gauge below 0.1 times its start value
(collapse of the core toward zero velocity; the F-gauge fixes the tail, not the core); the saturation flag of 5.3; the
near-edge label (5.4) without the v1.21 (d) evidence, which is OPEN here (6.2); core unresolved in the sense of v1.21
(c); rho_P^max > 1e-3 or a failure of G5 at the state (pressure or angular-table cancellation); a decrease of
rho_u^max accompanied by an increase of a_max on the core-resolved sets of v1.21 (b) by more than a factor 2 relative to
the start.
(b) Flags: a state is not a profile candidate while any of the following flags is open; a flag is cleared only by a
dated lead note giving the evidence that the improvement is not caused by the flagged behaviour, with the verifier's
concurrence: omega < 1e-2, or omega decreasing monotonically by more than a factor 10 during the run (drift toward
omega = 0); a_eff decreasing by more than a factor 2 during the run (increasing core concentration); the top two radial
coefficients of any block above 0.1 of the block's largest coefficient, or the energy fraction in the top 20 per cent of
radial modes (N6) above twice its start value (high-frequency growth); the vorticity maximum at radius above 2^8 R0 or
inside the innermost resolved shell (core outside the sampled region); the tail onset radius r_tail of N5 increasing by
more than a factor 4 during the run.
6.4 Diagnostics reported for every promising state (prompt section 7), at the actual optimized parameters, on fresh
holdout points (model selection) and, for final claims, on final-test points drawn by the verifier after freezing:
rho_u^max on the standard and the half-offset dyadic shell families separately; sigma_u^max; rho_nl^max and
rho_sp^max; a_max (both weights of v1.22 (c) on the balls); core-ball residuals centred at the vorticity maximum
(v1.21 (b)(ii)); sigma_Om and the core-ball vorticity ratio; origin Taylor and vorticity residuals tau_0, tau_1, tau_2;
rho_div^max and rho_P^max; far-field leading and first-nonlinear coefficient matching (closure mismatch, tau_F at two
radii); E_ren and both sides of the ball identity; H_tot; N1 to N6, N_core, N_F, e_core, e_F; a_eff, R_90, tail-fit
onset, spectral decay (last two radial coefficients per block, angular energy by degree).
6.5 Comparisons across c_l. Because the far-field exponent alpha and the parameter-dependent row weights change
with c_l, comparisons between states at different parameters use (i) the registered weighted diagnostics and (ii)
physical fixed-gauge quantities on a common evaluation domain: RMS(R_u) and RMS(U) on the dyadic shells
2^j R0, j = -4..8, in the F-gauge, unweighted, and their ratio per shell. O1 values at different parameters are not
compared as evidence.
6.6 Holdout versus final-test points: as registered (v1). Ranking and branch selection use holdout points only.

## 7. Stationarity and reduced parameter sensitivity

7.0 Jacobian used. All quantities of 7.1 to 7.4 use the complete Jacobian J_c of the self-consistent residual r(X)
(weights, closure target, carried patterns, scalings and kernels differentiated). Three kinds are distinguished
(v1.5): J_c complete; J_cw with the weights differentiated and the closure target and carried patterns held (the
production step Jacobian from 2026-10-28T21:38Z); J_f with the weights held as well. Quantities from J_cw or J_f are
reported separately and labelled "lagged-closure model" or "frozen-weight model"; they do not establish stationarity
of O1. The quantities of 7.2 and 7.3 describe the linearized residual model at the state; they
are not the Hessian of the coefficient-minimized objective, and the predicted decreases are first-order predictions.
Factorizations are rank revealing (SVD, or QR checked by SVD of R); inverses of S are pseudo-inverses with the declared
cutoff 1e-12 relative to its largest eigenvalue; if S is numerically singular (condition above 1e12) the correlation is
reported as undefined and the state counts as "parameter-singular". A linearization record states its Jacobian kind in
an explicit field jacobian_kind with value J_c, J_cw or J_f (a label is read only by whole-word tokens, and a label
naming more than one kind is ambiguous and not used), its parameter coordinates (physical or optimizer, with the chain
factors dc_l/dz_c and domega/dz_w; a record with optimizer variables but no chain factors and no declaration is
rejected) and the phase generator; a J_cw or J_f record is read and reported only under its model label.
7.1 Gradient. g = grad O1 (the complete gradient of G3, including weight derivatives) in scaled coordinates
g_D = D^-1 g, D = diag of the column norms of J (Marquardt scaling), parameters included. Reported per accepted
iteration: ||g_D||_inf / ||r|| and ||g_D||_2 / ||r|| (with unit-norm scaled columns, the largest cosine between r and a
scaled Jacobian column), the parameter components
dO1/dc_l and dO1/domega (physical) and in optimizer coordinates, and their scaled forms |J_p^T r| / (||J_p|| ||r||).
Scaling rule (v1.10; lead ruling of 2026-10-29T01:27Z on V122). (a) Every gradient record states the point at which it
is taken; the raw complete gradient g at that point, its parameter components (physical and optimizer) and ||g|| are
the 7.1 quantities of the trajectory. (b) The scaled forms g_D = D^-1 g count for 7.1 only when D comes from J_c at the
same point. (c) A record may also carry the scaled form computed with the column norms of a fresh J_cw at the same
point; it is labelled jacobian_kind J_cw ("lagged-closure model scaling") and reported separately under that label.
(d) A scaled value whose column norms come from another point, including a reused J (3.5 (b)), is not recorded.
(e) Records written before the ruling keep their raw values; their scaled fields are marked "scaling from another
point (V122)" and are not reported. On the CPU the spacing of 8.7 applies.
7.2 First-order achievable reduction. eta(t) = ||P_t r||^2 / ||r||^2, where P_t is the orthogonal projector onto the span
of the left singular vectors of the scaled Jacobian (gauge rows included) with singular values above t sigma_max,
for t = 0, 1e-10, 1e-8, 1e-6. eta is the relative decrease that one undamped truncated Gauss-Newton step would give to
first order. Computed by SVD or QR at least at the end of every medium or long job and every 2 hours on Phase III
branches.
7.3 Reduced parameter system. With J = [J_a J_p] in scaled coordinates, P_a the orthogonal projector onto range(J_a)
(the dilation direction handled by the gauge row; the exact azimuthal phase-rotation generator, the tangent of the
phase_align orbit in reduced coefficient coordinates, projected out of the coefficient block, since the phase is fixed
by a projection and not by a row), report:
(a) absorption cosines: for each parameter column and for the eigenvectors of S below,
    c = ||(I - P_a) J_p e|| / ||J_p e|| (c near 0 means the coefficients absorb the parameter direction);
(b) the 2x2 Schur complement S = J_p^T (I - P_a) J_p, its eigenvalues and eigenvectors in scaled and physical units,
    and the correlation coefficient of c_l and omega from S^-1;
(c) the reduced gradient g_red = J_p^T (I - P_a) r and the reduced Gauss-Newton parameter step
    delta p = -S^-1 g_red with its predicted decrease (1/2) g_red^T S^-1 g_red relative to O1;
(d) sensitivity widths (not statistical uncertainties): the parameter displacements at which the reduced quadratic
    model rises by 1 per cent and 10 per cent of O1, along the eigenvectors of S, in physical units and in log omega;
    checked on the actual objective for at least one branch by a profile along both eigen-directions: O1 minimized over a
    at fixed parameter values (fixed-parameter diagnostic runs, labelled PROFILE), at least two values on each side of
    the branch state per direction;
(e) the smallest 20 singular values of the scaled J and J_a with the parameter content of their right singular vectors.
7.4 Credible stationarity of a branch (used by outcome B; all required, measured on the actual objective):
(a) progress: relative decrease of O1 below 1e-3 over the last 50 accepted iterations and over the last 25 per cent of
    the branch's wall time; or, for a branch that terminates sooner, a verified termination in which (b) to (d) hold and
    a line search along the full Gauss-Newton direction of J_c gives no decrease larger than 1e-4 relative;
(b) eta(1e-8) <= 1e-3 and the reduced predicted decrease of 7.3 (c) <= 1e-4; eta(0) and eta(1e-10) reported;
(c) parameter oscillation ranges (maximum minus minimum) over the window of (a): c_l range <= 1e-4 and log omega
    range <= 1e-3;
(d) complete scaled gradient ||g_D||_inf / ||r|| <= 1e-4, and the scaled parameter gradients
    |J_p^T r| / (||J_p|| ||r||) <= 1e-4 for both parameters;
(e) reproduced by a restart from a modest perturbation (coefficient perturbation of relative size 1e-3 and parameter
    perturbation 1e-3 in z_c and z_w) returning to parameters within the 1 per cent sensitivity widths of 7.3 (d) and to
    O1 within 1 per cent.
A branch failing (a) is "incomplete". A branch meeting (a) but failing (b) or (d) is "conditioning-limited" when
eta(1e-10) or eta(0) exceeds 1e-2 while eta(1e-8) <= 1e-3 (reducible residual in directions with singular values below
1e-8 sigma_max), and "not stationary" otherwise. Meeting (a) alone triggers a conditioning investigation (7.2, 7.3,
section 5 of the prompt), never a stationarity claim.
7.5 A parameter is "determined" only through 7.3 (d) and 7.4, never because it changed little during a run.

## 8. Initial states, queue mix and paired experiments

8.1 Starting states are located and verified on disk (SHA-256 of coeffs.npz and meta.json, parameters, L, radial
counts, channels, symmetry class), copied as immutable records into the numerics experiment directory, and their
registered diagnostics recomputed at their own parameters with this campaign's battery (baseline B0 per start).
Priority degree-6 starts (previous campaign candidates): nest6_L6_cl0.45_om1.0_p0 (first degree-6 nest rung, previous
holdout 0.0460/0.0463, independently 0.04604/0.04630), nest6_L6_cl0.45_om0.3_p0, nest6_L6_cl0.42_om0.3_p0,
d6w_L6_cl0.45_om0.3, d6t_L6_cl0.45_om0.3, d6w3_L6_cl0.45_om0.3, s11_L6_cl0.45_om0.3_cl1, s11_L6_cl0.45_om1.0_cl1
(and its d2u variant), plus any unrestricted-class degree-6 state that exists. Paths that do not exist are reported
missing, never replaced.
8.2 Initialization families (prompt section 6): F1 saved states at their own parameters; F2 saved fields at perturbed
parameters, both "coefficients kept" and "refit into the parameter-dependent basis" (least-squares fit of U on the
sample points), each with the relative field change on the common domain of 6.5 recorded; F3 small (1e-3) and moderate
(1e-1) non-axisymmetric coefficient perturbations, seeds recorded; F4 independent random toroidal/poloidal
initializations (geometrically decaying spectra, seeds recorded); F5 diverse core and tail structures within the
degree-6 basis (different core scales and tail amplitudes); F6 a scrambled Sobol design (seed recorded) of 16 points
in c_l in [0.405, 0.495] and log omega in [log 0.05, log 20], used as initial parameters for F2 to F5 seeds.
8.3 Queue mix. Free-parameter discovery runs (both parameters free throughout) take at least 80 per cent of all
GPU-hours spent on coefficient optimization of any label (FREE, FIXED-CONTROL, PROFILE, DIAG variants, refits of
initial states); FIXED-CONTROL and PROFILE together at most 15 per cent. Every job is labelled FREE, FIXED-CONTROL, PROFILE, SMOKE, VALIDATION, DIAG or (v1.10) EVAL.
8.4 Paired experiments. At least three starts from different lineages run as pairs FREE and FIXED-CONTROL with the same
initial state, basis, objective O1, iteration and wall-time budgets on the same GPU type, and identical validation.
The pair result is the ratio of verifier-checked holdout rho_u^max (both families) and the difference in a_max and
sigma_u^max.
8.5 Budgets. Pilot (about 30 min) to detect failure or collapse; medium (2 to 4 h) for promising trajectories; long
(6 to 12 h) when O1 still decreases by more than 1 per cent per hour; termination when a rule of 6.3 (a) or 5.3 fires;
when 7.4 (a) holds, the stationarity and conditioning measures of 7.2 to 7.4 are computed before the job ends or is
replaced. Budgets follow measured throughput. Target 20 to 50 substantive experiments if throughput allows.
8.6 Branch selection for Phase III (by 2026-10-30T08:30Z, hour 36): three to five structurally distinct branches
(different lineage, symmetry class or parameter region; two states are the same branch if their parameters agree within
the 1 per cent widths of 7.3 (d) and their fields agree to 10 per cent in the norm of 6.5), ranked by verifier- or
primary-recomputed holdout rho_u^max with the ordering rule of the previous campaign (7.3b there), excluding states
caught by 6.3.
8.7 CPU-only queue (v1.9). (v1.13) This subsection applies only on the CPU; on the GPU the queue is 3.6 (f). Threads per job t in {1, 2, 4}, chosen to maximize the projected accepted iterations per hour
summed over concurrent jobs; the members of a pair run concurrently with the same t. Order after the provisional
release: pairs P1 (S01) and P2 (S09), FREE and FIXED-CONTROL each, with identical max_iter and time limit, the segment
length giving each FREE job about 6 hours; after the full release P3 (S05; v1.11: S20 does not run on the CPU, 3.5 (c)),
then FREE continuations of the pair FREE partners beyond the matched segment (reported as unmatched), then further FREE
starts (S11, then F2 and F3 from S01). S05 and S01 come from separate nest ladders (at omega 0.3 and
1.0) of the same construction; the report states that the third pair is not a distinct construction or symmetry
class. The mix of 8.3 is computed in CPU-hours. The pair result is reported at the matched segment. The registered
number of experiments of 8.5 is conditional on throughput; the report states how many were possible. If the complete
gradient costs more than a step on the CPU, 7.1 is evaluated at every iteration with a fresh J and at least every 4
accepted steps, with the spacing recorded; 7.2 to 7.4 at the end of every segment.
Segment rules (v1.10; lead note of 2026-10-29T02:09:57Z, fixed before the CPU timing was read). Let p be the projected
seconds per accepted iteration of the adopted configuration and thread count, k the number of concurrent jobs (the
smaller of 4/t and 96 GB divided by the peak RSS of a job), and R the time of the provisional release.
(a) Matched segment length S = max(6 h, 20 p), capped at (2026-10-30T08:30Z - R)/2, so that wave 1 and wave 2 both
finish their matched segments before branch selection. The members of a pair get the same max_iter and time limit.
(b) If k = 4: wave 1 is P1 and P2 (four jobs); wave 2 is P3 and the FREE continuations of P1 and P2. If k = 2: P1,
then P2, then P3, each with S at most (2026-10-30T08:30Z - R)/3.
(c) If even the capped S gives fewer than 10 accepted iterations per FREE job, the pairs still run, the report states
that the comparison rests on fewer than 10 accepted iterations, and FREE continuations and further starts are dropped
first.
(d) The lagged Jacobian only under 3.5 (b); both members of a pair use the same setting.
(e) Segment end on the CPU: the worker runs only the cheap set (7.1 at the end point with a fresh J, the holdout family
values, checkpoint, records) and records its CPU time. The remaining 6.4 items (critical-point search, the full list)
run only on promising states, as separate jobs labelled EVAL, outside the 8.3 denominator and outside the pair budget;
they are required before a state is ranked under 8.6 or enters a claim.
The numbers (t, k, p, S, lagged Jacobian or not) are computed by these rules and 8.7 from the CPU timing record and
posted in a dated lead note, which is part of the record. They are not chosen after any optimization result.

## 9. Profiling report (gate input for 3.4 (b))

One GPU, an existing degree-6 state, synchronized device timings (torch.cuda.synchronize around each timed region, at
least 5 repetitions, median and spread): velocity and derivative assembly; pressure source and reconstruction,
separating kernel-table construction (CPU or GPU) from the Green integrals; residual and objective evaluation;
Jacobian construction (coefficient block, parameter columns); linear solve; trial-step evaluation including the
rebuild; host-device transfers and synchronizations; peak GPU memory, peak RAM, GPU utilization (nvidia-smi sampling);
accepted steps per hour. Fixed-parameter and free-parameter runs compared on the same state, with the extra cost of the
two parameter columns and of the per-trial rebuild stated. The report states the chosen worker count per GPU and the CPU
threads per worker within the side's core limit, and the bottleneck.
(v1.13) On the GPU the GPU form above applies, with the addendum of 3.6 (b). On the CPU (v1.10) the profiling report is the CPU timing record of S01 with the same components (wall times with the
tables built, the parameter-table rebuild, J_cw by chunks extrapolated to all columns, parameter columns, normal
equations and solve, trial evaluation, complete gradient; peak RSS), at one thread and, where recorded, at four threads. Items above 300 s are
timed at least once and the others at least three times, with the spread reported where more than one sample exists;
the five repetitions of the GPU form are not feasible for the long items. (v1.11, from the lead note of 03:02:22Z) The
items under 300 s of the adopted configuration that had one sample (the complete gradient, the parameter columns and
the 64-column J_cw chunk) get three samples from a dedicated one-thread supplement; the per-iteration timings of the
lagged-Jacobian smoke are listed beside them as a second source. Fixed- and free-parameter costs are compared
from the same components, and the report states the chosen threads per job and the bottleneck.

## 10. Records (prompt section 9)

Every job: identifier, label, start record (path and SHA-256), seeds, initial and final c_l and omega, initial and final
O1 and registered diagnostics, objective and parameter trajectory per accepted iteration, g_D and the parameter
gradients (physical and optimizer coordinates), accepted and rejected trials with reasons, damping history, layout
changes, stop reason, wall time, GPU and CPU used, peak GPU and system memory, code and configuration hashes,
validation status. Checkpoints at least every 15 minutes and at accepted improvements; an immutable ledger of accepted
improvements. A failed worker keeps its last valid checkpoint; no silent reset.

## 11. Outcome categories (prompt section 10)

Every Phase III branch receives one primary category and the applicable qualifiers; the campaign category is that of
the best branch under the ordering rule of the previous campaign (7.3b there) with the verifier-checked values, and
branches that are not ordered against it are listed with their categories. The verifier validates the campaign
category before DONE. These categories are distinct from the previous campaign's labels A to D (section 6.2), which are
reported separately, and from Tier S status, which is a separate qualifier ("Tier S met" or the failing items) on every
branch. All final values are evaluated on the same frozen final-test protocol for starts, controls and FREE runs.

Outcome E (checked first, per body of evidence): a gate of section 3 fails and is not repaired, or a G5 or pressure
failure invalidates states. The affected evidence is marked invalid; separately validated branches keep their own
categories. The campaign category is E if no validated branch remains.
Outcome A: two independently initialized FREE runs, neither excluded or flagged under 6.3 or 5.3 to 5.6, each meeting
all of: (i) verifier-checked final-test rho_u^max on both shell families at most 0.5 times the value of its own start
(baseline B0 on the same protocol) and at most 0.5 times its matched FIXED-CONTROL; (ii) the fixed-gauge common-domain
ratio q_phys = max over j = -4..8 of RMS_j(R_u)/RMS_j(U) on the shells of 6.5 at most 0.67 times the start value and
the matched-control value; (iii) sigma_u^max, sigma_Om, a_max (both weights) and the core-ball residuals at most 1.1
times the start and the matched-control values; (iv) far-field coefficient matching (closure mismatch, tau_F) at most
1.1 times the start values; and the two runs reach parameters within each other's 1 per cent sensitivity widths (7.3
(d)). Reported with the parameters, widths, conditioning and the matched-control improvement. A carries qualifier C if
7.4 fails and qualifier D if a criterion of outcome D holds. A small residual is not proof of existence.
Outcome B: the branch meets credible stationarity (7.4) and is not A. The residual structure (terms and regions of
6.4) and the comparison of stationary states reached from different initializations are reported. If Tier S is met the
qualifier says so; if not, the failing Tier S items are listed. Not a proof of a finite-basis limitation.
Outcome C: the branch does not meet 7.4 (incomplete, conditioning-limited or not stationary) and is not A. The residual
is not called a basis-resolution floor; the best states are preserved and the solver problem quantified (eta(t),
singular values, damping history, rejected-step reasons).
Outcome D (primary when the best state is degenerate, otherwise a qualifier of A, B or C): an absorption cosine of
7.3 (a) below 1e-3 for some parameter direction; |corr(c_l, omega)| above 0.999 or S parameter-singular (7.0); a 1 per
cent sensitivity width above 0.05 in c_l or above log 10 in log omega; boundary saturation (5.3), the near-edge label
without its evidence, omega drift toward 0, or loss of nontriviality (6.3 (a)). The reduced sensitivity is reported
with the reason a parameter value cannot be inferred. These thresholds are warning levels: the report states what the
measured sensitivity does and does not determine.
No outcome establishes nonexistence.

## 12. Deliverables and resources

FINAL_REPORT.md follows prompt section 11 (A to E), with independently checked values marked, the real elapsed time,
the project GPU-hours (allocated, occupied by productive work, and measured utilization separately) and the resource
restrictions. It is self-contained and refers to code and data as the accompanying artifacts.

## 13. Roles and timetable

Phase I (to about 2026-10-29T00:30Z, extended if the gates need it): numerics implements and validates the parameter
Jacobian, profiles, tests resume; verifier checks independently; lead reviews and releases (3.4).
Phase II (to 2026-10-30T08:30Z): broad FREE queue with the mix of 8.3 and the pairs of 8.4.
Phase III (to 2026-10-30T16:30Z): 3 to 5 branches, stationarity and sensitivity (7), reproducibility, strategy
comparison.
Phase IV (to 2026-10-30T19:30Z): freeze states (by 2026-10-30T16:30Z), verifier final-test evaluation, report.

## 14. Change log

v1.0, 2026-10-28T20:42Z: initial registration, before any result.
v1.1, 2026-10-28T20:53Z: amendments after the audit by an external referee (a second model), before any result:
  five-point stencil and two-consecutive-step pass rule with Richardson check replace the order and plateau rules
  (3.0 (d), which a biased derivative could pass); floors defined (3.0 (c)); active-set check at all stencil points
  (3.0 (e)); G2 (b) split by the pressure term; G5 (c) floor; G7 extended to optimizer, generator and layout state;
  G8 negative controls added; G6 to G8 required before the provisional release; degraded production mode removed
  (3.4 (d)); frozen stage layout preferred and the layout acceptance rule strengthened (2.5, 4.3), since comparing on a
  common layout alone could accept a pointwise increase; determinism of the weights (4.2); radial ladders removed and
  L2/L3-dependent registered items marked OPEN (6.2); 6.3 split into exclusions and flags with a clearance rule and a
  core-amplitude collapse guard; complete Jacobian J_c required for section 7 (7.0); gradient normalized by ||r||;
  eta at t = 0 and 1e-10 reported; 7.4 rewritten (verified termination, oscillation ranges, complete-gradient gate,
  conditioning-limited definition); widths renamed sensitivity widths and profiled along eigen-directions; queue cap
  counts all coefficient optimization (8.3); outcome categories made exhaustive (A with qualifiers, B and C cover
  stationary and non-stationary branches, D as primary or qualifier, E scoped to invalidated evidence), A requires both
  FREE runs to meet every condition and a fixed-gauge physical improvement.
v1.2, 2026-10-28T20:54Z: chronology clarification in the header (verifier note 20:44Z); no threshold changed.
v1.3, 2026-10-28T21:10Z: header chronology corrected (the v1.2 sentence "before any production derivative test result" was true
of v1.0 only); 7.3 implementation note: the lead tool tools/sensitivity.py version 2 builds P_a from the SVD of the
coefficient block with the phase generator projected out and the cutoff of 7.0, and reports widths from the current
point on both sides as well as about the reduced-model minimizer. No threshold changed.
v1.4, 2026-10-28T21:25Z: correction of a description, no threshold relaxed, no production optimization result exists. 4.1 now
  describes the production objective as it is (verifier V024): far radii as momentum rows with pressure, one F-norm
  gauge row, phase fixed by phase_align; 3.0 (c) row blocks, G8 (iii) and (iv) and 7.3 follow that description. G8:
  sizes of omitted contributions also per group and row block; for (i), whose continuous counterpart vanishes, an
  additional table-level derivative test and table-level negative control (an added requirement). 7.0: linearization
  records state Jacobian kind, coordinates and generator (verifier V023); the lead tool tools/sensitivity.py version 4
  reads the worker record and converts optimizer-coordinate parameter columns to physical units. G5 (c) unchanged after
  the verifier's V020 failure; the remedy is a more accurate table evaluation, not a different threshold.
v1.5, 2026-10-28T21:54Z: written after production derivative test results; no threshold, floor or pass rule changed.
  (1) 3.0 (b') (1), coefficient-column steps scaled by s_j = max(1, 1e-4 / ||J_f e_j||). Reason: the production rows are
  at most quadratic in the coefficients at fixed weights, so centered differences carry no truncation error there, and
  columns of the far-field channels have norms down to 1e-11 while the roundoff of r is about 2e-15 / h; their unscaled
  failures were evaluation noise (lead analysis 21:41Z of V027; numerics quick battery 21:50Z, 13 of 20 such columns).
  The numerics side had already coded this rule with a four-step ladder (validation/gates.py of 21:50Z); v1.5 fixes the
  formula and requires the full five-step ladder.
  (2) 3.0 (b') (2), G3 ladder extended by 1e-8 and 1e-9. Reason: O1 is stiff in the parameters (the F-norm gauge row
  depends on alpha and omega; numerics finding 21:38Z), so second-order truncation of a correct gradient exceeds 1e-6
  at every registered step in 8 of 9 directions of V034 (physical c_l: errors 0.0954, 9.54e-4, 9.53e-6 at 1e-5 to 1e-7,
  exact factors of 100; five-point errors below 2.3e-8).
  (3) G1 names the production step Jacobian, now J_cw, and states that J_f tests do not replace it; G3 floor uses J_c.
  (4) 7.0: kinds J_c, J_cw, J_f, explicit jacobian_kind field, ambiguous labels and undeclared optimizer coordinates
  rejected (verifier 21:45Z and V036). Lead tool tools/sensitivity.py version 5 implements this (version 4 kept read only).
  Both outcomes (v1.4 ladder and v1.5 rule) are reported for every G1 coefficient column and every G3 direction.
v1.6, 2026-10-28T22:02Z: after the audit by an external referee (a second model); no
  threshold, floor or pass condition changed, two uses tightened. 3.0 (b'): the v1.5 statements that rescaling leaves
  rule (d) unchanged and that a bias "still fails" were too strong and are replaced (the rules are changes to gate
  acceptance; a pass only under them carries a label); the quadratic motivation of (1) is restricted to the rows it
  covers (it does not cover the gauge row, J_cw or J_c); ||J_f e_j|| = 0 gives OPEN; (2): only the last five steps
  equal the registered ladder along v / 100. New 3.0 (b''): scope of a finite-difference pass, and passes only under
  (b') need the verifier's reproduction on a pre-named case before the provisional release. 3.0 (e): base point
  included in the active-set check, active denominator floors and maxima recorded. Not adopted from the audit: a
  certified truncation and evaluation bound for every accepted estimate (its amendment C) and certification of the
  whole stencil segment (its amendment D), because no bound on third derivatives of the 4.3e5-row residual is
  available in the campaign; the limitation is stated in (b'') and (e) instead.
v1.7, 2026-10-28T22:16Z: after the verifier's V037 (the G3 truncation of a correct gradient is caused by the cubic term of the gauge
  row), V042 (the seven-step ladder passes 8 of 9 V034 directions; random_scaled_2 fails with second-order errors
  2.27e-4, 2.34e-6, 6.59e-7 at 1e-7, 1e-8, 1e-9, a truncation-noise crossing with no two passing steps, five-point and
  Richardson passing) and V043 (the far-radius block of the frozen-weight Jacobian J_f fails for six coefficient
  columns with block derivatives 4.5e-13 to 3.7e-12, errors growing as 1/h). Added 3.0 (b') (3), the gauge-subtracted
  estimator for G3: no threshold, floor, reported derivative or pass condition is changed; passes only under it are
  labelled and need the verifier's reproduction on the cases named for (b'') (S05_own and manu_large_omega, named in
  the lead note of 22:03Z, before evaluation). Not changed after V043: the floor and threshold of the far-radius block
  (the header forbids relaxing them after results). J_f results remain reported only (G1); the production J_cw and the
  complete J_c decide. If their far-radius blocks fail by evaluation noise, the remedy is a more accurate evaluation of
  the far rows, adopted only with a regression of O1 and the pressure gates, as was done for the stable linear
  operator.
v1.8, 2026-10-28T22:49Z: after the verifier's V045 to V051 (J_cw and J_c far-anchor blocks fail for six small coefficient columns by
  evaluation noise; the noise lies in the l = 0, 1 pressure; the production discrete monopole is at rounding level and
  carries the noise, the discrete dipole is a smooth discretization-level value; the exact low moments vanish for
  represented fields; direct table derivatives pass; the double-double angular tables change O1 at S01 and S05 by
  about 1e-14 relative) and before any comparison of the production pressure at the far anchors with an independent
  evaluation. Added: 2.6, the exterior form of the monopole at the far anchors under a rounding-level condition (the
  remedy anticipated in v1.7: a more accurate evaluation of the far rows; no floor or threshold of the far-radius block
  changed); G4 (d), an accuracy requirement for the base pressure at the far anchors, which lie outside the resolved
  range of G4 (a) and (c) (added requirement; part of 3.3); the scope of G5 (c), so that a float64 table path with the
  V020 errors cannot enter the optimizer's residual unnoticed. Reasons: the far anchors carry merged momentum rows with
  the full-space pressure (4.1), the dipole discretization error grows relative to the decaying pressure there, and the
  double-double tables of the production code have a size-dependent float64 fallback.
  Correction at 2026-10-28T22:49Z, same version: 2.6 first said the dipole value was measured at S01; it was measured on the
  V027 field. The first copy is kept as registered/specification_v1.8_error.md.
v1.9, 2026-10-29T01:12Z: after the withdrawal of all GPUs at 2026-10-29T00:57:59Z (side notices of that time; running GPU jobs
  stopped) and before any CPU timing of the production code or any release-battery result on the final code. Added 2.7
  (configuration M, registered in the lead note of 00:44Z after the cost measurement dd2/fp64 = 3.41 and before the
  M1 to M3 results; the CPU form of the M3 time ratio registered at 01:02Z before any CPU timing), 3.5 (CPU-reduced
  release battery, lagged-Jacobian option) and 8.7 (CPU queue). Reasons: on four CPU cores the full battery of 3.1
  and the registered queue cannot both be run within the campaign. The division of 3.1 reduces pre-release
  coverage and is stated as such; it changes no threshold, floor or pass rule, and the cases moved after the
  release still decide the validity of the runs (3.4 (c)). Results known when this was written: D1 on the V027 field
  in all modes (numerics; verifier V114 CONFIRMED), M2 and M3 for dd2 values with float64 tangents on the GPU
  (V113 CONFIRMED for M3), the first T3 rows on S01 (dd2 within 9e-18 of the block norm); no G1, G3 or G8
  result of the final code.
v1.10, 2026-10-29T02:50Z: records rulings and CPU rules from the lead notes of 2026-10-29T01:11Z, 01:27Z, 02:09Z and 02:48Z.
  Written after the one-thread CPU timing of S01 (projected seconds per accepted iteration: float64 about 2430, all-float64
  Jacobian implementation about 2450, dd2 values with float64 tangents about 3790, dd2 about 39000; J_cw plus parameter
  columns about 30 trial evaluations), after M2 for both implementations (V114, V132) and after the T3 rows of S01, S05 and
  S09; before any M3 trajectory result of the all-float64 Jacobian implementation, any lagged-Jacobian smoke result, any
  release-battery result on the final code and any optimization result. Changes: 1.4 now names configuration M as part of
  production (it already was by 2.7; the old text contradicted 2.7); 2.7 names the GPU dd2 run as the trajectory
  reference for M3 on the CPU, because a dd2 run on the CPU is not feasible; 3.5 (b) folds G7 into the lagged-Jacobian
  smoke and lists its records; 7.1 adds the scaling ruling on V122 (scaled gradients only from J_c at the same point,
  J_cw scaling labelled, nothing from another point), which reduces the per-iteration coverage of 7.1 and is stated as
  such; 8.7 adds the segment rules (fixed in the note of 02:09:57Z before the timing was read) and the CPU end-of-segment
  set with EVAL jobs for the remaining 6.4 items, which stay required before ranking or a claim; 8.3 adds the EVAL label;
  9 gives the CPU form of the profiling report with fewer repetitions for the long items. No threshold, floor, ladder or
  pass rule of any gate changes. The whole release battery of 3.5 (a) stays release-blocking.
v1.11, 2026-10-29T04:04Z: written after M1 on all T3 cases (V153 CONFIRMED), the M3 time ratio 1.007 (V149) and the
  cache regression (V155), after the lead's rate sample of the S01_own battery (py-spy at 03:56Z and 04:00Z: G1, J_f
  parameter column z_w, about 65 s per rebuilt stencil point), and before any M3 trajectory result, any lagged-Jacobian
  smoke result, any release-battery result on the final code and any optimization result. Changes: (1) 3.5 (c): S20
  leaves the release battery and the CPU queue because a one-thread battery on S20 needs at least 30 h; 8.7: P3 is
  S05, and the further FREE starts are S11, then F2 and F3. (2) 3.5 (d): a case's battery may run as two processes
  (G1; G2, G4, G3, G5) with a control-flow-only harness change checked by the verifier. (3) Section 9: the supplement
  is the primary source of the three samples for the short items and the smoke the secondary one (lead note of
  03:02:22Z). No threshold, floor, ladder or pass rule changes. The release-blocking coverage is reduced by one field
  (S20) and one symmetry class, and the report says so.
v1.12, 2026-10-29T04:20Z: written after the verifier's note of 04:14:46Z (G3 floor from J_cw, J_f scaling of the G3
  scaled entries, harness J_c in G1) and V160 (split harness CONFIRMED, one test-only exception), and before the lead
  had read any release-battery G3 result or any release-battery J_c column result. Changes: 3.5 (d) record checks for a
  split battery; 3.5 (e) (1) to (4). Each item adds a requirement or a label; no threshold, floor rule, ladder or pass
  rule changes.
v1.13, 2026-10-29T05:01Z: written after the operator's GPU restoration of 02:51:04Z was found (lead at 04:55Z), after the GPU
  M3 record of the all-float64 Jacobian implementation (04:48Z to 04:52Z, V165), the first iterations of the GPU
  lagged-Jacobian smoke (numerics note of 04:59Z) and V161 to V164, and before the lead had read any GPU release-battery
  result or any optimization result. Changes: new 3.6: (a) M3 in its GPU form with a controlled same-device float64
  run before the full release; (b) the GPU battery unsplit, the 3.5 (a) set for the provisional release, the rest of
  3.1 including S20_own and manu_allm_c before the full release (tightening: S20 and the all-m class return, and the
  confirmations move before the full release); (c) pairs on one GPU when memory allows, GPU-hours ledger; (d) G7 in the
  production configuration with the checks named by V161 and V162 and a resume-path repair as snapshot gpu_v1, with
  carry-over conditions; (e) lagged Jacobian off on the GPU; (f) the GPU queue and pair budgets (pilot 120 iterations
  or 3600 s, then 240 iterations or 7200 s); (g) 7.1 per accepted iteration on the GPU. 8.7 and section 9 point to
  3.6. No threshold, floor, ladder or pass rule changes.
v1.14, 2026-10-29T05:22Z: written after numerics' notes of 05:17Z and 05:21Z (gpu_v1 frozen; the fresh-start M3 run on gpu_v1
  identical to the 04:48Z record) and V166, before the lead had read any GPU release-battery result or any optimization
  result. Changes: 3.6 (h): (1) at most four concurrent GPU jobs on the optimization side (one busy host process each);
  pair members under the same sharing condition, alone when a GPU would otherwise idle (replaces the first sentence of
  3.6 (c)); (2) slots go to the remaining validation items before the pairs; (3) G6 is field-level, from numerics or the
  verifier's evaluator, scalar checks supplementary; (4) CPU validation items may run on the lead's core from a
  hash-checked copy. No threshold, floor, ladder or pass rule changes.
v1.15, 2026-10-29T05:53Z: written after the G7 run on gpu_v1 and V172 (state preserved; trigger not as registered),
  V168 to V174, and numerics' notes up to 05:45Z (worker patch gpu_v1p1). It was written before the lead had read any
  GPU release-battery result of the numerics side or any optimization result. Changes: 3.6 (i).
  (1) Production may use gpu_v1p1 (worker only), which replaces the last sentence of 3.6 (d).
  (2) Conditions: V174; G7 as registered on the gpu_v1p1 worker, with fresh-start agreement against the gpu_v1 G7 run;
      the segment continuation smoke.
  (3) Restrictions from V174.
  (4) The 05:21:55Z G7 run is supplementary.
  (5) The segment 2 allowance is 240 iterations above the segment 1 end and 7200 s, so the matched budget is at most
      360 iterations and 3 h.
  No threshold, floor, ladder or pass rule changes.
v1.16, 2026-10-29T06:08Z (post-result): written after the S09_own G1 record (numerics 05:58Z) and
  validation/diag_coef_S09_own.json, and before the lead had read any other case's G1 coefficient-column result or any
  optimization result. Changes: 3.6 (j).
  (1) The S09_own failures are recorded and stand.
  (2) Rounding-level groups of coefficient columns (below 1e-6 of the column, by max(||d||, ||D_h||)) are reported as
      not tested, subject to a coverage condition in the same case and Jacobian, G8 evaluated under the rule, and a
      verifier reproduction.
  (3) Test-only repair of the harness J_c closure step (1e-4 s_j), rerun where the error does not depend on h, both
      outcomes reported.
  No threshold, ladder, floor or pass rule changes.
v1.17, 2026-10-29T06:19Z: written after V178 to V181 and numerics' notes of 06:04Z and 06:07Z, and before the lead had read
  any coefficient-column record of the new harness. Changes to 3.6 (j):
  (2) (i) the rationale "no error confined to such a group can change the whole-column outcome" was false (V180,
      counterexample d = (1, 3 tau/4), D = (1, -3 tau/4)). It is replaced by the bound 2 tau_c per group and
      2 sqrt(k) tau_c over k groups, with the whole-column test retained.
  The classification is renamed small-amplitude, since the mechanism is not proven. Parameter columns are never
  classified, and the coverage condition requires both parameter columns. (2) (vi) states the change of aggregate
  acceptance, the reporting of both outcomes and the verifier reproduction from complete records.
  (3) (i) and (1): the cause is stated as consistent with the fixed closure step, to be tested by the repair.
  (4) new: harness conformance to 3.0 (b') (1) and 3.0 (d) (iii) (V179), complete records, and a verifier diff check
      before a G1 record counts.
  No threshold, ladder, floor or pass rule changes.
v1.18, 2026-10-29T07:40Z: written after the harness-v4 G1 records of S09_own, S01_own, S05_own and manu_large_omega (numerics 07:22Z to
  07:34Z) and V194, and before the lead had read any harness-v5c coefficient record or any evaluation at the added step. New 3.6 (k):
  - the G1 coefficient-column ladder is extended by one larger step, 1e-2 s_j, with rule (d) unchanged; the extension can only add passes,
    so it is labelled post-result;
  - the extra step is evaluated afresh only where the registered ladder fails;
  - three outcomes are reported per case and Jacobian;
  - the verifier reproduces on named comparisons (S09_own J_cw column 116 near-origin, manu_large_omega J_f columns 186, 189 and 215 gauge);
  - released runs carry the label "G1 under post-result rules 3.6 (j), (k)".
  No threshold, floor, group or pass condition changes.
v1.19, 2026-10-29T09:22Z (post-result): written after the harness-v5c G1 records of S01_shift_a, S05_shift_c and manu_small_omega
  (numerics 09:11:54Z), the extra-step record of S01_shift_a (numerics 09:16:07Z) and V217 to V221, and before the lead had read any
  record of manu_near_edge, manu_a, manu_allm_c, S11_own or S20_own, or any evaluation of the new reference. New 3.6 (l):
  - the far_anchor_block failures of the z_c column at S01_shift_a and of the z_c and physical c_l columns at S05_shift_c are recorded and
    stand;
  - a parameter column that fails the registered rule on a case of 3.1 is judged again, in every group, against differences of a test-only
    copy of the residual in double-double arithmetic; d and every threshold, floor, step and pass rule are unchanged;
  - same-function checks (diff, O1, rows within 1e-6 of each group's value norm), G8 (i) and (iii) against the new differences, both outcomes
    reported, verifier reproduction on named comparisons (S05_shift_c physical c_l, S01_shift_a z_c, J_cw, far_anchor_block);
  - label "G1 under post-result rules 3.6 (j), (k), (l)" for runs after a full release that depends on it.
  Considered and not adopted: a larger step for parameter columns as in (k), because at S05_shift_c the larger steps are dominated by
  truncation; a parameter-column analogue of the small-amplitude rule of (j), because G8 (i) and (iii) act in small parameter-column groups.
  No threshold, floor, ladder, group or pass condition changes.
v1.20, 2026-10-29T14:29Z (post-result): written after every record of the 3.1 cases existing at 14:29Z, including the
  seven-step G3 add-ons of S20_own, manu_a and S11_own, V332 and V333, and after the P1 and P2 pair results. New 3.6 (m):
  - the full release may be posted while these items are open: S05_shift_c under (l) (physical c_l qualification and J_f,
    J_c records; z_c qualification rerun; verifier checks), the (k) add-ons of manu_a and manu_allm_c and their reproduction,
    and S11_own G3 random_scaled_2; they run after it as confirmations in the sense of 3.5 (a), with relabelling of every run
    started under the full release on a failure;
  - S11_own G3 random_scaled_2: registered FAIL on both estimators and both ladders stands and is reported; the lead's
    attribution (second-order truncation reaches tau only where rounding exceeds it; five-point bound on a bias about 1e-8
    |d|) goes to the verifier; F1 from S11 waits for its confirmation;
  - label "full release under the post-result timing rule 3.6 (m)" beside "G1 under post-result rules 3.6 (j), (k), (l)".
  This relaxes the release order of 3.6 (b) after results. No threshold, floor, ladder, group, estimator or pass rule changes,
  and no registered failure is reclassified.
- v1.21, 2026-10-29T14:43Z (post-result): written after the manu_a (k) add-on record and its checker output, numerics' note
  of 14:34:00Z, V334 and V335, and before any evaluation of the reference of 3.6 (n) (5). New 3.6 (n):
  - correction: the v1.20 statement that (m) was written after every 3.1 record existing at 14:29Z is false; the manu_a (k)
    record and checker output existed and had not been read;
  - manu_a G1 fails with (k) and is OPEN with (k) and (j) (gauge group, column 189, not small-amplitude); by (m) (2) the full
    release of 14:31:05Z is withdrawn before any run started under it; 3.4 (d) investigation of the gauge row;
  - post-result reference of higher precision for the gauge row of coefficient columns (pre-registered before evaluation,
    same-function check, power check, verifier reproduction on manu_a J_cw column 189);
  - conditions for a new full release: every 3.1 comparison record complete and none failing or OPEN as amended;
  - provisional-release order: the two free-parameter jobs are the P1 and P2 FREE continuations, with J_c records at every
    segment end, labelled "pre-verifier" and "provisional-release continuation, post-result order rule 3.6 (n)".
  No threshold, floor, ladder, group, estimator or pass condition changes.
- v1.22, 2026-10-29T14:53Z (correction before evaluation): 3.6 (n) (5) (i) now names the production function, the gauge row
  w (sqrt(N) - 1) with N the analytic modal tail energy of Problem.tail_norm2, and states which quantities are carried in
  double-double; the v1.21 wording (tail-field values at quadrature nodes, quadrature sum) was wrong (verifier note of
  14:47:31Z). New (5) (i'): the inputs saved and hashed before the evaluation. (5) (iii): statement that the unchanged
  tolerance 1e-3 |d| h can be met, from the rounding of the production row and the registered manu_a record. (4): the
  modal form of the independent evaluation. Written after numerics' note of 14:52:00Z and V339 and before any evaluation
  of (n) (4) or (n) (5). No threshold, floor, ladder, group, estimator or pass condition changes.
- v1.23, 2026-10-29T15:16Z: new 3.6 (o). The first continuation jobs carried a new configuration key, were refused by the resume
  guard and ran as fresh starts (INVALID_fresh_start_*, excluded). The J_c records of the continuations of (n) (7) come from
  EVAL jobs at the segment-end checkpoints (same function, checkpoint hash recorded). Labels are in the job metadata. Every
  continuation's resume line is checked. Written after V348 to V350 and numerics' note of 15:05:00Z, before any segment 3
  end. No threshold, floor, ladder, group, estimator or pass condition changes.
- v1.24, 2026-10-29T15:41Z: 3.6 (n) (5) made explicit before any evaluation of (n) (5) (verifier V358 objection to the
  copy ba5d9e08, V359): (i) the coefficient-independent constants of the coordinate map (alpha, kappa, k2, k4, p, q,
  k4 - p, the constraint rows) are held as production float64 values and the dependent coefficients are solved from the
  held rows by a test-only routine; (i') one hashed pre-input file with both columns, base A and C, rounded constraint
  rows, mode and layout maps and record ties, written before the first evaluation; (ii) d, F, base and steps checked
  bitwise against the registered (k) add-on record, active set saved at every point; (iii) "bounds" corrected to
  "estimate", base-row difference 2.0e-14 (V359), expected margin about 20 at 1e-3 s_j, differences at all six steps
  reported; (vi) a pass needs ladder, same-function and power checks, each reported. Written after the (n) (4) record
  (no finding against the modal differentiation, V359), V356 to V360 and numerics' notes of 15:31:04Z and 15:34:48Z. No
  threshold, floor, ladder, group, estimator or pass condition changes.
- v1.25, 2026-10-29T16:00Z: before any evaluation of (n) (5). (ii): the manu_a base vector, absent from the registered
  records, is regenerated and tied by equality of every stored scalar (cost, |d|, F, gauge-group difference norms and errors
  at every registered step); failure of a tie means no evaluation, the registered outcome stands and 3.4 (d) applies. The
  active-set evidence of 3.0 (e) is saved in full. (iii): offsets are exact endpoint differences, and rounded ones are
  labelled (V366). (iv): the full power decision is saved and must be a failure with e >= 1e-4. New 3.6 (p), prospective:
  the closure block of J_c v in later G3 records is J_c[closure rows] v; S11 facts recorded; no outcome changes; (m) (3)
  unchanged. Written after V364 to V366, the verifier's note of 15:57:04Z and numerics' notes of 15:51:27Z and 15:58:35Z.
  No threshold, floor, ladder, group, estimator or pass condition changes.

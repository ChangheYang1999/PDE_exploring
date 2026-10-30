# c1 shared contracts (coordinator the coordinator)

Version: the run contracts v01, written 2026-10-28 between 20:33Z and 20:38Z (run start T0 = 2026-10-28T20:30:31Z); Amendment v02 at 20:44Z, v03 at 21:05Z, v04 at 21:34Z (end of file).
Changes are made only by publishing a new version section at the end of this file ("Amendment vNN") with its UTC time.
An amendment never changes the meaning of an ID that is already in use; it adds new IDs.

Path abbreviations: the run directory = working file r6 (not published), SH = the exchange directory , A2 = source data (read-only, not included): analysis2/IPM_Analysis_II.artifacts,
C4 = source data (read-only, not included): case4.

## 0. Status vocabulary (mandatory in every shared file)

Theory claims (theory_vNN.md, THEORY_FINAL.md):
- A2-THEOREM: a statement proved in analysis2 and labelled THEOREM there (proof audited by the r5 verifier). Cite the
  section of A2/S1_CLOSURE.md or the part Pnn of A2/S1_PROOFS.md. Use only within its exact stated scope.
- AUDITED: a new result whose complete written proof and numerical constants the T4 theory auditor has marked CONFIRMED (cite the audit
  entry). Only AUDITED and A2-THEOREM results may be called "proved" in any report.
- CLAIMED: a complete written proof exists in the author's lane, audit pending or not finished.
- CONDITIONAL: a theorem one of whose hypotheses is not yet verified; list the unverified hypotheses by name.
- HEURISTIC: derivation with gaps, a scaling argument, or a numerical indication. Never used as a hypothesis of a claim.
- REFUTED: a counterexample or an error was found (cite it).

Numerical quantities (numerics_vNN.md, NUMERICS_FINAL.md, candidate manifests):
- LOSS: a training objective value. Never a norm.
- FLOAT: an independently recomputed floating-point value (state the rule, the grid or quadrature, the truncation
  radius and the precision). Never a bound.
- LB / UB: a rigorous lower / upper bound on the complete whole-plane quantity (interval or ball arithmetic, exact
  rational identities, a proved exterior bound). A bound on a finite box only is labelled BOX-LB / BOX-UB and is
  not a whole-plane bound.
- VALIDATED: a rigorous two-sided enclosure [LB, UB] of the complete whole-plane quantity.
- EXACT: an exact rational or algebraic identity (for example an exactly vanishing far-field sector).
- Audit suffix: CONFIRMED-N4 (the N4 numerical auditor has independently reproduced the number or certificate; cite the audit entry),
  PENDING-N4. Only CONFIRMED-N4 numbers may be called "certified" in any report.

## 1. Equation, parity class and conventions (identical to A2/S1_CLOSURE.md, section 1)

- F(rho; c_l) = (c_l X + U[rho]).grad rho - rho on R^2, X = (x, y), r = |X|, theta = atan2(y, x).
- U[h] = (-R_1 R_2 h, R_1^2 h), R_j = d_j (-Delta)^(-1/2). Equivalently U = (-psi_y, psi_x) with -Delta psi = d_x h,
  psi the canonical inverse (odd in x and in y, psi = o(r^2)).
- Fourier convention (only where Fourier formulas are used): hat f(xi) = int f(X) e^(-i X.xi) dX; R_j has symbol
  -i xi_j/|xi|; U_1 has symbol xi_1 xi_2/|xi|^2 and U_2 has symbol -xi_1^2/|xi|^2.
  Plancherel: ||f||_2^2 = (2 pi)^(-2) ||hat f||_2^2.
- Parity class S1: rho even in x and odd in y. All function spaces are completions of the smooth compactly supported
  functions of this class.
- Strain: c[h] = d_y U_2[h](0) = -h_y(0)/4 + (1/pi) PV int sin(3 theta) h(X) r^(-3) dX (the local term -h_y(0)/4 is
  part of the definition and may never be dropped).
- Linearization: L h = V.grad h - h + U[h].grad rho_tilde, V = c_l X + U[rho_tilde]; correction equation
  L h + U[h].grad h = -F(rho_tilde; c_l).

## 2. Primary chart (normalization) and the reference data

PRIMARY chart (default for every candidate):
- c_l = 4076476460239181/2251799813685248 = 4076476460239181/2^51 exactly (state 131;
  A2/numerics/data/exact_constants_131.json, sha256 65f3493f5b8cfba332bcf0bfbe5f5e16768abc8799b9b2417974a8634ee76354).
- gamma = 1/c_l, delta = 1 - gamma, p_n = 1 - n delta.
- Leading angular profile Theta_0 = the exact Theta_0 of the same file (state 131). Its exponent gamma and Theta_0 are
  fixed: corrections must not change them (A2-THEOREM: the correction spaces E_2, X, N_s are transverse to scaling).
- Center normalization (B0n): c_l + c[rho_tilde] = 1 exactly. For state 131, c[rho_bar] = -1824676646553933/2^51
  exactly. Every candidate must report the status of (B0n) (EXACT, or an enclosure).
- a_0 = d_y rho_tilde(0) must be reported (exact rational or enclosure). For state 131,
  a_0 = 12102479225522702540364244077864789/1174964343508337542719888806641664 = 10.30029489183...
- The scaling direction is excluded by fixing c_l and Theta_0. No phase condition is added unless a theory_vNN file
  derives one that is continuous in the selected space.

EXP charts: a candidate with a different c_l or Theta_0 is in an experimental chart. Its manifest must say
chart = EXP-<slug>, give the exact new c_l and Theta_0, and the numerics file must notify batch T in its first section.
An EXP candidate is never compared with a PRIMARY-chart threshold unless a theory_vNN file states a theorem for that
chart.

Far-field sectors (A2/S1_CLOSURE.md, section 10, Corollary E1): for a finite potential of canonical generator form the
residual expands in sectors (h, q), h, q >= 0 integers, with exponent e(h, q) = gamma - h delta - 2q and angular
coefficient E_(h,q)(theta). The sectors with e >= -2 are (h, 0), h = 0, ..., 5 (exponents p_1 to p_6) and (0, 1), (1, 1)
(exponents gamma - 2 and 2 gamma - 3); (0, 0) vanishes automatically at c = 1/gamma. Membership of F in N_s (and in
H) holds exactly when all eight vanish (A2-THEOREM). Every candidate must publish a sector table: (h, q), exact
exponent, angular coefficients (exact rationals or ball enclosures, all Fourier modes), status EXACT-ZERO /
ENCLOSED-NONZERO / FLOAT, and the first surviving nonzero sector with its angular L^2 norm.
Angular norm convention: ||E||_ang = (int_0^(2 pi) |E(theta)|^2 dtheta)^(1/2), full circle, no 1/(2 pi) factor. A2 uses
the full circle for the fixed sectors (3081.27, 9679.97) but a quadrant value for ||E_1|| = 0.0910 of state 131 (the
full-circle value is 0.18208, the N4 numerical auditor V001/V002); always state which, and default to full circle. For a seven-branch or
other enlarged family the sector list must be rederived for that family and the derivation cited.

## 3. Registered norms (norm IDs)

Common notation: ||f||_2^2 = int_(R^2) |f|^2 dX (Lebesgue measure, no normalizing factor). ||f||_H = ||(-Delta)^(-1/2) f||_2
= sup over phi in Hdot^1 of <f, phi>/||grad phi||_2 (homogeneous Hdot^-1). D^j f is the tensor of all ordered derivatives,
|D^j f|^2 = sum over (i_1, ..., i_j) in {1, 2}^j of |d_(i_1) ... d_(i_j) f|^2 (Frobenius), so |D^2 f|^2 =
f_xx^2 + 2 f_xy^2 + f_yy^2. omega = (1 + 4 r^2)^(2/5), <r> = (1 + r^2)^(1/2), J = (1 - Delta)^(1/2).

NORM-A2-E2 (A2/S1_CLOSURE.md, section 2):
  E_0(f)^2 = ||f||_2^2 + (20/21) ||f||_H^2,  E_1(f)^2 = ||grad f||_2^2 + 16 E_0(f)^2,
  E_2(f)^2 = ||omega D^2 f||_2^2 + 2^14 E_1(f)^2
          = P2^2 + 2^14 G1^2 + 2^18 G0^2 + 2^18 (20/21) H^2,
  with the mandatory components P2 = ||omega D^2 f||_2, G1 = ||grad f||_2, G0 = ||f||_2, H = ||f||_H.
NORM-A2-Q3: Q3 = ||omega D^3 f||_2 (needed for the residual conversion).
NORM-A2-Ns18: N_s(f) = E_2(J^s f) at s = 2^-18 (Theorem D(b)). NORM-A2-Ns28: the same at s = 2^-28 (Theorem D(a)).
  Admissible certified bounds (A2-THEOREM): UB: N_s(f) <= E^(1 - s) (2 Q3^2 + 16410 E^2)^(s/2) + 34 s E with E = E_2(f);
  LB: N_s(f) >= (1 - 34 s) E_2(f) for s < 1/34 (any partial square sum of the components may replace E_2), and
  N_s(f) >= ||f||_inf, ||f||_(C^(1/2)) <= N_s(f).
NORM-A2-Nw (Theorem D_w, A2/S1_CLOSURE.md, section 7a): w = (1 + r^2/R^2)^(-11/10), omega_1 = <r>^(-1/5),
  P_1(g) = ||omega_1 D g||_2, P_2(g) = ||omega D^2 g||_2, L(g) = ||w g||_H, E^w(g)^2 = P_2^2 + 2^22 P_1^2 + 2^53 L^2,
  N^w_s(g) = E^w(J^s g). A numerical result must state R (2^31, 2^32 or 2^35) and s.
NORM-A2-LOG: the logarithmic norms of A2/S1_CLOSURE.md, section 11 and A2/S1_PROOFS.md P75 to P77; use only with an
  exact citation of the version.

Pointwise and Hoelder quantities (to be reported when available, labelled as above): ||F||_inf, weighted sups such as
sup <r>^k |D^j F|, and [D^j F]_(C^alpha). New norms requested by batch T are registered only through a
theory_vNN.md section "Norm registry" with ID NORM-T-<slug>-v<k>, which must give: the exact formula with every constant
and weight, the parity class, the Fourier convention if used, the mandatory components, the rigorous comparison
inequalities (if any) that numerics may use to produce LB/UB, and the theorem (framework ID) in which the norm is the
forcing norm. Numerics may only report a value for a norm ID that has been registered, citing theory_vNN.

Do not compare a residual measured in one norm ID with a threshold proved for another. If a conversion inequality
between two norms is used, cite it (A2-THEOREM or AUDITED) and report both numbers.

## 4. Framework IDs (theorems with thresholds)

Baseline frameworks (all A2-THEOREM):
- FW-A2-Db: Theorem D(b). Hypotheses (B0), (B0n), (B1) to (B5), (B7), (B9c), (B10m), (B10s); s = 2^-18, ball 2^-16,
  threshold N_s(F) <= 1/1572864 = 6.3578287760...e-7 (NORM-A2-Ns18).
- FW-A2-Da: Theorem D(a). s = 2^-28, threshold 2^-27/20 = 3.7252902984619140625e-10 (NORM-A2-Ns28), (B9) instead of (B9c).
- FW-A2-Dw1: Theorem D_w with sharper constants, s = 3 * 2^-31, ball 5 * 2^-32, threshold N^w_s(F) <= 2^-35 at
  R = 2^31, 2^32 or 2^35, hypotheses (W0), (Wn), (W1) (or its R = 2^32 / R = 2^31 forms, or the weaker matrix floor of P24),
  (W2), (W3), (Wm), (Ws).
- FW-A2-Dw2: second version of Theorem D_w (smooth commutator, P43), s = 3 * 2^-21, ball 5 * 2^-27, threshold
  N^w_s(F) <= 2^-30, same hypothesis list.
- FW-A2-LOGP: the parametric logarithmic theorem (A2/S1_CLOSURE.md, section 11 (vii); P105).
New frameworks: FW-T-<route>-<slug>-v<k> (route = TA, TB, TC, TD, TE or T4ALT), registered in a theory_vNN.md section
"Framework registry" with: domain, range and norm IDs; linear inverse status and constant; nonlinear constants;
admissible ball; threshold; complete hypothesis list with each hypothesis labelled by an ID FW-...:H<n>; status.

## 5. Candidate IDs, snapshots and hashes

ID format: C1-<lane>-<NNN>-<slug>, lane in {N1, N3, N4}, NNN a three-digit counter per lane, slug [a-z0-9-]{1,24}.
Example: C1-N1-001-s131-repro. An ID is immutable: corrected coefficients get a new ID with parent = old ID.

Baseline IDs (defined here, referring to read-only sources by path and SHA-256):
- C1-BASE-S131: C4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
  (7ff9415cbbe66f9d4a105aa4a999704e67157d8376c969b7561a1c01b1de57bc) and accepted_00000131.npz
  (e9cc69d7ccadcea661918ebe810836d62e19608aac38aa7000d136aeb9207c1c). The latest accepted state of case 4 according to
  C4/IPM_case4.artifacts/README.md; batch N must confirm in numerics_v01 that no newer accepted state exists.
- C1-BASE-S088: .../state088_handoff/accepted_00000088.json (30b1c9c4673e7de7fa6e52c5d7e0af3790e013c43c5f7456a5c4b8d2dcc67a42;
  the published JSON differs from its original bytes, see the case 4 README) and accepted_00000088.npz
  (81e7825571f72706982042d4b178b75a6101f4c1caeac31bbd4a66be0d681035).
- C1-A2-d2: A2/certificates/numerics_data/nb_d2_exact.json (f3339f85eff0ac81033a2a1f0fd07e12298ef9bd74da501a4e874c3cef6057e3).
- C1-A2-Mpen2: A2/certificates/P10_refit_inputs/nb_Mpen2_exact.json (07bb884b96121b22ca099c3b9d3451d19a65d6af684422b595b305e48d918e05).
- C1-A2-b6: A2/numerics/data/nb_b6_exact.json (8e6d05fe4f718b05336d1f68a81f58572afeb1ab65a631f61681687e1295f309).
- C1-A2-m10: A2/certificates/P10_refit_inputs/n12_m10_exact.json (7af0121b42f4da44d3faa8ef234fad61e723cc8ce4e09c15f11f4301201cb10c).
- C1-A2-TAILREP: the potential-level tail repair of state 131 at R = 2^1024 (A2/S1_CLOSURE.md, section 3; no file).

New candidate snapshot (written only by batch N lanes): directory SH/candidate_snapshots/<ID>/ with
- MANIFEST.json with keys: id, created_utc, created_by_lane, parent (ID or source path + sha256), chart (PRIMARY or
  EXP-<slug>), c_l_exact, theta0 (reference or exact data), a0 (value + status), B0n_status, basis (text description,
  generator count, branch list, radial and angular degrees), coefficient_files [{name, sha256, format, exactness}],
  evaluator_code [{path, sha256}] (path inside the creating lane), sector_table (file name + sha256),
  loss (value + definition, labelled LOSS), notes;
- the coefficient files themselves (exact rationals preferred; if binary64, say so) and the sector table;
- SHA256SUMS listing every other file in the directory.
Once SHA256SUMS is written the directory is never modified. Batch N keeps SH/candidate_snapshots/INDEX.md (append-only,
one line per ID: ID, UTC, lane, parent, chart, one-line description, sha256 of MANIFEST.json).

## 6. Versioned exchange files

SH/theory_requirements/theory_vNN.md (NN = 01, 02, ...; written only by the T1/T3 theory worker after consulting the T2 theory worker and the T4 theory auditor).
Header block: version, UTC time, author, consulted lanes and the exact files consulted, supersedes, framework IDs and
norm IDs defined or used, candidate IDs referred to, and "Response to numerics_vMM" (what was changed because of which
numerical finding; "none" must be justified). Required sections (prompt section 12): Norm registry; Framework registry;
residual regularity and decay requirements; necessary far-field cancellation conditions; inverse and nonlinear
constants (with status labels); admissible residual threshold; matrix positivity and background conditions (each
with an ID, an exact pointwise statement, and the region); numerical quantities whose reduction would most improve
closure (ranked, with the expected effect on the closure ratio).

SH/numerical_results/numerics_vNN.md (written only by the N1/N2 numerics worker after consulting the N3 numerics worker and the N4 numerical auditor).
Header block: version, UTC time, author, consulted lanes and files, supersedes, candidate IDs, norm IDs and the
theory_vMM version they follow, and "Response to theory_vMM". Required sections (prompt section 12): source checkpoint
and candidate ID; basis and coefficient-file path; normalization status; far-field sector table status; a residual
table with columns
  candidate ID | norm ID | component | value | label (LOSS/FLOAT/BOX-LB/BOX-UB/LB/UB/VALIDATED/EXACT) |
  audit (CONFIRMED-N4 + entry / PENDING-N4) | method and precision | reproduction command;
locations and scales dominating the residual; background hypotheses table with columns
  candidate ID | hypothesis ID (B1, W2, FW-...:H3, ...) | region | margin | label | audit;
next proposed numerical improvement.

Audit records: The T4 theory auditor and the N4 numerical auditor each keep one append-only audit file in their own lane (the N4 numerical auditor uses verdict ledger;
The T4 theory auditor names its file in its status file, default AUDITS.md), one entry per
audited item: AUDIT-ID (T4-NNN or N4-NNN), UTC, target (file path + sha256 + claim label or number), verdict
(CONFIRMED / REFUTED / INCOMPLETE / IN-PROGRESS), what was independently redone (proof read line by line,
independent code, other precision), evidence path.

## 7. Closure matrix

SH/closure_matrix.md, written only by the coordinator, one row per (framework ID, candidate ID) pair with: residual in forcing
space; all background hypotheses hold; residual LB; residual UB; threshold; ratio (UB/threshold for closure,
LB/threshold for exclusion); missing proof or certification; status PROVED (every hypothesis AUDITED/A2-THEOREM and
every number CONFIRMED-N4) / CONDITIONAL / NUMERICAL ONLY / RULED OUT / OPEN. RULED OUT is used only when an
A2-THEOREM or AUDITED result excludes the pair within its exact assumptions (for example LB > threshold, or a
certified hypothesis violation). Earlier versions are kept in working file . (not published)

## 8. Timeline, checkpoints and feedback rule

Checkpoints (UTC): H2 = 2026-10-28T22:30Z (baseline: numerics_v01 and theory_v01 expected by then or shortly after),
H8 = 2026-10-29T04:30Z, H12 = 2026-10-29T08:30Z, H16 = 12:30Z, H18 = 14:30Z, freeze H22 = 18:30Z, team stop H23 = 19:30Z.
THEORY_FINAL.md (the T1/T3 theory worker lane) and NUMERICS_FINAL.md (the N1/N2 numerics worker lane): first drafts by H12, kept current, final by 19:00Z.
Feedback rule: within one hour of a theory_vNN publication, batch N records an acknowledgement and its planned reaction
(in the next numerics_vMM or, if none is due, a dated line in its status log (not published) headed "ACK theory_vNN"); the same
for batch T after each numerics_vMM ("ACK numerics_vMM" in its status log (not published)). The coordinator checks and records the
acknowledgements in team notes.

## 9. Resources

Cores (taskset, low priority): The coordinator, the T1/T3 theory worker, the T2 theory worker, the T4 theory auditor share cores 50 and 51; the N1/N2 numerics worker 52 to 54; the N3 numerics worker 55 and 56;
The N4 numerical auditor 57. Each lane runs at most the number of busy computations its own instructions allow. The four lanes on cores
50 and 51 should keep heavy certification runs short and announce any run over 30 minutes in their status file.
The coordinator runs no heavy computation. Memory under 48 GB per lane, disk under 3 GB per lane. Read-only sources: copy
before executing; set PYTHONDONTWRITEBYTECODE=1 or run python -B when importing copied code.

## Amendment v02 (2026-10-28T20:44Z)

Source: an the second model cross-check of v01 against A2/S1_CLOSURE.md and exact_constants_131.json (working file contract-check (not published)/
answer.md), every point rechecked by the coordinator against S1_CLOSURE.md lines 45 to 101, 285 to 296, 350 to 474. No ID
changes meaning. Items 1 and 2 correct v01 transcription errors.

1. Fourier convention (section 1), correction: with hat f(xi) = int f e^(-i X.xi) dX one has hat(d_j f) = i xi_j hat f,
   so R_j = d_j (-Delta)^(-1/2) has symbol +i xi_j/|xi| (v01 wrote -i xi_j/|xi|). The velocity symbols in v01 are
   correct and unchanged: U_1 = -R_1 R_2 has symbol xi_1 xi_2/|xi|^2, U_2 = R_1^2 has symbol -xi_1^2/|xi|^2.
2. FW-A2-Da (section 4), completion: ball radius r = 2^-27 (not 2^-16), eta = r/20 = 2^-27/20 (S1_CLOSURE.md line 289).
   Parameter table of the baseline frameworks:
   | framework | s | ball r | threshold eta |
   |---|---|---|---|
   | FW-A2-Db | 2^-18 | 2^-16 | r/24 = 1/1572864 |
   | FW-A2-Da | 2^-28 | 2^-27 | r/20 = 2^-27/20 |
   | FW-A2-Dw1 | 3 * 2^-31 | 5 * 2^-32 | 2^-35 |
   | FW-A2-Dw2 | 3 * 2^-21 | 5 * 2^-27 | 2^-30 |
3. Ball constraint: every baseline framework's solution ball is {N(h) <= r, c[h] = 0}; the constraint c[h] = 0 is part
   of the framework and must be part of every new framework registry entry (or its replacement stated).
4. Radius-dependent (W1) bounds of FW-A2-Dw1 (S1_CLOSURE.md lines 350 to 474). A numerical (W1) check must name the
   radius and use the matching list (bounds on sup r^d (|D rho| + r |D^2 rho|), sup r^(d-1) |u|, sup r^d |Du|,
   sup r^(1+d) |D^2 u|):
   - R = 2^35: d = 2/5, bounds (152, 18, 18, 45);
   - R = 2^32: d = 4/9 (needs 4/9 < 1 - gamma), bounds (190, 23, 23, 56);
   - R = 2^31: d = 4/9, bounds (186, 22, 22, 56). The weaker matrix floor of P24 (M >= (5/2) I on r <= R, or the
     position-dependent floor) is proved only at R = 2^31.
5. Norm details:
   - ||f||_(C^(1/2)) means supremum plus seminorm (S1_CLOSURE.md line 80).
   - Tensor bounds in (B1) to (B7) are Frobenius suprema; in (B9) and (B9c), ||T||_S is the sum over ordered indices of
     the component suprema. Report which one a number is.
   - In the lower bound N_s(f) >= (1 - 34 s) E_2(f), "partial square sum" means the square root of any partial sum of
     the weighted squares P2^2, 2^14 G1^2, 2^18 G0^2, 2^18 (20/21) H^2, with the coefficients retained.
6. Exact equalities. (B0n) and the vanishing of a sector are equalities: an enclosure containing zero proves neither.
   Sector status values are EXACT-ZERO, ENCLOSED-NONZERO (enclosure excludes zero), INCONCLUSIVE (enclosure contains
   zero, not exact), FLOAT. (B0n) status is EXACT or INCONCLUSIVE (with the enclosure); only EXACT counts for a
   PRIMARY-chart closure row.
7. C1-A2-TAILREP is a theoretical object (S1_CLOSURE.md section 3 uses "a fixed smooth radial cutoff eta_R" without a
   formula). Any numerical tail-repair candidate must state its cutoff function exactly in its MANIFEST.json.
8. Strain domain: the formula c[h] = -h_y(0)/4 + (1/pi) PV int sin(3 theta) h r^-3 dX is proved for h in C^(1,a) near 0
   with sublinear growth (S1_CLOSURE.md line 48). On N_s it applies because N_s embeds in H^(2+s) and C^(1/2) control is
   available; on weaker spaces (E_2 at s = 0, H, L^2) the trace formula must be justified by the theory file that uses it.

## Amendment v03 (2026-10-28T21:05Z): independence of audits

Reason: The T4 theory auditor verdict ledger entries T4-004 to T4-009 mark CONFIRMED proofs written by the T4 theory auditor itself ("author
self-audit"). Prompt section 16 forbids presenting a check as independent when it is not.
1. Theory. A CONFIRMED verdict of the T4 theory auditor on a proof written by the T4 theory auditor is a self-audit. Such a result is labelled
   CLAIMED (the T4 theory auditor self-audit) in shared files and reports. It becomes AUDITED when the T1/T3 theory worker or the T2 theory worker records an
   independent review in its own lane (file path, sha256 of the reviewed PROOF.md, verdict CONFIRMED / REFUTED /
   INCOMPLETE, the steps redone) and the T4 theory auditor or theory_vNN cites it. The same rule applies to counterexamples: a
   the T4 theory auditor REFUTED verdict that rests on a the T4 theory auditor counterexample is a CLAIMED refutation until reviewed. Proofs written by
   the T1/T3 theory worker or the T2 theory worker and confirmed by the T4 theory auditor are AUDITED as before.
2. Numerics. CONFIRMED-N4 requires that the N4 numerical auditor reproduced a number claimed by another lane or by an archived source
   with its own code path. A number first produced by the N4 numerical auditor (no prior claim to reproduce) carries its rigorous label
   (LB, UB, VALIDATED, EXACT) with the suffix N4-ORIGIN, and becomes CONFIRMED when the N3 numerics worker or the N1/N2 numerics worker reproduces it
   independently, or when the T4 theory auditor checks the underlying proof and the N4 numerical auditor's computation is the evidence (state which).
3. A row of the closure matrix is RULED OUT only through an A2-THEOREM or AUDITED obstruction together with
   CONFIRMED numbers. A pair excluded only by a CLAIMED obstruction is listed as OPEN with the note "excluded if
   <ID> is audited".

## Amendment v04 (2026-10-28T21:34Z): who may remove the N4-ORIGIN suffix

Decision on the question raised in the T4 theory auditor team note 13 and the N4 numerical auditor verdict ledger (supplement 21:29Z): Amendment v03 item 2
is widened. A number first produced by the N4 numerical auditor becomes CONFIRMED when any other lane (the N1/N2 numerics worker, the N3 numerics worker, or the T4 theory auditor) reproduces
it with its own code path (different implementation of the derivative, integration or postprocessing step that the
number depends on) and records the comparison with hashes. Shared exact inputs that are themselves already CONFIRMED
(for example the canonical coefficient conversion) may be reused. Accordingly N4-018 is CONFIRMED by T4-018 (state 131
background seminorms) and N4-022 is CONFIRMED by T4-021 (point gaps for the FW-T-TB-rebal-v1 ball and T4's graded box).
The same rule applies symmetrically: a number first produced by the T4 theory auditor code is confirmed by an independent the N4 numerical auditor (or
The N3 numerics worker, the N1/N2 numerics worker) reproduction.

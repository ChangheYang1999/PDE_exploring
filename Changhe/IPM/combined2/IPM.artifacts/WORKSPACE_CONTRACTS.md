# c2 shared contracts (coordinator the coordinator)

Version: WORKSPACE_CONTRACTS.md v01, written 2026-11-02 between 18:06Z and 18:20Z (run start T0 = 2026-11-02T18:05:30Z).
Changes are made only by appending an "Amendment vNN" section at the end of this file with its UTC time. An amendment
never changes the meaning of an ID already in use; it adds IDs or corrects a transcription with a dated note.

Path convention in every file that may be published: paths are relative to the combined2 root, the directory that holds
the agents `c2-*`, the exchange directory `exchange/` and the read-only sources `source/`. Examples:
`JOINT_CLOSURE_LEDGER.md`, `source/IPM/combined1/combined1.report.md`, `source/c1_full/combined1_theory_agent_2/notes/...`.
Never write an absolute local path into a report, manifest, ledger or evidence log.

Abbreviations: C1 = `source/IPM/combined1`, C1A = `C1/combined1.artifacts`, C1F = `source/c1_full`,
A2 = `source/IPM/analysis2/IPM_Analysis_II.artifacts`, A4 = `source/IPM/analysis4`, HOL = `source/IPM/Holder`,
SH = `the exchange`.

## 0. Team registry (registered 2026-11-02T18:20Z)

| agent | role | publishes | owns |
|---|---|---|---|
| The coordinator | coordinator (sections 19, 20 of the prompt) | SH/JOINT_CLOSURE_LEDGER.md | WORKSPACE_CONTRACTS.md, team notes, MIDCAMPAIGN_REPORT.md, FINAL_REPORT.md (= COORDINATOR_FINAL_REPORT.md), final bundle |
| The first theory agent | theory: O1 (k = 0 lifting), parameter optimization (section 14); theory publisher | SH/theory_requirements/theory_vNN.md | THEORY_NEW_RESULTS.md, EXISTING_PROOFS_REFERENCE.md |
| The second theory agent | theory: O2 (uniform small-k lifting), O3 (invariant ball) | through the first theory agent | proof files in its agent |
| The first numerics agent | numerics: N1 (existing basis, min ||F||_2^2 with exact constraints), background screening; numerics publisher | SH/numerical_results/numerics_vNN.md, SH/candidate_snapshots/ | NUMERICAL_OPTIMIZATION.md |
| The second numerics agent | numerics: N2 (basis expansion), S_F evaluator (section 18) | through the first numerics agent | evaluator code and candidate files in its agent |
| The theory auditor | independent theory auditor | its AUDIT_LEDGER.md | verdicts on theory claims |
| The numerical auditor | independent numerical auditor | its AUDIT_LEDGER.md | verdicts on numbers and certificates |

Each agent writes only in its own directory; the exchange directory has the fixed writers listed above.

## 1. Status vocabulary (mandatory in every shared file)

Theory statements:
- IMPORTED: an established result of Part II of the prompt (R1 to R11), used within exactly the hypotheses stated
  there. EXISTING_PROOFS_REFERENCE.md (the first theory agent) gives for each R its authoritative source file and line numbers, or the
  note "no detailed source located; the prompt's Part II statement is the reference". Do not re-prove. A use outside
  the stated hypotheses is not IMPORTED: it is a new claim.
- HISTORICAL: a theorem or certificate of an earlier campaign (combined1, Analysis II, Analysis IV, Hoelder report)
  with its original audit ID (for example "combined1 theory audit 162"). Usable as a reference statement; when a
  HISTORICAL numerical certificate is used as a hypothesis of the final theorem it must be re-verified in this
  workspace (it then becomes CONFIRMED-AN).
- PROVED: a new result of this campaign whose complete written proof and constants the theory auditor has marked CONFIRMED (cite
  the AT entry). Only PROVED, IMPORTED and HISTORICAL theorems may be called proved in any report.
- CLAIMED: a complete written proof exists in the author's agent; audit pending.
- CONDITIONAL: proved (or claimed) under named hypotheses that are not yet verified; list each by its hypothesis ID.
- HEURISTIC: derivation with gaps, scaling argument or numerical indication; never a hypothesis of a claim.
- OPEN, REFUTED (cite the counterexample or error).

Numerical quantities:
- LOSS: an optimizer objective. Never a norm.
- FLOAT: floating-point value; state the rule, grid or quadrature, truncation radius, far-field treatment, precision.
  Never a bound.
- BOX-LB / BOX-UB: rigorous bound on a bounded region only (name the region).
- LB / UB: rigorous bound on the complete whole-plane quantity (interval or ball arithmetic, exact identities, a proved
  exterior bound). VALIDATED: rigorous two-sided enclosure [LB, UB]. EXACT: exact rational or algebraic identity.
- Audit suffix: CONFIRMED-AN (the numerical auditor reproduced it with its own code path; cite the AN entry) or PENDING-AN. Only
  CONFIRMED-AN numbers may be called certified. A number first produced by the numerical auditor carries the suffix AN-ORIGIN and
  becomes CONFIRMED when a numerics agent reproduces it with its own code path (or the theory auditor checks the underlying proof
  and the numerical auditor computation is the evidence; say which).
- An enclosure containing zero proves no equality. Exact equalities (normalization, vanishing sectors) need EXACT.

Audit records: the theory auditor and the numerical auditor each keep AUDIT_LEDGER.md in their agent, newest entry last, one entry per item:
ID (AT-NNN or AN-NNN), UTC date, claim and target (relative path + sha256 + label or number), method (what was
independently redone), result, verdict CONFIRMED / REFUTED / OPEN. A self-audit (the auditor confirming its own
derivation) is labelled as such and is not an independent confirmation.

## 2. Equation, parity and conventions

- Stationary equation: (c_l X + U[rho]).grad rho - rho = 0 on R^2, X = (x, y), r = |X|.
- U[f] = (-R_1 R_2 f, R_1^2 f), R_j = d_j (-Delta)^(-1/2), div U[f] = 0. Fourier convention (only where Fourier
  formulas are used): hat f(xi) = int f(X) e^(-i X.xi) dX, hat(d_j f) = i xi_j hat f, R_j has symbol +i xi_j/|xi|
  (combined1 WORKSPACE_CONTRACTS.md Amendment v02 correction), U_1 has symbol xi_1 xi_2/|xi|^2, U_2 has symbol -xi_1^2/|xi|^2
  (the prompt's m(xi)). Plancherel: ||f||_2^2 = (2 pi)^(-2) ||hat f||_2^2.
- For the growing background the velocity is defined from the potential: rho_bar = -d_y Delta chi,
  u_bar = (-chi_xyy, chi_xxy) (prompt section 15).
- Parity class S1: even in x, odd in y. Function spaces are closures of the smooth compactly supported S1 functions.
- Strain functional: ell(h) = d_y U_2[h](0) = -h_y(0)/4 + (1/pi) PV int sin(3 theta) h(X) r^(-3) dX (A2/S1_CLOSURE.md
  line 49; valid for h in C^(1,a) near 0 with sublinear growth). The local term -h_y(0)/4 is part of the definition.
- Linearization: L h = V.grad h - h + U[h].grad rho_bar, V = c_l X + u_bar; A_k = L + U[k].grad, W_k = V + U[k];
  correction equation L h + U[h].grad h = -F, F = V.grad rho_bar - rho_bar.
- Normalization (B0n): c_l + ell(rho_bar) = 1, equivalently DV(0) = diag(b, 1). Since V(0) = 0, rho_bar_x(0) = 0 and
  d_y V_1(0) = 0 by S1, one has F_y(0) = (c_l + ell(rho_bar) - 1) a_0, so the compatibility F_y(0) = 0 is equivalent to
  (B0n) when a_0 != 0 (coordinator remark; the first theory agent to confirm in EXISTING_PROOFS_REFERENCE.md).
- Solution class of the target theorem: h in K_{R,M} (prompt R5.1): S1, ell(h) = 0, ||h||_2 <= R, H_{sigma,alpha}(h) <= M.

## 3. Fixed constants and the notation table

- c_l = 4076476460239181/2251799813685248 = 4076476460239181/2^51 exactly (the string "c_l_exact" of Candidate 007's
  MANIFEST.json; also state 131 of case 4). c_l = 1.8103192101999980... Never varied in this campaign.
- b = 2 c_l - 1 = 2.6206384204, d = b - 1 = 2 c_l - 2 = 1.6206384204, (b + 3)/2 = 2.8103192102.
- a_0 = d_y rho_bar(0) > 0 (Candidate 007: FLOAT 10.31200 in its MANIFEST notes; exact rational to be published by
  the first numerics agent in numerics_v01 and confirmed by the numerical auditor).

Symbols that the prompt uses with two meanings. In every shared file use the left column:

| symbol here | meaning | prompt location | value at c_l |
|---|---|---|---|
| gamma_b = 1/c_l | basis exponent | section 15 ("gamma") | 0.5523887690 |
| delta_b = 1 - 1/c_l | basis exponent step | section 15 ("delta") | 0.4476112310 |
| gamma_9 = 1 - 1/c_l | far-field decay exponent of D u_bar, grad rho_bar | R9 ("gamma") | 0.4476112310 (= delta_b) |
| delta | Hoelder excess of the source space C^(1+alpha+delta) | sections 13, 14, 18, R6 | parameter |
| kappa | nonlocal part of the signed L^2 bound (R1) | R1 | 007: HISTORICAL kappa_HS = 0.72816468 |
| kappa_ang = alpha/(b - 1) = alpha/(2 c_l - 2) | frozen angular loss | R6, R7 | 0.3085 at alpha = 1/2 |
| R = ||F||_2/beta_0 | L^2 radius of K_{R,M} | R5 | |
| R_ext | exterior radius of R9 | R9 ("R") | |
| M | weighted Hoelder radius of K_{R,M} | R5 | |
| nu | weight exponent of the frozen source norm (R6.4) | R6 | 7/4 initially |

## 4. Norms (registered norm IDs)

Basic conventions: ||f||_2^2 = int_(R^2) |f|^2 dX over the full plane, no normalizing factor (a value on a quarter
plane or half circle must be labelled; for an S1 function the full-plane square is 4 times the quarter-plane square).
|v| is the Euclidean norm of a vector; for derivative tensors |D^j f|^2 = sum over ordered index tuples (Frobenius),
so |D^2 f|^2 = f_xx^2 + 2 f_xy^2 + f_yy^2. ||g||_inf is the supremum over R^2 unless a region is named.
w_sigma(X) = <X>^sigma = (1 + |X|^2)^(sigma/2).

- NORM-HOL: for 0 < beta < 1, [g]_(C^beta(Omega)) = sup over x != y in Omega of |g(x) - g(y)|/|x - y|^beta (Euclidean
  norm of the difference for vector or tensor g); Omega = R^2 unless named. For an integer k >= 0 and 0 < beta < 1,
  ||g||_(C^(k,beta)) = sum_{j=0..k} ||D^j g||_inf + [D^k g]_(C^beta). For a noninteger s = k + beta,
  C^s = C^(k,beta). An integer total order (alpha + delta = 1) is not allowed without a separate registration.
- NORM-H (default solution norm, product form): H_{sigma,alpha}(f) = ||w_sigma f||_(C^(1,alpha)(R^2)).
  The localized variant NORM-H-LOC: H^loc_{sigma,alpha}(f) = sup_X w_sigma(X) ||f||_(C^(1,alpha)(B_1(X))) may be
  used by a theorem only with an explicit two-sided conversion to NORM-H (constants stated) or if the whole closure
  is done in NORM-H-LOC; the ledger records which norm each theorem uses.
- NORM-SF (strong residual norm, prompt section 18): S_F(alpha, delta, sigma) = ||w_sigma F||_(C^(1+alpha+delta)(R^2)).
  For 1 + alpha + delta < 2 this is ||g||_inf + ||grad g||_inf + [grad g]_(C^(alpha+delta)) with g = w_sigma F; for
  2 < 1 + alpha + delta < 3 it is ||g||_inf + ||grad g||_inf + ||D^2 g||_inf + [D^2 g]_(C^(alpha+delta-1)).
  Every reported value states (alpha, delta, sigma) and gives the components separately:
  S0 = ||g||_inf, S1 = ||grad g||_inf, S2 = ||D^2 g||_inf (always, even when not part of the norm), S3 = ||D^3 g||_inf
  when available, and the top seminorm Stop with its method. A grid maximum of a difference quotient is FLOAT only;
  a rigorous upper bound may use, for Lipschitz G on R^2 and 0 < beta < 1,
  [G]_(C^beta) <= (2 ||G||_inf)^(1-beta) ||DG||_inf^beta (with G = grad g or D^2 g), with the whole-plane suprema
  certified including the far field.
- NORM-L2: G0 = ||F||_2. Also report G1 = ||grad F||_2 and ||F||_inf when cheap (historical comparability).
- New norms are registered only in a theory_vNN.md section "Norm registry" with ID NORM-T-<slug>-v<k>: exact formula,
  every constant and weight, region, mandatory components, and the theorem (framework ID) that uses it. Numerics
  report values only for registered norm IDs. Never compare a value in one norm ID with a threshold in another without
  a cited conversion inequality.

## 5. Theorem frameworks and hypothesis IDs

- The target theorem is the conditional fixed point R5 (IMPORTED) with its invariance hypothesis (R5.3) supplied by
  new estimates (O1 to O3). Every theorem statement used for closure is registered in a theory_vNN.md section
  "Framework registry" with ID FW-C2-<slug>-v<k>: spaces (domain, range, norm IDs), parameter values or ranges
  (alpha, delta, sigma, nu, radii), every hypothesis with an ID FW-C2-<slug>-v<k>:H<n> and its exact inequality,
  the constants with status labels, the resulting threshold(s), and its status (PROVED, CLAIMED, CONDITIONAL, ...).
- Background hypotheses (inequalities on rho_bar, u_bar, V, the flow, beta_0) get IDs BG-<n> in a theory_vNN.md
  section "Hypothesis registry", with the exact pointwise statement, the region, and which framework uses them.
  These are the rows that numerics_agent_1/the second numerics agent screen (FLOAT) and the numerical auditor certifies.
- A closure ratio G = eps_theory/||F||_2 (prompt section 20) is computed in the ledger only from a threshold of a
  PROVED framework (or, labelled as such, CLAIMED or CONDITIONAL, never "definitive"). Where the threshold is a
  region in (||F||_2, S_F) or depends on several norms, the ledger records the tradeoff curve, not a single ratio.

## 6. Candidate IDs, snapshots and hashes

- C2-REF-007: the authoritative Candidate 007 = C1A/candidates/C1-N1-007-d2w-j7-e2bal/, coefficient file
  d2w_j7_n4_E2bal_mid180_exact.json, sha256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21
  (MANIFEST.json 977ed6ad5f78b87f135df441fea337cf0866bbf746bcf1f29d81734ea427f98b, sector_table.json
  9d54471429323126d6270de5779ef6566f6753a1ce943bee65073be75b68f42a; hashes verified by the coordinator 2026-11-02T18:09Z).
  Its exact rational coefficients are the reference; the binary64 rounding is not (combined1: rounding reintroduces
  far-field sector (1,0)). It is never modified or replaced as "Candidate 007".
- New candidates: C2-<agent>-<NNN>-<slug>, agent in {N1, N2}, NNN a three-digit counter per agent, slug [a-z0-9-]{1,24}.
  The first numerics agent publishes all snapshots (an N2 candidate keeps its N2 ID and created_by_lane the second numerics agent). An ID is immutable: a
  corrected candidate is a new ID with parent = old ID.
- Snapshot directory SH/candidate_snapshots/<ID>/ containing MANIFEST.json, the exact coefficient file(s), the sector
  table, and SHA256SUMS listing every other file. Once SHA256SUMS is written the directory is never modified.
  MANIFEST.json keys: id, created_utc, created_by_lane, parent (ID + sha256), c_l_exact (must equal the string above;
  otherwise the candidate is out of scope), basis (description, generator count, branches, angular and radial
  degrees), constraints (number of exact rows and what they enforce), coefficient_files [{name, sha256, format,
  exactness}], evaluator_code [{relative path, sha256}], B0n_status (EXACT or INCONCLUSIVE), a0 (exact or enclosure),
  sector_table (file + sha256; first surviving sector exponent and its full-circle angular norm), loss (value +
  definition, label LOSS), G0 = ||F||_2 (value + label + audit), background screen (theta, kappa, beta_0 with labels),
  S_F (parameters, components, labels), notes.
- Admissibility rule (default until a theory_vNN registers a different one): a candidate is eligible for the ledger
  only if c_l is exactly c_l(007), (B0n) is EXACT, and every far-field sector that vanishes exactly for 007 vanishes
  exactly (EXACT-ZERO) for it, so that F decays at least like r^e with the first surviving exponent e <= -2.79.
  The binding requirement of the C^(1,alpha) framework is: every surviving sector exponent e satisfies e < -sigma
  (finiteness of S_F) and e < -1 (F in L^2); theory_vNN states the exact rule for the chosen sigma.
- SH/candidate_snapshots/INDEX.md (written by the first numerics agent, append-only): one line per ID with UTC, agent, parent, one-line
  description, sha256 of MANIFEST.json.

## 7. Versioned exchange files

SH/theory_requirements/theory_vNN.md (NN = 01, 02, ...; written only by the first theory agent after consulting the second theory agent and the theory auditor).
Header: version, UTC, author, agents and files consulted, supersedes, framework, hypothesis and norm IDs, candidate
IDs, "Response to numerics_vMM" (what changed because of which numerical finding). Required sections, in this order
(prompt section 19 theory items and section 14):
  T1 strongest theorem proved (statement with spaces and constants, status label, AT entry);
  T2 remaining analytical lemma(s) (exact statement of what is missing);
  T3 current admissible residual threshold (||F||_2 and S_F, or the tradeoff region; label);
  T4 optimized theoretical parameters (alpha, delta, sigma, nu, radii) and the constraints used, including
     delta > alpha/(2 c_l - 2), a_0 > b(1 + alpha) - 1, the weighted margin of R9;
  T5 background constants required (Hypothesis registry, BG-n, exact inequalities and regions);
  T6 sensitivity of closure to each norm and constant; which candidate changes would help (ranked);
  Norm registry; Framework registry.

SH/numerical_results/numerics_vNN.md (written only by the first numerics agent after consulting the second numerics agent and the numerical auditor).
Header: version, UTC, author, agents and files consulted, supersedes, candidate IDs, norm IDs and the theory_vMM it
follows, "Response to theory_vMM". Required sections (prompt section 19 numerics items):
  N1 best ||F||_2 (candidate ID, value, label, audit);
  N2 best strong residual norm S_F (parameters, components, label, audit);
  N3 Pareto candidates (table: ID, G0, S_F, beta_0 screen, first surviving sector, basis size);
  N4 basis size and objective changes;
  N5 conditioning and optimization bottlenecks;
  N6 failed structural constraints (sectors, B0n, (B-L2), any BG-n);
  N7 background certification status (table: candidate | BG-n | region | value or margin | label | audit);
  plus a residual table: candidate | norm ID | component | value | label | audit | method and precision | command.

Feedback rule: within one hour of a theory_vNN publication the first numerics agent records "ACK theory_vNN" with the planned reaction in
its status file (or the next numerics file); the same for the first theory agent after each numerics_vMM ("ACK numerics_vMM").
Each team publishes at least once per exchange cycle (section 9).

## 8. Joint closure ledger (prompt section 20)

SH/JOINT_CLOSURE_LEDGER.md is written only by the coordinator; earlier versions are kept in coordinator/ledger_history/.
Layout:
  (a) Verdict line: whether a complete existence theorem is certified (YES/NO) and the first failing inequality.
  (b) Constants block: c_l, a_0, b, beta_0 (with theta, kappa), ||F||_2, S_F, alpha, delta, sigma, nu, R, M and every
      other binding background or inverse constant; each with value, label, audit, source.
  (c) Condition table, one row per theorem condition of the strongest registered framework (and of any alternative
      framework still alive): ID | exact inequality | proven analytical threshold (framework, status) | current
      numerical value or enclosure (candidate, label, audit) | certified? | margin | sensitivity to theory
      parameters | team that can improve it.
  (d) Closure ratio G = eps_theory/||F||_2 only when the threshold comes from a PROVED framework; otherwise "not
      computed" with the reason.
  (e) Candidate table (C2-REF-007 and every snapshot): G0, S_F, beta_0, admissibility.
  (f) Changes since the previous version.

## 9. Timeline (UTC), exchange cycles and deliverables

Exchange cycle times X_n = T0 + 4n hours: X1 2026-11-02T22:05Z, X2 11-03T02:05Z, X3 06:05Z, X4 10:05Z, X5 14:05Z,
X6 18:05Z, X7 22:05Z, X8 11-04T02:05Z, X9 06:05Z, X10 10:05Z, X11 14:05Z. Each publisher posts a new version before
each X_n; the coordinator updates the ledger and team notes within about 45 minutes after X_n.
- By X1: EXISTING_PROOFS_REFERENCE.md first version; theory_v01 (framework skeleton, hypothesis registry, parameter
  constraints, quantities needed from numerics); numerics_v01 (007 confirmed by hash, ||F||_2 reproduced from exact
  coefficients, exact a_0 and (B0n), sector table, historical certificate list, first S_F FLOAT plan).
- H12 to H24 (2026-11-03T06:05Z to 18:05Z): coordinator mid-campaign report MIDCAMPAIGN_REPORT.md, written
  between X4 and X5 (target 2026-11-03T12:05Z).
- X11 = 2026-11-04T14:05Z: no new major routes; targeted audits only.
- 2026-11-04T15:35Z: final versions of THEORY_NEW_RESULTS.md, EXISTING_PROOFS_REFERENCE.md (the first theory agent),
  NUMERICAL_OPTIMIZATION.md (the first numerics agent), final theory_vNN and numerics_vNN; auditors' last verdicts by 16:50Z.
- 2026-11-04T17:05:30Z: team stop. The coordinator finalizes FINAL_REPORT.md and the final ledger within the following hour.

## 10. Resources

Cores (taskset, low priority): the coordinator, the first theory agent, the second theory agent and the theory auditor share cores 40 and 41 (at most one busy computation
per agent; announce any run over 30 minutes in status file); the first numerics agent 42 to 45 (up to 4), the second numerics agent 46 to 49 (up to 4),
the numerical auditor 50 (one). The coordinator runs no heavy computation. Read-only sources: copy before executing; run python with -B or
PYTHONDONTWRITEBYTECODE=1 when importing copied code. Keep agent disk use within the per-agent limit.

## Amendment v02 (2026-11-02T18:17Z)

The v01 text above is frozen in coordinator/contracts_history/CONTRACTS_v01.md (sha256 7272fe697f670818...). Current
version: v02 = v01 plus this amendment. Triggered by the theory audit exchange audit_v04 (AT-004, AT-005, AT-006).

A2.1 Times (correction). The times "18:20Z" in the v01 header and in the section 0 heading were planned times written
before the clock was read. The v01 file was last written at 2026-11-02T18:13:12Z (file modification time); the
registry and all v01 definitions are in force from that time.

A2.2 Function spaces (replaces the sentence "Function spaces are closures of the smooth compactly supported S1
functions" in section 2; AT-006, theory_audit/research/function_space_contract/PROOF.md).
- L2_S1 = the S1 subspace of L^2(R^2) (equivalently, the L^2 closure of the smooth compactly supported S1 functions).
- The solution space of R5 is the full weighted Hoelder space: the S1 functions f in L^2 with f in C^(1,alpha)_loc and
  H_{sigma,alpha}(f) < infinity, with K_{R,M} defined inside it exactly as in R5.1. No closure in the Hoelder norm is
  taken: such a closure is a strictly smaller space whose bounded sets need not be closed in L^2 (AT-006).
- A smooth core or operator domain (for example the common core of the energy identity in R1) is named separately by
  the theorem that uses it, with its topology (graph norm).

A2.3 Strong-norm membership (AT-004, CONFIRMED by the theory auditor, conditional on AN-001, which the numerical auditor CONFIRMED). For F given
by a finite potential expansion whose first surviving far-field sector has exponent e and a nonzero coefficient,
||w_sigma F||_(C^s) < infinity for noninteger s > 0 (inhomogeneous global norm) if and only if sigma <= -e. For
C2-REF-007, e = 4/c_l - 5 and the ceiling is sigma <= 5 - 4/c_l = 11375183046454913/4076476460239181 = 2.790444924...
In section 6 the condition "e < -sigma" is replaced by "e <= -sigma"; F in L^2 still requires e < -1. Finiteness is
qualitative only; any threshold that depends on the size of S_F needs a numerical upper bound.

A2.4 The origin identity of section 2, F_y(0) = (c_l + ell(rho_bar) - 1) a_0, is CONFIRMED by the theory auditor as AT-005
(theory_audit/research/origin_compatibility_audit/PROOF.md). It is a statement about rho_bar and F only, not about an L^2
correction.

A2.5 Registry addition. The theory auditor and the numerical auditor publish immutable exchange notes in their own agents,
theory_audit/exchange/audit_vNN.md and numerical_audit/exchange/audit_vNN.md, with verdicts in their AUDIT_LEDGER.md. The publishers
the first theory agent and the first numerics agent read the newest of these before each theory_vNN or numerics_vNN.

A2.6 Resources (section 10 addition). The first numerics agent has GPU 0 and cores 42 to 45; the second numerics agent has GPU 1 and cores 46 to 49, as in
their agent files. The numerical auditor uses core 50.

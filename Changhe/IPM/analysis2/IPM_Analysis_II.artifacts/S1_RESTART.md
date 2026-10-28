# S1 restart and reproduction instructions

Final version of 2026-10-28T17:48Z (end of the run). This file explains how to reproduce every certified number of the report from the
accompanying artifacts, which differences between a rerun and the shipped files are expected, and how to continue the
research. Certified numbers and their files are listed in S1_NUMERICAL_CERTIFICATES.md; proofs are in S1_PROOFS.md;
the closure conditions and margins are in S1_CLOSURE.md.

## 1. Contents of the artifacts

Published folder. The reproduction runs of section 9 used the complete certificate packet of 697 files (about
491 MB), listed with sizes and SHA-256 hashes in certificates/MANIFEST_FULL.txt. To stay under 50 MB, the published
folder keeps every program and every input below 1 MB, plus the exact refit records (nb_*_exact.json), the exact d2
record and the stationary tail of state 131. It omits 168 files (about 478 MB): the two exact d2 polynomial and
derivative records of P95 (145 MB and 165 MB), the 65 MB cell file of the original matrix certificate, other derived
records above 1 MB, the run logs, and the copies of the two original checkpoints. certificates/OMITTED.txt lists each
omitted file with its size, hash and reason. certificates/MANIFEST.txt lists the published files, and
restore_layout.py checks against it. Pass the original case 4 artifacts folder as its third argument to supply the
checkpoints (their hashes equal those of the original). For publication, internal references were removed from 23
Markdown audit and proof texts, and their hashes in MANIFEST.txt differ from MANIFEST_FULL.txt. Programs that read an
omitted file, or that compare the hash of an edited text, can therefore not be rerun from this folder alone. This
applies in particular to the late rechecks of section 3a. The accompanying README.md says which commands run as given.

- S1_PROOFS.md: proof parts P1 to P99, P101 to P106, P108 and P111, each labelled P<part>.<item>.
- S1_CLOSURE.md: the hypotheses (B0) to (B11), the conditional closure theorems, the threshold tables and the status of
  every hypothesis for each reference that was examined.
- S1_NUMERICAL_CERTIFICATES.md: every certified number, with certificate file, method, size and independent audit.
- certificates/: 697 files (programs and JSON data, about 491 MB), one subfolder per proof part: the certificates and
  checks of parts P1 to P32, the inputs of the recomputation programs of the later parts (verification records,
  exact source records, the two original checkpoints and some files of the numerical work), and the certificate
  records of the later whole-plane bounds of P95, P99, P101, P104 and P105 (S1_NUMERICAL_CERTIFICATES.md sections 6i
  and 6j) with everything their rechecks and audits read: the program modules, the exact polynomial and derivative
  records of the refit d2 (145 MB and 165 MB), the audit records of P90, P91, P93, P96 and P106, and in
  P0_proof_texts the six proof texts whose hashes the P105 audit checks. certificates/MANIFEST.txt lists every file
  with its size and SHA-256 hash.
- scripts/restore_layout.py: checks the manifest and recreates the directory layout the programs expect.
- scripts/run_late_rechecks.py: reruns the independent rechecks and exact audits of P95, P99, P101, P104 and P105 in
  the restored layout and compares every output with the shipped record (section 3a).
- scripts/run_checks.py: reruns the checks (and optionally the certificate searches) in the restored layout and compares
  every rewritten JSON file with the shipped copy.
- scripts/closure_arithmetic.py: interval arithmetic for the threshold tables of S1_CLOSURE.md section 8.
- scripts/check_*.py with their JSON outputs: independent recomputations of the numerical statements of the later
  parts (from P33 on), each written from the statements of the proof only; S1_NUMERICAL_CERTIFICATES.md section 6h
  lists which part each one checks. Their inputs are shipped in certificates/ (see above), and
  scripts/run_recomputations.py reruns all of them in the restored layout and compares each output with the shipped
  JSON record (section 3).
- scripts/build_proofs.py and scripts/collect_certificates.py: the tools that assembled S1_PROOFS.md and certificates/
  from the original part-by-part proof tree. That tree is not shipped (S1_PROOFS.md is its assembled form), so these
  two scripts are included for transparency only.

## 2. Environment

- Python 3.12 (tested with 3.12.13).
- python-flint 0.9.0 (FLINT exact rationals and polynomials, Arb ball arithmetic), mpmath 1.3.0, sympy 1.14.0,
  numpy 2.5.0. No other packages, no GPU and no network access are needed.
- All programs are single-threaded. Set OMP_NUM_THREADS=1 and OPENBLAS_NUM_THREADS=1; run_checks.py does this itself.
- Disk: about 491 MB for the certificates (the same again for a restored copy), plus about 115 MB for the residual-norm polynomial files that P12 regenerates.
- Times below are wall-clock times on one core of a shared machine at low priority.

## 3. Restore and rerun all checks

    python3 scripts/restore_layout.py certificates BASE --relocate
    python3 scripts/run_checks.py certificates BASE

    python3 scripts/restore_layout.py certificates BASE2 --relocate
    python3 scripts/run_recomputations.py certificates BASE2

BASE and BASE2 are empty directories. restore_layout.py verifies all 697 files against MANIFEST.txt before copying and stops
with a nonzero exit status on any hash mismatch. Expected output: "relocated the fixed paths in 22 programs" and "697 files restored under BASE; 0 hash mismatches".
Option --relocate rewrites, in the restored copies only, the absolute input paths of 22 programs to the shipped copies
under BASE; without it those programs need the original machine layout.

run_checks.py runs 113 programs in the order of the proof parts (exact reconstructions, interval re-evaluations,
independent audits of the partition certificates, constant computations). Each program has a time limit of 540 s; option --timeout SECONDS changes it (on a heavily loaded
machine the run times below were observed to grow by a factor of up to 3). For
each program it prints one line: folder and program, exit status, run time, and for every JSON file the program rewrote
one of "same"; "same values" followed by the reason (recorded SHA-256 hashes of input files differ, the program now
writes a key that the shipped file lacks, or the shipped file carries the verdict of the independent review); "new" (no shipped copy); or "DIFFERS" with the differing keys. A summary is
written to BASE/run_checks.log. Option --only FOLDER,FOLDER,... restricts the run to the listed certificate folders.

Expected result (observed on 2026-10-28, 08:41Z to 09:21Z, from a fresh restore of the 523-file set): every program
exits with status 0 and no output DIFFERS; the whole run took 40 minutes on one core of the shared machine (15 minutes
for the earlier 66-program set at load about 38, about 8 minutes for a still smaller set on a less loaded machine). In
the 113-program run the longest were annular_candidates.py nb_stableA2_exact (394 s), annular_candidates.py
nb_stableA3_exact (233 s), arb_hessian.py algebraic_n12_m10_k8 (229 s), r2_extra_audit.py (185 s), audit_norms.py
n12_m10 (177 s), audit_sharp_coefficients.py (162 s) and audit_extra_coefficients.py (127 s); in the 66-program run they were audit_sharp_coefficients.py (174 s), arb_hessian.py
algebraic_n12_m10_k8 (115 s), audit_norms.py n12_m10 (107 s), audit_extra_coefficients.py (100 s), audit_matrix.py
n12_m5 (84 s), auxiliary_polynomials.py (43 s) and audit_norms.py state131 (34 s). The following non-"same" lines are expected and harmless:

- P4_energy/auxiliary_certificate_audit.json: /records[1]/coefficient_file_sha256. The audit records the hash of
  state131_coefficient_bounds.json, which coefficient_bounds.py has just rewritten with a new time stamp; all values agree.
- P11_audit/check_series_cap.json: /inspected_rtm_sha256 is absent. The program optionally records the hash of a
  floating-point evaluator of the numerical work, which is not part of the artifacts; the certified values agree.
- P12_residual_norms/*_norms.json and *_audit.json: /polynomial_sha256 and /norm_record_sha256. compact_norms.py
  regenerates the intermediate polynomial file (reported as "new"), whose time stamp changes its hash; the certified
  norm enclosures agree.
- P14_algebraic_repair/*_points.json and *_points_audit.json: /input_sha256 and /points_sha256, for the same reason
  (construct.py rewrites the repair files with a new time stamp).
- P10_refits/n12_m10_points.json and n12_m12_points.json: reported as "new" (point values of two refits that are not
  used by any certificate and are not shipped).
- P14_algebraic_repair/algebraic_*.json (the repairs): /base_record_sha256, because the base records were rewritten
  earlier in the run; *_matrix_grid.json: /input_sha256, for the same reason.
- P14_algebraic_repair/*_arb_hessian.json: /source_record_sha256 and /code_sha256, and "review verdict of the shipped
  file (/verdict)": the program writes the provisional verdict PENDING_PROOF_AUDIT, while the shipped file carries the
  verdict CONFIRMED and the program hash recorded by the independent review. The norm enclosures agree.
- P14_algebraic_repair/residual_gap.json: "review verdict of the shipped file (/status)", for the same reason.
  arb_norms.py and resume_arb_norms.py (all residual norms of the m10 K8 and K16 repairs; each run reached the 570 s
  command limit and was completed by a resume of 2 to 3 minutes) are not rerun by run_checks.py; run them as
  python3 arb_norms.py NAME from BASE/13_algebraic_repair/verification and, if the command limit interrupts them,
  python3 resume_arb_norms.py NAME.

Any line reporting DIFFERS, or a nonzero exit status, is a reproduction failure.

run_recomputations.py copies scripts/ to BASE2/recomputations/ and runs the independent recomputations
scripts/check_*.py of the later parts (S1_NUMERICAL_CERTIFICATES.md section 6h) one after another, single-threaded,
with the restored tree BASE2 as their input; each program has a time limit of 1500 s (option --timeout). It compares
every output with the shipped record scripts/check_*.json, ignoring only keys that record elapsed time (and, for the
three programs whose checkpoint path it rewrites in the copies, the program hash), and prints one line per program
("same" or DIFFERS with the differing keys) followed by a count. Run it on a fresh restore, as above, or before
run_checks.py: run_checks.py rewrites some of the files that the recomputations read with new time stamps, and the
recomputation records store the SHA-256 hashes of their inputs, which then differ (the program prints a note if it
finds the log of run_checks.py in its directory). Expected result: "32 programs, 0 not reproduced"
(observed on 2026-10-28, 15:30Z to 15:48Z, on a fresh restore with --relocate: every one of the 32 programs "same",
exit status 0, 17 minutes; see section 9). The longest were check_p52.py (308 s), check_p88_p92.py (179 s),
check_p48_p49.py (114 s), check_jet_distance.py (96 s) and check_p95.py (58 s).

## 3a. Rerun the rechecks of the later global bounds

    mkdir -p DIR/research
    python3 scripts/restore_layout.py certificates DIR/research
    python3 scripts/run_late_rechecks.py certificates DIR/research

DIR is an empty directory. The programs of P95, P99, P101, P104 and P105 address their inputs as
<parent of the base directory>/research/<part>/verification/..., so the restored tree must be a directory named
research (run_late_rechecks.py stops otherwise); --relocate is not needed for them. run_late_rechecks.py runs 26
programs one after another, single-threaded: the ten rechecks of P99, the two rechecks and the exact residual algebra
audit of P101, the three rechecks and the third-derivative algebra audit of P104, the consolidation of P95 (104 hash
and completion checks), the contract audit of P105 (47 exact checks) and the seven 640-bit rechecks of the d2 covers
of P95 (three matrix groups, four norm groups). The two audits record the SHA-256 hashes of the shipped P95 rechecks,
so they run before the rechecks rewrite those files. Each program rewrites its record in DIR/research, and the driver
compares it with the shipped record, ignoring time stamps and elapsed times; for the P95 rechecks it compares the verdict, the leaf count and the rows of leaf bounds (two shipped
rechecks were produced in resumable chunks and carry bookkeeping fields that a single run does not write). It prints
one line per program ("same" or DIFFERS with the differing keys) and a count. Expected result: "26 runs, 0 not
reproduced", about 28 minutes on one core (the longest are the P95 rechecks of D2rho, about 600 s, of D2u, about
310 s, and of M2, about 250 s). Observed on 2026-10-28 from 16:45Z to 17:13Z: "26 runs, 0 not reproduced" (section 9). The d2 polynomial and derivative records themselves are shipped, and every certificate binds them by
SHA-256; their generators build.py and build_derivatives.py of P95 are not run by the driver. build.py reads the refit
file from a fixed location outside the restored tree, <parent of DIR>/<numerics folder>/research/data/nb_d2_exact.json of the production machine; the
file is shipped as certificates/numerics_data/nb_d2_exact.json, so a copy placed there should let it run, but that
regeneration (about 145 MB and 165 MB of output) was not repeated from the bundle.

## 4. Rerun the certificate searches

    python3 scripts/run_checks.py certificates BASE --searches

This also reruns the partition searches that produced the matrix and coefficient certificates, with the parameters
recorded in the shipped files:

| program (folder) | arguments | certificate produced | observed time |
|---|---|---|---|
| compact_certificate.py (P4_energy) | --state 131 --target 3.8 | (B1), 244 leaves | 5 s |
| auxiliary_certificate.py (P4_energy) | --state 131 --quantity A --factor; then --quantity DU; then --quantity N | (B2) 62 leaves; sym DU <= (17/20) I, 49 leaves; N <= 100 I, 5 leaves | 1.6 s, 1.6 s, 0.5 s |
| high_symbol_certificate.py (P6_P7_weighted) | --k 2 --radius 1/2 --sigma 1/5 --target 1/2 --adaptive | (B5), 201 leaves | 22 s |
| high_symbol_certificate.py (P6_P7_weighted) | --k 3 --radius 1/2 --sigma 6/5 --target=-5/4 --adaptive --tag _auxiliary | (B6), 282 leaves | 65 s |
| high_symbol_certificate.py (P6_P7_weighted) | --k 1 --radius 1 --sigma 0 --target 9/10 --adaptive --tag _unweighted09 | (B4), 153 leaves | 17 s |
| sharp_N_certificate.py (P6_P7_weighted) | none | (B3), 849 leaves | 42 s |
| sharp_coefficients.py (P6_P7_weighted) | none | (B7), 663 leaves | 88 s |
| extra_coefficients.py (P6_P7_weighted) | none | (B9), 315 leaves | 34 s |
| residual_derivative_lower.py (P3_tails) | --state 131 --cut 10 --radius 100 | residual Hessian lower bounds | 58 s |
| certify_matrix.py (P10_refits) | n12_m5 | M >= (19/5) I for the refit m5, 1346 leaves | 330 s (stops at 480 s; see below) |
| construct_splice.py (P10_tail_splice) | none | exact stationary tail potentials | 9 s |

The searches are deterministic, and the regenerated certificates agree with the shipped ones up to time stamps. One
expected note: state131_aux_DU_certificate.json and state131_aux_N_certificate.json are reported as "same values; keys
absent from the shipped file (/factored)", because the shipped files were written before the program recorded this flag
(they use the unfactored bound, factored = false, as the rerun does). sharp_N_certificate.py also rewrites its audit
state131_N1_audit.json, whose recorded /certificate_sha256 changes with the time stamp of the regenerated certificate
("same values"). The negative target of the k = 3 search must be written --target=-5/4 (with a space the argument
parser reads -5/4 as an option).

certify_matrix.py stops after 480 s of wall-clock time (a fixed limit in the program) and then writes status
INCOMPLETE with the leaves accepted so far and the pending cells; run_checks.py then reports DIFFERS at /accepted,
/pending and /status. This happened on the shared machine at load about 38 (1005 of the 1346 leaves in 480 s). The
search is deterministic: the 1005 accepted leaves were identical to the first 1005 leaves of the shipped certificate,
with no failed cell, so the run is consistent with the shipped certificate but does not reproduce all of it. On an idle
core the search takes about 330 s. The shipped certificate itself is independently checked by audit_matrix.py n12_m5,
which is one of the checks of section 3.

## 5. Exact reconstruction from the case 4 checkpoints

The exact reference is reconstructed from the accepted checkpoints of the case 4 run. To rerun this step, pass the
artifacts folder published with the case 4 report as the third argument; its subfolder checkpoints/ must contain
state088_handoff/accepted_00000088.json and .npz and state131_last_unverified/accepted_00000131.json and .npz.

    python3 scripts/restore_layout.py certificates BASE CASE4_ARTIFACTS_FOLDER
    python3 scripts/run_checks.py certificates BASE --recover --only P1_source

recover_state.py converts the stored hexadecimal floating-point coefficients and the frozen normalizers into exact
rationals, eliminates the center condition exactly, maps the shifted-Legendre basis to the canonical generators, and
asserts that the SHA-256 hash of the canonical serialization equals the hash archived in the checkpoint
(4d80cf85ea1746d41c3fcfbdc622c74465cff5b9358e68614e521531ea78fb01 for state 131). It rewrites state088_exact.json and
state131_exact.json, which should be "same".

## 6. Closure arithmetic

    python3 scripts/closure_arithmetic.py

prints the threshold table of S1_CLOSURE.md section 8 (mpmath interval arithmetic): for each scenario the fractional
order s, the rate mu, the residual threshold eta0 and the product c_s r, followed by the two stated choices of Theorem D
(s = 2^-28, eta = 3.7e-10; s = 2^-18, eta = 1/1572864 (about 6.3578e-7)).

## 7. Applying the certificates to a new reference

The decisive open step is a reference whose residual lies in N_s and is small (section 8). Programs that take a
reference name read an exact potential record. For the names state088 and state131 the record is
source_audit/<name>_exact.json; for any other name it is 08_refits/verification/<name>_audit.json, a JSON file with the
keys cl (exact rational string), canonical_order (list of generator indices [j, m, k]), canonical_coefficients (exact
rational strings, same order), canonical_sha256 and, for certify_matrix.py, source_sha256. The algebraic repair records
of P14 have this format. With such a record:

- compact_norms.py NAME and audit_norms.py NAME (P12) give certified whole-plane norms ||grad F||_2, ||omega D^2 F||_2,
  ||omega D^3 F||_2, and decide exactly whether ||F||_2 and ||r F||_2 are finite. Cost grows with the number and
  degree of the generators; for the m10 refit it is about 20 s plus 70 s.
- certify_matrix.py NAME (P10) searches a partition certificate of (B1), M >= (19/5) I; audit_matrix.py NAME audits it.
- audit_exact_refit.py NAME (P10) lists every residual sector with exponent above -5/2 with exact coefficients.
- point_probe.py NAME and audit_points.py NAME (P14) give certified point values of the residual and of the smallest
    eigenvalue of M, and with ||f||_infinity <= N_s(f) a rigorous lower bound for N_s(F).
- arb_hessian.py NAME [BITS] (P14.2) gives a certified ||omega D^2 F||_2 by 1024-bit ball polynomials, with two
  independent radial integrations; for large repairs it is much faster than the exact rational P12 pipeline (76 s for
  m10 K8). matrix_grid.py NAME ... (P14) evaluates M and F on the 73 by 65 polar grid of P14.1 section 6 and selects the
  point of least eigenvalue; audit_grid_minima.py re-evaluates the selected points independently. The grid itself is a
  selection device, not a certificate.

The search and audit programs for (B1) to (B9) in P4_energy and P6_P7_weighted read the source record
source_audit/state131_exact.json, either through the option --state or under a fixed name. To certify these hypotheses
for a new reference, write its record in the same format (keys exact_parameters.cl, canonical_order,
canonical_coefficients, canonical_serialization_sha256), point the input path of each program to it, and rerun each
search and then its audit; the targets are those of S1_CLOSURE.md section 3. Every hypothesis must be certified again for the
new reference: agreement of the center jets or of the far-field moments does not transfer a certificate.

## 8. Continuation: state of the problem and next steps

What is proved. Four conditional existence theorems reduce existence near an exact reference with c = c_l to
certifiable inequalities and one residual bound (S1_CLOSURE.md; FINAL_REPORT section 5).

- Theorem D (unweighted space N_s): variant (b) needs N_s(F) <= 1/1572864 (about 6.3578e-7) at s = 2^-18. All of (B0)
  to (B9) and (B11) are certified for state 131, but (B10m), F in N_s, fails for the checkpoint and for every refit of
  the original 860-generator family (Theorem E). The algebraic tail repairs of P14 put F in N_s exactly but have
  N_s(F) > 11.48.
- Theorem D_w (weighted space with weight radius R; first version P17 to P24, second version P43 and P63): it needs
  ||w F||_(Hdot^-1) < 2^-61 and |F| < 2^-44 near the origin (first version) or 2^-56 and 2^-39 (second version).
  Every hypothesis of the first version, including membership of the residual, holds for the checkpoint, whose
  residual misses the threshold by more than 2^119 at every R >= 2^31.
- The logarithmic theorem (P83 to P88): native norm M with tau = 2^-24, 1/2 < beta <= 1; it needs
  M(F) <= 2^-25 tau^beta (2 beta - 1)^(1/2), which is at most 1.083e-12 < 2^-37. The native residual floors (P86)
  exceed this by more than 2^121 (checkpoint) and 2^67 (Mpen2, d2).
- The parametric form (P89 to P91) frees the third velocity and the third and fourth density derivative bounds. For
  every parameter choice the gaps exceed 2^119 (checkpoint) and 2^65 (Mpen2, d2); with the exact global caps of P91
  they exceed 2^213 and 2^243.
- The matrix hypothesis of the checkpoint holds with the sharp global margin M >= (c + 2) I, equality only at the
  origin (P94; with the certificates of P4, P92 and P93, four independent certificates). The auxiliary bounds (B4) to
  (B6) of the checkpoint are recomputed independently from the exact potential with better margins (P96:
  M_1 >= 0.972875 I, M_2 >= 0.587238 I, M_3 >= -1.230876 I, ||sym DU|| <= 0.810792), and its center remainders are
  bounded explicitly on r <= 1/10 (P98). For the exact refit d2 the matrix bounds M >= (19/5) I of (W1) and M_1,
  M_2 >= I/2 of (W2) hold on the whole plane, and so do the decay bounds of the logarithmic theorem at R = 2^31
  (186, 22, 22, 56) and its five fixed derivative bounds (P95). With the exact caps of P91 (Astar = 2^189,
  tau = 2^-210) d2 satisfies every reference hypothesis of the parametric logarithmic theorem and its residual lies
  in the forcing space; only residual smallness fails, by more than 2^243 (P105). The fixed fourth-derivative bound
  512 of (W3) fails for d2 at certified off-axis points (P54, P58), so only the parametric form applies to it. For
  the checkpoint, programs independent of the earlier ones recompute the density sign, A >= -(1/20) I and the matrix
  inputs at large radius (P99) and the three decay constants (P104), and give a directed far-field residual bound
  abs(F(X)) <= 0.243535 abs(X)^(2 gamma - 1) for abs(X) >= 300 (P101).

Necessary local tests exclude exact solutions within distances much larger than the radii of these theorems (P40,
P45 to P52, P73, P86, P90). The checkpoint and the early refits m4, m5, m10, m12, m14 admit no correction at all in
the unweighted affine class (Theorem E). In short, regularity and the matrix condition are not the bottleneck: the
residual is.

Next steps, in order of expected value.

1. A reference with a much smaller residual. In the six-branch generator family the sector r^(-2.133) is fixed by the
   six leading branches; it keeps the unweighted norm above 22986 times its threshold for every choice of
   coefficients and every radial degree up to 3675 (P32 to P35). A seventh stationary branch cancels it; the next fixed
   sector is r^(p_8), p_8 = -2.581, which only an eighth branch cancels (P32, P60). Cancel the descendant sector (2, 1)
   exactly rather than by a penalty: in the first seven-branch fit b6 it is the leading sector. The target is
   M(F) < 2^-37 for the logarithmic theorem (in particular ||w F||_(Hdot^-1) < 2^-63.5), or the thresholds of
   Theorem D_w above.
2. Reject candidates cheaply, in this order: the annular lower bounds of P51 and P52 and the native floors of P86 (a
   floor above the threshold ends the candidate); the derivative contract at off-axis points (P54, P58) or the global
   caps of P91; then the whole-plane derivative and decay covers and the contract assembly (P95, P105), the matrix certificate (the Bernstein method of P92 or the Taylor-box covering of P93) and
   (B2) to (B9). The certificate programs apply to any finite rational potential of the canonical form (section 7).
3. Decide the six- and seven-branch families. For each fixed radial degree the weighted residual norm over the family
   has a positive lower bound (P56, P57, P60) that is not evaluated; the evaluated weaker bound of P62 is below 1e-50
   and decides nothing. Evaluating the sharper bound, or exhibiting a family member below the threshold, is the open
   quantitative question.
4. A different correction class, with explicit tail coordinates for the sectors Theta_1, ..., Theta_5. This needs a
   new inverse theorem in a strictly subcritical correction space: in the critical weighted Sobolev spaces no closed
   realization with finitely many added parameters and equations is upper semi-Fredholm (P61, P64, P65).

## 9. Reproduction log


- 2026-10-28T04:32Z: fresh restore of the 187-file set, full check run, 52 programs, all exit status 0, about 8 min;
  only the expected differences of section 3.
- 2026-10-28T04:41Z: fresh restore of the 218-file set (with P14 and the frozen endpoint constants), run with --only
  P5_frozen,P14_algebraic_repair, 10 programs, all exit status 0; only the expected differences of section 3.
- 2026-10-28T04:47Z: searches of P4_energy and P10_tail_splice, with the checks of P4_energy, P10_tail_splice and
  P14_algebraic_repair (including construct.py 256 4096 and the point values of the K = 256 and 4096 repairs), 21
  programs, all exit status 0; every certificate "same" apart from the /factored note of section 4 and the expected
  hash notes of section 3.
- 2026-10-28T04:58Z: checks and searches of P6_P7_weighted, 23 programs, on a machine at load about 35 to 110 (the two
  coefficient audits took 223 s and 210 s); every output "same" (sharp_N_certificate.py: the hash note of section 4),
  except the k = 3 search, which exited with status 2 because of the argument syntax. Rerun at 05:05Z with
  --target=-5/4: 282 leaves, certificate "same".
- 2026-10-28T05:19Z: checks of P3_tails and P10_refits with the searches residual_derivative_lower.py and
  certify_matrix.py n12_m5, 9 programs, all exit status 0, every output "same" (two unshipped point files "new"),
  except certify_matrix.py, which stopped at its 480 s limit with 1005 accepted leaves identical to the first 1005
  leaves of the shipped certificate and no failed cell (section 4).
- 2026-10-28T05:23Z: fresh restore of the 256-file set (with P15, the grid scan, the Hessian certificates and the m14
  audit), run with --only P10_refits,P14_algebraic_repair,P15_homogeneous_weight, 14 programs, all exit status 0, all
  outputs "same" or with the expected notes of section 3. The two arb_hessian.py outputs were reported as DIFFERS at
  /verdict by the earlier comparison, which did not yet know the review verdict; their enclosures agree, and
  run_checks.py now classifies this as a review note.
- 2026-10-28T05:28Z to 05:43Z: fresh restore of the 256-file set and the complete check run (then 64 programs; the
  K = 256, 4096 point audit was added afterwards as the 65th), all exit status 0, no DIFFERS; the only non-"same"
  lines were the expected notes of section 3 and the "new" polynomial and point files.
- 2026-10-28T05:52Z to 05:56Z: fresh restore of the 264-file set (with the all-component norm records of P14.2 section
  5), run with --only P14_algebraic_repair, 12 programs including residual_gap.py, all exit status 0, no DIFFERS; only
  the expected notes of section 3.
- 2026-10-28T08:41Z to 09:21Z: fresh restore of the 523-file set with --relocate and the complete check run, 113
  programs, all exit status 0, no DIFFERS; only the expected notes of section 3 (40 minutes).
- 2026-10-28T14:23Z to 14:41Z: fresh restore of the 558-file set (with the inputs of the recomputation programs)
  without --relocate, and run_recomputations.py: "30 programs, 0 not reproduced", exit status 0 (18 minutes).
- 2026-10-28T14:47Z to 15:23Z: fresh restore of the 564-file set with --relocate ("relocated the fixed paths in 22
  programs", 0 hash mismatches) and the complete check run: 113 programs, all exit status 0, no DIFFERS; every other
  line "same", "new" or "same values" with recorded hashes of rewritten inputs or of relocated programs, or a review
  verdict, as reason (20 minutes). run_recomputations.py was then run in the same directory: 25 of 31
  programs "same"; the other six (check_p31_constants, check_p33_p35_constants, check_p39_p40, check_p48_p49,
  check_p51, check_p62) differ only in the recorded SHA-256 hashes of input files that run_checks.py had rewritten with
  new time stamps, and every computed value agrees. Hence section 3 runs the recomputations on a second fresh restore.
- 2026-10-28T15:30Z to 15:48Z: second fresh restore, of the 573-file set (with the inputs of check_p95.py) with
  --relocate ("relocated the fixed paths in 22 programs", 0 hash mismatches), and run_recomputations.py alone:
  "32 programs, 0 not reproduced", exit status 0, every program "same" (17 minutes).
- 2026-10-28T16:13Z: restore of the 674-file set (with the records of P95, P99, P101, P104 and P105 of
  S1_NUMERICAL_CERTIFICATES.md sections 6i and 6j) without --relocate: "674 files restored", 0 hash mismatches, under
  one second. No recomputation program reads the added records and no shipped program changed, so the runs above
  stand. The added programs contain no absolute path, but they address their inputs relative to a directory named
  research and import modules and read records that this set did not contain; an independent dependency audit found
  this, and the missing files were added (next entries).
- 2026-10-28T16:30Z: fresh restore of the 685-file set (with the P95 modules and the audit records read by the late
  programs) into a directory named research, then the ten rechecks of P99, the two rechecks and the algebra audit of
  P101 and the three rechecks and the algebra audit of P104: 17 runs, every one "same", exit status 0 (about 2 minutes).
- 2026-10-28T16:33Z: fresh restore of the 693-file set (with the two exact d2 records and the six proof texts) into a
  directory named research: the same 17 runs "same", then the P95 rechecks of M, M1, M2 and u "same" (90, 161, 249 and
  45 s). The run was stopped there to start the complete run of section 3a, in which the P105 audit precedes the P95
  rechecks (it records the hashes of the shipped rechecks, which the rechecks rewrite).
- 2026-10-28T16:45Z to 17:13Z: fresh restore of the 697-file set (with the consolidation records of P95) into a
  directory named research ("697 files restored", 0 hash mismatches), then run_late_rechecks.py as in section 3a:
  "26 runs, 0 not reproduced", exit status 0, every program "same" (28 minutes; the longest were the P95 rechecks of
  D2rho, 602 s, D2u, 309 s, and M2, 253 s; the consolidation of P95 and the audit of P105 took 0.8 s and 3.8 s).

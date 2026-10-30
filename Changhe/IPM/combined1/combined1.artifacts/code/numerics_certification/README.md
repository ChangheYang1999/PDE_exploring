# Artifacts of lane the N3 numerics worker (N3: full-plane residual norms and certification)

All paths are relative to this folder. Python: python3 with python-flint (arb) and mpmath.
Run every command from a working copy of the lane root layout: code/ here corresponds to certification/ in the lane; the exact
coefficient files are the read-only sources listed in results/*/source_path (copied in the lane under source_copy/).

## What is here
- code/e2norms.py: exact whole-plane Beta-integral norms of the residual F and of D^d F (d <= 3): G0 = ||F||_2, rF = ||r F||_2,
  G1 = ||grad F||_2, P2 = ||omega D^2 F||_2, Q3 = ||omega D^3 F||_2, Pw1, D2, rD2, and the E_2 / N_s assembly (analysis2 conventions).
- code/hminus1.py: two-sided enclosure of ||F||_{Hdot^-1} (exact Galerkin potential in the generator family per angular mode,
  duality lower bound, identity plus parity-Hardy upper bound, exact tail bounds).
- code/wlap_norms.py and code/candidate_pipeline.py: theory_v02 norms NORM-T-WLAP-v1 (N_a), NORM-T-WL2-v1, NORM-T-WEAK-v1 (I_k, A_k,
  B_k, C_k, H_k, m_k, weak distance LB) and the E_2 components from one exact residual assembly (the pipeline reuses a stored F record).
- code/build_F_record.py: assembles the exact compactified F once (<ID>_Fpoly_cache.json, about 1.3 GB for 1922 generators; not kept).
- code/weak_from_cache.py: NORM-T-WEAK-v1 probes for any k (exact rationals for small k, 512-bit Beta-moment balls for large k, shift
  handled by the Gamma function) and the exact signed weak pairing per dyadic annulus.
- code/general_probe.py: weak distance probes with general radial polynomials and odd angular modes (reproduction of the T4 theory auditor T4-182 and
  T4-185 on 007; probe vectors in source_copy/t4_probes).
- code/wlap_modes.py: per-angular-mode split of N_a (mode profile; modes 1 + 3 projected LB for the NC-T-ORIGIN-INV cell test).
- code/hminus1_hardy_fix.py, code/hminus1_mode_hardy.py: sharpening of the Hdot^-1 upper bounds by the direct and the mode-n Hardy
  inequality ||F_n||_H <= ||r F_n||_2 / n (lemma and proof in the docstring; refereed by the second model, the second model/mode-hardy/answer.md).
- code/jobqueue.sh with code/jobs_core55.txt, code/jobs_core56.txt: the file-based job queue used from 02:42Z on.
- code/assemble_norms.py: conversion of the component enclosures into the registered norm IDs (NORM-A2-Ns18, NORM-T-X3-v1, ...).
- code/audit_e2norms.py: second arithmetic path (u = 1 - t integrals at 640 bits, Cartesian jet checks).
- code/bernstein_cover.py: Bernstein covers of the background inequalities (theta <= tau, M1 >= mu I, A >= -I/20).
- code/point_fields.py, code/theta_scan.py, code/dyadic.py, code/dyadic_lap_test.py: point fields (rigorous jets), FLOAT theta scans,
  dyadic region integrals.
- code/jobqueue.sh, code/jobs_core5*.txt, code/queue_*.sh, code/run_candidate.sh: the job scripts actually used (real order of runs).
- code/legqs_norms.py (with code/legqs_e2norms.py, code/legqs_integrals.py): exact whole-plane norms and weak pairings for candidates with
  multi-scale legqs functions (R0^2 + r^2)^(-N) (C1-N1-016 and later): tuple-key fields, canonical form, exact rational reduction of every
  radial integral to R1 + R2 I0 (one transcendental I0 = int_0^1 v^b0/(1+a v) dv per scale and exponent class, 1024-bit ball).
  code/legqs_probe.py: the T4-064 / T4-185 weak probes for such candidates. code/legqs_tests.py: the validation (A: tables vs 2F1 balls;
  C: R0 = 1 identity with e2norms; D: point values vs direct mpmath differentiation; E: scaled norms); code/legqs_quadcheck.py:
  independent 2D quadrature of G0 and rF for the synthetic scaled candidate (results/legqs_quadcheck_synthetic.json).
  code/legqs_norms_run016_frozen.py is the exact version used by the C1-N1-016 run (sha256 in its record); code/legqs_terms.py is the
  unpacked term algebra used only for checks. Design notes: notes/LEGQS_EXTENSION_PLAN.md; referee: the second model/legqs_method/answer.md.
- code/legqs_hardy.py: mode-wise Hardy UPPER bound of ||F||_H for legqs candidates (H^2 <= sum_n ||r F_n||_2^2 / n^2 over the sine modes of the
  exact F record); code/hardy_cover_check.py: the H18 check that the modes used are exactly the modes of F and that the mode squares enclose rF^2
  from both sides; code/legqs_hdual.py: rigorous duality LOWER bound of ||F||_H per mode (Galerkin potentials r^3 (1-t)^beta t^k sin(n theta),
  exact Gram, ball pairings; self-test against the recorded probe pairings), with the E_2 lower bound that uses it.
- code/legqs_cells.py: the seven-cell test (NC-T-ORIGIN-INV, modes 1 + 3 projected N_h) for legqs candidates; code/legqs_cells_test.py: its
  d2 validation against T4-107 / N4-099. code/legqs_secondpath.py: second arithmetic path (every radial integral by the t-monomial Beta x 2F1
  ball route) for the four legqs norms, with the overlap check against the production records. code/legqs_report.py: publication tables
  with directional rounding. code/final_tables.py: regenerates every table of notes/N3_CERTIFICATION_SUMMARY.md from the records; code/h18_note.py: prints the H18 falsification results (mode cover, duality lower bounds, residual enclosures, second paths) from the records
  (notes/make_summary.sh assembles the summary from notes/summary_head.md, the generated tables and notes/summary_tail.md).
- t4_probes/: the probe vector files (frozen T4 vectors n = 7 and n = 1, held-out monomials (n, K), first-mode K = 2048).
- notes/: N3_CERTIFICATION_SUMMARY.md (the complete tables) and the legqs design plan. the second model/: referee answers.
- results/: the JSON records cited in team notes (every number reported by this lane), logs/: the run logs.

## Reproduction commands (lane layout: certification/ = code/)
    PY=python3
    $PY -B certification/e2norms.py <exact.json> <ID> certification/results            # components; <ID>_e2norms.json, <ID>_e2norms.log
    $PY -B certification/hminus1.py <ID> <exact.json> certification/results 24 20 61   # Hdot^-1 enclosure; <ID>_hminus1.json
    $PY -B certification/candidate_pipeline.py <exact.json> <ID> certification/results  # weak probe, WL2, N_a cover, components
    $PY -B certification/assemble_norms.py <ID>                                         # registered norm IDs; <ID>_registered_norms.json
    $PY -B certification/audit_e2norms.py <ID> certification/results <exact.json>       # second arithmetic path
    $PY -B certification/bernstein_cover.py <exact.json> <ID> A 2/25 certification/results --seconds 3600
    $PY -B certification/build_F_record.py <exact.json> certification/results                 # exact F record (cache) for the tools below
    $PY -B certification/general_probe.py <ID> <F record> <exact.json> certification/results source_copy/t4_probes/n7_a0.json source_copy/t4_probes/a0.json
    $PY -B certification/weak_from_cache.py <ID> <F record> <exact.json> certification/results --k 0,1,2,3,4,5,6,7,8,128,512,1024,2048 --annuli_k 0,8
    $PY -B certification/wlap_modes.py <ID> <F record> certification/results 0,1 [1,3]        # per-mode N_a (optional mode restriction)
    $PY -B certification/hminus1_hardy_fix.py <ID> <F record> certification/results; $PY -B certification/hminus1_mode_hardy.py <ID> certification/results
    $PY -B certification/legqs_tests.py ACDE                                              # legqs validation (about 3 min)
    $PY -B certification/legqs_norms.py <exact.json> <ID> certification/results --norms G0,rF,G1,P2 --order 2   # <ID>_legqs_norms.json, <ID>_legqs_Fpoly.json
    $PY -B certification/legqs_probe.py <ID> certification/results/<ID>_legqs_Fpoly.json <exact.json> certification/results source_copy/t4_probes/<probe>.json ...
    $PY -B certification/legqs_hardy.py <ID> certification/results/<ID>_legqs_Fpoly.json certification/results            # <ID>_legqs_hardy.json
    $PY -B certification/legqs_cells.py <ID> certification/results/<ID>_legqs_Fpoly.json certification/results            # <ID>_legqs_cells.json
    $PY -B certification/legqs_secondpath.py <ID> certification/results/<ID>_legqs_Fpoly.json certification/results G1,P2,G0,rF   # <ID>_legqs_secondpath.json
    $PY -B certification/hardy_cover_check.py <ID> certification/results/<ID>_legqs_Fpoly.json certification/results      # <ID>_hardy_cover.json
    $PY -B certification/legqs_hdual.py <ID> certification/results/<ID>_legqs_Fpoly.json certification/results --modes 1,3,...,31 --kmax 14 --classes 8 --selftest source_copy/t4_probes/a0.json
    $PY -B certification/legqs_hres.py <ID> certification/results/<ID>_legqs_Fpoly.json certification/results --modes 1,3,...,31 --kmax 14 --classes 8 --tag _hres_full
    $PY -B certification/final_tables.py > notes/N3_FINAL_TABLES.md; $PY -B certification/h18_note.py; bash notes/make_summary.sh   # the summary tables
Expected checks: see the "validation" entries in team notes (state 131 reproduces the analysis2 P12 enclosures of P2 and Q3;
d2 components agree with the N4 numerical auditor N4-024/026/043/050; d2 Hdot^-1 agrees with N4-020; N_a(d2) agrees with T4-107/N4-099).

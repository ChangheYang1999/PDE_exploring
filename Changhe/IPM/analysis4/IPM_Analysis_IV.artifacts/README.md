# Accompanying artifacts for IPM Analysis IV

This folder accompanies the report `IPM_Analysis_IV.report.md`. It contains the code, certificate outputs and data behind
the three documents placed at its top level: the theory report `FARFIELD_CONVERGENCE_THEORY.md`, the numerical report
`FARFIELD_NUMERICAL_EXPERIMENTS.md` and the summary `FINAL_SUMMARY.md`. Beside them are the theory scripts with their exact
certificate outputs, the numerical recursion code with its per-order run data and exported coefficients, the independent
verification (an independent low-order implementation, 307 standalone proofs and the claim and radius maps), and the exact
data of the best candidates. The published folder omits operational logs, scratch data, team messages, the chronological
verification ledger, the verification receipts kept beside each proof, and the multi-GB binary recursion checkpoints.

## Directory map

- `theory_code/`: scripts of the theory part (Brjuno constants, Theorem E constants, prime congruences, logarithmic series, tuned series and their exact certificates); index in `theory_code/README.md`.
- `theory_code/tuned/`: tuned pure series at rational delta: exact compatibility polynomials, response bounds, majorant radii, certificate outputs (`tq_cert_*.log`, `*.out`) and the queue scripts that record the command lines; index in `theory_code/tuned/README.md`.
- `theory_code/review/`, `theory_code/modscan/`, `theory_code/oddnum/`: independent reproductions inside the theory part, modular scans of the first compatibility coefficient, odd-numerator checks.
- `theory_code/final_repro/`: fresh reruns of the main theory scripts made at the end of the run, with their outputs and diffs (`final_repro/README.md`).
- `numerics/`: far-field recursion code (`code/`), run scripts (`jobs/`), per-order run data (`logs/`), result tables (`notes/`) and compact coefficient exports (`ckpt/`); see `numerics/README.md`.
- `verification/`: the independent verification: `code/` (including the independent Cartesian low-order implementation `code/cartesian_verify.py`), `proofs/NN_topic/PROOF.md` (307 standalone proofs, reading order in `proofs/INDEX.md`), `REPRODUCTION.md`, `VERIFY_SUMMARY.md`, `FINAL_CLAIM_MAP.md`, `CERTIFIED_RADII.md`, `current_certified_radii.json`.
- `candidate_data/`: exact parameters and leading Fourier data of Candidate 007, exported far-field coefficients, and the exact compatibility polynomials and roots of the tuned profiles; see `candidate_data/README.md`.

## Requirements

Python 3 (the runs used 3.12) with numpy, sympy and mpmath for the theory scripts (scipy for three exploratory
logarithmic-series scripts); python-flint 0.9 for the numerical recursion and most verification scripts; gmpy2 for part of
the verification code. The computations run on CPUs, some with multiple worker processes; no GPU, server or build step is needed.

## Restart instructions

All commands start in this artifacts folder. Scripts that write outputs overwrite the stored file of the same name; to
compare, run them in a copy of the folder and use `diff`.

(a) Theory constants and certificates (commands as rerun at the end of the run, see `theory_code/final_repro/README.md`):

```sh
cd theory_code
python3 constants.py ../numerics/notes/cand007_f1.json        # -> constants_out.json (Theorem A constants)
python3 check_chi.py                                          # low-order consistency of the recurrence
python3 prime_kappa_check.py 23                               # prime-denominator congruence of Theorem P
python3 rational_finite_order.py tuned/candidate007_leading_exact.json   # -> logs/rational_finite_order.json (Theorem E)
cd tuned
python3 o6_sym.py 3                 # first obstruction O_6 at delta = 2/3
python3 sigma_check.py              # -> sigma_check.json
python3 sigma_inf_check.py          # after sigma_check.py
python3 component_box_check.py
python3 tq_cert.py 4                # -> tq_cert_Q4.out (Corollary T_4(a), about 17 s); tq_cert.py 6 gives Corollary T_6(a)
python3 tq5_bounds_radius.py        # Corollary T_5(b)
python3 tq_bounds_radius.py 4       # Corollary T_4(b)
python3 tq_minima.py 5 5 8 5 6 5 5  # Corollary T_5(c)
python3 tq_certh.py 9 2             # Corollary T_{9,2} (delta = 4/9)
```

The reference outputs are the stored files of the same names; the reruns in `final_repro/` agree with them apart from
timing lines. Further invocations, run times and the higher-period certificates (`tq_cert.py 7` to `10`, `tq_radiush.py`,
`tq_block.py`, `hh_float.py`) are listed in `theory_code/tuned/README.md`; the `run_after_queue*.sh` scripts record the exact
command lines used.

(b) Numerical experiments (run from inside `numerics/`; requirements python-flint 0.9, numpy, mpmath, sympy):

```sh
cd numerics
# Candidate 007 profile at 2048 bits (finished at order 500)
python3 code/run_recursion.py --tag c007_p2048 --ring arb --prec 2048 --cl cand007 --f1 cand007 --N 500 --ckpt-every 10 --resume
# generic run; resumes from ckpt/<tag>.pkl if present, otherwise starts at order 1
python3 code/run_recursion.py --tag <tag> --ring arb --prec 1024 --cl cand007 --f1 cand007 --N 500 --ckpt-every 10 --resume
# canonical 2/3 logarithmic series (recorded command; starts at order 1 without a checkpoint; certified through order 329)
python3 code/logff.py --tag log_sin1_c3_p512 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 350 --ckpt-every 5 --resume --workers 4 --stop-rel-rad 1e9
# continuation from the order-329 state (needs ckpt/log_sin1_c3_from329.pkl; the first resume used --reset-radii)
python3 code/logff.py --tag log_sin1_c3_from329 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 440 --ckpt-every 5 --resume --workers 4 --stop-rel-rad 1e9
# sensitivity diagnostic on a copy of the 329 state
python3 code/logff.py --tag log_sin1_c3_pert329 --ring arb --prec 512 --A 2 --B 3 --f1 sin1 --N 350 --ckpt-every 5 --resume --workers 2 --stop-rel-rad 1e9 --perturb-radii 20261031
# tuned series (delta = 1/3; use --a 4 --b 9 with notes/tuned49_poly.json for delta = 4/9)
python3 code/tuned_general.py --tag T --a 1 --b 3 --poly-coeffs @notes/tuned13_poly.json --root-guess 0.51215647362 --prec 1024 --N 300
python3 code/tuned_cQ.py --tag T --Q 5 --root-guess 0.5599810534719769 --prec 1024 --N 300
# single-harmonic tuned series (sin 7 theta at delta = 4/5; also --a 4 --b 7 --f1-single 9 and --a 4 --b 9 --f1-single 11)
python3 code/tuned_general.py --tag T --a 4 --b 5 --f1-single 7 --prec 1024 --N 300
# Q = 9 root check
python3 code/tuned_general.py --tag T --a 2 --b 9 --poly-coeffs @notes/tunedQ9_poly.json --root-guess 0.421494658566 --prec 512 --N 99
# section-13 evaluation of a checkpoint
python3 code/evaluate_series.py ckpt/T.pkl --N 10,20,40,80 --R 1,2,4,8 --out notes/eval_T.json
```

The large binary recursion checkpoints (`ckpt/*.pkl`, 0.05 to 2.2 GB each) are not included. `numerics/ckpt/` holds only
compact JSON exports of the coefficients (orders up to 100, or 60 for the logarithmic series), which are for inspection and
cannot be resumed from; every resume command above therefore regenerates its state from order 1 unless a checkpoint is
present. The orders above 329 of the canonical 2/3 run are a continuation from the stored order-329 midpoints with reset
radii (see `numerics/README.md` and section 5.11b of the numerical report). The scripts in `numerics/jobs/` record the exact
command lines of all runs.

(c) Independent verification (from `verification/REPRODUCTION.md`, run from inside `verification/`):

```sh
cd verification
PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 python3 code/cartesian_verify.py --c 5/3 --initial 1:1,3:1 --order 4 --out replay/two_mode_replay.json
# compare the "recursion" and "self_checks" objects with two_mode_c5_3_N4.json (timestamps differ)
PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 python3 code/cartesian_verify.py --candidate ../../../combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json --order 2 --out replay/candidate_replay.json
```

The second command reads the Candidate 007 coefficient file of the read-only source project `Changhe/IPM/combined1`,
which in Changhe Yang's repository sits at `../../../combined1` relative to `verification/`; adjust the prefix if your
checkout differs. The same leading data are stored in `candidate_data/candidate007_leading_exact.json`. These replays check the recurrence and the input
extraction at low order; they do not reprove the infinite convergence claims, whose proofs are the standalone files in
`verification/proofs/` (mapped to the report by `verification/FINAL_CLAIM_MAP.md`, radii in `verification/CERTIFIED_RADII.md`).
Many other verification scripts read inputs from the original project layout and from receipt folders that are not
published; they are retained as the record of the checks.

## Notes on omitted material

- Per-run logs and diagnostics of the theory part's logarithmic-series scripts (about 13 MB) and the cache files
  `theory_code/tuned/tq_sigma_Q*.cache.json` (regenerated on the first rerun) are not included.
- `verification/current_certified_radii.json` cites certificate files of the full verification record by path and SHA-256;
  those files are not included in this folder.
- The large coefficient exports and logarithmic-series tables are retained result data, not scratch output.
  `candidate_data/c007_p2048_coeffs_n100.json` and its copy in `numerics/ckpt/` contain scaled Fourier coefficients.
  `numerics/notes/log_sin1_c2_p512_table.json` and `numerics/notes/log_sin1_c3_p512.regen_table.json` contain
  density and stream norms by logarithmic column, root diagnostics and factorially weighted ratios used to inspect
  finite-order growth. These tables cover prefixes of the completed runs; the final per-order records are in
  `numerics/logs/`. Their role and interpretation are described in `numerics/README.md` and the numerical report.
- Two floating transcripts, `theory_code/tuned/hhf_Q7h1_root1_N301_f64.out` and `hhf_Q8h1_root1_N304_f64.out`, are published
  in projected form: runtime warning lines show `[local runtime path]` instead of a local path; all numerical lines are unchanged.
